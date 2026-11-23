#!/usr/bin/env python3
"""data_bank2.py — the second tranche of rule questions.

The first tranche (data_bank.py) states each rule once, in the form the rule is
written. This tranche tests the same rules the way a paper tests them: the
Explanation that changes the answer, the negative form, the sequence, the
distinction between two provisions that read alike, and the case stated as a
short set of facts.
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
Q("RB-001", "1", "Rule 1(2)", "Commencement",
  "Which statement about the commencement of the 2016 Rules is correct?",
  "Notified on 25 July 2016; in force from 1 January 2016",
  ("Notified and in force from 1 January 2016",
   "The rules were not in existence in January; the gazette notification came in July."),
  ("Notified on 1 January 2016; in force from 25 July 2016",
   "The two dates are the other way round, and the earlier one is the date of effect, not the date of notification."),
  ("In force from 1 April 2016, the start of the financial year",
   "The financial year plays no part in rule 1(2); the date is the calendar 1 January."),
  "Rule 1(2) is a deeming provision: the rules were notified in the gazette on 25 July 2016 and are deemed to have "
  "come into force on 1 January 2016. Two dates doing two different jobs — the later one starts the three-month "
  "option period under rule 6, the earlier one starts the arrears under rule 14. A question that offers both dates "
  "in one option is testing whether you know which is which.",
  "Notification 25.07.2016; effect 01.01.2016.",
  "Rule 1(2), CCS (Revised Pay) Rules, 2016",
  "Swapping the date of notification with the date of effect")

# ---------------------------------------------------------------- rule 2
Q("RB-002", "2", "Rule 2(2)", "Applicability",
  "Which of the following is EXCLUDED from the 2016 Rules?",
  "A person re-employed in Government service after retirement",
  ("A person serving in the Indian Audit and Accounts Department",
   "Rule 2(1) expressly includes the IA&AD, after consultation with the C&AG."),
  ("A person appointed to a civil post on the Civil Estimates",
   "That is precisely the class rule 2(1) covers."),
  ("A person holding a post in a Ministry of the Central Government",
   "A civil post under the Central Government is the core of rule 2(1)."),
  "Rule 2(2) lists the exclusions, and the re-employed pensioner is one of them. The examination trick is the "
  "negative form: three options describe people plainly inside rule 2(1), and one describes a category the rule "
  "puts outside. Reading the question as 'who is covered' instead of 'who is excluded' inverts the answer.",
  "Re-employed pensioners are outside the rules.",
  "Rule 2(1) and 2(2), CCS (Revised Pay) Rules, 2016",
  "Answering the positive question when the stem asks for the exclusion")

Q("RB-003", "2", "Rule 2", "Applicability",
  "Rule 2 applies the 2016 Rules to persons serving in the Indian Audit and Accounts Department:",
  "After consultation with the Comptroller and Auditor General",
  ("Without any consultation whatever, the rules being general law applicable to every department alike",
   "The rule speaks of consultation, and the IA&AD is singled out for it."),
  ("On the recommendation of the Department of Expenditure, as the department that made the rules",
   "The consultation the rule requires is with the C&AG, not with the Department of Expenditure."),
  ("Only if the State Accountant General certifies their pay",
   "No certification by a State authority appears anywhere in the rule."),
  "Rule 2(1) applies the rules to persons serving in the Indian Audit and Accounts Department, and requires that "
  "this be done after consultation with the Comptroller and Auditor General. The IA&AD is audited by, and staffed "
  "under, an authority whose independence the Constitution protects, so the rule takes the trouble to name the "
  "consultation rather than leave it to general administrative practice.",
  "IA&AD: in, after consultation with the C&AG.",
  "Rule 2(1), CCS (Revised Pay) Rules, 2016",
  "Treating the IA&AD as an excluded department")

# ---------------------------------------------------------------- rule 3
Q("RB-004", "3", "Rule 3", "Definitions",
  "'Existing basic pay' for the purposes of rule 7 is:",
  "Pay in the Pay Band plus the grade pay",
  ("Pay in the Pay Band alone",
   "The grade pay is part of the pre-revised basic pay, and leaving it out understates the 2.57 product."),
  ("Pay in the Pay Band plus grade pay plus dearness allowance",
   "Dearness allowance is a separate element under 'existing emoluments'; it is not part of existing basic pay."),
  ("The minimum of the Pay Band, whatever the servant draws",
   "Existing basic pay is what the servant actually draws, not the floor of his band."),
  "Existing basic pay is the sum the fitment factor multiplies: pay in the pay band plus grade pay. The gazette "
  "illustration is the cleanest proof — 12,560 is 10,160 plus 2,400, and the grade pay is inside the figure that is "
  "multiplied. The adjacent definition, existing emoluments, adds dearness allowance to this sum and is used for a "
  "different purpose, protecting a servant from loss under rule 7(7).",
  "Existing basic pay = pay in band + grade pay. No DA.",
  "Rules 3(i) and 7(1)(A), CCS (Revised Pay) Rules, 2016",
  "Leaving the grade pay out of the figure that gets multiplied")

# ---------------------------------------------------------------- rule 4
Q("RB-005", "4", "Rule 4", "Level of posts",
  "The Level of a post under the 2016 Rules is determined by:",
  "The caption of the relevant column of the Pay Matrix",
  ("The pay the incumbent was drawing on 31 December 2015",
   "That decides the cell, not the Level; the Level is a property of the post."),
  ("An order of the Department of Expenditure in each individual case",
   "Rule 4 fixes the mapping in the Schedule; it does not call for a case-by-case order."),
  ("The grade pay the incumbent elects to retain under rule 5",
   "The option under rule 5 is about the pay STRUCTURE, not about which Level the post belongs to."),
  "Rule 4 provides that the Level of a post is as specified against it in Part A of the Schedule — in practice, the "
  "column caption that pairs an old Pay Band and Grade Pay with a Level. The mapping is a matter of reading the "
  "caption, and it belongs to the post, not to the person holding it. Two servants on the same post share a Level "
  "even if they are on different cells.",
  "Level belongs to the post, and it is read off the column caption.",
  "Rule 4 and Part A of the Schedule, CCS (Revised Pay) Rules, 2016",
  "Deriving the Level from the individual servant's pay")

Q("RB-006", "4", "Rule 4", "Level of posts",
  "Grade Pay ₹4,200 in Pay Band 2 (9300-34800) enters which Level?",
  "Level 6",
  ("Level 5", "Level 5 is Grade Pay ₹2,800 in PB-1."),
  ("Level 7", "Level 7 is Grade Pay ₹4,600 in PB-2."),
  ("Level 8", "Level 8 is Grade Pay ₹4,800 in PB-2."),
  "In PB-2 the grade pays climb ₹4,200, ₹4,600, ₹4,800 and ₹5,400 against Levels 6, 7, 8 and 9. Grade Pay ₹4,200 "
  "therefore enters Level 6, whose first cell is ₹35,400. The four Levels sit close together in the caption — one "
  "row apart each — which is why the mapping questions are usually answered by counting rows rather than recalling "
  "the number.",
  "PB-2: GP 4200 → L6, 4600 → L7, 4800 → L8, 5400 → L9.",
  "Rule 4 and Part A of the Schedule, CCS (Revised Pay) Rules, 2016",
  "Counting the Level rows from the wrong grade pay",
  level="6", cells=pm.matrix("6")[0:4], marks={"both": 1},
  table_note="Level 6, cells 1 to 4. Grade Pay ₹4,200 in PB-2 enters here, at ₹35,400 on cell 1.")

# ---------------------------------------------------------------- rule 5
Q("RB-007", "5", "Rule 5", "Option",
  "A servant elects the existing pay structure. Which statement is correct?",
  "He draws pay in the old structure until his next increment there",
  ("He is fixed in the revised structure and the option takes effect only for allowances",
   "The option is about the pay structure itself; allowances follow from whichever structure applies."),
  ("He must repay the arrears of the revised structure already drawn",
   "There is nothing to repay; arrears arise from the revised structure, which he has not entered."),
  ("He keeps the old structure for his whole remaining service",
   "The first proviso to rule 5 ends the old structure at his next increment in it."),
  "The first proviso to rule 5 allows a servant to continue in the existing pay structure until the date on which "
  "he earns his next or any subsequent increment in that structure, or until he vacates the post, whichever is "
  "earlier. So he stays on the old band and grade pay, drawing the old dearness allowance, and is brought into the "
  "matrix on the first increment date that falls after the option.",
  "Old structure ends at the next old-structure increment.",
  "Rule 5 and its first proviso, CCS (Revised Pay) Rules, 2016",
  "Believing the option is permanent")

Q("RB-008", "5", "Rule 5, Explanation 2", "Option",
  "A person appointed to his first Government post on 10 February 2016 asks to remain on the existing pay structure. "
  "What is the position?",
  "He cannot elect it — a first appointment on or after 01.01.2016 has no option",
  ("He may elect it, and may retain one Pay Band and Grade Pay",
   "Explanation 1 limits a valid option to one scale; it does not create an option for someone outside the eligible "
   "class."),
  ("He may elect it because he joined before the rules were notified on 25 July 2016",
   "The cut-off is the date of appointment, not the date of notification; a February 2016 appointee is after 1 January."),
  ("He may elect it until his first increment in the old structure",
   "The first proviso ends a valid option; it does not extend eligibility to a person Explanation 2 excludes."),
  "Explanation 2 to rule 5 provides that the option shall not be admissible to a person appointed to a post for the "
  "first time in Government service, or by transfer from another post, on or after 1 January 2016 — and that such a "
  "person shall be allowed pay only in the revised pay structure. So the option is not a choice open to everyone; it "
  "is confined to those already in service before 2016. Explanation 1 then limits even them to one Pay Band and Grade "
  "Pay.",
  "Appointed on or after 01.01.2016: no option at all, under Explanation 2.",
  "Rule 5, Explanation 2, CCS (Revised Pay) Rules, 2016",
  "Treating the option as available to every servant regardless of when he joined")

Q("RB-009", "6", "Rule 6(2)", "Exercise of option",
  "Once the option has been exercised, how may a servant revise it?",
  "He may not — and the option, once exercised, is final",
  ("He may revise it once, before his next increment",
   "There is no second chance; the rule makes the option final the moment it is exercised."),
  ("He may revise it within the three-month window",
   "A fresh election inside the window is not a revision of the option; the option itself is final when made."),
  ("He may revise it with the sanction of the Head of Office",
   "No departmental authority is given power to reopen a final option."),
  "Rule 6(4) provides that the option once exercised shall be final. Together with the three-month window in rule "
  "6(1) and the deemed election in rule 6(3), this is a closed scheme: decide in time, in writing, and live with "
  "it. The reason is administrative — the old and revised structures carried different dearness allowance, and a "
  "right of revision would let servants arbitrage the difference.",
  "Option in time, in writing, once — and final.",
  "Rules 6(3), 6(4), CCS (Revised Pay) Rules, 2016",
  "Treating the election as revisitable")

Q("RB-010", "6", "Rule 6(1)", "Exercise of option",
  "A servant is on deputation abroad on the last date for exercising the option. The time allowed to him is:",
  "Three months from taking charge in India",
  ("Three months from the date of notification, with no extension",
   "The proviso expressly extends the time for a servant who is out of India."),
  ("Three months from the date of his return to India, whenever that may be",
   "The proviso runs from the date he takes charge of a post in India, not from the date of arrival."),
  ("One year from the date of notification",
   "The rule gives three months, measured from a different starting point."),
  "The proviso to rule 6(1) gives a servant who is out of India on the date the option falls due three months from "
  "the date he takes charge of his post in India. The companion proviso does the same for a servant under "
  "suspension, running from his return to duty. Both are extensions of a three-month period, not fresh periods.",
  "Out of India: three months from taking charge in India.",
  "Rule 6(1) and its provisos, CCS (Revised Pay) Rules, 2016",
  "Running the extension from the date of arrival rather than the date of taking charge")

# ---------------------------------------------------------------- rule 7
Q("RB-011", "7", "Rule 7(1)(A)(i)", "Fixation",
  "In rule 7(1)(A)(i), the servant's pay is fixed at:",
  "The cell equal to the figure, or the next higher cell",
  ("The cell nearest to the figure, whether above or below",
   "The rule never goes down: it takes the equal cell, or failing that the next higher one."),
  ("The cell below the figure, so that the increment absorbs the excess",
   "That would leave the servant with less than his entitlement under the multiplication."),
  ("The first cell of the Level, without reference to the figure",
   "The first cell is the rule only where the figure falls below it, under clause (ii)."),
  "Clause (i) of rule 7(1)(A) directs the figure to be located in the Level and pay to be fixed at the cell equal "
  "to it or, if there is no such cell, at the next higher cell. The direction is one-way by design: a servant "
  "should not lose by the conversion, so the excess of the cell over the figure is not recovered from him. That is "
  "why the gazette's ₹32,279 becomes ₹32,300, and the ₹21 is simply left.",
  "Equal or next HIGHER. Never lower.",
  "Rule 7(1)(A)(i), CCS (Revised Pay) Rules, 2016",
  "Rounding the cell choice to the nearest figure")

Q("RB-012", "7", "Rule 7", "Fixation",
  "Which of these gets rule 7(1)(A) wrong?",
  "Multiplying by 2.57 and then adding the grade pay",
  ("Multiplying the pay in the Pay Band and the grade pay together by 2.57, then rounding the product to the rupee",
   "That is the rule. The grade pay goes into the figure before the multiplication, and the rounding is of the "
   "product, which is what has the fraction."),
  ("Rounding the product to the nearest rupee before looking for a cell, and taking the next higher cell if there is "
   "no equal one",
   "That is the rule, step for step: round the product, then locate it, going up and never down."),
  ("Taking the first cell of the Level where the product falls below it, instead of the product itself",
   "That is clause (ii) of rule 7(1)(A), which exists for exactly that case."),
  "There is an order and the rule is written in it: assemble existing basic pay as pay in the band PLUS grade pay, "
  "multiply by 2.57, round the product to the rupee, then locate that figure in the Level and take the equal or next "
  "higher cell. Adding the grade pay after the multiplication puts it outside the factor — the servant would get "
  "2.57 times his band pay and then a flat grade pay, which is not what the rule says and understates the result.",
  "Grade pay is inside the figure that gets multiplied.",
  "Rule 7(1)(A)(i) and (ii), CCS (Revised Pay) Rules, 2016",
  "Adding the grade pay after the multiplication instead of before it")

Q("RB-013", "7", "Rule 7(6)", "Merged Levels",
  "Two posts in different Pay Bands are placed in the same Level by the Schedule. Their pay on fixation:",
  "Is fixed in the same Level, each on his own figure",
  ("Is fixed at the first cell of the merged Level for both of them alike",
   "The first cell is for direct recruits under rule 8; existing servants are fixed on their own figures."),
  ("Continues in the two old Pay Bands until each servant is promoted",
   "The merger is the point of the exercise; the old bands do not survive it."),
  ("Is fixed by taking the higher of the two old Pay Bands for both",
   "Fixation is individual, on each servant's own existing basic pay."),
  "Rule 7(6) deals with the case where two or more posts in different Pay Bands are placed in the same Level. Each "
  "servant is fixed independently under clause (A): his own existing basic pay is multiplied by 2.57 and located in "
  "the Level. Two servants from different bands may therefore finish on the same cell, or on cells apart, "
  "according to their own pay — the merger of the Level does not merge their pay.",
  "Merged Level, not merged pay: each servant is fixed on his own figure.",
  "Rule 7(6), CCS (Revised Pay) Rules, 2016",
  "Assuming a merger of Levels equalises the pay of the servants in them")

Q("RB-014", "7", "Rule 7(9)", "Pay above the matrix",
  "A servant's existing basic pay, multiplied by 2.57, exceeds the last cell of his Level. What happens?",
  "He is fixed at the last cell of the Level",
  ("He is placed in the next higher Level at the corresponding cell",
   "A fixation under rule 7(1)(A) never changes the Level of the post; the Level is fixed by rule 4."),
  ("He is placed at a cell above the last one, created for the purpose",
   "The matrix has no cells beyond the last one of a column; nothing is created on fixation."),
  ("His pay is left unrevised until the Level is revised",
   "Fixation still takes place; the question is where it lands."),
  "Rule 7(9) covers the servant whose 2.57 figure runs past the top of his Level. He is fixed at the last cell of "
  "the Level; the matrix cannot take him higher, because the column ends. In practice this is rare — the top cells "
  "of the lower Levels are high enough for almost every servant — but it is the reason rule 7(9) exists, and the "
  "reason a pay fixation statement must show the Level's last cell alongside the figure.",
  "Above the top of the Level: the last cell, and no further.",
  "Rule 7(9), CCS (Revised Pay) Rules, 2016",
  "Inventing a cell above the end of the column",
  level="1", cells=pm.matrix("1")[-3:], marks={"land": 40},
  table_note="The last three cells of Level 1. Cell 40 is ₹56,900, and the column stops there — a figure above it "
             "has nowhere in this Level to land.")

Q("RB-015", "7", "Rule 7(11)", "Officiating pay",
  "A servant officiating in a higher post draws less than the pay of the lower post he substantively holds. The rule "
  "requires:",
  "His pay fixed at a stage not below his substantive post",
  ("His officiating appointment to be terminated",
   "The rule regulates the pay of the officiating appointment; it does not end it."),
  ("The difference to be paid as personal pay until he is confirmed",
   "Personal pay protects an excess of old over new emoluments; this rule sets a floor, not a supplement."),
  ("Nothing, because an officiating appointment carries no protection",
   "Rule 7(11) exists precisely to give that protection."),
  "Rule 7(11) provides that a servant officiating in a higher post shall be paid at a stage in the officiating post "
  "which is not less than the stage he would have reached in his substantive post. Without it, a promotion by "
  "officiation could leave a servant worse off than staying where he was — which is the anomaly the rule is written "
  "to prevent.",
  "Officiating pay never falls below the substantive stage.",
  "Rule 7(11), CCS (Revised Pay) Rules, 2016",
  "Treating officiating pay as free of any floor")

# ---------------------------------------------------------------- rule 8
Q("RB-016", "8", "Rule 8", "Direct recruits",
  "A direct recruit joins a Level 6 post on 1 March 2016. His pay is:",
  "₹35,400, the first cell of Level 6",
  ("₹90,978, being ₹35,400 × 2.57, on the analogy of existing servants",
   "The fitment factor applies to an existing basic pay; a recruit has none to fit."),
  ("₹36,500, the second cell, because he joined in the second half-year",
   "The half-year affects the increment date under rule 10, not the starting cell under rule 8."),
  ("₹30,300, being the 6th CPC entry pay of ₹11,800 with grade pay",
   "That is the pre-revised figure; the revised starting point is the matrix's first cell."),
  "Rule 8 fixes the pay of a direct recruit appointed on or after 1 January 2016 at the minimum pay or the first "
  "cell of the Level. For Level 6 the column opens at ₹35,400. His increment date is then fixed by rule 10(2) from "
  "the date of his appointment: 1 March falls between 2 January and 1 July, so his first increment falls on 1 "
  "January 2017.",
  "Direct recruit: first cell, and the increment date from the joining date.",
  "Rules 8 and 10(2), CCS (Revised Pay) Rules, 2016",
  "Applying the fitment factor to a direct recruit",
  level="6", cells=pm.matrix("6")[0:4], marks={"both": 1},
  table_note="Level 6, cells 1 to 4. Every direct recruit starts on cell 1, ₹35,400.")

Q("RB-017", "8", "Rule 8, proviso", "Direct recruits",
  "The proviso to rule 8 allows personal pay to a direct recruit in which case?",
  "Where he joined before the notification with higher fixed emoluments",
  ("Wherever his qualifications are higher than those prescribed for the post",
   "Qualifications play no part in the proviso; it is about a pay figure already fixed."),
  ("Where he joins after 25 July 2016, the date of notification",
   "The proviso is about the window BEFORE the notification, not after it."),
  ("Where his previous employer paid him more than the first cell",
   "The comparison is with the emoluments already fixed in Government service, not with a private employer."),
  "The proviso to rule 8 is narrow. It covers a direct recruit appointed between 1 January 2016 and the date of "
  "notification whose emoluments had already been fixed and exceeded the first cell of the Level. Personal pay "
  "makes up the difference, and is absorbed by later increments. The rule is not a general protection for new "
  "entrants, and it closes once the rules are notified.",
  "The rule 8 proviso is a closed window: 01.01.2016 to notification.",
  "Rule 8 and its proviso, CCS (Revised Pay) Rules, 2016",
  "Reading the proviso as a general protection for new entrants")

# ---------------------------------------------------------------- rule 9
Q("RB-018", "9", "Rule 9", "Increments",
  "Where an increment is withheld as a measure of punishment, the effect on the matrix position is that:",
  "He does not move to the next cell",
  ("The servant moves to the next cell but draws the old pay for the period of the punishment",
   "A withheld increment means the move itself does not happen; the cell IS the pay."),
  ("The servant is moved back one cell for the period",
   "Withholding stops the movement; it does not reverse it."),
  ("The Level itself is reduced for the period of the punishment",
   "The Level belongs to the post and is not altered by a punishment withholding an increment."),
  "Because rule 9 makes the increment a movement down the vertical cells of the Level, withholding an increment "
  "operates on that movement: the servant stays on the cell he is on for the period of the withholding. The "
  "consequence is cumulative, because the cells he would have passed are never reached — which is why a withheld "
  "increment is a heavier punishment than a year's loss of pay.",
  "Withholding holds the servant on the cell; the loss compounds.",
  "Rule 9, read with the CCS (CCA) Rules, CCS (Revised Pay) Rules, 2016",
  "Treating a withheld increment as a one-year deduction")

Q("RB-019", "9", "Rule 9", "Increments",
  "A servant is drawing a cell that is not the last of his Level. On his increment date he:",
  "Moves one cell down the same Level, whatever the rupee step",
  ("Moves to the cell that is 3% above his pay, rounded up",
   "The 3% is in the matrix already; the rule asks for the next cell, not a fresh computation."),
  ("Moves to the corresponding cell of the next Level",
   "Changing Level is promotion or MACP, never an increment."),
  ("Moves one cell, and also draws a special increment for the year",
   "Rule 9 gives one movement; there is no annual special increment in the matrix."),
  "Rule 9 makes the increment the next vertical cell of the applicable Level, and nothing more. Because the matrix "
  "rounds each cell to the nearest ₹100, the rupee step is not constant even within a Level: in Level 4 the first "
  "steps are ₹800 and later steps are ₹900. The servant's entitlement is the cell, not the percentage.",
  "One cell. The rupee step is whatever the matrix makes it.",
  "Rule 9, CCS (Revised Pay) Rules, 2016",
  "Recomputing the increment as a percentage of current pay")

# ---------------------------------------------------------------- rule 10
Q("RB-020", "10", "Rule 10(2)", "Increment date",
  "A servant is appointed on 2 January 2017. His first increment falls on:",
  "1 January 2018",
  ("1 July 2017",
   "1 July is the date for appointments between 2 July and 1 January. A January appointment is in the other window."),
  ("1 January 2019, after a full year in the Level",
   "The half-year rule gives him the next 1 January, not a year after that."),
  ("2 January 2018, on his first anniversary",
   "The revised structure has no anniversary increments; it has two fixed dates."),
  "Rule 10(2) assigns 2 January to 1 July to 1 January, and 2 July to 1 January to 1 July — both ends inclusive. An "
  "appointment on 2 January falls at the very start of the first window, so his increment falls on the next 1 "
  "January, 2018. Note how close the two ends are: an appointment on 1 January goes to 1 July, and one on 2 January "
  "goes to 1 January, a day apart in the calendar and six months apart in the increment.",
  "2 January → 1 January. 1 January → 1 July.",
  "Rule 10(2), CCS (Revised Pay) Rules, 2016",
  "Missing the one-day boundary between the two windows")

Q("RB-021", "10", "Rule 10(2)", "Increment date",
  "Two servants are promoted on the same day, one on 1 July 2016 and the other on 2 July 2016. Their next increments "
  "fall on:",
  "1 January 2017 for the first, 1 July 2017 for the second",
  ("1 July 2017 for both, since both were promoted in July",
   "The rule turns on the exact date, and 1 July closes the first window while 2 July opens the second."),
  ("1 January 2017 for both, since both were promoted in the first half of the year",
   "The windows are not halves of the year but 2 January–1 July and 2 July–1 January."),
  ("1 July 2016 for the first, 1 January 2017 for the second",
   "An increment cannot fall on the date of the promotion itself."),
  "Rule 10(2) splits the year at 1 July and 1 January, with both ends inclusive. 1 July is the LAST day of the "
  "window that goes to 1 January; 2 July is the FIRST day of the window that goes to 1 July. Two servants promoted "
  "a day apart therefore wait six months apart for their increment, and the same pattern recurs at 1 and 2 January.",
  "1 July → the coming 1 January. 2 July → the coming 1 July.",
  "Rule 10(2), CCS (Revised Pay) Rules, 2016",
  "Believing both July appointments fall in the same window")

# ---------------------------------------------------------------- rule 11
Q("RB-022", "11", "Rule 11", "Late switch-over",
  "A servant who switched to the revised structure on 1 July 2017 is entitled to arrears from:",
  "1 July 2017, the date of his switch-over",
  ("1 January 2016, the date the rules came into force",
   "A servant who stayed on the old structure was paid under it until he switched; there is no arrears for that period."),
  ("1 January 2017, the preceding 1 January",
   "There is no provision carrying the switch-over back to an earlier 1 January."),
  ("25 July 2016, the date of notification",
   "Notification is not the date from which a late switch-over operates."),
  "Rule 11 fixes the pay of a servant revising his pay from a date later than 1 January 2016 in the manner "
  "prescribed by rule 7(1)(A). The revised pay runs from the date of the revision, so the arrears run from that "
  "date too. Until then he was drawing, and was entitled to draw, the old pay with the old dearness allowance. "
  "Rule 14's arrears are for the gap between revision and notification, not for a period the servant spent "
  "outside the revised structure by his own election.",
  "Late switch: pay and arrears both run from the switch date.",
  "Rules 11 and 14, CCS (Revised Pay) Rules, 2016",
  "Awarding a late switcher the arrears of the whole period from 01.01.2016")

# ---------------------------------------------------------------- rule 12
Q("RB-023", "12", "Rule 12", "Deputation and personal pay",
  "Personal pay granted under rule 12 is:",
  "Absorbed in future increments of pay",
  ("A permanent addition to basic pay until retirement",
   "Personal pay is by design absorbable; a permanent addition would defeat the purpose of the matrix."),
  ("Paid as a lump sum on the date of notification",
   "It is a monthly protection, not a one-off payment."),
  ("Converted into a higher cell on confirmation of the deputation",
   "The rule protects the difference as personal pay; it does not move the servant up the matrix."),
  "Rule 12 protects the pay of an officer on deputation under the Central Staffing Scheme by granting the "
  "difference as Personal Pay with effect from the date of notification. Personal pay is absorbed as increments "
  "raise the pay it is added to, so the protection diminishes by itself and disappears when the servant's pay "
  "catches up. The same technique appears in rules 7(7), 8 and 9; it is the standard way the rules protect a "
  "figure without departing from the matrix.",
  "Personal pay is always absorbable.",
  "Rule 12, CCS (Revised Pay) Rules, 2016",
  "Treating personal pay as a permanent addition")

# ---------------------------------------------------------------- rule 13
Q("RB-024", "13", "Rule 13(i)", "Promotion",
  "On promotion, the pay is fixed at the equal or next higher cell of the new Level in relation to:",
  "The stepped figure in the old Level",
  ("The pay drawn in the old Level before any increment",
   "Skipping the increment understates the promoted pay by one full step, every time."),
  ("The first cell of the new Level",
   "That is the treatment of a direct recruit under rule 8."),
  ("The average of the old and new Levels",
   "The rules contain no averaging device for promotion."),
  "Rule 13(i) has two limbs and they run in order. First, one increment is granted in the Level from which the "
  "servant is promoted. Second, that figure is placed in the Level of the promoted post at the cell equal to it, "
  "or at the next higher cell. The reference point for the second limb is therefore the post-increment figure in "
  "the old Level — ₹29,600 in the gazette illustration — not the pre-increment ₹28,700.",
  "The reference point is the stepped figure in the OLD Level.",
  "Rule 13(i), CCS (Revised Pay) Rules, 2016",
  "Taking the equal-or-next-higher cell from the pre-increment pay")

Q("RB-025", "13", "Rule 13(i)", "Promotion",
  "A servant drawing ₹44,900 in Level 7 is promoted to Level 8. Level 8 opens at ₹47,600. His pay becomes:",
  "₹47,600, the first cell of Level 8",
  ("₹46,200, his pay after the increment in Level 7",
   "₹46,200 is the stepping stone, and it is not a cell of Level 8; the rule then takes the next higher cell."),
  ("₹49,000, the second cell, to give him a full step",
   "The rule takes the equal or next higher cell, not a fixed number of steps."),
  ("₹44,900, unchanged until the next increment date",
   "A promotion always fixes the pay on the date of promotion."),
  "The increment in Level 7 takes ₹44,900 to ₹46,200. Level 8's cells are ₹47,600, ₹49,000 and so on, so ₹46,200 has "
  "no equal cell and the rule takes the next higher one, ₹47,600. The servant therefore gains ₹2,700 on promotion, "
  "of which ₹1,300 is the old-Level increment and ₹1,400 the jump to the higher Level's first cell. It is worth "
  "noticing that his promotion gain is larger than his increment, which is unusual and is exactly why the example "
  "is used.",
  "44,900 → 46,200 (old Level) → 47,600 (first cell of the new).",
  "Rule 13(i), CCS (Revised Pay) Rules, 2016",
  "Stopping at the stepped figure because it happens to be printed in the old Level",
  level="8", cells=pm.matrix("8")[0:4], marks={"land": 1},
  table_note="Level 8, cells 1 to 4. The stepped figure of ₹46,200 in Level 7 is below cell 1 (₹47,600), so the "
             "promotion lands on ₹47,600.")

Q("RB-026", "13", "Rule 13", "Promotion",
  "The combined effect of rule 13 is best described as:",
  "Increment first, in the old Level",
  ("Placement in the new Level, then an increment in the new Level afterwards",
   "That is the sequence the rule forbids, because it pays the increment at the higher Level's rates."),
  ("Two increments in the old Level, then placement",
   "Two increments is the FR 22(I)(a)(1) option, not the default under rule 13."),
  ("Placement at the same cell number in the new Level",
   "The matrix has no rule matching cell for cell across Levels; the figures differ."),
  "Rule 13(i) is a single operation with a fixed order: increment where you are, then move. Putting the increment "
  "after the move would pay it at the rates of the higher Level and give a larger gain than the rule intends. The "
  "FR 22(I)(a)(1) option is the one route to two increments, and it is a choice the servant makes, not the default.",
  "Increment first, in the OLD Level. Then place.",
  "Rule 13(i), read with FR 22(I)(a)(1), CCS (Revised Pay) Rules, 2016",
  "Reversing the order to pay the increment in the new Level")

# ---------------------------------------------------------------- rule 14
Q("RB-027", "14", "Rule 14", "Arrears",
  "Arrears under rule 14 are computed on the difference between:",
  "Pay plus dearness allowance, revised and unrevised",
  ("Basic pay alone, revised and unrevised",
   "The Explanation to rule 14 expressly includes dearness allowance on both sides of the comparison."),
  ("Gross salary, including all allowances",
   "The comparison is of pay and dearness allowance, not of every allowance drawn."),
  ("The revised pay and the pay the servant would have drawn after his next increment",
   "The comparison is with the unrevised position over the same period, not with a future increment."),
  "The Explanation to rule 14 defines arrears as the difference between the aggregate of pay AND dearness allowance "
  "admissible under the revised structure from 1 January 2016, and the aggregate that would have been admissible "
  "had the pay not been revised. Both sides of the comparison carry DA, which is why a servant who stayed on the "
  "old structure and one who moved to the new can be compared on a like-for-like basis.",
  "Both sides of the arrears comparison carry DA.",
  "Rule 14 and its Explanation, CCS (Revised Pay) Rules, 2016",
  "Computing arrears on basic pay without dearness allowance")

# ---------------------------------------------------------------- rule 15
Q("RB-028", "15", "Rule 15", "Overriding effect",
  "Which of these is NOT among the sets of rules overridden by rule 15?",
  "The CCS (Leave) Rules, 1972",
  ("The CCS (Revised Pay) Rules, 2008",
   "Rule 15 names the 2008 rules expressly."),
  ("The CCS (Revised Pay) Rules, 1997",
   "Rule 15 names the 1997 rules expressly."),
  ("The Fundamental Rules",
   "Rule 15 overrides the Fundamental Rules to the extent of any inconsistency."),
  "Rule 15's list is of pay rules and the Fundamental Rules: the FRs, and the Revised Pay Rules of 1947, 1960, "
  "1973, 1986, 1997 and 2008. The CCS (Leave) Rules, 1972 are not in it — they govern leave, and where leave "
  "salary is calculated on pay the 1972 Rules simply take the pay as the 2016 Rules leave it. The negative form of "
  "the question is the point: an examiner lists three named rules and one plausible stranger.",
  "Rule 15 overrides pay rules and the FRs — not the leave rules.",
  "Rule 15, CCS (Revised Pay) Rules, 2016",
  "Assuming every earlier CCS rule is overridden")

# ---------------------------------------------------------------- rule 16 and 17, paired
Q("RB-029", "16", "Rule 16", "Relaxation",
  "Undue hardship in a particular case under the 2016 Rules may be relieved by:",
  "The President, by order",
  ("The Central Government, on a reference under rule 17",
   "Rule 17 is about interpretation; the relief of hardship is rule 16 and it names the President."),
  ("The Department of Expenditure, by a general order",
   "The power is case-specific and is given to the President."),
  ("The Head of Department, with the concurrence of Finance",
   "No departmental authority holds the relaxation power under these rules."),
  "Rule 16 allows the President, if satisfied that the operation of any provision causes undue hardship in a "
  "particular case, to dispense with or relax that provision to such extent and on such conditions as he thinks "
  "necessary. Note the two limits in the words: a particular case, not a class of cases, and such conditions as "
  "he thinks fit. It is a safety valve, not a power to amend the rules.",
  "Relaxation is presidential, case-specific and conditional.",
  "Rule 16, CCS (Revised Pay) Rules, 2016",
  "Treating the relaxation power as a general power to amend")

Q("RB-030", "16", "Rule 16", "Relaxation",
  "A question arises whether a particular allowance falls within the definition of 'pay' in rule 3. The reference is "
  "to:",
  "The Central Government, under rule 17",
  ("The President, under rule 16",
   "Rule 16 relieves hardship; it does not decide what a definition means."),
  ("The Department of Personnel and Training, as the cadre authority",
   "The rules name the Central Government; the department through which it acts is an administrative matter."),
  ("The Pay Commission that recommended the structure",
   "A Pay Commission is a recommendatory body and has no continuing jurisdiction over the rules."),
  "Rule 17 provides that any question relating to the interpretation of the rules shall be referred to the Central "
  "Government for decision. An allowance's place within the definition of pay is an interpretation question, so it "
  "goes under rule 17, not rule 16. The pair is the standard test: hardship goes to the President, meaning goes to "
  "the Central Government.",
  "Meaning → rule 17, Central Government. Hardship → rule 16, President.",
  "Rules 16 and 17, CCS (Revised Pay) Rules, 2016",
  "Sending an interpretation question to the President")

# ---------------------------------------------------------------- case files
Q("RB-031", "7", "Rule 7(1)(A)", "Case file",
  "A clerk in Level 4 was drawing ₹10,160 in the Pay Band with Grade Pay ₹2,400 on 31 December 2015. On 1 July 2016 "
  "he is still on the old structure. On fixation, which of these is correct?",
  "₹32,300, cell 9 of Level 4, when he enters the revised structure",
  ("₹32,279 — the product, without rounding to a cell",
   "The product is located in the matrix; ₹32,279 is not a cell, so the rule takes the next higher one."),
  ("₹31,400, cell 8, because it is the nearest cell",
   "The rule does not choose the nearest cell; it goes up to the next cell, never down."),
  ("No fixation at all, because he elected to remain on the old structure",
   "The election ends at his next increment in the old structure, and the fixation is then made."),
  "His existing basic pay is 10,160 + 2,400 = 12,560. Multiplied by 2.57 that is 32,279.20, rounded to 32,279, which "
  "is not a cell of Level 4 — cell 8 is 31,400 and cell 9 is 32,300 — so the rule takes the next higher cell. This "
  "is the gazette's own illustration, and the figures have not been altered in the reproduction.",
  "12,560 × 2.57 = 32,279 → ₹32,300, cell 9 of Level 4.",
  "Rule 7(1)(A)(i) and its gazette illustration, CCS (Revised Pay) Rules, 2016",
  "Stopping at the product, or dropping to the nearest cell",
  level="4", cells=pm.matrix("4")[6:12], marks={"land": 9},
  table_note="Level 4, cells 7 to 12. The product of ₹32,279 falls between cell 8 (₹31,400) and cell 9 (₹32,300), so "
             "it lands on cell 9.")

Q("RB-032", "13", "Rule 13(i)", "Case file",
  "An assistant in Level 4 at ₹28,700 is promoted to Level 5 on 1 September 2016. Which statement is correct?",
  "₹30,100 in Level 5, increment on 1 July 2017",
  ("₹29,600 in Level 5, because that is the stepped figure",
   "₹29,600 is a Level 4 figure; Level 5 has no such cell, so the next higher cell applies."),
  ("₹28,700 in Level 5, unchanged, with the next increment on 1 July 2017",
   "A promotion on 1 September falls in the 2 July–1 January window, which gives 1 July."),
  ("₹31,000 in Level 5, by taking two increments for the promotion",
   "Two increments is the FR 22 option, which the servant must elect; it is not the default."),
  "Two things happen, and they are separate. Rule 13(i) fixes the pay: 28,700 steps to 29,600 in Level 4, and "
  "29,600 has no equal cell in Level 5, so the pay is fixed at 30,100 on cell 2. Rule 10(2) then fixes the "
  "increment date from the date of promotion: 1 September lies between 2 July and 1 January, so the next increment "
  "is on 1 July 2017. Pay and date are governed by different rules and must be worked separately.",
  "Pay under rule 13, date under rule 10(2). Two questions, not one.",
  "Rules 13(i) and 10(2), CCS (Revised Pay) Rules, 2016",
  "Answering the pay question correctly and the date question from the promotion date's month",
  level="5", cells=pm.matrix("5")[0:5], marks={"land": 2},
  table_note="Level 5, cells 1 to 5. The stepped figure of ₹29,600 is below cell 1 (₹29,200)? No — it lies between "
             "cell 1 and cell 2, so the pay is fixed on cell 2, ₹30,100.")

Q("RB-033", "12", "Rule 12", "Case file",
  "An IAS officer is on deputation to a Central Ministry under the Central Staffing Scheme. But for the deputation he "
  "would have drawn ₹1,80,000 in his parent cadre; on the deputation he draws ₹1,71,000. Rule 12 gives him:",
  "₹9,000 as personal pay, absorbed by future increments",
  ("₹4,500, half the difference, as a permanent addition to his deputation pay",
   "Personal pay is absorbed as increments accrue; it is not permanent."),
  ("Nothing, because the deputation pay is regulated by the deputation terms",
   "Rule 12 is precisely the protection against that result for a Central Staffing Scheme officer."),
  ("Re-fixation at ₹1,80,000 in the deputation Level",
   "The matrix has no such cell in most Levels, and the rule uses personal pay rather than a cell."),
  "Rule 12 protects the difference as Personal Pay with effect from the date of notification. The officer draws "
  "1,71,000 plus 9,000, and the 9,000 is absorbed as increments raise the 1,71,000 until the two meet. Note the "
  "three conditions the rule needs: a posting under the Central Staffing Scheme, a parent-cadre pay that would have "
  "been higher, and a computation from the date of notification rather than from 1 January 2016.",
  "CSS deputation, difference as personal pay, from 25.07.2016, absorbed.",
  "Rule 12, CCS (Revised Pay) Rules, 2016",
  "Dating the protection from 01.01.2016 instead of notification")

Q("RB-034", "14", "Rule 14", "Case file",
  "A servant was on the old structure until 30 June 2017, when his next old-structure increment ended his option and "
  "he entered the revised structure. His arrears under rule 14 are for:",
  "Nothing at all",
  ("The whole period from 1 January 2016 to 30 June 2017, since the rules took effect in January",
   "He was lawfully drawing the old structure in that period and has no claim to the revised pay for it."),
  ("The period from 25 July 2016 to 30 June 2017",
   "Notification is not the date from which his revised pay runs; the switch-over date is."),
  ("A period to be fixed by the Head of Department",
   "The rules fix the position; there is no discretion to award arrears for a period spent on the old structure."),
  "Arrears under rule 14 arise because the revised structure operated from 1 January 2016 while the rules were "
  "notified in July. A servant who elected the old structure was paid under it, lawfully, until his option ended. "
  "He enters the revised structure on 1 July 2017 under rule 11, and his revised pay runs from that date. He "
  "therefore has no arrears for the period before it — the election cost him the arrears and gained him the old "
  "structure.",
  "An old-structure election forfeits the arrears for the period it covers.",
  "Rules 5, 11 and 14, CCS (Revised Pay) Rules, 2016",
  "Awarding arrears to a servant who had elected the old structure")

Q("RB-035", "13", "Rule 13(ii)", "Case file",
  "A senior medical officer's basic pay plus Non Practicing Allowance is computed at ₹2,45,000 after fixation. The "
  "ceiling in rule 13(ii) is averaged from Levels 17 and 18. What follows?",
  "The excess above ₹2,37,500 is not admissible, so the NPA is trimmed",
  ("The basic pay itself is reduced to bring the total within the ceiling",
   "The cap operates on pay plus NPA; it does not rewrite the cell the officer has been fixed on."),
  ("Nothing, because the cap applies only to officers below Level 15",
   "The rule draws no such line; it applies to every servant receiving NPA."),
  ("The officer is placed in Level 18 to accommodate the figure",
   "There is no upward movement in the rule; the cap restricts, it does not promote."),
  "The ceiling is the average of the basic pay of the Apex Level (Level 17, ₹2,25,000) and the Level of the Cabinet "
  "Secretary (Level 18, ₹2,50,000), which is ₹2,37,500. A total of ₹2,45,000 exceeds it by ₹7,500, and the NPA — "
  "not the basic pay — is trimmed to bring the total within the cap. This is the one place in the rules where a "
  "figure in the matrix is used as a ceiling rather than a destination.",
  "NPA cap = (₹2,25,000 + ₹2,50,000) ÷ 2 = ₹2,37,500. The NPA gives way.",
  "Rule 13(ii), CCS (Revised Pay) Rules, 2016",
  "Reducing basic pay instead of the allowance to meet the cap")

print_ = None
