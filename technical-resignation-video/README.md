# DoPT Technical Resignation & Lien — Video Masterclass

A 16-chapter, simple-English Q&A explainer video built from the consolidated
**DoPT O.M. No. DOPT-1669266628362 dated 24.11.2022** (Paras 2.1 to 5).

* **16 chapters · 64 exam-ready cards · 16 min 19 s · 1920×1080**
* Embedded chapter markers (16) — players show a navigable chapter list
* Riya (student) asks one question per chapter; the teacher answers card by card
* Every chapter closes on a yellow **"trap / remember"** strip
* Indian-English narration, colour-coded burned-in subtitles, 1920×1080

```
00:00  Title card + course roadmap
Ch 1–8   Technical resignation: definition, pre-joining applications, leave,
         LTC, pay protection, seniority, pension/NPS/GPF, service book
Ch 9–13  Lien: definition, retention, the 2+1 year rule, termination, transfer
Ch 14–15 Joining time & pay, Transfer T.A. and the 3-year bar
Ch 16    Master recap + the 8 constituent O.M.s
```

---

## Files

Two cuts of the same recording are shipped — the voice is identical in both:

| File | Length | What changed |
|---|---|---|
| `tech_resignation_masterclass.mp4` | **16 min 19 s** | **The final file.** Inter-card padding tightened (0.45→0.18 s after a card, 0.85→0.32 s after a question). Voice speed untouched. |
| `tech_resignation_masterclass_brisk.mp4` | 15 min 06 s | The tightened cut played back at 1.08× (`setpts` + `atempo`), pitch preserved. Chapters rescaled to match. Use this for repeat revision. |

Nothing was re-recorded to make either one. Padding is only ~6 % of the runtime, so
trimming it reclaims ~36 s; the brisk cut is where the remaining 73 s comes from.

| File | What it is |
|---|---|
| `build_technical_resignation.py` | Everything: scene data + slide renderer + subtitle/mux engine |
| `tech_resignation_reference_sheet.md` | Full official wording behind every card (auto-generated) |
| `narration/` | The exact text sent to the voices, plus `manifest.json` |
| `studio_raw/` | Long voice recordings, one per chapter *(not in git)* |
| `build/` | Slides, per-card audio, clips, alignment report *(not in git)* |
| `tech_resignation_masterclass.mp4` | The finished video *(not in git)* |
| `chapters/ch01…ch16.mp4` | One cut per chapter *(not in git)* |

---

## Rebuilding from scratch

```bash
python3 -m venv .venv && . .venv/bin/pip install Pillow imageio-ffmpeg
export FFMPEG="$(python3 -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')"

python3 build_technical_resignation.py --audit            # layout/density gate
python3 build_technical_resignation.py --preview          # render the 98 slides
python3 build_technical_resignation.py --dump-narration   # write narration/ text
#   -> record each narration/<clip>.txt into studio_raw/<clip>.wav, then:
python3 build_technical_resignation.py --align            # split into per-card audio
python3 build_technical_resignation.py --build --chapter-wise
```

`--audit` is a hard gate: it fails the build if any card title, body, chapter
title, question or hook strip cannot fit its box. It also catches the silent
truncation bug the original template had (a wrapped chapter title used to be
clipped to one line without warning).

---

## How the audio is timed

The narration is recorded as **one long take per chapter** (one per speaker run),
which is what makes it sound natural. The engine then has to decide where each
on-screen card begins. It does that in two steps:

1. **Predict** — split the take by character count, weighted so sentence-ending
   punctuation gets extra time.
2. **Snap** — run `silencedetect` and move each predicted boundary onto a real
   pause, scoring candidates by *pause length − distance*, because the pause
   between beats is reliably longer than a pause between sentences inside a beat.

Measured result across the 98 beats: **14.2–19.9 chars/sec, median 16.7** — i.e.
no beat is mistimed by more than a fraction of a second. `build/alignment_report.json`
holds every cut, duration and snap offset.

The same anchoring is then applied *inside* each beat to time the individual words for
captions: the beat is split at sentence ends and those boundaries are snapped onto
detected pauses. Three models were measured against real speech; the pause-midpoint
anchor is what ships (a pause-*edge* anchor, which looks more principled, measures worse):

| Word-timing model | median error | bias | > 0.5 s |
|---|---|---|---|
| length-weighted only | 0.29 s | −0.23 s | 15 % |
| **anchored to pause midpoint (shipped)** | **0.18 s** | **−0.21 s** | **11 %** |
| anchored to pause edge | 0.25 s | −0.26 s | 12 % |

---

## Pronunciation

`normalize_for_tts()` runs an ordered pass over the **same** text that becomes the
subtitles, so what you hear and what you read never disagree. Order matters —
clause expansions run before bare acronym expansion, or `FR 9(24)` would become
`F.R. 9(24)` and the clause rule could never match.

| Written | Spoken |
|---|---|
| `FR 9(24)` / `F.R. 9(13)` | "F.R. 9 clause 24" / "F.R. 9 clause 13" |
| `Para 2.1.1` | "Paragraph 2.1.1" |
| `lien` | "lee en" |
| `CCL`, `HPL`, `EL` | "child care leave", "half pay leave", "earned leave" |
| `PSU` | "public sector undertaking" |
| `TTA`, `LTC`, `NPS`, `GPF`, `DoPT` | spelled out as letters |
| `yrs` | "years" |
| `24.11.2022` (in the intro) | "twenty fourth November, twenty twenty two" |

---

## Build verification

Every render is checked before it is called done. Measured on the delivered file:

| Check | Result |
|---|---|
| Captions present on every beat | 98/98 |
| Caption baseline (drift = visible jumping) | 59–66 px, median 59 — no outliers |
| Speaker colours | 16/16 Riya beats cyan, 82/82 teacher beats white |
| Beat timing consistency | 14.2–19.9 chars/sec, median 16.7 |
| Dead air (silence > 1.5 s) | none |
| Caption sync vs actual speech | median 0.08 s, p90 0.54 s — captions trail by ~0.2 s |
| Integrated loudness | −16.0 LUFS, true peak −1.0 dBFS, LRA 2.9 LU |
| Streams | H.264 1920×1080@30 + AAC 48 kHz stereo, faststart enabled |
| Chapter markers | 16 embedded and in range |

When re-trimming encoded clips with `-c copy`, ffmpeg rounds each cut **up** to the next
packet boundary (+0.1 s worst case, +8 s cumulative over 98 beats). Any timeline you
compute from *nominal* beat lengths will therefore drift out of sync with the real file —
measure the timeline from the actual clip durations or the QA sweep will report caption
dropouts that are not there.

Two bugs worth remembering, both found by these checks rather than by eye:

* **Captions stacked vertically.** Cues overlapped by 0.1 s at each boundary; libass
  treats overlapping events as a collision and silently shifts them up, so subtitles
  jumped between y≈816 and y≈1018 between cues. Cues now tile the timeline exactly.
* **`resampler=soxr` after `loudnorm` crashes ffmpeg** —
  `Assertion best_input >= 0 failed at src/fftools/ffmpeg_filter.c:1923`. It is
  intermittent (it built the main file, then aborted on chapter 2). Plain
  `aresample=48000` is used instead.

## Content provenance

Rule content is unchanged from the verified source build. Only presentation was
touched in this revision (see the *ENGINE REVISION NOTES* block in the script
docstring). No rule, number, O.M. reference or threshold was altered; the three
narration-only edits were grammar fixes ("technical resign **to**" → "submit a
technical resignation **to take up**").
