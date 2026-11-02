# -*- coding: utf-8 -*-
"""L3 integrated cases 01–08."""

L3A = [
    dict(id="L3-01", title="From charge sheet to compulsory retirement — a file audit",
         facts=("Shri A, a Group ‘B’ officer with 27 years' service, was served with articles of charge on 16.01.2026 alleging (i) an irregular payment of "
                "₹12,40,000 without sanction and (ii) failure to maintain the contingent register. He filed his defence on 02.02.2026. The disciplinary "
                "authority condoned two days' delay, appointed the Deputy Secretary as inquiry authority on 10.03.2026, and the first hearing was held on "
                "20.03.2026. The report of 05.08.2026 held charge 1 not proved and charge 2 proved. The disciplinary authority disagreed on charge 1; its "
                "tentative reasons were recorded in a file note, and a copy of the report was sent to the officer on 20.08.2026 asking for a representation "
                "within 15 days, without the note. He represented on 02.09.2026. On 20.09.2026 he was compulsorily retired. The file shows that the Deputy "
                "Secretary had, as the then controlling officer, recorded in the preliminary investigation that “the officer appears to have misappropriated "
                "the amount and must be dealt with severely”."),
         record=[["Charge sheet served", "16.01.2026", "r.14(3)–(4)"],
                 ["Defence", "02.02.2026", "day 17; delay condoned"],
                 ["Inquiry authority appointed", "10.03.2026", "the same officer who investigated"],
                 ["First hearing", "20.03.2026", "within 10 working days"],
                 ["Report", "05.08.2026", "charge 1 not proved; charge 2 proved"],
                 ["Report supplied", "20.08.2026", "disagreement note withheld"],
                 ["Representation", "02.09.2026", "does not address charge 1"],
                 ["Penalty", "20.09.2026", "compulsory retirement"]],
         questions=["Is the appointment of the inquiry authority valid?",
                    "Was the inquiry completed within the time allowed?",
                    "What is the effect of the defence filed on day 17?",
                    "Was the procedure after the report regular?",
                    "What is the consequence for the penalty?",
                    "What may the department do next, and what is his remedy meanwhile?"],
         path=["competence: r.12", "inquiry authority: bias", "timelines: r.14(4), (24)", "disagreement: r.15(2)", "penalty: r.15(6)", "remedy"],
         steps=[["1. Penalty competence", "Compulsory retirement is a major penalty; it was imposed by the authority competent under r.12(2), no defect shown", "12(2), 11(vii)", 2],
                ["2. Inquiry authority", "The officer who had recorded a view on the officer's guilt in the preliminary investigation could not sit as inquiry authority; a reasonable apprehension of bias vitiates the inquiry", "14(2); A.K. Kraipak (1969)", 3],
                ["3. Charge sheet", "Articles of charge, statement of imputations and lists of documents and witnesses were delivered; r.14(3)–(4) satisfied in form", "14(3)–(4)", 2],
                ["4. Defence", "Filed on day 17; the authority condoned the delay and took it on record, which is the correct course — the 15 days is not a guillotine once the defence is accepted", "14(4)", 2],
                ["5. Appearance", "First hearing on 20.03.2026, within 10 working days of the appointment on 10.03.2026", "14(7)", 1],
                ["6. Completion", "Report on 05.08.2026 falls within six months of 10.03.2026 (expiring 10.09.2026); r.14(24) satisfied", "14(24)", 2],
                ["7. Disagreement", "The tentative reasons for disagreeing on charge 1 were recorded on file but never communicated; the officer was asked to answer a case he could not see", "15(2)", 3],
                ["8. Representation", "Considered, but it could not have addressed the uncommunicated disagreement; there is no waiver without knowledge", "15(2), 15(4)", 1],
                ["9. Penalty", "Compulsory retirement, influenced by charge 1, cannot stand; and because the whole inquiry was conducted by a biased authority, the finding on charge 2 falls with it", "15(6); 11(vii)", 3],
                ["10. Consequence", "The penalty is set aside; a fresh inquiry by another authority is permissible, on both charges, within the limits of r.14", "14(2); Art. 311", 2],
                ["11. Remedy and money", "Appeal under r.23(ii); on reinstatement the period is regulated under FR 54 and the pension consequence under the pension rules", "23(ii); FR 54", 1]],
         wrong=["<b>“The defence was late, so it could be ignored.”</b> It was condoned and taken on record; the defect disappears.",
                "<b>“Bias must be proved by evidence of actual prejudice.”</b> A reasonable apprehension, on the officer's own recorded view, is enough.",
                "<b>“Only charge 1 is affected by the disagreement.”</b> The bias affects the entire inquiry, including charge 2."],
         answer=("The inquiry is vitiated twice over — by the inquiry authority's pre-judged view and by withholding the tentative reasons for disagreement — so "
                 "the compulsory retirement is set aside; a fresh inquiry by a different authority is permissible on both charges, and his appeal lies under r.23(ii)."),
         model=("Three questions decide this file: who held the inquiry, what was done after the report, and what the penalty rests on. The inquiry authority had, "
                "during the preliminary investigation, recorded that the officer appeared to have misappropriated the amount and must be dealt with severely. A "
                "person who has already formed and recorded a view on guilt cannot thereafter hold a fair inquiry; the test is not proof of actual bias but a "
                "reasonable apprehension of it, and on this record the apprehension is well founded. The inquiry is therefore vitiated from its inception, and "
                "the finding on charge 2 falls with the finding on charge 1. Independently, rule 15(2) required the report to be supplied together with the "
                "disciplinary authority's tentative reasons for disagreeing with the inquiry authority on charge 1. Those reasons were recorded on the file but "
                "never communicated, so the officer was asked to meet a case whose basis he could not see, and his representation cannot be treated as a waiver "
                "of something he did not know. The penalty of compulsory retirement is therefore set aside. That does not entitle him to a clean record: a fresh "
                "inquiry by an authority unconnected with the investigation may be held on both charges, subject to the timelines in rule 14, and the period of "
                "the intervening suspension or absence from duty will be regulated under FR 54 when the matter concludes. His appeal lies under rule 23(ii), and "
                "the appellate authority should not remit the case to the same disciplinary authority without directing a different inquiry authority."),
         tags=[["12", "Rule 12 — disciplinary authorities"], ["14", "Rule 14 — procedure"], ["14(24)", "Rule 14(24) — completion of inquiry"],
               ["15", "Rule 15 — action on the inquiry report"], ["23", "Rule 23 — appealable orders"], ["FR 54", "FR 54 — pay on reinstatement"]]),

    dict(id="L3-02", title="Suspension, acquittal and the arithmetic of reinstatement",
         facts=("Shri B, a Group ‘B’ officer drawing basic pay ₹56,100 in Level 8, was suspended with effect from 01.03.2026 in view of a criminal case. The "
                "charge sheet in the departmental proceeding was issued on 20.04.2026. The criminal court acquitted him on 14.09.2026 with a finding that the "
                "prosecution had failed to prove the demand and that the witnesses were unreliable. He was reinstated on 30.09.2026. During suspension he was "
                "paid subsistence allowance at 50% for March to May 2026 and 75% for June to September 2026. DA is 63% ⚑. He asks for full pay for the entire "
                "period, treatment of the period as duty, and consequential seniority."),
         record=[["Suspension", "01.03.2026", "r.10(1)(b)"],
                 ["Charge sheet", "20.04.2026", "within the review period"],
                 ["Acquittal", "14.09.2026", "prosecution evidence rejected"],
                 ["Reinstatement", "30.09.2026", "—"],
                 ["Period", "7 months", "01.03.2026–30.09.2026"],
                 ["Pay", "₹56,100 + DA 63% ⚑", "base ₹91,443"]],
         questions=["Was the suspension validly continued to 30.09.2026?",
                    "What is the effect of the acquittal?",
                    "Compute the full pay for the period and the arrears after adjusting subsistence allowance.",
                    "Should the period be treated as duty?",
                    "What of seniority and promotion?"],
         path=["r.10(1)(b) valid", "review + extension to 30.09.2026", "acquittal: FR 54", "full pay ₹91,443 p.m.", "arrears after SA", "period as duty"],
         steps=[["1. Validity", "Suspension on a criminal case is competent under r.10(1)(b); the charge sheet followed on 20.04.2026, within the first review period", "10(1)(b), 10(6)", 2],
                ["2. Continuation", "The file shows reviews and extensions covering the period to 30.09.2026; absent a gap, the suspension remained valid", "10(6)–(7)", 2],
                ["3. Effect of acquittal", "An acquittal on the merits, the prosecution evidence having been rejected, is not a technical acquittal; the suspension is then treated as wholly unjustified", "FR 54(1)(a)", 2],
                ["4. Full pay", "Pay plus DA: ₹56,100 × 1.63 = <b>₹91,443</b> per month ⚑", "FR 54; DA order", 2],
                ["5. Gross for seven months", "₹91,443 × 7 = <b>₹6,40,101</b>", "FR 54", 2],
                ["6. Subsistence paid", "50% for three months: ₹45,721.50 × 3 = ₹1,37,164.50; 75% for four months: ₹68,582.25 × 4 = ₹2,74,329; total <b>₹4,11,493.50</b>", "FR 53", 3],
                ["7. Arrears", "₹6,40,101 − ₹4,11,493.50 = <b>₹2,28,607.50</b>", "FR 54", 2],
                ["8. Period", "The period is treated as duty for all purposes, since the suspension was wholly unjustified", "FR 54(1)(a)", 2],
                ["9. Seniority", "He retains his position in the seniority list and is considered for promotion as if he had not been suspended; the sealed-cover question does not arise because the proceeding is over", "FR 54; Jankiraman (1991)", 2],
                ["10. Caution", "If the departmental proceeding continues after the acquittal, a penalty cannot rest on the same evidence without independent application of mind", "14; 19", 1]],
         wrong=["<b>“Acquittal means automatic reinstatement with full pay.”</b> It depends on the character of the acquittal and on FR 54.",
                "<b>“Subsistence allowance is deducted from basic pay only.”</b> Arrears are computed on pay plus DA, less what was actually paid.",
                "<b>“The period remains suspension.”</b> On a wholly unjustified suspension it is duty."],
         answer=("The suspension was validly continued, but the acquittal on the merits makes it wholly unjustified: full pay of <b>₹91,443</b> a month for seven "
                 "months is <b>₹6,40,101</b>, less subsistence of ₹4,11,493.50, leaving arrears of <b>₹2,28,607.50</b>, with the period treated as duty and "
                 "seniority protected."),
         model=("The suspension was competently ordered under rule 10(1)(b), a criminal case being under investigation, and it was kept alive by reviews and "
                "extensions under rule 10(6), the charge sheet following on 20.04.2026. The acquittal of 14.09.2026 is not a technical acquittal: the court "
                "rejected the prosecution evidence, which means the foundation of the suspension and of the criminal case disappeared on the merits. The "
                "consequence is governed by FR 54. The suspension being wholly unjustified, the officer is entitled to full pay and allowances for the period "
                "01.03.2026 to 30.09.2026, that is ₹56,100 plus DA at 63 per cent — ₹91,443 a month, or ₹6,40,101 for seven months. He has already received "
                "subsistence allowance of ₹1,37,164.50 for the first three months at 50 per cent and ₹2,74,329 for the next four at 75 per cent, totalling "
                "₹4,11,493.50, which must be adjusted, leaving ₹2,28,607.50. The period counts as duty for all purposes, his seniority is unaffected, and he is "
                "to be considered for promotion as though he had never been suspended. The departmental proceeding, if it continues, cannot be decided on the "
                "same material that the criminal court rejected without an independent application of mind."),
         tags=[["10", "Rule 10 — suspension"], ["10(1)", "Rule 10(1) — grounds"], ["10(6)", "Rule 10(6) — review"],
               ["FR 53", "FR 53 — subsistence"], ["FR 54", "FR 54 — pay on reinstatement"]]),

    dict(id="L3-03", title="Three years one stage down — pay, increments and pension",
         facts=("Shri C, in Level 7 with basic pay ₹52,000 from 01.07.2025 (increment on 1 July), was imposed the penalty of reduction by one stage for three "
                "years under r.11(v) with effect from 01.07.2026. The penalty order is in the standard form: no increment is to be earned during the three "
                "years, and what comes after them is not postponed. It was applied to the pay he was drawing immediately before the increment of 01.07.2026 "
                "fell due, ₹52,000, so the next lower stage is ₹50,500; the stages above are ₹53,600, ₹55,200, ₹56,900 and ₹58,600. "
                "DA is 63% ⚑. He retires on 30.06.2030."),
         record=[["Pay from 01.07.2025", "₹52,000", "Level 7"],
                 ["Penalty effective", "01.07.2026, 3 years", "r.11(v)"],
                 ["Lower stage", "₹50,500", "one stage"],
                 ["Increment date", "1 July", "annual"],
                 ["Retirement", "30.06.2030", "pension follows"]],
         questions=["What is the pay during each year of the penalty?",
                    "What is the total loss of basic pay?",
                    "What is the pay on expiry of the penalty?",
                    "How does the penalty affect his pension?",
                    "Was the direction on future increments within power?"],
         path=["r.11(v)", "fix at ₹50,500", "no increments for 3 years", "loss year by year", "restore notional stage", "pension effect"],
         steps=[["1. Character", "Reduction by one stage for three years with directions on increments is a major penalty under r.11(v), not the minor penalty under r.11(iiia)", "11(v), 11(iiia)", 2],
                ["2. Pay during penalty", "Pay fixed at the lower stage, <b>₹50,500</b>, from 01.07.2026 to 30.06.2029; no increment is earned", "11(v); DoPT 18.06.2019", 2],
                ["3. Notional stages", "But for the penalty he would have drawn ₹53,600 (01.07.2026), ₹55,200 (01.07.2027) and ₹56,900 (01.07.2028)", "11(v)", 2],
                ["4. Loss year 1", "(₹53,600 − ₹50,500) × 12 = <b>₹37,200</b>", "11(v)", 2],
                ["5. Loss year 2", "(₹55,200 − ₹50,500) × 12 = <b>₹56,400</b>", "11(v)", 2],
                ["6. Loss year 3", "(₹56,900 − ₹50,500) × 12 = <b>₹76,800</b>", "11(v)", 2],
                ["7. Total", "₹37,200 + ₹56,400 + ₹76,800 = <b>₹1,70,400</b> of basic pay; DA follows the pay", "11(v)", 2],
                ["8. On expiry", "Because future increments are not postponed, pay is fixed on 01.07.2029 at the notional stage <b>₹58,600</b>", "11(v); DoPT 18.06.2019", 2],
                ["9. Pension", "Pension is computed on emoluments or average emoluments of the last ten months; the three years at the reduced stage depress the average, so the penalty reduces pension even after it has run", "CCS (Pension) Rules, 2021", 2],
                ["10. The direction", "The directions on increments are part of the penalty and must be in the order; here they are, and they are within r.11(v)", "11(v)", 1]],
         wrong=["<b>“The loss is ₹1,500 × 36.”</b> That ignores the increments he would have earned.",
                "<b>“On expiry he restarts at ₹52,000.”</b> He moves to the notional stage because postponement was not directed.",
                "<b>“The penalty ends with the period.”</b> Its effect on average emoluments continues into pension."],
         answer=("Pay is <b>₹50,500</b> for three years, the loss is <b>₹1,70,400</b> of basic pay, and on 01.07.2029 pay is fixed at the notional stage "
                 "<b>₹58,600</b>; the reduced emoluments depress his average for pension, which is the penalty's longest shadow."),
         model=("The order imposes a major penalty under rule 11(v): reduction to a lower stage for a specified period, with directions on increments and future "
                "effect. Pay during the period is fixed at the lower stage of ₹50,500 from 01.07.2026 to 30.06.2029, and because the order directs that no "
                "increments shall be earned, it remains there. Had he not been penalised, he would have drawn ₹53,600 from 01.07.2026, ₹55,200 from 01.07.2027 "
                "and ₹56,900 from 01.07.2028. The loss of basic pay is therefore ₹37,200, ₹56,400 and ₹76,800 — ₹1,70,400 in all, with DA at 63 per cent "
                "following the pay. Because the order does not postpone future increments, on expiry his pay is fixed at the stage he would have reached, "
                "₹58,600, and not at the stage from which he was reduced. The penalty nevertheless has a longer reach: pension is computed on the emoluments "
                "or the average of the last ten months, and three years at a reduced stage depress that average, so the pension fixed on 30.06.2030 will be "
                "lower than it would otherwise have been. That consequence is inherent in the penalty and is the reason the choice between r.11(iiia), "
                "r.11(iv) and r.11(v) matters so much."),
         tags=[["11", "Rule 11 — penalties"], ["11(v)", "Rule 11(v) — reduction to a lower stage"], ["11(iiia)", "Rule 11(iiia) — minor one-stage reduction"]]),

    dict(id="L3-04", title="Ex parte inquiry, an illness letter, and an enhanced penalty",
         facts=("Smt D was served with articles of charge on 05.01.2026. She appeared before the inquiry authority on 19.01.2026, sought inspection of documents, "
                "and was allowed inspection on 27.01.2026. On 10.02.2026 she did not appear and sent no intimation. The authority recorded the default and "
                "examined three witnesses ex parte, closing the evidence the same day. The report of 20.05.2026 held all charges proved. It was supplied on "
                "25.05.2026 with 15 days to represent. On 09.06.2026 she filed a representation saying she had been ill from 08.02.2026 to 25.02.2026 and "
                "attaching a medical certificate. On 30.06.2026 the disciplinary authority imposed reduction to a lower stage for three years. She appealed on "
                "05.08.2026. On 20.09.2026 the appellate authority, without notice, enhanced the penalty to removal, recording that the charges involved "
                "integrity and that the penalty was inadequate."),
         record=[["Charge sheet", "05.01.2026", "—"],
                 ["First appearance", "19.01.2026", "documents sought"],
                 ["Inspection", "27.01.2026", "allowed"],
                 ["Default", "10.02.2026", "no intimation"],
                 ["Ex parte evidence", "10.02.2026", "three witnesses"],
                 ["Report", "20.05.2026", "all charges proved"],
                 ["Representation", "09.06.2026", "illness, with certificate"],
                 ["Penalty", "30.06.2026", "reduction, 3 years"],
                 ["Enhancement", "20.09.2026", "removal, no notice"]],
         questions=["Was the ex parte inquiry validly conducted?",
                    "What should the disciplinary authority have done with the illness certificate?",
                    "Was the penalty of 30.06.2026 sustainable?",
                    "Was the enhancement valid?",
                    "What is the final position?"],
         path=["r.14(20) ex parte", "record of default", "illness: cause to be examined", "r.15(2) representation", "enhancement needs r.27(2)(iv)", "remand"],
         steps=[["1. The default", "Non-appearance on 10.02.2026 without intimation, after a granted inspection, is a default within r.14(20)", "14(20)", 2],
                ["2. The record", "The authority recorded the default and took the evidence of the Presenting Officer; the procedure in r.14(11) and (20) was followed on the face of the record", "14(11), (20)", 2],
                ["3. But the illness", "A representation supported by a certificate, alleging inability to attend on the very date of default, raises a question of sufficient cause; the authority had to consider it before acting on an ex parte report", "14(20), 15(2)", 3],
                ["4. If accepted", "The inquiry should be reopened to the extent of allowing cross-examination of the witnesses already examined, which cures the prejudice without a fresh inquiry", "14(14), (20)", 2],
                ["5. The penalty", "Reduction for three years is competent under r.11(v) and was imposed after the report and representation; absent a decision on the illness, it rests on an inquiry whose fairness is in question", "15(2), (6)", 3],
                ["6. The enhancement", "The appellate authority may enhance under r.27(2), but only after a reasonable opportunity to represent against the enhanced penalty", "27(2)(iv)", 3],
                ["7. The notice", "No notice was given; the enhancement from reduction to removal is therefore void", "27(2)(iv)", 2],
                ["8. Severability", "The appellate order falls to the extent of the enhancement; the original penalty revives unless the appellate authority redoes the exercise after notice", "27(2)", 2],
                ["9. Final position", "Remit to the disciplinary authority to decide the illness question; if the cause is accepted, reopen cross-examination; then re-decide the penalty; the appellate authority may act only after notice", "14(20), 15(2), 27(2)(iv)", 3]],
         wrong=["<b>“An ex parte inquiry is conclusive.”</b> It is valid only if the default is established and the fairness of the record survives challenge.",
                "<b>“Illness after the default is irrelevant.”</b> It goes to sufficient cause for non-appearance.",
                "<b>“Enhancement is the appellate authority's discretion.”</b> It has a statutory precondition."],
         answer=("The ex parte course was open on 10.02.2026, but the illness certificate required a decision on sufficient cause before the report was acted on; "
                 "the enhancement to removal was void for want of the opportunity under <b>r.27(2)(iv)</b>, and the matter must go back for that decision and "
                 "for a fresh penalty."),
         model=("Two separate controls operate here, one at the inquiry and one in appeal. At the inquiry, rule 14(20) permits an ex parte inquiry where the "
                "employee does not appear, and the authority did record the default and take the Presenting Officer's evidence. But the employee then placed "
                "before the disciplinary authority a representation supported by a medical certificate covering the very date of default. That is an "
                "explanation of the absence, and rule 15(2) requires the authority to consider the representation before it acts on the report. It could not "
                "treat the ex parte record as conclusive without deciding whether the absence was sufficiently caused; if it accepts the explanation, the "
                "remedy is not a fresh inquiry but reopening the record so that the witnesses already examined can be cross-examined, which removes the "
                "prejudice at the least cost. In appeal, the appellate authority's power to enhance under rule 27(2) is real but conditional: rule 27(2)(iv) "
                "forbids an enhanced penalty unless the appellant has had a reasonable opportunity, in the manner of rule 16, of representing against it. No "
                "notice was given, so the enhancement to removal is void, and the penalty of reduction for three years revives unless the appellate authority "
                "re-does the exercise after notice. The file therefore goes back twice over — to the disciplinary authority on the illness, and then to the "
                "penalty stage."),
         tags=[["14(20)", "Rule 14(20) — ex parte inquiry"], ["15(2)", "Rule 15(2) — representation on the report"],
               ["27", "Rule 27 — consideration of appeal"], ["27(2)", "Rule 27(2)(iv) — enhancement"]]),

    dict(id="L3-05", title="Conviction, dismissal and two levels of challenge",
         facts=("Shri E, a Senior Audit Officer in the Indian Audit and Accounts Department, was convicted on 15.03.2026 under the Prevention of Corruption Act "
                "and sentenced to two years' rigorous imprisonment. He was dismissed the same day under r.19(i) without any representation on the penalty. He "
                "appealed to the Accountant General on 20.04.2026; the appeal was dismissed on 30.06.2026. On 15.09.2026 he filed a revision petition before "
                "the Comptroller and Auditor-General, asking that the dismissal be set aside because (i) no inquiry was held, (ii) he was not heard on the "
                "penalty, and (iii) his criminal appeal is pending. The CAG proposes to enhance the penalty to “dismissal with forfeiture of pension”, which "
                "is not a penalty known to the rules."),
         record=[["Conviction", "15.03.2026", "2 years' RI"],
                 ["Dismissal", "15.03.2026", "r.19(i), no representation"],
                 ["Appeal to AG", "20.04.2026", "dismissed 30.06.2026"],
                 ["Revision to CAG", "15.09.2026", "r.29(1)(ii)"],
                 ["Criminal appeal", "pending", "conviction not suspended"],
                 ["Proposed", "“dismissal with forfeiture of pension”", "not a r.11 penalty"]],
         questions=["Was the dismissal competent without an inquiry?",
                    "Was a representation on the penalty necessary?",
                    "Is the CAG competent to revise the appellate order?",
                    "Can the CAG enhance as proposed?",
                    "What is the correct disposal of the revision?"],
         path=["r.19(i)", "no inquiry needed", "representation discretionary", "CAG revision — subordinate test", "enhancement needs opportunity", "penalty must be one in r.11"],
         steps=[["1. The power", "Where a penalty is imposed on the ground of conduct leading to conviction on a criminal charge, r.19(i) dispenses with the r.14 inquiry", "19(i)", 2],
                ["2. The safeguard", "The proviso permits a representation on the penalty proposed; it is not mandatory in terms, but its denial is a relevant factor and good practice", "proviso to 19(i)", 2],
                ["3. Pendency of appeal", "A conviction under appeal is a conviction unless suspended; the department could act on it", "19(i)", 2],
                ["4. CAG's revision power", "The CAG may revise an order under the rules for a servant in the IA&AD, at any time, if the authority which made the order in appeal is subordinate to him — the Accountant General is", "29(1)(ii); second proviso", 3],
                ["5. Consultation", "Where the Commission must be consulted, the advice must be obtained and a copy supplied with an opportunity to represent", "19, second proviso; 32", 2],
                ["6. The proposed penalty", "There is no penalty of “dismissal with forfeiture of pension”; a revising authority may impose a penalty in r.11, not invent one", "29(1)(b), 11", 2],
                ["7. Enhancement", "An enhancing order requires a reasonable opportunity of representation against the penalty proposed", "proviso to 29(1)", 3],
                ["8. Pension", "Forfeiture of pension is not part of the penalty but a consequence under the pension rules, and it follows only on dismissal, after their own procedure", "CCS (Pension) Rules, 2021", 2],
                ["9. Disposal", "Reject the challenge to the inquiry; set aside the proposed form of penalty; if enhancement is still proposed, issue a notice and hear him", "29(1); 11", 2]],
         wrong=["<b>“Rule 19 permits any penalty.”</b> It permits the penalties in r.11, not new ones.",
                "<b>“The CAG cannot revise an appellate order.”</b> He can, if the appellate authority is subordinate to him.",
                "<b>“A criminal appeal suspends the conviction.”</b> Only an order of the appellate court does."],
         answer=("The dismissal was competent under <b>r.19(i)</b> without an inquiry and without a mandatory representation; the CAG may revise, but the proposed "
                 "penalty does not exist in r.11 and cannot be imposed without a notice and an opportunity under the proviso to <b>r.29(1)</b>."),
         model=("The dismissal rests on rule 19(i): where the penalty is imposed on the ground of conduct which led to conviction on a criminal charge, the inquiry "
                "under rule 14 is dispensed with, and the order was passed on the day of conviction. The proviso to rule 19(i) permits a representation on the "
                "penalty proposed, but it is permissive, and the omission does not by itself vitiate the order; the conviction, moreover, stands until the "
                "criminal appellate court suspends or sets it aside, so the pendency of the appeal does not disable the department. The revision before the "
                "Comptroller and Auditor-General is competent: rule 29(1)(ii) confers the power for a servant in the Indian Audit and Accounts Department at any "
                "time, and the second proviso is satisfied because the Accountant General, who decided the appeal, is subordinate to him. The difficulty lies in "
                "what is proposed. A revising authority may confirm, reduce, enhance or set aside a penalty, or impose a penalty under rule 11; it cannot create "
                "a penalty called dismissal with forfeiture of pension, because forfeiture of pension is not a penalty under rule 11 but a consequence that "
                "flows, under the pension rules, from dismissal itself. And any enhancement requires a reasonable opportunity of representation against the "
                "penalty proposed, which has not been given. The revision should therefore be disposed of by upholding the inquiry and the penalty of dismissal, "
                "setting aside the proposed additional forfeiture, and, if any further penalty is contemplated, issuing a notice and hearing the officer first."),
         tags=[["19", "Rule 19 — special procedure"], ["29", "Rule 29 — revision"], ["11", "Rule 11 — penalties"],
               ["15(3)", "Rule 15(3) — Commission's advice and representation"]]),

    dict(id="L3-06", title="Recovery, appeal and revision — a small file with three stages",
         facts=("Shri F, a Group ‘C’ storekeeper, was noticed a proposed recovery of ₹2,40,000 for pecuniary loss caused by negligence. He represented that the loss "
                "was ₹1,50,000 and produced the stock register. On 30.04.2026 the disciplinary authority imposed recovery of ₹3,60,000, relying on a special audit "
                "report of 20.04.2026 that had never been put to him. He appealed on 02.06.2026; the appellate authority reduced the recovery to ₹2,40,000 on "
                "15.07.2026, holding that the audit figure was reliable. He now seeks revision before the Head of Department, contending that the appellate order "
                "merely restored the figure that was never communicated."),
         record=[["Notice", "₹2,40,000 proposed", "computation supplied"],
                 ["Representation", "loss said to be ₹1,50,000", "stock register produced"],
                 ["Audit report", "20.04.2026", "not put to him"],
                 ["Order", "30.04.2026", "recovery ₹3,60,000"],
                 ["Appeal", "02.06.2026", "reduced to ₹2,40,000"],
                 ["Revision", "to Head of Department", "r.29(1)(iv)"]],
         questions=["Was the recovery of ₹3,60,000 valid?",
                    "What was the maximum sustainable on the notice?",
                    "Was the appellate order sound?",
                    "What should the revising authority do?",
                    "What is the money position if the original notice is the ceiling?"],
         path=["r.11(iii) recovery", "quantum must be noticed", "₹2,40,000 ceiling", "appeal reduced to ceiling", "revision: reasons for reduction", "final figure"],
         steps=[["1. The penalty", "Recovery of pecuniary loss caused by negligence is a minor penalty under r.11(iii); the amount must be quantified and put to the employee", "11(iii), 16(1)(a)", 2],
                ["2. The notice", "The proposal put ₹2,40,000 with a computation; that defined the case he had to meet", "16(1)(a)", 2],
                ["3. The increase", "Recovery of ₹3,60,000 on an audit report never supplied breached the opportunity; the excess of ₹1,20,000 is unsustainable", "16(1)(a), (c)", 3],
                ["4. His figure", "His contention of ₹1,50,000 does not bind the authority; the stock register is material to be weighed, with reasons", "16(1)(c), (e)", 2],
                ["5. The appeal", "The appellate authority reduced to ₹2,40,000 but justified it on the audit report, which the employee had never seen; the figure is right but the reasoning is defective", "27(2)", 3],
                ["6. The revision", "The Head of Department may revise under r.29(1)(iv) at any time, but only if the appellate authority is subordinate to him", "29(1)(iv); second proviso", 2],
                ["7. Power on revision", "He may confirm, modify or set aside, reduce or enhance; enhancement requires an opportunity", "29(1)(a)–(b); proviso", 2],
                ["8. Money", "The sustainable recovery is ₹2,40,000 on the notice; of this, nothing has been recovered, so the balance is ₹2,40,000, payable as directed, with no interest unless the rules provide it", "11(iii)", 2],
                ["9. Course", "Uphold ₹2,40,000, but record that the figure rests on the notice and not on the uncommunicated audit report; if a higher figure is sought, issue a fresh notice", "16(1)(a); 29", 2]],
         wrong=["<b>“Audit's figure is conclusive.”</b> The employee must meet the figure before it is recovered.",
                "<b>“The appeal cures the notice.”</b> It reduced the amount but relied on material never supplied.",
                "<b>“The Head of Department can revise only within six months.”</b> That limit applies to the appellate authority."],
         answer=("Recovery beyond <b>₹2,40,000</b> was unsustainable for want of notice, and the appellate order, though right in figure, rested on an "
                 "uncommunicated report; the revision should confirm ₹2,40,000 on the notice and require a fresh notice for anything more."),
         model=("The penalty is one of recovery of pecuniary loss under rule 11(iii), a minor penalty, and the procedure in rule 16 required the employee to be "
                "informed of the proposal and the imputations and given a reasonable opportunity of representation. The notice of 09.01.2026 quantified the loss "
                "at ₹2,40,000 and supplied the computation; that was the case he had to answer. The order of 30.04.2026 recovered ₹3,60,000 on the strength of a "
                "special audit report of 20.04.2026 which was never put to him, and to that extent it denied the opportunity the rule guarantees. The appellate "
                "authority reduced the recovery to ₹2,40,000, which is the correct ceiling, but justified the figure by the same audit report. The result is right "
                "in amount and wrong in reasoning: the sustainable figure is ₹2,40,000 because that is what was noticed, not because the audit report is reliable. "
                "On revision, the Head of Department may confirm, modify or set aside the appellate order, being a superior authority within the second proviso to "
                "rule 29(1). He should confirm the recovery of ₹2,40,000 on the basis of the notice, record that his finding of negligence rests on the material "
                "that was supplied, and direct that any higher figure be pursued only through a fresh notice with the audit report and a fresh opportunity. Nothing "
                "has been recovered so far, and no interest arises on the recovery unless the rules provide for it."),
         tags=[["11", "Rule 11 — penalties"], ["11(iii)", "Rule 11(iii) — recovery"], ["16", "Rule 16 — minor penalties"],
               ["27", "Rule 27 — appeal"], ["29", "Rule 29 — revision"]]),

    dict(id="L3-07", title="A sealed cover opened twenty-six months later",
         facts=("A charge sheet was issued to Shri G on 02.05.2024. The Departmental Promotion Committee met on 15.06.2024 and placed its recommendation in a "
                "sealed cover. The inquiry concluded on 11.08.2026 with all charges held not proved. The sealed cover was opened on 20.08.2026 and he was "
                "promoted with effect from that date. He claims promotion from 15.06.2024 with arrears of the difference between the two levels, which is "
                "₹2,700 a month, and consequential seniority. The department says the promotion can only be prospective."),
         record=[["Charge sheet", "02.05.2024", "major penalty"],
                 ["DPC", "15.06.2024", "sealed cover"],
                 ["Charges", "not proved", "11.08.2026"],
                 ["Cover opened", "20.08.2026", "promotion prospective"],
                 ["Claim", "from 15.06.2024", "26 months"],
                 ["Difference", "₹2,700 per month", "—"]],
         questions=["Was the sealed cover procedure available?",
                    "From what date does promotion take effect on exoneration?",
                    "Compute the arrears.",
                    "What of seniority and further promotion?",
                    "What is the remedy if the department refuses?"],
         path=["charge pending on DPC date", "sealed cover valid", "exoneration", "promotion from DPC date", "arrears ₹70,200", "seniority restored"],
         steps=[["1. Availability", "On 15.06.2024 a charge sheet had been issued and a major penalty was proposed; the second of the three categories was met and the cover was properly used", "DoPT OM No. 22011/4/91-Estt.(A), 14.09.1992, para 2(ii); Jankiraman (1991)", 2],
                ["2. The rule of outcome", "On conclusion the cover is opened. Exoneration is the case the OM addresses: the due date is worked back from the position in the panel and the date of the next junior's promotion. A penalty is the other case — para 3.1 — and there is none here", "DoPT OM 14.09.1992, paras 3 and 3.1", 3],
                ["3. Application", "All charges were held not proved on 11.08.2026 — exoneration, not a penalty; his panel position is acted upon and the due date fixed with reference to his junior's promotion from the same DPC", "DoPT OM 14.09.1992, para 3", 3],
                ["4. Arrears", "₹2,700 × 26 months = <b>₹70,200</b> on basic pay. The OM leaves notional arrears for the interval to the appointing authority's discretion, but a refusal must be reasoned — and here the only reason is the department's own delay", "DoPT OM 14.09.1992, para 6", 2],
                ["5. Pay fixation", "Pay is refixed in the higher level from 15.06.2024, with increments that would have accrued, and arrears recalculated on that basis", "FR 22; DoPT instructions", 2],
                ["6. Seniority", "He regains the seniority he would have had, and is considered for the next promotion accordingly", "Jankiraman (1991)", 2],
                ["7. Delay", "The two-year inquiry is itself a breach of the r.14(24) discipline; it cannot be used to postpone the benefit further", "14(24)", 2],
                ["8. Remedy", "Appeal against any order refusing retrospective promotion, or a representation followed by appeal; the appellate authority may direct the effective date", "23(iv), 27", 2]],
         wrong=["<b>“The sealed cover is opened prospectively.”</b> The effective date is the DPC date if the outcome permits.",
                "<b>“Exoneration gives only notional promotion.”</b> It gives promotion with arrears.",
                "<b>“The department may await the criminal case.”</b> There is none; the proceeding concluded."],
         answer=("The sealed cover was properly used, but exoneration on 11.08.2026 entitles him to promotion from <b>15.06.2024</b> with arrears of "
                 "<b>₹70,200</b>, refixation of pay in the higher level and consequential seniority."),
         model=("The sealed cover procedure was available on 15.06.2024, because a charge sheet had been issued and a major penalty was proposed, and the decision "
                "in Union of India v. K.V. Jankiraman (1991) requires the recommendation to be kept in a sealed cover rather than withheld. What happens on the "
                "conclusion of the proceeding depends on the outcome, and the outcome here is complete exoneration: all charges were held not proved. In that "
                "event the officer is entitled to promotion with effect from the date of the Departmental Promotion Committee, not from the date the cover was "
                "opened. He is therefore to be promoted from 15.06.2024, his pay is to be refixed in the higher level with the increments that would have accrued, "
                "and he is entitled to the difference between the two levels for twenty-six months, which at ₹2,700 a month is ₹70,200, before the consequential "
                "recalculation of allowances. His seniority must be restored to what it would have been, and his case considered for further promotion "
                "accordingly. The department's objection that the promotion can only be prospective is contrary to the rule of outcome, and the twenty-six month "
                "inquiry, itself outside the discipline of rule 14(24), cannot be used to postpone the benefit further."),
         tags=[["14", "Rule 14 — procedure"], ["14(24)", "Rule 14(24) — completion"], ["15", "Rule 15 — action on the report"],
               ["23", "Rule 23 — appealable orders"]]),

    dict(id="L3-08", title="One transaction, two officers, and an incompetent common proceeding",
         facts=("A payment of ₹18,00,000 was made without sanction. The Drawing Officer, Smt H (Group ‘B’), and the cashier, Shri I (Group ‘C’), were both "
                "charged. The Deputy Secretary ordered a common proceeding under r.18, appointed herself the disciplinary authority for both, and imposed removal "
                "on Smt H and withholding of two increments for two years on Shri I. The Joint Secretary is the authority competent to dismiss Smt H; the "
                "Deputy Secretary can impose only minor penalties on Group ‘B’ officers of that office. Smt H appeals against removal; Shri I accepts his penalty."),
         record=[["Transaction", "₹18,00,000 unsanctioned", "both charged"],
                 ["Order under r.18", "by Deputy Secretary", "—"],
                 ["Competence for Smt H", "Joint Secretary", "to dismiss"],
                 ["Penalty on Smt H", "removal", "r.11(viii)"],
                 ["Penalty on Shri I", "two increments, 2 years", "r.11(iv), minor"],
                 ["Appeal", "by Smt H only", "—"]],
         questions=["Was the common proceeding validly ordered?",
                    "Was the penalty on Smt H within competence?",
                    "Does the defect affect Shri I's penalty?",
                    "What is the consequence for each?",
                    "What should the department do?"],
         path=["r.18(1) authority competent to dismiss all", "Deputy Secretary not competent for H", "proceeding bad", "H's penalty void", "I's penalty stands unless prejudice"],
         steps=[["1. The condition", "A common proceeding may be ordered only by an authority competent to impose dismissal on all the servants concerned", "18(1)", 3],
                ["2. Application", "The Deputy Secretary could not dismiss Smt H; the order convening the common proceeding was therefore without jurisdiction", "18(1)", 3],
                ["3. Competence to penalise", "Removal of Smt H by the Deputy Secretary breaches r.12(4)(a): no authority subordinate to the appointing authority may impose a major penalty", "12(4)(a)", 3],
                ["4. The inquiry itself", "The inquiry conducted under an invalid common proceeding is not thereby void in every respect; the evidence is usable, but the penalties must be imposed by competent authorities", "18, 12", 2],
                ["5. Smt H", "Her removal is void for want of competence; a fresh order by the Joint Secretary on the existing record, after applying its mind, is permissible", "12(4)(a), 15(6)", 3],
                ["6. Shri I", "A minor penalty imposed on him is within the Deputy Secretary's competence, and he has not appealed; but he may raise the invalidity of the common proceeding if it caused prejudice", "18; 23", 2],
                ["7. His acceptance", "Acceptance of the penalty does not cure a jurisdictional defect, but a minor penalty imposed by a competent authority stands", "12(3), 12(4)", 2],
                ["8. Appeal", "Smt H's appeal lies under r.23(ii) to the appellate authority competent for her; the appellate authority should set aside the removal and direct a fresh order by the competent authority", "23(ii), 27", 2],
                ["9. Record", "The department should record that the common proceeding was misconceived and regularise the two files separately", "18", 2]],
         wrong=["<b>“A common proceeding validates any penalty.”</b> It is a procedural facility, not a source of competence.",
                "<b>“Shri I's penalty falls with the proceeding.”</b> It was within his authority's competence, and no prejudice is shown.",
                "<b>“Removal can be ratified by the Joint Secretary later.”</b> A fresh order on the record is needed, not ratification."],
         answer=("The common proceeding was misconceived because the Deputy Secretary could not dismiss Smt H, and her removal breached <b>r.12(4)(a)</b>; the "
                 "removal is void and a fresh order by the Joint Secretary is needed, while Shri I's minor penalty, being within competence, stands."),
         model=("Rule 18 permits a common proceeding where two or more Government servants are concerned in one case, but only an authority competent to impose "
                "dismissal on all of them may order it. The Deputy Secretary could not dismiss Smt H, a Group ‘B’ officer for whom the Joint Secretary is the "
                "competent authority, so the order convening the common proceeding was itself without jurisdiction. That defect is compounded when the Deputy "
                "Secretary proceeded to impose removal on her, because rule 12(4)(a) forbids any authority subordinate to the appointing authority from imposing "
                "a penalty under rule 11(v) to (ix). Her removal is therefore void, and the appropriate course is a fresh order by the Joint Secretary on the "
                "record already made, after applying its mind; the department cannot ratify the Deputy Secretary's order retrospectively. Shri I's position "
                "differs: withholding of two increments is a minor penalty, within the competence of the authority that imposed it, and he has not appealed. "
                "The invalidity of the common proceeding does not by itself invalidate his penalty, because the inquiry was regular and he shows no prejudice; "
                "if he wished to challenge it, he would have to show that the defective forum affected the fairness of his inquiry. The department should "
                "regularise the two files separately and record why the common proceeding was misconceived."),
         tags=[["18", "Rule 18 — common proceedings"], ["12", "Rule 12 — disciplinary authorities"],
               ["12(4)", "Rule 12(4) — limits on competence"], ["23", "Rule 23 — appealable orders"]]),
]
