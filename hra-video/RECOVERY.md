# RECOVERY STATE — HRA masterclass

## What happened

Between turns the sandbox home directory was reset. `/home/user/hra-video/` (which lived
**outside** the git repo) was wiped completely — both MP4s, all 28 recorded WAV clips,
`build_hra.py`, `scenes_hra.py`, the rendered slides, the README and the reference sheet.
The git repo was also rolled back to its base commit `6910bb8`, so earlier commits were lost.

**Lesson applied:** everything now lives inside `/home/user/agency-agents/hra-video/`.
Untracked files *inside* the repo survive a reset (proved: `technical-resignation-video/`
is untracked and came back intact). Files outside the repo do not survive.

Note: `.venv` and `build/` are snapshot-excluded directory names, so the virtualenv is
named **`tools-venv`** and the build directory is **`work/`** — neither is excluded.

## Recovered (verified)

| Asset | Status |
|---|---|
| `hra_source.pdf` | copied from `/tmp/arena-coding-uploads/` — the original 20-page scan |
| `source_lines.txt` | 949 lines / 4,102 words @220 dpi — matches the pre-loss extraction (950 / 4,102) |
| `source_page_index.json` | page → line ranges |
| `narration_source.py` | **all 28 approved clips, 20,870 chars** — the canonical script |
| `tools-venv/` | Pillow 13, pypdf, pymupdf, cv2 5.0 (headless), rapidocr-onnxruntime, ffmpeg 7.0.2 |
| `../technical-resignation-video/build_technical_resignation.py` | the renderer/slide/mux engine to clone |

The narration is the expensive asset and it is safe. Audio can be re-recorded from it
verbatim; slides and card text are re-derived from it.

## Rebuild plan

1. ✅ narration secured
2. ✅ toolchain rebuilt
3. ✅ source re-OCR'd
4. ⬜ write `scenes_hra.py` — 17 chapters × 4 cards (`short` / `full` / `say`) + `q`/`q_say`
      + `hook`/`hook_say`, plus the one `flow` (`hra_ladder` on `h05`) and `PART_STARTS`
5. ⬜ clone `build_technical_resignation.py` → `build_hra.py`, splice in scenes, patch header
      (title, intro/outro, `hra_reference_sheet.md`, HRA pronunciation rules)
6. ⬜ `--audit` → `--dump-narration` → re-record 28 clips (10/turn platform cap → 3 turns)
7. ⬜ `--align` → `--build --chapter-wise` → brisk 1.08× with rescaled chapters → QA
8. ⬜ deliver

## Verified current-position facts (do not re-research — checked 21 Oct 2026)

| DA band | X | Y | Z | From |
|---|---|---|---|---|
| below 25% | 24% | 16% | 8% | 1.1.2016 — printed in the PDF, **superseded** |
| 25%–50% | 27% | 18% | 9% | 1.7.2021 |
| 50%+ | **30%** | **20%** | **10%** | **1.1.2024 — current** |

- DA = **60%** w.e.f. 1.1.2026 — DoE O.M. 1/1(i)/2026-E.II(B) dated 22.04.2026.
  The 1.7.2026 instalment was **not notified** as of 21.10.2026.
- Floor: Rs **5,400 / 3,600 / 1,800** (X/Y/Z) = 30/20/10% of Rs 18,000.
- **Only two rungs** (25%, 50%) — both passed. No third step.
- O.M. 2/4/2022-E.II(B) is still the governing Master O.M. (newest HRA entry on
  doe.gov.in/orders-circulars/32; no corrigendum).
- Revision is **self-operating** — DoE ID Note 2/5/2017-E.II(B) dated 04.08.2021 says no
  separate order issues at each threshold. That is why no "30%" order exists.
- No Accommodation Certificate **abolished** — O.M. 2/5/2017-E.IIB dated 03.05.2019.
- 8th CPC: constituted 03.11.2025 (Gazette), chair Justice Ranjana Prakash Desai,
  18-month term → report ~May 2027. **No recommendations yet** (Lok Sabha reply 10.08.2026).
  40/35/30% are **staff-side demands, not law**.

## Engine constants to carry into `build_hra.py`

- Layout budgets: `BODY_START/BODY_MIN` 34/26, `TITLE_START/TITLE_MIN` 30/22,
  node title/sub 18/16, hook on one line ≥20 px.
- Pacing: `PAD_QUESTION 0.32`, `PAD_HOOK 0.38`, `PAD_ANSWER 0.18`, `PAD_TITLE 0.55`,
  `PAD_OUTRO 0.70`.
- Encode: `-c:v libx264 -tune stillimage -preset veryfast -crf 17`, audio
  `loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000` + `-b:a 192k` + `+faststart`.
- Brisk: `setpts=PTS/1.08` + `atempo=1.08` + **`-r 30`**, then **manually rescale chapter
  metadata** by 1/1.08 (`setpts` does not remap chapter marks). Reuse the master's exact
  `crf 17 + tune stillimage`, never `crf 20` with no tune.
- Captions: `Default` white 40 px / `Student` yellow 40 px, `\N` wrap ~42 chars.
- `normalize_for_tts()` ordering: clause refs → expansions → `lien`→`lee en` → acronyms →
  dashes to commas → whitespace collapse. Applied to both the TTS request and subtitles.

## HRA pronunciation additions (beyond the technical-resignation lexicon)

`HRA`→"H.R.A.", `DA`→"D.A.", `CPC`→"C.P.C.", `DoE`→"D.O.E.", `IA&AD`→"I.A. and A.D.",
`UA`→"U.A.", `TB`→"T.B.", `DDO`→"D.D.O.", `NGO`→"non-gazetted officer", `Rs`→"rupees",
`km`→"kilometres", Annexure I/II/III → "Annexure One/Two/Three", and O.M. file numbers:
`-E.II(B)`/`E.IIB`→"E two B", `(i)`/`(ii)`/`(iii)`→"sub one/two/three", `/`→"slash".
(Order matters: the Annexure and `-E.II(B)` rules must run **before** the `/` rule.)

## Chapter plan (17 × 4 = 68 cards)

| # | id | chapter strip |
|---|---|---|
| 1 | `h01_scope_of_master_om` | SCOPE OF APPLICATION |
| 2 | `h02_pay_and_family` | PARAS 1.1–1.2 |
| 3 | `h03_same_station_ua` | PARAS 1.3–1.4 |
| 4 | `h04_city_classification` | PARA 2.1 |
| 5 | `h05_rates_and_da_ladder` | PARA 2.1 NOTE (has the `hra_ladder` flow) |
| 6 | `h06_position_today_2026` | CURRENT 2026 |
| 7 | `h07_eighth_cpc` | 8TH CPC STATUS |
| 8 | `h08_place_of_duty` | PARAS 3.1–3.3 |
| 9 | `h09_eight_km_rule` | PARA 3.4 |
| 10 | `h10_who_cannot_draw` | PARAS 4.1–4.5 |
| 11 | `h11_transfer_retention` | PARAS 4.6–4.9 |
| 12 | `h12_sharing_rules` | PARAS 5.1–5.4 |
| 13 | `h13_guest_house` | PARA 5.5 |
| 14 | `h14_during_leave` | PARA 6.1 |
| 15 | `h15_other_circumstances` | PARAS 6.2–6.9 |
| 16 | `h16_certificates` | PARA 7 |
| 17 | `h17_master_recap` | RECAP |

`FLOWS` = one entry, `hra_ladder` (4 nodes / 3 edges: 24% → 27% → 30% → TODAY).
`PART_STARTS = ["h01_scope_of_master_om", "h05_rates_and_da_ladder", "h10_who_cannot_draw",
"h14_during_leave"]`

## Voices

Teacher = `voice-00`, student (Riya) = `voice-01` — the Indian-accent pair the user chose
for the technical-resignation video. Confirmed still valid.
