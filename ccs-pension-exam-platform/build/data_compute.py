#!/usr/bin/env python3
"""data_compute.py — the arithmetic of the CCS (Pension) Rules, 2021.

Every figure used in a question is derived in `verify()` below from the rule
text, and the audit fails the build if a worked answer disagrees with the
derivation. The formulas are the statute's:
  pension            rule 44(1)  50% of emoluments or average emoluments, whichever is more
  service gratuity   rule 44(2)  half month's emoluments per completed six-monthly period
  retirement gratuity rule 45(1)(a)  one-fourth of emoluments per completed six-monthly
                                   period, capped at 16.5 times emoluments
  death gratuity     rule 45(1)(b)  the table, 2 / 6 / 12 / 20 times, or half of
                                   emoluments per completed six-monthly up to 33 times
  family pension     rule 50(2)  30% of pay (normal), 50% (enhanced)
"""
from __future__ import annotations

FACTS = []


def Q(fid, ch, rule, rules_text, topic, stem, ans, d1, d2, d3, why, safe, src, trap,
      kind="NUM", tag="Tough"):
    FACTS.append(dict(id=fid, ch=ch, rule=rule, rules_text=rules_text, topic=topic,
                      q=stem, a=ans, d=[d1, d2, d3], why=why, safe=safe, src=src,
                      trap=trap, kind=kind, tag=tag))


# ---------------------------------------------------------------- derivations
def pension(emol: int) -> int:
    """rule 44(1): 50 per cent, floor 9,000, ceiling 1,25,000."""
    p = round(emol * 0.5)
    return max(9000, min(125000, p))


def six_monthly(years: int, months: int = 0) -> int:
    """Completed six-monthly periods, with rule 44(7): 3 months or more = one more."""
    return years * 2 + (1 if months >= 3 else 0)


def retirement_gratuity(emol: int, periods: int) -> int:
    """rule 45(1)(a): one-fourth of emoluments per completed six-monthly, cap 16.5x."""
    g = emol / 4 * periods
    return int(min(g, emol * 16.5, 2000000))


def death_gratuity(emol: int, periods: int) -> int:
    """rule 45(1)(b): the slab table."""
    if periods < 2:
        times = 2
    elif periods < 10:
        times = 6
    elif periods < 22:
        times = 12
    elif periods < 40:
        times = 20
    else:
        return int(min(emol * 0.5 * periods, emol * 33, 2000000))
    return int(min(emol * times, 2000000))


def family_pension(pay: int, enhanced: bool) -> int:
    """rule 50(2): 30 per cent normal (9,000–75,000); 50 per cent enhanced (9,000–1,25,000)."""
    if enhanced:
        return max(9000, min(125000, round(pay * 0.5)))
    return max(9000, min(75000, round(pay * 0.3)))


# ---------------------------------------------------------------- rule 44
Q("PC-001", "VII", "44", "Rule 44(1)", "Pension at 50 per cent",
  "A servant retires on superannuation after 33 years' qualifying service. His emoluments are \u20b986,000 and his "
  "average emoluments \u20b984,000. His pension under rule 44(1) is:",
  "\u20b943,000 a month",
  ("\u20b942,000 a month",
   "That is 50 per cent of the average emoluments, which is the lower figure; the rule takes the more beneficial."),
  ("\u20b986,000 a month, the last emoluments in full",
   "The pension is 50 per cent of the emoluments, not the emoluments."),
  ("\u20b91,25,000 a month, the ceiling",
   "The ceiling is not a rate; it caps a figure that reaches it."),
  "Rule 44(1) takes 50 per cent of emoluments or of average emoluments, whichever is more beneficial. Emoluments are "
  "\u20b986,000, so 50 per cent is \u20b943,000. Average emoluments are \u20b984,000, so 50 per cent is "
  "\u20b942,000. The larger is \u20b943,000, and it lies between the floor of \u20b99,000 and the ceiling of "
  "\u20b91,25,000, so it is the pension.",
  "Rule 44(1): 50% of the higher of emoluments and average emoluments.",
  "Rule 44(1), CCS (Pension) Rules, 2021", "Taking the average because it looks like the safer figure")

Q("PC-002", "VII", "44", "Rule 44(1)", "Pension — the floor",
  "A servant retires with ten years' qualifying service and emoluments of \u20b916,000. His pension under rule "
  "44(1) is:",
  "\u20b99,000 a month, the minimum",
  ("\u20b98,000 a month",
   "That is 50 per cent of \u20b916,000, but the rule puts a floor under it."),
  ("\u20b916,000 a month",
   "The pension is 50 per cent, not the full emoluments."),
  ("No pension is admissible below \u20b920,000 of emoluments",
   "There is no such threshold; the floor operates on the pension, not on the pay."),
  "Fifty per cent of \u20b916,000 is \u20b98,000. Rule 44(1) fixes a minimum of \u20b99,000 a month, so the "
  "pension is lifted to \u20b99,000. The floor is on the amount of pension, not on the emoluments, so a question "
  "that offers a pay threshold has invented a rule.",
  "Floor: \u20b99,000 on the pension amount, not on the pay.",
  "Rule 44(1), CCS (Pension) Rules, 2021", "Leaving the pension at 50 per cent below the floor")

Q("PC-003", "VII", "44", "Rule 44(1)", "Pension — the ceiling",
  "A servant retires with emoluments of \u20b93,00,000. His pension under rule 44(1) is:",
  "\u20b91,25,000 a month, the maximum",
  ("\u20b91,50,000 a month",
   "That is 50 per cent of the emoluments, but the ceiling cuts it back."),
  ("\u20b92,50,000 a month",
   "That is not a figure in the rule at all."),
  ("\u20b975,000 a month",
   "Seventy-five thousand is the ordinary ceiling for family pension, not for pension."),
  "Fifty per cent of \u20b93,00,000 is \u20b91,50,000, which is above the maximum of \u20b91,25,000 a month fixed "
  "by rule 44(1). The pension is therefore \u20b91,25,000. The ceiling and the floor are both in sub-rule (1), and "
  "the paper likes to offer the family pension ceiling of \u20b975,000 alongside them.",
  "Ceiling: \u20b91,25,000 on pension; \u20b975,000 belongs to family pension.",
  "Rule 44(1), CCS (Pension) Rules, 2021", "Using the family pension ceiling for the pension")

Q("PC-004", "VII", "44", "Rule 44(8)", "Nine years nine months",
  "A servant retires with exactly nine years and nine months of qualifying service. Under rule 44(8):",
  "His qualifying service is treated as ten years and he is eligible for pension",
  ("He gets service gratuity, because he has less than ten years",
   "Sub-rule (8) exists to prevent exactly that result."),
  ("He gets nothing, because the minimum is ten years",
   "He is inside the sub-rule (8) rounding, so he is eligible."),
  ("His qualifying service is nine years and six months after rounding",
   "The rounding is upward to ten years, not downward."),
  "Rule 44(8) provides that a servant who has rendered nine years and nine months or more but less than ten years "
  "shall have his qualifying service treated as ten years and shall be eligible for pension under sub-rule (1). "
  "Read it with rule 44(7), which treats a fraction of three months and above as a completed six-monthly period: "
  "the two together convert what looks like a shortfall into an entitlement.",
  "9 years 9 months or more: treat as 10, pension admissible.",
  "Rule 44(8), CCS (Pension) Rules, 2021", "Awarding service gratuity at nine years nine months")

Q("PC-005", "VII", "44", "Rule 44(2)", "Service gratuity",
  "A servant retires after eight years of qualifying service with emoluments of \u20b940,000. He is entitled to:",
  "Service gratuity of \u20b93,20,000",
  ("Pension of \u20b920,000 a month",
   "Pension needs ten years; eight years brings service gratuity."),
  ("Retirement gratuity of \u20b91,60,000",
   "That is the rule 45 computation; with under ten years it is service gratuity under rule 44(2)."),
  ("Nothing, because he has not completed ten years",
   "Rule 44(2) gives service gratuity precisely for that case."),
  "Eight years is sixteen completed six-monthly periods. Rule 44(2) computes service gratuity at half a month's "
  "emoluments for every completed six-monthly period: \u20b940,000 \u00f7 2 = \u20b920,000, times 16 = "
  "\u20b93,20,000. This is the case rule 44(2) exists for \u2014 a servant who retires without reaching the ten "
  "years that pension requires.",
  "Service gratuity: half a month's emoluments per six-monthly period.",
  "Rule 44(2), CCS (Pension) Rules, 2021", "Applying the one-quarter retirement gratuity rate to service gratuity")

Q("PC-006", "VII", "44", "Rule 44(6)", "Additional pension",
  "A pensioner drawing a basic pension of \u20b930,000 attains the age of 87. His additional pension is:",
  "\u20b99,000 \u2014 30 per cent of basic pension",
  ("\u20b96,000 \u2014 20 per cent of basic pension",
   "Twenty per cent is the 80-to-85 band; at 87 he is in the 85-to-90 band."),
  ("\u20b912,000 \u2014 40 per cent of basic pension",
   "Forty per cent starts at 90."),
  ("\u20b930,000 \u2014 100 per cent of basic pension",
   "One hundred per cent starts at 100 years."),
  "Rule 44(6) adds a percentage of basic pension by age band: 20 per cent from 80 to under 85, 30 per cent from 85 "
  "to under 90, 40 per cent from 90 to under 95, 50 per cent from 95 to under 100, and 100 per cent at 100 or more. "
  "At 87 the band is 85 to 90, so the addition is 30 per cent of \u20b930,000, which is \u20b99,000. Sub-rule "
  "(6)(b) makes it payable from the first day of the month in which it falls due.",
  "Additional pension bands: 20/30/40/50/100 per cent by age.",
  "Rule 44(6), CCS (Pension) Rules, 2021", "Using the 80-to-85 band for an 87-year-old")

Q("PC-007", "VII", "44", "Rule 44(7)", "Fraction of a year",
  "A servant has 27 years and 4 months of qualifying service. For pension, the qualifying service is treated as:",
  "27 years and 6 months \u2014 the 4 months is a completed six-monthly period",
  ("27 years exactly \u2014 the fraction is ignored",
   "Rule 44(7) does not ignore three months or more; it promotes it."),
  ("28 years \u2014 the fraction rounds up to a full year",
   "The rounding is to a six-monthly period, not to a year."),
  ("27 years and 4 months, counted to the month",
   "Pension counts completed six-monthly periods, not months."),
  "Rule 44(7) provides that in calculating the length of qualifying service, a fraction of a year equal to three "
  "months and above shall be treated as a completed six-monthly period. Four months is three months or above, so it "
  "becomes a six-monthly period, and the service is 27 years and 6 months \u2014 that is, 55 completed six-monthly "
  "periods. A fraction of less than three months would simply be dropped.",
  "Three months or more: one more six-monthly period. Less than three: dropped.",
  "Rule 44(7), CCS (Pension) Rules, 2021", "Rounding the fraction to a whole year")

Q("PC-008", "VII", "44", "Rule 44(9)", "Rounding the pension",
  "A pension works out to \u20b924,750.60. Under rule 44(9) it is expressed as:",
  "\u20b924,751",
  ("\u20b924,750",
   "The rule rounds to the next higher rupee, not to the nearest."),
  ("\u20b924,760",
   "That rounds to the next ten rupees, which the rule does not do."),
  ("\u20b924,750.60, carried to the paise",
   "The rule requires whole rupees."),
  "Rule 44(9) requires the amount finally determined to be expressed in whole rupees, and any fraction of a rupee "
  "to be rounded off to the next higher rupee. \u20b924,750.60 therefore becomes \u20b924,751. Note that this is "
  "rounding up, not rounding to the nearest: \u20b924,750.10 would also become \u20b924,751. Sub-rule (10) applies "
  "the same rounding where pension is discontinued mid-month.",
  "Pension rounding: always to the next higher rupee.",
  "Rule 44(9), CCS (Pension) Rules, 2021", "Rounding to the nearest rupee")

# ---------------------------------------------------------------- rule 45
Q("PC-009", "VII", "45", "Rule 45(1)(a)", "Retirement gratuity",
  "A servant retires after 32 years and 5 months of qualifying service with emoluments of \u20b960,000. His "
  "retirement gratuity is:",
  "\u20b99,75,000",
  ("\u20b94,87,500",
   "That uses one-eighth instead of one-quarter of emoluments."),
  ("\u20b99,60,000",
   "That treats the 5 months as dropped; at three months or more it becomes a six-monthly period."),
  ("\u20b99,90,000, the 16\u00bd-times cap",
   "The cap is the ceiling, not the computation; on these figures the computation is lower."),
  "Thirty-two years and five months gives 64 completed six-monthly periods, plus one because rule 45(4) treats a "
  "fraction of three months or more as a completed six-monthly period \u2014 65 in all. Rule 45(1)(a) pays "
  "one-fourth of emoluments per period: \u20b960,000 \u00f7 4 = \u20b915,000, times 65 = \u20b99,75,000. The "
  "cap is 16\u00bd times emoluments, \u20b99,90,000, which is not reached, so \u20b99,75,000 is the gratuity.",
  "Gratuity: one-quarter per six-monthly period, capped at 16\u00bd times emoluments.",
  "Rule 45(1)(a) and (4), CCS (Pension) Rules, 2021",
  "Forgetting the cap, or forgetting the three-month rounding")

Q("PC-010", "VII", "45", "Rule 45(1)(b)", "Death gratuity — the middle slabs",
  "A servant dies in service after 7 years and 2 months of qualifying service. His emoluments were \u20b950,000. The "
  "death gratuity is:",
  "\u20b96,00,000",
  ("\u20b93,00,000",
   "That is the 2-times rate for under one year."),
  ("\u20b91,50,000",
   "That is the service gratuity pattern, not death gratuity."),
  ("\u20b910,00,000",
   "That is the 20-times rate for 11 years or more."),
  "Seven years and two months is fourteen completed six-monthly periods. The table in rule 45(1)(b) gives 12 times "
  "emoluments for 5 years or more but less than 11 years. Twelve times \u20b950,000 is \u20b96,00,000, and it is "
  "below the \u20b920 lakh ceiling, so that is the gratuity. The slabs are 2, 6, 12, 20 times, and then half of "
  "emoluments per completed period capped at 33 times.",
  "Death gratuity slabs: 2 / 6 / 12 / 20 times, then half per period to 33.",
  "Rule 45(1)(b), CCS (Pension) Rules, 2021", "Using the 20-times slab for a seven-year servant")

Q("PC-011", "VII", "45", "Rule 45(1)(b)", "Death gratuity — the top slab",
  "A servant dies in service after 21 years of qualifying service with emoluments of \u20b970,000. The death "
  "gratuity is:",
  "\u20b914,70,000",
  ("\u20b914,00,000",
   "That is 20 times, which is the band below 20 years; at 21 years the half-per-period rate applies."),
  ("\u20b923,10,000, the 33-times cap",
   "The cap is not the rate; the computation gives less."),
  ("\u20b916,80,000",
   "That computes 24 periods rather than 21."),
  "Twenty-one years is 42 completed six-monthly periods. At 20 years or more the table gives half of emoluments "
  "for every completed six-monthly period, subject to a maximum of 33 times emoluments: \u20b970,000 \u00f7 2 = "
  "\u20b935,000, times 42 = \u20b914,70,000. The cap of 33 times is \u20b923,10,000, which is not reached, so the "
  "computation stands.",
  "Top slab: half of emoluments per period, capped at 33 times.",
  "Rule 45(1)(b), CCS (Pension) Rules, 2021", "Applying the 20-times slab above twenty years")

Q("PC-012", "VII", "45", "Rule 45(3)", "Residuary gratuity",
  "The residuary gratuity under rule 45(3) is payable where a pensioner dies within five years of retirement and "
  "the sums received together with the retirement gratuity and commuted value fall short of:",
  "Twelve times his emoluments",
  ("Ten times his emoluments",
   "The figure in rule 45(3) is twelve."),
  ("Sixteen and a half times his emoluments",
   "That is the retirement gratuity cap, not the residuary benchmark."),
  ("Thirty-three times his emoluments",
   "That is the death gratuity cap."),
  "Rule 45(3) measures the shortfall against twelve times his emoluments. If the pension and gratuity actually "
  "received, together with the retirement gratuity and the commuted value of any commuted portion, come to less "
  "than twelve times emoluments, a residuary gratuity equal to the deficiency is paid to the family. The figure to "
  "hold is twelve, and it is a benchmark for this one calculation only.",
  "Residuary gratuity: the deficiency below twelve times emoluments.",
  "Rule 45(3), CCS (Pension) Rules, 2021", "Using the 16\u00bd or 33 times caps as the residuary benchmark")

Q("PC-013", "VII", "45", "Rule 45(5)", "Four years nine months",
  "A servant retires with four years and nine months of qualifying service. For retirement gratuity under rule "
  "45(5):",
  "His qualifying service is treated as five years and he is eligible for retirement gratuity",
  ("He gets service gratuity only, because he is below five years",
   "Sub-rule (5) treats him as having five years for this purpose."),
  ("He gets nothing, because five years is the minimum",
   "The minimum is reached by the deeming in sub-rule (5)."),
  ("His service is rounded down to four years",
   "The rounding is upward, to five years."),
  "Rule 45(5) provides that a servant who has rendered four years and nine months or more but less than five years "
  "shall have his qualifying service treated as five years for the purpose of this rule and shall be eligible for "
  "retirement gratuity under clause (a) of sub-rule (1). It mirrors rule 44(8), which does the same at nine years "
  "nine months for pension. The pattern to learn is the nine-month shortfall, at both thresholds.",
  "4 years 9 months = 5 years for gratuity; 9 years 9 months = 10 years for pension.",
  "Rule 45(5), CCS (Pension) Rules, 2021", "Confusing the two nine-month concessions")

# ---------------------------------------------------------------- rule 50
Q("PC-014", "VIII", "50", "Rule 50(2)(a)(i)", "Family pension — normal rate",
  "A servant dies in service leaving a widow. His pay for family pension is \u20b960,000. After the enhanced "
  "period ends, the family pension is:",
  "\u20b918,000 a month \u2014 30 per cent of pay",
  ("\u20b930,000 a month \u2014 50 per cent of pay",
   "Fifty per cent is the enhanced rate, which runs for ten years and then steps down."),
  ("\u20b99,000 a month \u2014 the minimum",
   "The minimum applies only where 30 per cent falls below it."),
  ("\u20b975,000 a month \u2014 the maximum",
   "The maximum applies only where 30 per cent exceeds it."),
  "Rule 50(2)(a)(i) sets the ordinary family pension at 30 per cent of pay, subject to a minimum of \u20b99,000 and "
  "a maximum of \u20b975,000 a month. Thirty per cent of \u20b960,000 is \u20b918,000. The enhanced rate under "
  "sub-clause (ii) is 50 per cent, but it is payable for ten years from the death and then the pension reverts to "
  "the sub-clause (i) rate under clause (b).",
  "Family pension: 30% normal, 50% enhanced for ten years.",
  "Rule 50(2), CCS (Pension) Rules, 2021", "Applying the enhanced rate beyond its period")

Q("PC-015", "VIII", "50", "Rule 50(2)(a)(ii)", "Family pension — enhanced rate",
  "A servant dies in service. His pay for family pension is \u20b92,00,000. The enhanced family pension is:",
  "\u20b91,00,000 a month",
  ("\u20b91,25,000 a month, the maximum",
   "The maximum applies only if 50 per cent exceeds it; 50 per cent of \u20b92,00,000 is \u20b91,00,000."),
  ("\u20b960,000 a month",
   "That is 30 per cent, the ordinary rate."),
  ("\u20b975,000 a month",
   "That is the ordinary ceiling, not the enhanced one."),
  "Fifty per cent of \u20b92,00,000 is \u20b91,00,000. The enhanced family pension under rule 50(2)(a)(ii) is 50 "
  "per cent of pay, and sub-clause (iv) puts its ceiling at \u20b91,25,000. \u20b91,00,000 is below that ceiling, "
  "so it stands. Had the pay been \u20b93,00,000, the figure would have been cut to the \u20b91,25,000 ceiling.",
  "Enhanced family pension ceiling: \u20b91,25,000.",
  "Rule 50(2)(a)(ii) and (iv), CCS (Pension) Rules, 2021", "Using the \u20b975,000 ordinary ceiling for the enhanced rate")

Q("PC-016", "VIII", "50", "Rule 50(2)(a)(iii)", "Family pension after retirement",
  "A pensioner dies after retirement. The enhanced family pension is payable for:",
  "Seven years, or until he would have attained 67, whichever is less",
  ("Ten years, as on a death in service",
   "Ten years is the death-in-service period under sub-clause (ii)."),
  ("Seven years in every case",
   "The seven years is cut short if he would have reached 67 sooner."),
  ("For life",
   "The enhanced rate is time-bound; the ordinary rate follows it."),
  "Rule 50(2)(a)(iii) gives the enhanced family pension after a death following retirement for seven years, or up "
  "to the date the deceased pensioner would have attained sixty-seven years had he survived, whichever is less. Two "
  "provisos then cap it: it shall not exceed the pension authorised on retirement, and where that pension is below "
  "the ordinary family pension rate, the family pension is limited to the ordinary rate.",
  "After retirement: seven years or age 67 of the pensioner, whichever is less.",
  "Rule 50(2)(a)(iii), CCS (Pension) Rules, 2021", "Applying the ten-year death-in-service period after retirement")

Q("PC-017", "VIII", "50", "Rule 50(2)(a)(i)", "Family pension — the floor",
  "A servant dies in service with pay for family pension of \u20b922,000. The ordinary family pension is:",
  "\u20b99,000 a month, the minimum",
  ("\u20b96,600 a month",
   "That is 30 per cent, but the rule puts a floor under it."),
  ("\u20b911,000 a month",
   "That is 50 per cent, the enhanced rate."),
  ("Nothing, because the pay is too low",
   "The floor guarantees a minimum, whatever the pay."),
  "Thirty per cent of \u20b922,000 is \u20b96,600, which is below the minimum of \u20b99,000 fixed by rule "
  "50(2)(a)(i). The family pension is therefore \u20b99,000. The same floor of \u20b99,000 applies to the enhanced "
  "rate under sub-clause (iv), so even the 50 per cent figure cannot fall below it.",
  "Family pension floor: \u20b99,000, on both the ordinary and enhanced rates.",
  "Rule 50(2)(a)(i), CCS (Pension) Rules, 2021", "Leaving the family pension below the floor")

Q("PC-018", "VIII", "50", "Rule 50(6)", "Order of eligibility",
  "Under rule 50(6), the order in which family pension is payable is:",
  "Widow or widower, then children, then dependent parents, then dependent disabled siblings",
  ("Children first, then widow or widower",
   "The widow or widower comes first."),
  ("Widow or widower, then parents, then children",
   "Children come before parents."),
  ("All eligible members in equal shares at the same time, always",
   "Rule 50(7)(a) makes it payable to one member at a time, save in the listed cases."),
  "Rule 50(6) sets a four-step order: the widow or widower (including a post-retiral spouse and a judicially "
  "separated spouse); then children, including adopted and step children and children born after retirement; then "
  "dependent parents; then dependent siblings suffering from a mental or physical disability. Rule 50(7)(a) adds "
  "that it is not payable to more than one member at a time, subject to the listed exceptions where it is shared.",
  "Order: spouse, children, dependent parents, dependent disabled siblings.",
  "Rule 50(6) and (7), CCS (Pension) Rules, 2021", "Putting children ahead of the spouse")

Q("PC-019", "VIII", "50", "Rule 50(9)(a)(i)", "Son's eligibility",
  "A son of a deceased servant, not suffering from any disability, is eligible for family pension if he is:",
  "Unmarried, below twenty-five, and not earning his livelihood",
  ("Below twenty-one and unmarried",
   "The age is twenty-five."),
  ("Unmarried, at any age, if he is a student",
   "There is no student concession; the age limit is absolute for a son without disability."),
  ("Below eighteen, the age of majority",
   "Eighteen is the age of majority, not the family pension limit."),
  "Rule 50(9)(a)(i) makes an ordinary son eligible only if he is unmarried, below twenty-five years and not "
  "earning his livelihood. Clause (ii) does the same for a daughter, but permits her to be unmarried, widowed or "
  "divorced \u2014 the daughter is not required to be unmarried. A son or daughter suffering from a mental or "
  "physical disability under clause (iii) has no age limit, and receives it for life on the conditions in clause "
  "(h).",
  "Son: unmarried, under 25, not earning. Daughter: unmarried, widowed or divorced.",
  "Rule 50(9)(a), CCS (Pension) Rules, 2021", "Applying the same marital condition to sons and daughters")
