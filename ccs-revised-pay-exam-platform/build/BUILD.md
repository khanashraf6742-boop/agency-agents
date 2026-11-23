# How this platform is built

Nothing in the finished HTML is typed by hand. It is assembled from the sources in this directory, and the
build refuses to write the file if any check fails.

## The pipeline

```
paymatrix.py          the Pay Matrix as code: 19 Levels, 543 cells, the fitment helpers, and a self-check
rules.py              Rules 1-17 with their statutory text, a plain-language summary, figures, traps and hooks
data_numeric.py       the numerical set — N() appends one question with its steps, distractors and matrix slice
data_bank.py          the general bank, written in the rule's own form
data_bank2.py         the general bank, written the way a paper tests it (negative, sequencing, case files)
        |
        v
engine.py             shuffles each question's options, balances the key, builds the answer block and the
                      matrix payload -> pay.json, matrix.json, rules_out.json
        |
        v
audit.py              46 checks. Re-derives every rupee asserted in an answer from paymatrix.py. Refuses to
                      pass a question whose table is not a real slice of the Level it claims, whose key is not
                      unique, or whose options two of which propose the same figure. -> ../AUDIT.md
        |
        v
assemble.py           runs audit.py, and stops if it fails. Inlines CSS, JS and JSON into shell.html
                      -> ../CCS-Revised-Pay-Rules-2016-Exam-Platform.html
                      -> ../Numerical-Set-Worked-Solutions.md
        |
        v
smoke.js              72 behavioural checks against the BUILT file in jsdom
```

## Running it

```bash
cd build
python3 paymatrix.py     # the matrix self-check: 19 levels, 543 cells, 0 disagreements
python3 engine.py        # build the JSON
python3 audit.py         # 46 checks; exits non-zero on failure
python3 assemble.py      # refuses to write the HTML if the audit failed
node smoke.js            # 72 checks against the built HTML
```

No third-party Python packages. `smoke.js` needs `jsdom`, which the repository already carries in
`/home/user/agency-agents/node_modules`.

## The three things that keep the figures honest

**1. The matrix is regenerated, not trusted.** `paymatrix.py` holds the gazette figures, and its `__main__` block
rebuilds every column from its first cell by 3 per cent rounded to the nearest ₹100 and compares. A single
disagreement is a failure. This is how the *nearest* ₹100 was established: rounding *up* desynchronises 18 of the
19 columns.

**2. Every asserted rupee is re-derived.** `audit.py` does not read the answer options looking for a figure; it
recomputes the sum from the stem's inputs and compares. `pm.next_higher_cell("4", round(12560 * 2.57)) == 32300`
and `"32,300" in key("PY-001")` are two halves of one assertion — either half alone could pass while the item was
wrong.

**3. A table may only mark a cell it can defend.** A question's `marks` name the cell the reader starts from and the
cell he lands on. The audit asserts that both are real cells of the Level displayed, that the cell NUMBER is right,
and that the note actually discusses the figure — because the first version of this build marked a "pay before" cell
in the *destination* Level of a promotion, where that pay does not exist.

## Editing a question

Add or edit the `N(...)` / `Q(...)` call in the right data file, keeping the argument order:

```
N(topic, rule, rules_text, stem, answer, steps, distractors, safe, source, trap,
  level=..., cells=..., marks={"start": n, "land": m}, table_note=...)
```

`answer` must match one of the options verbatim in substance; the engine places it and records the letter. `steps`
are rendered as a numbered list, so write one clause of the rule per step. Each distractor is a
`(text, why_it_is_wrong)` pair — the second element is what the reader sees under *Where the other options come
from*, so write the mistake, not a restatement of the right answer.

Then re-run the pipeline. If `audit.py` fails, do not work around it: the check that failed is almost always
pointing at a real defect in the item.
