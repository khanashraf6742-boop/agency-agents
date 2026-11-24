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


# ---------------------------------------------------------------------------- the closed whitelist
#
# These five citations point at provisions the statute does not contain. They are defects in the
# gazette, not in the transcription: each was checked against the published rule text, and the
# wording quoted against each entry is verbatim from it.
#
# THIS IS A CLOSED LIST. unresolved() fails on any citation that is not an exact
# (source provision, target address) match for an entry here, so a transcription gap cannot be
# excused as "probably another statute defect". The list may shrink; it may not grow without
# re-reading the gazette. If an amendment corrects one of these references, delete the entry and
# the audit tightens automatically - audit.py asserts that every entry still occurs, so a stale
# entry fails the build rather than sitting here forever.
KNOWN_DEFECTS = {
    ("8(4)(d)", "8(9)"): {
        "quote": "deemed to have been instituted in accordance with sub-rule (9) till the date of retirement",
        "reason": "Rule 8 contains only sub-rules (1) to (8); there is no sub-rule (9) for proceedings "
                  "to be instituted under. The drafter has used a sub-rule number the target provision "
                  "does not have.",
    },
    ("65(5)(d)", "8(5)(c)"): {
        "quote": "retirement gratuity was not paid on retirement in accordance with clause (c) of "
                 "sub-rule (5) of rule 8",
        "reason": "Rule 8(5) is a single unbroken sentence - it is not divided into clauses - so there "
                  "is no clause (c). The drafter has used a clause label the target provision does not "
                  "support.",
    },
    ("65(5)(e)", "8(5)(c)"): {
        "quote": "gratuity was not paid on retirement in accordance with clause (c) of sub-rule (5) "
                 "of rule 8",
        "reason": "The same defect as rule 65(5)(d), repeated verbatim in the adjacent clause: rule "
                  "8(5) has no clauses.",
    },
    ("76(5)(e)", "77(1)(b)"): {
        "quote": "The amount of gratuity withheld under clause (b) of sub-rule (1) of rule 77",
        "reason": "Rule 77(1) is lettered (i) to (x), not (a), (b), (c), so there is no clause (b) of "
                  "rule 77(1). The withholding the drafter means is done under clause (vi) of rule "
                  "77(1), which withholds ten per cent pending intimation from the Directorate of "
                  "Estates. The same sentence also cites clause (viii) of rule 77(1), which does "
                  "exist - only the (b) reference is defective.",
    },
    ("81(2)", "76(2)(d)"): {
        "quote": "Subject to provisions of clause (d) of sub-rule (2) of rule 76",
        "reason": "Rule 76(2) is a single paragraph - it is not divided into lettered clauses - so "
                  "there is no clause (d). The drafter has used a clause label the target provision "
                  "does not have.",
    },
}


def unresolved(include_known=True):
    """Citations that name an address the statute does not contain.

    Resolution is exact. There is deliberately no lenient fallback of the kind that would accept
    an address merely because some provision begins with its prefix: leniency in a resolver is
    indistinguishable from a blind spot, and the whole point of this check is that a gap surfaces.
    """
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
            bad.append((p["path"], target, p["text"][max(0, pos - 70):pos + 40]))
    if include_known:
        return bad
    return [b for b in bad if (b[0], b[1]) not in KNOWN_DEFECTS]


def unknown():
    """Unresolved citations that are NOT one of the five enumerated statute defects.

    This is the control. It must be empty, and the audit fails if it is not: any entry here is a
    candidate transcription gap and has to be investigated, not whitelisted.
    """
    return unresolved(include_known=False)


def defect_occurrences():
    """Every occurrence of a whitelisted defect, with the exact span it sits in.

    Keyed by (source, target) an entry can hide a provision that cites the defect in several
    places; counting occurrences keeps the documentation honest about how often the statute
    repeats each one.
    """
    provs, have = inventory()
    seen = {}
    for p in provs:
        for pos, target in citations(p["text"], owner=p["rule"]):
            key = (p["path"], target)
            if key in KNOWN_DEFECTS:
                seen.setdefault(key, []).append((pos, p["text"][max(0, pos - 110):pos + 90]))
    return seen


def defects():
    """The whitelist, with how many times each defective reference actually occurs."""
    occ = defect_occurrences()
    out = []
    for key, meta in KNOWN_DEFECTS.items():
        out.append({"source": key[0], "target": key[1],
                    "occurrences": len(occ.get(key, [])),
                    "quote": meta["quote"], "reason": meta["reason"]})
    return sorted(out, key=lambda d: (int(d["source"].split("(")[0]), d["source"]))


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
