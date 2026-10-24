#!/usr/bin/env python3
"""
make_video.py - build the Hinglish masterclass MP4 inside this sandbox.

It reuses build_pension_b2.py for the slide design, adds a baked caption band,
and muxes one clip per narration segment from the MP3s in ./voice_audio.

  python make_video.py --range 0 8 --out part1.mp4
  python make_video.py --list                # which segments already have audio
"""
import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

FF = imageio_ffmpeg.get_ffmpeg_exe()
ROOT = Path(__file__).resolve().parent
AUDIO = ROOT / "voice_audio"
WORK = ROOT / "video_build"
SLIDES = WORK / "slides"
W, H = 1920, 1080

spec = importlib.util.spec_from_file_location("b2", ROOT / "build_pension_b2.py")
b2 = importlib.util.module_from_spec(spec)
_argv = sys.argv                      # build_pension_b2 reads sys.argv on import
sys.argv = ["x"]
try:
    spec.loader.exec_module(b2)
except SystemExit:
    pass
sys.argv = _argv


def segs():
    """Flat list of (scene, scene_index, seg_index, who, text, reveal, kind)."""
    out = []
    for si, sc in enumerate(b2.SCENES):
        for gi, (who, text, reveal, kind) in enumerate(b2.build_segments(sc)):
            out.append((sc, si, gi, who, text, reveal, kind))
    return out


def audio_path(si, gi):
    return AUDIO / f"s{si:02d}_g{gi:02d}.mp3"


def duration(path: Path) -> float:
    proc = subprocess.run([FF, "-i", str(path), "-f", "null", "-"],
                          capture_output=True, text=True)
    tail = proc.stderr.strip().splitlines()
    for line in reversed(tail):
        if "time=" in line:
            stamp = line.split("time=")[1].split()[0]
            h, m, s = stamp.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"could not read duration of {path}")


def draw_caption(img_path: Path, text: str, who: str):
    img = Image.open(img_path).convert("RGB")
    d = ImageDraw.Draw(img)
    f = b2.font(27, False)
    max_w = W - 220
    lines = b2.wrap_text(d, text, f, max_w)
    if len(lines) > 4:                      # keep the caption band readable
        f = b2.font(23, False)
        lines = b2.wrap_text(d, text, f, max_w)
    lh = int(f.size * 1.32)
    block_h = len(lines) * lh
    y0 = 862 + (196 - block_h) // 2
    label = "RIYA" if who == "student" else "TEACHER"
    col = (240, 228, 66) if who == "student" else (148, 163, 184)
    for i, ln in enumerate(lines):
        d.text((100, y0 + i * lh), ln, font=f, fill=(226, 232, 240))
    fl = b2.font(18, True)
    d.text((W - 100 - b2.text_w(d, label, fl), 830), label, font=fl, fill=col)
    img.save(img_path)


def build_slide(idx, sc, si, gi, text, reveal, kind):
    SLIDES.mkdir(parents=True, exist_ok=True)
    p = SLIDES / f"s{si:02d}_g{gi:02d}.png"
    b2.render_frame(sc, si + 1, len(b2.SCENES), reveal, kind, p)
    draw_caption(p, text, "student" if kind == "question" else "teacher")
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--range", nargs=2, type=int, metavar=("FROM", "TO"))
    ap.add_argument("--out", default="pension_b2_hinglish.mp4")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--pad", type=float, default=0.45)
    args = ap.parse_args()

    all_segs = segs()
    have = [s for s in all_segs if audio_path(s[1], s[2]).exists()]
    if args.list:
        print(f"{len(have)}/{len(all_segs)} segments have audio")
        for sc, si, gi, _w, _t, _r, _k in all_segs:
            mark = "OK " if audio_path(si, gi).exists() else "-- "
            print(f"  {mark}s{si:02d}_g{gi:02d}  {sc['id']}")
        return

    lo, hi = (0, len(all_segs)) if not args.range else (args.range[0], min(args.range[1], len(all_segs)))
    todo = [s for s in all_segs[lo:hi]]
    missing = [s for s in todo if not audio_path(s[1], s[2]).exists()]
    if missing:
        sys.exit(f"{len(missing)} segment(s) in range still have no audio, e.g. {missing[0][0]['id']}")

    WORK.mkdir(parents=True, exist_ok=True)
    clips = []
    for n, (sc, si, gi, who, text, reveal, kind) in enumerate(todo):
        png = build_slide(n, sc, si, gi, text, reveal, kind)
        mp3 = audio_path(si, gi)
        dur = duration(mp3) + args.pad + (0.5 if kind in ("question", "hook") else 0.0)
        clip = WORK / f"clip_{lo + n:04d}.mp4"
        subprocess.run([
            FF, "-y", "-loop", "1", "-framerate", "2", "-i", str(png), "-i", str(mp3),
            "-af", "apad", "-t", f"{dur:.3f}", "-r", "30",
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-pix_fmt", "yuv420p",
            "-vf", "scale=1920:1080", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
            str(clip)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        clips.append(clip)
        print(f"  clip {n + 1}/{len(todo)}  {sc['id']}  {dur:5.1f}s")

    lst = WORK / "concat.txt"
    lst.write_text("\n".join(f"file '{c.name}'" for c in clips) + "\n", encoding="utf-8")
    out = ROOT / args.out
    subprocess.run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(out)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    total = sum(duration(c) for c in clips)
    print(f"\nDONE {out}  {total / 60:.2f} min  {out.stat().st_size / 1048576:.1f} MB")


if __name__ == "__main__":
    main()
