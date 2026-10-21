# PFRDA NPS Corporate Sector Model — Video Masterclass (Delivery Notes)

Source: official PFRDA Information Brochure, Sections 1-7 (16 Q&A chapters, student Riya + Teacher).
Voices: **Indian English (en-IN)** — male Teacher + female student (Riya), chosen by the user from auditions.
Spec: 1920x1080 MP4 (H.264), burned subtitles (white = Teacher, yellow = Riya), loudness-normalised audio.

## Files
| File | What |
|---|---|
| `nps_corporate_complete_masterclass.mp4` | **FULL MASTER VIDEO: all 16 chapters, 17 min 37 s** |
| `nps_corporate_part1_masterclass.mp4` | Part 1 video: Chapters 1-5, 5 min 40 s |
| `nps_corporate_part2_masterclass.mp4` | **Part 2 video: Chapters 6-10, 5 min 15 s** |
| `nps_corporate_part3_masterclass.mp4` | Part 3 video: Chapters 11-16, 6 min 42 s |
| `full_youtube_chapters.txt` | Copy-paste YouTube chapter timestamps for the full master (all 16) |
| `part2_youtube_chapters.txt` / `part3_youtube_chapters.txt` | YouTube timestamps for Parts 2 / 3 |
| `part1_youtube_chapters.txt` | Copy-paste YouTube chapter timestamps for Part 1 |
| `nps_corporate_complete_reference_sheet.md` | Full verbatim text behind every on-screen card (all 16 chapters) |
| `build_nps_corporate_complete.py` | Complete 16-chapter compiler (fixed, see below) |
| `narration_manifest.json` | Pronunciation-proofed spoken text, chapter by chapter |
| `assemble_part.py` | Arena part assembler (silence-snapped card timing) |

## Fixes applied with discretion (no rule content changed)
1. **Crash fix:** Chapter 6 on-screen title (85 chars) could not fit one line and crashed
   `--preview` / full build. Shortened title only; card/full text untouched.
2. **Pronunciation proofing (spoken text only):** `Tier-I/II` spoken as "Tier 1/2";
   helpline `1800222080` read digit-by-digit; `pfrda.org.in` / `cra-nsdl.com` spelled out;
   `0.0075` spoken in full; every acronym (PFRDA, PRAN, NSDL, SHCIL...) dotted for letter-perfect reading.
3. **Sync:** each chapter narrated as one clip per speaker; card-reveal cuts snapped to real
   speech pauses (ffmpeg silencedetect), so cards change between sentences, never mid-word.

## Verification evidence
- `--audit`: ALL CARDS WITHIN BUDGET; all `calc_asserts` (worked examples) evaluate True.
- All 97 slides rendered; question/teacher/hook frames visually inspected.
- Output probed: H.264 1920x1080 30 fps + AAC stereo 48 kHz; durations 00:05:40.43 (Part 1), 00:05:15.29 (Part 2), 00:06:41.66 (Part 3), 00:17:37.40 (full master = exact sum).
- Frames inspected every part: question frames, flow-diagram node sync (Ch. 8, Ch. 13), card-highlight vs subtitle sync (Ch. 5, 10, 13, 16).
- Full master decoded end-to-end with zero errors after the 48 kHz normalisation fix.

## Status: COMPLETE
All 16 chapters delivered as three part-videos plus one combined master
(`nps_corporate_complete_masterclass.mp4`, stream-copy join of Parts 1-3 after
normalising Part 1 audio to 48 kHz; full decode check = 0 errors; audio verified
alive in 20-second windows across both joins). Riya's Part-3 questions were recorded
in pairs and sliced at the detected between-question pause (cuts within 0.6 s of the
length-proportional prediction; resulting clips 6.5-8.3 s, same range as Parts 1-2).

## Currency caution (important)
Figures are faithful to the source brochure (2011-12 era), e.g. Rs. 1 lakh overall cap,
50% equity ceiling, Tier-I Rs. 6,000/year minimum, exit/annuity conditions. Pension and tax
provisions have been revised since; **verify current limits on pfrda.org.in / the latest
PFRDA Exit Regulations before quoting any figure in an exam answer or client advice.**
