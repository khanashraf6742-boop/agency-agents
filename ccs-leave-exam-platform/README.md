# CCS (Leave) Rules, 1972 — study and practice platform

A single-file, offline exam platform for the Central Civil Services (Leave) Rules, 1972.
Open `CCS-Leave-Rules-1972-Exam-Platform.html` in any modern browser; nothing is fetched
from the network and no server is needed.

## What is inside the HTML file

| Datasets | Count | What they are |
| --- | --- | --- |
| Rule cards | 69 | Rules 1–66 plus 38‑A, 39‑A to 39‑D, 43‑A, 43‑AA, 43‑B, 43‑C — bare text, plain explanation, Hinglish gloss, requirements, exceptions, authority, key figures, cross‑references and the exam trap |
| MCQs | 682 | Four options, one key, a full explanation in the pension-platform layout (Answer → Steps & Statutory Rationale → Why the others are wrong → Exam-safe point → Statutory Authority) |
| Numerical 80 | 80 | A separate set of every arithmetic question in the book, each with a three-step worked solution and a note on which mistake produces each wrong option. Also published as `Numerical-80-CCS-Leave-Rules-1972.md` |
| Flashcards | 341 | Rule identification (69), key figures (65), competent authorities (67), definitions (10) and exam traps (130) |
| Revision modules | 40 | Every rule in the book, grouped into microlearning cards with a mnemonic |
| CBT papers | 31 | Chapter tests, focused rule tests, numeric drills, clause audits, case-file papers, five 100-question full lengths, plus a statement/negative/sequence drill and a timed run at the Numerical 80 |
| Comparative tables | 28 | Leave salary by type, the combination matrix, the register of deleted rules, the First Schedule, all forms |
| Case files | 20 | Establishment files with facts, issue, correct action, authority and the point to carry away |
| Forms | 11 | Forms I–X with the rule, signatory and timing of each |
| Amendments | 19 | Every instrument that moved a figure, with the date in force |
| Core facts | 40 | The last-page revision sheet |

## Using it

* **Dashboard** — coverage, accuracy, weakest chapters, recent papers.
* **Question practice** — filter by chapter, difficulty, unseen, bookmarked or mistakes;
  search the stem, the id or the explanation; shuffle the set.
* **Numerical 80** — the arithmetic set, grouped into nine blocks, with stepwise solutions that can be
  opened per question or all at once, and a one-click download of the whole set as a text file.
* **Test series** — a timed CBT with a palette, mark-for-review, a countdown and a
  question-by-question scorecard.
* **Numerical lab** — six calculators that show the arithmetic: EL credit with the
  285-day buffer, commutation, retirement encashment, the EOL penalties, the study-leave
  combination cap and CCL tranches.
* **Export / Import** — progress is kept in the browser's local storage; the header
  buttons move it between devices as JSON.

## Rebuilding

The build directory holds the generators; the HTML is assembled from them.

```bash
cd build
python3 engine.py        # writes mcqs.json and num80.json (needs data_*.py + rules.json)
python3 build_extras.py  # writes extras.json (flashcards, modules, mocks, tables, cases, forms, amendments, core)
python3 assemble.py      # writes ../CCS-Leave-Rules-1972-Exam-Platform.html and ../Numerical-80-CCS-Leave-Rules-1972.md
python3 smoke_audit.py   # writes ../AUDIT.md; exits non-zero if any content check fails
node smoke.js            # headless test: 15 checks over every view (needs jsdom)
```

`smoke.js` needs `npm install jsdom` once. The test fails loudly if a view stops
rendering, a filter returns nothing, a mock cannot be scored, a calculator throws or a
console error appears. `smoke_audit.py` is the content side of the same discipline: it
re-derives the counts, checks that every key letter matches its explanation, and refuses
a build in which a numerical answer contradicts its own arithmetic.

### Source of each figure

* **Bare text** — DoPT consolidation of the CCS (Leave) Rules, 1972, edition updated
  24.09.2024, reproduced rule by rule in `rules.json` with the guide's clause‑level
  annotations. `extract_rules.py` built that file from the supplied study guide.
* **Key figures** — Rules 26, 27, 29–32, 38, 38‑A, 39–39‑D, 43–43‑C, 44, 49–63, each
  cross‑checked against the amendment register.
* **Non‑statutory leave** — casual leave, special casual leave, compensatory leave and
  restricted holidays come from DoPT O.M.s and the Leave Brochure. They are held in a
  separate chapter (`NS`) and every card, question and flashcard says so. **No rule
  number is ever cited for them**, because they are not in the Rules.
* **Deleted and omitted provisions** — Rules 18, 23(1)–(2), 30(1)(b), 30(1)(c),
  30(1)(e), 32(2)(c), 35–37, 45, 46 and 58–59 are treated as dead law. The bank tests
  only their *status*, never a benefit under them. The register is in table 19.

### Quality rules enforced by the build

* Exactly four distinct options; the key letter in the explanation always matches the
  `ans` field.
* No two questions share a stem or an identical option set.
* The correct option is not systematically the longest: across the bank it is the
  longest option in 51% of questions, and the case files (which used to be 20/20) are
  now 6/20.
* Distractors never come from the same rule as the answer, and a distractor's figures
  never overlap the answer's figures.
* Omitted rules are never asked as "which rule governs X"; they are asked only as
  "what is its status" or "what did it once govern".

## The question families added in the second pass

The first edition tested rules well but under-tested *format*. These were added:

| Family | Count | Why |
| --- | --- | --- |
| `STMT-` | 12 | Multi-statement "how many are correct" items — the format most competitive papers use |
| `NEG-` | 10 | "Which of the following is NOT …" items, where the three distractors are true statements of the same rule |
| `SEQ-` | 8 | Items where the *order* of the steps is the test — regularisation, encashment, commutation checks, the study-leave exit |
| `HL-` | 10 | The headline figures (730, 360, 90, 28, 18, 12, 3, 10, 5, 300) one rule at a time |
| `WORK-` | 9 | The study guide's own nine hardest trap-cases, converted from worked examples into questions |

## Licence and caution

This is a study aid, not a consolidated statute and not legal advice. Casual leave and
the other non-statutory heads are labelled as such throughout. Verify any operative
figure against the bare Rules, or the O.M. in force, before using it in an office order.
