# -*- coding: utf-8 -*-
"""L3 integrated cases, third pass: common proceedings and the sealed cover.

Case ids L3-17 to L3-21.  Kept in a separate module so the first two L3 blocks
remain stable: meta.CLOCKS and the L1 cross-references point at those ids.

Every proposition here is traced either to the text of r.18, r.14(23), r.15, r.24
or to DoPT OM No. 22011/4/91-Estt.(A) dated 14.09.1992 (sealed cover), read with
Union of India v. K.V. Jankiraman (1991), A.N. Mohanan (2007) and
Union of India v. B.V. Gopinath (2014).  The OM is executive instruction, not
statutory rule: the book says so wherever the distinction matters.
"""

L3C = [

    # ------------------------------------------------------------------ 17
    dict(id="L3-17", title="One proceeding, two officers, one incompetent signature",
         facts=("A payment of ₹24,00,000 was made on a forged sanction. Smt L, an Assistant Accounts Officer (Group ‘B’), was the drawing officer and "
                "Shri M, a Senior Accountant (Group ‘C’), certified the bills. The Joint Secretary ordered a common proceeding under r.18 and, because he "
                "was going on deputation, named the Deputy Secretary as the authority to function as the disciplinary authority for the common proceeding; "
                "the order recorded that r.14 and r.15 would apply and that the Deputy Secretary might impose any penalty under r.11 except removal and "
                "dismissal. The Schedule read with the general order makes the Joint Secretary the disciplinary authority for both posts; Smt L’s appointing "
                "authority is the Joint Secretary, and Shri M’s is the Deputy Secretary. The Deputy Secretary imposed removal on Smt L and removal on Shri M. "
                "Shri M appealed to the Joint Secretary, who dismissed the appeal. Smt L has now appealed."),
         record=[["Transaction", "₹24,00,000", "forged sanction"],
                 ["Order under r.18", "Joint Secretary", "Deputy Secretary named as D.A."],
                 ["Specification of penalties", "“any penalty except removal and dismissal”", "no wider power given"],
                 ["Appointing authority — Smt L", "Joint Secretary", "Group ‘B’"],
                 ["Appointing authority — Shri M", "Deputy Secretary", "Group ‘C’"],
                 ["Penalties imposed", "removal on both", "r.11(viii)"],
                 ["Shri M’s appeal", "allowed to stand", "dismissed by the J.S."],
                 ["Smt L’s appeal", "filed now", "—"]],
         questions=["Was a common proceeding competent at all?",
                    "Was the Deputy Secretary competent to impose removal on either officer?",
                    "Does the answer differ for the two officers, and why?",
                    "What survives of the inquiry and the evidence?",
                    "Where does each appeal now lie?"],
         path=["r.18(1): authority competent to dismiss all", "satisfied by the J.S.", "r.18(2) subject to r.12(4)", "D.S. cannot impose a major penalty", "Smt L: void — Shri M: valid", "two different appellate forums"],
         steps=[["1. The condition", "A common proceeding may be ordered by the President or by an authority competent to impose dismissal on <i>all</i> the servants concerned; the Joint Secretary was competent for both, so the condition in r.18(1) was met and the consent requirement in the Note (which applies only where the competent authorities are different) never arose", "18(1) and Note", 3],
                ["2. The order under r.18(2)", "The order must specify the authority which may function as the disciplinary authority, the penalties it may impose, and the procedure; it specified all three, and r.18(2) is expressly subject to r.12(4) — so the specification could not enlarge the Deputy Secretary’s power", "18(2)", 2],
                ["3. The jurisdictional vice", "The Deputy Secretary is subordinate to the Joint Secretary, who is Smt L’s appointing authority. No authority subordinate to the appointing authority may impose a penalty in r.11(v)–(ix), and r.18(2) cannot cure that: it is subject to r.12(4)", "12(4)(a); 18(2)", 3],
                ["4. Smt L", "Her removal is void for want of competence. The defect is jurisdictional, not procedural: it is not ratified by the Joint Secretary’s later approval, by her participation in the inquiry, or by the appellate order — a fresh order by a competent authority is required", "12(4)(a)", 3],
                ["5. Shri M", "The Deputy Secretary was his appointing authority, so removal was within r.12(2) and no question of subordination arises. That the r.18 order withheld removal from the Deputy Secretary’s specification is an internal contradiction. ⚠ Two readings are open: that the specification binds, so the order is beyond it and must be rectified; or that it is curable and caused no prejudice, because the penalty imposed was one his own appointing authority could impose under r.12(2). The second is the better view, since the defect lies in the order and not in the statute, but the point is worth stating rather than assuming", "12(2); 18(2)", 2],
                ["6. The record", "The inquiry authority was validly appointed under r.14(2) and the proceeding before it was regular. The defect lies in the disciplinary authority, not in the inquiry, so the evidence and the report survive and a competent authority may act on them after complying with r.15(2) afresh", "14(2), 15(2)", 2],
                ["7. Smt L’s appeal", "Her appeal lies to the President: under r.24(1)(i)(b) because the order is made by an authority other than one subordinate to her appointing authority, and equally under the proviso to r.24(2)(i), since the Joint Secretary’s own superior is subordinate to the President and the President is her appellate authority under r.24(1)(i)(b)", "24(1)(i)(b); 24(2)(i), proviso", 3],
                ["8. Shri M’s appeal", "In a common proceeding the appeal lies under r.24(2)(i) to the authority to which the disciplinary authority is immediately subordinate. Here the Joint Secretary heard his own subordinate’s order — which the rule permits — but he must not be asked to review, as appellate authority, an order he himself passed in Smt L’s file", "24(2)(i)", 2],
                ["9. What the department should do", "Treat the common proceeding as validly ordered but incompetently concluded so far as Smt L is concerned; have the Joint Secretary pass a reasoned order on her file under r.15(2) and (6) on the existing record, and keep the two files apart from that point", "18; 15(4), 15(6)", 2]],
         wrong=["<b>“The whole common proceeding is void, so both penalties fall.”</b> The vice is competence to impose, not competence to inquire: the proceeding and its evidence stand, and only the incompetent penalty falls.",
                "<b>“The Deputy Secretary needed the Joint Secretary’s consent.”</b> The Note to r.18(1) requires consent only where the authorities competent to impose dismissal are <i>different</i>. Where one authority is competent for all, it may order the proceeding alone.",
                "<b>“Both appeals lie to the Joint Secretary.”</b> r.24(2)(i) sends a common-proceeding appeal to the disciplinary authority’s own superior, and the proviso to r.24(2)(i) sends Smt L’s to the President."],
         answer=("The common proceeding was competently ordered — the Joint Secretary could dismiss both — but the Deputy Secretary could not impose removal on Smt L, "
                 "whose appointing authority is the Joint Secretary: her removal is void under r.12(4)(a), while Shri M’s stands because the Deputy Secretary was his "
                 "appointing authority. The inquiry record survives; the Joint Secretary must pass a fresh reasoned order on Smt L’s file. Her appeal lies to the "
                 "President under r.24(1)(i)(b) and the proviso to r.24(2)(i)."),
         model=("Rule 18 does not create a power to punish; it creates a power to join. Sub-rule (1) allows a common proceeding only where the President, or an "
                "authority competent to impose dismissal on <i>all</i> the servants concerned, so orders; the Note adds that where those authorities are "
                "different, the highest of them may order it with the consent of the others. Here the Joint Secretary was competent to dismiss both officers, so "
                "the condition was satisfied and no consent was needed. Sub-rule (2) then required the order to specify the authority which may function as the "
                "disciplinary authority, the penalties it may impose and the procedure to be followed. All three were specified — and the specification was "
                "itself subject to r.12(4), because sub-rule (2) says so in terms. The Deputy Secretary, being subordinate to Smt L’s appointing authority, "
                "could not impose on her any penalty in r.11(v) to (ix); his removal order is therefore without jurisdiction, and the defect is not one of "
                "procedure that participation or later approval can cure. Shri M stands differently: the Deputy Secretary was his appointing authority, and "
                "removal was within r.12(2), so his penalty is good even though the r.18 order had withheld that power in terms — a contradiction that caused "
                "him no prejudice. What survives is the inquiry: the inquiring authority was appointed under r.14(2), the evidence was recorded regularly, and "
                "the report is on file. A competent disciplinary authority may therefore act on that record, but it must do so itself, supplying its tentative "
                "reasons for disagreement under r.15(2) and recording findings before imposing a major penalty under r.15(6). On appeal, Smt L goes to the "
                "President: the order against her is made by an authority other than one subordinate to her appointing authority, which is the case r.24(1)(i)(b) "
                "covers, and the proviso to r.24(2)(i) reaches the same result for a common-proceeding appeal. The Joint Secretary must not sit as appellate "
                "authority on a file in which he is himself the disciplinary authority."),
         tags=[["18", "Rule 18 — common proceedings"], ["12", "Rule 12 — disciplinary authorities"],
               ["24", "Rule 24 — appellate authority"], ["15", "Rule 15 — action on the inquiry report"]]),

    # ------------------------------------------------------------------ 18
    dict(id="L3-18", title="A joint disagreement note and findings that are not charge-wise",
         facts=("Shri N, an Accounts Officer (Group ‘B’), and Shri O, an Assistant Accounts Officer (Group ‘B’), were proceeded against in a common proceeding "
                "under r.18 for the same transaction. Two articles of charge were framed against each. The inquiry authority returned a single report holding "
                "charge 1 proved against both and charge 2 not proved, and the disciplinary authority issued one note of disagreement covering both officers on "
                "charge 2, without distinguishing between them. The note and report were supplied on 18.05.2026 and both officers represented on 03.06.2026. On "
                "08.07.2026 the disciplinary authority passed a one-page order recording that “the charges are proved” and imposed on each the penalty of "
                "reduction by one stage for two years under r.11(v), with no direction that increments would not be earned. Shri N’s pay was ₹52,000 in Level 7 from 01.07.2025, his increment falling due on 1 July; the "
                "penalty took effect on 01.07.2026, and the stage below the ₹52,000 he was then drawing is ₹50,500, the stage above ₹53,600. Both appeal."),
         record=[["Common proceeding", "r.18", "two articles each"],
                 ["Report", "one, joint", "charge 1 proved · charge 2 not"],
                 ["Disagreement note", "one, joint", "no officer-wise reasons"],
                 ["Supplied / represented", "18.05.2026 / 03.06.2026", "within 15 days"],
                 ["Order", "08.07.2026", "“the charges are proved”"],
                 ["Penalty", "one stage, two years", "no direction on increments"],
                 ["Shri N’s pay", "₹52,000", "Level 7, from 01.07.2025"],
                 ["Stages", "₹50,500 below · ₹53,600 above", "one stage each way"]],
         questions=["Does a common proceeding permit a joint report and a joint disagreement note?",
                    "What does r.15(2) and r.15(4) require of the disciplinary authority’s order?",
                    "Is the order of 08.07.2026 sustainable?",
                    "If the penalty is re-imposed, what will it cost Shri N?",
                    "What is his pay on expiry, and where does the appeal lie?"],
         path=["r.18 joins the proceeding, not the persons", "joint report permissible", "reasons and findings must be officer-wise and charge-wise", "order records no finding", "penalties fall, record survives", "appeal under r.24(2)(i)"],
         steps=[["1. The joinder", "Rule 18 joins the proceeding, not the persons. Each officer remains entitled to a finding on each article of charge against him, and the joinder does not dilute that: it is a procedural economy, not a merger of defences", "18", 1],
                ["2. The note", "Rule 15(2) requires the report to be forwarded with the disciplinary authority’s tentative reasons for disagreement, and fifteen days to represent. A single document may serve both officers if it states the reasons on each charge for each of them; here it did not distinguish between them, but both knew the charge and both were heard on it", "15(2)", 3],
                ["3. The trap", "The vice is not the joint note but the absence of a finding. Rule 15(4) requires the disciplinary authority to consider the representation and <i>record its findings</i> before proceeding under r.15(5) or (6); the inquiry report itself must carry findings and reasons on each article under r.14(23)(i)(d)", "15(4); 14(23)", 3],
                ["4. The order", "“The charges are proved” is a conclusion, not a finding. It does not say which charge, against which officer, on what evidence, nor does it deal with the disagreement on charge 2 — which was never converted into a finding at all. To that extent the order is not an order under r.15", "15(4), 15(6)", 3],
                ["5. Consequence", "The penalties fall, but the inquiry does not. The disciplinary authority may pass a fresh order on the existing record, after considering the representations already made and recording charge-wise, officer-wise findings; no fresh inquiry and no fresh note are needed", "15(4), 15(1)", 3],
                ["6. If re-imposed — pay", "Reduction by one stage under r.11(v) fixes pay at the stage below the ₹52,000 he was drawing when the order took effect, that is <b>₹50,500</b>, from 01.07.2026", "11(v)", 2],
                ["7. The loss", "(₹53,600 − ₹50,500) × 12 = ₹37,200 in year one against the notional ₹53,600, and (₹55,200 − ₹50,500) × 12 = ₹56,400 in year two, totalling <b>₹93,600</b> of basic pay; the order is silent on increments, and silence cannot be read as a direction that they are earned", "11(v)", 3],
                ["8. On expiry", "Because there is no direction postponing future increments, pay is fixed on 01.07.2028 at the notional stage <b>₹56,900</b>; the omission of a direction therefore costs him the two years of loss and nothing after them", "11(v)", 2],
                ["9. Appeal", "The appeal lies under r.23(ii) and, in a common proceeding, to the authority to which the disciplinary authority is immediately subordinate under r.24(2)(i); because that authority is itself subordinate to the President and the President is the appellate authority for a Group ‘B’ officer under r.24(1)(i)(b), the proviso to r.24(2)(i) sends it to the President", "23(ii); 24(2)(i), proviso", 2]],
         wrong=["<b>“A common proceeding requires a separate report for each officer.”</b> It does not. What it requires is a finding on each charge against each officer — the document may be joint, the findings may not.",
                "<b>“The disagreement note was invalid because it was common.”</b> The note must state the reasons; a common note that states them officer-wise is good. This one failed on reasons, and the order failed on findings.",
                "<b>“The penalty is void because the order says nothing about increments.”</b> Rule 11(v) requires directions, but the omission is curable and, on this arithmetic, costs him nothing after the period."],
         answer=("The joinder was competent and a joint report and note are permissible, but the order of 08.07.2026 records no finding on any charge against either "
                 "officer and never deals with the disagreement on charge 2. The penalties therefore fall and the disciplinary authority must pass a fresh reasoned "
                 "order on the existing record. If the penalty is re-imposed, Shri N loses <b>₹93,600</b> of basic pay over two years and is fixed at "
                 "<b>₹56,900</b> on expiry."),
         model=("A common proceeding under rule 18 is an economy of procedure and nothing more. The report may be joint and the note of disagreement may be joint, "
                "provided each officer can see the reasons that touch him; what the rules do not permit is a joint conclusion in place of individual findings. "
                "Rule 14(23)(i)(d) requires the inquiring authority to record findings on each article of charge with reasons, and rule 15(4) requires the "
                "disciplinary authority, after considering the representation, to record its own findings before it proceeds under sub-rule (5) or (6). The order "
                "of 08.07.2026 does neither. It says that “the charges are proved”, which identifies no charge, no officer and no evidence, and it leaves the "
                "disagreement on charge 2 exactly where the note had left it. That is not a finding, and a penalty cannot rest on it. The consequence is "
                "proportionate: the penalties are quashed, but the inquiry and its record survive, because the defect is in the final order and not in the "
                "procedure that produced the report. The disciplinary authority may therefore act again on the same material — after considering the "
                "representations of 03.06.2026, which it already has, and after recording a finding on each charge against each officer. If it re-imposes "
                "reduction by one stage for two years on Shri N, his pay falls to ₹50,500 from 01.07.2026 against a notional ₹53,600; the loss of basic pay is ₹37,200 in the first year "
                "and ₹56,400 in the second, ₹93,600 in all; and on expiry he is fixed at the notional stage of ₹56,900, because no postponement of increments "
                "was directed. The appeal goes to the President, through the proviso to rule 24(2)(i), and the appellants should ask for the order to be set "
                "aside and, in the alternative, for the findings to be recorded afresh."),
         tags=[["18", "Rule 18 — common proceedings"], ["15", "Rule 15 — action on the inquiry report"],
               ["14", "Rule 14 — procedure"], ["11", "Rule 11 — penalties"], ["24", "Rule 24 — appellate authority"]]),

    # ------------------------------------------------------------------ 19
    dict(id="L3-19", title="A sealed cover that had no business existing",
         facts=("On 12.06.2025 a Departmental Promotion Committee met to fill four posts of Assistant Accounts Officer and placed Shri P’s case in a sealed cover "
                "because a vigilance complaint of 02.05.2025 was under preliminary inquiry. His immediate junior, Shri Q, was promoted from that panel on "
                "01.07.2025. A charge sheet was issued to Shri P only on 10.02.2026, and the proceeding is still pending. He asks for promotion from 01.07.2025. "
                "The department says the sealed cover was lawful because his conduct was under investigation, and that in any event his promotion can now only be "
                "prospective. The difference between the two levels is ₹3,000 a month from 01.07.2025 and ₹3,100 a month from 01.07.2026."),
         record=[["Vigilance complaint", "02.05.2025", "preliminary inquiry only"],
                 ["DPC", "12.06.2025", "sealed cover"],
                 ["Junior promoted", "01.07.2025", "Shri Q, same panel"],
                 ["Charge sheet", "10.02.2026", "nine months later"],
                 ["Proceeding", "pending", "—"],
                 ["Difference in pay", "₹3,000 / ₹3,100 a month", "from 01.07.2025 / 01.07.2026"]],
         questions=["What are the only circumstances in which a sealed cover may be used?",
                    "Was the sealed cover available on 12.06.2025?",
                    "Does the later charge sheet help the department?",
                    "From what date is he entitled to promotion, and how much is due?",
                    "What is the remedy, and what of the six-monthly review?"],
         path=["executive instruction, not rule", "three closed categories", "preliminary inquiry is not one", "cover unlawful", "promotion from 01.07.2025", "arrears ₹42,200"],
         steps=[["1. The device", "The sealed cover is not in the CCA Rules at all. It is a device of executive instruction — DoPT OM No. 22011/4/91-Estt.(A) dated 14.09.1992, issued after <i>Jankiraman</i> — and it operates only within the categories that the OM closes", "DoPT OM 14.09.1992, para 2; Jankiraman (1991)", 2],
                ["2. The three categories", "A cover may be used only where the servant is under suspension, or a charge sheet has been issued and the proceeding is pending, or prosecution for a criminal charge is pending. The list is exhaustive and the date of the DPC governs", "DoPT OM 14.09.1992, para 2(i)–(iii)", 3],
                ["3. The position on 12.06.2025", "On that date there was a complaint and a preliminary inquiry. There was no suspension, no charge sheet and no prosecution. None of the three categories was met, so the cover had no business existing", "DoPT OM 14.09.1992, para 2; Jankiraman (1991)", 3],
                ["4. Investigation is not a category", "<i>Jankiraman</i> decided exactly this: pendency of an investigation, or the grant of sanction for prosecution, is not enough; the relevant date is the date of the DPC, and the DPC guidelines say that where the matter is at a preliminary stage the officer is assessed and promoted with the others", "Jankiraman (1991); DPC guidelines", 2],
                ["5. Para 7 does not help", "Para 7 deems a cover where one of the three circumstances arises <i>after</i> the DPC’s recommendation and before promotion. Nothing arose between 12.06.2025 and 01.07.2025, and a charge sheet of 10.02.2026 cannot reach back over the event", "DoPT OM 14.09.1992, para 7", 2],
                ["6. The date", "Since the cover was unlawful, his case was not governed by para 3 at all: he was entitled to be promoted with the panel on <b>01.07.2025</b>, the date his junior from the same panel was promoted", "DoPT OM No. 22011/4/91-Estt.(A), 14.09.1992, para 3", 3],
                ["7. The later charge sheet", "It legitimises a future cover, not a past one. From 10.02.2026 the department may put the <i>next</i> DPC’s finding in a cover, and it may not promote him meanwhile — but that does not disturb the entitlement that had already accrued", "DoPT OM 14.09.1992, para 2(ii)", 2],
                ["8. Arrears", "Twelve months at ₹3,000 = ₹36,000, and from 01.07.2026 ₹3,100 a month, which for July and August 2026 is ₹6,200 — totalling <b>₹42,200</b> of basic pay computed to 31.08.2026, with DA following the pay and the pension contribution to be regularised", "DoPT OM 14.09.1992, para 6; FR 22", 3],
                ["9. Remedy and review", "A DPC recommendation is not an appealable order: r.22(ii) excludes interlocutory and step-in-aid orders. The appealable order is the one on his pay and promotion, which lies under r.23(iv) to the appellate authority, and the six-monthly review required by para 4 — never held — is the internal remedy that should have prevented this file from arising", "22(ii); 23(iv); DoPT OM para 4", 2]],
         wrong=["<b>“Conduct under investigation is the third category.”</b> It is not. The categories are suspension, charge sheet with a proceeding pending, and pending prosecution. A preliminary inquiry is none of them.",
                "<b>“The later charge sheet validates the earlier cover.”</b> The validity of a cover is tested on the date of the DPC that used it.",
                "<b>“Even so, promotion can only be prospective.”</b> Where the cover was unlawful, the entitlement runs from the date the panel took effect — the date his junior was promoted."],
         answer=("The sealed cover was unlawful: on 12.06.2025 there was a preliminary inquiry and nothing more, and none of the three categories in the 1992 OM was "
                 "met. He is entitled to promotion from <b>01.07.2025</b>, with <b>₹42,200</b> of arrears computed to 31.08.2026, and the charge sheet of 10.02.2026 "
                 "governs only the next DPC. The remedy is an appeal against the pay order under r.23(iv), after a representation."),
         model=("The sealed cover is the most misunderstood device in this branch of the law, because it is not in the rules. It comes from executive "
                "instruction: DoPT OM No. 22011/4/91-Estt.(A) dated 14.09.1992, issued to give effect to <i>Jankiraman</i>. The OM allows a cover in three "
                "circumstances only — the servant is under suspension; a charge sheet has been issued and the proceeding is pending; or prosecution for a criminal "
                "charge is pending — and it tests them on the date of the DPC. On 12.06.2025 Shri P was in none of the three. A complaint had been received and a "
                "preliminary inquiry had begun, which is precisely the stage at which the instructions require the officer to be assessed and promoted along with "
                "the rest, because the onus of expediting the proceedings is on the department and not on the officer. The cover was therefore without authority, "
                "and para 7 cannot save it: that paragraph deems a cover only where one of the three circumstances arises after the recommendation and before "
                "promotion, and nothing arose. The consequence is not that his promotion is prospective. It is that he was entitled to be promoted with the panel "
                "on 01.07.2025, the date his immediate junior from the same panel was promoted, with the pay of the higher level from that date. The arrears to "
                "31.08.2026 are ₹42,200 of basic pay, and DA follows. The charge sheet of 10.02.2026 is not irrelevant: from that date the department may place "
                "the next DPC’s finding in a cover and decline to promote him pending the proceeding, and it may not use the past cover to postpone the benefit "
                "that had already accrued. The remedy is an appeal against the order on his pay and promotion under rule 23(iv), the recommendation of a DPC "
                "being an interlocutory step outside rule 23 and expressly outside rule 22(i) and (ii); and the department should record why the six-monthly "
                "review required by para 4 of the OM was never held."),
         tags=[["23", "Rule 23 — orders against which an appeal lies"], ["22", "Rule 22 — orders against which no appeal lies"],
               ["27", "Rule 27 — consideration of appeal"]]),

    # ------------------------------------------------------------------ 20
    dict(id="L3-20", title="The cover that said “unfit” — and who may read it",
         facts=("A charge sheet was issued to Smt R on 18.03.2025 and the proceeding was pending when the Departmental Promotion Committee met on 20.04.2025; "
                "her case was placed in a sealed cover. The proceeding ended on 12.07.2026 with all charges held not proved. On 30.07.2026 the cover was opened: "
                "the DPC had graded her “unfit for promotion” for 2025-26. The reason, as the file shows, is a below-benchmark entry for 2023-24 which was never "
                "communicated to her. She asks for promotion from 20.04.2025 and for a copy of the DPC’s finding. The department says the cover is confidential and "
                "that exoneration carries no entitlement."),
         record=[["Charge sheet", "18.03.2025", "proceeding pending"],
                 ["DPC", "20.04.2025", "sealed cover"],
                 ["Outcome", "12.07.2026", "all charges not proved"],
                 ["Cover opened", "30.07.2026", "graded “unfit”"],
                 ["Stated reason", "APAR 2023-24", "never communicated"],
                 ["Six-monthly review", "not held", "fifteen months"]],
         questions=["Was the cover available on 20.04.2025?",
                    "What does exoneration actually do to a cover?",
                    "Can she be refused promotion on an uncommunicated grading?",
                    "Must the finding in the cover be shown to her?",
                    "What is the correct course now?"],
         path=["cover available — charge sheet pending", "exoneration opens it", "a finding of ‘unfit’ is not a date", "uncommunicated APAR cannot found the refusal", "disclosure where it is relied on", "re-DPC after communication"],
         steps=[["1. Availability", "On 20.04.2025 a charge sheet had been issued and the proceeding was pending — the second category. The cover was properly used, and the fact that the charges later failed does not make its use unlawful", "DoPT OM No. 22011/4/91-Estt.(A), 14.09.1992, para 2(ii); Jankiraman (1991)", 2],
                ["2. What exoneration does", "It opens the cover and it fixes the due date by reference to the position assigned in the panel and the date of the next junior’s promotion. Exoneration therefore gives a date only where the panel gave a position", "DoPT OM 14.09.1992, para 3", 3],
                ["3. What this cover says", "It says “unfit for promotion” for that year. There is no position in the panel, so there is no date to work back from, and exoneration by itself creates no entitlement. To that extent the department is right — and it is right for the wrong reason", "DoPT OM 14.09.1992, para 3; Jankiraman (1991)", 3],
                ["4. The foundation", "The refusal rests on the 2023-24 entry. An adverse grading that is used to deny promotion must have been communicated and open to representation; an uncommunicated entry cannot be the foundation of the denial, and the DPC must assess on the record it may lawfully use", "DoPT OM No. 21011/1/2005-Estt.(A), 23.07.2009; natural justice", 3],
                ["5. Disclosure", "The finding in the cover is not privileged against the officer whose promotion it decides. Where a denial rests on it, it must be disclosed to the extent necessary to meet it; secrecy is a practice, not a term of the OM, and the Supreme Court has confined it", "Gopinath (2014)", 3],
                ["6. What follows", "Not promotion now, but a re-assessment: communicate the APAR, dispose of any representation, and place the case before a review DPC. If she is then found fit, promotion runs from 20.04.2025 with consequential seniority and pay", "DoPT OM 14.09.1992, para 3", 2],
                ["7. The review", "The six-monthly review under para 4 was not held for fifteen months. That does not by itself entitle her to promotion, but the omission must be recorded and answered, and it is evidence of the delay that the OM exists to prevent", "DoPT OM 14.09.1992, para 4", 2],
                ["8. Two opposite errors", "“Exoneration means promotion” is wrong on a cover that records unfitness; “the cover can never be looked into” is wrong where the finding is relied on to deny a benefit. The correct position is that the finding must be disclosed, its foundation must be lawful, and the assessment must then be made again", "Jankiraman (1991); Gopinath (2014)", 2]],
         wrong=["<b>“Exoneration entitles her to promotion from the date of the DPC.”</b> Only if the cover records a position in the panel. A finding of “unfit” has no date to work back from.",
                "<b>“The sealed cover is confidential and cannot be disclosed.”</b> Where the denial of promotion rests on it, it must be disclosed to the extent needed to meet it.",
                "<b>“The failure to hold the six-monthly review entitles her to promotion.”</b> It is a procedural failure that must be explained; it does not create an entitlement."],
         answer=("The cover was properly used, but exoneration does not here yield a date: the DPC had graded her “unfit”, so there is no panel position to work "
                 "back from. The refusal nevertheless cannot stand as it is, because it rests on an uncommunicated APAR entry and on a finding she has never been "
                 "shown. The APAR must be communicated, any representation disposed of, and a review DPC held; if she is then found fit, promotion runs from "
                 "<b>20.04.2025</b>."),
         model=("Three questions are often run together here, and they must be kept apart. The first is whether the cover could be used: it could, because on "
                "20.04.2025 a charge sheet had been issued and the proceeding was pending, which is the second of the three categories in the 1992 OM. The second "
                "is what exoneration does: it opens the cover and it lets the due date be worked back from the position in the panel and the date of the next "
                "junior’s promotion — but only if the panel gave a position. This cover gave none; it recorded that she was unfit for that year, and a finding of "
                "unfitness cannot be converted into a date. The third question, which decides the case, is what the finding of unfitness may rest on. The file "
                "shows that it rests on a below-benchmark entry for 2023-24 that was never communicated to her. An adverse entry that is used to deny promotion "
                "must be communicated and open to representation; until it is, it cannot be the foundation of the denial, and a DPC that proceeds on it has "
                "assessed on material the officer has had no chance to meet. The finding must also be shown to her to that extent: the sealed cover is a device "
                "for withholding a <i>recommendation</i> until a proceeding concludes, not a licence to decide her career on material she may not see, and the "
                "Supreme Court has confined the practice accordingly. The correct course is therefore neither promotion nor refusal but re-assessment: "
                "communicate the APAR, dispose of the representation, and place the case before a review DPC. If she is found fit on a lawful record, her "
                "promotion runs from 20.04.2025 with consequential seniority and pay. Finally, the department must answer for the fifteen months in which the "
                "six-monthly review required by para 4 was never held; that omission does not create an entitlement, but it is exactly the delay the OM was "
                "written to prevent."),
         tags=[["23", "Rule 23 — orders against which an appeal lies"], ["27", "Rule 27 — consideration of appeal"]]),

    # ------------------------------------------------------------------ 21
    dict(id="L3-21", title="Retirement, a sealed cover and a pension that is short",
         facts=("A charge sheet was issued to Shri S on 05.08.2025, three months before he retired on 30.06.2026 from Level 7, where he was drawing ₹50,500 fixed on 01.07.2025, his increment falling due on 1 July. "
                "The Departmental Promotion Committee had met on 10.09.2025 and placed his case in a sealed cover; from the same panel his immediate junior was "
                "promoted to Level 8 with effect from 01.12.2025, his pay on promotion being fixed under FR 22 at the stage next above ₹50,500, that is ₹52,000. The proceeding concluded on 20.09.2026 with all charges held not proved, and "
                "the cover was opened on 05.10.2026: he had been placed third in the panel and found fit. The department has sanctioned pension on ₹50,500, "
                "saying that a promotion after retirement cannot be given and that no pay can be paid for a period during which he did not hold the post."),
         record=[["Charge sheet", "05.08.2025", "before retirement"],
                 ["DPC", "10.09.2025", "sealed cover · third in panel"],
                 ["Junior promoted", "01.12.2025", "Level 8, fixed at ₹52,000"],
                 ["Retirement", "30.06.2026", "Level 7, ₹50,500"],
                 ["Exonerated", "20.09.2026", "cover opened 05.10.2026"],
                 ["Pension sanctioned on", "₹50,500", "department’s basis"]],
         questions=["Does the proceeding and the cover survive retirement?",
                    "Should the promotion be given effect, and from what date?",
                    "Can he claim arrears of pay for the notional period?",
                    "What does the notional promotion do to his pension?",
                    "What happens if a penalty had been imposed instead?"],
         path=["proceeding continues for the cover", "para 3: work back from panel and junior", "notional promotion from 01.12.2025", "no pay — he did not hold the post", "average emoluments rise", "pension refixed"],
         steps=[["1. Survival", "Retirement does not abort the proceeding or the cover, and it does not take away the remedy: a person who has ceased to be in service may still appeal under r.24(1), and r.23 applies to him by its Explanation (i). The cover must therefore be opened and acted upon", "23, Explanation (i); 24(1)", 2],
                ["2. The notional date", "On exoneration the due date is fixed by reference to the position in the panel and the date of the next junior’s promotion. Third in the panel, with his junior promoted on 01.12.2025, gives <b>01.12.2025</b>", "DoPT OM No. 22011/4/91-Estt.(A), 14.09.1992, para 3", 3],
                ["3. No arrears of pay", "He did not hold the higher post, so there is no pay for it. The OM leaves even notional arrears for the interval to the appointing authority’s discretion, and after retirement the notional promotion operates on pension, not on salary", "DoPT OM 14.09.1992, para 6", 3],
                ["4. What it does affect", "Pension is computed on the average of the emoluments of the last ten months — here 01.09.2025 to 30.06.2026 — and the notional promotion from 01.12.2025 raises the emoluments for seven of those ten months", "CCS (Pension) Rules, 2021", 2],
                ["5. The average", "Three months at ₹50,500 = ₹1,51,500; seven months at ₹52,000 = ₹3,64,000; total ₹5,15,500 over ten months = <b>₹51,550</b> of basic pay, DA following the pay", "CCS (Pension) Rules, 2021", 3],
                ["6. The pension", "Fifty per cent of ₹51,550 is <b>₹25,775</b> a month, against the ₹25,250 sanctioned; the difference is ₹525 a month, with arrears from 01.07.2026", "CCS (Pension) Rules, 2021", 3],
                ["7. Gratuity and commutation", "Both are emolument-based and must be recalculated on the notional pay, subject to the prescribed ceiling; there is no question of pay arrears, but there is a question of the retirement gratuity and of commuted value", "CCS (Pension) Rules, 2021", 2],
                ["8. If a penalty had been imposed", "Para 3.1 would have applied: the finding would not be acted upon, the case would go to the next DPC in the normal course, and any pension effect would then be governed by the pension rules’ own provisions on withholding — not by the sealed cover", "DoPT OM 14.09.1992, para 3.1; CCS (Pension) Rules, 2021", 3]],
         wrong=["<b>“A promotion after retirement is impossible, so the cover is spent.”</b> The promotion is notional — it fixes the date and the emoluments, and on those the pension is recalculated.",
                "<b>“He is entitled to the pay of Level 8 for seven months.”</b> He never held the post. What he gets is the pension effect of the notional promotion, and notional arrears only if the appointing authority so directs.",
                "<b>“The cover lapses on retirement.”</b> It does not; and if a penalty had been imposed instead of exoneration, para 3.1 would have governed, not para 3."],
         answer=("The proceeding and the cover survived retirement, and exoneration fixes the notional promotion at <b>01.12.2025</b> — third in the panel, his junior "
                 "promoted that day. He gets no arrears of pay, because he never held the post, but his last-ten-months average becomes <b>₹51,550</b> and his "
                 "pension <b>₹25,775</b> instead of ₹25,250, with arrears from 01.07.2026 and consequential revision of gratuity and commutation."),
         model=("Retirement is not an escape from the file. The proceeding continues, the cover is opened on its conclusion, and the retired officer keeps his "
                "remedies: rule 24(1) allows an appeal by a person who has ceased to be in Government service, and the Explanation to rule 23 makes the same "
                "point for pensionary orders. On exoneration, para 3 of the 1992 OM requires the due date to be fixed by reference to the position assigned in the "
                "panel and the date of the next junior’s promotion. He was third and his immediate junior was promoted on 01.12.2025, so the notional promotion "
                "is from that date. Two things follow, and they must not be confused. The first is pay: he did not hold the higher post, so there is no salary "
                "for it, and the OM leaves even notional arrears for the interval to the appointing authority’s discretion. The second is pension, and that is "
                "where the value lies. Pension is computed on the average emoluments of the last ten months — three at ₹50,500 and seven at ₹52,000, which is "
                "₹5,15,500 and an average of ₹51,550 — so the pension becomes ₹25,775 a month instead of ₹25,250, with arrears from 01.07.2026, and the "
                "retirement gratuity and commuted value must be revised on the same basis. The department’s statement that a promotion cannot be given after "
                "retirement confuses the promotion with the pay of the post; what the OM directs is notional promotion, and its currency is pension. Had the "
                "proceeding ended in a penalty rather than in exoneration, para 3.1 would have applied instead: the finding would not have been acted upon, the "
                "case would have gone to the next DPC, and the pension consequence would have been governed by the pension rules and not by the cover."),
         tags=[["23", "Rule 23 — orders against which an appeal lies"], ["24", "Rule 24 — appellate authority"],
               ["14", "Rule 14 — procedure"]]),
]
