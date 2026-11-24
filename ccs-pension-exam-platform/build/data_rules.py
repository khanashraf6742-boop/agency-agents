#!/usr/bin/env python3
"""data_rules.py — questions on the text of the CCS (Pension) Rules, 2021.

Every item is answerable from the verbatim text in pension_rules.py, and the
source line names the rule. No item asks about a rule that is not transcribed.
"""
from __future__ import annotations

FACTS = []


def Q(fid, ch, rule, rules_text, topic, stem, ans, d1, d2, d3, why, safe, src, trap,
      kind="RULE", tag="Tough"):
    FACTS.append(dict(id=fid, ch=ch, rule=rule, rules_text=rules_text, topic=topic,
                      q=stem, a=ans, d=[d1, d2, d3], why=why, safe=safe, src=src,
                      trap=trap, kind=kind, tag=tag))


# ------------------------------------------------------------------ Chapter I
Q("PEN-001", "I", "1", "Rule 1", "Commencement",
  "The CCS (Pension) Rules, 2021 came into force:",
  "From the date of their publication in the Official Gazette",
  ("From 1 January 2021, the start of the year",
   "The rules do not adopt a calendar date; they adopt the date of publication."),
  ("From 1 April 2016, retrospectively",
   "There is no retrospective commencement in rule 1(2)."),
  ("From the date the National Pension System Rules came into force",
   "The two instruments are separate; rule 1(2) fixes this one's own date."),
  "Rule 1(2) brings the rules into force with effect from the date of their publication in the Official Gazette. "
  "They were notified by G.S.R. 868(E) dated 20 December 2021, so that is the commencement date. Notice the "
  "contrast with the 2016 Pay Rules, which were given retrospective effect from 1 January 2016: the pension rules "
  "have no such deeming provision, and a question that offers 1 January 2021 is trading on the wrong instrument.",
  "Commencement: date of publication in the Gazette, 20.12.2021.",
  "Rule 1(2), CCS (Pension) Rules, 2021", "Assuming a retrospective date as in the 2016 Pay Rules")

Q("PEN-002", "I", "2", "Rule 2", "Application — the cut-off",
  "The 2021 Rules apply to Government servants appointed:",
  "On or before 31 December 2003, on a pensionable establishment",
  ("On or after 1 January 2004, because the rules are new",
   "That is the class the rules do NOT cover; post-2003 entrants are under the NPS Rules."),
  ("On any date, whatever the date of appointment",
   "The cut-off date is central to rule 2, not incidental to it."),
  ("On or before 31 December 2003, in any establishment including a contributory one",
   "Rule 2 expressly excludes persons entitled to a Contributory Provident Fund."),
  "Rule 2 applies the rules to servants appointed on or before 31 December 2003, appointed substantively to civil "
  "services and posts borne on pensionable establishments. The cut-off is the whole architecture of the 2021 Rules: "
  "the same notification period also produced the CCS (Implementation of National Pension System) Rules, 2021, which "
  "govern those appointed after that date unless they fall in one of the Explanation cases.",
  "Cut-off: 31.12.2003, and the establishment must be pensionable.",
  "Rule 2, CCS (Pension) Rules, 2021", "Reading the 2021 date in the title as the cut-off")

Q("PEN-003", "I", "2", "Rule 2 — Explanation (1)", "Induction training",
  "A servant was put on induction training in 2003 and appointed on a regular basis in 2004. Rule 2's Explanation:",
  "Covers him if the training was essential for the regular appointment and the training period counted as qualifying service",
  ("Excludes him, because the regular appointment was after the cut-off",
   "The Explanation exists precisely to bring this case in."),
  ("Covers him whatever the terms of the training",
   "Three conditions attach, and all three must be met."),
  ("Excludes him unless he was paid a regular salary during training",
   "A salary or a stipend suffices; a regular salary is not required."),
  "Explanation (1) to rule 2 brings in a servant put on induction training on or before 31 December 2003 followed "
  "by regular appointment after that date, on three conditions: completion of the training was an essential "
  "condition for the regular appointment; he was eligible for a salary or a stipend during it; and the training "
  "period was eligible to count as qualifying service under the 1972 Rules. Miss any one and the Explanation does "
  "not reach him.",
  "Induction training: three cumulative conditions, all in Explanation (1).",
  "Rule 2, Explanation (1), CCS (Pension) Rules, 2021", "Taking induction training as an automatic inclusion")

Q("PEN-004", "I", "3", "Rule 3(1)(o)", "Gratuity — three kinds",
  "The definition of 'gratuity' in rule 3(1)(o) includes:",
  "Service gratuity, retirement or death gratuity, and residuary gratuity",
  ("Only retirement gratuity",
   "The definition is wider, and it names three instruments."),
  ("Only service gratuity and retirement gratuity",
   "Residuary gratuity under rule 45(3) is also inside the definition."),
  ("Retirement gratuity and commuted value of pension",
   "Commutation is pension, not gratuity."),
  "Rule 3(1)(o) defines gratuity to include service gratuity under rule 44, retirement or death gratuity under rule "
  "45(1), and residuary gratuity under rule 45(3). The three are different instruments with different triggers: "
  "service gratuity replaces pension where qualifying service falls short; retirement and death gratuity are the "
  "lump sum on retirement or death; residuary gratuity fills up a shortfall where a pensioner dies within five "
  "years of retiring.",
  "Three gratuities: service (r.44), retirement/death (r.45(1)), residuary (r.45(3)).",
  "Rule 3(1)(o), CCS (Pension) Rules, 2021", "Treating 'gratuity' as a single instrument")

Q("PEN-005", "I", "4", "Rule 4(1)", "Permanent transfer — the option",
  "A servant permanently transferred from a post not governed by these rules may elect to remain under his old "
  "pension rules. The option must be exercised:",
  "Within six months of the order of permanent transfer, or of return from leave if on leave",
  ("Within three months of the transfer order, in every case",
   "Three months is the voluntary-retirement notice period, not this option."),
  ("At any time before retirement",
   "The option is time-bound, and the period runs from the transfer."),
  ("Within one year of the transfer order",
   "The figure is six months, extended only for a servant on leave."),
  "The proviso to rule 4(1) gives six months from the date of issue of the order of permanent transfer, or, if the "
  "servant is on leave on that date, six months from his return from leave, whichever is later. Rule 4(2) requires "
  "the option in writing to the authority making the transfer order, and rule 4(3) makes it final. Three separate "
  "sub-rules, three separate testable facts.",
  "Option: six months, in writing, and final.",
  "Rule 4, CCS (Pension) Rules, 2021", "Running the six months from the date of joining rather than the order")

Q("PEN-006", "II", "5", "Rule 5(1)", "Which rules govern the claim",
  "A servant's claim to pension is governed by:",
  "The rules in force when he retires, is retired, discharged, resigns or dies",
  ("The rules in force when he was appointed",
   "Pension is governed by the rules at the exit, not the entry."),
  ("The rules in force on the date he applies for pension",
   "The claim is judged at the event, not at the application."),
  ("Whichever set of rules is more beneficial to him",
   "Rule 5(1) fixes a single date; it offers no comparison."),
  "Rule 5(1) is a choice-of-law provision: the claim is regulated by the provisions in force at the time the "
  "servant retires, is retired, is discharged, is allowed to resign, or dies. That is why the 1972 Rules still "
  "govern servants who retired before 20 December 2021, and why the 2021 Rules reach a retirement that happens "
  "after that date even where the service was rendered under the older rules.",
  "Claim governed by the rules at the exit event.",
  "Rule 5(1), CCS (Pension) Rules, 2021", "Applying the rules in force at appointment")

Q("PEN-007", "II", "5", "Rule 5(2)", "The last day",
  "The day on which a servant retires, and the date of his death, are treated as:",
  "A completed working day — the last completed working day in the case of retirement",
  ("A day outside service, so no pay or qualifying service accrues",
   "Rule 5(2) does the opposite: it makes the day count."),
  ("A day of leave in every case",
   "Leave is the position only where he was in fact on leave immediately before."),
  ("A half day, for pension arithmetic",
   "The rule treats the day as completed, not as a fraction."),
  "Rule 5(2) treats the day of retirement or discharge as the last completed working day and the date of death as a "
  "completed working day. The proviso deals with the case where the servant was, immediately before, on leave or "
  "under suspension: then the day of retirement or death is part of that leave, absence or suspension. The point "
  "matters because a day more or less can move the ten-month average under rule 32.",
  "Day of retirement or death counts as a completed day.",
  "Rule 5(2), CCS (Pension) Rules, 2021", "Excluding the day of retirement from service")

Q("PEN-008", "II", "6", "Rule 6(1)", "Two pensions",
  "Under rule 6(1), a Government servant:",
  "Shall not earn two pensions in the same service or post at the same time or by the same continuous service",
  ("May earn two pensions if the second is for a different post",
   "The bar is on two pensions in the same service or post at the same time, not on two posts generally."),
  ("May always draw a second pension after re-employment",
   "Re-employment is dealt with in rule 6(2) and is also barred, subject to rules 19 and 20."),
  ("Shall not earn two pensions even for wholly separate services",
   "The bar is confined to the same service or post and the same continuous service."),
  "Rule 6(1) bars two pensions in the same service or post at the same time or by the same continuous service. "
  "Rule 6(2) then bars a separate pension or gratuity for a period of re-employment, except as provided in rule 19 "
  "or rule 20. The two sub-rules are often confused: (1) is about double-counting one service, (2) is about a "
  "pensioner who returns to Government service.",
  "No two pensions for the same service or post at the same time.",
  "Rule 6(1), CCS (Pension) Rules, 2021", "Reading rule 6(1) as a bar on all second pensions")

Q("PEN-009", "II", "7", "Rule 7(1)(b)", "Withholding — the floor",
  "Where a part of pension is withheld under rule 7(1)(b), the pension shall not be reduced below:",
  "The amount of minimum pension under rule 44",
  ("Fifty per cent of the pension originally sanctioned",
   "The proviso fixes a floor by reference to rule 44, not a percentage."),
  ("The amount of family pension admissible",
   "Family pension is a different instrument under rule 50."),
  ("There is no floor; the whole pension may be withheld",
   "The whole may be withheld, but a part may not be reduced below the floor."),
  "Rule 7(1)(b) allows the Appointing Authority to withhold or withdraw a pension, or part of it, permanently or "
  "for a specified period, where the pensioner is convicted of a serious crime or found guilty of grave misconduct. "
  "The proviso puts a floor under a partial withholding: the amount shall not be reduced below the minimum pension "
  "under rule 44. Withholding in full is a different power and is not touched by the proviso.",
  "Partial withholding: never below the rule 44 minimum.",
  "Rule 7(1)(b) and its proviso, CCS (Pension) Rules, 2021", "Applying the floor to a full withholding")

Q("PEN-010", "II", "7", "Rule 7(4)(b)", "Publication by an intelligence officer",
  "A retired servant of an Intelligence organisation in the Second Schedule to the RTI Act publishes material on "
  "his work without clearance. The undertaking he gave was in:",
  "Format 1",
  ("Form 1",
   "Form 1 is the application for commercial employment under rule 9; the undertaking is a Format."),
  ("Format 2",
   "Format 2 is the President's sanction to institute proceedings after retirement."),
  ("Form 3",
   "Form 3 is the nomination for gratuity."),
  "The rulebook appends two separate series and rule 3 defines them separately: a Form is a form appended to the "
  "rules, and a Format is a format appended to them. Rule 7(4)(b) requires the undertaking to be given in Format 1, "
  "and a failure to observe it is treated as grave misconduct under rule 7. The distinction is worth learning as a "
  "pair, because the paper tests it by offering a Form where a Format is required.",
  "Publication undertaking: Format 1, not Form 1.",
  "Rules 3(1)(k), 3(1)(l) and 7(4)(b), CCS (Pension) Rules, 2021", "Confusing the Form series with the Format series")

Q("PEN-011", "II", "8", "Rule 8(2)(c)", "Proceedings after retirement",
  "Departmental proceedings not instituted while the servant was in service:",
  "May be instituted only with the sanction of the President, in Format 2",
  ("May be instituted by any authority that could have done so in service",
   "The sanction of the President is a pre-condition, in Format 2."),
  ("May be instituted for any event, however old",
   "Clause (ii) bars an event more than four years before the institution."),
  ("May never be instituted after retirement",
   "They may, on the conditions in rule 8(2)(c), which is why the sub-rule exists."),
  "Rule 8(2)(c) sets three limits on proceedings not instituted in service: they shall not be instituted save with "
  "the sanction of the President in Format 2; they shall not concern an event more than four years before the "
  "institution; and they shall be conducted by such authority and place as the President directs. The proviso adds "
  "that a memorandum of charges must be communicated to the pensioner in Format 3.",
  "Post-retirement proceedings: President's sanction, four-year bar, Formats 2 and 3.",
  "Rule 8(2)(c), CCS (Pension) Rules, 2021", "Ignoring the four-year bar on the event")

Q("PEN-012", "II", "8", "Rule 8(4)(a)", "Provisional pension — the amount",
  "Where proceedings are pending, the provisional pension under rule 8(4)(a) is equal to:",
  "The maximum pension that would have been admissible on the qualifying service up to retirement",
  ("Two-thirds of the pension that would have been admissible",
   "Two-thirds is the compulsory-retirement provisional figure under rule 40(3)."),
  ("The minimum pension under rule 44",
   "The minimum is a floor elsewhere; here the amount is the maximum pension."),
  ("Fifty per cent of the pension, pending conclusion",
   "There is no such fraction in rule 8(4)."),
  "Rule 8(4)(a) authorises a provisional pension equal to the maximum pension that would have been admissible on "
  "the qualifying service up to the date of retirement \u2014 or, if the servant was under suspension on that "
  "date, up to the day before he was placed under suspension. This is the proceedings case, and it is deliberately "
  "generous because no gratuity is paid at all under rule 8(4)(c) until the proceedings conclude.",
  "Proceedings case: maximum admissible pension, and no gratuity.",
  "Rule 8(4), CCS (Pension) Rules, 2021", "Confusing rule 8(4) with the rule 62 delay case")

Q("PEN-013", "II", "8", "Rule 8(6)", "Recovery from pension",
  "Where the President orders recovery of pecuniary loss from pension, the recovery shall not ordinarily exceed:",
  "One-third of the pension admissible on the date of retirement",
  ("One-half of the pension admissible on the date of retirement",
   "The rule says one-third."),
  ("The whole pension, since it is a recovery of loss",
   "The rule caps the rate, which is the point of sub-rule (6)."),
  ("Ten per cent of the pension",
   "Ten per cent is the gratuity withholding in the rule 62 delay case."),
  "Rule 8(6) puts a rate cap on a recovery of pecuniary loss where the President decides not to withhold or "
  "withdraw the pension: the recovery shall not ordinarily be made at a rate exceeding one-third of the pension "
  "admissible on the date of retirement. The word 'ordinarily' leaves room for an exceptional case, but the "
  "starting rule is one-third.",
  "Recovery cap: one-third of the pension at retirement.",
  "Rule 8(6), CCS (Pension) Rules, 2021", "Confusing the one-third recovery with the ten per cent withholding")

Q("PEN-014", "II", "9", "Rule 9(1)", "Commercial employment",
  "A Group 'A' pensioner wishing to take up commercial employment must obtain sanction if he does so:",
  "Within one year of his retirement",
  ("Within two years of his retirement",
   "The period in rule 9(1) is one year."),
  ("At any time after retirement",
   "The rule is confined to the first year; after that no sanction is required."),
  ("Within six months of his retirement",
   "Six months is the rule 4 option period."),
  "Rule 9(1) requires a pensioner who was a member of Central Service Group 'A' immediately before retirement to "
  "obtain the previous sanction of the Government before accepting commercial employment within one year of "
  "retirement, applying in Form 1. Rule 9(8) supplies the sanction for breach: the Government may declare that he "
  "is not entitled to the whole or part of his pension for such period as the order specifies.",
  "Commercial employment: one year, sanction in Form 1.",
  "Rule 9(1), CCS (Pension) Rules, 2021", "Treating the bar as permanent")

Q("PEN-015", "II", "10", "Rule 10(1)", "Employment under a foreign Government",
  "A Group 'A' pensioner accepting employment under a Government outside India without permission:",
  "Forfeits pension for the period of that employment, or such longer period as the Government directs",
  ("Forfeits his pension permanently in every case",
   "The rule ties the loss to the period of employment, extendable by direction."),
  ("Suffers no consequence, because the pension is already sanctioned",
   "Rule 10(1) attaches a consequence, and it is a period-based loss."),
  ("Must refund his entire gratuity",
   "The rule speaks of pension for the period, not of refunding gratuity."),
  "Rule 10(1) requires previous permission of the Central Government for employment under any Government outside "
  "India, and provides that no pension is payable in respect of any period for which he is so employed, or such "
  "longer period as the Government may direct. Read it against rule 9: rule 9 is commercial employment anywhere and "
  "carries a declaration power over pension; rule 10 is employment under a foreign Government and carries a "
  "period-based forfeiture.",
  "Foreign Government employment: pension lost for the period.",
  "Rule 10(1), CCS (Pension) Rules, 2021", "Confusing the foreign-employment bar with the commercial-employment bar")
