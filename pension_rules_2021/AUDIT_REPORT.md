# Senior-professor audit — CCS (Pension) Rules 2021, Batch 1 (Rules 1 to 10)

**Audited file:** `build_pension_rules_batch1_simple_english_video.md` (v1, 32 chapters, 2x2 box slides)
**Upgraded file:** `build_pension_r1_10_v2.py` (31 chapters, screenshot-style row cards + 4 tables + 1 chart)
**Rule set audited:** Rule 1 to Rule 10 = Chapter I (Preliminary) and Chapter II (General Conditions), plus the Explanation to Rule 2 and the Explanations inside Rules 3, 7, 8 and 9.
**Audit date:** 24.10.2026

---

## 0. Language decision (your open question)

| Layer | Language | Why |
|---|---|---|
| On-screen text (banners, titles, chips, row cards, tables, trap strips) | **English, plain "city English"** | These are the notes a reader screenshots. Rule numbers, provisos and definitions must appear exactly as an examiner expects them, so English only. |
| Narration | **Hinglish in Roman script, zero Devanagari** | Explains the English card in the spoken register your audience actually thinks in. Roman only, so it renders in DejaVu/any subtitle font and never breaks the ASS subtitle engine. |
| Subtitle track | Transcribes the narration (Hinglish) | Matches the audio word-for-word, so it doubles as a transcript. |

This is what v2 does: every scene has an English `rows`/`table`/`bars` block for the screen and a separate Hinglish `hi` string per card for the voice. The two are never mixed on the same line.

---

## 1. Verdict

| Test | Result |
|---|---|
| Rule coverage, Rule 1 to Rule 10 | **100 %** — all 10 rules, all sub-rules, all provisos, both Explanations sets |
| Sub-rule / clause coverage | **53 of 53** print-available units accounted for, including 8 exclusions, 6 Explanation limbs, 26 definitions |
| Gaps found in v1 | **20** (6 missing entirely, 9 half-stated, 5 mis-attributed) |
| Factual errors in v1 | **5**, all corrected (see §3) |
| Non-obscure check | **Passed** — every card states *what the rule does*, not just *that it exists*; every chapter ends with a usable trap |
| Density check | **Passed** — `--audit` proves no card needs a font below the floor, so nothing silently shrinks or clips |
| Honesty of sourcing | **Passed** — 4 items stay flagged as unread (Rule 87, Rule 44 figure, G.S.R. 775(E) date, G.S.R. 410(E) 120-day date) and are printed as `FLAG` on screen |

---

## 2. The 20 gaps in v1 → where they are fixed now

| # | Rule unit | What v1 missed | Fixed in |
|---|---|---|---|
| 1 | **Preamble** of G.S.R. 868(E) | Never stated the enabling power at all | Ch 1 row 1 (Art. 309 proviso + Art. 148(5) C&AG) |
| 2 | **R2 Expl. limb (2)** | Gave the two alternative routes but dropped the closing condition — that all other conditions for counting that earlier service must also be met | Ch 4, row "LIMB (2) — THE CONDITION" (`TRAP` pill) |
| 3 | **R2 Expl. limb (5)** | Printed "UNVERIFIED: Rule 10 of the NPS Rules" — now confirmed against the NPS Rules 2021 (G.S.R. 227(E) of 30.03.2021) | Ch 6, whole chapter, `NEW` pill |
| 4 | **R6(2)** | Said "a re-employed pensioner gets no separate pension", but omitted the **four categories** (superannuation / retiring / compulsory retirement / compassionate allowance after dismissal or removal) | Ch 15, row "RULE 6(2) — FOUR CATEGORIES" |
| 5 | **R7(1)(b) proviso** | The Rule 7 chapter promised "floor = Rule 44 minimum" in its hook but never stated the proviso itself | Ch 16, row "7(1)(b) — THE FLOOR" |
| 6 | **R7(4)(c)** | Missing: undertaking in **duplicate** on transfer, one copy in the service book with an entry | Ch 17, folded into row "7(4)(b) AND (c)" |
| 7 | **R7 Explanation (b) to (e)** | Only the pension = family pension limb was given; serious crime, grave misconduct, publication and information were left out | Ch 17, row "THE EXPLANATION (a) TO (e)" |
| 8 | **R8(4)(d)** | Missing the crucial exception: where misconduct is only *under investigation* or *contemplated*, provisional pension does not apply and full pension plus gratuity issue under Rule 63 | Ch 21, row "8(4)(d) — THE EXCEPTION" |
| 9 | **R8(5)** | Missing the **no-recovery** rule where the final pension is lower than the provisional pension | Ch 21, row "8(5) — THE ADJUSTMENT" |
| 10 | **R8(9)** | v1 treated 8(6A) as base text and never noticed the sub-rule (9) cross-reference | Ch 22 — 8(9) communication added to the one-third row, and the anomaly gets its own `FLAG` row |
| 11 | **R9 Explanation (a)(i)** | No definition of commercial employment at all — no agent, no co-operative society office, no directorship, no partnership, and no carve-out for wholly/substantially Government-owned bodies | Ch 24, three rows |
| 12 | **R9 Explanation (a)(ii)(A)–(C)** | Consultancy/practice was one vague line | Ch 24, row "EXPL. (a)(ii) — PRACTICE" with all three limbs |
| 13 | **R9 Explanation (b)** | Missing: on re-employment without break, "date of retirement" means the date of **final** cessation (this moves the one-year clock) | Ch 24, last row |
| 14 | **R9(3) Explanations** | Two explanations inside 9(3) were never quoted: "conflict of interest" excludes normal economic competition; "far in excess" excludes industry buoyancy | Ch 25 table, rows (c) and (f) plus the trap strip |
| 15 | **R9(6)(ii)–(iv)** | Only directorship/consultancy was named; the encouragement of scientific/cultural work, liberal non-Government posts, and the honorary = paid = self-employment rule were dropped | Ch 26, row "9(6) — LIBERAL GRANTS" |
| 16 | **R9(7) proviso** | Missing show-cause protection before a worse order on representation | Ch 26, row "9(7) — THIRTY DAYS" |
| 17 | **R9(8) two provisos** | Missing show-cause, and the three mandatory factors (financial circumstances, nature and emoluments of the job, any other factor) | Ch 26, row "9(8) — BREACH" |
| 18 | **R9(9)** | Missing: every Rule 9 order must be **communicated** | Ch 26, row "9(9) — COMMUNICATION" |
| 19 | **R10(1) tail** | Missing "or for such longer period as the Government may direct" — the phrase that makes Rule 10 harsher than Rule 9 | Ch 27, row "10(1) — THE CONSEQUENCE" |
| 20 | **R5(2) proviso** | Missing: if the servant was on leave, absent or under suspension, the day of retirement/death stays inside that leave/absence/suspension | Ch 14, row "THE PROVISO" |

---

## 3. Five factual errors in v1, corrected

1. **"6 Explanations" under Rule 2.** The Rules print **one** Explanation containing **six numbered limbs**. v2 labels them "limb (1) … limb (6)" and adds an exam line telling the student not to write "Explanation 5".
2. **Rule 8(6A) treated as base text.** It was inserted by **G.S.R. 770(E) of 07.10.2022**. v2 shows it as an amendment (`NEW` pill) and keeps the 2022 notification as the authority for the three-authority structure of Rule 8(1).
3. **"President" in Rule 7.** v1's hook was right but two cards drifted. v2 states the Appointing Authority in the label, the body and the trap, and contrasts it with Rule 8's three authorities in a comparison table.
4. **Rule 3 clause letters.** The printed copy runs the Pension Payment Order and Qualifying Service definitions as (v) and (w), with Retirement Benefits (x), Service Book (y), Treasury (z). v2 uses that order and adds a note that PPO includes e-PPO.
5. **Rule 87 cited as confirmed.** v1 used the repeal in an answer-shaped card while marking it unverified. v2 keeps the point but flags it as Batch 6 material, so a student never quotes it as read text.

---

## 4. What the visual layer now does (matching your screenshot)

* **Top module bar** — `MODULE 01/31`, scrolling topic ticker, check date, voice badge.
* **Section banner** — full-width, one line, chapter name.
* **Big title** — one line, never wraps (audited).
* **Four anchor chips** — the four ideas of the chapter, each with a one-line gloss.
* **Row cards** — one full-width bordered row per sub-rule / clause / proviso, coloured spine on the left, coloured label, generous English body, and a `EXAM / TRAP / FLAG / NEW` pill on the right so the student can rank what to memorise.
* **Yellow trap strip** — `CLASSIC UPSC TRAP:` line at the foot of every chapter, always two lines maximum.
* **Segmented progress bar** — one segment per chapter, filled as the reveal advances.
* **Three special layouts:** a **table** for Rule 2 exclusions, Rule 7 vs Rule 8, Rule 9(3) factors and the amendment chart; a **grouped bar chart** for every time limit (days / months / years, each group scaled to itself, value printed on every bar); a **question slide** with the chapter's row map and the trap preview.

Reveal policy: rows appear one by one with the narration, at **final size from the first frame**, so nothing shifts or reflows mid-sentence. The trap strip appears with the last row and gets its own spoken beat.

---

## 5. What is still honestly unverified (printed as flags, not hidden)

| Item | Why it stays open |
|---|---|
| Rule 87 verbatim | Batch 6 material; only its effect is asserted |
| Rule 44 minimum pension (reported Rs 9,000) | Rule 44 not read in this batch; the figure is a secondary report |
| G.S.R. 775(E) exact date (Sept 2026) | Garbled in the copy read |
| G.S.R. 410(E) commencement (16.11.2024, 120 days) | Month arithmetic supports it; publication date rests on a secondary source |
| Rule 8 sub-rule (9) | Cross-referred by 8(4)(d) but not printed in the rule — flagged as a drafting anomaly rather than invented |
| Fresh DoPPW O.M.s after 22.06.2026 | Not exhaustively searched; doppw.gov.in and eGazette were not readable in this pass |

---

## 6. Run it

```bash
pip install Pillow edge-tts                 # ffmpeg + ffprobe with libass also on PATH
python build_pension_r1_10_v2.py --audit    # density + narration + coverage check, no ffmpeg needed
python build_pension_r1_10_v2.py --preview  # 212 slide PNGs only
python build_pension_r1_10_v2.py --no-tts   # silent timing test
python build_pension_r1_10_v2.py --only c06_rule2_expl5_nps   # one chapter
python build_pension_r1_10_v2.py --part 2   # chapters 11-20 only
python build_pension_r1_10_v2.py            # full MP4, Hinglish narration + burned subtitles
```

`--audit` exits non-zero if any card, chip, table cell or trap line would need a font below its floor, so a dense edit can never ship as unreadable text.

Outputs: `pension_b1_rules_1_to_10_city_hinglish.mp4`, `pension_b1_reference_sheet.md` (every card + every spoken line), `previews/*.png`.
