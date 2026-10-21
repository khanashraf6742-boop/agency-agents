#!/usr/bin/env python3
"""
Byte-range HTTP download server for the HRA masterclass deliverables.

Serves an index page at / and every file under ROOT as a Content-Disposition
attachment, with RFC-7233 range support (HTTP 206) so downloads resume and
playback scrubbing works.

    python3 serve_downloads.py
    DL_ROOT=/some/dir DL_PORT=8010 python3 serve_downloads.py
"""
import html
import os
import re
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote

ROOT = Path(os.environ.get("DL_ROOT", Path(__file__).resolve().parent)).resolve()
PORT = int(os.environ.get("DL_PORT", "8000"))
CHUNK = 1 << 20  # 1 MiB

SUFFIXES = {".mp4", ".md", ".pdf", ".srt", ".vtt", ".zip", ".json", ".txt", ".py"}
HIDE_DIRS = {"work", "tools-venv", "__pycache__"}


def human(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} TB"


def collect():
    out = []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        if any(part in HIDE_DIRS for part in rel.parts[:-1]):
            continue
        if rel.parts[0].startswith(".") or rel.name.startswith("."):
            continue
        if p.suffix.lower() in SUFFIXES:
            out.append((rel, p.stat().st_size))
    out.sort(key=lambda x: (x[0].parts[0] == "chapters", str(x[0])))
    return out


CSS = """
body{font:15px/1.55 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
     margin:0 auto;padding:40px 28px;background:#0f1216;color:#e8ecf1;max-width:1000px}
h1{font-size:22px;margin:0 0 4px;font-weight:600}
p.sub{color:#8b98a6;margin:0 0 26px;font-size:14px}
table{border-collapse:collapse;width:100%}
th{text-align:left;font-size:12px;letter-spacing:.06em;text-transform:uppercase;
   color:#7f8c9b;border-bottom:1px solid #2a323c;padding:8px 10px;font-weight:600}
td{padding:11px 10px;border-bottom:1px solid #1c222a;vertical-align:top}
tr:hover td{background:#151b22}
a{color:#5fb0ff;text-decoration:none;font-weight:500}
a:hover{text-decoration:underline}
.sz{color:#8b98a6;font-variant-numeric:tabular-nums;white-space:nowrap}
.badge{display:inline-block;border-radius:3px;padding:1px 6px;font-size:11px;margin-left:8px}
.b-master{background:#1f6feb22;color:#5fb0ff;border:1px solid #1f6feb55}
.b-brisk{background:#2ea04322;color:#5fd68a;border:1px solid #2ea04355}
.b-block{background:#d2992222;color:#e3b341;border:1px solid #d2992255}
.b-ch{background:#8957e522;color:#b980ff;border:1px solid #8957e555}
code{background:#1a2029;padding:2px 6px;border-radius:3px;font-size:13px}
.note{margin-top:28px;padding:14px 16px;background:#1a2029;border-left:3px solid #d29922;
      border-radius:0 4px 4px 0;font-size:14px;color:#c3ccd6}
"""


def badge(name: str) -> str:
    if name == "hra_masterclass.mp4":
        return '<span class="badge b-master">Master \u2014 start here</span>'
    if "brisk" in name:
        return '<span class="badge b-brisk">Brisk 1.08\u00d7</span>'
    if "rates_block" in name:
        return '<span class="badge b-block">Rates block \u2014 Ch 5\u20137</span>'
    if name.startswith("ch") and name[2:4].isdigit():
        return '<span class="badge b-ch">Chapter</span>'
    return ""


def index_page():
    rows = []
    for rel, size in collect():
        rows.append('<tr><td><a href="/%s">%s</a>%s</td><td class="sz">%s</td></tr>'
                    % (quote(str(rel)), html.escape(str(rel)), badge(rel.name), human(size)))
    body = "\n".join(rows) or '<tr><td colspan="2">No files yet.</td></tr>'
    return """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>HRA Masterclass &mdash; Downloads</title><style>%s</style></head><body>
<h1>House Rent Allowance &mdash; Masterclass Downloads</h1>
<p class="sub">DoE O.M. No. 2/4/2022-E.II(B) dated 30.12.2022 &nbsp;&bull;&nbsp;
rates updated to the position as of 21 October 2026.<br>
Click to download &mdash; every file is served as an attachment with resume support
(<code>Content-Disposition</code> + HTTP 206).</p>
<table><thead><tr><th>File</th><th>Size</th></tr></thead><tbody>
%s
</tbody></table>
<div class="note"><strong>Heads up:</strong> the PDF you supplied prints HRA at
24&percnt;&nbsp;/&nbsp;16&percnt;&nbsp;/&nbsp;8&percnt;. That is the <em>base</em> rate only.
Both automatic Dearness Allowance triggers in the Note to Para 2.1 have since fired &mdash;
the rate in force today is <strong>30&percnt;&nbsp;/&nbsp;20&percnt;&nbsp;/&nbsp;10&percnt;</strong>
from 1.1.2024, with DA at 60&percnt; from 1.1.2026. If you only watch one thing, watch the
<strong>Rates block</strong>.</div>
</body></html>""" % (CSS, body)


class Handler(BaseHTTPRequestHandler):
    server_version = "ArenaDL/1.0"
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _headers(self, code, ctype, length, extra):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        if length is not None:
            self.send_header("Content-Length", str(length))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Cache-Control", "no-store")
        for k, v in extra.items():
            self.send_header(k, v)
        self.end_headers()

    def _parse_range(self, size):
        rng = self.headers.get("Range")
        if not rng:
            return (0, size - 1) if size else (0, 0)
        m = re.match(r"^bytes=(\d*)-(\d*)$", rng.strip())
        if not m:
            return None
        s, e = m.group(1), m.group(2)
        if s == "" and e == "":
            return None
        if s == "":
            start, end = max(0, size - int(e)), size - 1
        else:
            start = int(s)
            end = int(e) if e else size - 1
        end = min(end, size - 1)
        if start > end or start >= size:
            return None
        return start, end

    def _send_file(self, path: Path, size: int):
        rng = self._parse_range(size)
        extra = {"Content-Disposition": 'attachment; filename="%s"' % path.name}
        if rng is None:
            body = ("Range Not Satisfiable: requested range outside 0-%d" % max(size - 1, 0)).encode()
            self._headers(416, "text/plain; charset=utf-8", len(body), {})
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        start, end = rng
        length = end - start + 1
        partial = length != size
        if partial:
            extra["Content-Range"] = "bytes %d-%d/%d" % (start, end, size)
        self._headers(206 if partial else 200, "application/octet-stream", length, extra)
        if self.command == "HEAD":
            return
        try:
            with open(path, "rb") as fh:
                fh.seek(start)
                remaining = length
                while remaining > 0:
                    buf = fh.read(min(CHUNK, remaining))
                    if not buf:
                        break
                    self.wfile.write(buf)
                    remaining -= len(buf)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        rel = self.path.split("?", 1)[0].lstrip("/")
        if rel in ("", "/", "index.html"):
            body = index_page().encode("utf-8")
            self._headers(200, "text/html; charset=utf-8", len(body), {})
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        target = (ROOT / rel).resolve()
        if not (target == ROOT or str(target).startswith(str(ROOT) + os.sep)):
            self._headers(403, "text/plain; charset=utf-8", 9, {})
            if self.command != "HEAD":
                self.wfile.write(b"Forbidden")
            return
        if not target.is_file():
            self._headers(404, "text/plain; charset=utf-8", 9, {})
            if self.command != "HEAD":
                self.wfile.write(b"Not found")
            return
        self._send_file(target, target.stat().st_size)


def main():
    srv = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    srv.daemon_threads = True
    print("serving %s on http://0.0.0.0:%d" % (ROOT, PORT), flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        srv.server_close()


if __name__ == "__main__":
    main()
