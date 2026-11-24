#!/usr/bin/env python3
"""forms.py — the Forms and Formats appended to the CCS (Pension) Rules, 2021.

Rule 3(1)(k) defines a "Form" as a form appended to these rules; rule 3(1)(l)
defines a "Format" as a format appended to them. They are two separate appended
series with independent numbering, which is why the statute can speak of Form 3
(the gratuity nomination) and Format 3 (the memorandum of charges) in the same
breath.

Each entry is (number, kind, title, prescribing provision, what it is for,
sourced). "sourced" is True only where the prescribing sub-rule was read in the
gazette text transcribed in pension_rules.py. An entry that is not sourced
carries no rule citation rather than a guessed one.
"""

FORMS = [
    ("Form 1", "Form", "Application for permission to accept commercial employment",
     "Rule 9(1)", "A pensioner applies for sanction to take up commercial employment after retirement.", True),
    ("Form 2", "Form", "Check list for considering an application for commercial employment",
     "Rule 9(5)", "The administrative Ministry works the commercial-employment case on this check list.", True),
    ("Form 3", "Form", "Nomination for retirement gratuity and death gratuity",
     "Rule 46(1)", "Filed by a Government servant on initial appointment; countersigned by the Head of Office.", True),
    ("Form 4", "Form", "Details of family",
     "Rules 50(15), 57(2)(a), 58(1)", "Family particulars for family pension; re-submitted with the pension papers.", True),
    ("Form 5", "Form", "Intimation of marriage, remarriage or birth of a child after retirement",
     "Rule 50(15)(f)", "Post-retirement change in family, with the marriage or birth certificate attached.", True),
    ("Form 6", "Form", "Form of application for pension and commutation, with bank particulars",
     "Rules 57(2)(b), 58(1), 80(5)(a)", "The substantive claim for pension; also the option for commutation.", True),
    ("Form 7", "Form", "Pension calculation sheet and check list, with account enfacement",
     "Rules 59(1), 60(1)(ii), 63(1)(a)", "Part I is completed by the Head of Office; Part II by the Accounts Officer.", True),
    ("Form 7-A", "Form", "Details of the final order in departmental or judicial proceedings",
     "Rule 63(5)(a)", "Forwarded by the Head of Office within thirty days of the order, to authorise the final pension.", True),
    ("Form 8", "Form", "Application by an existing pensioner or family pensioner",
     "Rule 63(1)(f)", "Asks the Accounts Officer to add a disabled child, dependent parent or disabled sibling to the PPO.", True),
    ("Form 9", "Form", "Claim for gratuity by a nominee or member of the family",
     "Rules 47(8), 71(2)(b), 75(7)(b)", "Submitted on the Format 11 letter; a missing claim does not stall the others.", True),
    ("Form 10", "Form", "Claim for family pension",
     "Rules 50(12)(c), 71(3), 76(9)(d), 79(2)(b)(i)", "The family pension claim, including the income declaration required by rule 50.", True),
    ("Form 11", "Form", "Family pension and gratuity case forwarded to the Accounts Officer",
     "Rules 74(1), 76(1)", "Completed by the Head of Office within one month of receipt of the claim.", True),
    ("Form 12", "Form", "Claim for family pension by a widow, widower or other eligible member of a pensioner",
     "Rule 79(2)(a)(ii)", "Claim against a pensioner's PPO, with the death certificate and a Format 9 undertaking.", True),
    ("Form 13", "Form", "Claim for residuary gratuity",
     "Rules 45(3), 79(6)", "Where the pensioner dies within five years of retirement and the 12-times test is not met.", True),
]

FORMATS = [
    ("Format 1", "Format", "Undertaking on post-retirement publication by an intelligence organisation servant",
     "Rule 7(4)(b)", "Required in duplicate on transfer out of the organisation; breach is grave misconduct.", True),
    ("Format 2", "Format", "Sanction of the President to institute departmental proceedings",
     "Rule 8(2)(c)(i)", "The sanction that opens proceedings against a pensioner on a cause of action before retirement.", True),
    ("Format 3", "Format", "Memorandum of charges communicated to the pensioner",
     "Rule 8(2)(c) proviso", "The charges themselves; Format 2 sanctions, Format 3 states them.", True),
    ("Format 4", "Format", "Certificate of qualifying service",
     "Rule 30(1)", "Issued at eighteen years of service and again with five years left before superannuation.", True),
    ("Format 5", "Format", "Relieving order on absorption in a State Government, corporation or autonomous body",
     "Rules 35(3), 36(4)", "States the period within which the servant must join; extendable for recorded reasons.", True),
    ("Format 6", "Format", "Medical certificate of incapacity for service",
     "Rule 39(8)", "Invalid pension follows within forty five days of receipt of this certificate.", True),
    ("Format 7", "Format", "Indemnity bond for a minor's share of gratuity",
     "Rule 47(7)", "Allows up to twenty per cent to be paid without a guardianship certificate.", True),
    ("Format 8", "Format", "Indemnity bond for the family of a missing servant, pensioner or family pensioner",
     "Rules 51(5)(b), 71(6)(d), 79(3)(iii)", "Accompanies the police report in a missing-person case.", True),
    ("Format 9", "Format", "Undertaking to the bank",
     "Rules 57(2)(a), 63(4)(a), 74(1), 80(2)", "Filed with the pension papers and forwarded with the PPO for the Special Seal.", True),
    ("Format 10", "Format", "Covering letter forwarding a pension or family pension case to the Accounts Officer",
     "Rules 60(1)(ii), 74(1), 80(5)(c)", "Carries the assessment of Government dues under rule 67.", True),
    ("Format 11", "Format", "Letter to the nominee or family member inviting a gratuity claim",
     "Rules 71(2)(b), 71(6)(a)", "Invites the claim in Form 9.", True),
    ("Format 12", "Format", "Letter to the eligible family member or guardian inviting a family pension claim",
     "Rules 71(3), 71(6)(b), 79(3)(ii)", "Invites the claim in Form 10.", True),
    ("Format 13", "Format", "Sanction of family pension by the Head of Office",
     "Rules 79(2)(b)(i), 79(3)(iv), 80(5)(b)", "Issued where the PPO does not already name the person now entitled.", True),
]

# Forms appended to the CCS (Leave) Rules, 1972. Rule 3(h) of those rules defines
# a "Form" as a Form appended to the Second Schedule; the leave rules have that one
# appended series and no separate Formats series.
LEAVE_FORMS = [
    ("Form 1", "Form", "Application for leave or extension of leave", "Rule 14",
     "Signed by the servant, or by the spouse, parent, major child or limited guardian on a disability.", True),
    ("Form 2", "Form", "Form of leave account", "Rule 15",
     "Maintained by the Audit Officer for Gazetted and the Head of Office for non-Gazetted servants.", True),
    ("Form 3", "Form", "Medical certificate for Gazetted officers", "Rule 19",
     "Required for leave on medical certificate; waiver only up to three days.", True),
    ("Form 3-A", "Form", "Medical certificate for disability cases", "Rules 19, 20",
     "Used where the disability route is invoked.", True),
    ("Form 4", "Form", "Medical certificate for non-Gazetted servants", "Rule 19",
     "The counterpart of Form 3 for non-Gazetted staff.", True),
    ("Form 5", "Form", "Medical certificate of fitness to return to duty", "Rule 24(3)",
     "Filed on return from leave on medical certificate.", True),
    ("Form 6", "Form", "Bond for a temporary Government servant \u2014 extraordinary leave for study", "Rule 32(3)",
     "Binds a temporary servant who takes extraordinary leave to pursue study.", True),
    ("Form 7", "Form", "Bond for a permanent Government servant \u2014 study leave", "Rule 53(4)",
     "Three-year bond; five years for the Central Health Service.", False),
    ("Form 8", "Form", "Bond for extension of study leave \u2014 permanent servant", "Rule 53(4)",
     "Executed where study leave is extended.", False),
    ("Form 9", "Form", "Bond for a non-permanent Government servant \u2014 study leave", "Rule 53(4)",
     "The non-permanent counterpart of Form 7.", False),
    ("Form 10", "Form", "Bond for extension of study leave \u2014 non-permanent servant", "Rule 53(4)",
     "The non-permanent counterpart of Form 8.", False),
]

if __name__ == "__main__":
    print(f"pension Forms {len(FORMS)} (sourced {sum(1 for f in FORMS if f[5])}) / "
          f"Formats {len(FORMATS)} (sourced {sum(1 for f in FORMATS if f[5])}) / "
          f"leave Forms {len(LEAVE_FORMS)} (sourced {sum(1 for f in LEAVE_FORMS if f[5])})")
