#!/usr/bin/env python3
"""xrefs.py — resolve every internal cross-reference the Rules make.

The Rules cite themselves constantly: "clause (e) of sub-rule (9)", "sub-rule (4) of
rule 62", "rules 46, 47, 48". Each citation is a claim that a provision exists. If a
citation does not resolve against the parsed inventory, either the parser is wrong or
the transcription is short of text — and either way the platform would be teaching from
an incomplete rule. This module turns those claims into a test.
"""
from __future__ import annotations

import re

import pension_rules as pr
import provisions as pv

NUMWORDS = {w: i + 1 for i, w in enumerate(
    "one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
    "fifteen sixteen seventeen eighteen nineteen twenty".split())}


def _expand_list(text):
    """'rules 46, 47 and 48' -> ['46','47','48']; 'rules 57 and 58' -> ['57','58']"""
    out = []
    for part in re.split(r",|\band\b", text):
        part = part.strip()
        m = re.match(r"^(\d{1,3})$", part)
        if m:
            out.append(m.group(1))
    return out


PAT_SUBRULE_OF_RULE = re.compile(r"sub-rules?\s*\((\w{1,4})\)\s*of\s*(?:the\s*)?rule\s*(\d{1,3})")
PAT_CLAUSE_OF_SUBRULE_OF_RULE = re.compile(
    r"clauses?\s*\((\w{1,4})\)\s*of\s*sub-rule\s*\((\w{1,4})\)\s*of\s*(?:the\s*)?rule\s*(\d{1,3})")
PAT_CLAUSE_OF_SUBRULE_HERE = re.compile(r"clauses?\s*\((\w{1,4})\)\s*of\s*sub-rule\s*\((\w{1,4})\)")
PAT_CLAUSE_OF_RULE = re.compile(r"clauses?\s*\((\w{1,4})\)\s*of\s*(?:the\s*)?rule\s*(\d{1,3})")
PAT_SUBCLAUSE = re.compile(r"sub-clauses?\s*\((\w{1,4})\)")
PAT_RULES = re.compile(r"\brules?\s*(\d{1,3}(?:\s*(?:,|and|or)\s*\d{1,3})*)")
PAT_SUBRULE_HERE = re.compile(r"(?<!of )sub-rules?\s*\((\w{1,4})\)")


def citations(text, owner=None):
    """Every citation in one provision, as (offset, address) claims to be resolved.

    A citation naming its own rule is resolved against that rule. A citation that
    names no rule ("sub-rule (2)") can only mean the rule the text sits in, so it is
    attributed to the owner. Getting that direction wrong is what makes a resolver
    report faults that are not there, so the rule-naming forms are tried first and
    their spans are then excluded from the bare forms.
    """
    out, consumed = [], []

    def span(a, b):
        consumed.append((a, b))
        return any(a < y and x < b for x, y in consumed[:-1])

    for m in PAT_CLAUSE_OF_SUBRULE_OF_RULE.finditer(text):
        out.append((m.start(), f"{m.group(3)}({m.group(2)})({m.group(1)})"))
        span(m.start(), m.end())
    for m in PAT_SUBRULE_OF_RULE.finditer(text):
        out.append((m.start(), f"{m.group(2)}({m.group(1)})"))
        span(m.start(), m.end())
    for m in PAT_CLAUSE_OF_RULE.finditer(text):
        out.append((m.start(), f"{m.group(2)}({m.group(1)})"))
        span(m.start(), m.end())
    for m in PAT_RULES.finditer(text):
        for n in _expand_list(m.group(1)):
            out.append((m.start(), n))
        span(m.start(), m.end())
    if owner:
        for m in PAT_CLAUSE_OF_SUBRULE_HERE.finditer(text):
            if span(m.start(), m.end()):
                continue
            out.append((m.start(), f"{owner}({m.group(2)})({m.group(1)})"))
        for m in PAT_SUBRULE_HERE.finditer(text):
            if span(m.start(), m.end()):
                continue
            out.append((m.start(), f"{owner}({m.group(1)})"))
        for m in PAT_SUBCLAUSE.finditer(text):
            if span(m.start(), m.end()):
                continue
            out.append((m.start(), f"{owner}~sc({m.group(1)})"))
    return sorted(out)


def inventory():
    provs = pv.build()
    have = {p["path"] for p in provs}
    # a citation to a clause only needs the clause address to exist
    return provs, have


# Citations that point at a provision the statute does not contain. These are defects in the
# gazette, not in the transcription: each one was checked against the published rule text.
# The audit fails on any unresolved citation that is not listed here, so a transcription gap
# shows up as an error while a known defect in the instrument stays visible but does not.
KNOWN_DEFECTS = {
    # r8(4)(d) refers to sub-rule (9) of rule 8, but rule 8 has only sub-rules (1) to (8).
    ("8(4)(d)", "8(9)"): "rule 8 ends at sub-rule (8); the reference is to sub-rule (4) or is a "
                         "carry-over from the 1972 Rules, where the corresponding provision sat in sub-rule (9)",
    # r65(5)(d) and (e) refer to clause (c) of sub-rule (5) of rule 8; rule 8(5) has no clauses.
    ("65(5)(d)", "8(5)(c)"): "rule 8(5) is a single sentence without clauses; the clause letter is a "
                             "carry-over from the 1972 Rules",
    ("65(5)(e)", "8(5)(c)"): "rule 8(5) is a single sentence without clauses; the clause letter is a "
                             "carry-over from the 1972 Rules",
    # r76(5)(e) uses the withholding power in r77(1), which is a single unlettered sub-rule.
    ("76(5)(e)", "77(1)(b)"): "rule 77(1) has clauses (i) to (x), not (a) and (b); the withholding is "
                              "done under clause (vi) of rule 77(1)",
    # r81(2) refers to rule 76(2)(d); rule 76(2) has no clauses.
    ("81(2)", "76(2)(d)"): "rule 76(2) is a single paragraph without clauses",
}


def unresolved(include_known=True):
    provs, have = inventory()
    bad = []
    for p in provs:
        for pos, target in citations(p["text"], owner=p["rule"]):
            if "~sc(" in target:
                continue
            if target in have:
                continue
            if target.isdigit() and 1 <= int(target) <= 87:
                continue
            if any(h.startswith(target + "(") or h.startswith(target + "#") for h in have):
                continue
            if not include_known and (p["path"], target) in KNOWN_DEFECTS:
                continue
            bad.append((p["path"], target, p["text"][max(0, pos - 70):pos + 40]))
    return bad


def unknown():
    """Unresolved citations that are not on the known-defect list. This must be empty."""
    return [b for b in unresolved() if (b[0], b[1]) not in KNOWN_DEFECTS]


if __name__ == "__main__":
    provs, have = inventory()
    print(f"inventory: {len(provs)} provisions, {len(have)} distinct addresses\n")
    bad = unresolved()
    print(f"known defects in the instrument: {len(KNOWN_DEFECTS)}\n")
    seen = set()
    for src, target, ctx in bad:
        key = (src, target)
        if key in seen:
            continue
        seen.add(key)
        flat = re.sub(r"\s+", " ", ctx)[:96]
        print(f"{src:>16} -> {target:<14} {flat}")
    print(f"\n{len(seen)} unresolved cross-references")
