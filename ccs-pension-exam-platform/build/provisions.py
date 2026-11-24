#!/usr/bin/env python3
"""provisions.py — carve every rule into addressable provisions.

A gazette rule is a tree: sub-rules (1) (2), then clauses — drafted sometimes as
(a) (b) and sometimes as (i) (ii) — then sub-clauses, then items, any of which may
carry a proviso or an explanation. The transcribed text runs them inline, so the
tree cannot be read off punctuation alone.

The parse anchors on the one series that never repeats: the sub-rule digits. Within
a rule they run 1, 2, 3 ... without a gap, so a bracketed digit at the expected next
value is a sub-rule marker and any other bracketed digit is a cross-reference. Once
the sub-rule boundaries are fixed, each sub-rule body is small enough for the clause
series to be read locally: if the body opens clauses with (a), those are the clauses;
if it goes straight to (i), the drafter used roman numerals for the clause level.

Every provision keeps the address that reaches it — "50(2)(a)(ii)", "44(1)#P1" for a
proviso, "50(9)#E1" for an explanation — so coverage can be measured rather than claimed.
"""
from __future__ import annotations

import re

import pension_rules as pr

ROMAN = {r: i + 1 for i, r in enumerate(
    "i ii iii iv v vi vii viii ix x xi xii xiii xiv xv xvi xvii xviii xix xx".split())}

DIGIT = re.compile(r"\((\d{1,2})\)")
ALPHA = re.compile(r"\(([a-z])\)")
UPPER = re.compile(r"\(([A-Z])\)")
ROM = re.compile(r"\(([ivxl]{1,5})\)")
PROVISO = re.compile(r"Provided (?:further )?that")
EXPL = re.compile(r"Explanation(?:\s*-?\s*\d)?")

REF_CUE = re.compile(
    r"(?:\brule|\brules|\bsub-rule|\bsub-rules|\bclause|\bclauses|\bsub-clause|"
    r"\bsub-clauses|\bitem|\bitems|\bForm|\bFormat|\bparagraph|\bsection|\bentry|"
    r"\bentries|\bcategory|\bExplanation)\s*$", re.I)


def _cued(text, pos, width=34):
    return bool(REF_CUE.search(text[max(0, pos - width):pos]))


def subrule_markers(text):
    """Positions of the sub-rule markers: the bracketed digits running 1, 2, 3 ..."""
    out, expect = [], 1
    for m in DIGIT.finditer(text):
        if _cued(text, m.start()):
            continue
        if int(m.group(1)) != expect:
            continue
        nxt = text[m.end():m.end() + 2]
        if nxt.startswith(")"):
            continue
        out.append((m.start(), m.end(), m.group(1)))
        expect += 1
    return out


def _series(text):
    """Locate the clause series used in this fragment: [(start, end, token)]."""
    # 'i' may be a letter or a roman numeral. Include it here: the run below is
    # accepted only if it opens at (a) and continues without a gap, which a roman
    # series never does.
    alpha = [(m.start(), m.end(), m.group(1)) for m in ALPHA.finditer(text)
             if not _cued(text, m.start())]
    if alpha and alpha[0][2] == "a":
        run, expect = [], "a"
        for pos, end, tok in alpha:
            if tok == expect:
                run.append((pos, end, tok))
                expect = chr(ord(expect) + 1)
        return run, "alpha"
    rom, expect = [], 1
    for m in ROM.finditer(text):
        if _cued(text, m.start()):
            continue
        if ROMAN.get(m.group(1)) == expect:
            rom.append((m.start(), m.end(), m.group(1)))
            expect += 1
    return rom, "roman"


def _carve(text, markers, depth, prefix):
    """Split text at markers, recursing one level down inside each slice."""
    out = []
    lead = text[:markers[0][0]].strip() if markers else text.strip()
    if lead:
        out.append((prefix, depth, lead))
    for i, (start, end, tok) in enumerate(markers):
        stop = markers[i + 1][0] if i + 1 < len(markers) else len(text)
        body = text[end:stop].strip()
        path = f"{prefix}({tok})"
        out.append((path, depth, body))
    return out


def split_rule(num, text):
    """Return [(path, depth, kind, body)] for one rule."""
    subs = subrule_markers(text)
    if not subs:
        return [(str(num), 0, "rule", text.strip())]

    pieces = []
    lead = text[:subs[0][0]].strip()
    if lead:
        pieces.append((str(num), 0, "rule", lead))

    for i, (start, end, tok) in enumerate(subs):
        stop = subs[i + 1][0] if i + 1 < len(subs) else len(text)
        body = text[end:stop].strip()
        base = f"{num}({tok})"
        if not body:
            pieces.append((base, 1, "sub-rule", ""))
            continue
        clauses, series = _series(body)
        if not clauses:
            pieces.append((base, 1, "sub-rule", body))
            continue
        pieces.append((base, 1, "sub-rule", body[:clauses[0][0]].strip()))
        for j, (cs, ce, ctok) in enumerate(clauses):
            cstop = clauses[j + 1][0] if j + 1 < len(clauses) else len(body)
            cbody = body[ce:cstop].strip()
            cpath = f"{base}({ctok})"
            subs2, _ = _series_roman_only(cbody)
            if not subs2:
                pieces.append((cpath, 2, "clause", cbody))
                continue
            pieces.append((cpath, 2, "clause", cbody[:subs2[0][0]].strip()))
            for k, (ss, se, stok) in enumerate(subs2):
                sstop = subs2[k + 1][0] if k + 1 < len(subs2) else len(cbody)
                pieces.append((f"{cpath}({stok})", 3, "sub-clause", cbody[se:sstop].strip()))
    return pieces


def _series_roman_only(text):
    rom, expect = [], 1
    for m in ROM.finditer(text):
        if _cued(text, m.start()):
            continue
        if m.group(1) == "i" and expect == 1:
            rom.append((m.start(), m.end(), "i"))
            expect = 2
            continue
        if ROMAN.get(m.group(1)) == expect:
            rom.append((m.start(), m.end(), m.group(1)))
            expect += 1
    return rom, "roman"


def lift_qualifiers(pieces):
    """Detach provisos and explanations so each can be tested on its own."""
    out = []
    for path, depth, kind, body in pieces:
        cuts = sorted({m.start() for pat in (PROVISO, EXPL) for m in pat.finditer(body)})
        if not cuts:
            out.append(dict(path=path, depth=depth, kind=kind, text=body))
            continue
        head = body[:cuts[0]].strip()
        if head:
            out.append(dict(path=path, depth=depth, kind=kind, text=head))
        np_ = ne = 0
        for j, c in enumerate(cuts):
            frag = body[c:cuts[j + 1] if j + 1 < len(cuts) else len(body)].strip()
            if not frag:
                continue
            if frag.startswith("Provided"):
                np_ += 1
                out.append(dict(path=f"{path}#P{np_}", depth=depth, kind="proviso", text=frag))
            else:
                ne += 1
                out.append(dict(path=f"{path}#E{ne}", depth=depth, kind="explanation", text=frag))
    return out


def build():
    out = []
    for n in range(1, 88):
        for p in lift_qualifiers(split_rule(n, pr.TEXT[str(n)])):
            p["rule"] = n
            out.append(p)
    return out


if __name__ == "__main__":
    from collections import Counter
    ps = build()
    print(f"{len(ps)} provisions from 87 rules")
    for k, v in sorted(Counter(p["kind"] for p in ps).items()):
        print(f"  {k:12} {v}")
    for n in (45, 62):
        print(f"\n---- rule {n}")
        for p in ps:
            if p["rule"] == n:
                print(f"{p['path']:>24} {p['kind']:12} {p['text'][:58]}")
