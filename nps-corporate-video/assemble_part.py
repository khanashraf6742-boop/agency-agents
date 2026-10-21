#!/usr/bin/env python3
"""Arena assembly: slice per-chapter Arena-TTS audio at silence-snapped card boundaries,
build per-segment slide clips, concat, burn ASS subtitles, loudnorm. No ffprobe needed.
Usage: python assemble_part.py 1|2|3  (audio in audio/chNN_teacher.mp3 / chNN_student.mp3,
slides in nps_corporate_complete_build/slides, output nps_corporate_part<N>_masterclass.mp4)"""
import json, re, subprocess, sys
from pathlib import Path
import imageio_ffmpeg
from mutagen.mp3 import MP3

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
ROOT = Path(__file__).resolve().parent
SLIDES = ROOT / "nps_corporate_complete_build" / "slides"
AUDIO = ROOT / "audio"
WORK = ROOT / "build"
WORK.mkdir(exist_ok=True)

PART = int(sys.argv[1])
PART_RANGES = {1: range(0, 5), 2: range(5, 10), 3: range(10, 16)}

code = (ROOT / "build_nps_corporate_complete.py").read_text(encoding="utf-8")
ns = {"__name__": "asm"}
exec(code.split("async def main")[0], ns)
SCENES = [ns["SCENES"][i] for i in PART_RANGES[PART]]
normalize = ns["normalize_for_tts"]


def mp3_dur(p: Path) -> float:
    return float(MP3(str(p)).info.length)


def silence_mids(p: Path):
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", str(p), "-af",
                        "silencedetect=noise=-38dB:d=0.22", "-f", "null", "-"],
                       capture_output=True, text=True)
    txt = r.stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", txt)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", txt)]
    return sorted((a + b) / 2 for a, b in zip(starts, ends))


def snap_bounds(texts, duration, mids):
    total = sum(len(t) for t in texts)
    bounds, acc, prev = [], 0, 0.0
    for k, t in enumerate(texts[:-1]):
        acc += len(t)
        exp = duration * acc / total
        remaining = len(texts) - 1 - k
        cand = [m for m in mids if prev + 1.0 < m < duration - remaining * 1.0 and abs(m - exp) <= 3.5]
        b = min(cand, key=lambda m: abs(m - exp)) if cand else min(max(exp, prev + 1.0), duration - remaining * 1.0)
        bounds.append(b); prev = b
    return [0.0] + bounds + [duration]


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def fmt_ass(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def cues_for(text, offset, dur, style, chunk=8):
    toks = text.split()
    if not toks:
        return []
    step = dur / len(toks)
    words = [(w, i * step, (i + 1) * step) for i, w in enumerate(toks)]
    out, buf = [], []
    for w in words:
        buf.append(w)
        if len(buf) >= chunk or w[0].endswith((".", "?", "!", ":")):
            out.append((offset + buf[0][1], offset + buf[-1][2] + 0.12, style, " ".join(x[0] for x in buf)))
            buf = []
    if buf:
        out.append((offset + buf[0][1], offset + buf[-1][2] + 0.15, style, " ".join(x[0] for x in buf)))
    return out


jobs = []  # (who, kind, slide, audio_path, audio_dur, spoken_text)
for sc in SCENES:
    segs = ns["build_segments"](sc)
    chno = int(re.match(r"c\d+_(\d+)", sc["id"]).group(1))
    tpath = AUDIO / f"ch{chno:02d}_teacher.mp3"
    spath = AUDIO / f"ch{chno:02d}_student.mp3"
    teach_texts = [normalize(t) for (w, t, _r, _k) in segs if w == "teacher"]
    dur = mp3_dur(tpath)
    edges = snap_bounds(teach_texts, dur, silence_mids(tpath))
    print(f"{sc['id']}: teacher {dur:.1f}s edges {[round(e,1) for e in edges]}", flush=True)
    slices = []
    for i in range(len(teach_texts)):
        out = WORK / f"{sc['id']}_t{i}.wav"
        run([FFMPEG, "-y", "-ss", f"{edges[i]:.3f}", "-to", f"{edges[i+1]:.3f}", "-i", str(tpath),
             "-c:a", "pcm_s16le", str(out)])
        slices.append((out, edges[i + 1] - edges[i], teach_texts[i]))
    ti = 0
    for gi, (who, text, reveal, kind) in enumerate(segs):
        slide = SLIDES / f"{sc['id']}_{gi:02d}_{kind}.png"
        assert slide.exists(), slide
        if who == "student":
            jobs.append((who, kind, slide, spath, mp3_dur(spath), normalize(text)))
        else:
            ap, ad, tx = slices[ti]; ti += 1
            jobs.append((who, kind, slide, ap, ad, tx))

print(f"building {len(jobs)} clips...", flush=True)
clips, cues, cursor = [], [], 0.0
for i, (who, kind, slide, ap, ad, tx) in enumerate(jobs):
    dur = ad + (0.9 if kind in ("question", "hook") else 0.5)
    clip = WORK / f"part{PART}_clip_{i:03d}.mp4"
    run([FFMPEG, "-y", "-loop", "1", "-framerate", "5", "-i", str(slide), "-i", str(ap),
         "-af", "apad", "-t", f"{dur:.3f}",
         "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-g", "60", "-r", "30",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(clip)])
    cues += cues_for(tx, cursor, ad, "Student" if who == "student" else "Default")
    clips.append(clip); cursor += dur
print(f"timeline {cursor/60:.2f} min; concat + subtitles...", flush=True)

concat = WORK / f"part{PART}_concat.txt"
concat.write_text("\n".join(f"file '{c.name}'" for c in clips) + "\n", encoding="utf-8")
raw = WORK / f"part{PART}_raw.mp4"
subprocess.run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", concat.name, "-c", "copy", raw.name],
               check=True, cwd=str(WORK), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, "
        "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
        "MarginR, MarginV, Encoding\n"
        "Style: Default,DejaVu Sans,38,&H00FFFFFF,&H0000E6FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,160,160,70,1\n"
        "Style: Student,DejaVu Sans,38,&H0042E4F0,&H0000E6FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,160,160,70,1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text")
lines = [head] + [f"Dialogue: 0,{fmt_ass(s)},{fmt_ass(e)},{st},,0,0,0,,{tx}" for s, e, st, tx in cues]
ass = WORK / f"part{PART}_subtitles.ass"
ass.write_text("\n".join(lines) + "\n", encoding="utf-8")

outmp4 = ROOT / f"nps_corporate_part{PART}_masterclass.mp4"
subprocess.run([FFMPEG, "-y", "-i", raw.name, "-vf", f"subtitles='{ass.name}'",
                "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                "-c:v", "libx264", "-crf", "19", "-preset", "veryfast", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(outmp4)],
               check=True, cwd=str(WORK), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"DONE {outmp4} | {cursor/60:.2f} min | {outmp4.stat().st_size/1048576:.1f} MB", flush=True)
(Path(__file__).parent / "build" / f"part{PART}_timeline.json").write_text(
    json.dumps({"minutes": cursor / 60, "clips": len(clips), "cues": len(cues)}, indent=1), encoding="utf-8")
