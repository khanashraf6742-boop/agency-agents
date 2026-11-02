#!/usr/bin/env python3
"""Serve the deliverable with a real one-click download path.

Static hosting sends .html as text/html, so clicking the file *renders* it and
the GitHub raw endpoint sends text/plain, so clicking that *shows the source*.
Neither is a download. This server adds /download, which sends the same bytes
with Content-Disposition: attachment, so the browser saves the file instead.

    python3 serve.py            # http://0.0.0.0:8000/
      /                       the book, rendered
      /download               the book, saved as a file
      /<name>.pdf|.zip        print edition and archive
"""
from __future__ import annotations

import os
import shutil
import sys

PORT = 8000
BOOK = "CCS_CCA_Rules_1965_Case_Studies_2026-11-02.html"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))  # the repository root holds the deliverables
STAGE = "/tmp/preview"


def stage() -> None:
    """Copy the deliverables out of the repo so the server has one clean root."""
    os.makedirs(STAGE, exist_ok=True)
    for name in os.listdir(ROOT):
        if name.startswith("CCS_CCA_Rules") and name.endswith((".html", ".pdf", ".zip")):
            shutil.copy2(os.path.join(ROOT, name), os.path.join(STAGE, name))
    shutil.copy2(os.path.join(ROOT, BOOK), os.path.join(STAGE, "index.html"))


def main() -> int:
    stage()
    import http.server
    import socketserver

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=STAGE, **kw)

        def do_GET(self):  # noqa: N802
            if self.path.split("?")[0] in ("/download", "/download/"):
                self.send_response(200)
                self.send_header("Content-Type", "application/octet-stream")
                self.send_header("Content-Disposition", f'attachment; filename="{BOOK}"')
                size = os.path.getsize(os.path.join(STAGE, BOOK))
                self.send_header("Content-Length", str(size))
                self.end_headers()
                with open(os.path.join(STAGE, BOOK), "rb") as fh:
                    shutil.copyfileobj(fh, self.wfile)
                return
            super().do_GET()

        def log_message(self, fmt, *args):
            sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"serving {STAGE} on 0.0.0.0:{PORT} · /download saves {BOOK}")
        httpd.serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())
