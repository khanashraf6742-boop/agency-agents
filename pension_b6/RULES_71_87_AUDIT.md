# Senior-professor audit — CCS (Pension) Rules 2021, Batch 6, Rules 71–87

**Audit date:** 24 October 2026
**Files audited:** `build_pension_rules_batch6_simple_english_video.md` (the compiler script, 1,685 lines, 32 chapters, 128 cards) + the reference screenshot `Screenshot 2026-10-24 022051.png`
**Deliverable:** `pension_b6/build_pension_b6.py` — the updated compiler, with an enforced coverage gate.

---

## 0. What actually arrived (so we are not auditing the wrong thing)

| You asked for | What reached me | What I did |
|---|---|---|
| "both the test files" | **One** `.md` — and that `.md` *is* the Python script, wrapped in a code fence | Extracted the script (1,685 lines, valid Python) and audited it |
| "the Python file" | The same script inside that `.md` | Same file; no second source was present |
| "the screenshot" | `Screenshot 2026-10-24 022051.png` | Read it — but note the subject mismatch below |

⚠️ **The screenshot is not pension content.** It is a *polity* card (Art. 15(5)/15(6), Art. 16(3), the Triple Test, Art. 104/106 of the 106th Amendment, "CLASSIC UPSC TRAP" strip), timestamped 5:03 / 48:50 of a 13-hour video. It is, however, a perfect **design** reference, so I rebuilt the pension deck on its visual grammar. If you meant a second file (e.g. `src/B6.txt`, `ledger/B6_verified.json` or the Batch-5 checker), it did not come through — send it and I will audit against it too.

---

## 1. Method

1. Extracted the script and parsed all 32 scenes / 128 cards / 241 ledger IDs into a flat table.
2. Obtained the **bare text** of Chapter XI (Rules 71–78), Chapter XII (79–80), Chapter XIII (81–84) and Chapter XIV (85–87) — every sub-rule, clause, proviso and Explanation — and read all of it.
3. Built a **rule inventory** of 115 sub-rule units and mapped every unit to the chapter that teaches it. This inventory now lives inside the script as `INVENTORY` and is machine-checked: `--coverage` fails the build if any unit is unmapped, or if any chapter teaches nothing.
4. Compared the script's *claims* against that text, card by card, flagging (a) gaps, (b) stale "unverified" flags, (c) wrong counts, (d) wrong pointers, (e) places where the statute itself is misprinted.
5. Rebuilt the rendering layer to match the screenshot and re-authored all 128 narration lines in Hinglish (Roman script).

**Verdict: the earlier draft was structurally sound — all 17 rules were present, no rule was missing — but it was thin at nine places, and it hedged ("not confirmed") on roughly a dozen points that the bare text settles outright. Both are fixed.**

---

## 2. Coverage matrix (what the script now asserts, and proves)

| Rule | Sub-rule units mapped | Taught in chapter | Verdict |
|---|---|---|---|
| 71 | 14 | 1, 2, 3 | complete — incl. 71(6)(a)–(g) |
| 72 | 7 | 5, 6 | complete |
| 73 | 10 | 7, 8 | complete — incl. the proviso to 73(2)(b)(iii) |
| 74 | 5 | 9 | complete |
| 75 | 8 | 10, 11 | complete |
| 76 | 18 | 12, 13, 14 | complete — incl. (5A) and 76(5)(c)–(e) |
| 77 | 11 | 15, 16 | complete — incl. 77(1)(i)(a)–(g) and (g)(A)–(E) |
| 78 | 2 | 17 | complete |
| 79 | 13 | 20, 21, 22 | complete — incl. 79(4)(c) |
| 80 | 10 | 23, 24 | complete |
| 81 | 3 | 25 | complete |
| 82 | 1 | 26 | complete |
| 83 | 2 | 26 | complete |
| 84 | 3 | 27 | complete |
| 85 | 1 | 28 | complete (was gist) |
| 86 | 2 | 28 | complete (was gist) |
| 87 | 5 | 29 | complete (was gist) |

**115 / 115 units covered.** Six chapters are deliberately cross-cutting and own no rule: 4 (Forms map), 18 (retirement vs death), 19 (the chain), 30 (2025 O.M.s), 31 (amendment register), 32 (recap).

Run it yourself:

```
python build_pension_b6.py --coverage     # matrix + density gate; exits 1 on any hole
```

---

## 3. Gaps found and filled (this is the "fill them in the same format" part)

| # | Hole | Fix |
|---|---|---|
| 1 | **Rule 73(2)(b) proviso** was missing entirely — a period that *cannot* be verified must be reported to the referring office simultaneously | Chapter 8, card 1 rewritten |
| 2 | **Rule 77(1)(i)** was one line; the statute lists seven items (a)–(g), and (g) has sub-items (A)–(E) — unrecovered period, standard-rent-bill amounts, proposed recovery out of gratuity, earlier Directorate references | Chapter 15, card 1 rebuilt around the list |
| 3 | **Rule 76(5)(c)–(e)** — the *missing-servant* balance of gratuity (one-month intimation, six-month wait, adjustment of the Rule 77 withholding) | Chapter 14, card 2 rebuilt |
| 4 | **Rule 79(4)(c)** — the child who was *already* a major at the remarriage | Chapter 22, card 1 |
| 5 | **Format 7** (indemnity bond where the claimant is a minor) and **Form 3** (common nomination for gratuity + GPF + CGEGIS, Rule 46) | Chapter 4 table, two new rows |
| 6 | **Rules 85, 86, 87** were explicitly "close gist / unverified" | Chapters 28–29 rewritten on the bare text, hedges removed |
| 7 | **Rule 79(1)** was "not seen in full" | Chapter 20, card 1 rewritten; the ineligibility trigger is now quoted, not guessed |
| 8 | **Rule 79(2)(b)** "a person who became a member of the family after retirement" was flagged as not found | It *is* in the text; flag removed, words quoted |
| 9 | **Rule 77(1)(i)** "so that family pension and gratuity are not delayed" and "standard rent bill" were flagged | Both are in the text; flags removed |

---

## 4. Corrections to the source podcast (kept as exam traps)

The script already corrected the source on sub-rule counts. I re-verified each count against the bare text and they are right: **71 → six; 72 → three; 73 → three; 74 → four; 75 → eight; 76 → eight plus 5A; 77(1) → ten clauses plus 77(2); 79 → six; 80 → five; 81 → three; 84 → three.**

Also confirmed: the 8-9-10-11-12-13 mnemonic is unsafe; Form A is superseded for retirees by Form 6-A; the Rule 83 example had to be recomputed (a 30 June retiree's first pension is July's); the September 2025 calendar stages are **9, 10-A, 10-B, 11**; and the O.M. of 30.10.2025 does **not** say family pension starts the next day (that is Rule 81(2)).

---

## 5. Four drafting slips **in the statute itself** (teach the clause, not the pointer)

1. **Rule 75(5)(b)** sends you to "sub-rule (3) of rule 74" for recoverable dues; the dues are in **Rule 74(4)** — 74(3) only says keep copies.
2. **Rule 76(5)(e)** cites "clause (b) of sub-rule (1) of rule 77" for the 10 % withholding (**that is clause (vi)**) and "clause (viii)" for licence fee (**that is clause (iii)**).
3. **Rule 81(2)** prints "clause (d) of sub-rule (2) of rule 76"; the family-pension start date is **76(3)(b)** (and 76(3)(e) for a missing servant).
4. **Rule 76 numbering:** G.S.R. 770(E) of 07.10.2022 says, word for word, *"In rule 76 … for the brackets, figure and words '(5) The fact of the issue', the brackets, figure and words '(5A) The fact of the issue' shall be substituted."* Rule 76 therefore reads (1)–(5), **(5A)**, (6), (7), (8). Reproductions that never carried the duplicate renumber the tail and print those clauses as (6)–(9) — which is exactly why the card images must cite **clause text**, not list position.

---

## 6. What is deliberately *not* over-claimed

* Rules 45, 47, 50, 51, 57, 62, 64, 65, 68 belong to Batches 4–5 and appear here only as cross-references; the reference sheet says so.
* Dynamic figures (dearness relief, GPF rate) are labelled "check the latest O.M." — the rule is permanent, the figure is not.
* Amendment currency is stated as a *negative result limited to the pages searched* (nothing after G.S.R. 410(E) up to 21.10.2026), not as a guarantee.

---

## 7. Language: the answer to your question

> **English on screen, Hinglish narration** — exactly as you chose.

* **On screen:** English only, plain administrative "city English". Every technical term is glossed once (*Head of Office*, *licence fee*, *damages*, *residuary gratuity*, *commutation*, *PPO*, *PDA*, *CPAO*).
* **Voice:** Hinglish in **Roman script** — Hindi grammar, English technical nouns ("*Death ki khabar milte hi woh decide karta hai ki death gratuity deni hai ya family pension*").
* **No Devanagari anywhere.** The build asserts this before it renders a single frame (`assert_no_devanagari()`), so a stray Hindi string cannot slip into a slide or a subtitle.
* **Voice engine:** `en-IN-PrabhatNeural` (teacher) + `en-IN-NeerjaNeural` (student). For a warmer Hindi vowel, swap to `--teacher hi-IN-MadhurNeural --student hi-IN-SwaraNeural`; the script is voice-agnostic.

---

## 8. Visual rebuild, mapped to your screenshot

| Element in your screenshot | In the new build |
|---|---|
| Thin coloured bar at the very top | accent bar, width 8 px |
| "CHAPTER 1 • ART 15(5)…" bordered tab | chapter tab, accent-tinted, rounded |
| One-line white title | title, auto-fits to two lines max |
| Top-right metadata chips | `BATCH 6 • RULES 71-87` and `ENGLISH ON SCREEN • HINGLISH VOICE` |
| Question banner with `Q` circle + "RIYA ASKS" chip | same; chip switches from "RIYA ASKS" to "THE TEACHER EXPLAINS" on answer frames |
| **Four coloured pills** (Art. 15(5)/(6), Art. 16(3), Triple Test, 104/106) | four topic pills: rule reference + a two-or-three-word sub-label |
| **Four detail rows**: coloured label left, key-point right, newest ringed in gold | identical, gold ring + 4 px border on the newest row |
| **Gold "CLASSIC UPSC TRAP" strip** | gold **TRAP** strip, tag chip + single-line trap |
| Segmented progress bar at the foot | accent-coloured segmented bar + `CHAPTER n OF 32` |
| — | **Tables for comparison chapters** (Forms map, retirement vs death, amendment register, key numbers): real 3-column tables, revealed in four beats, vertically centred, longest row ≤ 112 px |

The reference screenshots are in `sample_frames/`.

---

## 9. File manifest

| File | What it is |
|---|---|
| `build_pension_b6.py` | **the updated compiler** — 32 chapters, 128 cards, 4 tables, coverage gate, language gate, Hinglish narration, `--script` / `--coverage` / `--audit` / `--preview` / `--no-tts` / `--part` |
| `pension_b6_reference_sheet.md` | generated: coverage matrix + full examinable wording behind every card + the four drafting slips |
| `pension_b6_narration_script.md` | generated: shooting script — English on-screen line and Hinglish SAY line, card by card |
| `pension_b6_masterclass.mp4` | **the rendered master** — 39 min 27 s, 1920×1080, 24 fps, 33.9 MB, silent bed (see §11) |
| `sample_frames/*.png` | six rendered 1920×1080 frames from the actual build |
| `pension_b6_build/` | build output (slides, audio, clips); git-ignored |
| `../build_pension_rules_batch6_simple_english_video.md` | the original upload, untouched, for diffing |

## 10. Run order

```bash
python build_pension_b6.py --coverage      # rule matrix + density gate (no ffmpeg needed)
python build_pension_b6.py --script        # write the two markdown deliverables
python build_pension_b6.py --preview       # 1920x1080 PNGs for eyeballing
python build_pension_b6.py --no-tts        # silent full render (timing test)
python build_pension_b6.py                 # full build: edge-tts + ffmpeg (libass) -> pension_b6_masterclass.mp4
python build_pension_b6.py --part 2        # render only chapters 12-22
```

Full build needs `edge-tts` (internet) and `ffmpeg`/`ffprobe` with **libass** for the burned-in subtitles. The density gate stops the build before rendering if any card, pill, trap strip or table cell would have to shrink below its legibility floor — so a bad edit can never reach the encoder.

---

## 11. The rendered master

`pension_b6_masterclass.mp4` — **39 min 27 s, 1920×1080, H.264, 24 fps, 33.9 MB**, all 32 chapters, 193 reveal beats, audio stream present.

**Download**

```
https://github.com/khanashraf6742-boop/agency-agents/raw/arena/b90f672d-agency-agents/pension_b6/pension_b6_masterclass.mp4
```

Browsable page (has a Download button): `…/blob/arena/b90f672d-agency-agents/pension_b6/pension_b6_masterclass.mp4`

**Why the audio is silent.** Two sandbox limits, both outside the script:

1. `edge-tts` cannot reach `speech.platform.bing.com` → no synthesis.
2. `uploads.github.com` refuses TLS → no release asset, so the master is committed to the repo and served from the raw URL instead.

The narration itself is finished and committed (`pension_b6_narration_script.md`, 128 SAY lines). Running the compiler on any machine with internet and ffmpeg produces the voiced cut in one command:

```bash
python build_pension_b6.py     # Hinglish neural voices + burned captions + loudness-normalised master
```

**Encoder settings used for this master** (all overridable):

| Setting | Value | Why |
|---|---|---|
| `--fps` | 24 | stills need nothing faster; 24 fps with `-tune stillimage` cut the file from 41.5 MB to 33.9 MB for the same 39 minutes |
| `--clip-crf` | 23 | per-slide clips stay flat, so quality loss is invisible |
| silent bed | 24 kHz mono, 24 kbps | ~0.4 MB for a 39-minute file instead of ~60 MB |
| `--no-subs` | auto-on with `--no-tts` | captions would have no timings to follow; the cards already carry the text |

Regenerate with `python build_pension_b6.py --no-tts` (≈6 min 30 s on 2 vCPU).
