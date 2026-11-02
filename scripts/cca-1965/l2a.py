# -*- coding: utf-8 -*-
"""L2 standard cases 01–11 — the major-penalty procedure."""

L2A = [
    dict(id="L2-01", title="The defence that arrived on day 54",
         facts=("Shri A, an Assistant Accounts Officer, was served with articles of charge on 12.03.2026. "
                "He asked for time on 26.03.2026, which the disciplinary authority allowed to 11.04.2026. On 10.04.2026 "
                "he asked again, and was allowed time to 26.04.2026. On 05.05.2026 he filed a 42-page written statement "
                "of defence with 19 annexures. The disciplinary authority rejected it as time-barred and appointed an "
                "inquiry authority the same day, recording that the employee had defaulted."),
         record=[["Charge sheet delivered", "12.03.2026", "runs the 15-day clock"],
                 ["First extension", "to 11.04.2026", "15 days, allowed"],
                 ["Second extension", "to 26.04.2026", "within the overall cap"],
                 ["Defence filed", "05.05.2026", "9 days after the cap expired"],
                 ["Inquiry authority appointed", "05.05.2026", "same day as rejection"]],
         questions=["What is the last date on which a written statement of defence could lawfully be filed?",
                    "Was the disciplinary authority right to reject the defence of 05.05.2026?",
                    "May the inquiry now proceed, and on what record?",
                    "What should the disciplinary authority do with the 19 annexures?"],
         path=["Charge sheet 12.03.2026", "15 days", "extensions of 15 days at a time", "overall cap 45 days", "cap expires 26.04.2026", "late defence ≠ nullity of inquiry"],
         steps=[["Issue", "Whether a defence filed after the overall cap can be rejected and the inquiry continued", "14(4)", 1],
                ["The cap", "45 days from receipt: 12.03.2026 + 45 days = <b>26.04.2026</b>; the extensions to 11.04 and 26.04 both fall inside it", "14(4)", 2],
                ["No further extension", "The proviso forbids an extension that takes the total beyond 45 days; a third request cannot be allowed, however reasonable", "14(4), proviso", 2],
                ["Effect of rejection", "Rejection of the late defence is lawful; the inquiry is not vitiated merely because the defence was refused", "14(4), 14(5)(b)", 1],
                ["But the record", "The authority must record the default, the dates of service and each extension — the order of 05.05.2026 does this", "14(5)(b), 14(20)", 1],
                ["The annexures", "They must still be placed on the inquiry record and considered as defence material at the appropriate stage; refusing to look at them at all is a prejudice argument waiting to succeed", "14(16)–(19)", 1]],
         wrong=["<b>“The delay is condonable under rule 31.”</b> Rule 31 is about time-limits prescribed by the rules for authorities, not about the employee's right to file a defence beyond the cap.",
                "<b>“The inquiry is void because the defence was not taken.”</b> The rule expressly contemplates proceeding where no defence is submitted.",
                "<b>“45 days runs from the date of the charge sheet.”</b> It runs from <i>receipt</i> by the employee."],
         answer=("The last valid date was <b>26.04.2026</b> (45 days from 12.03.2026); the rejection is lawful and the inquiry may proceed, "
                 "but the defence and its annexures must be taken on the inquiry record and considered before findings."),
         tags=[["14(4)", "Rule 14(4) — defence, extensions and the 45-day cap"], ["14(5)", "Rule 14(5) — inquiry where the defence is not filed"],
               ["14(20)", "Rule 14(20) — ex parte inquiry"]]),

    dict(id="L2-02", title="Ex parte after a single default",
         facts=("The charge sheet against Smt B was received by the inquiry authority on 03.08.2026. She appeared on 14.08.2026, "
                "pleaded not guilty, and was given a list of witnesses. On 31.08.2026 she appeared without her defence assistant and "
                "sought an adjournment, which was allowed to 07.09.2026. She did not appear on 07.09.2026 and sent no intimation. "
                "The inquiry authority recorded her absence, examined the four departmental witnesses ex parte, and closed the evidence. "
                "She then appeared on 21.09.2026 asking to cross-examine the witnesses. The inquiry authority refused."),
         record=[["Charge sheet received by I.A.", "03.08.2026", "10 working days run from here"],
                 ["First appearance", "14.08.2026", "plea recorded: not guilty"],
                 ["Adjournment allowed", "to 07.09.2026", "at her request"],
                 ["Default", "07.09.2026", "recorded"],
                 ["Evidence taken ex parte", "07.09.2026", "four witnesses"],
                 ["Request to cross-examine", "21.09.2026", "refused"]],
         questions=["Was the ex parte course open to the inquiry authority?",
                    "Could she claim cross-examination as of right after the default?",
                    "What should the inquiry authority have recorded before closing the evidence?",
                    "If the report is adverse, what is her best ground?"],
         path=["Appearance within 10 working days", "default on 07.09.2026", "r.14(20) ex parte", "record the default", "evidence of the P.O.", "report + supply to employee"],
         steps=[["Issue", "Validity of an ex parte inquiry after one default", "14(20)", 1],
                ["Appearance", "Notice for 14.08.2026 fell within 10 working days of 03.08.2026; she appeared and pleaded, so r.14(7)–(9) are satisfied", "14(7), 14(9)", 1],
                ["The default", "Non-appearance on 07.09.2026 after a granted adjournment is a default within r.14(20); the authority may proceed ex parte", "14(20)", 2],
                ["The requirement", "Before closing, the authority should record that notice was served, that the default was wilful or unexplained, and that the Presenting Officer's evidence was taken in her absence", "14(11), 14(20)", 2],
                ["Cross-examination", "The right to cross-examine is exercisable when the evidence is taken; after a valid ex parte closure it is not available as of right, but the authority may permit recall to cure prejudice", "14(14)", 1],
                ["Consequence", "The inquiry is valid; her remedy is to show prejudice or to challenge the penalty, and the report must still be supplied to her with 15 days to represent", "15(2)", 1]],
         wrong=["<b>“An ex parte inquiry is void.”</b> Rule 14(20) expressly permits it.",
                "<b>“She must be given a fresh inquiry because she asked to cross-examine.”</b> The request came after a valid closure; permission would be discretionary.",
                "<b>“The evidence of the witnesses is inadmissible.”</b> It was recorded in the inquiry; its weight is for the disciplinary authority."],
         answer=("The ex parte inquiry was valid under <b>r.14(20)</b> provided the default and service were recorded; her request to cross-examine "
                 "after closure is not a matter of right, and the report must be supplied with <b>15 days</b> to represent."),
         tags=[["14(7)", "Rule 14(7) — appearance within 10 working days"], ["14(14)", "Rule 14(14) — evidence and cross-examination"],
               ["14(20)", "Rule 14(20) — ex parte inquiry"], ["15(2)", "Rule 15(2) — representation on the report"]]),

    dict(id="L2-03", title="A lawyer at the inquiry table",
         facts=("Shri C, a Senior Accounts Officer facing a major-penalty inquiry, asked to be represented by an advocate. "
                "The Presenting Officer appointed by the disciplinary authority is a Deputy Secretary with a law degree but is "
                "not enrolled as an advocate. The disciplinary authority refused permission, recording that the charges relate to "
                "financial irregularities within the employee's own knowledge and that no legal issue arises. Shri C then asked "
                "that a retired Section Officer, who had earlier assisted in two inquiries, be allowed to assist him."),
         record=[["Charge", "irregular payment of ₹18,40,000", "major penalty"],
                 ["Presenting Officer", "Deputy Secretary, law degree", "not a legal practitioner"],
                 ["Request 1", "advocate", "refused"],
                 ["Request 2", "retired Section Officer", "pending"]],
         questions=["Was the refusal of a legal practitioner correct?",
                    "May a retired Government servant assist, and on what conditions?",
                    "If the Presenting Officer is later replaced by a prosecutor on the panel of the Department, what follows?",
                    "What must the inquiry authority record on the second request?"],
         path=["r.14(8)(a)", "is the P.O. a legal practitioner?", "no", "discretion of the D.A.", "record reasons", "retired servant — r.14(8)(b)"],
         steps=[["Issue", "Right to representation in a major-penalty inquiry", "14(8)", 1],
                ["The rule", "A legal practitioner may be engaged only where the Presenting Officer is a legal practitioner or the disciplinary authority permits, having regard to the circumstances", "14(8)(a)", 2],
                ["Here", "A law degree without enrolment does not make the Presenting Officer a legal practitioner; refusal was therefore within power if reasons were recorded", "14(8)(a)", 2],
                ["Retired servant", "Permissible under r.14(8)(b) subject to the conditions prescribed by the President's order; the authority should apply the conditions, not refuse as a class", "14(8)(b)", 2],
                ["If the P.O. changes", "Appointment of a legal practitioner as Presenting Officer revives the employee's right to engage one; continuing without offering it is a procedural defect", "14(8)(a)", 1]],
         wrong=["<b>“A law degree makes the Presenting Officer a legal practitioner.”</b> Enrolment, not education, is the test.",
                "<b>“Legal representation is a fundamental right in departmental inquiries.”</b> It is a regulated facility, not an unqualified right.",
                "<b>“A retired Government servant can never assist.”</b> Rule 14(8)(b) expressly allows it on conditions."],
         answer=("The refusal of an advocate was within power because the Presenting Officer is not a legal practitioner and reasons were recorded; "
                 "a retired Government servant may assist under <b>r.14(8)(b)</b> on the prescribed conditions, and if a legal practitioner is later "
                 "appointed as Presenting Officer the employee must be offered the same facility."),
         tags=[["14(8)", "Rule 14(8) — defence assistant and legal practitioner"]]),

    dict(id="L2-04", title="Nineteen documents and a non-availability certificate",
         facts=("Smt D sought inspection of the documents listed with the charge sheet. The list named 23 documents; 19 were produced for "
                "inspection on the date fixed. Of the remaining four, the office issued a non-availability certificate for two and said the "
                "other two were “in a sealed cover in another division”. She sought production of the two, and of the statements of two "
                "witnesses whose names were in the list. The inquiry authority refused, recording that the charge could be proved from the "
                "19 documents produced, and closed the evidence. Her defence is that the two withheld documents would show that the payment "
                "was authorised by a superior."),
         record=[["Documents listed", "23", "—"],
                 ["Produced for inspection", "19", "within 5 days"],
                 ["Non-availability certificate", "2", "r.14(13)"],
                 ["Withheld", "2", "“sealed cover, another division”"],
                 ["Witness statements sought", "2", "not supplied"],
                 ["Inquiry closed", "same day", "refusal recorded"]],
         questions=["Was the inquiry authority bound to secure the two withheld documents?",
                    "What is the consequence of refusing them where the defence says they are exculpatory?",
                    "Was the refusal to supply the witness statements a defect?",
                    "What is the correct course at this stage?"],
         path=["listed documents", "r.14(11)(i) inspection", "r.14(13) production or certificate", "withheld without certificate", "prejudice asserted and specific", "report must address it"],
         steps=[["Issue", "Non-production of listed documents and non-supply of witness statements", "14(11), 14(13)", 1],
                ["Inspection", "The 19 documents produced within the permitted time satisfy r.14(11)(i) as to those documents", "14(11)(i)", 1],
                ["Production", "For documents in the Government's possession but not produced, r.14(13) permits only production or a non-availability certificate; “in a sealed cover in another division” is neither", "14(13)", 2],
                ["Witness statements", "Copies of the statements of listed witnesses must be furnished not later than three days before examination; refusal with no reason is a defect", "Note to 14(11)", 2],
                ["Prejudice", "The defence identifies the documents and what they would establish; that is a concrete claim of prejudice, not a bare assertion, and it must be answered in the report", "B. Karunakar (1993); Chandrama Tewari (1988)", 2],
                ["Course", "The report must record a finding on the prejudice claim; if it is accepted, the inquiry reopens for those documents only", "15(1)", 1]],
         wrong=["<b>“Every non-supply vitiates the inquiry.”</b> Prejudice must be shown, and here it must be articulated document by document.",
                "<b>“A sealed cover is a lawful ground of refusal.”</b> Only production or a non-availability certificate is contemplated.",
                "<b>“Witness statements can be supplied at the hearing.”</b> The rule fixes three days before examination."],
         answer=("The refusal of the two documents was contrary to <b>r.14(13)</b> and the refusal of the statements to the <b>Note to r.14(11)</b>; because "
                 "the defence has shown specific prejudice, the report must decide that claim, and if it is accepted the inquiry reopens on those documents."),
         model=("Smt D's inquiry is governed by rule 14 of the CCS (CCA) Rules, 1965. Inspection of the listed documents was offered within the time "
                "allowed by rule 14(11)(i), and for two documents a non-availability certificate was issued as rule 14(13) permits. For two documents, "
                "however, neither production nor a certificate was furnished: the reason recorded — that they lie in a sealed cover in another division — "
                "is not a ground recognised by rule 14(13), which requires production or a certificate of non-availability within one month of requisition. "
                "Copies of the statements of listed witnesses stand on a different footing: the Note to rule 14(11) requires them to be furnished not later "
                "than three days before the witness is examined, and no reason for refusal appears. The consequence is not automatic nullity. Following "
                "B. Karunakar (1993) and Chandrama Tewari (1988), non-supply vitiates the proceeding only where prejudice is shown; here the defence has "
                "identified the documents and the use it would make of them, which is a specific claim and not a bare assertion. The inquiry report must "
                "therefore decide that claim. If it is accepted, the inquiry reopens for production and inspection of those two documents and for the "
                "supply of the statements, and the employee must be heard on them before findings are recorded."),
         tags=[["14(11)", "Rule 14(11) — inspection and adjournment"], ["14(13)", "Rule 14(13) — production of documents"],
               ["14(14)", "Rule 14(14) — examination of witnesses"], ["15(1)", "Rule 15(1) — remission for further inquiry"]]),

    dict(id="L2-05", title="Three clear days — and a witness nobody listed",
         facts=("At the hearing on 12.10.2026 the Presenting Officer closed the departmental evidence. On 19.10.2026 he applied to examine "
                "one more witness, a cashier whose name was not in the list served with the charge sheet, saying she had been traced late. "
                "The inquiry authority allowed the application and fixed 27.10.2026. The employee objected that he had had no notice and no "
                "statement of the new witness. The authority recorded that he would have “ample time” and proceeded on 27.10.2026."),
         record=[["Departmental evidence closed", "12.10.2026", "—"],
                 ["Application for new witness", "19.10.2026", "not in the original list"],
                 ["Date fixed", "27.10.2026", "8 calendar days later"],
                 ["Statement of new witness", "not supplied", "—"],
                 ["Objection", "recorded", "overruled"]],
         questions=["What does r.14(15) require before a newly introduced witness is examined?",
                    "Was the interval of eight calendar days sufficient?",
                    "Does the absence of a statement of the new witness matter?",
                    "What order should the inquiry authority have passed?"],
         path=["new evidence after closure", "r.14(15)", "3 clear days", "plus statement 3 days before", "otherwise recall or exclude"],
         steps=[["Issue", "Introduction of evidence not in the list after the departmental case closed", "14(15)", 1],
                ["The rule", "Where the Presenting Officer applies to produce evidence not included in the list, the inquiry authority must adjourn for not less than three clear days", "14(15)", 2],
                ["Clear days", "27.10.2026 is the eighth calendar day after 19.10.2026, so three clear days are available on the face of the record; the objection on that ground fails", "14(15)", 2],
                ["But the statement", "The requirement in the Note to r.14(11) — copies not later than three days before examination — applies to every listed or newly introduced witness; a witness with no statement leaves nothing to cross-examine against", "Note to 14(11)", 2],
                ["Cure", "The authority should adjourn, direct supply of the statement, and then examine the witness; the 27.10.2026 evidence is irregular but curable by recall", "14(15); B. Karunakar (1993)", 1]],
         wrong=["<b>“Three clear days means three working days.”</b> Clear days exclude both termini; they need not be working days.",
                "<b>“A new witness can never be introduced.”</b> Rule 14(15) expressly contemplates it.",
                "<b>“The evidence is void.”</b> It is irregular and curable, not void, absent prejudice."],
         answer=("The three-clear-day requirement in <b>r.14(15)</b> was met, but examining a new witness without supplying a copy of her statement "
                 "breached the <b>Note to r.14(11)</b>; the evidence is irregular and curable by adjourning, supplying the statement and recalling the witness."),
         tags=[["14(15)", "Rule 14(15) — three clear days"], ["14(11)", "Rule 14(11) — witness statements"],
               ["14(14)", "Rule 14(14) — examination of witnesses"]]),

    dict(id="L2-06", title="The inquiry that ran into its second year",
         facts=("The inquiry authority was appointed on 09.01.2026. No extension was sought. The report was signed on 14.10.2026. "
                "The record shows sittings on 12 of the 40 weeks, three adjournments sought by the Presenting Officer, two by the employee, "
                "and one period of five months in which nothing happened because the authority was on deputation. The employee's defence is "
                "that the delay itself vitiates the inquiry; the department says the timeline is directory."),
         record=[["Appointment of I.A.", "09.01.2026", "6 months run from here"],
                 ["Six months expire", "09.07.2026", "no extension sought"],
                 ["Report signed", "14.10.2026", "3 months beyond"],
                 ["Sittings", "12 in 40 weeks", "—"],
                 ["Inactivity", "5 months", "I.A. on deputation"]],
         questions=["What is the statutory limit for completing the inquiry, and from when does it run?",
                    "What was the last date for the report without an extension?",
                    "Is the delay fatal?",
                    "What is the employee's best argument, and what must the disciplinary authority record?"],
         path=["r.14(24)", "6 months from appointment", "expired 08.07.2026", "no extension", "delay ≠ automatic nullity", "prejudice must be shown"],
         steps=[["Issue", "Completion of the inquiry beyond the statutory period, without extension", "14(24)", 1],
                ["The clock", "Six months from 09.01.2026 ended on <b>09.07.2026</b>; an extension had to be sought before expiry, in writing, with reasons, and could be up to six months at a time", "14(24)(a)–(c)", 2],
                ["Breach", "The report of 14.10.2026 is three months beyond the limit, and no extension order exists; the authority acted outside the rule", "14(24)", 2],
                ["Consequence", "The limit is directory in form; delay does not automatically vitiate unless it has caused prejudice to the defence — a proposition to be argued, not assumed", "14(24); Ajay Kumar Choudhary (2015), by analogy", 2],
                ["Prejudice here", "Five months of inactivity by an authority on deputation, with witnesses' memories ageing and one witness since retired, is material prejudice the employee can point to", "14(24)", 1],
                ["Cure and recording", "The disciplinary authority should record its view on prejudice before acting on the report; a fresh inquiry is not the automatic remedy", "15(1)", 1]],
         wrong=["<b>“The inquiry is void because the six months expired.”</b> The limit is directory; prejudice decides.",
                "<b>“An extension can be granted later with retrospective effect.”</b> The rule requires it before expiry, for recorded reasons.",
                "<b>“The 18-month target is the statutory limit.”</b> That is an administrative target, not the rule."],
         answer=("Six months from 09.01.2026 ended on <b>09.07.2026</b>; the report of 14.10.2026 was outside r.14(24) with no extension, but the breach "
                 "vitiates only on proof of prejudice — which the employee has a substantial argument for, given five months of inactivity."),
         tags=[["14(24)", "Rule 14(24) — completion of the inquiry"], ["15(1)", "Rule 15(1) — remission for further inquiry"]]),

    dict(id="L2-07", title="The plea that was never recorded",
         facts=("At the first hearing on 05.05.2026 the employee produced a written statement denying the charges and said he wished to be heard "
                "in person. The inquiry authority's order sheet for that date reads: “Charged officer present. He denies the charges. Case adjourned "
                "to 02.06.2026 for departmental evidence.” At the next hearing the Presenting Officer examined three witnesses. The employee "
                "cross-examined two and declined the third. The report records that “the charged officer pleaded not guilty”. No signed record of "
                "the plea appears on the file, and the employee now says he never pleaded and was never asked."),
         record=[["First hearing", "05.05.2026", "denial noted, no signed plea"],
                 ["Adjourned to", "02.06.2026", "departmental evidence"],
                 ["Witnesses examined", "3", "two cross-examined"],
                 ["Report", "—", "records “not guilty”"]],
         questions=["What does r.14(9) require when the employee appears and does not admit the charges?",
                    "What is the effect of the missing signed record?",
                    "Can the defect be cured at this stage?",
                    "Does it matter that he cross-examined the witnesses?"],
         path=["appearance", "r.14(9) ask guilty or defence", "record plea, sign, obtain signature", "omission = irregular", "cure by recording before findings"],
         steps=[["Issue", "Recording of the plea and its consequences", "14(9)–(10)", 1],
                ["The duty", "On appearance the inquiry authority must ask whether the employee is guilty or has a defence; if he pleads guilty, the plea must be recorded, signed and countersigned by him", "14(9)", 2],
                ["What happened", "The order sheet records a denial, not an inquiry into the plea; there is no signed record. The duty under r.14(9) was not performed in the manner the rule requires", "14(9)", 2],
                ["Consequence", "It is an irregularity in the record; since the employee participated, cross-examined and denied the charges, no prejudice arises from the absence of a signed plea, and the findings on the merits stand", "14(9); B. Karunakar (1993)", 2],
                ["Cure", "Before the report is acted on, the authority should record the plea afresh on the basis of the order sheet, or note the denial expressly in the report", "14(9)–(10), 14(23)", 1],
                ["If he had pleaded guilty", "The authority would still have to record findings on each charge after such evidence as it thinks fit, and act under r.15 — a plea is not the end of the case", "14(5)(a), 14(10)", 1]],
         wrong=["<b>“A guilty plea ends the inquiry.”</b> Findings and r.15 still follow.",
                "<b>“The report is void.”</b> The omission is an irregularity in the record, and no prejudice is shown.",
                "<b>“The plea can be inferred from cross-examination.”</b> The rule requires it to be asked and recorded."],
         answer=("The inquiry authority failed to perform the duty under <b>r.14(9)</b> to ask and record the plea, but since the employee denied the "
                 "charges and participated fully, the irregularity caused no prejudice and can be cured by recording the denial before the report is acted on."),
         tags=[["14(9)", "Rule 14(9) — plea"], ["14(10)", "Rule 14(10) — findings on admitted charges"],
               ["14(23)", "Rule 14(23) — the inquiry report"]]),

    dict(id="L2-08", title="The report, the disagreement and the missing note",
         facts=("The inquiry authority found charge 1 not proved and charges 2 and 3 proved. The disciplinary authority, a Joint Secretary, "
                "disagreed on charge 1 and proposed to hold it proved. A copy of the report was supplied to the employee with a covering letter "
                "asking for his representation within 15 days. No reasons for the disagreement were communicated. The employee's representation "
                "says he “notes the conclusions”. The disciplinary authority then imposed a reduction to a lower stage for two years."),
         record=[["Report", "charge 1 not proved; 2 and 3 proved", "—"],
                 ["Disagreement", "charge 1", "tentative reasons not communicated"],
                 ["Report supplied", "yes", "15 days given"],
                 ["Representation", "filed", "does not address the disagreement"],
                 ["Penalty", "reduction, two years", "r.11(v)"]],
         questions=["What does r.15(2) require where the disciplinary authority disagrees with the report?",
                    "Does the employee's silence cure the omission?",
                    "What is the consequence for the finding on charge 1?",
                    "Can the penalty on charges 2 and 3 stand?"],
         path=["report received", "tentative reasons for disagreement", "communicate to employee", "15 days", "findings recorded", "penalty"],
         steps=[["Issue", "Disagreement with the inquiry report and the opportunity on it", "15(2)", 1],
                ["The rule", "The report must be supplied together with the authority's own <i>tentative reasons for disagreement</i>, and the employee may represent within 15 days", "15(2)", 2],
                ["Breach", "The report was supplied but the tentative reasons were not; the employee was therefore never given the case he had to meet on charge 1", "15(2)", 2],
                ["Silence", "A representation that fails to address an uncommunicated disagreement cannot amount to waiver; he could not have known the reasons", "15(2)", 1],
                ["Consequence", "The finding on charge 1 is vitiated and must be re-made after communicating the reasons; the penalty, being a composite one influenced by that finding, cannot be sustained as it stands", "15(2), 15(4)", 2],
                ["What survives", "The findings on charges 2 and 3 are untouched, and the disciplinary authority may re-impose a penalty on them after fresh consideration", "15(4)–(6)", 1]],
         wrong=["<b>“The report alone is enough.”</b> Where the authority disagrees, its tentative reasons are part of the material that must be supplied.",
                "<b>“He did not object, so he waived it.”</b> Waiver requires knowledge.",
                "<b>“Only charge 1 is affected.”</b> A composite penalty must be reconsidered as a whole."],
         answer=("Failure to communicate the tentative reasons for disagreement breached <b>r.15(2)</b>; the finding on charge 1 must be re-made after "
                 "supplying them, and the composite penalty must be reconsidered on the surviving findings."),
         model=("The disciplinary authority's power to differ from its inquiry authority is undoubted, but rule 15(2) of the CCS (CCA) Rules, 1965 makes "
                "the disagreement a matter of record before it is acted on: a copy of the report must be forwarded with the authority's own tentative "
                "reasons for disagreement on any article of charge, and the Government servant must be allowed fifteen days to represent. Here the report "
                "was supplied but the reasons for differing on charge 1 were not, so the employee was asked to answer a case whose basis he could not see. "
                "The fact that his representation did not deal with the disagreement cannot cure the omission, because waiver presupposes knowledge of "
                "what is waived. The finding on charge 1 is therefore vitiated and must be re-made after the tentative reasons are communicated and a "
                "fresh representation considered. The findings on charges 2 and 3 are unaffected, but the penalty of reduction for two years was imposed "
                "on the three charges as a whole and cannot stand unaltered; the authority must reconsider the penalty on the surviving findings, recording "
                "its reasons as rule 15(4) requires."),
         tags=[["15(2)", "Rule 15(2) — report and tentative reasons for disagreement"], ["15(4)", "Rule 15(4) — findings on the representation"],
               ["15(6)", "Rule 15(6) — penalty without a second show-cause"]]),

    dict(id="L2-09", title="The show-cause that no longer exists",
         facts=("A major-penalty order dated 30.09.2026 imposes compulsory retirement. The file shows: charge sheet, inquiry, report holding two "
                "charges proved, a copy of the report supplied on 12.08.2026 with 15 days to represent, a representation, and the order. It does "
                "not show any notice proposing the penalty or any representation on the proposed penalty. The employee's appeal says the order is "
                "void because he was never heard on the penalty. He cites a commentary that sets out rule 15 in its pre-2014 form."),
         record=[["Report", "two charges proved", "—"],
                 ["Report supplied", "12.08.2026", "15 days given"],
                 ["Representation", "filed 26.08.2026", "considered"],
                 ["Proposed-penalty notice", "none", "pre-2014 requirement"],
                 ["Order", "30.09.2026", "compulsory retirement"]],
         questions=["What did rule 15 require before 31.10.2014, and what does it require now?",
                    "Is the absence of a proposed-penalty notice a defect?",
                    "How should the appellate authority deal with the commentary relied on?",
                    "Is the penalty otherwise sustainable?"],
         path=["major penalty", "inquiry under r.14", "report → r.15(2) representation", "r.15(6): no further opportunity", "order valid"],
         steps=[["Issue", "Whether a major penalty requires a second show-cause on the proposed penalty", "15(2), 15(6)", 1],
                ["The obsolete rule", "Before the Second Amendment of 31.10.2014, rule 15 required a notice of the penalty proposed and a representation on it; the rule was recast with effect from that date", "⊘ pre-2014 r.15", 2],
                ["The current rule", "After the report, the authority supplies it with any disagreement note, considers the representation, records findings, and may impose a major penalty; r.15(6) expressly dispenses with a further opportunity", "15(2), 15(4), 15(6)", 2],
                ["Application", "The report was supplied, 15 days were given, a representation was filed and considered; the requirements are satisfied and no proposed-penalty notice was needed", "15(2), 15(4)", 2],
                ["The appeal", "The ground fails; the commentary is outdated and cannot be followed against the text", "15(6)", 1],
                ["Residual check", "The authority must still have applied its mind and recorded reasons; if the order is a bare conclusion, that — not the absent notice — is the appealable defect", "15(4), 17", 1]],
         wrong=["<b>“Natural justice always requires a show-cause on the penalty.”</b> For major penalties the statutory scheme now places the opportunity at the report stage.",
                "<b>“The commentary is authority.”</b> A commentary cannot displace the text as amended.",
                "<b>“Without the second show-cause the order is void.”</b> The requirement no longer exists."],
         answer=("No proposed-penalty notice was required: after the 2014 amendment the opportunity is on the inquiry report under <b>r.15(2)</b>, and "
                 "<b>r.15(6)</b> dispenses with any further representation on the penalty. The appeal ground therefore fails."),
         tags=[["15", "Rule 15 — action on the inquiry report"], ["15(6)", "Rule 15(6) — no second show-cause"],
               ["17", "Rule 17 — communication of orders"]]),

    dict(id="L2-10", title="The advice nobody showed him",
         facts=("The disciplinary authority proposed to impose removal on an officer holding a Group ‘A’ post and referred the case to the Union "
                "Public Service Commission. The Commission advised that the penalty be reduced to withholding of one increment for two years. "
                "The disciplinary authority accepted the advice and passed the order on 18.07.2026. A copy of the advice was placed on the file "
                "but not sent to the officer. He learned of it from the order, which recites that the Commission was consulted."),
         record=[["Reference to UPSC", "12.05.2026", "consultation necessary"],
                 ["Advice", "reduction to one increment, 2 years", "—"],
                 ["Advice supplied to employee", "no", "only on the file"],
                 ["Order", "18.07.2026", "in terms of the advice"]],
         questions=["Was consultation with the Commission necessary?",
                    "What does the rule require after the advice is received?",
                    "What is the consequence of not supplying it?",
                    "What should the disciplinary authority do now?"],
         path=["consultation necessary", "advice received", "supply copy to employee", "15 days to represent", "then order"],
         steps=[["Issue", "Supply of the Commission's advice before the penalty", "15(3)(b), 32", 1],
                ["Consultation", "Consultation is required where the rules so provide; once made, the advice becomes part of the material on which the order rests", "15(3)(a)", 2],
                ["The duty", "A copy of the advice must be forwarded to the employee, who may represent within 15 days; rule 32 states the general obligation", "15(3)(b), 32", 2],
                ["Breach", "The advice was not supplied, so the officer was denied the opportunity to meet the very material that decided the penalty", "15(3)(b)", 2],
                ["Consequence", "The order is vitiated to that extent; the position follows S.K. Kapoor v. Union of India (2010) and is now reflected in the rules", "15(3)(b); S.K. Kapoor (2010)", 2],
                ["Cure", "Supply the advice, allow 15 days, consider the representation and pass a fresh order — the penalty need not be re-agitated on the merits", "15(3)(b), 15(4)", 1]],
         wrong=["<b>“The advice is confidential.”</b> The rule requires it to be supplied.",
                "<b>“He could have asked for it.”</b> The duty is on the authority.",
                "<b>“The whole inquiry is void.”</b> Only the stage after the advice is affected; the inquiry stands."],
         answer=("Not supplying the Commission's advice breached <b>r.15(3)(b)</b> (and, for a minor penalty, <b>r.16(1)(d)</b>); the order is vitiated and must be re-made after "
                 "supplying the advice and allowing <b>15 days</b> to represent."),
         tags=[["15(3)", "Rule 15(3) — consultation and supply of the Commission's advice"], ["16(1)", "Rule 16(1) — minor-penalty procedure"]]),

    dict(id="L2-11", title="Four years of withheld increments",
         facts=("A Group ‘C’ clerk was imposed the penalty of withholding of two increments for four years, without cumulative effect, by an "
                "order of 21.04.2026. He had been given a notice of the proposal and imputations on 02.02.2026, filed a representation on 20.02.2026, "
                "and was heard in person on 10.03.2026. No inquiry was held. The order records that an inquiry was “not considered necessary”. "
                "The penalty will postpone his next increment and, on his own calculation, reduce his pensionable average emoluments."),
         record=[["Proposal and imputations", "02.02.2026", "r.16(1)(a)"],
                 ["Representation", "20.02.2026", "considered"],
                 ["Personal hearing", "10.03.2026", "—"],
                 ["Inquiry", "none", "“not considered necessary”"],
                 ["Penalty", "two increments, 4 years", "r.11(iv)"]],
         questions=["Is withholding of increments a minor penalty?",
                    "Was an inquiry mandatory in these facts?",
                    "What is the effect of the four-year duration and the pension consequence?",
                    "What is the consequence of the omission?"],
         path=["r.11(iv) minor", "but r.16(1-A)", ">3 years → inquiry", "also pension effect", "inquiry mandatory", "order vitiated"],
         steps=[["Issue", "Whether an inquiry was mandatory for withholding of increments", "16(1), 16(1-A)", 1],
                ["Classification", "Withholding of increments is a minor penalty under r.11(iv), and minor penalties ordinarily follow the r.16 procedure without an inquiry", "11(iv), 16(1)", 1],
                ["The trigger", "An inquiry in the manner of r.14(3)–(23) is mandatory where the withholding is for more than three years, or is cumulative, or is likely to affect pension adversely", "16(1-A)", 3],
                ["Application", "Four years exceeds three, and the order itself postpones the next increment with a pension effect; the trigger operates on either limb", "16(1-A)", 2],
                ["Consequence", "The order is vitiated for want of the mandatory inquiry; the notice-and-representation route under r.16(1)(a) is not a substitute", "16(1-A)", 2],
                ["Course", "The authority may re-open the case and hold the inquiry; it cannot cure the defect by a fresh personal hearing alone", "16(1-A), 16(1)(b)", 1]],
         wrong=["<b>“It is a minor penalty, so no inquiry is needed.”</b> Rule 16(1-A) makes the procedure major for certain minor penalties.",
                "<b>“Four years is within the three-year limit because it is not cumulative.”</b> Duration and cumulation are separate triggers.",
                "<b>“A personal hearing cures it.”</b> The rule requires an inquiry in the manner of r.14(3)–(23)."],
         answer=("Although withholding of increments is a minor penalty, the four-year duration and the pension effect attracted <b>r.16(1-A)</b>; no inquiry "
                 "was held, so the order of 21.04.2026 is vitiated and the case must be re-opened."),
         tags=[["11", "Rule 11 — penalties"], ["16", "Rule 16 — minor penalties"],
               ["16(1-A)", "Rule 16(1-A) — mandatory inquiry for certain minor penalties"]]),
]
