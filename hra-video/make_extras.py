#!/usr/bin/env python3
"""Produce the brisk 1.08x cut and the standalone rates block (chapters 5-7).

Both are derived from the master / chapter cuts produced by build_hra.py.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location("bh", "build_hra.py")
bh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bh)
FF = bh.ffmpeg_bin()
SPEED = 1.08


def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        print("FAILED:", " ".join(c[:5]))
        print(r.stderr[-2500:])
        sys.exit(1)
    return r


def probe(p):
    r = subprocess.run([FF, "-hide_banner", "-i", str(p)], capture_output=True, text=True)
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


# ---- 1. brisk cut, matching the master's exact encode settings ---------------
src, dst = Path("hra_masterclass.mp4"), Path("hra_masterclass_brisk.mp4")
run([FF, "-y", "-i", str(src),
     "-vf", f"setpts=PTS/{SPEED}", "-af", f"atempo={SPEED}", "-r", "30",
     "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-crf", "17",
     "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
     "-movflags", "+faststart", str(dst)])
print(f"[1] brisk rendered ({SPEED}x, crf 17 + tune stillimage, -r 30)")

# setpts does NOT remap chapter marks -> rescale them by hand
meta = Path("work/hra_masterclass_chapters.txt").read_text()
meta2 = re.sub(r"(START=|END=)(\d+)",
               lambda m: f"{m.group(1)}{int(int(m.group(2)) / SPEED)}", meta)
Path("work/hra_masterclass_brisk_chapters.txt").write_text(meta2)
tmp = dst.with_suffix(".chapters.mp4")
run([FF, "-y", "-i", str(dst), "-i", "work/hra_masterclass_brisk_chapters.txt",
     "-map_metadata", "1", "-map_chapters", "1", "-codec", "copy", str(tmp)])
shutil.move(str(tmp), str(dst))
print(f"[2] {meta2.count('[CHAPTER]')} chapter marks rescaled by 1/{SPEED} and embedded")

# ---- 2. standalone rates block: chapters 5 + 6 + 7 --------------------------
parts = [(5, "Rates And DA Ladder", Path("chapters/ch05_h05_rates_and_da_ladder.mp4")),
         (6, "Position Today 2026", Path("chapters/ch06_h06_position_today_2026.mp4")),
         (7, "8th CPC Status",      Path("chapters/ch07_h07_eighth_cpc.mp4"))]
missing = [str(p) for _, _, p in parts if not p.exists()]
if missing:
    print("missing chapter files:", missing)
    sys.exit(1)

lst = Path("work/rates_concat.txt")
lst.write_text("".join(f"file '{p.resolve()}'\n" for _, _, p in parts))
blk = Path("hra_rates_block_ch05-ch07.mp4")
run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
     "-movflags", "+faststart", str(blk)])

ds = [probe(p) for _, _, p in parts]
lines = [";FFMETADATA1"]
t = 0.0
for (num, label, _), d in zip(parts, ds):
    lines += ["[CHAPTER]", "TIMEBASE=1/1000",
              "START=%d" % int(t * 1000), "END=%d" % int((t + d) * 1000),
              "title=Chapter %d - %s" % (num, label), ""]
    t += d
Path("work/rates_block_chapters.txt").write_text("\n".join(lines), encoding="utf-8")
tmp = blk.with_suffix(".ch.mp4")
run([FF, "-y", "-i", str(blk), "-i", "work/rates_block_chapters.txt",
     "-map_metadata", "1", "-map_chapters", "1", "-codec", "copy", str(tmp)])
shutil.move(str(tmp), str(blk))
print("[3] rates block = ch05+ch06+ch07, %.0fs, 3 chapter marks" % sum(ds))
