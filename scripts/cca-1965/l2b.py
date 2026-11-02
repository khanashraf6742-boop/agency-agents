# -*- coding: utf-8 -*-
"""L2 standard cases 12–22 — competence, penalties and money."""

L2B = [
    dict(id="L2-12", title="Censure recorded in the confidential roll",
         facts=("On 06.06.2026 the controlling officer recorded a censure in Shri E's confidential roll for a delay in reconciling a ledger, "
                "after an oral discussion. No written proposal, no statement of imputations and no opportunity of representation was given. "
                "The entry says: “Censured orally on 06.06.2026; recorded for future reference.” Shri E came to know of it when his promotion "
                "file was considered in September 2026."),
         record=[["Oral discussion", "02.06.2026", "no record"],
                 ["Censure recorded", "06.06.2026", "no notice, no representation"],
                 ["Knowledge", "September 2026", "promotion file"],
                 ["Limitation for appeal", "45 days", "from delivery of the order"]],
         questions=["Is a censure a penalty, and what procedure does it require?",
                    "Does an oral censure become a penalty when it is recorded?",
                    "From when does the appeal period run?",
                    "What is the remedy?"],
         path=["censure = r.11(i)", "r.16(1)(a) notice + representation", "no notice", "order void", "appeal from communication"],
         steps=[["Issue", "Whether censure can be imposed without notice and representation", "11(i), 16(1)(a)", 1],
                ["Classification", "Censure is a minor penalty under r.11(i) and attracts the r.16 procedure", "11(i), 16(1)", 1],
                ["The requirement", "The employee must be informed in writing of the proposal and the imputations and given a reasonable opportunity to represent; a finding must be recorded on each imputation", "16(1)(a), (c), (e)", 2],
                ["Application", "An oral discussion followed by an entry in the confidential roll satisfies neither limb; the entry is an order imposing a penalty without the procedure", "16(1)", 2],
                ["Limitation", "The order was never communicated; limitation runs from delivery, and the 45 days began when the entry was made known to him in September 2026", "25, 30", 1],
                ["Remedy", "He may appeal under r.23(ii); the penalty is liable to be set aside for want of procedure, leaving the administration free to commence a regular proceeding", "23(ii), 16(1)", 1]],
         wrong=["<b>“A censure is only a warning, so no procedure is needed.”</b> It is a penalty; the procedure is short, not absent.",
                "<b>“Recording an oral censure is a formality.”</b> The record is the order.",
                "<b>“The appeal is time-barred.”</b> Limitation runs from delivery, which had not occurred."],
         answer=("Censure is a penalty under <b>r.11(i)</b> and required the <b>r.16(1)(a)</b> notice and opportunity; the entry is void for want of "
                 "procedure, and limitation for the appeal ran from its communication in September 2026."),
         tags=[["11", "Rule 11 — penalties"], ["16", "Rule 16 — minor penalties"], ["25", "Rule 25 — limitation"],
               ["30", "Rule 30 — service of orders"]]),

    dict(id="L2-13", title="Two officials, one transaction",
         facts=("A payment of ₹9,60,000 was made without sanction. The Drawing Officer, Smt F (Group ‘B’), verified it; the cashier, Shri G "
                "(Group ‘C’), disbursed it. Both face the same imputations. The disciplinary authority competent to dismiss both is the Joint "
                "Secretary (Administration). She proposes a common proceeding, with herself as the disciplinary authority for both. The appointing "
                "authority of Smt F is the Deputy Secretary; of Shri G, the Under Secretary. Smt F objects that the proceeding is bad because "
                "different authorities are involved and because she is a Group ‘B’ officer while the cashier is Group ‘C’."),
         record=[["Transaction", "₹9,60,000 unsanctioned", "same facts"],
                 ["Smt F", "Group ‘B’, Drawing Officer", "appointing authority: Deputy Secretary"],
                 ["Shri G", "Group ‘C’, cashier", "appointing authority: Under Secretary"],
                 ["Proposed DA", "Joint Secretary", "competent to dismiss both"]],
         questions=["What does rule 18 require for a common proceeding?",
                    "Is the Joint Secretary competent as the common disciplinary authority?",
                    "Can the two receive different penalties in one proceeding?",
                    "Is Smt F's objection about groups well founded?"],
         path=["same case, two servants", "r.18(1) common proceeding", "authority competent to dismiss all", "one authority conducts", "penalties may differ"],
         steps=[["Issue", "Common proceedings against two Government servants concerned in one case", "18(1)–(3)", 1],
                ["The condition", "Where two or more Government servants are concerned in any case, an authority competent to impose dismissal on all of them may order a common proceeding", "18(1)", 2],
                ["Competence here", "The Joint Secretary is competent to dismiss both, so the condition is satisfied even though the appointing authorities differ", "18(1), 18(2)", 2],
                ["Groups", "The difference of groups is irrelevant once a single authority is competent for both; Explanation II to r.12 deals with a servant promoted to a higher group, not with joint proceedings", "18(2); r.12", 2],
                ["Different penalties", "A common proceeding is a common inquiry, not a common penalty; the authority may impose different penalties on the two, for recorded reasons", "18(3), 15(6)", 1],
                ["Objection", "Smt F's objection fails; her remedy on the merits is an appeal to the appellate authority competent for her", "18, 23–24", 1]],
         wrong=["<b>“A common proceeding needs identical appointing authorities.”</b> It needs one authority competent to dismiss all.",
                "<b>“A common proceeding must end in identical penalties.”</b> The inquiry is common; the penalty is individual.",
                "<b>“The Group difference makes it invalid.”</b> Competence is what matters."],
         answer=("A common proceeding is competent under <b>r.18(1)</b> because the Joint Secretary can dismiss both; differing groups and appointing "
                 "authorities do not bar it, and the penalties may differ if reasons are recorded."),
         tags=[["18", "Rule 18 — common proceedings"], ["12", "Rule 12 — disciplinary authorities"],
               ["15", "Rule 15 — action on the inquiry report"]]),

    dict(id="L2-14", title="Reasons written a month after the order",
         facts=("A Superintendent of Central Excise was dismissed on 22.01.2026 under rule 19(ii). The order records only that “the disciplinary "
                "authority is satisfied that it is not reasonably practicable to hold an inquiry”. On 26.02.2026, after the dismissal, the "
                "authority issued a detailed note explaining that two witnesses had turned hostile and one had threatened the others. The employee's "
                "appeal relies on the absence of reasons in the order."),
         record=[["Dismissal order", "22.01.2026", "no reasons recorded"],
                 ["Explanatory note", "26.02.2026", "after the order, after the appeal"],
                 ["Ground relied on", "19(ii)", "not reasonably practicable"],
                 ["Statutory safeguard", "Commission consultation", "record silent"]],
         questions=["What must a disciplinary authority record before invoking rule 19(ii)?",
                    "Can the reasons be supplied later?",
                    "What is the standard of review of the satisfaction?",
                    "What follows for the order?"],
         path=["r.19(ii)", "satisfaction of the D.A.", "reasons in writing", "contemporaneous", "reviewable for relevance", "post-facto reasons fail"],
         steps=[["Issue", "Invocation of r.19(ii) without reasons in the order", "19(ii)", 1],
                ["The condition", "The disciplinary authority must be satisfied, for reasons recorded by it in writing, that it is not reasonably practicable to hold an inquiry in the manner provided", "19(ii)", 2],
                ["Timing", "The reasons must exist and be recorded when the power is exercised; a note issued five weeks later, after the appeal, is not a record of the satisfaction but a reconstruction of it", "19(ii)", 2],
                ["Review", "The satisfaction is not immune: the reasons are open to examination for their relevance, and the court does not substitute its own satisfaction for the authority's", "Tulsiram Patel (1985)", 2],
                ["The note", "Even taken at face value, hostile witnesses and a threat to witnesses would ordinarily call for protection of witnesses, not abandonment of the inquiry", "19(ii)", 1],
                ["Consequence", "The order is unsustainable; the matter must be remitted for a regular inquiry, and the employee is entitled to consequential treatment", "19(ii); 10(4)–(5)", 1],
                ["Commission", "Where consultation is necessary it must be made and the advice supplied — the record is silent on this", "19, second proviso", 1]],
         wrong=["<b>“Rule 19 needs no reasons.”</b> The sub-rule itself requires reasons in writing.",
                "<b>“Reasons can be given later to defend the order.”</b> That is after-the-event justification.",
                "<b>“The court will decide whether an inquiry was practicable.”</b> It examines relevance, not sufficiency."],
         answer=("Rule 19(ii) requires reasons recorded when the power is exercised; a note five weeks later cannot cure their absence, and on the facts "
                 "the reasons would not have justified abandoning the inquiry, so the dismissal falls and a regular inquiry must be held."),
         model=("Rule 19(ii) of the CCS (CCA) Rules, 1965 allows the disciplinary authority to dispense with the inquiry only where it is satisfied, for "
                "reasons recorded by it in writing, that it is not reasonably practicable to hold one. The requirement is not decorative: the record is "
                "the means by which the discretion is kept within its purpose, and the reasons must exist at the time the power is exercised. Here the "
                "order of 22.01.2026 records the satisfaction but no reason, and the explanation of 26.02.2026 — issued after the dismissal and after the "
                "appeal — is a reconstruction rather than a record. Following Union of India v. Tulsiram Patel (1985), the satisfaction is open to review "
                "for the relevance of the reasons given, though not for their sufficiency, and the court will not substitute its own view of what was "
                "practicable. Even taken at its highest, the later note describes witnesses who turned hostile and a threat to witnesses: those are grounds "
                "for protecting the inquiry, not for abandoning it. The dismissal is therefore unsustainable. The appropriate course is remission for a "
                "regular inquiry, and the authority must also satisfy the requirement of consultation, and supply the Commission's advice where "
                "consultation is necessary."),
         tags=[["19", "Rule 19 — special procedure"], ["19(ii)", "Rule 19(ii) — not reasonably practicable"],
               ["15", "Rule 15 — action on the inquiry report"]]),

    dict(id="L2-15", title="The removal signed by the Head of Office",
         facts=("Shri H, a Group ‘C’ Auditor, was removed from service by an order of the Head of Office dated 11.04.2026 after a regular inquiry. "
                "The appointing authority for the post is the Accountant General. The Head of Office is three levels below the Accountant General "
                "and is authorised to impose minor penalties on Group ‘C’ staff. The inquiry was otherwise regular, the charges were proved, and the "
                "penalty was endorsed by the Deputy Accountant General after the event."),
         record=[["Appointing authority", "Accountant General", "r.12(2)"],
                 ["Order passed by", "Head of Office", "r.12(3) powers only"],
                 ["Penalty", "removal", "r.11(viii), major"],
                 ["Endorsement", "Deputy AG, after the order", "post facto"],
                 ["Inquiry", "regular", "no procedural defect"]],
         questions=["Who was competent to impose removal?",
                    "Can the defect be cured by the endorsement?",
                    "Does the regularity of the inquiry save the order?",
                    "What is the consequence, and what may the department do next?"],
         path=["major penalty", "r.12(2) authority", "never subordinate to appointing authority", "r.12(4)(a)", "order void", "cannot be ratified"],
         steps=[["Issue", "Competence to impose a major penalty", "12(2), 12(4)(a)", 1],
                ["The rule", "A major penalty must be imposed by the authority competent under r.12, and no penalty under r.11(v)–(ix) may be imposed by any authority subordinate to the appointing authority", "12(2), 12(4)(a)", 2],
                ["Application", "The Head of Office is three levels below the appointing authority; his r.12(3) power is confined to minor penalties on Group ‘C’ staff", "12(3), 12(4)(a)", 2],
                ["Nullity", "A penalty imposed by an authority without jurisdiction is void, not merely irregular; a regular inquiry cannot supply the want of competence", "12(4)(a)", 2],
                ["Ratification", "Approval after the order cannot validate it; competence must exist when the order is made", "12(4)(a)", 1],
                ["Consequence", "The order is set aside; the department may direct the competent authority to pass a fresh order on the existing inquiry record after applying its mind", "12(2), 15(6)", 2]],
         wrong=["<b>“The Head of Office can impose any penalty on Group ‘C’ staff.”</b> Rule 12(3) stops at minor penalties.",
                "<b>“The Deputy AG's endorsement cures it.”</b> Ratification after the event is not competence.",
                "<b>“A good inquiry saves a bad order.”</b> Competence is jurisdictional."],
         answer=("Removal could be imposed only by the authority competent under <b>r.12(2)</b>; the Head of Office was barred by <b>r.12(4)(a)</b>, so the "
                 "order is void and cannot be ratified — a fresh order by the competent authority is required."),
         tags=[["12", "Rule 12 — disciplinary authorities"], ["12(4)", "Rule 12(4) — limits on competence"],
               ["11", "Rule 11 — penalties"]]),

    dict(id="L2-16", title="A minor penalty that the Head of Office could impose",
         facts=("Smt I, a Group ‘C’ clerk in a subordinate office, was censured by the Head of Office on 03.03.2026 after notice and a representation. "
                "The appointing authority for her post is the Head of Department, who is two levels above. The Head of Office is not lower in rank "
                "than the authority specified under r.12(2) for that office. The employee's appeal says the order is void for want of competence. "
                "The departmental instruction in force authorises Heads of Office to impose minor penalties on Group ‘C’ staff of their office."),
         record=[["Post", "Group ‘C’ clerk", "—"],
                 ["Penalty", "censure", "r.11(i), minor"],
                 ["Order by", "Head of Office", "not lower in rank than r.12(2) authority"],
                 ["Procedure", "notice + representation", "r.16(1)(a)"],
                 ["Appointing authority", "Head of Department", "two levels above"]],
         questions=["Is the Head of Office competent to impose a minor penalty here?",
                    "Does it matter that the appointing authority is higher?",
                    "What is the effect of the departmental instruction?",
                    "Would the answer differ for removal?"],
         path=["minor penalty", "r.12(3)", "Secretary or Head of Office", "rank condition satisfied", "competent", "major penalty? different answer"],
         steps=[["Issue", "Competence of a Head of Office to impose a minor penalty on Group ‘C’ staff", "12(3)", 1],
                ["The rule", "For Group ‘C’ (other than the Central Secretariat Clerical Service) and Group ‘D’, the Secretary of the Ministry or the Head of Office may impose a r.11 penalty, subject to the rank condition", "12(3)(a)–(b)", 2],
                ["Application", "The Head of Office is not lower in rank than the r.12(2) authority, and censure is a minor penalty; competence is established by r.12(3) itself, not merely by the instruction", "12(3)(b)", 2],
                ["The instruction", "It confirms the position; it cannot enlarge r.12 and would be irrelevant if it contradicted it", "12(3)", 1],
                ["Removal", "For a major penalty the answer changes: r.12(4)(a) bars any authority subordinate to the appointing authority, so the Head of Office could not impose it", "12(4)(a)", 2],
                ["Conclusion", "The censure is valid; the appeal on competence fails", "12(3)", 1]],
         wrong=["<b>“Only the appointing authority can impose any penalty.”</b> Rule 12(3) is an independent source of competence for minor penalties.",
                "<b>“Rule 12(3) allows any penalty.”</b> It allows a penalty under r.11, read with the bar in r.12(4)(a).",
                "<b>“The instruction is the source of power.”</b> The rule is."],
         answer=("The Head of Office was competent under <b>r.12(3)</b> to impose censure because the rank condition is satisfied; competence for a major "
                 "penalty would have been barred by <b>r.12(4)(a)</b>."),
         tags=[["12", "Rule 12 — disciplinary authorities"], ["12(3)", "Rule 12(3) — minor penalties on Group ‘C’/‘D’"]]),

    dict(id="L2-17", title="Institution by one authority, imposition by another",
         facts=("The Secretary of the Ministry directed, on 14.02.2026, that disciplinary proceedings be instituted against Shri J, a Group ‘A’ "
                "officer, and nominated the Additional Secretary to hold the inquiry. On the inquiry report, the Secretary imposed a penalty of "
                "reduction to a lower stage. The appointing authority for Shri J's post is the President; the Secretary is authorised by a general "
                "order to impose all penalties on Group ‘A’ officers of the Ministry other than the highest post. Shri J argues that the Secretary "
                "could not institute and decide the same case, and that in any event the President alone was competent."),
         record=[["Direction to institute", "Secretary, 14.02.2026", "r.13"],
                 ["Inquiry held by", "Additional Secretary", "nominated"],
                 ["Penalty by", "Secretary", "r.12(2) + general order"],
                 ["Appointing authority", "President", "—"],
                 ["General order", "empowers Secretary", "for Group ‘A’ posts"]],
         questions=["Who may institute proceedings under rule 13?",
                    "Was the Secretary competent to impose the penalty?",
                    "Is there any bar on the same authority instituting and deciding?",
                    "What would change if no general order existed?"],
         path=["r.13 institution", "r.12 imposition", "general order empowers", "competent", "no constitutional bar", "President's pleasure unaffected"],
         steps=[["Issue", "Competence to institute and to impose, and whether they must be different authorities", "13, 12(2)", 1],
                ["Institution", "The President or an authority empowered by general or special order may institute; a disciplinary authority may also do so. The Secretary is therefore competent if the general order covers the direction", "13", 2],
                ["Imposition", "A penalty may be imposed by the authority specified by general or special order; the Secretary's power for Group ‘A’ posts rests on that order read with r.12(2)", "12(2)(b)", 2],
                ["Same authority", "The Rules do not require the instituting and imposing authorities to differ; the safeguard is the inquiry, the report and the representation, not a separation of roles", "13, 14, 15", 2],
                ["Without the order", "Absent a general order, imposition would fall to the appointing authority, that is the President, and the Secretary's order would be without jurisdiction", "12(2)", 2],
                ["Pleasure", "The President's pleasure under Article 310 is unaffected by delegation of the rule-making power to impose penalties", "12(1)", 1]],
         wrong=["<b>“The same officer cannot institute and decide.”</b> Nothing in the Rules requires separation.",
                "<b>“Only the President can penalise a Group ‘A’ officer.”</b> A general order can empower another authority.",
                "<b>“The Secretary's direction to institute is itself the penalty.”</b> Institution is not imposition."],
         answer=("The Secretary acted within <b>r.13</b> and within the general order read with <b>r.12(2)</b>; the Rules do not require different "
                 "authorities for institution and imposition, and absent the general order the President alone could have imposed the penalty."),
         tags=[["13", "Rule 13 — authority to institute proceedings"], ["12", "Rule 12 — disciplinary authorities"]]),

    dict(id="L2-18", title="One stage down for two years",
         facts=("Shri K, in Level 7 with basic pay ₹49,000 fixed on 01.07.2025, annual increment on 1 July, was imposed the penalty of reduction "
                "by one stage for two years under r.11(v) by an order dated 20.06.2026, effective 01.07.2026. The order directs that he shall not "
                "earn increments during the period and that the reduction shall not postpone his future increments. The reduction was applied to the pay he "
                "was drawing on that day, ₹49,000, so the next lower stage in the level is ₹47,600."),
         record=[["Pay on 01.07.2025", "₹49,000", "Level 7"],
                 ["Increment date", "1 July", "annual"],
                 ["Penalty effective", "01.07.2026", "two years"],
                 ["Lower stage", "₹47,600", "one stage"],
                 ["DA for illustration", "63% ⚑", "from 01.07.2026"]],
         questions=["What is his pay during the penalty period?",
                    "What is the monetary loss over the two years?",
                    "What is his pay on 01.07.2028?",
                    "What difference would a direction postponing future increments have made?"],
         path=["r.11(v) reduction", "fix at lower stage", "no increments during period", "loss computed year by year", "restore to notional stage"],
         steps=[["Issue", "Pay fixation and monetary effect of a reduction to a lower stage", "11(v)", 1],
                ["Pay during the period", "Pay is fixed at the lower stage, <b>₹47,600</b>, from 01.07.2026 to 30.06.2028; no increment is earned because the order says so", "11(v); DoPT 18.06.2019", 2],
                ["Notional pay but for the penalty", "On 01.07.2026 he would have drawn ₹50,500 and on 01.07.2027 ₹52,000", "11(v)", 2],
                ["Loss, year 1", "(₹50,500 − ₹47,600) × 12 = <b>₹34,800</b>", "11(v)", 2],
                ["Loss, year 2", "(₹52,000 − ₹47,600) × 12 = <b>₹52,800</b>", "11(v)", 2],
                ["Total loss", "₹34,800 + ₹52,800 = <b>₹87,600</b> (basic pay only; DA follows the pay)", "11(v)", 1],
                ["On expiry", "Because the order does not postpone future increments, pay is fixed on 01.07.2028 at the stage he would have reached — <b>₹53,600</b> — and not at ₹49,000 or ₹50,500", "11(v); DoPT 18.06.2019", 2]],
         wrong=["<b>“He continues at ₹49,000.”</b> Reduction means the lower stage, not the same pay.",
                "<b>“Loss is ₹1,400 × 24 = ₹33,600.”</b> That ignores the increments he would have earned but for the penalty.",
                "<b>“On expiry he starts again from ₹49,000.”</b> Without a direction postponing future increments, he is placed at the notional stage."],
         answer=("Pay during the penalty is <b>₹47,600</b>; the loss is <b>₹87,600</b> over two years; and on 01.07.2028 his pay is fixed at "
                 "<b>₹53,600</b>, the stage he would have reached, because the order does not postpone future increments."),
         tags=[["11", "Rule 11 — penalties"], ["11(v)", "Rule 11(v) — reduction to a lower stage"]]),

    dict(id="L2-19", title="Reduction to a lower time-scale",
         facts=("Smt L, an Assistant Accounts Officer in Level 8, was imposed the penalty of reduction to the lower time-scale of Senior Accountant "
                "(Level 7) for three years, with a direction that she will not regain her original seniority in Level 8 on expiry. She was promoted "
                "to Level 8 on 01.04.2023 on the basis of seniority. After the penalty, a vacancy in Level 8 arose in 2027 and the department promoted "
                "a junior. She claims the penalty could not affect her seniority and that she should be considered for the 2027 vacancy."),
         record=[["Substantive post", "Assistant Accounts Officer, Level 8", "promoted 01.04.2023"],
                 ["Penalty", "reduction to Level 7, three years", "r.11(vi)"],
                 ["Direction", "no restoration of seniority", "express"],
                 ["Vacancy", "2027, Level 8", "junior promoted"],
                 ["Expiry", "three years", "seniority per direction"]],
         questions=["What are the incidents of a penalty under r.11(vi)?",
                    "Is the direction on seniority permissible?",
                    "Could she be considered for the 2027 vacancy?",
                    "What happens on expiry of the period?"],
         path=["r.11(vi)", "lower time-scale", "bar to promotion during period", "seniority direction", "restoration deferred", "promotion after expiry only"],
         steps=[["Issue", "Effect of a reduction to a lower time-scale on promotion and seniority", "11(vi)", 1],
                ["The penalty", "Reduction to a lower time-scale, grade, post or service for a specified period, which is a bar to promotion during that period to the time-scale from which she was reduced", "11(vi)", 2],
                ["The directions", "The order must state whether the period operates to postpone future increments and whether she regains original seniority on expiry; the direction here defers restoration", "11(vi)(a)–(b)", 2],
                ["Promotion during the period", "She cannot be promoted to Level 8 while the penalty runs; the 2027 promotion of a junior is therefore not by itself illegal", "11(vi)", 2],
                ["On expiry", "She regains the lower time-scale position and is considered for promotion thereafter, but without the seniority she would otherwise have had, because the direction says so", "11(vi)(b)", 2],
                ["Challenge", "Her remedy is to challenge the direction as disproportionate, not to assert a right to promotion during the penalty", "11(vi); proportionality cases", 1]],
         wrong=["<b>“A reduction penalty cannot affect seniority.”</b> Rule 11(vi) expressly directs the seniority consequence.",
                "<b>“She must be promoted in 2027 because a vacancy arose.”</b> The penalty is a statutory bar during its currency.",
                "<b>“On expiry seniority revives automatically.”</b> Only if the order so directs."],
         answer=("The penalty under <b>r.11(vi)</b> bars promotion to Level 8 during its three years and, on the direction given, defers restoration of "
                 "seniority; the 2027 promotion of a junior was therefore not illegal, and her challenge must be to the direction itself."),
         tags=[["11", "Rule 11 — penalties"], ["11(vi)", "Rule 11(vi) — reduction to a lower time-scale"]]),

    dict(id="L2-20", title="Recovery of more than was put to him",
         facts=("Shri M, a storekeeper, was given a notice on 09.01.2026 proposing recovery of ₹1,60,000 for pecuniary loss caused by negligence in "
                "the issue of stores. The notice set out the computation. He represented that the loss was ₹1,05,000 and produced the issue register. "
                "On 30.03.2026 the disciplinary authority imposed recovery of ₹2,40,000, adopting a revised computation prepared after the "
                "representation and never put to him. He has repaid nothing."),
         record=[["Notice", "09.01.2026", "₹1,60,000 proposed"],
                 ["Representation", "with register", "loss said to be ₹1,05,000"],
                 ["Revised computation", "not put to him", "₹2,40,000"],
                 ["Order", "30.03.2026", "recovery of ₹2,40,000"],
                 ["Penalty class", "r.11(iii), minor", "—"]],
         questions=["What is the maximum amount that could be recovered on this record?",
                    "What is the defect in the order?",
                    "Does the employee's own figure bind the authority?",
                    "What is the correct course?"],
         path=["r.11(iii) recovery", "quantum in the notice", "no enhancement without opportunity", "₹1,60,000 ceiling", "remit for fresh notice"],
         steps=[["Issue", "Recovery of pecuniary loss and the opportunity on quantum", "11(iii), 16(1)(a)", 1],
                ["The penalty", "Recovery must be of a pecuniary loss caused by negligence or breach of orders, and the amount must be quantified", "11(iii)", 1],
                ["The notice", "The proposal fixed the loss at ₹1,60,000; that is the case the employee was called upon to meet", "16(1)(a)", 2],
                ["Enhancement", "Recovering ₹2,40,000 on a computation prepared after the representation, and never supplied, denies the opportunity the rule requires and is unsustainable beyond ₹1,60,000", "16(1)(a), 16(1)(c)", 3],
                ["His figure", "His computation of ₹1,05,000 does not bind the authority; the authority may reject it for reasons, on the material", "16(1)(c), 16(1)(e)", 1],
                ["Course", "Recovery may be sustained up to ₹1,60,000; to recover more, a fresh notice with the revised computation and a fresh opportunity is necessary", "16(1)(a)", 2]],
         wrong=["<b>“The authority may recover whatever the audit works out.”</b> The employee must meet the figure proposed.",
                "<b>“His figure of ₹1,05,000 must be accepted.”</b> It is material for consideration, not a binding admission.",
                "<b>“The order is wholly void.”</b> It is good to the extent of the amount noticed."],
         answer=("Recovery is sustainable only up to <b>₹1,60,000</b>, the amount put to him; the increase to ₹2,40,000 on an uncommunicated "
                 "computation breaches <b>r.16(1)(a)</b> and requires a fresh notice and opportunity."),
         tags=[["11", "Rule 11 — penalties"], ["11(iii)", "Rule 11(iii) — recovery"],
               ["16", "Rule 16 — minor penalties"]]),

    dict(id="L2-21", title="Compulsory retirement: a penalty or a power?",
         facts=("Shri N, a Section Officer aged 56, was compulsory retired by an order dated 12.08.2026 under FR 56(j) after review of his service "
                "record. The order recites the review committee's recommendation that he is ineffective. A separate order of the same date imposes "
                "compulsory retirement under r.11(vii) after a departmental inquiry in which two charges were proved. He challenges both, saying "
                "that compulsory retirement is a penalty and cannot be imposed under FR 56(j) without an inquiry, and that two orders cannot stand."),
         record=[["Age", "56", "FR 56(j) available"],
                 ["Order 1", "FR 56(j), 12.08.2026", "service-record review"],
                 ["Order 2", "r.11(vii), 12.08.2026", "two charges proved"],
                 ["Inquiry", "held for order 2", "—"],
                 ["Effect sought", "same", "both end service"]],
         questions=["Is compulsory retirement under r.11(vii) the same thing as compulsory retirement under FR 56(j)?",
                    "Which order can stand?",
                    "What is the difference in consequence?",
                    "What should the department have done?"],
         path=["two distinct powers", "FR 56(j): public interest, no inquiry", "r.11(vii): penalty, inquiry", "one order must go", "elect before acting"],
         steps=[["Issue", "Whether FR 56(j) and r.11(vii) are alternative routes to the same order", "11(vii); FR 56(j)", 1],
                ["The penalty", "Compulsory retirement is a major penalty under r.11(vii) and requires an inquiry under r.14, which was held and in which two charges were proved", "11(vii), 14", 2],
                ["The power", "FR 56(j) permits compulsory retirement in the public interest on review of the record, without a disciplinary inquiry; the test is the employee's continued utility, not misconduct", "FR 56(j); Explanation (vii) to r.11", 2],
                ["The overlap", "The two orders cannot both operate on the same date for the same end; the punitive order supersedes the FR 56(j) order as the operative decision", "11(vii)", 2],
                ["Consequence", "Only the r.11(vii) order can stand, and it carries the incidents of a major penalty — including appeal under r.23(ii) and no bar to future Government employment", "11(vii), 23(ii)", 2],
                ["Course", "The department should have elected one route before issuing any order; issuing both exposes the punitive order to the charge that the FR 56(j) route was used to avoid the inquiry", "11(vii); FR 56(j)", 1]],
         wrong=["<b>“Compulsory retirement needs an inquiry whichever power is used.”</b> FR 56(j) is not a penalty.",
                "<b>“Both orders can stand together.”</b> They operate on the same service on the same date.",
                "<b>“The FR 56(j) order is void because an inquiry was held.”</b> The defect lies in issuing two orders, not in the review."],
         answer=("Compulsory retirement under <b>FR 56(j)</b> is an administrative power exercised on the service record, while under <b>r.11(vii)</b> it is "
                 "a major penalty; both were passed on the same date for the same end, so only the punitive order can stand."),
         tags=[["11", "Rule 11 — penalties"], ["11(vii)", "Rule 11(vii) — compulsory retirement"],
               ["23", "Rule 23 — orders against which appeal lies"]]),

    dict(id="L2-22", title="Dismissal or removal — the difference that outlives the job",
         facts=("Two officials of the same office were found guilty of the same misconduct — accepting a small gratification. Shri O was dismissed "
                "and Shri P removed from service, both after regular inquiries. Shri O had 24 years of qualifying service; Shri P, 27 years. "
                "Both apply for pension. Shri O also applies for a post in a public sector bank and is told he is ineligible. Shri P's application "
                "is accepted."),
         record=[["Shri O", "dismissal, r.11(ix)", "24 years' service"],
                 ["Shri P", "removal, r.11(viii)", "27 years' service"],
                 ["Gratification proved", "same transaction", "proviso to r.11"],
                 ["PSU application", "O rejected, P accepted", "future employment"]],
         questions=["What is the legal difference between dismissal and removal?",
                    "What is the pension consequence of each?",
                    "Was the difference in penalty permissible on these facts?",
                    "What is the remedy for the official who thinks the penalties were reversed?"],
         path=["dismissal: disqualification + forfeiture", "removal: no disqualification", "pension follows the pension rules", "proviso to r.11", "appeal"],
         steps=[["Issue", "Consequences of dismissal as against removal", "11(viii), (ix)", 1],
                ["Definitional difference", "Removal is not a disqualification for future Government employment; dismissal ordinarily is", "11(viii), (ix)", 2],
                ["Pension", "Dismissal ordinarily entails forfeiture of past service and of pension, subject to the compassionate-allowance provision in the pension rules; removal does not forfeit past service, and pension is regulated under those rules, including their provisions on withholding", "11(viii); CCS (Pension) Rules, 2021", 3],
                ["Proviso to r.11", "Where the charge is acceptance of gratification, removal or dismissal <i>shall</i> be imposed; any other penalty only in an exceptional case with special reasons", "provisos to 11", 2],
                ["Consistency", "The same misconduct can attract different penalties if the records differ, but on identical facts with no distinguishing feature the difference invites an Article 14 challenge", "11; administrative law", 1],
                ["Remedy", "An appeal under r.23(ii) to the appellate authority, and thereafter revision; the PSU refusal is a consequence of dismissal, not a separate order", "23, 29", 1]],
         wrong=["<b>“Dismissal and removal are the same with different names.”</b> The disqualification and the pension consequence differ.",
                "<b>“Removal forfeits pension.”</b> It does not forfeit past service; pension is governed by the pension rules.",
                "<b>“Gratification can attract censure.”</b> Only in an exceptional case with special reasons."],
         answer=("Dismissal ordinarily disqualifies from future Government employment and forfeits past service for pension, while removal does neither; "
                 "on identical facts the difference in penalty needs a distinguishing reason, and the remedy is appeal under <b>r.23(ii)</b>."),
         tags=[["11", "Rule 11 — penalties"], ["11(viii)", "Rule 11(viii) — removal"],
               ["11(ix)", "Rule 11(ix) — dismissal"], ["23", "Rule 23 — orders against which appeal lies"]]),
]
