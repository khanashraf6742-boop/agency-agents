#!/usr/bin/env python3
"""rules.py — the seventeen rules of the CCS (Revised Pay) Rules, 2016.

Text is the notified gazette text (G.S.R. 721(E), 25.07.2016), clause by clause.
Where an amendment has since moved a figure, the amendment is recorded in
AMENDMENTS and the rule carries a pointer, so a question can test either the
rule as notified or the position as it now stands.
"""
from __future__ import annotations

from verbatim import TEXT as VERBATIM

RULES = [
    dict(no="1", title="Short title and commencement",
         chapter="I",
         text="(1) These rules may be called the Central Civil Services (Revised Pay) Rules, 2016. "
              "(2) They shall be deemed to have come into force on the 1st day of January, 2016.",
         bare="Notified 25.07.2016; deemed to come into force on 01.01.2016.",
         why="The rules were notified in July but operate from January. Everything — arrears, the option, "
             "the increment date — is measured from 1 January 2016, not from the date of the gazette.",
         figures=["01.01.2016", "25.07.2016"],
         trap="Treating 25.07.2016, the date of notification, as the date of effect.",
         hooks=["notification", "effective date", "commencement"]),

    dict(no="2", title="Categories of Government servants to whom the rules apply",
         chapter="II",
         text="(1) Save as otherwise provided by or under these rules, these rules shall apply to persons appointed to civil "
              "services and posts in connection with the affairs of the Union whose pay is debitable to the Civil Estimates "
              "as also to persons serving in the Indian Audit and Accounts Department. (2) These rules shall not apply to— "
              "(i) persons appointed to the Central Civil Services and posts in Group 'A', 'B' and 'C', under the "
              "administrative control of the Administrator of the Union Territory of Chandigarh; (ii) persons locally recruited "
              "for services in Diplomatic, Consular or other Indian establishments in foreign countries; (iii) persons not in "
              "whole-time employment; (iv) persons paid out of contingencies; (v) persons paid otherwise than on a monthly "
              "basis including those paid only on a piece rate basis; (vi) persons employed on contract except where the "
              "contract provides otherwise; (vii) persons re-employed in Government service after retirement; (viii) any other "
              "class or category of persons whom the President may, by order, specifically exclude.",
         bare="Applies to Union civil posts on the Civil Estimates and to the IA&AD. Eight exclusions, including Chandigarh "
              "UT staff, locally recruited staff abroad, part-timers, contingent-paid staff, non-monthly and piece-rate "
              "staff, contract staff, and re-employed pensioners.",
         why="The exclusion of re-employed pensioners is the one examiners reach for: a re-employed officer draws pay under "
             "a different dispensation, and the Revised Pay Rules do not fix it. Contract staff are excluded unless the "
             "contract says otherwise — the proviso runs the other way from what candidates assume.",
         figures=["eight exclusions"],
         trap="Assuming a re-employed pensioner is covered because he is a Government servant.",
         hooks=["applicability", "exclusion", "re-employed", "contract", "Chandigarh"]),

    dict(no="3", title="Definitions",
         chapter="I",
         text="In these rules, unless the context otherwise requires,— (i) 'existing basic pay' means pay drawn in the "
              "prescribed existing Pay Band and Grade Pay or pay in the existing scale; (ii) 'existing Pay Band and Grade Pay' "
              "means the Pay Band and Grade Pay applicable to the post held as on the date immediately before the notification "
              "of these rules, whether in a substantive or officiating capacity; (iii) 'existing scale' means the pay scale "
              "applicable in the Higher Administrative Grade, HAG+, Apex scale and that applicable to the Cabinet Secretary; "
              "(iv) 'existing pay structure' means the present system of Pay Band and Grade Pay or the pay scale applicable as "
              "on the date immediately before the coming into force of these rules; (v) 'existing emoluments' mean the sum of "
              "(i) existing basic pay and (ii) existing dearness allowance at index average as on 1st day of January, 2006; "
              "(vi) 'Pay Matrix' means the Matrix specified in Part A of the Schedule, with Levels of pay arranged in vertical "
              "cells; (vii) 'Level' means the Level corresponding to the existing Pay Band and Grade Pay or scale; (viii) 'pay "
              "in the Level' means pay drawn in the appropriate Cell of the Level; (ix) 'revised pay structure' means the Pay "
              "Matrix and the Levels specified therein; (x) 'basic pay' in the revised pay structure means the pay drawn in the "
              "prescribed Level in the Pay Matrix; (xi) 'revised emoluments' means the pay in the Level; (xii) 'Schedule' "
              "means a schedule appended to these rules.",
         bare="Defines existing basic pay, Pay Matrix, Level, cell, revised pay structure and revised emoluments. Note what "
              "'revised emoluments' means: the pay in the Level, and nothing else.",
         why="Two definitions carry marks. First, basic pay in the revised structure is the pay in the Level — a single "
             "figure, with no grade pay added, because grade pay has been absorbed into the matrix. Second, revised "
             "emoluments means pay in the Level alone: not pay plus allowances.",
         figures=["twelve definitions"],
         trap="Adding grade pay to the revised basic pay, which no longer exists as a separate element.",
         hooks=["definition", "basic pay", "revised emoluments", "cell"]),

    dict(no="4", title="Level of posts",
         chapter="II",
         text="The Level of posts shall be determined in accordance with the various Levels as assigned to the corresponding "
              "existing Pay Band and Grade Pay or scale as specified in the Pay Matrix.",
         bare="A post's Level is read off the matrix against its old Pay Band and Grade Pay.",
         why="This is the bridge: the old structure decides the new Level, and only then does pay get fixed. Grade Pay "
             "5400 in PB-2 maps to Level 9, the same Grade Pay in PB-3 maps to Level 10 — which is why the same figure "
             "in two different Pay Bands lands in two different Levels.",
         figures=["Level 9 (GP 5400, PB-2)", "Level 10 (GP 5400, PB-3)"],
         trap="Reading Grade Pay alone: 5400 appears in both PB-2 and PB-3 and maps to Levels 9 and 10.",
         hooks=["level of post", "mapping", "grade pay"]),

    dict(no="5", title="Drawal of pay in the revised pay structure",
         chapter="III",
         text="Save as otherwise provided in these rules, a Government servant shall draw pay in the Level in the revised pay "
              "structure applicable to the post to which he is appointed: Provided that a Government servant may elect to "
              "continue to draw pay in the existing pay structure until the date on which he earns his next or any subsequent "
              "increment in the existing pay structure or until he vacates his post or ceases to draw pay in the existing pay "
              "structure: Provided further that where a Government servant has been placed in a higher grade pay or scale "
              "between 1st day of January, 2016 and the date of notification of these rules on account of promotion or "
              "upgradation, he may elect to switch over to the revised pay structure from the date of such promotion or "
              "upgradation. Explanation 1.— The option to retain the existing pay structure shall be admissible only in respect "
              "of one existing Pay Band and Grade Pay or scale. Explanation 2.— The option shall not be admissible to any person "
              "appointed to a post for the first time in Government service or by transfer from another post on or after the "
              "1st day of January, 2016, and he shall be allowed pay only in the revised pay structure.",
         bare="Revised structure is the default. An existing servant may elect to stay on the old structure until he earns "
              "his next increment there, or until he vacates the post — but the option covers only one Pay Band and Grade Pay, "
              "and nobody appointed on or after 01.01.2016 has it at all.",
         why="Three separate limits live in this one rule and examiners test them separately: the option runs only to the "
             "next increment in the old structure; it is available for one scale only; and it is unavailable to anyone "
             "appointed on or after 01.01.2016, including by transfer.",
         figures=["one Pay Band and Grade Pay", "01.01.2016 cut-off"],
         trap="Giving the option to a direct recruit appointed in February 2016.",
         hooks=["option", "existing pay structure", "drawal"]),

    dict(no="6", title="Exercise of option",
         chapter="III",
         text="(1) The option under the provisos to rule 5 shall be exercised in writing in the form appended to these rules so "
              "as to reach the authority mentioned in sub-rule (2) within three months of the date of notification of these "
              "rules or where any revision in the existing pay structure is made by any order subsequent to the date of "
              "notification, within three months of the date of such order: Provided that (i) in the case of a Government "
              "servant who is out of India on leave or deputation or foreign service or active service, the option shall be "
              "exercised within three months of the date of his taking charge of his post in India, and (ii) where a Government "
              "servant is under suspension on the 1st day of January, 2016, the option may be exercised within three months of "
              "his return to duty if that date is later. (2) The option shall be intimated to the Head of his Office along with "
              "an undertaking in the form appended. (3) If the intimation is not received within the time specified, the "
              "Government servant shall be deemed to have elected to be governed by the revised pay structure with effect from "
              "the 1st day of January, 2016. (4) The option once exercised shall be final.",
         bare="Three months, in writing, to the Head of Office, with an undertaking. Out of India or under suspension, three "
              "months from taking charge in India or from return to duty. No intimation means deemed election of the revised "
              "structure from 01.01.2016. The option once exercised is final.",
         why="The deemed-election rule is the sharp edge: silence is not a neutral act. A servant who lets the three months "
             "pass is taken to have chosen the revised structure from 1 January 2016, whether or not that was better for him. "
             "Notes 1 to 3 extend the facility to those discharged, those who died, and those on leave with leave salary.",
         figures=["three months", "01.01.2016"],
         trap="Reading silence as leaving the choice open.",
         hooks=["option form", "three months", "deemed election", "final"]),

    dict(no="7", title="Fixation of pay in the revised pay structure",
         chapter="III",
         text="(1)(A) In the case of all employees— (i) the pay in the applicable Level in the Pay Matrix shall be the pay "
              "obtained by multiplying the existing basic pay by a factor of 2.57, rounded off to the nearest rupee, and the "
              "figure so arrived at will be located in that Level in the Pay Matrix and if such an identical figure corresponds "
              "to any Cell in the applicable Level, the same shall be the pay, and if no such Cell is available, the pay shall "
              "be fixed at the immediate next higher Cell; (ii) if the minimum pay or the first Cell in the applicable Level is "
              "more than the amount arrived at under sub-clause (i), the pay shall be fixed at the minimum pay or the first "
              "Cell of that applicable Level. (B) medical officers with NPA: existing basic pay multiplied by 2.57 plus DA on "
              "the pre-revised NPA admissible as on 1.1.2006, then located in the Level. (2) Where a post has been upgraded as "
              "indicated in Part B or Part C of the Schedule, the existing basic pay is arrived at by adding the pay in the "
              "existing Pay Band plus the Grade Pay corresponding to the Level to which the post has been upgraded. (7) Where "
              "the existing emoluments exceed the revised emoluments, the difference shall be allowed as personal pay to be "
              "absorbed in future increases in pay. (8) Where a senior's pay gets fixed in a Cell lower than that of a junior "
              "in the same cadre, his pay shall be stepped up to the same Cell as that of the junior.",
         bare="Basic pay × 2.57, rounded to the rupee, then placed at the equal or next higher cell of the Level. If the "
              "first cell is higher, the first cell is the pay. Excess of old emoluments over new becomes personal pay. "
              "Senior-junior anomalies are stepped up.",
         why="Two operations in sequence, and candidates collapse them: the multiplication is rounded to the nearest RUPEE, "
             "and only then is the cell chosen — and the cell is always equal or HIGHER, never lower. So the servant never "
             "loses by the cell landing, and if the landing cell is above his product he gains the difference.",
         figures=["2.57", "nearest rupee", "equal or next higher cell"],
         trap="Rounding the product to the nearest 100 instead of the nearest rupee before locating the cell.",
         hooks=["fixation", "2.57", "fitment", "personal pay", "stepping up"]),

    dict(no="8", title="Fixation of pay of direct recruits appointed on or after 01.01.2016",
         chapter="III",
         text="The pay of employees appointed by direct recruitment on or after 1st day of January, 2016 shall be fixed at the "
              "minimum pay or the first Cell in the Level applicable to the post to which such employees are appointed: "
              "Provided that where the existing pay of such employee appointed on or after 1st day of January, 2016 and before "
              "the date of notification of these rules has already been fixed in the existing pay structure and if his existing "
              "emoluments happen to exceed the minimum pay or the first Cell in the Level, such difference shall be paid as "
              "personal pay to be absorbed in future increments in pay.",
         bare="A direct recruit on or after 01.01.2016 starts at the first cell of his Level — no multiplication, no "
              "negotiation. If he was appointed before the notification and his old emoluments were higher, the excess is "
              "personal pay.",
         why="The first cell is not a floor that can be exceeded; it is the fixed starting point. The only addition "
             "permitted is personal pay for those appointed in the window between 01.01.2016 and 25.07.2016 whose old "
             "emoluments were higher, and that personal pay is absorbed by future increments.",
         figures=["first Cell", "01.01.2016"],
         trap="Applying the 2.57 fitment to a direct recruit appointed in 2016.",
         hooks=["direct recruit", "minimum pay", "first cell", "personal pay"]),

    dict(no="9", title="Increments in Pay Matrix",
         chapter="IV",
         text="The increment shall be as specified in the vertical Cells of the applicable Level in the Pay Matrix.",
         bare="An increment is one cell down the same Level. It is a step in the matrix, not a percentage worked out on the day.",
         why="The gazette illustration is the whole rule: 32300 in Level 4 becomes 33300. Because the cells already carry "
             "the 3%, the increment is not recomputed — the officer simply moves to the next printed figure. At the top of "
             "a Level there is no further cell, so the pay stays where it is.",
         figures=["one vertical cell"],
         trap="Computing 3% of the current pay instead of reading the next cell, which differs by a rounded amount.",
         hooks=["increment", "vertical cell"]),

    dict(no="10", title="Date of next increment in revised pay structure",
         chapter="IV",
         text="(1) There shall be two dates for grant of increment namely, 1st January and 1st July of every year, instead of the "
              "existing date of 1st July: Provided that an employee shall be entitled to only one annual increment either on 1st "
              "January or 1st July depending on the date of his appointment, promotion or grant of financial upgradation. "
              "(2) The increment in respect of an employee appointed or promoted or granted financial upgradation including "
              "upgradation under MACPS during the period between the 2nd day of January and 1st day of July (both inclusive) "
              "shall be granted on 1st day of January and the increment in respect of an employee appointed or promoted or "
              "granted financial upgradation during the period between the 2nd day of July and 1st day of January (both "
              "inclusive) shall be granted on 1st day of July.",
         bare="Two increment dates, 1 January and 1 July, and only one increment a year. The half-year in which you were "
              "appointed, promoted or given MACP decides which of the two dates is yours.",
         why="The mapping is counter-intuitive and is the single most examinable thing in the rule: appointment between "
             "2 January and 1 July gives the increment on the following 1 JANUARY; appointment between 2 July and 1 January "
             "gives it on the following 1 JULY. Both ranges are inclusive at both ends.",
         figures=["1 January", "1 July", "2 January", "2 July", "one increment a year"],
         trap="Awarding both dates in the year of appointment, or reversing the two half-years.",
         hooks=["increment date", "1 January", "1 July", "DNI"]),

    dict(no="11", title="Revision of pay from a date subsequent to 01.01.2016",
         chapter="III",
         text="Where a Government servant who continues to draw his pay in the existing pay structure is brought over to the "
              "revised pay structure from a date later than 1st day of January, 2016, his pay in the revised pay structure "
              "shall be fixed in the manner prescribed in accordance with clause (A) of sub-rule (1) of rule 7.",
         bare="A late switcher gets exactly the rule 7(1)(A) treatment, applied on the date he actually switches.",
         why="There is no special formula for a late switch: the same 2.57 multiplication and the same equal-or-next-higher "
             "cell. What changes is the date from which the revised pay runs — and therefore the arrears.",
         figures=["rule 7(1)(A)"],
         trap="Inventing a separate fitment for a servant who switches over in 2017.",
         hooks=["late option", "switch over"]),

    dict(no="12", title="Pay protection to officers on Central deputation under the Central Staffing Scheme",
         chapter="V",
         text="If the pay of the officers posted on deputation to the Central Government under the Central Staffing Scheme, "
              "after fixation in the revised pay structure either under these rules or as per the instructions regulating such "
              "fixation of pay on the post to which they are appointed on deputation, happens to be lower than the pay these "
              "officers would have been entitled to had they been in their parent cadre and would have drawn that pay but for "
              "the Central deputation, such difference in the pay shall be protected in the form of Personal Pay with effect "
              "from the date of notification of these rules.",
         bare="A Central Staffing Scheme deputationist whose revised deputation pay is lower than what his parent cadre would "
              "have paid him gets the difference as personal pay from 25.07.2016.",
         why="Only Central Staffing Scheme deputationists are covered, and the protection is Personal Pay — not a higher cell "
             "and not a notch. Personal pay is absorbable, which is why it disappears against future increments.",
         figures=["Personal Pay", "25.07.2016"],
         trap="Extending the protection to every officer on deputation.",
         hooks=["deputation", "personal pay", "CSS"]),

    dict(no="13", title="Fixation of pay on promotion on or after 01.01.2016",
         chapter="V",
         text="The fixation of pay in case of promotion from one Level to another in the revised pay structure shall be made "
              "in the following manner, namely:— (i) One increment shall be given in the Level from which the employee is "
              "promoted and he shall be placed at a Cell equal to the figure so arrived at in the Level of the post to which "
              "promoted and if no such Cell is available in the Level to which promoted, he shall be placed at the next higher "
              "Cell in that Level. (ii) In the case of Government servants receiving Non Practicing Allowance, their basic pay "
              "plus NPA shall not exceed the average of basic pay of the revised scale applicable to the Apex Level and the "
              "Level of the Cabinet Secretary.",
         bare="On promotion: one increment in the OLD Level first, then the equal or next higher cell in the NEW Level. "
              "No increment directly in the new Level.",
         why="The order is the whole point and it is where the marks are lost. Give the increment in the new Level and the "
             "officer lands on a different, usually lower, figure. The gazette illustration is exact: 28700 in Level 4 "
             "goes to 29600, and 29600 does not exist in Level 5, so he takes 30100.",
         figures=["one increment in the old Level", "equal or next higher cell"],
         trap="Giving the promotion increment in the new Level instead of the old one.",
         hooks=["promotion", "fixation", "MACP"]),

    dict(no="14", title="Mode of payment of arrears of pay",
         chapter="V",
         text="The arrears shall be paid during the Financial Year 2016-2017. Explanation.— 'arrears of pay' means the "
              "difference between (i) the aggregate of the pay and dearness allowance to which he is entitled on account of the "
              "revision effective from 1st January, 2016, and (ii) the aggregate of the pay and dearness allowance to which he "
              "would have been entitled for that period had his pay and allowances not been so revised.",
         bare="Arrears were to be paid in FY 2016-17, and are the difference between revised and unrevised pay plus DA.",
         why="The definition in the Explanation does the work: arrears are computed on pay AND dearness allowance together, "
             "not pay alone. A candidate who computes the difference on basic pay only will be out by the whole DA element.",
         figures=["FY 2016-2017"],
         trap="Computing arrears on basic pay alone and ignoring DA.",
         hooks=["arrears", "2016-17", "DA"]),

    dict(no="15", title="Overriding effect of rules",
         chapter="VI",
         text="The provisions of the Fundamental Rules, the Central Civil Services (Revision of Pay) Rules, 1947, the Central "
              "Civil Services (Revised Pay) Rules, 1960, 1973, 1986, 1997 and 2008 shall not, save as otherwise provided in "
              "these rules, apply to cases where pay is regulated under these rules, to the extent they are inconsistent with "
              "these rules.",
         bare="These rules override the Fundamental Rules and every earlier Revised Pay Rules to the extent of inconsistency.",
         why="Note the qualification: overriding only to the extent of inconsistency. The Fundamental Rules are not repealed; "
             "FR 22 and FR 35 continue to operate where the 2016 rules are silent, which is why promotion fixation under "
             "FR 22(I)(a)(1) still supplies the option.",
         figures=["FR", "1947", "1960", "1973", "1986", "1997", "2008"],
         trap="Treating the Fundamental Rules as repealed altogether.",
         hooks=["overriding", "FR", "inconsistency"]),

    dict(no="16", title="Power to relax",
         chapter="VI",
         text="Where the President is satisfied that the operation of all or any of the provisions of these rules causes undue "
              "hardship in any particular case, he may, by order, dispense with or relax the requirements of that rule to such "
              "extent and subject to such conditions as he may consider necessary for dealing with the case in a just and "
              "equitable manner.",
         bare="The President may relax any rule to relieve undue hardship.",
         why="The power is the President's alone and is triggered by undue hardship. It is not a general dispensing power for "
             "departments and cannot be exercised by a Head of Department.",
         figures=["President"],
         trap="Reading the relaxation power as available to any sanctioning authority.",
         hooks=["relaxation", "President", "hardship"]),

    dict(no="17", title="Interpretation",
         chapter="VI",
         text="If any question arises relating to the interpretation of any of the provisions of these rules, it shall be "
              "referred to the Central Government for decision.",
         bare="Questions of interpretation go to the Central Government.",
         why="The referral is to the Central Government, not to the President and not to the Department of Expenditure "
             "alone. Paired with rule 16 in questions about who decides what.",
         figures=["Central Government"],
         trap="Sending an interpretation question to the President.",
         hooks=["interpretation", "Central Government"]),
]

# The statutory text is held in verbatim.py, one string per rule, transcribed from the
# gazette. Anything in this file's `text` field is a placeholder; the real text wins.
for _r in RULES:
    if _r["no"] in VERBATIM:
        _r["text"] = VERBATIM[_r["no"]]
    _r["verbatim"] = _r["no"] in VERBATIM

CHAPTERS = [
    ("I", "Preliminary and definitions", "Rules 1 and 3"),
    ("II", "Scope and Levels", "Rules 2 and 4"),
    ("III", "Option and fixation", "Rules 5 to 8 and 11"),
    ("IV", "Increments", "Rules 9 and 10"),
    ("V", "Promotion, deputation and arrears", "Rules 12 to 14"),
    ("VI", "Overriding, relaxation and interpretation", "Rules 15 to 17"),
]

AMENDMENTS = [
    dict(no="1", instrument="Department of Expenditure Resolution, Gazette notification",
         date="16.05.2017",
         effect="Index of rationalisation of Level 13 raised from 2.57 to 2.67, and the whole Level 13 column re-cast. "
                "The first cell moves from ₹1,18,500 to ₹1,23,100 and the twentieth from ₹2,07,900 to ₹2,15,900. "
                "Every other Level is untouched.",
         figures=["2.57 → 2.67", "118500 → 123100"],
         why="This is the finest point in the whole Schedule. A question that quotes the notified Schedule will say 118500; "
             "a question about the position today must say 123100. The difference of ₹4,600 at the first cell is the mark."),
    dict(no="2", instrument="Rule 10 — increment dates",
         date="25.07.2016",
         effect="Two increment dates, 1 January and 1 July, introduced in place of the single 1 July date, with one "
                "increment only in a year.",
         figures=["01.01", "01.07"],
         why="Creates the half-year mapping in rule 10(2), which is the most examined mechanical point in the Rules."),
]
