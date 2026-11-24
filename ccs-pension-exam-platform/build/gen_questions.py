#!/usr/bin/env python3
"""gen_questions.py — deterministic questions derived from each provision's own text.

The hand-written facts answer the question the examiner asks. These answer a narrower
one that the audit can check without a human: does the platform contain a question
whose answer is this provision? The generator sits on top of provisions.py, so a
provision is reached only if the parser found it, and a clause that is missing from
the transcription produces no question — which is how the rule 50 gap surfaced.
"""
from __future__ import annotations

import re

import provisions as pv

CHAPTER_OF = {}
CHAPTERS = [
    ("I", 1, 4), ("II", 5, 10), ("III", 11, 30), ("IV", 31, 32), ("V", 33, 41),
    ("VI", 42, 43), ("VII", 44, 49), ("VIII", 50, 51), ("IX", 52, 52),
    ("X", 53, 70), ("XI", 71, 78), ("XII", 79, 80), ("XIII", 81, 84), ("XIV", 85, 87),
]
for _c, _lo, _hi in CHAPTERS:
    for _n in range(_lo, _hi + 1):
        CHAPTER_OF[_n] = _c

# fragments that carry no testable proposition on their own
STOP = re.compile(
    r"^(and|or|namely|as the case may be|if any|where applicable|whichever is (?:earlier|later|less)|"
    r"as applicable|if applicable)$", re.I)

BREAK = re.compile(r"\s*[:\u2014]\s*$")


def _clean(t: str) -> str:
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"^(?:and|or)\s+", "", t, flags=re.I)
    return t


def _fallback_stem(path: str, kind: str) -> str:
    """A stem for a provision whose text is carried entirely by its children."""
    if kind == "sub-rule" and "(" in path:
        n, rest = path.split("(", 1)
        return f"Rule {n} is set out in numbered paragraphs. Which of the following is the opening of sub-rule ({rest.rstrip(')')}) of rule {n}?"
    return f"Which of the following is the text of {describe(path)}?"


KIND_WORD = {
    "rule": "rule", "sub-rule": "sub-rule", "clause": "clause",
    "sub-clause": "sub-clause", "proviso": "proviso", "explanation": "Explanation",
}


def describe(path: str) -> str:
    """Turn 50(9)(h)(iii) into 'clause (iii) of clause (h) of sub-rule (9) of rule 50'."""
    if "#P" in path:
        base, suf = path.split("#P")
        return f"the {'second ' if suf == '2' else ''}proviso to {describe(base)}"
    if "#E" in path:
        base, suf = path.split("#E")
        return f"Explanation {suf} to {describe(base)}"
    m = re.match(r"^(\d+)((?:\([^)]*\))*)$", path)
    if not m:
        return path
    rule, rest = m.group(1), m.group(2)
    toks = re.findall(r"\(([^)]*)\)", rest)
    if not toks:
        return f"rule {rule}"
    words = ["sub-rule", "clause", "sub-clause", "item"]
    parts = []
    for i, t in enumerate(toks):
        w = words[min(i, 3)]
        parts.append(f"{w} ({t})")
    return ", ".join(parts[1:] + [parts[0]]).replace(", ", " of ") + f" of rule {rule}"


def _kind(path: str) -> str:
    if "#P" in path:
        return "proviso"
    if "#E" in path:
        return "explanation"
    depth = path.count("(")
    return {0: "rule", 1: "sub-rule", 2: "clause", 3: "sub-clause"}.get(depth, "item")


def provision_stem(path: str, text: str) -> str:
    k = _kind(path)
    d = describe(path)
    body = _clean(text)
    if k == "proviso":
        return f"Which of the following is the text of {d}?"
    if k == "explanation":
        return f"Which of the following is the text of {d}?"
    if re.match(r"^(where|if|in case|when|subject to|nothing|no |every|any )", body, re.I):
        return f"{d[0].upper() + d[1:]} of the CCS (Pension) Rules, 2021 begins with which words?"
    return f"Which of the following is the text of {d}?"


OPEN = re.compile(r"(?<=[.;])\s+(?=[A-Z(])")


def opening(text: str, limit=300):
    """The opening sentence of a long provision, cut at a sentence boundary."""
    text = _clean(text)
    if len(text) <= limit:
        return text
    for m in OPEN.finditer(text):
        if m.start() >= 80:
            return text[:m.start()].strip()
    return text[:limit].rsplit(" ", 1)[0].strip()


def collect(limit_chars=340, min_chars=40):
    """Provisions that can carry a text-recognition question on their own text."""
    out = []
    for p in pv.build():
        text = _clean(p["text"])
        if len(text) < min_chars or len(text) > limit_chars:
            continue
        if STOP.match(text):
            continue
        if BREAK.search(text):
            continue
        out.append((p["path"], text))
    return out


def _distractor_pool():
    """Texts that are real provisions, used as wrong answers."""
    return collect(limit_chars=400, min_chars=30)


def long_facts():
    """Provisions too long to offer whole, asked by their opening words instead."""
    from provisions import build as build_all
    provs = [p for p in build_all() if p["path"][0].isdigit()]
    pool = []
    for p in provs:
        t = _clean(p["text"])
        if len(t) > 340:
            o = opening(t)
            if len(o) >= 60:
                pool.append((p["path"], o))
    texts = [t for _, t in pool]
    out = []
    for i, (path, text) in enumerate(pool):
        rule_no = int(re.match(r"(\d+)", path).group(1))
        head = " ".join(text.split()[:5]).lower()
        picks, j = [], 0
        while len(picks) < 3 and j < len(texts):
            cand = texts[(i * 11 + j * 37 + 5) % len(texts)]
            j += 1
            if cand == text or " ".join(cand.split()[:5]).lower() == head or cand in picks:
                continue
            picks.append(cand)
        if len(picks) < 3:
            continue
        out.append(dict(
            id=f"TX-{1000 + i:04d}", ch=CHAPTER_OF.get(rule_no, "I"), rule=str(rule_no),
            rules_text=f"Rule {rule_no} \u00b7 {path}",
            topic=describe(path).capitalize(),
            q=f"Which of the following is the opening of {describe(path)}?",
            a=text,
            d=[(x, "These are the opening words of a different provision of the same rules.") for x in picks],
            why="The answer is the provision's own opening words, cut at a sentence boundary. The other options "
                "are the opening words of other provisions, so the question tests recall of how this provision begins.",
            safe=f"{describe(path)} opens in these words.",
            src=f"{describe(path).capitalize()}, CCS (Pension) Rules, 2021",
            trap="Matching the tone of the statute rather than the provision",
            kind="TEXT", tag="Standard", covers=[path],
        ))
    return out


def facts():
    """One text-recognition question per eligible provision, plus the fallback stems."""
    pool = _distractor_pool()
    texts = [t for _, t in pool]
    out = []
    seen = set()
    for i, (path, text) in enumerate(collect()):
        if not path[0].isdigit():
            continue
        rule_no = int(re.match(r"(\d+)", path).group(1))
        ch = CHAPTER_OF.get(rule_no, "I")
        fid = f"TX-{i + 1:04d}"
        # distractors: three other real provisions, chosen so that none shares the opening
        # words of the key, which would make the answer ambiguous
        head = " ".join(text.split()[:4]).lower()
        picks, j = [], 0
        while len(picks) < 3 and j < len(texts):
            cand = texts[(i * 7 + j * 31 + 11) % len(texts)]
            j += 1
            if cand == text or " ".join(cand.split()[:4]).lower() == head:
                continue
            if cand in picks:
                continue
            picks.append(cand)
        if len(picks) < 3:
            continue
        stem = provision_stem(path, text)
        if stem in seen:
            continue
        seen.add(stem)
        out.append(dict(
            id=fid, ch=ch, rule=str(rule_no),
            rules_text=f"Rule {rule_no}" + ("" if path == str(rule_no) else " · " + path),
            topic=describe(path).capitalize(),
            q=stem, a=text,
            d=[(x, "It is the text of a different provision of these rules.") for x in picks],
            why=("The answer reproduces the provision as notified. The three wrong options are other provisions "
                 "of the same rules, so the question tests recall of this provision rather than recognition of "
                 "the statute's style."),
            safe=f"{describe(path)} of rule {rule_no}, in its own words.",
            src=f"{describe(path).capitalize()}, CCS (Pension) Rules, 2021",
            trap="Recognising the text of a neighbouring provision instead of this one",
            kind="TEXT", tag="Standard", covers=[path],
        ))
    return out


if __name__ == "__main__":
    got = collect()
    print(f"{len(got)} provisions can carry a text question")
    print()
    for path, text in got[:6]:
        print(describe(path))
        print("   ", provision_stem(path, text))
        print("   ", text[:110])
        print()
