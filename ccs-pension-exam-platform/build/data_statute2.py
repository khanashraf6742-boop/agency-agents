#!/usr/bin/env python3
"""data_statute2.py — statutory questions, Chapters VII to X."""
from __future__ import annotations

from data_statute import Q

FACTS = []


def Q2(*a, **k):
    before = len(__import__("data_statute", fromlist=["FACTS"]).FACTS)
    Q(*a, **k)
    import data_statute as ds
    FACTS.append(ds.FACTS.pop())


Q2("PS-017", "VII", "44", "Rule 44(6)", "Additional pension",
  "A pensioner drawing a basic pension of \u20b940,000 attains 92 years of age. His additional pension is:",
  "\u20b916,000, being 40 per cent",
  ("\u20b912,000, being 30 per cent", "Thirty per cent is the band for 85 to under 90 years."),
  ("\u20b920,000, being 50 per cent", "Fifty per cent is the band for 95 to under 100 years."),
  ("\u20b940,000, being 100 per cent", "One hundred per cent is reached only at 100 years or more."),
  "Rule 44(6) pays additional pension by band: 20 per cent from 80 to under 85 years, 30 per cent from 85 to under "
  "90, 40 per cent from 90 to under 95, 50 per cent from 95 to under 100, and 100 per cent at 100 years or more. At "
  "92 the band is 40 per cent, which on a basic pension of \u20b940,000 is \u20b916,000. The additional pension is "
  "payable from the first day of the calendar month in which it falls due.",
  "92 years: the 40 per cent band.",
  "Rule 44(6)(a), CCS (Pension) Rules, 2021", "Using the 85-year or 95-year band")

Q2("PS-018", "VII", "44", "Rule 44(7) and (8)", "Fractional qualifying service",
  "A servant retires with 27 years and 4 months of qualifying service. For rule 44 the service is reckoned as:",
  "27 years and 6 months",
  ("27 years exactly", "Four months is three months or more, so it becomes a completed six-monthly period."),
  ("28 years", "The rounding is to a six-monthly period, not to a whole year."),
  ("27 years and 9 months", "The fraction becomes one six-monthly period, not two."),
  "Rule 44(7) provides that in calculating the length of qualifying service a fraction of a year equal to three months "
  "and above is treated as a completed six-monthly period and reckoned as qualifying service. Four months reaches "
  "that threshold, so 27 years and 4 months is reckoned as 27 years and 6 months. Rule 44(8) makes a separate "
  "concession for nine years and nine months or more, treating it as ten years so that pension is payable at all.",
  "Three months or more becomes a completed six-monthly period.",
  "Rule 44(7) and (8), CCS (Pension) Rules, 2021", "Rounding to a whole year, or dropping the fraction")

Q2("PS-019", "VII", "44", "Rule 44(9)", "Rounding of pension",
  "A pension finally determined under rule 44 comes to \u20b924,750.50. The amount payable is:",
  "\u20b924,751",
  ("\u20b924,750", "The rule rounds to the next higher rupee, not to the nearest rupee."),
  ("\u20b924,750.50, because pensions may be expressed in paise", "Rule 44(9) requires expression in whole rupees."),
  ("\u20b924,800, rounded to the nearest hundred", "There is no rounding to hundreds in the rule."),
  "Rule 44(9) requires the amount of pension, service gratuity, compassionate allowance, additional pension and "
  "additional compassionate allowance finally determined to be expressed in whole rupees, with any fraction of a "
  "rupee rounded off to the next higher rupee, separately for each amount. Rule 44(10) applies the same rounding to "
  "the pension payable for a fraction of a month where pension is discontinued mid-month.",
  "Round up to the next rupee, separately for each amount.",
  "Rule 44(9) and (10), CCS (Pension) Rules, 2021", "Rounding to the nearest rupee instead of upwards")

Q2("PS-020", "VII", "45", "Rule 45(1)(b) Table", "Death gratuity rates",
  "A servant dies in service with 7 years of qualifying service and emoluments of \u20b950,000. The death gratuity is:",
  "\u20b96,00,000",
  ("\u20b93,00,000", "That is the six-times rate for one year or more but less than five years."),
  ("\u20b91,00,000", "That is the two-times rate for less than one year."),
  ("\u20b910,00,000", "That is the twenty-times rate, reached only at eleven years."),
  "Rule 45(1)(b) pays death gratuity by band: twice emoluments below one year, six times at one year or more but under "
  "five, twelve times at five years or more but under eleven, twenty times at eleven years or more but under twenty, "
  "and half of emoluments for every completed six-monthly period beyond twenty years, capped at thirty-three times. "
  "Seven years falls in the twelve-times band, so \u20b950,000 gives \u20b96,00,000.",
  "Seven years: twelve times emoluments.",
  "Rule 45(1)(b), CCS (Pension) Rules, 2021", "Using the twenty-times band for a seven-year death")

Q2("PS-021", "VII", "45", "Rule 45(3)", "Residuary gratuity",
  "A servant retires, draws pension and retirement gratuity, and dies three years later. A residuary gratuity is "
  "payable where the sums he received:",
  "fall short of twelve times his emoluments, and the deficiency is then paid to his family",
  ("fall short of sixteen and a half times his emoluments",
   "Sixteen and a half times is the cap on retirement gratuity under rule 45(1)(a)."),
  ("fall short of thirty-three times his emoluments", "Thirty-three times is the cap on death gratuity."),
  ("fall short of five years' pension", "The comparison is with twelve times emoluments, not five years of pension."),
  "Rule 45(3) applies where a servant who became eligible for service gratuity or pension dies within five years of "
  "retirement, including compulsory retirement as a penalty, and the sums actually received by him on account of "
  "gratuity or pension, together with the retirement gratuity and the commuted value of any commuted portion, are "
  "less than twelve times his emoluments. A residuary gratuity equal to the deficiency is then paid to the family in "
  "the manner indicated in rule 47(1).",
  "Residuary gratuity: top up to twelve times emoluments, within five years of retirement.",
  "Rule 45(3), CCS (Pension) Rules, 2021", "Confusing the twelve-times residuary test with the gratuity caps")

Q2("PS-022", "VII", "45", "Rule 45(2)", "Death by suicide",
  "The death gratuity table in rule 45(1)(b) applies:",
  "also to the death of a Government servant by suicide",
  ("only to natural deaths", "Rule 45(2) extends the table to suicide expressly."),
  ("only where the family establishes the death was attributable to service",
   "No such condition attaches to the death gratuity table."),
  ("only if the servant had completed one year of qualifying service",
   "The table itself has a band for less than one year."),
  "Rule 45(2) states that the provision of clause (b) of sub-rule (1) shall also be applicable in the case of death of "
  "a Government servant by suicide. The clause is not confined to deaths in the course of duty, and the table it "
  "carries applies from the lowest band of less than one year of qualifying service.",
  "Suicide: the ordinary death gratuity table applies.",
  "Rule 45(2), CCS (Pension) Rules, 2021", "Assuming the table is limited to natural or duty deaths")

Q2("PS-023", "VII", "48", "Rule 48", "Debarring a person from gratuity",
  "A son eligible for a share of gratuity is charged with abetting his father's murder. His claim:",
  "remains suspended until the criminal proceedings conclude",
  ("is forfeited immediately on the charge being framed",
   "Suspension of the claim is the consequence; forfeiture follows conviction."),
  ("is unaffected, because a charge is not a conviction", "Rule 48(1) suspends the claim on the charge itself."),
  ("passes to his own children in the meantime", "The rule does not provide for transmission on a charge."),
  "Rule 48(1) suspends the claim of a person charged with murdering the Government servant, or abetting it, until the "
  "criminal proceedings conclude. Under rule 48(2) conviction debars him and the share passes to the other eligible "
  "members of the family, while acquittal makes the share payable to him. Rule 48(3) applies the same scheme where "
  "the death occurs after retirement, and the Explanation includes abetting a death by suicide.",
  "Charge suspends; conviction debars; acquittal restores.",
  "Rule 48, CCS (Pension) Rules, 2021", "Treating the charge as immediate forfeiture")

Q2("PS-024", "VIII", "50", "Rule 50(13)", "Two family pensions",
  "Both husband and wife are Government servants and both die. Their eligible child draws two family pensions. Where "
  "both pensions are at the ordinary rate under rule 50(2)(a)(i), the combined amount is limited to:",
  "\u20b975,000 per mensem",
  ("\u20b91,25,000 per mensem", "That ceiling applies where either pension is at the enhanced rate."),
  ("\u20b91,00,000 per mensem", "That figure does not appear in rule 50(13)."),
  ("No limit, because two separate pensions are involved",
   "Rule 50(13) caps the sum precisely because two pensions are involved."),
  "Rule 50(13) deals with the case where both spouses were Government servants. If the surviving child is eligible "
  "to draw two pensions at the enhanced rate, or where one enhanced pension later converts to the ordinary rate, the "
  "sum is limited to \u20b91,25,000 a month. Where both pensions are payable at the ordinary rate under "
  "rule 50(2)(a)(i), the sum is limited to \u20b975,000 a month.",
  "Two ordinary-rate family pensions: \u20b975,000 combined.",
  "Rule 50(13), CCS (Pension) Rules, 2021", "Applying the \u20b91,25,000 ceiling to two ordinary-rate pensions")

Q2("PS-025", "VIII", "50", "Rule 50(10)(b)", "Family pension to parents",
  "Where family pension is admissible to the parents, it is payable:",
  "to the mother first, and failing her to the father",
  ("to the father first, and failing him to the mother",
   "Rule 50(10)(b) reverses the usual order and names the mother first."),
  ("to both in equal shares", "The rule provides a sequence, not equal shares."),
  ("to whichever parent the Head of Office considers dependent",
   "Dependence is a precondition; the order between the parents is fixed by the rule."),
  "Rule 50(10)(a) makes family pension payable to the parents for life where no widow, widower or eligible child "
  "survives, if the parents were dependent on the servant immediately before death. Clause (b) then fixes the order: "
  "the mother first, failing which the father. The Explanation deems parents dependent where their combined income "
  "is less than the minimum family pension and the dearness relief admissible on it.",
  "Parents: mother first, then father.",
  "Rule 50(10) and its Explanation, CCS (Pension) Rules, 2021", "Assuming the father takes first")

Q2("PS-026", "VIII", "50", "Rule 50(15)(f)", "Change of family after retirement",
  "A pensioner marries after retirement. He must intimate the change to the Head of Office:",
  "in Form 5, with a copy of the marriage certificate",
  ("in Form 4, with a copy of the marriage certificate",
   "Form 4 is the pre-retirement family particulars form, re-submitted with the pension papers."),
  ("in Format 5, with a copy of the marriage certificate", "Format 5 is the relieving order on absorption."),
  ("by an ordinary letter; no form is prescribed", "Rule 50(15)(f) prescribes Form 5 and the certificate."),
  "Rule 50(15)(a) requires the family particulars in Form 4 on entering service, and clause (e) requires an "
  "up-to-date Form 4 with the pension papers before retirement. Clause (f) then deals with events after retirement: "
  "where the servant marries or remarries, or a child is born, he must intimate the Head of Office in Form 5 with a "
  "copy of the marriage or birth certificate, as the case may be.",
  "Post-retirement change of family: Form 5, with the certificate.",
  "Rule 50(15)(f), CCS (Pension) Rules, 2021", "Answering Form 4 for a post-retirement event")

Q2("PS-027", "VIII", "50", "Rule 50(15)(c)", "Disability certificate",
  "Where a disability manifests in a child or dependent sibling, the fact must be supported by a medical certificate "
  "from:",
  "an authority competent to issue a disability certificate under the RPwD Act, 2016, or a Medical Board",
  ("any registered medical practitioner", "Rule 50(15)(c) names two specific sources."),
  ("the Head of Office's own assessment",
   "The Head of Office receives and records the certificate; he does not issue it."),
  ("the Pension Disbursing Authority", "The disbursing authority has no certifying role under this clause."),
  "Rule 50(15)(c) requires the fact of a disability to be supported by a certificate from either an authority "
  "competent to issue a disability certificate under the Rights of Persons with Disabilities Act, 2016 and the Rules "
  "of 2017, or a Medical Board comprising a Medical Superintendent, Principal, Director or Head of the Institution "
  "or his nominee as Chairman and two other members, at least one of whom is a specialist in the particular area of "
  "disability.",
  "Disability: an RPwD-authorised authority or a Medical Board.",
  "Rule 50(15)(c), CCS (Pension) Rules, 2021", "Accepting any doctor's certificate")

Q2("PS-028", "VIII", "51", "Rule 51(8)(b)", "Missing servant and death gratuity",
  "A Government servant goes missing and a police report is lodged. Death gratuity becomes payable:",
  "when the death is conclusively established, or on expiry of seven years from the police report, whichever is earlier",
  ("only when the death is conclusively established, however long it takes",
   "The seven-year limb exists precisely for the case where death is never established."),
  ("on expiry of six months from the police report",
   "Six months is the waiting period before family pension and gratuity may start, not the trigger."),
  ("on expiry of twelve years from the police report", "The period is seven years."),
  "Rule 51(8)(a) bars payment of family pension, including arrears, and of gratuity before six months from the date of "
  "lodging the police report. Clause (b) then fixes when death gratuity becomes payable: after the death is "
  "conclusively established, or on expiry of seven years from the date of the report, whichever is earlier. Clause "
  "(c) requires any difference between death gratuity and retirement gratuity to be paid within three months of the "
  "claim.",
  "Death gratuity: conclusive proof or seven years, whichever is earlier.",
  "Rule 51(8), CCS (Pension) Rules, 2021", "Applying the six-month wait to the death gratuity trigger")

Q2("PS-029", "VIII", "51", "Rule 51(5)(b)", "Missing servant claim documents",
  "A claim in a missing-person case must be accompanied by:",
  "an indemnity bond in Format 8, with copies of the police report and the untraced report",
  ("an indemnity bond in Format 7, with the same reports",
   "Format 7 is the indemnity bond for a minor's share of gratuity."),
  ("a succession certificate", "A succession certificate belongs to the rule 49 route where there is no family."),
  ("a death certificate from the registering authority",
   "Rule 71(6)(e) expressly says the Head of Office shall not wait for one."),
  "Rule 51(5)(a) requires claims to be submitted after a police report has been lodged as an FIR, daily diary entry or "
  "general diary entry. Clause (b) requires the claim to be accompanied by an Indemnity Bond in Format 8 together "
  "with a copy of that report and a report from the police that the person could not be traced despite all efforts. "
  "Rule 71(6)(e) reinforces the scheme by directing the Head of Office not to wait for a death certificate.",
  "Missing person: Format 8 indemnity bond plus the two police reports.",
  "Rule 51(5) and rule 71(6)(e), CCS (Pension) Rules, 2021", "Answering Format 7, or waiting for a death certificate")

Q2("PS-030", "IX", "52", "Rule 52(4)", "Dearness relief to a family pensioner",
  "A family pensioner takes up employment under a State Government. Dearness relief on the family pension:",
  "continues to be payable during the employment",
  ("is suspended during the employment", "That is the rule for a pensioner, not for a family pensioner."),
  ("is payable only if her pay is at the minimum of the scale",
   "The minimum-of-scale condition belongs to rule 52(2), which rule 52(4) disapplies here."),
  ("is payable only after she retires from that employment", "Rule 52(4) preserves it during the employment."),
  "Rule 52(2) denies dearness relief to a pensioner or compassionate allowance holder who is re-employed or absorbed, "
  "subject to the three-condition proviso in rule 52(2) and the certificate regime in rule 52(3). Rule 52(4) carves "
  "family pensioners out of that denial: a family pensioner employed under the Central or State Government or a "
  "corporation, company, body or bank under them remains eligible to draw dearness relief on family pension during "
  "the employment.",
  "Family pensioner employed: dearness relief continues.",
  "Rule 52(2) to (4), CCS (Pension) Rules, 2021", "Applying the re-employment bar to a family pensioner")
