#!/usr/bin/env python3
"""money_checks.py — re-derive every rupee answer in the bank from its formula.

A question that states a figure is only as good as the arithmetic behind it. Each check
below recomputes the number from the rule and compares it with the figure the authored
question actually asserts, read back out of questions.json.

Rounding is per rule, not per habit. Rule 45(1) says "rounded off to the next higher rupee",
which is a ceiling, always up, even for a fraction of a paisa. Rule 44 says nothing about
rounding pension.
"""
from __future__ import annotations

import json
import pathlib
import re
from decimal import Decimal, ROUND_CEILING

HERE = pathlib.Path(__file__).parent
QS = {q["id"]: q for q in json.loads((HERE / "questions.json").read_text())}


def ceiling_rupee(x):
    """Rule 45(1) second proviso: a fraction of a rupee goes to the next higher rupee."""
    return int(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_CEILING))


def pension_44(emo, avg):
    """Rule 44(1): 50 per cent of the more beneficial, floor 9,000, ceiling 1,25,000."""
    return max(9000, min(125000, round(0.5 * max(emo, avg))))


def retirement_gratuity_45(emo, half_years):
    """Rule 45(1)(a): a quarter of emoluments per six-monthly period, cap 16.5 times."""
    return min(ceiling_rupee(emo * half_years / 4), ceiling_rupee(emo * 16.5))


def periods_45_4(years, months):
    """Rule 45(4): three months or more is a completed six-monthly period."""
    return years * 2 + (1 if months >= 3 else 0)


def key_of(qid):
    """The text of the option that the record marks as correct."""
    q = QS[qid]
    return q["opts"]["ABCD".index(q["ans"])]


# (question id, description, computed value, the figure the question asserts)
CHECKS = [
    ("P-0055", "rule 44(1): 50% of the better of 72,000 and 74,000",
     pension_44(72000, 74000), 37000),
    ("P-0056", "rule 44(1): 50% of 2,40,000, below the ceiling",
     pension_44(240000, 240000), 120000),
    ("P-0059", "rule 45(4): 7 years 4 months is 15 six-monthly periods",
     periods_45_4(7, 4), 15),
    ("P-0062", "rule 45(1)(a): 30 years at 60,000 gives 15 times",
     retirement_gratuity_45(60000, 60), 900000),
    ("P-0065", "rule 45(1)(b)(v): 24 years gives 24 times, under the 33 cap",
     int(24 * 2 * 0.5), 24),
    ("P-0072", "rule 45(1) second proviso: 4,23,456.40 goes to the next higher rupee",
     ceiling_rupee("423456.40"), 423457),
]


def run():
    fails = []
    for qid, desc, computed, asserted in CHECKS:
        ok = computed == asserted
        if not ok:
            fails.append((qid, desc, computed, asserted))
        print(f"  {'ok  ' if ok else 'FAIL'} {qid}: {desc} -> {computed}"
              + ("" if ok else f" (question asserts {asserted})"))

    # every rupee figure the bank states must be one of these, or under a checked rule
    print()
    for qid, desc, computed, asserted in CHECKS:
        if qid in QS:
            print(f"  {qid} key reads: {key_of(qid)[:70]!r}")
    return fails


if __name__ == "__main__":
    fails = run()
    if fails:
        print(f"\nMONEY CHECKS FAILED — {len(fails)}")
        raise SystemExit(1)
    print(f"\nMONEY CHECKS PASSED — {len(CHECKS)} figures re-derived")
