# Audit Report — CCS (Pension) Rules 2021, Batch 3 (Rules 31–41)
### Reviewer's note, clause by clause, against the verbatim Gazette text

**Deliverable audited:** `build_pension_rules_batch3_simple_english_video.md` (the Python compiler, 1,513 lines, 26 chapters, 105 cards).
**Reference used for this audit:** the verbatim Gazette text of the CCS (Pension) Rules, 2021 carrying **Chapter IV (Rules 31–32)** and **Chapter V (Rules 33–41)**, read from the CAG-hosted copy of the notification (`agwb.cag.gov.in/.../Circular_CCS_Pension_Rules_2021.pdf`), not from a page-summarising tool.
**Scope rule:** every rule number mentioned in the file, from the **first** mentioned (§31) to the **last** mentioned (§41), plus the provisions those rules cross-refer to (Rule 44, Rule 45, FR 9(21)(a)(i), FR 56).

---

## 1. Verdict in one paragraph

The previous build was **structurally sound and unusually honest** — it tracked 105 cards, flagged what it had not read, and avoided invented case law. But measured against the Gazette it was **not clause-complete**. Of the **134 discrete provisions** that Rules 31–41 actually contain, **21 were missing or materially under-specified**, and **four cards carried "not verified" flags on points the Gazette text settles in one sentence.** Three of the 21 gaps were in Rule 31 alone, where sub-rules (3), (6), (8) and (9) had been compressed into a six-word list ("higher post during leave; … re-employed pensioner; converted PSU") and thereby lost every operative condition. Two whole families of clauses — **Rules 37(30)–(31) and 38(26)–(29)**, including the **51 % disinvestment safeguards** and the **Prasar Bharati carve-out** — had **no card at all**. The build is now **clause-complete for Rules 31–41** — **134 of 134 provisions tracked, 0 left open** — with the rupee amounts in §6 still flagged as figures to date rather than facts to assert.

---

## 2. Coverage matrix

| Rule | Provisions tracked | Already covered | **Added / rewritten** | Still open | Outside this batch |
|---|---|---|---|---|---|
| 31 | 15 | 9 | **6** | 0 | 0 |
| 32 | 9 | 7 | **2** | 0 | 0 |
| 33 | 1 | 1 | 0 | 0 | 0 |
| 34 | 4 | 4 | 0 | 0 | 0 |
| 35 | 10 | 10 | 0 | 0 | 0 |
| 36 | 10 | 10 | 0 | 0 | 0 |
| 37 | 28 | 24 | **4** | 0 | 0 |
| 38 | 21 | 14 | **7** | 0 | 0 |
| 39 | 16 | 14 | **2** | 0 | 0 |
| 40 | 6 | 5 | **1** | 0 | 0 |
| 41 | 7 | 7 | 0 | 0 | 0 |
| 44 (cited) | 2 | 2 | 0 | 0 | 0 |
| 42, 43, FR 56 (cited only) | 3 | 0 | 0 | 0 | **3** |
| **Total** | **134** | **110** | **22** | **0** | **2** |

Reproduce with `python build_pension_b3.py --audit` — it prints the full matrix, provision by provision, then fails (exit 1) if any card is over the type budget.

---

## 3. What was missing, and what the Gazette says

### 3.1 Rule 31 — the definition rule lost its conditions

| Clause | What the old card said | What the Gazette says | Where it now lives |
|---|---|---|---|
| **31(3)** | "higher appointment during leave" | The higher-post **emoluments count only if it is certified that he would have continued to hold that higher appointment but for his proceeding on leave** | Ch 26 |
| **31(6)** | "deputation to an ex-cadre post" | An ex-cadre post **in the same or another Department, OR the Armed Forces of India**; plus a **proviso**: on leave after release from the ex-cadre post, the **parent-department** pay counts | Ch 26 |
| **31(8)** | "re-employed pensioner" | Only where the pensioner **elected to retain** his earlier pension **and** his re-employment pay was reduced **by not more than that pension**; the pension element that reduced the pay is emoluments | Ch 26 |
| **31(9)** | "converted PSU" | Only where the servant **opts to retain the Government pensionary benefits**; then PSU/body pay is emoluments — the **option is the trigger** | Ch 26 |
| **31(11)** | "died while a penalty cut his pay" | The penalty must reduce pay **only during its currency**, with pay restored on expiry; a permanent/cumulative reduction is outside both 31(11) and 32(6) | Ch 26 |

### 3.2 Rule 32 — the fraction machinery was asserted, never written

The old card said "a month = 30 days" and moved on. The **Illustration** actually attached to Rule 32(3) does the arithmetic, and it is examinable:

> retires 16 July 2019 → **nine full months + 14/30 of September 2018 + 16/30 of July 2019 = ten months**; and *"this formula shall also apply in the case of the month of February, irrespective of whether the month has twenty eight days or twenty nine days."*

That is **two separate provisions** (the fraction illustration, and the February rule) that were compressed into five words. They are now a dedicated chapter (Ch 27) with a situations/divisor table.

### 3.3 Rules 37 and 38 — two entire clause families were absent

| Clause | Provision | Why it matters |
|---|---|---|
| **37(30) / 38(27)** | On **51 % or more disinvestment** the Government **shall** specify adequate safeguards for absorbed employees | A mandatory duty, not a discretion |
| **37(31) / 38(28)** | What those safeguards must contain: VRS or continued service, benefits on Government or PSU/body terms by the employee's option, assured earned pension with relaxation of qualifying service | The rule supplies the menu; the old build had nothing |
| **38(26)(a)–(c)** | PF balance and leave balances transfer to the body; a **later dismissal by the body does NOT forfeit** Government-service benefits, and the Ministry reviews | The mirror image of the 2025-amended Rule 37(29)(c) — the contrast *is* the exam point |
| **38(29)** | Nothing in Rule 38 applies to **IIS / CSS officers**, or to persons on cadres outside Akashvani and Doordarshan serving in them | The **Prasar Bharati carve-out**; Rule 37 has no such carve-out (its carve-out is BSNL/MTNL, 37(26)–(28)) |

Also repaired inside the existing chapters: **Rule 38(1)–(13)** was a two-line summary; the full mechanics (en-masse transfer, the three clocks, deeming, abolition of posts, two-year repatriation, option (a)/(b) split at 38(11)–(38)(13)) now appear in the full-wording text behind the card.

### 3.4 Four "not verified" flags that the text closes

| Flag on the old card | Gazette wording | Result |
|---|---|---|
| Rule 37(2): *"whether the three months run from notification of the rules or from the communication … not confirmed"* | **Two clocks**: the PSU is to *ask* within 3 months of notifying its rules, and the servant is to *opt* within 3 months of that communication | **Closed** — Ch 29 |
| Rule 39(4): *"only the recorded age is confirmed"* | Both the age from **official records** and the age in the **service book** go to the medical authority, with a copy of the request to the servant | **Closed** — Ch 29 |
| Rule 39(9): *"before or after appointment not checked"* | *"examined … **either before his appointment or after his appointment** … and declared fit"* | **Closed** — Ch 29 |
| Rule 40(2): *"original, appellate and review orders: not seen"* | *"whether **original, appellate or in exercise of power of review**"* | **Closed** — Ch 29 |

A house rule was added to the file: **"not verified" never means "wrong"** — it means the wording had not yet been seen. **Five flags are now closed** (three clocks in 37(2), two ages in 39(4), either timing in 39(9), three order-types in 40(2), and the 2026 proviso to 37(7)); only the rupee figures stay flagged (§6).

---

## 4. Teaching quality — was it obscure?

The old narration was accurate but **lexical rather than explanatory**: it named the sub-rule and moved on, and it repeatedly used register that a first-time candidate cannot decode ("notional", "ex-cadre", "capitalised value", "unqualified resignation") without a gloss. Three fixes were applied throughout:

1. **Every technical word now gets a plain gloss at first use** — emoluments → "the pay figure on which pension is worked out"; deemed → "treated as if"; ex-cadre → "outside his own cadre"; capitalised value → "the lump sum equal to the pension paid in the future"; unqualified resignation → "resignation without conditions attached".
2. **Every chapter now ends in a decision line, not a summary** — e.g. Ch 31 answers "which way does two-thirds point?" with a drawn chart, because the exam failure is *direction*, not arithmetic.
3. **Traps were converted from warnings into comparisons** — Rule 36 vs 35 vs 37 vs 38 now share one grid (Ch 30), and Rule 40 vs 41 share one chart (Ch 31), so the difference is seen rather than remembered.

No invented case law was added. Every example is labelled **invented** where it is invented, and the four arithmetic corrections from the previous build (Bilal's 7,70,000 ÷ 10; the 38,611.5 → 38,612 rounding; the 77,500 correction to Case 1; 33,333.33 → 33,334) were re-checked and stand.

---

## 5. What the file now is

| | Before | **After** |
|---|---|---|
| Chapters | 26 | **32** |
| Cards | 105 | **130** |
| Provisions tracked | none (prose flags only) | **134, machine-checked** |
| Layouts | one (four cards in a grid) | **dashboard, table, chart** |
| Narration | English | **Hinglish (Roman script only)** |
| On-screen language | English | English (unchanged) |
| Devanagari characters in the file | 0 | **0** (asserted by the audit script) |
| Structure guard | id uniqueness | id uniqueness + colour validity + tuple width + **type-density fail** |

Six new chapters were spliced in **before** the recap, and the recap was renumbered to Chapter 32 so it stays last:

| New chapter | Purpose | Layout |
|---|---|---|
| **26** Rule 31(3), (6), (8), (9), (11) — the five conditions | closes the Rule 31 gaps | dashboard |
| **27** Rule 32(3) fractions — 14/30, 16/30, February | the arithmetic everyone skips | **table** |
| **28** Rules 37(30)–(31), 38(26)–(29) | the clauses nobody quotes | dashboard |
| **29** Four flags now closed | audit transparency as content | **table** |
| **30** Rules 35/36/37/38 on one grid | stops the four absorption rules blurring | **table** |
| **31** Two-thirds, drawn | floor vs ceiling, seen not remembered | **chart** |

Extra dashboard furniture added to match the reference frame: meta strip with `nn/32` + chapter slug + audio meter, violet citation pill, badge chip, **four accent tiles**, labelled ledger rows, amber **KEY TAKEAWAY** row, amber **CLASSIC UPSC TRAP** band, per-chapter progress ticks, and a NEXT footer.

---

## 6. What was the last open flag — and how it closed

**G.S.R. 775(E)**, the proviso inserted below Rule 37(7), was the one provision this audit carried as `OPEN`. It is now read in full and carded (Ch 13, card 4), and the matrix marks it `COVERED`. The operative words:

> *"Provided that nothing in this sub-rule shall be applicable to the employees (other than OF Schools and OF Hospitals) of erstwhile Ordnance Factory Board who do not opt for absorption in DPSUs, such employees shall continue to be on deemed deputation till retirement to the DPSUs, created from the conversion of its production units, on terms of foreign service without any deputation allowance."*
>
> — CCS (Pension) Amendment Rules, 2026, notified **2 September 2026**, published **7 September 2026**, File No. 4/27/2026-P&PW(D).

The examinable content is the **negative space**, and the build says all three parts out loud: the opt-out must come from an **erstwhile Ordnance Factory Board** employee; **OF Schools and OF Hospitals are excluded** from the protection; and the consequence is not pension but **status** — deemed deputation *till retirement*, on foreign-service terms, **without** deputation allowance.

Two cautions remain in the script, and neither is a coverage gap:

1. **Money figures** — Rs 9,000 minimum, Rs 1,25,000 maximum, Rs 54,000 medical threshold. Nothing in Rules 31–41 fixes these; they come from Rule 44 and the latest amending O.M. Every card that quotes them carries "check the latest O.M.".
2. **Whether Rule 44(9) rounding reaches a provisional pension** (Rule 40(3)) — the rule text does not say. The Suresh example gives 33,334 with the rounding shown and the caveat attached.

So the honest audit line is now: **132 covered + 0 open + 2 outside the batch (Rules 42–43, FR 56, held for Batch 4).**

---

## 7. Language decision (as chosen)

| Layer | Language | Notes |
|---|---|---|
| **On-screen board** | **English** — Indian urban register, short labelled phrases | unchanged from your choice |
| **Narration** | **Hinglish, Roman script only** | never Devanagari; "Rule thirty-one, sub rule teen me ek condition chhupi hai" |
| **Subtitles** | the spoken Hinglish | cut from the neural voice's word boundaries, so they stay in sync |
| **TTS normaliser** | leaves Roman Hinglish alone, rewrites only references and acronyms | `Rule 37(29)(c)` → "Rule 37, sub rule 29, clause c"; `UPSC` → "U.P.S.C."; `Rs.` → "Rupees" |

Voices: teacher `en-IN-PrabhatNeural`, student `en-IN-NeerjaNeural`, rate `+6%` — the same en-IN pair the previous build used, so the Hinglish phonetics land without an accent switch.

---

## 8. How to run, and what has already been proved to work

```bash
python build_pension_b3.py --verify     # says which ffmpeg / ffprobe / libass this machine gets
python build_pension_b3.py --audit      # matrices + type-budget gate, no ffmpeg, no internet
python build_pension_b3.py --preview    # 32 PNGs of the finished board
python build_pension_b3.py --no-tts     # silent dry run: real layout, real timing
python build_pension_b3.py --part 2     # middle third only
python build_pension_b3.py --layout table   # force one layout everywhere
python build_pension_b3.py --only c3_13_rule37_chain
python build_pension_b3.py --captions soft   # captions as a track instead of burned in
python build_pension_b3.py              # full build: edge-tts + ffmpeg with libass
```

Output: `pension_b3_masterclass.mp4` (1920×1080, H.264 + AAC, burned-in Hinglish subtitles, loudness-normalised to −16 LUFS), plus `pension_b3_reference_sheet.md` — the full-wording sheet behind every card, ~59,000 characters.

### Tooling robustness (added this round)

| Problem | Handling |
|---|---|
| System `ffmpeg` not installed | Falls back to the static ffmpeg 7.0.2 shipped by the `imageio-ffmpeg` wheel; `--verify` prints the exact binary |
| `ffprobe` missing | Durations are parsed out of `ffmpeg -i`'s own progress report, so clip length still equals audio length to the frame |
| ffmpeg without libass | `--captions burn` degrades to a soft subtitle track automatically, with a printed note |
| Voice engine unreachable | The build **stops with exit code 2 and an explicit message** instead of quietly shipping a silent film; `--no-tts` is the deliberate way to rehearse offline |
| Subtitle collisions | Cues sit in their own lane at `MarginV 54` of 1080, **below** the closing band and the trap bar, with the progress strip pinned to the bottom edge; the NEXT footer is suppressed in the film. Verified against the encoded master, not just the slide renderer |
| Rehearsals overwriting a master | `--build-dir PATH` moves slides, audio and clips to a scratch folder, so a dry run can never clobber a real render |

### Render verification actually performed here

* All **226 frames** of the 32 chapters (intro, question, every card reveal, trap, hook) render without a type-budget failure.
* **The whole film was rendered end-to-end** — 32 chapters, 196 segments, 1,279 subtitle cues — through slide → audio → clip → concat → libass burn → loudnorm → MP4:

  | Check | Result |
  |---|---|
  | Duration | **41:57** (silent rehearsal pacing; the voiced build runs shorter, ~33–36 min) |
  | Streams | video h264 High, **1920×1080, 25 fps** + audio aac 48 kHz |
  | Captions | 1,279 cues burned, in a dedicated lane under the closing band, clear of the progress strip |
  | Frames pulled back at 1:35, 10:00, 25:00, 39:10 | chrome, tiles, reveals, trap band and caption lane all correct, nothing overlapping |

* The voice leg could not be exercised in this sandbox because `speech.platform.bing.com` is unreachable from it; that is exactly the failure the new guard reports with exit code 2. On a machine with `pip install edge-tts` and normal HTTPS, `python build_pension_b3.py` runs the voiced build unchanged.

---

## 9. Files in this delivery

| File | What it is |
|---|---|
| **`build_pension_b3.py`** | the updated compiler — 32 chapters, 130 cards, 134-provision audit, 3 layouts, Hinglish track |
| `pension_b3_reference_sheet.md` | the examinable full wording behind every on-screen card (generated) |
| `CCS_PENSION_B3_AUDIT_REPORT.md` | this audit |
| `pension_b3_preview_montage.png` | six finished frames: dashboard, table, chart, trap state, flag table, grid |
