"""Chapter VII: regulation of pension and gratuity, rules 44 to 49."""
from authoring import Q

# ---------------------------------------------------------------- rule 44
Q("P-0055", 44, "VII", "44(1)",
  "A servant retires on superannuation with 28 years' qualifying service. His emoluments are \u20b972,000 and his average emoluments \u20b974,000. His monthly pension is:",
  ("\u20b937,000",
   "Fifty per cent of the more beneficial figure, which is the average emoluments of \u20b974,000"),
  [("\u20b936,000",
    "That is 50 per cent of last emoluments, which is the lower of the two numbers here"),
   ("\u20b974,000",
    "Pension is a percentage of emoluments, not the emoluments themselves"),
   ("\u20b91,25,000",
    "That is the ceiling, which caps a figure that reaches it")],
  "Rule 44(1) grants a pension calculated at 50 per cent of emoluments or of average emoluments, whichever is "
  "more beneficial to the servant, subject to a floor of \u20b99,000 and a ceiling of \u20b91,25,000 a month. Here 50 "
  "per cent of emoluments is \u20b936,000 and 50 per cent of average emoluments is \u20b937,000, so the pension is "
  "\u20b937,000. The election is not a matter of choice for the servant: the rule directs that the more beneficial "
  "figure be taken, so the calculation must always be done both ways.",
  "Taking the last emoluments because they were the last drawn")

Q("P-0056", 44, "VII", "44(1)",
  "A servant retires with 22 years' qualifying service and emoluments of \u20b92,40,000. His monthly pension is:",
  ("\u20b91,25,000, the ceiling",
   "Fifty per cent would be \u20b91,20,000 here only if the figure were lower; the ceiling is the cap on the uncapped entitlement"),
  [("\u20b91,20,000, being fifty per cent",
    "Fifty per cent of \u20b92,40,000 is \u20b91,20,000, which is below the ceiling and is the correct figure"),
   ("\u20b92,40,000",
    "Pension is a percentage of emoluments, not the emoluments"),
   ("\u20b99,000, the minimum",
    "The minimum applies only where the calculation falls below it")],
  "Rule 44(1) caps pension at \u20b91,25,000 a month. Where 50 per cent of emoluments or of average emoluments "
  "exceeds that figure, the pension is the ceiling; where it falls below, the figure governs. A candidate who "
  "sees a large emolument figure and reaches for the ceiling will be caught when the calculation produces a "
  "number below it, as here: 50 per cent of \u20b92,40,000 is \u20b91,20,000, which is under the cap, so \u20b91,20,000 is "
  "the answer.",
  "Applying the ceiling as though it were the rate")

Q("P-0057", 44, "VII", "44(1)",
  "Pension under rule 44(1) can be sanctioned only to a servant who has completed qualifying service of at least:",
  ("ten years",
   "Rule 44(1) requires ten years for pension"),
  [("five years",
    "Five years is the threshold for retirement gratuity under rule 45(1)(a)"),
   ("fifteen years",
    "No such threshold appears in rule 44"),
   ("twenty years",
    "Twenty years is the qualifying service for voluntary retirement under rule 43")],
  "Rule 44(1) makes a servant eligible for pension on completing a qualifying service of not less than ten "
  "years. Below that threshold rule 44(2) provides a service gratuity instead, calculated at half a month's "
  "emoluments for every completed six-monthly period of service. Three thresholds in these rules are easily "
  "confused and should be kept apart: five years for retirement gratuity under rule 45(1)(a), ten years for "
  "pension under rule 44(1), and twenty years for retirement on completion of twenty years' qualifying service "
  "under rule 43.",
  "Confusing the ten-year pension threshold with the five-year gratuity threshold")

Q("P-0058", 44, "VII", "44(2)",
  "A servant retires under rule 34 with 7 years' qualifying service. He is entitled to:",
  ("service gratuity, at half a month's emoluments per six-monthly period",
   "Rule 44(2) substitutes service gratuity where pension is not earned"),
  [("pension at fifty per cent of emoluments",
    "Pension needs ten years, so seven is short"),
   ("both pension and gratuity",
    "The two are alternatives under sub-rules (1) and (2)"),
   ("nothing, because he did not complete ten years",
    "Service gratuity exists precisely for the short-service case")],
  "Rule 44(2) provides that a servant who retires under one of the rules referred to in sub-rule (1) but has "
  "not become eligible for pension shall be eligible instead for a service gratuity, calculated at half a "
  "month's emoluments for every completed six-monthly period of qualifying service. The two sub-rules are "
  "alternatives, not cumulative: a servant with ten years or more gets pension, and one with less gets service "
  "gratuity. That is why the ten-year line matters so much in practice.",
  "Assuming a short-service retirement produces nothing")

Q("P-0059", 44, "VII", "44(2)",
  "A servant with 7 years and 4 months' qualifying service retires. For service gratuity under rule 44(2), the number of completed six-monthly periods is:",
  ("15 periods",
   "Seven years is 14 periods and the extra four months rounds up to one more under rule 45(4)"),
  [("7 periods",
    "That counts years, not six-monthly periods"),
   ("14 periods",
    "Four months is three months or more, so rule 45(4) adds a period to the 14"),
   ("16 periods",
    "That would need the four months to complete two periods, which it does not")],
  "Rule 44(2) calculates service gratuity at half a month's emoluments for every completed six-monthly period "
  "of qualifying service. Rule 45(4) supplies the rounding rule for gratuity generally: a fraction of a year "
  "equal to three months or more is treated as a completed six-monthly period. Seven years yields 14 periods, "
  "and the remaining four months, being three months or more, yields one more, so the count is 15. The "
  "arithmetic is deliberately tested because a candidate who forgets the rounding loses a half-month of "
  "emoluments.",
  "Forgetting the three-month rounding in sub-rule (4)")

Q("P-0060", 44, "VII", "44(4)(a)",
  "A servant with 18 years' qualifying service is compulsorily retired. His compulsory retirement pension is:",
  ("such portion of the superannuation pension as is sanctioned",
   "Rule 44(4)(a) makes it a proportion of the superannuation pension"),
  [("the full superannuation pension in every case",
    "The rule makes it a portion fixed by the competent authority"),
   ("half the superannuation pension in every case",
    "The rule does not fix the proportion at a half"),
   ("service gratuity, because he was compulsorily retired",
    "Service gratuity applies below ten years; he has eighteen")],
  "Rule 44(4)(a) deals with a servant compulsorily retired after completing qualifying service of not less than "
  "ten years who has become eligible for compulsory retirement pension under rule 40. The amount of that "
  "pension is such portion or percentage of the superannuation pension calculated under sub-rule (1) as the "
  "competent authority may sanction under rule 40. The proportion is therefore a matter for the sanctioning "
  "authority and not a fixed figure, which is why a question asking for 'the' percentage has no single answer "
  "in the rules.",
  "Assuming compulsory retirement carries a fixed fraction of pension")

Q("P-0061", 44, "VII", "44(5)(a)",
  "A servant with 14 years' service is dismissed and sanctioned a compassionate allowance. Its amount is:",
  ("a portion of the pension he would have earned, as rule 41 sanctions",
   "Rule 44(5)(a) measures the allowance against the pension he would have earned"),
  [("the full pension he would have got on superannuation",
    "The rule makes it a portion of that pension, not the whole"),
   ("service gratuity under sub-rule (2)",
    "Sub-rule (5)(b) uses the gratuity measure only below ten years"),
   ("nothing, because dismissal forfeits all benefits",
    "Rule 41 provides the compassionate allowance precisely for this case")],
  "Rule 44(5)(a) provides that where a servant is dismissed or removed after completing qualifying service of "
  "not less than ten years and is sanctioned a compassionate allowance under rule 41, the amount is such "
  "portion or percentage of the pension which would have been admissible had he retired on superannuation as "
  "the competent authority may sanction under rule 41. Rule 24 forfeits the service for ordinary pension "
  "purposes, and rule 41 with rule 44(5) is the mechanism by which a long-serving servant who is dismissed "
  "still receives something.",
  "Reading rule 24's forfeiture as leaving nothing at all")

# ---------------------------------------------------------------- rule 45
Q("P-0062", 45, "VII", "45(1)(a)",
  "A servant retires with 30 years' qualifying service and emoluments of \u20b960,000. His retirement gratuity is:",
  ("capped at 16\u00bd times his emoluments",
   "Sixty half-yearly periods at a quarter each would far exceed the 16\u00bd times cap"),
  [("\u20b94,50,000, being 30 \u00d7 \u00bc \u00d7 emoluments",
    "That is 7\u00bd times emoluments and is below the true figure; the quarter-per-period calculation gives 15 times"),
   ("\u20b93,60,000, being six times emoluments",
    "Six times is a death gratuity rate for one to five years' service"),
   ("thirty times emoluments, being one month per year",
    "The rule uses a quarter per six-monthly period, not a month per year")],
  "Rule 45(1)(a) grants retirement gratuity equal to one-fourth of emoluments for each completed six-monthly "
  "period of qualifying service, subject to a maximum of 16\u00bd times the emoluments. Thirty years is 60 "
  "six-monthly periods, and a quarter of emoluments for each gives 15 times the emoluments, which is under the "
  "cap. A servant with 33 years or more would reach the 16\u00bd times ceiling, because 66 quarters is 16\u00bd. The "
  "cap is expressed as a multiple of emoluments, not as a rupee figure, and that is what makes it durable "
  "across pay revisions.",
  "Applying the maximum without first computing the quarter-per-period figure")

Q("P-0063", 45, "VII", "45(1)(a)",
  "Retirement gratuity under rule 45(1)(a) is available only to a servant who has completed qualifying service of at least:",
  ("five years",
   "Rule 45(1)(a) requires five years and eligibility for service gratuity or pension"),
  [("ten years",
    "Ten years is the pension threshold in rule 44(1)"),
   ("one year",
    "One year is a death gratuity band, not the retirement gratuity threshold"),
   ("twenty years",
    "Twenty years is the voluntary retirement threshold under rule 43")],
  "Rule 45(1)(a) grants retirement gratuity to a servant who has completed five years' qualifying service and "
  "has become eligible for service gratuity or pension under rule 44. The five-year threshold is lower than "
  "the ten years pension requires precisely because gratuity is the benefit that bridges the gap: a servant "
  "with seven years gets service gratuity under rule 44(2) and retirement gratuity under rule 45(1)(a). Rule "
  "45(5) then helps the borderline case, treating four years and nine months or more as five years.",
  "Applying the ten-year pension threshold to gratuity")

Q("P-0064", 45, "VII", "45(1)(b)(iii)",
  "A servant dies in service after 7 years' qualifying service. The death gratuity payable is:",
  ("12 times his emoluments",
   "Seven years falls in the five-to-eleven band, which pays 12 times"),
  [("6 times his emoluments",
    "Six times is the band for one year or more but less than five"),
   ("20 times his emoluments",
    "Twenty times begins at eleven years"),
   ("half his emoluments per six-monthly period",
    "That is the measure for twenty years or more, capped at 33 times")],
  "Rule 45(1)(b) sets death gratuity by bands of qualifying service: less than one year, two times emoluments; "
  "one year or more but less than five, six times; five years or more but less than eleven, twelve times; "
  "eleven years or more but less than twenty, twenty times; and twenty years or more, half of emoluments for "
  "each completed six-monthly period subject to a maximum of 33 times. Seven years sits in the third band, so "
  "the family receives twelve times his emoluments. The bands are stated in years of service, not in months, "
  "and the boundaries are 'or more but less than', so each year belongs to exactly one band.",
  "Using the six-times rate that applies below five years")

Q("P-0065", 45, "VII", "45(1)(b)(v)",
  "A servant with 24 years' qualifying service dies in service. The death gratuity is:",
  ("half of emoluments per six-monthly period, capped at 33 times",
   "Twenty years or more moves the calculation to the per-period measure with its own cap"),
  [("20 times his emoluments, the top band rate",
    "Twenty times is the band below this one, ending at twenty years"),
   ("12 times his emoluments",
    "Twelve times is the five-to-eleven band"),
   ("24 times his emoluments, one for each year",
    "The rule uses a half per six-monthly period, which gives 24 times here and is under the cap")],
  "The final band in rule 45(1)(b) applies where qualifying service is twenty years or more: death gratuity is "
  "half of emoluments for every completed six-monthly period of qualifying service, subject to a maximum of 33 "
  "times emoluments. Twenty-four years is 48 six-monthly periods, and half for each gives 24 times emoluments, "
  "which is under the 33 times cap. A servant with 66 or more six-monthly periods, that is 33 years, would "
  "reach the cap. The switch from a flat multiple to a per-period measure at twenty years is the point most "
  "often missed.",
  "Stopping at the twenty-times band because it looks like the top")

Q("P-0066", 45, "VII", "45(1)(b)",
  "Death gratuity is payable under rule 45(1)(b) where a servant dies in service. The proviso to sub-rule (1) caps retirement and death gratuity together at:",
  ("twenty lakh rupees, as the rule is printed",
   "The proviso to rule 45(1) states twenty lakh rupees"),
  [("twenty-five lakh rupees, as an order of 2024 raised it",
    "An Office Memorandum of 30 May 2024 raised the ceiling to twenty-five lakh from 1 January 2024, but rule 45 still prints twenty lakh"),
   ("thirty-three times emoluments, with no rupee cap",
    "Thirty-three times is the per-period cap in the top band, not the overall ceiling"),
   ("sixteen and a half times emoluments",
    "That is the retirement gratuity cap in clause (a)")],
  "The proviso to rule 45(1) prints a ceiling of twenty lakh rupees on retirement and death gratuity. The "
  "Office Memorandum of 30 May 2024 raised the operative maximum to twenty-five lakh rupees with effect from 1 "
  "January 2024, and its paragraph 7 records that the formal amendment to the Rules will be notified "
  "separately. The rule text has not caught up. A candidate should know both figures and know which is which: "
  "the printed rule says twenty lakh, and the order in force pays twenty-five.",
  "Assuming the printed ceiling is still the operative one")

Q("P-0067", 45, "VII", "45(3)",
  "A pensioner who retired with a pension dies two years later. A residuary gratuity is payable where the sums already received fall short of:",
  ("12 times his emoluments",
   "Rule 45(3) uses 12 times emoluments as the floor for the deficiency calculation"),
  [("six times his emoluments",
    "Six times is the one-to-five-year death gratuity rate, not this floor"),
   ("twenty times his emoluments",
    "Twenty times is a death gratuity band, not the residuary measure"),
   ("the retirement gratuity he received",
    "The retirement gratuity is one of the sums counted towards the floor")],
  "Rule 45(3) provides a residuary gratuity where a servant who became eligible for service gratuity or "
  "pension on retirement dies within five years of that retirement. If the sums actually received by him on "
  "account of gratuity or pension, together with the retirement gratuity admissible under sub-rule (1) and the "
  "commuted value of any commuted portion, are less than twelve times his emoluments, a residuary gratuity "
  "equal to the deficiency may be granted to his family. The purpose is to guarantee a minimum lump sum to the "
  "family of a pensioner who dies soon after retiring.",
  "Assuming the family gets nothing because he had already retired")

Q("P-0068", 45, "VII", "45(4)",
  "In reckoning qualifying service for gratuity, a fraction of a year of three months or more is treated as:",
  ("a completed six-monthly period",
   "Rule 45(4) rounds three months or more up to a full six-monthly period"),
  [("half a six-monthly period",
    "The rule treats it as a whole period, not a half"),
   ("nothing, until a full six months accrues",
    "Three months or more is exactly what the rule rounds up"),
   ("a completed year",
    "The rounding is to a six-monthly period, not a year")],
  "Rule 45(4) supplies the rounding rule for calculating the length of qualifying service under rule 45: a "
  "fraction of a year equal to three months or more is treated as a completed six-monthly period and reckoned "
  "as qualifying service. The rule is generous in the servant's favour and is deliberately so, because the "
  "gratuity is built out of six-monthly periods: a servant at four years and ten months needs the rounding to "
  "cross the five-year threshold in sub-rule (1)(a), which sub-rule (5) separately assists by treating four "
  "years and nine months as five years.",
  "Dropping the part-period instead of rounding it up")

Q("P-0069", 45, "VII", "45(5)",
  "A servant retires with exactly 4 years and 10 months' qualifying service. For the purpose of rule 45 his qualifying service is treated as:",
  ("five years, so he is eligible for gratuity",
   "Rule 45(5) treats four years and nine months or more as five years"),
  [("four years, so he gets nothing",
    "The sub-rule exists to prevent exactly that result"),
   ("four and a half years",
    "The sub-rule rounds up to five years, not to a half"),
   ("ten years, for pension",
    "The deeming is to five years and for gratuity only")],
  "Rule 45(5) provides that a servant who has rendered qualifying service of four years and nine months or "
  "more but less than five years shall have his qualifying service treated as five years for the purpose of "
  "this rule, and shall be eligible for retirement gratuity under clause (a) of sub-rule (1). It is a "
  "narrowly drawn bridge across the five-year threshold, and it operates only for rule 45. It does not make "
  "him eligible for pension under rule 44, which needs ten years, and it does not change his actual service "
  "anywhere else in the rules.",
  "Extending the deeming beyond rule 45")

Q("P-0070", 45, "VII", "45(2)",
  "The death gratuity rates in rule 45(1)(b) apply to a servant who dies by suicide:",
  ("yes, sub-rule (2) extends them expressly to that case",
   "Rule 45(2) applies clause (b) to death by suicide"),
  [("no, because suicide is not death in service",
    "The sub-rule was inserted to put the point beyond doubt"),
   ("only if the family produces a medical certificate",
    "No such condition appears in the sub-rule"),
   ("only where there is no criminal proceeding pending",
    "The sub-rule attaches no such condition")],
  "Rule 45(2) provides that clause (b) of sub-rule (1), the death gratuity table, shall also be applicable in "
  "the case of death of a Government servant by suicide. The sub-rule exists because it might otherwise have "
  "been argued that a death by suicide is not a death in service for the purpose of the table, which would "
  "have deprived the family of the gratuity in the very circumstances where it is most needed. It is a short "
  "provision and worth remembering as an example of the rules reaching a result that a literal reading might "
  "not.",
  "Reading 'dies while in service' as excluding suicide")

Q("P-0071", 45, "VII", "45(6)-prov-2",
  "For the purpose of gratuity under rule 45, dearness allowance admissible on the date of retirement or death:",
  ("is also treated as emoluments",
   "The second proviso to rule 45(6) includes DA in emoluments for gratuity"),
  [("is excluded from emoluments",
    "The proviso includes it, which is the point of the provision"),
   ("is included only for death gratuity",
    "The proviso covers retirement and death alike"),
   ("is included only if the servant had opted for it",
    "No option is required by the proviso")],
  "Rule 45(6) requires emoluments for gratuity to be reckoned in accordance with rule 31. Two provisos then "
  "modify that: if the servant's emoluments were reduced during the last ten months of service, average "
  "emoluments under rule 32 are treated as emoluments, and dearness allowance admissible on the date of "
  "retirement or death is also treated as emoluments for the purpose of this rule. The second proviso matters "
  "because it brings DA into the gratuity base, which the definition in rule 31 does not do of its own force.",
  "Leaving dearness allowance out of the gratuity base")

Q("P-0072", 45, "VII", "45(1)-prov-2",
  "The gratuity finally calculated under rule 45 comes to \u20b94,23,456.40. The amount payable is:",
  ("\u20b94,23,457, rounded up to the next higher rupee",
   "The second proviso to rule 45(1) rounds a fraction of a rupee up"),
  [("\u20b94,23,456, rounded down",
    "The proviso rounds up, not down"),
   ("\u20b94,23,456.40, paid to the paise",
    "Gratuity is rounded to the rupee"),
   ("\u20b94,23,500, rounded to the nearest hundred",
    "The rounding is to the rupee, not to hundreds")],
  "The second proviso to rule 45(1) provides that where the amount of retirement or death gratuity, as "
  "finally calculated, contains a fraction of a rupee, it shall be rounded off to the next higher rupee. The "
  "direction is upward in every case, so a fraction however small increases the payment by one rupee. That is "
  "worth contrasting with rule 44, which says nothing about rounding pension, and with the pay rules, which "
  "round differently again.",
  "Rounding down, or to the nearest rupee rather than up")
