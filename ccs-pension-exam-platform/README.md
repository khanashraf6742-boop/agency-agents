# CCS (Pension) Rules, 2021 — Exam Platform

A single self-contained HTML file covering the whole of the CCS (Pension) Rules, 2021, built to the same
standard as the pay and leave platforms.

**Open `CCS-Pension-Rules-2021-Exam-Platform.html`.** No server, no dependencies.

## What is in it

| | Count |
|---|---|
| Rules in the statute | 87 |
| Rules transcribed from the gazette, full text | **87** |
| Words of statutory text | 42,754 |
| Chapters | 14 |
| Forms appended to the rules | 14 |
| Formats appended to the rules | 13 |
| Questions | 95 |
| Sourced FAQs | 10 |

Nothing is pending. There is no rule present as a title only, and no passage paraphrased in place of its text.

## The Form / Format distinction

Rule 3 of these Rules defines two different things:

- **rule 3(1)(k)** — a "Form" means a form appended to these rules;
- **rule 3(1)(l)** — a "Format" means a format appended to them.

They are separately numbered series. Form 3 is the gratuity nomination under rule 46; Format 3 is the memorandum
of charges under rule 8(2)(c). The platform keeps two registers and marks every entry with the sub-rule that
prescribes it, so a question that asks for a Form cannot be answered with a Format.

## How the build is verified

`build/audit.py` runs 21 checks and **exits non-zero** if any fails. The load-bearing ones:

- all 87 rules transcribed, no rule left pending, and every chapter's span present;
- every question cites a rule the build actually holds;
- every Form and Format citation resolves to a transcribed sub-rule;
- every worked rupee figure re-derives from the formula the explanation claims to apply;
- the answer letters are used evenly, and the key is not visibly the longest option;
- every FAQ cites a transcribed rule.

`build/smoke.js` then parses the built HTML with jsdom and checks the rendered result: 87 rule cards numbered
1–87 with no gaps, rule 3 defining both Form and Format, rule 87 being the repeal, 95 questions with four
options and one key each, and 14 + 13 register rows all sourced.

```
cd build
python3 engine.py     # 95 questions
python3 audit.py      # 21 checks, writes AUDIT.md
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
build/engine.py           record builder and option balancer
build/data_*.py           the question facts
build/assemble.py         builds the HTML
build/audit.py            21 checks
build/smoke.js            jsdom checks
```

## Corrections made to the source copy

Two defects in the taxguru transcript, both handled explicitly rather than silently:

1. **Chapter XII's opening rule is printed as "66".** It is rule 79. The sequence already carries a rule 66
   (revision of pension) in Chapter X, and rules 80 to 87 follow 79 consecutively. It is transcribed under 79,
   with a note in `pension_rules.py`.
2. **Forms are 14, not 13.** Rule 63(5)(a) prescribes **Form 7-A**, which the statute's own download list
   includes. The register carries all fourteen.

## A figure the statute and current practice disagree on

Rule 45(1) caps gratuity at **₹20 lakh** in the text notified on 20 December 2021. The ceiling was raised to
**₹25 lakh** with effect from 1 January 2024 by a subsequent Office Memorandum. The platform states the rule
text and flags the change in the FAQ rather than silently substituting the later figure for the statutory one.
