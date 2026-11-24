#!/usr/bin/env python3
"""data_statute.py — statutory questions, Chapters III to IX."""
from __future__ import annotations

FACTS = []


def Q(fid, ch, rule, rules_text, topic, stem, ans, d1, d2, d3, why, safe, src, trap,
      kind="RULE", tag="Tough"):
    FACTS.append(dict(id=fid, ch=ch, rule=rule, rules_text=rules_text, topic=topic,
                      q=stem, a=ans, d=[d1, d2, d3], why=why, safe=safe, src=src,
                      trap=trap, kind=kind, tag=tag))


Q("PS-001", "III", "11", "Rule 11", "Commencement of qualifying service",
  "Qualifying service commences from the date the Government servant:",
  "takes charge of the post to which he is first appointed, substantively or in an officiating or temporary capacity",
  ("completes the probation period attached to his first post",
   "Rule 16 separately provides that probation followed by confirmation qualifies."),
  ("attains the age of eighteen years, in every case",
   "Service before eighteen is excluded by the second proviso, with a military-service exception."),
  ("is confirmed in his first appointment",
   "Confirmation is dealt with at rule 16; commencement is at rule 11."),
  "Rule 11 fixes commencement at the date of taking charge of the post to which the servant is first appointed, "
  "whether substantively, in an officiating capacity or on a temporary basis. Two provisos qualify it: officiating "
  "or temporary service must be followed without interruption by substantive appointment, and service before the age "
  "of eighteen does not count except in the case of military service counted for civil pension under rule 20.",
  "Qualifying service begins on taking charge, not on confirmation.",
  "Rule 11, CCS (Pension) Rules, 2021", "Reading confirmation or probation into the commencement date")

Q("PS-002", "III", "17", "Rule 17", "Service as apprentice",
  "Service as an apprentice counts as qualifying service:",
  "only in the case of a Subordinate Accounts Service apprentice in the IA&AD or the Defence Accounts Department",
  ("in every case, because apprenticeship is a recognised form of service",
   "Rule 17 is a rule of exclusion, not inclusion."),
  ("never, under any circumstances",
   "There is an express exception for SAS apprentices in the two accounts departments."),
  ("only where the apprentice was subsequently confirmed",
   "The exception is by department and service, not by later confirmation."),
  "Rule 17 states the general rule first: service as an apprentice shall not qualify. It then carves out the "
  "Subordinate Accounts Service apprentice in the Indian Audit and Accounts Department or the Defence Accounts "
  "Department. The examinable point is the narrowness of the exception, which sits alongside rule 16, where service "
  "on probation followed by confirmation does qualify.",
  "Apprenticeship: excluded, except SAS apprentices in IA&AD and Defence Accounts.",
  "Rules 16 and 17, CCS (Pension) Rules, 2021", "Generalising the SAS exception to all apprentices")

Q("PS-003", "III", "21", "Rule 21", "Leave that counts as qualifying service",
  "Which leave counts as qualifying service without any special order?",
  "All leave for which leave salary is payable, and all extraordinary leave granted on medical certificate",
  ("All extraordinary leave, whatever the reason for which it was granted",
   "Ordinary extraordinary leave counts only if the appointing authority so allows at the time of grant."),
  ("Only earned leave and half pay leave",
   "Leave salary is the test, which also covers commuted leave and leave not due."),
  ("No leave at all counts; only duty counts",
   "Rule 21 is an inclusive provision and expressly counts leave with salary."),
  "Rule 21 counts all leave during service for which leave salary is payable and all extraordinary leave granted on "
  "medical certificate. The proviso allows the appointing authority, at the time of granting other extraordinary "
  "leave, to direct that it count where the servant could not join or rejoin duty because of civil commotion or was "
  "prosecuting higher scientific and technical studies.",
  "Leave with salary and medical-certificate EOL count; other EOL does not unless allowed on grant.",
  "Rule 21, CCS (Pension) Rules, 2021", "Counting all extraordinary leave as qualifying")

Q("PS-004", "III", "23", "Rule 23", "Suspension and qualifying service",
  "Time under suspension counts as qualifying service where, on conclusion of the inquiry, the servant:",
  "is fully exonerated, or only a minor penalty is imposed and the suspension is held wholly unjustified",
  ("is awarded any penalty short of dismissal",
   "The rule requires exoneration, or a minor penalty with an unjustified suspension."),
  ("is reinstated, whatever the findings", "Reinstatement is not the test; the findings on the inquiry are."),
  ("has the period regularised as extraordinary leave",
   "Regularising it as extraordinary leave is a different consequence under rule 27."),
  "Rule 23(1) counts suspension time only where the servant is fully exonerated, or where only a minor penalty is "
  "imposed and the suspension is held to be wholly unjustified. Rule 23(2) otherwise excludes it unless the competent "
  "authority expressly declares that it shall count, and rule 23(3) requires that declaration to be made by order and "
  "recorded in the service book.",
  "Suspension counts only on exoneration, or a minor penalty with unjustified suspension.",
  "Rule 23, CCS (Pension) Rules, 2021", "Assuming any reinstatement makes suspension count")

Q("PS-005", "III", "26", "Rule 26(6)", "Withdrawal of resignation",
  "A Government servant resigns to take up an appointment in a private commercial company. He later asks to withdraw "
  "the resignation. The appointing authority:",
  "shall not accept the request, because the resignation was to join a private commercial company",
  ("may accept it if the absence did not exceed ninety days",
   "The ninety-day condition in rule 26(5)(iii) cannot rescue a resignation of this kind."),
  ("may accept it with the President's approval",
   "Rule 26(6) is an absolute bar, not a matter of higher sanction."),
  ("may accept it if a comparable post is available",
   "Availability of the post is one of the rule 26(5) conditions, which rule 26(6) overrides."),
  "Rule 26(5) permits withdrawal in the public interest on four conditions, including absence of not more than ninety "
  "days and availability of the post. Rule 26(6) then bars withdrawal altogether where the resignation was tendered "
  "to take up an appointment in a private commercial company, or in a corporation or company owned or controlled by "
  "the Government, or in a body controlled or financed by it.",
  "Withdrawal is barred where the resignation was to join a company or body.",
  "Rule 26(5) and (6), CCS (Pension) Rules, 2021", "Applying the ninety-day rule to a barred category")

Q("PS-006", "III", "27", "Rule 27(1)", "Interruption in service",
  "An interruption in service forfeits past service, except in which case?",
  "Joining time while on transfer from one post to another",
  ("Unauthorised absence after the post has been filled substantively",
   "Clause (b) protects unauthorised absence in continuation of authorised leave only while the post is not filled substantively."),
  ("Resignation accepted to join another Government post without permission",
   "Rule 26 governs resignation, and the protection in rule 26(2) requires proper permission."),
  ("Dismissal followed by reinstatement on review",
   "Reinstatement restores past service under rule 25, but the dismissal itself was not an excepted interruption."),
  "Rule 27(1) lists five exceptions to forfeiture: authorised leave of absence; unauthorised absence in continuation "
  "of authorised leave so long as the post is not filled substantively; suspension immediately followed by "
  "reinstatement, or ending in death or retirement; transfer to non-qualifying service in the public interest; and "
  "joining time on transfer. Rule 27(2) then lets the appointing authority commute periods of absence without leave "
  "retrospectively into extraordinary leave.",
  "Joining time is an excepted interruption.",
  "Rule 27, CCS (Pension) Rules, 2021", "Treating any absence as an excepted interruption")

Q("PS-007", "III", "30", "Rule 30(4)", "Finality of verification",
  "Verification of qualifying service under rule 30 is:",
  "final, and not to be reopened except on a subsequent change in the rules or orders governing qualifying service",
  ("provisional until the pension case is settled",
   "Rule 30(4) makes the verification final, not provisional."),
  ("open to reopening at any time on audit objection",
   "Only a change in the governing rules and orders reopens it."),
  ("final only where the servant has completed eighteen years",
   "The eighteen-year point is one of the two occasions for verification, not a condition of finality."),
  "Rule 30(1) requires verification after eighteen years of service and again when five years remain before "
  "superannuation, with the result communicated in Format 4. Rule 30(4) makes the verification final and immune from "
  "reopening except where a subsequent change in the rules and orders governing the conditions under which service "
  "qualifies for pension necessitates it.",
  "Verification is final; only a change of rules reopens it.",
  "Rule 30(1) and (4), CCS (Pension) Rules, 2021", "Treating the Format 4 certificate as provisional")

Q("PS-008", "IV", "32", "Rule 32(3) Illustration", "Average emoluments across a broken month",
  "A servant retires on 16 July 2019. For the fractional periods of the last ten months, emoluments are computed:",
  "by multiplying the emolument by 14/30 and 16/30, whatever the number of days in the month",
  ("by taking the actual number of days in each calendar month as the denominator",
   "The rule fixes a thirty-day month precisely to avoid that."),
  ("by ignoring the fractional periods altogether",
   "The rule includes equal periods before the ten months so that fractions add to a full month."),
  ("by rounding each fraction up to a whole month",
   "Rounding up belongs to rule 44(9), and to the amount of pension, not to average emoluments."),
  "Rule 32(3) provides that where leave without salary or suspension not counting as service falls within the last ten "
  "months, the period is disregarded and an equal period before the ten months is included, a month being reckoned as "
  "thirty days so that fractions add up to a full month. The illustration works the point: a retirement on 16 July "
  "2019 gives fractional periods of fourteen days of September 2018 and sixteen days of July 2019, computed at 14/30 "
  "and 16/30, including for February.",
  "Thirty-day month: 14/30 and 16/30, even for February.",
  "Rule 32(3) and its Illustration, CCS (Pension) Rules, 2021", "Using the calendar month as the denominator")

Q("PS-009", "IV", "31", "Rule 31(7)", "Emoluments on deputation",
  "Pay drawn while on deputation to a State Government is:",
  "not treated as emoluments; the pay he would have drawn under the Central Government is treated as emoluments",
  ("treated as emoluments, because it is the pay actually drawn",
   "Actual drawal does not decide the question; rule 31(6) and 31(7) split ex-cadre from State deputation."),
  ("treated as emoluments only if the deputation exceeded one year",
   "There is no duration condition in rule 31(7)."),
  ("ignored altogether for pension purposes",
   "It is not ignored; the counterfactual Central pay is substituted for it."),
  "Rule 31(6) treats pay drawn on deputation to an ex-cadre post in the same or another Central Government Department, "
  "or to the Armed Forces, as emoluments. Rule 31(7) draws the opposite conclusion for deputation to a State "
  "Government or foreign service: that pay is not emoluments, and the pay the servant would have drawn under the "
  "Central Government is treated as emoluments instead.",
  "State deputation: substitute the Central pay; ex-cadre: actual pay counts.",
  "Rules 31(6) and 31(7), CCS (Pension) Rules, 2021", "Confusing ex-cadre deputation with State deputation")

Q("PS-010", "IV", "31", "Rule 31(1) Explanation", "Stagnation increment",
  "For the calculation of retirement benefits, a stagnation increment is:",
  "treated as emoluments",
  ("excluded, because it is not basic pay", "The Explanation to rule 31(1) expressly includes it."),
  ("included only for gratuity, not for pension", "The Explanation speaks of retirement benefits generally."),
  ("included only where it was actually drawn for ten months",
   "The ten-month averaging is a rule 32 question, not a condition on the Explanation."),
  "Rule 31(1) defines emoluments as basic pay under rule 9(21)(a)(i) of the Fundamental Rules immediately before "
  "retirement or on the date of death, and adds non-practising allowance for a medical officer in lieu of private "
  "practice. The Explanation then provides that a stagnation increment shall be treated as emoluments for the "
  "calculation of retirement benefits.",
  "Stagnation increment counts as emoluments.",
  "Rule 31(1) and its Explanation, CCS (Pension) Rules, 2021", "Treating the stagnation increment as outside basic pay")

Q("PS-011", "V", "39", "Rule 39(3)", "Medical authority for invalid pension",
  "For a non-Gazetted servant whose pay exceeds \u20b954,000 a month, the medical authority for invalid pension is:",
  "a Medical Board",
  ("the Civil Surgeon alone", "The Civil Surgeon route is for the other cases in rule 39(3)(b)."),
  ("a District Medical Officer alone", "The District Medical Officer is within clause (b), not clause (a)."),
  ("any authorised medical attendant", "The attendant appears in the leave rules, not here."),
  "Rule 39(3) fixes the authority by clause (a) and clause (b): a Medical Board for a Gazetted servant and for a "
  "non-Gazetted servant whose pay under rule 9(21) of the Fundamental Rules exceeds fifty-four thousand rupees a "
  "month; and the Civil Surgeon, a District Medical Officer, or a Medical Officer of equivalent status in other "
  "cases. Rule 39(7) adds that a lady doctor shall sit on the Board when a woman is examined.",
  "Medical Board above \u20b954,000 and for all Gazetted servants.",
  "Rule 39(3) and (7), CCS (Pension) Rules, 2021", "Using the pay threshold only for non-Gazetted staff")

Q("PS-012", "V", "41", "Rule 41(2)", "Compassionate allowance decision",
  "Where a servant is dismissed, the competent authority must decide on a compassionate allowance:",
  "not later than three months after the order imposing the penalty",
  ("within six months of the order, in every case",
   "Six months is the rule 41(4) period, and only for penalties imposed before the rules commenced."),
  ("at any time before the servant attains superannuation", "Rule 41(2) sets a three-month limit."),
  ("only if the servant applies within ninety days",
   "The authority must act on its own motion or on the representation, within the same three months."),
  "Rule 41(1) forfeits pension and gratuity on dismissal or removal, subject to a compassionate allowance not "
  "exceeding two-thirds of the pension or gratuity that would have been admissible on superannuation retirement. "
  "Rule 41(2) requires the competent authority to decide the question on its own motion or on the servant's "
  "representation not later than three months after the penalty order. Rule 41(4) gives six months only where the "
  "penalty was imposed before the rules commenced.",
  "Three months for a live case; six months only for pre-commencement penalties.",
  "Rule 41(2) and (4), CCS (Pension) Rules, 2021", "Swapping the three-month and six-month periods")

Q("PS-013", "V", "39", "Rule 39(8)", "Time limit for invalid pension",
  "Where a servant is found unfit for further service, invalid pension may be granted:",
  "not later than forty five days from the date of receipt of the Format 6 certificate",
  ("within three months of the application for retirement",
   "The trigger is the certificate, and the period is forty-five days."),
  ("within thirty days of the medical examination",
   "Thirty days is the period for requesting the examination under rule 39(3)."),
  ("within six months of the medical certificate", "Six months is not the period in rule 39(8)."),
  "Rule 39(8) requires the medical authority to issue a Medical Certificate in Format 6 where the servant is found "
  "unfit for further service or fit only for less laborious work. Where he is found unfit, invalid pension may be "
  "granted under rule 44 not later than forty-five days from the date of receipt of that certificate. Rule 39(3) "
  "separately requires the Head of Office to request the examination within fifteen days and the examination to be "
  "held within thirty days.",
  "Invalid pension: forty-five days from receipt of Format 6.",
  "Rule 39(3) and (8), CCS (Pension) Rules, 2021", "Running the clock from the application instead of the certificate")

Q("PS-014", "VI", "43", "Rule 43(1) fourth proviso", "Voluntary retirement and fractional service",
  "A servant with 19 years and 10 months of qualifying service seeks voluntary retirement under rule 43. He:",
  "is not eligible, because the rule 44(7) rounding of three months or more does not apply to rule 43",
  ("is eligible, since 19 years and 10 months rounds up to 20 years",
   "The fourth proviso expressly disapplies the rounding for rule 43."),
  ("is eligible if the appointing authority condones the shortfall",
   "There is no condonation route in rule 43 for the twenty-year requirement."),
  ("is eligible only if he gives six months' notice", "Notice length is not the obstacle; the qualifying service is."),
  "Rule 43(1) allows voluntary retirement after twenty years' qualifying service on three months' notice. Its fourth "
  "proviso requires that the servant has completed, or will complete, twenty years on the intended date of "
  "retirement, and expressly disapplies rule 44(7), under which a fraction of three months or more is treated as a "
  "completed six-monthly period. Nineteen years and ten months therefore falls short, and the rule 44(8) concession "
  "of nine years and nine months is confined to pension on invalid retirement.",
  "Twenty years exact for rule 43; no rounding under rule 44(7).",
  "Rule 43(1) fourth proviso, CCS (Pension) Rules, 2021", "Importing rule 44(7) rounding into rule 43")

Q("PS-015", "VI", "43", "Rule 43(4)(b)", "Curtailed notice and commutation",
  "Where the appointing authority relaxes the three-month notice under rule 43(4), the condition is that the servant:",
  "shall not apply for commutation of a part of his pension before the expiry of the three-month notice period",
  ("shall forfeit one month's pension", "No forfeiture of pension is prescribed."),
  ("shall serve the balance of the notice after retirement", "That would contradict the relaxation itself."),
  ("shall not receive retirement gratuity until the notice period ends",
   "The bar in the rule is on commutation, not on gratuity."),
  "Rule 43(4)(a) allows a request for acceptance of less than three months' notice with reasons; clause (b) lets the "
  "appointing authority relax the notice where the curtailment causes no administrative inconvenience, on the "
  "condition that the servant shall not apply for commutation of a part of his pension before the expiry of the "
  "three-month notice period. Commutation is governed by the CCS (Commutation of Pension) Rules, 1981 under rule 84(2).",
  "Curtailed notice: no commutation until the three months would have run.",
  "Rule 43(4)(b), CCS (Pension) Rules, 2021", "Missing the commutation condition attached to the relaxation")

Q("PS-016", "VI", "43", "Rule 43(3)", "Withholding permission to retire",
  "Which circumstance does NOT entitle the appointing authority to withhold permission to retire under rule 43?",
  "The servant has applied for an advance of pay",
  ("The servant is under suspension", "Clause (i) of rule 43(3) covers suspension."),
  ("A charge sheet has been issued and disciplinary proceedings are pending",
   "Clause (ii) covers pending disciplinary proceedings."),
  ("Judicial proceedings on charges of grave misconduct are pending",
   "Clause (iii) covers them, and the Explanation defines when they are pending."),
  "Rule 43(3) allows permission to be withheld in three circumstances: suspension; a charge sheet issued with "
  "disciplinary proceedings pending; and judicial proceedings on charges which may amount to grave misconduct. The "
  "Explanation treats judicial proceedings as pending once a complaint or police report of which the Magistrate "
  "takes cognizance has been made. Even in those cases, the proviso permits acceptance with the approval of the "
  "President.",
  "Three grounds for withholding; the President's approval can override them.",
  "Rule 43(3) and its Explanation, CCS (Pension) Rules, 2021", "Inventing a fourth ground for withholding")
