#!/usr/bin/env python3
"""data_statute3.py — statutory questions, Chapters X to XIV."""
from __future__ import annotations

FACTS = []


def Q(fid, ch, rule, rules_text, topic, stem, ans, d1, d2, d3, why, safe, src, trap,
      kind="RULE", tag="Tough"):
    FACTS.append(dict(id=fid, ch=ch, rule=rule, rules_text=rules_text, topic=topic,
                      q=stem, a=ans, d=[d1, d2, d3], why=why, safe=safe, src=src,
                      trap=trap, kind=kind, tag=tag))


Q("PS-031", "X", "54", "Rule 54(1)", "Retirement list",
  "Every Head of Department must prepare a list of servants due to retire within the next fifteen months:",
  "by the 15th day of every month",
  ("by the last day of every month", "The last day is when a copy goes to the Accounts Officer under rule 54(2)."),
  ("once a year, in January", "The list is monthly."),
  ("by the 1st day of every month", "The rule fixes the fifteenth."),
  "Rule 54(1) requires every Head of Department to have a list prepared by the 15th day of every month of all "
  "Government servants due to retire within the next fifteen months of that date. Rule 54(2) requires a copy to the "
  "Accounts Officer before the last day of every month. Rule 54(3) deals with other retirements: the Head of Office "
  "must inform the Accounts Officer within ten days of the order.",
  "List by the 15th; copy to Accounts Officer by the month's last day.",
  "Rule 54, CCS (Pension) Rules, 2021", "Swapping the fifteenth and the last day of the month")

Q("PS-032", "X", "56", "Rule 56", "Start of preparatory work",
  "Preparatory work for processing a pension case begins:",
  "one year before retirement, or on proceeding on leave preparatory to retirement, whichever is earlier",
  ("six months before retirement, when Form 4 and Form 6 fall due",
   "The six-month point is the deadline for those forms under rule 57(2)(a), not the start of preparation."),
  ("eight months before retirement, when the third stage begins",
   "Eight months is a deadline within the year, not its start."),
  ("on the date of the retirement order", "That is the rule 58 trigger for other retirements."),
  "Rule 56 requires every Head of Office to undertake the preparatory work one year before the date of superannuation "
  "retirement, or on the date the servant proceeds on leave preparatory to retirement, whichever is earlier. Rule 57 "
  "divides that year into three stages, with verification of service complete eight months before superannuation and "
  "the third stage beginning no later than eight months before retirement.",
  "One year out, or on leave preparatory to retirement, whichever is earlier.",
  "Rule 56 and rule 57(1), CCS (Pension) Rules, 2021", "Starting at the six-month or eight-month milestone")

Q("PS-033", "X", "57", "Rule 57(1)(a)(v)", "Unanswered verification reference",
  "A Head of Office refers a period of service to another office for verification and receives no response within the "
  "two months allowed. The period:",
  "is deemed to qualify for pension",
  ("is treated as non-qualifying", "The rule deems the opposite where no response comes."),
  ("is held in abeyance until the other office replies", "The deeming provision exists to prevent that delay."),
  ("must be verified from pay bills by the referring office",
   "That is the sub-clause (ii) route, not the consequence of silence."),
  "Rule 57(1)(a)(iv) gives the office receiving a verification reference two months to verify and reply, with a "
  "proviso requiring any period incapable of verification to be flagged at once. Sub-clause (v) then provides that "
  "if no response is received within that time, the period shall be deemed to qualify for pension. Sub-clause (vi) "
  "fixes responsibility on the Secretary of the Ministry where a non-qualifying period was not communicated.",
  "Silence for two months: the period is deemed to qualify.",
  "Rule 57(1)(a)(iv) to (vi), CCS (Pension) Rules, 2021", "Treating silence as exclusion")

Q("PS-034", "X", "57", "Rule 57(1)(b)(v)", "Verification of emoluments",
  "For calculating emoluments and average emoluments, the Head of Office verifies correctness of emoluments:",
  "only for the twenty-four months preceding retirement, and no earlier period",
  ("for the last ten months only", "Ten months is the averaging window; the verification window is twenty-four."),
  ("for the whole of the last five years", "The rule expressly stops at twenty-four months."),
  ("for the entire service", "The rule expressly confines verification to twenty-four months."),
  "Rule 57(1)(b)(iv) requires the Head of Office to verify from the service book the correctness of the emoluments "
  "drawn or to be drawn during the last ten months of service. Sub-clause (v) then limits that exercise: to ensure "
  "those ten months are correctly shown, the Head of Office verifies correctness only for the twenty-four months "
  "preceding retirement, and not for any period before that date. Rule 63(1)(c) imposes the same limit on the "
  "Accounts Officer.",
  "Twenty-four months, not the ten-month averaging window.",
  "Rule 57(1)(b)(v) and rule 63(1)(c), CCS (Pension) Rules, 2021",
  "Equating the ten-month average with the verification window")

Q("PS-035", "X", "62", "Rule 62(3)(a)", "Provisional pension and gratuity",
  "Where provisional pension and gratuity are sanctioned under rule 62, the sanction authorises:",
  "100 per cent of pension, and 100 per cent of gratuity withholding ten per cent of the gratuity",
  ("two-thirds of pension, and the full gratuity",
   "Two-thirds is the rule 40 provisional figure for compulsory retirement."),
  ("100 per cent of pension, but no gratuity at all",
   "That is the position under rule 8 where proceedings are pending."),
  ("50 per cent of pension and 90 per cent of gratuity", "Neither figure appears in rule 62(3)."),
  "Rule 62(3)(a) requires the Head of Office to authorise, from the date following retirement, 100 per cent of "
  "pension as provisional pension and 100 per cent of the gratuity as provisional gratuity while withholding ten per "
  "cent of the gratuity. Rule 62(4) requires the sanction within ten days after retirement on superannuation, or "
  "within one month of the forms for other retirements, and rule 62(6)(a) caps provisional pension at six months.",
  "100 per cent of both, with ten per cent of gratuity withheld.",
  "Rule 62(3) to (6), CCS (Pension) Rules, 2021", "Importing the rule 40 two-thirds figure")

Q("PS-036", "X", "62", "Rule 62(7)", "Provisional becoming final",
  "The final pension and gratuity are not determined within six months of the provisional sanction. The Accounts "
  "Officer:",
  "shall treat the provisional pension and gratuity as final and issue the PPO on expiry of the six months",
  ("shall continue the provisional pension indefinitely",
   "Rule 62(7) converts it instead of extending it."),
  ("shall refer the case to the Department of Pension and Pensioners' Welfare",
   "No such reference is provided for in rule 62(7)."),
  ("shall recover the provisional pension paid",
   "The rule converts the provisional payment; it does not recover it."),
  "Rule 62(6)(a) caps provisional pension at six months from retirement or from submission of Form 4 and Form 6, "
  "whichever is later. Rule 62(7) then provides that where the final amounts have not been determined within that "
  "period, the Accounts Officer shall treat the provisional pension and gratuity as final and issue the pension "
  "payment order immediately on the expiry of the six months. Rule 62(8) then releases the withheld gratuity.",
  "Six months: provisional becomes final.",
  "Rule 62(6) to (8), CCS (Pension) Rules, 2021", "Reading the six months as extendable")

Q("PS-037", "X", "63", "Rule 63(1)(a) and (b)", "PPO timelines",
  "The Accounts Officer must issue the pension payment order for a superannuation retirement:",
  "not later than two months before the date of retirement",
  ("within forty five days of receiving the papers",
   "The forty-five-day limit applies to retirements other than on superannuation under clause (b)."),
  ("within one month of receiving the papers",
   "One month is the family pension timeline under rule 76(1), not this one."),
  ("on the date of retirement itself", "The rule requires issue in advance of that date."),
  "Rule 63(1)(a) requires the Accounts Officer, on receiving the pension case under rule 60, to apply the checks, "
  "record the enfacement in Part II of Form 7, assess pension, family pension and gratuity, and issue the pension "
  "payment order not later than two months before the date of superannuation retirement. Clause (b) gives forty-five "
  "days from receipt of the papers where the retirement is otherwise than on superannuation.",
  "Two months in advance for superannuation; forty-five days otherwise.",
  "Rule 63(1)(a) and (b), CCS (Pension) Rules, 2021", "Using the forty-five-day limit for a superannuation case")

Q("PS-038", "X", "65", "Rule 65(5)(a)", "Interest on delayed pension",
  "A servant retires on superannuation and his pension is paid late for administrative reasons. Interest runs from:",
  "the date following the expiry of three months from the date of retirement",
  ("the date following the expiry of one month from retirement", "The period is three months."),
  ("the date of retirement itself", "Interest begins only after the three-month grace period."),
  ("the date six months after retirement", "Six months is the missing-person waiting period, not the interest trigger."),
  "Rule 65(1) allows interest on arrears at the rate applicable to General Provident Fund amounts where delay is "
  "attributable to administrative reasons or lapses, unless the delay was the servant's own failure to comply with "
  "the procedure. Rule 65(5)(a) then fixes the start of the period for a superannuation retirement at the date "
  "following the expiry of three months from retirement, running to the date of payment.",
  "Interest: three months after retirement.",
  "Rule 65(1) and (5)(a), CCS (Pension) Rules, 2021", "Starting interest from the date of retirement")

Q("PS-039", "X", "66", "Rule 66(2) proviso", "Revision to the disadvantage of a pensioner",
  "A clerical error in a pension authorised two years and three months ago is detected. The pension may be revised "
  "to the pensioner's disadvantage:",
  "only with the concurrence of the Department of Pension and Pensioners' Welfare",
  ("on the Head of Office's own authority", "The proviso requires a higher concurrence after two years."),
  ("never, because more than two years have passed", "The rule permits revision with concurrence; it does not bar it."),
  ("only with the sanction of the Ministry of Finance",
   "The Ministry of Finance is consulted under rule 66(4) on waiver of recovery, not on the revision."),
  "Rule 66(2) protects a pension once authorised, permitting revision to the disadvantage of the pensioner only where "
  "a clerical error is subsequently detected. Its proviso adds that where the error is detected more than two years "
  "after authorisation or revision, no such revision may be ordered without the concurrence of the Department of "
  "Pension and Pensioners' Welfare. Rule 66(3) leaves the question whether an error is clerical to the "
  "administrative Ministry.",
  "After two years: DP&PW concurrence.",
  "Rule 66(2) and its proviso, CCS (Pension) Rules, 2021", "Treating the two-year point as an absolute bar")

Q("PS-040", "X", "67", "Rule 67(3)", "Recovery from gratuity",
  "Which of these may NOT be recovered from retirement gratuity?",
  "A personal loan taken by the servant from a cooperative society",
  ("Balance of a house building advance", "A house building advance is Government dues under clause (b)."),
  ("Arrears of income tax deductible at source", "Clause (b) names it expressly."),
  ("Arrears of licence fee for Government accommodation",
   "Clause (a) covers accommodation dues and related charges."),
  "Rule 67(2) adjusts against retirement gratuity the Government dues assessed by the Head of Office and outstanding "
  "at retirement. The Explanation defines Government dues as accommodation dues including licence fee arrears, "
  "damages, and electricity, water and PNG charges under clause (a), and under clause (b) the balance of house "
  "building, conveyance or other advances, overpayment of pay, allowances or leave salary, and arrears of income tax "
  "deductible at source. Rule 67(3) then forbids recovery of anything that is not Government dues in that sense.",
  "Only Government dues come out of gratuity.",
  "Rule 67(2) and (3), CCS (Pension) Rules, 2021", "Recovering a private debt from gratuity")

Q("PS-041", "X", "68", "Rule 68(7)(a)", "No Demand Certificate",
  "The Directorate of Estates must issue a No Demand Certificate after the accommodation is vacated:",
  "within fourteen days of the application",
  ("within one month of the application", "The period is fourteen days."),
  ("within two months of the application",
   "Two months is the period for the Directorate's reply under rule 68(1)(a)."),
  ("within seven days of the application", "Seven days is the rule 71(4)(c) period for a death intimation."),
  "Rule 68(7)(a) requires the Directorate of Estates to give the No Demand Certificate within fourteen days of the "
  "application made after actual vacation of the accommodation. Clause (b) entitles the allottee to interest at "
  "General Provident Fund rates on the excess withheld gratuity if the certificate is delayed beyond that, and clause "
  "(c) makes the Directorate of Estates pay it through the Accounts Officer.",
  "Fourteen days for the No Demand Certificate.",
  "Rule 68(7), CCS (Pension) Rules, 2021", "Using the two-month or one-month periods from rule 68(1)")

Q("PS-042", "X", "70", "Rule 70(2)", "Deemed retirement",
  "The office fails to issue the retirement notification on time. The servant:",
  "is deemed to have retired on attaining the age of superannuation, and is not entitled to continue",
  ("continues in service until the notification issues", "Rule 70(2) expressly denies that consequence."),
  ("is entitled to pay for the period of delay",
   "The rule does not create a right to pay for a failure to notify."),
  ("must apply afresh for pension", "Pension follows from the deemed retirement."),
  "Rule 70(1) requires a Gazette notification for a Gazetted servant, or an office order for a non-Gazetted servant, "
  "specifying the date of retirement within a week, with a copy to the Accounts Officer. Rule 70(2) then provides "
  "that unless specific extension orders issue, the servant is deemed to have retired on attaining the age of "
  "superannuation, and the office's failure to issue the notification does not entitle him to continue beyond that "
  "date.",
  "Deemed retirement on the superannuation date, notification or not.",
  "Rule 70, CCS (Pension) Rules, 2021", "Treating the notification as constitutive of retirement")

Q("PS-043", "XI", "71", "Rule 71(4)(a)", "Death of an allottee",
  "A Government servant dies while in occupation of Government accommodation. The licence fee outstanding for the "
  "period before his death:",
  "stands waived",
  ("is recovered from the death gratuity", "Only dues relating to damages are recovered from death gratuity."),
  ("is recovered from the family pension", "The rule waives the pre-death licence fee."),
  ("is recovered from the provident fund", "The rule provides no such recovery."),
  "Rule 71(4)(a) waives the dues pertaining to outstanding licence fee for the period before the date of death of a "
  "servant who was an allottee. Clause (b) keeps dues relating to damages recoverable from the death gratuity, and "
  "provides that if the family retains the accommodation, no licence fee is recovered for the month of death and the "
  "first three months after it. Clause (c) requires the Head of Office to write to the Directorate of Estates within "
  "seven days.",
  "Pre-death licence fee waived; damages still recoverable.",
  "Rule 71(4), CCS (Pension) Rules, 2021", "Recovering the waived licence fee from death gratuity")

Q("PS-044", "XI", "75", "Rule 75(1)", "Provisional family pension",
  "On death of a servant in service, provisional family pension must be drawn:",
  "within fifteen days of receipt of the claim",
  ("within one month of receipt of the claim",
   "One month is the rule 74(1) period for forwarding the case, and the rule 76(1) period for the Accounts Officer."),
  ("within seven days of receipt of the claim", "Seven days is the intimation period to the Directorate of Estates."),
  ("within forty five days of receipt of the claim",
   "Forty-five days is the invalid pension period under rule 39(8)."),
  "Rule 75(1) requires the Head of Office, once satisfied of the claimant's eligibility, to draw provisional family "
  "pension not exceeding the maximum admissible, within fifteen days of receipt of the claim, issuing a sanction "
  "letter and drawing the amount as establishment pay is drawn. Rule 75(3) continues it for six months from the day "
  "after death unless extended under rule 76.",
  "Provisional family pension: fifteen days.",
  "Rule 75(1) and (3), CCS (Pension) Rules, 2021", "Using the one-month case-forwarding period")

Q("PS-045", "XI", "74", "Rule 74(4)(c)", "Gratuity held over",
  "The maximum amount of gratuity that may be held over pending assessment of Government dues on a death case is:",
  "ten per cent of the amount of gratuity",
  ("twenty per cent of the amount of gratuity", "Twenty per cent is the rule 47(7) minor's-share figure."),
  ("one-third of the amount of gratuity", "One-third is the rule 8(6) recovery cap."),
  ("fifty per cent of the amount of gratuity", "No such figure appears in rule 74."),
  "Rule 74(4) requires the Head of Office to draw the Accounts Officer's attention to outstanding Government dues, "
  "including under clause (b) the amount of gratuity held over partly for adjustment of unassessed dues and partly "
  "as a margin, and clause (c) caps that held-over amount at ten per cent of the gratuity. Rule 76(5)(e) then "
  "provides for adjustment of the withheld amount against outstanding licence fee and refund of the balance.",
  "Held-over gratuity: ten per cent maximum.",
  "Rule 74(4) and rule 76(5)(e), CCS (Pension) Rules, 2021", "Confusing it with the one-third recovery cap")

Q("PS-046", "XII", "79", "Rule 79(2)(b)(i)", "Sanction of family pension on a pensioner's death",
  "A pensioner dies leaving a family member not named in the pension payment order. The Head of Office sanctions "
  "family pension:",
  "in Format 13, within one month of receipt of the claim in Form 10",
  ("in Format 12, within one month of the claim",
   "Format 12 is the letter inviting the claim, not the sanction."),
  ("in Form 13, within one month of the claim", "Form 13 is the residuary gratuity claim."),
  ("in Form 10, within three months of the claim", "Form 10 is the claim itself, and the period is one month."),
  "Rule 79(2)(b)(i) applies where the pension payment order names no family member, or where the person now entitled "
  "is someone else, including a person who joined the family after retirement. The Head of Office must, within one "
  "month of receiving a claim in Form 10, sanction the family pension in Format 13 in favour of the person entitled. "
  "Rule 80(1) then requires the Accounts Officer to authorise payment within one month of the sanction.",
  "Sanction: Format 13, on a Form 10 claim, within one month.",
  "Rule 79(2)(b)(i) and rule 80(1), CCS (Pension) Rules, 2021", "Answering Format 12 or Form 13")

Q("PS-047", "XII", "79", "Rule 79(6)", "Residuary gratuity claim",
  "A claim for residuary gratuity on the death of a retired servant is made in:",
  "Form 13",
  ("Form 12", "Form 12 is the family pension claim against a pensioner's PPO."),
  ("Form 9", "Form 9 is the death gratuity claim by a nominee or family member."),
  ("Format 13", "Format 13 is the Head of Office's sanction of family pension."),
  "Rule 79(6) provides that where a residuary gratuity becomes payable to the family of a deceased retired servant "
  "under rule 45(3), the Head of Office sanctions its payment on receipt of a claim in Form 13 from the person or "
  "persons eligible. Rule 45(3) grants the residuary gratuity where the sums received by the pensioner before death "
  "fall short of twelve times his emoluments within five years of retirement.",
  "Residuary gratuity: claim in Form 13.",
  "Rule 79(6) and rule 45(3), CCS (Pension) Rules, 2021", "Answering Format 13 for the claim")

Q("PS-048", "XIII", "81", "Rule 81(3)", "Pension for the day of death",
  "Pension, including family pension, is payable:",
  "for the day on which its recipient dies",
  ("up to the day before the recipient dies", "Rule 81(3) includes the day of death."),
  ("only up to the last working day of the month", "That is the payment convention in rule 83(2), not the accrual."),
  ("for the whole month in which the recipient dies", "The rule fixes the day of death, not the whole month."),
  "Rule 81(1) makes pension other than family pension payable from the date the servant ceases to be borne on the "
  "establishment. Rule 81(2) makes family pension payable from the day after the death or ineligibility, subject to "
  "rule 76(2)(d) and rule 79(3)(iv). Rule 81(3) then provides that pension, including family pension, is payable for "
  "the day on which its recipient dies.",
  "The day of death is a pension day.",
  "Rule 81, CCS (Pension) Rules, 2021", "Stopping pension on the day before death")

Q("PS-049", "XIII", "83", "Rule 83(2)", "Payment of monthly pension",
  "A monthly pension is payable:",
  "on or after the last working day of the month to which it relates, except March",
  ("on the first working day of every month without exception",
   "Only March is paid on or after the first working day of April."),
  ("on the last working day of every month without exception", "March is the exception."),
  ("in advance, on the first day of the month to which it relates",
   "Payment is on or after the last working day, not in advance."),
  "Rule 83(1) requires gratuity to be paid in lump sum. Rule 83(2) makes a pension fixed at monthly rates payable "
  "monthly on or after the last working day of the month to which it relates, except for the month of March, when it "
  "is payable on or after the first working day of April. Rule 82 confines all pensions and gratuities to rupees in "
  "India.",
  "Last working day, with March paid in April.",
  "Rules 82 and 83, CCS (Pension) Rules, 2021", "Forgetting the March exception")

Q("PS-050", "XIV", "85", "Rule 85", "Interpretation",
  "A doubt arises on the interpretation of the pension rules. It is referred to:",
  "the Government in the Department of Pension and Pensioners' Welfare or the Department of Personnel and Training, "
  "depending on the rule or subject",
  ("the Ministry of Finance (Department of Expenditure) in every case",
   "The Ministry of Finance is consulted on waiver of recovery under rule 66(4)."),
  ("the Comptroller and Auditor General", "The C&AG audits; it does not decide interpretation."),
  ("the Central Administrative Tribunal", "The Tribunal adjudicates disputes; it is not the interpretative authority."),
  "Rule 85 requires a doubt on the interpretation of the rules to be referred for decision to the Government in the "
  "Department of Pension and Pensioners' Welfare or the Department of Personnel and Training, depending on the rule "
  "or the subject on which a decision is required and the Department concerned with it. Rule 86 separately allows a "
  "Ministry to relax a rule causing undue hardship, with the concurrence of one of those two Departments.",
  "Interpretation: DP&PW or DoPT, by subject.",
  "Rules 85 and 86, CCS (Pension) Rules, 2021", "Sending every question to the Ministry of Finance")

Q("PS-051", "XIV", "86", "Rule 86 proviso", "Power to relax",
  "A Ministry wishes to relax a rule that is causing undue hardship. It may do so:",
  "by order recording reasons, with the concurrence of DP&PW or DoPT",
  ("on its own authority, recording reasons", "The proviso requires the concurrence of one of the two Departments."),
  ("only with the approval of the President", "The concurrence required is departmental, not presidential."),
  ("only through a fresh notification amending the rules", "Rule 86 is a relaxation power, not an amendment route."),
  "Rule 86 permits a Ministry or Department satisfied that a rule causes undue hardship to dispense with or relax it "
  "by order for reasons recorded in writing, to the extent and on the exceptions and conditions it considers just "
  "and equitable. The proviso forbids any such order except with the concurrence of the Department of Pension and "
  "Pensioners' Welfare or the Department of Personnel and Training, according to the rule or subject.",
  "Relaxation: reasoned order plus DP&PW or DoPT concurrence.",
  "Rule 86 and its proviso, CCS (Pension) Rules, 2021", "Relaxing a rule without concurrence")

Q("PS-052", "XIV", "87", "Rule 87(2)(c)", "Repeal and saving",
  "A pension case of a servant who retired before the 2021 Rules commenced is pending on commencement. It is decided:",
  "under the old rules, as if the 2021 Rules had not been made",
  ("under the 2021 Rules, because they are now in force", "Rule 87(2)(c) saves the old law for pending cases."),
  ("under whichever set of rules is more beneficial", "The saving is not a beneficial-choice provision."),
  ("by the Department of Pension and Pensioners' Welfare", "The saving prescribes the law, not a new authority."),
  "Rule 87(1) repeals the old rules, including the CCS (Pension) Rules, 1972, so far as they provide for matters now "
  "contained in the 2021 Rules. Rule 87(2) saves nominations, family particulars and pension applications made under "
  "the old rules, and requires pending cases of authorisation of pension under clause (c), and of gratuity and family "
  "pension under clause (d), to be disposed of under the old rules as if the new rules had not been made.",
  "Pending cases: the old rules still govern.",
  "Rule 87, CCS (Pension) Rules, 2021", "Applying the new rules to a case pending on commencement")

Q("PS-053", "XIV", "87", "Rule 87(2)(a)", "Saving of nominations",
  "A nomination for gratuity made under the 1972 Rules before commencement of the 2021 Rules:",
  "is deemed to have been made under the corresponding provisions of the 2021 Rules",
  ("lapses on commencement and must be re-made", "Rule 87(2)(a)(i) saves it rather than letting it lapse."),
  ("continues under the 1972 Rules indefinitely", "It is deemed to be made under the new rules."),
  ("must be re-executed in Form 3 within six months", "No re-execution period is imposed on a saved nomination."),
  "Rule 87(2)(a) treats every nomination for gratuity, every form giving family details for family pension, and every "
  "formal application for sanction of pension made under the old rules as made under the corresponding provisions of "
  "the 2021 Rules. Clause (b) deals with the opposite case, requiring a nomination or family form not yet made to be "
  "made under the new rules after commencement.",
  "Old nominations carry over as if made under the new rules.",
  "Rule 87(2)(a) and (b), CCS (Pension) Rules, 2021", "Treating saved nominations as lapsed")
