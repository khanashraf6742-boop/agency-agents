# CCS (Pension) Rules 2021 — Batch 1 (Rules 1 to 10) — explainer video

Deliverable: `pension_b1_rules_1_to_10_city_hinglish.mp4` — 1920x1080, 30 fps, 31 chapters, 49:44.

**Direct download (91.3 MB):**
<https://github.com/khanashraf6742-boop/agency-agents/raw/arena/a191c798-agency-agents/pension_rules_2021/pension_b1_rules_1_to_10_city_hinglish.mp4>

**Play in the browser:**
<https://github.com/khanashraf6742-boop/agency-agents/blob/arena/a191c798-agency-agents/pension_rules_2021/pension_b1_rules_1_to_10_city_hinglish.mp4>

The MP4 is force-added to git (the repo `.gitignore` excludes `*.mp4`), so it is served straight from the branch. Release-asset uploads were not possible: `uploads.github.com` is blocked in the build sandbox. If you later merge this branch into `main`, the ~91 MB blob becomes part of `main`'s history — move it to Releases or LFS at that point if you want a lean repo.

## What is in the video

| Item | Value |
|---|---|
| Chapters | 31 (Rules 1 to 10, Chapter I and Chapter II, plus the O.M.s and amendments) |
| Rule cards | 130 full-width rows, one per rule / sub-rule / clause / proviso / Explanation limb |
| Charts | 4 tables (Rule 2 exclusions, Rule 7 vs Rule 8, Rule 9(3) factors, amendments) + 1 grouped bar chart of every time limit |
| On-screen language | English, plain city English |
| Caption track | Hinglish in Roman script, burned in (no Devanagari anywhere) |
| Frame style | Module bar, chapter banner, one-line title, four anchor chips, bordered row cards with EXAM / TRAP / FLAG / NEW pills, yellow UPSC trap strip, segmented progress bar |

## Important: audio status

This build is **silent** (a silent AAC track is muxed so the MP4 is universally playable). The sandbox has no route to the Microsoft Edge TTS endpoint, and no offline TTS engine could be installed, so the Hinglish narration could not be synthesized here. Everything else is final: slides, reveals, timings and the burned Hinglish captions.

To get the same video **with the voice**, run one command on any machine with internet:

```bash
pip install Pillow edge-tts        # ffmpeg is auto-detected, or pip install imageio-ffmpeg
python build_pension_r1_10_v2.py   # full build: en-IN-PrabhavNeural teacher + en-IN-NeerjaNeural student
```

The narration is already written and timed per card (`hi` field of every row), so the voiced build differs only in audio. Voice, rate and part-splitting are flags: `--teacher`, `--student`, `--rate -4%`, `--part 1|2|3`.

## Full command set

```bash
python build_pension_r1_10_v2.py --audit      # coverage + font-density + narration-language check (no ffmpeg)
python build_pension_r1_10_v2.py --preview    # 212 slide PNGs, no video
python build_pension_r1_10_v2.py --only c06_rule2_expl5_nps   # one chapter
python build_pension_r1_10_v2.py --no-tts     # silent video (this build)
python build_pension_r1_10_v2.py              # voiced video
```

## Other files

- `build_pension_r1_10_v2.py` — the generator (single file, ~2.9k lines including all content)
- `AUDIT_REPORT.md` — senior-professor audit: 20 gaps in v1 closed, 5 factual errors corrected, coverage matrix, open flags
- `pension_b1_reference_sheet.md` — every on-screen card with the exact spoken line, useful as a revision handout
- `previews/*.png` — sample frames in the finished style
- `source_v1/` — the original script that was audited

## Honest flags kept in the video

Rule 87 verbatim, the Rule 44 ₹9,000 figure, the exact date of G.S.R. 775(E) and the 120-day commencement of G.S.R. 410(E) remain marked `FLAG` on screen, and the Rule 8 sub-rule (9) cross-reference is called out as a drafting anomaly rather than invented.
