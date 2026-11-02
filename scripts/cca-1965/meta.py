# -*- coding: utf-8 -*-
"""Front matter, scope register, clocks, authorities, case law and sources
for the CCS (CCA) Rules, 1965 case-study book.

Law date: 01.11.2026. Only in-force text is taught; superseded provisions are
listed in the obsolete register and appear in cases only as a distinguishing
wrong answer (glyph ⊘).
"""

TITLE = "CCS (CCA) Rules, 1965"
SUBTITLE = "Case Studies at Three Levels — Non-Obsolete Content"
VERSION = "v1.0"
LAW_DATE = "01.11.2026"
BUILD_STAMP = "2026-11-02"

PITCH = ("L1 concept checks · L2 standard cases · L3 integrated exam cases<br/>"
         "In-force text as on <b>01.11.2026</b> · pitched at the Assistant Audit / Accounts Officer "
         "(AAO) level, with CAG / IA&amp;AD annotations")

COVERAGE = [
    ("Coverage",
     "CCS (Classification, Control and Appeal) Rules, 1965, Parts I–IX (rules 1–35) as amended up to "
     "01.11.2026 — the 2009 amendment substituting rule 11(vi), the 2014 Second Amendment (31.10.2014) "
     "recasting rule 15 and removing the second show-cause on the proposed penalty, the 2014 Third "
     "Amendment (19.11.2014) on complaints-committee compensation, and the 2017 statutory timelines "
     "(G.S.R. 548(E), 02.06.2017). Operative instructions are cited with number and date."),
    ("Format",
     "Facts → record worksheet → questions; solutions in Issue → Rule → Conditions → Application → "
     "Calculation → Conclusion, with marks per step, a decision path, common wrong answers and — for L3 — "
     "a model answer in exam register."),
    ("Non-obsolete filter",
     "Every provision was classified <b>IN</b>, <b>IN (concept only)</b>, <b>OUT (omitted)</b>, "
     "<b>OUT (transitional)</b>, <b>OUT (no case value)</b> or <b>OUT (superseded)</b> before drafting. Superseded provisions are <b>not taught</b>: they appear in "
     "the obsolete register and, where a reader is likely to meet them, as a wrong answer marked ⊘ with the "
     "amending instrument named."),
    ("Checks",
     "Every deadline, period, suspension review date, mark total and rupee figure is recomputed by script "
     "from the facts (`scripts/cca-1965/verify.py`); every proposition is traced to the current text in the "
     "citation table. The build refuses to write on a failed audit."),
    ("Beyond the rules",
     "Two subjects sit beside the text and are examined here because they decide real files: common proceedings under r.18, and the "
     "sealed cover, which is <b>not in the CCA Rules at all</b> but in DoPT OM No. 22011/4/91-Estt.(A) dated 14.09.1992, read with "
     "<i>Jankiraman</i>. The OM is executive instruction: it binds the executive, it does not override the rules, and every case that "
     "uses it says so. Its three categories, its six-monthly review and its two-year point are treated as clocks, with the OM paragraph "
     "cited each time."),
    ("Flags",
     "<b>⚑</b> a rate or order still awaited · <b>⚠</b> a genuinely unsettled point · <b>⊘</b> a superseded "
     "provision, shown only to be distinguished. No flag is decorative: each names what would settle it."),
]

LEGEND = [
    ("L1", "Concept checks",
     "One-line recall with the trap. Cover the answer column and test yourself in 2 minutes."),
    ("L2", "Standard cases",
     "3–5 issues each, worked step by step with marks. Attempt on paper, then open the solution."),
    ("L3", "Integrated exam cases",
     "Full file → competence → procedure → penalty → money → appeal → model answer."),
]

METHOD = [
    ("Issue", "Which stage of the disciplinary process, and what is being decided — competence, procedure, penalty, money or appeal?"),
    ("Rule", "Quote the sub-rule and its test. “Rule 14” is not a citation for a fifteen-day limit."),
    ("Conditions", "Check each limb of the sub-rule: who, on what ground, within what time, with what record."),
    ("Application", "Apply the facts, one limb per line. Name the date or the signature that decides it."),
    ("Calculation", "Dates, working days, periods, pay and money — formula first, then the figure."),
    ("Conclusion", "One line: what survives, what falls, what must be redone, and the trap."),
]

NUMBERS = [
    ("Penalties", "Minor: censure · withholding of promotion · recovery · one-stage reduction ≤ 3 years (non-cumulative, pension-neutral) · withholding of increments. "
                  "Major: reduction to a lower stage · reduction to a lower time-scale · compulsory retirement · removal · dismissal."),
    ("Major-penalty clocks (r.14)", "Defence 15 days, extensions of 15 days at a time, <b>cap 45 days</b> · appearance within <b>10 working days</b> (+10) · "
                                    "adjournment ≤ 30 days · inspection 5 days (+5) · documents 1 month · witness statements 3 days before examination · "
                                    "inquiry report <b>6 months</b> (+6 months at a time)."),
    ("Report and advice", "Representation on the inquiry report <b>15 days</b> · representation on the Commission’s advice <b>15 days</b> · "
                          "no second show-cause on the proposed penalty for a major penalty."),
    ("Suspension", "Review before <b>90 days</b> · extension ≤ <b>180 days</b> at a time · no validity beyond 90 days without extension · "
                   "deemed suspension for detention or imprisonment exceeding <b>48 hours</b>."),
    ("Subsistence", "FR 53: <b>50%</b> of pay + DA for the first 90 days, <b>75%</b> thereafter, less deductions ordered."),
    ("Appeal and revision", "Appeal <b>45 days</b> from delivery · revision by the appellate authority within <b>6 months</b> · "
                            "revision by the President / CAG / Head of Department at any time · review by the President only, on new material."),
]

CLOCKS = [
    ("Charge sheet to defence", "15 days, extendable 15 days at a time; overall 45 days from receipt", "r.14(4)", ["L2-01", "L3-01"]),
    ("Appearance before the inquiry authority", "10 working days from receipt of the charge sheet (+10 days)", "r.14(7)", ["L2-02", "L2-07"]),
    ("Adjournment at the Presenting Officer’s request", "3 clear days", "r.14(15)", ["L2-05"]),
    ("Inspection of listed documents", "5 days (+5)", "r.14(11)(i)", ["L2-04"]),
    ("Production of other documents", "1 month, or a non-availability certificate", "r.14(13)", ["L2-04"]),
    ("Copies of witness statements", "not later than 3 days before that witness is examined", "Note to r.14(11)", ["L2-05"]),
    ("Completion of the inquiry", "6 months from appointment of the inquiry authority (+6 months at a time)", "r.14(24)", ["L2-06", "L3-13"]),
    ("Representation on the inquiry report", "15 days", "r.15(2)", ["L2-08", "L3-01", "L3-18"]),
    ("Representation on the Commission’s advice", "15 days", "r.15(3)(b), r.16(1)(d)", ["L2-10"]),
    ("Suspension review", "before 90 days; extension ≤ 180 days at a time", "r.10(6)–(7)", ["L2-25", "L2-28", "L2-29", "L3-02", "L3-09"]),
    ("Appeal", "45 days from delivery of the order", "r.25", ["L2-35", "L2-36", "L2-44", "L3-16"]),
    ("Revision by the appellate authority", "6 months from the order; the CAG and the President have no such bar", "r.29(1)(v)", ["L2-41", "L2-42", "L2-43", "L3-16"]),
    ("Review", "at any time, President only, on new material", "r.29-A", ["L2-42", "L2-43", "L3-16"]),
    ("Sealed cover — decision of the DPC", "tested on the date the DPC meets, on the three closed categories only", "DoPT OM 14.09.1992, para 2", ["L2-30", "L3-07", "L3-19", "L3-20", "L3-21"]),
    ("Sealed cover — review", "first review at 6 months from the first DPC; every 6 months after", "DoPT OM 14.09.1992, para 4", ["L3-19", "L3-20"]),
    ("Sealed cover — ad hoc promotion", "may be considered only after 2 years from the first DPC", "DoPT OM 14.09.1992, para 5", ["L3-20"]),
    ("Sealed cover — opening", "on conclusion of the proceeding; exoneration relates the promotion back to the panel date", "DoPT OM 14.09.1992, paras 3 and 3.1", ["L2-30", "L3-07", "L3-19", "L3-20", "L3-21"]),
]

SCOPE = [
    ("1", "Short title and commencement", "IN (concept only)", "date of coming into force only"),
    ("2", "Interpretation", "IN", "definitions drive coverage and authority — note the dead organisational references"),
    ("3", "Application", "IN", "coverage and the five exclusions; a standing trap"),
    ("4", "Classification of Services", "IN (concept only)", "text retains class-based language; Group A/B/C governs in practice"),
    ("5", "Constitution of Central Civil Services", "OUT (no case value)", "live but purely machinery — see r.4 and r.6 instead"),
    ("6", "Classification of Posts", "IN (concept only)", "feeds the Group test in r.12"),
    ("7", "General Central Service", "IN (concept only)", "identifies the service for r.12(2)(b)"),
    ("8", "Appointments to Group A services and posts", "IN (concept only)", "President as appointing authority"),
    ("9", "Appointments to other services and posts", "IN (concept only)", "appointing authority for other groups"),
    ("10", "Suspension", "IN", "core — grounds, deemed suspension, review, subsistence"),
    ("11", "Penalties", "IN", "core — taxonomy, provisos, Explanation"),
    ("12", "Disciplinary authorities", "IN", "core — competence defects are the commonest ground of challenge"),
    ("13", "Authority to institute proceedings", "IN", "institution is not imposition"),
    ("14", "Procedure for imposing major penalties", "IN", "core — the sequence and the clocks"),
    ("15", "Action on inquiry report", "IN", "post-2014 shape only; the second show-cause is gone"),
    ("16", "Procedure for imposing minor penalties", "IN", "includes the mandatory-inquiry triggers"),
    ("17", "Communication of orders", "IN (concept only)", "one-liner; affects the limitation date"),
    ("18", "Common proceedings", "IN", "one case minimum"),
    ("19", "Special procedure in certain cases", "IN", "Article 311(2) second proviso interface"),
    ("20", "Officers lent to State Governments", "IN (concept only)", "machinery"),
    ("21", "Officers borrowed from State Governments", "IN (concept only)", "machinery; lending authority’s role"),
    ("22", "Orders against which no appeal lies", "IN", "three exclusions, one of them subject to an exception"),
    ("23", "Orders against which appeal lies", "IN", "core — the appealable list is wider than penalties"),
    ("24", "Appellate authority", "IN", "Schedule first, then the rule’s fallback"),
    ("25", "Period of limitation of appeals", "IN", "45 days from delivery; condonation"),
    ("26", "Form and contents of appeal", "IN", "formal defects and their cure"),
    ("27", "Consideration of appeal", "IN", "powers, enhancement and its precondition"),
    ("28", "Implementation of orders in appeal", "IN", "who implements"),
    ("29", "Revision", "IN", "CAG power for IA&AD; six months for the appellate authority"),
    ("29-A", "Review", "IN", "President only, new material only"),
    ("30", "Service of orders and notices", "IN (concept only)", "service mode feeds limitation"),
    ("31", "Power to relax time-limit and condone delay", "IN (concept only)", "who may condone what"),
    ("32", "Supply of copy of Commission’s advice", "OUT (omitted)", "omitted by the 2014 Second Amendment; the duty now sits in r.15(3)(b) and r.16(1)(d)"),
    ("33", "Transitory provisions", "OUT (transitional)", "transitional only"),
    ("34", "Repeal and saving", "OUT (transitional)", "transitional only"),
    ("35", "Removal of doubts", "OUT (transitional)", "transitional only"),
    ("Schedule", "Authorities for services, groups and posts", "IN (concept only)", "cited, not reproduced — read with general or special orders"),
    ("Art. 311", "Constitutional safeguards", "IN", "the rules are read subject to it; Rule 19 maps to the second proviso"),
    ("FR 53", "Subsistence allowance", "IN", "the money during suspension"),
    ("FR 54", "Pay on reinstatement", "IN", "the money after suspension"),
]

OBSOLETE = [
    ("“A second show-cause on the penalty proposed must precede a major penalty.”",
     "Deleted. The disciplinary authority acts on the inquiry report and the representation on it; no further "
     "opportunity on the proposed penalty is required.",
     "CCA (Second Amendment) Rules, 31.10.2014 (G.S.R. 769(E)), substituting r.15"),
    ("“Posts are Class I, II, III and IV.”",
     "Group A/B/C governs competence and appeal. The rule text retains older class language in places; read it as Group.",
     "DoPT instructions on classification of posts, 08.12.2017 (11012/10/2016-Estt.A-III)"),
    ("“Inquiry must be completed in 90 days / the charge sheet must issue in 3 months.”",
     "Those were administrative instructions. The statutory limits now sit in r.14: 45-day defence cap, 10 working days "
     "appearance, 6-month inquiry with recorded extensions.",
     "G.S.R. 548(E), 02.06.2017; DoPT FAQ, 08.12.2017 (11012/09/2016-Estt.A-III)"),
    ("“Any appellate authority may review its order.”",
     "Review belongs to the President alone, on new material that changes the nature of the case. Other authorities exercise revision.",
     "r.29 and r.29-A"),
    ("“The Commission’s advice is not supplied to the employee.”",
     "A copy is supplied and the employee is heard on it (15 days).",
     "CCA (Second Amendment) Rules, 31.10.2014; r.15(3)(b), r.16(1)(d) — and r.32, which had required the supply, was omitted"),
    ("“Rule 19 lets the department skip the inquiry whenever it is convenient.”",
     "Three gates only, each with a condition and an authorising level; reasons must be recorded and are reviewable.",
     "r.19 read with Art. 311(2), second proviso"),
    ("“A temporary hand’s termination under the Temporary Service Rules is a penalty.”",
     "It is excluded from the definition of penalty by Explanation (viii)(b). The route is narrow: it applies only while the servant is genuinely temporary, and never where the foundation is misconduct.",
     "r.11, Explanation (viii)(b); CCS (TS) Rules, 1965, r.5(1)"),
    ("“The Planning Commission, Postal Services Board and Telecom Board are live authorities.”",
     "Dead organisational references in the text. Read as the successor office; do not build a competence answer on them.",
     "r.2(l)(vi), r.29(1)(iii)"),
]

AUTHORITY = [
    ("Any penalty on any Government servant", "President", "r.12(1)", "process under r.14/r.16 still required"),
    ("Major penalty", "Disciplinary authority competent under r.12; never an authority subordinate to the appointing authority", "r.12(2), r.12(4)(a)", "Head of Office imposing removal"),
    ("Minor penalty, Group C (not CSCS) / Group D", "Secretary of the Ministry/Department, or the Head of Office if not lower in rank than the r.12(2) authority", "r.12(3)", "Head of Office lower in rank"),
    ("Probationer at LBSNAA", "Director of the Academy — censure and recovery only, after r.16", "r.12(4)(c)", "any major penalty"),
    ("Institution of proceedings", "President or an empowered authority; a disciplinary authority may itself institute", "r.13", "confusing institution with imposition"),
    ("Appeal", "Schedule / general or special order; fallback in r.24", "r.24", "appeal to “the next senior officer”"),
    ("Revision", "President; CAG for IA&AD; Head of Department; appellate authority within six months", "r.29(1)", "treating revision as a second appeal"),
    ("Review", "President only", "r.29-A", "any other authority reviewing"),
    ("Condonation of delay", "The authority before whom the delayed proceeding is filed, within r.31 / the proviso to r.25", "r.25, r.31", "condonation by an authority not seized of the matter"),
]

CASELAW = [
    ("Natural justice applies to departmental inquiries; the hearing must be fair, not formally perfect",
     "A.K. Kraipak v. Union of India (1969)", "administrative-law foundation; not a code of procedure"),
    ("The inquiry report must be supplied before the penalty is imposed",
     "Union of India v. Mohd. Ramzan Khan (1991); Managing Director, ECIL v. B. Karunakar (1993)",
     "supply is mandatory; relief depends on prejudice, which the employee must raise"),
    ("Non-supply of documents or the report vitiates only where prejudice is shown",
     "B. Karunakar (1993)", "prejudice is fact-specific; a bare assertion will not do"),
    ("A copy of the Commission’s advice must be supplied and the employee heard on it",
     "S.K. Kapoor v. Union of India (2010), now reflected in the rules",
     "advice only, not the Commission’s working notes"),
    ("Suspension must not be extended mechanically; a charge memo must follow within a reasonable time",
     "Union of India v. Ajay Kumar Choudhary (2015)", "read with the r.10(6)–(7) review architecture"),
    ("Findings are not reappreciated as an appeal; interference lies for perversity or want of evidence",
     "Union of India v. H.C. Goel (1964); Union of India v. P. Gunasekaran (2015)",
     "sufficiency of evidence is for the authority"),
    ("Penalty must be proportionate; interference with quantum is exceptional",
     "Union of India v. G. Ganayutham (1997); Lucknow Kshetriya Gramin Bank v. Rajendra Singh (2013)",
     "proportionality applied sparingly, not as a re-weighing"),
    ("The second proviso to Article 311(2) and Rule 19 dispense with the inquiry, not with the reasons",
     "Union of India v. Tulsiram Patel (1985)", "reasons are reviewable for relevance, not sufficiency"),
    ("Sealed cover applies only where a charge sheet has been issued or a prosecution is pending at the date of the DPC; an investigation is not enough",
     "Union of India v. K.V. Jankiraman (1991); Union of India v. B.V. Gopinath (2014)",
     "the date of consideration decides the sealed cover; material relied on to deny promotion must be disclosed"),
    ("Where any penalty is imposed, the sealed-cover finding is not acted upon and the case goes to the next DPC",
     "A.N. Mohanan v. Union of India (2007)",
     "para 3.1 of the 1992 OM applied; a censure is a blameworthy factor and carries no right to promotion in that year"),
    ("Unauthorised absence requires a finding that the absence was without authority",
     "Krushnakant B. Parmar v. Union of India (2012)", "the finding must match the charge"),
    ("A termination of a probationer is punitive if misconduct is its foundation, whatever its form",
     "Dipti Prakash Banerjee v. S.N. Bose National Centre (1999); Radhey Shyam Gupta v. U.P. State Agro Industries (1999)",
     "Pavanendra Narayan Verma v. Sanjay Gandhi PGI (2002) supplies the test: form plus foundation"),
]

SOURCES = [
    ("CCS (Classification, Control and Appeal) Rules, 1965 — Gazette text with amendments up to 01.11.2026",
     "https://www.referencer.in/CS_Regulations/CCS(CCA)Rules1965/Default.aspx"),
    ("DoPT — Frequently Asked Questions on time-bound disciplinary proceedings, 08.12.2017 (11012/09/2016-Estt.A-III)",
     "https://www.referencer.in/cs_regulations/ccs(cca)rules1965/11012_09_2016-Estt.A-III.aspx"),
    ("DoPT — classification of posts under the CCS (CCA) Rules, 08.12.2017 (11012/10/2016-Estt.A-III)",
     "https://www.referencer.in/CS_Regulations/CCS(CCA)Rules1965/11012_10_2016-Estt.A-III.aspx"),
    ("DoPT — regulation of pay on imposition of a penalty, 18.06.2019 (11012/15/2016-Estt.A-III)",
     "https://www.referencer.in/CS_Regulations/CCS(CCA)Rules1965/11012_15_2016_Estt.A-III.aspx"),
    ("DoPT — instructions on the sealed cover procedure, 19.01.2017 (11012/6/2016-Estt.A-III)",
     "https://www.referencer.in/CS_Regulations/CCS(CCA)Rules1965/11012_6_2016-Estt.A-III.aspx"),
    ("DoPT OM No. 22011/4/91-Estt.(A), 14.09.1992 — promotion of Government servants against whom disciplinary or court proceedings "
     "are pending: the sealed cover, paras 2 to 7 (full text, PDF)",
     "https://documents.doptcirculars.nic.in/D2/D02est/22011_4_91-Estt.A-14091992.pdf"),
    ("DoPT OM No. 22011/4/2007-Estt.(D), 28.04.2014 — effect of penalties on promotion and the role of the DPC (full text, PDF)",
     "https://documents.doptcirculars.nic.in/D2/D02est/22011_4_2007-Estt.D-28042014.pdf"),
    ("Indian Kanoon — consolidated text of the Rules (as published)",
     "https://indiankanoon.org/doc/18288843/"),
]

NOTES = [
    "The law date is 01.11.2026. The rules are applied as amended; the 2014 Second Amendment, the 2014 Third Amendment, "
    "the 2009 amendment to r.11(vi) and the 2017 statutory timelines are treated as part of the text, not as footnotes.",
    "Rule 15 is taught only in its post-31.10.2014 form. A case that turns on the absence of a second show-cause on the "
    "proposed penalty is a case about an obsolete provision — marked ⊘ wherever it appears.",
    "Classification follows Group A/B/C. Where the text retains class-based language (for example in r.4 or r.24), the "
    "operative Group reading is used and the textual lag is flagged in the L1 traps.",
    "Every date arithmetic in this book uses the conventions published in the verification harness: statutory day counts "
    "run from the day after the trigger unless the rule says “from the date of”; clear days exclude both termini; "
    "45-day and six-month caps are computed from the trigger date and not by adding extensions.",
    "Pay figures use 7th CPC matrix values and illustrative DA/DR of 60% (01.01.2026) and 63% ⚑ (01.07.2026). The 63% rate "
    "rests on the Cabinet decision of 28.10.2026; the formal order was awaited on the law date and is flagged ⚑ wherever "
    "it drives a figure.",
    "Facts, names, file numbers and offices are constructed for teaching. No case describes a real officer, and no case "
    "should be read as a finding about any real proceeding.",
    "The sealed-cover cases apply executive instruction, not rule: DoPT OM No. 22011/4/91-Estt.(A) dated 14.09.1992, issued after "
    "Jankiraman. Where a case turns on it, the paragraph is cited, and the book says plainly that the OM cannot enlarge a power given by "
    "the rules — which is why r.18(2) is read as subject to r.12(4).",
    "Communication of adverse entries in the APAR is governed by DoPT OM No. 21011/1/2005-Estt.(A)(Pt-II) dated 23.07.2009, read with "
    "the OM of 14.05.2009: an adverse entry must be communicated, the officer may represent against it, and an uncommunicated entry cannot "
    "be the foundation of a denial of promotion. That OM is cited by number and date because the Department has moved it between hosts; "
    "check the current copy on the DoPT circulars site before relying on it.",
    "Nothing here replaces the Gazette text or the departmental instructions in force in the office where a case is handled.",
]
