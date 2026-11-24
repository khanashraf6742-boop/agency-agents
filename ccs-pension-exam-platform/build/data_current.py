#!/usr/bin/env python3
"""data_current.py — questions on the instruments that changed the 2021 Rules.

Everything here is keyed to amendments.py. A question that quotes a figure carries the
instrument that sets the figure, so the audit can check that no question states a
superseded number as if it were current.
"""
from __future__ import annotations

FACTS = []


def Q(fid, ch, rule, rules_text, topic, stem, ans, d1, d2, d3, why, safe, src, trap,
      kind="CURRENT", tag="Tough", covers=None, version=None):
    FACTS.append(dict(id=fid, ch=ch, rule=rule, rules_text=rules_text, topic=topic,
                      q=stem, a=ans, d=[d1, d2, d3], why=why, safe=safe, src=src,
                      trap=trap, kind=kind, tag=tag, covers=covers or [],
                      version=version))


# --------------------------------------------------------------- the gratuity ceiling
Q("CU-001", "VII", "45", "Rule 45(1) and O.M. 30.05.2024", "Ceiling on gratuity",
  "What is the maximum amount of retirement gratuity or death gratuity admissible to a Central Government "
  "civil servant today?",
  "Twenty-five lakh rupees, with effect from 1 January 2024",
  ("Twenty lakh rupees, because that is the figure printed in rule 45(1)",
   "The rule text is still twenty lakh rupees, but the order of 30 May 2024 raised the limit to twenty-five lakh with effect from 1 January 2024."),
  ("Thirty lakh rupees, on the Seventh Pay Commission's second revision",
   "No order has gone beyond twenty-five lakh rupees."),
  ("No monetary ceiling, after the 2024 amendment",
   "The ceiling was raised, not removed."),
  "Rule 45(1) as notified in 2021 caps gratuity at twenty lakh rupees. The Department of Pension and Pensioners' "
  "Welfare, by Office Memorandum No. 28/03/2024-P&PW(B)/Gratuity/9559 dated 30 May 2024, increased the maximum to "
  "twenty-five lakh rupees with effect from 1 January 2024, the date the dearness allowance reached fifty per cent. "
  "Paragraph 7 of that order says the formal amendment to the Rules will be notified separately, so the printed "
  "rule still carries the old figure and the order governs the payment.",
  "The operative ceiling is twenty-five lakh rupees; rule 45(1) still prints twenty lakh.",
  "Rule 45(1), CCS (Pension) Rules, 2021 and O.M. No. 28/03/2024-P&PW(B)/Gratuity/9559 dated 30.05.2024",
  "Quoting the printed rule as the current entitlement", covers=["45(1)"], version="A-2024-03")

Q("CU-002", "VII", "45", "Rule 45(1) and O.M. 30.05.2024", "Trigger for the gratuity increase",
  "The gratuity ceiling was raised from twenty lakh to twenty-five lakh rupees because:",
  "the dearness allowance rate reached fifty per cent, which is the trigger written into the Seventh Pay Commission's scheme",
  ("the Eighth Pay Commission made its first recommendation",
   "The Eighth Pay Commission had not reported when the order issued."),
  ("Parliament amended the Payment of Gratuity Act, 1972",
   "That Act governs private employment, not the CCS (Pension) Rules."),
  ("the retirement age was raised to sixty-two years",
   "No change in the age of superannuation was made."),
  "The Seventh Pay Commission linked a further twenty-five per cent increase in the gratuity ceiling to the "
  "dearness allowance reaching fifty per cent. The Department of Expenditure raised dearness allowance from "
  "forty-six to fifty per cent with effect from 1 January 2024 by its order of 12 March 2024, and the pension "
  "order of 30 May 2024 followed with effect from the same date.",
  "DA at fifty per cent is the trigger, and the date is 1 January 2024.",
  "O.M. No. 28/03/2024-P&PW(B)/Gratuity/9559 dated 30.05.2024, paragraph 2",
  "Treating the increase as a Pay Commission recommendation in its own right",
  covers=["45(1)"], version="A-2024-03")

Q("CU-003", "VII", "45", "O.M. 24.10.2025", "Scope of the twenty-five lakh ceiling",
  "The twenty-five lakh rupee gratuity ceiling applies to:",
  "persons governed by the CCS (Pension) Rules, 2021 and the CCS (Payment of Gratuity under NPS) Rules, 2021",
  ("every employee of a body funded by the Central Government, including autonomous bodies and universities",
   "The order of 24 October 2025 excludes autonomous bodies, universities and societies."),
  ("employees of public sector undertakings and banks, who follow Central Government rates",
   "Public sector undertakings and banks are expressly outside the order."),
  ("State Government employees whose rules are modelled on the Central Rules",
   "State Governments are expressly outside the order."),
  "The order of 24 October 2025 states the scope that the order of 30 May 2024 left unstated. The twenty-five "
  "lakh rupee ceiling belongs to the two central rule sets. Public sector undertakings, banks, port trusts, the "
  "Reserve Bank of India, autonomous bodies, universities, State Governments and societies are not covered by it "
  "and continue under their own schemes.",
  "The ceiling is confined to the two central rule sets.",
  "DoP&PW O.M. F.No. 2/9/2025-P&PW(F) dated 24.10.2025",
  "Extending a central ceiling to PSUs and autonomous bodies", covers=["45(1)"], version="A-2025-02")

# --------------------------------------------------------------- rule 8 after 2022
Q("CU-004", "I", "8", "Rule 8(1) as substituted in 2022", "Competent authority to withhold pension",
  "After the amendment of 2022, who may withhold or withdraw a pension under rule 8(1) where the appointing "
  "authority for the post was subordinate to the President?",
  "the Secretary of the administrative Ministry or Department",
  ("the President, who reserves the power to himself",
   "The 2022 amendment moved the power to the Secretary where the appointing authority is subordinate to the President."),
  ("the Comptroller and Auditor-General of India, in every case",
   "The Comptroller and Auditor-General acts only for the Indian Audit and Accounts Department."),
  ("the Head of Office who processed the pension case",
   "The Head of Office prepares the case; the power belongs to the authority in rule 8(1)."),
  "Rule 8(1) was substituted by G.S.R. 770(E) dated 7 October 2022. The power is now exercised by the President "
  "where the President is the appointing authority for the post, by the Secretary of the administrative Ministry "
  "or Department where the appointing authority is subordinate to the President, and by the Comptroller and "
  "Auditor-General for a pensioner who retired from the Indian Audit and Accounts Department from a post below "
  "that level.",
  "President, Secretary, or C&AG, according to who appointed the pensioner.",
  "Rule 8(1), CCS (Pension) Rules, 2021 as substituted by G.S.R. 770(E) dated 07.10.2022",
  "Reading rule 8(1) from the 2021 gazette alone", covers=["8(1)"], version="A-2022-01")

Q("CU-005", "I", "8", "Rule 8(6A)", "Appeal against an order under rule 8",
  "An appeal against an order withholding pension passed by the Secretary of a Ministry lies to:",
  "the President, who decides it in consultation with the Union Public Service Commission",
  ("the Union Public Service Commission directly",
   "The Commission is consulted; it does not hear the appeal."),
  ("the Central Administrative Tribunal in the first instance",
   "The statutory appeal under rule 8(6A) comes first; the Tribunal is a judicial remedy."),
  ("no authority, because rule 8 orders are final",
   "Only an order of the President is final; sub-rule (6A)(b) creates an appeal against any other authority's order."),
  "Sub-rule (6A) was inserted by G.S.R. 770(E) dated 7 October 2022. Clause (a) says no appeal lies against an "
  "order made by the President. Clause (b) says an appeal against an order passed by any other authority lies to "
  "the President, who passes such orders as he deems fit in consultation with the Union Public Service "
  "Commission.",
  "Appeal lies to the President unless the President passed the order.",
  "Rule 8(6A), inserted by G.S.R. 770(E) dated 07.10.2022",
  "Assuming every rule 8 order is appealable", covers=["8(6)"], version="A-2022-01")

# --------------------------------------------------------------- female nominee
Q("CU-006", "VIII", "50", "Rule 50(8) and O.M. 01.01.2024", "Nomination by a female Government servant",
  "A female Government servant whose divorce proceedings are pending may ask that family pension be paid to her "
  "eligible child in precedence to her husband. That request is made:",
  "in writing to the Head of Office, and it operates if she dies during the pendency of the proceedings",
  ("by a fresh nomination in Form 4, which overrides the statutory order in rule 50(6)",
   "Form 4 records family details; the order of eligibility in rule 50(6) is not displaced by it."),
  ("to the Pension Disbursing Authority after retirement only",
   "The request may be made by a serving Government servant or a pensioner, and it is made to the Head of Office."),
  ("by will, since the spouse's right is a matter of succession",
   "The order of 1 January 2024 sets a written request to the Head of Office, not a testamentary disposition."),
  "The Department's Office Memorandum No. 1/1(1)/2023-P&PW(E) dated 1 January 2024 applies where divorce "
  "proceedings are pending in a competent court, or where the woman has filed a case against her husband under "
  "the Protection of Women from Domestic Violence Act, the Dowry Prohibition Act or the Indian Penal Code. "
  "Paragraph 3(a) requires a request in writing to the Head of Office, which takes effect if she dies during the "
  "pendency of those proceedings.",
  "Written request to the Head of Office, effective on death during the proceedings.",
  "DoP&PW O.M. No. 1/1(1)/2023-P&PW(E) dated 01.01.2024, paragraphs 3(a) and 4",
  "Treating the request as a nomination form", covers=["50(8)"], version="A-2024-02")

Q("CU-007", "VIII", "50", "O.M. 01.01.2024, paragraph 3(b)", "Disbursal where the mother has nominated a child",
  "Where the female Government servant had made such a request and dies during the proceedings, and is survived "
  "by a widower with a minor child, the family pension is payable to:",
  "the widower, provided he is the guardian of the child, and to the child through the actual guardian if he ceases to be guardian",
  ("the minor child directly, through a guardian appointed by the court",
   "The widower receives it while he remains the guardian; the child's direct right arises on attaining majority."),
  ("the widower absolutely, because the nomination lapses on death",
   "The nomination does not lapse; it changes the order in which the pension is disbursed."),
  ("the child and the widower in equal shares",
   "The order sets a sequence, not a sharing, unless more than one person is payable at the same time."),
  "Paragraph 3(b)(ii) of the order provides that where the deceased is survived by a widower with a minor child "
  "or a child suffering from a disorder or disability of mind, the family pension is payable to the widower "
  "provided he is the guardian; if he ceases to be the guardian it is payable to the child through the person who "
  "is the actual guardian, and when the minor attains majority and remains eligible it becomes payable to the "
  "child.",
  "Widower as guardian first; the child takes over on majority.",
  "DoP&PW O.M. No. 1/1(1)/2023-P&PW(E) dated 01.01.2024, paragraph 3(b)(ii)",
  "Paying the minor directly", covers=["50(8)", "50(9)"], version="A-2024-02")

Q("CU-008", "VIII", "50", "O.M. 01.01.2024", "Effect of the female-nominee order on the rule text",
  "The order of 1 January 2024 allowing a female Government servant to nominate her child in precedence to her "
  "husband:",
  "was issued as an Office Memorandum, and paragraph 6 records that the formal amendment to rule 50 would be notified separately",
  ("substituted clause (a) of rule 50(8) in the Gazette the same day",
   "No gazette amendment issued on 1 January 2024; the order is an Office Memorandum."),
  ("inserted a new sub-rule (8A) into rule 50",
   "Sub-rule (8A) was not inserted; the order works within sub-rules (8) and (9)."),
  ("was struck down for want of legislative competence",
   "The order stands and has been reiterated in paragraph 4 of the order of 29 October 2026."),
  "The instrument is Office Memorandum No. 1/1(1)/2023-P&PW(E) dated 1 January 2024. Paragraph 6 says that a "
  "formal amendment to rule 50 \"will be notified separately\", and no such amendment appears in the gazette "
  "series up to the amendment rules of 2025. The rule text is therefore unchanged and the order operates as an "
  "instruction on how a case under it is to be decided.",
  "An Office Memorandum, not an amendment of the rule text.",
  "DoP&PW O.M. No. 1/1(1)/2023-P&PW(E) dated 01.01.2024, paragraph 6",
  "Assuming the rule text was amended", covers=["50(8)"], version="A-2024-02")

# --------------------------------------------------------------- Form 6-A
Q("CU-009", "X", "57", "Rule 57(2)(a) as substituted in 2024", "Form 6-A at retirement",
  "From the date the amendment rules of 2024 took effect, the retiring Government servant submits the completed "
  "family and pension particulars:",
  "in Form 6-A, not later than six months before the date of retirement",
  ("in Form 4 and Form 6, as rule 57(2)(a) originally required",
   "Form 4 and Form 6 were replaced by Form 6-A for the retirement case."),
  ("in Form 10, at any time before the Pension Payment Order issues",
   "Form 10 is the family pension claim for a death case."),
  ("in Format 9, which is the bank undertaking",
   "Format 9 is an undertaking to the bank, and the 2024 amendment replaced it in this context with Form 6-A."),
  "G.S.R. 410(E) dated 16 July 2024 substituted rule 57(2)(a) so that the Government servant submits duly "
  "completed Form 6-A to the Head of Office not later than six months before his date of retirement. It also "
  "substituted rule 57(3) so that where Form 6-A is submitted by the spouse or another member of the family, the "
  "Government servant is not entitled to commutation until he applies for it himself.",
  "Form 6-A, six months before retirement.",
  "Rule 57(2)(a), as substituted by G.S.R. 410(E) dated 16.07.2024",
  "Staying with Form 4 and Form 6", covers=["57(2)(a)", "57(1)(c)(iii)"], version="A-2024-01")

Q("CU-010", "X", "80", "Rule 80(5) proviso as substituted in 2024", "Form 6-A in place of Form 10",
  "Where a Government servant dies after retirement and no member of the family is eligible for family pension, "
  "the person in whose favour a gratuity nomination was made may submit:",
  "Form 6-A in place of Form 10, giving his or her bank account details in Form 6-A",
  ("Form 10, because the gratuity nominee has no other route",
   "The proviso substituted in 2024 gives the gratuity nominee Form 6-A instead."),
  ("Form 4 together with Format 9",
   "Both were subsumed into Form 6-A for this purpose."),
  ("no form at all, the gratuity being paid on the nomination itself",
   "A claim form is still required; the proviso names it."),
  "The first proviso to rule 80(5)(a) was substituted by G.S.R. 410(E) dated 16 July 2024. Where there is no "
  "member of the family eligible to receive family pension on the death of the Government servant, a member of "
  "the family in whose favour a nomination was made for payment of gratuity is allowed to submit Form 6-A in "
  "place of Form 10, and must indicate the details of his or her bank account in Form 6-A.",
  "Gratuity nominee: Form 6-A instead of Form 10.",
  "Rule 80(5)(a), first proviso, as substituted by G.S.R. 410(E) dated 16.07.2024",
  "Sending the nominee to Form 10", covers=["80(5)(a)#P1", "80(5)(c)"], version="A-2024-01")

Q("CU-011", "X", "53", "Rule 53(1) as substituted in 2024", "Which system carries Form 6-A",
  "Under rule 53(1) as substituted in 2024, a retiring official who is on e-HRMS submits Form 6-A through:",
  "e-HRMS, and only in superannuation cases",
  ("Bhavishya, in every case",
   "Bhavishya is the route for cases other than superannuation and for officials not on e-HRMS."),
  ("either system, at the official's choice",
   "The rule assigns the route by case and by whether the official is on e-HRMS."),
  ("the Head of Office, who uploads it on the official's behalf",
   "The official submits; the Head of Office processes."),
  "Rule 53(1) was substituted by G.S.R. 410(E). Unless exempted by a general or special order, the pension case "
  "is processed online through Bhavishya or e-HRMS. Retiring officials who are on e-HRMS submit Form 6-A through "
  "e-HRMS, and only for superannuation. Those not on e-HRMS, and cases other than superannuation such as "
  "voluntary retirement, premature retirement, absorption, invalidation, compulsory retirement and dismissal or "
  "removal, submit Form 6-A through Bhavishya.",
  "e-HRMS for superannuation, Bhavishya for everything else.",
  "Rule 53(1), as substituted by G.S.R. 410(E) dated 16.07.2024",
  "Assuming one system covers every case", covers=["53(1)"], version="A-2024-01")

# --------------------------------------------------------------- rule 37(29)(c)
Q("CU-012", "V", "37", "Rule 37(29)(c) as substituted in 2025", "Forfeiture after absorption in a PSU",
  "After the amendment of 2025, where an employee absorbed in a public sector undertaking is dismissed from the "
  "undertaking for subsequent misconduct, his retirement benefits for the Government service:",
  "are forfeited, and the undertaking's decision is subject to review by the administrative Ministry",
  ("are protected, because the Government service ended on absorption",
   "That was the position before the 2025 amendment and is no longer the rule."),
  ("are forfeited only if the Central Government separately dismisses him",
   "The undertaking's order now operates on the Government service benefits."),
  ("are reduced by half but cannot be forfeited",
   "The rule speaks of forfeiture, not reduction."),
  "G.S.R. 340(E) dated 22 May 2025 substituted clause (c) of rule 37(29). Dismissal, removal or retrenchment "
  "from the public sector undertaking after absorption, for subsequent misconduct, now leads to forfeiture of the "
  "retirement benefits for the Government service as well, and the undertaking's decision is subject to review "
  "by the Ministry administratively concerned with it. The Explanation applies rules 7 and 8 read with rule 41 "
  "and sub-rule (5) of rule 44 analogously.",
  "Forfeiture now reaches the Government service benefits.",
  "Rule 37(29)(c), as substituted by G.S.R. 340(E) dated 22.05.2025",
  "Reading the pre-2025 protection into the rule", covers=["37(29)(c)"], version="A-2025-01")

Q("CU-013", "V", "37", "Rule 37(26)(c)", "Autonomous bodies after the 2025 amendment",
  "The 2025 amendment to rule 37(29)(c) changed the position for an employee absorbed in a public sector "
  "undertaking. What is the position for an employee absorbed in an autonomous body?",
  "unchanged: dismissal from the autonomous body does not amount to forfeiture of the retirement benefits for Government service",
  ("also changed, because the same clause governs both",
   "The autonomous body provision is rule 37(26)(c) and was not amended."),
  ("changed more strictly, because autonomous bodies are funded by the Government",
   "No change was made to rule 37(26)(c)."),
  ("governed by the 2024 amendment instead",
   "The 2024 amendment dealt with forms, not forfeiture."),
  "The amendment of 2025 substituted clause (c) of sub-rule (29) only. Clause (c) of sub-rule (26), which deals "
  "with an employee absorbed in an autonomous body, still says that dismissal or removal from the body for "
  "subsequent misconduct shall not amount to forfeiture of the retirement benefits for the service rendered "
  "under the Government.",
  "PSU: forfeiture. Autonomous body: protection intact.",
  "Rules 37(29)(c) and 37(26)(c), CCS (Pension) Rules, 2021",
  "Assuming the amendment reached both clauses", covers=["37(29)(c)"], version="A-2025-01")

# --------------------------------------------------------------- additional pension
Q("CU-014", "VII", "44", "Rule 44(6) and O.M. 18.10.2024", "Additional pension by age band",
  "A pensioner attains eighty-two years of age. The additional pension admissible is:",
  "twenty per cent of the basic pension, from the first day of the calendar month in which the age of eighty is attained",
  ("ten per cent, rising to twenty per cent at eighty-five",
   "The table starts at twenty per cent for the band from eighty to less than eighty-five."),
  ("twenty per cent, from the pensioner's birthday",
   "The order fixes the first day of the calendar month in which it falls due."),
  ("no additional pension before eighty-five",
   "The first band begins at eighty."),
  "Rule 44(6) sets the bands: twenty per cent from eighty years to less than eighty-five, thirty per cent from "
  "eighty-five, forty per cent from ninety, fifty per cent from ninety-five and one hundred per cent from one "
  "hundred years. The order of 18 October 2024 reiterates the table and confirms payment from the first day of "
  "the calendar month in which the entitlement falls due, illustrating it with a pensioner born on 20 August "
  "1942 who draws the increment from 1 August 2022.",
  "Twenty per cent, from the first day of the birth month.",
  "Rule 44(6), CCS (Pension) Rules, 2021 and DoP&PW O.M. dated 18.10.2024",
  "Running the increment from the birthday", covers=["44(6)", "50(3)"], version="A-2024-04")

# --------------------------------------------------------------- 2026 family pension orders
Q("CU-015", "VIII", "50", "O.M. 29.10.2026", "Two wives",
  "Where a deceased Government servant is survived by two widows, the family pension is:",
  "paid to the widows in equal shares, and on the death or ineligibility of one her share passes to her child or children",
  ("paid to the first wife only, the second marriage being void",
   "Rule 50(8)(c) provides for equal shares; the legality of the marriage is decided first under the 2025 instruction."),
  ("paid to the widow who was nominated in Form 4",
   "Form 4 records details; it does not displace rule 50(8)(c)."),
  ("withheld until a court decides which marriage is valid",
   "The Department's direction is to consult the Department of Legal Affairs on legality, not to withhold the pension."),
  "Rule 50(8)(c) provides that where the deceased is survived by more widows than one, family pension is paid to "
  "them in equal shares, and on the death or ineligibility of a widow her share becomes payable to her child or "
  "children who fulfil the conditions in sub-rule (9). The order of 27 October 2025 adds that where the legality "
  "of the second marriage is in question, the matter is to be settled in consultation with the Department of "
  "Legal Affairs case by case before eligibility is decided.",
  "Equal shares between widows, then to each widow's children.",
  "Rule 50(8)(c), CCS (Pension) Rules, 2021 and DoP&PW O.M. dated 27.10.2025",
  "Paying only the first wife", covers=["50(8)(c)", "50(6)"], version="A-2026-01")

Q("CU-016", "VIII", "50", "O.M. 29.10.2026", "Divorce and judicial separation",
  "A deceased pensioner is survived by a judicially separated widow and no child. Her claim to family pension:",
  "is considered under rule 50(8)(h), a decree of judicial separation not having dissolved the marriage",
  ("fails, because a judicially separated spouse is treated as divorced",
   "The order of 29 October 2026 distinguishes the two expressly: a divorced spouse is not eligible, a judicially separated one may be."),
  ("succeeds at the enhanced rate without any condition",
   "The claim is subject to the conditions in rule 50(8)(h) and the following clauses."),
  ("is decided by the court that granted the decree",
   "The decree does not fix the pension; the Rules do."),
  "The Office Memorandum of 29 October 2026 records that a decree of judicial separation permits the spouses to "
  "live separately without dissolving the marriage, so a judicially separated widow or widower may be considered "
  "under rule 50(8)(h) to (j). Where there is no eligible child the claim is examined under rule 50(8)(h). A "
  "divorced spouse is not eligible, though the children of the marriage may be.",
  "Judicial separation: eligible. Divorce: not eligible.",
  "DoP&PW O.M. No. 1/1(39)/2026-P&PW(E)/E-12002-(7) dated 29.10.2026, paragraphs 2 to 4",
  "Treating judicial separation as divorce", covers=["50(8)(h)", "50(8)(i)", "50(8)(j)"], version="A-2026-02")

Q("CU-017", "VIII", "50", "O.M. 29.10.2026", "Order of eligibility",
  "After the spouse and all children cease to be eligible, family pension under rule 50 becomes payable next to:",
  "the dependent parents, the mother ordinarily preceding the father",
  ("the dependent siblings with a disability, before the parents",
   "Siblings come after the parents, under rule 50(11)."),
  ("the married daughters, who return to the list",
   "Married daughters are excluded by rule 50(9)(n) unless disabled."),
  ("the widowed mother only, the father being excluded",
   "The father is eligible if the mother is not; the mother ordinarily precedes him."),
  "Rule 50(6) sets the order: widow or widower, then children, then dependent parents, then dependent siblings "
  "with a mental or physical disability. Rule 50(10)(b) provides that family pension admissible to parents is "
  "payable to the mother failing which to the father, and the order of 29 October 2026 repeats that the mother "
  "ordinarily precedes the father.",
  "Parents next, mother before father; siblings last.",
  "Rule 50(6) and 50(10)(b), CCS (Pension) Rules, 2021 and DoP&PW O.M. dated 29.10.2026",
  "Putting siblings ahead of parents", covers=["50(6)", "50(10)(b)"], version="A-2026-01")

Q("CU-018", "VIII", "50", "Rule 50(13) and O.M. 29.10.2026", "Two family pensions",
  "Both husband and wife were Central Government servants. Both die, and one eligible child survives. If both "
  "family pensions are payable at the ordinary rate, the combined amount is limited to:",
  "seventy-five thousand rupees per month",
  ("one lakh twenty-five thousand rupees per month",
   "That limit applies where at least one pension is at the enhanced rate."),
  ("one lakh fifty thousand rupees per month",
   "No such limit appears in rule 50(13)."),
  ("the ordinary maximum, with no separate limit for two pensions",
   "Rule 50(13) sets a separate combined limit."),
  "Rule 50(13) sets three limits. Where the child draws two pensions at the enhanced rate, the combined amount "
  "is limited to one lakh twenty-five thousand rupees a month. Where one pension falls from the enhanced to the "
  "ordinary rate, the combined amount is still limited to one lakh twenty-five thousand. Where both are at the "
  "ordinary rate, the combined amount is limited to seventy-five thousand rupees a month.",
  "Two ordinary pensions: seventy-five thousand. Any enhanced element: one lakh twenty-five thousand.",
  "Rule 50(13), CCS (Pension) Rules, 2021",
  "Applying the single-pension ceiling to two pensions", covers=["50(13)"], version="A-2026-01")

Q("CU-019", "VIII", "50", "Rule 50(14)", "Claimant charged with murder",
  "A person otherwise eligible for family pension is charged with abetting the suicide of the Government "
  "servant. Family pension to that person:",
  "is not paid until the criminal proceedings conclude, and is paid meanwhile to the other eligible member of the family",
  ("is paid, because a charge is not a conviction",
   "Rule 50(14)(c) suspends payment on the charge itself."),
  ("is forfeited permanently",
   "Forfeiture follows only on conviction; on acquittal the pension becomes payable to him from the date of acquittal."),
  ("is paid into court until the trial ends",
   "The rule redirects it to the other eligible member of the family."),
  "Rule 50(14)(c) provides that where a person eligible for family pension is charged with murdering the "
  "Government servant or abetting it, the pension is not paid to that person until the criminal proceedings "
  "conclude. Clause (d) pays it to the other eligible member meanwhile, and the Explanation says the charge "
  "includes abetting death by suicide. Clause (e) then provides for conviction and acquittal: on conviction the "
  "person is debarred, and on acquittal the pension becomes payable to him from the date of acquittal.",
  "Charge suspends, conviction debars, acquittal restores.",
  "Rule 50(14), CCS (Pension) Rules, 2021",
  "Waiting for conviction before suspending", covers=["50(14)"])

Q("CU-020", "VIII", "50", "Rule 50(9)(h)", "Disabled child, for life",
  "Family pension to a son or daughter suffering from a disability referred to in rule 50(9)(h) is payable:",
  "for life, provided the disability existed before the death of the Government servant or pensioner and his or her spouse",
  ("until the age of twenty-five, like any other child",
   "The age of twenty-five is the ceiling for the first category of children, not this one."),
  ("for life, whatever the date on which the disability arose",
   "Condition (i) requires the disability to have existed before the death."),
  ("for ten years from the date of death",
   "No such period appears in the rule."),
  "Clause (h) of rule 50(9) provides for family pension for life to a son or daughter suffering from a disorder "
  "or disability of mind, including the mentally retarded, or a physical disability of the kind described, so as "
  "to render him or her unable to earn a living even after twenty-five years. Condition (i) requires the "
  "disability to have existed before the death of the Government servant or pensioner and his or her spouse.",
  "For life, but the disability must pre-date the death.",
  "Rule 50(9)(h), CCS (Pension) Rules, 2021",
  "Applying the twenty-five year ceiling to a disabled child", covers=["50(9)(h)"])

Q("CU-021", "VIII", "50", "Rule 50(9)(j)", "Unmarried or widowed or divorced daughter",
  "Family pension to an unmarried, widowed or divorced daughter beyond twenty-five years is payable:",
  "for life or until she marries or remarries or starts earning her livelihood, whichever is earliest",
  ("for life, without any condition",
   "Marriage, remarriage or earning a livelihood ends it."),
  ("until she attains thirty years of age",
   "No age of thirty appears in the rule."),
  ("only if she is the eldest child",
   "The order of birth decides the sequence between sisters, not eligibility."),
  "Clause (j) of rule 50(9) continues family pension to an unmarried, widowed or divorced daughter beyond "
  "twenty-five years for life or until she marries or remarries or starts earning her livelihood, whichever is "
  "earliest. Among more than one such daughter, the pension is payable in the order of birth, and a younger "
  "daughter becomes eligible when the elder next above her marries, remarries, starts earning or dies. For a "
  "widowed or divorced daughter, the widowhood or divorce must have occurred during the lifetime of the "
  "Government servant or pensioner or of his or her spouse, with a proviso for a divorce decree granted after "
  "their death where proceedings were filed during their lifetime.",
  "For life subject to three cessations, in order of birth.",
  "Rule 50(9)(j), CCS (Pension) Rules, 2021",
  "Making the pension unconditional or indefinite in all cases", covers=["50(9)(j)"])

Q("CU-022", "VIII", "50", "Rule 50(15)(a)", "Family details in Form 4",
  "A Government servant who has no family at the time of entering service must furnish the details of family:",
  "in Form 4 as soon as he acquires a family",
  ("at the time of retirement only, in Form 6-A",
   "Form 6-A is the retirement form; the obligation arises on acquiring a family."),
  ("within one year of marriage, by a separate intimation",
   "The rule requires Form 4 as soon as the family is acquired."),
  ("not at all, until a family pension claim arises",
   "The rule creates a positive obligation."),
  "Rule 50(15)(a)(i) requires a Government servant, on entering service, to give the details of his family in "
  "Form 4 to the Head of Office, including the spouse, all children, parents and disabled siblings, whether or "
  "not eligible for family pension. Clause (a)(ii) provides that if he has no family he furnishes the details in "
  "Form 4 as soon as he acquires one. Clause (b) requires any subsequent change in the size of the family to be "
  "communicated, including the marriage of a child.",
  "Form 4 on acquiring a family, and on every later change.",
  "Rule 50(15)(a) and (b), CCS (Pension) Rules, 2021",
  "Deferring the obligation to retirement", covers=["50(15)(a)(i)", "50(15)(b)"])

Q("CU-023", "X", "76", "Rule 76", "Provisional family pension",
  "Where a Government servant dies in service and the family pension case cannot be finalised, provisional "
  "family pension is sanctioned:",
  "by the Head of Office, and it continues until the final amount is determined",
  ("by the Accounts Officer, after the Pension Payment Order issues",
   "The Head of Office sanctions; the Accounts Officer authorises the final pension."),
  ("only on the orders of the Secretary of the Ministry",
   "No such sanction is required."),
  ("for a maximum of six months in every case",
   "The period may be extended with the approval of the Head of Department."),
  "Rule 76 provides for provisional family pension so that the family is not left without support while the "
  "final authorisation is under process. The Head of Office sanctions it, and rule 76(2) allows the period to be "
  "extended on the case being submitted to the Head of Department. The order of 29 October 2026 restates the "
  "mechanism.",
  "Sanctioned by the Head of Office, extended through the Head of Department.",
  "Rule 76, CCS (Pension) Rules, 2021",
  "Waiting for final authorisation before paying anything", covers=["76(1)"], version="A-2026-08")

Q("CU-024", "VIII", "50", "Rule 50(2)(a)(iv)", "Enhanced family pension ceiling",
  "The enhanced rate of family pension is subject to a maximum of:",
  "one lakh twenty-five thousand rupees a month",
  ("seventy-five thousand rupees a month",
   "That is the maximum for the ordinary rate."),
  ("one lakh rupees a month",
   "That figure belongs to an earlier pay commission cycle."),
  ("two lakh rupees a month",
   "No order has raised the family pension ceiling beyond one lakh twenty-five thousand."),
  "Rule 50(2)(a)(i) fixes the ordinary rate at thirty per cent of pay subject to a minimum of nine thousand and "
  "a maximum of seventy-five thousand rupees a month. Sub-clause (iv) applies a minimum of nine thousand and a "
  "maximum of one lakh twenty-five thousand rupees a month to the enhanced rate under sub-clause (ii) or "
  "(iii). The order of 29 October 2026 confirms both figures are current.",
  "Ordinary ceiling seventy-five thousand; enhanced ceiling one lakh twenty-five thousand.",
  "Rule 50(2)(a)(iv), CCS (Pension) Rules, 2021",
  "Confusing the two ceilings", covers=["50(2)(a)(iv)"], version="A-2026-03")

# --------------------------------------------------------------- procedure orders
Q("CU-025", "XIV", "85", "O.M. 03.03.2023", "NPS to CCS coverage",
  "A Central Government civil employee appointed in 2005 against a post advertised in 2003 asks to be covered by "
  "the CCS (Pension) Rules instead of the National Pension System. That is possible:",
  "under the one-time option in the order of 3 March 2023, where the post was advertised on or before 22 December 2003",
  ("in no case, since posts after 31 December 2003 are outside the Rules",
   "The order of 3 March 2023 creates a one-time option that reaches such cases."),
  ("on a fresh recruitment against a pre-2004 vacancy",
   "The option attaches to the post and the individual, not to a fresh appointment."),
  ("by an order of the appointing authority in each case, at its discretion",
   "The option is exercised by the employee and considered by the appointing authority under the order."),
  "The notification of 22 December 2003 introduced the National Pension System, and the rules were amended on "
  "30 December 2003 so that they ceased to apply to persons appointed after 31 December 2003. The Department's "
  "order of 3 March 2023 gives a one-time option to a central civil employee appointed against a post advertised "
  "or notified on or before 22 December 2003, who is covered by the NPS on joining, and provides for the option "
  "to be placed before the appointing authority. The option, once exercised, is final.",
  "One-time option for pre-22.12.2003 vacancies, under the 2023 order.",
  "DoP&PW O.M. No. 57/05/2021-P&PW(B) dated 03.03.2023",
  "Treating the date of appointment as the date that matters", covers=["2"])

Q("CU-026", "VII", "44", "Rule 44(1)", "Minimum pension today",
  "The minimum pension payable under rule 44(1) is:",
  "nine thousand rupees per month",
  ("three thousand five hundred rupees per month",
   "That was the figure under the Fourth Pay Commission and is long superseded."),
  ("seven thousand rupees per month",
   "Six thousand was the figure at an earlier stage of the Seventh Pay Commission; it was raised to nine thousand."),
  ("twelve thousand rupees per month",
   "No such minimum appears in the rule."),
  "Rule 44(1) fixes pension at fifty per cent of emoluments or average emoluments, whichever is more beneficial, "
  "subject to a minimum of nine thousand rupees and a maximum of one lakh twenty-five thousand rupees per "
  "month. Neither limit has been revised by any subsequent order in the register on this platform.",
  "Nine thousand minimum, one lakh twenty-five thousand maximum.",
  "Rule 44(1), CCS (Pension) Rules, 2021",
  "Quoting a pre-2016 minimum", covers=["44(1)"])

Q("CU-027", "X", "62", "Rule 62(4)", "Sanction of provisional pension",
  "Sanction of provisional pension in a superannuation case must issue:",
  "not later than ten days after the date of retirement",
  ("within one month of the date of retirement",
   "One month applies where the retirement is otherwise than on superannuation."),
  ("within three months of the date of retirement",
   "Three months is the interest trigger under rule 65, not the sanction deadline."),
  ("on the date of retirement, together with the Pension Payment Order",
   "The rule sets a deadline after retirement."),
  "Rule 62(4) requires a sanction for provisional pension to issue not later than ten days after the date of "
  "retirement in a case of retirement on superannuation, and within one month from the date of submission of "
  "the forms where the retirement is otherwise than on superannuation. Rule 65(1) then makes interest payable "
  "at the General Provident Fund rate where the sanction or payment is delayed for administrative reasons.",
  "Ten days on superannuation, one month otherwise.",
  "Rule 62(4), CCS (Pension) Rules, 2021",
  "Mixing the sanction deadline with the interest trigger", covers=["62(4)"])

Q("CU-028", "I", "2", "Rule 2 and O.M. 03.03.2023", "Who the Rules apply to",
  "The CCS (Pension) Rules, 2021 apply to a Government servant appointed:",
  "on or before 31 December 2003, subject to the exclusions in rule 2 and the option in the 2023 order",
  ("on any date, whatever the date of appointment",
   "The Rules were confined to persons appointed on or before 31 December 2003."),
  ("after 31 December 2003, if he is not covered by the National Pension System",
   "The converse is the point: post-2003 appointees are under the NPS unless the 2023 option applies."),
  ("only if he was confirmed in his appointment before 2004",
   "Confirmation is not the test in rule 2."),
  "Rule 2 applies the Rules to Government servants appointed on or before 31 December 2003 who are borne on "
  "pensionable establishments, subject to eight exclusions and an Explanation that brings in several further "
  "categories. The order of 3 March 2023 adds a one-time option for a person appointed after that date against a "
  "post advertised on or before 22 December 2003.",
  "Cut-off 31.12.2003, with the 2023 option as the exception.",
  "Rule 2, CCS (Pension) Rules, 2021 and DoP&PW O.M. dated 03.03.2023",
  "Reading the cut-off without the option", covers=["2"])

Q("CU-029", "VIII", "50", "Rule 50(10)", "Dependent parents",
  "Family pension to dependent parents is payable:",
  "for life, if the parents were dependent on the Government servant immediately before his death",
  ("for ten years from the date of death",
   "No such period applies to parents."),
  ("to the father in every case, as the head of the family",
   "Rule 50(10)(b) gives it to the mother failing which to the father."),
  ("only if there is no widow and no child, and no dependent sibling",
   "Siblings come after parents, not before."),
  "Rule 50(10)(a) makes family pension payable to the parents for life where the deceased is not survived by a "
  "widow or widower or a child eligible for family pension, or where the widow or widower and all children cease "
  "to be eligible, if the parents were dependent on the Government servant immediately before his or her death. "
  "Clause (b) prefers the mother, and the Explanation deems the parents dependent if their combined income is "
  "less than the minimum family pension plus the dearness relief on it.",
  "Parents after spouse and children; mother first; for life.",
  "Rule 50(10), CCS (Pension) Rules, 2021",
  "Putting the father first", covers=["50(10)(a)", "50(10)(b)"])

Q("CU-030", "VIII", "50", "Rule 50(11)", "Dependent sibling",
  "Family pension to a dependent sibling suffering from a mental or physical disability is payable:",
  "for life, if the sibling was wholly dependent on the Government servant immediately before his death and the disability existed before it",
  ("until the sibling attains twenty-five years",
   "The age limit does not apply to a sibling with a disability."),
  ("for five years, renewable on a fresh medical certificate",
   "The pension is for life; the certificate is annual evidence of continued eligibility."),
  ("only if the sibling is unmarried",
   "Marriage does not disqualify a sibling with a disability, by the same reasoning as rule 50(9)(i)."),
  "Rule 50(11)(a) makes family pension payable to a dependent sibling suffering from a mental or physical "
  "disability, for life, where no widow or widower, child or parent is eligible, and the sibling was wholly "
  "dependent on the Government servant immediately before his or her death. Clause (b) applies the same "
  "disability criteria as rule 50(9)(h) and (i), and its proviso requires the disability to have existed before "
  "the death.",
  "Siblings last in the order, for life, dependency and pre-existing disability required.",
  "Rule 50(11), CCS (Pension) Rules, 2021",
  "Applying the twenty-five year limit to a sibling", covers=["50(11)(a)", "50(11)(b)"])


# --------------------------------------------------- the remaining sub-rules, asked directly
# Sixteen sub-rules were not reached by the text generator because their text ends in a
# colon and is carried by clauses below them. Each is asked here instead.
Q("CU-031", "I", "4", "Rule 4(1)", "Transfer into the Rules",
  "A Government servant is transferred permanently to a service or post to which the CCS (Pension) Rules apply, "
  "from one to which they do not. He:",
  "becomes subject to these rules",
  ("remains under his former pension scheme until he opts",
   "Rule 4(1) applies the rules on permanent transfer; it does not preserve the former scheme."),
  ("is covered only if his former service is counted for pension",
   "Counting is dealt with separately in rule 13 and rule 14."),
  ("must complete five years in the new post before the rules apply",
   "No qualifying period is attached to the transfer itself."),
  "Rule 4(1) provides that a Government servant transferred permanently to a service or post to which these rules "
  "apply from one to which they do not apply becomes subject to these rules. The rule's second sub-rule deals "
  "with the converse transfer, out of the rules, and saves the pension already earned.",
  "Permanent transfer in brings the servant under the Rules.",
  "Rule 4(1), CCS (Pension) Rules, 2021", "Reading in an option or a qualifying period", covers=["4(1)"])

Q("CU-032", "I", "5", "Rule 5(2)", "The last working day",
  "The day on which a Government servant retires, is retired, is discharged or is allowed to resign is treated "
  "as:",
  "his last completed working day, so that pension does not run from it",
  ("a day of duty, so that it counts as qualifying service",
   "Rule 5(2) makes it the last completed working day, which is a different thing."),
  ("the date from which pension begins in every case",
   "Pension begins from the date he ceases to be borne on the establishment, under rule 81."),
  ("excluded from service altogether",
   "The day is not removed from service; it is characterised."),
  "Rule 5(2) provides that the day on which a Government servant retires or is retired or is discharged or is "
  "allowed to resign shall be treated as his last completed working day. Rule 81(1) then makes pension payable "
  "from the date on which he ceases to be borne on the establishment, and rule 81(3) pays pension for the day on "
  "which the recipient dies.",
  "Retirement day is the last completed working day.",
  "Rule 5(2), CCS (Pension) Rules, 2021", "Treating the retirement day as a day of duty", covers=["5(2)"])

Q("CU-033", "I", "9", "Rule 9(1)", "Commercial employment: Group A officers",
  "A pensioner who was a member of a Central Service Group A immediately before retirement wishes to accept "
  "commercial employment within one year. He must:",
  "obtain the previous sanction of the Government",
  ("merely inform the Ministry after accepting the employment",
   "Rule 9(1) requires previous sanction, not information afterwards."),
  ("wait out the year, since permission cannot be given before it ends",
   "Permission may be given, and must be sought, before the employment is accepted."),
  ("apply to the Union Public Service Commission directly",
   "The Commission is consulted in some cases; the application goes to the Government."),
  "Rule 9(1) requires a pensioner who, immediately before retirement, was a member of a Central Service Group A, "
  "and who wishes to accept commercial employment before the expiry of one year from the date of retirement, to "
  "obtain the previous sanction of the Government. Rule 9(2) provides that sanction is not to be refused except "
  "on specified grounds, and rule 9(7) gives a right to a reasoned order and a review after thirty days.",
  "Previous sanction of the Government, within one year.",
  "Rule 9(1), CCS (Pension) Rules, 2021", "Substituting intimation for sanction", covers=["9(1)"])

Q("CU-034", "I", "9", "Rule 9(7)", "Refusal of permission",
  "Where the Government refuses permission for commercial employment or grants it subject to conditions, the "
  "applicant:",
  "may, within thirty days of receipt of the order, ask for the reasons and for a review of the order",
  ("has no remedy under the Rules",
   "Rule 9(7) creates the remedy."),
  ("may appeal to the Union Public Service Commission",
   "The Commission may be consulted in the review; the request goes to the Government."),
  ("must wait one year before applying again",
   "The rule provides a review, not a waiting period."),
  "Rule 9(7) provides that where the Government grants the permission subject to conditions or refuses it, the "
  "applicant may, within thirty days of the receipt of the order, request the Government to furnish the reasons "
  "for the order and to review it.",
  "Thirty days to seek reasons and a review.",
  "Rule 9(7), CCS (Pension) Rules, 2021", "Treating the refusal as final", covers=["9(7)"])

Q("CU-037", "III", "31", "Rule 31(6)", "Pay on deputation",
  "Pay drawn by a Government servant while on deputation to an ex-cadre post in another Department, or to the "
  "Armed Forces of India, is treated as emoluments:",
  "for the purpose of calculating pension and gratuity",
  ("only if the deputation was outside India",
   "No such condition appears in the sub-rule."),
  ("not at all, since emoluments mean the pay of the parent post",
   "The sub-rule brings deputation pay in as emoluments."),
  ("only if the borrowing Department bears the pension liability",
   "The rule concerns the pay reckoned, not who pays."),
  "Rule 31(6) provides that pay drawn by a Government servant while on deputation to an ex-cadre post in the "
  "same or some other Department of the Government, or to the Armed Forces of India, shall be treated as "
  "emoluments for the purpose of calculating pension and gratuity.",
  "Deputation pay counts as emoluments.",
  "Rule 31(6), CCS (Pension) Rules, 2021", "Reckoning only the parent post pay", covers=["31(6)"])

Q("CU-038", "V", "35", "Rule 35(3)", "Relieving order on absorption",
  "A Government employee joins a State Government on immediate absorption. The relieving order is issued:",
  "in Format 5, and it must indicate the period within which he is to join the State Government",
  ("in Form 5, which is the family details form",
   "Format 5 and Form 5 are different instruments; absorption uses the Format."),
  ("orally, with the period confirmed by the State Government",
   "The rule requires a written order in Format 5."),
  ("only after he joins the State Government",
   "The order precedes the joining and fixes the period for it."),
  "Rule 35(3) requires the relieving order, in a case of immediate absorption, to be issued in Format 5, "
  "indicating the period within which the Government servant shall join the State Government. Its proviso allows "
  "the relieving authority to extend that period for reasons beyond the servant's control, recorded in writing.",
  "Format 5, with the joining period stated.",
  "Rule 35(3), CCS (Pension) Rules, 2021", "Confusing Format 5 with Form 5", covers=["35(3)"])

Q("CU-039", "V", "36", "Rule 36(5)", "Joining period on absorption in a body",
  "Where a Government servant is absorbed in a corporation, company or body, the relieving order:",
  "indicates the period within which he must join, which the relieving authority may extend for reasons beyond his control",
  ("fixes no period, the matter being left to the corporation",
   "The order must state the period."),
  ("must be issued in Form 6-A after the 2024 amendment",
   "Form 6-A is the pension application form, not the relieving order."),
  ("is unnecessary where the absorption is on immediate absorption basis",
   "Rule 36(4) and (5) apply precisely to that case."),
  "Rule 36(5) provides that the relieving order shall indicate the period within which the Government servant "
  "shall join the Corporation or Company or the Body, and its proviso allows the relieving authority to extend "
  "that period for reasons beyond the servant's control, recorded in writing.",
  "The relieving order states a period, extendable on record.",
  "Rule 36(5), CCS (Pension) Rules, 2021", "Leaving the joining period unstated", covers=["36(5)"])

Q("CU-040", "V", "39", "Rule 39(1)", "Invalidation and the 2016 Act",
  "Where a Government servant acquires a disability to which section 20 of the Rights of Persons with "
  "Disabilities Act, 2016 applies, his case is governed by:",
  "the provisions of that Act, read with these rules",
  ("these rules alone, the Act applying only to private employment",
   "Rule 39(1) expressly defers to the Act."),
  ("the CCS (Extraordinary Pension) Rules, 1939 in every case",
   "Those Rules apply to a different class of case."),
  ("the National Pension System rules",
   "The NPS rules govern post-2003 appointees."),
  "Rule 39(1) provides that the case of a Government servant acquiring a disability, where the provisions of "
  "section 20 of the Rights of Persons with Disabilities Act, 2016 are applicable, shall be governed by the "
  "provisions of that Act, read with these rules.",
  "Section 20 of the 2016 Act governs, read with the Rules.",
  "Rule 39(1), CCS (Pension) Rules, 2021", "Applying the Rules alone", covers=["39(1)"])

Q("CU-041", "V", "41", "Rule 41(1)", "Dismissal and forfeiture",
  "A Government servant dismissed or removed from service under the CCS (CCA) Rules:",
  "forfeits his pension and gratuity",
  ("retains his pension but forfeits gratuity",
   "Rule 41(1) forfeits both."),
  ("retains both, subject to a reduction ordered by the President",
   "Forfeiture is automatic; rule 41(2) allows a compassionate allowance in deserving cases."),
  ("forfeits only the portion attributable to the period after the misconduct",
   "The forfeiture is of pension and gratuity, not of a period."),
  "Rule 41(1) provides that a Government servant who is dismissed or removed from service shall forfeit his "
  "pension and gratuity. The rule then allows the authority competent to dismiss or remove him to sanction a "
  "compassionate allowance in a deserving case, and rule 44(5) fixes its ceiling at two-thirds of the pension or "
  "gratuity that would have been admissible.",
  "Dismissal or removal forfeits pension and gratuity; compassionate allowance is the exception.",
  "Rule 41(1), CCS (Pension) Rules, 2021", "Assuming a discretionary reduction rather than forfeiture", covers=["41(1)"])

Q("CU-042", "VI", "43", "Rule 43(2)", "Acceptance of voluntary retirement notice",
  "A notice of voluntary retirement given under rule 43(1):",
  "requires acceptance by the appointing authority",
  ("takes effect on the date stated in it without acceptance",
   "Rule 43(2) requires acceptance, subject to its proviso."),
  ("may be accepted with effect from an earlier date at the authority's discretion",
   "Acceptance cannot advance the date."),
  ("must be accepted within thirty days or it lapses",
   "The rule fixes no such period."),
  "Rule 43(2) provides that the notice of voluntary retirement given under sub-rule (1) shall require acceptance "
  "by the appointing authority. Its proviso deals with the case where the appointing authority does not refuse "
  "the request before the expiry of the notice period, in which case the retirement takes effect on the date of "
  "its expiry.",
  "Acceptance is required; silence until expiry operates as it.",
  "Rule 43(2), CCS (Pension) Rules, 2021", "Treating the notice as self-executing", covers=["43(2)"])

Q("CU-043", "VI", "43", "Rule 43(6)", "Withdrawal of the notice",
  "A Government servant who has given notice of voluntary retirement wishes to withdraw it. He:",
  "is precluded from withdrawing it except with the approval of the appointing authority",
  ("may withdraw it at any time before the date of retirement",
   "Rule 43(6) restricts withdrawal to a case approved by the appointing authority."),
  ("may withdraw it only with the consent of the President",
   "The approving authority is the appointing authority."),
  ("cannot withdraw it in any circumstances",
   "The rule permits withdrawal with approval."),
  "Rule 43(6) provides that a Government servant who has elected to retire under the rule and has given the "
  "necessary notice to that effect to the appointing authority shall be precluded from withdrawing his notice "
  "except with the specific approval of that authority.",
  "Withdrawal needs the appointing authority's specific approval.",
  "Rule 43(6), CCS (Pension) Rules, 2021", "Treating the notice as revocable at will", covers=["43(6)"])

Q("CU-044", "VII", "46", "Rule 46(7)", "Cancelling a nomination",
  "A nomination made under rule 46 may be cancelled:",
  "at any time, by a notice in writing to the Head of Office",
  ("only once, and only with the sanction of the Head of Department",
   "The rule allows cancellation at any time."),
  ("only before retirement",
   "The rule fixes no such limit."),
  ("only by making a fresh nomination, cancellation on its own being ineffective",
   "The proviso requires a fresh nomination to accompany the notice where a family exists, but the notice itself is the operative act."),
  "Rule 46(7) allows a Government servant to cancel a nomination at any time by sending a notice in writing to "
  "the Head of Office. Its proviso requires him, along with the notice, to send a fresh nomination in the "
  "prescribed form where he has a family.",
  "Notice in writing to the Head of Office; a fresh nomination accompanies it.",
  "Rule 46(7), CCS (Pension) Rules, 2021", "Requiring prior sanction", covers=["46(7)"])

Q("CU-045", "X", "66", "Rule 66(2)", "Revision to the disadvantage of the pensioner",
  "Once pension or family pension has been authorised after final assessment, it:",
  "shall not be revised to the disadvantage of the Government servant, except as provided in rules 7 and 8",
  ("may be revised downwards at any time within five years",
   "Rule 66(2) protects the authorised amount."),
  ("may never be revised in either direction",
   "Revision in the pensioner's favour is provided for by rule 66(1)."),
  ("may be revised downwards only on the orders of the President",
   "Rules 7 and 8 are the route, not a general power of revision."),
  "Rule 66(2) provides that, subject to rules 7 and 8, pension or family pension once authorised after final "
  "assessment or revised under sub-rule (1) shall not be revised to the disadvantage of the Government servant, "
  "except in the circumstances the rule sets out. Rule 66(1) allows revision in his favour, and specifies how "
  "an arrear is computed and paid.",
  "No downward revision outside rules 7 and 8.",
  "Rule 66(2), CCS (Pension) Rules, 2021", "Treating the authorised pension as open to any revision", covers=["66(2)"])

Q("CU-046", "XII", "80", "Rule 80(1)", "Authority to pay after sanction",
  "On receipt of the sanction under rule 79 for family pension or residuary gratuity, the Accounts Officer "
  "shall authorise payment:",
  "within one month from the date of receipt of the sanction",
  ("within ten days from the date of receipt of the sanction",
   "Ten days is the Special Seal of Authority step in rule 80(3)."),
  ("within three months from the date of receipt of the sanction",
   "Three months is the interest trigger for delayed gratuity, not the authorisation period."),
  ("without any time limit, the sanction being sufficient authority",
   "The rule fixes a period."),
  "Rule 80(1) requires the Accounts Officer, on receipt of the sanction under rule 79, to authorise the payment "
  "within one month from the date of receipt of the sanction. Its first proviso makes interest payable where "
  "gratuity is delayed beyond three months from the date of submission of the claim for administrative reasons, "
  "and rule 80(3) gives the Central Pension Accounting Office ten days to issue the Special Seal of Authority.",
  "One month to authorise; ten days for the seal; three months for the interest trigger.",
  "Rule 80(1), CCS (Pension) Rules, 2021", "Mixing the one-month and ten-day periods", covers=["80(1)"])


# ------------------------------------------- clauses and provisos the generator cannot reach
# These carry no opening words of their own (a bare list item, a proviso that begins with a
# pronoun) or the list they sit in is too long to offer whole, so each is asked directly.
Q("CU-047", "I", "3", "Rule 3(1)(u)", "Pension Disbursing Authority",
  "Rule 3(1)(u) defines a Pension Disbursing Authority to mean:",
  "a bank selected in consultation with the Reserve Bank of India, a post office, a treasury including a sub-treasury, or an Accounts Officer",
  ("the Central Pension Accounting Office alone",
   "That office issues the Special Seal of Authority; it does not disburse."),
  ("the Head of Office that sanctioned the pension",
   "The Head of Office sanctions and forwards; the disbursing authorities are listed in the definition."),
  ("any bank in which the pensioner holds an account",
   "The bank must be one selected in consultation with the Reserve Bank of India."),
  "Rule 3(1)(u) defines Pension Disbursing Authority by enumeration: a bank selected in consultation with the "
  "Reserve Bank of India, a post office, a treasury including a sub-treasury, or an Accounts Officer. Rule 80(4) "
  "then requires the Pension Disbursing Authority to disburse family pension within fifteen days of receiving the "
  "Special Seal of Authority.",
  "Four kinds of disbursing authority, the bank being a selected bank.",
  "Rule 3(1)(u), CCS (Pension) Rules, 2021", "Treating any bank as a disbursing authority", covers=["3(1)(u)(ii)", "3(1)(u)(iii)", "3(1)(u)(iv)"])

Q("CU-048", "I", "3", "Rule 3(1)(z)", "Treasury",
  "For the purposes of the Rules, 'Treasury':",
  "includes a Sub-Treasury",
  ("excludes a Sub-Treasury, which is a separate office",
   "The definition expressly includes it."),
  ("means only a Treasury in a State capital",
   "No such limitation appears."),
  ("means the Reserve Bank of India acting as banker to the Government",
   "That is a different office, dealt with elsewhere."),
  "Rule 3(1)(z) provides that 'Treasury' includes a Sub-Treasury. The definition matters because rule 3(1)(u) "
  "makes a treasury including a sub-treasury one of the Pension Disbursing Authorities.",
  "'Treasury' includes a Sub-Treasury, and both may disburse.",
  "Rule 3(1)(z), CCS (Pension) Rules, 2021", "Reading the inclusion out of the definition", covers=["3(1)(z)"])

Q("CU-049", "I", "7", "Rule 7(1)(b)", "Retirement benefits after a disciplinary finding",
  "Rule 7 allows the Government to withhold or withdraw retirement benefits where a Government servant is found:",
  "to have been guilty of grave misconduct or negligence during the period of service, including service rendered on re-employment",
  ("to have been inefficient in the discharge of his duties",
   "Inefficiency is dealt with through the disciplinary rules, not rule 7."),
  ("to hold property disproportionate to his known sources of income, in every case",
   "That may found a criminal case; rule 7 speaks of grave misconduct or negligence."),
  ("to have failed to complete the qualifying service stated in his service book",
   "A service-book defect is corrected under rule 57, not rule 7."),
  "Rule 7 deals with the right of the Government to withhold or withdraw pension or gratuity where the pensioner "
  "is found guilty of grave misconduct or negligence during the period of service, including service rendered on "
  "re-employment after retirement. Rule 8 then prescribes the procedure and the authority, as substituted in 2022.",
  "Grave misconduct or negligence during service, including re-employment.",
  "Rule 7(1)(b), CCS (Pension) Rules, 2021", "Widening rule 7 to any inefficiency", covers=["7(1)(b)"])

Q("CU-050", "I", "8", "Rule 8(2)(c)(iii)", "Sanction for proceedings instituted later",
  "A departmental proceeding not instituted while the Government servant was in service:",
  "shall not be instituted after retirement except with the sanction of the authority competent to pass an order under rule 8(1)",
  ("may be instituted by any authority that could have instituted it during service",
   "Rule 8(2)(c) requires the sanction of the competent authority."),
  ("may not be instituted at all after retirement",
   "It may be, with sanction and within the limitations the rule sets."),
  ("may be instituted only by the President",
   "The competent authority under rule 8(1) varies with the appointing authority."),
  "Rule 8(2)(c) provides that a departmental proceeding, if not instituted while the Government servant was in "
  "service, whether before his retirement or during his re-employment, shall not be instituted in respect of a "
  "cause of action which arose more than four years before the institution of the proceeding, and shall not be "
  "instituted save with the sanction of the authority competent to pass an order under rule 8(1).",
  "Later proceedings need the sanction of the rule 8(1) authority and a four-year limit.",
  "Rule 8(2)(c), CCS (Pension) Rules, 2021", "Overlooking the sanction requirement", covers=["8(2)(c)(iii)"])

Q("CU-051", "III", "20", "Rule 20(1)(i)", "Counting military service",
  "Military service rendered before civil employment is counted as qualifying service:",
  "in the case of a re-employed Government servant, on the conditions set out in rule 20",
  ("in every case, without conditions",
   "Rule 20 attaches conditions, including the nature of the discharge."),
  ("never, military service being governed by separate rules",
   "Rule 20 provides for counting it in specified cases."),
  ("only if the military service exceeded five years",
   "No such threshold appears in the sub-rule."),
  "Rule 20 governs the counting of military service towards civil qualifying service. Sub-rule (1) deals with a "
  "person who was re-employed in civil service, and clause (i) with the case where he had rendered military "
  "service before his re-employment, on the conditions the sub-rule sets out, including the character of his "
  "discharge from the military.",
  "Military service counts only on rule 20's conditions.",
  "Rule 20(1)(i), CCS (Pension) Rules, 2021", "Counting military service unconditionally", covers=["20(1)(i)"])

Q("CU-052", "III", "27", "Rule 27(1)(a)", "Interruption in service",
  "Where a Government servant's service is interrupted, rule 27 provides that:",
  "the interruption does not amount to removal or dismissal, and the service rendered before it may be counted on the conditions in the rule",
  ("the earlier service is forfeited in every case",
   "Rule 27 allows it to be counted on conditions."),
  ("the interruption operates as a break in qualifying service unless condoned by the President",
   "The rule's own machinery applies, not a presidential condonation."),
  ("the servant must be reappointed through the Staff Selection Commission",
   "Reappointment procedure is not what rule 27 regulates."),
  "Rule 27 deals with an interruption in the service of a Government servant. Sub-rule (1) provides that the "
  "interruption shall not amount to removal or dismissal within the meaning of rule 11 of the CCS (CCA) Rules, "
  "and clause (a) provides for the counting of the service rendered before the interruption subject to the "
  "conditions in the rule.",
  "An interruption is not a removal, and the earlier service may still count.",
  "Rule 27(1)(a), CCS (Pension) Rules, 2021", "Treating every interruption as forfeiture", covers=["27(1)(a)"])

Q("CU-053", "V", "39", "Rule 39(9)", "Invalidation: the medical board's opinion",
  "Where the medical authority finds the Government servant unfit for further service, the appointing authority:",
  "shall accept the finding and proceed to invalidate him, subject to the proviso",
  ("may retain him in service against the medical finding",
   "The proviso deals only with a specific case, not a general power to disregard the finding."),
  ("must refer the finding to the Union Public Service Commission",
   "No such reference appears in the sub-rule."),
  ("may invalidate him only after a second board confirms it",
   "A second board is not required."),
  "Rule 39(9) deals with the course to be followed where the medical authority declares a Government servant "
  "unfit for further service, and its proviso carves out the case in which the Government servant may be "
  "retained or dealt with otherwise. The invalid pension that follows is calculated under rule 44 with the "
  "concession in the proviso to rule 44(1).",
  "The finding is acted on, subject only to the proviso.",
  "Rule 39(9), CCS (Pension) Rules, 2021", "Reading a general discretion into the proviso", covers=["39(9)#P1"])

Q("CU-054", "VI", "43", "Rule 43(3)(iii)", "Voluntary retirement: the notice period",
  "A notice of voluntary retirement given by a Government servant:",
  "must be given at least three months before the date on which he wishes the retirement to take effect",
  ("may be given one month before that date",
   "Three months is the period in the rule."),
  ("must be given six months before that date",
   "Six months is the rule 57 period for pension papers, not the notice of retirement."),
  ("may be given at any time, the period being fixed by the appointing authority",
   "The rule fixes the period."),
  "Rule 43(3) sets out what the notice of voluntary retirement must contain and the period it must be given "
  "before the intended date. The appointing authority may, under the rule, accept the notice with a shorter "
  "period in a case where it is satisfied that the circumstances justify it.",
  "Three months' notice, and the authority may accept a shorter one.",
  "Rule 43(3), CCS (Pension) Rules, 2021", "Confusing the notice period with the pension-papers period", covers=["43(3)(iii)"])

Q("CU-055", "VII", "45", "Rule 45(6)", "Nominees for death gratuity",
  "Which of the following is the correct order of the family members named in the Explanation to rule 45(6)?",
  "wife or wives including a judicially separated wife; husband; sons; unmarried daughters; widowed or divorced daughters; father; mother; brothers; unmarried, widowed and divorced sisters; married daughters; children of a pre-deceased son",
  ("wife or wives; sons; unmarried daughters; husband; father; mother; married daughters",
   "The husband is placed second, before the sons."),
  ("wife or wives; children; parents; brothers and sisters; children of a pre-deceased son",
   "The Explanation lists the members individually, not by class."),
  ("wife or wives; sons; daughters including married daughters; parents; siblings",
   "A married daughter is placed after the sisters."),
  "The Explanation to rule 45(6) sets out the members of the family for the purposes of rules 45 to 49. The "
  "order it prints is: wife or wives including a judicially separated wife or wives, in the case of a male "
  "Government servant; husband including a judicially separated husband, in the case of a female Government "
  "servant; sons including stepsons and adopted sons; unmarried daughters including stepdaughters and adopted "
  "daughters; widowed or divorced daughters including stepdaughters and adopted daughters; father including "
  "adoptive parents; mother including adoptive parents; brothers including stepbrothers suffering from a "
  "disorder or disability of mind; unmarried sisters, widowed sisters and divorced sisters including "
  "stepsisters; married daughters; and children of a pre-deceased son.",
  "Husband comes second, and a married daughter comes after the sisters.",
  "Rule 45(6) and the Explanation to it, CCS (Pension) Rules, 2021",
  "Assuming married daughters rank with unmarried ones", covers=["45(6)#E1", "45(6)(x)", "45(6)(xi)"])

Q("CU-056", "VII", "46", "Rule 46(4)(i)", "Nomination where the nominee predeceases",
  "A Government servant may provide in his nomination that, in respect of a nominee who predeceases him:",
  "his share shall become payable to the other nominee or nominees named in the nomination",
  ("his share shall fall into the estate of the Government servant",
   "The nomination may direct it to the other nominees instead."),
  ("the nomination shall stand cancelled in its entirety",
   "Clause (ii) deals with invalidity on the nominee's marriage; clause (i) preserves the share for the others."),
  ("his share shall be paid to the Government",
   "Nothing lapses to the Government."),
  "Rule 46(4)(i) allows a Government servant, in his nomination, to provide that in respect of any specified "
  "nominee who predeceases him, the nomination shall become invalid in respect of that nominee and the share "
  "shall become payable to the other nominee or nominees named in the nomination. Its provisos deal with a "
  "nomination made when the servant had no family, and with the case of a single nominee.",
  "The share passes to the other nominees, not to the estate.",
  "Rule 46(4)(i), CCS (Pension) Rules, 2021", "Letting the nomination fail on a nominee's death", covers=["46(4)(i)", "46(4)(i)#P1"])

Q("CU-057", "VII", "47", "Rule 47(1)(b)", "Residuary gratuity: the family members",
  "Where a family pension of a Government servant who was not governed by the Workmen's Compensation Act "
  "becomes payable for a period less than seven years, the residuary gratuity is distributed:",
  "among the surviving members of the family in the order the rule sets out, in the proportions mentioned",
  ("to the estate of the Government servant",
   "Rule 47 distributes it among the family members it names."),
  ("to the nominee named for gratuity, in every case",
   "The nomination operates in a specific situation within rule 47, not always."),
  ("to the spouse alone, in every case",
   "Several classes of family member are provided for."),
  "Rule 47(1)(b) deals with the distribution of the residuary gratuity where the family pension of a Government "
  "servant not governed by the Workmen's Compensation Act becomes payable for less than the period of seven "
  "years. It distributes the amount among the surviving members of the family in the order and proportions the "
  "sub-rule sets out, beginning with the widow or widower and the children, and reaching the more distant "
  "relatives only in default.",
  "Residuary gratuity goes to the family in the rule's order, not to the estate.",
  "Rule 47(1)(b), CCS (Pension) Rules, 2021", "Assuming the estate takes the residuary gratuity", covers=["47(1)(b)(ii)", "47(1)(b)(iii)", "47(1)(b)(iv)"])

Q("CU-058", "VIII", "50", "Rule 50(2)(a)(iii)", "Enhanced family pension after retirement",
  "Where a Government servant dies after retirement, the enhanced rate of family pension is payable:",
  "for seven years or until the pensioner would have attained sixty-seven years, whichever is earlier",
  ("for ten years from the date of death",
   "Ten years applies to a death while in service."),
  ("for seven years, whatever the pensioner's age",
   "The sixty-seven year limit cuts the period short."),
  ("until the family pensioner attains sixty-seven years",
   "The age is the deceased pensioner's, not the family pensioner's."),
  "Rule 50(2)(a)(iii) provides that, in the event of the death of a Government servant after retirement, the "
  "enhanced rate is payable for seven years or until the date on which the deceased Government servant would "
  "have attained sixty-seven years, whichever is earlier. Its first proviso caps the amount at the family pension "
  "admissible under sub-clause (i), and the second deals with the pension authorised on retirement where it was "
  "itself below the ordinary family pension.",
  "Seven years, cut short at the deceased's sixty-seven.",
  "Rule 50(2)(a)(iii), CCS (Pension) Rules, 2021", "Applying the ten-year period to a death after retirement", covers=["50(2)(a)(iii)", "50(2)(a)(iii)#P1"])

Q("CU-059", "VIII", "50", "Rule 50(7)(b)", "Sharing family pension",
  "Where family pension is payable to more than one member of the family at the same time:",
  "it is paid in equal shares, any fraction of a rupee being rounded up, subject to the overall maximum",
  ("it is paid to the eldest in full, who maintains the others",
   "The rule requires equal shares."),
  ("it is paid in the shares entered in the Pension Payment Order, which the Head of Office may vary",
   "Rule 50(7)(b) fixes equal shares."),
  ("it is paid in the proportions the widow or widower decides",
   "The rule does not leave the proportions to a family member."),
  "Rule 50(7)(b) provides that where family pension is payable to more than one member of the family at the "
  "same time it is paid in equal shares, and if a share contains a fraction of a rupee it is rounded off to the "
  "next higher rupee. Its proviso prevents the rounding-up from carrying the total above the maximum prescribed "
  "by the rule: any excess fraction is ignored.",
  "Equal shares, fractions rounded up, total capped at the maximum.",
  "Rule 50(7)(b), CCS (Pension) Rules, 2021", "Rounding up to a total above the ceiling", covers=["50(7)(b)"])

Q("CU-060", "VIII", "50", "Rule 50(9)(j)", "Divorced daughter: proceedings filed during life",
  "A divorce is decreed after the death of the Government servant, but the proceedings were filed during the "
  "lifetime of the servant or his spouse. The divorced daughter's family pension:",
  "is payable from the date of divorce",
  ("is not payable, because the divorce took place after the death",
   "The first proviso saves precisely this case."),
  ("is payable from the date of the servant's death",
   "The pension begins on the divorce, not earlier."),
  ("is payable only if the court so orders",
   "The proviso makes it payable by force of the rule."),
  "The first proviso to rule 50(9)(j)(vi) provides that family pension shall be payable to a divorced daughter "
  "from the date of divorce if the divorce proceedings were filed in a competent court during the lifetime of "
  "the Government servant or pensioner or his or her spouse but the divorce took place after their death. The "
  "second proviso prevents her pension from starting while another eligible member is already drawing it.",
  "From the date of divorce where the proceedings predate the death.",
  "Rule 50(9)(j), first proviso to clause (vi), CCS (Pension) Rules, 2021",
  "Refusing the pension because the decree came later", covers=["50(9)(j)(vi)#P1"])

Q("CU-061", "X", "57", "Rule 57(1)(a)(iv)", "Unverified service: the notice",
  "Where a period of service cannot be verified from the records, the Head of Office:",
  "issues a notice to the Government servant, and if no reply comes within the time allowed, treats the period as not countable",
  ("counts the period in the servant's favour by default",
   "Verification is required; silence in answer to the notice counts against the period."),
  ("refers the matter to the Accounts Officer immediately",
   "The Head of Office first asks the servant."),
  ("reports the servant for a disciplinary offence",
   "The rule provides a notice and a determination, not a penalty."),
  "Rule 57(1)(a)(iv) provides for communication with the Government servant where a period of service is not "
  "capable of being verified from the records, and clause (v) provides that if no response is received within "
  "the time allowed, the Head of Office shall treat the period as not counting as qualifying service, subject "
  "to clause (vi), which allows it to be counted if later found to be admissible.",
  "Notice, then non-counting on silence, provisionally.",
  "Rule 57(1)(a)(iv) and (v), CCS (Pension) Rules, 2021", "Counting unverified service by default", covers=["57(1)(a)(iv)"])

Q("CU-062", "X", "57", "Rule 57(3)(b)", "Where no family member is eligible",
  "Where the Head of Office is satisfied that there is no member of the family eligible to receive family "
  "pension, the pension papers are submitted:",
  "by the gratuity nominee, on the conditions in the proviso",
  ("not at all, until a claimant appears",
   "The rule provides a route through the gratuity nominee."),
  ("by the Head of Office himself, who signs in place of the family",
   "The nominee submits."),
  ("to the Central Pension Accounting Office directly",
   "The papers go through the Head of Office to the Accounts Officer."),
  "Rule 57(3)(b) provides for the case where there is no member of the family eligible to receive family "
  "pension, and its proviso, as substituted by G.S.R. 410(E) dated 16 July 2024, deals with the position where "
  "the form is submitted by the spouse or another member of the family: the Government servant is then not "
  "entitled to commutation until he applies for it himself under the CCS (Commutation of Pension) Rules, 1981.",
  "The gratuity nominee files, and commutation waits for the servant's own application.",
  "Rule 57(3)(b) and its proviso, as substituted by G.S.R. 410(E) dated 16.07.2024",
  "Reading the pre-2024 proviso", covers=["57(3)(b)"], version="A-2024-01")

Q("CU-063", "X", "58", "Rule 58(2)(b)", "Retirement other than on superannuation",
  "A Government servant retiring otherwise than on superannuation submits Form 6-A:",
  "immediately after the competent authority approves the retirement or the retirement takes effect",
  ("six months before the date of retirement",
   "Six months is the superannuation period under rule 57(2)(a)."),
  ("within one month of the Pension Payment Order",
   "The form precedes the order."),
  ("only if the retirement was voluntary",
   "The rule covers every retirement other than on superannuation."),
  "Rule 58(1), as substituted by G.S.R. 410(E), requires a Government servant who is retiring or has retired "
  "for reasons other than superannuation to submit Form 6-A to the Head of Office immediately after the "
  "competent authority has approved the retirement or the retirement has become effective, as the case may be. "
  "Its proviso on commutation mirrors rule 57(3).",
  "Immediately on approval or effect, not six months ahead.",
  "Rule 58(2)(b) and rule 58(1), as substituted by G.S.R. 410(E) dated 16.07.2024",
  "Applying the superannuation timetable", covers=["58(2)(b)"], version="A-2024-01")

Q("CU-064", "X", "62", "Rule 62(3)(b)(i)", "Amount recoverable stated in the sanction",
  "The letter of sanction of provisional pension must specify:",
  "the amount recoverable from the gratuity as assessed under rule 67, and the amount of provisional gratuity after deducting it",
  ("only the amount of provisional pension",
   "The gratuity and the recovery must both be stated."),
  ("the name of the officer responsible for the delay",
   "Responsibility is fixed under rule 65(4), separately."),
  ("the date on which the final pension will be authorised",
   "The rule does not require a forecast date."),
  "Rule 62(3)(b) requires the Head of Office to specify in the letter of sanction the amount recoverable from "
  "the gratuity as assessed under rule 67, and clause (i) requires the amount of provisional pension to be "
  "stated while clause (ii) requires the amount of provisional gratuity after deducting the recovery.",
  "Both figures go into the sanction: the recovery and the net gratuity.",
  "Rule 62(3)(b), CCS (Pension) Rules, 2021", "Omitting the recovery from the sanction", covers=["62(3)(b)(i)"])

Q("CU-065", "X", "63", "Rule 63(1)(d)", "Pension Payment Order and the family",
  "The Pension Payment Order issued by the Accounts Officer must:",
  "include the names of the members of the family eligible for family pension, and the share of each where the pension is shared",
  ("name only the pensioner",
   "Rule 63(1)(d) requires the family members to be named."),
  ("name the family members only if the pensioner asks",
   "The requirement is unconditional."),
  ("leave the family to be added by the Pension Disbursing Authority",
   "The Accounts Officer includes them in the order."),
  "Rule 63(1)(d) requires the Pension Payment Order to include the names of the members of the family eligible "
  "for family pension, and their shares where the family pension is to be shared, for example children from a "
  "wife who is not alive or children from a divorced wife. Rule 79(2)(a)(iv) then allows names to be added later "
  "on the Head of Office's communication.",
  "The order names the eligible family members and their shares.",
  "Rule 63(1)(d), CCS (Pension) Rules, 2021", "Naming only the pensioner", covers=["63(1)(d)", "63(1)(d)#P1"])

Q("CU-066", "XI", "70", "Rule 70(1)(b)", "Recovery of Government dues",
  "Government dues recoverable from the gratuity are recovered:",
  "by the Head of Office, who assesses the dues and adjusts them against the gratuity under the rule",
  ("only by the Accounts Officer, after the Pension Payment Order issues",
   "The Head of Office makes the assessment and the adjustment."),
  ("only with the consent of the pensioner",
   "Certain dues are recovered without consent, as rule 77(1)(x) shows for dearness relief."),
  ("only by a civil court on a suit by the Government",
   "The Rules provide for administrative recovery."),
  "Rule 70 deals with the recovery of Government dues from the gratuity. Sub-rule (1) requires the Head of "
  "Office to assess the dues and, in clause (b), to recover them from the amount of gratuity becoming payable, "
  "with the procedure and the priorities the rule sets out.",
  "Assessment and recovery both sit with the Head of Office.",
  "Rule 70(1)(b), CCS (Pension) Rules, 2021", "Leaving recovery to the Accounts Officer", covers=["70(1)(b)"])

Q("CU-067", "XIII", "84", "Rule 84(1)", "Other rules that apply to payment",
  "The procedure for the payment of gratuity, of pension, of pension undrawn for more than a year, and of "
  "pension in respect of a deceased pensioner is governed by:",
  "the Treasury Rules of the Central Government, save as otherwise provided in these rules",
  ("the General Financial Rules, 2017",
   "Rule 84(1) names the Treasury Rules."),
  ("the Central Civil Services (Commutation of Pension) Rules, 1981",
   "Those Rules govern commutation, under rule 84(2)."),
  ("the Payment of Arrears of Pension (Nominations) Rules, 1983",
   "Those Rules govern nomination for arrears, under rule 84(3)."),
  "Rule 84 applies other rules to the payment of pension. Sub-rule (1) applies the Treasury Rules of the "
  "Central Government to the procedure for payment of gratuity, pension, pension undrawn for more than a year, "
  "and pension in respect of a deceased pensioner; sub-rule (2) applies the CCS (Commutation of Pension) Rules, "
  "1981 to commutation; and sub-rule (3) applies the Payment of Arrears of Pension (Nominations) Rules, 1983 to "
  "nomination for arrears.",
  "Treasury Rules for payment, Commutation Rules for commutation, Arrears Rules for nomination.",
  "Rule 84(1), CCS (Pension) Rules, 2021", "Substituting the General Financial Rules", covers=["84(1)(i)", "84(1)(ii)"])


# ------------------------------------------- rules 11 and 21, with stems of their own
# The corpus already asks these two points in the ordinary way; these versions are framed
# from the proviso side, which is a different question and reaches a different provision.
Q("CU-068", "III", "11", "Rule 11 and its provisos", "Service before the age of eighteen",
  "A person appointed at seventeen years of age. The service rendered before he attained eighteen:",
  "does not count as qualifying service, except in the case of military service counted for civil pension under rule 20",
  ("counts in full, because service is service",
   "The second proviso to rule 11 excludes it."),
  ("counts from the date of his first increment",
   "No such rule exists."),
  ("counts only if he was confirmed before he turned eighteen",
   "Confirmation is not the test; the age is."),
  "Rule 11 makes qualifying service commence from the date the Government servant takes charge of the post to "
  "which he is first appointed, substantively or in an officiating or temporary capacity. The first proviso "
  "requires officiating or temporary service to be followed without interruption by substantive appointment, and "
  "the second proviso excludes service rendered before the age of eighteen, except in the case of military "
  "service counted for civil pension under rule 20.",
  "Boy service is excluded by the second proviso, military service being the exception.",
  "Rule 11, second proviso, CCS (Pension) Rules, 2021",
  "Counting service rendered before eighteen", covers=["11", "11#P1"])

Q("CU-069", "III", "21", "Rule 21 and its proviso", "Extraordinary leave other than on medical certificate",
  "Extraordinary leave granted because the servant could not rejoin duty on account of civil commotion counts "
  "as qualifying service:",
  "only where the appointing authority so directs at the time of granting it",
  ("automatically, civil commotion being a cause beyond his control",
   "The proviso requires a direction."),
  ("never, whatever the cause",
   "The proviso allows the direction in this and one other case."),
  ("if he produces a certificate from the district magistrate after rejoining",
   "The rule turns on the direction at the time of grant, not on later evidence."),
  "Rule 21 counts all leave for which leave salary is payable and all extraordinary leave granted on medical "
  "certificate without any order. Its proviso allows the appointing authority, at the time of granting other "
  "extraordinary leave, to direct that it count as qualifying service where the Government servant could not "
  "join or rejoin duty because of civil commotion, or was prosecuting higher scientific and technical studies.",
  "Commotion EOL counts only on a direction given when it was granted.",
  "Rule 21, proviso, CCS (Pension) Rules, 2021",
  "Treating civil commotion as an automatic ground", covers=["21", "21#P1"])
