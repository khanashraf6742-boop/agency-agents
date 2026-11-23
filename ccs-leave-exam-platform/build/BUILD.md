# build/ — source generators for the CCS (Leave) Rules 1972 platform

`build/` is ignored by the repository's root `.gitignore` (line 57: `build/`), so the
generators live here on disk but are not committed. The deliverable is the assembled
HTML one directory up; this file says how to rebuild it.

## Pipeline

```
rules.json ──┬─> data_map.systematic_facts()
             ├─> data_derived.conditions/limits/authorities/combinations/scl_table
             ├─> data_core.FACTS          (authored, Ch I – IV-D)
             ├─> data_special.FACTS       (authored, V-A, V-B, IV-C)
             ├─> data_study.FACTS         (authored, Rules 50–66, Schedules, Forms)
             ├─> data_nonstat.FACTS       (CLNS-01…30, chapter NS)
             └─> data_cases.FACTS         (CASE-01…20) + data_numeric.numeric_facts()
                        │
                    engine.py ──> mcqs.json  (635 questions)
                        │
build_extras.py ──> extras.json (flashcards, modules, mocks, tables, cases, forms, amendments, core)
                        │
                    assemble.py ──> ../CCS-Leave-Rules-1972-Exam-Platform.html
                        │
                     smoke.js  (jsdom, 14 checks)
```

Run, in order:

```bash
python3 build_extras.py    # extras.json  (independent of mcqs.json? no — run after engine.py)
python3 engine.py          # mcqs.json
python3 build_extras.py    # extras.json, now that mock ids exist
python3 assemble.py        # the HTML
node smoke.js              # needs `npm install jsdom`
```

`extras.json` maps mock papers onto question ids, so run `engine.py` first and
`build_extras.py` again after it.

## Files

| File | Role |
| --- | --- |
| `extract_rules.py` | Parsed the supplied study guide into `rules.json`; kept for provenance |
| `rules.json` | 69 rule records: title, chapter, bare text, summary, Hinglish, conditions, exceptions, authority, key figures, forms, cross-references, traps |
| `data_core.py` | Authored MCQs for Chapters I–IV-D |
| `data_special.py` | Authored MCQs for maternity, paternity, CCL, WRIIL, LPR, encashment, seamen, POSH, departmental leave |
| `data_study.py` | Authored MCQs for study leave, Rules 64–66, the First Schedule and the forms |
| `data_nonstat.py` | Casual leave, SCL, comp-off and RH — chapter `NS`, `rule = 0`, every source marked non-statutory |
| `data_numeric.py` | Computed numerical drills (EL credit, HPL, ceilings, commutation, encashment, EOL penalties, LTC, CCL, maternity, study, dies non) |
| `data_cases.py` | 20 dated administrative case files; appends the numeric drill |
| `data_map.py` | Rule-identification pairs; omits dead rules from the option lists |
| `data_derived.py` | Clause-level, key-figure, authority and combination questions generated from `rules.json` and the guide's tables |
| `engine.py` | Shuffles options from a hash of the question id, rotates the key, enforces four distinct options, writes the explanation layout |
| `build_extras.py` | Flashcards, 40 modules, 29 mock papers, 28 tables, cases, forms, 19 amendments, the Core 40 |
| `assemble.py` | Inlines data, CSS and JS into the single HTML file |
| `smoke.js` | Headless test of every view, filter, paper and calculator |

## Content rules the generators enforce

* An **omitted rule is never a live citation**. Rules 58 and 59 are asked about only as
  "what is its status" and "what did it once govern", and are never offered as a rival
  answer to a live rule.
* A **distractor never shares a number with the correct option**, and never comes from
  the same rule as the answer.
* **No identical option sets**: each generator keeps a set of the combinations it has
  already used and picks another when a drill lands on the same four figures.
* **Casual leave, SCL, comp-off and RH never carry a rule number** in a stem.
  Their chapter is `NS`, their `rule` field is `0`, and their sources say so.
* Case answers are stored as **short capsules** so that the correct option is not
  identifiable by being the longest one (this used to be true for 20/20 case questions).
* Study-leave answers are capped the same way; the bank-wide rate at which the correct
  option is also the longest is 51%, which is what a blind guess would give.

## Second pass — question families and the Numerical 80

Two new data files were added after the first publication.

### `data_plus.py` — 49 questions in five unfamiliar formats

| Prefix | Count | What it tests |
| --- | --- | --- |
| `STMT-` | 12 | Multi-statement "how many are correct". The options are counts (only (i); only (ii) and (iii); all three), so spotting one false statement is not enough — you have to audit all three. |
| `NEG-` | 10 | "Which of the following is NOT …". The distractors are true statements of the same rule, so the item fails unless the one false proposition is actually known. |
| `SEQ-` | 8 | Process order — regularising overstay, the encashment sequence, the commutation checks, the study-leave exit. The wrong options are the same steps in a plausible but wrong order. |
| `HL-` | 10 | The headline figures, one rule each: 730, 360, 90, 28, 18, 12, 3, 10, 5, 300. |
| `WORK-` | 9 | The study guide's nine trap-cases, converted from worked examples into questions. |

`STMT-` items are checked at audit time to ensure the key is written as a count, never a sentence.

### `data_num80.py` — 80 numerical questions with stepwise solutions

Nine blocks: earned leave credit and the 285-day buffer (12), half pay leave and dies non (8),
commuted leave and leave not due (7), encashment and the 300-day pot (9), maternity/child care/adoption (9),
study leave (11), departures and overstay (7), LPR and foreign service (8), vacation and joining time (8).

Each item is written with `N(block, rule, chapter, stem, answer, steps, distractors, safe_point, source, trap, tag)`.
`engine.py` renders it to a record whose `expl` has the same five-part shape as an MCQ explanation:
`Answer / Worked solution, step by step / Where the other options come from / Exam-safe point / Statutory Authority`.

**The arithmetic is a build-time assertion.** Every numeric answer was re-derived in Python during authoring
and several were wrong on the first pass — the buffer items, the encashment total and the LND limit in
particular. Do not edit a number without re-running `engine.py` and checking the printed block counts.

`numeric80_records()` writes `build/num80.json`; `assemble.py` inlines it as `NUM80_DATA` (the single-file
platform cannot fetch a sibling file) and also writes the readable study edition
`Numerical-80-CCS-Leave-Rules-1972.md` from the same records, so the HTML and the markdown can never drift.

### Pipeline

```
python3 engine.py        # mcqs.json + num80.json
python3 build_extras.py  # extras.json (reads num80.json for MOCK-31)
python3 assemble.py      # the single HTML + Numerical-80-...md
python3 smoke_audit.py   # AUDIT.md — content checks, exits non-zero on failure
node smoke.js            # end-to-end UI test
```

### Notes for the next editor

* `STMT-`/`NEG-`/`SEQ-`/`HL-`/`WORK-` ids must stay in their own namespace; `data_study.py` already owns
  `MISC-01..03`, and the engine asserts unique ids.
* MOCK-31 draws its 40 questions from `num80.json`, so those ids are registered in `MCQS_MAP` as well as
  `NUM80_MAP`. Any new paper that uses the numerical set must do the same.

## Third pass — the last eighteen (682 → 700)

Eighteen questions were added to `data_plus.py` in a final block, each chosen because a high-yield rule was thin
in the bank or was being tested only through the rule-map families:

| Id | Rule | Point tested |
| --- | --- | --- |
| `LPR-05` | 38 | what LPR is composed of; EOL excluded by the Note |
| `COM-05` | 30(2) | conversion and recovery where the servant resigns after commuted leave |
| `EW-05` | 40 | full pay / half pay rates across EL, commuted and HPL |
| `ADV-01` | 42 | advance of leave salary, 30-day threshold, one month's pay |
| `LTC-08` | 38-A | refund with interest at PF + 2% where the LTC is not availed |
| `DEATH-03` | 39-C | the order in which the cash equivalent is paid |
| `INV-03` | 39-B(2) | no HPL leg on invalidation for a temporary servant |
| `PSU-03` | 39-D | earned leave only on absorption |
| `SEA-03` | 47 | seaman's two limbs |
| `COM-06` | 30(1)(a) | refused commutation falls back to ordinary HPL |
| `EW-06` | 34 | the pension test for re-employment |
| `FORM-05` | 14 | Form 1 for leave and for extension |
| `ORD-03` | 16 | provisional sanction of 60 days |
| `EW-07` | 21(1) | leave ends the day before charge is resumed |
| `EW-08` | 22 | prefixed/suffixed holidays, automatic on medical certificate |
| `VAC-01` | 28(1)(b) | the 20-day fraction for vacation not taken |
| `ADP-03` | 43-AA | the male route on adoption: 15 days within six months |
| `WRIIL-07` | 44(2)(a) | the half pay tail converted at an equal HPL debit |

Two lessons worth keeping:

* **Chapter codes are a taxonomy, not the rule's chapter number.** `IV-A` holds Rules 26–42 and `IV-C` holds
  Rules 38-A to 39-D; assigning by the statutory chapter puts a question in the wrong filter. Check an existing
  question on the same rule before choosing the code (`LS-01` for Rule 40, `SEA-01` for Rule 47, `LTC-01` for
  Rule 38-A).
* **A correct option that is also the longest option is a free mark.** Thirteen of these eighteen were written
  that way on the first pass. The fix is always the same: shorten the key to its bare proposition and lengthen
  the distractors with the plausible reason a candidate would invent. `smoke_audit.py` now fails the build if
  the share of such questions across the bank rises above 55%.

`MOCK-32` draws exactly these eighteen, so the paper and the block cannot drift apart; `smoke.js` scores it to
18/18 and asserts the bank is 700.
