#!/usr/bin/env python3
"""data_bank.py — the general question bank on the CCS (Revised Pay) Rules, 2016.

Concepts, not arithmetic: who may exercise the option, which increment date
applies to which half-year, what each rule overrides, which Level a Grade Pay
maps to, and the amendments that moved a figure. Where a question turns on a
Level, the slice of the matrix it needs is attached so the platform can draw it.
"""
from __future__ import annotations

import paymatrix as pm

FACTS = []


def Q(fid, rule, rules_text, topic, stem, ans, d1, d2, d3, why, safe, src, trap,
      level=None, cells=None, marks=None, tag="Tough", table_note=None,
      table_kind=None, cells_before=None, cells_after=None, mapping=None, highlight=None,
      before_label=None, after_label=None):
    FACTS.append(dict(id=fid, rule=rule, rules_text=rules_text, topic=topic, q=stem,
                      a=ans, d=[d1, d2, d3], why=why, safe=safe, src=src, trap=trap,
                      level=level, cells=cells, marks=marks or {}, tag=tag,
                      table_note=table_note,
                      table_kind=table_kind, cells_before=cells_before, cells_after=cells_after,
                      mapping=mapping, highlight=highlight,
                      before_label=before_label, after_label=after_label))


# ---------------------------------------------------------------- rule 1
Q("RP-001", "1", "Rule 1(2)", "Commencement",
  "The CCS (Revised Pay) Rules, 2016 were notified on 25 July 2016. From what date do they operate?",
  "1 January 2016",
  ("25 July 2016, the date of notification", "Rule 1(2) deems the rules to have come into force earlier than the gazette."),
  ("1 April 2016, the start of the financial year", "The award operated from the calendar year, not the financial year."),
  ("1 January 2017, one year after the award", "The award operated from 01.01.2016; a year's postponement would have doubled the arrears."),
  "Rule 1(2) deems the rules to have come into force on 1 January 2016, although they were notified on 25 July 2016. "
  "The gap of nearly seven months is what generates the arrears that rule 14 then deals with. The same split — effect "
  "from January, notification in July — gives rise to the option, because servants had to be given a chance to stay on "
  "the old structure for the months already worked.",
  "Notified 25.07.2016; in force from 01.01.2016.",
  "Rule 1(2), CCS (Revised Pay) Rules, 2016",
  "Confusing the date of notification with the date of effect")

Q("RP-002", "1", "Rule 1(2)", "Commencement",
  "For what reason does the gap between July 2016 and January 2016 matter in practice?",
  "Because it is the period for which arrears became payable",
  ("Because it is the period during which the option could be exercised",
   "The option ran for three months from notification under rule 6, not across the gap."),
  ("Because the increments for that period were cancelled",
   "Increments were not cancelled. Rule 10 moved the increment dates and the arrears covered the revised pay for those months."),
  ("Because servants appointed in that gap were excluded from the rules",
   "Rule 8 expressly covers direct recruits appointed on or after 01.01.2016, including those appointed in the gap."),
  "The revised structure operated from January but the rules were notified in July, so every servant had been drawing "
  "unrevised pay for seven months. Rule 14 requires that difference to be paid during the financial year 2016-17, and "
  "defines it as the difference in pay AND dearness allowance between the revised and unrevised positions.",
  "January effect, July notification = arrears for the gap, paid in FY 2016-17.",
  "Rules 1(2) and 14, CCS (Revised Pay) Rules, 2016",
  "Assuming the arrears were paid as a lump of basic pay only")

# ---------------------------------------------------------------- rule 2
Q("RP-003", "2", "Rule 2", "Applicability",
  "Which of the following is NOT excluded from the operation of the CCS (Revised Pay) Rules, 2016?",
  "A person serving in the Indian Audit and Accounts Department",
  ("A person employed on contract", "Rule 2(2)(vi) excludes contract staff unless the contract provides otherwise."),
  ("A person paid out of contingencies", "Rule 2(2)(iv) excludes persons paid out of contingencies."),
  ("A person re-employed in Government service after retirement, drawing a pension", "Rule 2(2)(vii) excludes re-employed pensioners."),
  "Rule 2(1) expressly applies the rules to persons serving in the Indian Audit and Accounts Department, after "
  "consultation with the Comptroller and Auditor General. The IA&AD is therefore INSIDE the rules, while the eight "
  "categories in rule 2(2) are outside them. A question that lists contract staff, contingent-paid staff and re-employed "
  "pensioners is testing the exclusion list; the IA&AD is the odd one out because it is included.",
  "IA&AD is expressly included by rule 2(1).",
  "Rule 2(1) and 2(2), CCS (Revised Pay) Rules, 2016",
  "Reading the IA&AD as an excluded department")

Q("RP-004", "2", "Rule 2(2)(vi)", "Applicability",
  "A department engages a consultant on a contract that is silent about pay rules. Is he covered by the 2016 Rules?",
  "No — contract staff are excluded unless the contract provides otherwise",
  ("Yes — every person on the Government's payroll is covered",
   "Rule 2(1) covers persons appointed to civil posts on the Civil Estimates. A consultant on contract is a separate "
   "category, dealt with by rule 2(2)(vi)."),
  ("Yes, but only if he is paid monthly", "Monthly payment is one of the conditions in rule 2(2)(v)'s exclusion. Being paid monthly does not bring a contract appointment inside the rules."),
  ("No — but only because the contract is silent, since a contract that extends the rules would bring him in",
   "That is precisely the position under rule 2(2)(vi): silent contracts exclude, and a contract that provides otherwise "
   "includes."),
  "Rule 2(2)(vi) excludes persons employed on contract EXCEPT where the contract provides otherwise. The proviso therefore "
  "reverses the usual assumption: silence excludes, and inclusion has to be written into the contract. This is the one "
  "exclusion in rule 2 that a department can switch off by drafting.",
  "Contract staff: excluded unless the contract says otherwise.",
  "Rule 2(2)(vi), CCS (Revised Pay) Rules, 2016",
  "Assuming a monthly-paid consultant is automatically covered")

# ---------------------------------------------------------------- rule 3
Q("RP-005", "3", "Rule 3(x)", "Definitions",
  "In the revised pay structure, what does 'basic pay' mean?",
  "The pay drawn in the prescribed Level in the Pay Matrix",
  ("Pay in the Level plus grade pay", "Grade pay has been absorbed into the matrix. There is no separate grade pay to add."),
  ("Pay in the Level plus dearness allowance", "Dearness allowance is an allowance, not part of basic pay; rule 3(xi) separately defines revised emoluments."),
  ("The first cell of the Level, whatever the servant actually draws", "The first cell is only the entry point. Basic pay is the cell the servant actually occupies."),
  "Rule 3(x) defines basic pay in the revised pay structure as the pay drawn in the prescribed Level in the Pay Matrix. "
  "Because the matrix figure already carries the grade pay rationalised into it, there is nothing to add. This single "
  "definition is why every subsequent calculation — leave salary, encashment, pension — is done on one number instead of "
  "two.",
  "Basic pay = the cell figure. No grade pay, no DA.",
  "Rule 3(x), CCS (Revised Pay) Rules, 2016",
  "Adding grade pay to the revised basic pay")

Q("RP-006", "3", "Rule 3(xi)", "Definitions",
  "'Revised emoluments' under rule 3(xi) means:",
  "The pay in the Level",
  ("Pay in the Level plus every allowance drawn with it", "Allowances are outside the definition; revised emoluments is the pay in the Level alone."),
  ("Pay in the Level plus dearness allowance", "DA was part of the OLD emoluments definition, which is how the two definitions are told apart."),
  ("Basic pay plus grade pay plus dearness allowance, as before the revision", "That is the shape of 'existing emoluments', not of revised emoluments."),
  "Rule 3(xi) defines revised emoluments as the pay in the Level. The contrast is deliberate: 'existing emoluments' under "
  "rule 3(v) is a SUM — existing basic pay plus existing dearness allowance at the 2006 index average — whereas revised "
  "emoluments is a single figure. Rule 7(7) uses the comparison between the two to award personal pay, which is why the "
  "definitions must be kept apart.",
  "Existing emoluments is a sum; revised emoluments is one figure.",
  "Rules 3(v) and 3(xi), CCS (Revised Pay) Rules, 2016",
  "Treating the two emoluments definitions as interchangeable")

# ---------------------------------------------------------------- rule 4
Q("RP-007", "4", "Rule 4", "Level of posts",
  "A post carried Grade Pay ₹7,600 in Pay Band 3 before 2016. Which Level does it enter?",
  "Level 12",
  ("Level 11", "Level 11 is Grade Pay ₹6,600 in PB-3."),
  ("Level 12, but only if the incumbent elects the revised structure", "Rule 4 fixes the Level of the POST. Election under rule 5 concerns the pay structure, not which Level the post belongs to."),
  ("Level 13", "Level 13 is Grade Pay ₹8,700 in PB-4, one whole grade above."),
  "Rule 4 reads the Level off the matrix caption against the old Pay Band and Grade Pay. In PB-3 (15600-39100) the grade "
  "pays run ₹5,400, ₹6,600 and ₹7,600 against Levels 10, 11 and 12. Grade Pay ₹7,600 therefore enters Level 12, whose "
  "first cell is ₹78,800. The mapping is mechanical and needs no calculation — but it needs the Pay Band as well as the "
  "grade pay.",
  "PB-3: GP 5400 → L10, GP 6600 → L11, GP 7600 → L12.",
  "Rule 4 and Part A of the Schedule, CCS (Revised Pay) Rules, 2016",
  "Counting Levels from the wrong end of the Pay Band",
  level="12", cells=pm.matrix("12")[0:4], marks={"both": 1},
  table_note="Level 12, cells 1 to 4. The post enters at the first cell, ₹78,800.")

# ---------------------------------------------------------------- rule 5
Q("RP-008", "5", "Rule 5, proviso 1", "Option",
  "A servant elects to continue in the existing pay structure. How long may he remain there?",
  "Until his next increment in the old structure",
  ("For exactly one year from 1 January 2016, whatever his increment cycle", "The proviso is tied to the next increment in the OLD structure, which may fall well within or beyond a year."),
  ("Indefinitely, for the rest of his service and through every later revision", "The option runs only to the next increment in the old structure."),
  ("Until the date of notification, 25 July 2016", "That is the date by which the choice had to be communicated, not the end of the period of the old structure."),
  "The first proviso to rule 5 permits the servant to draw pay in the existing structure until the date on which he earns "
  "his next or any subsequent increment in that structure, or until he vacates the post or ceases to draw pay in it, "
  "whichever is earlier. The option is therefore self-terminating: the first increment in the old structure ends it whether "
  "or not the servant wants to continue.",
  "Option ends at the next increment in the old structure.",
  "Rule 5, first proviso, CCS (Revised Pay) Rules, 2016",
  "Treating the option as a permanent choice of the old structure")

Q("RP-009", "5", "Rule 5, Explanation 1", "Option",
  "A servant holds a permanent post and is also officiating in a higher post. In how many Pay Bands and Grade Pays may he "
  "retain the existing structure?",
  "One",
  ("Two, one for each post", "Explanation 1 limits the option to a single Pay Band and Grade Pay, whatever the number of posts held."),
  ("As many as the posts he holds, provided he applies separately for each", "Separate applications do not enlarge the Explanation 1 limit."),
  ("None, because an officiating servant has no substantive post", "Being substantive on one post and officiating on another is exactly the situation in which the one-scale limit has to be applied."),
  "Explanation 1 to rule 5 provides that the option to retain the existing pay structure is admissible only in respect of "
  "ONE existing Pay Band and Grade Pay or scale. A servant holding several posts must choose which single scale he "
  "retains; for the remaining posts he is brought into the revised structure. Explanation 3 then protects his substantive "
  "pay on the post in respect of which he retained the old structure.",
  "One Pay Band and Grade Pay, however many posts are held.",
  "Rule 5, Explanation 1, CCS (Revised Pay) Rules, 2016",
  "Multiplying the option by the number of posts held")

# ---------------------------------------------------------------- rule 6
Q("RP-010", "6", "Rule 6(1)", "Exercise of option",
  "Within what period must the option under rule 5 be exercised?",
  "Three months from the date of notification",
  ("One month from the date of notification", "One month is the period for the FR 22(I)(a)(1) option on promotion, not for the rule 5 option."),
  ("Six months from 1 January 2016", "The clock runs from notification, not from the date of effect."),
  ("Before the first increment after 1 January 2016", "That is when the old structure ceases under rule 5, which is a different question from when the choice must be made."),
  "Rule 6(1) requires the option in writing so as to reach the authority within three months of the date of notification, "
  "or within three months of any subsequent order revising the existing structure. Two cases are extended: a servant out "
  "of India gets three months from taking charge of his post in India, and a servant under suspension on 1 January 2016 "
  "gets three months from his return to duty.",
  "Three months from notification, in writing.",
  "Rule 6(1), CCS (Revised Pay) Rules, 2016",
  "Running the three months from the date of effect instead of notification")

Q("RP-011", "6", "Rule 6(1), proviso (ii)", "Exercise of option",
  "A servant was under suspension on 1 January 2016. How is his option period computed?",
  "Three months from his return to duty",
  ("He loses the option, because a suspended servant cannot make an election", "Note (3) and the proviso preserve the option; suspension does not forfeit it."),
  ("Three months from the date of the order of suspension", "The starting point is the return to duty, not the suspension."),
  ("Three months from the conclusion of the disciplinary proceedings, whichever is later", "The proviso runs from the return to duty, not from the end of the proceedings."),
  "The proviso to rule 6(1) extends the time for a servant under suspension to three months from the date of his return "
  "to duty, where that date is later than the period otherwise allowed. Rule 7(5) meanwhile keeps him on subsistence "
  "allowance based on the existing structure, and makes his pay in the revised structure subject to the final order in "
  "the disciplinary proceedings — so the option and the pay are both held open, in different ways.",
  "Suspension: option from return to duty; pay subject to the final order.",
  "Rule 6(1), proviso (ii), read with rule 7(5), CCS (Revised Pay) Rules, 2016",
  "Starting the suspension proviso from the suspension rather than the return")

Q("RP-012", "6", "Rule 6(4)", "Exercise of option",
  "A servant exercises the option to continue in the existing structure and a year later wishes to change his mind. What is "
  "the position?",
  "He cannot — the option once exercised is final",
  ("He may change it before his next increment", "The facility to change is closed by rule 6(4); the increment only ends the old structure, it does not reopen the choice."),
  ("He may change it with the sanction of the Head of Department", "No authority is given power to reopen a final option under rule 6."),
  ("He may change it within three months of the notification", "Three months is the window for making the choice, not for revisiting it."),
  "Rule 6(4) says in terms that the option once exercised shall be final. The design is deliberate: the old structure and "
  "the revised structure carry different dearness allowance treatment, so allowing servants to move between them as "
  "allowances rose would make the pay bill unmanageable. The choice is made once, in writing, within three months, and it "
  "ends at the next increment in the old structure under rule 5.",
  "Option once exercised is final.",
  "Rule 6(4), CCS (Revised Pay) Rules, 2016",
  "Treating the election as revisitable while it is still running")

# ---------------------------------------------------------------- rule 7
Q("RP-013", "7", "Rule 7(1)(A)(i)", "Fixation",
  "In fixing pay under rule 7(1)(A)(i), the figure obtained by multiplying existing basic pay by 2.57 is rounded off to the:",
  "Nearest rupee",
  ("Nearest ten rupees", "The rule says nearest rupee, and the gazette's own illustration rounds 32279.20 to 32279."),
  ("Nearest hundred rupees", "Rounding the product to the nearest ₹100 is a common misreading: the rounding to ₹100 belongs to the CELLS of the matrix, not to the product."),
  ("Next higher rupee", "The rule is nearest rupee, which may round down: 32279.20 became 32279."),
  "Rule 7(1)(A)(i) rounds the product to the nearest rupee before locating it. The gazette illustration is explicit: "
  "12560 × 2.57 = 32279.20, rounded off to 32279. Only after that is the figure located in the Level. Confusing this "
  "rounding with the matrix's own rounding of cells to ₹100 is the most common error in the whole rule, because both "
  "roundings appear in the same sentence of the rule's operation.",
  "Product rounds to the rupee; cells are already rounded to ₹100.",
  "Rule 7(1)(A)(i) and its illustration, CCS (Revised Pay) Rules, 2016",
  "Rounding the product to the nearest ₹100")

Q("RP-014", "7", "Rule 7(7)", "Personal pay",
  "Where a servant's existing emoluments exceed his revised emoluments, what follows?",
  "Personal pay, absorbed by later increments",
  ("The difference is paid as arrears for one year only", "Arrears under rule 14 are a different mechanism, covering the gap between revised and unrevised pay from January 2016."),
  ("His pay is fixed at the cell that matches his existing emoluments, and the matrix is departed from", "The fixation under rule 7(1) is unaffected; the excess is protected separately as personal pay."),
  ("The difference is forfeited, the revised structure being exhaustive of pay", "Rule 7(7) exists precisely to prevent forfeiture."),
  "Rule 7(7) provides that where the existing emoluments exceed the revised emoluments, the difference is allowed as "
  "personal pay to be absorbed in future increases in pay. Personal pay is not a permanent addition: it shrinks as "
  "increments raise the basic pay, until it is fully absorbed. The same technique is used in rules 8, 9 and 12 — wherever "
  "the new structure would otherwise leave a servant worse off.",
  "Excess of old over new becomes personal pay, absorbed by future increments.",
  "Rule 7(7), CCS (Revised Pay) Rules, 2016",
  "Treating personal pay as a permanent addition to basic pay")

Q("RP-015", "7", "Rule 7(8)", "Stepping up",
  "On fixation, a senior's pay lands in a lower cell than that of his junior in the same cadre. What does the rule require?",
  "The senior's pay is stepped up to the same cell as the junior's",
  ("The junior's pay is reduced to the senior's cell", "Stepping up never reduces anyone's pay; it raises the senior."),
  ("Both are referred to the Central Government under rule 17", "Rule 7(8) provides the answer itself; no reference is needed."),
  ("Nothing, because fixation is mechanical and anomalies are accepted", "Rule 7(8) is precisely the provision that refuses to accept this anomaly."),
  "Rule 7(8) provides that where, on fixation, a servant who was drawing more pay than a junior in the same cadre before "
  "1 January 2016 gets fixed in a lower cell than that junior, his pay shall be stepped up to the same cell. A second "
  "stepping-up provision, rule 7(10), covers the case where a senior promoted before 1 January 2016 draws less than a "
  "junior promoted after it, and requires the re-fixation order to be issued under Fundamental Rule 27.",
  "Senior fixed below junior: step the senior up to the junior's cell.",
  "Rules 7(8) and 7(10), CCS (Revised Pay) Rules, 2016",
  "Reducing the junior's pay instead of stepping up the senior")

Q("RP-016", "7", "Rule 7(2)", "Upgraded posts",
  "A post is upgraded under Part B of the Schedule from Grade Pay ₹2,400 to ₹2,800. For fixation, the existing basic pay "
  "is arrived at by adding:",
  "Pay in the Pay Band plus the upgraded grade pay",
  ("Pay in the Pay Band plus Grade Pay ₹2,400, the grade pay actually held on 1 January 2016",
   "Rule 7(2) uses the grade pay corresponding to the Level to which the post has been UPGRADED, not the one being drawn."),
  ("Pay in the Pay Band alone, without any grade pay", "Grade pay is always part of existing basic pay under rule 3(i)."),
  ("The first cell of the upgraded Level, without any multiplication", "That is the treatment for a direct recruit under rule 8, not for an upgraded post."),
  "Rule 7(2) provides that where a post has been upgraded under Part B or Part C of the Schedule, the existing basic pay "
  "is arrived at by adding the pay drawn in the existing Pay Band plus the grade pay CORRESPONDING TO THE LEVEL TO WHICH "
  "THE POST HAS BEEN UPGRADED. The gazette illustration uses 12960 (10160 + 2800), not 12560, and lands the servant at "
  "₹33,900 in Level 5 rather than the ₹32,300 he would have reached at his old grade pay.",
  "Upgraded post: use the UPGRADED grade pay in the existing basic pay. 12960 × 2.57 → 33900.",
  "Rule 7(2) and its illustration, CCS (Revised Pay) Rules, 2016",
  "Using the old grade pay for a post that has been upgraded",
  level="5", cells=pm.matrix("5")[0:6], marks={"land": 6},
  table_note="Level 5, cells 1 to 6. Take the gazette illustration: at the upgraded grade pay the existing basic pay "
             "is ₹12,960, and ₹12,960 × 2.57 = ₹33,307, which lands on cell 6 (₹33,900). At the OLD grade pay it would "
             "have been ₹12,560 × 2.57 = ₹32,279, landing on cell 5 (₹32,900) — one cell lower.")

Q("RP-017", "7", "Rule 7(5)", "Suspension",
  "A servant under suspension on 1 January 2016: what does rule 7(5) provide about his pay?",
  "Subsistence on the old structure; revised pay awaits the final order",
  ("He is fixed in the revised structure like everyone else, and the pay is not disturbed pending the inquiry", "Rule 7(5) expressly holds the revised pay subject to the final order in the disciplinary proceedings."),
  ("He is fixed in the revised structure at the first cell of his Level", "That is rule 8 for direct recruits, not rule 7(5) for a suspended servant."),
  ("His pay is fixed in the revised structure but without arrears", "It is not the arrears that are withheld but the fixation itself, which awaits the final order."),
  "Rule 7(5) keeps a suspended servant on subsistence allowance computed on the existing pay structure, and makes his pay "
  "in the revised structure subject to the final order in the pending disciplinary proceedings. The logic is that until "
  "the proceedings end it is not known whether the servant will be exonerated, punished by reduction of pay, or removed — "
  "and a fixation made in the meantime could not be undone easily.",
  "Suspension: subsistence on the old structure; revised pay waits for the final order.",
  "Rule 7(5), CCS (Revised Pay) Rules, 2016",
  "Fixing a suspended servant's pay at once on the revised structure")

Q("RP-018", "7", "Rule 7(1)(B)", "Medical officers with NPA",
  "For a medical officer entitled to Non Practicing Allowance, what is added to the 2.57 product before the cell is located?",
  "DA on the pre-revised NPA",
  ("The full revised NPA at the new rates", "Rule 7(1)(B)(ii) keeps the PRE-REVISED NPA on top of the revised pay until revised rates are decided."),
  ("Nothing — medical officers are fixed under clause (A) like every other servant", "Clause (B) is a separate and express route for officers with NPA."),
  ("An amount equivalent to dearness allowance on the pre-revised basic pay, at the same 125 per cent", "The DA element is on the NPA, not on the basic pay — basic pay has already been multiplied by 2.57."),
  "Rule 7(1)(B)(i) adds to the 2.57 product an amount equivalent to dearness allowance on the pre-revised NPA admissible as "
  "on 1 January 2006. The gazette illustration works it through: basic pay 21000 × 2.57 = 53970, NPA 25% of 21000 = "
  "5250, DA at 125% on the NPA = 6563, total 60533, which lands on ₹61,300 in Level 10. Rule 7(1)(B)(ii) then adds the "
  "pre-revised NPA of ₹5,250 to the revised pay until revised NPA rates are decided, giving ₹66,550.",
  "NPA route: 2.57 product + DA on pre-revised NPA, then the cell; pre-revised NPA added on top.",
  "Rule 7(1)(B) and its illustration, CCS (Revised Pay) Rules, 2016",
  "Adding the revised NPA instead of the pre-revised one",
  level="10", cells=pm.matrix("10")[0:6], marks={"land": 4},
  table_note="Level 10, cells 1 to 6. In the gazette illustration ₹21,000 × 2.57 = ₹53,970, plus ₹6,563 of DA on the "
             "pre-revised NPA of ₹5,250, gives ₹60,533, which lands on cell 4 (₹61,300). Leave the DA out and the figure "
             "is ₹53,970, below the first cell — so the DA is what carries him on to the Level.")

# ---------------------------------------------------------------- rule 8
Q("RP-019", "8", "Rule 8", "Direct recruits",
  "A person appointed by direct recruitment to a Level 10 post on 1 August 2016 starts at:",
  "₹56,100, the first cell of Level 10",
  ("₹1,44,177, being ₹56,100 × 2.57", "The fitment factor multiplies an EXISTING basic pay. A direct recruit has none."),
  ("₹57,800, the second cell, on the ground that a mid-year joiner starts a step higher", "The date of joining does not move the starting cell; rule 8 fixes the first cell."),
  ("₹61,300, the fourth cell, by applying the 2.57 factor to the minimum", "Applying 2.57 to the minimum would double-count the fitment, which is built into the matrix already."),
  "Rule 8 fixes the pay of a direct recruit appointed on or after 1 January 2016 at the minimum pay or the first cell of "
  "the Level. For Level 10 that is ₹56,100. The proviso to rule 8 gives personal pay only to a narrow class — those "
  "appointed between 1 January 2016 and the notification whose existing emoluments had already been fixed and exceeded "
  "the first cell.",
  "Direct recruit: first cell, no fitment.",
  "Rule 8, CCS (Revised Pay) Rules, 2016",
  "Applying 2.57 to a direct recruit's starting pay",
  level="10", cells=pm.matrix("10")[0:4], marks={"both": 1},
  table_note="Level 10, cells 1 to 4. Every direct recruit starts on cell 1, ₹56,100.")

# ---------------------------------------------------------------- rule 9
Q("RP-020", "9", "Rule 9", "Increments",
  "Under rule 9, an increment is:",
  "A move to the next vertical cell in the same Level",
  ("A 3% addition to the pay drawn on the increment date", "The 3% is already built into the cells when the matrix is constructed; the rule directs you to the next cell."),
  ("A move to the corresponding cell in the next Level", "Changing Level is promotion or MACP, not an increment."),
  ("A one-cell move that may be withheld only by the President", "Rule 9 says nothing about withholding; the increment is a matrix step, with the consequences of withholding governed elsewhere."),
  "Rule 9 provides that the increment shall be as specified in the vertical cells of the applicable Level. The matrix has "
  "already done the arithmetic, at 3% compounded and rounded to the nearest ₹100, so the increment is a movement, not a "
  "calculation. That is why the rupee step varies from cell to cell — ₹800 at the foot of Level 4, ₹900 a few cells later.",
  "Increment = next vertical cell in the same Level.",
  "Rule 9, CCS (Revised Pay) Rules, 2016",
  "Recomputing 3% on the increment date")

Q("RP-021", "9", "Rule 9", "Increments",
  "Sixth pay commission increments accrued on 1 July each year. Under the 2016 Rules, how many increment dates are there "
  "in a year?",
  "Two dates, one increment a year",
  ("One — 1 July, as before", "Rule 10 replaced the single 1 July date with two dates."),
  ("Two — and a servant appointed early enough in the year may draw both of them", "Rule 10(1) allows only ONE annual increment, on one of the two dates."),
  ("Two — 1 January and 1 April", "The second date is 1 July, not 1 April."),
  "Rule 10(1) creates two dates for the grant of increment, 1 January and 1 July, in place of the single 1 July date, but "
  "the proviso allows an employee only ONE annual increment, on whichever of the two dates his appointment, promotion or "
  "financial upgradation gives him. The two dates are a device for placing new entrants at the right point in the year, "
  "not an extra increment.",
  "Two dates, one increment a year.",
  "Rule 10(1) and its proviso, CCS (Revised Pay) Rules, 2016",
  "Awarding both dates in the year of appointment")

# ---------------------------------------------------------------- rule 10
Q("RP-022", "10", "Rule 10(2)", "Increment date",
  "A servant is promoted on 1 July 2016. On which date does his next increment fall?",
  "1 January 2017",
  ("1 July 2017", "1 July 2017 is the date for promotions between 2 July and 1 January. A promotion ON 1 July falls in the other range, which is inclusive of 1 July."),
  ("1 July 2016, the same day as the promotion", "A servant gets one increment a year and cannot take promotion and annual increment on the same date."),
  ("1 January 2018, because the promotion on 1 July breaks the cycle", "The promotion resets the date to 1 January 2017, not a year further on."),
  "Rule 10(2) assigns the period between 2 January and 1 July (BOTH INCLUSIVE) to 1 January, and the period between 2 July "
  "and 1 January (both inclusive) to 1 July. A promotion on 1 July falls in the first range because 1 July is its closing "
  "date, so the increment accrues on 1 January 2017. The inclusive ends are the trap: 1 July belongs to the January date, "
  "and 1 January belongs to the July date.",
  "1 July promotion → 1 January increment. The ends are inclusive and cross over.",
  "Rule 10(2), CCS (Revised Pay) Rules, 2016",
  "Treating 1 July as belonging to the July date, when it is the closing date of the January range")

Q("RP-023", "10", "Rule 10(2)", "Increment date",
  "A servant already fixed in the revised structure on 1 January 2016 — on which date did his next increment accrue?",
  "1 July 2016",
  ("1 January 2017", "That is the date for those appointed or promoted in the January–July window. A servant whose pay was fixed on 1 January 2016 was given the first proviso to rule 10, which sets 1 July 2016."),
  ("1 July 2017", "The second proviso to rule 10 makes the increment AFTER 1 July 2016 fall on 1 July 2017, not the first one."),
  ("1 January 2016, on the same date as the fixation", "Fixation is not an increment. The first increment came six months later."),
  "The first proviso to rule 10(2) provides that where pay was fixed in the revised structure as on 1 January, the next "
  "increment in that Level shall accrue on 1 July 2016; the second proviso then puts the following increment on 1 July "
  "2017. So the whole service was moved onto the July cycle for 2016 and 2017 before settling into the two-date system "
  "according to each servant's own appointment or promotion history.",
  "Fixed on 01.01.2016 → increment 01.07.2016 → next 01.07.2017.",
  "Rule 10(2) and its provisos, CCS (Revised Pay) Rules, 2016",
  "Forgetting the two transitional provisos for those fixed on 1 January 2016")

# ---------------------------------------------------------------- rule 11
Q("RP-024", "11", "Rule 11", "Late switch-over",
  "A servant who continued on the old structure switches to the revised structure from 1 July 2017. How is his revised pay "
  "fixed?",
  "Under rule 7(1)(A), as in 2016",
  ("By whatever formula was in force on 1 July 2017, which by then had been revised", "Rule 11 sends the late switcher to rule 7(1)(A), the same clause used in 2016."),
  ("At the cell corresponding to his old pay, without any fitment at all", "Rule 11 incorporates the fitment; without the 2.57 multiplication he would stay on an unrevised figure."),
  ("At the first cell of his Level, as for a direct recruit", "Rule 8's first-cell rule is for direct recruits, not for a servant converting from the old structure."),
  "Rule 11 provides that a servant brought over to the revised structure from a date later than 1 January 2016 has his pay "
  "fixed in the manner prescribed in clause (A) of rule 7(1). So the same 2.57 multiplication, the same rounding to the "
  "rupee and the same equal-or-next-higher cell apply — only the date from which the revised pay runs is different, and "
  "with it the arrears.",
  "Late switch = rule 7(1)(A) applied on the date of switching.",
  "Rule 11, CCS (Revised Pay) Rules, 2016",
  "Inventing a separate formula for a late switch-over")

# ---------------------------------------------------------------- rule 12
Q("RP-025", "12", "Rule 12", "Deputation and personal pay",
  "Rule 12 protects the pay of officers on deputation under which scheme, and in what form?",
  "The Central Staffing Scheme, as personal pay",
  ("All deputations, as a higher cell in the Level of the deputation post", "The rule is confined to the Central Staffing Scheme, and the protection is personal pay, not a cell."),
  ("The Central Staffing Scheme, as a special pay allowance outside the pay matrix", "The rule names personal pay, which is absorbable; special pay is a different device."),
  ("All deputations, as personal pay from 1 January 2016", "Both halves are wrong: the scheme is limited to the CSS and the protection runs from the date of notification, 25 July 2016."),
  "Rule 12 applies where an officer posted on deputation to the Central Government under the Central Staffing Scheme would, "
  "but for the deputation, have drawn more in his parent cadre. The difference is protected as Personal Pay with effect "
  "from the date of notification of the rules. Personal pay is absorbable, so the protection melts away as increments "
  "raise the deputation pay.",
  "CSS deputationists only; personal pay; from 25.07.2016.",
  "Rule 12, CCS (Revised Pay) Rules, 2016",
  "Extending the protection to every deputation and dating it from 01.01.2016")

# ---------------------------------------------------------------- rule 13
Q("RP-026", "13", "Rule 13(i)", "Promotion",
  "On promotion from one Level to another, where is the increment given?",
  "In the Level from which the employee is promoted",
  ("In the Level to which he is promoted", "That is the classic error. Rule 13(i) gives the increment in the old Level, and only then places him in the new one."),
  ("In whichever Level gives the higher figure", "The rule fixes one order; it does not allow a choice."),
  ("In neither — promotion is a straight placement at the equal or next higher cell", "Placement at the equal or next higher cell is the SECOND step, taken after the increment in the old Level."),
  "Rule 13(i) requires one increment to be given in the Level from which the employee is promoted, and then places him at "
  "the cell equal to the figure so arrived at in the Level of the promoted post, or at the next higher cell if there is "
  "no equal cell. The gazette illustration: 28700 in Level 4 goes to 29600, and since 29600 is not a Level 5 cell he is "
  "placed at 30100.",
  "Increment in the old Level, then equal-or-next-higher cell in the new Level.",
  "Rule 13(i), CCS (Revised Pay) Rules, 2016",
  "Giving the promotion increment in the new Level")

Q("RP-027", "13", "Rule 13(ii)", "Promotion with NPA",
  "For a servant receiving Non Practicing Allowance, rule 13(ii) caps basic pay plus NPA at:",
  "The average of Levels 17 and 18",
  ("The basic pay of the Cabinet Secretary, that being the highest figure in the matrix", "The cap is the AVERAGE of the Apex Level and the Cabinet Secretary's Level."),
  ("The basic pay of the Apex Level, that being the ceiling for all senior posts", "The cap also takes in the Cabinet Secretary's Level, averaged with the Apex Level."),
  ("The first cell of the highest Level in the matrix", "There is no such cap in rule 13(ii)."),
  "Rule 13(ii) provides that for Government servants receiving Non Practicing Allowance, basic pay plus NPA shall not "
  "exceed the average of the basic pay of the revised scale applicable to the Apex Level and the Level of the Cabinet "
  "Secretary. With Level 17 at ₹2,25,000 and Level 18 at ₹2,50,000, the average is ₹2,37,500 at the first cells — the "
  "ceiling against which a senior medical officer's pay plus NPA is measured.",
  "NPA cap: average of Level 17 and Level 18 basic pay.",
  "Rule 13(ii), CCS (Revised Pay) Rules, 2016",
  "Using the Cabinet Secretary's pay alone as the cap",
  table_kind="mapping",
  mapping=[("—", "80000", "17"), ("—", "90000", "18")],
  highlight=["17", "18"],
  table_note="Levels 17 and 18 are single fixed cells, ₹2,25,000 and ₹2,50,000. Their average is ₹2,37,500.")

# ---------------------------------------------------------------- rule 14
Q("RP-028", "14", "Rule 14", "Arrears",
  "Rule 14 requires arrears to be paid during which financial year?",
  "2016-17",
  ("2015-16", "The rules were notified in July 2016, after that year had ended."),
  ("2017-18", "The arrears were to be paid in the year of notification, 2016-17."),
  ("In three equal instalments over 2016-17 to 2018-19", "Rule 14 fixes a single financial year, 2016-17."),
  "Rule 14 directs that the arrears shall be paid during the Financial Year 2016-2017. The Explanation then defines arrears "
  "as the difference between the aggregate of pay AND dearness allowance under the revised structure from 1 January 2016, "
  "and the aggregate the servant would have drawn had the pay not been revised. The reference to DA is what makes the "
  "definition work, because the old structure continued to attract DA at the pre-revision rates.",
  "Arrears in FY 2016-17, computed on pay plus DA.",
  "Rule 14 and its Explanation, CCS (Revised Pay) Rules, 2016",
  "Computing arrears on basic pay alone")

# ---------------------------------------------------------------- rule 15
Q("RP-029", "15", "Rule 15", "Overriding effect",
  "What is the effect of rule 15 on the Fundamental Rules?",
  "They yield, but only where inconsistent",
  ("The Fundamental Rules are repealed in their entirety, and with them FR 22 and FR 35", "Rule 15 overrides only to the extent of inconsistency, and only for cases where these rules apply."),
  ("The Fundamental Rules continue to apply in full as the general law, these rules being subordinate", "Rule 15 reverses that priority for the cases it covers."),
  ("The Fundamental Rules apply only to Group A officers, and never to Group B or C", "Rule 15 draws no distinction between Groups."),
  "Rule 15 gives these rules an overriding effect over the Fundamental Rules and every earlier Revised Pay Rules — 1947, "
  "1960, 1973, 1986, 1997 and 2008 — but only to the extent of inconsistency, and only in cases where pay is regulated "
  "under the 2016 rules. The FRs are therefore not repealed: FR 22(I)(a)(1) still supplies the promotion option, and "
  "FR 27 the stepping-up order, because the 2016 rules do not deal with those matters exhaustively.",
  "Override to the extent of inconsistency only; the FRs survive where the rules are silent.",
  "Rule 15, CCS (Revised Pay) Rules, 2016",
  "Treating the Fundamental Rules as repealed")

# ---------------------------------------------------------------- rule 16
Q("RP-030", "16", "Rule 16", "Relaxation",
  "Who may relax a provision of the CCS (Revised Pay) Rules, 2016 to relieve undue hardship?",
  "The President, by order",
  ("The Department of Expenditure, by notification", "The rule names the President, not the department that made the rules."),
  ("The Head of the Department concerned, in writing", "No departmental authority is given the relaxation power."),
  ("The Central Government, on a reference under rule 17", "Rule 17 referral is for interpretation, and rule 16 vests the relaxation power in the President."),
  "Rule 16 allows the President, if satisfied that the operation of any provision causes undue hardship in a particular "
  "case, to dispense with or relax the requirement to such extent and on such conditions as he considers necessary. "
  "Contrast rule 17, where a question of INTERPRETATION is referred to the Central Government: two different powers, two "
  "different authorities, and examiners pair them deliberately.",
  "Hardship → President. Interpretation → Central Government.",
  "Rule 16, read with rule 17, CCS (Revised Pay) Rules, 2016",
  "Sending a relaxation request to the Central Government and an interpretation question to the President")

Q("RP-031", "17", "Rule 17", "Interpretation",
  "A question arises on the interpretation of rule 10(2). To whom is it referred?",
  "The Central Government",
  ("The President", "The President has the relaxation power under rule 16; interpretation goes elsewhere."),
  ("The Department of Expenditure's Pay Commission cell", "The rule names the Central Government, whatever internal body may assist it."),
  ("The Comptroller and Auditor General", "The CAG is consulted on the rules and audits expenditure, but is not the interpreting authority."),
  "Rule 17 provides that if any question arises relating to the interpretation of any provision of the rules, it shall be "
  "referred to the Central Government for decision. Pairing rule 16 and rule 17 is the standard test: relaxation for "
  "undue hardship sits with the President, interpretation with the Central Government.",
  "Interpretation → Central Government.",
  "Rule 17, CCS (Revised Pay) Rules, 2016",
  "Confusing the interpretation reference with the relaxation power")

print_ = None
