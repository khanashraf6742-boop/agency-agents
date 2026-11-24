"""Chapter II: regulation of claims, conditions, good conduct, withholding,
commercial employment, employment under a Government outside India."""
from authoring import Q

# ---------------------------------------------------------------- rule 5
Q("P-0011", 5, "II", "5(1)",
  "A servant retires on 31 May 2024. His pension claim falls to be decided by the rules in force:",
  ("on that date, not on the date the claim is settled",
   "Rule 5(1) fixes the governing rules by the date of retirement, not the date of decision"),
  [("on the date the Head of Office forwards the case",
    "Processing dates do not change the rule that governs the claim"),
   ("on the date the Accounts Officer authorises the pension",
    "Authorisation is a later step and does not select the governing rules"),
   ("on whichever date is more beneficial to the servant",
    "No such choice is given by rule 5")],
  "Rule 5(1) provides that any claim to pension or family pension shall be regulated by the provisions in "
  "force at the time when the Government servant retires, is retired, is discharged, is allowed to resign, or "
  "dies, as the case may be. The governing law is therefore frozen at the event, not at the administrative "
  "stage. That matters whenever the rules are amended: an amendment after retirement changes the position for "
  "those who retire after it, and does not reopen a case already governed by the earlier text unless the "
  "amending instrument itself says otherwise.",
  "Applying whatever version of the rules is current when the file is decided")

Q("P-0012", 5, "II", "5(2)",
  "A servant's last working day was 30 June and he died on 2 July while on leave. For the purposes of these rules his date of death is treated as:",
  ("a completed working day, and the day falls within his leave",
   "Rule 5(2) treats death as a completed working day and the proviso keeps the day within the leave"),
  [("outside service altogether, so no death gratuity is payable to the family",
    "Treating the day as a completed working day puts it inside service"),
   ("the last day of the month, by deeming",
    "The rule deems the day of death, not a month-end"),
   ("irrelevant, because he had already retired",
    "He had not retired; retirement on superannuation and death in service are different events")],
  "Rule 5(2) treats the day of retirement, discharge, resignation or death as the last completed working day. "
  "Its proviso deals with a servant who, immediately before retirement or death, was absent on leave or "
  "otherwise, or under suspension: the day of retirement or death is part of that leave, absence or "
  "suspension. The effect is that the day counts for service purposes without being converted into duty. A "
  "candidate who reads the main clause alone will treat the day as duty; a candidate who reads the proviso "
  "alone may think it does not count at all.",
  "Reading the deeming clause without its proviso")

# ---------------------------------------------------------------- rule 6
Q("P-0013", 6, "II", "6(1)",
  "A servant completes twenty-two years, retires, and is re-employed the next day in another Ministry. He later claims a second pension for the re-employed period. Under rule 6(1) he:",
  ("cannot earn two pensions for the same continuous service",
   "Rule 6(1) bars two pensions in the same service or post at the same time or by the same continuous service"),
  [("is entitled to a second pension because the post is different",
    "The bar operates on continuous service, and a change of post does not break it"),
   ("is entitled to a second pension because there was a fresh appointment",
    "Rule 6(2) addresses re-employment and does not create a second pension"),
   ("forfeits the first pension on re-employment",
    "The rule bars a second pension; it does not take away the first")],
  "Rule 6(1) is a short, absolute provision: a Government servant shall not earn two pensions in the same "
  "service or post at the same time or by the same continuous service. Rule 6(2) then deals with the "
  "re-employed pensioner and provides that, except as provided in rule 19 or rule 20, he is not entitled to a "
  "separate pension or gratuity for the period of re-employment. The two together mean that a re-employed "
  "pensioner draws his original pension but does not build a second one, subject to the specific counting "
  "provisions in rules 19 and 20.",
  "Assuming a new appointment necessarily starts a new pension")

Q("P-0014", 6, "II", "6-Explanation-2",
  "A servant resigns from a public sector undertaking with its permission to join the Government in 2002. On retirement from Government service he claims pension from the Government for his PSU years. That claim:",
  ("fails, because the PSU bears its own pension liability",
   "Explanation 2 to rule 6 puts the PSU pension on the PSU and disclaims Government liability"),
  [("succeeds, because he joined with proper permission",
    "Proper permission protects his Government pension; it does not shift the PSU liability"),
   ("succeeds, because the two periods together exceed the minimum service",
    "Aggregation is dealt with in rule 19, not by shifting liability"),
   ("fails, because service in a PSU is never counted",
    "It may be counted under rule 19; what fails here is the claim against the Government for it")],
  "The first proviso to rule 6(2) allows a servant who came from an autonomous body or public sector "
  "undertaking with proper permission on or before 31 December 2003 to receive pension and gratuity for the "
  "Government service in addition to anything received from the body. Explanation 2 then fixes where each "
  "liability sits: pension on account of the PSU service is paid by the PSU itself, and the Government bears "
  "no liability for it. So the servant keeps both, but each is paid by the employer whose service gave rise "
  "to it. The second proviso caps the combined gratuity at what would have been admissible on the whole "
  "service.",
  "Reading 'proper permission' as making the Government liable for the earlier service")

# ---------------------------------------------------------------- rule 7
Q("P-0015", 7, "II", "7(1)(b)",
  "A pensioner is found guilty of grave misconduct. The Appointing Authority proposes to withhold part of his pension. The reduction must not take the pension below:",
  ("the minimum pension under rule 44",
   "The first proviso to rule 7(1)(b) sets that floor"),
  [("half of his last emoluments",
    "No such floor appears in rule 7"),
   ("the family pension admissible to his widow",
    "Family pension is a separate entitlement under rule 50"),
   ("the amount of gratuity he received",
    "Gratuity is a lump sum and is not a floor for pension")],
  "Rule 7(1)(b) allows the Appointing Authority, by order in writing, to withhold or withdraw a pension or "
  "part of it, permanently or for a specified period, where the pensioner is convicted of a serious crime or "
  "found guilty of grave misconduct. The first proviso fixes a floor: where a part of the pension is withheld "
  "or withdrawn, the amount shall not be reduced below the minimum pension under rule 44. The second proviso "
  "requires consultation with the Union Public Service Commission before final orders. The distinction worth "
  "holding is between reducing a pension, which is capped in effect by that floor, and withholding it "
  "entirely, which the rule also permits in a suitable case.",
  "Assuming a part-withholding can reduce the pension to nothing")

Q("P-0016", 7, "II", "7(3)(a)",
  "Where a pensioner is prima facie guilty of grave misconduct but has not been convicted by a court, he must be given a notice. The period allowed to him for representation is:",
  ("fifteen days, extendable by up to fifteen more",
   "Rule 7(3)(a) fixes fifteen days, with further time not exceeding fifteen days"),
  [("thirty days, extendable without limit",
    "Thirty days is the period for a representation under rule 9(7), a different provision"),
   ("ten days, with no extension",
    "Neither the period nor the bar on extension is right"),
   ("such period as the Appointing Authority thinks fit",
    "The rule fixes the period and caps the extension")],
  "Rule 7(3) applies where the case does not fall under rule 7(2), that is, where there is no conviction by a "
  "court. Before passing an order the authority must serve a notice specifying the proposed action and the "
  "ground for it, calling on the pensioner to submit a representation within fifteen days of receipt or such "
  "further time, not exceeding fifteen days, as the authority allows, and must then take that representation "
  "into consideration. The structure is a compact natural-justice code: notice, a fixed opportunity, and a "
  "duty to consider what comes back.",
  "Confusing the rule 7 notice period with the rule 9 representation period")

Q("P-0017", 7, "II", "7(2)",
  "A pensioner is convicted of a serious crime by a court. Before taking action under rule 7(1) the authority should:",
  ("act in the light of the court's judgment on the conviction",
   "Rule 7(2) directs the authority to take action in the light of that judgment"),
  [("conduct a fresh departmental enquiry into the same conduct",
    "Rule 7(2) routes the authority to the judgment rather than to a fresh enquiry"),
   ("wait for the appeal period to expire in every case",
    "No such waiting period appears in rule 7(2)"),
   ("ignore the conviction unless it is for an offence under the Official Secrets Act",
    "The Act is one example within 'serious crime', not the only route")],
  "Rule 7(2) deals with the case where a pensioner is convicted of a serious crime by a court of law and "
  "directs that action under sub-rule (1) shall be taken in the light of the judgment of the court relating to "
  "that conviction. Rule 7(3) is expressly the 'case not falling under sub-rule (2)', which is why the notice "
  "procedure does not apply to a convicted pensioner: the court has already found the facts. The Explanation "
  "defines serious crime to include an offence under the Official Secrets Act, 1923, and grave misconduct to "
  "include disclosure of secret material.",
  "Running the sub-rule (3) notice procedure against a convicted pensioner")

# ---------------------------------------------------------------- rule 8
Q("P-0018", 8, "II", "8(1)",
  "Before the President passes final orders withholding a pension under rule 8, he must consult:",
  ("the Union Public Service Commission",
   "The first proviso to rule 8(1) requires that consultation"),
  [("the Comptroller and Auditor-General",
    "The C&AG is the withholding authority for the Indian Audit and Accounts Department, not a consultee here"),
   ("the Department of Personnel and Training",
    "No consulting role is given to the Department by rule 8"),
   ("the pensioner's last Head of Department",
    "The Head of Department processes the case; he is not the consultee")],
  "Rule 8(1) reserves to the President the right to withhold or withdraw a pension or gratuity, in full or in "
  "part, and to order recovery of pecuniary loss, where in departmental or judicial proceedings the pensioner "
  "is found guilty of grave misconduct or negligence. The first proviso requires consultation with the Union "
  "Public Service Commission before final orders; the second fixes the same floor as rule 7, that a part "
  "withholding cannot take the pension below the minimum under rule 44. G.S.R. 770(E) of 7 October 2022 "
  "substituted sub-rule (1) so that the power is exercised by the President only where the President is the "
  "appointing authority, and otherwise by the Secretary of the administrative Ministry or Department.",
  "Treating the UPSC as an appellate body rather than a consultee")

Q("P-0019", 8, "II", "8(2)(c)(ii)",
  "Departmental proceedings are instituted after retirement over an event that occurred five years earlier. They are:",
  ("not permissible: the event is outside the four-year limit in rule 8(2)(c)(ii)",
   "Rule 8(2)(c)(ii) bars proceedings over an event more than four years before institution"),
  [("permissible, because there is no time limit",
    "The four-year bar in clause (c)(ii) is a time limit"),
   ("permissible, because the pensioner can always be heard",
    "Hearing the pensioner does not cure the time bar"),
   ("permissible if the President sanctions them in Format 2",
    "The sanction in Format 2 is a separate requirement and does not displace the four-year bar")],
  "Where departmental proceedings were not instituted while the servant was in service, rule 8(2)(c) imposes "
  "three conditions: they may not be instituted save with the sanction of the President in Format 2; they may "
  "not concern an event that took place more than four years before institution; and they must be conducted by "
  "such authority and place as the President directs, following the procedure applicable to proceedings in "
  "which dismissal could be ordered. The proviso requires a memorandum of charges in Format 3. The three "
  "conditions are cumulative, so a valid sanction does not rescue a proceeding that is out of time.",
  "Thinking a presidential sanction cures the four-year bar")

Q("P-0020", 8, "II", "8(2)(b)",
  "Proceedings were started against a servant under rule 16 of the CCS (Classification, Control and Appeal) Rules, 1965 while he was in service and continued after retirement. Their effect on his pension is:",
  ("none at all: clause (b) says they have no effect on pension or gratuity",
   "Clause (b) expressly disapplies the withholding regime to rule 16 proceedings"),
  [("the pension is withheld until they conclude",
    "That is the position for other proceedings, not for rule 16 proceedings"),
   ("the pension is reduced to provisional pension",
    "Provisional pension under rule 8(3) does not attach to rule 16 proceedings"),
   ("the pension is forfeited if the finding is against him",
    "Clause (b) removes the pension consequence altogether")],
  "Rule 8(2)(b) begins with a non obstante formula: notwithstanding sub-rule (1) and clause (a), departmental "
  "proceedings instituted under rule 16 of the CCA Rules, 1965 while the servant was in service and continued "
  "after retirement shall have no effect on the pension and gratuity of the pensioner. The reason is that rule "
  "16 proceedings concern minor penalties, which do not carry the pension consequences that rule 8 exists to "
  "enforce. Compare clause (a), which continues proceedings begun while in service and treats them as "
  "proceedings under rule 8, and sub-rule (3), which brings in provisional pension.",
  "Extending the withholding regime to minor-penalty proceedings")

Q("P-0021", 8, "II", "8(3),8(4)(a)",
  "A servant against whom departmental proceedings are instituted retires on superannuation. He is sanctioned provisional pension equal to:",
  ("the maximum pension admissible up to the date of retirement",
   "Rule 8(4)(a) fixes provisional pension at the maximum admissible on that service"),
  [("fifty per cent of his last pay",
    "That is the ordinary pension rate, not the provisional figure"),
   ("the minimum pension under rule 44",
    "The minimum is a floor, not the measure of provisional pension"),
   ("the family pension admissible to his family",
    "Family pension is separately provided for in rule 51 and rule 50")],
  "Rule 8(3) requires a provisional pension to be sanctioned where a servant who has retired is faced with "
  "departmental or judicial proceedings, or where rule 14 CCA proceedings are continued under sub-rule (2). "
  "Rule 8(4)(a) measures it: the Accounts Officer authorises provisional pension equal to the maximum pension "
  "that would have been admissible on qualifying service up to the date of retirement, or, if he was under "
  "suspension on that date, up to the date immediately preceding suspension. The generosity is deliberate: the "
  "servant is presumed entitled to the best figure until the proceedings produce a reason to reduce it.",
  "Using the ordinary rate instead of the maximum admissible")

Q("P-0022", 8, "II", "8(4)(c)",
  "A servant retires with proceedings pending. As regards his gratuity, rule 8(4)(c) provides that:",
  ("no gratuity at all until the proceedings conclude and final orders issue",
   "Clause (c) withholds gratuity until that point"),
  [("gratuity is paid in full with the provisional pension",
    "The rule withholds it, which is the contrast with provisional pension"),
   ("gratuity is paid at half the admissible amount",
    "No partial release is provided for"),
   ("gratuity is forfeited on retirement",
    "It is withheld pending the outcome, not forfeited")],
  "The structure of rule 8(4) is that pension and gratuity are treated differently while proceedings are "
  "pending. Provisional pension is paid, at the maximum admissible rate, from the day after retirement until "
  "final orders. Gratuity, by contrast, is withheld entirely: clause (c) provides that no gratuity shall be "
  "paid until the proceedings conclude and final orders are issued. That is why the two are spoken of "
  "separately throughout the pension-processing rules, and why rule 62 provides separately for provisional "
  "gratuity in cases that do not involve proceedings at all.",
  "Assuming pension and gratuity are always treated alike while proceedings pend")

Q("P-0023", 8, "II", "8(4)(d)",
  "Allegations of misconduct are under investigation but no proceedings have been instituted by the date of retirement. The pension and gratuity:",
  ("are paid under rule 63, subject to later proceedings under rule 8(2)",
   "Clause (d) releases them, with the proviso preserving the effect of sub-rule (2)"),
  [("are withheld until the investigation ends",
    "Clause (d) disapplies the withholding regime in exactly this situation"),
   ("are paid as provisional pension only",
    "Provisional pension under sub-rule (4) is what clause (d) disapplies"),
   ("are forfeited if the investigation later finds misconduct",
    "The proviso routes any later proceedings through sub-rule (2); forfeiture is not automatic")],
  "Rule 8(4)(d) is the safety valve in the scheme. Where allegations of misconduct are still under "
  "investigation, or proceedings are merely contemplated and have not been instituted or deemed instituted, on "
  "the date of retirement, the provisions of sub-rule (4) do not apply, and the pension and gratuity are "
  "authorised on retirement in accordance with rule 63. Its proviso keeps the door open: any departmental "
  "proceedings instituted after retirement remain subject to sub-rule (2), including the four-year bar and the "
  "requirement of presidential sanction. The policy is that a servant is not left unpaid merely because an "
  "investigation is in the air.",
  "Withholding benefits because an investigation is merely on foot")

Q("P-0024", 8, "II", "8(5)",
  "Provisional pension of \u20b940,000 was paid for two years. The final pension sanctioned is \u20b936,000. The recovery of the excess is:",
  ("not made: the final pension is lower than the provisional pension",
   "Rule 8(5) bars recovery where the final pension is less than the provisional pension"),
  [("made in full from the next pension payment",
    "The rule expressly bars that recovery"),
   ("made at one-third of the pension each month",
    "The one-third rate governs recovery of pecuniary loss under rule 8(6), not adjustment here"),
   ("made by reducing the gratuity",
    "Neither adjustment nor reduction of gratuity is provided for in this situation")],
  "Rule 8(5) provides that provisional pension paid under sub-rule (4) is adjusted against the final "
  "retirement benefits sanctioned on conclusion of the proceedings, but that no recovery shall be made where "
  "the pension finally sanctioned is less than the provisional pension, or where the pension is reduced or "
  "withheld permanently or for a specified period. The rule therefore allows the shortfall to fall on the "
  "Government rather than on the pensioner. That is a deliberate policy choice and is worth contrasting with "
  "the one-third recovery rate in sub-rule (6), which applies to recovery of pecuniary loss, a different kind "
  "of debt.",
  "Recovering an overpayment that the rule excuses")

Q("P-0025", 8, "II", "8(6)",
  "The President decides not to withhold a pension but orders recovery of a pecuniary loss from it. The monthly recovery shall not ordinarily exceed:",
  ("one-third of the pension admissible at retirement",
   "Rule 8(6) caps the instalment at one-third"),
  [("one-half of the pension admissible at retirement",
    "Half is the family pension rate, not this cap"),
   ("ten per cent of the pension",
    "Ten per cent is the withholding in rule 77(1)(vi) for accommodation dues"),
   ("the whole pension, since the loss is Government money",
    "The rule caps the rate; it does not permit the whole pension")],
  "Rule 8(6) deals with the case where the President decides not to withhold or withdraw pension but orders "
  "recovery of pecuniary loss from it. The recovery shall not ordinarily be made at a rate exceeding one-third "
  "of the pension admissible on the date of retirement. The word 'ordinarily' leaves room for an exceptional "
  "case, but the normal ceiling is a third. Two other caps sit nearby in the scheme and are easy to confuse: "
  "the ten per cent withheld under rule 77(1)(vi) pending a no-demand certificate for Government "
  "accommodation, and the one-third here, which concerns recovery of a loss rather than security for a due.",
  "Confusing the one-third recovery cap with the ten per cent accommodation withholding")

Q("P-0026", 8, "II", "8-Explanation(1)(a)",
  "Departmental proceedings are deemed instituted under rule 8 on the date:",
  ("the statement of charges issues, or the earlier date of suspension",
   "Explanation 1(a) fixes the date of the statement of charges, or of earlier suspension"),
  [("the authority first forms a suspicion",
    "Suspicion is not the trigger in the Explanation"),
   ("the pensioner is informed of the proposed penalty",
    "That is a later stage in the proceedings"),
   ("the enquiry officer submits his report",
    "The report comes at the end; institution is at the start")],
  "Explanation 1(a) to rule 8 deems departmental proceedings to be instituted on the date on which the "
  "statement of charges is issued to the servant or pensioner or, if he was placed under suspension from an "
  "earlier date, on that earlier date. The date matters because rule 8(2)(c)(ii) bars post-retirement "
  "proceedings over an event more than four years old, and because the pending-proceedings question in rule "
  "8(4)(d) turns on whether proceedings were instituted by the date of retirement. Explanation 1(b) does the "
  "same work for judicial proceedings: the date of the complaint or police report for criminal proceedings, and "
  "the date the suit is filed for civil proceedings.",
  "Dating institution from the final report rather than the charge sheet")

Q("P-0027", 8, "II", "8-Explanation(4)",
  "'Civil proceedings' in rule 8 has a narrow meaning. It means proceedings in respect of:",
  ("a civil suit filed by the Government only",
   "Explanation 4 confines the expression to suits filed by the Government"),
  [("any civil suit touching the servant's service",
    "A suit by a private party is outside the definition"),
   ("any proceeding in a civil court, including appeals",
    "The definition is confined to suits filed by the Government"),
   ("proceedings under the Contempt of Courts Act",
    "Contempt is not a civil suit filed by the Government")],
  "Explanation 4 to rule 8 provides that the expression civil proceedings means such proceedings in respect of "
  "a civil suit filed by the Government only. That is narrower than it sounds, because it excludes a suit "
  "brought against the Government by a private litigant, even where the subject matter touches the servant's "
  "service. The reason is that rule 8 exists to protect the public purse where the Government is pursuing a "
  "remedy, not to convert private litigation into a ground for withholding a pension. Criminal proceedings are "
  "defined separately in Explanation 1(b)(i) by reference to the complaint or police report.",
  "Treating any civil litigation as civil proceedings under rule 8")

# ---------------------------------------------------------------- rule 9
Q("P-0028", 9, "II", "9(1)",
  "A Group 'A' pensioner wishes to take up commercial employment. He needs the previous sanction of the Government if he proposes to start:",
  ("within one year of his retirement",
   "Rule 9(1) fixes the one-year window by reference to the date of retirement"),
  [("within two years of his retirement",
    "The window is one year, not two"),
   ("at any time after retirement, whenever it begins",
    "The rule is confined to the first year"),
   ("within six months of his retirement",
    "Six months is the election period under rule 4, a different provision")],
  "Rule 9(1) requires a pensioner who was, immediately before retirement, a member of Central Service Group "
  "'A' and who wishes to accept commercial employment before the expiry of one year from the date of "
  "retirement, to obtain the previous sanction of the Government, applying in Form 1. Two provisos matter: a "
  "servant already permitted to take up a particular commercial employment during leave preparatory to "
  "retirement or refused leave needs no further permission to continue it, and a servant may not negotiate for "
  "commercial employment during service without the prior permission of the administrative Ministry or "
  "Department, which is given only for special reasons.",
  "Confusing the one-year window with the six-month election period in rule 4")

Q("P-0029", 9, "II", "9(7)",
  "The Government grants permission under rule 9 subject to conditions the pensioner thinks unreasonable. He may represent against the conditions within:",
  ("thirty days of receiving the order",
   "Rule 9(7) allows thirty days from receipt of the order"),
  [("fifteen days of receiving the order",
    "Fifteen days is the notice period in rule 7(3)(a)"),
   ("ninety days of receiving the order",
    "No ninety-day period appears in rule 9"),
   ("one year from the date of retirement",
    "The one-year period governs when sanction is needed, not when a representation is made")],
  "Rule 9(7) gives an applicant whose permission is granted subject to conditions, or refused, thirty days from "
  "receipt of the order to make a representation, and allows the Government to pass such orders as it thinks "
  "fit. Its proviso protects the pensioner: no order other than one cancelling the condition or granting "
  "permission without conditions may be made without giving him an opportunity to show cause against the order "
  "proposed. So the representation cannot simply be rejected with no hearing: any outcome adverse to him must be "
  "preceded by a show-cause opportunity.",
  "Assuming the representation can be rejected without a hearing")

Q("P-0030", 9, "II", "9(8)",
  "A pensioner takes up commercial employment in the eighth month after retirement without sanction. The Government may:",
  ("declare, for recorded reasons, that he is not entitled to the whole or part",
   "Rule 9(8) authorises that declaration, after a show-cause opportunity"),
  [("recover from him a penalty equal to one full year's pension by way of fine",
    "The rule operates on entitlement, not by a fixed monetary penalty"),
   ("prosecute him for a criminal offence under the rules",
    "Rule 9(8) is an administrative consequence, not a criminal one"),
   ("forfeit his gratuity in addition to the pension",
    "The rule speaks of pension, not gratuity")],
  "Rule 9(8) provides that where a pensioner takes up commercial employment within one year of retirement "
  "without prior permission, or breaches a condition of permission granted, the Government may by order in "
  "writing, for reasons recorded, declare that he shall not be entitled to the whole or such part of the "
  "pension, and for such periods, as may be specified. The first proviso requires an opportunity to show "
  "cause; the second requires the Government to have regard to his financial circumstances, the nature of and "
  "emoluments from the employment, and any other relevant factor. The sanction is therefore proportionate "
  "rather than automatic.",
  "Assuming breach produces an automatic and total forfeiture")

Q("P-0031", 9, "II", "9-Explanation(a)(i)",
  "Which of the following is NOT 'commercial employment' for the purposes of rule 9?",
  ("Employment under a body corporate owned or controlled by the Central Government",
   "The Explanation expressly excludes such employment from the definition"),
  [("A directorship of a company engaged in trading",
    "A directorship is expressly included"),
   ("A partnership in a professional firm",
    "Partnership of such a firm is expressly included"),
   ("Setting up practice as a consultant in matters relatable to official knowledge",
    "This is the second limb of the definition")],
  "The Explanation to rule 9 defines commercial employment in two limbs. The first is employment in any "
  "capacity, including that of an agent, under a company, co-operative society, firm or individual engaged in "
  "trading, commercial, industrial, financial or professional business, and includes a directorship and a "
  "partnership, but expressly does not include employment under a body corporate wholly or substantially owned "
  "or controlled by the Central Government or a State Government. The second limb is setting up practice as an "
  "adviser or consultant in matters where the pensioner lacks professional qualifications and the work is "
  "relatable to his official knowledge, or where his position would give clients an unfair advantage, or where "
  "the work involves liaison with Government offices.",
  "Reading the definition's exclusions as inclusions")

Q("P-0032", 9, "II", "9(3)(b)",
  "In deciding whether to permit commercial employment, the Government must consider whether the officer was privy to sensitive information during:",
  ("the last three years of his service",
   "Rule 9(3)(b) fixes a three-year look-back"),
  [("the last five years of his service before he laid down office",
    "The period is three years, not five"),
   ("his entire service, however long",
    "The clause is confined to the last three years"),
   ("the last year of his service only",
    "One year is the window for sanction, not the look-back for sensitive information")],
  "Rule 9(3) lists the factors to which the Government must have regard in granting or refusing permission. "
  "Clause (b) asks whether the officer has been privy to sensitive or strategic information in the last three "
  "years of his service which is directly related to the areas of interest or work of the organisation he "
  "proposes to join, or the areas in which he proposes to practise or consult. Clause (c) looks to conflict of "
  "interest between the policies of the office he held in those same three years and the interest represented "
  "by the organisation, with an Explanation that normal economic competition is not conflict of interest.",
  "Extending the sensitive-information look-back to the whole of service")

# ---------------------------------------------------------------- rule 10
Q("P-0033", 10, "II", "10",
  "Rule 10 governs a pensioner taking employment under a Government outside India. Its effect is that such employment:",
  ("requires sanction, and the pension may be withheld if taken without it",
   "Rule 10 puts foreign Government employment under sanction and attaches a pension consequence"),
  [("is freely permitted once the pension is sanctioned",
    "The rule imposes a sanction requirement"),
   ("ends the pension from the date of the employment",
    "The consequence is withholding, not automatic cessation"),
   ("is treated as foreign service for pension purposes",
    "Foreign service is defined in rule 3(1)(j); rule 10 concerns employment under another Government")],
  "Rule 10 deals with a pensioner who takes employment under any Government outside India. Such employment "
  "requires the sanction of the Central Government, and where it is taken without that sanction the pension "
  "may be withheld. The rule is the counterpart, in the pension rules, of the general principle that a "
  "pensioner remains subject to a measure of control in his post-retirement dealings with foreign "
  "governments. It is distinct from rule 9, which is about commercial employment in the private sector within "
  "one year, and from the definition of foreign service in rule 3(1)(j), which concerns the source of a "
  "serving officer's pay.",
  "Confusing employment under a foreign Government with foreign service")
