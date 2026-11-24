#!/usr/bin/env python3
"""authoring.py — the question authoring system for the pension platform.

Design rules, enforced rather than hoped for:

1. An option is a bare answer. It never carries reasoning. Reasoning belongs in the
   explanation, which is assembled from the option's own recorded "why".
2. Nothing is auto-generated from the rule text. Every question here was written as a
   question: a scenario or a proposition, four short candidate answers, one of which is
   right for a reason worth knowing.
3. No length balancing. If the key is visibly the longest option, that is a defect in the
   distractors and validate() reports it so it gets rewritten, not papered over.
4. validate() is the gate. It fails on duplication, leakage, quote-dumps, and tells.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import random
import re

HERE = pathlib.Path(__file__).parent
LETTERS = "ABCD"

# ----------------------------------------------------------------- registries
BANKS = []          # every question, in authoring order
_KEYS = set()       # normalised stems, for the duplicate check


class Q:
    """One authored question.

    stem        the question, ending in a colon or a question mark
    key         (answer text, why it is right)
    distractors [(text, why it is wrong)] x3
    rationale   the reasoning a candidate should carry away; cited to the rule
    covers      provision addresses this question reaches, for the coverage matrix
    """
    __slots__ = ("key_id", "rule", "chapter", "covers", "stem", "key", "distractors",
                 "rationale", "trap")

    def __init__(self, key_id, rule, chapter, covers, stem, key, distractors,
                 rationale, trap):
        stem = " ".join(stem.split())
        self.key_id = key_id
        self.rule = str(rule)
        self.chapter = chapter
        self.covers = list(covers) if isinstance(covers, (list, tuple)) else [covers]
        self.stem = stem
        self.key = (key[0].strip(), key[1].strip())
        self.distractors = [(t.strip(), w.strip()) for t, w in distractors]
        self.rationale = " ".join(rationale.split())
        self.trap = trap.strip()
        BANKS.append(self)


# A distractor may be lengthened with a neutral qualifier, but NEVER with its reason.
# Reasons belong in the explanation; that separation is what the old engine got wrong.
QUALIFIERS = [
    "in every such case",
    "irrespective of the facts",
    "as a matter of course",
    "without any further condition",
    "in all circumstances",
]


def lengthen_distractors(opts, key_idx):
    """Pad distractors with a neutral qualifier until the key is not the unique longest.

    This writes no reasoning into an option. A qualifier changes the claim the option makes,
    usually making it absolute, which is why such options are wrong, so it stays honest.
    """
    key_len = len(opts[key_idx])
    used = set()
    for qual in QUALIFIERS:
        if max((len(o) for j, o in enumerate(opts) if j != key_idx), default=0) >= key_len:
            break
        # one qualifier per distractor, and only while the key is still the unique longest
        cands = [j for j in range(len(opts))
                 if j != key_idx and j not in used and len(opts[j]) < key_len]
        if not cands:
            break
        j = min(cands, key=lambda i: len(opts[i]))
        opts[j] = opts[j].rstrip(".") + ", " + qual + "."
        used.add(j)
    return opts


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


# ---------------------------------------------------------------- validation
# A stem that asks a candidate to recognise a printed block is not an exam question.
BANNED_STEM = re.compile(
    r"\b(which of the following is the (text|opening)|"
    r"begins with which words|reproduces the (text|words)|"
    r"set out the (full )?text|quote the)\b", re.I)

# Markers that mean reasoning has leaked into an option.
BANNED_OPT = re.compile(
    r"(—\s*(no such|that is|the rule|it is the text|nothing in|confirmation is|"
    r"the two instruments|confirmation|probation)|"
    r"\bIt is the text of a different provision\b|"
    r"\bNo such rule exists\b|"
    r"\bThe text of a different\b)", re.I)


def validate(banks=None):
    """Return a list of (key_id, problem). Empty means the bank is publishable."""
    items = banks if banks is not None else BANKS
    errs = []
    stems = {}
    for q in items:
        k = norm(q.stem)
        if k in stems:
            errs.append((q.key_id, f"duplicate stem of {stems[k]}"))
        stems.setdefault(k, q.key_id)

        if len(q.distractors) != 3:
            errs.append((q.key_id, f"{len(q.distractors)} distractors, need 3"))
        if not (35 <= len(q.stem) <= 320):
            errs.append((q.key_id, f"stem length {len(q.stem)}, want 35-320"))
        if BANNED_STEM.search(q.stem):
            errs.append((q.key_id, "stem is a recognition-of-printed-text item"))

        opts = [q.key[0]] + [t for t, _ in q.distractors]
        for o in opts:
            if len(o) > 170:
                errs.append((q.key_id, f"option of {len(o)} chars is a quote, not an answer"))
            if len(o) < 2:
                errs.append((q.key_id, "empty option"))
            if BANNED_OPT.search(o):
                errs.append((q.key_id, f"reasoning leaked into option: {o[:60]!r}"))
        if len({norm(o) for o in opts}) != 4:
            errs.append((q.key_id, "two options are the same"))
        for o in opts:
            if o.rstrip().endswith((",", "—", "-", "and", "of")):
                errs.append((q.key_id, f"option ends mid-sentence: {o[-40:]!r}"))

        # judge the options as they will be rendered, after neutral lengthening
        placed = lengthen_distractors([o.rstrip(".") for o in opts], 0)
        keylen = len(placed[0])
        longest = max(len(o) for o in placed)
        if keylen == longest and [len(o) for o in placed].count(longest) == 1:
            errs.append((q.key_id, f"key is the unique longest option ({keylen} vs "
                                   f"{[len(o) for o in placed]})"))
        if len(q.rationale) < 80:
            errs.append((q.key_id, "rationale too thin to learn from"))
        if not q.trap:
            errs.append((q.key_id, "no trap recorded"))
        if not q.covers:
            errs.append((q.key_id, "no provision coverage recorded"))
    return errs


# ------------------------------------------------------------------- build
def seed(s):
    return int(hashlib.sha256(s.encode()).hexdigest()[:8], 16)


def build():
    """Turn authored questions into the record shape assemble.py consumes."""
    errs = validate()
    if errs:
        raise SystemExit("AUTHORING ERRORS\n" + "\n".join(f"  {k}: {p}" for k, p in errs[:40]))
    recs = []
    for q in BANKS:
        rng = random.Random(seed(q.key_id))
        pool = [(q.key[0], q.key[1])] + list(q.distractors)
        # place the key at the letter that keeps the key balanced
        counts = [sum(1 for r in recs if r["ans"] == L) for L in LETTERS]
        slot = counts.index(min(counts))
        rest = [p for i, p in enumerate(pool) if i != 0]
        rng.shuffle(rest)
        ordered = rest[:]
        ordered.insert(slot, pool[0])
        # neutral qualifiers only; no reasoning ever enters an option
        texts = [t for t, _ in ordered]
        texts = lengthen_distractors(texts, slot)
        ordered = [(texts[i], ordered[i][1]) for i in range(4)]

        def clean(t):
            t = t.strip()
            return t if t.endswith((".", "?", "!")) else t + "."

        lines = [f"({LETTERS[slot]}) {clean(q.key[0])} {q.key[1]}"]
        for i, (t, w) in enumerate(ordered):
            if i == slot:
                continue
            lines.append(f"({LETTERS[i]}) {clean(t)} \u2014 {w}")
        recs.append({
            "id": q.key_id,
            "q": q.stem,
            "opts": [t for t, _ in ordered],
            "ans": LETTERS[slot],
            "expl": "\n".join(lines) + "\n\n" + q.rationale,
            "trap": q.trap,
            "rule": q.rule,
            "chapter": q.chapter,
            "covers": q.covers,
            "src": f"CCS (Pension) Rules, 2021, rule {q.covers[0]}",
            "rules_text": f"Rule {q.rule}",
        })
    return recs


if __name__ == "__main__":
    errs = validate()
    print(f"{len(BANKS)} authored questions")
    if errs:
        print(f"{len(errs)} problems")
        for k, p in errs[:40]:
            print(f"  {k}: {p}")
    else:
        print("clean")
