# -*- coding: utf-8 -*-
"""L3 integrated cases 09–16."""

L3B = [
    dict(id="L3-09", title="Detention, deemed suspension, acquittal — and a file that forgot the review",
         facts=("Shri J, a Group ‘C’ Auditor drawing basic pay ₹44,900 (DA 60% to 30.06.2026, 63% ⚑ thereafter), was arrested on 12.01.2026 in a criminal case "
                "and released on bail on 20.01.2026. The appointing authority was informed on 22.01.2026. No suspension order and no review were ever issued. "
                "He was tried, acquitted on 14.07.2026 on the merits, and allowed to resume duty on 15.07.2026. He was paid subsistence allowance at 50% for the "
                "first three months and 75% for the rest. He claims full pay for the whole period, and the department says he was never suspended at all."),
         record=[["Arrest", "12.01.2026", "custody"],
                 ["Release", "20.01.2026", "8 days"],
                 ["Intimation", "22.01.2026", "to appointing authority"],
                 ["Review", "none", "no order"],
                 ["Acquittal", "14.07.2026", "on the merits"],
                 ["Resumed duty", "15.07.2026", "—"],
                 ["Pay", "₹44,900 + DA", "base ₹71,840"]],
         questions=["Was he under suspension, and from when?",
                    "When did that suspension cease to be valid?",
                    "Is the department right that he was never suspended?",
                    "What is he entitled to for the period?",
                    "How is the period to be treated?"],
         path=["r.10(2)(a) detention >48h", "deemed from 12.01.2026", "proviso to r.10(7): 90 days from intimation", "lapse 21.04.2026", "acquittal → FR 54", "full pay + duty"],
         steps=[["1. Deemed suspension", "Detention of eight days exceeds 48 hours, so he is deemed to have been suspended with effect from the date of detention, <b>12.01.2026</b>", "10(2)(a)", 3],
                ["2. The clock", "For a deemed suspension, the ninety days count from release or from intimation of release, whichever is later — here <b>22.01.2026</b>", "proviso to 10(7)", 3],
                ["3. The lapse", "Ninety days counted inclusively from 22.01.2026 are complete on <b>21.04.2026</b>; with no review and no extension, the suspension ceased to be valid at the end of that day", "10(6), 10(7)", 3],
                ["4. The department's plea", "It is untenable: a deemed suspension operates by force of the rule and needs no order; the absence of a review is the department's failure, not the employee's", "10(2)", 2],
                ["5. Pay to 21.04.2026", "Subsistence allowance under FR 53: 50% of ₹71,840 = ₹35,920 for the first ninety days", "FR 53(i)", 2],
                ["6. Pay after lapse", "From 22.04.2026 he was entitled to full pay: ₹71,840 a month until 30.06.2026 and ₹73,187 from 01.07.2026 ⚑", "FR 53; 10(7)", 3],
                ["7. Acquittal", "The acquittal is on the merits, so the suspension is treated as wholly unjustified and the whole period counts as duty with full pay", "FR 54(1)(a)", 3],
                ["8. Arrears", "Full pay for the period 12.01.2026–14.07.2026, less the subsistence already paid, is the arrears; the period of invalid suspension is not to be debited against leave", "FR 54", 2],
                ["9. Regularisation", "The department must regularise the record, treat the period as duty, and restore consequential benefits, including any promotion considered in the interval", "FR 54; Jankiraman (1991)", 1]],
         wrong=["<b>“Without an order there is no suspension.”</b> A deemed suspension operates by the rule.",
                "<b>“The ninety days run from arrest.”</b> They run from release or intimation, whichever is later.",
                "<b>“He was only entitled to subsistence throughout.”</b> After the lapse he was entitled to full pay, and on acquittal to the whole period as duty."],
         answer=("He was under a deemed suspension from <b>12.01.2026</b>; the ninety days ran from intimation on 22.01.2026 and the suspension lapsed on "
                 "<b>21.04.2026</b>, so full pay is due from 22.04.2026, and the acquittal on the merits makes the whole period duty with arrears after "
                 "adjusting the subsistence paid."),
         model=("No order of suspension was passed, and none was needed. Detention in custody for eight days, which exceeds forty-eight hours, creates a deemed "
                "suspension with effect from the date of detention under rule 10(2)(a), and it is immaterial that the file contains no order; the rule itself "
                "supplies the order. The ninety-day clock for a deemed suspension does not run from arrest: the proviso to rule 10(7) counts it from release or "
                "from intimation of release, whichever is later, which here is 22.01.2026. Counted inclusively, the ninety days expired on 21.04.2026, and "
                "because no review committee met and no extension issued, the suspension ceased to be valid at the end of that day. From 22.04.2026 he was "
                "entitled to full pay — ₹44,900 plus DA, that is ₹71,840 a month, rising to ₹73,187 from 01.07.2026 when DA becomes 63 per cent. The acquittal "
                "of 14.07.2026 is on the merits, so the suspension is treated as wholly unjustified and the entire period from 12.01.2026 to 14.07.2026 counts "
                "as duty for all purposes under FR 54, with full pay less the subsistence allowance already drawn, and with no debit to his leave account. The "
                "department's contention that he was never suspended is unsound, and its failure to review is not a Defence to the claim for arrears."),
         tags=[["10", "Rule 10 — suspension"], ["10(2)", "Rule 10(2) — deemed suspension"], ["10(7)", "Rule 10(7) — validity"],
               ["FR 53", "FR 53 — subsistence"], ["FR 54", "FR 54 — pay on reinstatement"]]),

    dict(id="L3-10", title="A probationer, a shortage and a termination letter",
         facts=("Smt K was appointed as a probationer for two years from 01.08.2025. In April 2026 a stock verification found a shortage of ₹86,000 in the "
                "counter she handled. The controlling officer's note of 02.05.2026 records that she had “misappropriated the amount and should be removed”. "
                "On 10.06.2026 her services were terminated “during the period of probation in accordance with the terms of appointment”, with one month's pay in "
                "lieu of notice. No inquiry was held. Her representation asking for the verification report was not answered. She completed 22 years of age in "
                "2026 and has no other employment."),
         record=[["Appointment", "01.08.2025", "two years' probation"],
                 ["Shortage", "₹86,000", "April 2026 verification"],
                 ["Note", "02.05.2026", "“misappropriated… should be removed”"],
                 ["Termination", "10.06.2026", "terms of appointment"],
                 ["Inquiry", "none", "—"],
                 ["Request for report", "refused", "—"]],
         questions=["Is termination during probation a penalty?",
                    "What decides whether this termination is punitive?",
                    "What does the record establish?",
                    "What is the consequence, and what options does the department have?",
                    "What is her remedy?"],
         path=["Explanation (viii)(a) to r.11", "simpliciter vs punitive", "foundation = misconduct", "inquiry required", "termination void", "remedy"],
         steps=[["1. The rule", "Termination of a probationer during probation in accordance with the terms of appointment is not a penalty", "Explanation (viii)(a) to r.11", 2],
                ["2. The test", "Where misconduct is the foundation and the order is not a simpliciter discharge, the termination is punitive and requires the r.14 procedure; the label and the pay in lieu do not decide", "Dipti Prakash Banerjee (1999); Radhey Shyam Gupta (1999)", 3],
                ["3. The record", "The shortage, the note that she had misappropriated and should be removed, and the proximity of the termination establish that the foundation was the alleged misappropriation", "Explanation (viii)(a) to r.11", 3],
                ["4. The inquiry", "None was held, so the punitive termination is void; the denial of the verification report compounded the denial of the opportunity", "14(3)–(4)", 3],
                ["5. Pay in lieu", "One month's pay in lieu of notice does not convert a punitive order into a simpliciter discharge", "Explanation (viii)(a) to r.11", 2],
                ["6. Consequence", "Reinstatement with consequential benefits, or a fresh proceeding after a regular inquiry; the department cannot both plead probation and punish misconduct", "11, 14", 3],
                ["7. Alternative", "If the department genuinely doubts her suitability, it may terminate simpliciter on material unrelated to the alleged misconduct, recording that basis", "Explanation (viii)(a) to r.11", 2],
                ["8. Remedy", "Appeal under r.23(ii) within 45 days of delivery; if the order is not a penalty, the appeal lies against the order as one affecting conditions of service", "23(iv), 25", 2]],
         wrong=["<b>“A probationer can always be discharged.”</b> Not when the discharge is founded on misconduct.",
                "<b>“The letter says ‘during probation’, so it is simpliciter.”</b> Substance decides.",
                "<b>“Pay in lieu regularises it.”</b> It does not change the character of the order."],
         answer=("The termination is punitive in substance because the alleged misappropriation was its foundation, and no inquiry was held; it is void, and the "
                 "department must either reinstate her or hold a regular inquiry, or terminate simpliciter on material unconnected with the misconduct."),
         model=("The starting point is the Explanation to rule 11: termination of a probationer during or at the end of probation, in accordance with the terms of "
                "appointment, is not a penalty. That protection is real but conditional. Where the order, whatever its form, is founded on an allegation of "
                "misconduct, it is punitive in substance and attracts the procedure in rule 14. The record here leaves little room: a stock verification found a "
                "shortage of ₹86,000, the controlling officer recorded on 02.05.2026 that she had misappropriated the amount and should be removed, and the "
                "termination followed five weeks later without any inquiry or any answer to her request for the verification report. The letter's recital of the "
                "terms of appointment and the payment of one month's salary in lieu of notice do not alter its character, because the foundation of the order "
                "was the alleged misappropriation and not an assessment of probationary suitability. The termination is therefore void. The department has two "
                "lawful courses: reinstate her and, if it wishes to pursue the shortage, hold a regular inquiry with the documents and witnesses; or terminate "
                "her simpliciter on material that does not rest on the alleged misconduct, recording the basis. What it cannot do is punish her for "
                "misappropriation while describing the order as a probationary discharge. Her appeal lies under rule 23, and limitation runs from delivery of the "
                "order."),
         tags=[["11", "Rule 11 — penalties"], ["14", "Rule 14 — procedure"], ["23", "Rule 23 — appealable orders"]]),

    dict(id="L3-11", title="Five increments, cumulative, and no inquiry at all",
         facts=("Shri L, a Group ‘C’ clerk with basic pay ₹44,900, was imposed the penalty of withholding of five increments with cumulative effect for five years "
                "by an order of 12.02.2026. He had been given a notice of the proposal and imputations on 05.01.2026 and filed a representation. No inquiry was "
                "held. The order records that the penalty would “operate cumulatively and postpone future increments and pensionary benefits”. He continued in "
                "service and his pay was fixed at ₹44,900 throughout."),
         record=[["Notice and imputations", "05.01.2026", "r.16(1)(a)"],
                 ["Representation", "filed", "considered"],
                 ["Inquiry", "none", "—"],
                 ["Penalty", "five increments, cumulative, 5 years", "r.11(iv)"],
                 ["Effect recorded", "future increments and pension", "—"],
                 ["Pay drawn", "₹44,900", "unchanged"]],
         questions=["Was this a minor penalty?",
                    "Was an inquiry mandatory?",
                    "What is the notional pay he should have reached?",
                    "What is the consequence of the order?",
                    "What must the department do now?"],
         path=["r.11(iv) minor", "but r.16(1-A)", "cumulative + >3 years + pension", "inquiry mandatory", "order void", "fresh inquiry"],
         steps=[["1. Classification", "Withholding of increments is a minor penalty under r.11(iv)", "11(iv)", 1],
                ["2. The trigger", "An inquiry in the manner of r.14(3)–(23) is mandatory where the withholding exceeds three years, or is cumulative, or is likely to affect pension", "16(1-A)", 3],
                ["3. Application", "All three limbs are present: five years, cumulative effect, and the order itself records a pension consequence", "16(1-A)", 3],
                ["4. The omission", "No inquiry was held; the notice-and-representation route of r.16(1)(a) is not a substitute for the mandatory inquiry", "16(1-A)", 3],
                ["5. Consequence", "The order is void; the penalty cannot be sustained and the withheld increments must be restored", "16(1-A)", 3],
                ["6. Notional pay", "Five increments from ₹44,900 would take him to ₹52,000 in Level 7 (₹46,200, ₹47,600, ₹49,000, ₹50,500, ₹52,000), so the pay he should have drawn is ₹52,000, not ₹44,900", "11(iv)", 2],
                ["7. Arrears", "The difference for the period must be paid, and the pensionable average recalculated, because the recorded effect on pension flows from a void order", "11(iv), 16(1-A)", 2],
                ["8. Fresh proceeding", "The department may hold the mandatory inquiry and, if the charge is proved, impose a penalty that satisfies r.16(1-A)", "16(1-A), 16(1)(b)", 2],
                ["9. Alternative penalty", "If it wishes to avoid the inquiry, it must confine itself to a penalty that does not attract r.16(1-A), such as withholding of one increment for two years without cumulative effect", "16(1-A), 11(iv)", 1]],
         wrong=["<b>“Minor penalties never need an inquiry.”</b> Rule 16(1-A) creates three exceptions.",
                "<b>“Cumulative effect is a formality.”</b> It is one of the statutory triggers.",
                "<b>“The order can be regularised by holding an inquiry now.”</b> A fresh proceeding is needed; the old order is void."],
         answer=("Although withholding of increments is a minor penalty, the five-year term, the cumulative effect and the pension consequence made an inquiry "
                 "mandatory under <b>r.16(1-A)</b>; no inquiry was held, so the order is void and pay must be restored to the notional <b>₹52,000</b>."),
         model=("The penalty of withholding of increments is classified as a minor penalty by rule 11(iv), and the ordinary procedure under rule 16 is the notice "
                "and representation route. That route was not sufficient here. Rule 16(1-A) requires an inquiry in the manner laid down in sub-rules (3) to (23) "
                "of rule 14 before an order of withholding of increments is made where the withholding is likely to affect pension adversely, or exceeds three "
                "years, or is to operate cumulatively. The order of 12.02.2026 fails all three: it withholds five increments, it directs cumulative effect, and it "
                "records in terms that future increments and pensionary benefits will be postponed. No inquiry was held, so the mandatory procedure was absent "
                "and the order is void. The consequence is not merely formal. Five increments from ₹44,900 would have taken his pay to ₹52,000 in the level, "
                "whereas he has been held at ₹44,900; the difference must be paid, his pensionable emoluments recalculated, and the recording of a pension "
                "consequence cannot stand when the order that produced it is void. The department may start again and hold the inquiry that rule 16(1-A) "
                "requires, or, if it wishes to avoid an inquiry, confine itself to a penalty that does not attract that sub-rule."),
         tags=[["11", "Rule 11 — penalties"], ["11(iv)", "Rule 11(iv) — withholding of increments"],
               ["16", "Rule 16 — minor penalties"], ["16(1-A)", "Rule 16(1-A) — mandatory inquiry"]]),

    dict(id="L3-12", title="Revision, the subordinate test, and an enhancement that cannot be made",
         facts=("Shri M, a Group ‘B’ officer in the Indian Audit and Accounts Department, was censured by the Accountant General on 20.02.2026. He appealed to the "
                "Principal Accountant General, who dismissed the appeal on 30.05.2026. On 12.09.2026 the Comptroller and Auditor-General issued a notice proposing "
                "to revise the Principal Accountant General's appellate order and enhance the penalty to withholding of two increments for two years. The notice "
                "called for a representation “if any” within seven days. Shri M objects that the CAG cannot revise an order passed in appeal by an authority of "
                "equal standing, that the notice is time-barred, and that seven days is not a reasonable opportunity."),
         record=[["Censure", "20.02.2026", "by Accountant General"],
                 ["Appeal", "dismissed 30.05.2026", "by Principal AG"],
                 ["Notice of revision", "12.09.2026", "by CAG"],
                 ["Proposed", "withholding of 2 increments", "r.11(iv)"],
                 ["Time allowed", "7 days", "“if any”"]],
         questions=["Is the CAG competent to revise the appellate order?",
                    "Is there a time limit on the CAG's revision?",
                    "Was the opportunity adequate?",
                    "What is the correct disposal?"],
         path=["r.29(1)(ii)", "CAG for IA&AD, any time", "second proviso: subordinate test", "enhancement needs reasonable opportunity", "dispose on merits"],
         steps=[["1. The power", "The CAG may revise any order under the rules in the case of a Government servant serving in the IA&AD, at any time, on his own motion or otherwise", "29(1)(ii)", 2],
                ["2. The subordinate test", "The power is exercisable only if the authority which made the order in appeal, or the authority to which an appeal would lie where none was preferred, is subordinate to the CAG; the Principal Accountant General is", "second proviso to 29(1)", 3],
                ["3. No time limit", "The six-month limit in r.29(1)(v) applies to revision by an appellate authority; the CAG's power is not so limited", "29(1)(ii), (v)", 2],
                ["4. Waiting period", "Revision may not commence until the appeal period expires or the appeal is disposed of; the appeal was decided on 30.05.2026, so the notice is not premature", "29(2)", 2],
                ["5. Enhancement", "No enhancing order may be made unless the servant has had a reasonable opportunity of representing against the penalty proposed", "proviso to 29(1)", 3],
                ["6. Seven days", "Seven days to answer a proposal to enhance from censure to withholding of two increments is not a reasonable opportunity on any view, and the words “if any” compound the deficiency", "proviso to 29(1)", 3],
                ["7. Disposal", "The notice is competent as to power, forum and time, but the opportunity must be re-given; no enhancing order may be passed until then", "29(1)", 2],
                ["8. If no enhancement", "The CAG may confirm or set aside the appellate order without any such opportunity", "29(1)(a)–(b)", 1]],
         wrong=["<b>“An appellate order cannot be revised.”</b> It can, if the making authority is subordinate.",
                "<b>“Six months applies to the CAG.”</b> That limit applies to the appellate authority's revision.",
                "<b>“Seven days is reasonable because the record is short.”</b> Reasonableness depends on what must be answered, and an enhancement needs a real opportunity."],
         answer=("The CAG may revise the Principal Accountant General's appellate order at any time and is not bound by the six-month limit, but the seven-day "
                 "notice is not a reasonable opportunity; the notice must be reissued and no enhancement made until a proper representation is considered."),
         model=("Three objections are taken, and two of them fail. The Comptroller and Auditor-General's power of revision under rule 29(1)(ii) extends to any "
                "Government servant serving in the Indian Audit and Accounts Department and may be exercised at any time, either on his own motion or otherwise. "
                "The second proviso requires that the authority which made the order in appeal be subordinate to him; the Principal Accountant General is, so the "
                "objection that the revisional authority is of equal standing is misconceived. Nor is there a time bar: the six months in rule 29(1)(v) governs "
                "revision by an appellate authority, not by the CAG. Rule 29(2) required only that the appeal be disposed of first, and it was, on 30.05.2026. The "
                "third objection succeeds. The proviso to rule 29(1) forbids any order imposing or enhancing a penalty unless the servant has had a reasonable "
                "opportunity of making a representation against the penalty proposed, and where a major penalty is proposed without a prior inquiry, an inquiry in "
                "the manner of rule 14 is required. Seven days to answer a proposal that converts a censure into withholding of two increments is not a reasonable "
                "opportunity, and the invitation to represent “if any” suggests the outcome was already settled. The notice must be reissued with a proper "
                "opportunity, and no enhancing order may be passed until the representation is considered and reasons are recorded."),
         tags=[["29", "Rule 29 — revision"], ["29-A", "Rule 29-A — review"], ["11", "Rule 11 — penalties"]]),

    dict(id="L3-13", title="A charge sheet from 2019 and an inquiry that began in 2026",
         facts=("Articles of charge were issued to Shri N on 12.03.2019. He submitted a defence in April 2019. No inquiry authority was appointed until 05.01.2026. "
                "The inquiry concluded on 20.06.2026. Two of the four listed witnesses had retired by then, one had died, and the key file could not be traced "
                "because it had been weeded out under the retention schedule in 2023. The report held all charges proved, relying mainly on the statements "
                "recorded in 2018 during the preliminary investigation. The penalty of reduction to a lower stage for two years was imposed on 30.07.2026."),
         record=[["Charge sheet", "12.03.2019", "—"],
                 ["Defence", "April 2019", "—"],
                 ["Inquiry authority", "05.01.2026", "nearly 7 years later"],
                 ["Report", "20.06.2026", "all charges proved"],
                 ["Witnesses", "2 retired, 1 died", "—"],
                 ["File", "weeded out 2023", "—"],
                 ["Penalty", "30.07.2026", "reduction, 2 years"]],
         questions=["What does r.14(24) require, and was it observed?",
                    "What is the effect of relying on preliminary-investigation statements?",
                    "Has prejudice been shown?",
                    "What is the consequence for the penalty?",
                    "What is the remedy, and can a fresh inquiry be held?"],
         path=["r.14(24) 6 months from appointment", "7 years delay", "evidence unavailable", "prejudice", "penalty unsustainable", "no fresh inquiry on dead evidence"],
         steps=[["1. The clock", "The inquiry had to be concluded within six months of the appointment of the inquiry authority; the appointment itself came nearly seven years after the charge sheet", "14(24)", 2],
                ["2. The breach", "No explanation appears for the seven-year interval, and no extension was sought; the delay is unexplained and extraordinary", "14(24)", 2],
                ["3. Evidence", "Statements recorded in a preliminary investigation are not evidence; they may be used to contradict a witness under the rules of evidence, but not as the basis of findings where the witness is unavailable for cross-examination", "14(14); 14(3)(ii)(b)", 3],
                ["4. Prejudice", "Two witnesses retired, one died and the key file was weeded out; the defence could neither cross-examine nor produce the document, so prejudice is patent and specific", "14(11)–(14)", 3],
                ["5. Consequence", "The findings rest on material that could not be tested and on a record the department itself destroyed; the penalty cannot stand", "15(2), 15(6)", 3],
                ["6. Fresh inquiry", "A fresh inquiry is permissible in principle, but not on the same unavailable evidence; the department must show it can produce witnesses and documents", "14(2)", 2],
                ["7. Remedy", "Appeal under r.23(ii); the appellate authority may set aside the penalty and, if a fresh inquiry is ordered, must fix a time limit", "23(ii), 27", 2],
                ["8. Administrative", "The file should record accountability for the delay, which is a failure of the r.14(24) discipline and of the record-retention rules", "14(24)", 1]],
         wrong=["<b>“Delay alone vitiates.”</b> Delay plus prejudice vitiates; here both are present.",
                "<b>“Preliminary statements can be read as evidence.”</b> They cannot substitute for examination and cross-examination.",
                "<b>“The file was weeded out lawfully, so no prejudice.”</b> Lawful weeding does not cure the loss to the defence."],
         answer=("The inquiry breached <b>r.14(24)</b> by a margin of years and rested on untested preliminary statements after the witnesses and the file had "
                 "disappeared; prejudice being patent, the penalty is unsustainable and a fresh inquiry can only proceed on evidence that still exists."),
         model=("Rule 14(24) requires the inquiry authority to conclude the inquiry and submit its report within six months of receiving its order of appointment, "
                "with extensions of not more than six months at a time for reasons recorded in writing. Here the charge sheet was issued on 12.03.2019, the "
                "defence was filed in April 2019, and no inquiry authority was appointed until 05.01.2026. That interval is unexplained, and no extension was "
                "sought at any stage. The report then relied principally on statements recorded in the preliminary investigation in 2018, although by 2026 two of "
                "the listed witnesses had retired, one had died and the key file had been weeded out. Statements recorded behind the employee's back are not "
                "evidence, and rule 14(14) contemplates examination and cross-examination; the employee could neither test the statements nor produce the "
                "document, and the department's own retention decisions caused part of that loss. Prejudice is therefore specific and demonstrable, not "
                "speculative, and the findings cannot stand. The penalty is set aside. A fresh inquiry is not barred in law, but it can only proceed on evidence "
                "that still exists; the appellate authority should require the department to satisfy it on that point before remitting, and should fix a time "
                "limit so that the delay is not repeated."),
         tags=[["14", "Rule 14 — procedure"], ["14(24)", "Rule 14(24) — completion"],
               ["15", "Rule 15 — action on the report"], ["23", "Rule 23 — appealable orders"]]),

    dict(id="L3-14", title="Eighty-nine days' absence and the ultimate penalty",
         facts=("Shri O absented himself from 01.02.2026 to 30.04.2026 — 89 days — without sanctioned leave. He had applied for leave on 28.01.2026, which was "
                "refused on 30.01.2026 and the refusal was sent to his address. He did not respond. A charge sheet was issued on 20.05.2026 alleging unauthorised "
                "absence; he replied that his mother was ill in his home town. No medical evidence was produced. The inquiry held the charge proved and the "
                "disciplinary authority imposed removal, recording that “absence of this length is abandonment of service and cannot be tolerated”. He has 19 "
                "years' service and a clean record."),
         record=[["Absence", "01.02.2026–30.04.2026", "89 days"],
                 ["Leave applied", "28.01.2026", "refused 30.01.2026"],
                 ["Charge sheet", "20.05.2026", "unauthorised absence"],
                 ["Defence", "mother ill", "no evidence"],
                 ["Penalty", "removal", "r.11(viii)"],
                 ["Record", "19 years, clean", "—"]],
         questions=["What must be established to prove unauthorised absence?",
                    "Was the charge proved on this record?",
                    "Is removal proportionate?",
                    "What should the appellate authority do?"],
         path=["charge: absence without authority", "finding must match", "proved on facts", "penalty: proportionality", "consider lesser penalty", "remand"],
         steps=[["1. The charge", "The charge is absence without authority; it requires a finding that leave was refused or not sanctioned and that the absence was therefore unauthorised", "14(3); Krushnakant B. Parmar (2012)", 3],
                ["2. The finding", "Leave was refused on 30.01.2026 and communicated; he remained absent for 89 days; the finding matches the charge", "14(23)", 2],
                ["3. The defence", "Illness of a relative is no answer to a refusal of leave, and no medical evidence was produced; the explanation was rightly rejected", "14(14), 14(18)", 2],
                ["4. Characterisation", "Long unauthorised absence can amount to misconduct justifying removal, but the penalty must be proportionate and reasons must engage with the record", "11(viii)", 2],
                ["5. Proportionality", "Nineteen years' clean service, a single period of absence, a stated family reason, and an order that treats absence as “abandonment” without a finding of intent: the penalty is severe and the reasoning does not address the mitigating record", "Ganayutham (1997); Rajendra Singh (2013)", 3],
                ["6. What is not the issue", "Abandonment of service is not a statutory penalty; the penalty imposed is removal, and it must be justified as such", "11(viii)", 2],
                ["7. Disposal", "The appellate authority may reduce the penalty to a lesser one in r.11, or remit for reconsideration of quantum with reasons, but should not set aside the finding", "27(2)", 3],
                ["8. Money", "If the penalty is reduced to withholding of increments or recovery, the intervening period must be regularised and pay fixed accordingly", "11; FR 54", 2]],
         wrong=["<b>“Absence is abandonment, so removal is automatic.”</b> Abandonment is not a penalty in the rules.",
                "<b>“Any absence without leave justifies removal.”</b> Proportionality applies, especially with long clean service.",
                "<b>“The illness plea fails, so no mitigation exists.”</b> Mitigation is not limited to a successful defence."],
         answer=("The charge of unauthorised absence was proved, but removal is disproportionate on 19 years' clean service for a single 89-day absence with a "
                 "stated family reason; the appellate authority should reduce the penalty or remit for reconsideration of quantum under <b>r.27(2)</b>."),
         model=("The charge is absence without authority, and it requires proof that leave was applied for, refused or not sanctioned, and that the absence was "
                "therefore unauthorised; following Krushnakant B. Parmar v. Union of India (2012), a finding of mere absence will not do. On this record that "
                "finding is properly made: leave was applied for on 28.01.2026, refused on 30.01.2026 and the refusal communicated, and the officer remained away "
                "for eighty-nine days without any further application. His explanation that his mother was ill is not supported by any medical evidence and does "
                "not answer the refusal. The finding therefore stands. The penalty does not. Removal is the second most severe penalty in rule 11, and the order "
                "rests on an assertion that absence of this length is “abandonment of service” — a characterisation the rules do not use and which the order does "
                "not support with any finding of intent never to return. Against that stand nineteen years of unblemished service and a single period of absence "
                "with a stated family reason. Proportionality, as explained in Union of India v. G. Ganayutham (1997) and Lucknow Kshetriya Gramin Bank v. "
                "Rajendra Singh (2013), requires the penalty to bear a reasonable relation to the misconduct; that relation is missing, and the reasons do not "
                "engage with the mitigating record. The appellate authority should reduce the penalty to one within rule 11 that fits the misconduct, or remit the "
                "question of quantum for reconsideration with reasons, leaving the finding undisturbed."),
         tags=[["11", "Rule 11 — penalties"], ["11(viii)", "Rule 11(viii) — removal"], ["27", "Rule 27 — consideration of appeal"],
               ["15", "Rule 15 — action on the report"]]),

    dict(id="L3-15", title="Two penalties for one act",
         facts=("Shri P was found to have misappropriated ₹65,000 from a cash imprest. In a single order dated 15.04.2026 the disciplinary authority imposed two "
                "penalties: recovery of ₹65,000 under r.11(iii) and withholding of three increments for three years under r.11(iv). The order records that both are "
                "for the same act. He appealed, contending that two penalties cannot be imposed for one misconduct and that in any event recovery of the full amount "
                "plus a penal withholding duplicates the punishment."),
         record=[["Misappropriation", "₹65,000", "one act"],
                 ["Penalty 1", "recovery ₹65,000", "r.11(iii)"],
                 ["Penalty 2", "3 increments, 3 years", "r.11(iv)"],
                 ["Order", "single, 15.04.2026", "same act"],
                 ["Procedure", "r.16, notice and hearing", "no inquiry"]],
         questions=["Can two penalties be imposed for one act?",
                    "Is recovery of the amount a penalty at all?",
                    "Was the procedure for the second penalty adequate?",
                    "What is the correct disposal?"],
         path=["one misconduct → one penalty", "recovery is a penalty under r.11(iii)", "no double penalty", "second falls", "remand for choice"],
         steps=[["1. The rule", "Rule 11 lists penalties but does not authorise more than one penalty for a single act of misconduct; the scheme of r.16 and r.15 contemplates a penalty, not a bundle", "11, 16", 2],
                ["2. Recovery", "Recovery of pecuniary loss is itself a penalty under r.11(iii), not a mere restitution, so it cannot be treated as no penalty", "11(iii)", 3],
                ["3. Duplication", "Recovery of the full ₹65,000 and a punitive withholding for the same act punishes twice; the second penalty cannot stand alongside the first", "11", 3],
                ["4. The procedure", "Both penalties are minor, and the notice-and-hearing route was followed; but for withholding of three increments no inquiry was required, since the triggers in r.16(1-A) are absent", "16(1), 16(1-A)", 2],
                ["5. Which stands", "The recovery is the more directly compensatory and is sustainable; the withholding falls, unless the authority vacates the recovery and substitutes another penalty", "11(iii), 11(iv)", 3],
                ["6. Reservation", "Where the misconduct has distinct limbs, or where two penalties address distinct consequences, the position may differ; the order here expressly ties both to one act, which removes that argument", "11", 2],
                ["7. Disposal", "Appeal under r.23(ii); set aside the withholding, confirm the recovery, and leave the authority free to impose one penalty of its choice after reasons", "23(ii), 27", 2]],
         wrong=["<b>“Rule 11 permits any number of penalties.”</b> It lists penalties; it does not authorise duplication for one act.",
                "<b>“Recovery is not a penalty, so there is no duplication.”</b> Recovery under r.11(iii) is expressly a penalty.",
                "<b>“Both penalties are minor, so both are harmless.”</b> Their combined effect is still double punishment."],
         answer=("Two penalties for one act are not permissible; recovery under <b>r.11(iii)</b> is itself a penalty, so the withholding of increments cannot stand "
                 "alongside it, and the appellate authority should set aside the latter and confirm the recovery."),
         model=("Rule 11 sets out the penalties that may be imposed “for good and sufficient reasons”, and rules 15 and 16 describe how a penalty is decided; "
                "neither contemplates the imposition of two penalties for a single act of misconduct. Here the order itself ties both penalties to the same act of "
                "misappropriating ₹65,000, and the argument that they address different things is therefore closed. Recovery of pecuniary loss under rule 11(iii) "
                "is not mere restitution; it is a penalty in its own right, and the authority chose it. Having done so, it could not also impose a punitive "
                "withholding of increments for the same act, because that would punish twice for one wrong. The procedure was otherwise regular: both penalties are "
                "minor, notice and a hearing were given, and the withholding of three increments did not attract rule 16(1-A), since it neither exceeded three "
                "years nor was cumulative nor affected pension. The withholding must therefore be set aside and the recovery confirmed. If the authority considers "
                "recovery inadequate, it may vacate it and impose a single penalty that reflects both the loss and the misconduct, recording its reasons; what it "
                "may not do is impose both."),
         tags=[["11", "Rule 11 — penalties"], ["11(iii)", "Rule 11(iii) — recovery"], ["11(iv)", "Rule 11(iv) — withholding of increments"],
               ["16", "Rule 16 — minor penalties"], ["23", "Rule 23 — appealable orders"]]),

    dict(id="L3-16", title="Appeal, revision, review — a map with three clocks",
         facts=("A penalty of withholding of promotion for two years was imposed on Shri Q on 10.01.2026 and delivered on 15.01.2026. He filed an appeal on "
                "20.02.2026. The appellate authority dismissed it on 20.04.2026. On 12.08.2026 he filed a revision petition before the appellate authority and, "
                "on the same day, a review petition before the President, relying on a document that he says he obtained only in July 2026 and which, he claims, "
                "shows that the penalty was based on a mistaken identity. The revision was rejected on 05.09.2026 as time-barred; the review is pending."),
         record=[["Penalty", "10.01.2026", "delivered 15.01.2026"],
                 ["Appeal", "20.02.2026", "within 45 days"],
                 ["Appellate order", "20.04.2026", "dismissed"],
                 ["Revision filed", "12.08.2026", "r.29(1)(v)"],
                 ["Review filed", "12.08.2026", "r.29-A"],
                 ["New document", "July 2026", "mistaken identity"]],
         questions=["Was the appeal in time?",
                    "Within what date could the appellate authority revise?",
                    "Was the revision rightly rejected?",
                    "Is the review competent, and before whom?",
                    "What should happen to the two petitions?"],
         path=["appeal: 45 days from delivery → 01.03.2026", "revision: 6 months from order → 10.07.2026", "revision barred", "review: President, new material", "review may proceed"],
         steps=[["1. Appeal", "Limitation ran from delivery on 15.01.2026; forty-five days expired on <b>01.03.2026</b>, and the appeal of 20.02.2026 is within time", "25", 2],
                ["2. Appellate order", "Dismissal on 20.04.2026 was within the appellate authority's power and is the order that now stands", "27(2)", 2],
                ["3. Revision clock", "Revision by the appellate authority must be within six months of the date of the order proposed to be revised — six months from 10.01.2026 is <b>10.07.2026</b>", "29(1)(v)", 3],
                ["4. The bar", "The petition of 12.08.2026 is beyond that date; rule 31 cannot revive a period that had already expired, and r.29(2) does not extend it", "29(1)(v), 29(2), 31", 3],
                ["5. Review", "Review lies to the President alone, at any time, on new material or evidence not available earlier which changes the nature of the case", "29-A", 3],
                ["6. The document", "A document obtained in July 2026 that shows mistaken identity is precisely the kind of new material r.29-A contemplates; the review is competent", "29-A", 3],
                ["7. Two petitions", "The revision was rightly rejected; the review may be entertained, but the President must be satisfied that the material could not earlier have been produced", "29-A", 3],
                ["8. Order of decision", "The review should be decided first, since if the identity point is accepted the penalty falls and the revision question becomes academic", "29-A", 2]],
         wrong=["<b>“Revision is a second appeal with a fresh 45 days.”</b> It is six months from the order, and it waits for the appeal.",
                "<b>“Rule 31 cures any delay.”</b> It cannot revive an expired period.",
                "<b>“The appellate authority can review.”</b> Review is Presidential only."],
         answer=("The appeal was in time; revision by the appellate authority expired on <b>10.07.2026</b> and was rightly rejected; but review before the President "
                 "under <b>r.29-A</b> is competent on the July document, and should be decided first because it may make the revision academic."),
         model=("Three different clocks govern the three remedies, and they are not interchangeable. The appeal was governed by rule 25: forty-five days from "
                "delivery on 15.01.2026, expiring on 01.03.2026, and the appeal of 20.02.2026 was in time. The appellate authority decided it on 20.04.2026 and "
                "that order now stands. Revision under rule 29(1)(v) had to be sought within six months of the date of the order proposed to be revised, that is "
                "by 10.07.2026; the target is the penalty order of 10.01.2026, passed by an authority subordinate to the appellate authority, for revision under "
                "rule 29 runs against an order of a subordinate authority and not against the revising authority's own appellate order, and the second "
                "proviso to rule 29(1) proceeds on that footing. The petition of 12.08.2026 is outside the six months, and rule 31 cannot revive a "
                "period already expired, since it deals with relaxation and "
                "condonation of time limits where the rules permit it, not with reopening a closed right. Review is different in kind. Rule 29-A allows the "
                "President, at any time, on his own motion or otherwise, to review an order where new material or evidence that could not earlier have been "
                "produced has come to notice and changes the nature of the case. A document obtained in July 2026 which shows that the penalty rested on mistaken "
                "identity is exactly such material, so the review petition is competent and should be entertained by the President, who must satisfy himself that "
                "it could not have been produced earlier. The review should be decided first: if the identity point is accepted the penalty falls, and the "
                "revision, already barred, becomes academic."),
         tags=[["25", "Rule 25 — limitation"], ["29", "Rule 29 — revision"], ["29-A", "Rule 29-A — review"],
               ["31", "Rule 31 — condonation"], ["27", "Rule 27 — appeal"]]),
]
