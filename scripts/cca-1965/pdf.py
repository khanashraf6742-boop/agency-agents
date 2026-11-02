#!/usr/bin/env python3
"""Render the finished book to a print PDF with xhtml2pdf.

The HTML book is the deliverable; this is the reading/printing copy. It is not a
second design — it flattens what xhtml2pdf cannot do (flex, grid, sticky
toolbar, interactive <details>) so that the PDF opens anywhere, including a
phone, and every answer is already visible.

    python3 scripts/cca-1965/pdf.py [SOURCE.html] [--out OUT.pdf]
"""
from __future__ import annotations

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DEFAULT = os.path.join(ROOT, "CCS_CCA_Rules_1965_Case_Studies_2026-11-02.html")

FONT_DIR = os.path.join(HERE, ".fonts")
FONT_DIR_FALLBACK = "/usr/share/fonts/truetype/dejavu"

PDF_CSS = """
@font-face { font-family: Djv; src: url("__FONT_DIR__/DejaVuSans.ttf"); }
@font-face { font-family: Djv; font-weight: bold; src: url("__FONT_DIR__/DejaVuSans-Bold.ttf"); }
@font-face { font-family: Dmv; src: url("__FONT_DIR__/DejaVuSansMono.ttf"); }
@font-face { font-family: Dmv; font-weight: bold; src: url("__FONT_DIR__/DejaVuSansMono-Bold.ttf"); }
@page { size: A4; margin: 13mm 10mm 14mm 10mm;
        @bottom-center { content: counter(page); font-size: 7.5pt; color: #6b7a8f; } }
body { font-family: Djv; font-size: 8.6pt; line-height: 1.38; color: #1d2b40; }
h1 { font-size: 17pt; color: #14284b; }
h2 { font-size: 11.5pt; color: #ffffff; background-color: #14284b; padding: 5px 8px; page-break-after: avoid; }
h3 { font-size: 9.6pt; color: #14284b; }
.sub { font-size: 8pt; color: #6b7a8f; }
.flt, .top-index, nav.toc .grp { display: none; }
.cover { background-color: #14284b; padding: 26px 22px; margin-bottom: 10px; }
.cover h1, .cover .law, .cover .k, .cover .disc, .cover span, .cover b { color: #ffffff; }
.cover table td, .cover table th { border-color: #46608c; color: #e7edf7; }
.stats div { display: inline-block; width: 33mm; text-align: center; padding: 6px 3px; }
.stats b { font-size: 14pt; }
.legend div, .howbox { border: 1px solid #d6deea; padding: 5px 7px; margin-bottom: 5px; }
.case { border: 1px solid #c9d4e5; padding: 5px 7px; margin: 7px 0; }
.ch { background-color: #eef3fa; padding: 4px 6px; }
.facts { background-color: #f6f8fc; border-left: 3px solid #2b5797; padding: 4px 6px; }
.lab { font-size: 7.2pt; color: #2b5797; }
.path span { display: inline-block; border: 1px solid #c5d3ea; padding: 0 5px; margin: 1px 2px; font-size: 7.4pt; }
.wrong { background-color: #fdecea; border-left: 3px solid #c0392b; padding: 4px 6px; }
.ans { background-color: #e9f6ee; border-left: 3px solid #2e8b57; padding: 4px 6px; }
.model { background-color: #fff4d6; border-left: 3px solid #e0b23a; padding: 4px 6px; }
.chips span { display: inline-block; border: 1px solid #c5d3ea; padding: 0 5px; margin: 1px 2px; font-size: 7.2pt; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #c9d4e5; padding: 2.5px 4px; font-size: 8pt; vertical-align: top; }
th { background-color: #e8eef8; font-size: 7.8pt; color: #1d2b40; font-weight: bold; }
.cover th { background-color: #20385f; color: #f6b385; width: 34mm; }
td.r { font-family: Dmv; font-size: 7.2pt; color: #2b5797; width: 26mm; }
td.m { width: 11mm; text-align: center; font-weight: bold; }
td.s { width: 30mm; font-weight: bold; color: #1f3b63; }
.mk { font-size: 7.4pt; color: #6b7a8f; }
.center { text-align: center; }
"""


def flatten(html: str) -> str:
    """Turn the interactive book into a linear print document."""
    html = re.sub(r'(?s)<div class="flt".*?</div>\s*(?=<h2 class="pb" id="how-to")', "", html)
    html = re.sub(r'(?s)<a class="top-index".*?</a>', "", html)

    # <details> can't be printed as a widget: promote it to a plain block and
    # keep the summary as a label so the reader still sees where the solution starts.
    html = re.sub(r"<details[^>]*>", '<div class="solution">', html)
    html = html.replace("</details>", "</div>")
    html = re.sub(r'(?s)<summary[^>]*>\s*Show solution\s*</summary>', '<div class="lab">Solution — step by step</div>', html)
    html = re.sub(r'(?s)<summary[^>]*>(.*?)</summary>', r'<div class="lab">\1</div>', html)

    # answers were hidden behind the reveal button; in print they are always open
    html = html.replace(' hidden=""', "")
    html = html.replace(" hidden", "")

    html = re.sub(r'(?s)<style>.*?</style>', "", html, count=1)
    html = html.replace("</style>", "</style>", 1)
    # insert our stylesheet after the (now removed) book CSS
    html = html.replace('<link rel="stylesheet" href="__pdf__"/>', "")
    css = PDF_CSS.replace("__FONT_DIR__", "file://" + FONT_DIR)
    html = html.replace("</head>", f"<style>{css}</style></head>", 1)

    # the script has nothing to do in print, and xhtml2pdf would choke on it
    html = re.sub(r"(?s)<script>.*?</script>", "", html)

    # the pill and the marks badge are flex children in the browser; in a linear
    # document they run into the title ("L2L2-01 ... 8 marks")
    html = re.sub(r'<span class="lv L\d">L\d</span>\s*', "", html)
    html = re.sub(r'<span class="mk">(.*?)</span>', r"<br/><span class=\"mk\">\1</span>", html)

    # <b>60</b><span>L1 concept checks</span> needs a line break without flex
    html = re.sub(r"<b>(\d+)</b><span>(.*?)</span>", r"<b>\1</b><br/><span>\2</span>", html)
    # the level badge sits directly against its label in the legend
    html = re.sub(r'(<span class="lv [^"]*">L\d</span>)<b>', r"\1 <b>", html)

    # xhtml2pdf has no layout box for the HTML5 sectioning elements; make them divs
    for tag in ("section", "nav", "article", "header", "footer", "main"):
        html = re.sub(rf"<{tag}([^>]*)>", r"<div\1>", html)
        html = html.replace(f"</{tag}>", "</div>")

    # inline monospace spans would fall back to Courier, which has no ⚑/⊘/⚠/₹
    html = html.replace("font-family:monospace", "font-family:Dmv")

    # block layout everywhere flex/grid was used
    html = html.replace('<div class="stats">', '<div class="stats">')
    return html


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?", default=DEFAULT)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    src = os.path.abspath(args.source)
    out = args.out or os.path.splitext(src)[0] + ".pdf"
    with open(src, encoding="utf-8") as fh:
        raw = fh.read()

    sys.path.insert(0, "/tmp/x2p")
    from xhtml2pdf import pisa  # noqa: E402
    from reportlab.pdfbase import pdfmetrics  # noqa: E402
    from reportlab.pdfbase.ttfonts import TTFont  # noqa: E402

    for name, file in (("Djv", "DejaVuSans.ttf"), ("Djv-Bold", "DejaVuSans-Bold.ttf"),
                       ("Dmv", "DejaVuSansMono.ttf"), ("Dmv-Bold", "DejaVuSansMono-Bold.ttf")):
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, file)))
    pdfmetrics.registerFontFamily("Djv", normal="Djv", bold="Djv-Bold", italic="Djv", boldItalic="Djv-Bold")
    pdfmetrics.registerFontFamily("Dmv", normal="Dmv", bold="Dmv-Bold", italic="Dmv", boldItalic="Dmv-Bold")

    body = flatten(raw)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "wb") as fh:
        result = pisa.CreatePDF(body, dest=fh, encoding="utf-8")
    if result.err:
        print(f"FAILED — {result.err} page(s) reported errors")
        return 1
    print(f"written: {out} ({os.path.getsize(out):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
