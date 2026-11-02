# -*- coding: utf-8 -*-
"""L2 standard cases 23–34 — suspension, subsistence and the edges of penalty."""

L2C = [
    dict(id="L2-23", title="Forty hours in custody",
         facts=("Shri Q was detained by the police on a criminal complaint at 06.00 on 09.03.2026 and released on bail at 22.00 on 10.03.2026 — "
                "40 hours. The department issued a suspension order on 12.03.2026 recording that he had been detained. The charge sheet in the "
                "departmental proceeding followed on 02.04.2026. He claims that the period 09.03.2026 to 12.03.2026 must be treated as deemed "
                "suspension and that he should be paid only subsistence allowance, and the department claims that no suspension operated before 12.03.2026."),
         record=[["Detention", "09.03.2026, 06.00", "—"],
                 ["Release", "10.03.2026, 22.00", "40 hours"],
                 ["Suspension order", "12.03.2026", "express"],
                 ["Charge sheet", "02.04.2026", "departmental"]],
         questions=["Was there a deemed suspension?",
                    "From what date did suspension operate?",
                    "What is the effect of the 40 hours on pay for those days?",
                    "What should the suspension order have recorded?"],
         path=["r.10(2)(a)", "detention > 48 hours?", "40 hours — no", "express order 12.03.2026", "suspension from that date"],
         steps=[["Issue", "Whether detention of 40 hours attracts a deemed suspension", "10(2)(a)", 1],
                ["The rule", "A deemed suspension arises with effect from the date of detention only if the detention exceeds 48 hours", "10(2)(a)", 2],
                ["Application", "The detention ran from 06.00 on 09.03.2026 to 22.00 on 10.03.2026 — 40 hours; the threshold is not crossed and there is no deemed suspension", "10(2)(a)", 3],
                ["The express order", "The suspension operated from 12.03.2026, the date of the order; the preceding days are duty, not suspension", "10(1)", 2],
                ["Pay", "The employee is entitled to full pay for 09.03.2026 to 11.03.2026 and subsistence allowance only from 12.03.2026; reference to detention in the order does not backdate it", "10(2), FR 53", 1],
                ["Drafting", "The order should state its effective date and, where detention is the ground, the period of custody, so the register is unambiguous", "10(1)–(2)", 1]],
         wrong=["<b>“Any detention means deemed suspension.”</b> Only detention exceeding 48 hours.",
                "<b>“Suspension runs from the date of the incident.”</b> It runs from the order, or from the date specified for a deemed suspension.",
                "<b>“The 40 hours are suspension because the order mentions detention.”</b> A recital cannot backdate an order."],
         answer=("There was no deemed suspension: the detention was 40 hours, below the 48-hour threshold in <b>r.10(2)(a)</b>; suspension operated from "
                 "<b>12.03.2026</b> and the earlier days are duty for pay."),
         tags=[["10", "Rule 10 — suspension"], ["10(2)", "Rule 10(2) — deemed suspension"]]),

    dict(id="L2-24", title="Convicted on Friday, dismissed on Friday",
         facts=("Shri R, a Group ‘C’ employee, was convicted on 13.02.2026 of an offence under the Prevention of Corruption Act and sentenced to "
                "one year's rigorous imprisonment. The disciplinary authority dismissed him the same day under rule 19(i). He was released on bail "
                "by the appellate court on 20.02.2026, the conviction not having been suspended. His representation says that no inquiry was held, "
                "that the conviction is under appeal, and that he should have been treated as under deemed suspension instead of being dismissed."),
         record=[["Conviction", "13.02.2026", "1 year RI"],
                 ["Dismissal", "13.02.2026", "r.19(i)"],
                 ["Bail", "20.02.2026", "conviction not suspended"],
                 ["Appeal", "pending", "—"],
                 ["Inquiry", "none", "dispensed with"]],
         questions=["Was rule 19(i) available?",
                    "Was a deemed suspension under r.10(2)(b) attracted?",
                    "What is the effect of the pendency of the criminal appeal?",
                    "What safeguards did rule 19 require?"],
         path=["conviction on criminal charge", "r.19(i) inquiry dispensed with", "no deemed suspension because dismissal followed", "representation on penalty may be given", "consultation if necessary"],
         steps=[["Issue", "Imposition of a penalty on the ground of conduct leading to conviction", "19(i), 10(2)(b)", 1],
                ["The power", "Where a penalty is imposed on the ground of conduct which led to conviction on a criminal charge, the inquiry under r.14 may be dispensed with", "19(i)", 2],
                ["Deemed suspension", "A deemed suspension under r.10(2)(b) arises only where no dismissal, removal or compulsory retirement follows the conviction; here dismissal followed the same day, so it is not attracted", "10(2)(b)", 2],
                ["The safeguard", "The proviso permits an opportunity of representation on the penalty proposed; it is not mandatory in terms but its denial is a factor if the penalty is challenged", "proviso to 19(i)", 2],
                ["Pendency of appeal", "A conviction under appeal is still a conviction unless suspended; the department need not await the appeal, though it may do so", "19(i)", 2],
                ["Consultation", "Where the Commission must be consulted, the advice must be obtained and supplied before the order", "19, second proviso", 1]],
         wrong=["<b>“A conviction under appeal cannot found a penalty.”</b> The conviction stands until suspended or set aside.",
                "<b>“He must be deemed suspended instead.”</b> The rule excludes that where dismissal follows.",
                "<b>“Rule 19 allows an order with no reasons at all.”</b> The penalty must still be reasoned on the conduct."],
         answer=("Rule 19(i) was available and the dismissal on the day of conviction was competent; <b>r.10(2)(b)</b> was not attracted because dismissal "
                 "followed, and the pendency of the appeal does not by itself invalidate the penalty."),
         tags=[["19", "Rule 19 — special procedure"], ["10(2)", "Rule 10(2) — deemed suspension"],
               ["11", "Rule 11 — penalties"]]),

    dict(id="L2-25", title="The review that was never held",
         facts=("Smt S was suspended on 10.01.2026 pending a disciplinary proceeding. No review committee met. The file contains an office note of "
                "08.04.2026 recording that “the suspension may continue as the inquiry is in progress”, signed by the Section Officer. No order of "
                "extension was issued. The charge sheet was served on 15.05.2026. On 20.05.2026 the department informed her that she “continues to be "
                "under suspension”. She claims she ceased to be under suspension on 10.04.2026."),
         record=[["Suspension", "10.01.2026", "effective date"],
                 ["90 days complete", "09.04.2026", "inclusive count"],
                 ["Office note", "08.04.2026", "no order, Section Officer"],
                 ["Charge sheet", "15.05.2026", "after lapse"],
                 ["“Continues” letter", "20.05.2026", "after lapse"]],
         questions=["On what date did the suspension cease to be valid?",
                    "Could the office note operate as an extension?",
                    "What is the effect of the charge sheet served in May?",
                    "What is she entitled to?"],
         path=["r.10(6) review before 90 days", "r.10(7) validity", "no review committee", "no extension order", "validity ends 09.04.2026"],
         steps=[["Issue", "Validity of a suspension not reviewed within ninety days", "10(6), 10(7)", 1],
                ["The review duty", "The competent authority must review before the expiry of ninety days from the effective date, on the Review Committee's recommendation, and pass an order extending or revoking", "10(6)", 2],
                ["The arithmetic", "Ninety days counted inclusively from <b>10.01.2026</b> are complete on <b>09.04.2026</b>", "10(6), 10(7)", 2],
                ["The consequence", "Without an extension order passed after review before that date, the order is not valid after the ninety-day period; it lapsed at the end of 09.04.2026", "10(7)", 2],
                ["The note", "An office note by a Section Officer is neither a review by the competent authority nor an order of extension", "10(6), 10(7)", 1],
                ["The charge sheet", "Service of a charge sheet in May does not retrospectively validate the lapsed suspension; a fresh order under r.10(1)(a) would be required", "10(1), 10(7)", 1],
                ["Money", "She must be paid full pay for the period after the lapse, the suspension having ceased to be valid, subject to the treatment of the period on the conclusion of the proceeding", "FR 53, FR 54", 1]],
         wrong=["<b>“Suspension continues until the inquiry ends.”</b> It continues only while validly extended.",
                "<b>“The office note is an extension.”</b> It is neither a review nor an order.",
                "<b>“The lapse is cured by the later charge sheet.”</b> A lapsed order cannot be revived retrospectively."],
         answer=("With no review and no extension, the suspension ceased to be valid at the end of <b>09.04.2026</b>; the office note and the later charge "
                 "sheet cannot revive it, and she is entitled to full pay thereafter, subject to r.10(6)–(7) and FR 53–54."),
         model=("A suspension under rule 10(1) does not run indefinitely. Rule 10(6) requires the competent authority to review it before the expiry of "
                "ninety days from the effective date, on the recommendation of the Review Committee, and to pass an order either extending or revoking it, "
                "and rule 10(7) provides that the order shall not be valid after ninety days unless it is so extended before expiry. Counting inclusively "
                "from 10.01.2026, the ninety days were complete on 09.04.2026. No Review Committee met and no order of extension issued; the office note of "
                "08.04.2026 signed by a Section Officer is neither a review by the competent authority nor an order, and the letter of 20.05.2026 cannot "
                "supply what was never done. The suspension therefore ceased to be valid at the end of 09.04.2026. Service of the charge sheet on "
                "15.05.2026 did not retrospectively validate it; had the department wished to suspend her afresh, it needed a fresh order under rule 10(1)(a) "
                "on material then existing. For the period after the lapse she is entitled to full pay, and the treatment of the entire period will be "
                "determined when the proceeding concludes under FR 54. The lesson is that the review architecture is mandatory, and that a charge sheet "
                "does not extend a suspension."),
         tags=[["10", "Rule 10 — suspension"], ["10(6)", "Rule 10(6) — review of suspension"],
               ["10(7)", "Rule 10(7) — validity after 90 days"]]),

    dict(id="L2-26", title="Custody, release and the ninety-day clock",
         facts=("Shri T was arrested on 10.03.2026 and remained in judicial custody until release on 02.06.2026. The appointing authority was informed "
                "of the release on 05.06.2026. The department treated the 90-day review clock as running from 10.03.2026 and, on that basis, held the "
                "suspension to have lapsed on 07.06.2026 and revoked it. He argues that the suspension continued until the review architecture was "
                "satisfied and that his pay for the intervening period has been wrongly withheld."),
         record=[["Detention from", "10.03.2026", "—"],
                 ["Release", "02.06.2026", "custody ended"],
                 ["Intimation", "05.06.2026", "to appointing authority"],
                 ["Department’s assumption", "clock from 10.03.2026", "lapse 07.06.2026"],
                 ["Revocation", "07.06.2026", "—"]],
         questions=["When does the ninety-day period begin for a deemed suspension in custody?",
                    "Was the department's computation right?",
                    "What is the effect of the revocation?",
                    "What is he entitled to for the period 10.03.2026 to 05.06.2026?"],
         path=["r.10(2)(a) deemed from detention", "proviso to r.10(7)", "90 days from release or intimation, later", "05.06.2026 → 02.09.2026", "revocation valid but premised on wrong date"],
         steps=[["Issue", "Computation of the ninety-day period for a deemed suspension following detention", "10(2)(a), proviso to 10(7)", 1],
                ["Deemed suspension", "Detention exceeding 48 hours creates a deemed suspension with effect from the date of detention, that is <b>10.03.2026</b>", "10(2)(a)", 2],
                ["The special clock", "For a deemed suspension, the review need not be undertaken if the servant is still in custody at the end of ninety days; the ninety days count from release or from intimation of release, whichever is later", "proviso to 10(7)", 3],
                ["Application", "Release was on 02.06.2026 and intimation on 05.06.2026; the ninety days therefore ran from <b>05.06.2026</b> and would have been complete on <b>02.09.2026</b>", "proviso to 10(7)", 2],
                ["The department's date", "Its computation from 10.03.2026 is wrong; the revocation on 07.06.2026 is nevertheless effective, because revocation is always open to the competent authority", "10(5)(c)", 1],
                ["Money", "For 10.03.2026 to 07.06.2026 he was under a valid deemed suspension and is entitled to subsistence allowance under FR 53, not to full pay; full pay runs from revocation", "FR 53", 1]],
         wrong=["<b>“The 90 days run from arrest.”</b> For a deemed suspension they run from release or intimation.",
                "<b>“The revocation is invalid because the date was miscalculated.”</b> Revocation is always available.",
                "<b>“He gets full pay for the whole period.”</b> The deemed suspension was valid until revoked."],
         answer=("The ninety days ran from <b>05.06.2026</b> (later of release and intimation) and would have ended on <b>02.09.2026</b>; the revocation on "
                 "07.06.2026 is valid, and he is entitled to subsistence allowance — not full pay — until that date."),
         tags=[["10", "Rule 10 — suspension"], ["10(2)", "Rule 10(2) — deemed suspension"],
               ["10(7)", "Rule 10(7) — validity and the custody proviso"]]),

    dict(id="L2-27", title="What suspension costs",
         facts=("Shri U, a Group ‘B’ officer with basic pay ₹44,900 in Level 7, was suspended with effect from 04.02.2026. DA is 63% ⚑ from "
                "01.07.2026 and 60% before that. The suspension order directs recovery of ₹1,200 per month towards house rent and ₹500 per month "
                "towards a society loan. He remained under suspension until 30.09.2026. He asks what he should have been paid, and the office has paid "
                "him 75% throughout, saying that “after the first month the higher rate applies”."),
         record=[["Basic pay", "₹44,900", "Level 7"],
                 ["DA", "60% to 30.06.2026; 63% ⚑ thereafter", "—"],
                 ["Suspension", "04.02.2026 to 30.09.2026", "—"],
                 ["Deductions ordered", "₹1,200 + ₹500 per month", "—"],
                 ["Office practice", "75% from the first month", "wrong"]],
         questions=["What is the subsistence allowance for the first ninety days?",
                    "From what date does the higher rate apply, and at what figure?",
                    "Do the ordered deductions apply?",
                    "What is the monthly excess paid, and what follows?"],
         path=["FR 53", "first 90 days: 50% of pay+DA", "90 days end 04.05.2026", "75% from 05.05.2026", "deductions as ordered"],
         steps=[["Issue", "Computation of subsistence allowance during suspension", "FR 53", 1],
                ["Base", "Pay plus DA: ₹44,900 × 1.60 = <b>₹71,840</b> to 30.06.2026; ₹44,900 × 1.63 = <b>₹73,187</b> from 01.07.2026 ⚑", "FR 53", 2],
                ["First ninety days", "50% of the base: <b>₹35,920</b> per month from 04.02.2026", "FR 53(i)", 2],
                ["The change", "Ninety days counted inclusively from 04.02.2026 are complete on <b>04.05.2026</b>; the higher rate applies from <b>05.05.2026</b>", "FR 53(ii)", 2],
                ["Higher rate", "75% of the base: <b>₹53,880</b> to 30.06.2026 and <b>₹54,890.25</b> from 01.07.2026 ⚑", "FR 53(ii)", 2],
                ["Deductions", "The deductions directed in the suspension order apply to the subsistence allowance, so the net figures are ₹34,220 and ₹53,190.25 respectively", "FR 53", 1],
                ["The excess", "Paying 75% throughout overpaid the first ninety days by ₹17,960 a month; the excess is recoverable only after notice, and cannot be adjusted without an opportunity", "FR 53; 16(1)(a)", 1]],
         wrong=["<b>“75% applies after the first month.”</b> The step is at ninety days.",
                "<b>“Subsistence is 50% of basic pay.”</b> It is a percentage of pay plus DA.",
                "<b>“Deductions do not apply to subsistence allowance.”</b> They do, if the order directs them."],
         answer=("₹35,920 a month for the first ninety days (04.02.2026–04.05.2026), then 75% from <b>05.05.2026</b> — ₹53,880 rising to ₹54,890.25 from "
                 "01.07.2026 ⚑ — less the ordered deductions; the office's flat 75% overpaid the early months."),
         tags=[["10", "Rule 10 — suspension"], ["FR 53", "FR 53 — subsistence allowance"]]),

    dict(id="L2-28", title="Five months, no charge sheet",
         facts=("Smt V, a Senior Auditor, was suspended on 06.02.2026 on the ground that a disciplinary proceeding was contemplated. The review "
                "committee recommended continuance on 30.04.2026 without any material beyond the pending vigilance verification. The extension order "
                "of 02.05.2026 records only that “the verification is continuing”. No charge sheet has been issued by 30.09.2026. She asks that the "
                "suspension be revoked and that the period be treated as duty."),
         record=[["Suspension", "06.02.2026", "proceeding contemplated"],
                 ["Review", "30.04.2026", "no material beyond verification"],
                 ["Extension", "02.05.2026, 180 days", "“verification continuing”"],
                 ["Charge sheet", "none by 30.09.2026", "8 months"],
                 ["Prejudice", "posting withheld, promotion due 2026", "asserted"]],
         questions=["Was the extension order sustainable?",
                    "What does the case law require before a charge memo?",
                    "Can she insist on revocation?",
                    "What relief should be granted?"],
         path=["r.10(1)(a) contemplation", "r.10(6) review + reasons", "Ajay Kumar Choudhary", "charge memo within reasonable time", "revocation + consequential relief"],
         steps=[["Issue", "Continuance of suspension for eight months without a charge sheet", "10(1)(a), 10(6)", 1],
                ["Power and its condition", "Suspension may be ordered where a proceeding is contemplated or pending, but the review must rest on material, not on the continuation of an inquiry into whether there is a case", "10(1)(a), 10(6)", 2],
                ["The extension", "An order that recites only that verification is continuing does not engage with the necessity of suspension; it is a mechanical extension", "10(6)", 2],
                ["The case law", "Suspension is not to be extended mechanically and a charge memo should follow within a reasonable time; continued suspension without charges causes prejudice that cannot be compensated by subsistence alone", "Ajay Kumar Choudhary (2015)", 3],
                ["Her request", "Revocation is always open to the competent authority and may be sought at any time; the authority must apply its mind to whether suspension is still necessary", "10(5)(c)", 2],
                ["Relief", "Revoke the suspension; treat the period after the point at which the suspension ceased to serve any purpose as duty for pay, and consider her promotion claim for 2026 without prejudice", "10(5), FR 54", 1]],
         wrong=["<b>“Suspension can continue while vigilance verifies.”</b> Verification is not a proceeding, and it cannot indefinitely justify suspension.",
                "<b>“Only the appellate authority can end it.”</b> Revocation is available under r.10(5)(c) at any time.",
                "<b>“Compensation is the remedy.”</b> The remedy is to end the suspension and regularise the period."],
         answer=("The extension was mechanical and cannot sustain eight months without a charge sheet; following <b>Ajay Kumar Choudhary (2015)</b> and "
                 "<b>r.10(6)</b>, the suspension should be revoked and the period regularised as duty, with her promotion claim considered on merits."),
         tags=[["10", "Rule 10 — suspension"], ["10(6)", "Rule 10(6) — review of suspension"],
               ["FR 54", "FR 54 — pay on reinstatement"]]),

    dict(id="L2-29", title="Three extensions and an objection",
         facts=("Shri W was suspended on 02.05.2023. Reviews were held and extensions ordered on 28.07.2023, 20.01.2024, 15.07.2024, 08.01.2025, "
                "03.07.2025, 26.12.2025 and 20.06.2026, each for 180 days. The inquiry is still pending in October 2026 and the charge sheet was served "
                "in June 2023. He objects that a suspension cannot lawfully continue beyond two years and that the repeated extensions are a punishment."),
         record=[["Suspension", "02.05.2023", "—"],
                 ["Extensions", "seven, each 180 days", "reviews held before expiry"],
                 ["Charge sheet", "June 2023", "served"],
                 ["Inquiry", "pending", "October 2026"],
                 ["Objection", "2-year ceiling", "asserted"]],
         questions=["Is there a two-year ceiling on suspension?",
                    "What makes an extension valid?",
                    "What is the consequence of the extensions here?",
                    "What should he argue instead?"],
         path=["no outer limit in r.10", "each extension after review, before expiry, ≤180 days", "validity sustained", "real issues: delay + necessity"],
         steps=[["Issue", "Whether suspension can continue beyond two years by successive extensions", "10(6), 10(7)", 1],
                ["The rule", "Rule 10 prescribes no outer limit; it prescribes a process — review before 90 days, then extension for not more than 180 days at a time, each extension preceded by a review before the running period expires", "10(6), 10(7)", 2],
                ["Application", "Seven extensions of 180 days each, ordered on dates before the running period expired, satisfy the process on its face", "10(6)", 2],
                ["No ceiling", "There is therefore no two-year ceiling; the objection as framed fails", "10(6)–(7)", 1],
                ["But necessity", "Each review must consider whether suspension remains necessary; a review that merely recites the inquiry's pendency is vulnerable", "10(6); Ajay Kumar Choudhary (2015)", 2],
                ["Delay", "An inquiry pending for over three years with the charge sheet served in 2023 raises delay and prejudice, which affect the penalty and the continued suspension, not its formal validity", "14(24); 15", 2],
                ["Money", "If the suspension is found unjustified on conclusion, the period may be regularised as duty under FR 54", "FR 54", 1]],
         wrong=["<b>“Suspension cannot exceed two years.”</b> No such limit exists in the rules.",
                "<b>“Repeated extensions are a penalty.”</b> They are administrative, but must be justified at each review.",
                "<b>“The extensions are void because they total more than 180 days.”</b> The limit is per extension, not in total."],
         answer=("There is no two-year ceiling: seven extensions of 180 days each, ordered after review and before expiry, satisfy <b>r.10(6)–(7)</b>; his "
                 "real grounds are the necessity at each review and the delay in completing the inquiry."),
         tags=[["10", "Rule 10 — suspension"], ["10(6)", "Rule 10(6) — review and extension"],
               ["14(24)", "Rule 14(24) — completion of the inquiry"]]),

    dict(id="L2-30", title="The envelope that stayed sealed",
         facts=("A charge sheet was issued to Shri X on 12.04.2026. The Departmental Promotion Committee met on 20.05.2026 and placed its recommendation "
                "in a sealed cover because the disciplinary proceeding was pending. The proceeding ended on 15.12.2026 with a censure. The sealed cover was "
                "opened on 05.01.2027 and he was promoted with effect from 05.01.2027. He claims promotion from 20.05.2026 with arrears, because censure is a "
                "minor penalty. A junior shown below him in the same panel was promoted on 20.05.2026."),
         record=[["Charge sheet", "12.04.2026", "major penalty proposed"],
                 ["DPC", "20.05.2026", "sealed cover"],
                 ["Conclusion", "15.12.2026", "censure"],
                 ["Cover opened", "05.01.2027", "promotion from that date"],
                 ["Junior promoted", "20.05.2026", "from the same panel"],
                 ["Claim", "20.05.2026 with arrears", "—"]],
         questions=["Was the sealed cover procedure available on 20.05.2026?",
                    "What follows from the proceeding ending in a penalty rather than in exoneration?",
                    "From what date does the promotion take effect?",
                    "Can he claim arrears or stepping-up with the junior promoted earlier?",
                    "What would have followed had he been exonerated entirely?"],
         path=["charge pending on DPC date", "sealed cover permissible", "outcome is a penalty, not exoneration", "para 3.1: findings not acted upon", "next DPC, penalty in view", "effect from that later date"],
         steps=[["Issue", "Sealed cover, a censure, and the effective date of promotion", "DoPT OM No. 22011/4/91-Estt.(A), 14.09.1992, para 2", 1],
                ["Availability", "On 20.05.2026 a charge sheet had been issued and the proceeding was pending — the second of the three categories; the cover was properly used", "DoPT OM 14.09.1992, para 2(ii); Jankiraman (1991)", 2],
                ["The outcome rule", "The cover is opened on conclusion, but the findings are acted upon only on exoneration. Where any penalty is imposed, the findings <i>shall not be acted upon</i> and the case goes to the next DPC in the normal course, having regard to the penalty", "DoPT OM 14.09.1992, para 3.1", 2],
                ["Censure", "Censure carries no currency period, so the next DPC was free to find him fit notwithstanding it; that is why he was promoted at all in January 2027. It does not make the promotion retrospective", "DoPT OM 14.09.1992, para 3.1; A.N. Mohanan (2007)", 1],
                ["The date", "Promotion therefore runs from <b>05.01.2027</b>, the date of the order giving effect to the fresh assessment — not from the DPC of 20.05.2026, whose finding was never acted upon", "DoPT OM 14.09.1992, para 3.1", 2],
                ["Arrears and stepping-up", "No arrears for the interval; the OM leaves even notional arrears to the appointing authority's discretion after exoneration, and there is none here. Pay is fixed from actual promotion and there is no stepping-up with the junior", "DoPT OM 14.09.1992, para 6; FR 22", 1],
                ["Contrast", "Had he been exonerated, the due date would have been worked back by reference to his position in the panel and the date of his next junior's promotion — here 20.05.2026, with seniority and consequential benefits", "DoPT OM 14.09.1992, paras 3 and 6", 1]],
         wrong=["<b>“Censure is minor, so the sealed cover must be given effect from the DPC date.”</b> That is the trap. Para 3.1 keys on <i>any</i> penalty: the finding is not acted upon, and the case goes to the next DPC — which is why the promotion is from 05.01.2027.",
                "<b>“Promotion must be ante-dated to the DPC.”</b> Only exoneration — or a finding of fitness by the next DPC — has that effect, and then only by working the date back from the panel.",
                "<b>“He can claim stepping-up because his junior went earlier.”</b> The OM expressly excludes stepping-up where promotion was withheld on account of a penalty."],
         answer=("The sealed cover was properly used on 20.05.2026, but the proceeding ended in a penalty, not in exoneration. Under para 3.1 of the 1992 OM the "
                 "sealed-cover finding could not be acted upon at all: his case had to go to the next DPC, which was free to find him fit because censure has no "
                 "currency. Promotion therefore runs from <b>05.01.2027</b>; there are no arrears for the interval and no stepping-up with the junior. Exoneration "
                 "would have produced the opposite result — promotion from <b>20.05.2026</b>, by working the date back from his panel position."),
         tags=[["11", "Rule 11 — penalties"], ["15", "Rule 15 — action on the inquiry report"]]),

    dict(id="L2-31", title="Termination during probation",
         facts=("Smt Y was appointed on probation for two years on 01.07.2025. On 10.06.2026 her services were terminated “in accordance with the terms of "
                "appointment” during the probation period. The file shows a preliminary verification report finding that she had accepted ₹15,000 from a "
                "vendor, a note by the controlling officer that her conduct was “unsatisfactory and calls for action”, and no inquiry of any kind. She "
                "challenges the order as punitive in substance."),
         record=[["Appointment", "01.07.2025", "two years' probation"],
                 ["Verification report", "May 2026", "₹15,000 from a vendor"],
                 ["Note", "June 2026", "“calls for action”"],
                 ["Termination", "10.06.2026", "terms of appointment"],
                 ["Inquiry", "none", "—"]],
         questions=["Is termination during probation a penalty?",
                    "When does such an order become punitive in substance?",
                    "What does the record here show?",
                    "What is the consequence?"],
         path=["Explanation (viii)(a) to r.11", "termination per terms — not a penalty", "but misconduct as foundation", "punitive", "inquiry required"],
         steps=[["Issue", "Whether a termination during probation founded on misconduct is a penalty in substance", "Explanation (viii)(a) to r.11", 1],
                ["The rule", "Termination of a probationer during or at the end of probation, in accordance with the terms of appointment, is not a penalty", "Explanation (viii)(a) to r.11", 2],
                ["The limit", "Where misconduct is the foundation of the order and the termination is not a simpliciter discharge, it is punitive and requires the r.14 procedure; the form of the order does not decide its character", "Dipti Prakash Banerjee (1999); Radhey Shyam Gupta (1999)", 3],
                ["Application", "The verification report, the note that action is called for, and the proximity of the order to those documents show that the foundation was the alleged acceptance of money, not an assessment of probationary suitability", "Explanation (viii)(a) to r.11", 2],
                ["Consequence", "The order is unsustainable as a punitive termination without inquiry; the department may hold a regular inquiry, or terminate simpliciter on material unrelated to the alleged misconduct", "11, 14", 2],
                ["Caution", "A probationer has no right to confirmation, but the department cannot use the probation route to punish misconduct without a hearing", "Explanation (viii)(a) to r.11", 1]],
         wrong=["<b>“A probationer can always be terminated without inquiry.”</b> Only where the termination is not founded on misconduct.",
                "<b>“The label decides.”</b> Substance decides.",
                "<b>“No inquiry is needed because she has no right to the post.”</b> The right to the post and the right to a hearing on misconduct are different questions."],
         answer=("Termination during probation is not a penalty, but where misconduct is the foundation the order is punitive in substance and required an "
                 "inquiry; on this record the termination is unsustainable."),
         tags=[["11", "Rule 11 — penalties"], ["14", "Rule 14 — procedure"]]),

    dict(id="L2-32", title="Termination of a temporary hand under TS Rule 5(1)",
         facts=("Shri Z, a temporary clerk appointed in 1998 and regularised in 2004, was served with a notice on 12.02.2026 terminating his services "
                "under rule 5(1) of the CCS (Temporary Service Rules), 1965, with one month's pay in lieu of notice. The accompanying note records that "
                "he had been absent without leave for 47 days and that “his services are no longer required”. He had 28 years' service and no inquiry "
                "was held."),
         record=[["Appointment", "1998, temporary", "regularised 2004"],
                 ["Notice", "12.02.2026", "TS Rule 5(1)"],
                 ["Allegation", "47 days' absence", "no inquiry"],
                 ["Service", "28 years", "—"],
                 ["Order", "one month's pay in lieu", "—"]],
         questions=["Is termination under TS Rule 5(1) a penalty?",
                    "Was the Temporary Service Rules route available to him in 2026?",
                    "What does the accompanying note reveal?",
                    "What is the consequence?"],
         path=["Explanation (viii)(b) to r.11", "not a penalty", "but TS Rules apply to temporary service", "regularised 2004 — no longer temporary", "foundation = misconduct"],
         steps=[["Issue", "Use of the Temporary Service Rules to terminate a regularised employee for misconduct", "Explanation (viii)(b) to r.11", 1],
                ["The exclusion", "Termination of a temporary Government servant under rule 5(1) of the Temporary Service Rules is not a penalty under the CCA Rules", "Explanation (viii)(b) to r.11", 1],
                ["Availability", "The Temporary Service Rules govern temporary service; an employee regularised in 2004 is not a temporary servant in 2026, so the route was not available to him", "CCS (TS) Rules, 1965", 2],
                ["The foundation", "The note attributes 47 days' absence without leave, which is misconduct; the order is therefore punitive in substance and needed an inquiry", "Radhey Shyam Gupta (1999)", 3],
                ["Pay in lieu", "Payment in lieu of notice does not convert a punitive termination into a simpliciter one", "Explanation (viii)(b) to r.11", 1],
                ["Consequence", "The termination is unsustainable; reinstatement with consequential benefits, or a fresh proceeding after a regular inquiry, follows", "11, 14", 1]],
         wrong=["<b>“TS Rule 5(1) can be used for anyone.”</b> It applies to temporary service, and he was regularised.",
                "<b>“One month's pay makes it lawful.”</b> The foundation, not the payment, decides.",
                "<b>“Absence without leave is not misconduct.”</b> It is, and its use as the foundation makes the order punitive."],
         answer=("The Temporary Service Rules did not apply to a clerk regularised in 2004, and the termination, founded on 47 days' absence, was punitive "
                 "in substance and required an inquiry; it is unsustainable."),
         tags=[["11", "Rule 11 — penalties"], ["14", "Rule 14 — procedure"]]),

    dict(id="L2-33", title="Sympathy as an exceptional case",
         facts=("A Group ‘B’ officer was found to hold assets of ₹1.42 crore disproportionate to his known sources of income. The inquiry established the "
                "charge. The disciplinary authority imposed reduction to a lower stage for three years, recording that the officer had 22 years of service, "
                "a daughter to marry and a clean record until then, and that dismissal would be “disproportionate to the circumstances”."),
         record=[["Assets", "₹1.42 crore", "disproportionate"],
                 ["Charge", "proved", "—"],
                 ["Penalty", "reduction, three years", "r.11(v)"],
                 ["Reasons", "service, family, clean record", "special reasons?"],
                 ["Statutory command", "removal or dismissal", "provisos to r.11"]],
         questions=["What penalty does the rule require on this charge?",
                    "Can family circumstances amount to an exceptional case?",
                    "What is the standard for “special reasons recorded in writing”?",
                    "What is the consequence of the order?"],
         path=["proviso to r.11", "removal or dismissal shall be imposed", "other penalty only exceptional + special reasons", "sympathy ≠ exceptional", "order unsustainable"],
         steps=[["Issue", "Penalty for possession of assets disproportionate to known sources", "provisos to 11", 1],
                ["The command", "Where the charge of disproportionate assets is established, the penalty in r.11(viii) or (ix) <i>shall</i> be imposed", "first proviso to 11", 3],
                ["The exception", "Any other penalty is permissible only in an exceptional case and for special reasons recorded in writing", "second proviso to 11", 2],
                ["Application", "Long service, a daughter's marriage and a previously clean record are mitigating circumstances, not exceptional ones; they would be present in most cases and cannot displace a statutory command", "second proviso to 11", 3],
                ["Consequence", "The order is unsustainable and must be set aside; the competent authority must impose removal or dismissal, or record genuinely exceptional reasons of a kind that distinguishes the case from the ordinary", "provisos to 11", 2]],
         wrong=["<b>“The authority has discretion in every case.”</b> The first proviso removes it except within the second.",
                "<b>“Long service is an exceptional circumstance.”</b> It is common, not exceptional.",
                "<b>“Proportionality permits any lesser penalty.”</b> Proportionality operates within the statutory command here."],
         answer=("The first proviso to <b>r.11</b> required removal or dismissal; family and service considerations are mitigating, not the exceptional case "
                 "contemplated by the second proviso, so the lesser penalty is unsustainable."),
         tags=[["11", "Rule 11 — penalties"]]),

    dict(id="L2-34", title="The Committee, the compensation and the promotion",
         facts=("A complaint of sexual harassment was made against Shri AA. The Complaints Committee conducted an inquiry following the r.14 procedure and "
                "found the complaint proved. It recommended payment of ₹3,00,000 as compensation and the penalty of withholding of promotion for two years. "
                "The disciplinary authority accepted both and passed a single order. Shri AA objects that the Committee had no power to hold the inquiry, that "
                "compensation is not a penalty known to the rules, and that he was never given a notice under r.16."),
         record=[["Complaint", "sexual harassment", "r.3C, Conduct Rules"],
                 ["Inquiry by", "Complaints Committee", "r.14 procedure followed"],
                 ["Recommendations", "₹3,00,000 + withholding of promotion", "—"],
                 ["Order", "single, both accepted", "no r.16 notice"],
                 ["Penalty class", "withholding of promotion", "r.11(ii), minor"]],
         questions=["Was the Complaints Committee competent to hold the inquiry?",
                    "Is compensation a penalty under the CCA Rules?",
                    "Was a r.16 notice necessary for the minor penalty?",
                    "Can both reliefs stand in one order?"],
         path=["proviso to r.14(2)", "Committee deemed inquiry authority", "compensation excluded from penalty", "minor penalty may follow r.14 inquiry via r.15(5)", "both may stand"],
         steps=[["Issue", "Competence of a Complaints Committee and the character of compensation", "proviso to 14(2); Explanation (ix) to 11", 1],
                ["Competence", "Where the complaint is of sexual harassment within rule 3C of the Conduct Rules, the Complaints Committee is deemed to be the inquiry authority appointed by the disciplinary authority", "proviso to 14(2)", 2],
                ["Compensation", "Compensation awarded on the recommendation of a Complaints Committee does not amount to a penalty within rule 11; it is a separate civil consequence and may be ordered", "Explanation (ix) to 11", 2],
                ["The minor penalty", "A minor penalty may be imposed after a r.14 inquiry without a separate r.16 notice, because r.15(5) expressly permits it notwithstanding r.16", "15(5)", 2],
                ["One order", "Both consequences may be recorded in one order provided each is separately reasoned and the employee has been heard on the inquiry report", "15(2), 15(5)", 2],
                ["Residual", "The quantum of compensation must be reasoned and proportionate; a figure with no working is vulnerable", "Explanation (ix) to 11", 1]],
         wrong=["<b>“The Committee cannot hold an inquiry.”</b> The proviso to r.14(2) deems it the inquiry authority.",
                "<b>“Compensation is an illegal penalty.”</b> It is expressly outside the definition of penalty.",
                "<b>“A r.16 notice was essential.”</b> Rule 15(5) allows a minor penalty after a r.14 inquiry."],
         answer=("The Complaints Committee was the deemed inquiry authority under the <b>proviso to r.14(2)</b>; compensation is not a penalty "
                 "(<b>Explanation (ix)</b>), the minor penalty could be imposed under <b>r.15(5)</b> without a separate r.16 notice, and both may stand if "
                 "separately reasoned."),
         tags=[["14", "Rule 14 — procedure"], ["11", "Rule 11 — penalties"], ["15", "Rule 15 — action on the report"]]),
]
