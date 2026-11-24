#!/usr/bin/env python3
"""engine.py — build the question records for the pension platform.

A fact is written as key + three distractors + the reasoning. The engine places
the key at a chosen letter so the answer key stays balanced, and assembles the
explanation in the same five-line shape the pay and leave platforms use:
Answer / why each distractor fails / steps & rationale / exam-safe point / authority.
"""
from __future__ import annotations

import json
import pathlib
import random

HERE = pathlib.Path(__file__).parent
LETTERS = "ABCD"


def seed(s: str) -> int:
    return sum((i + 1) * ord(c) for i, c in enumerate(s))


# A key that is visibly the longest option gives the answer away. Where the reasoning in
# the fact file has already explained why each distractor fails, the engine may append
# that reasoning to the distractor itself, which lengthens it honestly rather than padding
# it. The explanation keeps the same text, so nothing new is asserted.
MAX_EXTEND = 3


def balance_lengths(pool, ans_idx: int):
    """Lengthen distractors, never the key, until the key is not the unique longest.

    Appending a distractor's own recorded reason is a fair way to lengthen it: the
    reason is why the option is wrong, so attributing it to the option is correct.
    """
    texts = [t for t, _ in pool]
    whys = [w for _, w in pool]
    key_len = len(texts[ans_idx])
    others = sorted((i for i in range(4) if i != ans_idx), key=lambda i: len(texts[i]))
    for i in others:
        if not whys[i] or len(texts[i]) >= key_len:
            continue
        addition = " \u2014 " + whys[i].rstrip(".")
        if len(texts[i]) + len(addition) <= key_len + 10:
            texts[i] = texts[i].rstrip(".") + addition
            whys[i] = None
    # second pass: close a gap of less than 12 characters by lengthening the nearest
    # distractor with whatever its reason allows, without over-running the key.
    key_len = len(texts[ans_idx])
    others = sorted((i for i in range(4) if i != ans_idx), key=lambda i: -len(texts[i]))
    for i in others:
        if not whys[i]:
            continue
        gap = key_len - len(texts[i])
        if 0 < gap < 12:
            addition = " \u2014 " + whys[i].rstrip(".")
            if len(texts[i]) + len(addition) <= key_len:
                texts[i] = texts[i].rstrip(".") + addition
                whys[i] = None
    return [(texts[i], whys[i]) for i in range(4)]


def build_record(f: dict, idx: int) -> dict:
    # Construct the option list around the intended answer slot rather than shuffling
    # and hoping. The key goes to a slot fixed by a deterministic rotation, and the
    # three distractors are shuffled into the remaining three slots.
    rng = random.Random(seed(f["id"]))
    target = (idx * 3 + idx // 4) % 4
    distractors = list(f["d"])
    rng.shuffle(distractors)

    pool = []
    di = 0
    for slot in range(4):
        if slot == target:
            pool.append((f["a"], None))
        else:
            pool.append(distractors[di])
            di += 1
    ans_idx = target
    pool = balance_lengths(pool, ans_idx)

    opts, whys = [], []
    for text, why in pool:
        opts.append(text)
        whys.append(why)
    assert len(opts) == 4 and len({o.strip().lower() for o in opts}) == 4, f["id"]
    ans = LETTERS[ans_idx]

    expl = ["( " + ans + ") " + opts[ans_idx].rstrip(".") + "."]
    for L, (o, why) in enumerate(zip(opts, whys)):
        if why:
            expl.append(f"({LETTERS[L]}) {o.rstrip('.')}. \u2014 {why}")
    expl += ["", f["why"], "", f"Exam-safe point: {f['safe']}", "", f"Statutory Authority: {f['src']}"]

    return dict(
        id=f["id"], chapter=f["ch"], rule=f["rule"], rules_text=f["rules_text"],
        topic=f["topic"], q=f["q"], opts=opts, ans=ans,
        tag=f.get("tag", "Tough"), expl="\n".join(expl), src=f["src"], trap=f["trap"],
        kind=f.get("kind", "RULE"),
        covers=f.get("covers", []), version=f.get("version"),
    )


def main():
    import data_rules
    import data_compute
    import data_forms
    import data_statute
    import data_statute2
    import data_statute3
    import data_current
    import gen_questions

    facts = (data_rules.FACTS + data_compute.FACTS + data_forms.FACTS
             + data_statute.FACTS + data_statute2.FACTS + data_statute3.FACTS
             + data_current.FACTS + gen_questions.facts() + gen_questions.long_facts())
    ids = [f["id"] for f in facts]
    assert len(ids) == len(set(ids)), "duplicate ids"
    recs = [build_record(f, i) for i, f in enumerate(facts)]
    (HERE / "questions.json").write_text(json.dumps(recs, ensure_ascii=False, indent=1))
    print(f"{len(recs)} questions written")


if __name__ == "__main__":
    main()
