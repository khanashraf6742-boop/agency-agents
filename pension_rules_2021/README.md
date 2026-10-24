# CCS (Pension) Rules 2021 — Batch 1 (Rules 1 to 10) explainer

| File | What it is |
|---|---|
| `build_pension_r1_10_v2.py` | The upgraded compiler: 31 chapters, screenshot-style row cards, 4 tables, 1 bar chart, English on screen, Hinglish (Roman) narration, burned subtitles. |
| `AUDIT_REPORT.md` | The senior-professor audit: rule-by-rule coverage matrix, the 20 gaps found in v1, the 5 factual errors corrected, and the items still flagged as unverified. |
| `pension_b1_reference_sheet.md` | Auto-generated sheet: every on-screen card plus the exact spoken line, for print or revision. |
| `previews/*.png` | Six sample frames in the finished style. |
| `source_v1/` | The original 32-chapter script that was audited, kept for the record. |

```bash
pip install Pillow edge-tts        # ffmpeg + ffprobe with libass on PATH for the MP4
python build_pension_r1_10_v2.py --audit      # coverage + density + narration check (no ffmpeg)
python build_pension_r1_10_v2.py --preview    # 212 slide PNGs
python build_pension_r1_10_v2.py              # full MP4 with Hinglish voice + subtitles
```
