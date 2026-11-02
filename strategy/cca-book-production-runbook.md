# Runbook — Producing a CCS rules case-study book with the Government Rules team

**Owner:** Government Rules Supervisor · **Division:** `government-rules` · **Applies to:** CCS (CCA) 1965, CCS (Pension) 2021, CCS (Conduct) 1964, CCS (Leave) 1933 study products
**Reference build:** `CCS_CCA_Rules_1965_Case_Studies_2026-11-02.html`

This is the pipeline the supervisor runs. It is written so that a second supervisor can reproduce a signed-off book from the repository alone.

---

## 0. Roster and why each seat exists

| Agent | Seat | Owns | Fails the product if absent |
|---|---|---|---|
| `government-rules-supervisor` | 🧭 Supervisor | scope lock, contracts, gates, sign-off | nobody can say what was excluded or what was not checked |
| `ccs-scope-authority-analyst` | 🗂️ Scope | scope register, authority matrix, obsolete register | authority statements drift from the text |
| `cca-procedure-specialist` | 📜 Procedure | rules 11, 14–19 | procedure cases lose their sub-rules and timelines |
| `cca-suspension-appeals-specialist` | ⏸️ Suspension & appeals | rules 10, 22–29A, FR 53 | suspension and limitation arithmetic go wrong |
| `service-law-precedent-researcher` | ⚖️ Precedent | judgments and OMs, at the width decided | citations inflate into slogans |
| `cca-case-author` | ✍️ Author | L1/L2/L3 items in house style | items become essays, marks stop reconciling |
| `cca-quant-verifier` | 🔍 Verifier | recomputation, citation audit, red team | "checked" replaces "proved" |
| `ccs-book-builder` | 🖨️ Builder | HTML book, indices, print, a11y | the deliverable is not shippable |

The supervisor never drafts content and the verifier never edits it. Independence is the control.

---

## 1. Intake (T-0)

Collect, before any drafting:

- [ ] the topic and the audience (exam level, office use, training)
- [ ] the **law date** — the date the text is stated to be current
- [ ] the **format precedent** (if the requester supplies an existing book, its structure is the contract)
- [ ] the **level mix** (L1/L2/L3 counts) and the marks convention
- [ ] every source that will be treated as canonical

Output: a one-paragraph brief and a law date. Nothing else starts until the law date is fixed, because every later check is "as on" that date.

---

## 2. Gate G0 — scope lock

The scope analyst produces the **scope register**: every rule classified `IN` / `IN (concept only)` / `OUT (spent)` / `OUT (superseded)`, one line of reason each.

Pass criteria:
- every rule in the instrument appears
- every exclusion cites the instrument that changed or exhausted it
- the obsolete register has at least the entries the team knows secondary sources still teach

Blocking examples from the reference build: the pre-2014 second show-cause; Class I–IV nomenclature; pre-2017 circular timelines; "review" attributed to appellate authorities; "Commission's advice not to be supplied".

---

## 3. Gate G1 — contracts

The supervisor writes one delegation board row per slice (see the supervisor agent's template). Each row names: owner, reviewer, deliverable file, count, and machine-checkable acceptance criteria.

Rules for slicing:
- one slice per **rule cluster**, never per "chapter of a book"
- a slice must be reviewable in one sitting
- overlapping slices are a design error, not a coordination problem

---

## 4. Gate G2 — shape

The author submits content modules. The builder's `--audit` mode is the shape gate: required blocks present, counts match the contract, marks reconcile, every step row carries a provision.

Reject on shape only. Do not mix shape and truth in one review pass — authors fix the wrong thing.

---

## 5. Gate G3 — truth

The verifier runs:

```bash
python3 scripts/cca-1965/verify.py
```

It recomputes every asserted date, period and rupee figure from the facts and checks every proposition against the citation table. Non-zero exit blocks assembly.

Pass criteria:
- 0 failing assertions
- every figure traceable to a fact or a stated rate
- every citation traced to the current text
- every `⚑` item has the order still awaited named

---

## 6. Gate G4 — build

```bash
python3 scripts/cca-1965/build.py --out CCS_CCA_Rules_1965_Case_Studies_$(date +%F).html
```

The build refuses to write on: duplicate ids, unresolved anchors, external resources, empty required blocks, marks mismatch.

Then the whole file is cross-checked against its own source modules — granularly, element by element:

```bash
python3 scripts/cca-1965/validate.py CCS_CCA_Rules_1965_Case_Studies_$(date +%F).html
```

`validate.py` re-reads `l1.py`, `l2a–d.py`, `l3a–c.py` and `meta.py`, parses the finished HTML with its own mini-DOM, and compares both directions: is every source item rendered, and is every rendered item traceable to the source? It then audits the file as a whole. Twelve groups:

| Group | What it proves |
|---|---|
| A | file size, one `<script>`, doctype, charset, viewport, language, no external resources, no `http://` beyond source links, script syntax |
| B | tag nesting, duplicate ids, broken anchors, heading order, table and `details` structure, script-referenced ids that do not exist |
| C | source-vs-render for every L1 row, every L2/L3 case, both registers, the matrices and the indices — heading, marks badge, facts, record, questions, path, step cells, total row, answer, model answer, tags, back-links |
| D | every date is a real calendar date and lies on or before the law date; rupee grouping; percentages; flags |
| E | clock, scope, obsolete, case-law and source cross-references; every rule cited exists in the register; every OM number cited is traceable in the notes or sources |
| F | spacing, quote and dash hygiene, duplicated sentences, literal markup leaking into the text, front-matter counts, print rules |

A print edition is rendered from the same HTML, so the PDF can never drift from the book:

```bash
pip install --target /tmp/x2p xhtml2pdf
PYTHONPATH=/tmp/x2p python3 scripts/cca-1965/pdf.py
```

`pdf.py` flattens what a PDF cannot do — it drops the toolbar, promotes every `<details>` to a visible block, removes the reveal buttons and keeps the level pill and marks badge off the heading line — then renders A4 with DejaVu (which carries ⚑, ⊘, ⚠ and ₹). The four fonts are copied into `scripts/cca-1965/.fonts/` on first use and are git-ignored; the folder falls back to the system DejaVu if it is missing. Ship the HTML and the PDF together.

It prints `VALID — n assertions, 0 errors, 0 warnings` or a numbered list of failures and exits non-zero. `--quiet` prints only the failures. A warning is not automatically noise: the first run produced 74 errors of which five were real defects and sixty-nine were the validator's own assumptions — every false positive was fixed in the validator, never by loosening the book.

Then the builder's QA checklist (print, mobile, keyboard, JavaScript disabled) is run by a human.

---

## 7. Gate G5 — red team

Two passes, both adversarial:

**Obsolete-law pass.** For every legal proposition in the book, ask: *was this true before an amendment?* If yes, the book must show the older form only as `⊘` in a wrong-answer block, with the amending instrument named.

**Bright-examinee pass.** Read only the facts and questions. Can the case be answered by pattern-matching the rule number from the title? If yes, rewrite the facts so the issue is buried in a date, a signature or a procedural gap.

---

## 8. Gate G6 — sign-off

The deployment memo is written, signed and committed with the book. It must state:

- law date and source set
- counts by level and the number of rules/provisions anchored
- results of each gate with the command or artefact that proves it
- open `⚑` items
- **what was not verified**

A memo without the last section is rejected.

---

## 8A. Content passes — how the book grows without going stale

The book was built in passes, and any later pass must follow the same shape:

| Pass | What it added | Why it was needed |
|---|---|---|
| 1 | Front matter, scope and obsolete registers, 60 L1 checks, 44 L2 cases, L3-01…16 | the base instrument |
| 2 | Corrections forced by reading the Gazette text against the draft: r.32 omitted in 2014, Explanation (viii) re-citation, *Dipti Prakash Banerjee*, four arithmetic and date slips | the draft was internally consistent and partly wrong |
| 3 | L3-17…21 on common proceedings and the sealed cover; the sealed-cover clock rows; the `Beyond the rules` block | two subjects that decide real files and were not in the book |

Rules for a new pass:

1. **Add a module, never renumber.** New cases go in a new `l3<letter>.py` and are appended. `meta.CLOCKS`, the L1 cross-references and every anchor in the shipped HTML point at ids; renumbering silently breaks them.
2. **Re-read the primary text before drafting.** Pass 2 exists because a plausible proposition (r.32 requires supply of the UPSC advice) had been repealed a decade earlier.
3. **Say which instrument you are using.** The sealed cover is executive instruction, not rule. A case that uses the OM says so in the first step and never lets the OM enlarge a power in the rules.
4. **Extend `verify.py` in the same commit.** Every new money figure and date gets an assertion; every new case gets an existence check and a citation check.
5. **Fix the index in the same pass.** Every clock row must point at a case that actually computes it; a stale cross-reference is worse than no reference.
6. **Run `validate.py` last, and read its warnings as findings.** It compares the finished HTML with the modules that generated it, so it catches what `verify.py` cannot: a case that lost a step in rendering, an index row that lost its link, an OM cited in the text but missing from the sources.

---

## 9. Definition of done

- [ ] book opens offline, prints clean, works without JavaScript for content
- [ ] every internal index link resolves
- [ ] marks reconcile everywhere
- [ ] zero superseded provisions taught as current
- [ ] `verify.py` exits 0 and its output is quoted in the memo
- [ ] `validate.py` prints `VALID` with zero errors, and every warning is either fixed or explained in the memo
- [ ] a print PDF is rendered from the shipped HTML and opens with every solution visible
- [ ] rebuild is one command, deterministic, and documented
- [ ] the roster, the register and the memo are committed alongside the book

---

## 10. Reuse for the next instrument (Pension 2021, Conduct 1964, Leave 1933)

Only three things change: the scope register, the clocks table, and the arithmetic classes. The level structure, the six-step method, the marking convention, the builder and the verifier harness are reused unchanged.

Keep one builder per instrument family under `scripts/<instrument>/`, and keep `verify.py` assertions per instrument. Never fork the house style: a reader who has used one book in the series must not have to relearn the layout in the next.
