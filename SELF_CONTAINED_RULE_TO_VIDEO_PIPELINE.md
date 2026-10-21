# SELF-CONTAINED PROMPT + PIPELINE: turn ANY government rule / service-instruction source into a verified, simple-English, Q&A video-script (one Python script inside a .md file) with Harness² Recursive Harnessing Optimization

This file is **complete on its own**. Everything the work needs is inside it, including **code-enforced anti-hallucination gates** built directly into `check_scenes.py`, an automated kit extractor in Step 1, and recursive agent harness refinement via **Harness²**.

| What | Where in this file |
|---|---|
| The prompt you paste into Claude / Agent Runner | **PART A** |
| The step-by-step method | **PART B** |
| The Harness² recursive optimization framework | **PART C** |
| The video engine | **Appendix 1** (`engine_template.py`) |
| The scene & anti-hallucination checker | **Appendix 2** (`check_scenes.py`) |
| The final .md assembler | **Appendix 3** (`build_script_md.py`) |
| The scene format specification | **Appendix 4** (`FORMAT_SPEC.md`) |
| A tiny working sample + sample ledger & source | **Appendix 5** |
| Coverage proof, practice scenes, quality gates, lessons, workflow script | **Appendices 6–10** |
| Deployment & environment matrix, failure-mode messages, troubleshooting | **Appendix 11** |

**Your first action in a new place:** create an empty working folder, then run the Step 1 extractor in Part B.

## PART A — THE MASTER PROMPT (copy everything inside the box into Claude, with your source attached)

```text
ROLE
You are building a SIMPLE-ENGLISH, QUESTION-AND-ANSWER VIDEO-SCRIPT COMPILER (one Python script inside a Markdown file) from a government rules source. The learner is a competitive-exam / departmental-exam candidate. A student character (Riya) asks one question per chapter; the teacher answers it card by card. Every chapter is an "explanation scene".

INPUTS
1. SOURCE: {{SOURCE_FILE_OR_LINK}}             (PDF / HTML / DOCX / pasted text; may mix Hindi words and English)
2. SCOPE: {{RULES_OR_PARAS_TO_COVER}}          (for example "page 1 to Rule 9", "Rules 11-13", "whole document")
3. TOOLKIT: the kit in "SELF-CONTAINED PROMPT + PIPELINE" (Appendices 1-5). Unpack it using the Step 1 extractor script — do NOT copy-paste appendices by hand and do NOT write your own engine.
4. EXTRAS: {{EXTRA_REQUIREMENTS}}
5. OUTPUT FOLDER: {{OUTPUT_FOLDER}}
6. TODAY: {{TODAY}}

NON-NEGOTIABLE RULES
R1  COMPLETENESS & VERBATIM SOURCE SUBSTRING. Nothing in the scope may be omitted: every rule, sub-rule, clause, sub-clause, proviso, explanation, note, exception, table row, form/proforma, numbered Government decision (GID/OM), threshold, date and condition must appear (card text, full text or narration). Build a LEDGER first with exact line numbers ("source_lines") and verbatim text ("source_verbatim") copied directly from the source file — never summarize the source into the ledger by memory. `check_scenes.py --ledger --source` mechanically verifies that every item's `source_verbatim` is an exact whitespace-normalized substring of the source file and that 100% of non-obsolete ledger IDs are covered.
R2  CURRENCY & TIER-1 AUTHORITY LOCK. Check every item against the LATEST OFFICIAL position. Tag each item: confirmed | changed | obsolete | unverified. You may ONLY set status to "changed" or "obsolete" when backed by a Tier-1 official government source you actually read (official domains such as dopt.gov.in, doe.gov.in, pensionersportal.gov.in, egazette.gov.in, indiacode.nic.in, cag.gov.in, cvc.gov.in, mha.gov.in, finmin.nic.in, or a full Supreme Court / High Court judgment, G.S.R., S.O., or O.M. number). `check_scenes.py` blocks status="changed" or "obsolete" if `evidence` lacks a Tier-1 marker. Secondary compilations (Swamy's/Nabhi summaries, coaching blogs, forums) are search leads ONLY; if the official Tier-1 text cannot be read, keep the printed source rule, tag the item "unverified", and state the unconfirmed lead on the card.
R3  OBSOLETE CONTENT BLOCKING (ALL ARTEFACTS). Never present superseded content, old limits, repealed OM numbers, or defunct bodies as current law in any artefact. Remove obsolete items, or mention them only inside a line explicitly prefixed with `OBSOLETE / HISTORY ONLY:` naming the replacement. Record every superseded figure, form name or acronym in the ledger's `"obsolete_tokens"` list so `check_scenes.py` blocks accidental leaks using word-boundary matching.
R4  NO INVENTION & QUOTE FIDELITY. Never invent a wording, number, date, percentage, Rupee amount, OM/G.S.R. number or case. Every non-example citation, OM number, year, percentage and Rupee figure in your cards AND narration is mechanically checked against the verified source text and Tier-1 ledger entries by `check_scenes.py --ledger --source` (for `confirmed` items, only `source_verbatim` is trusted, so typing a hallucinated figure into `current_position` or `note` will still fail). Set `"read_verbatim": true` in the ledger ONLY when you read the exact official clause text verbatim; if `"read_verbatim": false`, `check_scenes.py` blocks single-quoted clauses in FULL unless labelled `"close restatement"`. If an item is `"unverified"`, the card MUST include the exact phrase `"not confirmed against an official source"`.
R5  SIMPLE ENGLISH & DETERMINISTIC EXAMPLES. Hindi/Hinglish words become plain English. Every technical term is explained in everyday words; when asked, with a concrete real-life example (labelled "Example:", invented names are illustrative, every number recomputed and verified via Python expressions in the scene's `"calc_asserts"` list — every expression MUST evaluate to the boolean `True`).
R6  HONEST LIMITS. Anything outside the file (general knowledge, later court rulings, side notes) is labelled "general knowledge, not in the file". Source quirks (duplicate paragraph numbers, typos, mismatched headings) are kept as printed and flagged, not silently fixed.
R7  Q&A STYLE. Every chapter is ONE question asked by the student (Riya) and answered by the teacher, following the Q&A STYLE GUIDE below.

Q&A STYLE GUIDE
 - The question is what a candidate would really ask, not a topic label. Good: "Can the President exclude a group from the rules, and who settles a doubt?" Bad: "Rule 3(2) to 3(4)".
 - Question types to mix across a batch: WHAT does it say; WHAT IS THE DIFFERENCE between X and Y; WHAT HAPPENS IF; WHO DECIDES / WHO SANCTIONS; WITHIN WHAT TIME; WHEN DOES THE EXCEPTION APPLY.
 - Answer order inside the cards: (1) the rule in plain words, (2) the proviso / exception / explanation, (3) a real example, (4) the trap or look-alike term. The last card of a chapter is the "trap" or "remember" card; the hook strip is a one-line memory aid.
 - Voices: the student speaks short, curious sentences ("Sir, ..."); the teacher speaks plainly, uses "for example", and never reads a clause as a wall of text — the exact words go in the FULL text, the spoken narration explains them.
 - Openers/transitions to vary: "Let us take the rule first", "Now the exception", "Here is a real example", "Be careful, this is the trap", "Remember:".

OPTIONAL SWITCHES (default OFF; turn on only if the user asks)
 - PRACTICE_QA=on       -> add practice scenes at the end of each part (Appendix 7). Default: explanation scenes only.
 - GLOSSARY=on          -> also deliver the shared glossary (Part B, Step 12). Recommended for multi-batch jobs.
 - HARNESS_RECURSION=on -> activate Harness² recursive prompting and tool optimization (Part C) for high-complexity rules.

PIPELINE (do the steps in this order; do not skip a gate; details in Part B)
S0  Clarify only if truly ambiguous (use the question tool once: scope, format, explanation-only vs quizzes).
S1  Install the kit (Appendices 1-5) into `WORK/kit/` using the automated Step 1 extractor and run the self-test.
S2  Read the source fully. Extract it to clean text per rule/para with preserved line numbers.
S3  Decide the BATCHES (about 16-35 chapters or 4,000-10,000 source words each; split big rules into their own batch). Tell the user the number of batches first.
S4  Build the LEDGER per batch (one entry per examinable item, stable id, `"source_lines"` and exact `"source_verbatim"` extracted from the source text) and VERIFY each item online against Tier-1 official sources (prefer a real browser tool to read exact text; fetch tools only summarise, so set `"read_verbatim": false`). Save as JSON.
S5  WRITE the scenes file per batch in the exact scene format (Appendix 4), 3-5 numbered decisions per chapter, every scene tagged `"covers": [ledger ids]` and `"calc_asserts": [...]` for worked examples. (Optionally apply Harness² Task-Level Propose–Probe–Compose steps).
S6  Run the CHECKER with grounding enabled (`python3 check_scenes.py scenes_<n>.txt --ledger B<n>_verified.json --source B<n>.txt`) until PASS.
S7  Independent AUDIT by a fresh agent / fresh pass: item-by-item coverage against the source AND the ledger, fact check, recompute every worked example, check obsolete/unverified flags, fix directly, re-run the checker with `--ledger` and `--source`, and confirm `"remaining_gaps": []` in `meta_<n>.json`.
S8  ASSEMBLE the final .md with `build_script_md.py`, run its `--audit`, render `--preview`, look at 2-3 slides.
S9  CROSS-CHECKS across all batches: glossary consistency, every "see Rule X" resolved, one consolidated CHANGE LOG, an OBSOLETE-TERM SWEEP of all outputs. Update Harnessing-Level reflection cache across batches.
S10 DELIVER each .md file and a short report: what was covered, what changed versus the source, what is unverified, how to build the video locally.
For several batches, run verify -> write -> audit per batch, batches in parallel (Part B, Step 8).

SCENE FORMAT (summary; the full specification is Appendix 4 and a working sample is Appendix 5)
  scene = {id, chapter, title (one line), accent, badge, q, [intro], [lead], q_say, [flow], boxes[3-5], hook, hook_say, covers, [calc_asserts]}
  box   = (card title <=40 chars, SHORT on-screen text, FULL text (exact wording, citations), COLOUR, spoken narration)
  limits: title <= ~72 chars; badge <= 22 chars; question <= ~105 chars; hook <= ~105 chars (one line);
          SHORT text <= ~150 chars (4 cards), <= ~100 (scene with a flow diagram), <= ~110 (5 cards);
          no double quote or backslash inside any string; no arrow/emoji glyphs; numbers spoken in words in narration.

DELIVERABLES
 - One .md per batch: title, a ````python fenced script (docstring + engine + scenes), runnable as `python build_X.py --audit | --preview | --no-tts | --part N (N from PART_STARTS, or PART_STARTS = "auto") | (full build)`.
 - A short report per batch: counts (items; confirmed / changed / obsolete / unverified), what was removed, sources actually read, what could not be verified.
Placeholders to fill: {{SOURCE_FILE_OR_LINK}}, {{RULES_OR_PARAS_TO_COVER}}, {{EXTRA_REQUIREMENTS}}, {{OUTPUT_FOLDER}}, {{TODAY}}.
```

## PART B — THE PIPELINE IN DETAIL

Notation: `WORK/` = your working folder (any empty folder). `<stem>` = a short file-safe name for the batch (e.g. `rules_1_9`, `leave_rules_b1`). `<n>` = batch number.

### Step 0 — Ask only what changes the work

If the request is underspecified, ask once: scope, explanation-only vs practice questions, one file or several, special requirements (real example per technical term, latest position only). Do not ask when the request is clear.

### Step 1 — Install the kit (automated extraction + self-test)

Create `WORK/kit/` and unpack Appendices 1–5 automatically from this file using the `KIT_FILE` markers.

| Appendix | Extracted file in `WORK/kit/` | Purpose |
|---|---|---|
| 1 | `engine_template.py` | the engine |
| 2 | `check_scenes.py` | layout + mechanical anti-hallucination checker (`--ledger` / `--source`) |
| 3 | `build_script_md.py` | assembler |
| 4 | `FORMAT_SPEC.md` | format specification |
| 5 | `sample_scenes.txt`, `sample_ledger.json`, `sample_source.txt` | working sample scenes, ledger, source |

Run this one-step unpack + self-test block (replace `PIPELINE.md` with the path to this file):

```bash
mkdir -p WORK/kit && python3 - PIPELINE.md WORK/kit <<'PY'
import re, sys, pathlib

md = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
out = pathlib.Path(sys.argv[2])

# Fence-aware regex: capture the opening fence length (3 or 4 backticks) and require
# the SAME fence to close. Otherwise FORMAT_SPEC.md (which uses a 4-backtick fence
# because it contains 3-backtick blocks) would never match and be silently skipped.
KIT_RE = re.compile(
    r'<!-- KIT_FILE: (\S+) BEGIN -->\s*(`{3,4})[^\n]*\n(.*?)\n\2\s*<!-- KIT_FILE: END -->',
    re.S,
)

EXPECTED = {
    'engine_template.py', 'check_scenes.py', 'build_script_md.py',
    'FORMAT_SPEC.md', 'sample_scenes.txt', 'sample_ledger.json', 'sample_source.txt',
}

got = set()
for name, fence, body in KIT_RE.findall(md):
    (out / name).write_text(body + '\n', encoding='utf-8')
    print(f'unpacked {name}  ({len(fence)}-backtick fence)')
    got.add(name)

missing = EXPECTED - got
if missing:
    sys.exit(f'KIT EXTRACTION INCOMPLETE: missing {sorted(missing)}')
extras = got - EXPECTED
if extras:
    print(f'note: extracted extra kit files not in expected set: {sorted(extras)}')
print(f'KIT extracted: {len(got)} files (expected {len(EXPECTED)})')
PY
cd WORK/kit
python3 check_scenes.py sample_scenes.txt --ledger sample_ledger.json --source sample_source.txt   # expect: PASS: 5 scenes, 17 cards (a PART_STARTS "note:" line comes first)
echo '{"scope":"test","sources":["s"],"changes_vs_source":[],"key_facts":["k"],"not_verified":["n"],"remaining_gaps":[]}' > meta_test.json
python3 build_script_md.py sample_scenes.txt meta_test.json selftest "Self test" selftest.md
python3 - <<'PY'
import re; t=open('selftest.md',encoding='utf-8').read()
open('selftest.py','w',encoding='utf-8').write(re.search(r'````python\n(.*)\n````',t,re.S).group(1))
PY
python3 selftest.py --audit                        # expect: ALL CARDS WITHIN BUDGET
python3 selftest.py --preview                      # expect: slides written to selftest_build/slides
```

Do not edit markers or placeholders in `engine_template.py`. Edit the engine only to add pronunciation fixes to `_TTS_FIXES` (see Step 9).

Environment (Appendix 11 has the full matrix and troubleshooting):
- **Python 3.10+** — the engine checks this at start and exits with a one-line message instead of an obscure syntax error.
- **Pillow** — auto-installed if missing: plain `pip`, then `--user`, then `--break-system-packages` (PEP 668 "externally managed" Debian/Ubuntu). `check_scenes.py` uses the same fallbacks.
- **ffmpeg + ffprobe** (full video build only; `--audit` and `--preview` never call them) — if ffmpeg is missing the engine tries the `imageio-ffmpeg` wheel, which ships a static build **with libass**; if ffprobe is missing, durations and the stream check fall back to parsing `ffmpeg -i`. A static ffmpeg still needs a font on the box (DejaVu/Liberation, or the wheel's bundled fonts).
- **edge-tts + internet** (neural voices) — install failures and offline runs are reported clearly; use `--no-tts` for a silent layout/timing pass. `--tts=off` is never required: the flag is `--no-tts`.

### Step 2 — Research first, build later

Read the source completely (PDF page by page in chunks of up to 20 pages; large HTML in portions). Research official sources before reading any output-format skill or writing the deliverable. Only then write scenes.

### Step 3 — Turn the source into clean, splittable text

- PDF: `pdftotext -layout file.pdf out.txt` (keeps paragraph numbering). If scanned, view page images.
- HTML: parse with Python's `html.parser`; write headings as `#### Heading`, table cells separated by `|`, lists as `-`; drop `<script>`/`<style>`.
- Split into batch files at heading boundaries (`WORK/src/B1.txt`, `B2.txt`, ...) plus `preamble.txt` for front matter. Word counts per batch determine chapter sizing. Keep everything under `WORK/`.

### Step 4 — Choose the batches

| Source size per batch | Chapters |
|---|---|
| 4,000–8,000 words | 16–26 |
| 8,000–10,000 words | 28–35 |
| reference-heavy tail | up to ~60 (build in `--part` thirds) |

Keep one rule family together; give very long rules their own batch. Tell the user the number of batches before starting.

### Step 5 — The LEDGER and the verification pass (per batch)

Never summarise the source from memory into the ledger. Extract the exact line range and verbatim text from `WORK/src/B<n>.txt` into `"source_lines"` and `"source_verbatim"`. `check_scenes.py --source` verifies that `"source_verbatim"` is an exact whitespace-normalized substring:

```json
{
  "batch": "B1",
  "obsolete_tokens": ["any batch-wide superseded form or scale name"],
  "items": [
    {
      "id": "R4(1)",
      "ref": "Rule 4(1)",
      "source_lines": "L12-L18",
      "source_verbatim": "exact text copied from WORK/src/B1.txt lines 12-18",
      "status": "confirmed|changed|obsolete|unverified",
      "read_verbatim": true,
      "current_position": "latest official wording or restatement (single-quoted text only if read_verbatim is true)",
      "evidence": "Tier-1 official URL or OM/G.S.R. number and date",
      "obsolete_tokens": ["superseded figure or OM number to block from cards"],
      "note": "what changed / what to flag"
    }
  ]
}
```

Id scheme: `R3(2)(a)`, `R4-PROV1`, `R4-EXPL`, `GID4-7`, `LIMIT-...`, `TL-...`, `P2.4.5(iii)`.

Research & anti-hallucination rules:
- Load web search / fetch tools; if a real browser tool exists, use it to read exact official text and set `"read_verbatim": true`.
- Tier-1 lock: only the official domains listed in Part A plus full court judgments and G.S.R./S.O./O.M. numbers may flip status. Secondary compilations are leads only; keep the printed rule, mark `"status": "unverified"`, and record the unconfirmed lead.
- Closed-loop grounding for `confirmed` items: `check_scenes.py` trusts ONLY `"source_verbatim"` (locked to the source file), NOT `"current_position"` or `"note"`.
- Record every URL actually read. Save `WORK/ledger/B<n>_verified.json`.
- Prefer 150 small items to 40 lumped ones; never drop an obsolete item silently.

### Step 6 — Write the scenes

Write `WORK/scenes/scenes_<n>.txt` — exactly `SCENES = [...]`, `FLOWS = {...}`, `PART_STARTS = [...]`. Colours `RED ORANGE BLUE GREEN SKY YELLOW PINK` are engine-predefined. For `--part` builds use `PART_STARTS = "auto"` for even thirds, or name the real part-start ids (1–3); a list of just the first few scene ids is treated as a placeholder and auto-balanced.

- SHORT = screen text (plain words, one-line example); FULL = exact legal wording and citations; narration = 2–4 spoken sentences, numbers written in words (hard limit 100 words per card, 35 for `q_say`, 40 for `hook_say`, 80 for `intro`, 40 for `lead`; the engine's `--audit` enforces these).
- Worked examples: explain terms simply, give a real example, verify arithmetic via Python expressions in `"calc_asserts"` (every expression must evaluate to `True`).
- Chunking: write 4–6 scenes per chunk file, concatenate into `scenes_<n>.txt`, run checker.

### Step 7 — The CHECKER (visual budgets + mechanical anti-hallucination gates)

```bash
python3 WORK/kit/check_scenes.py WORK/scenes/scenes_<n>.txt \
    --ledger WORK/ledger/B<n>_verified.json \
    --source WORK/src/B<n>.txt
```

Mechanical gates enforced:
- Exact verbatim substring check of all `"source_verbatim"` against `--source`.
- Tier-1 evidence verification on all `changed` and `obsolete` entries.
- 100% ledger coverage and zero ghost / invented IDs in `"covers"`.
- Word-boundary obsolete-token leaks blocked from all card text and spoken lines (plural-aware: `ACR` also blocks `ACRs`; comma variants of amounts are matched).
- Mandatory `"not confirmed against an official source"` disclaimer for unverified items.
- Prohibition of single-quoted verbatim clauses for summary-only fetches (`read_verbatim: false`).
- Extraction and validation of all rule numbers, OM numbers, years, percentages, and Rupee amounts across every text field (title, chapter, badge, question, hook, intro, lead, plus every card's SHORT/FULL/narration) against the verified corpus.
- Dynamic evaluation of mathematical assertions in `"calc_asserts"` (any truthy result passes).
- `intro` allowed only on the first scene of a batch.

### Step 8 — The agent WORKFLOW (when the job has several batches)

```text
for each batch B<n> (batches in parallel):
   Stage 1  VERIFY  reads B<n>.txt + preamble, builds the verbatim-anchored ledger, researches Tier-1
                    official sources, writes B<n>_verified.json
   Stage 2  WRITE   reads B<n>.txt + B<n>_verified.json + FORMAT_SPEC.md + sample_scenes.txt,
                    writes scenes_<n>.txt, runs check_scenes.py --ledger --source to PASS
   Stage 3  AUDIT   a FRESH agent re-reads source + ledger + scenes, finds gaps/errors, fixes them,
                    re-runs check_scenes.py --ledger --source, writes meta_<n>.json (remaining_gaps: [])
return per-batch summaries
```

### Step 9 — Pronunciation, then assemble the final .md

Add custom acronyms and rule citations to `_TTS_FIXES` in `kit/engine_template.py`. Save metadata in `meta_<n>.json` with `"remaining_gaps": []`. Assemble:

```bash
python3 WORK/kit/build_script_md.py WORK/scenes/scenes_<n>.txt WORK/meta/meta_<n>.json \
    <stem> "<Title of the batch>" /mnt/outputs/build_<stem>_simple_english_video.md
```

Test assembled file with `--audit` and `--preview`.

### Step 10 — Delivery and honest reporting

Deliver .md. State coverage metrics, changes versus source, and unverified items. Report ground-truth stats from `check_scenes.py --ledger --source`.

### Step 11 — Building the actual video (run on local machine)

```bash
python build_<stem>.py --audit          # 1. card-density check
python build_<stem>.py --preview        # 2. render slides only
python build_<stem>.py --no-tts         # 3. silent dry run
python build_<stem>.py --part 1         # 4. build part 1 (1..N from PART_STARTS, or "auto")
python build_<stem>.py                  # 5. full build
```

### Step 12 — Shared GLOSSARY (one file for all batches)

```json
{"term":"probation", "plain":"a trial period before the job becomes permanent",
 "example":"Asha joins on 1 April and is on probation for two years; if her work is good she is confirmed.",
 "source_ref":"P2.1.1", "first_chapter":"c01_04", "status":"current"}
```

### Step 13 — CROSS-BATCH LINK CHECK ("see Rule X")

Scan all scene files for rule cross-references to ensure every mentioned rule is covered or explicitly flagged as external.

### Step 14 — Consolidated CHANGE LOG and OBSOLETE-TERM SWEEP

Merge all batch metadata into a unified change table and perform a final word-boundary sweep across all generated documents.

## PART C — HARNESS² RECURSIVE HARNESSING OPTIMIZATION (Optional / High-Scale Pipeline)

For large statutory rulebooks (e.g. 100+ rules, multi-volume civil service rules), manual prompt engineering and static instructions degrade across later batches. Harness² optimizes the agent system around the model across two recursive levels while keeping model weights fixed:

```
                     ┌───────────────────────────────────────────────┐
                     │          HARNESSING-LEVEL RECURSION           │
                     │  (Experience Reflector updates shared memory, │
                     │   tool guidance & prompt invariants)          │
                     └──────────────────────┬────────────────────────┘
                                            │ Updates
                                            ▼
┌───────────────────────────────────────────────────────────────────────────────────┐
│                            TASK-LEVEL RECURSION                                   │
│                                                                                   │
│    Base Batch Draft ──► [PROPOSE] ──► [PROBE] ──► [COMPOSE] ──► Verified Artifact │
│      (Stage 2 WRITE)      Edits      Parallel    Synthesize     (Audit PASS)      │
│                                      Candidates  Best Traits                      │
└───────────────────────────────────────────────────────────────────────────────────┘
```

### 1. The Eight Harness Components

Harness² modulates eight components for the compiler: System Prompt (role + personas); Guardrails (`check_scenes.py` invariants); Memory (`WORK/NOTES.md`, glossary, change log); Tool Guidance (search syntax, browser usage, safe `calc_asserts`); Subagents (separate VERIFY / WRITE / AUDIT instances); Skills (`FORMAT_SPEC.md` + grounding rules); Scripts (`build_script_md.py`, density checks); Plugins (ASS subtitles, TTS normalisation, Pillow rendering).

### 2. Task-Level Recursion: Propose–Probe–Compose

- **Propose:** Harness Editor proposes K candidate revisions to scene chunks (layout variants, alternate pedagogical breakdowns).
- **Probe:** Run candidates through `check_scenes.py --ledger --source` and `engine_template.py --audit`; record layout-density margins and token-grounding status.
- **Compose:** Merge the best-grounded, highest-readability cards that pass all mechanical checks.

### 3. Harnessing-Level Recursion: Persistent Reflection

After each batch's Stage 3 AUDIT, an Experience Reflector extracts behavioural contrasts: failures flagged by `check_scenes.py`; newly confirmed acronyms added to `_TTS_FIXES` and `glossary.json`; the resulting reflection updates `WORK/NOTES.md` and improvement prompts for subsequent batches.

### 4. CLI Execution Flags

```bash
harness2 --bench ccs-pipeline --k 2 --mode parallel --only-domains batch-3
harness2 --bench ccs-pipeline --k 2 --mode sequential --only-domains batch-3
harness2 --bench ccs-pipeline --substrate cx
```

---

## APPENDIX 1 — `engine_template.py`

<!-- KIT_FILE: engine_template.py BEGIN -->
```python
#!/usr/bin/env python3
"""__DOCSTRING__"""
import argparse
import asyncio
import re
import shutil
import subprocess
import sys
from pathlib import Path

if sys.version_info < (3, 10):
    sys.exit(f"ERROR: Python 3.10 or newer is required (this interpreter is {sys.version.split()[0]}).")


def pip_install(package: str) -> bool:
    """pip install with fallbacks, so it also works on PEP 668 'externally managed' systems
    (Debian/Ubuntu python3) where a plain pip install is refused. Returns True on success."""
    for extra in ([], ["--user"], ["--break-system-packages"]):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", *extra, package],
                                  stdout=subprocess.DEVNULL)
            return True
        except subprocess.CalledProcessError:
            continue
    return False


try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    pip_install("Pillow")
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        sys.exit("ERROR: Pillow is required to render slides.\n"
                 "  python3 -m pip install --user Pillow        (add --break-system-packages on Debian/Ubuntu)\n"
                 "  or create a virtualenv:  python3 -m venv .venv && . .venv/bin/activate && pip install Pillow")


FFMPEG = "ffmpeg"
FFPROBE = "ffprobe"


def _find_tool(name: str):
    """Locate ffmpeg/ffprobe: PATH first, then the imageio-ffmpeg wheel (ffmpeg only)."""
    found = shutil.which(name)
    if found:
        return found
    if name == "ffmpeg":
        try:
            import imageio_ffmpeg
            return imageio_ffmpeg.get_ffmpeg_exe()
        except Exception:
            return None
    return None


def require_media_tools():
    """Resolve ffmpeg (with an automatic imageio-ffmpeg fallback) and explain clearly when it is missing.
    ffprobe is optional: durations and the stream check fall back to parsing `ffmpeg -i`."""
    global FFMPEG, FFPROBE
    ff = _find_tool("ffmpeg")
    if not ff:
        print("ffmpeg not found on PATH - trying the imageio-ffmpeg wheel ...")
        if pip_install("imageio-ffmpeg"):
            ff = _find_tool("ffmpeg")
    if not ff:
        sys.exit("ERROR: ffmpeg is required for the video build (slides and --audit do not need it).\n"
                 "  Linux:   sudo apt install ffmpeg        (libass is needed to burn subtitles)\n"
                 "  macOS:   brew install ffmpeg\n"
                 "  Windows: winget install Gyan.FFmpeg  or  https://ffmpeg.org/download.html\n"
                 "  Any OS:  python3 -m pip install --user imageio-ffmpeg")
    FFMPEG = ff
    fp = _find_tool("ffprobe")
    if fp:
        FFPROBE = fp
    else:
        FFPROBE = None
        print("note: ffprobe not found - falling back to `ffmpeg -i` for durations and the stream check.")


W, H = 1920, 1080
BUILD_DIR = Path("__STEM___build")
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
OUT_STEM = "__STEM___masterclass"
OUTPUT_MP4 = Path(OUT_STEM + ".mp4")

# Density budget (px). Build fails if text needs to go below these.
BODY_START, BODY_MIN = 34, 26
TITLE_START, TITLE_MIN = 30, 22
NODE_T_MIN, NODE_S_MIN = 18, 16

BG_TOP = (10, 16, 36)
BG_BOT = (22, 30, 58)
CARD_BG = (28, 39, 62)
TEXT_WHITE = (248, 250, 252)
MUTED = (148, 163, 184)
ORANGE = (230, 159, 0)
GREEN = (0, 158, 115)
BLUE = (0, 114, 178)
SKY = (86, 180, 233)
RED = (213, 94, 0)
YELLOW = (240, 228, 66)
PINK = (204, 121, 167)

DEFAULT_TEACHER = "en-IN-PrabhatNeural"
DEFAULT_STUDENT = "en-IN-NeerjaNeural"

# Pronunciation fixes for the neural voice. Longer patterns first.
_TTS_FIXES = [
    (r'\bUPSC\b', 'U.P.S.C.'), (r'\bSSC\b', 'S.S.C.'), (r'\bCVC\b', 'C.V.C.'), (r'\bCBI\b', 'C.B.I.'),
    (r'\bDoPT\b', 'D.O.P.T.'), (r'\bDOPT\b', 'D.O.P.T.'), (r'\bDoP&AR\b', 'D.O.P. and A.R.'), (r'\bMHA\b', 'M.H.A.'),
    (r'\bOMs\b', 'O.M.s'), (r'\bOM\b', 'O.M.'), (r'\bGIDs\b', 'Government of India decisions'), (r'\bGID\b', 'Government of India decision'),
    (r'\bCCS\b', 'C.C.S.'), (r'\bCCA\b', 'C.C.A.'), (r'\bCAG\b', 'C.A.G.'), (r'C&AG', 'C.A.G.'), (r'\bGOI\b', 'G.O.I.'),
    (r'\bDPC\b', 'D.P.C.'), (r'\bAPAR\b', 'A.P.A.R.'), (r'\bACR\b', 'A.C.R.'), (r'\bACP\b', 'A.C.P.'), (r'\bMTS\b', 'M.T.S.'),
    (r'\bFR\b', 'F.R.'), (r'\bSR\b', 'S.R.'), (r'\bCPC\b', 'C.P.C.'), (r'\bRR\b', 'R.R.'), (r'\bRTI\b', 'R.T.I.'), (r'\bFCRA\b', 'F.C.R.A.'),
    (r'\bIAS\b', 'I.A.S.'), (r'\bIPS\b', 'I.P.S.'), (r'\bIFS\b', 'I.F.S.'), (r'\bLBSNAA\b', 'L.B.S.N.A.A.'), (r'\bNITI\b', 'Nitee'),
    (r'\bSC/ST\b', 'S.C. and S.T.'), (r'\bOBC\b', 'O.B.C.'), (r'\bw\.e\.f\.', 'with effect from'), (r'\bW\.E\.F\.', 'with effect from'),
    (r'\bRs\.', 'Rupees'), (r'G\.S\.R\.', 'G.S.R.'),
    # rule / paragraph references (3 levels first)
    (r'Rule\s+(\d+)\((\d+)\)\(([a-z]+)\)\(([ivx]+)\)', r'Rule \1, sub rule \2, clause \3, sub clause \4'),
    (r'Rule\s+(\d+)\((\d+)\)\(([a-z]+)\)', r'Rule \1, sub rule \2, clause \3'),
    (r'Rule\s+(\d+)\(([a-z])\)\(([ivx]+)\)', r'Rule \1, clause \2, sub clause \3'),
    (r'Rule\s+(\d+)\((\d+)\)', r'Rule \1, sub rule \2'),
    (r'Rule\s+(\d+)\(([a-z])\)', r'Rule \1, clause \2'),
    (r'Rule\s+(\d+)\s?-?([A-Z])\b(?!\()', r'Rule \1 \2'),
    (r'[Pp]ara\s+(\d+(?:\.\d+)*)\(([a-z]+)\)', r'Para \1, clause \2'),
    (r'Article\s+(\d+)\((\d)\)\(([abc])\)', r'Article \1, clause \2, proviso \3'),
    (r'Article\s+(\d+)\((\d)\)', r'Article \1, clause \2'),
    (r'\bsub-rules\b', 'sub rules'), (r'\bsub-rule\b', 'sub rule'),
    (r'[\u2014\u2013]', ','),
]


def normalize_for_tts(text: str) -> str:
    for pat, rep in _TTS_FIXES:
        text = re.sub(pat, rep, text)
    return re.sub(r'[ \t]+', ' ', text).strip()


def even_parts(n_scenes, n_parts):
    """Split n_scenes scenes into n_parts parts whose sizes differ by at most one.
    The earlier parts take the extra scene (5 scenes, 3 parts -> 2 / 2 / 1)."""
    n_parts = max(1, min(int(n_parts), n_scenes))
    base, extra = divmod(n_scenes, n_parts)
    sizes = [base + (1 if i < extra else 0) for i in range(n_parts)]
    ranges, start = [], 0
    for size in sizes:
        ranges.append((start, start + size))
        start += size
    return ranges


def resolve_parts(part_starts, scene_ids):
    """Turn PART_STARTS into (start, end) scene ranges for --part, plus a note to print.

    PART_STARTS may be:
      * "auto"      -> three parts of nearly equal size (fewer parts if the batch is tiny);
      * [] or None  -> a single part (the whole batch), so --part 1 stays valid;
      * 1-3 scene ids -> that many parts, each starting at its id, the last running to the end.

    Placeholder repair: a list that is merely the first N scene ids (c01, c02, c03) marks no
    real boundary - honouring it literally would turn --part 1 and --part 2 into single-chapter
    runs. Such a list is treated as "no boundary declared" and the batch is split into N nearly
    equal parts, with a note explaining why. Real boundaries (c01, c12, c23) are never touched.
    """
    n_scenes = len(scene_ids)
    if isinstance(part_starts, str):
        if part_starts.strip().lower() != "auto":
            sys.exit(f"PART_STARTS must be 'auto' or a list of scene ids; got {part_starts!r}")
        return even_parts(n_scenes, 3), ""
    if part_starts is None or (isinstance(part_starts, (list, tuple)) and not part_starts):
        return even_parts(n_scenes, 1), ""
    if not isinstance(part_starts, (list, tuple)):
        sys.exit(f"PART_STARTS must be 'auto' or a list of 0-3 scene ids; got {part_starts!r}")
    if len(part_starts) > 3:
        sys.exit(f"PART_STARTS must have 0-3 scene ids; got {len(part_starts)}")
    by_id = {sid: i for i, sid in enumerate(scene_ids)}
    missing = [pid for pid in part_starts if pid not in by_id]
    if missing:
        sys.exit(f"PART_STARTS ids not found in SCENES: {missing}")
    idx = [by_id[pid] for pid in part_starts]
    if idx[0] != 0:
        sys.exit(f"PART_STARTS must start with the first scene id; got index {idx[0]}")
    if any(idx[i] >= idx[i + 1] for i in range(len(idx) - 1)):
        sys.exit(f"PART_STARTS indices must be strictly increasing; got {idx}")
    if idx == list(range(len(idx))) and n_scenes > len(idx):
        n = len(idx)
        if n == 1:
            return even_parts(n_scenes, 1), (
                f"PART_STARTS names only the first scene id, which is no real part boundary; "
                f"building the whole batch as a single part instead "
                f"(use PART_STARTS = 'auto' or name the true part-start ids to override)")
        return even_parts(n_scenes, n), (
            f"PART_STARTS names only the first {n} scene ids, which is no real part boundary; "
            f"splitting the {n_scenes} scenes into {n} nearly equal parts instead "
            f"(use PART_STARTS = 'auto' or name the true part-start ids to override)")
    return [(idx[i], idx[i + 1] if i + 1 < len(idx) else n_scenes) for i in range(len(idx))], ""


# ===== SCENES_BEGIN =====
SCENES = []
FLOWS = {}
PART_STARTS = []
# ===== SCENES_END =====

assert len({s["id"] for s in SCENES}) == len(SCENES), "duplicate scene id"

FULL = {}
for _sc_ in SCENES:
    _new, _seen = [], set()
    for (_t, _short, _full, _c, _n) in _sc_["boxes"]:
        assert _t not in _seen, f"duplicate card title in {_sc_['id']}: {_t}"
        _seen.add(_t)
        FULL[(_sc_["id"], _t)] = _full
        _new.append((_t, _short, _c, _n))
    _sc_["boxes"] = _new


def write_reference_sheet():
    out = ["# __TITLE__ - full-wording reference sheet", "",
           "Every card on screen is a short key-point; the full wording / examinable facts of each card are listed here.", ""]
    for sc in SCENES:
        out += [f"## {sc['chapter']}", f"**{sc['title']}**  ({sc['badge']})", "", f"Q: {sc['q']}", ""]
        for (t, _b, _c, _n) in sc["boxes"]:
            out += [f"### {t}", FULL[(sc["id"], t)], ""]
        out += [f"> {sc['hook']}", ""]
    Path("__STEM___reference_sheet.md").write_text("\n".join(out), encoding="utf-8")


_FONT_CACHE = {}


def font(size: int, bold: bool = False):
    key = (size, bold)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    names = (["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "arialbd.ttf", "NotoSans-Bold.ttf", "SegoeUIBold.ttf"]
             if bold else
             ["DejaVuSans.ttf", "LiberationSans-Regular.ttf", "arial.ttf", "NotoSans-Regular.ttf", "segoeui.ttf"])
    f = None
    for n in names:
        try:
            f = ImageFont.truetype(n, size)
            break
        except Exception:
            continue
    if f is None:
        try:
            f = ImageFont.load_default(size)
        except TypeError:
            f = ImageFont.load_default()
    _FONT_CACHE[key] = f
    return f


def text_w(draw, s, f):
    b = draw.textbbox((0, 0), s, font=f)
    return b[2] - b[0]


def wrap_text(draw, text, f, max_w):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split(" "):
            t = f"{cur} {w}".strip()
            if text_w(draw, t, f) <= max_w:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def fit_block(draw, text, bold, max_w, max_h, start, min_size=15, spacing=1.30):
    for size in range(start, min_size - 1, -1):
        f = font(size, bold)
        lines = wrap_text(draw, text, f, max_w)
        lh = int(size * spacing)
        if len(lines) * lh <= max_h:
            return f, lines, lh, size
    raise ValueError(f"CARD TOO DENSE (needs < {min_size}px): {text[:80]!r} - shorten the on-screen text")


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def dim(c, t=0.55):
    return lerp(CARD_BG, c, t)


def background():
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(H):
        d.line([(0, y), (W, y)], fill=lerp(BG_TOP, BG_BOT, y / H))
    for x in range(40, W, 60):
        for y in range(180, 850, 60):
            d.point((x, y), fill=(34, 46, 76))
    return img, d


def draw_skyline(d, x0, y_base, accent):
    col = lerp((20, 30, 56), accent, 0.22)
    blocks = [(0, 38), (22, 62), (50, 46), (74, 80), (100, 54), (128, 70), (156, 40), (182, 58), (208, 34)]
    for dx, h in blocks:
        d.rectangle([x0 + dx, y_base - h, x0 + dx + 20, y_base], fill=col)
    d.polygon([(x0 + 74, y_base - 80), (x0 + 84, y_base - 98), (x0 + 94, y_base - 80)], fill=col)


def draw_node(d, x, y, w, h, title, sub, color, newest):
    dark_text = color in (ORANGE, SKY, YELLOW, GREEN)
    tcol = (10, 16, 36) if dark_text else TEXT_WHITE
    if newest:
        d.rounded_rectangle([x - 5, y - 5, x + w + 5, y + h + 5], radius=16, outline=YELLOW, width=3)
    d.rounded_rectangle([x, y, x + w, y + h], radius=12, fill=color, outline=TEXT_WHITE, width=2)
    f1, l1, _, _ = fit_block(d, title, True, w - 28, 34, 24, NODE_T_MIN, 1.1)
    f2, l2, _, _ = fit_block(d, sub, False, w - 28, 28, 18, NODE_S_MIN, 1.1)
    if len(l1) > 1 or len(l2) > 1:
        raise ValueError(f"Flow node text wraps (would be clipped): {title!r} / {sub!r}")
    d.text((x + 14, y + 8), l1[0], font=f1, fill=tcol)
    d.text((x + 14, y + 8 + 34), l2[0], font=f2, fill=tcol)


def draw_flow(d, flow_key, reveal):
    flow = FLOWS[flow_key]
    nodes, edges = flow["nodes"], flow["edges"]
    for (i, j, col, step) in edges:
        if step <= reveal:
            a, b = nodes[i], nodes[j]
            ax, ay = a[0] + a[2], a[1] + a[3] // 2
            bx, by = b[0], b[1] + b[3] // 2
            d.line([(ax, ay), (bx, by)], fill=col, width=5)
            d.polygon([(bx, by), (bx - 14, by - 9), (bx - 14, by + 9)], fill=col)
    for (x, y, w, h, t, s, c, step) in nodes:
        if step <= reveal:
            draw_node(d, x, y, w, h, t, s, c, newest=(step == reveal))


def card_boxes(scene):
    n = len(scene["boxes"])
    top = 290
    if "flow" in scene:
        gap = 20
        bw_ = (W - 160 - gap * (n - 1)) // n
        return [(80 + i * (bw_ + gap), 490, bw_, 300) for i in range(n)]
    if n == 4:
        return [(80, top, 860, 245), (980, top, 860, 245), (80, top + 255, 860, 245), (980, top + 255, 860, 245)]
    gap = 20
    bw_ = (W - 160 - gap * (n - 1)) // n
    return [(80 + i * (bw_ + gap), top, bw_, 480) for i in range(n)]


def render_frame(scene, qno, total, reveal, kind, out_path: Path):
    img, d = background()
    acc = scene["accent"]
    n = len(scene["boxes"])

    d.rectangle([0, 0, W, 10], fill=acc)
    d.text((80, 34), scene["chapter"], font=font(22, True), fill=ORANGE)
    f_t, l_t, _, _ = fit_block(d, scene["title"], True, 1440, 50, 40, 26, 1.1)
    d.text((80, 76), l_t[0], font=f_t, fill=TEXT_WHITE)
    bd = scene["badge"]
    fb = font(20, True)
    bw = text_w(d, bd, fb) + 50
    d.rounded_rectangle([W - 80 - bw, 45, W - 80, 95], radius=10, fill=acc)
    d.text((W - 80 - bw + 25, 59), bd, font=fb, fill=(10, 16, 36) if acc in (ORANGE, SKY, GREEN) else TEXT_WHITE)
    d.line([(80, 150), (W - 80, 150)], fill=(51, 65, 85), width=2)

    asking = kind == "question"
    bt, bb = 162, 272
    d.rounded_rectangle([80, bt, W - 80, bb], radius=18,
                        fill=lerp(CARD_BG, acc, 0.20 if asking else 0.10),
                        outline=YELLOW if asking else lerp(CARD_BG, acc, 0.5),
                        width=5 if asking else 2)

    if kind == "intro":
        # Intro slide: show a chapter intro label instead of the raw question.
        f_q, l_q, lh_q, _ = fit_block(d, f"Introduction - {scene['chapter']}", True, 1250, 92, 38, 22, 1.22)
        ty = bt + (bb - bt - len(l_q) * lh_q) // 2
        for i, ln in enumerate(l_q):
            d.text((200, ty + i * lh_q), ln, font=f_q, fill=TEXT_WHITE)
        chip, chip_col = ("CHAPTER INTRO", SKY)
    else:
        d.ellipse([100, bt + 20, 170, bt + 90], fill=acc)
        qs = f"Q{qno}"
        fq = font(30 if len(qs) < 3 else 24, True)
        d.text((135 - text_w(d, qs, fq) // 2, bt + 36), qs, font=fq, fill=(10, 16, 36) if acc in (ORANGE, SKY, GREEN) else TEXT_WHITE)
        f_q, l_q, lh_q, _ = fit_block(d, scene["q"], True, 1250, 92, 38, 22, 1.22)
        ty = bt + (bb - bt - len(l_q) * lh_q) // 2
        for i, ln in enumerate(l_q):
            d.text((200, ty + i * lh_q), ln, font=f_q, fill=TEXT_WHITE)
        chip, chip_col = (("RIYA ASKS (Student)", YELLOW) if asking else ("THE TEACHER EXPLAINS", GREEN))

    draw_skyline(d, 1560, bb - 8, acc)
    fc = font(17, True)
    cw = text_w(d, chip, fc) + 30
    d.rounded_rectangle([W - 100 - cw, bt + 10, W - 100, bt + 40], radius=14, fill=chip_col)
    d.text((W - 100 - cw + 15, bt + 14), chip, font=fc, fill=(10, 16, 36))

    if "flow" in scene:
        draw_flow(d, scene["flow"], reveal)
    boxes = card_boxes(scene)

    for i, ((bt_, body, col, _), (x, y, w, h)) in enumerate(zip(scene["boxes"], boxes)):
        if i >= reveal:
            continue
        newest = (i == reveal - 1) and kind == "answer"
        c = col if newest or kind in ("hook",) else dim(col, 0.8)
        if newest:
            d.rounded_rectangle([x - 6, y - 6, x + w + 6, y + h + 6], radius=20, outline=YELLOW, width=4)
        d.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=CARD_BG, outline=c, width=3 if newest else 2)
        d.rectangle([x, y + 8, x + 12, y + h - 8], fill=c)
        f_bt, l_bt, lh_bt, _ = fit_block(d, bt_, True, w - 60, 62, TITLE_START, TITLE_MIN, 1.15)
        for k, ln in enumerate(l_bt):
            d.text((x + 32, y + 16 + k * lh_bt), ln, font=f_bt, fill=c)
        body_top = y + 16 + len(l_bt) * lh_bt + 10
        f_b, l_b, lh_b, _ = fit_block(d, body, False, w - 60, y + h - body_top - 14, BODY_START, BODY_MIN, 1.25)
        for k, ln in enumerate(l_b):
            d.text((x + 32, body_top + k * lh_b), ln, font=f_b, fill=TEXT_WHITE)

    if kind == "hook":
        d.rounded_rectangle([80, 796, W - 80, 846], radius=12, fill=YELLOW)
        f_h, l_h, _, _ = fit_block(d, scene["hook"], True, W - 200, 36, 24, 20, 1.1)
        if len(l_h) > 1:
            raise ValueError(f"Hook strip wraps (shorten): {scene['hook']!r}")
        d.text((100, 807), l_h[0], font=f_h, fill=(10, 16, 36))

    d.rectangle([0, 855, W, 1070], fill=(7, 11, 24))
    d.line([(80, 855), (W - 80, 855)], fill=(30, 41, 59), width=2)
    d.rectangle([0, 1068, W, H], fill=(20, 28, 50))
    seg_w = W / total
    d.rectangle([0, 1068, int(seg_w * (qno - 1) + seg_w * min(1.0, (reveal + (1 if kind == "hook" else 0)) / (n + 1))), H], fill=ORANGE)
    for k in range(1, total):
        d.line([(int(seg_w * k), 1068), (int(seg_w * k), H)], fill=(7, 11, 24), width=2)
    img.save(out_path)


def audit_density():
    img, d = background()
    bad = 0
    print(f"{'scene':26s} {'card':36s} title body  chars")
    for sc in SCENES:
        for (t, body, _c, _n), (x, y, w, h) in zip(sc["boxes"], card_boxes(sc)):
            try:
                _, l_bt, lh_bt, ts = fit_block(d, t, True, w - 60, 62, TITLE_START, TITLE_MIN, 1.15)
                body_top = y + 16 + len(l_bt) * lh_bt + 10
                _, _, _, bs = fit_block(d, body, False, w - 60, y + h - body_top - 14, BODY_START, BODY_MIN, 1.25)
                flag = "" if bs >= 28 else "  (tight)"
                print(f"{sc['id'][:26]:26s} {t[:36]:36s} {ts:>4d} {bs:>4d}  {len(body):>4d}{flag}")
            except ValueError as e:
                bad += 1
                print(f"{sc['id'][:26]:26s} {t[:36]:36s}  FAIL  {e}")
        try:
            _, l_h, _, hs = fit_block(d, sc["hook"], True, W - 200, 36, 24, 20, 1.1)
            if len(l_h) > 1:
                raise ValueError("hook wraps")
        except ValueError:
            bad += 1
            print(f"{sc['id']}: HOOK does not fit on one line at >=20px ({len(sc['hook'])} chars)")

        # Narration length: fail-fast so over-long run-ons surface in --audit, not in audio.
        for key, mx in (('q_say', 35), ('hook_say', 40), ('intro', 80), ('lead', 40)):
            if key in sc:
                wc = len(sc[key].split())
                if wc > mx:
                    bad += 1
                    print(f"{sc['id']}: NARRATION FAIL - {key} is {wc} words (max {mx})")
        for (t, _sh, _c, nar) in sc["boxes"]:
            wc = len(nar.split())
            if wc > 100:
                bad += 1
                print(f"{sc['id']}: NARRATION FAIL - card '{t[:36]}' is {wc} words (max 100)")

    print(f"\n{'ALL CARDS WITHIN BUDGET' if not bad else str(bad) + ' ITEM(S) OVER BUDGET'}")
    return bad


def build_segments(scene):
    n = len(scene["boxes"])
    segs = []
    if scene.get("intro"):
        segs.append(("teacher", scene["intro"], 0, "intro"))
    segs.append(("student", scene["q_say"], 0, "question"))
    if scene.get("lead"):
        segs.append(("teacher", scene["lead"], 0, "lead"))
    for i, b in enumerate(scene["boxes"]):
        segs.append(("teacher", b[3], i + 1, "answer"))
    segs.append(("teacher", scene["hook_say"], n, "hook"))
    return segs


def _duration_from_ffmpeg(path: Path) -> float:
    """ffprobe-free duration: parse the 'Duration: h:mm:ss.xx' line that ffmpeg -i prints on stderr."""
    err = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", err)
    if not m:
        raise RuntimeError(f"cannot read the duration of {path} (ffprobe missing and ffmpeg printed none)")
    h, mnt, s = m.groups()
    return int(h) * 3600 + int(mnt) * 60 + float(s)


def probe_duration(path: Path) -> float:
    if not FFPROBE:
        return _duration_from_ffmpeg(path)
    out = subprocess.check_output(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        text=True).strip()
    return float(out)


def stream_info(path: Path):
    """ffprobe stream listing, or the same information parsed out of `ffmpeg -i` when ffprobe is absent."""
    if FFPROBE:
        return subprocess.check_output([FFPROBE, "-v", "error", "-show_entries", "stream=codec_type,width,height",
                                        "-of", "csv=p=0", str(path)], text=True).split()
    err = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    info = []
    for line in err.splitlines():
        line = line.strip()
        if " Video: " in line:
            m = re.search(r"(\d{2,5})x(\d{2,5})", line)
            info.append(f"video,{m.group(1)},{m.group(2)}" if m else "video,,")
        elif " Audio: " in line:
            info.append("audio,,")
    return info


def silent_audio(text: str, out: Path) -> float:
    dur = max(1.5, len(text.split()) / 2.6)
    subprocess.run([FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", f"{dur:.2f}",
                    "-c:a", "libmp3lame", str(out)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return dur


async def tts_segment(text, voice, out: Path, rate, sem):
    import edge_tts
    text = normalize_for_tts(text)
    async with sem:
        last = None
        for attempt in range(4):
            try:
                try:
                    com = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
                except TypeError:
                    com = edge_tts.Communicate(text, voice, rate=rate)
                words = []
                with open(out, "wb") as f:
                    async for ch in com.stream():
                        if ch["type"] == "audio":
                            f.write(ch["data"])
                        elif ch["type"] == "WordBoundary":
                            s = ch["offset"] / 1e7
                            words.append((ch["text"], s, s + ch["duration"] / 1e7))
                if out.stat().st_size < 500:
                    raise RuntimeError("empty audio returned")
                return words
            except Exception as e:
                last = e
                await asyncio.sleep(1.5 * (attempt + 1))
        raise RuntimeError(f"edge-tts failed for segment {out.name}: {last}")


def fmt_ass(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def write_ass(cues, path: Path):
    head = (
        "[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, "
        "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
        "MarginR, MarginV, Encoding\n"
        "Style: Default,DejaVu Sans,38,&H00FFFFFF,&H0000E6FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,160,160,70,1\n"
        "Style: Student,DejaVu Sans,38,&H0042E4F0,&H0000E6FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,160,160,70,1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"
    )
    lines = [head]
    for s, e, style, txt in cues:
        lines.append(f"Dialogue: 0,{fmt_ass(s)},{fmt_ass(e)},{style},,0,0,0,,{txt}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def make_cues(words, offset, style, chunk=8):
    """Group words into cues by count OR by accumulated character length.
    Breaking only on periods caused one-word cues on abbreviations like 'No.' - use length instead."""
    cues, buf, chars = [], [], 0
    for w in words:
        buf.append(w)
        chars += len(w[0]) + 1
        if len(buf) >= chunk or chars >= 60:
            cues.append((offset + buf[0][1], offset + buf[-1][2] + 0.12, style, " ".join(x[0] for x in buf)))
            buf, chars = [], 0
    if buf:
        cues.append((offset + buf[0][1], offset + buf[-1][2] + 0.15, style, " ".join(x[0] for x in buf)))
    return cues


def even_words(text, dur):
    toks = text.split()
    step = dur / max(len(toks), 1)
    return [(t, i * step, (i + 1) * step) for i, t in enumerate(toks)]


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true", help="print card-density table and exit (no ffmpeg needed)")
    ap.add_argument("--preview", action="store_true", help="render slides only")
    ap.add_argument("--no-tts", action="store_true", help="silent audio (offline layout/timing test)")
    ap.add_argument("--teacher", default=DEFAULT_TEACHER)
    ap.add_argument("--student", default=DEFAULT_STUDENT)
    ap.add_argument("--rate", default="-4%")
    ap.add_argument("--part", type=int, help="build one part only: 1..N, where N comes from PART_STARTS (or PART_STARTS = 'auto')")
    args = ap.parse_args()

    if args.audit:
        sys.exit(1 if audit_density() else 0)
    write_reference_sheet()
    if audit_density():
        sys.exit("Build stopped: fix the over-dense cards or over-long narration listed above.")

    for d in (BUILD_DIR, SLIDES_DIR, AUDIO_DIR):
        d.mkdir(parents=True, exist_ok=True)
    global SCENES, OUTPUT_MP4
    if args.part:
        ranges, note = resolve_parts(PART_STARTS, [x["id"] for x in SCENES])
        n_parts = len(ranges)
        if not (1 <= args.part <= n_parts):
            plural = "part" if n_parts == 1 else "parts"
            sys.exit(f"--part {args.part} is invalid: the batch is split into {n_parts} {plural} (valid range: 1..{n_parts})")
        if note:
            print(f"note: {note}")
        _a, _b = ranges[args.part - 1]
        SCENES = SCENES[_a:_b]
        OUTPUT_MP4 = Path(f"{OUT_STEM}_part{args.part}.mp4")
    total = len(SCENES)

    print(f"=== Step 1: rendering slides for {total} Q&A scenes ===")
    jobs = []
    for si, sc in enumerate(SCENES):
        for gi, (who, text, reveal, kind) in enumerate(build_segments(sc)):
            sp = SLIDES_DIR / f"{sc['id']}_{gi:02d}_{kind}.png"
            render_frame(sc, si + 1, total, reveal, kind, sp)
            jobs.append((si, who, text, kind, reveal, sp, AUDIO_DIR / f"{sc['id']}_{gi:02d}.mp3"))
        print(f"  scene {si+1:02d}/{total}  {sc['id']}")
    if args.preview:
        print(f"Preview done: {SLIDES_DIR.resolve()}")
        return

    require_media_tools()

    print(f"\n=== Step 2: narration ({'SILENT TEST' if args.no_tts else args.student + ' / ' + args.teacher}) ===")
    words_by_job = {}
    if not args.no_tts:
        try:
            import edge_tts  # noqa: F401
        except ImportError:
            if not pip_install("edge-tts"):
                sys.exit("ERROR: edge-tts could not be installed.\n"
                         "  python3 -m pip install --user edge-tts   (it also needs internet access)\n"
                         "  Offline? build with --no-tts for a silent timing/layout pass.")
        sem = asyncio.Semaphore(4)
        tasks = [tts_segment(t, args.student if who == "student" else args.teacher, mp3, args.rate, sem)
                 for (_, who, t, _, _, _, mp3) in jobs]
        results = await asyncio.gather(*tasks)
        for i, w in enumerate(results):
            words_by_job[i] = w

    print("\n=== Step 3: building clips ===")
    clips, cues, cursor = [], [], 0.0
    for i, (si, who, text, kind, reveal, sp, mp3) in enumerate(jobs):
        if args.no_tts:
            sd = silent_audio(text, mp3)
            words = even_words(normalize_for_tts(text), sd)
        else:
            sd = probe_duration(mp3)
            words = words_by_job[i] or even_words(text, sd)
        dur = sd + (0.9 if kind in ("question", "hook") else 0.5)
        clip = BUILD_DIR / f"clip_{i:03d}.mp4"
        subprocess.run([
            FFMPEG, "-y", "-loop", "1", "-framerate", "5", "-i", str(sp), "-i", str(mp3),
            "-af", "apad", "-t", f"{dur:.3f}",
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-g", "60", "-r", "30", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(clip)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cues += make_cues(words, cursor, "Student" if who == "student" else "Default")
        clips.append(clip)
        cursor += dur
    print(f"  {len(clips)} clips | timeline {cursor/60:.2f} min")

    print("\n=== Step 4: concat + burn subtitles ===")
    concat = BUILD_DIR / "concat.txt"
    concat.write_text("\n".join(f"file '{c.name}'" for c in clips) + "\n", encoding="utf-8")
    raw = BUILD_DIR / "raw_concat.mp4"
    subprocess.run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(raw)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ass = BUILD_DIR / "subtitles.ass"
    write_ass(cues, ass)
    ass_esc = str(ass).replace("\\", "/").replace(":", "\\:")
    subprocess.run([
        FFMPEG, "-y", "-i", str(raw), "-vf", f"subtitles='{ass_esc}'",
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(OUTPUT_MP4)], check=True,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    dur = probe_duration(OUTPUT_MP4)
    info = stream_info(OUTPUT_MP4)
    print("\n=== Step 5: verification ===")
    print("streams:", info)
    print(f"DONE: {OUTPUT_MP4.resolve()}  |  {dur/60:.2f} min  |  {OUTPUT_MP4.stat().st_size/1048576:.1f} MB")
    if not any(s.startswith("audio") for s in info):
        print("WARNING: no audio stream found!")


if __name__ == "__main__":
    asyncio.run(main())
```
<!-- KIT_FILE: END -->

## APPENDIX 2 — `check_scenes.py`

<!-- KIT_FILE: check_scenes.py BEGIN -->
```python
#!/usr/bin/env python3
"""Usage: python3 check_scenes.py <scenes_file> [--ledger <B_verified.json>] [--source <B.txt>]
<scenes_file> holds: SCENES = [ ... ]  FLOWS = {...}  PART_STARTS = [...]   (see FORMAT_SPEC.md).
Needs engine_template.py in the same folder. Enforces visual layout budgets AND mechanical anti-hallucination gates.
calc_asserts: any expression that evaluates to a truthy value passes (typically `True`)."""
import sys, os, re, json, math, datetime, argparse, subprocess, tempfile, shutil
from fractions import Fraction
D = os.path.dirname(os.path.abspath(__file__))
BEGIN, END = '# ===== SCENES_BEGIN =====', '# ===== SCENES_END ====='

# Tier-1 markers: specific official government domains + official legal instruments.
# Deliberately does NOT include bare '.gov.in' / '.nic.in' / 'gazette' (too broad - a coaching
# blog hosted on a government subdomain would slip through; a blog that merely says "gazette"
# would too). 'gazette of india' is kept because it names the official publication.
TIER1_MARKERS = (
    'dopt.gov.in', 'doe.gov.in', 'pensionersportal.gov.in', 'egazette.gov.in', 'indiacode.nic.in',
    'cag.gov.in', 'cvc.gov.in', 'mha.gov.in', 'finmin.nic.in', 'persmin.gov.in',
    'supreme court', 'high court',
    'g.s.r.', 's.o.', 'o.m. no', 'om no', 'gazette of india',
)


def combine(scenes_text, stem='check', title='check', doc='check'):
    t = open(os.path.join(D, 'engine_template.py'), encoding='utf-8').read()
    a, b = t.index(BEGIN), t.index(END) + len(END)
    t = t[:a] + scenes_text + '\n' + t[b:]
    return t.replace('__STEM__', stem).replace('__TITLE__', title).replace('__DOCSTRING__', doc)


def norm_ws(s):
    return re.sub(r'\s+', ' ', s).strip()


def norm_num_token(s):
    return norm_ws(s).lower().replace(',', '')


def _obsolete_leaks(tok, line):
    """Word-boundary obsolete-token match that also catches plurals and comma variants.
    - 'ACR' must also match 'ACRs'
    - 'Rs. 3500' must also match 'Rs. 3,500' and 'Rs. 3,500s'
    The plain word-boundary alone misses both (the 's' suffix and the comma variant)."""
    if not tok:
        return False
    variants = {tok, tok + 's'}
    variants = {v.replace(',', '') for v in variants} | variants
    line_nc = line.replace(',', '')
    for v in variants:
        pat = r'(?<!\w)' + re.escape(v) + r'(?!\w)'
        if re.search(pat, line, re.I) or re.search(pat, line_nc, re.I):
            return True
    return False


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('scenes_file')
    ap.add_argument('--ledger', help='path to B<n>_verified.json for mechanical grounding checks')
    ap.add_argument('--source', help='path to WORK/src/B<n>.txt for verbatim and token grounding checks')
    args = ap.parse_args()

    sc_raw = open(args.scenes_file, encoding='utf-8').read()
    code = combine(sc_raw)
    tmp = tempfile.mkdtemp(); p = os.path.join(tmp, 'm.py'); open(p, 'w', encoding='utf-8').write(code)
    try:
        compile(code, p, 'exec')
    except SyntaxError as e:
        # Report the line number in the SCENE file, not the combined file.
        engine_src = open(os.path.join(D, 'engine_template.py'), encoding='utf-8').read()
        scenes_start = engine_src[:engine_src.index(BEGIN)].count('\n') + 1
        scenes_line = (e.lineno or 0) - scenes_start + 1 if e.lineno else 0
        shutil.rmtree(tmp, ignore_errors=True)
        if scenes_line > 0:
            print(f'SYNTAX ERROR (scenes file line {scenes_line}): {e.msg}')
        else:
            print(f'SYNTAX ERROR (engine template, combined line {e.lineno}): {e.msg}')
        sys.exit(1)
    r = subprocess.run([sys.executable, p, '--audit'], cwd=tmp, capture_output=True, text=True)
    out = r.stdout + r.stderr
    errs = [l for l in out.split('\n') if any(k in l for k in ('FAIL', 'HOOK', 'Error', 'Traceback', 'duplicate', 'NARRATION'))]
    ns = {'__name__': 'chk'}
    exec(code.split('async def main')[0], ns)
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        # Same fallbacks as the engine: plain, --user, then --break-system-packages (PEP 668).
        ok = False
        for extra in ([], ['--user'], ['--break-system-packages']):
            if subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', *extra, 'Pillow']).returncode == 0:
                ok = True
                break
        if not ok:
            print("FAIL\n - Pillow is required: python3 -m pip install --user Pillow (add --break-system-packages on Debian/Ubuntu)")
            sys.exit(1)
        from PIL import Image, ImageDraw
    d = ImageDraw.Draw(Image.new('RGB', (10, 10))); fb = ns['fit_block']
    ids = []
    id_set = set()
    safe_eval_ns = {
        'datetime': datetime, 'math': math, 'Fraction': Fraction,
        'round': round, 'min': min, 'max': max, 'abs': abs, 'sum': sum,
        'len': len, 'str': str, 'int': int, 'float': float, 'bool': bool,
        'tuple': tuple, 'list': list, 'set': set, 'dict': dict,
        'range': range, 'sorted': sorted, 'any': any, 'all': all, 'zip': zip,
    }

    for s in ns['SCENES']:
        sid = s.get('id', '?')
        if sid in id_set: errs.append(f'{sid}: duplicate scene id')
        id_set.add(sid); ids.append(sid)
        for k in ('id', 'chapter', 'title', 'accent', 'badge', 'q', 'q_say', 'boxes', 'hook', 'hook_say'):
            if k not in s: errs.append(f'{sid}: missing key {k}')
        if not 1 <= len(s['boxes']) <= 5: errs.append(f'{sid}: needs 1-5 cards, has {len(s["boxes"])}')
        try:
            _, l, _, _ = fb(d, s['title'], True, 1440, 50, 40, 26, 1.1)
            if len(l) != 1: errs.append(f'{sid}: TITLE wraps ({len(s["title"])} chars) - shorten')
        except ValueError: errs.append(f'{sid}: TITLE too long ({len(s["title"])} chars)')
        try: fb(d, s['q'], True, 1250, 92, 38, 22, 1.22)
        except ValueError: errs.append(f'{sid}: QUESTION too long ({len(s["q"])} chars)')
        if ns['text_w'](d, s['badge'], ns['font'](20, True)) + 50 > 420: errs.append(f'{sid}: BADGE too wide: {s["badge"]}')
        if len(s['chapter']) > 95: errs.append(f'{sid}: CHAPTER line too long ({len(s["chapter"])} chars)')
        if 'flow' in s and s['flow'] not in ns['FLOWS']: errs.append(f'{sid}: unknown flow key {s["flow"]}')
        for (t, short, c, nar) in s['boxes']:
            full_txt = ns['FULL'][(sid, t)]
            for lab, x in (('narration', nar), ('short text', short)):
                if '"' in x or '\\' in x: errs.append(f'{sid}: {lab} of card "{t}" has a double quote or backslash')
            if ('EXAMPLE' in t.upper() or 'Example:' in short or 'Example:' in full_txt or 'Example:' in nar):
                # Include narration: worked arithmetic is naturally spoken, not printed on the card.
                num_src = re.sub(r'\b(?:Rule|Para|Article)\s+\d+', '', ' '.join([short, full_txt, nar]))
                ex_nums = re.findall(r'\b\d+\b', num_src)
                if ex_nums and not s.get('calc_asserts'):
                    errs.append(f'{sid}: card "{t}" has a numeric example but scene has no "calc_asserts" (use ["NO_MATH"] if no arithmetic/date step)')
        for expr in s.get('calc_asserts', []):
            if expr == 'NO_MATH': continue
            try:
                if not eval(expr, {'__builtins__': {}}, safe_eval_ns):
                    errs.append(f'{sid}: calc_asserts failed (evaluated falsy): {expr!r}')
            except Exception as ex:
                errs.append(f'{sid}: calc_asserts error in {expr!r}: {ex}')
        for lab in ('q_say', 'hook_say', 'intro', 'lead'):
            x = s.get(lab, '')
            if '"' in x or '\\' in x: errs.append(f'{sid}: {lab} has a double quote or backslash')
        if any(ch in s['hook'] + s['title'] + ''.join(b[1] for b in s['boxes']) for ch in '→←↔✓✔✅⚠'):
            errs.append(f'{sid}: contains an arrow/emoji glyph the font cannot draw')

    # "intro" is only allowed on the first scene of a batch (FORMAT_SPEC.md).
    for i, s in enumerate(ns['SCENES']):
        if 'intro' in s and i != 0:
            errs.append(f"{s['id']}: 'intro' is only allowed on the first scene of a batch")

    ps = ns.get('PART_STARTS', [])
    if isinstance(ps, str):
        if ps.strip().lower() != 'auto':
            errs.append(f'PART_STARTS must be "auto" or a list of 0-3 scene ids; got {ps!r}')
        elif not ns['SCENES']:
            errs.append('PART_STARTS = "auto" needs at least one scene')
    elif not isinstance(ps, (list, tuple)) or len(ps) > 3:
        errs.append(f'PART_STARTS must be "auto" or a list of 0-3 scene ids; got {ps!r}')
    elif not ps:
        pass  # [] means one part: the whole batch
    elif any(pid not in id_set for pid in ps):
        errs.append(f'PART_STARTS refers to unknown ids: {ps!r}')
    else:
        p_idx = [ids.index(pid) for pid in ps]
        if p_idx[0] != 0:
            errs.append(f'PART_STARTS must start at scene index 0; got {p_idx}')
        elif any(p_idx[i] >= p_idx[i+1] for i in range(len(p_idx)-1)):
            errs.append(f'PART_STARTS indices must be strictly increasing; got {p_idx}')
    # --part must always produce non-empty, gap-free, in-order parts (auto or explicit alike).
    try:
        _ranges, _note = ns['resolve_parts'](ps, ids)
        if not _ranges or _ranges[0][0] != 0 or _ranges[-1][1] != len(ids) or any(a >= b for a, b in _ranges):
            errs.append(f'PART_STARTS produces empty or non-covering parts: {_ranges}')
        elif _note:
            print(f'note: {_note}')
    except SystemExit as ex:
        errs.append(f'PART_STARTS invalid: {ex}')

    for s in ns['SCENES']:
        for (t, body, c, n), (x, y, w, h) in zip(s['boxes'], ns['card_boxes'](s)):
            try:
                _, l_bt, lh_bt, _ = fb(d, t, True, w - 60, 62, ns['TITLE_START'], ns['TITLE_MIN'], 1.15)
                body_top = y + 16 + len(l_bt) * lh_bt + 10
                f, lines, _, _ = fb(d, body, False, w - 60, y + h - body_top - 14, ns['BODY_START'], ns['BODY_MIN'], 1.25)
                for ln in lines:
                    if ns['text_w'](d, ln, f) > w - 59: errs.append(f'{s["id"]}: a word is wider than card "{t}": {ln}')
            except ValueError: pass

    if args.ledger:
        raw_ledger = json.load(open(args.ledger, encoding='utf-8'))
        items = raw_ledger['items'] if isinstance(raw_ledger, dict) and 'items' in raw_ledger else raw_ledger
        by_id = {it['id']: it for it in items}
        obs_tokens = set(raw_ledger.get('obsolete_tokens', []) if isinstance(raw_ledger, dict) else [])
        src_raw = open(args.source, encoding='utf-8').read() if args.source else ''
        src_norm = norm_ws(src_raw).lower()
        grounded_chunks = [src_raw] if src_raw else []

        for it in items:
            lid = it['id']
            st = it.get('status', '')
            sv = it.get('source_verbatim', '')
            ev = it.get('evidence', '')
            if st not in ('confirmed', 'changed', 'obsolete', 'unverified'):
                errs.append(f'LEDGER {lid}: invalid status {st!r}')
            if not sv:
                errs.append(f'LEDGER {lid}: missing source_verbatim (never summarize without verbatim source text)')
            elif src_norm and norm_ws(sv).lower() not in src_norm:
                errs.append(f'LEDGER {lid}: source_verbatim is not an exact substring of --source file')
            else:
                grounded_chunks.append(sv); grounded_chunks.append(it.get('ref', ''))
            if st in ('changed', 'obsolete'):
                if not ev or not any(m in ev.lower() for m in TIER1_MARKERS):
                    errs.append(f'LEDGER {lid}: status={st} requires Tier-1 official source/OM/G.S.R. in evidence; got {ev!r}')
                else:
                    grounded_chunks.append(it.get('current_position', '')); grounded_chunks.append(ev)
                # Changed items ALSO carry obsolete_tokens: a changed item is "old X -> new Y";
                # the old value is still superseded and must be blocked from every card.
                obs_tokens.update(it.get('obsolete_tokens', []))
            elif st == 'unverified':
                grounded_chunks.append(it.get('current_position', '')); grounded_chunks.append(ev); grounded_chunks.append(it.get('note', ''))

        covered_ids = set()
        META_TAGS = {'MAP', 'RECAP', 'PRACTICE'}
        for s in ns['SCENES']:
            sid = s['id']
            sc_covers = s.get('covers', [])
            if not sc_covers:
                errs.append(f'{sid}: missing or empty "covers" list')
            for cid in sc_covers:
                covered_ids.add(cid)
                if cid not in META_TAGS and cid not in by_id:
                    errs.append(f'{sid}: covers unknown ledger id "{cid}" (invented id)')
                elif cid in by_id:
                    st = by_id[cid].get('status')
                    all_card_txt = ' '.join(b[1] + ' ' + ns['FULL'][(sid, b[0])] for b in s['boxes'])
                    if st == 'obsolete' and 'OBSOLETE / HISTORY ONLY' not in all_card_txt:
                        errs.append(f'{sid}: covers obsolete ledger item "{cid}" without "OBSOLETE / HISTORY ONLY" label')
                    if st == 'unverified' and 'not confirmed against an official source' not in all_card_txt.lower():
                        errs.append(f'{sid}: covers unverified item "{cid}" without "not confirmed against an official source" on a card')
                    if by_id[cid].get('read_verbatim') is False:
                        for (t, _sh, _c, _nar) in s['boxes']:
                            ft = ns['FULL'][(sid, t)]
                            if re.search(r"'[^']{12,}'", ft) and 'close restatement' not in ft.lower():
                                errs.append(f'{sid}: card "{t}" quotes text in single quotes for "{cid}" (read_verbatim=false) without "close restatement"')

            if obs_tokens:
                chunks = [s['title'], s['chapter'], s['badge'], s['q'], s['q_say'], s['hook'], s['hook_say'],
                          s.get('intro', ''), s.get('lead', '')]
                for (t, sh, _c, nar) in s['boxes']:
                    chunks.extend([t, sh, ns['FULL'][(sid, t)], nar])
                for ch_txt in chunks:
                    for line in ch_txt.split('\n'):
                        if 'OBSOLETE / HISTORY ONLY' in line:
                            continue
                        for tok in obs_tokens:
                            if _obsolete_leaks(tok, line):
                                errs.append(f'{sid}: obsolete token {tok!r} leaked outside an "OBSOLETE / HISTORY ONLY" line')

        for it in items:
            if it.get('status') != 'obsolete' and it['id'] not in covered_ids:
                errs.append(f'LEDGER {it["id"]} ({it.get("ref", "")}): non-obsolete item not covered by any scene')

        corpus_norm = norm_num_token(' '.join(grounded_chunks))
        # NOTE: O.M. numbers may contain internal dots - allow dot inside the tail.
        TOKEN_PATS = [
            r'\b(?:Rule|Para|Article)\s+\d+[A-Z]?(?:\([^)]+\))*',
            r'\b(?:G\.S\.R\.|S\.O\.)\s*\d+[A-Z]*(?:\([A-Z]+\))?',
            r'\bO\.?M\.?\s*No\.?\s*[\w/\-.()]+',
            r'\b(?:19\d\d|20\d\d)\b',
            r'\b\d+(?:\.\d+)?\s*%',
            r'\bRs\.?\s*[\d,]+',
        ]
        for s in ns['SCENES']:
            sid = s['id']
            # Card SHORT/FULL/narration: skip worked-example cards (their figures are verified via calc_asserts).
            for (t, sh, _c, nar) in s['boxes']:
                if 'EXAMPLE' in t.upper():
                    continue
                for txt_block in (sh, ns['FULL'][(sid, t)], nar):
                    for line in txt_block.split('\n'):
                        if line.strip().lower().startswith(('example:', 'example (')):
                            continue
                        for pat in TOKEN_PATS:
                            for m in re.finditer(pat, line):
                                tok = norm_num_token(m.group(0))
                                if tok not in corpus_norm:
                                    errs.append(f'{sid}: card "{t}" has ungrounded token "{m.group(0)}" not found in verified ledger or source')
            # Extended scan: title, chapter, badge, question, hook, intro, lead must be grounded too.
            # Hallucinated OM / G.S.R. / year / percentage in these fields used to slip through.
            for lab in ('title', 'chapter', 'badge', 'q', 'q_say', 'hook', 'hook_say', 'intro', 'lead'):
                lab_text = s.get(lab, '') or ''
                for line in lab_text.split('\n'):
                    if line.strip().lower().startswith(('example:', 'example (')):
                        continue
                    for pat in TOKEN_PATS:
                        for m in re.finditer(pat, line):
                            tok = norm_num_token(m.group(0))
                            if tok not in corpus_norm:
                                errs.append(f'{sid}: {lab} has ungrounded token "{m.group(0)}" not found in verified ledger or source')

    shutil.rmtree(tmp, ignore_errors=True)
    if errs:
        print('FAIL'); [print(' -', e) for e in errs]; sys.exit(1)
    print('PASS:', len(ns['SCENES']), 'scenes,', sum(len(s['boxes']) for s in ns['SCENES']), 'cards')
```
<!-- KIT_FILE: END -->

## APPENDIX 3 — `build_script_md.py`

<!-- KIT_FILE: build_script_md.py BEGIN -->
```python
#!/usr/bin/env python3
"""Usage: python3 build_script_md.py <scenes_file> <meta.json> <stem> "<Title>" <out.md>
meta.json: {"scope": "...", "sources": ["..."], "changes_vs_source": ["..."], "key_facts": ["..."], "not_verified": ["..."], "remaining_gaps": []}
Builds the final .md (title + python fence with docstring, engine, scenes) from engine_template.py; compiles it as a check."""
import sys, os, json
D = os.path.dirname(os.path.abspath(__file__))
from check_scenes import combine

def esc(s):
    """Escape characters that would break the triple-quoted docstring."""
    return str(s).replace('\\', '/').replace('"""', "'''")

def esc_md(s):
    """Escape characters that would break the outer Markdown heading line.
    The heading line cannot contain newlines or backticks (they'd break Markdown)."""
    return str(s).replace('\n', ' ').replace('\r', '').replace('`', "'")

scenes = open(sys.argv[1], encoding='utf-8').read(); meta = json.load(open(sys.argv[2], encoding='utf-8'))
for req_k in ("scope", "sources", "changes_vs_source", "key_facts", "not_verified"):
    if req_k not in meta: sys.exit(f"ERROR: meta.json missing required key {req_k!r}")
if "remaining_gaps" not in meta:
    sys.exit('ERROR: meta.json must contain "remaining_gaps": [] (write [] when there are none)')
if meta.get("remaining_gaps"):
    sys.exit(f"ERROR: meta.json has unresolved remaining_gaps: {meta['remaining_gaps']}")
stem, title, out = sys.argv[3], sys.argv[4], sys.argv[5]
probe_code = combine(scenes, stem=stem, title=esc(title), doc='probe')
ns = {'__name__': 'probe'}
exec(probe_code.split('async def main')[0], ns)
n = len(ns['SCENES'])
def bl(k): return '\n'.join('  * ' + esc(x) for x in meta.get(k, [])) or '  * (none recorded)'
doc = f'''
{esc(title)}
SIMPLE ENGLISH Q&A EXPLANATION MASTERCLASS COMPILER - {n} chapters. Scope: {esc(meta.get("scope", ""))}
=====================================================================================================
SOURCES READ / CHECKED IN THIS BUILD:
{bl("sources")}
CHANGES VERSUS THE SOURCE (outdated / superseded / corrected):
{bl("changes_vs_source")}
KEY FACTS:
{bl("key_facts")}
NOT VERIFIED (flagged on the cards - quote the official text in an answer sheet):
{bl("not_verified")}
Usage
    python build_{stem}.py --audit      # density check only (no ffmpeg / internet)
    python build_{stem}.py --preview    # slides only
    python build_{stem}.py --no-tts     # silent dry run
    python build_{stem}.py --part 1     # build one part (1..N from PART_STARTS, or PART_STARTS = "auto")
    python build_{stem}.py              # full build (needs internet for edge-tts; ffmpeg+ffprobe with libass on PATH)
'''
code = combine(scenes, stem=stem, title=esc(title), doc=doc)
compile(code, 'built', 'exec')
# Header line: escape separately so a stray backtick or newline in title/scope cannot break the outer Markdown.
md = (
    f'# {esc_md(title)} - Simple English Video Compiler (Python script)\n\n'
    f'Scope: {esc_md(meta.get("scope", ""))}\n\n'
    f'Save the code block as `build_{stem}.py` and run it as described in its docstring.\n\n'
    f'````python\n{code}\n````\n'
)
open(out, 'w', encoding='utf-8').write(md); print('written', out, len(md.split('\n')), 'lines')
```
<!-- KIT_FILE: END -->

## APPENDIX 4 — `FORMAT_SPEC.md`

<!-- KIT_FILE: FORMAT_SPEC.md BEGIN -->
````markdown
# FORMAT_SPEC - scene file format for the video-script compiler

A scenes file is a plain text file with exactly three top-level assignments:

```python
SCENES = [ {...scene...}, {...scene...}, ... ]
FLOWS = { "flow_key": {"nodes": [...4 nodes...], "edges": [...3 edges...]}, ... }   # may be {}
PART_STARTS = ["id_of_first_scene", "id_of_first_scene_of_2nd_third", "id_of_first_scene_of_3rd_third"]   # or "auto"
```

The colour names `RED, ORANGE, BLUE, GREEN, SKY, YELLOW, PINK` are already defined by the engine. Do not import anything. Do not write any other code.

`PART_STARTS` may have **1, 2 or 3** entries; the first entry MUST be the first scene's id, and the entries MUST be strictly increasing in scene order. It may also be the string `"auto"` (no ids needed) or `[]` (one part). `--part N` on the built script validates N against the number of **resolved** parts.

How `PART_STARTS` becomes parts (`resolve_parts()` in the engine, verified by `check_scenes.py`):

| `PART_STARTS` | `--part` count | Split |
|---|---|---|
| `"auto"` | 3 (fewer for tiny batches) | nearly equal parts, earlier parts take the extra scene: 5 scenes -> 2 / 2 / 1 |
| `[]` or `None` | 1 | the whole batch |
| 1-3 real boundary ids, e.g. `["c01_x", "c12_y", "c23_z"]` | `len(PART_STARTS)` | part *i* starts at entry *i*; the last part runs to the end (26 scenes -> 11 / 11 / 4) |
| the first N scene ids, e.g. `["c01", "c02", "c03"]` | `len(PART_STARTS)` | **placeholder repair**: the list names no real boundary, so the batch is split into N nearly equal parts and a note is printed |

The placeholder-repair row is what stops `--part 1` and `--part 2` from becoming single-chapter runs when the list is only the first few scene ids. Real boundaries are always honoured exactly. Every resolved part is non-empty, in order, and covers the batch with no gap or overlap.

## A scene

```python
{
  "id": "c03_07_strike_definition",          # unique; start with c<batch>_<serial>; used by PART_STARTS and covers
  "chapter": "CHAPTER 7 • RULE 7(ii): STRIKES",   # at most 95 characters; chapter numbers restart in every batch
  "title": "RULE 7(ii) — WHAT COUNTS AS A STRIKE",  # ONE line on screen, about 72 characters at most
  "accent": RED, "badge": "RULE 7(ii)",       # badge: short label, about 22 characters at most
  "q": "What exactly is a strike under these rules?",  # the question on screen, about 105 characters at most
  "intro": "...",                              # OPTIONAL: only the first scene of a batch (checker enforces this)
  "lead": "...",                               # OPTIONAL: a short teacher transition before the first card
  "q_say": "Sir, what exactly is a strike ...?",       # the question as Riya says it (max 35 words)
  "flow": "flow_key",                          # OPTIONAL: draws the 4-step diagram under the question
  "boxes": [ (title, SHORT, FULL, COLOUR, narration), ... ],   # 3 to 5 cards; 4 is ideal
  "hook": "REMEMBER: ... !",                   # ONE line, about 105 characters at most
  "hook_say": "Remember: ...",                 # the hook as spoken (max 40 words)
  "covers": ["R7(ii)", "GID7-2"],              # REQUIRED: ledger ids covered by this scene (verified by check_scenes.py --ledger)
  "calc_asserts": ["12000 * 0.50 == 6000"],    # REQUIRED if any card has a numeric worked example.
                                               #   Each string is eval()'d with empty builtins; ANY truthy result passes.
                                               #   Use ["NO_MATH"] when there is no arithmetic/date step.
}
```

## A card (box tuple of five strings/colour)

`(card title, SHORT, FULL, COLOUR, narration)`

- **card title**: at most about 40 characters, capitals are fine ("THE RULE", "THE PROVISO", "REAL EXAMPLE", "THE TRAP").
- **SHORT**: what is drawn on the card. Plain words. At most about 150 characters with 4 cards, about 110 with 5 cards, about 100 when the scene has a flow diagram. It may hold a one-line example.
- **FULL**: the exact wording, citations, amounts, OM numbers, dates. Not drawn on the card; written to the reference sheet. Wording that was not read verbatim from an official source (`"read_verbatim": false` in the ledger) must be called a close restatement if quoted in single quotes.
- **COLOUR**: one of the predefined colours.
- **narration**: what the teacher says. Two to four sentences (three to six if it carries a worked example). Hard maximum 100 words per card; the built script's `--audit` fails above that. Numbers spelled as spoken. Acronyms may stay as written because the engine's pronunciation table (`_TTS_FIXES`) fixes them.

## Forbidden in strings

- no double quote character and no backslash inside any narration, SHORT, q_say, hook_say, intro or lead (use single quotes in FULL text);
- no arrows or emoji (use words); a bullet dot `•` and an em dash `—` are fine;
- no tabs; strings are in plain Python quotes; long strings may be split across lines in parentheses.

## A flow diagram

```python
"flow_key": {
  "nodes": [ (x, y, w, h, "TITLE", "sub line", COLOUR, step_number), ... exactly 4 ... ],
  "edges": [ (from_index, to_index, COLOUR, step_number), ... exactly 3 ... ],
}
```

Use these fixed positions so nothing overlaps (copy them from the sample): nodes at `y=300, h=80`, with `(x, w)` = `(80, 420), (570, 430), (1070, 360), (1500, 340)`. Node title: up to about 24 characters; sub line: up to about 24 characters. Edges connect node 0→1, 1→2, 2→3. A scene with a flow shows the diagram, so its card SHORT texts must be shorter (about 100 characters).

## The `calc_asserts` namespace

Each string is `eval()`'d with `{'__builtins__': {}}` and the following names in scope:

`datetime`, `math`, `Fraction`, `round`, `min`, `max`, `abs`, `sum`, `len`, `str`, `int`, `float`, `bool`, `tuple`, `list`, `set`, `dict`, `range`, `sorted`, `any`, `all`, `zip`.

`True` and `False` are language keywords and always available. If you need a builtin not in this list, rewrite the expression (or extend the namespace in `check_scenes.py`). `["NO_MATH"]` means "no arithmetic or date step, nothing to verify" — use it when a scene has an example with no numbers, or when the example's numbers are covered by another scene's `calc_asserts`.

## The "close restatement" tag

`check_scenes.py` treats any single-quoted phrase of **12 or more characters** inside FULL text as an attempt to quote verbatim. If the ledger entry for a covered id has `"read_verbatim": false` (i.e. the source was only summarised, not read verbatim), the checker fails unless the FULL text also contains the literal phrase `close restatement`. To quote a summary-only source, write:

> 'The rule requires that the employee inform the superior before the deadline.' (close restatement)

To avoid the check entirely, do not use single quotes around phrases of 12+ characters in FULL text on summary-only items — paraphrase in plain words instead.

## Content & anti-hallucination rules

- One chapter = one question a real candidate would ask. Answer order across the cards: the rule in plain words, the proviso or exception, a real example, the trap or look-alike term. Last card of most chapters is the trap/remember card.
- Every examinable item of the ledger must be covered somewhere and listed in some scene's `covers`.
- Never invent a rule number, OM/G.S.R. number, 4-digit year, percentage or Rupee amount: `check_scenes.py --ledger --source` scans every non-example card line and narration, and every text field (title, chapter, badge, question, hook, intro, lead), and fails if any citation or figure is absent from the verified source file and ledger.
- Obsolete items are not presented as current. If one must be mentioned, the line must begin `OBSOLETE / HISTORY ONLY:` and name the replacement.
- Unverified items MUST be flagged on the card with the exact phrase `not confirmed against an official source`.
- Worked examples use invented names and recomputed numbers backed by `"calc_asserts"` (every expression must evaluate truthy).
- Vary the transitions: "Let us take the rule first", "Now the exception", "Here is a real example", "Be careful, this is the trap", "Remember:".

## Checker

`python3 check_scenes.py scenes_file.txt --ledger B<n>_verified.json --source B<n>.txt` must print PASS. Fix defects by shortening the SHORT text, splitting the chapter, or correcting ungrounded figures; never by cutting a rule out of the FULL text or narration.
````
<!-- KIT_FILE: END -->

## APPENDIX 5 — sample scenes, ledger & source (FICTIONAL rule, format sample only)

### `sample_scenes.txt`

<!-- KIT_FILE: sample_scenes.txt BEGIN -->
```python
SCENES = [
    # FORMAT SAMPLE ONLY. The rules below are FICTIONAL ("Model Service Rules") and exist only to show the shape. Replace with real content.
    {
        "id": "c01_overview",
        "chapter": "CHAPTER 1 • MODEL SERVICE RULES: THE MAP",
        "title": "THE MODEL RULES AT A GLANCE — THREE PARTS, NINE RULES",
        "accent": RED, "badge": "INDEX • RULES 1-9",
        "q": "How is this rule book laid out, and where do we begin?",
        "intro": ("Welcome! In this series we study the Model Service Rules, one rule at a time, with every sub rule, clause and proviso. "
                  "First, a map of the whole book. Let us hear Riya's question."),
        "q_say": "Sir, how is this rule book arranged, and where do we begin?",
        "flow": "map",
        "boxes": [
            ("PART I: GENERAL",
             "Rules 1-3: short title, definitions, application.",
             "Part I General: Rule 1 (short title and commencement), Rule 2 (definitions), Rule 3 (application). FICTIONAL SAMPLE TEXT.",
             RED,
             "Part 1 is General. It has Rules 1 to 3: the short title, the definitions and where the rules apply."),
            ("PART II: DUTIES",
             "Rules 4-6: what an employee must do, with one exception.",
             "Part II Duties: Rule 4 (general duty), Rule 5 (reporting), Rule 6 (exception for emergencies). FICTIONAL SAMPLE TEXT.",
             ORANGE,
             "Part 2 is Duties. Rules 4 to 6 say what an employee must do, and Rule 6 gives an exception for emergencies."),
            ("PART III: PENALTIES",
             "Rules 7-9: minor and major penalties, and who may impose them.",
             "Part III Penalties: Rule 7 (minor penalties), Rule 8 (major penalties), Rule 9 (authority). FICTIONAL SAMPLE TEXT.",
             BLUE,
             "Part 3 is Penalties. Rules 7 to 9 list the minor and major penalties and say who may impose them."),
        ],
        "hook": "REMEMBER: 3 Parts • General 1-3 • Duties 4-6 • Penalties 7-9!",
        "hook_say": "Remember: three Parts. General is Rules 1 to 3, Duties is Rules 4 to 6, and Penalties is Rules 7 to 9.",
        "covers": ["MAP", "R1-3"],
    },
    {
        "id": "c02_rule4_duty",
        "chapter": "CHAPTER 2 • RULE 4: THE GENERAL DUTY",
        "title": "RULE 4 — WHAT IS THE GENERAL DUTY, AND WHAT IS THE PROVISO?",
        "accent": ORANGE, "badge": "RULE 4",
        "q": "What does Rule 4 require of an employee, and does the proviso change it?",
        "q_say": "Sir, what does Rule 4 require, and does its proviso change anything?",
        "boxes": [
            ("THE RULE",
             "An employee must do the assigned work honestly and on time.",
             "Rule 4(1): 'Every employee shall perform the assigned work honestly and within the time fixed.' FICTIONAL SAMPLE TEXT.",
             SKY,
             "Let us take the rule first. Every employee must do the assigned work honestly and within the time that is fixed."),
            ("THE PROVISO",
             "Proviso: if the time cannot be met, tell the superior BEFORE the deadline.",
             "Proviso to Rule 4(1): if the work cannot be finished in time, the employee shall inform the superior before the time expires. FICTIONAL SAMPLE TEXT.",
             GREEN,
             "Now the proviso. If the work cannot be finished in time, the employee must tell the superior before the time runs out."),
            ("REAL EXAMPLE",
             "Example: Asha must finish a report by Friday. On Wednesday she tells her officer it will be late.",
             "Example (invented names): Asha is told to finish a report by Friday. On Wednesday she sees it will take until Monday, so she informs her officer on Wednesday. She has followed the proviso. If she had said nothing until Saturday, she would not have.",
             ORANGE,
             "Here is a real example. Asha must finish a report by Friday. On Wednesday she sees it will be late, so she tells her officer at once. That follows the proviso."),
            ("THE TRAP",
             "Trap: telling the superior AFTER the deadline does not satisfy the proviso.",
             "The proviso speaks of informing BEFORE the time expires. Informing after the deadline is not compliance. FICTIONAL SAMPLE TEXT.",
             RED,
             "Be careful, this is the trap. The proviso says before the time expires. Telling the superior after the deadline is too late."),
        ],
        "hook": "REMEMBER: Rule 4 = honest and on time; if late, tell BEFORE the deadline!",
        "hook_say": "Remember: Rule 4 means honest and on time, and if you will be late, tell your superior before the deadline.",
        "covers": ["R4(1)", "R4-PROV1"],
        "calc_asserts": ["NO_MATH"],
    },
    {
        "id": "c03_chain",
        "chapter": "CHAPTER 3 • WHO IMPOSES A PENALTY: RULES 7 TO 9 IN ORDER",
        "title": "FROM A LAPSE TO A PENALTY — THE STEP-BY-STEP ROUTE",
        "accent": SKY, "badge": "RULES 7 • 8 • 9",
        "q": "Given a lapse, how do we find the penalty and the authority, step by step?",
        "q_say": "Sir, how do we use Rules 7, 8 and 9 together to reach the penalty and the authority?",
        "flow": "route",
        "boxes": [
            ("STEP 1: THE LAPSE",
             "Name the lapse and check it against Rule 4 or 5.",
             "Identify the lapse and the rule it breaches (Rule 4 or Rule 5). FICTIONAL SAMPLE TEXT.",
             SKY,
             "Step 1: name the lapse and check which rule it breaks, Rule 4 or Rule 5."),
            ("STEP 2: MINOR OR MAJOR",
             "Pick the list: Rule 7 minor penalties or Rule 8 major penalties.",
             "Rule 7 lists the minor penalties; Rule 8 lists the major penalties. FICTIONAL SAMPLE TEXT.",
             BLUE,
             "Step 2: decide whether the lapse is minor or major, and open Rule 7 or Rule 8."),
            ("STEP 3: THE AUTHORITY",
             "Rule 9 names who may impose that penalty.",
             "Rule 9 names the authority for each class of penalty. FICTIONAL SAMPLE TEXT.",
             GREEN,
             "Step 3: Rule 9 tells us who may impose that penalty."),
            ("STEP 4: RECORD IT",
             "Write the order with the rule number and reasons.",
             "The order states the rule, the penalty and the reasons. FICTIONAL SAMPLE TEXT.",
             RED,
             "Step 4: write the order, with the rule number and the reasons."),
        ],
        "hook": "REMEMBER: Lapse, then minor or major, then authority, then a reasoned order!",
        "hook_say": "Remember: find the lapse, choose minor or major, find the authority, and write a reasoned order.",
        "covers": ["R7", "R8", "R9"],
    },
    {
        "id": "c04_rule98_historical",
        "chapter": "CHAPTER 4 • RULE 98: SUPERSEDED PROCEDURE (HISTORY ONLY)",
        "title": "RULE 98 — THE OLD PROCEDURE IS HISTORY",
        "accent": RED, "badge": "HISTORY ONLY",
        "q": "Is the old procedure still current, or has it been replaced?",
        "q_say": "Sir, is the old procedure still current, or has it been replaced?",
        "boxes": [
            ("OBSOLETE / HISTORY ONLY",
             "OBSOLETE / HISTORY ONLY: Rule 98 (Form 99-Old) is replaced by Rule 98A.",
             "OBSOLETE / HISTORY ONLY: Rule 98 and Form 99-Old are superseded by Rule 98A and its new form; they are not current law. FICTIONAL SAMPLE TEXT.",
             RED,
             "This is history only. Rule 98 has been replaced by Rule 98A. Do not use the old form."),
            ("THE NEW POSITION",
             "Current law: Rule 98A and its new form apply.",
             "Current position: Rule 98A and its associated new form apply. FICTIONAL SAMPLE TEXT.",
             GREEN,
             "The current position is Rule 98A and its new form. The old procedure must not be used."),
            ("THE TRAP",
             "Trap: the old form name still appears on some office templates.",
             "Old printed templates that still show the superseded form must be replaced with the new form. FICTIONAL SAMPLE TEXT.",
             ORANGE,
             "Be careful, this is the trap. Some old office templates may still show the old form. Replace them with the new form."),
        ],
        "hook": "REMEMBER: current = Rule 98A and the new form, not the old one!",
        "hook_say": "Remember: Rule 98A is the current rule; the old form is history only.",
        "covers": ["R98-OLD"],
        "calc_asserts": ["NO_MATH"],
    },
    {
        "id": "c05_rule99_unverified",
        "chapter": "CHAPTER 5 • RULE 99: AN UNVERIFIED LEAD",
        "title": "RULE 99 — A LEAD WE COULD NOT CONFIRM",
        "accent": PINK, "badge": "UNVERIFIED",
        "q": "Is Rule 99 current? Can we confirm the lead against an official source?",
        "q_say": "Sir, is Rule 99 current? Can we confirm the lead against an official source?",
        "boxes": [
            ("THE LEAD",
             "A secondary source says Rule 99 was amended. Not confirmed against an official source.",
             "A secondary compilation mentions a possible amendment to Rule 99. Not confirmed against an official source. FICTIONAL SAMPLE TEXT.",
             PINK,
             "A secondary source says Rule 99 was amended, but we could not confirm this against an official source."),
            ("WHAT WE DID",
             "We searched Tier-1 official sources. The lead could not be confirmed.",
             "Search of dopt.gov.in, doe.gov.in and egazette.gov.in did not return an official notice on Rule 99 in the time available. FICTIONAL SAMPLE TEXT.",
             SKY,
             "We searched official government sources. The amendment could not be confirmed in the time available."),
            ("THE SAFE POSITION",
             "Keep the printed rule and tag it unverified until the official text is read.",
             "Until the official text is read, apply the printed rule as written and tag the item unverified. FICTIONAL SAMPLE TEXT.",
             GREEN,
             "The safe position is to keep the printed rule and tag it unverified until the official text is read."),
        ],
        "hook": "REMEMBER: no official source, no change — keep the printed rule!",
        "hook_say": "Remember: without an official source, keep the printed rule as it stands.",
        "covers": ["R99"],
        "calc_asserts": ["NO_MATH"],
    },
]

FLOWS = {
    "map": {
        "nodes": [
            (80, 300, 420, 80, "Part I: GENERAL", "Rules 1-3", RED, 1),
            (570, 300, 430, 80, "Part II: DUTIES", "Rules 4-6", ORANGE, 2),
            (1070, 300, 360, 80, "Part III: PENALTIES", "Rules 7-9", BLUE, 3),
            (1500, 300, 340, 80, "Next batch", "Later rules", GREEN, 4),
        ],
        "edges": [(0, 1, RED, 2), (1, 2, ORANGE, 3), (2, 3, BLUE, 4)],
    },
    "route": {
        "nodes": [
            (80, 300, 420, 80, "LAPSE", "Rule 4 or 5", SKY, 1),
            (570, 300, 430, 80, "MINOR / MAJOR", "Rule 7 or 8", BLUE, 2),
            (1070, 300, 360, 80, "AUTHORITY", "Rule 9", GREEN, 3),
            (1500, 300, 340, 80, "ORDER", "Reasons recorded", RED, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, BLUE, 3), (2, 3, GREEN, 4)],
    },
}

# Placeholder boundaries: these are the first three scene ids, not real part starts.
# resolve_parts() detects that, splits the five scenes into 2 / 2 / 1 for --part 1 / 2 / 3,
# and prints a note. Use PART_STARTS = "auto" to ask for even parts explicitly, or name the
# true part-start ids (for example ["c01_overview", "c04_rule98_historical"]) to control them.
PART_STARTS = ["c01_overview", "c02_rule4_duty", "c03_chain"]
```
<!-- KIT_FILE: END -->

### `sample_ledger.json`

<!-- KIT_FILE: sample_ledger.json BEGIN -->
```json
{
  "batch": "sample",
  "obsolete_tokens": ["Form 99-Old"],
  "items": [
    {
      "id": "R1-3",
      "ref": "Rules 1-3",
      "source_lines": "L1-L3",
      "source_verbatim": "Part I General: Rule 1 (short title and commencement), Rule 2 (definitions), Rule 3 (application). Rules 1-3. Part II Duties: Rule 4 (general duty), Rule 5 (reporting), Rule 6 (exception for emergencies). Rules 4-6. Part III Penalties: Rule 7 (minor penalties), Rule 8 (major penalties), Rule 9 (authority). Rules 7-9.",
      "status": "confirmed",
      "read_verbatim": true,
      "current_position": "Part I General covers Rules 1-3; Part II Duties covers Rules 4-6; Part III Penalties covers Rules 7-9.",
      "evidence": "Sample source L1-L3",
      "obsolete_tokens": [],
      "note": ""
    },
    {
      "id": "R4(1)",
      "ref": "Rule 4(1)",
      "source_lines": "L4",
      "source_verbatim": "Rule 4(1): 'Every employee shall perform the assigned work honestly and within the time fixed.'",
      "status": "confirmed",
      "read_verbatim": true,
      "current_position": "Rule 4(1): 'Every employee shall perform the assigned work honestly and within the time fixed.'",
      "evidence": "Sample source L4",
      "obsolete_tokens": [],
      "note": ""
    },
    {
      "id": "R4-PROV1",
      "ref": "Proviso to Rule 4(1)",
      "source_lines": "L5",
      "source_verbatim": "Proviso to Rule 4(1): if the work cannot be finished in time, the employee shall inform the superior before the time expires.",
      "status": "confirmed",
      "read_verbatim": true,
      "current_position": "Proviso to Rule 4(1): inform superior before deadline expires.",
      "evidence": "Sample source L5",
      "obsolete_tokens": [],
      "note": ""
    },
    {
      "id": "R7",
      "ref": "Rule 7",
      "source_lines": "L6",
      "source_verbatim": "Rule 7 lists the minor penalties (after checking Rule 4 or Rule 5).",
      "status": "confirmed",
      "read_verbatim": true,
      "current_position": "Rule 7 lists minor penalties.",
      "evidence": "Sample source L6",
      "obsolete_tokens": [],
      "note": ""
    },
    {
      "id": "R8",
      "ref": "Rule 8",
      "source_lines": "L7",
      "source_verbatim": "Rule 8 lists the major penalties.",
      "status": "confirmed",
      "read_verbatim": true,
      "current_position": "Rule 8 lists major penalties.",
      "evidence": "Sample source L7",
      "obsolete_tokens": [],
      "note": ""
    },
    {
      "id": "R9",
      "ref": "Rule 9",
      "source_lines": "L8",
      "source_verbatim": "Rule 9 names the authority for each class of penalty.",
      "status": "confirmed",
      "read_verbatim": true,
      "current_position": "Rule 9 names the penalty authority.",
      "evidence": "Sample source L8",
      "obsolete_tokens": [],
      "note": ""
    },
    {
      "id": "R98-OLD",
      "ref": "Rule 98 (superseded by Rule 98A)",
      "source_lines": "L9",
      "source_verbatim": "Rule 98-Old: superseded Form 99-Old procedure.",
      "status": "obsolete",
      "read_verbatim": true,
      "current_position": "Rule 98 superseded by Rule 98A (G.S.R. 999(E), 2024).",
      "evidence": "FICTIONAL SAMPLE - gazette of india, G.S.R. 999(E), 2024",
      "obsolete_tokens": ["Form 99-Old", "Rule 98-Old"],
      "note": "historical only; use Rule 98A and the new form"
    },
    {
      "id": "R99",
      "ref": "Rule 99 (unverified lead)",
      "source_lines": "L10",
      "source_verbatim": "Rule 99: an unverified lead.",
      "status": "unverified",
      "read_verbatim": false,
      "current_position": "A secondary compilation reports a possible amendment; not confirmed against an official source.",
      "evidence": "Coaching blog (secondary source, not Tier-1)",
      "obsolete_tokens": [],
      "note": "needs browser-based verification against dopt.gov.in"
    }
  ]
}
```
<!-- KIT_FILE: END -->

### `sample_source.txt`

<!-- KIT_FILE: sample_source.txt BEGIN -->
```text
Part I General: Rule 1 (short title and commencement), Rule 2 (definitions), Rule 3 (application). Rules 1-3.
Part II Duties: Rule 4 (general duty), Rule 5 (reporting), Rule 6 (exception for emergencies). Rules 4-6.
Part III Penalties: Rule 7 (minor penalties), Rule 8 (major penalties), Rule 9 (authority). Rules 7-9.
Rule 4(1): 'Every employee shall perform the assigned work honestly and within the time fixed.'
Proviso to Rule 4(1): if the work cannot be finished in time, the employee shall inform the superior before the time expires.
Rule 7 lists the minor penalties (after checking Rule 4 or Rule 5).
Rule 8 lists the major penalties.
Rule 9 names the authority for each class of penalty.
Rule 98-Old: superseded Form 99-Old procedure.
Rule 99: an unverified lead.
```
<!-- KIT_FILE: END -->

---

## APPENDIX 6 — Coverage & Grounding Proof (built into `check_scenes.py`)

Running `check_scenes.py` with `--ledger` and `--source` automatically proves coverage and grounding before delivery:

```bash
python3 WORK/kit/check_scenes.py WORK/scenes/scenes_<n>.txt \
    --ledger WORK/ledger/B<n>_verified.json \
    --source WORK/src/B<n>.txt
```

A PASS proves: (1) every ledger item's `source_verbatim` is an exact whitespace-normalized substring of `B<n>.txt`; (2) every `changed`/`obsolete` item cites a Tier-1 official source in `evidence`; (3) zero non-obsolete ledger items lack a `covers` tag; (4) zero invented ledger IDs appear in `covers`; (5) zero obsolete tokens leaked as words outside `OBSOLETE / HISTORY ONLY:` lines (plural-aware: `ACR` also blocks `ACRs`; comma variants of amounts match); (6) every unverified item carries `"not confirmed against an official source"` on its card; (7) no summary-only source (`"read_verbatim": false`) is quoted as verbatim without `"close restatement"`; (8) every non-example Rule/Para/Article ref, G.S.R./S.O./O.M. number, 4-digit year, percentage, and Rupee amount across every text field (title, chapter, badge, question, hook, intro, lead, and every card's SHORT/FULL/narration) exists in the verified corpus; (9) every `calc_asserts` math/date expression evaluates truthy; (10) `intro` appears on the first scene only.

## APPENDIX 7 — OPTIONAL practice Q&A scenes (only if `PRACTICE_QA=on`)

Same scene structure, added as the LAST chapters of each part, ids prefixed `pq`. One scene = one practice question with a model answer, four cards:

```python
{
  "id": "pq_c3_01", "chapter": "PRACTICE 1 • RULE X(2)-(4)", "title": "PRACTICE — CAN AN ORDER EXCLUDE A GROUP FROM THE RULES?",
  "accent": PINK, "badge": "PRACTICE",
  "q": "An order excludes one group of staff from Rule X. Is it valid, and who decides a doubt?",
  "q_say": "Sir, here is a practice question. ...",
  "boxes": [
    ("THE QUESTION",   SHORT, FULL, SKY,   narration),
    ("MODEL ANSWER",   SHORT, FULL, GREEN, narration),
    ("WHY",            SHORT, FULL, BLUE,  narration),
    ("COMMON MISTAKE", SHORT, FULL, RED,   narration),
  ],
  "hook": "REMEMBER: ... !", "hook_say": "Remember: ...",
  "covers": ["PRACTICE", "RX(2)", "RX(4)"],
  "calc_asserts": ["NO_MATH"],
}
```

Rules: (1) every practice question tests an item whose ledger status is `confirmed` or `changed` (current position), never obsolete; (2) scenario figures are verified by `calc_asserts` and recomputed by the auditor; (3) the model answer cites only rules covered in the batch; (4) 4-6 practice scenes per part; (5) practice scenes stay at the end of their own part, so `PART_STARTS` still splits evenly.

## APPENDIX 8 — Quality gates checklist (tick every line before sending)

- [ ] Kit unpacked via the Step 1 extractor; self-test passed (including `--ledger sample_ledger.json --source sample_source.txt`) and the extractor reported **all 7 expected kit files** (engine_template.py, check_scenes.py, build_script_md.py, FORMAT_SPEC.md, sample_scenes.txt, sample_ledger.json, sample_source.txt)
- [ ] Source read completely; batches chosen and announced
- [ ] Ledger built for every batch with `"source_lines"`, exact `"source_verbatim"` (verified against `--source`), `"read_verbatim"`, and `"obsolete_tokens"`; Tier-1 authority lock observed
- [ ] Obsolete items removed or marked `OBSOLETE / HISTORY ONLY:`; `changed` items show the current position backed by a Tier-1 official source and carry their superseded tokens in `obsolete_tokens`
- [ ] Unverified items visibly flagged on the card (`not confirmed against an official source`); outside-the-file facts labelled
- [ ] `check_scenes.py --ledger --source` returns PASS; independent audit set `remaining_gaps: []` in `meta_<n>.json`
- [ ] (If Harness² enabled) Propose–Probe–Compose pass confirmed density and token stability; lessons appended to reflection notes
- [ ] Every worked example verified via `calc_asserts` and recomputed by the auditor
- [ ] Pronunciation table extended with this source's acronyms
- [ ] `--audit` clean (card density AND narration length); `--preview` rendered; 2-3 slides inspected; no overflowing word; intro slide shows the "Introduction" label and a `CHAPTER INTRO` chip, not the raw question block
- [ ] `PART_STARTS` checked with `--part`: every part non-empty and in order (use `PART_STARTS = "auto"` for even thirds; the checker prints a note when a placeholder list is auto-balanced)
- [ ] Docstring lists sources, changes versus source, key facts, NOT VERIFIED, usage
- [ ] Every chapter is one real question; question types mixed; answer order rule, exception, example, trap
- [ ] Glossary consistent; every "see Rule X" resolved; consolidated change log written
- [ ] Obsolete-term sweep done over ALL outputs
- [ ] Practice scenes (only if switched on) test current items only
- [ ] Clean-machine gate: Step 1 run once on a fresh machine/container (no Pillow, no ffmpeg) and once with ffmpeg present; both self-tests PASS
- [ ] Offline gate: `--audit` and `--preview` work with no network; `--no-tts` completes a full silent build; the failure messages in Appendix 11 appear as documented when a dependency is missing
- [ ] Closing message: coverage, changes, unverified items, how to build locally, Sources as links

## APPENDIX 9 — Lessons learned (mistakes made and fixed in earlier work, generalised)

- A tool that only summarises pages cannot give verbatim clause text - set `"read_verbatim": false` and say "close restatement", or use a browser tool.
- Summarising during ledger creation drops provisos and flips "may"/"shall" - always store `source_lines` and copy `source_verbatim` directly from the source file.
- For `confirmed` items, only `source_verbatim` is trusted. (An agent could hallucinate a number into `current_position` and pass the token check otherwise.)
- Secondary blogs and coaching compilations often misstate amendments - lock `changed` and `obsolete` status overrides to Tier-1 official government domains.
- Raw pipe characters (`|`) inside regexes can get escaped to `\vert{}` by Markdown table/Canvas serialisers - `[a-z]+` already matches both letter clauses and Roman numeral sub-clauses.
- Substring matching on short obsolete tokens like "ACR" false-positives on "across" or "macro" - always match obsolete tokens with word boundaries; AND remember to include plurals (`ACRs`) and comma variants (`Rs. 3,500` vs `Rs. 3500`) or the leak escapes the other way.
- A `changed` item is "old X -> new Y" — old X is still superseded and must be blocked from every card. Collect `obsolete_tokens` from `changed` items too, not only from `obsolete` items.
- Agents sometimes stay faithful on-screen but improvise a year or rule number in the spoken narration (or the title, question, hook, chapter line, intro or lead) - `check_scenes.py` must scan every text field, not only SHORT/FULL/narration.
- Examples can be right when the rule is right but the spoken arithmetic is wrong - scan the NARRATION for digits when requiring `calc_asserts`; the card often has no numeric example while the voice does.
- Unvalidated `PART_STARTS` ids crash `--part` builds at runtime - validate that `PART_STARTS` is `"auto"`, `[]`, or a list of 1-3 valid, strictly increasing scene IDs starting at index 0, and validate `--part` against the resolved part count with a pluralised message.
- `PART_STARTS` holding only the first few scene ids is a placeholder, not a boundary plan. Slicing literally between consecutive ids made `--part 1` and `--part 2` single-chapter runs. Detect that shape, auto-balance to N nearly equal parts, and say so in a printed note; honour real boundaries exactly and add `PART_STARTS = "auto"` for even thirds.
- Arrows, emoji and double quotes break the font or the narration strings.
- Text coverage can be complete while currency is unproven - report both separately.
- Usage limits can interrupt a workflow; resume it (cached agents replay) and re-check that the failed stages' output files exist.
- In a cloud sandbox, the neural voice service and a libass-enabled ffmpeg may be unavailable - deliver the script and let the user build locally.
- Do not sit in long polling or sleep loops the user cannot see; report progress in short messages and run long builds in the background.
- A source quirk (duplicate numbering, mismatched heading) is kept as printed and flagged, never silently "corrected".
- Examples can be wrong even when the rule is right - enforce `calc_asserts` and have the auditor recompute them.
- A question written as a topic label makes weak Q&A; write the question a candidate would really ask.
- A letter-and-number reference such as "2(l)" can be misread on screen; write "CLAUSE L" in the title and badge.
- A long hyphenated word can poke out of a card; reword it instead of shrinking the font.
- A docstring-in-a-fence (4-backtick) inside another fenced markdown needs a fence-aware extractor regex (`(`{3,4})` + matching backreference) - matching only 3 backticks silently skips the file.
- Scaling with Harness² Propose–Probe–Compose prevents prompt degradation in multi-batch rulebooks.

## APPENDIX 10 — OPTIONAL workflow script skeleton (only for environments that have a multi-agent Workflow tool and where the user agreed to its scale)

```javascript
export const meta = {
  name: 'rules-to-video-scripts-harness2',
  description: 'Per batch: verify against Tier-1 official sources, write scenes with Harness2 recursive refinement, independent audit with mechanical grounding gates',
  phases: [{ title: 'Verify' }, { title: 'Write & Refine' }, { title: 'Audit' }, { title: 'Reflect' }],
}
const BATCHES = args.batches            // e.g. ["B1","B2","B3"] - files WORK/src/B1.txt ...
const COMMON = 'Read WORK/kit/FORMAT_SPEC.md, WORK/kit/sample_scenes.txt and WORK/NOTES.md first. Never invent a wording, number, date or OM number. Today is ' + args.today + '.'
const results = await pipeline(
  BATCHES,
  b => agent(COMMON + ' TASK VERIFY for ' + b + ': follow the VERIFY task block; write WORK/ledger/' + b + '_verified.json with source_lines, exact source_verbatim, read_verbatim, and obsolete_tokens.',
             { label: 'verify:' + b, phase: 'Verify' }),
  (v, b) => agent(COMMON + ' TASK WRITE for ' + b + ': execute Propose-Probe-Compose recursion; write WORK/scenes/scenes_' + b + '.txt; run check_scenes.py --ledger WORK/ledger/' + b + '_verified.json --source WORK/src/' + b + '.txt until PASS.',
             { label: 'write:' + b, phase: 'Write & Refine' }),
  (w, b) => agent(COMMON + ' TASK AUDIT for ' + b + ' (assume the draft has gaps and errors): follow the AUDIT task block; fix the file; re-run check_scenes.py --ledger --source; write WORK/meta/meta_' + b + '.json with remaining_gaps:[].',
             { label: 'audit:' + b, phase: 'Audit' }),
  (a, b) => agent(COMMON + ' TASK REFLECT for ' + b + ': extract behavioral contrasts and audit feedback; update WORK/NOTES.md for subsequent batch harnessing.',
             { label: 'reflect:' + b, phase: 'Reflect' })
)
return results
```

---

## APPENDIX 11 — Deployment & environment matrix (make it work anywhere)

This file is **not a web service**: it is a document plus a Python kit. "Deployed" means three places, and each is verified below.

| Where it runs | What is verified | Gate |
|---|---|---|
| **As a document** (GitHub rendering, a wiki, a pasted prompt) | every fenced block is balanced; the 4-backtick `FORMAT_SPEC.md` block nests correctly inside this appendix; no stray HTML; pure UTF-8 | the fence walk in "Deploy checks" (below) |
| **As a kit installer** (Step 1, first run in a new place) | extractor finds **all 7** kit files, then the checker, assembler, `--audit` and `--preview` all pass on the bundled sample | Step 1 block prints `PASS: 5 scenes, 17 cards` |
| **As a video builder** (`build_<stem>.py`, run locally or in CI) | full silent build (slides, clips, concat, libass burn, `ffmpeg -i` verification) completes and reports video + audio streams at 1920x1080 | `--no-tts` produces `<stem>_masterclass.mp4` |

### Verified environment matrix (recorded from real runs)

| Environment | Python | Pillow | ffmpeg / ffprobe | Result |
|---|---|---|---|---|
| Linux container, clean venv | 3.11 | auto-installed | neither on PATH | `--audit` and `--preview` PASS |
| Linux container, static ffmpeg with libass, plus ffprobe | 3.11 | auto-installed | both on PATH | full `--no-tts` build PASS (3.6 min timeline) |
| Linux container, **no** ffmpeg or ffprobe on PATH | 3.11 | present | resolved via `imageio-ffmpeg`; durations via `ffmpeg -i` | full `--no-tts` build PASS, identical duration, streams and file size |
| 26 scenes / 111 cards, `PART_STARTS = "auto"` | 3.11 | present | static ffmpeg | `--audit` clean, parts of 10 / 9 / 9, `--part 3` build PASS (5.7 min, 126 subtitle cues) |
| No Pillow, no package index reachable | 3.11 | missing | n/a | one-screen error naming the install commands, no traceback |
| No ffmpeg, no imageio wheel, no index | 3.11 | present | missing | one-screen error naming OS install commands, no traceback |

Python 3.10 compatibility is checked statically: all three kit scripts parse with `feature_version=(3, 10)`. At runtime the engine refuses anything older than 3.10 with one explanatory line instead of a syntax error.

### What the engine does when a dependency is missing

| Missing | Behaviour |
|---|---|
| Python < 3.10 | exits at startup: `ERROR: Python 3.10 or newer is required (this interpreter is X.Y.Z).` |
| Pillow | tries `pip`, `pip --user`, then `pip --break-system-packages`; if all fail it prints the install commands plus the virtualenv alternative and exits 1 |
| ffmpeg | prints `ffmpeg not found on PATH - trying the imageio-ffmpeg wheel ...`, installs it when allowed, then resolves the static binary: `pip install --user imageio-ffmpeg` |
| ffmpeg (every route) | exits with Linux, macOS, Windows and `pip` install commands, and says that `--audit` and `--preview` work without it |
| ffprobe only | prints `note: ffprobe not found - falling back to "ffmpeg -i" for durations and the stream check.` and continues |
| libass or fonts | ffmpeg's own error is surfaced; use a full build (`apt install ffmpeg` includes libass) and a font package such as `fonts-dejavu-core` |
| edge-tts or network | exits with the install command and the `--no-tts` workaround; the neural voices need outbound internet |
| package index blocked | pip's own line is shown, then the kit's actionable message; nothing hangs and nothing half-writes |

### Deploy checks to run in one paste

Save this file as `PIPELINE.md` in an empty folder and run the three checks in order. They write only inside `WORK/`.

```bash
# 1. the document itself: every fenced block must close
python3 - PIPELINE.md <<'CHECK1'
import re, sys
t = open(sys.argv[1], encoding='utf-8').read()
stack = []
for n, line in enumerate(t.split('\n'), 1):
    m = re.match(r'^(`{3,})(.*)$', line)
    if not m:
        continue
    ticks, rest = len(m.group(1)), m.group(2)
    if not stack:
        stack.append((ticks, n))
    elif ticks >= stack[-1][0] and not rest.strip():
        stack.pop()
print('unclosed fences:', stack or 'none')
sys.exit(1 if stack else 0)
CHECK1

# 2. installer + kit self-test
mkdir -p WORK/kit && python3 - PIPELINE.md WORK/kit <<'CHECK2'
import re, sys, pathlib
md = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'); out = pathlib.Path(sys.argv[2])
KIT_RE = re.compile(r'<!-- KIT_FILE: (\S+) BEGIN -->\s*(`{3,4})[^\n]*\n(.*?)\n\2\s*<!-- KIT_FILE: END -->', re.S)
EXPECTED = {'engine_template.py', 'check_scenes.py', 'build_script_md.py', 'FORMAT_SPEC.md',
            'sample_scenes.txt', 'sample_ledger.json', 'sample_source.txt'}
got = set()
for name, fence, body in KIT_RE.findall(md):
    (out / name).write_text(body + '\n', encoding='utf-8'); got.add(name)
missing = EXPECTED - got
if missing:
    sys.exit(f'KIT EXTRACTION INCOMPLETE: missing {sorted(missing)}')
print(f'KIT extracted: {len(got)} files (expected {len(EXPECTED)})')
CHECK2
cd WORK/kit && python3 check_scenes.py sample_scenes.txt --ledger sample_ledger.json --source sample_source.txt

# 3. the builder: dependency-light paths first, then a real build
echo '{"scope":"deploy check","sources":["bundled sample"],"changes_vs_source":[],"key_facts":["sample kit only"],"not_verified":["none"],"remaining_gaps":[]}' > meta_test.json
python3 build_script_md.py sample_scenes.txt meta_test.json selftest "Self test" selftest.md
python3 - <<'CHECK3'
import re
t = open('selftest.md', encoding='utf-8').read()
open('selftest.py', 'w', encoding='utf-8').write(re.search(r'````python\n(.*)\n````', t, re.S).group(1))
CHECK3
python3 selftest.py --audit                      # expect: ALL CARDS WITHIN BUDGET
python3 selftest.py --preview                    # expect: slides written to selftest_build/slides
python3 selftest.py --no-tts                     # silent full build; ffmpeg or the imageio-ffmpeg wheel
python3 selftest.py --part 1 --preview           # PART_STARTS = "auto"-style parts still work
```

### Deployment habits that keep it perfect

- **Pin the document, not the machine.** Keep `PIPELINE.md` and each generated `build_<stem>.py` under version control; the whole kit is reproducible from the file alone.
- **Stage the checks by cost.** `--audit` in CI (seconds, no ffmpeg), `--preview` on the build box, `--no-tts` nightly, the voiced build only where the TTS service is reachable.
- **Treat `WORK/` as scratch.** The kit writes only there; publish just the deliverables (`build_*.md`, `*_reference_sheet.md`, `*.mp4`).
- **Never ship a build from a machine where the self-test did not print `PASS: 5 scenes, 17 cards`.** That one line proves extraction, verbatim grounding, the obsolete and unverified gates, coverage and layout budgets together.
- **Fresh-container smoke test before announcing a batch:** run Step 1 exactly as published, then `--audit`. A missing Pillow must produce the documented message, never a traceback.
- **Watch the two silent risks:** a static ffmpeg without libass (subtitles fail at the burn step) and a bare container with no fonts (blocks render as boxes). Both are caught by looking at one rendered slide, which `--preview` gives you in seconds.

## Version history

- **v2.2 (this file)** — deployment hardening: `engine_template.py` refuses Python < 3.10 with one line; Pillow installs through `pip`, `--user` then `--break-system-packages` (PEP 668), and `check_scenes.py` uses the same fallbacks; `require_media_tools()` resolves ffmpeg from PATH or the `imageio-ffmpeg` wheel, treats ffprobe as optional and falls back to `ffmpeg -i` for durations (`_duration_from_ffmpeg`) and stream checks (`stream_info`); every missing dependency now exits with an actionable message instead of a traceback. New **Appendix 11** records the verified environment matrix, the failure-mode messages, a one-paste deploy check and deployment habits; Step 1 states the environment contract; Appendix 8 adds clean-machine and offline gates.
- **v2.1** — `--part` partitioning fixed: new `resolve_parts()` / `even_parts()` in `engine_template.py`; `PART_STARTS = "auto"` for even thirds, `[]` for one part, real boundary ids honoured exactly, and a placeholder list (just the first N scene ids) auto-balanced to N nearly equal parts with a printed note. `check_scenes.py` validates the resolved parts (non-empty, in order, gap-free, covering) and accepts `"auto"`; `FORMAT_SPEC.md` documents the four cases with worked sizes; sample scenes carry an explanatory comment; Appendix 8 adds a `--part` gate and Appendix 9 the lesson.
- **v2** — fixed Step 1 extractor for 4-backtick fences + post-check for all 7 expected kit files; `check_scenes.py` — obsolete tokens now collected from `changed` items too, token grounding extended to every text field (`title`, `chapter`, `badge`, `q`, `q_say`, `hook`, `hook_say`, `intro`, `lead`), `calc_asserts` check now includes narration, plural- and comma-aware obsolete-token matching, `safe_eval_ns` extended with the standard builtins (`len`, `str`, `int`, `float`, `bool`, `tuple`, `list`, `set`, `dict`, `range`, `sorted`, `any`, `all`, `zip`), syntax errors reported by **scene-file** line number, `intro` restricted to the first scene, `nic.in/gazette` dropped from `TIER1_MARKERS`; `engine_template.py` — `--part` gives a pluralised error and no bare `StopIteration`, `--audit` reports over-long narration, intro slide shows an "Introduction" label with a `CHAPTER INTRO` chip; `build_script_md.py` — `title`/`scope` escaped on the Markdown header line, missing `remaining_gaps` is now an error; samples — added `c04_rule98_historical` (obsolete) and `c05_rule99_unverified` (unverified) so the self-test exercises the `OBSOLETE / HISTORY ONLY` and `not confirmed against an official source` branches; `FORMAT_SPEC.md` — documents the `calc_asserts` namespace, narration word limits, the "close restatement" heuristic, and the intro-first-scene rule.
- **v1** — initial.

---

### What changed in this pass, mapped to the fix list

| # | Fix | Where to look |
|---|---|---|
| 1 | Fence-aware extractor + missing-file post-check | Step 1 bash block |
| 2 | Obsolete tokens collected from `changed` items too | `check_scenes.py` – ledger loop |
| 3 | Token grounding on title/chapter/badge/q/q_say/hook/hook_say/intro/lead | `check_scenes.py` – extended scan after card loop |
| 4 | `calc_asserts` required when narration has a numeric example | `check_scenes.py` – `is_example_card` / `num_src` uses `nar` |
| 5 | Plural- and comma-aware obsolete-token matching | `check_scenes.py` – `_obsolete_leaks()` |
| 6 | `--part` pluralised error, no `StopIteration` | `engine_template.py` – `if args.part:` block |
| 7 | `--audit` narration length check | `engine_template.py` – `audit_density()` tail |
| 8 | `title`/`scope` escaped on Markdown header | `build_script_md.py` – `esc_md()` + `md` f-string |
| 9 | `safe_eval_ns` extended | `check_scenes.py` – `safe_eval_ns` dict |
| 10 | Sample scenes & ledger exercise `obsolete` and `unverified` branches | `c04_rule98_historical`, `c05_rule99_unverified`, `R98-OLD`, `R99` |
| 11 | `remaining_gaps` required in `meta.json` | `build_script_md.py` – early `sys.exit` |
| 12 | `intro` restricted to first scene | `check_scenes.py` – post-loop check |
| 13 | `calc_asserts` namespace documented | `FORMAT_SPEC.md` – "The `calc_asserts` namespace" |
| 14 | Intro slide chip now reads `CHAPTER INTRO` and shows a label instead of the raw question | `engine_template.py` – `render_frame` |
| 15 | Syntax-error line numbers refer to the scene file | `check_scenes.py` – `except SyntaxError` |
| 16 | Close-restatement heuristic documented | `FORMAT_SPEC.md` – "The close restatement tag" |
| 17 | `nic.in/gazette` removed from `TIER1_MARKERS` | `check_scenes.py` – tuple literal |
| 18 | `--part` no longer degenerates into single-chapter runs: `resolve_parts()` / `even_parts()`, `PART_STARTS = "auto"`, placeholder repair with a printed note, and checker validation of the resolved ranges | `engine_template.py` – helpers + `if args.part:` block; `check_scenes.py` – `PART_STARTS` block; `FORMAT_SPEC.md` – `PART_STARTS` table |
| 19 | Python < 3.10 refused with one line; Pillow install falls back through `--user` and `--break-system-packages` in both the engine and the checker | `engine_template.py` – header; `check_scenes.py` – Pillow bootstrap |
| 20 | ffmpeg resolved from PATH or `imageio-ffmpeg`; ffprobe optional with `ffmpeg -i` fallbacks for durations and streams | `engine_template.py` – `require_media_tools()`, `_duration_from_ffmpeg()`, `stream_info()` |
| 21 | Every missing dependency exits with an actionable message (no traceback), and `edge-tts` failures point at `--no-tts` | `engine_template.py` – install and TTS blocks |
| 22 | Deployment contract documented: verified environment matrix, failure-mode table, one-paste deploy check, habits | `APPENDIX 11`; Step 1 environment paragraph; Appendix 8 gates |

### One behaviour you'll notice on the self-test

The `--ledger sample_ledger.json --source sample_source.txt` self-test now prints **`PASS: 5 scenes, 17 cards`** (up from 3 scenes / 11 cards) because the two new sample scenes (`c04`, `c05`) exercise the branches that were previously untested. If your terminal prints any other count, extraction or ledger loading is broken — re-check the Step 1 output for `missing [...]`.

The sample `PART_STARTS` is a placeholder (the first three scene ids), so building it now prints a note and splits the five scenes **2 / 2 / 1** instead of 1 / 1 / 3:

```text
$ python selftest.py --part 1 --preview
note: PART_STARTS names only the first 3 scene ids, which is no real part boundary; splitting the 5 scenes into 3 nearly equal parts instead (use PART_STARTS = 'auto' or name the true part-start ids to override)
  scene 01/2  c01_overview
  scene 02/2  c02_rule4_duty
```

`python selftest.py --part 4` now reports `--part 4 is invalid: the batch is split into 3 parts (valid range: 1..3)`.
