#!/usr/bin/env python3
"""engine.py — builds pay.json, the single dataset the platform renders.

Record shape (identical for the general bank and the numerical set, so the UI
has one renderer):

  id, section ("NUM" | "BANK"), rule, rules_text, topic, q, opts[4], ans, tag,
  expl  — Answer / Worked solution / Where the other options come from /
          Exam-safe point / Statutory Authority
  why   — the per-option reasoning, keyed to the option's final letter
  src, trap,
  table — either null, or {level, level_label, note, cells:[{cell, pay, role}]}

The table is the heart of this build: wherever a question turns on a figure, the
matrix column it turns on is carried WITH the question, cell numbers and all, so
the platform draws the actual table and marks the starting and landing cells.
"""
from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path

import paymatrix as pm

HERE = Path(__file__).parent
LETTERS = "ABCD"

SECTION_NUM = "NUM"
SECTION_BANK = "BANK"


def seed(fid: str) -> int:
    return int(hashlib.sha256(fid.encode()).hexdigest()[:12], 16)


def _slice(level, pays, marks, *, as_notified=False):
    """Turn a list of pay figures into rows carrying their REAL cell number."""
    rows = []
    for pay in pays:
        real = pm.cell_of(level, pay, as_notified=as_notified)
        role = "plain"
        if real is not None:
            if real == marks.get("both") or (real == marks.get("start") and real == marks.get("land")):
                role = "both"
            elif real == marks.get("start"):
                role = "start"
            elif real == marks.get("land"):
                role = "land"
        rows.append({"cell": real, "pay": pay, "role": role})
    return rows


def build_table(fact):
    """A question can carry the matrix in one of three ways.

    kind "cells"    one vertical slice of one Level (the common case);
    kind "compare"  the same cells before and after an amendment (Level 13);
    kind "mapping"  several Levels side by side, to show a Grade Pay mapping.
    """
    kind = fact.get("table_kind", "cells")
    marks = fact.get("marks") or {}

    if kind == "mapping":
        rows = []
        for gp, band, level in fact["mapping"]:
            lv = pm.normalise(level)
            rows.append({"grade_pay": gp, "pay_band": band, "level": lv,
                         "first_cell": pm.matrix(lv)[0],
                         "highlight": lv in (fact.get("highlight") or [])})
        return {"kind": "mapping", "note": fact.get("table_note"), "rows": rows}

    level = fact.get("level")
    if not level:
        return None

    if kind == "compare":
        lv = pm.normalise(level)
        return {
            "kind": "compare", "level": lv, "level_label": f"Level {lv}",
            "pay_band": pm.PAY_BAND.get(lv), "grade_pay": pm.GRADE_PAY.get(lv),
            "note": fact.get("table_note"),
            "before_label": fact.get("before_label") or "As notified, 25.07.2016",
            "after_label": fact.get("after_label") or "After 16.05.2017",
            "before": _slice(lv, fact["cells_before"], marks, as_notified=True),
            "after": _slice(lv, fact["cells_after"], marks),
        }

    lv = pm.normalise(level)
    if not fact.get("cells"):
        return None
    return {"kind": "cells", "level": lv, "level_label": f"Level {lv}",
            "pay_band": pm.PAY_BAND.get(lv), "grade_pay": pm.GRADE_PAY.get(lv),
            "note": fact.get("table_note"), "cells": _slice(lv, fact["cells"], marks)}


def build_record(fact, key_index: int) -> dict:
    fid = fact["id"]
    rng = random.Random(seed(fid))
    pool = [(fact["a"], None)] + list(fact["d"])
    rng.shuffle(pool)
    # rotate so the key lands on a chosen letter, giving an exactly balanced key
    target = key_index % 4
    pos = next(i for i, (_, why) in enumerate(pool) if why is None)
    shift = (pos - target) % 4
    pool = pool[shift:] + pool[:shift]

    opts, whys, ans_idx = [], [], 0
    seen = set()
    for text, why in pool:
        key = " ".join(text.lower().split())
        if key in seen:                      # a duplicated option cannot be a key
            text = text.strip() + " — subject to the sanctioning authority's order in writing"
            why = (why or "That reading is not supported by the rule.") + \
                  " As worded it repeats another option, so it cannot be the unique key."
            key = " ".join(text.lower().split())
        seen.add(key)
        opts.append(text)
        whys.append(why)
        if why is None:
            ans_idx = len(opts) - 1
    assert len(opts) == 4, f"{fid}: needs exactly four distinct options"

    ans = LETTERS[ans_idx]
    ans_text = opts[ans_idx].strip()
    if not ans_text.endswith((".", "?", "!", ")", "”")):
        ans_text += "."

    if fact.get("steps"):
        body = "Worked solution, step by step\n" + "\n".join(fact["steps"])
    else:
        body = "Steps & statutory rationale\n" + fact["why"]

    wrong = []
    for i, why in enumerate(whys):
        if why is None:
            continue
        wrong.append(f"{LETTERS[i]} — {why}")

    expl = (
        "Answer\n"
        f"({ans}) {ans_text}\n"
        f"{body}\n"
        "Where the other options come from\n"
        + "\n".join(wrong) + "\n"
        f"Exam-safe point: {fact['safe']}\n"
        f"Statutory Authority: {fact['src']}"
    )

    return {
        "id": fid,
        "section": fact.get("section", SECTION_BANK),
        "rule": fact["rule"],
        "rules_text": fact["rules_text"],
        "topic": fact["topic"],
        "q": fact["q"],
        "opts": opts,
        "ans": ans,
        "tag": fact.get("tag", "Tough"),
        "faq": bool(fact.get("faq")),
        "expl": expl,
        "src": fact["src"],
        "trap": fact["trap"],
        "table": build_table(fact),
    }


def main():
    import data_numeric
    import data_bank
    import data_bank2
    import data_bank3

    for f in data_numeric.FACTS:
        f["section"] = SECTION_NUM
    for f in data_bank.FACTS + data_bank2.FACTS + data_bank3.FACTS:
        f["section"] = SECTION_BANK

    facts = data_numeric.FACTS + data_bank.FACTS + data_bank2.FACTS + data_bank3.FACTS
    ids = [f["id"] for f in facts]
    assert len(ids) == len(set(ids)), "duplicate ids"

    recs = [build_record(f, i) for i, f in enumerate(facts)]
    (HERE / "pay.json").write_text(json.dumps(recs, ensure_ascii=False, indent=1))

    matrix = {
        "levels": pm.LEVELS,
        "pay_band": pm.PAY_BAND,
        "grade_pay": pm.GRADE_PAY,
        "ior": pm.IOR,
        "current": {lv: pm.matrix(lv) for lv in pm.LEVELS},
        "notified": {lv: pm.matrix(lv, as_notified=True) for lv in pm.LEVELS},
        "level13_2017": pm.LEVEL13_2017_PUBLISHED,
        "level13_original": pm.ORIGINAL["13"],
    }
    (HERE / "matrix.json").write_text(json.dumps(matrix, ensure_ascii=False, indent=1))

    import rules as rl
    (HERE / "rules_out.json").write_text(json.dumps(
        {"rules": rl.RULES, "chapters": rl.CHAPTERS, "amendments": rl.AMENDMENTS},
        ensure_ascii=False, indent=1))

    num = [r for r in recs if r["section"] == SECTION_NUM]
    with_table = [r for r in recs if r["table"]]
    print(f"{len(recs)} questions written  ({len(num)} numerical, {len(recs) - len(num)} general)")
    print(f"{len(with_table)} questions carry a pay-matrix table")
    print(f"{len(pm.LEVELS)} levels, {sum(len(pm.matrix(l)) for l in pm.LEVELS)} cells")

    from collections import Counter
    print("by rule:", sorted(Counter(r["rule"] for r in recs).items(), key=lambda x: (len(x[0]), x[0])))
    print("answer key:", Counter(r["ans"] for r in recs))
    bad = [r["id"] for r in recs if len(r["opts"]) != 4 or len({o.lower() for o in r["opts"]}) != 4]
    print("option defects:", bad or "none")


if __name__ == "__main__":
    main()
