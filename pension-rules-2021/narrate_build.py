#!/usr/bin/env python3
"""Narration pipeline for the Batch 4 master.

The video compiler (build_pension_b4.py) paces the slides from the caption text.
This tool replaces that guess with the real voice: every clip is split back into
its narration segments at the pauses the voice actually makes, the slide
timeline is rebuilt from those measured durations, and the finished audio is
laid under the frames.

Workflow
    python narrate_build.py --status     how many clips exist / still to make
    python narrate_build.py --plan       print the next batch of clips to record
    python narrate_build.py --build      assemble video + narration

Segmentation
    Each clip covers a known, ordered list of narration segments. The clip is
    split into exactly that many pieces by a monotonic dynamic-programming
    alignment against a character-share estimate, choosing real silences as
    boundaries. Measured error on the first batch: <= 0.9 s.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "pension_b4_build"
RUNS = BUILD / "runs"
STATE = BUILD / "narration_state.json"
FPS = 25
TEACHER_VOICE = "voice-00"
STUDENT_VOICE = "voice-01"
STUDENT_BATCH = 8          # questions per batched student clip
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


# ---------------------------------------------------------------- plan ------
def load_scenes():
    spec = __import__("importlib.util").util.spec_from_file_location(
        "b4", ROOT / "build_pension_b4.py")
    mod = __import__("importlib.util").util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_runs():
    """Every maximal same-speaker run of segments, in video order."""
    b4 = load_scenes()
    runs = []
    for ci, sc in enumerate(b4.SCENES):
        who = None
        buf, segs = [], []
        for speaker, text, reveal, kind in b4.build_segments(sc):
            clean = re.sub(r"\s+", " ", b4.strip_rich(text)).strip()
            if speaker != who:
                if who:
                    runs.append({"ch": ci, "id": sc["id"], "speaker": who,
                                 "text": " ".join(buf), "segs": segs})
                who, buf, segs = speaker, [], []
            buf.append(clean)
            segs.append({"text": clean, "kind": kind, "reveal": reveal})
        if who:
            runs.append({"ch": ci, "id": sc["id"], "speaker": who,
                         "text": " ".join(buf), "segs": segs})
    for i, r in enumerate(runs):
        r["run"] = i
        r["png"] = f"master_{r['ch']:02d}_{r['segs'][0]['reveal']:02d}.png"
    return runs


def clip_plan(runs):
    """Assign every run to a clip: teachers one per clip, students batched."""
    clips = []
    pending_students = []
    for r in runs:
        single = f"run_{r['run']:02d}.mp3"
        if r["speaker"] == "teacher":
            clips.append({"file": single, "voice": TEACHER_VOICE, "runs": [r["run"]]})
        elif (RUNS / single).exists():
            # already recorded on its own in an earlier pass
            clips.append({"file": single, "voice": STUDENT_VOICE, "runs": [r["run"]]})
        else:
            pending_students.append(r["run"])
    for k in range(0, len(pending_students), STUDENT_BATCH):
        chunk = pending_students[k:k + STUDENT_BATCH]
        clips.append({"file": f"student_b{k // STUDENT_BATCH:02d}.mp3",
                      "voice": STUDENT_VOICE, "runs": chunk})
    for c in clips:
        c["path"] = RUNS / c["file"]
        c["text"] = " ".join(speak_text(runs[i]["text"]) for i in c["runs"])
        c["units"] = [(i, j) for i in c["runs"] for j in range(len(runs[i]["segs"]))]
    return clips


def speak_text(t):
    """Speech-only normalisation.

    Short all-caps tokens (DR, PSU, VRS, O.M.) must stay capitalised so the
    voice spells them out; long ones (BAHATTAR) are emphasis and read better
    in lower case.
    """
    return re.sub(r"\b[A-Z]{5,}\b", lambda m: m.group(0).lower(), t)


# ------------------------------------------------------------- ffmpeg ------
def probe(path):
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)],
                       capture_output=True, text=True)
    hit = [l for l in r.stderr.splitlines() if "Duration" in l]
    if not hit:
        raise RuntimeError(f"cannot probe {path}")
    h, m, s = hit[0].split("Duration:")[1].split(",")[0].strip().split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def silences(path):
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path), "-af",
                        "silencedetect=noise=-32dB:d=0.16", "-f", "null", "-"],
                       capture_output=True, text=True)
    out, start = [], None
    for line in r.stderr.splitlines():
        m = re.search(r"silence_start: ([\d.]+)", line)
        if m:
            start = float(m.group(1))
        m = re.search(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", line)
        if m and start is not None:
            out.append(((start + float(m.group(1))) / 2, float(m.group(2))))
            start = None
    return out


def align(cands, expected):
    """Pick len(expected) monotonic silence boundaries closest to the estimates."""
    n = len(expected)
    if n == 0:
        return []
    if not cands:
        return expected[:]
    INF = 1e18
    cost = [[INF] * len(cands) for _ in range(n)]
    back = [[-1] * len(cands) for _ in range(n)]
    for j, (pos, d) in enumerate(cands):
        cost[0][j] = abs(pos - expected[0]) + max(0.0, 0.30 - d) * 8
    for i in range(1, n):
        best, arg = INF, -1
        for j in range(len(cands)):
            if j and cost[i - 1][j - 1] < best:
                best, arg = cost[i - 1][j - 1], j - 1
            if arg >= 0:
                cost[i][j] = best + abs(cands[j][0] - expected[i]) \
                    + max(0.0, 0.30 - cands[j][1]) * 8
                back[i][j] = arg
    j = min(range(len(cands)), key=lambda x: cost[n - 1][x])
    picked = []
    for i in range(n - 1, -1, -1):
        picked.append(cands[j][0])
        j = back[i][j]
    return sorted(picked)


def split_clip(path, units, runs):
    """Return [(start, end)] one per unit, using real pauses as boundaries."""
    dur = probe(path)
    chars = [len(runs[r]["segs"][s]["text"]) for r, s in units]
    total = sum(chars)
    acc, expected = 0, []
    for c in chars[:-1]:
        acc += c
        expected.append(dur * acc / total)
    cuts = align(silences(path), expected)
    edges = [0.0] + cuts + [dur]
    return [(edges[i], edges[i + 1]) for i in range(len(units))]


# --------------------------------------------------------------- build -----
def build(args):
    runs = load_runs()
    clips = clip_plan(runs)
    missing = [c["file"] for c in clips if not c["path"].exists()]
    if missing:
        sys.exit(f"{len(missing)} clips missing, e.g. {missing[:3]}; run --plan")

    pieces = []
    for c in clips:
        spans = split_clip(c["path"], c["units"], runs)
        for (r, s), (a, b) in zip(c["units"], spans):
            seg = runs[r]["segs"][s]
            pieces.append({"run": r, "seg": seg, "text": seg["text"],
                           "kind": seg["kind"], "speaker": runs[r]["speaker"],
                           "clip": c["path"], "a": a, "b": b, "dur": max(0.8, b - a)})

    # timeline: a segment's slide lives exactly as long as its audio + breathe
    frame_cursor, items = 0, []
    for p in pieces:
        pad = 0.95 if p["kind"] in ("question", "hook", "intro") else 0.55
        seconds = max(2.2, p["dur"] + pad)
        frames = max(2, int(round(seconds * FPS)))
        items.append({**p, "frames": frames, "t0": frame_cursor / FPS,
                      "seconds": frames / FPS})
        frame_cursor += frames
    total = frame_cursor / FPS
    print(f"  segments {len(items)} | frames {frame_cursor} | runtime {total/60:.2f} min")

    # captions
    b4 = load_scenes()
    cues = []
    for it in items:
        cues += b4.caption_cues(it["text"], it["t0"], it["seconds"],
                                "Student" if it["speaker"] == "student" else "Default")
    ass = BUILD / "master_captions.ass"
    b4.write_ass(cues, ass, caption_layout=True)
    print(f"  captions {len(cues)}")

    # master audio: one WAV per segment, exact length, then concatenated
    wavdir = BUILD / "wav"
    wavdir.mkdir(exist_ok=True)
    for old in wavdir.glob("*.wav"):
        old.unlink()
    wavs = []
    for i, it in enumerate(items):
        out = wavdir / f"seg_{i:04d}.wav"
        length = it["frames"] / FPS
        src = str(it["clip"]).replace("\\", "/")
        fc = (f"[0:a]atrim={it['a']:.3f}:{it['b']:.3f},asetpts=PTS-STARTPTS,"
              f"aresample=48000,aformat=channel_layouts=stereo,adelay=110:all=1[s];"
              f"[1:a][s]amix=inputs=2:duration=first:normalize=0[o]")
        subprocess.run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
                        "-i", src, "-f", "lavfi", "-t", f"{length:.4f}",
                        "-i", "anullsrc=r=48000:cl=stereo", "-filter_complex", fc,
                        "-map", "[o]", "-t", f"{length:.4f}", "-ar", "48000",
                        "-ac", "2", str(out)], check=True)
        wavs.append(out)
        if (i + 1) % 50 == 0:
            print(f"    audio {i+1}/{len(items)}")
    master = BUILD / "narration.wav"
    listing = BUILD / "wav_list.txt"
    listing.write_text("".join(f"file '{w.as_posix()}'\n" for w in wavs), encoding="utf-8")
    subprocess.run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error", "-f", "concat",
                    "-safe", "0", "-i", str(listing), "-c", "copy", str(master)], check=True)
    print(f"  audio {probe(master)/60:.2f} min")

    # video: one exact-length clip per still, captions burned in, then joined
    parts_dir = BUILD / "parts"
    if parts_dir.exists():
        for p in parts_dir.glob("*.mp4"):
            p.unlink()
    parts_dir.mkdir(exist_ok=True)
    timeline = []
    for it in items:
        png = BUILD / "cap_slides" / it.get("png", "")
        timeline.append(it)
    # group consecutive segments that share a still
    groups = []
    for it in items:
        png = f"master_{runs[it['run']]['ch']:02d}_{it['seg']['reveal']:02d}.png"
        if groups and groups[-1]["png"] == png:
            groups[-1]["frames"] += it["frames"]
        else:
            groups.append({"png": png, "frames": it["frames"], "t0": it["t0"]})
    print(f"  stills {len(groups)}")
    parts = []
    for idx, g in enumerate(groups):
        png = BUILD / "slides" / g["png"]
        safe = BUILD / "cap_slides" / g["png"]
        if not safe.exists():
            b4.caption_safe_slide(png, safe)
        part = parts_dir / f"part_{idx:03d}.mp4"
        filt = (f"setpts=PTS+{g['t0']:.3f}/TB,ass=master_captions.ass,"
                f"setpts=PTS-{g['t0']:.3f}/TB,format=yuv420p")
        subprocess.run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
                        "-loop", "1", "-framerate", str(FPS), "-i", str(safe),
                        "-vf", filt, "-frames:v", str(g["frames"]),
                        "-c:v", "libx264", "-preset", args.preset, "-crf", str(args.crf),
                        "-tune", "stillimage", "-g", str(FPS * 10), "-pix_fmt", "yuv420p",
                        "-video_track_timescale", "90000", str(part)],
                       check=True, cwd=str(BUILD))
        parts.append(part)
        if (idx + 1) % 25 == 0:
            print(f"    video {idx+1}/{len(groups)}")
    plist = BUILD / "parts_list.txt"
    plist.write_text("".join(f"file '{p.resolve().as_posix()}'\n" for p in parts),
                     encoding="utf-8")
    silent = BUILD / "video_silent.mp4"
    subprocess.run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error", "-f", "concat",
                    "-safe", "0", "-i", str(plist), "-c", "copy", str(silent)], check=True)

    out = Path(args.out).resolve()
    subprocess.run([FFMPEG, "-y", "-hide_banner", "-loglevel", "error",
                    "-i", str(silent), "-i", str(master),
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-shortest", "-movflags", "+faststart", str(out)], check=True)
    print(f"DONE {out} | {out.stat().st_size/1048576:.1f} MB | {probe(out)/60:.2f} min")
    return out


# ---------------------------------------------------------------- main -----
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--limit", type=int, default=10, help="clips to print in --plan")
    ap.add_argument("--out", default=str(ROOT / "pension_b4_master_silent.mp4"))
    ap.add_argument("--crf", type=int, default=26)
    ap.add_argument("--preset", default="medium")
    args = ap.parse_args()

    RUNS.mkdir(parents=True, exist_ok=True)
    runs = load_runs()
    clips = clip_plan(runs)
    done = [c for c in clips if c["path"].exists()]
    todo = [c for c in clips if not c["path"].exists()]

    if args.status:
        print(f"clips {len(done)}/{len(clips)} done, {len(todo)} to go")
        for c in todo[:20]:
            print(f"  todo {c['file']:<18} {len(c['text']):>5} chars  runs={c['runs']}")
        return

    if args.plan:
        batch = todo[:args.limit]
        print(f"### NEXT {len(batch)} CLIPS ({len(todo)} remaining)\n")
        for c in batch:
            print(f"--- file: pension_b4_build/runs/{c['file']} | voice: {c['voice']} "
                  f"| {len(c['text'])} chars")
            print(c["text"])
            print()
        return

    if args.build:
        build(args)
        return

    ap.print_help()


if __name__ == "__main__":
    main()
