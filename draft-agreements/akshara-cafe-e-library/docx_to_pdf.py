#!/usr/bin/env python3
"""
DOCX -> PDF converter for the Akshara Café draft (ReportLab Platypus).
Hindi (Devanagari) paragraphs are rendered via PyMuPDF Story (HarfBuzz shaping)
to high-res images and embedded, because ReportLab does not shape Indic scripts.
English uses Tinos (Times-compatible) fonts downloaded to /tmp/fonts.
"""
import os, re, sys, hashlib, html as htmlmod
sys.path.insert(0, "/usr/local/lib/python3.11/dist-packages")

from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph as RLPara, Spacer, Table as RLTable,
                                TableStyle, PageBreak, Image, HRFlowable, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

SRC = "/home/user/agency-agents/draft-agreements/akshara-cafe-e-library/01_Draft_License_Agreement_Akshara_Cafe_E-Library_For_Approval.docx"
OUT = "/home/user/agency-agents/draft-agreements/akshara-cafe-e-library/01_Draft_License_Agreement_Akshara_Cafe_E-Library_For_Approval.pdf"
FONTDIR = "/tmp/fonts"
HINDI_CACHE = "/tmp/hindi_cache"
os.makedirs(HINDI_CACHE, exist_ok=True)

pdfmetrics.registerFont(TTFont("Tinos-Regular", f"{FONTDIR}/Tinos-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Tinos-Bold", f"{FONTDIR}/Tinos-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Tinos-Italic", f"{FONTDIR}/Tinos-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Tinos-BoldItalic", f"{FONTDIR}/Tinos-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("Tinos", normal="Tinos-Regular", bold="Tinos-Bold",
                              italic="Tinos-Italic", boldItalic="Tinos-BoldItalic")
pdfmetrics.registerFont(TTFont("DejaVuSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))

NAVY = colors.HexColor("#1F2E6E")
MAROON = colors.HexColor("#7A1F1F")
GREY = colors.HexColor("#555555")
PAGE_W, PAGE_H = A4
MARGIN_X = 55
AVAIL = PAGE_W - 2 * MARGIN_X

DEV_RE = re.compile(r"[ऀ-ॿ]")

# ---------------- Hindi line renderer (MuPDF Story) ----------------
def hindi_image(text, pt_size, bold, color_hex):
    import pymupdf
    from PIL import Image as PILImage, ImageChops
    key = hashlib.sha256(f"{text}|{pt_size}|{bold}|{color_hex}".encode()).hexdigest()[:16]
    png = os.path.join(HINDI_CACHE, f"{key}.png")
    meta = os.path.join(HINDI_CACHE, f"{key}.txt")
    if not os.path.exists(png):
        fam = "ndb" if bold else "nd"
        css = ("@font-face {font-family: nd; src: url(NotoSansDevanagari-Regular.ttf);}"
               "@font-face {font-family: ndb; src: url(NotoSansDevanagari-Bold.ttf);}")
        esc = htmlmod.escape(text)
        html_doc = f'<p style="font-family: {fam}; font-size: 48px; color: {color_hex}; margin: 0;">{esc}</p>'
        arch = pymupdf.Archive(FONTDIR)
        story = pymupdf.Story(html=html_doc, user_css=css, archive=arch)
        tmp_pdf = os.path.join(HINDI_CACHE, f"{key}.pdf")
        writer = pymupdf.DocumentWriter(tmp_pdf)
        mediabox = pymupdf.Rect(0, 0, 3000, 160)
        dev = writer.begin_page(mediabox)
        story.place(pymupdf.Rect(10, 10, 2990, 150))
        story.draw(dev)
        writer.end_page(); writer.close()
        doc = pymupdf.open(tmp_pdf)
        pix = doc[0].get_pixmap(dpi=300)
        pix.save(png)
        # trim white margins
        im = PILImage.open(png).convert("L")
        bbox = ImageChops.difference(im, PILImage.new("L", im.size, 255)).getbbox()
        imc = PILImage.open(png)
        if bbox:
            pad = 8
            bbox = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), min(imc.width, bbox[2]+pad), min(imc.height, bbox[3]+pad))
            imc = imc.crop(bbox)
        imc.save(png)
        with open(meta, "w") as f:
            f.write(f"{imc.width} {imc.height}")
    with open(meta) as f:
        w_px, h_px = (int(x) for x in f.read().split())
    # 48px font on a 300dpi render: 1 css pt = 300/72 px ; scale to target pt size
    scale = (pt_size / 48.0) * (72.0 / 300.0)
    w_pt, h_pt = w_px * scale, h_px * scale
    if w_pt > AVAIL:
        ratio = AVAIL / w_pt
        w_pt *= ratio; h_pt *= ratio
    return png, w_pt, h_pt

# ---------------- Helpers ----------------
def run_markup(run, para_font_size):
    t = run.text
    if not t:
        return ""
    t = htmlmod.escape(t)
    # fallback font for ballot box which Tinos lacks
    t = t.replace("☐", '<font name="DejaVuSans">☐</font>')
    # preserve multiple spaces minimally (ReportLab collapses) - convert double spaces
    t = t.replace("  ", "&nbsp;&nbsp;")
    bold = bool(run.bold)
    italic = bool(run.italic)
    size = None
    try:
        if run.font.size:
            size = run.font.size.pt
    except Exception:
        pass
    color = None
    try:
        if run.font.color and run.font.color.rgb is not None:
            color = f"#{run.font.color.rgb}"
    except Exception:
        pass
    hl = False
    try:
        hl = run.font.highlight_color is not None
    except Exception:
        pass
    inner = t
    if bold and italic:
        inner = f"<b><i>{inner}</i></b>"
    elif bold:
        inner = f"<b>{inner}</b>"
    elif italic:
        inner = f"<i>{inner}</i>"
    attrs = []
    if size and abs(size - para_font_size) > 0.1:
        attrs.append(f'size="{size}"')
    if color:
        attrs.append(f'color="{color}"')
    if hl:
        attrs.append('backColor="#FFF59D"')
    if attrs:
        inner = f"<font {' '.join(attrs)}>{inner}</font>"
    return inner

def para_font_size(p):
    for r in p.runs:
        try:
            if r.font.size:
                return r.font.size.pt
        except Exception:
            pass
    s = p.style.name
    if s == "Heading 1": return 14.5
    if s == "Heading 2": return 12
    if s == "Heading 3": return 11
    return 10.5

def alignment_of(p, in_cell=False):
    a = p.alignment
    if a == WD_ALIGN_PARAGRAPH.CENTER: return TA_CENTER
    if a == WD_ALIGN_PARAGRAPH.RIGHT: return TA_RIGHT
    if a == WD_ALIGN_PARAGRAPH.JUSTIFY: return TA_JUSTIFY
    if a == WD_ALIGN_PARAGRAPH.LEFT: return TA_LEFT
    return TA_LEFT if in_cell else TA_JUSTIFY

def convert_para(p, in_cell=False, avail=AVAIL):
    text_all = p.text
    if not text_all.strip():
        return None
    pPr = p._p.find(qn('w:pPr'))
    if pPr is not None and pPr.find(qn('w:pBdr')) is not None and not text_all.strip():
        return HRFlowable(width="100%", thickness=1.1, color=NAVY, spaceAfter=7, spaceBefore=2)
    size = para_font_size(p)
    style_name = p.style.name
    is_heading = style_name.startswith("Heading")
    space_before = 9 if style_name == "Heading 1" else (7 if style_name == "Heading 2" else 5 if is_heading else 1)
    try:
        if p.paragraph_format.space_before is not None:
            space_before = p.paragraph_format.space_before.pt
    except Exception:
        pass
    space_after = 3.5
    try:
        if p.paragraph_format.space_after is not None:
            space_after = p.paragraph_format.space_after.pt
    except Exception:
        pass
    left = 0; first = 0
    try:
        if p.paragraph_format.left_indent is not None:
            left = p.paragraph_format.left_indent.pt
        if p.paragraph_format.first_line_indent is not None:
            first = p.paragraph_format.first_line_indent.pt
    except Exception:
        pass
    align = alignment_of(p, in_cell=in_cell)
    # Hindi paragraph -> image
    if DEV_RE.search(text_all):
        bold = any(r.bold for r in p.runs) or is_heading
        col = "#1A1A1A"
        for r in p.runs:
            try:
                if r.font.color and r.font.color.rgb is not None:
                    col = f"#{r.font.color.rgb}"; break
            except Exception:
                pass
        if is_heading:
            col = "#1F2E6E"
        png, w_pt, h_pt = hindi_image(text_all.strip(), size, bold, col)
        if w_pt > avail:
            ratio = avail / w_pt; w_pt *= ratio; h_pt *= ratio
        img = Image(png, width=w_pt, height=h_pt)
        img.hAlign = "CENTER" if align == TA_CENTER else ("RIGHT" if align == TA_RIGHT else "LEFT")
        img.spaceBefore = space_before; img.spaceAfter = space_after
        if in_cell and align == TA_CENTER:
            wrap = RLTable([[img]], colWidths=[avail])
            wrap.setStyle(TableStyle([("ALIGN", (0,0), (-1,-1), "CENTER"),
                                      ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                                      ("LEFTPADDING", (0,0), (-1,-1), 0),
                                      ("RIGHTPADDING", (0,0), (-1,-1), 0),
                                      ("TOPPADDING", (0,0), (-1,-1), 0),
                                      ("BOTTOMPADDING", (0,0), (-1,-1), 0)]))
            return wrap
        return img
    markup = "".join(run_markup(r, size) for r in p.runs)
    if is_heading and "<b>" not in markup:
        markup = f"<b>{markup}</b>"
    text_color = NAVY if style_name in ("Heading 1", "Heading 2") else colors.HexColor("#1A1A1A")
    # runs may override with explicit color (centred colored titles) -> keep style color black; font tags handle it
    st = ParagraphStyle(
        name=f"s{id(p)}", fontName="Tinos-Bold" if (is_heading) else "Tinos-Regular",
        fontSize=size, leading=size * 1.22,
        alignment=align, spaceAfter=space_after, spaceBefore=space_before,
        textColor=text_color if not in_cell else colors.HexColor("#1A1A1A"),
        leftIndent=left, firstLineIndent=first,
    )
    try:
        return RLPara(markup, st)
    except Exception as e:
        # fallback: plain escaped text
        return RLPara(htmlmod.escape(text_all), st)

def cell_shading(cell):
    tcPr = cell._tc.find(qn('w:tcPr'))
    if tcPr is not None:
        shd = tcPr.find(qn('w:shd'))
        if shd is not None:
            fill = shd.get(qn('w:fill'))
            if fill and fill != "auto":
                return f"#{fill}"
    return None

def cell_borderless(cell):
    tcPr = cell._tc.find(qn('w:tcPr'))
    if tcPr is not None:
        b = tcPr.find(qn('w:tcBorders'))
        if b is not None:
            vals = [el.get(qn('w:val')) for el in b]
            if vals and all(v == "nil" for v in vals):
                return True
    return False

def convert_table(tbl):
    ncols = max(len(r.cells) for r in tbl.rows)
    # widths from first row cell.width
    widths = []
    for c in tbl.rows[0].cells:
        try:
            widths.append(c.width.pt if c.width else None)
        except Exception:
            widths.append(None)
    if len(widths) < ncols:
        widths += [None] * (ncols - len(widths))
    if any(w is None for w in widths):
        widths = [AVAIL / ncols] * ncols
    total = sum(widths)
    widths = [w * AVAIL / total for w in widths]

    data = []
    style_cmds = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ]
    borderless = all(cell_borderless(c) for r in tbl.rows for c in r.cells)
    if not borderless:
        style_cmds += [
            ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#8A93A6")),
            ("BOX", (0, 0), (-1, -1), 0.9, NAVY),
        ]
    for ri, row in enumerate(tbl.rows):
        out_row = []
        for ci, cell in enumerate(row.cells):
            flow = []
            cwd = widths[ci] - 10 if ci < len(widths) else 100
            hi_avail = max(cwd, 30)
            globals()['AVAIL_TMP'] = hi_avail
            for p in cell.paragraphs:
                # temp set module AVAIL for hindi cap via param
                f = convert_para_cell(p, hi_avail)
                if f is not None:
                    flow.append(f)
            if not flow:
                flow = [RLPara("", ParagraphStyle(name=f"e{ri}{ci}", fontName="Tinos-Regular", fontSize=10))]
            out_row.append(flow if len(flow) > 1 else flow[0])
            sh = cell_shading(cell)
            if sh:
                style_cmds.append(("BACKGROUND", (ci, ri), (ci, ri), colors.HexColor(sh)))
        data.append(out_row)
    repeat = 1 if (len(data) > 3 and cell_shading(tbl.rows[0].cells[0]) == "#1F2E6E") else 0
    t = RLTable(data, colWidths=widths, repeatRows=repeat)
    t.hAlign = "CENTER"
    t.setStyle(TableStyle(style_cmds))
    return t

def convert_para_cell(p, avail):
    return convert_para(p, in_cell=True, avail=avail)

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Tinos-Bold", 7.5)
    canvas.setFillColor(MAROON)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 30, "DRAFT  FOR  APPROVAL  —  NOT  FOR  EXECUTION")
    canvas.setFont("Tinos-Regular", 7)
    canvas.setFillColor(GREY)
    canvas.drawCentredString(
        PAGE_W / 2, 26,
        f"Draft License Agreement — Akshara Café, E-Library, NITK Surathkal  |  Basis: CEC Minutes dated 23-09-2026, Item No. 4  |  Page {doc.page}")
    canvas.restoreState()

def main():
    document = Document(SRC)
    story = []
    body = document.element.body
    for child in body.iterchildren():
        if child.tag == qn('w:p'):
            p = Paragraph(child, document)
            # page break?
            has_pb = False
            for br in child.iter(qn('w:br')):
                if br.get(qn('w:type')) == 'page':
                    has_pb = True
            if has_pb and not p.text.strip():
                story.append(PageBreak())
                continue
            pPr = child.find(qn('w:pPr'))
            if not p.text.strip() and pPr is not None and pPr.find(qn('w:pBdr')) is not None:
                story.append(HRFlowable(width="100%", thickness=1.1, color=NAVY, spaceAfter=7, spaceBefore=2))
                continue
            if not p.text.strip():
                story.append(Spacer(1, 3))
                continue
            f = convert_para(p)
            if f is not None:
                story.append(f)
        elif child.tag == qn('w:tbl'):
            tbl = Table(child, document)
            try:
                story.append(convert_table(tbl))
            except Exception as e:
                print("TABLE ERROR:", e)
                raise
            story.append(Spacer(1, 4))
    doc = SimpleDocTemplate(OUT, pagesize=A4,
                            leftMargin=MARGIN_X, rightMargin=MARGIN_X,
                            topMargin=46, bottomMargin=40,
                            title="Draft License Agreement — Akshara Café, E-Library, NITK Surathkal (For Approval)",
                            author="Accounts Section-I, NITK Surathkal")
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print("Saved:", OUT)

if __name__ == "__main__":
    main()
