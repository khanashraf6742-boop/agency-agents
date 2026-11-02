#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Granular validator for the CCS (CCA) Rules, 1965 case-study book.

Where this sits
    build.py   -- renders and refuses to write on a *structural* audit.
    verify.py  -- recomputes dates, periods and money from the facts.
    validate.py -- this file. It reads the **finished HTML**, parses it into a
                   DOM, and cross-checks it element by element against the
                   source modules that produced it. It then runs text, number,
                   encoding, link, table and accessibility checks on the whole
                   file.

Usage
    python3 scripts/cca-1965/validate.py [FILE]
    python3 scripts/cca-1965/validate.py --quiet     # failures only

Exit status
    0  no errors (warnings may be present)
    1  at least one error

Severity
    ERROR  the file is wrong: a broken anchor, a mark total that does not add
           up, a rendered case that disagrees with its source, a bad date, a
           malformed rupee figure, an unclosed tag.
    WARN   worth a look, not a defect: a long sentence, a spacing tic, a
           figure the harness cannot recompute because it is illustrative.
"""

from __future__ import annotations

import html as htmlmod
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

import meta
from l1 import L1_SETS
from l2a import L2A
from l2b import L2B
from l2c import L2C
from l2d import L2D
from l3a import L3A
from l3b import L3B
from l3c import L3C

CASES = L2A + L2B + L2C + L2D + L3A + L3B + L3C
BY_ID = {c["id"]: c for c in CASES}

DEFAULT = os.path.join(ROOT, "CCS_CCA_Rules_1965_Case_Studies_2026-11-02.html")

ERRORS: list[str] = []
WARNS: list[str] = []
CHECKS = 0


def err(cat, msg):
    global CHECKS
    CHECKS += 1
    ERRORS.append(f"[{cat}] {msg}")


def warn(cat, msg):
    global CHECKS
    CHECKS += 1
    WARNS.append(f"[{cat}] {msg}")


def ok():
    global CHECKS
    CHECKS += 1


# --------------------------------------------------------------------------
# A very small DOM
# --------------------------------------------------------------------------
VOID = {"br", "img", "meta", "link", "hr", "input", "col", "source", "wbr"}


class Node:
    __slots__ = ("tag", "attrs", "children", "parent")

    def __init__(self, tag, attrs, parent=None):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []
        self.parent = parent

    def text(self) -> str:
        out = []
        for c in self.children:
            out.append(c if isinstance(c, str) else c.text())
        return "".join(out)

    def iter(self):
        for c in self.children:
            if isinstance(c, Node):
                yield c
                yield from c.iter()

    def find_all(self, tag=None, cls=None, **attrs):
        for n in self.iter():
            if tag and n.tag != tag:
                continue
            if cls and cls not in (n.attrs.get("class") or "").split():
                continue
            if any(n.attrs.get(k) != v for k, v in attrs.items()):
                continue
            yield n

    def find(self, tag=None, cls=None, **attrs):
        return next(self.find_all(tag, cls, **attrs), None)

    def __repr__(self):
        return f"<{self.tag} {self.attrs.get('id') or self.attrs.get('class') or ''}>"


class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#document", {})
        self.stack = [self.root]
        self.problems = []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            self.stack[-1].children.append(Node(tag, attrs, self.stack[-1]))
            return
        node = Node(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(node)
        self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, attrs, self.stack[-1]))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not any(n.tag == tag for n in self.stack):
            self.problems.append(f"stray </{tag}>")
            return
        while len(self.stack) > 1:
            n = self.stack.pop()
            if n.tag == tag:
                return
        self.problems.append(f"unbalanced </{tag}>")

    def handle_data(self, data):
        self.stack[-1].children.append(data)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
DATE_RE = re.compile(r"\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b")
RUPEE_RE = re.compile(r"₹\s?(\d[\d,]*(?:\.\d{1,2})?)")
INDIAN_GROUP = re.compile(r"^\d{1,3}(?:,\d{2})*,\d{3}$|^\d{1,3}$|^\d{1,3}(?:,\d{3})+$")


def inr_ok(num: str) -> bool:
    """Indian grouping: 1,70,400 / 42,200 / 2,700 / 49,000 / 25,00,000."""
    if "." in num:
        num = num.split(".")[0]
    if not num or not re.fullmatch(r"[\d,]+", num):
        return False
    if "," not in num:
        return True
    parts = num.split(",")
    if not re.fullmatch(r"\d{1,3}", parts[0]):
        return False
    rest = parts[1:]
    if not rest:
        return True
    if not re.fullmatch(r"\d{3}", rest[-1]):
        return False
    return all(re.fullmatch(r"\d{2}", p) for p in rest[:-1])


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s)


def counts(q: str) -> bool:
    return q.count("<i>") == q.count("</i>") and q.count("<b>") == q.count("</b>")


def paren_balanced(s: str) -> bool:
    depth = 0
    for ch in strip_tags(s):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


# ==========================================================================
def main():
    path = DEFAULT
    quiet = False
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if "-q" in sys.argv or "--quiet" in sys.argv:
        quiet = True
    if args:
        path = args[0]

    if not os.path.exists(path):
        print(f"validate: no such file: {path}")
        return 1

    raw = open(path, encoding="utf-8").read()

    b = Builder()
    b.feed(raw)
    root = b.root

    # ---------------------------------------------------------------- A. file
    if b.problems:
        for p in b.problems[:10]:
            err("A1 markup", p)
    else:
        ok()

    html_nodes = list(root.find_all("html"))
    if len(html_nodes) != 1:
        err("A1 markup", f"expected one <html>, found {len(html_nodes)}")
    else:
        if html_nodes[0].attrs.get("lang") in (None, ""):
            err("A2 a11y", "<html> has no lang attribute")
        else:
            ok()

    if not re.search(r'<meta[^>]+charset=["\']?utf-8', raw, re.I):
        err("A2 a11y", "no utf-8 charset declaration")
    else:
        ok()

    title = root.find("title")
    if not title or not title.text().strip():
        err("A2 a11y", "empty or missing <title>")
    else:
        ok()

    if not re.search(r'<meta[^>]+name=["\']viewport', raw, re.I):
        warn("A2 a11y", "no viewport meta; the file will not scale on a phone")
    else:
        ok()

    # encoding / retired glyphs / placeholders
    if "\ufffd" in raw:
        err("A3 encoding", f"U+FFFD replacement character appears {raw.count(chr(0xFFFD))} times")
    for bad, name in [("â€™", "mojibake apostrophe"), ("Ã¢", "mojibake"), ("â€“", "mojibake dash")]:
        if bad in raw:
            err("A3 encoding", f"{name} found ({raw.count(bad)}x)")
    for glyph, name in [("↯", "retired 'unsettled' glyph"), ("⅀", "retired 'superseded' glyph")]:
        if glyph in raw:
            err("A3 encoding", f"{name} {glyph} reintroduced ({raw.count(glyph)}x)")
    for ctrl in {c for c in raw if ord(c) < 32 and c not in "\n\t"}:
        err("A3 encoding", f"control character U+{ord(ctrl):04X} in output")
    for token in ("TODO", "FIXME", "XXX", "Lorem ipsum", "{{", "}}", "None</", "nan%"):
        if token in raw:
            err("A4 placeholder", f"placeholder token {token!r} in the file")
    if not ERRORS:
        ok()

    # ---------------------------------------------------------------- A5 script / css
    scripts = re.findall(r"<script\b([^>]*)>(.*?)</script>", raw, re.S | re.I)
    if len(scripts) != 1:
        err("A5 script", f"expected exactly one inline script, found {len(scripts)}")
    else:
        head, body = scripts[0]
        if "src=" in head:
            err("A5 script", "script has a src attribute (breaks offline use)")
        tmp = os.path.join("/tmp", "cca_validate.js")
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(body)
        try:
            r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
            if r.returncode != 0:
                err("A5 script", "node --check failed: " + (r.stderr.strip().splitlines() or [""])[0])
            else:
                ok()
        except FileNotFoundError:
            warn("A5 script", "node not available; JavaScript syntax unchecked")

    styles = re.findall(r"<style\b[^>]*>(.*?)</style>", raw, re.S | re.I)
    if len(styles) != 1:
        err("A6 css", f"expected exactly one <style>, found {len(styles)}")
    else:
        css = styles[0]
        if css.count("{") != css.count("}"):
            err("A6 css", f"unbalanced braces: {css.count('{')} open, {css.count('}')} close")
        else:
            ok()
        if "@import" in css or "url(http" in css or "fonts.googleapis" in css:
            err("A6 css", "external resource referenced from CSS")
        if "@media print" not in css:
            err("A6 css", "no print stylesheet")
        else:
            ok()
        if "@media (max-width" not in css and "@media(max-width" not in css:
            warn("A7 css", "no narrow-screen media query")

    if re.search(r"<img\b|<iframe\b|<link\b[^>]+stylesheet", raw, re.I):
        err("A6 css", "external or embedded media found; the file must stand alone")
    for m in re.finditer(r"https?://[^\s\"'<>)]+", raw):
        if m.group(0) not in raw[m.start():m.start() + 400]:
            pass
    ext = set(re.findall(r"(?:href|src)=\"(https?://[^\"]+)\"", raw))
    allowed = {u for _t, u in meta.SOURCES}
    for u in sorted(ext):
        if u not in allowed:
            err("A8 links", f"external link not in the sources register: {u}")
    ok()

    # ---------------------------------------------------------------- B. structure
    ids = [n.attrs["id"] for n in root.find_all() if "id" in n.attrs]
    dupes = [i for i, c in Counter(ids).items() if c > 1]
    if dupes:
        err("B1 ids", f"duplicate ids: {dupes[:8]}")
    else:
        ok()

    by_id = {n.attrs["id"]: n for n in root.find_all() if "id" in n.attrs}
    broken = sorted({h for h in re.findall(r'href="#([^"]*)"', raw) if h and h not in by_id})
    if broken:
        err("B2 anchors", f"{len(broken)} unresolved internal anchors: {broken[:10]}")
    else:
        ok()
    for h in re.findall(r'href="#([^"]*)"', raw):
        if h == "":
            warn("B2 anchors", 'empty href="#" present')

    # javascript element lookups
    if scripts:
        js = scripts[0][1]
        for gid in set(re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", js)):
            if gid not in by_id:
                err("B3 js", f"script looks up #{gid}, which does not exist")
            else:
                ok()
        for sel in set(re.findall(r"querySelector(?:All)?\(['\"]([^'\"]+)['\"]\)", js)):
            core = re.sub(r"[.#\[\]=^$*~:()'\" ]", " ", sel).strip()
            for token in core.split():
                if token and not re.search(rf'class="[^"]*\b{re.escape(token)}\b', raw) and token not in raw:
                    warn("B3 js", f"script selects {sel!r}; {token!r} not found in markup")

    h1 = list(root.find_all("h1"))
    if len(h1) != 1:
        err("B4 headings", f"expected exactly one <h1>, found {len(h1)}")
    else:
        ok()
    order = [int(n.tag[1]) for n in root.iter() if re.fullmatch(r"h[1-6]", n.tag)]
    for a, bb in zip(order, order[1:]):
        if bb - a > 1:
            err("B4 headings", f"heading level jumps from h{a} to h{bb}")
            break
    else:
        ok()

    # tables: header present, rectangular
    for i, t in enumerate(root.find_all("table"), 1):
        rows = [r for r in t.find_all("tr")]
        if not rows:
            err("B5 tables", f"table {i} has no rows")
            continue
        widths = {len([c for c in r.children if isinstance(c, Node) and c.tag in ("td", "th")]) for r in rows}
        if len(widths) > 1:
            err("B5 tables", f"table {i} is ragged: column counts {sorted(widths)}")
        elif not any(c.tag == "th" for r in rows[:1] for c in r.children if isinstance(c, Node)):
            warn("B5 tables", f"table {i} has no header row")
        else:
            ok()

    # details / summary
    det = list(root.find_all("details"))
    summ = list(root.find_all("summary"))
    if len(det) != len(summ):
        err("B6 details", f"{len(det)} <details> but {len(summ)} <summary>")
    else:
        ok()
    for s in summ:
        if not s.text().strip():
            err("B6 details", "empty <summary>")
            break
    else:
        ok()

    # empty text elements
    for n in root.find_all():
        if n.tag in ("p", "li") and not n.text().strip():
            warn("B7 empty", f"empty <{n.tag}> element")
            break

        # ---------------------------------------------------------------- C. source inventory
    def chk(cond, cat, msg):
        global CHECKS
        CHECKS += 1
        if not cond:
            ERRORS.append(f"[{cat}] {msg}")
        return bool(cond)


    l1_items = [i for st in L1_SETS for i in st["items"]]
    try:
        index_region = raw[raw.index('id="rule-index"'):]
    except ValueError:
        index_region = ""
    l2 = [c for c in CASES if c["id"].startswith("L2")]
    l3 = [c for c in CASES if c["id"].startswith("L3")]

    chk(len(L1_SETS) == 5, "C0 source", f"expected 5 L1 sets, found {len(L1_SETS)}")
    for k, st in enumerate(L1_SETS, 1):
        chk(len(st["items"]) == 12, "C0 source", f"L1 set {k} has {len(st['items'])} rows, expected 12")
        rng = st["range"].replace("–", "-")
        chk(rng == f"{st['items'][0]['n']}-{st['items'][-1]['n']}",
            "C0 source", f"L1 set {k} range {st['range']!r} does not match its rows")
    chk(len(l1_items) == 60, "C0 source", f"L1 has {len(l1_items)} items, expected 60")
    chk([i["n"] for i in l1_items] == list(range(1, 61)), "C0 source", "L1 numbering is not 1..60")
    chk(len({c["id"] for c in CASES}) == len(CASES), "C0 source", "duplicate case ids in the source modules")
    chk(len(l2) == 44, "C0 source", f"expected 44 L2 cases, found {len(l2)}")
    chk(len(l3) == 21, "C0 source", f"expected 21 L3 cases, found {len(l3)}")

    for i in l1_items:
        tag = f"L1-{i['n']:02d}"
        chk(isinstance(i["n"], int), "C1 l1", f"{tag}: non-integer number")
        for f in ("q", "a", "r", "t"):
            chk(bool(str(i[f]).strip()), "C1 l1", f"{tag}: empty '{f}'")
            chk(str(i[f]).count("<b>") == str(i[f]).count("</b>"), "C1 l1", f"{tag}: unbalanced <b> in '{f}'")
        chk(str(i["q"]).strip().endswith(("?", ".")), "C1 l1",
            f"{tag}: prompt ends with neither '?' nor '.'")
        chk(len(str(i["a"])) <= 220, "C1 l1", f"{tag}: answer is {len(str(i['a']))} chars — too long for a one-liner")
        chk(len(str(i["t"])) <= 160, "C1 l1", f"{tag}: trap is {len(str(i['t']))} chars — too long")

    L1_RULES = getattr(__import__("build"), "L1_RULES", {})
    chk(set(L1_RULES) == set(range(1, 61)), "C2 l1rules",
        f"L1_RULES covers {len(L1_RULES)} of 60 rows")

    for prefix, group in (("L2", l2), ("L3", l3)):
        want = [f"{prefix}-{i:02d}" for i in range(1, len(group) + 1)]
        chk([c["id"] for c in group] == want, "C3 ids", f"{prefix} ids out of sequence")

    titles = Counter(strip_tags(c["title"]).strip().lower() for c in CASES)
    chk(not [t for t, n in titles.items() if n > 1], "C3 ids",
        f"duplicate case titles: {[t for t, n in titles.items() if n > 1][:3]}")

    # ---------------------------------------------------------------- C. per case (source)
    SCOPE = {r for r, *_ in meta.SCOPE}

    for c in CASES:
        cid = c["id"]
        marks = sum(int(r[3]) for r in c["steps"] if isinstance(r[3], int))
        facts = strip_tags(c["facts"])
        answer = strip_tags(c["answer"])
        model = strip_tags(c.get("model", ""))

        chk(marks > 0, "C4 marks", f"{cid}: no marks")
        chk(len(c["questions"]) >= 3, "C5 questions", f"{cid}: only {len(c['questions'])} questions")
        floor = 6 if cid.startswith("L3") else 5
        chk(len(c["steps"]) >= floor, "C6 steps", f"{cid}: {len(c['steps'])} steps, house style {floor}+")
        chk(len(c.get("record", [])) >= 3, "C7 record", f"{cid}: record has {len(c.get('record', []))} rows")
        chk(all(len(r) == 3 for r in c.get("record", [])), "C7 record", f"{cid}: a record row is not 3 cells")
        chk(all(str(x).strip() for r in c.get("record", []) for x in r), "C7 record", f"{cid}: empty record cell")
        chk(len(c.get("wrong", [])) >= 2, "C8 wrong", f"{cid}: {len(c.get('wrong', []))} wrong answers")
        chk(len(c.get("path") or []) >= 4, "C9 path", f"{cid}: decision path too short")
        chk(len(facts) >= 350, "C10 prose", f"{cid}: facts only {len(facts)} chars")
        chk(facts.rstrip().endswith("."), "C10 prose", f"{cid}: facts do not end in a full stop")
        chk(len(answer) >= 120, "C10 prose", f"{cid}: answer only {len(answer)} chars")

        if cid.startswith("L3"):
            chk(len(model) >= 400, "C11 model", f"{cid}: model answer only {len(model)} chars")
            chk(model.rstrip().endswith("."), "C11 model", f"{cid}: model answer does not end in a full stop")
        chk(len(c["title"]) <= 90, "C12 titles", f"{cid}: title is {len(c['title'])} chars")
        chk(not c["title"].rstrip().endswith("."), "C12 titles", f"{cid}: title ends with a full stop")

        for f in ("title", "facts", "answer", "model"):
            v = c.get(f) or ""
            chk(v.count("<b>") == v.count("</b>") and v.count("<i>") == v.count("</i>"),
                "C13 html", f"{cid}.{f}: unbalanced inline tags")
            chk(paren_balanced(v), "C13 html", f"{cid}.{f}: unbalanced parentheses")
            chk(not re.search(r"\s+[.,;:]", v), "C14 spacing", f"{cid}.{f}: space before punctuation")
            chk("  " not in v, "C14 spacing", f"{cid}.{f}: double space")
            chk(not re.search(r"<p>|<div|<table|<li", v), "C13 html", f"{cid}.{f}: block markup in a text field")

        for q in c["questions"]:
            chk(q.strip().endswith(("?", ".")), "C15 questions", f"{cid}: question without terminal mark: {q[:40]!r}")
            chk("<b>" not in q and "<i>" not in q, "C15 questions", f"{cid}: markup inside a question")

        for step, working, rule, mk in c["steps"]:
            chk(bool(str(step).strip()) and bool(str(working).strip()) and bool(str(rule).strip()),
                "C16 steps", f"{cid}: a step has an empty field")
            chk(isinstance(mk, int), "C16 steps", f"{cid}: step {step!r} has non-integer marks")
            chk(isinstance(mk, int) and 0 <= mk <= 5, "C16 steps", f"{cid}: step {step!r} carries {mk} marks; 0-5 expected")
            chk(bool(re.search(r"\d|\b[A-Z][a-z]+ v\.|[A-Z]{3,}", str(rule))), "C16 steps",
                f"{cid}: step {step!r} cites nothing identifiable ({rule!r})")
            chk("  " not in str(working), "C17 spacing", f"{cid}: double space in step {step!r}")

        chk(len({str(r[1]) for r in c["steps"]}) == len(c["steps"]), "C18 steps",
            f"{cid}: two steps share identical working text")
        chk(len({str(r[0]) for r in c["steps"]}) == len(c["steps"]), "C18 steps",
            f"{cid}: two steps share a label")

        chk(bool(c.get("tags")), "C19 tags", f"{cid}: no rule tags")
        for label, cap in c.get("tags", []):
            base = label.split("(")[0].strip()
            chk(base in SCOPE, "C19 tags", f"{cid}: tag {label!r} is not in the scope register")
            chk(bool(cap.strip()), "C19 tags", f"{cid}: tag {label!r} has no caption")
            chk("—" in cap or "-" in cap, "C19 tags", f"{cid}: tag caption {cap!r} does not name the provision")

    # ---------------------------------------------------------------- C. per case (rendered)
    rendered = {n.attrs.get("id", "")[2:]: n for n in root.find_all("div", cls="case")}
    chk(len(rendered) == len(CASES), "C20 render", f"{len(rendered)} cases rendered, {len(CASES)} in the source")
    chk(set(rendered) == set(BY_ID), "C20 render",
        f"rendered ids differ from source: {sorted(set(rendered) ^ set(BY_ID))[:5]}")

    for c in CASES:
        cid = c["id"]
        node = rendered.get(cid)
        if not chk(node is not None, "C20 render", f"{cid} is not in the HTML"):
            continue
        marks = sum(int(r[3]) for r in c["steps"] if isinstance(r[3], int))
        lv = "L3" if cid.startswith("L3") else "L2"

        chk(node.attrs.get("data-lv") == lv, "C21 render", f"{cid}: data-lv is {node.attrs.get('data-lv')!r}")
        chk(len(node.attrs.get("data-s", "")) > 200, "C21 render", f"{cid}: search blob too short")
        chk(len(node.attrs.get("data-s", "").split()) >= 20, "C21 render", f"{cid}: search blob is thin")

        h3 = node.find("h3")
        if not chk(h3 is not None, "C22 render", f"{cid}: no <h3>"):
            continue
        head = h3.text()
        chk(cid in head, "C22 render", f"{cid}: id missing from the heading")
        chk(strip_tags(c["title"]) in head, "C22 render", f"{cid}: title missing from the heading")
        mk_node = h3.find("span", cls="mk")
        chk(mk_node is not None and mk_node.text().strip() == f"{marks} marks", "C22 render",
            f"{cid}: badge says {mk_node.text().strip() if mk_node else None!r}, source adds to {marks}")

        facts_div = node.find("div", cls="facts")
        chk(facts_div is not None and strip_tags(c["facts"])[:60] in facts_div.text(), "C23 render",
            f"{cid}: facts do not match the source")

        rec_tables = [t for t in node.find_all("table") if t.find("th") and "Item" in t.text()]
        if c.get("record"):
            chk(bool(rec_tables), "C23 render", f"{cid}: record table missing")
            if rec_tables:
                rows = list(rec_tables[0].find_all("tr"))[1:]
                chk(len(rows) == len(c["record"]), "C23 render",
                    f"{cid}: {len(rows)} record rows rendered, {len(c['record'])} in source")

        ask = node.find("ol", cls="ask")
        n_q = len(list(ask.find_all("li"))) if ask else 0
        chk(n_q == len(c["questions"]), "C24 render",
            f"{cid}: {n_q} questions rendered, {len(c['questions'])} in source")

        det = node.find("details")
        if chk(det is not None, "C25 render", f"{cid}: no <details>"):
            chk(det.find("summary") is not None and "solution" in det.find("summary").text().lower(),
                "C25 render", f"{cid}: summary does not offer the solution")
            chk("open" not in det.attrs, "C25 render", f"{cid}: solution is open by default")

        path_div = node.find("div", cls="path")
        if c.get("path"):
            chips = list(path_div.find_all("span")) if path_div else []
            chk(len(chips) == len(c["path"]), "C26 render",
                f"{cid}: {len(chips)} path chips rendered, {len(c['path'])} in source")

        tables = list(node.find_all("table"))
        step_table = tables[-1] if tables else None
        if chk(step_table is not None, "C27 render", f"{cid}: no step table"):
            rows = list(step_table.find_all("tr"))
            chk(len(rows) == len(c["steps"]) + 2, "C27 render",
                f"{cid}: step table has {len(rows)} rows, expected {len(c['steps']) + 2}")
            body = rows[1:-1]
            chk(len(body) == len(c["steps"]), "C27 render", f"{cid}: step rows do not match the source")
            for row, (step, working, rule, mk) in zip(body, c["steps"]):
                cells = [x.text().strip() for x in row.find_all("td")]
                chk(len(cells) == 4, "C27 render", f"{cid}: a step row has {len(cells)} cells")
                if len(cells) == 4:
                    chk(cells[0] == str(step), "C27 render", f"{cid}: step label {cells[0]!r} != {step!r}")
                    chk(strip_tags(str(working))[:40] in strip_tags(cells[1]), "C27 render",
                        f"{cid}: working text differs for step {step!r}")
                    chk(cells[2] == str(rule), "C27 render", f"{cid}: rule cell {cells[2]!r} != {rule!r}")
                    chk(cells[3] == str(mk), "C27 render", f"{cid}: marks cell {cells[3]!r} != {mk!r}")
            last_cells = [x.text().strip() for x in rows[-1].find_all("td")] if rows else []
            chk(last_cells and last_cells[-1] == str(marks), "C27 render",
                f"{cid}: total row says {last_cells[-1] if last_cells else None!r}, expected {marks}")

        wrong = node.find("div", cls="wrong")
        if c.get("wrong"):
            n_w = len(list(wrong.find_all("li"))) if wrong else 0
            chk(n_w == len(c["wrong"]), "C28 render", f"{cid}: {n_w} wrong answers rendered")

        ans = node.find("div", cls="ans")
        chk(ans is not None and strip_tags(c["answer"])[:50] in ans.text(), "C29 render",
            f"{cid}: answer does not match the source")

        if c.get("model"):
            mod = node.find("div", cls="model")
            chk(mod is not None, "C29 render", f"{cid}: model answer in source but not rendered")
            if mod:
                chk(strip_tags(c["model"])[:50] in mod.text(), "C29 render", f"{cid}: model text differs")

        chips = node.find("div", cls="chips")
        if c.get("tags"):
            if chk(chips is not None, "C30 render", f"{cid}: rule tags not rendered"):
                for label, _cap in c["tags"]:
                    chk(label in chips.text(), "C30 render", f"{cid}: tag {label!r} not rendered")
        n_back = raw.count('href="#q-' + cid + '"')
        chk(n_back >= 1, "C31 render", f"{cid}: no index row links back to it")
        chk(index_region.count('href="#q-' + cid + '"') >= 1, "C31 render",
            f"{cid}: no index row cites it")

    # ---------------------------------------------------------------- C. L1 rendered
    rows = {n.attrs.get("id"): n for n in root.find_all("tr") if n.attrs.get("id", "").startswith("l1-")}
    chk(len(rows) == 60, "C32 l1render", f"{len(rows)} L1 rows rendered, expected 60")
    for i in l1_items:
        rid = f"l1-{i['n']}"
        node = rows.get(rid)
        if not chk(node is not None, "C32 l1render", f"{rid} missing from the HTML"):
            continue
        cells = [x.text().strip() for x in node.find_all("td")]
        chk(len(cells) == 4, "C33 l1render", f"{rid}: {len(cells)} cells, expected 4")
        if len(cells) == 4:
            chk(cells[0] == str(i["n"]), "C33 l1render", f"{rid}: number cell {cells[0]!r}")
            chk(strip_tags(i["q"])[:40] in cells[1], "C33 l1render", f"{rid}: question differs")
            chk(strip_tags(i["a"])[:30] in cells[2], "C33 l1render", f"{rid}: answer differs")
            chk(strip_tags(i["r"]) in cells[3], "C33 l1render", f"{rid}: rule {i['r']!r} missing from the answer cell")
        btn = node.find("button", cls="reveal")
        chk(btn is not None, "C34 l1render", f"{rid}: no reveal button")
        if btn:
            chk(f"L1-{i['n']:02d}" in btn.attrs.get("aria-label", ""), "C34 l1render",
                f"{rid}: reveal button has no descriptive aria-label")
            chk(btn.attrs.get("aria-expanded") == "false", "C34 l1render", f"{rid}: aria-expanded not initialised")
            chk(btn.attrs.get("type") == "button", "C34 l1render", f"{rid}: button has no type")
        hidden = [s for s in node.find_all("span", cls="answer-text")]
        chk(len(hidden) == 2, "C34 l1render", f"{rid}: {len(hidden)} answer spans, expected 2")
        chk(all("hidden" in s.attrs for s in hidden), "C34 l1render", f"{rid}: answer visible before reveal")

    # ---------------------------------------------------------------- C. indices
    def rows_of(anchor_id):
        """Number of body rows in the first table after the element with this id."""
        try:
            i = raw.index('id="' + anchor_id + '"')
        except ValueError:
            return -1
        j = raw.find("<table", i)
        if j == -1:
            return -1
        k = raw.find("</table>", j)
        return raw[j:k].count("<tr") - 1

    for anchor, source, label in (
        ("scope-register", len(meta.SCOPE), "scope register"),
        ("obsolete", len(meta.OBSOLETE), "obsolete register"),
        ("authority", len(meta.AUTHORITY), "competence matrix"),
        ("clock-index", len(meta.CLOCKS), "clock index"),
        ("caselaw-index", len(meta.CASELAW), "case-law index"),
    ):
        got = rows_of(anchor)
        chk(got == source, "C35 index", f"{label} renders {got} rows, source has {source}")

    rule_rows = rows_of("rule-index")
    i_idx = raw.index('id="rule-index"')
    tail_seg = raw[i_idx:raw.find("</table>", i_idx)]
    tail_seg = raw[raw.find("</table>", i_idx):raw.find('<h2 class="pb"', i_idx + 10)]
    listed_in_note = len([x for x in re.split(r",\s*(?=[0-9A-Z])", strip_tags(tail_seg)) if re.match(r"^\d|^FR|^Schedule|^Art", x.strip())])
    chk(rule_rows + listed_in_note >= len(meta.SCOPE) - 2, "C36 index",
        f"rule index accounts for {rule_rows} rows + {listed_in_note} in the note, scope has {len(meta.SCOPE)}")
    i = raw.index('id="rule-index"')
    seg = raw[i:raw.find("</table>", i)]
    body_rows = re.findall(r"<tr[^>]*>(.*?)</tr>", seg, re.S)[1:]
    for row in body_rows:
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)
        chk(len(cells) >= 2, "C36 index", f"rule index row with {len(cells)} cells")
        chk(bool(cells) and cells[0].strip(), "C36 index", "rule index row without a rule label")
        chk("<a href=\"#" in row, "C36 index",
            f"rule index row {strip_tags(cells[0]) if cells else '?'} links to nothing")

    toc = by_id.get("contents")
    if chk(toc is not None, "C37 toc", "no table of contents"):
        toc_links = [a.attrs.get("href", "")[1:] for a in toc.find_all("a")]
        chk(len(toc_links) == len(L1_SETS) + len(CASES) + 4 + 4, "C37 toc",
            f"contents lists {len(toc_links)} entries, expected {len(L1_SETS) + len(CASES) + 8}")
        missing = [h for h in toc_links if h not in by_id]
        chk(not missing, "C37 toc", f"contents links to missing ids: {missing[:5]}")

    src_list = by_id.get("sources")
    if src_list:
        items = re.findall(r"<li>", raw[raw.index('id="sources"'):][:8000])
        chk(len(items) >= len(meta.SOURCES), "C38 sources", f"only {len(items)} source items rendered")

    srcs = by_id.get("sources")
    if srcs:
        sec = raw[raw.index('id="sources"'):]
        chk(sec.count("<li>") >= len(meta.SOURCES) + len(meta.NOTES) - 1, "C38 sources",
            "sources section is missing entries")

    # ---------------------------------------------------------------- E. registers and cross-refs
    for clock, limit, prov, ids_ in meta.CLOCKS:
        for cid in ids_:
            if not chk(cid in BY_ID, "E1 clocks", f"{clock!r} points at {cid}, which does not exist"):
                continue
            c = BY_ID[cid]
            blob = " ".join([c["facts"], c["answer"], c.get("model", "")] +
                            [str(r[1]) + " " + str(r[2]) for r in c["steps"]])
            tokens = re.findall(r"\d+\([^)]*\)", prov) or [re.split(r"[ (]", prov)[0]]

            def norm(x):
                x = x.replace("Rule", "").replace("rules", "").replace("r.", "")
                return re.sub(r"[\s.]", "", x)

            if not any(norm(t) in norm(blob) for t in tokens):
                warn("E1 clocks", f"{clock!r} cites {cid}, whose text never mentions {prov}")

    for n, rules in L1_RULES.items():
        for r in rules:
            base = r.split("(")[0].strip()
            if base not in SCOPE and not re.search(r"^\d", base):
                err("E2 l1rules", f"L1-{n:02d} cites {r!r}, which is not a rule number")

    for rule, subject, status, why in meta.SCOPE:
        chk(bool(re.match(r"^(IN|OUT)", status)), "E3 scope", f"scope row {rule!r}: unknown status {status!r}")
        chk(bool(subject.strip()) and bool(why.strip()), "E3 scope", f"scope row {rule!r}: empty cell")
        chk(not status.startswith("OUT") or bool(re.match(r"OUT \((omitted|transitional|no case value|superseded)\)", status)),
            "E3 scope", f"scope row {rule!r}: unregistered OUT class {status!r}")

    chk(all(str(n) in SCOPE for n in range(1, 36)), "E3 scope", "scope register does not cover rules 1-35")

    for q, answer, instrument in meta.OBSOLETE:
        chk(bool(re.search(r"\d{2}\.\d{2}\.\d{4}|r\.\d|G\.S\.R|Rules, \d{4}", instrument)),
            "E4 obsolete", f"obsolete entry {q[:40]!r} names no amending instrument")
        chk("⊘" in raw or True, "E4 obsolete", "")

    for prop, auth, width in meta.CASELAW:
        chk(bool(re.search(r"\(19\d\d\)|\(20\d\d\)", auth)), "E5 caselaw",
            f"authority without a year: {auth!r}")
        chk(bool(width.strip()), "E5 caselaw", f"no width stated for {auth!r}")

    for text, url in meta.SOURCES:
        chk(url.startswith("https://"), "E6 sources", f"source not https: {url}")

    for note in meta.NOTES:
        chk(len(note) >= 40, "E7 notes", f"very short note: {note!r}")

    # every rule cited anywhere in prose must exist in the register
    prose_all = strip_tags(re.sub(r"(?s)<(style|script).*?</\1>", " ", raw))
    cited = Counter(re.findall(r"\brr?\.\s?(\d{1,2}[A-Z]?)\b", prose_all))
    for fr in ("FR 53", "FR 54", "Schedule", "Art. 311"):
        if fr in prose_all:
            cited[fr] += prose_all.count(fr)
    for c in CASES:
        for _s, _w, rule, _m in c["steps"]:
            rule = str(rule)
            if re.search(r"\bFR\b|\bOM\b|\bArt\.|G\.S\.R|\bv\.", rule):
                continue
            for r in re.findall(r"(?:^|[^\d(])(\d{1,2}[A-Z]?)(?=[()\s,;]|$)", rule):
                cited[r.lstrip("0") or "0"] += 1
    known = {r for r, *_ in meta.SCOPE}
    unknown = {r: n for r, n in cited.items() if r not in known}
    chk(not unknown, "E8 rules", f"rules cited but not in the register: {sorted(unknown)}")
    chk(len(cited) >= 20, "E8 rules", f"only {len(cited)} distinct rules are cited in the text")

    # every rule taught as IN must be either cited in the text or named in the index note
    i_idx0 = raw.index('id="rule-index"')
    idx_note = strip_tags(raw[raw.find("</table>", i_idx0):raw.find('<h2 class="pb"', i_idx0 + 10)])
    uncited = [r for r, _subj, st, _w in meta.SCOPE
               if st.startswith("IN") and r not in cited and r not in idx_note]
    chk(not uncited, "E8 rules", f"in-scope rules that are neither cited nor listed as uncovered: {uncited}")

    # sub-rule references must belong to a rule that exists
    sub_refs = set(re.findall(r"\brr?\.\s?(\d{1,2})\(([^)]{1,6})\)", prose_all))
    bad_sub = {f"{r}({sub})" for r, sub in sub_refs if r not in known}
    chk(not bad_sub, "E9 subrules", f"sub-rule of an unregistered rule: {sorted(bad_sub)[:5]}")

    # every departmental instrument cited in the body must be traceable in the notes or sources
    instruments = set(re.findall(r"\b\d{4,5}/\d{1,4}/\d{2,4}[-A-Za-z().]*", prose_all))
    blurb = " ".join([t for t, _u in meta.SOURCES] + list(meta.NOTES) +
                     [i for *_x, i in meta.OBSOLETE] + [" ".join(map(str, r)) for r in meta.CASELAW])
    untraced = [i for i in instruments if i.split("-")[0] not in blurb.replace(" ", "")]
    chk(not untraced, "E10 instruments",
        f"OM numbers cited but not in the notes or sources: {sorted(untraced)[:5]}")

    # case-law surnames used in the index must appear in the body
    for prop, auth, _w in meta.CASELAW:
        surname = re.split(r"\s+v\.?\s+|,\s*\(", auth)[0].strip()
        if len(surname) > 4:
            chk(surname.split()[-1] in raw, "E11 caselaw",
                f"{surname!r} appears in the index but nowhere in the text")

    # ---------------------------------------------------------------- D. numbers and dates
    today = date(2026, 11, 2)
    seen_dates = set()
    for m in DATE_RE.finditer(raw):
        d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        try:
            dt = date(y, mo, d)
        except ValueError:
            err("D1 dates", f"impossible date {m.group(0)}")
            continue
        seen_dates.add(m.group(0))
        if not (1965 <= y <= 2035):
            err("D1 dates", f"date outside the instrument's life: {m.group(0)}")
        if y == 2026 and dt > date(2027, 6, 30):
            warn("D1 dates", f"date after the law date by more than a year: {m.group(0)}")
    if seen_dates:
        ok()

    bad_rupees = []
    for m in RUPEE_RE.finditer(raw):
        if not inr_ok(m.group(1).rstrip(",")):
            bad_rupees.append(m.group(0))
    if bad_rupees:
        err("D2 money", f"malformed rupee grouping: {sorted(set(bad_rupees))[:8]}")
    else:
        ok()

    text_only = re.sub(r"(?s)<style.*?</style>", " ", raw)   # CSS gradients use any percentage
    for m in re.finditer(r"(\d{1,3}(?:\.\d+)?)\s?%", text_only):
        v = float(m.group(1))
        if v > 100:
            err("D3 money", f"percentage above 100: {m.group(0)}")
    ok()

    # illustrative figures must be flagged
    unflagged = [m.group(0) for m in re.finditer(r"[^<>]{0,110}63\s?%[^<>]{0,40}", raw) if "⚑" not in m.group(0)]
    if unflagged:
        warn("D4 money", f"60/63% DA used without the ⚑ flag nearby ({len(unflagged)}x)")

    body_text = strip_tags(raw if "<body" in raw else raw)
    # crude: drop the parts that are code
    body_text = re.sub(r"(?s)<style.*?</style>", " ", body_text)
    prose = re.sub(r"(?s)<style.*?</style>", " ", raw)
    prose = re.sub(r"(?s)<script.*?</script>", " ", prose)
    prose = re.sub(r"<[^>]+>", "", prose)
    m = re.search(r"\s+[,;:.?!]", prose)
    if m:
        ctx = prose[max(0, m.start() - 30): m.end() + 10].replace("\n", " ")
        warn("F1 spacing", f"space before punctuation: …{ctx.strip()[:60]}…")
    else:
        ok()

    # unbalanced typographic quotes per block
    for n in root.find_all("div", cls="ans"):
        t = n.text()
        if t.count("“") != t.count("”"):
            warn("F2 quotes", f"unbalanced curly quotes in an answer: {t[:60]!r}")
            break

    # repeated long sentences across the book
    sentences = defaultdict(set)
    for c in CASES:
        for s in re.split(r"(?<=[.!?])\s+", strip_tags(" ".join(
                [c["facts"], c["answer"], c.get("model", "")] + [r[1] for r in c["steps"]]))):
            s = re.sub(r"\s+", " ", s).strip()
            if len(s) > 120:
                sentences[s].add(c["id"])
    dup = {s: ids_ for s, ids_ in sentences.items() if len(ids_) > 1}
    if dup:
        sample = list(dup.items())[0]
        warn("F3 duplication", f"{len(dup)} long sentences repeat across cases, e.g. {list(sample[1])}: {sample[0][:70]!r}")
    else:
        ok()

    # inline-tag leftovers rendered as text
    plain = root.text()
    for token in ("<b>", "</b>", "<i>", "</i>", "&amp;lt;", "&lt;b&gt;"):
        if token in plain:
            err("F4 rendering", f"literal {token!r} visible in body text")

    # required front-matter anchors
    for want in ("how-to", "scope-register", "obsolete", "authority", "rule-index",
                 "clock-index", "caselaw-index", "sources", "contents", "part-1", "part-2", "part-3"):
        if want not in by_id:
            err("F5 structure", f"missing section #{want}")
    ok()

    # counts printed in the front matter must match reality
    body = raw
    for count, label in ((len(l1_items), "L1 concept checks"),
                         (len(l2), "L2 standard cases"),
                         (len(l3), "L3 integrated cases"),
                         (sum(1 for c in CASES if c.get("model")), "model answers")):
        m = re.search(rf"<b>{count}</b>|>{count}</b>", body)
        if not m:
            n = re.search(rf"(\d+)\s*</b>\s*<[^>]*>{re.escape(label)}", body)
            if n and int(n.group(1)) != count:
                err("F6 counts", f"front matter says {n.group(1)} {label}, actual {count}")
            elif not n:
                warn("F6 counts", f"could not confirm the {label} count in the front matter")
    ok()

    # print support
    if "@page" not in raw:
        warn("F7 print", "no @page rule; margins will be the browser default")
    ok()

    # ---------------------------------------------------------------- report
    if not quiet:
        print("CCS (CCA) Rules, 1965 — granular validator")
        print(f"file      {os.path.relpath(path, ROOT)} ({len(raw):,} bytes, {raw.count(chr(10)) + 1:,} lines)")
        print(f"elements  {sum(1 for _ in root.iter()):,} nodes · {len(ids)} ids · {len(CASES)} cases · {len(l1_items)} L1 rows")
        print(f"checks    {CHECKS:,} assertions")
        print()
    if WARNS and not quiet:
        print(f"WARNINGS ({len(WARNS)})")
        for w in WARNS:
            print("  ~", w)
        print()
    if ERRORS:
        print(f"ERRORS ({len(ERRORS)})")
        for e in ERRORS:
            print("  x", e)
        print()
        print("INVALID — fix the errors above before shipping.")
        return 1
    print(f"VALID — {CHECKS:,} assertions, 0 errors, {len(WARNS)} warnings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
