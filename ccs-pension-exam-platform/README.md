# CCS (Pension) Rules, 2021 — Exam Platform

A single self-contained HTML file covering the whole of the CCS (Pension) Rules, 2021, built to the same
standard as the pay and leave platforms.

**Open `CCS-Pension-Rules-2021-Exam-Platform.html`.** No server, no dependencies.

## What is in it

| | Count |
|---|---|
| Rules in the statute | 87 |
| Rules transcribed from the gazette, full text | **87** |
| Words of statutory text | 48,153 |
| Chapters | 14 |
| Forms appended to the rules | 14 |
| Formats appended to the rules | 13 |
| **Provisions parsed from the text** | **1,065** |
| Provisions reached by at least one question | **1,065 (100 %)** |
| Questions | 1,033 |
| Instruments in the amendment register | 18 |
| Sourced FAQs | 10 |

Nothing is pending. There is no rule present as a title only, and no passage paraphrased in place of its text.

## Coverage is measured, not asserted

The platform claims to reach every part of the statute, so the build parses the rule text into
provisions — rules, sub-rules, clauses, sub-clauses, provisos and Explanations — and then checks
every one of them against the questions that cite it. `build/coverage.py` reports the result and
`build/audit.py` fails the build if any provision is left without a question.

| Level | Provisions | With a question |
|---|---|---|
| Rule as a whole | 16 | 16 |
| Sub-rule | 408 | 408 |
| Clause | 396 | 396 |
| Sub-clause | 119 | 119 |
| Proviso | 84 | 84 |
| Explanation | 42 | 42 |
| **Total** | **1,065** | **1,065 (100 %)** |

`AUDIT.md` prints the matrix provision by provision with the questions that reach each one, so the
claim can be checked by hand as well as by code.

## The amendment register

The 2021 gazette is the starting point, not the current position. Eighteen instruments have changed or
explained it since: three sets of amendment rules and fifteen office memoranda. Every one is in the
page with its number, date, effective date and the provisions it touches, and a per-rule badge shows
which rules carry an amendment.

Eight were read in full and their paragraphs are reflected in the questions. The other ten are
recorded from the Department's own circular index: the instrument, its number, its date and its
effect, but not paragraph text. The page marks the difference — **full text** against **from the
index** — so an entry that has not been read is never presented as though it had been.

Three of the instruments amend the rule text itself and are applied to it:

- **G.S.R. 770(E)** of 7 October 2022 — the withholding power in rule 8 moves from the President to
  the Secretary or the Comptroller and Auditor-General, and a new appeal to the President is added;
- **G.S.R. 410(E)** of 16 July 2024 — Form 6-A replaces Form 4 and Form 6 across the pension rules;
- **G.S.R. 340(E)** of 22 May 2025 — forfeiture of Government-service benefits on dismissal or
  removal from a public sector undertaking, following *Suraj Pratap Singh v CMD BSNL*.

The rest operate on the rules without amending their text. That is a real feature of this statute and
the platform shows it rather than smoothing it over.

## The Form / Format distinction

Rule 3 of these Rules defines two different things:

- **rule 3(1)(k)** — a "Form" means a form appended to these rules;
- **rule 3(1)(l)** — a "Format" means a format appended to them.

They are separately numbered series. Form 3 is the gratuity nomination under rule 46; Format 3 is the memorandum
of charges under rule 8(2)(c). The platform keeps two registers and marks every entry with the sub-rule that
prescribes it, so a question that asks for a Form cannot be answered with a Format.

## How the build is verified

`build/audit.py` runs 57 checks and **exits non-zero** if any fails. The load-bearing ones:

- all 87 rules transcribed, no rule left pending, and every chapter's span present;
- every question cites a rule the build actually holds;
- every Form and Format citation resolves to a transcribed sub-rule;
- every worked rupee figure re-derives from the formula the explanation claims to apply;
- the answer letters are used evenly, and the key is not visibly the longest option;
- every FAQ cites a transcribed rule;
- **every provision of the statute is reached by a question**, at all six levels;
- every internal cross-reference resolves, or is on a short list of defects that are in the
  instrument itself (see below);
- every instrument in the amendment register names provisions that exist, and no two share an id;
- no question offers the superseded twenty-lakh gratuity ceiling as the current one.

`build/smoke.js` then parses the built HTML with jsdom and checks the rendered result: 87 rule cards numbered
1–87 with no gaps, rule 3 defining both Form and Format, rule 87 being the repeal, every question with four
options and one key each, 14 + 13 register rows all sourced, the amendment register carrying all eighteen
instruments, and the coverage section showing 100 per cent.

```
cd build
python3 engine.py     # 1,033 questions from the rule text and the orders
python3 coverage.py   # provision-level reach
python3 audit.py      # 57 checks, writes AUDIT.md
python3 assemble.py   # the HTML
node smoke.js         # DOM checks
```

## Files

```
CCS-Pension-Rules-2021-Exam-Platform.html   the deliverable
AUDIT.md                                    generated report
build/pension_rules.py    TEXT: all 87 rules, paragraph for paragraph
build/titles.py           the 87 marginal headings
build/forms.py            14 Forms, 13 Formats, 11 leave Forms
build/provisions.py       parses the text into 1,065 provisions
build/coverage.py         which provisions a question reaches
build/xrefs.py            resolves every internal citation
build/amendments.py       the 18 instruments, with provenance
build/gen_questions.py    whole-text and opening-words questions
build/data_current.py     the current-affairs facts
build/engine.py           record builder and option balancer
build/data_*.py           the hand-written question facts
build/assemble.py         builds the HTML
build/audit.py            57 checks
build/smoke.js            jsdom checks
```

## Corrections made to the source copy

Two defects in the taxguru transcript, both handled explicitly rather than silently:

1. **Chapter XII's opening rule is printed as "66".** It is rule 79. The sequence already carries a rule 66
   (revision of pension) in Chapter X, and rules 80 to 87 follow 79 consecutively. It is transcribed under 79,
   with a note in `pension_rules.py`.
2. **Forms are 14, not 13.** Rule 63(5)(a) prescribes **Form 7-A**, which the statute's own download list
   includes. The register carries all fourteen.

## Where the current order differs from the printed rule

Rule 45(1) caps gratuity at **₹20 lakh** in the text notified on 20 December 2021. The ceiling was raised to
**₹25 lakh** with effect from 1 January 2024 by an Office Memorandum whose paragraph 7 says the formal
amendment to the Rules will be notified separately. It has not been. The page states the rule text, states the
order, and marks the question that turns on the difference — it does not silently substitute the later figure
for the statutory one, and it does not teach a candidate to answer with a superseded one.

The same pattern applies in three other places, all shown on the page:

- **family pension to a child before the husband** — rule 50(8)(a) pays the spouse first, an Office
  Memorandum of 1 January 2024 lets a female servant ask for her child first when a matrimonial proceeding is
  pending, and paragraph 6 of that order says the rule amendment will be notified separately;
- **the withholding authority in rule 8** — the 2021 text gives it to the President, G.S.R. 770(E) moves it to
  the Secretary or the C&AG with an appeal to the President;
- **Form 4 and Form 6 at retirement** — both are now Form 6-A under G.S.R. 410(E) of 16 July 2024.

## Defects in the instrument itself

Five cross-references in the gazette point at provisions that do not exist. They are not transcription
errors: each was checked against the published text directly. `build/xrefs.py` lists them and
`build/audit.py` fails on any unresolved citation that is *not* on that list, so a transcription gap
cannot hide among them.

| Citation | Refers to | The defect |
|---|---|---|
| r8(4)(d) | sub-rule (9) of rule 8 | rule 8 has only (1)–(8) |
| r65(5)(d), r65(5)(e) | clause (c) of rule 8(5) | rule 8(5) has no clauses |
| r76(5)(e) | clause (b) of rule 77(1) | rule 77(1) has clauses (i)–(x) |
| r81(2) | clause (d) of rule 76(2) | rule 76(2) has no clauses |

Rule 35 was truncated in an earlier build and the check caught it: rule 35(1) says "subject to
sub-rule (6)", and the transcription stopped at (5). Sub-rules (6) and (7) are now present, and the
audit asserts that rule 35 carries every sub-rule its own text cites.
