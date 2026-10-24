# Pension Batch 2 — production package

CCS (Pension) Rules 2021 · Chapter III (Qualifying Service) · Rules 11 to 30
**English on screen · Hinglish narration (Roman script)**

---

## 1. What is in this package

| File | Use |
|---|---|
| `build_pension_b2.py` | **The production file.** One self-contained Python script that renders all slides, generates the Hinglish voice-over, burns subtitles and muxes the MP4. |
| `build_pension_rules_batch2_simple_english_video_1.md` | The same script inside the original Markdown wrapper (archive copy). |
| `pension_b2_reference_sheet.md` | Auto-generated English full wording behind every row and card — your answer bank. Regenerated on every run. |
| `PENSION_B2_CLAUSE_AUDIT.md` | The clause-by-clause audit: 20 rules, 81 statutory units, verdict table, language split. |
| `pension_b2_preview/*.png` | Six sample frames showing the final look (rows, table, chart, panel). |

---

## 2. Requirements

- Python 3.9 or newer
- `ffmpeg` and `ffprobe` on PATH, **with libass** (needed for burned subtitles)
- Internet on the first run only: `edge-tts` is used for narration
- Pillow (the script installs it automatically if missing)

```bash
# Debian / Ubuntu
sudo apt install ffmpeg python3-pip
# Windows: install ffmpeg (gyan.dev build includes libass) and add it to PATH
```

---

## 3. Commands

```bash
python build_pension_b2.py --audit      # no ffmpeg needed: density + clause ledger + language audit
python build_pension_b2.py --preview    # slides only, into pension_b2_build/slides
python build_pension_b2.py --no-tts     # silent dry run, checks timing and encode
python build_pension_b2.py              # full build -> pension_b2_masterclass.mp4
python build_pension_b2.py --part 1     # one third of the chapters (1, 2 or 3)
```

Optional voice control:

```bash
python build_pension_b2.py --teacher en-IN-PrabhatNeural --student en-IN-NeerjaNeural --rate -4%
```

---

## 4. Expected output

| Property | Value |
|---|---|
| Chapters | 34 (28 teaching, 5 revision-visual, 1 recap) |
| Slides | 226 frames, 1920 × 1080 |
| Narration | 9,819 words, roughly 60–70 minutes at the default rate |
| Video | H.264, yuv420p, 30 fps, AAC 192 kbps, loudness normalised to −16 LUFS |
| Subtitles | Burned in from a generated `.ass` file (word-timed from edge-tts boundaries) |
| Progress bar | Bottom strip advances one segment per slide |

---

## 5. Before you publish — the honest flags

These are carried on the cards themselves; do not delete them from the video.

1. Every rule is a **close restatement** of Chapter III, not verbatim Gazette text. The full chapter was read from a
   reproduction, not the Gazette PDF.
2. The exact **day of the September 2025 DoPPW O.M.** is illegible; only the month is stated.
3. The **effective date of G.S.R. 410(E)** is unsettled (16.11.2024 on secondary sites, 13.11.2024 on a 120-day count).
4. The **six-month method** used in the Rule 21 example is an assumption, not rule text.
5. G.S.R. 775(E) of 2026 (Rule 37(7)) belongs to Batch 3 and is not covered here.

---

## 6. Re-running the audit after any edit

```bash
python build_pension_b2.py --audit
```

It must end with:

```
ALL CHAPTERS WITHIN BUDGET
ALL CLAUSES TAUGHT
LANGUAGE SPLIT OK
```

If you edit a row, the clause ledger tells you which statutory unit went missing; if you edit narration, the language
audit tells you which segment is not Hinglish or has slipped into Devanagari.

---

## 7. In-sandbox video build (no ffmpeg install needed)

`make_video2.py` builds the real MP4 inside this environment:

```bash
python make_video2.py --list                  # chunk / segment progress
python make_video2.py --segments 0 55 --out part1.mp4
python make_video2.py --out pension_b2_hinglish.mp4     # everything narrated so far
```

- Narrated audio lives in `voice_audio/` as 45 chunks (`chunk_NN.mp3`), each single-voice and <=1400 characters.
  Teacher chunks use the male Indian-accent voice, student chunks the female one.
- A chunk covers whole segments; `make_video2.py` slices it back into per-segment audio by character proportion
  (validated to +/-0.8 s on a ground-truth chunk) so slides change with the narration.
- Each slide carries a baked Hinglish caption band, so the video reads like a class recording.
- ffmpeg comes from `imageio-ffmpeg` (7.0.2, libx264 + AAC), so nothing needs to be installed on the host.

Progress is tracked by `voice_chunks.json` (which segments each chunk covers) and `voice_chunk_voices.json`.
