#!/usr/bin/env python3
"""paymatrix.py — the CCS (Revised Pay) Rules, 2016 pay matrix, cell by cell.

Two versions are held because the schedule in the notified rules is not the
schedule in force:

  ORIGINAL  Part A of the Schedule to G.S.R. 721(E) dated 25.07.2016.
            Level 13 starts at 1,18,500 (index of rationalisation 2.57).

  CURRENT   Level 13 revised by the Department of Expenditure resolution
            dated 16.05.2017, which raised that level's IOR from 2.57 to 2.67
            and re-cast every cell of it. Level 13 now starts at 1,23,100.
            Every other level is unchanged.

Both are stored, because the difference is itself the best examinable point in
the Schedule. `matrix(level)` returns the CURRENT cells — that is what a pay
question should be worked against today.

The current Level 13 column is derived here by the Government's own arithmetic
(cell n+1 = round(3% of cell n up to the next 100)) rather than transcribed, and
that derivation is checked against the published post-2017 cells in AUDIT.
"""
from __future__ import annotations

import math


def half_up(x: float) -> int:
    """Round a rupee amount the way the Rules do: .5 always goes up.

    Python's built-in round() is banker's rounding, so 6562.5 becomes 6562.
    The gazette rounds the same figure UP to 6563, and every rounding step in
    these rules (the 2.57 product, and the DA on a pre-revised NPA) must match.
    """
    return int(math.floor(x + 0.5))


LEVELS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
          "13", "13A", "14", "15", "16", "17", "18"]

#: Pay Band / Grade Pay / Level caption row of Part A of the Schedule.
PAY_BAND = {
    "1": "5200-20200", "2": "5200-20200", "3": "5200-20200", "4": "5200-20200",
    "5": "5200-20200", "6": "9300-34800", "7": "9300-34800", "8": "9300-34800",
    "9": "9300-34800", "10": "15600-39100", "11": "15600-39100", "12": "15600-39100",
    "13": "37400-67000", "13A": "37400-67000", "14": "37400-67000",
    "15": "67000-79000", "16": "75500-80000", "17": "80000", "18": "90000",
}
GRADE_PAY = {
    "1": "1800", "2": "1900", "3": "2000", "4": "2400", "5": "2800",
    "6": "4200", "7": "4600", "8": "4800", "9": "5400 (PB-2)", "10": "5400 (PB-3)",
    "11": "6600", "12": "7600", "13": "8700", "13A": "8900", "14": "10000",
    "15": "—", "16": "—", "17": "—", "18": "—",
}
#: Index of rationalisation, 7th CPC Report Table 4 (as applied by the Schedule).
IOR = {
    "1": 2.57, "2": 2.57, "3": 2.57, "4": 2.57, "5": 2.57,
    "6": 2.62, "7": 2.62, "8": 2.62,
    "9": 2.67, "10": 2.67, "11": 2.67, "12": 2.67,
    "13": 2.67, "13A": 2.62, "14": 2.67,
    "15": 2.72, "16": 2.78, "17": None, "18": None,
}
#: Level 13 stood at 2.57 until the resolution of 16.05.2017.
IOR_ORIGINAL_13 = 2.57

#: Part A of the Schedule, transcribed from the Gazette (G.S.R. 721(E)), rows 1..40.
#: Level 13 here is the ORIGINAL column (118500 .. 207900).
ORIGINAL = {
    "1":  [18000, 18500, 19100, 19700, 20300, 20900, 21500, 22100, 22800, 23500,
           24200, 24900, 25600, 26400, 27200, 28000, 28800, 29700, 30600, 31500,
           32400, 33400, 34400, 35400, 36500, 37600, 38700, 39900, 41100, 42300,
           43600, 44900, 46200, 47600, 49000, 50500, 52000, 53600, 55200, 56900],
    "2":  [19900, 20500, 21100, 21700, 22400, 23100, 23800, 24500, 25200, 26000,
           26800, 27600, 28400, 29300, 30200, 31100, 32000, 33000, 34000, 35000,
           36100, 37200, 38300, 39400, 40600, 41800, 43100, 44400, 45700, 47100,
           48500, 50000, 51500, 53000, 54600, 56200, 57900, 59600, 61400, 63200],
    "3":  [21700, 22400, 23100, 23800, 24500, 25200, 26000, 26800, 27600, 28400,
           29300, 30200, 31100, 32000, 33000, 34000, 35000, 36100, 37200, 38300,
           39400, 40600, 41800, 43100, 44400, 45700, 47100, 48500, 50000, 51500,
           53000, 54600, 56200, 57900, 59600, 61400, 63200, 65100, 67100, 69100],
    "4":  [25500, 26300, 27100, 27900, 28700, 29600, 30500, 31400, 32300, 33300,
           34300, 35300, 36400, 37500, 38600, 39800, 41000, 42200, 43500, 44800,
           46100, 47500, 48900, 50400, 51900, 53500, 55100, 56800, 58500, 60300,
           62100, 64000, 65900, 67900, 69900, 72000, 74200, 76400, 78700, 81100],
    "5":  [29200, 30100, 31000, 31900, 32900, 33900, 34900, 35900, 37000, 38100,
           39200, 40400, 41600, 42800, 44100, 45400, 46800, 48200, 49600, 51100,
           52600, 54200, 55800, 57500, 59200, 61000, 62800, 64700, 66600, 68600,
           70700, 72800, 75000, 77300, 79600, 82000, 84500, 87000, 89600, 92300],
    "6":  [35400, 36500, 37600, 38700, 39900, 41100, 42300, 43600, 44900, 46200,
           47600, 49000, 50500, 52000, 53600, 55200, 56900, 58600, 60400, 62200,
           64100, 66000, 68000, 70000, 72100, 74300, 76500, 78800, 81200, 83600,
           86100, 88700, 91400, 94100, 96900, 99800, 102800, 105900, 109100, 112400],
    "7":  [44900, 46200, 47600, 49000, 50500, 52000, 53600, 55200, 56900, 58600,
           60400, 62200, 64100, 66000, 68000, 70000, 72100, 74300, 76500, 78800,
           81200, 83600, 86100, 88700, 91400, 94100, 96900, 99800, 102800, 105900,
           109100, 112400, 115800, 119300, 122900, 126600, 130400, 134300, 138300, 142400],
    "8":  [47600, 49000, 50500, 52000, 53600, 55200, 56900, 58600, 60400, 62200,
           64100, 66000, 68000, 70000, 72100, 74300, 76500, 78800, 81200, 83600,
           86100, 88700, 91400, 94100, 96900, 99800, 102800, 105900, 109100, 112400,
           115800, 119300, 122900, 126600, 130400, 134300, 138300, 142400, 146700, 151100],
    "9":  [53100, 54700, 56300, 58000, 59700, 61500, 63300, 65200, 67200, 69200,
           71300, 73400, 75600, 77900, 80200, 82600, 85100, 87700, 90300, 93000,
           95800, 98700, 101700, 104800, 107900, 111100, 114400, 117800, 121300, 124900,
           128600, 132500, 136500, 140600, 144800, 149100, 153600, 158200, 162900, 167800],
    "10": [56100, 57800, 59500, 61300, 63100, 65000, 67000, 69000, 71100, 73200,
           75400, 77700, 80000, 82400, 84900, 87400, 90000, 92700, 95500, 98400,
           101400, 104400, 107500, 110700, 114000, 117400, 120900, 124500, 128200, 132000,
           136000, 140100, 144300, 148600, 153100, 157700, 162400, 167300, 172300, 177500],
    "11": [67700, 69700, 71800, 74000, 76200, 78500, 80900, 83300, 85800, 88400,
           91100, 93800, 96600, 99500, 102500, 105600, 108800, 112100, 115500, 119000,
           122600, 126300, 130100, 134000, 138000, 142100, 146400, 150800, 155300, 160000,
           164800, 169700, 174800, 180000, 185400, 191000, 196700, 202600, 208700],
    "12": [78800, 81200, 83600, 86100, 88700, 91400, 94100, 96900, 99800, 102800,
           105900, 109100, 112400, 115800, 119300, 122900, 126600, 130400, 134300, 138300,
           142400, 146700, 151100, 155600, 160300, 165100, 170100, 175200, 180500, 185900,
           191500, 197200, 203100, 209200],
    "13": [118500, 122100, 125800, 129600, 133500, 137500, 141600, 145800, 150200, 154700,
           159300, 164100, 169000, 174100, 179300, 184700, 190200, 195900, 201800, 207900],
    "13A": [131100, 135000, 139100, 143300, 147600, 152000, 156600, 161300, 166100, 171100,
            176200, 181500, 186900, 192500, 198300, 204200, 210300, 216600],
    "14": [144200, 148500, 153000, 157600, 162300, 167200, 172200, 177400, 182700, 188200,
           193800, 199600, 205600, 211800, 218200],
    "15": [182200, 187700, 193300, 199100, 205100, 211300, 217600, 224100, 230800],
    "16": [205400, 211600, 217900, 224400, 231100, 238000],
    "17": [225000],
    "18": [250000],
}

#: Level 13 as re-cast by the resolution of 16.05.2017 (IOR 2.67).
LEVEL13_2017_PUBLISHED = [
    123100, 126800, 130600, 134500, 138500, 142700, 147000, 151400, 155900, 160600,
    165400, 170400, 175500, 180800, 186200, 191800, 197600, 203500, 209600, 215900,
]


def _next_cell(cell: int) -> int:
    """The matrix's own rule: add 3% of the cell, then round to the NEAREST 100.

    18000 + 540 = 18540 -> 18500, not 18600: the matrix rounds to nearest, and
    that is precisely what makes every column reproducible from its first cell.
    """
    raw = cell * 1.03
    return int(math.floor(raw / 100.0 + 0.5)) * 100


def _derive(first: int, rungs: int) -> list[int]:
    out = [first]
    while len(out) < rungs:
        out.append(_next_cell(out[-1]))
    return out


def matrix(level: str, *, as_notified: bool = False) -> list[int]:
    """The vertical cells of a Level, current unless `as_notified` is asked for."""
    level = normalise(level)
    if level == "13" and not as_notified:
        return list(LEVEL13_2017_PUBLISHED)
    return list(ORIGINAL[level])


def normalise(level) -> str:
    s = str(level).strip().upper().replace(" ", "").replace("LEVEL", "L").replace("L-", "")
    if s.startswith("L"):
        s = s[1:]
    if s == "13A":
        return "13A"
    return str(int(s)) if s.isdigit() else s


def cell_of(level, pay: int, *, as_notified: bool = False) -> int | None:
    """Which cell number (1-based) of the level holds this exact pay."""
    cells = matrix(level, as_notified=as_notified)
    return cells.index(pay) + 1 if pay in cells else None


def next_higher_cell(level, figure: int, *, as_notified: bool = False) -> int:
    """The rule-7(1)(A)(i) / rule-13 step: equal cell if it exists, else the next higher."""
    for c in matrix(level, as_notified=as_notified):
        if c >= figure:
            return c
    return matrix(level, as_notified=as_notified)[-1]


def increment(level, pay: int, *, n: int = 1, as_notified: bool = False) -> int | None:
    """Move down n cells. None when the level is exhausted."""
    cells = matrix(level, as_notified=as_notified)
    if pay not in cells:
        return None
    i = cells.index(pay) + n
    return cells[i] if i < len(cells) else None


def fix_2016(existing_basic: int, level, *, as_notified: bool = False) -> dict:
    """Rule 7(1)(A)(i): multiply by 2.57, round to the rupee, land on a cell."""
    level = normalise(level)
    product = round(existing_basic * 2.57)
    landed = next_higher_cell(level, product, as_notified=as_notified)
    return {"existing": existing_basic, "product": product, "pay": landed,
            "cell": cell_of(level, landed, as_notified=as_notified),
            "shortfall": landed - product}


def promote(pay: int, from_level, to_level) -> dict:
    """Rule 13: one increment in the old level, then the equal-or-next-higher cell."""
    import copy  # noqa: F401
    fl, tl = normalise(from_level), normalise(to_level)
    stepped = increment(fl, pay)
    landed = next_higher_cell(tl, stepped)
    return {"from_pay": pay, "stepped": stepped, "pay": landed,
            "cell": cell_of(tl, landed), "gain": landed - pay,
            "exact": stepped in matrix(tl)}


def macp(pay: int, from_level, to_level) -> dict:
    """MACP is the same step as rule 13: no vacancy, no change of duties."""
    return promote(pay, from_level, to_level)


def macp_option(pay: int, from_level, to_level) -> dict:
    """The FR 22(I)(a)(1) option: hold at the next higher cell now, re-fix with two
    increments on the date of the next increment in the lower level."""
    fl, tl = normalise(from_level), normalise(to_level)
    interim = next_higher_cell(tl, pay)
    two_up = increment(fl, pay, n=2)
    final = next_higher_cell(tl, two_up)
    return {"interim": interim, "two_up": two_up, "final": final,
            "cell": cell_of(tl, final)}


def level13_impact(pay: int) -> dict:
    """The 16.05.2017 revision of Level 13, at a given cell."""
    old = matrix("13", as_notified=True)
    new = matrix("13")
    if pay not in old:
        return {}
    i = old.index(pay)
    return {"old": pay, "new": new[i] if i < len(new) else None,
            "gain": (new[i] - pay) if i < len(new) else None}


def summary() -> dict:
    out = {}
    for lv in LEVELS:
        cells = matrix(lv)
        out[lv] = {"cells": len(cells), "first": cells[0], "last": cells[-1],
                   "pay_band": PAY_BAND[lv], "grade_pay": GRADE_PAY[lv], "ior": IOR[lv]}
    return out


if __name__ == "__main__":
    # self-check: the Government's own rounding rule must regenerate every
    # column from its first cell, and reproduce the published Level 13 revision.
    bad = []
    for lv in LEVELS:
        got = matrix(lv)
        derived = _derive(got[0], len(got))
        if got != derived:
            first_bad = next(i for i in range(len(got)) if got[i] != derived[i])
            bad.append((lv, first_bad + 1, got[first_bad], derived[first_bad]))
    l13 = _derive(123100, 20)
    if l13[:20] != LEVEL13_2017_PUBLISHED:
        bad.append(("13 (2017)", 0, l13[:20], LEVEL13_2017_PUBLISHED))
    for lv, cell, have, want in bad:
        print(f"  MISMATCH Level {lv} cell {cell}: matrix has {have}, 3%-rule gives {want}")
    print(f"{'FAIL' if bad else 'OK'}: {len(LEVELS)} levels, "
          f"{sum(len(matrix(l)) for l in LEVELS)} cells, "
          f"{len(bad)} disagreements with the Government's 3% rounding rule")
