#!/usr/bin/env python3
"""amendments.py — every instrument that has changed the CCS (Pension) Rules, 2021.

The 2021 gazette is not the current law. Three sets of amendment rules have been
notified since (2022, 2024, 2025), and the Department of Pension and Pensioners'
Welfare has issued office memoranda that operate on the rules without amending
their text. This module records both, because the difference matters: a question
that quotes rule 45(1) as "twenty lakh rupees" is quoting the rule correctly and
stating the entitlement wrongly, and only a register that carries both can say so.

Each entry records:
    id        short handle used by questions and by the audit
    kind      "rules" for a gazette amendment, "om" for an office memorandum
    number    the G.S.R. number or the file number printed on the order
    date      date of the order
    effective the date the change takes effect, in the order's own words where it
              is not a plain date
    affects   the provision paths the instrument touches, as provisions.py
              addresses them
    effect    what it does, in one sentence
    before / after  the text that changed, where the instrument substitutes text
    status    "in force", "superseded", or "reiterated"
    source    where the text was read
    verified  "gazette text" when the full operative text was read, "summary"
              when only a reliable summary was seen

Nothing here is reconstructed from memory. Where the full text was not obtained,
the entry says so in `verified` and the platform shows that flag.
"""
from __future__ import annotations

AMENDMENTS = [

    # ------------------------------------------------------------------ 2022
    dict(
        id="A-2022-01",
        kind="rules",
        number="G.S.R. 770(E)",
        title="Central Civil Services (Pension) Amendment Rules, 2022",
        date="07.10.2022",
        effective="07.10.2022 (date of publication in the Official Gazette)",
        affects=["8(1)", "8(2)(a)#P1", "8(2)(c)", "8(4)(d)", "8(6)", "8(6)",
                 "20(1)(iii)#E1", "46(5)(a)", "50(9)(h)", "76(5)"],
        effect=(
            "Rewrites the power to withhold or withdraw pension so that the competent authority is the "
            "President only where the President is the appointing authority, and otherwise the Secretary of "
            "the administrative Ministry or Department, or the Comptroller and Auditor-General for the "
            "Indian Audit and Accounts Department; adds sub-rule (6A) providing an appeal to the President; "
            "and makes four consequential corrections in rules 20, 46, 50 and 76."
        ),
        before=(
            "(1) The President reserves to himself the right of withholding a pension or gratuity ... and of "
            "ordering recovery ... if, in any departmental or judicial proceedings, the pensioner is found "
            "guilty of grave misconduct or negligence ..."
        ),
        after=(
            "(1)(a) The President, in the case of a pensioner who retired from a post for which the President "
            "is the appointing authority; (b) the Secretary of the Administrative Ministry or Department, in "
            "the case of a pensioner who retired from a post for which an authority subordinate to the "
            "President is the appointing authority; and (c) the Comptroller and Auditor-General of India ... "
            "may, by order in writing, withhold a pension or gratuity, or both ..."
        ),
        status="in force",
        source="G.S.R. 770(E), Gazette of India, Part II, Sec. 3, sub-sec. (i), 7 October 2022",
        verified="gazette text",
        note=(
            "Sub-rule (6A)(a) is absolute: no appeal lies against an order made by the President. An appeal "
            "against an order of any other authority lies to the President, who decides it in consultation "
            "with the Union Public Service Commission."
        ),
    ),

    # ------------------------------------------------------------------ 2024
    dict(
        id="A-2024-01",
        kind="rules",
        number="G.S.R. 410(E)",
        title="Central Civil Services (Pension) Amendment Rules, 2024",
        date="16.07.2024",
        effective=(
            "after one hundred twenty days from the date of publication in the Official Gazette "
            "(the notification's own words; 16.07.2024 + 120 days is 13.11.2024)"
        ),
        affects=["50(15)(e)", "53(1)", "53(2)(a)", "53(2)(b)", "57(1)(c)(iii)", "57(2)(a)",
                 "57(3)(a)", "57(3)(b)", "57(3)(b)#P1", "58(1)", "58(2)(a)", "58(2)(b)",
                 "58(2)(b)#P1", "59(1)", "59(2)", "60(1)(i)", "60(3)", "60(4)", "62(6)(a)",
                 "63(4)(a)", "63(4)(b)", "80(5)(a)#P1", "80(5)(c)"],
        effect=(
            "Introduces a single pension application form, Form 6-A, replacing Form 4, Form 6 and the "
            "undertaking to the Bank in Format 9 across the retirement process; substitutes clause (e) of "
            "rule 50(15) so that family details are furnished in Form 6-A at retirement; and rewrites rule "
            "80(5) so that where no family member is eligible for family pension the gratuity nominee may "
            "submit Form 6-A in place of Form 10."
        ),
        before=(
            "rule 50(15)(e): the Government servant shall submit the up to date details of the family in "
            "Form 4 again along with the pension papers"
        ),
        after=(
            "rule 50(15)(e): The Government servant shall submit the up to date details of the family again "
            "in Form 6-A at the time of retirement from Government service."
        ),
        status="in force",
        source="G.S.R. 410(E), Gazette of India, 16 July 2024 [F. No. 55/13/2023-P&PW(C)]",
        verified="gazette text",
        note=(
            "Rule 57(3) now carries a proviso that where Form 6-A is submitted by the spouse or another "
            "family member, the Government servant is not entitled to commutation until he applies for it "
            "himself under the CCS (Commutation of Pension) Rules, 1981. Rule 80(5)(c) now reads "
            "\"Form 4, Form 10, Format 9 and Format 13 (if applicable) or Form 6-A, as the case may be\"."
        ),
    ),
    dict(
        id="A-2024-02",
        kind="om",
        number="No. 1/1(1)/2023-P&PW(E)",
        title=(
            "Allowing a female Government servant or female pensioner to nominate her child or children for "
            "family pension in precedence to her husband"
        ),
        date="01.01.2024",
        effective="01.01.2024",
        affects=["50(8)", "50(9)", "50(6)(i)"],
        effect=(
            "Where divorce proceedings are pending in a competent court, or the woman has filed a case "
            "against her husband under the Protection of Women from Domestic Violence Act, the Dowry "
            "Prohibition Act or the Indian Penal Code, she may ask in writing that family pension be paid to "
            "her eligible child or children in precedence to her husband; the order then sets out five ways "
            "in which the pension is to be disbursed."
        ),
        before=(
            "rule 50(8)(a): family pension at the rate specified in sub-rule (2) shall be payable to such "
            "widow or widower, up to the date of death or re-marriage, whichever is earlier"
        ),
        after=(
            "Same text, read with the order: on a request under paragraph 3(a), family pension is disbursed "
            "to the eligible child or children first, and to the widower only where no child is eligible, or "
            "after all the children cease to be eligible."
        ),
        status="in force (administrative instruction)",
        source=(
            "DoP&PW O.M. No. 1/1(1)/2023-P&PW(E) dated 1 January 2024, paragraphs 3(a), 3(b)(i)-(v) and 6"
        ),
        verified="order text",
        note=(
            "Paragraph 6 of the order says a formal amendment to rule 50 \"will be notified separately\". No "
            "such amendment appears in the gazette series up to the 2025 amendment, so the order operates on "
            "the rule as an instruction and the rule text itself is unchanged. A question that asks for the "
            "statutory text of rule 50(8) therefore still gets the spouse-first answer; a question that asks "
            "what the Department has decided gets the child-first answer. The platform carries both."
        ),
    ),
    dict(
        id="A-2024-03",
        kind="om",
        number="No. 28/03/2024-P&PW(B)/Gratuity/9559",
        title=(
            "Enhancement of the maximum limit of gratuity to Central Government employees on reaching the "
            "Dearness Allowance rate of 50 per cent"
        ),
        date="30.05.2024",
        effective="01.01.2024",
        affects=["45(1)", "45(1)(b)(v)#P1"],
        effect=(
            "Raises the maximum limit of retirement gratuity and death gratuity under the CCS (Pension) "
            "Rules, 2021 and the CCS (Payment of Gratuity under NPS) Rules, 2021 by 25 per cent, from "
            "Rs 20.00 lakh to Rs 25.00 lakh, with effect from 1 January 2024, triggered by the dearness "
            "allowance rate reaching 50 per cent."
        ),
        before="maximum of twenty lakh rupees under rule 45(1)",
        after="maximum of twenty-five lakh rupees, with effect from 1 January 2024",
        status="in force (administrative instruction)",
        source="DoP&PW O.M. No. 28/03/2024-P&PW(B)/Gratuity/9559 dated 30 May 2024, paragraphs 3 and 7",
        verified="order text",
        note=(
            "Paragraph 7 says the formal amendment to both rule sets \"will be notified separately\". The rule "
            "text therefore still prints twenty lakh rupees. A pension case decided on or after 1 January "
            "2024 is settled at twenty-five lakh rupees under this order, not under the printed rule."
        ),
    ),
    dict(
        id="A-2024-04",
        kind="om",
        number="F.No. 38/10(04)/2024-P&PW(A) (e 10124)",
        title=(
            "Conditions for grant of additional pension to retired Central Government civil employees covered "
            "under the CCS (Pension) Rules, 2021"
        ),
        date="18.10.2024",
        effective="payable from the first day of the calendar month in which it falls due",
        affects=["44(6)", "50(3)"],
        effect=(
            "Reiterates the age-band table in rule 44(6): additional pension of 20 per cent from 80 years, "
            "30 per cent from 85, 40 per cent from 90, 50 per cent from 95 and 100 per cent from 100 years, "
            "and fixes the date of payment at the first day of the calendar month in which the pensioner "
            "reaches the age band."
        ),
        before="rule 44(6) table, as printed",
        after="same table, with the worked illustration of a pensioner born on 20 August 1942 drawing the "
              "20 per cent increment from 1 August 2022",
        status="reiterated",
        source="DoP&PW O.M. F.No. 38/10(04)/2024-P&PW(A) dated 18 October 2024",
        verified="order text",
        note=(
            "The order confirms that the rule 44(6) table is current and has not been revised upward. "
            "The illustration is examinable: entitlement runs from the first day of the birth month in which "
            "the age is reached, not from the birthday."
        ),
    ),

    # ------------------------------------------------------------------ 2025
    dict(
        id="A-2025-01",
        kind="rules",
        number="G.S.R. 340(E)",
        title="Central Civil Services (Pension) Amendment Rules, 2025",
        date="22.05.2025",
        effective="22.05.2025 (published in the Gazette on 23.05.2025; in force on publication)",
        affects=["37(29)(c)"],
        effect=(
            "Reverses the protection given to a Government servant absorbed in a public sector undertaking: "
            "dismissal, removal or retrenchment from the undertaking for subsequent misconduct now forfeits "
            "the retirement benefits for the Government service as well, and the undertaking's decision is "
            "subject to review by the administrative Ministry. Rules 7 and 8 read with rule 41 and rule 44(5) "
            "apply analogously."
        ),
        before=(
            "rule 37(29)(c): the dismissal or removal from service of the public sector undertaking ... shall "
            "not amount to forfeiture of the retirement benefits for the service rendered under the Government"
        ),
        after=(
            "rule 37(29)(c): the dismissal or removal from service of the public sector undertaking ... for "
            "any subsequent misconduct shall lead to forfeiture of the retirement benefits for the service "
            "rendered under the Government also"
        ),
        status="in force",
        source="G.S.R. 340(E), Gazette of India, 23 May 2025 [F. No. 04/17/2023-P&PW(D)]",
        verified="gazette text",
        note=(
            "The same protection still stands for an employee absorbed in an autonomous body: rule 37(26)(c) "
            "was not touched. The amendment gives effect to the Supreme Court's order of 9 January 2023 in "
            "Suraj Pratap Singh v. CMD BSNL."
        ),
    ),
    dict(
        id="A-2025-02",
        kind="om",
        number="F.No. 2/9/2025-P&PW(F)",
        title="Applicability of the twenty-five lakh rupee gratuity ceiling",
        date="24.10.2025",
        effective="24.10.2025",
        affects=["45(1)"],
        effect=(
            "Restricts the enhanced ceiling to persons governed by the CCS (Pension) Rules, 2021 and the CCS "
            "(Payment of Gratuity under NPS) Rules, 2021, and states that it does not apply to public sector "
            "undertakings, banks, port trusts, the Reserve Bank of India, autonomous bodies, universities, "
            "State Governments or societies."
        ),
        before="ceiling of twenty-five lakh rupees, scope unstated",
        after="ceiling of twenty-five lakh rupees, limited to the two central rule sets",
        status="in force (clarification)",
        source="DoP&PW O.M. F.No. 2/9/2025-P&PW(F) dated 24 October 2025",
        verified="summary",
        note="Read with A-2024-03, which raised the ceiling but did not state its scope.",
    ),
    dict(
        id="A-2025-03",
        kind="om",
        number="F.No. 2/8/2025-P&PW(F)",
        title="Gratuity under the CCS (Payment of Gratuity under NPS) Rules, 2021 on resignation",
        date="24.10.2025",
        effective="24.10.2025",
        affects=[],
        effect=(
            "Resignation, other than resignation to take up another appointment under the Government, does "
            "not earn gratuity; gratuity requires five years' qualifying service and discharge by "
            "superannuation, invalidation, voluntary retirement or absorption."
        ),
        before="",
        after="",
        status="in force (clarification)",
        source="DoP&PW O.M. F.No. 2/8/2025-P&PW(F) dated 24 October 2025",
        verified="summary",
        note=(
            "This is the NPS gratuity rule set, not the CCS (Pension) Rules, 2021, and is included only "
            "because it is frequently confused with the resignation provisions of rule 44."
        ),
    ),
    dict(
        id="A-2025-04",
        kind="om",
        number="F.No. 1/1(11)/2024-P&PW(F)",
        title=(
            "Settlement of family pension between two wives of a Government servant or pensioner under the "
            "CCS (Pension) Rules, 2021"
        ),
        date="27.10.2025",
        effective="27.10.2025",
        affects=["50(6)", "50(6)(iv)#E1", "50(8)(c)"],
        effect=(
            "Directs that a case involving a second wife while the first wife is alive be decided under the "
            "Rules, and that the legality of the second marriage be settled first in consultation with the "
            "Department of Legal Affairs, case by case, before eligibility for family pension is decided."
        ),
        before="",
        after="",
        status="in force (instruction)",
        source="DoP&PW O.M. dated 27 October 2025",
        verified="summary",
        note=(
            "The Explanation to rule 50(6) defines widow and widower as a spouse legally wedded to the "
            "deceased, which is what makes the reference to the Department of Legal Affairs necessary."
        ),
    ),
    dict(
        id="A-2025-05",
        kind="om",
        number="F.No. 1/1(11)/2024-P&PW(F)",
        title="Clarification on the enhanced rate of family pension in death-after-retirement cases",
        date="27.10.2025",
        effective="27.10.2025",
        affects=["50(2)(a)(iii)"],
        effect=(
            "Confirms that the enhanced rate is payable for seven years or until the retired Government "
            "servant would have attained sixty-seven years, whichever is earlier, irrespective of whether "
            "the retirement age was 60 or 65 years."
        ),
        before="",
        after="",
        status="in force (clarification)",
        source="DoP&PW O.M. dated 27 October 2025",
        verified="summary",
        note="The rule says sixty-seven years; the order explains that the age does not shift with the retirement age.",
    ),

    # ------------------------------------------------------------------ 2026
    dict(
        id="A-2026-01",
        kind="om",
        number="No. 1/1(39)/2026-P&PW(E)/E-12002-(1)",
        title="Order of priority among eligible family members for payment of family pension",
        date="29.10.2026",
        effective="29.10.2026",
        affects=["50(6)", "50(6)(i)", "50(6)(ii)", "50(6)(iii)", "50(6)(iv)",
                 "50(8)(e)", "50(8)(f)", "50(8)(g)", "50(9)"],
        effect=(
            "Reiterates the statutory order of eligibility: spouse first, then children of three categories "
            "(children in order of birth until 25, marriage or livelihood; then children with a disability, "
            "for life; then unmarried, widowed or divorced daughters), then dependent parents with the "
            "mother ordinarily preceding the father, then dependent siblings with a disability."
        ),
        before="",
        after="",
        status="reiterated",
        source="DoP&PW O.M. No. 1/1(39)/2026-P&PW(E)/E-12002-(1) dated 29 October 2026",
        verified="order text",
        note=(
            "Paragraph 5 refers to rule 50(8)(e) to (g) by their letters. Those clauses were missing from "
            "the first transcription of rule 50 on this platform and were restored when this cross-reference "
            "was resolved. Paragraph 4 records the two exceptions: the female nominee in marital discord, and "
            "the judicially separated spouse who comes after the children."
        ),
    ),
    dict(
        id="A-2026-02",
        kind="om",
        number="No. 1/1(39)/2026-P&PW(E)/E-12002-(7)",
        title="Family pension entitlement in cases of divorce and judicial separation of a spouse",
        date="29.10.2026",
        effective="29.10.2026",
        affects=["50(8)(h)", "50(8)(i)", "50(8)(j)"],
        effect=(
            "A decree of judicial separation does not dissolve the marriage, and a judicially separated "
            "widow or widower may be considered under rule 50(8)(h) to (j). A divorced spouse is not "
            "eligible, though the children of the marriage may be."
        ),
        before="",
        after="",
        status="reiterated",
        source="DoP&PW O.M. No. 1/1(39)/2026-P&PW(E)/E-12002-(7) dated 29 October 2026",
        verified="order text",
        note=(
            "This order is the reason clauses (h), (i) and (j) of rule 50(8) had to be restored: it decides "
            "cases under them by name."
        ),
    ),
    dict(
        id="A-2026-03",
        kind="om",
        number="No. 1/1(39)/2026-P&PW(E)/E-12002",
        title="Quantum of family pension under rule 50(2)",
        date="29.10.2026",
        effective="29.10.2026",
        affects=["50(2)(a)(i)", "50(2)(a)(ii)", "50(2)(a)(iii)", "50(2)(a)(iv)"],
        effect=(
            "Reiterates ordinary family pension at 30 per cent of pay subject to Rs 9,000 to Rs 75,000 and "
            "enhanced family pension at 50 per cent subject to Rs 9,000 to Rs 1,25,000, and repeats that the "
            "sixty-seven year limit is fixed and does not move with the age of superannuation."
        ),
        before="",
        after="",
        status="reiterated",
        source="DoP&PW O.M. dated 29 October 2026",
        verified="summary",
        note="Confirms the figures in rule 50(2)(a)(i) and (iv) are current and have not been revised.",
    ),
    dict(
        id="A-2026-04",
        kind="om",
        number="No. 1/1(39)/2026-P&PW(E)",
        title=(
            "Not earning a livelihood and dependency while determining eligibility for family pension"
        ),
        date="29.10.2026",
        effective="29.10.2026",
        affects=["50(9)(b)", "50(9)(c)", "50(10)(b)#E1", "50(11)(b)#E1"],
        effect=(
            "Explains the income test that decides whether a claimant is earning a livelihood, and the "
            "distinction between a child or sibling with a disability and other members of the family."
        ),
        before="",
        after="",
        status="reiterated",
        source="DoP&PW O.M. dated 29 October 2026",
        verified="summary",
        note="The threshold in the rule is the minimum family pension plus the dearness relief admissible on it.",
    ),
    dict(
        id="A-2026-05",
        kind="om",
        number="No. 1/1(39)/2026-P&PW(E)",
        title=(
            "Procedure for intimation and recording of widowhood or divorce of a pensioner daughter"
        ),
        date="29.10.2026",
        effective="29.10.2026",
        affects=["50(9)(j)", "50(15)(g)"],
        effect=(
            "Sets out how the Head of Office is to be told of a daughter's widowhood or divorce so that a "
            "future family pension claim can be considered."
        ),
        before="",
        after="",
        status="reiterated",
        source="DoP&PW O.M. dated 29 October 2026",
        verified="summary",
        note="Rule 50(15)(g) already requires intimation of a post-retirement change in the family.",
    ),
    dict(
        id="A-2026-06",
        kind="om",
        number="No. 1/1(39)/2026-P&PW(E)",
        title=(
            "Inclusion and co-authorisation of eligible family members as family pensioners in the Pension "
            "Payment Order"
        ),
        date="29.10.2026",
        effective="29.10.2026",
        affects=["63(4)", "63(5)", "79(2)(a)(iv)"],
        effect=(
            "Explains when the name of a family member is entered in the Pension Payment Order as a "
            "co-authorised family pensioner, and the note that a disabled child, dependent parent or disabled "
            "sibling is added only where there is no other eligible prior claimant."
        ),
        before="",
        after="",
        status="reiterated",
        source="DoP&PW O.M. dated 29 October 2026",
        verified="summary",
        note="",
    ),
    dict(
        id="A-2026-07",
        kind="om",
        number="No. 1/1(39)/2026-P&PW(E)",
        title=(
            "Prescribed forms and formats relevant for pensioners and family pensioners and their online "
            "availability"
        ),
        date="29.10.2026",
        effective="29.10.2026",
        affects=["80(5)"],
        effect=(
            "Lists the forms and formats currently prescribed and where they are published, following the "
            "consolidation into Form 6-A by G.S.R. 410(E)."
        ),
        before="",
        after="",
        status="in force (instruction)",
        source="DoP&PW O.M. dated 29 October 2026",
        verified="summary",
        note="",
    ),
    dict(
        id="A-2026-08",
        kind="om",
        number="No. 1/1(39)/2026-P&PW(E)",
        title="Sanction and payment of provisional family pension on the death of a serving Government servant",
        date="29.10.2026",
        effective="29.10.2026",
        affects=["76(1)"],
        effect=(
            "Restates the provisional family pension mechanism under rule 76 so that a family is not left "
            "without support while final authorisation is in process."
        ),
        before="",
        after="",
        status="reiterated",
        source="DoP&PW O.M. dated 29 October 2026",
        verified="summary",
        note="",
    ),
]

# rules that an instrument has changed, for the "as amended" banner on a rule card
BY_RULE: dict[int, list[str]] = {}
for _a in AMENDMENTS:
    for _p in _a["affects"]:
        _head = _p.split("(")[0].split("#")[0]
        _r = int(_head) if _head.isdigit() else 0
        if _r:
            BY_RULE.setdefault(_r, [])
            if _a["id"] not in BY_RULE[_r]:
                BY_RULE[_r].append(_a["id"])


def for_rule(n: int) -> list[dict]:
    ids = BY_RULE.get(int(n), [])
    return [a for a in AMENDMENTS if a["id"] in ids]


def get(aid: str) -> dict:
    for a in AMENDMENTS:
        if a["id"] == aid:
            return a
    raise KeyError(aid)


if __name__ == "__main__":
    print(f"{len(AMENDMENTS)} instruments")
    kinds = {}
    for a in AMENDMENTS:
        kinds[a["kind"]] = kinds.get(a["kind"], 0) + 1
    print(" ", kinds)
    print(f"verified at full text: {sum(1 for a in AMENDMENTS if a['verified'] != 'summary')}")
    touched = sorted({int(k) for k in BY_RULE})
    print(f"rules touched: {len(touched)} -> {touched}")
