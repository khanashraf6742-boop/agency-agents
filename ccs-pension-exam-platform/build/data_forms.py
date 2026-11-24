#!/usr/bin/env python3
"""data_forms.py — Forms and Formats under the CCS (Pension) Rules, 2021.

Every item turns on the Form/Format distinction the statute itself draws in
rules 3(1)(k) and 3(1)(l), or on the prescribing rule recorded in forms.py.
"""
from __future__ import annotations

FACTS = []


def Q(fid, ch, rule, rules_text, topic, stem, ans, d1, d2, d3, why, safe, src, trap,
      kind="FORM", tag="Tough"):
    FACTS.append(dict(id=fid, ch=ch, rule=rule, rules_text=rules_text, topic=topic,
                      q=stem, a=ans, d=[d1, d2, d3], why=why, safe=safe, src=src,
                      trap=trap, kind=kind, tag=tag))


Q("PF-001", "II", "3", "Rule 3(1)(k) and 3(1)(l)", "Form and Format — the distinction",
  "The rules define a 'Form' and a 'Format' separately. Which is correct?",
  "A Form is a form appended to the rules; a Format is a format appended to them \u2014 two separate series",
  ("They are synonyms, and either word may be used for any appendix",
   "Rules 3(1)(k) and 3(1)(l) define them in two separate clauses."),
  ("A Form is used in service, a Format after retirement",
   "The distinction is by appendix, not by stage of service."),
  ("A Format is a form prescribed by a State Government",
   "Nothing in the definition ties a Format to a State."),
  "Rule 3(1)(k) defines a Form as a form appended to these rules; rule 3(1)(l) defines a Format as a format "
  "appended to them. The two series are appended separately and are numbered independently, which is why the "
  "rules can speak of Form 3 (nomination) and Format 3 (memorandum of charges) without confusion. When a question "
  "asks which instrument is prescribed, the answer depends on the clause, and the clause says Form or Format.",
  "Form and Format are two distinct appended series.",
  "Rules 3(1)(k) and 3(1)(l), CCS (Pension) Rules, 2021", "Treating Form and Format as interchangeable")

Q("PF-002", "VII", "46", "Rule 46(1)", "Nomination for gratuity",
  "A Government servant, on initial appointment, makes a nomination for retirement and death gratuity in:",
  "Form 3",
  ("Format 3",
   "Format 3 is the memorandum of charges to a pensioner under rule 8."),
  ("Form 1",
   "Form 1 is the application for commercial employment."),
  ("Form 9",
   "Form 9 is the claim a family member submits for gratuity."),
  "Rule 46(1) requires a Government servant, on his initial appointment, to make a nomination in Form 3 conferring "
  "on one or more persons the right to receive the retirement gratuity and death gratuity payable under rule 45. "
  "The nomination goes to the Head of Office, who verifies and countersigns it under rule 46(9)(b) and has an "
  "entry made in the service book.",
  "Nomination: Form 3, filed on initial appointment.",
  "Rule 46(1), CCS (Pension) Rules, 2021", "Answering Format 3 for the nomination")

Q("PF-003", "II", "8", "Rule 8(2)(c) proviso", "Memorandum of charges",
  "A memorandum of charges to be communicated to a pensioner under rule 8 is in:",
  "Format 3",
  ("Form 3",
   "Form 3 is the nomination for gratuity, which is a very different document."),
  ("Format 1",
   "Format 1 is the intelligence organisation's publication undertaking."),
  ("Form 9",
   "Form 9 is a family member's claim for gratuity."),
  "The proviso to rule 8(2)(c) requires the memorandum of charges to be communicated to the pensioner in Format 3. "
  "The Formats are the working papers of the proceedings side of the rules \u2014 the sanction to institute "
  "proceedings is Format 2, the charges are Format 3 \u2014 while the Forms belong mostly to the claims and "
  "certificates side.",
  "Charges memorandum: Format 3. Sanction: Format 2.",
  "Rule 8(2)(c) proviso, CCS (Pension) Rules, 2021", "Reaching for Form 3 because it is the better-known number")

Q("PF-004", "II", "7", "Rule 7(4)(b)", "RTI undertaking",
  "The undertaking on post-retirement publication, required of a servant of an Intelligence organisation, is in:",
  "Format 1",
  ("Form 1",
   "Form 1 begins the commercial-employment process."),
  ("Format 4",
   "Format 4 is the certificate of qualifying service."),
  ("Form 2",
   "Form 2 is the check list for commercial employment."),
  "Rule 7(4)(b) requires the undertaking in Format 1. A failure to observe it is treated as grave misconduct under "
  "rule 7, which is why the undertaking is a statutory document and not an internal formality. In a case of a "
  "servant transferred out of such an organisation, rule 7(4)(c) requires the undertaking in duplicate, one copy "
  "in the service book and one kept by the organisation.",
  "Publication undertaking: Format 1, and in duplicate on transfer.",
  "Rule 7(4)(b) and (c), CCS (Pension) Rules, 2021", "Answering Form 1 for the undertaking")

Q("PF-005", "III", "30", "Rule 30(1)", "Certificate of qualifying service",
  "The Head of Office communicates the qualifying service determined at verification to the servant in:",
  "Format 4",
  ("Form 4",
   "Form 4 is the particulars-of-family form."),
  ("Format 6",
   "Format 6 is the medical certificate of incapacity."),
  ("Format 5",
   "Format 5 is the relieving order on absorption in a State Government."),
  "Rule 30(1) requires the Head of Office, in consultation with the Accounts Officer, to verify service and "
  "communicate the qualifying service determined in Format 4 on two occasions: after eighteen years of service, "
  "and when five years of service remain before superannuation. Rule 30(4) makes that verification final and not "
  "open to reopening except on a change in the rules.",
  "Qualifying service certificate: Format 4, at 18 years and at 5 years to go.",
  "Rule 30(1) and (4), CCS (Pension) Rules, 2021", "Answering Form 4 for the certificate")

Q("PF-006", "V", "39", "Rule 39(8)", "Medical certificate of incapacity",
  "The medical authority's certificate of incapacity for service, leading to invalid pension, is issued in:",
  "Format 6",
  ("Form 5",
   "Form 5 is a medical certificate, but under the leave rules, not this one."),
  ("Format 3",
   "Format 3 is the memorandum of charges."),
  ("Form 6",
   "Form 6 is a different instrument again; the incapacity certificate is a Format."),
  "Rule 39(8) requires the medical authority to issue a Medical Certificate in Format 6, and if the servant is "
  "found unfit for further service, invalid pension may be granted under rule 44 not later than forty five days "
  "from the receipt of that certificate. The forty-five-day period is the testable figure: it runs from the "
  "receipt of the Format 6 certificate, not from the application.",
  "Incapacity certificate: Format 6; invalid pension within 45 days of receipt.",
  "Rule 39(8), CCS (Pension) Rules, 2021", "Confusing Format 6 with the leave rules' Form 5")

Q("PF-007", "II", "9", "Rule 9(1)", "Commercial employment application",
  "A pensioner applying for sanction to take up commercial employment applies in:",
  "Form 1",
  ("Format 1",
   "Format 1 is the publication undertaking."),
  ("Form 5",
   "Form 5 is not the right series for this; the application is a Form, and it is Form 1."),
  ("Format 2",
   "Format 2 is the President's sanction to institute proceedings."),
  "Rule 9(1) requires the application to be made in Form 1, and rule 9(5) requires the administrative Ministry to "
  "maintain a check list in Form 2. The two Form numbers sit next to each other and belong to the same procedure: "
  "the pensioner applies in Form 1 and the Ministry works the case on the Form 2 check list. A question that "
  "offers Format 1 is testing whether you noticed the word.",
  "Commercial employment: application in Form 1, check list in Form 2.",
  "Rules 9(1) and 9(5), CCS (Pension) Rules, 2021", "Answering Format 1 for the application")

Q("PF-008", "VII", "47", "Rule 47(7)", "Minor's share of gratuity",
  "Where there is no natural guardian, up to twenty per cent of a minor's share of gratuity may be paid on:",
  "An indemnity bond in Format 7",
  ("A succession certificate",
   "A succession certificate is the rule 49 route where there is no family and no nomination."),
  ("A guardianship certificate, which is always required",
   "The rule 47(7) procedure exists to allow payment without one, up to twenty per cent."),
  ("An affidavit sworn before a Magistrate",
   "The instrument is an indemnity bond, and it is a Format."),
  "Rule 47(7) allows payment of an amount not exceeding twenty per cent of the minor's share to a guardian without "
  "a guardianship certificate, on an indemnity bond in Format 7; the balance follows on production of the "
  "certificate of guardianship. Rule 47(6) prefers the natural guardian, and rule 47(5) makes the payment to the "
  "guardian on the minor's behalf.",
  "Minor's gratuity: 20 per cent on a Format 7 indemnity bond, balance on guardianship certificate.",
  "Rule 47(5) to (7), CCS (Pension) Rules, 2021", "Removing the twenty per cent ceiling")
