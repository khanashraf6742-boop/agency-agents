#!/usr/bin/env python3
"""coverage.py — measure question coverage against the provision inventory.

Coverage is reported at three depths, because they answer different questions:

  rule        one question reaching the rule at all
  sub-rule    one question reaching each sub-rule, clause or sub-clause
  provision   one question reaching each proviso, each Explanation, each clause letter

The third is the depth the platform claims. Anything not reached is listed by path so
the gap is visible rather than averaged away.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict

import provisions as pv


def load():
    import pathlib
    return json.loads((pathlib.Path(__file__).parent / "questions.json").read_text())


def normalise(path: str) -> str:
    """A question may cite the provision or the provision's parent; both count for the parent."""
    return path.strip()


def covered(qs):
    """Map provision path -> ids of questions that reach it."""
    hit = defaultdict(set)
    for q in qs:
        for c in q.get("covers") or []:
            hit[normalise(c)].add(q["id"])
    return hit


def ancestor_paths(path: str):
    """Every address a question could cite to reach this provision: itself and its parents."""
    if "#" in path:
        base, suf = path.split("#", 1)
        return [path, base]
    out = [path]
    while "(" in path:
        path = path[:path.rfind("(")]
        out.append(path)
    return out


def report(qs=None, verbose=True):
    qs = qs or load()
    provs = pv.build()
    hit = covered(qs)

    def reached(p):
        for a in ancestor_paths(p["path"]):
            if a in hit:
                return True
        return False

    # a parent is covered if any descendant is asked about it
    child_of = defaultdict(list)
    for p in provs:
        base = p["path"].split("#")[0]
        while "(" in base:
            base = base[:base.rfind("(")]
            child_of[base].append(p["path"])

    def reached_with_children(p):
        if reached(p):
            return True
        return any(reached({"path": d}) for d in child_of.get(p["path"], []))

    by_reach = {"rule": [], "sub-rule": [], "provision": []}
    for p in provs:
        ok = reached_with_children(p)
        if p["kind"] in ("rule", "sub-rule"):
            if not ok:
                by_reach["sub-rule"].append(p["path"])
        else:
            if not ok:
                by_reach["provision"].append(p["path"])

    rules_seen = {int(re.match(r"(\d+)", p["path"]).group(1)) for p in provs if reached_with_children(p)}
    all_rules = set(range(1, 88))

    # a coverage percentage per kind
    per_kind = Counter()
    per_kind_hit = Counter()
    for p in provs:
        per_kind[p["kind"]] += 1
        if reached_with_children(p):
            per_kind_hit[p["kind"]] += 1

    if verbose:
        print(f"questions                : {len(qs)}")
        print(f"provisions in inventory  : {len(provs)}")
        print(f"rules with a question    : {len(rules_seen)}/87")
        if all_rules - rules_seen:
            print(f"  rules not reached      : {sorted(all_rules - rules_seen)}")
        print()
        print(f"{'kind':12} {'provisions':>10} {'reached':>8} {'pct':>7}")
        for k in ("rule", "sub-rule", "clause", "sub-clause", "proviso", "explanation"):
            if per_kind[k]:
                print(f"{k:12} {per_kind[k]:>10} {per_kind_hit[k]:>8} {100 * per_kind_hit[k] / per_kind[k]:>6.1f}%")
        print()
        for label, miss in (("sub-rules / clauses", by_reach["sub-rule"]),
                            ("provisos / explanations", by_reach["provision"])):
            print(f"unreached {label}: {len(miss)}")
            for m in miss[:24]:
                print("   ", m)
            if len(miss) > 24:
                print(f"    ... and {len(miss) - 24} more")
            print()
    return dict(provs=len(provs), rules=len(rules_seen), per_kind=dict(per_kind),
                per_kind_hit=dict(per_kind_hit), missing=by_reach)


if __name__ == "__main__":
    report()
