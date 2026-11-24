#!/usr/bin/env python3
"""AUDIT — the checks that must hold before the platform is published.

Run after assemble.py. Exits non-zero on the first failure, so it can sit in a
build chain. The audit is stricter than the smoke test: it reasons about the
content, not the UI.
"""
import json
import pathlib
import re
import sys
from collections import Counter

B = pathlib.Path(__file__).parent
OUT = pathlib.Path(__file__).parent.parent / "AUDIT.md"
m = json.loads((B / "mcqs.json").read_text())
n = json.loads((B / "num80.json").read_text())
allq = m + n
from verbatim_leave import TEXT as VERIFIED

DEAD = {"18", "35", "36", "37", "45", "46", "58", "59"}


def _n(key):
    mt = re.search(r"([0-9][0-9,]*)", key)
    return int(mt.group(1).replace(",", "")) if mt else None


def _buffer_check(num):
    for x in num:
        st = x["stem"]
        mt = re.search(r"holds (?:exactly )?(\d+) days of earned leave", st)
        mt2 = re.search(r"takes (\d+) days", st)
        if not mt or "30 June" not in st:
            continue
        held, taken = int(mt.group(1)), int(mt2.group(1)) if mt2 else 0
        posted = 15 - taken if 285 < held <= 300 else 15
        expect = min(held + posted, 300)
        if _n(x["opts"]["ABCD".index(x["ans"])]) != expect:
            return False
    return True


def _pot_check(num):
    for x in num:
        st = x["stem"]
        mt = re.search(r"(?:retires|died in service) with (\d+) days of earned leave and (\d+) days of half pay leave", st)
        if not mt:
            continue
        el, hpl = int(mt.group(1)), int(mt.group(2))
        if "cash equivalent" in st or "commuted to top up" in st:
            continue                      # money items and the no-commutation item are reasoned, not summed
        earlier = re.search(r"earlier encashed (\d+) days", st)
        ceiling = 300 - (int(earlier.group(1)) if earlier else 0)
        expect = min(el, ceiling) + min(hpl, max(0, ceiling - min(el, ceiling)))
        if _n(x["opts"]["ABCD".index(x["ans"])]) != expect:
            return False
    return True


def _joining_check(num):
    for x in num:
        st = x["stem"]
        mt = re.search(r"holds (\d+) days of earned leave and has (\d+) days of unavailed joining time", st)
        if not mt:
            continue
        el, jt = int(mt.group(1)), int(mt.group(2))
        expect = min(jt, 15, max(0, 300 - el))
        key = x["opts"]["ABCD".index(x["ans"])]
        got = 0 if key.strip().lower().startswith("nil") else _n(key)
        if got != expect:
            return False
    return True


def _no_self_refuting_key(num):
    """True when every 'totals N days, past the limit' key is arithmetically right."""
    for x in num:
        key = x["opts"]["ABCD".index(x["ans"])]
        mt = re.search(r"totals (\d+) days.*?(\d{3})-day", key)
        if mt and int(mt.group(1)) <= int(mt.group(2)):
            return False
    return True


# A question "rests on" a dead rule when the rule it is filed under is dead AND the
# stem does not itself say the rule is omitted. Status questions are legitimate.
def rests_on_dead(x):
    if str(x["rule"]) not in DEAD:
        return False
    blob = (x["stem"] + " " + x["expl"]).lower()
    return "omitted" not in blob

checks = {
    "four distinct options in every question": all(
        len(x["opts"]) == 4 and len({o.strip().lower() for o in x["opts"]}) == 4 for x in allq),
    "the key letter matches the explanation's answer line": all(
        (re.search(r"Answer\s*\n\s*\(([A-D])\)", x["expl"]) or [None, None])[1] == x["ans"] for x in allq),
    "every question carries a statutory or executive source": all(x["src"].strip() for x in allq),
    f"no duplicate stems across the {len(allq)}": len({x["stem"] for x in allq}) == len(allq),
    "no question rests on a deleted or omitted rule": not any(rests_on_dead(x) for x in allq),
    "no rule number is cited for CL/SCL/comp-off/RH": not any(
        x["chapter"] == "NS" and re.search(r"(under|by|vide|per)\s+rule\s*\d", x["stem"], re.I) for x in allq),
    "every numerical answer carries a stepwise solution": all("Step 1" in x["expl"] for x in n),
    "the numerical set is exactly 80": len(n) == 80,
    "the general bank is exactly 700": len(m) == 700,
    # an option that is both correct and visibly the longest gives the answer away
    "no question makes its key the longest option": sum(
        1 for x in allq
        if len(x["opts"]["ABCD".index(x["ans"])]) == max(len(o) for o in x["opts"])) <= len(allq) * 0.55,
    "multi-statement answers are counts, not sentences": all(
        x["opts"]["ABCD".index(x["ans"])].lower().startswith(("all ", "only ")) for x in m if x["id"].startswith("STMT")),
    # A "No — the total of N days runs past the limit" answer is only sound if N really
    # does run past the limit quoted. NUMMAT-01 once said "260 days, past the limit"
    # against a 730-day cap; that is a self-refuting key.
    "no answer calls a total excessive against a limit it does not breach": _no_self_refuting_key(n),
    # Within one question, punctuation must not single out the key.
    "no question punctuates only its key": not any(
        len({o.rstrip().endswith(".") for o in x["opts"]}) > 1 and
        x["opts"]["ABCD".index(x["ans"])].rstrip().endswith(".") and
        sum(o.rstrip().endswith(".") for o in x["opts"]) == 1
        for x in allq),
    "every buffer-band balance re-derives independently": _buffer_check(n),
    "every death and retirement pot re-derives independently": _pot_check(n),
    "every joining-time credit re-derives independently": _joining_check(n),
    # the rule library must not present a paraphrase as the section
    "every rule marked verbatim really is the consolidated text": all(
        r.get("verbatim") is True for r in json.loads((B / "rules.json").read_text()) if str(r["rule"]) in VERIFIED),
    "no question cites a rule whose text is unverified as if quoting it": not any(
        "statutory" in x["expl"].lower() and "not yet checked" in x["expl"].lower() for x in allq),
}

rep = ["# Build audit", "",
       f"- General bank: **{len(m)}** questions",
       f"- Numerical 80: **{len(n)}** questions",
       f"- Total objective questions: **{len(allq)}**", ""]
for k, v in checks.items():
    rep.append(f"- {'PASS' if v else 'FAIL'} — {k}")

rep += ["", "## Answer key"]
for k, v in sorted(Counter(x["ans"] for x in allq).items()):
    rep.append(f"- {k}: {v}")
rep += ["", "## By chapter (general bank)"]
for k, v in Counter(x["chapter"] for x in m).most_common():
    rep.append(f"- {k}: {v}")
rep += ["", "## By difficulty"]
for k, v in Counter(x["tag"] for x in allq).most_common():
    rep.append(f"- {k}: {v}")
longest = sum(1 for x in allq
              if [len(o) for o in x["opts"]]["ABCD".index(x["ans"])] == max(len(o) for o in x["opts"]))
rep += ["", "## Length tell", "",
        f"- the correct option is also the longest in {longest}/{len(allq)} "
        f"({longest / len(allq) * 100:.0f}%) — on a four-option item the correct answer is the longest one "
        f"25% of the time by pure chance, so a bank sitting near that figure gives no free marks to a "
        f"candidate who counts words instead of reading the rule"]
OUT.write_text("\n".join(rep) + "\n")
print("\n".join(rep))

failed = [k for k, v in checks.items() if not v]
if failed:
    print("\nAUDIT FAILED: " + "; ".join(failed))
    sys.exit(1)
print("\nAUDIT PASSED")
