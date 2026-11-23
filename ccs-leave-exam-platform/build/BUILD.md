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
