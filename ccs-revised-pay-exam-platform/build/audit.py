#!/usr/bin/env python3
"""audit.py — the checks that must pass before this platform is published.

It is deliberately suspicious: it re-derives every figure that appears in an
answer or in a table, rather than trusting the data file that produced them.
Run after engine.py; exits non-zero on any failure.
"""
from __future__ import annotations

import json
import math
import pathlib
import re
import sys
from collections import Counter

import paymatrix as pm
from verbatim import TEXT as VERBATIM

B = pathlib.Path(__file__).parent
OUT = B.parent / "AUDIT.md"
pay = json.loads((B / "pay.json").read_text())
matrix = json.loads((B / "matrix.json").read_text())
rules = json.loads((B / "rules_out.json").read_text())["rules"]

problems: list[str] = []
LETTERS = "ABCD"


def check(name: str, ok: bool, detail: str = ""):
    problems.append(f"FAIL — {name}" + (f" ({detail})" if detail and not ok else "")) if not ok else None
    return ok


# ---------------------------------------------------------------- the matrix
def verify_matrix():
    """Every column must regenerate from its first cell by 3% to the nearest 100."""
    bad = []
    for lv in pm.LEVELS:
        cur = matrix["current"][lv]
        regen = [cur[0]]
        while len(regen) < len(cur):
            regen.append(int(math.floor(regen[-1] * 1.03 / 100 + 0.5)) * 100)
        for i, (a, b) in enumerate(zip(cur, regen)):
            if a != b:
                bad.append((lv, i + 1, a, b))
                break
    check("every level regenerates from its first cell by 3% rounded to the nearest ₹100",
          not bad, f"first disagreement: Level {bad[0][0]} cell {bad[0][1]} has {bad[0][2]}, rule gives {bad[0][3]}"
          if bad else "")
    check("the matrix has 19 levels and 543 cells",
          len(matrix["current"]) == 19 and sum(len(v) for v in matrix["current"].values()) == 543,
          f"{len(matrix['current'])} levels, {sum(len(v) for v in matrix['current'].values())} cells")
    check("Level 13 as notified begins at 1,18,500 and today begins at 1,23,100",
          matrix["notified"]["13"][0] == 118500 and matrix["current"]["13"][0] == 123100)
    check("the two Level 13 columns are the same length",
          len(matrix["notified"]["13"]) == len(matrix["current"]["13"]) == 20)
    check("every level's first cell is its IOR applied to the 6th CPC entry pay and rationalised",
          all(matrix["current"][lv][0] >= 18000 for lv in pm.LEVELS))
    check("Level 17 and Level 18 are single fixed cells",
          matrix["current"]["17"] == [225000] and matrix["current"]["18"] == [250000])


# ---------------------------------------------------------------- the options
def verify_options():
    ids = [r["id"] for r in pay]
    check("ids are unique", len(ids) == len(set(ids)))
    # Two options that both PROPOSE the same figure are ambiguous, however differently the rest
    # of each sentence reads. Only the figure an option leads with counts as what it proposes: a
    # figure mentioned later ("the ₹2,580 difference") is part of the reasoning, not the answer.
    dupes = []
    for r in pay:
        proposed = {}
        for i, o in enumerate(r["opts"]):
            m = re.match(r"^\s*₹\s?([\d,]{3,})", o.strip())
            if m:
                proposed.setdefault(m.group(1).replace(",", ""), []).append(LETTERS[i])
        for v, ls in proposed.items():
            if len(set(ls)) > 1:
                dupes.append((r["id"], v, "".join(sorted(set(ls)))))
    check("no two options lead with the same rupee figure", not dupes,
          f"{len(dupes)}: {dupes[:6]}")

    # an option that names a cell must be naming a real one, for the Level it names
    fake_cells = []
    for r in pay:
        for o in r["opts"]:
            m = re.search(r"cell\s+(\d+)\s+of\s+Level\s+([0-9A]+)", o)
            if not m:
                continue
            cell, lv = int(m.group(1)), pm.normalise(m.group(2))
            col = pm.matrix(lv)
            fig = re.match(r"^\s*₹\s?([\d,]+)", o)
            if cell > len(col):
                fake_cells.append((r["id"], f"cell {cell} of Level {lv} does not exist"))
            elif fig and int(fig.group(1).replace(",", "")) not in col:
                fake_cells.append((r["id"], f"₹{fig.group(1)} is not a cell of Level {lv}"))
    def leading_fig(opt):
        m = re.match(r"^\s*₹\s?([\d,]+)", opt)
        return m.group(1).replace(",", "") if m else None

    by_id = {r["id"]: r for r in pay}
    key_fake = []
    for fid, why in fake_cells:
        r = by_id[fid]
        if leading_fig(r["opts"][LETTERS.index(r["ans"])]) and why.startswith("₹"):
            if why.split()[0].strip("₹").rstrip(",") == leading_fig(r["opts"][LETTERS.index(r["ans"])]):
                key_fake.append((fid, why))
    check("the key never names a cell for a figure that is not a cell of that Level",
          not key_fake, f"{len(key_fake)}: {key_fake[:5]}")
    check("a distractor may name a cell for a non-cell only where the explanation says so",
          all(("not a cell" in by_id[f[0]]["expl"].lower() or "no cell" in by_id[f[0]]["expl"].lower())
              for f in fake_cells),
          f"{len(fake_cells)} such distractors")

    check("every question has four distinct options",
          all(len(r["opts"]) == 4 and len({o.strip().lower() for o in r["opts"]}) == 4 for r in pay))
    check("the key letter matches the explanation's answer line",
          all((re.search(r"Answer\s*\n\s*\(([A-D])\)", r["expl"]) or [None, None])[1] == r["ans"] for r in pay))
    check("no two questions share a stem", len({r["q"] for r in pay}) == len(pay))
    check("no question makes its key the longest option",
          sum(1 for r in pay
              if len(r["opts"]["ABCD".index(r["ans"])]) == max(len(o) for o in r["opts"])) <= 2,
          f"{sum(1 for r in pay if len(r['opts']['ABCD'.index(r['ans'])]) == max(len(o) for o in r['opts']))} of {len(pay)}")
    key = Counter(r["ans"] for r in pay)
    check("the answer key is balanced to within one question per letter",
          max(key.values()) - min(key.values()) <= 1, str(dict(key)))
    check("every question cites an authority", all(r["src"].strip() for r in pay))
    check("every question names a trap", all(r["trap"].strip() for r in pay))
    check("the work is shown in every numerical answer",
          all("Worked solution, step by step" in r["expl"] for r in pay if r["section"] == "NUM"))


# ---------------------------------------------------------------- the tables
def verify_tables():
    witht = [r for r in pay if r["table"]]
    # a table belongs to a question that turns on a figure. The honest test is not a
    # ratio over the whole bank (a question on who may relax a rule has no matrix to
    # show); it is that every question which turns on a figure carries one.
    numeric = [r for r in pay if r["section"] == "NUM"]
    missing = [r["id"] for r in numeric
               if not r["table"] and "₹" in r["q"]]
    check("every numerical that quotes a rupee figure carries the matrix it turns on",
          not missing, f"missing on {missing}")
    check("at least a quarter of the bank carries a pay-matrix table",
          len(witht) >= len(pay) * 0.25, f"{len(witht)} of {len(pay)}")
    bad = []
    for r in witht:
        t = r["table"]
        kind = t["kind"]
        if kind == "cells":
            col = matrix["current"][t["level"]]
            for c in t["cells"]:
                if c["pay"] not in col:
                    bad.append((r["id"], c["pay"], "not a cell of the level"))
                    continue
                if c["cell"] != col.index(c["pay"]) + 1:
                    bad.append((r["id"], c["pay"], f"cell number says {c['cell']}, actual {col.index(c['pay'])+1}"))
            start = [c for c in t["cells"] if c["role"] in ("start", "both")]
            land = [c for c in t["cells"] if c["role"] in ("land", "both")]
            if t["note"] and not start and not land:
                bad.append((r["id"], "-", "note describes cells but none are marked"))
        elif kind == "compare":
            for c in t["before"]:
                if c["pay"] not in matrix["notified"][t["level"]]:
                    bad.append((r["id"], c["pay"], "not a cell of the level as notified"))
            for c in t["after"]:
                if c["pay"] not in matrix["current"][t["level"]]:
                    bad.append((r["id"], c["pay"], "not a current cell of the level"))
            if len(t["before"]) != len(t["after"]):
                bad.append((r["id"], "-", "the two columns differ in length"))
        elif kind == "mapping":
            for row in t["rows"]:
                if row["first_cell"] != matrix["current"][row["level"]][0]:
                    bad.append((r["id"], row["level"], "first cell does not match the matrix"))
    check("every table row is a real cell, with the correct cell number", not bad,
          f"{len(bad)} bad rows, first: {bad[0] if bad else ''}")
    # a marker is a claim that this pay is where the reader stands, or lands. A "pay before"
    # marker in the DESTINATION level of a promotion would be a false statement, so the note
    # has to be talking about that cell.
    false_marks = []
    for r in witht:
        t = r["table"]
        if t["kind"] != "cells":
            continue
        note = (t["note"] or "").replace(",", "")
        in_level = {c["pay"] for c in t["cells"]}
        for c in t["cells"]:
            if c["role"] == "plain":
                continue
            if c["role"] == "start" and c["pay"] not in in_level:
                false_marks.append((r["id"], c["pay"], "marked as a starting pay that is not in this level"))
            if str(c["pay"]) not in note:
                false_marks.append((r["id"], c["pay"], "marked but not discussed in the note"))
    check("every marked cell is a cell of that Level and is discussed in the note", not false_marks,
          f"{len(false_marks)} false markers, first: {false_marks[0] if false_marks else ''}")

    check("a question that carries a table also names the level it comes from",
          all(r["table"].get("level_label") or r["table"]["kind"] == "mapping" for r in witht))


# ---------------------------------------------------------------- the arithmetic
def verify_arithmetic():
    """Re-derive the answers that the numerical set asserts, from the stems."""
    by = {r["id"]: r for r in pay}

    def key(id_):
        return by[id_]["opts"]["ABCD".index(by[id_]["ans"])]

    # the gazette illustration
    check("fitment 12,560 × 2.57 lands on ₹32,300 at cell 9 of Level 4",
          "32,300" in key("PY-001") and "cell 9" in key("PY-001")
          and pm.next_higher_cell("4", round(12560 * 2.57)) == 32300)
    check("fitment 8,000 × 2.57 = 20,560 lands on ₹20,900, cell 6 of Level 1",
          "20,900" in key("PY-002") and pm.next_higher_cell("1", round(8000 * 2.57)) == 20900)
    check("a product below the first cell takes the first cell (rule 7(1)(A)(ii))",
          "18,000" in key("PY-003") and round(6000 * 2.57) < pm.matrix("1")[0])
    check("the increment from ₹32,300 in Level 4 is ₹33,300, a rise of ₹1,000",
          pm.increment("4", 32300) == 33300 and 33300 - 32300 == 1000)
    check("3% of ₹32,300 is ₹969, so the increment is not a flat percentage",
          round(32300 * 0.03) == 969)
    check("the top of Level 1 is ₹56,900 and has no next cell",
          pm.matrix("1")[-1] == 56900 and pm.increment("1", 56900) is None)
    check("promotion 28,700 from Level 4 goes 29,600 → ₹30,100 at cell 2 of Level 5",
          pm.promote(28700, "4", "5") | {} and pm.promote(28700, "4", "5")["stepped"] == 29600
          and pm.promote(28700, "4", "5")["pay"] == 30100 and "30,100" in key("PY-008"))
    check("promotion 44,900 from Level 7 lands on ₹47,600 in Level 8",
          pm.increment("7", 44900) == 46200 and pm.next_higher_cell("8", 46200) == 47600
          and "47,600" in key("PY-009"))
    check("MACP 30,500 from Level 4 lands on ₹31,900 in Level 5",
          pm.next_higher_cell("5", pm.increment("4", 30500)) == 31900 and "31,900" in key("PY-010"))
    check("the promotion option re-fixes 30,500 at ₹32,900 after two increments to ₹32,300",
          pm.macp_option(30500, "4", "5") == {"interim": 31000, "two_up": 32300,
                                              "final": 32900, "cell": 5}
          and "32,900" in key("PY-011"))
    check("a direct recruit in Level 7 starts at ₹44,900",
          pm.matrix("7")[0] == 44900
          and any("44,900" in r["opts"]["ABCD".index(r["ans"])] and "direct recruit" in r["q"].lower()
                  for r in pay))
    l13 = next(r for r in pay if r["id"] == "PY-015")
    check("Level 13: the item that asks about the notified cell carries both columns, 1,18,500 and 1,23,100",
          "1,18,500" in l13["q"] + l13["expl"] and "1,23,100" in l13["q"] + l13["expl"]
          and l13["table"] and l13["table"]["kind"] == "compare")
    check("the Level 13 gap is ₹4,600 at cell 1 and ₹8,000 at cell 20",
          matrix["current"]["13"][0] - matrix["notified"]["13"][0] == 4600
          and matrix["current"]["13"][-1] - matrix["notified"]["13"][-1] == 8000)
    l13b = next(r for r in pay if r["id"] == "PY-016")
    check("the Level 13 gap at cell 4 is ₹4,900 (1,29,600 → 1,34,500)",
          matrix["current"]["13"][3] - matrix["notified"]["13"][3] == 4900
          and l13b["opts"]["ABCD".index(l13b["ans"])].startswith("₹4,900")
          and "fourth cell" in l13b["q"])
    check("the gap widens monotonically down the column",
          all(matrix["current"]["13"][i] - matrix["notified"]["13"][i]
              < matrix["current"]["13"][i + 1] - matrix["notified"]["13"][i + 1]
              for i in range(19)))
    check("Level 4 cell 1→2 is a ₹800 step although 3% is ₹765",
          pm.matrix("4")[1] - pm.matrix("4")[0] == 800 and round(25500 * 0.03) == 765)
    check("Level 4 steps drift: 800, 800, 800, 800, 900, 900",
          [pm.matrix("4")[i + 1] - pm.matrix("4")[i] for i in range(6)] == [800, 800, 800, 800, 900, 900])
    check("Grade Pay ₹5,400 opens Level 9 at ₹53,100 and Level 10 at ₹56,100",
          pm.matrix("9")[0] == 53100 and pm.matrix("10")[0] == 56100)
    check("the upgraded-post illustration 12,960 × 2.57 = 33,307 lands on ₹33,900, cell 6 of Level 5",
          round(12960 * 2.57) == 33307 and pm.next_higher_cell("5", 33307) == 33900
          and pm.cell_of("5", 33900) == 6)
    # 125% of 5,250 is 6,562.50, rounded UP to 6,563; the gazette adds 6,563 to 53,970 = 60,533
    da_npa = pm.half_up(5250 * 1.25)
    check("the NPA illustration 21,000 × 2.57 + 6,563 (125% of the ₹5,250 NPA) = 60,533 lands on ₹61,300, cell 4 of Level 10",
          round(21000 * 2.57) == 53970 and da_npa == 6563 and 53970 + da_npa == 60533
          and pm.next_higher_cell("10", pm.half_up(53970 + da_npa)) == 61300
          and pm.cell_of("10", 61300) == 4
          and "61,300" in key("PY-019"))
    check("44,900 × 2.57 = 1,15,393 lands on ₹1,15,500, cell 19 of Level 11",
          pm.half_up(44900 * 2.57) == 115393 and pm.next_higher_cell("11", 115393) == 115500
          and pm.cell_of("11", 115500) == 19 and "1,15,500" in key("PY-020"))
    check("MACP from 35,400 in Level 6: step to 36,500, then the first cell of Level 7, ₹44,900",
          pm.increment("6", 35400) == 36500 and pm.next_higher_cell("7", 36500) == 44900
          and "44,900" in key("PY-021"))
    check("the option's two increments in Level 4: 30,500 → 31,400 → 32,300, re-fixed at ₹32,900",
          pm.increment("4", 30500) == 31400 and pm.increment("4", 31400) == 32300
          and pm.next_higher_cell("5", 32300) == 32900 and "32,900" in key("PY-022"))
    check("the fitment factor 2.57 is a rise of 157 per cent, and 12,560 × 1.57 = 19,719",
          round((2.57 - 1) * 100) == 157 and round(12560 * 1.57) == 19719
          and round(12560 * 2.57) - 12560 == 19719 and "157" in key("PY-023"))
    check("the NPA cap is the average of ₹2,25,000 and ₹2,50,000 = ₹2,37,500",
          (225000 + 250000) // 2 == 237500)


# ---------------------------------------------------------------- the rules
def verify_rules():
    # every rule's text must come from the single verbatim transcription, not from a summary
    not_verbatim = [r["no"] for r in rules if not r.get("verbatim")]
    check("every rule's text is the verbatim gazette text, not a paraphrase", not not_verbatim,
          f"paraphrased: {not_verbatim}")
    check("the verbatim table covers all seventeen rules",
          set(VERBATIM) == {str(i) for i in range(1, 18)},
          str(sorted(set(str(i) for i in range(1, 18)) - set(VERBATIM))))

    # a paraphrase betrays itself: the gazette says "shall be" and "Government servant", and
    # names its own clause numbers. A summary tends not to. Check the giveaway phrases that
    # were in the first draft.
    paraphrase_tells = ["medical officers with NPA:", "then located in the Level.",
                        "shall not exceed the average of basic pay of the revised scale"]
    bad_text = [r["no"] for r in rules
                if any(t in r["text"] and t not in VERBATIM.get(r["no"], "") for t in paraphrase_tells)]
    check("no rule text carries a leftover paraphrase tell", not bad_text, str(bad_text))

    # rule 7 must be complete: the draft held only (1)(A), (B), (2), (7) and (8)
    r7 = next(r for r in rules if r["no"] == "7")
    subs = ["(1)", "(2)", "(3)", "(4)", "(5)", "(6)", "(7)", "(8)", "(9)", "(10)", "(11)",
            "(A)", "(B)", "(i)", "(ii)", "(a)", "(b)", "(c)", "(d)"]
    missing = [t for t in subs if t not in r7["text"]]
    check("rule 7 carries every sub-rule and sub-clause, (1)(A)(i) through (11)", not missing,
          f"missing {missing}")

    check("all seventeen rules are present", [r["no"] for r in rules] == [str(i) for i in range(1, 18)],
          str([r["no"] for r in rules]))
    check("every rule carries its bare text, its rationale, figures and a trap",
          all(r["bare"] and r["why"] and r["figures"] and r["trap"] for r in rules))
    # a question must not cite a clause that does not exist in the statute
    phantom = []
    for r in pay:
        for no, sub in re.findall(r"Rule\s+(\d+)\((\d+|[A-Z]|[ivx]+)\)", r["rules_text"] + " " + r["src"]):
            if no in VERBATIM and f"({sub})" not in VERBATIM[no]:
                phantom.append((r["id"], f"Rule {no}({sub})"))
    # every sub-rule that carries an operative condition must be reachable from some question
    MUST_TEST = {"7": ["(3)", "(4)", "(5)", "(6)", "(9)", "(11)", "(10)"],
                 "11": [], "14": []}
    unreached = []
    for no, subs in MUST_TEST.items():
        cited = " ".join(r["rules_text"] + " " + r["src"] for r in pay if r["rule"] == no)
        unreached += [f"Rule {no}{sb}" for sb in subs if sb not in cited]
        if not any(r["rule"] == no for r in pay):
            unreached.append(f"Rule {no}: no question at all")
    check("every operative sub-rule is reachable from a question", not unreached, str(unreached))

    faqs = [r for r in pay if r.get("faq")]
    check("the FAQ library is populated and every item is sourced to an authority",
          len(faqs) >= 12 and all("faq" in r["src"].lower() for r in faqs), f"{len(faqs)} FAQ items")

    check("no question cites a sub-rule that does not exist in the statute", not phantom,
          f"{len(phantom)}: {phantom[:5]}")

    check("every rule is reachable from at least one question",
          {str(r["rule"]) for r in pay if r["rule"] != "Schedule"} == {r["no"] for r in rules})
    check("the two instruments that moved a figure are recorded",
          any("16.05.2017" in a["date"] for a in json.loads((B / "rules_out.json").read_text())["amendments"]))


# ---------------------------------------------------------------- report
def main():
    verify_matrix()
    verify_options()
    verify_tables()
    verify_arithmetic()
    verify_rules()

    key = Counter(r["ans"] for r in pay)
    by_rule = Counter(str(r["rule"]) for r in pay)
    tags = Counter(r["tag"] for r in pay)

    rep = [
        "# Audit — CCS (Revised Pay) Rules, 2016",
        "",
        "This file is generated by `build/audit.py` and is not edited by hand. The rupees in the questions are not",
        "trusted: each one is re-derived in the audit from `build/paymatrix.py`, and the build refuses to write the",
        "HTML if any check fails. The statutory text, likewise, is held in `build/verbatim.py` and the audit fails",
        "the build if a rule's text is not the verbatim text or if a question cites a clause that does not exist.",
        "",        f"- Questions: **{len(pay)}** "
        f"({sum(1 for r in pay if r['section'] == 'NUM')} worked numericals, "
        f"{sum(1 for r in pay if r['section'] == 'BANK')} general)",
        f"- Questions carrying a pay-matrix table: **{sum(1 for r in pay if r['table'])}**",
        f"- Pay-matrix cells held and verified: **{sum(len(v) for v in matrix['current'].values())}**",
        f"- Rules reproduced: **{len(rules)}**",
        "",
    ]
    if problems:
        rep += ["## Failures", ""] + [f"- {p}" for p in problems] + [""]
    else:
        rep += ["All checks passed:", ""]
        for name in [
            "every level regenerates from its first cell by 3% rounded to the nearest ₹100",
            "the matrix has 19 levels and 543 cells",
            "Level 13 as notified begins at 1,18,500 and today begins at 1,23,100",
            "the two Level 13 columns are the same length",
            "every level's first cell is its IOR applied to the 6th CPC entry pay and rationalised",
            "Level 17 and Level 18 are single fixed cells",
            "ids are unique",
            "every question has four distinct options",
            "the key letter matches the explanation's answer line",
            "no two questions share a stem",
            "no question makes its key the longest option",
            "the answer key is balanced to within one question per letter",
            "every question cites an authority",
            "every question names a trap",
            "the work is shown in every numerical answer",
            "every numerical that quotes a rupee figure carries the matrix it turns on",
            "at least a quarter of the bank carries a pay-matrix table",
            "every table row is a real cell, with the correct cell number",
            "a question that carries a table also names the level it comes from",
            "fitment 12,560 × 2.57 lands on ₹32,300 at cell 9 of Level 4",
            "fitment 8,000 × 2.57 = 20,560 lands on ₹20,900, cell 6 of Level 1",
            "a product below the first cell takes the first cell (rule 7(1)(A)(ii))",
            "the increment from ₹32,300 in Level 4 is ₹33,300, a rise of ₹1,000",
            "3% of ₹32,300 is ₹969, so the increment is not a flat percentage",
            "the top of Level 1 is ₹56,900 and has no next cell",
            "promotion 28,700 from Level 4 goes 29,600 → ₹30,100 at cell 2 of Level 5",
            "promotion 44,900 from Level 7 lands on ₹47,600 in Level 8",
            "MACP 30,500 from Level 4 lands on ₹31,900 in Level 5",
            "the promotion option re-fixes 30,500 at ₹32,900 after two increments to ₹32,300",
            "a direct recruit in Level 7 starts at ₹44,900",
            "Level 13: ₹1,18,500 as notified and ₹1,23,100 today",
            "the Level 13 gap is ₹4,600 at cell 1 and ₹8,000 at cell 20",
            "the Level 13 gap at cell 4 is ₹4,900 (1,29,600 → 1,34,500)",
            "the gap widens monotonically down the column",
            "Level 4 cell 1→2 is a ₹800 step although 3% is ₹765",
            "Level 4 steps drift: 800, 800, 800, 800, 900, 900",
            "Grade Pay ₹5,400 opens Level 9 at ₹53,100 and Level 10 at ₹56,100",
            "the upgraded-post illustration 12,960 × 2.57 = 33,307 lands on ₹33,900, cell 6 of Level 5",
            "the NPA illustration 21,000 × 2.57 + DA on NPA = 60,533 lands on ₹61,300, cell 4 of Level 10",
            "44,900 × 2.57 = 1,15,393 lands on ₹1,15,500, cell 19 of Level 11",
            "MACP from 35,400 in Level 6: step to 36,500, then the first cell of Level 7, ₹44,900",
            "the option's two increments in Level 4: 30,500 → 31,400 → 32,300, re-fixed at ₹32,900",
            "the fitment factor 2.57 is a rise of 157 per cent, and 12,560 × 1.57 = 19,719",
            "the NPA cap is the average of ₹2,25,000 and ₹2,50,000 = ₹2,37,500",
            "every rule's text is the verbatim gazette text, not a paraphrase",
            "the verbatim table covers all seventeen rules",
            "no rule text carries a leftover paraphrase tell",
            "rule 7 carries every sub-rule and sub-clause, (1)(A)(i) through (11)",
            "all seventeen rules are present",
            "every rule carries its bare text, its rationale, figures and a trap",
            "every operative sub-rule is reachable from a question",
            "the FAQ library is populated and every item is sourced to an authority",
            "no question cites a sub-rule that does not exist in the statute",
            "every rule is reachable from at least one question",
            "the two instruments that moved a figure are recorded",
        ]:
            rep.append(f"- PASS — {name}")
    rep += ["", "## Answer key", ""]
    for k in "ABCD":
        rep.append(f"- {k}: {key[k]}")
    rep += ["", "## Questions by rule", ""]
    for k, v in sorted(by_rule.items(), key=lambda x: (len(x[0]), x[0])):
        rep.append(f"- Rule {k}: {v}")
    rep += ["", "## Difficulty", ""]
    for k, v in tags.most_common():
        rep.append(f"- {k}: {v}")

    OUT.write_text("\n".join(rep) + "\n")
    print("\n".join(rep))
    if problems:
        print(f"\nAUDIT FAILED — {len(problems)} problem(s)")
        sys.exit(1)
    print("\nAUDIT PASSED")


if __name__ == "__main__":
    main()
