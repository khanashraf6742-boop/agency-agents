#!/usr/bin/env python3
"""titles.py — marginal headings of the 87 rules, from the gazette text.

Every heading here was read off the gazette as printed, either as the bold
marginal note beside the rule or, where the source sets the heading only in the
chapter text, as the title the rule itself carries. Rules 25 to 28 have their
numbers only: the taxguru copy sets out rules 25-28 in a block without repeating
the numbers, so those four headings were read from the block and paired by order.
"""
from __future__ import annotations

TITLES = {
    1: "Short title and commencement",
    2: "Application",
    3: "Definitions",
    4: "Application to existing Central Government servants",
    5: "Regulation of claims to pension and gratuity",
    6: "Pension subject to conditions",
    7: "Pension and family pension subject to future good conduct",
    8: "Power to withhold or withdraw pension",
    9: "Commercial employment after retirement",
    10: "Employment under any Government outside India",
    11: "Commencement of qualifying service",
    12: "Conditions subject to which service qualifies",
    13: "Service in State Governments",
    14: "Service in autonomous bodies",
    15: "Service rendered in temporary status by casual labourers",
    16: "Counting of service on probation",
    17: "Counting of service as apprentice",
    18: "Counting of service on contract",
    19: "Counting of pre-retirement civil service in the case of re-employed Government servants",
    20: "Counting of military service rendered before civil employment",
    21: "Counting of periods spent on leave",
    22: "Counting of periods spent on training",
    23: "Counting of periods of suspension",
    24: "Forfeiture of service on dismissal or removal",
    25: "Counting of past service on reinstatement",
    26: "Forfeiture of service on resignation",
    27: "Effect of interruption in service",
    28: "Condonation of interruption in service",
    29: "Deputation to United Nations and other organisations",
    30: "Periodic verification of qualifying service",
    31: "Emoluments",
    32: "Average emoluments",
    33: "Superannuation pension or service gratuity",
    34: "Retiring pension or service gratuity",
    35: "Pension on absorption in or under a State Government",
    36: "Pension on absorption in or under a corporation, company or body",
    37: "Conditions for payment of pension on absorption consequent upon conversion of a Government "
        "Department into a Public Sector Undertaking",
    38: "Conditions for payment of pension on absorption consequent upon conversion of a Government "
        "Department into a Central Autonomous Body",
    39: "Invalid pension",
    40: "Compulsory retirement pension",
    41: "Compassionate allowance",
    42: "Retirement on completion of thirty years' qualifying service",
    43: "Retirement on completion of twenty years' qualifying service",
    44: "Amount of pension",
    45: "Retirement gratuity and death gratuity",
    46: "Nominations",
    47: "Persons to whom gratuity is payable",
    48: "Debarring a person from receiving gratuity",
    49: "Lapse of retirement gratuity and death gratuity",
    50: "Family pension",
    51: "Entitlements of family of a missing Government servant or pensioner or family pensioner",
    52: "Dearness relief on pension and family pension",
    53: "Processing of pension cases in the online pension sanctioning system",
    54: "Preparation of list of Government servants due for retirement",
    55: "Intimation to the Directorate of Estates regarding issue of \u2018No Demand Certificate\u2019",
    56: "Preparation for processing of pension case",
    57: "Stages for the processing of pension case on superannuation",
    58: "Submission of forms by Government servant retiring for reasons other than superannuation",
    59: "Completion of pension case",
    60: "Forwarding of pension case to Accounts Officer",
    61: "Intimation to Accounts Officer regarding any event having bearing on pension or any Government dues",
    62: "Provisional pension for reasons other than departmental or judicial proceedings",
    63: "Authorisation of pension and gratuity by the Accounts Officer",
    64: "Government servants on deputation",
    65: "Interest on delayed payment of gratuity, pension and family pension",
    66: "Revision of pension after authorisation",
    67: "Recovery and adjustment of Government dues",
    68: "Adjustment and recovery of dues pertaining to Government accommodation",
    69: "Adjustment and recovery of dues other than dues pertaining to Government accommodation",
    70: "Date of retirement to be notified",
    71: "Obtaining of claims for family pension and gratuity",
    72: "Verification of service and emoluments for family pension and gratuity",
    73: "Action to be taken in cases where service records are incomplete",
    74: "Forwarding the family pension case to the Accounts Officer",
    75: "Sanction, drawal and disbursement of provisional family pension and provisional gratuity on death "
        "of a Government servant",
    76: "Authorisation of final family pension and balance of the gratuity by the Accounts Officer",
    77: "Adjustment of Government dues",
    78: "Payment of family pension and death gratuity when a Government servant dies or goes missing while "
        "on deputation",
    79: "Sanction of family pension and residuary gratuity on the death or disappearance of a pensioner or "
        "family pensioner",
    80: "Authorisation of payment by Accounts Officer",
    81: "Date from which pension becomes payable",
    82: "Currency in which pension is payable",
    83: "Manner of payment of gratuity and pension",
    84: "Application of other rules",
    85: "Interpretation",
    86: "Power to relax",
    87: "Repeal and saving",
}

if __name__ == "__main__":
    import pension_rules as pr
    missing = [n for n in range(1, 88) if n not in TITLES]
    extra = [n for n in TITLES if n not in range(1, 88)]
    print(f"{len(TITLES)} titles; missing {missing}; out of range {extra}")
    print(f"all rules transcribed: {sorted(int(k) for k in pr.TEXT) == list(range(1, 88))}")
