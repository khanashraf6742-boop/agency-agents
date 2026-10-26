#!/usr/bin/env python3
"""Extract DOCX draft to Markdown for easy review / copy-paste."""
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.ns import qn

SRC = "draft-agreements/akshara-cafe-e-library/01_Draft_License_Agreement_Akshara_Cafe_E-Library_For_Approval.docx"
OUT = "draft-agreements/akshara-cafe-e-library/01_Draft_License_Agreement_Akshara_Cafe_E-Library_For_Approval.md"

def para_md(p):
    t = p.text.strip()
    if not t:
        return ""
    s = p.style.name
    if s == "Heading 1":
        return f"# {t}\n"
    if s == "Heading 2":
        return f"## {t}\n"
    if s == "Heading 3":
        return f"### {t}\n"
    return t + "\n"

def cell_text(cell):
    parts = [para_md(p).strip() for p in cell.paragraphs]
    txt = "<br>".join(x for x in parts if x)
    return txt.replace("|", "\\|").replace("\n", " ")

def table_md(tbl):
    rows = []
    for r in tbl.rows:
        rows.append([cell_text(c) for c in r.cells])
    if not rows:
        return ""
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * n) + " |"]
    for r in rows[1:]:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out) + "\n"

doc = Document(SRC)
lines = [
    "# Draft License Agreement for Approval — Akshara Café, E-Library, NITK Surathkal",
    "",
    "> **Basis:** Minutes of the Commercial Establishment Committee (CEC) Meeting held on 23-09-2026, "
    "Ref. No. 07/NITK/AC-1/2026-27/COM-ESTB/A6 dated 24-09-2026 — **Item No. 4**.",
    ">",
    "> **Status:** DRAFT FOR APPROVAL — NOT FOR EXECUTION. This Markdown file is a plain-text extraction of the "
    "DOCX/PDF draft for convenience of review and copy-paste. Matter highlighted in yellow in the DOCX/PDF "
    "(blanks to be filled/confirmed) appears here as plain text — refer to the DOCX/PDF for the authoritative formatted draft.",
    "",
    "---",
    "",
]
for child in doc.element.body.iterchildren():
    if child.tag == qn('w:p'):
        p = Paragraph(child, doc)
        has_pb = any(br.get(qn('w:type')) == 'page' for br in child.iter(qn('w:br')))
        if has_pb and not p.text.strip():
            lines += ["", "---", ""]
            continue
        md = para_md(p)
        if md:
            lines += [md, ""]
    elif child.tag == qn('w:tbl'):
        lines += [table_md(Table(child, doc)), ""]
with open(OUT, "w") as f:
    f.write("\n".join(lines))
print("Saved:", OUT)
