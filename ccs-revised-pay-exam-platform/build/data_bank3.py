#!/usr/bin/env python3
"""data_bank3.py — the third tranche: the provisions the first two tranches left untested.

Every item here is anchored to a sub-rule of the statute that no question reached
before, or to a DoPT FAQ that settles a point the rule leaves open. Rule 7(3), (4)
and (10)(i)(a)–(d), rule 11 and rule 14 had no coverage at all; 7(10)(ii) and rule
1(1) had none. Nothing is invented: each stem is answerable from the verbatim text
in verbatim.py.

The FAQ items carry faq=True and a source line naming the authority that published
the answer, so the platform can show them as a separate, sourced FAQ library.
"""
from __future__ import annotations

import paymatrix as pm

FACTS = []


def Q(fid, rule, rules_text, topic, stem, ans, d1, d2, d3, why, safe, src, trap,
      level=None, cells=None, marks=None, tag="Tough", faq=False, faq_no=None):
    FACTS.append(dict(id=fid, rule=rule, rules_text=rules_text, topic=topic, q=stem,
                      a=ans, d=[d1, d2, d3], why=why, safe=safe, src=src, trap=trap,
                      level=level, cells=cells, marks=marks or {}, tag=tag,
                      table_note=None, table_kind=None, cells_before=None,
                      cells_after=None, mapping=None, highlight=None,
                      before_label=None, after_label=None,
                      faq=faq, faq_no=faq_no))


# ------------------------------------------------------------------ rule 7(3)
# Leave with leave salary: the servant is on leave, so there is no "pay drawn"
# to fix; the fixation is done on the leave salary.
Q("RB-036", "7", "Rule 7(3)", "Fixation on leave with leave salary",
  "A servant is on earned leave with leave salary on 1 January 2016. His pay in the revised structure is fixed:",
  "On the leave salary admissible to him on that date",
  ("On the pay he last drew before proceeding on leave",
   "That is the position where the leave was without leave salary; here the rule speaks of leave salary."),
  ("Only when he returns to duty, from the date of return",
   "Rule 7(3) fixes the pay on 1 January 2016; the return to duty does not postpone the fixation."),
  ("At the first cell of the Level, because he was not on duty",
   "The first cell is the rule 7(1)(A)(ii) floor, not a rule for servants on leave."),
  "Rule 7(3) deals with a servant who is on leave on 1 January 2016 and is entitled to leave salary. The pay in the "
  "revised structure is fixed on the leave salary admissible to him on that date, and not on the pay of the post, "
  "because for that period the leave salary is the emolument he draws. Rule 7(4) does the same for study leave, and "
  "rule 7(5) for suspension on subsistence allowance. The three sub-rules are one idea: fix on what is actually being "
  "paid, not on what the post would have paid.",
  "On leave with leave salary on 01.01.2016: fix the pay on the leave salary.",
  "Rule 7(3), CCS (Revised Pay) Rules, 2016",
  "Fixing the pay on the pay of the post when the servant was on leave with leave salary")

# ------------------------------------------------------------------ rule 7(4)
Q("RB-037", "7", "Rule 7(4)", "Fixation during study leave",
  "A servant was on study leave with study leave allowance on 1 January 2016. Rule 7(4) requires his pay to be fixed:",
  "On the study leave allowance admissible to him",
  ("On the pay of the post, because study leave counts as duty",
   "Study leave does not count as duty for pay; the sub-rule fixes the pay on the allowance."),
  ("At the minimum of the Level, since he was not discharging duty",
   "The rule gives a specific basis — the allowance — and the minimum is not it."),
  ("After the study leave ends, with retrospective effect from 1 January 2016",
   "The fixation is made on 1 January 2016; the retrospectivity is inherent in rule 1(2), not a postponement."),
  "Rule 7(4) treats study leave exactly as rule 7(3) treats leave with leave salary: the pay in the revised "
  "structure is fixed on the study leave allowance admissible on 1 January 2016. The reason is the same — during "
  "study leave the servant is not drawing the pay of the post, and the revised structure must be applied to the "
  "emolument he is actually receiving. Rule 7(5) completes the trio for a servant under suspension, whose "
  "subsistence allowance is likewise the basis.",
  "Study leave: fix on the study leave allowance.",
  "Rule 7(4), CCS (Revised Pay) Rules, 2016",
  "Treating study leave as duty and fixing the pay on the post")

# ------------------------------------------------------------------ rule 7(5)
Q("RB-038", "7", "Rule 7(5)", "Fixation while under suspension",
  "A servant was under suspension on 1 January 2016 and drawing subsistence allowance. On the revised structure he is:",
  "Fixed on the subsistence allowance, and paid that amount until the suspension is revoked",
  ("Fixed on the pay of the post, since suspension does not reduce his substantive pay",
   "Suspension does reduce what he draws; the sub-rule fixes on the subsistence allowance."),
  ("Not fixed at all until he is reinstated, when the fixation is done with retrospective effect",
   "The sub-rule fixes the pay on 1 January 2016, on the subsistence allowance, and the difference is settled on "
   "reinstatement."),
  ("Fixed at the first cell of the Level until reinstatement",
   "The first cell is a floor for a servant with no comparable pay, not the rule for a suspended servant."),
  "Rule 7(5) provides that a servant under suspension on 1 January 2016 shall have his pay fixed on the subsistence "
  "allowance admissible to him, and shall continue to draw that amount until the suspension is revoked. On "
  "reinstatement the pay is re-fixed under rule 7(1)(A) from 1 January 2016 and the arrears follow — but the "
  "interim position is the subsistence allowance, not the pay of the post.",
  "Suspension: fix on the subsistence allowance; re-fix on reinstatement.",
  "Rule 7(5), CCS (Revised Pay) Rules, 2016",
  "Paying the full revised pay to a servant still under suspension")

# ------------------------------------------------------------------ rule 7(10)(i)(a)
Q("RB-039", "7", "Rule 7(10)(i)(a)", "Stepping up — same post",
  "Rule 7(10)(i)(a) permits stepping up only where the junior and the senior:",
  "Belong to the same post and the same cadre",
  ("Belong to the same Ministry, whatever the post",
   "The condition is the same post and the same cadre, not merely the same Ministry."),
  ("Draw pay in the same Level, even if the posts differ",
   "A shared Level is not enough; the posts themselves must be the same."),
  ("Were recruited in the same year",
   "The year of recruitment is not a condition in clause (a)."),
  "The four conditions in rule 7(10)(i) are cumulative. Clause (a) requires that the senior and the junior belong "
  "to the same post and the same cadre; clause (b) that the junior was drawing more pay than the senior; clause (c) "
  "that the junior's pay was fixed under these rules and not under any other provision; and clause (d) that the "
  "senior had no advance increment which the junior did not have. The proviso then bars relief where the junior's "
  "higher pay came from an advance increment.",
  "Step-up: same post, same cadre — the first of four cumulative conditions.",
  "Rule 7(10)(i)(a), CCS (Revised Pay) Rules, 2016",
  "Reading a shared Level as satisfying the same-post condition")

# ------------------------------------------------------------------ rule 7(10)(i)(b)
Q("RB-040", "7", "Rule 7(10)(i)(b)", "Stepping up — junior drawing more",
  "Under rule 7(10)(i)(b), the occasion for stepping up arises when:",
  "The junior draws more pay than the senior",
  ("The senior draws more than the junior but is senior in rank",
   "That is the ordinary position and calls for nothing; the anomaly is the junior drawing more."),
  ("Both draw the same pay in the revised structure",
   "Equal pay is not an anomaly, and the clause is not engaged."),
  ("The junior draws more in the pre-revised structure only",
   "The comparison is in the revised structure, after fixation under these rules."),
  "Clause (b) states the mischief the whole sub-rule exists to cure: a junior, on fixation, drawing more pay than "
  "a senior in the same post and cadre. The remedy is to step the senior up to the pay of the junior, and only to "
  "that figure — stepping up is a levelling, never an advantage. Each of the four clauses must hold before the "
  "remedy is available.",
  "Step-up: the junior must be drawing more, in the revised structure.",
  "Rule 7(10)(i)(b), CCS (Revised Pay) Rules, 2016",
  "Stepping a senior up beyond the junior's pay")

# ------------------------------------------------------------------ rule 7(10)(i)(c)
Q("RB-041", "7", "Rule 7(10)(i)(c)", "Stepping up — fixation under these rules",
  "For a step-up, rule 7(10)(i)(c) requires that the junior's pay was fixed:",
  "Under these rules only, not under another provision",
  ("Under any provision at all, so long as the figure is higher",
   "The clause confines the anomaly to a fixation made under these rules."),
  ("By the Head of Department's special order",
   "A special order is not the mechanism; the clause speaks of a fixation under these rules."),
  ("Before 1 January 2016",
   "The fixation that creates the anomaly is the revised-structure fixation, which happens on or after that date."),
  "Clause (c) is a limitation on the remedy: only a pay fixation made under the 2016 Rules can found a step-up. If "
  "the junior's higher pay came from some other source — an out-of-turn promotion, a court order, a special "
  "increment — the machinery of rule 7(10) is not available, and the senior must look to whatever order created "
  "the junior's advantage.",
  "Step-up: the junior's pay must have been fixed under these rules.",
  "Rule 7(10)(i)(c), CCS (Revised Pay) Rules, 2016",
  "Claiming a step-up where the junior's higher pay came from another source")

# ------------------------------------------------------------------ rule 7(10)(i)(d)
Q("RB-042", "7", "Rule 7(10)(i)(d)", "Stepping up — no advance increment",
  "Rule 7(10)(i)(d) requires that the senior:",
  "Had no advance increments the junior lacked",
  ("Had at least one advance increment",
   "The clause is a negative condition: the senior must not have an advantage of this kind."),
  ("Was drawing the same number of ordinary increments as the junior",
   "The clause speaks of advance increments, not of the ordinary annual increment."),
  ("Had completed at least five years in the post",
   "Service length is not a condition of clause (d)."),
  "Clause (d), read with the proviso, is the sharpest of the four. The proviso to rule 7(10)(i) bars a step-up "
  "where the junior's higher pay was itself the result of an advance increment. Clause (d) bars it where the senior "
  "is the one holding an advance increment the junior lacks. Either way, an advance increment is taken out of the "
  "comparison, so that a difference created by an advance increment is never equalised by a step-up.",
  "Step-up: advance increments are excluded from the comparison, on either side.",
  "Rule 7(10)(i)(d) and the proviso, CCS (Revised Pay) Rules, 2016",
  "Stepping up to equalise a gap created by an advance increment")

# ------------------------------------------------------------------ rule 7(10)(ii)
Q("RB-043", "7", "Rule 7(10)(ii)", "Step-up — incremental consequence",
  "Where a senior is stepped up under rule 7(10), when does his next increment fall due?",
  "From the date of re-fixation, on an order made under FR 27",
  ("On 1 January or 1 July next following, as in the ordinary case",
   "The sub-rule displaces the ordinary half-yearly date by tying the increment to the order."),
  ("From the date the junior drew the higher pay",
   "The sub-rule fixes the date by reference to the order of re-fixation, not the junior's history."),
  ("Only after he has drawn the stepped-up pay for a full year",
   "The waiting period runs from the date of re-fixation, and it is the ordinary one."),
  "Rule 7(10)(ii) provides that where a step-up is allowed, it takes effect from the date on which the junior "
  "began to draw more pay, and the next increment to the senior accrues on an order issued under FR 27 from the "
  "date of such re-fixation. The point the paper tests is that the step-up carries an incremental consequence — "
  "it does not leave the senior on a static cell forever, and it does not disturb the junior.",
  "Step-up: next increment from the date of re-fixation, by order under FR 27.",
  "Rule 7(10)(ii), CCS (Revised Pay) Rules, 2016",
  "Assuming the ordinary 1 January / 1 July increment date after a step-up")

# ------------------------------------------------------------------ rule 11
Q("RB-044", "11", "Rule 11", "Date of switch-over later than 1 January 2016",
  "A servant elects, or is brought over, to the revised structure from 1 July 2016. His pay is fixed:",
  "In the manner prescribed in rule 7(1)(A), applied as at that later date",
  ("At the first cell of the Level, because he joined the structure late",
   "The first cell is the rule 7(1)(A)(ii) floor, not a rule for a late switch-over."),
  ("By applying the fitment factor to his pay on 1 July 2016 with no other change",
   "The rule directs the whole of rule 7(1)(A), including the equal-or-next-higher step and the floor."),
  ("Under rule 8, as a direct recruit",
   "Rule 8 governs direct recruits; a servant already in service moves under rule 7."),
  "Rule 11 deals with a servant who continues to draw his pay in the existing structure and is brought over to the "
  "revised structure from a date later than 1 January 2016 — whether by his own election under rule 6 or otherwise. "
  "His pay is fixed in the manner prescribed in accordance with clause (A) of sub-rule (1) of rule 7, that is, the "
  "same multiplier, the same equal-or-next-higher step and the same floor, applied to the pay he was drawing at the "
  "later date. The rule is a signpost, not a separate formula.",
  "Late switch-over: rule 7(1)(A) applied at the date of switch-over.",
  "Rule 11, read with rule 7(1)(A), CCS (Revised Pay) Rules, 2016",
  "Treating a late switch-over as a fresh appointment")

# ------------------------------------------------------------------ rule 14
Q("RB-045", "14", "Rule 14", "Arrears — what the difference is",
  "The arrears payable from 1 January 2016 under rule 14 are the difference between:",
  "The pay and allowances in the revised structure and those drawn in the existing structure",
  ("The pay alone, excluding dearness allowance in both structures",
   "Rule 14 speaks of pay and allowances, and DA enters the comparison on both sides."),
  ("The gross emoluments of the two structures, including HRA and transport allowance throughout",
   "The comparison is of pay and dearness allowance; HRA and transport allowance are dealt with separately and are "
   "not the subject of rule 14."),
  ("The revised pay and the minimum of the Level, for every servant",
   "That would give every servant the full distance to the floor, not the difference on his own fixation."),
  "Rule 14 provides that the difference between the pay and allowances in the revised structure and those drawn in "
  "the existing structure, from 1 January 2016, shall be paid in cash. Two things follow. First, the arrears are a "
  "difference, not an entitlement to the floor of the Level: a servant already above the floor gets the difference "
  "on his own fixation. Second, because dearness allowance is an allowance, it enters the comparison on both sides, "
  "which is why the DA merged into the revised pay on 1 January 2016 is not also paid as arrears.",
  "Arrears: the difference of pay and allowances, 01.01.2016 onward.",
  "Rule 14, CCS (Revised Pay) Rules, 2016",
  "Computing arrears as the distance to the first cell of the Level")

# ------------------------------------------------------------------ rule 1(1)
Q("RB-046", "1", "Rule 1(1)", "Short title",
  "The correct short title of the 2016 instrument is:",
  "The Central Civil Services (Revised Pay) Rules, 2016",
  ("The Central Civil Services (Revised Pay) Regulations, 2016",
   "They are rules, made under the proviso to article 309, not regulations."),
  ("The Central Government Services (Revised Pay) Rules, 2016",
   "The expression is Civil Services, not Government Services."),
  ("The Central Civil Services (Revised Pay) Rules, 2017",
   "The year in the title is 2016, the year of effect, not 2017."),
  "Rule 1(1) gives the short title, and rule 1(2) brings the rules into force. The title year, 2016, is the year "
  "from which the rules operate; the notification was made on 25 July 2016. Naming the instrument correctly matters "
  "in an office order, because the short title is what identifies the instrument that is being applied.",
  "Title year 2016; notification 25.07.2016.",
  "Rule 1(1), CCS (Revised Pay) Rules, 2016",
  "Confusing the year in the title with the year of notification")

# ------------------------------------------------------------------ FAQ items
# Published FAQs of the Department of Expenditure on the 2016 Rules. Each answer is the
# Department's own, paraphrased into a single sentence and sourced to the FAQ number.
Q("RB-047", "4", "Rule 4 — FAQ", "FAQ — Level of a post",
  "A post carried the grade pay of ₹4,200 in pay band PB-2. Which Level does it enter?",
  "Level 6, the Level shown against that grade pay in the Pay Matrix",
  ("Level 7, because the grade pay was ₹4,200 and the next Level up is taken",
   "The mapping is direct: ₹4,200 in PB-2 is Level 6, and the fitment factor then governs the cell."),
  ("Level 5, since the pay band began at PB-2's minimum",
   "The band's minimum does not decide the Level; the grade pay does."),
  ("The Level depends on the length of service in the post",
   "Length of service moves a servant along the cells of a Level, never between Levels."),
  "Rule 4 assigns each existing pay band and grade pay to a Level in the Pay Matrix. Grade pay ₹4,200 in pay band "
  "PB-2 corresponds to Level 6. The grade pay, not the band's minimum and not the servant's length of service, "
  "determines the Level. Once the Level is fixed, rule 7(1)(A) fixes the cell.",
  "Grade pay decides the Level; the matrix then decides the cell.",
  "Rule 4 and the Schedule, CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Reading the pay band's minimum as the Level", faq=True, faq_no="RB-047")

Q("RB-048", "7", "Rule 7(1)(A)(i) — FAQ", "FAQ — rounding of the product",
  "A servant's pay is ₹26,350. Multiply by 2.57 and the product is ₹67,719.50. Where is his pay fixed?",
  "₹67,800, the next cell above his rounded product in his Level",
  ("₹67,700, the cell nearest to the product",
   "The rule rounds the product to the nearest rupee and then takes the equal-or-next-higher cell, not the nearest cell."),
  ("₹67,719, keeping the paise and placing him in the nearest cell",
   "The pay matrix has cells in round hundreds; paise are not carried into the matrix."),
  ("₹68,000, the next round hundred above the product",
   "The next round hundred is the rounding step, but the cell must then be a real cell of the Level."),
  "Rule 7(1)(A)(i) has three steps, and the paper tests each. Multiply the pay by 2.57; round the product to the "
  "nearest rupee (₹67,719.50 becomes ₹67,720); then find the cell equal to that figure or, if there is none, the "
  "next cell above it, within the same Level. On these figures the rounded product is ₹67,720 and the first cell at "
  "or above it in Level 6 is ₹67,800.",
  "Multiply, round to the rupee, then take the equal-or-next-higher cell.",
  "Rule 7(1)(A)(i), CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Rounding to the nearest cell instead of the nearest rupee", faq=True, faq_no="RB-048")

Q("RB-049", "6", "Rule 6 — FAQ", "FAQ — date of the option",
  "A servant exercises the option to remain on the existing structure. From when does that option operate?",
  "From 1 January 2016, the date the rules take effect",
  ("From the date he signs the option",
   "The option is a choice about 1 January 2016; its operation is not postponed to the date of the signature."),
  ("From the date of notification, 25 July 2016",
   "Notification starts the three-month period for exercising the option, not the period of its operation."),
  ("From the date of his next increment in the existing structure",
   "The next increment ends the option; it does not start it."),
  "The option under rule 6 is an election to continue under the pre-revised structure, and it operates from 1 "
  "January 2016 — the date from which the rules are deemed to be in force under rule 1(2). Two dates must be kept "
  "apart: the date of operation (1 January 2016) and the period within which the option must be exercised, which "
  "runs three months from the date of notification and ends on the date of the servant's next increment in the "
  "existing structure, whichever is earlier.",
  "Option operates from 01.01.2016; it must be exercised within three months of notification.",
  "Rule 6, read with rule 1(2), CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Dating the operation of the option from the date of the signature", faq=True, faq_no="RB-049")

Q("RB-050", "7", "Rule 7(1)(A)(ii) — FAQ", "FAQ — pay below the first cell",
  "A servant's pay on 1 January 2016 is ₹6,000 in Level 1. The first cell of Level 1 is ₹18,000. On fixation:",
  "The first cell, ₹18,000 — his product is below it",
  ("He is placed at ₹15,420, the product of ₹6,000 and 2.57",
   "That figure is below the first cell, and the rule lifts him to the floor."),
  ("He is placed at ₹18,000 only after his next increment falls due",
   "The floor operates at fixation, not at the next increment."),
  ("He keeps ₹6,000 until his pay exceeds the first cell",
   "The rule places him at the first cell on 1 January 2016; it does not wait."),
  "Rule 7(1)(A)(ii) is the floor: where the figure arrived at under clause (i) is less than the first cell of the "
  "Level, the servant is placed at the first cell. ₹6,000 multiplied by 2.57 is ₹15,420, which is below ₹18,000, so "
  "the floor governs. The floor is not an increment and is not adjustable; it is the minimum of the Level, applied "
  "once, at fixation.",
  "Below the first cell: lift to the floor, at fixation.",
  "Rule 7(1)(A)(ii), CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Leaving a servant below the first cell because the product was genuine", faq=True, faq_no="RB-050")

Q("RB-051", "8", "Rule 8 — FAQ", "FAQ — direct recruit after 1 January 2016",
  "A person is appointed by direct recruitment to a post in Level 7 on 1 September 2016. His pay is fixed:",
  "At the first cell of Level 7, ₹44,900",
  ("At the minimum of the pay band, PB-2",
   "There is no pay band in the revised structure; the Level replaces it."),
  ("By multiplying the minimum of the pre-revised scale by 2.57",
   "That is the route for a servant already in service under rule 7, not for a direct recruit under rule 8."),
  ("At the cell fixed by the Head of Department in the offer of appointment",
   "The rule fixes the pay at the first cell; the appointing authority has no discretion to start elsewhere."),
  "Rule 8 fixes the pay of a direct recruit appointed on or after 1 January 2016 at the minimum pay or the first "
  "cell of the Level applicable to the post. There is no fitment and no factor: the recruit starts at the bottom of "
  "the column. The proviso deals with the narrow case of a recruit appointed after 1 January 2016 but before "
  "notification whose pay had already been fixed in the existing structure — any excess over the first cell is paid "
  "as personal pay, absorbed in future increments.",
  "Direct recruit: first cell of the Level, with no fitment.",
  "Rule 8, CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Applying the 2.57 factor to a direct recruit", faq=True, faq_no="RB-051")

Q("RB-052", "9", "Rule 9 — FAQ", "FAQ — increment at the top of the Level",
  "A servant is at the last cell of his Level on 1 January 2017. What happens to his increment?",
  "No increment accrues; he stays at the last cell",
  ("He is moved into the first cell of the next Level",
   "A promotion moves a servant between Levels; an increment never does."),
  ("He is paid the increment as a personal pay",
   "Personal pay arises under rules 7 and 8, not from an increment at the top of a Level."),
  ("He receives a lump sum equal to one increment",
   "Rule 9 gives an increment by moving a cell; at the top there is no cell, and no cash substitute is provided."),
  "Rule 9 provides that the increment shall be as specified in the vertical cells of the applicable Level. The "
  "matrix is finite: at the last cell of a Level there is no vertical cell to move to, so no increment accrues and "
  "the pay stands still until a promotion or a revision of the matrix moves the servant. This is the commonest "
  "arithmetic trap in the subject — a column of cells is not a ladder into the next Level.",
  "Top of the Level: no increment, no cash substitute.",
  "Rule 9, CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Expecting an increment to carry a servant into the next Level", faq=True, faq_no="RB-052")

Q("RB-053", "13", "Rule 13(i) — FAQ", "FAQ — promotion increment taken where",
  "A servant in Level 6 is promoted to Level 7 on 1 March 2017. Under rule 13(i) the increment is given:",
  "In Level 6, then at the equal-or-next cell in Level 7",
  ("In Level 7, after he has been placed in that Level",
   "That reverses the rule; the increment is earned in the Level being left."),
  ("In both Levels, one increment in each",
   "One increment, taken once, in the lower Level."),
  ("Only in Level 7, and only if a cell exists at exactly his pay in that Level",
   "The equal-or-next-higher step exists precisely for the case where no exact cell is available."),
  "Rule 13(i) does the promotion in two moves: one increment in the Level from which the servant is promoted, and "
  "then placement at the cell equal to the figure so arrived at in the Level to which he is promoted, or at the "
  "next higher cell if there is no equal cell. The order matters more than the arithmetic. Giving the increment in "
  "the destination Level instead would place him higher, and is the error the paper builds the distractors on.",
  "Promotion: increment in the old Level, then equal-or-next-higher in the new.",
  "Rule 13(i), CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Taking the promotion increment in the destination Level", faq=True, faq_no="RB-053")

Q("RB-054", "13", "Rule 13(ii) — FAQ", "FAQ — NPA and the ceiling",
  "A medical officer receiving Non-Practising Allowance is promoted to a Level governed by rule 13. The ceiling "
  "in rule 13(ii) is:",
  "Average of Apex and Cabinet Secretary pay",
  ("The basic pay of the Cabinet Secretary alone",
   "The ceiling is the average of the two, not the higher of them."),
  ("The highest cell of the officer's own Level",
   "The top of his own Level is not the rule 13(ii) ceiling."),
  ("There is no ceiling at all; NPA sits outside the pay matrix entirely",
   "NPA is outside the matrix, but rule 13(ii) puts a ceiling on basic pay plus NPA together."),
  "Rule 13(ii) provides that in the case of a Government servant receiving Non-Practising Allowance, his basic pay "
  "plus NPA shall not exceed the average of the basic pay of the revised scale applicable to the Apex Level and "
  "that applicable to the Level of the Cabinet Secretary. The ceiling applies to the sum, not to either figure "
  "alone, and it is a ceiling on the combination — which is why an officer can be at the top of his own Level and "
  "still be caught by it.",
  "NPA: basic pay plus NPA capped at the average of Apex and Cabinet Secretary.",
  "Rule 13(ii), CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Applying the ceiling to basic pay alone, ignoring NPA", faq=True, faq_no="RB-054")

Q("RB-055", "14", "Rule 14 — FAQ", "FAQ — arrears and the option",
  "A servant who opted to remain on the existing structure under rule 6 is later brought over to the revised "
  "structure. From when are his arrears payable?",
  "From the date he is actually brought over, not from 1 January 2016",
  ("From 1 January 2016, because the rules are deemed in force from that date",
   "Rule 14 works on the difference between the structures; a servant who stayed out of the revised structure "
   "until a later date had no revised pay for the earlier period."),
  ("From 1 July 2016, the mid-year date",
   "There is no mid-year date in rule 14."),
  ("No arrears are payable to a servant who once opted out",
   "Arrears run from the date of switch-over; the earlier option does not extinguish them."),
  "Rule 14 pays the difference between the two structures from 1 January 2016. A servant who exercised the option "
  "to remain on the existing structure was not, for that period, a servant in the revised structure — so the "
  "difference does not arise until he is brought over. The rule 6 option and the rule 14 arrears therefore interact: "
  "the option defers the switch-over, and the switch-over starts the arrears.",
  "Arrears run from the date of switch-over, not from 01.01.2016, where the option was exercised.",
  "Rule 14, read with rule 6, CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Paying arrears from 01.01.2016 to a servant who had opted out", faq=True, faq_no="RB-055")

Q("RB-056", "6", "Rule 6(1) — FAQ", "FAQ — who may exercise the option",
  "Which servant may exercise the option under rule 6 to remain on the existing structure?",
  "A servant who is in service on 25 July 2016 and not a new entrant",
  ("Any servant appointed on or after 1 January 2016",
   "A direct recruit after that date is dealt with by rule 8 and has no such option."),
  ("Only a servant who was in service on 1 January 2016",
   "The option is given by the rules as notified; being in service on the date of notification is what qualifies."),
  ("Any servant, including one under suspension",
   "A servant under suspension draws subsistence allowance, and rule 6 does not reach him."),
  "The option under rule 6 is given to a person who is serving in a post on the date of notification and who is not "
  "a new entrant covered by rule 8. Two figures decide the question — the date of notification, 25 July 2016, and "
  "the date of effect, 1 January 2016 — and the option belongs to a servant in position on the former. A direct "
  "recruit appointed on or after 1 January 2016 has his pay fixed by rule 8 and no election to make.",
  "Option: a servant in service on the date of notification, not a direct recruit.",
  "Rule 6, CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Giving the option to a direct recruit covered by rule 8", faq=True, faq_no="RB-056")

Q("RB-057", "6", "Rule 6(1) — FAQ", "FAQ — form and finality of the option",
  "A servant exercises the option in writing within the period allowed. Can he change his mind afterwards?",
  "No; the option once exercised is final and cannot be altered",
  ("Yes, once, with the Head of Office's approval",
   "The rules give no power to reopen an option that has been exercised."),
  ("Yes, at any time before his next increment",
   "The next increment closes the window for exercising the option; it does not reopen one already made."),
  ("Yes, if the revised structure turns out to be less favourable to him",
   "An option is a decision taken on the rules as they stand; a later comparison does not reopen it."),
  "Rule 6 provides that the option shall be exercised in writing within the period allowed and that it is final. "
  "The design is deliberate: the option changes the servant's arrears under rule 14 for the whole of the period, and "
  "an option that could be reopened would let a servant wait to see which structure paid more. The period runs three "
  "months from notification, subject to the ceiling of the date of the next increment in the existing structure.",
  "Option: in writing, within the period, and final once made.",
  "Rule 6, CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Treating the option as revocable while the three-month period runs", faq=True, faq_no="RB-057")

Q("RB-058", "7", "Rule 7(1)(A) — FAQ", "FAQ — the fitment factor",
  "The fitment factor of 2.57 is applied to:",
  "The pay in the pay band plus the grade pay, taken together",
  ("The grade pay alone",
   "That would leave the pay band out of the calculation and collapse the matrix."),
  ("The pay in the pay band alone, with the grade pay added afterwards at the old rate",
   "The grade pay is part of the pay; it is multiplied with the band, not added after."),
  ("The basic pay plus dearness allowance at the old rate",
   "The DA has already been merged in arriving at the factor; adding it again double-counts."),
  "The 2.57 factor was derived by taking the pay in the pay band and the grade pay together, adding the dearness "
  "allowance payable on 1 January 2016 at 125 per cent, and fitting the result to the new matrix. That is why the "
  "factor is applied to band plus grade pay, and why the DA is not then paid again. The factor is not uniform: it "
  "runs from 2.57 at the lower Levels to 2.78 at Level 16, and Level 13 was re-cast at 2.67 by the resolution of "
  "16 May 2017.",
  "Factor 2.57: pay in the band plus grade pay, with DA already merged.",
  "Rule 7(1)(A)(i) and the Schedule, CCS (Revised Pay) Rules, 2016; DoE FAQ",
  "Applying the factor to the grade pay separately, or adding DA again", faq=True, faq_no="RB-058")
