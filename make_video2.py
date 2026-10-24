#!/usr/bin/env python3
"""
make_video2.py - assemble the Hinglish masterclass from chunk narration.

Why chunks: the voice engine here returns one audio file per call, so the 226
narration segments are narrated as 46 chunks of <=1400 characters, each chunk
covering a run of whole segments. This script slices every chunk back into
per-segment audio, times the slices by character proportion (validated to
within +/-0.8 s on a ground-truth chunk), renders the slide for that segment
with a baked Hinglish caption band, and muxes the lot.

  python make_video2.py --list                 # chunk and segment progress
  python make_video2.py --segments 0 40        # build a range of segments
  python make_video2.py --out master.mp4       # build everything that has audio
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw

FF = imageio_ffmpeg.get_ffmpeg_exe()
ROOT = Path(__file__).resolve().parent
AUDIO = ROOT / "voice_audio"
WORK = ROOT / "video_build"
SLIDES = WORK / "slides"
CLIPS = WORK / "clips"
W = 1920

ROWS = json.loads((ROOT / "voice_manifest.json").read_text(encoding="utf-8"))
CHUNKS = json.loads((ROOT / "voice_chunks.json").read_text(encoding="utf-8"))
CHUNK_FILE = [AUDIO / f"chunk_{k:02d}.mp3" for k in range(len(CHUNKS))]
SEG2CHUNK = {seg: k for k, ch in enumerate(CHUNKS) for seg in ch}


def load_b2():
    import importlib.util
    spec = importlib.util.spec_from_file_location("b2", ROOT / "build_pension_b2.py")
    b2 = importlib.util.module_from_spec(spec)
    argv = sys.argv
    sys.argv = ["x"]
    try:
        spec.loader.exec_module(b2)
    except SystemExit:
        pass
    sys.argv = argv
    return b2


B2 = load_b2()
FLAT = []                                   # (scene, si, gi, who, text, reveal, kind)
for si, sc in enumerate(B2.SCENES):
    for gi, (who, text, reveal, kind) in enumerate(B2.build_segments(sc)):
        FLAT.append((sc, si, gi, who, text, reveal, kind))
assert len(FLAT) == len(ROWS), "manifest out of date: rerun the manifest step"


def duration(path: Path) -> float:
    proc = subprocess.run([FF, "-i", str(path), "-f", "null", "-"], capture_output=True, text=True)
    stamp = [ln for ln in proc.stderr.splitlines() if "time=" in ln][-1].split("time=")[1].split()[0]
    h, m, s = stamp.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def segment_spans(k):
    """[(seg_index, start, end)] inside chunk k, proportional to characters."""
    segs = CHUNKS[k]
    total_chars = sum(len(ROWS[i]["text"]) for i in segs)
    total = duration(CHUNK_FILE[k])
    spans, t = [], 0.0
    for i in segs:
        d = total * len(ROWS[i]["text"]) / total_chars
        spans.append((i, t, t + d))
        t += d
    return spans


_SPAN_CACHE = {}


def audio_for(seg):
    """Path to a per-segment audio file, slicing it out of its chunk if needed."""
    direct = AUDIO / ROWS[seg]["f"].split("/")[-1]
    if direct.exists():
        return direct, 0.0, duration(direct)
    k = SEG2CHUNK.get(seg)
    if k is None or not CHUNK_FILE[k].exists():
        return None, 0.0, 0.0
    if k not in _SPAN_CACHE:
        _SPAN_CACHE[k] = segment_spans(k)
    for i, a, b in _SPAN_CACHE[k]:
        if i == seg:
            out = AUDIO / f"slice_{seg:03d}.mp3"
            if not out.exists():
                subprocess.run([FF, "-y", "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", str(CHUNK_FILE[k]),
                                "-c:a", "libmp3lame", "-q:a", "4", str(out)],
                               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return out, 0.0, b - a
    return None, 0.0, 0.0


def draw_caption(png: Path, text: str, who: str):
    img = Image.open(png).convert("RGB")
    d = ImageDraw.Draw(img)
    f = B2.font(27, False)
    lines = B2.wrap_text(d, text, f, W - 220)
    if len(lines) > 4:
        f = B2.font(23, False)
        lines = B2.wrap_text(d, text, f, W - 220)
    lh = int(f.size * 1.32)
    y0 = 862 + (196 - len(lines) * lh) // 2
    for i, ln in enumerate(lines):
        d.text((100, y0 + i * lh), ln, font=f, fill=(226, 232, 240))
    label = "RIYA" if who == "student" else "TEACHER"
    fl = B2.font(18, True)
    d.text((W - 100 - B2.text_w(d, label, fl), 830), label, font=fl,
           fill=(240, 228, 66) if who == "student" else (148, 163, 184))
    img.save(png)


def build(lo, hi, out_name, pad):
    SLIDES.mkdir(parents=True, exist_ok=True)
    CLIPS.mkdir(parents=True, exist_ok=True)
    todo = range(lo, min(hi, len(FLAT)))
    ready = [i for i in todo if audio_for(i)[0] is not None]
    if not ready:
        sys.exit("no audio in that range")
    if len(ready) < len(list(todo)):
        print(f"  note: building the {len(ready)} segments that have audio")

    clips = []
    for n, seg in enumerate(ready):
        sc, si, gi, who, text, reveal, kind = FLAT[seg]
        mp3, _off, sdur = audio_for(seg)
        png = SLIDES / f"seg_{seg:03d}.png"
        B2.render_frame(sc, si + 1, length_total(), reveal, kind, png)
        draw_caption(png, text, who)
        dur = sdur + pad + (0.5 if kind in ("question", "hook") else 0.0)
        clip = CLIPS / f"clip_{seg:03d}.mp4"
        subprocess.run([
            FF, "-y", "-loop", "1", "-framerate", "2", "-i", str(png), "-i", str(mp3),
            "-af", "apad", "-t", f"{dur:.3f}", "-r", "30", "-vf", "scale=1920:1080",
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(clip)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        clips.append(clip)
        if n % 10 == 0 or n == len(ready) - 1:
            print(f"  {n + 1}/{len(ready)}  seg {seg:03d}  {sc['id']}  {dur:5.1f}s")

    lst = WORK / "concat.txt"
    lst.write_text("\n".join(f"file '{c.resolve()}'" for c in clips) + "\n", encoding="utf-8")
    out = ROOT / out_name
    subprocess.run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(out)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    total = duration(out)
    print(f"\nDONE {out}  {int(total // 60)}m {total % 60:04.1f}s  {out.stat().st_size / 1048576:.1f} MB")
    return out


def length_total():
    return len(B2.SCENES)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--segments", nargs=2, type=int, metavar=("FROM", "TO"))
    ap.add_argument("--out", default="pension_b2_hinglish.mp4")
    ap.add_argument("--pad", type=float, default=0.45)
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    if args.list:
        have_chunks = sum(1 for p in CHUNK_FILE if p.exists())
        have_segs = sum(1 for i in range(len(FLAT)) if audio_for(i)[0] is not None)
        print(f"chunks narrated: {have_chunks}/{len(CHUNKS)} | segments with audio: {have_segs}/{len(FLAT)}")
        for k, p in enumerate(CHUNK_FILE):
            print(f"  {'OK ' if p.exists() else '-- '}chunk {k:02d}  segments {CHUNKS[k][0]:3d}-{CHUNKS[k][-1]:3d}"
                  f"  {ROWS[CHUNKS[k][0]]['scene']}")
        return

    lo, hi = (0, len(FLAT)) if not args.segments else tuple(args.segments)
    build(lo, hi, args.out, args.pad)


if __name__ == "__main__":
    main()
