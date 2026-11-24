#!/usr/bin/env python3
"""engine.py — build questions.json from the authored banks.

Everything in the bank is written by hand, one question at a time. This file does no
generation: it validates what was written, assigns a balanced answer letter, and writes
the records. The old generator that built items by quoting the rule text is gone, and so
is the length-balancing pass that used to paste reasons into the options.
"""
from __future__ import annotations

import json
import pathlib

import authoring
import banks

HERE = pathlib.Path(__file__).parent


def main():
    errs = authoring.validate()
    if errs:
        print(f"AUTHORING ERRORS — {len(errs)}")
        for k, p in errs[:30]:
            print(f"  {k}: {p}")
        raise SystemExit(1)

    recs = authoring.build()
    (HERE / "questions.json").write_text(json.dumps(recs, ensure_ascii=False, indent=1))

    by_ch = {}
    for r in recs:
        by_ch[r["chapter"]] = by_ch.get(r["chapter"], 0) + 1
    print(f"{len(recs)} questions written")
    print("by chapter:", " ".join(f"{k}:{v}" for k, v in sorted(by_ch.items())))

    keys = [r["ans"] for r in recs]
    print("answer key :", " ".join(f"{L}:{keys.count(L)}" for L in "ABCD"))


if __name__ == "__main__":
    main()
