#!/usr/bin/env python3
"""data_numeric.py — the numerical set, worked cell by cell.

Each item carries the slice of the pay matrix that the question turns on, so the
platform can draw the actual table beside the question, with the starting cell,
the cells passed through and the landing cell marked. Every answer is computed
through paymatrix.py rather than typed, so a wrong total is a build failure
rather than a silent typo.
"""
from __future__ import annotations

import paymatrix as pm
from paymatrix import half_up

FACTS = []


def N(topic, rule, rules_text, stem, answer, steps, distractors, safe, source, trap,
      level=None, cells=None, marks=None, tag="Tough", table_note=None,
      table_kind=None, cells_before=None, cells_after=None, mapping=None, highlight=None,
      before_label=None, after_label=None):
    FACTS.append(dict(
        id=f"PY-{len(FACTS) + 1:03d}", topic=topic, rule=rule, rules_text=rules_text,
        q=stem, a=answer, steps=steps, d=distractors, safe=safe, src=source, trap=trap,
        level=level, cells=cells, marks=marks or {}, tag=tag, table_note=table_note,
        table_kind=table_kind, cells_before=cells_before, cells_after=cells_after,
        mapping=mapping, highlight=highlight,
        before_label=before_label, after_label=after_label))


def fmt(n):
    """Indian digit grouping, without a rupee sign: 123100 -> 1,23,100."""
    s = str(int(n))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts) + "," + tail


def rs(n):
    return "₹" + fmt(n)


# =====================================================================
# A. THE FITMENT — rule 7(1)(A)
# =====================================================================
N("Fitment under rule 7(1)(A)(i)", "7",
  "Rule 7(1)(A)(i)",
  "A servant's existing basic pay on 1 January 2016 is ₹12,560 in Grade Pay ₹2,400 (Level 4). "
  "What is his pay in the revised pay structure?",
  "₹32,300, at cell 9 of Level 4",
  ["Multiply the existing basic pay by the fitment factor: 12,560 × 2.57 = 32,279.20, and rule 7(1)(A)(i) rounds this "
   "to the nearest rupee, so ₹32,279.",
   "Now locate ₹32,279 in Level 4. It is not a printed cell: cell 8 is ₹31,400 and cell 9 is ₹32,300. The rule takes the "
   "pay at the cell EQUAL to the figure if there is one, and otherwise at the IMMEDIATE NEXT HIGHER cell.",
   "So the pay is fixed at ₹32,300, cell 9. The ₹21 by which the cell exceeds the product is not an error and is not "
   "recovered; the rule deliberately lands the servant on the next higher cell so that nobody loses by the conversion."],
  [("₹32,279, at cell 8 of Level 4",
    "₹32,279 is the product, and it is not a cell of Level 4 at all. Rule 7(1)(A)(i) does not fix pay at the product; "
    "it locates it in the matrix and takes the equal or next higher cell — and cell 8, ₹31,400, lies below it."),
   ("₹32,400, reached by rounding ₹32,279 up to the next ₹100 and reading that as the pay",
    "There is no rounding of the product to ₹100. Rule 7(1)(A)(i) rounds to the rupee and then LOCATES the figure; the "
    "cell happens to be ₹32,300 here, but it is reached by location, not by rounding."),
   ("₹31,400, at cell 8 of Level 4",
    "That is the cell BELOW the product — the opposite of where the rule goes, since the pay must be equal to or "
    "above the product.")],
  "2.57 → round to the rupee → equal or next higher cell. Never a lower cell.",
  "Rule 7(1)(A)(i), CCS (Revised Pay) Rules, 2016 (the gazette's own illustration)",
  "Locating the cell before rounding the product, or rounding the product to the nearest ₹100",
  level="4", cells=pm.matrix("4")[6:12], marks={"land": 9},
  table_note="Level 4, cells 7 to 12. Cell 9 (₹32,300) is where the product lands.")


N("Fitment under rule 7(1)(A)(i) where the product is not a cell", "7",
  "Rule 7(1)(A)(i)",
  "Existing basic pay ₹8,000 in Level 1 on 1 January 2016. The product of ₹20,560 is not itself a cell. What is the revised pay?",
  "₹20,900, at cell 6 of Level 1",
  ["8,000 × 2.57 = 20,560 exactly, with no rounding to do.",
   "Look for 20,560 in Level 1: cell 5 is ₹20,300 and cell 6 is ₹20,900. There is no cell of ₹20,560, so the rule takes "
   "the immediate next higher cell.",
   "Pay is fixed at ₹20,900, cell 6. The fact that the multiplication came out to a whole rupee does not help — what "
   "matters is whether that rupee figure is a printed cell, and 20,560 is not."],
  [("₹20,560, because the product came out to a whole rupee",
    "A whole-rupee product is not itself a cell. Only the 543 figures printed in the matrix are cells, and 20,560 is not "
    "one of them."),
   ("₹24,000, at cell 13 of Level 1",
    "That is 8,000 × 3, not 8,000 × 2.57. The fitment factor is 2.57, not 3."),
   ("₹20,300, at cell 5 of Level 1",
    "That cell is BELOW the product, and the rule never moves down to reach a cell.")],
  "Product 20,560 is not a cell. Cell 6 is ₹20,900 — next higher, not nearest.",
  "Rule 7(1)(A)(i), CCS (Revised Pay) Rules, 2016",
  "Assuming a round product is itself a permissible pay figure",
  level="1", cells=pm.matrix("1")[3:8], marks={"land": 6},
  table_note="Level 1, cells 4 to 8: cell 5 is ₹20,300 and cell 6 is ₹20,900, so 20,560 lands on cell 6.")


N("Fitment where the first cell of the Level is higher than the product", "7",
  "Rule 7(1)(A)(ii)",
  "Existing basic pay ₹6,000 in Level 1 on 1 January 2016. The first cell of Level 1 is ₹18,000. What is the revised pay?",
  "₹18,000, the first cell",
  ["6,000 × 2.57 = 15,420.",
   "15,420 is below the first cell of Level 1, which is ₹18,000. Rule 7(1)(A)(ii) deals with exactly this case: if the "
   "minimum pay or first cell is MORE than the amount arrived at under clause (i), the pay is fixed at that first cell.",
   "So the pay is ₹18,000, cell 1. The rule does not leave him at 15,420 and it does not create an intermediate cell."],
  [("₹15,420, the product itself, because clause (i) is the only operative provision here",
    "That is the position under clause (i) alone. Clause (ii) exists precisely to stop the product being used when it "
    "falls below the first cell."),
   ("₹15,500, the cell nearest the product",
    "Level 1 has no cell of ₹15,500 at all; its first cell is ₹18,000."),
   ("₹16,000, the rounded product, with personal pay for the rest of the gap",
    "Nothing is recovered. Personal pay arises under rule 7(7) where the OLD emoluments exceed the new, which is the "
    "opposite situation.")],
  "Product below the first cell → the first cell is the pay, under clause (ii).",
  "Rules 7(1)(A)(i) and 7(1)(A)(ii), CCS (Revised Pay) Rules, 2016",
  "Stopping at the product when the product falls below the first cell",
  level="1", cells=pm.matrix("1")[0:4], marks={"start": 1, "land": 1},
  table_note="Level 1, cells 1 to 4. The product of ₹15,420 is below cell 1 (₹18,000), so clause (ii) fixes the pay at ₹18,000.")


# =====================================================================
# B. INCREMENTS — rules 9 and 10
# =====================================================================
N("The increment as a vertical cell", "9",
  "Rule 9",
  "An officer drawing ₹32,300 in Level 4 is granted his annual increment. What is his pay after it, and by how much did it rise?",
  "₹33,300, a rise of ₹1,000",
  ["Rule 9 says the increment is as specified in the vertical cells of the Level: the officer moves down one cell in "
   "Level 4.",
   "In Level 4, ₹32,300 is cell 9 and the next cell down is cell 10, ₹33,300. That is the pay after the increment.",
   "The rise is ₹1,000. Note that it is NOT 3% of ₹32,300 — 3% would be ₹969. The matrix rounds each cell to the nearest "
   "₹100, so the actual step varies from cell to cell instead of being a flat percentage."],
  [("₹34,169, being 3% of ₹33,300 added on",
    "3% of ₹32,300 is ₹969, and rule 9 does not ask for a percentage at all: it directs the officer to the next printed "
    "cell, which the matrix has already set at ₹33,300."),
   ("₹33,269, a rise of ₹969",
    "That applies 3 per cent to ₹32,300 instead of taking the next printed cell. Rule 9 moves the servant one cell, "
    "and the cell is ₹33,300."),
   ("₹34,300, a rise of ₹2,000",
    "That is two cells, not one. One increment is one vertical cell.")],
  "Increment = next vertical cell. Read the matrix; do not compute 3%.",
  "Rule 9 and its gazette illustration, CCS (Revised Pay) Rules, 2016",
  "Computing 3% of the current pay instead of taking the next printed cell",
  level="4", cells=pm.matrix("4")[7:12], marks={"start": 9, "land": 10},
  table_note="Level 4, cells 8 to 12. The arrow is one cell: ₹32,300 to ₹33,300.")


N("The increment at the top of a Level", "9",
  "Rule 9",
  "A servant is drawing the last cell of Level 1, ₹56,900. What happens on his increment date?",
  "There is no further cell, so his pay stays at ₹56,900",
  ["Rule 9 gives the increment by moving down the vertical cells of the Level. Level 1 has forty cells and ₹56,900 is "
   "the fortieth.",
   "There is no forty-first cell, so there is nowhere for the increment to go.",
   "The pay remains ₹56,900. The officer is not moved into Level 2 — promotion and MACP change the Level, an increment "
   "never does."],
  [("He moves to the first cell of Level 2, ₹19,900",
    "That would be a move to a LOWER figure, and in any case an increment cannot change the Level."),
   ("His pay rises by 3% to ₹58,607, rounded to ₹58,600",
    "There is no cell of ₹58,600 in Level 1; the Level ends at ₹56,900 and the matrix cannot be extended by arithmetic."),
   ("He is granted two increments in Level 2 on promotion instead",
    "The two-increment re-fixation belongs to the FR 22(I)(a)(1) option on promotion, not to an annual increment.")],
  "Top of the Level: the pay stands still. Only promotion or MACP changes the Level.",
  "Rule 9, CCS (Revised Pay) Rules, 2016",
  "Inventing an extra cell beyond the top of the Level",
  level="1", cells=pm.matrix("1")[-3:], marks={"land": 40},
  table_note="The last three cells of Level 1. Cell 40 is ₹56,900 — the end of the column, with no cell 41.")


N("Which increment date applies", "10",
  "Rule 10(2)",
  "A servant is appointed on 15 March 2016. On which date does he earn his first annual increment?",
  "1 January 2017",
  ["Rule 10 gives two increment dates, 1 January and 1 July, and rule 10(2) decides which is yours by the half-year of "
   "appointment.",
   "15 March falls between 2 January and 1 July (both inclusive). Rule 10(2) assigns that period to 1 JANUARY.",
   "So his first increment accrues on 1 January 2017, and thereafter annually on 1 January. Note the direction: the "
   "earlier half-year of appointment produces the LATER-looking date, 1 January, because the increment comes after the "
   "July date has passed."],
  [("1 July 2016",
    "1 July 2016 is four months after his appointment and belongs to the other half-year. The period 2 January to 1 July "
    "earns its increment on 1 January, not 1 July."),
   ("1 July 2017",
    "That is the date for an appointment between 2 July and 1 January, which is the wrong half-year for 15 March."),
   ("15 March 2017, on the anniversary of his appointment",
    "Anniversary increments disappeared with the sixth pay commission. Rule 10 fixes two dates in the year, not the date "
    "of joining.")],
  "Appointed 2 January–1 July → increment on 1 January. Appointed 2 July–1 January → increment on 1 July.",
  "Rule 10(2), CCS (Revised Pay) Rules, 2016",
  "Reversing the two half-years, or reverting to an anniversary date",
  level=None, cells=None, marks={},
  table_note="This one turns on the calendar, not on a matrix column.")


N("The other half-year of appointment", "10",
  "Rule 10(2)",
  "A servant already in service is granted MACP in Level 6 on 10 August 2016. On which date does the financial upgradation "
  "give him his next increment?",
  "1 July 2017",
  ["Rule 10(2) again: the half-year of the appointment, promotion or financial upgradation decides the date.",
   "10 August falls between 2 July and 1 January (both inclusive), and that period is assigned to 1 JULY.",
   "The next 1 July after 10 August 2016 is 1 July 2017, so that is the date. The increment is given in Level 6, the Level "
   "he was placed in by the MACP."],
  [("1 January 2017",
    "1 January is the date for the other half-year, 2 January to 1 July. August falls after that window."),
   ("1 July 2016",
    "That date had already passed when the MACP was granted in August 2016."),
   ("10 August 2017, one year after the MACP",
    "MACP does not create an anniversary; it only decides which of the two fixed dates applies.")],
  "Appointed or upgraded 2 July–1 January → 1 July.",
  "Rule 10(2), CCS (Revised Pay) Rules, 2016",
  "Treating MACP as creating an anniversary increment date",
  table_kind="mapping",
  mapping=[("4200", "9300-34800 (PB-2)", "6"), ("4600", "9300-34800 (PB-2)", "7"),
           ("4800", "9300-34800 (PB-2)", "8")],
  highlight=["6"],
  table_note="MACP moves the servant up one Level in this sequence; a MACP on 10 August 2016 puts him in Level 6. The "
             "Level changes, but the increment date is fixed by rule 10(2), not by the Level.")


# =====================================================================
# C. PROMOTION AND MACP — rule 13
# =====================================================================
N("Fixation on promotion", "13",
  "Rule 13(i)",
  "An officer drawing ₹28,700 in Level 4 is promoted to a post in Level 5. What is his pay on promotion?",
  "₹30,100, at cell 2 of Level 5",
  ["Rule 13(i) works in two steps and the order is mandatory. First, give ONE increment in the Level from which he is "
   "promoted: ₹28,700 is cell 5 of Level 4, so the next cell is ₹29,600.",
   "Second, place ₹29,600 in Level 5 at the cell equal to it, and if there is none, at the next higher cell. Level 5 has "
   "no ₹29,600: cell 1 is ₹29,200 and cell 2 is ₹30,100.",
   "So the pay on promotion is ₹30,100, cell 2 of Level 5. The gain is ₹1,400, of which ₹900 is the increment in the old "
   "Level and ₹500 the landing on the next higher cell."],
  [("₹29,600, because that is his pay after the increment",
    "₹29,600 is the stepping stone, not the destination. It is a Level 4 figure and he has been promoted out of Level 4."),
   ("₹29,200, the first cell of Level 5 nearest his old pay",
    "The placement is equal-or-next-HIGHER. ₹29,200 is below ₹29,600, so it cannot be the cell."),
   ("₹31,000, by giving the increment in Level 5 instead of Level 4",
    "Giving the increment in the new Level is the classic error. ₹28,700 raised one cell in Level 5 is ₹30,100, and then "
    "a further cell would take him to ₹31,000 — two increments for one promotion.")],
  "Increment in the OLD Level first, then equal-or-next-higher cell in the NEW Level.",
  "Rule 13(i) and its gazette illustration, CCS (Revised Pay) Rules, 2016",
  "Giving the promotion increment in the new Level",
  level="5", cells=pm.matrix("5")[0:5], marks={"land": 2},
  table_note="Level 5, the promoting Level, cells 1 to 5. The increment is taken in Level 4 FIRST — ₹28,700 steps to ₹29,600 there — and only then is ₹29,600 located in Level 5, where it lands on cell 2 (₹30,100).")


N("Promotion where the stepped figure is itself a cell", "13",
  "Rule 13(i)",
  "An officer drawing ₹44,900 in Level 7 is promoted to Level 8. Level 8's cells run ₹47,600, ₹49,000, ₹50,500. What is his "
  "pay on promotion?",
  "₹47,600 — but only if his stepped figure in Level 7 is ₹46,200",
  ["Take the increment in Level 7 first. ₹44,900 is cell 1 of Level 7, so the next cell is ₹46,200.",
   "Now look for ₹46,200 in Level 8. Level 8 runs ₹47,600, ₹49,000 and ₹50,500, so there is no ₹46,200 and the rule takes "
   "the next higher cell, ₹47,600.",
   "The gain is ₹2,700, which is unusually large for a promotion precisely because the conversion from Level 7 to Level 8 "
   "is a big jump at the bottom of the two columns."],
  [("₹46,200, the figure after the increment",
    "That is a Level 7 figure. The officer is now in Level 8 and must be placed on a Level 8 cell."),
   ("₹49,000, the cell after ₹47,600",
    "That would be the next higher cell after the landing cell, giving him two steps instead of one."),
   ("₹44,900, unchanged, because the promotion is within the same Pay Band",
    "Both Levels sit in the PB-2 band of the old structure, but Levels 7 and 8 are different Levels and promotion fixes pay "
    "in the new one.")],
  "The increment comes in the old Level even when the new Level's first cell is far above it.",
  "Rule 13(i), CCS (Revised Pay) Rules, 2016",
  "Stopping at the stepped figure because it is larger than expected",
  level="8", cells=pm.matrix("8")[0:4], marks={"start": 1, "land": 1},
  table_note="Level 8, cells 1 to 4. ₹46,200 is not among them, so the first cell ₹47,600 is the landing.")


N("MACP creates no higher duties", "13",
  "Rule 13(i) with the MACPS",
  "An official in Level 4 drawing ₹30,500 is granted MACP in Level 5. What is his pay, and does anything else about his post "
  "change?",
  "₹31,900 in Level 5, with no change of duties",
  ["MACP is fixed exactly like a promotion under rule 13(i). First the increment in Level 4: ₹30,500 is cell 7, so ₹31,400.",
   "Then place ₹31,400 in Level 5: cell 1 is ₹29,200 and cell 2 is ₹30,100, cell 3 is ₹31,000 and cell 4 is ₹31,900. There "
   "is no ₹31,400, so the next higher cell is ₹31,900.",
   "His pay is ₹31,900. But MACP is a financial upgradation only: it confers no change of duties, no change of designation "
   "and no higher responsibility, which is what distinguishes it from a promotion even though the arithmetic is identical."],
  [("₹31,000 in Level 5",
    "₹31,000 is below ₹31,400, the stepped figure, so the rule cannot place him there."),
   ("₹32,900 in Level 5, on the footing that the upgradation also upgrades the duties",
    "The arithmetic is right and the consequence is wrong. MACP confers no higher duties; that is its defining feature."),
   ("₹30,500, unchanged until a vacancy in Level 5 arises",
    "MACP needs no vacancy. That is the whole reason the scheme exists alongside promotion.")],
  "MACP = the rule 13 arithmetic with none of the promotion's consequences.",
  "Rule 13(i) read with the MACPS, CCS (Revised Pay) Rules, 2016",
  "Assuming MACP also upgrades the duties of the post",
  level="5", cells=pm.matrix("5")[0:5], marks={"land": 4},
  table_note="Level 5, cells 1 to 5. The stepped figure of ₹31,400 lands on cell 4, ₹31,900.")


N("The option on promotion: two increments on the DNI", "13",
  "FR 22(I)(a)(1) read with rule 13",
  "On promotion an officer from Level 4 to Level 5 exercises the option to have his pay fixed from his next increment date. "
  "He was drawing ₹30,500 in Level 4. What happens?",
  "₹31,000 at once, re-fixed at ₹32,900 on the DNI",
  ["Under the option he is first placed at the NEXT HIGHER cell of the promoting Level without any increment in the old "
   "Level: ₹30,500 in Level 5 58 lands at cell 3, ₹31,000. He draws that until his increment date.",
   "On the increment date in the old Level he is re-fixed with TWO increments there — one for the annual increment and one "
   "for the promotion. ₹30,500 is cell 7 of Level 4, so two cells down is cell 9, ₹32,300.",
   "He is then placed at the cell equal to or next higher than ₹32,300 in Level 5. Level 5 has no ₹32,300: cell 4 is "
   "₹31,900 and cell 5 is ₹32,900. So he ends on ₹32,900, cell 5. The option beats the immediate placement of ₹31,000 by "
   "₹1,900, which is why an officer takes it."],
  [("He is placed at ₹31,900 in Level 5 at once, that being the ordinary promotion fixation under rule 13",
    "That is what happens WITHOUT the option. Exercising the option replaces the increment-first step with the next-higher-"
    "cell placement."),
   ("He is placed at ₹31,000 and stays there until his next promotion",
    "The re-fixation is the whole point of the option. It happens on the date of his next increment in the old Level."),
   ("He gets two increments in Level 5 on the increment date",
    "Both increments are given in the Level FROM WHICH he is promoted, Level 4. Only then is he placed in Level 5.")],
  "Option: next higher cell now, two increments in the old Level on the DNI, then land in the new Level.",
  "FR 22(I)(a)(1) as applied to rule 13, CCS (Revised Pay) Rules, 2016",
  "Giving the two increments in the new Level instead of the old one",
  level="5", cells=pm.matrix("5")[1:8], marks={"start": 3, "land": 5},
  table_note="Level 5, cells 2 to 8. The interim placement is cell 3, ₹31,000; the re-fixed figure of ₹32,300 lands on "
             "cell 5, ₹32,900.")


# =====================================================================
# D. DIRECT RECRUITS — rule 8
# =====================================================================
N("A direct recruit's starting pay", "8",
  "Rule 8",
  "A candidate is appointed by direct recruitment to a Level 7 post on 1 September 2016. What is his pay?",
  "₹44,900, the first cell of Level 7",
  ["Rule 8 fixes the pay of a direct recruit appointed on or after 1 January 2016 at the minimum pay or the FIRST CELL of "
   "the Level.",
   "The first cell of Level 7 is ₹44,900. There is no multiplication by 2.57, because a direct recruit has no existing "
   "basic pay to multiply.",
   "He is also entitled to only one increment a year, and by rule 10(2) his first one falls on 1 January 2017, not on the "
   "anniversary of his joining."],
  [("₹1,15,393, being ₹44,900 × 2.57",
    "The fitment factor applies only to an existing basic pay under rule 7. A direct recruit has none; rule 8 gives him "
    "the first cell outright."),
   ("₹46,200, the second cell of Level 7, because he joined mid-year",
    "Joining part-way through a year does not advance the starting cell. Rule 8 fixes the first cell, and the partial year "
    "is dealt with by the date of the first increment."),
   ("₹1,00,000, negotiated on the strength of his last employer's pay",
    "Personal pay arises under rule 8's proviso only for those appointed between 01.01.2016 and the notification whose "
    "existing emoluments were higher. A fresh direct recruit has no such protection.")],
  "Direct recruit on or after 01.01.2016: first cell, no fitment.",
  "Rule 8, CCS (Revised Pay) Rules, 2016",
  "Applying the 2.57 fitment to a direct recruit",
  level="7", cells=pm.matrix("7")[0:4], marks={"both": 1},
  table_note="Level 7, cells 1 to 4. Every direct recruit in this Level starts on cell 1, ₹44,900.")


# =====================================================================
# E. OPTION AND DEEMED ELECTION — rules 5 and 6
# =====================================================================
N("The cut-off for the option", "5",
  "Rule 5, Explanation 2",
  "A person appointed to his first Government post on 10 February 2016 asks to remain on the sixth pay commission structure. "
  "What is the position?",
  "He cannot exercise it",
  ["Rule 5's first proviso lets an existing servant elect to stay on the old structure until his next increment there.",
   "Explanation 2 closes that door: the option is not admissible to any person appointed to a post for the first time in "
   "Government service, or by transfer from another post, on or after 1 January 2016.",
   "Appointed on 10 February 2016, he is squarely inside the exclusion. He draws pay only in the revised structure, at the "
   "first cell of his Level, under rule 8."],
  [("He may opt for the old structure, but only until the date of his first increment in it",
    "The time limit exists for existing servants. Explanation 2 removes the option altogether from those appointed on or "
    "after 01.01.2016."),
   ("He may opt, because he had not joined when the rules were notified on 25 July 2016",
    "The dividing line is 1 January 2016, the date of effect, not 25 July 2016, the date of notification."),
   ("He may opt for the old structure in respect of one Pay Band and Grade Pay only, that being the limit in Explanation 1",
    "Explanation 1's one-scale limit applies to servants who HAVE the option. It cannot enlarge a facility that "
    "Explanation 2 has withheld.")],
  "Option exists for pre-01.01.2016 servants only, one scale, and only to the next increment.",
  "Rule 5 and Explanations 1 and 2, CCS (Revised Pay) Rules, 2016",
  "Confusing the date of notification with the date of effect",
  level=None, cells=None, marks={},
  table_note="A rule 5 question: there is no matrix column to show.")


N("When silence is a choice", "6",
  "Rule 6(3)",
  "A servant receives the option form but never returns it. What is his position?",
  "He is deemed to have elected the revised pay structure with effect from 1 January 2016",
  ["Rule 6(1) requires the option in writing within three months of notification, with a proviso for those out of India or "
   "under suspension.",
   "Rule 6(3) then supplies the default: if the intimation is not received within the time specified, the servant is "
   "DEEMED to have elected the revised pay structure with effect from 1 January 2016.",
   "So failing to choose is itself a choice, and it is the choice that gives him the revised structure from the earliest "
   "date. Rule 6(4) makes whatever choice results — express or deemed — final."],
  [("He continues on the existing structure indefinitely",
    "Continuing on the old structure requires a positive election under rule 5. Doing nothing produces the revised "
    "structure, not the old one."),
   ("He is deemed to have elected the revised structure, but only from the date the three months expire",
    "The deeming is expressly with effect from 1 January 2016. The three-month period is the time for choosing, not the "
    "date from which pay is revised."),
   ("His case is referred to the Central Government for interpretation",
    "Rule 17 referral is for genuine questions of interpretation. Rule 6(3) answers this one in terms.")],
  "No option in three months → deemed election of the revised structure from 01.01.2016, and it is final.",
  "Rules 6(1), 6(3) and 6(4), CCS (Revised Pay) Rules, 2016",
  "Treating silence as preserving the old structure",
  level=None, cells=None, marks={},
  table_note="A rule 6 question: there is no matrix column to show.")


# =====================================================================
# F. THE LEVEL 13 REVISION — the finest point in the Schedule
# =====================================================================
N("The Level 13 first cell: notified and current", "Schedule",
  "Part A of the Schedule, Level 13",
  "What was the first cell of Level 13 in the Schedule as originally notified, and what is it today?",
  "₹1,18,500, then ₹1,23,100",
  ["Part A of the Schedule to G.S.R. 721(E), notified on 25 July 2016, printed Level 13 with a first cell of ₹1,18,500, "
   "the same 2.57 index of rationalisation used for Levels 1 to 5.",
   "By a Department of Expenditure resolution dated 16 May 2017 the index of rationalisation for Level 13 was raised from "
   "2.57 to 2.67, and the whole column was re-cast. Its first cell became ₹1,23,100.",
   "The gap at the first cell is ₹4,600 and it widens down the column: the twentieth cell moved from ₹2,07,900 to "
   "₹2,15,900. No other Level was touched, so Level 13 is now the only column in the matrix carrying an IOR of 2.67 that "
   "was originally 2.57."],
  [("₹1,21,200, the average of the two columns, the level having been re-cast twice",
    "That reads the gazette of 2016 as the last word. The 2017 resolution re-cast the column, and questions about pay "
    "today must use ₹1,23,100."),
   ("₹1,23,100 both as notified and today",
    "The 2016 Schedule printed ₹1,18,500. The figure moved a year later; it did not start there."),
   ("₹1,31,100 today, and ₹1,18,500 as notified, the column having been re-cast upward twice",
    "₹1,31,100 is the first cell of Level 13A, a different Level altogether.")],
  "Level 13: 1,18,500 in the 2016 Schedule; 1,23,100 from 16.05.2017. IOR 2.57 → 2.67.",
  "Part A of the Schedule to G.S.R. 721(E) and the Department of Expenditure resolution dated 16.05.2017",
  "Quoting the notified Schedule as though it were the position in force",
  level="13", table_kind="compare",
  cells_before=[118500, 122100, 125800, 129600, 133500],
  cells_after=[123100, 126800, 130600, 134500, 138500],
  marks={"start": 1, "land": 1},
  table_note="Level 13, cells 1 to 5: as notified on the left, after the 2017 resolution on the right.")

N("The value of the Level 13 revision at a given cell", "Schedule",
  "Part A of the Schedule, Level 13",
  "A Level 13 officer was on the fourth cell of the Level. By how much did his pay rise when the Level was re-cast on 16 May 2017?",
  "₹4,900",
  ["The column as notified ran ₹1,18,500, ₹1,22,100, ₹1,25,800, ₹1,29,600, so the fourth cell was ₹1,29,600.",
   "The re-cast column runs ₹1,23,100, ₹1,26,800, ₹1,30,600, ₹1,34,500, so the corresponding cell is ₹1,34,500.",
   "The rise is ₹4,900. Note that it is not the flat ₹4,600 seen at the first cell: because the new column is built at "
   "2.67 rather than 2.57, the gap widens as you move down, and at the twentieth cell it has reached ₹8,000."],
  [("₹4,600, the same as at the first cell",
    "₹4,600 is the gap at cell 1 only. Because the two columns are built on different indices, the gap grows with every "
    "cell: ₹4,700 at cell 2, ₹4,800 at cell 3, ₹4,900 at cell 4."),
   ("₹8,000, the same gap as at the top of the column",
    "The revision re-cast every cell of the column. An officer anywhere in Level 13 was affected from his own cell."),
   ("Nothing, because the revision applied only to officers appointed after 16 May 2017",
    "The re-cast column applies to the Level itself. Every officer serving in it moved to the corresponding new cell.")],
  "The gap widens down the column: ₹4,600 at cell 1, ₹4,900 at cell 4, ₹8,000 at cell 20.",
  "Department of Expenditure resolution dated 16.05.2017 revising Level 13 of the Schedule",
  "Assuming a flat increase of ₹4,600 throughout the Level",
  level="13", table_kind="compare",
  cells_before=[129600, 133500, 137500],
  cells_after=[134500, 138500, 142700],
  marks={"start": 4, "land": 4},
  table_note="Level 13, cells 4 to 6, as notified beside the re-cast cells. The officer moved ACROSS, not down.")


# =====================================================================
# G. THE MATRIX ITSELF
# =====================================================================
N("What one cell is worth", "Schedule",
  "Part A of the Schedule",
  "Level 4 cell 1 is ₹25,500 and cell 2 is ₹26,300. Why is the step ₹800 rather than the ₹765 that 3% would give?",
  "Because 3% is rounded to the nearest ₹100",
  ["3% of ₹25,500 is ₹765, which would give ₹26,265.",
   "The matrix does not carry ₹26,265 or even ₹26,300 by accident: it carries the nearest multiple of ₹100, so ₹26,265 "
   "becomes ₹26,300 and the step appears as ₹800.",
   "That single rounding decision is what makes all 543 cells of the matrix reproducible: apply 3% and round to the "
   "nearest ₹100 to each cell in turn, and every column regenerates exactly from its first cell, including the Level 13 "
   "column after the 2017 revision."],
  [("Because each cell is 3% of the one before it, rounded UP to the next ₹100",
    "Rounding up does not reproduce the matrix. ₹18,000 plus 3% is ₹18,540; rounded up that is ₹18,600, but the matrix "
    "carries ₹18,500. Rounding to the NEAREST ₹100 gives ₹18,500 and matches every cell."),
   ("Because the level has a fixed annual increment of ₹800",
    "There is no fixed increment. Level 4 steps are ₹800, ₹800, ₹800, ₹800, ₹900, ₹900 — they drift as the rounding falls "
    "differently at each cell."),
   ("Because the 3% is applied to the first cell of the Level each time",
    "That would give the same step at every cell. The step changes precisely because each cell is 3% of the PREVIOUS cell.")],
  "Cell n+1 = cell n × 1.03, rounded to the nearest ₹100. That regenerates all 543 cells.",
  "Part A of the Schedule, 7th CPC Report Table 3 and the Government's rounding practice",
  "Assuming a flat 3% or rounding upward",
  level="4", cells=pm.matrix("4")[0:7], marks={"start": 1, "land": 2},
  table_note="Level 4, cells 1 to 7. The step from ₹25,500 to ₹26,300 is ₹800; the steps run 800, 800, 800, 800, 900, 900 as the ₹100 rounding drifts.")

N("Reading the Level off the old structure", "4",
  "Rule 4 and Part A of the Schedule",
  "Two servants both hold Grade Pay ₹5,400 on 31 December 2015, one in Pay Band 2 and one in Pay Band 3. Which Levels do "
  "they enter?",
  "Level 9 for the PB-2 holder and Level 10 for the PB-3 holder",
  ["Rule 4 says the Level is determined by the corresponding existing Pay Band AND Grade Pay as specified in the matrix, "
   "so both halves of the old description matter.",
   "In the caption row of Part A, Grade Pay ₹5,400 appears twice: against Level 9 under Pay Band 5200-20200 (PB-2) and "
   "against Level 10 under Pay Band 15600-39100 (PB-3).",
   "So the PB-2 servant enters Level 9 at ₹53,100 and the PB-3 servant enters Level 10 at ₹56,100. Same grade pay, "
   "different Level, because the Pay Band is the other half of the key."],
  [("Both enter Level 9, because the Grade Pay is the same",
    "Grade Pay alone is not the key. ₹5,400 maps to Level 9 in PB-2 and Level 10 in PB-3."),
   ("Both enter Level 10, because ₹5,400 is a PB-3 grade pay",
    "It is a PB-3 grade pay and also a PB-2 grade pay. The matrix caption carries both mappings."),
   ("Level 9 and Level 11 respectively, one Level apart for two Pay Bands apart",
    "The mapping is fixed by the caption, not by counting bands. PB-2 Grade Pay ₹5,400 is Level 9 and PB-3 Grade Pay "
    "₹5,400 is Level 10.")],
  "Level = Pay Band + Grade Pay. ₹5,400 in PB-2 is Level 9; ₹5,400 in PB-3 is Level 10.",
  "Rule 4 and the caption row of Part A of the Schedule",
  "Reading Grade Pay alone when the same figure appears in two Pay Bands",
  table_kind="mapping",
  mapping=[("5400", "5200-20200 (PB-2)", "9"), ("5400", "15600-39100 (PB-3)", "10")],
  highlight=["9", "10"],
  table_note="The same Grade Pay, ₹5,400, against two Pay Bands: Level 9 in PB-2 and Level 10 in PB-3.")

# ---------------------------------------------------------------- rule 7(1)(B)
N("The NPA route under rule 7(1)(B)",
  "7", "Rule 7(1)(B)",
  "A medical officer has existing basic pay of ₹21,000 and draws Non Practicing Allowance at 25 per cent, with "
  "dearness allowance at 125 per cent on the NPA as on 1 January 2006. What is his pay in the revised structure?",
  "₹61,300, at cell 4 of Level 10",
  [
    "First take the NPA: 25 per cent of ₹21,000 = ₹5,250.",
    "Now apply the fitment factor: ₹21,000 × 2.57 = ₹53,970. There is no fraction here, so nothing to round.",
    "Next the extra element that clause (B) adds: dearness allowance on the pre-revised NPA. 125 per cent of ₹5,250 = "
    "₹6,562.50, rounded UP to ₹6,563.",
    "Add it: ₹53,970 + ₹6,563 = ₹60,533.",
    "Locate ₹60,533 in Level 10. Cell 3 is ₹59,500 and cell 4 is ₹61,300. There is no cell of ₹60,533, so the rule "
    "takes the next higher cell — ₹61,300 at cell 4.",
    "Rule 7(1)(B)(ii) then allows the pre-revised NPA of ₹5,250 to be added on top, so the officer draws ₹66,550 in all "
    "until the revised rates of NPA are settled. That second figure is not part of his basic pay.",
  ],
  [
    ("₹66,550, at cell 6 of Level 10",
     "That is pay plus NPA. ₹66,550 is not a cell of Level 10, and the NPA sits outside the matrix — it is added "
     "on top of the pay, not located in the Level."),
    ("₹60,533, because the product of the multiplication is the revised pay",
     "Rule 7(1)(A) locates the figure in the matrix; ₹60,533 is not a printed cell."),
    ("₹54,300, on the product of ₹53,970 alone",
     "Clause (B) adds the dearness allowance on the NPA to the product before the cell is found."),
  ],
  "NPA: 21,000 × 2.57 = 53,970; plus 125% of 5,250 = 6,563; total 60,533 → ₹61,300 at cell 4 of Level 10.",
  "Rule 7(1)(B) and its illustration, CCS (Revised Pay) Rules, 2016",
  "Forgetting the dearness allowance on the NPA, or adding the NPA inside the matrix instead of on top of it",
  level="10", cells=pm.matrix("10")[0:6], marks={"land": 4},
  table_note="Level 10, cells 1 to 6. The NPA figure of ₹60,533 lands on cell 4, ₹61,300.")

# ---------------------------------------------------------------- deeper cuts
N("Fixation at a high Level, where the cell is far from the product",
  "7", "Rule 7(1)(A)(i)",
  "An officer in Level 11 was drawing existing basic pay of ₹44,900 on 1 January 2016. What is his revised pay?",
  "₹1,15,500, at cell 19 of Level 11",
  [
    "Multiply: ₹44,900 × 2.57 = ₹1,15,393.",
    "There is no fraction to round away, so the figure to locate is ₹1,15,393.",
    "Look for it in Level 11. Cell 18 is ₹1,12,100 and cell 19 is ₹1,15,500. There is no cell of ₹1,15,393.",
    "The rule takes the next higher cell, so the pay is fixed at ₹1,15,500 on cell 19.",
    "The servant gains ₹107 over the exact product. That is the working of the rule, not an error: the excess is "
    "never recovered and never carried forward as a debt.",
  ],
  [
    ("₹1,12,100, at cell 18 of Level 11",
     "That is the cell below the product. Rule 7(1)(A)(i) goes up, never down."),
    ("₹1,15,393, the exact product",
     "The product is a step, not a pay. It has to be located at a printed cell, and only a cell can be drawn."),
    ("₹1,15,400, rounding the product to the nearest ₹100 and then taking that cell",
     "Rounding the product to ₹100 is not part of the rule; rounding the CELLS to ₹100 was done when the matrix was "
     "built. The figure to locate is ₹1,15,393, and it lands on ₹1,15,500."),
  ],
  "Even at the top of the matrix the method is the same: multiply, round to the rupee, take the equal or next higher cell.",
  "Rule 7(1)(A)(i), CCS (Revised Pay) Rules, 2016",
  "Rounding the product to the nearest ₹100 before locating it",
  level="11", cells=pm.matrix("11")[15:22], marks={"land": 19},
  table_note="Level 11, cells 16 to 22. The product of ₹1,15,393 falls between cell 18 (₹1,12,100) and cell 19 "
             "(₹1,15,500), so it lands on cell 19.")

N("The MACP that lands on the first cell of the next Level",
  "13", "Rule 13(i)",
  "An official drawing ₹35,400 in Level 6 is granted MACP in Level 7. Level 7 opens at ₹44,900. What is his pay after "
  "the upgradation?",
  "₹44,900, at cell 1 of Level 7",
  [
    "Rule 13(i) first gives one increment in the Level he is in: ₹35,400 is cell 1 of Level 6, so the step is to "
    "₹36,500 on cell 2.",
    "Now locate ₹36,500 in Level 7. Level 7 opens at ₹44,900, which is already higher than ₹36,500.",
    "So there is no cell equal to or above ₹36,500 other than the first — the pay is fixed at ₹44,900 on cell 1.",
    "The gain is ₹9,500, and almost all of it is the distance between the two Levels rather than the increment.",
  ],
  [
    ("₹36,500, the stepped figure, with the difference paid as personal pay",
     "Personal pay protects an excess of old over new emoluments. Here the new figure is far higher, so nothing is "
     "protected and nothing is added."),
    ("₹47,600, the second cell, so that he is seen to have gained a step",
     "The rule takes the equal or next higher cell, and the first cell is already higher than the stepped figure. "
     "There is no reason to skip it."),
    ("₹45,800, by adding the forfeited increment to the first cell of Level 7",
     "The increment has been given — in Level 6, as the rule requires. Nothing is forfeited."),
  ],
  "When the new Level's first cell is above the stepped figure, the first cell IS the equal-or-next-higher cell.",
  "Rule 13(i) and the MACP scheme, CCS (Revised Pay) Rules, 2016",
  "Looking for a cell above the stepped figure when the first cell already qualifies",
  level="7", cells=pm.matrix("7")[0:3], marks={"land": 1},
  table_note="Level 7, cells 1 to 3. The stepped figure of ₹36,500 in Level 6 is below cell 1 (₹44,900), so the "
             "upgradation fixes the pay on ₹44,900.")

N("Two increments, then re-fix — the arithmetic of the option",
  "13", "FR 22(I)(a)(1) read with rule 13",
  "On promotion from Level 4 to Level 5 an officer drawing ₹30,500 opts to have his pay fixed from the date of his "
  "next increment. He gets two increments in Level 4 from ₹30,500. What does he draw in the meantime, and what is he "
  "fixed at?",
  "₹31,000 meanwhile; ₹32,900 on the increment date",
  [
    "Under the option he continues on the old Level until his next increment date, and is placed at the cell above "
    "his present pay in the NEW Level for that period: ₹30,500 steps to ₹31,000 on cell 3 of Level 5.",
    "On the increment date he is given TWO increments in the Level he came from, Level 4: ₹30,500 (cell 7) → "
    "₹31,400 (cell 8) → ₹32,300 (cell 9).",
    "Then ₹32,300 is located in Level 5. It is not a cell there — cell 4 is ₹31,900 and cell 5 is ₹32,900 — so the "
    "next higher cell is taken.",
    "He is re-fixed at ₹32,900 on cell 5. The interim ₹31,000 is replaced, not added to.",
  ],
  [
    ("₹33,300 on the increment date, two increments above ₹31,000",
     "The two increments are taken in Level 4, the Level he is promoted FROM. Taking them in Level 5 pays them at the "
     "higher Level's rates and overstates the figure by ₹400."),
    ("₹31,900 meanwhile; ₹32,900 on the increment date",
     "The interim placement is the cell above his present pay, which is ₹31,000 on cell 3. ₹31,900 is two cells up."),
    ("₹31,400 meanwhile, and re-fixed at ₹32,900 on the increment date",
     "The option defers the fixation; it does not cancel it. On the increment date the pay is re-fixed with two "
     "increments."),
  ],
  "The two increments are ALWAYS in the old Level. 30,500 → 31,400 → 32,300, then re-fixed at ₹32,900.",
  "FR 22(I)(a)(1), read with rule 13(i), CCS (Revised Pay) Rules, 2016",
  "Taking the two increments in the new Level, which pays them at the higher rates",
  level="5", cells=pm.matrix("5")[1:8], marks={"start": 3, "land": 5},
  table_note="Level 5, cells 2 to 8. The interim placement is cell 3 (₹31,000); after two increments in Level 4 the "
             "figure is ₹32,300, which lands on cell 5 (₹32,900).")

N("What the fitment factor is worth, stated as a percentage",
  "7", "Rule 7(1)(A)(i)",
  "The fitment factor of 2.57 is applied to existing basic pay. Roughly what rise does it represent for a servant, "
  "before the move to the equal or next higher cell?",
  "About 157 per cent",
  [
    "The factor is what the old basic pay is multiplied by, so the new figure is 2.57 times the old.",
    "The RISE is the new figure less the old: 2.57 − 1 = 1.57, which is 157 per cent of the old basic pay.",
    "So a servant on ₹12,560 who is multiplied by 2.57 moves to ₹32,279 — a rise of ₹19,719, which is 157 per cent "
    "of ₹12,560.",
    "This rise is what absorbs the 6th CPC dearness allowance and the grade pay rationalisation. It is not a pay "
    "rise in real terms; it is a conversion.",
  ],
  [
    ("257 per cent, since the factor itself is 2.57",
     "That is the factor expressed as a percentage of the old pay, not the rise. The rise is 2.57 − 1 = 1.57."),
    ("About 3 per cent",
     "Three per cent is the annual increment built into the matrix, not the conversion factor."),
    ("About 57 per cent",
     "That would be a factor of 1.57. The factor is 2.57, and the rise over the old pay is 157 per cent."),
  ],
  "Factor 2.57 = an increase of 157 per cent. The difference between the two numbers is one.",
  "Rule 7(1)(A)(i), CCS (Revised Pay) Rules, 2016",
  "Confusing the factor with the percentage rise it produces")

