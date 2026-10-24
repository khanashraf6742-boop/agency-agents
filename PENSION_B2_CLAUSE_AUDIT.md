# Clause-by-clause audit — CCS (Pension) Rules 2021, Chapter III (Rules 11 to 30)

**Build audited:** `build_pension_b2.py` (Revision 3, 24 October 2026 — English on screen, Hinglish narration)
**Auditor's stance:** treat the chapter as a statute, not as a summary. Every sub-rule, proviso and Explanation must either be taught on screen or be flagged as not read. Anything in between is a defect.
**Result:** 20 rules, **81 statutory units**, all 81 now taught. Two substantive gaps were found and filled; four stale "unverified" flags were closed with the actual text.

---

## 1. Method (this audit can be re-run)

Full Chapter III text was read end to end (Rules 11 to 30, every sub-rule, every proviso, every Explanation), not a summary. The script now carries a machine-readable ledger:

```python
CLAUSE_LEDGER = [("14", "14(2) reciprocal arrangement", r"14\(2\)"), ...]   # 81 lines
python build_pension_b2.py --audit
```

`--audit` prints two tables: the on-screen density of every chapter, and unit coverage rule by rule, ending in `ALL CLAUSES TAUGHT` or a list of what is missing. The audit is therefore evidence, not assertion: anyone can re-run it after an edit.

---

## 2. Coverage verdict, rule by rule

| Rule | Units in the statute | Taught | Verdict |
|---|---|---|---|
| 11 | main + proviso 1 + proviso 2 | 3/3 | Correct. "Same or another service or post", and nothing before 18 except Rule 20 military service, both stated. |
| 12 | main + Explanation | 2/2 | Correct. Duties **and** pay, Consolidated Fund of India or Local Fund, and the exclusion of an establishment without a non-contributory scheme. |
| 13 | 13(1), proviso, 13(2), Explanation, 13(3) | 5/5 | Correct. Proper permission is taught as two limbs, and the Centre bears the whole cost. |
| 14 | 14(1), (a), (b), (c), (d), 14(2), Explanation, 14(3) | 8/8 | **Was defective — fixed.** 14(2) and the Explanation were flagged "not confirmed" and never taught. Both are now read and taught (Chapter 6). |
| 15 | main + scheme reference | 2/2 | **Was over-flagged — fixed.** The rule itself names the 1993 Casual Labourers Scheme and the notifying department (DoPT). The flag now covers only the 1993 order number and date. |
| 16 | probation and confirmation | 1/1 | Correct. |
| 17 | apprentice, two exceptions | 1/1 | Correct (Subordinate Accounts Service, IA&AD or Defence Accounts). |
| 18 | (i) contract limb, (ii) CPF refund limb | 2/2 | Correct. Both limbs cumulative, no break in duty. |
| 19 | 19(1), 19(2)(i)–(iii), 19(3), 19(4), 19(5), Explanation | 8/8 | Correct. 19(2)(ii) is the **pension** element (the source wrongly said gratuity); 19(2)(iii) set-off restored; capital value / commutation table explained. |
| 20 | 20(1), Expl. 1(i)–(iii), Expl. 2, Expl. 3, 20(2), 20(3), 20(4), 20(5) | 10/10 | Correct and current. Post-07.10.2022 wording ("was to be refunded") is marked as the operative text; the old wording is kept only as history. |
| 21 | main, proviso, Explanation | 3/3 | Correct, including the "silence means it counts" rule and the six-month limit for a late entry (six-month method itself flagged as assumed). |
| 22 | 22(1) to 22(4) | 4/4 | Correct, including regularisation of excess interruption by EOL. |
| 23 | 23(1), 23(2), 23(3) | 3/3 | Correct, and the authority is the **Competent Authority**, not the appointing authority. |
| 24 | dismissal and removal | 1/1 | Correct, including the warning that compulsory retirement is not named. |
| 25 | 25(1), 25(2) | 2/2 | Correct: gap counts only if regularised as duty or leave by a specific order of the reinstating authority. |
| 26 | 26(1) to 26(8) | 8/8 | Correct. Eight sub-rules (the source said twenty-six); 26(6) "body controlled or financed by Government" limb restored; 26(8) Rules 35/36 limb added. |
| 27 | 27(1)(a)–(e), 27(2) | 6/6 | Correct. The "five exceptions, two conditions" mnemonic is labelled a teaching device, not rule text. |
| 28 | 28(1) to 28(6) | 6/6 | Correct, including Defence Services and Railway Estimates, the four excluded causes, and the hearing before refusal. |
| 29 | option (a)/(b) and refund proviso | 1/1 | Correct: the option is the servant's, not the Government's. |
| 30 | 30(1) to 30(5) | 5/5 | Correct. "On each occasion" now confirmed, Format 4 distinguished from Form 6-A, finality and the 31 January report stated. |

---

## 3. What the audit actually changed

**Substantive gaps, now filled**

1. **Rule 14(2) was missing in substance.** It was on screen only as "wording not confirmed". It now appears as its own row: the lump-sum condition binds an autonomous body under a **State** Government only "in accordance with the reciprocal arrangement entered into by the Central Government with the concerned State Government", with the design note that Rule 13(3) puts the cost on the Centre.
2. **The Explanation to Rule 14 was absent altogether.** Now taught as two limbs: previous permission taken before applying, **and** the body's order reciting that the employee resigns to join the Government post with proper permission. The point that an after-the-fact no-objection letter fails is stated.
3. **Rule 15's notifying authority** (Ministry of Personnel, Public Grievances and Pensions, DoPT) is stated from the rule text instead of being flagged.
4. **Rule 26(8) and "on each occasion" in Rule 30(1)** are no longer flagged: the text was read.

**Deliberate non-claims retained (honesty over completeness)**

- Every rule is a **close restatement**, not Gazette or India Code text. That flag stays on the cards.
- The exact day of the September 2025 DoPPW O.M. is illegible; the effective date of G.S.R. 410(E) is unsettled (16.11.2024 on secondary sites against 13.11.2024 on a 120-day count).
- The six-month method used in the Rule 21 example is an assumption.
- G.S.R. 775(E) (Rule 37(7), 2026) belongs to the next batch.

---

## 4. Non-obscure check (is the content understandable?)

| Test | Finding |
|---|---|
| Jargon defined on first use | Pass — qualifying service, gratuity, commutation, capital value, PPO, EOL, NPS, autonomous body all defined where they appear. |
| Exam traps isolated | Pass — one "CLASSIC UPSC TRAP" strip per revision chapter, plus a trap card in every teaching chapter. |
| Numbers kept visible | Pass — 31.12.2003, 50 percent, 36 instalments, 90 days, six months, 18 and 5 years, 31 January. |
| Ambiguity removed | Pass — "silence" is taught three ways (Rules 21, 23, 28); "AND" versus "OR" is explicit in Rules 12 and 23; the cap asymmetry between 19(5) and 20(5) is taught as a pair. |
| Language | English on screen. Narration is Hinglish in Roman script (chosen 24.10.2026). No Devanagari anywhere in the file (only `•` and `—` as typography). |

---

## 5. Visual treatment, matched to the reference screenshot

The reference frame is a dense, dark, banded revision screen. The renderer was rebuilt to that grammar:

| Reference element | Implementation |
|---|---|
| Rounded violet chapter pill along the top | `CHAPTER n • …` pill, violet outline, lavender text |
| Four coloured header panels (Art. 15, 16, 31, 104th) | `layout: "panel"` chapters — four coloured chips with a title and a sub-line |
| Full-width rows: colour label on the left, white text on the right, thin colour bar at the edge | every teaching chapter is now `label + text` rows (405 px label column), one row revealed per narration segment |
| Amber trap strip at the foot | `CLASSIC UPSC TRAP: …` strip, amber fill and border |
| Table look (rows of a statutory map) | Table 1 (counting routes), Table 2 (loss, save, prove), Table 3 (provisos and Explanations) |
| Chart requirement | Bar chart of "share counted" — 100 percent bars, the single Rule 15 half bar, three zero bars |
| Progressive reveal | one row or bar per spoken segment; the newest row gets a yellow halo, as in the reference |

Layout is content-aware: a solver picks the largest body font that fits and then distributes the spare height, so rows are never clipped and never microscopic.

---

## 6. Files delivered

| File | What it is |
|---|---|
| `build_pension_b2.py` | The updated compiler: 34 chapters (28 teaching, 5 revision-visual, 1 recap), 226 narration segments, about 9,800 words (roughly 60 to 70 minutes), clause ledger and density audit built in. |
| `build_pension_rules_batch2_simple_english_video_1.md` | The original Markdown wrapper with the new code block inside. |
| `pension_b2_reference_sheet.md` | Auto-generated: the full wording behind every row and card. |
| `pension_b2_preview/*.png` | Six sample frames showing the new row, panel, table and chart layouts. |

**Run it**

```bash
python build_pension_b2.py --audit      # density + clause coverage, no ffmpeg, no internet
python build_pension_b2.py --preview    # slides only, into pension_b2_build/slides
python build_pension_b2.py --no-tts     # silent dry run (needs ffmpeg on PATH)
python build_pension_b2.py              # full build with edge-tts narration and burned subtitles
```

---

## 7. Language split (Revision 3)

| Layer | Language | Why |
|---|---|---|
| Chapter pills, titles, row labels, row text, tables, chart labels, trap strips, hook strips | **English** | The frame is the examinable text; it must read like a printed revision sheet, as in the reference screenshot. |
| `q_say` (student question) and every narration segment | **Hinglish, Roman script only** | A classroom in an Indian city explains in Hinglish; the choice was made explicitly in this revision. |
| Rule numbers, dates, section words, and legal terms inside the Hinglish | **English** | Keeps the audio quotable: "Rule 19 sub-rule 5", "thirty-first December 2003", "Format 4". |
| `FULL` text in `pension_b2_reference_sheet.md` | **English, unchanged** | So an English answer can still be written straight from the sheet. |

Mechanics: all 226 narration segments were rewritten (9,819 words, about 65 minutes at 150 wpm); dates and numbers are spelled in
words so the en-IN voice reads them cleanly. `--audit` now ends with a **language audit**: it fails on an empty narration, on any
Devanagari character in narration or on screen, and it reports how many segments read as Hinglish (currently 226 of 226).
