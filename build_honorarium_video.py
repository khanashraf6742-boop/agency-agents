#!/usr/bin/env python3
"""
Honorarium to Inquiry Officers / Presenting Officers — Master Explainer video compiler.
Source: DoPT O.M. DOPT-1668597747466 dated 16.11.2022 (Hinglish study guide uploaded), with the
MoD(Fin)/CGDA clarification dated 16.08.2023 and CVC communication dated 05.12.2022 (as quoted in that letter).

Pipeline (same method as the CEA and pension videos):
  1. SCENES (below) hold every card, table, chart, flowchart and Hinglish narration line.
  2. --preview  renders 1920x1080 PNG slides (one per reveal stage) into BUILD_DIR/slides
  3. narration clips are generated with the session voices (teacher = voice-00,
     student = voice-01) and saved as BUILD_DIR/clips/NNN.mp3 (NNN = scene index, 0-based)
  4. --build    assembles slides + clips into one H.264/AAC MP4 (BUILD_DIR/out/)
  5. --reference writes the English card reference sheet (markdown)
  6. --audit    checks every card fits its slide and prints density (no ffmpeg needed)

Card kinds (in addition to stat, row, table, steps, callout):
  bars   {"kind":"bars","color","title","items":[(label, value, value_text), ...],"max":optional}  horizontal bar chart
  quote  {"kind":"quote","color","label","text"}                 verbatim OM wording in a quote box

On-screen text is English only. Narration is Hinglish in Roman script (no Devanagari).
Unverified claims are tagged on screen as NOT VERIFIED; guide errors are tagged GUIDE FIX.

Usage:
  python3 build_honorarium_video.py --audit
  python3 build_honorarium_video.py --preview
  python3 build_honorarium_video.py --check-clips
  python3 build_honorarium_video.py --build
  python3 build_honorarium_video.py --reference
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

try:
    import imageio_ffmpeg
    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:  # fall back to a system ffmpeg
    FFMPEG = "ffmpeg"

W, H = 1920, 1080
FPS = 4
OUT_STEM = "honorarium_io_po_masterclass"
BUILD_DIR = Path(os.environ.get("HON_BUILD_DIR", "/home/user/honorarium_video/build"))
SLIDE_DIR = BUILD_DIR / "slides"
CLIP_DIR = BUILD_DIR / "clips"
SEG_DIR = BUILD_DIR / "segments"
OUT_DIR = BUILD_DIR / "out"
REFERENCE_MD = Path(__file__).with_name("honorarium_io_po_reference_sheet.md")

TITLE_TOP = "Honorarium to Inquiry Officers & Presenting Officers — DoPT O.M. 16.11.2022 — Master Explainer"
FOOTER = "Source: DoPT O.M. DOPT-1668597747466 (16.11.2022) · DoE I.D. 26.10.2022 · MoD(Fin)/CGDA clarification 16.08.2023 · Rates as on 2026-10-25"

# Palette (matches the dark-navy reference style)
BG_TOP = (10, 16, 36)
BG_BOT = (22, 30, 58)
CHROME = (14, 22, 44)
CARD_BG = (28, 39, 62)
ALT_BG = (34, 47, 74)
HEAD_BG = (20, 30, 54)
TEXT = (248, 250, 252)
MUTED = (148, 163, 184)
PAL = {
    "cyan": (86, 200, 240),
    "orange": (240, 159, 0),
    "green": (0, 190, 140),
    "purple": (168, 130, 255),
    "yellow": (240, 228, 66),
    "red": (240, 110, 100),
    "sky": (86, 180, 233),
    "blue": (96, 140, 255),
    "pink": (236, 130, 190),
}

# ---------------------------------------------------------------- fonts
_FONT_CACHE = {}


def font(size, bold=False):
    key = (int(round(size)), bold)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    names = (["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "arialbd.ttf"] if bold
             else ["DejaVuSans.ttf", "LiberationSans-Regular.ttf", "arial.ttf"])
    f = None
    for n in names:
        for base in ("", "/usr/share/fonts/truetype/dejavu/"):
            try:
                f = ImageFont.truetype(base + n, key[0])
                break
            except Exception:
                continue
        if f:
            break
    if f is None:
        f = ImageFont.load_default()
    _FONT_CACHE[key] = f
    return f


def wrap(text, f, max_w):
    lines = []
    for para in str(text).split("\n"):
        cur = ""
        for w in para.split():
            t = (cur + " " + w).strip()
            if not cur or f.getlength(t) <= max_w:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- layout
# Card kinds:
#   stat   {"kind":"stat","color","head","sub"}           colored header tile (grouped in rows of up to 4)
#   row    {"kind":"row","color","label","text"}           dark card, colored label on the left
#   table  {"kind":"table","color","title","headers","rows","widths"}  (widths = fractions)
#   steps  {"kind":"steps","color","steps":[...]}          flow boxes joined by arrows (max 5)
#   callout{"kind":"callout","color","text"}               full-width yellow-style callout
GAP = 16
PAD = 18
SIDE = 40
INNER_W = W - 2 * SIDE


def _lh(f):
    return int(f.size * 1.32)


def measure_card(card, s, width):
    """Return height needed by a single (non-stat) card at scale s."""
    k = card["kind"]
    if k == "row":
        lab_w = int(330 * s)
        f_lab = font(25 * s, True)
        f_txt = font(24 * s)
        txt_w = width - 2 * PAD - lab_w - 24
        n = max(len(wrap(card["label"], f_lab, lab_w)), len(wrap(card["text"], f_txt, txt_w)))
        return 2 * PAD + n * _lh(f_txt)
    if k == "callout":
        f = font(26 * s, True)
        return 2 * PAD + len(wrap(card["text"], f, width - 2 * PAD - 20)) * _lh(f)
    if k == "table":
        f_t = font(25 * s, True)
        f_h = font(21 * s, True)
        f_c = font(21 * s)
        h = 2 * PAD + _lh(f_t) + 8
        cws = [int(width * fr) for fr in card["widths"]]
        cws[-1] = width - 2 * PAD - sum(cws[:-1])
        hdr_lines = max(len(wrap(hd, f_h, cw - 16)) for hd, cw in zip(card["headers"], cws))
        h += hdr_lines * _lh(f_h) + 12
        for r in card["rows"]:
            n = max(len(wrap(str(c), f_c, cw - 16)) for c, cw in zip(r, cws))
            h += n * _lh(f_c) + 12
        return h
    if k == "steps":
        n = len(card["steps"])
        bw = (width - 2 * PAD - (n - 1) * 36) / n
        f = font(22 * s)
        lines = max(len(wrap(t, f, bw - 20)) for t in card["steps"])
        return 2 * PAD + lines * _lh(f) + 26
    if k == "bars":
        return 2 * PAD + _lh(font(25 * s, True)) + 10 + len(card["items"]) * int(44 * s) + 8
    if k == "quote":
        f_l = font(21 * s, True)
        f = font(22 * s)
        n = len(wrap(card["text"], f, width - 2 * PAD - 10))
        return 2 * PAD + _lh(f_l) + 6 + n * _lh(f)
    raise ValueError(k)


def stat_row_height(cards, s, width):
    cw = (width - (len(cards) - 1) * GAP) / len(cards)
    best = 0
    for c in cards:
        f_h = font(33 * s, True)
        f_s = font(21 * s)
        n_h = len(wrap(c["head"], f_h, cw - 2 * PAD))
        n_s = len(wrap(c.get("sub", ""), f_s, cw - 2 * PAD))
        best = max(best, 2 * PAD + n_h * _lh(f_h) + n_s * _lh(f_s) + 8)
    return best


def group_cards(cards):
    """Consecutive stat cards share one row (max 4)."""
    groups, cur = [], []
    for idx, c in enumerate(cards):
        if c["kind"] == "stat":
            cur.append((idx, c))
            if len(cur) == 4:
                groups.append(("stats", cur))
                cur = []
        else:
            if cur:
                groups.append(("stats", cur))
                cur = []
            groups.append(("card", [(idx, c)]))
    if cur:
        groups.append(("stats", cur))
    return groups


def layout(scene, s):
    """Return (title_lines, title_font, blocks, total_height) where blocks = [(kind, items, y, h)]."""
    f_title = font(44 * s, True)
    title_lines = wrap(scene["title"], f_title, INNER_W)
    y = 100 + len(title_lines) * _lh(f_title) + 16
    blocks = []
    for kind, items in group_cards(scene["cards"]):
        if kind == "stats":
            h = stat_row_height([c for _, c in items], s, INNER_W)
        else:
            h = measure_card(items[0][1], s, INNER_W)
        blocks.append((kind, items, y, h))
        y += h + GAP
    return title_lines, f_title, blocks, y - GAP


def fit_scale(scene):
    for s in (1.25, 1.18, 1.12, 1.06, 1.0, 0.94, 0.88, 0.82, 0.76, 0.70, 0.64):
        _, _, _, total = layout(scene, s)
        if total <= H - 60:
            return s, total
    raise ValueError(f"scene does not fit even at min scale: {scene['title']!r}")


# ---------------------------------------------------------------- drawing
def background():
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    return img


def draw_text_block(d, x, y, lines, f, fill, spacing=None):
    lh = spacing or _lh(f)
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y


def draw_card(d, x, y, w, h, color, visible=True):
    d.rounded_rectangle((x, y, x + w, y + h), radius=14, fill=CARD_BG, outline=color, width=3)


def draw_card_item(d, card, x, y, w, h, s):
    k = card["kind"]
    col = PAL[card.get("color", "sky")]
    if k == "row":
        draw_card(d, x, y, w, h, col)
        lab_w = int(330 * s)
        f_lab = font(25 * s, True)
        f_txt = font(24 * s)
        draw_text_block(d, x + PAD, y + PAD, wrap(card["label"], f_lab, lab_w), f_lab, col, _lh(f_txt))
        txt_x = x + PAD + lab_w + 24
        draw_text_block(d, txt_x, y + PAD, wrap(card["text"], f_txt, w - (txt_x - x) - PAD), f_txt, TEXT)
    elif k == "callout":
        d.rounded_rectangle((x, y, x + w, y + h), radius=14, fill=(52, 46, 22), outline=col, width=3)
        f = font(26 * s, True)
        lines = wrap(card["text"], f, w - 2 * PAD - 20)
        ty = y + PAD
        for ln in lines:
            tw = f.getlength(ln)
            d.text((x + (w - tw) / 2, ty), ln, font=f, fill=col)
            ty += _lh(f)
    elif k == "table":
        draw_card(d, x, y, w, h, col)
        f_t = font(25 * s, True)
        f_h = font(21 * s, True)
        f_c = font(21 * s)
        cy = y + PAD
        d.text((x + PAD, cy), card["title"], font=f_t, fill=col)
        cy += _lh(f_t) + 8
        cws = [int(w * fr) for fr in card["widths"]]
        cws[-1] = w - 2 * PAD - sum(cws[:-1])
        hdr_lines = max(len(wrap(hd, f_h, cw - 16)) for hd, cw in zip(card["headers"], cws))
        hh = hdr_lines * _lh(f_h) + 12
        d.rounded_rectangle((x + PAD, cy, x + w - PAD, cy + hh), radius=8, fill=HEAD_BG)
        cx = x + PAD
        for hd, cw in zip(card["headers"], cws):
            draw_text_block(d, cx + 8, cy + 6, wrap(hd, f_h, cw - 16), f_h, col, _lh(f_h))
            cx += cw
        cy += hh
        for ri, r in enumerate(card["rows"]):
            rl = [wrap(str(c), f_c, cw - 16) for c, cw in zip(r, cws)]
            n = max(len(z) for z in rl)
            rh = n * _lh(f_c) + 12
            if ri % 2 == 1:
                d.rectangle((x + PAD, cy, x + w - PAD, cy + rh), fill=ALT_BG)
            cx = x + PAD
            for j, (lines, cw) in enumerate(zip(rl, cws)):
                colr = TEXT if j > 0 else col
                draw_text_block(d, cx + 8, cy + 6, lines, f_c, colr, _lh(f_c))
                cx += cw
            cy += rh
    elif k == "steps":
        draw_card(d, x, y, w, h, col)
        n = len(card["steps"])
        bw = (w - 2 * PAD - (n - 1) * 36) / n
        f = font(22 * s)
        bx = x + PAD
        for i, t in enumerate(card["steps"]):
            d.rounded_rectangle((bx, y + PAD, bx + bw, y + h - PAD), radius=10,
                                fill=HEAD_BG, outline=col, width=2)
            draw_text_block(d, bx + 10, y + PAD + 8, wrap(t, f, bw - 20), f, TEXT, _lh(f))
            if i < n - 1:
                ax = bx + bw + 6
                ay = y + h / 2
                d.line([(ax, ay), (ax + 24, ay)], fill=col, width=3)
                d.polygon([(ax + 24, ay - 7), (ax + 36, ay), (ax + 24, ay + 7)], fill=col)
            bx += bw + 36
    elif k == "bars":
        draw_card(d, x, y, w, h, col)
        f_t = font(25 * s, True)
        f_l = font(22 * s)
        f_v = font(22 * s, True)
        d.text((x + PAD, y + PAD), card["title"], font=f_t, fill=col)
        cy = y + PAD + _lh(f_t) + 10
        row_h = int(44 * s)
        label_w = int(430 * s)
        value_w = int(200 * s)
        bar_max = w - 2 * PAD - label_w - value_w - 10
        mx = card.get("max") or max(v for _, v, _ in card["items"])
        for label, v, vt in card["items"]:
            ly = cy + (row_h - _lh(f_l)) // 2
            d.text((x + PAD, ly), label, font=f_l, fill=TEXT)
            bx0 = x + PAD + label_w
            bl = max(int(bar_max * v / mx), 4)
            bh = int(row_h * 0.55)
            by0 = cy + (row_h - bh) // 2
            d.rounded_rectangle((bx0, by0, bx0 + bl, by0 + bh), radius=6, fill=col)
            d.text((bx0 + bl + 10, ly), vt, font=f_v, fill=TEXT)
            cy += row_h
    elif k == "quote":
        draw_card(d, x, y, w, h, col)
        f_l = font(21 * s, True)
        f = font(22 * s)
        d.text((x + PAD, y + PAD), card["label"], font=f_l, fill=col)
        draw_text_block(d, x + PAD, y + PAD + _lh(f_l) + 6,
                        wrap(card["text"], f, w - 2 * PAD - 10), f, (200, 210, 225), _lh(f))


def draw_stat_row(d, items, x, y, w, h, s):
    n = len(items)
    cw = (w - (n - 1) * GAP) / n
    for i, (_, c) in enumerate(items):
        cx = x + i * (cw + GAP)
        col = PAL[c.get("color", "sky")]
        draw_card(d, cx, y, cw, h, col)
        f_h = font(33 * s, True)
        f_s = font(21 * s)
        ny = draw_text_block(d, cx + PAD, y + PAD, wrap(c["head"], f_h, cw - 2 * PAD), f_h, col, _lh(f_h))
        draw_text_block(d, cx + PAD, ny + 4, wrap(c.get("sub", ""), f_s, cw - 2 * PAD), f_s, TEXT, _lh(f_s))


def render_stage(scene, scene_no, n_scenes, chapter, stage, out_path):
    s, _ = fit_scale(scene)
    title_lines, f_title, blocks, _ = layout(scene, s)
    img = background()
    d = ImageDraw.Draw(img)

    # top chrome bar
    d.rectangle((0, 0, W, 44), fill=CHROME)
    d.text((SIDE, 11), TITLE_TOP, font=font(20, True), fill=MUTED)
    cl = f"CHAPTER · {chapter.upper()}"
    d.text((W - SIDE - font(20, True).getlength(cl), 11), cl, font=font(20, True), fill=PAL["sky"])

    # tag pill (e.g. "HOSTEL SUBSIDY · CLAUSE 7")
    tag = scene.get("tag", "")
    if tag:
        f_tag = font(19, True)
        tw = f_tag.getlength(tag)
        d.rounded_rectangle((SIDE, 60, SIDE + tw + 28, 92), radius=12, fill=(20, 40, 70),
                            outline=PAL["sky"], width=2)
        d.text((SIDE + 14, 66), tag, font=f_tag, fill=PAL["sky"])

    # title
    ty = 100
    for ln in title_lines:
        d.text((SIDE, ty), ln, font=f_title, fill=TEXT)
        ty += _lh(f_title)

    # cards (reveal: stage k shows the first k cards)
    visible = stage
    for kind, items, y, h in blocks:
        shown = [(i, c) for i, c in items if i < visible]
        if not shown:
            continue
        if kind == "stats":
            draw_stat_row(d, shown, SIDE, y, INNER_W, h, s)
        else:
            i, c = shown[0]
            draw_card_item(d, c, SIDE, y, INNER_W, h, s)

    # bottom timestamp-style bar
    d.rectangle((0, H - 36, W, H), fill=CHROME)
    d.text((SIDE, H - 29), FOOTER, font=font(18), fill=MUTED)
    rt = f"Scene {scene_no:03d} / {n_scenes:03d}   ·   Card {min(stage, len(scene['cards']))} / {len(scene['cards'])}"
    d.text((W - SIDE - font(18, True).getlength(rt), H - 29), rt, font=font(18, True), fill=PAL["yellow"])
    img.save(out_path)


# ---------------------------------------------------------------- media helpers
def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {' '.join(cmd)}\n{r.stderr[-800:]}")
    return r


def probe_duration(path):
    r = subprocess.run([FFMPEG, "-i", str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    m = re.search(r"Duration: (\d+):(\d+):(\d+(?:\.\d+)?)", r.stderr)
    if not m:
        raise RuntimeError(f"cannot read duration: {path}")
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def chapter_of(scenes, idx):
    return scenes[idx]["chapter"]


def scene_clip(idx):
    return CLIP_DIR / f"{idx:03d}.mp3"


def build_scene_video(idx, scene, n_stages, stage_pngs, dur):
    """One MP4 per scene: stills (one per reveal stage) timed to the narration length, plus audio."""
    lst = SEG_DIR / f"scene_{idx:03d}.txt"
    per = dur / n_stages
    lines = []
    for k, p in enumerate(stage_pngs):
        lines.append(f"file '{p.resolve()}'")
        lines.append(f"duration {per:.3f}")
    lines.append(f"file '{stage_pngs[-1].resolve()}'")
    lst.write_text("\n".join(lines) + "\n")
    out = SEG_DIR / f"scene_{idx:03d}.mp4"
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
         "-i", str(scene_clip(idx)),
         "-vf", f"fps={FPS},format=yuv420p", "-c:v", "libx264", "-preset", "veryfast",
         "-tune", "stillimage", "-crf", "24",
         "-c:a", "aac", "-b:a", "96k", "-ar", "48000", "-ac", "2",
         "-t", f"{dur:.3f}", "-movflags", "+faststart", str(out)])
    return out


# ---------------------------------------------------------------- content
SCENES = []
SCENES += [
  {"chapter": "Start Here", "tag": "INTRO · OM DOPT-1668597747466",
   "title": "Honorarium to Inquiry Officers and Presenting Officers: DoPT OM of 16 November 2022, card by card",
   "cards": [
     {"kind": "stat", "color": "cyan", "head": "90 / 70 / 60%", "sub": "Retired IO: of monthly basic pension, by witness count"},
     {"kind": "stat", "color": "green", "head": "15%", "sub": "Serving IO: of monthly basic pay drawn, per case"},
     {"kind": "stat", "color": "orange", "head": "10%", "sub": "Presenting Officer: of monthly basic pay drawn, per case"},
     {"kind": "stat", "color": "purple", "head": "Rs 5,000", "sub": "Per extra charged officer, common proceedings (IO only)"},
     {"kind": "row", "color": "sky", "label": "Scope", "text": "Ministries and Departments: departmental inquiries, including ICC (sexual harassment) inquiries. Rates apply to bills processed on or after 16.11.2022 (Para 15)."}],
   "narr": "Namaste dosto. Aaj hum DoPT ka Office Memorandum dated 16 November 2022 samjhenge, jo Inquiry Officer aur Presenting Officer ke honorarium ko govern karta hai. Is video mein paras 1 se 17 tak, rate tables, worked examples, aur guide ki galtiyan, sab cover hongi. Upar ke chaar stat cards poora rate-sheet hain: retired IO ko 90, 70 ya 60 percent, serving IO ko 15 percent, Presenting Officer ko 10 percent, aur common proceedings mein har extra charged officer ke liye 5,000 rupees. Har number ke saath OM ka paragraph reference diya gaya hai.",
   "spk": "teacher"},

  {"chapter": "Start Here", "tag": "OM IDENTITY · WHAT IS BINDING",
   "title": "Which order governs: identity, issuer and current status of the OM",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Order identity and status",
      "headers": ["Field", "Detail", "Status"],
      "rows": [
        ["Order number", "DOPT-1668597747466 · Government of India, DoPT, AVD (AVD-I/C-I), North Block, New Delhi", "VERIFIED"],
        ["Date and signatory", "16 November 2022 · signed by Rupesh Kumar, Under Secretary", "VERIFIED"],
        ["Subject", "Grant of Honorarium to IO / PO in departmental inquiries conducted by Ministries and Departments", "VERIFIED"],
        ["Concurrence", "Department of Expenditure I.D. Note 14/4/2009-E.II(B) dated 26.10.2022 (Para 17)", "Date VERIFIED; I.D. number NOT VERIFIED"],
        ["Supersedes", "OM 142/15/2010-AVD.I dated 31.07.2012 (serving part-time IO/PO) and OM 142/40/2015-AVD.I dated 15.09.2017 (retired IO)", "VERIFIED (Para 3)"],
        ["Current status", "Still cited in 2025 and 2026 ministry documents; no later OM superseding it found in search", "VERIFIED (search, Oct 2026)"]],
      "widths": [0.22, 0.56, 0.22]},
     {"kind": "row", "color": "green", "label": "Bottom line", "text": "Bills follow this OM. A 2012 or 2017 rate in a bill is an error, even where a ministry letter still quotes it."}],
   "narr": "Sir, yeh DOPT-1668597747466 wala OM hai kya, aur kya 2025 ya 2026 mein iska koi naya version aaya hai? Table mein order number, date, signatory, supersession aur current status hain, har line ke saath tag.", 
   "spk": "student"},

  {"chapter": "Start Here", "tag": "TAG KEY · HOW TO READ THE CARDS",
   "title": "How to read the tags on every card",
   "cards": [
     {"kind": "stat", "color": "green", "head": "VERIFIED", "sub": "Matched to the OM text or a reliable copy"},
     {"kind": "stat", "color": "red", "head": "GUIDE FIX", "sub": "Error or omission in the uploaded guide, corrected here"},
     {"kind": "stat", "color": "orange", "head": "NOT VERIFIED", "sub": "Outside the OM text, or only in a ministry letter. Confirm before use"},
     {"kind": "stat", "color": "cyan", "head": "ON-SCREEN", "sub": "English only. Narration is Hinglish, Roman script"}],
   "narr": "Har card par ek tag hota hai. Green VERIFIED ka matlab hai ki baat OM ke text se match karti hai. Red GUIDE FIX ka matlab hai ki uploaded guide mein galti ya kami thi, aur yahan use theek kiya gaya hai. Orange NOT VERIFIED ka matlab hai ki baat OM ke text mein nahi hai, ya sirf kisi ministry ke letter mein hai. Aise item ko bill mein use karne se pehle confirm karna zaroori hai. On-screen text sirf English mein hai, aur narration Hinglish mein hai.",
   "spk": "teacher"},

  {"chapter": "Start Here", "tag": "GUIDE AUDIT · ERRORS CORRECTED",
   "title": "Guide errors corrected in this video",
   "cards": [
     {"kind": "table", "color": "red", "title": "Guide statements corrected",
      "headers": ["Guide statement", "Correction in this video", "Basis"],
      "rows": [
        ["Para 15: bills settled at old rates are 'dobara nahi khola jaata'; the arrears window 'generally band hota hai'", "Too absolute. Bills paid at 2012 rates between 16.11.2022 and 02.01.2023 can be reopened for the difference on IO/PO request", "CGDA letter 16.08.2023 (MoD Finance), item iii"],
        ["'DA' used for Disciplinary Authority, Dearness Allowance and Daily Allowance", "Three different things. This video writes each one out in full", "OM Para 4(a)(i)+, Para 13, Para 14"],
        ["'Basic pay drawn' with no reference date for serving IO/PO", "Basic pay drawn on the date of nomination as IO/PO", "CGDA letter item iv, quoting CVC 05.12.2022 Para 3"],
        ["Transport booking analogy: 'MMT/BLTC-type' authorised booking rules", "Not in the OM. Dropped. Only the OM conditions are used: approval, authorised agency, cheapest fare", "OM Para 4(a)(i)+"],
        ["'PO practically hamesha serving officer hi hota hai'", "Interpretation, not an OM rule. Marked NOT VERIFIED", "OM Para 4(b) is silent on officer status"]],
      "widths": [0.38, 0.40, 0.22]}],
   "narr": "Ab guide ki galtiyan dekhte hain. Pehli galti Para 15 ki hai: guide kehti hai ki purane rates par settle hue bills dobara nahi khulte. Lekin MoD Finance ka clarification, jo CGDA letter dated 16 August 2023 mein hai, kehta hai ki 16 November 2022 se 2 January 2023 ke beech 2012 rates par paid cases ko IO ya PO ki request par reopen kiya ja sakta hai. Doosri galti 'DA' shabd ka use hai, jo Disciplinary Authority, Dearness Allowance aur Daily Allowance teeno ke liye chala hai. Teesri, basic pay ki reference date guide mein nahi hai. Chauthi, MMT aur BLTC wala travel analogy OM mein nahi hai, isliye hata diya gaya hai. Paanchvi, PO ke serving hone wala claim interpretation hai, isliye NOT VERIFIED mark kiya gaya hai.",
   "spk": "teacher"},

  {"chapter": "Start Here", "tag": "GAPS · NOT VERIFIED · OUTSIDE THE OM",
   "title": "What the guide leaves out, and what stays unverified",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Gaps filled and open items",
      "headers": ["Item", "Status", "Treatment in this video"],
      "rows": [
        ["No 50% reduction if the inquiry runs past 180 days", "GAP FILLED · VERIFIED via CGDA letter", "Chapter: 180-Day Deadline"],
        ["Basic pay on the date of nomination", "GAP FILLED · VERIFIED via CGDA letter", "Chapter: Basic Pay and CVC"],
        ["Time-based flat amounts in ministry empanelment letters (e.g. MIB 2024)", "NOT VERIFIED · ministry-specific", "Not applied. Check your own appointment letter"],
        ["2017 OM terms: 8 cases a year, 4 at a time, 50% on report, balance later", "NOT VERIFIED · whether still operative after 2022", "Shown for contrast only, in the sources card"],
        ["'Section-officer engagement is ultra vires'; 'PO practically always serving'; 'MMT/BLTC'", "NOT VERIFIED · guide interpretation", "Tagged where used"]],
      "widths": [0.42, 0.30, 0.28]}],
   "narr": "Guide ne kuch cheezein chhodi hain, aur kuch cheezein sirf ministry letters mein hain. MoD Finance ka clarification bataata hai ki 180 din se zyada chalne par koi 50 percent cut nahi hai, aur basic pay ki date bhi wahin se li gayi hai. Lekin kuch ministry letters mein time-based flat amounts hain, aur 2017 ke OM mein 8 cases a year aur 50 percent payment on report jaisi shartein thin. Yeh OM 2022 ke text mein nahi hain, isliye inhe NOT VERIFIED mark kiya gaya hai aur sirf comparison ke liye dikhaya gaya hai. Apne appointment letter aur DDO se hamesha confirm karein.",
   "spk": "teacher"},

  {"chapter": "History and Applicability", "tag": "PARA 1–3 · TIMELINE",
   "title": "Timeline: two older OMs, one consolidated OM, and the dates that matter",
   "cards": [
     {"kind": "steps", "color": "cyan", "steps": [
        "31.07.2012: serving part-time IO/PO rates (OM 142/15/2010)",
        "15.09.2017: retired IO rates (OM 142/40/2015)",
        "26.10.2022: DoE I.D. note concurrence",
        "16.11.2022: consolidated OM issued (this OM)",
        "02.01.2023: HQ circulation date cited in CGDA letter"]},
     {"kind": "row", "color": "green", "label": "Use", "text": "Bills processed on or after 16.11.2022 take the new rates (Para 15). Older bills: see the reopening window in the Para 15 chapter."}],
   "narr": "Timeline dekhiye. 2012 mein serving part-time IO aur PO ke rates the. 2017 mein retired IO ke rates aaye. Phir 26 October 2022 ko Department of Expenditure ka concurrence aaya, aur 16 November 2022 ko consolidated OM jaari hua. Circulation ki date 2 January 2023 hai, jo CGDA letter mein dikhti hai. Bill us date par process hota hai jab uspar Para 15 lagu hota hai. Purane 2012 aur 2017 ke rates ab chalte nahi, sirf reopening wali window ke alawa.",
   "spk": "teacher"},

  {"chapter": "History and Applicability", "tag": "PARA 1–3 · OM WORDING",
   "title": "Paras 1 to 3: what the OM says about its own history",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "OM PARA 1–3 (verbatim)",
      "text": "1. The rates of honorarium payable to Inquiry Officer (IO) / Presenting Officer (PO) in the case of departmental inquiries were last revised vide O.M No.142/15/2010-AVD.I dated 31st July, 2012 in the case of serving Government Servants functioning as part time IO/PO and vide O.M No.142/40/2015-AVD.I dated 15th September, 2017 in the case of retired Govt. Servants functioning as IO. 2. The existing rates were reviewed in consultation with Department of Expenditure and it has been decided to revise the existing rates. 3. Accordingly, these consolidated guidelines are being issued in supersession of DoPT's OMs dated 31.07.2012 and 15.09.2017."},
     {"kind": "callout", "color": "yellow", "text": "CHECK: a 2012 or 2017 rate in any bill is an error. Para 3 supersedes both OMs."}],
   "narr": "Para 1 se 3 mein OM apna history bataata hai. Serving part-time IO aur PO ke rates 2012 ke OM mein the, aur retired IO ke rates 2017 ke OM mein. Para 2 kehta hai ki Department of Expenditure ke saath consultation ke baad rates revise huye. Para 3 mein clear supersession hai: yeh consolidated guidelines purane dono OMs ki jagah hain. Isliye koi bhi bill purane rates par banana galat hai.",
   "spk": "teacher"},

  {"chapter": "History and Applicability", "tag": "PARA 5 · WHO IS COVERED",
   "title": "Para 5: the rates also cover ICC sexual-harassment inquiries",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "OM PARA 5 (verbatim, first sentence)",
      "text": "5. The revised structure of rates of honorarium and allowances as indicated above are intended to be made applicable to Departmental Proceedings including inquiry proceedings undertaken by the committee on Sexual Harassment, by Ministries / Departments in respect of officials / officers serving under different cadres of services under their administrative control."},
     {"kind": "row", "color": "green", "label": "ICC inquiries", "text": "Covered. Inquiries by the Committee on Sexual Harassment are named expressly in Para 5."},
     {"kind": "row", "color": "red", "label": "Objection rejected", "text": "'This applies only to CCA Rule 14 inquiries' is wrong. The OM names ICC inquiries."}],
   "narr": "Para 5 mein ek bahut important baat hai. Yeh rates sirf CCA Rule 14 ki departmental inquiries par nahi, balki Committee on Sexual Harassment ki inquiries par bhi lagu hote hain. Agar koi kahe ki yeh sirf Rule 14 ke liye hai, toh OM ka text us objection ko reject karta hai. Covered officials wahi hain jo Ministry ke administrative control mein different cadres mein kaam karte hain.",
   "spk": "teacher"},

  {"chapter": "History and Applicability", "tag": "PARA 5 · CARVE-OUTS AND CEILING",
   "title": "Para 5 carve-outs: own rules can survive, but funded autonomous bodies face a ceiling",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Who may keep separate honorarium rules",
      "headers": ["Case", "Own rules?", "Test to apply"],
      "rows": [
        ["Service cadre with separate IO/PO honorarium rules already in existence", "May continue its own instructions", "Rules in existence; the OM does not force a change"],
        ["Autonomous body, fully or partially funded by Government", "May keep its own provisions", "Not more beneficial than the OM rates. Equal or lower is allowed"],
        ["Ministry or Department, own cadre", "OM rates apply", "Paras 4(a) and 4(b) rates"],
        ["Autonomous body with no Government funding", "OM text does not state the ceiling", "NOT VERIFIED: the ceiling names only fully or partially funded bodies"]],
      "widths": [0.36, 0.28, 0.36]},
     {"kind": "callout", "color": "yellow", "text": "TEST: own rules survive only if they are not more beneficial than the OM."}],
   "narr": "Para 5 ke do carve-outs hain. Pehla, agar kisi cadre ya service ke paas pehle se alag IO aur PO honorarium rules hain, toh woh apne instructions continue kar sakte hain. Doosra, fully ya partially funded autonomous bodies apne provisions rakh sakti hain, lekin shart yeh hai ki woh OM ke rates se zyada beneficial na hon. Unfunded autonomous body ke liye OM ki ceiling clear nahi hai, isliye woh point NOT VERIFIED hai.",
   "spk": "teacher"},
]

SCENES += [
  {"chapter": "Retired IO Honorarium", "tag": "PARA 4(a)(i) · OM WORDING",
   "title": "Para 4(a)(i): retired IO honorarium, three witness categories",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "OM PARA 4(a)(i) (verbatim)",
      "text": "4. The rates of honorarium as revised are indicated in the table below: (a) The rates of honorarium payable to the Inquiry Officer: (i) Retired officers. Honorarium: Category I, where number of witnesses cited in the charge sheet is more than 10: an amount equal to 90% of the monthly basic pension drawn. Category II, where number of witnesses cited in the charge sheet are between 6-10: an amount equal to 70% of the monthly basic pension drawn. Category III, where number of witnesses cited in the charge sheet is less than 6: an amount equal to 60% of the monthly basic pension drawn. Rate per case (in rupees)."},
     {"kind": "row", "color": "green", "label": "Rate base", "text": "Monthly basic pension drawn. Dearness Allowance is not part of this base."}],
   "narr": "Ab retired IO ka honorarium. Para 4(a)(i) mein teen categories hain, aur har category ka driver hai charge sheet mein cited witnesses ki sankhya. Category I mein 10 se zyada witnesses hain, yaani 11 ya usse zyada, aur rate 90 percent hai. Category II mein 6 se 10 witnesses hain, aur rate 70 percent. Category III mein 6 se kam, aur rate 60 percent. Base monthly basic pension drawn hai, Dearness Allowance nahi.",
   "spk": "teacher"},

  {"chapter": "Retired IO Honorarium", "tag": "PARA 4(a)(i) · WITNESS BRACKETS",
   "title": "Witness brackets and the rate for each",
   "cards": [
     {"kind": "table", "color": "cyan", "title": "Retired IO: honorarium by witness bracket",
      "headers": ["Category", "Witnesses cited in charge sheet", "Honorarium per case", "Boundary check"],
      "rows": [
        ["I", "More than 10 (11 or more)", "90% of monthly basic pension drawn", "11 gives Category I"],
        ["II", "6 to 10", "70% of monthly basic pension drawn", "6 and 10 both give Category II"],
        ["III", "Fewer than 6 (5 or fewer)", "60% of monthly basic pension drawn", "5 gives Category III"]],
      "widths": [0.14, 0.30, 0.30, 0.26]},
     {"kind": "row", "color": "sky", "label": "Number line", "text": "1 to 5 = III (60%)   |   6 to 10 = II (70%)   |   11 and above = I (90%)"},
     {"kind": "callout", "color": "yellow", "text": "BOUNDARIES: 5 is Category III, 6 is Category II, 10 is Category II, 11 is Category I."}],
   "narr": "Boundaries dhyan se yaad rakhiye, kyunki exam aur bill dono mein yahin galti hoti hai. 5 witnesses ho toh Category III, 60 percent. 6 ho toh Category II, 70 percent. 10 bhi Category II hai. 11 ho toh Category I, 90 percent. Number line par dekhiye: 1 se 5 Category III, 6 se 10 Category II, aur 11 se upar Category I.",
   "spk": "teacher"},

  {"chapter": "Retired IO Honorarium", "tag": "PARA 4(a)(i) · CHART",
   "title": "Pension Rs 60,000: how the honorarium steps up with the witness count",
   "cards": [
     {"kind": "bars", "color": "cyan", "title": "Honorarium per case at monthly basic pension Rs 60,000",
      "items": [
        ["4 witnesses cited (Category III, 60%)", 36000, "Rs 36,000"],
        ["6 witnesses cited (Category II, 70%)", 42000, "Rs 42,000"],
        ["10 witnesses cited (Category II, 70%)", 42000, "Rs 42,000"],
        ["11 witnesses cited (Category I, 90%)", 54000, "Rs 54,000"],
        ["14 witnesses cited (Category I, 90%)", 54000, "Rs 54,000"]],
      "max": 60000},
     {"kind": "row", "color": "green", "label": "Reading", "text": "The honorarium jumps by Rs 6,000 at 6 witnesses and by Rs 12,000 at 11. Between 6 and 10 it stays flat."}],
   "narr": "Yeh chart dekhiye. Pension Rs 60,000 maan lijiye. 4 witnesses cited hon toh 36,000 rupees. 6 cited hon toh 42,000 rupees, yaani 6,000 ka jump. 10 cited par bhi 42,000, koi change nahi. 11 cited par 54,000, yaani 12,000 ka jump. Yeh chart sirf witness count ka effect dikhata hai, add-ons ko chhod kar.",
   "spk": "teacher"},

  {"chapter": "Retired IO Honorarium", "tag": "PARA 4(a)(i) · WORKED EXAMPLES",
   "title": "Worked examples: three retired IOs, one formula",
   "cards": [
     {"kind": "table", "color": "green", "title": "Honorarium = percentage for the category × monthly basic pension drawn",
      "headers": ["Case", "Witnesses cited", "Category", "Calculation", "Honorarium"],
      "rows": [
        ["A", "14", "I", "90% × Rs 60,000", "Rs 54,000"],
        ["B", "10", "II", "70% × Rs 60,000", "Rs 42,000"],
        ["C", "4", "III", "60% × Rs 60,000", "Rs 36,000"]],
      "widths": [0.10, 0.18, 0.14, 0.34, 0.24]},
     {"kind": "callout", "color": "yellow", "text": "All three figures match the OM rate table. Add-ons come separately."}],
   "narr": "Teen worked examples. Case A: 14 witnesses cited, Category I, 90 percent of 60,000, yaani 54,000 rupees. Case B: 10 witnesses cited, Category II, 70 percent of 60,000, yaani 42,000. Case C: 4 witnesses cited, Category III, 60 percent of 60,000, yaani 36,000. Formula sirf ek hai: category ka percentage, monthly basic pension se multiply karo. Add-ons ko alag se calculate karna hai.",
   "spk": "teacher"},

  {"chapter": "Retired IO Honorarium", "tag": "PARA 4(a)(i) · TRAPS",
   "title": "Traps: cited versus examined, per case versus per hearing, and the pension date",
   "cards": [
     {"kind": "row", "color": "red", "label": "Cited, not examined", "text": "The bracket counts witnesses cited in the charge sheet. If 12 are cited and only 4 are examined, the rate is still Category I."},
     {"kind": "row", "color": "orange", "label": "Per case", "text": "The OM rate is per case. Many hearings inside one case do not multiply the honorarium."},
     {"kind": "row", "color": "orange", "label": "Pension date", "text": "The OM says 'monthly basic pension drawn'. The reference date for pension is NOT VERIFIED; only the serving-officer date is clarified by CGDA."},
     {"kind": "callout", "color": "yellow", "text": "EXAM TRAP: 'cited' and 'examined' are different counts. The OM uses CITED."}],
   "narr": "Teen traps. Pehla: bracket cited witnesses se banta hai, examined se nahi. Agar 12 cited hain aur 4 examine hue, rate phir bhi Category I hai. Doosra: rate per case hai, per hearing nahi. Teesra: pension ki reference date OM mein clear nahi hai, aur CGDA clarification sirf serving officer ki basic pay date batata hai. Isliye pension date NOT VERIFIED mark hai.",
   "spk": "teacher"},

  {"chapter": "Retired IO Honorarium", "tag": "PARA 4(a)(i) · FLOW",
   "title": "Flow: which category applies to a retired IO",
   "cards": [
     {"kind": "steps", "color": "green", "steps": [
        "Count witnesses CITED in charge sheet",
        "11 or more? Category I: 90%",
        "6 to 10? Category II: 70%",
        "Fewer than 6? Category III: 60%",
        "Multiply by monthly basic pension drawn"]},
     {"kind": "row", "color": "sky", "label": "Then", "text": "Add the retired IO add-ons: transport, Daily Allowance and secretarial assistance. Those come in the next chapter."}],
   "narr": "Flow ek hi line mein: pehle cited witnesses ginein. Phir 11 ya zyada hon toh 90 percent, 6 se 10 ho toh 70 percent, aur 6 se kam ho toh 60 percent. Last mein monthly basic pension se multiply karein. Add-ons alag line mein hain.",
   "spk": "teacher"},

  {"chapter": "Retired IO Add-ons", "tag": "PARA 4(a)(i) · ADD-ONS",
   "title": "Retired IO add-ons: transport, Daily Allowance and secretarial assistance",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Retired IO: add-ons on top of the honorarium",
      "headers": ["Add-on", "Amount or rule", "Condition or anchor"],
      "rows": [
        ["Transport allowance", "Rs 40,000 per case, flat", "Lump sum; not linked to witness category"],
        ["Outstation air or rail", "Actual expenses, reimbursed in addition", "Class entitled at retirement; competent authority approval; DoPT/DoE instructions; authorised agency; cheapest fare"],
        ["Daily Allowance", "Same as the officer was entitled to immediately before retirement", "Pre-retirement entitlement. Not Dearness Allowance"],
        ["Secretarial assistance", "Category I: Rs 40,000; II: Rs 30,000; III: Rs 20,000", "Follows the same witness bracket as the honorarium"]],
      "widths": [0.22, 0.36, 0.42]},
     {"kind": "callout", "color": "red", "text": "GUIDE FIX: the guide uses 'DA' for Daily Allowance here, and for Disciplinary Authority elsewhere. Read each use in full."}],
   "narr": "Retired IO ke add-ons teen hain. Pehla, transport allowance 40,000 rupees per case, flat. Doosra, outstation journey mein actual air ya rail kharch, lekin class wahi jo retirement ke waqt entitled thi. Teesra, Daily Allowance, jo retirement se theek pehle ki entitlement ke barabar hai. Chautha, secretarial assistance, jo witness category ke hisaab se 40,000, 30,000 ya 20,000 rupees hai. Guide mein 'DA' ka ek hi shabd teen cheezon ke liye use hua hai, isliye yahan poora naam likha gaya hai.",
   "spk": "teacher"},

  {"chapter": "Retired IO Add-ons", "tag": "PARA 4(a)(i) · CHART",
   "title": "Package example: retired IO, pension Rs 55,000, 9 witnesses cited",
   "cards": [
     {"kind": "bars", "color": "green", "title": "Fixed package, before actual travel and Daily Allowance",
      "items": [
        ["Honorarium: 70% of Rs 55,000 (Category II)", 38500, "Rs 38,500"],
        ["Secretarial assistance (Category II)", 30000, "Rs 30,000"],
        ["Transport allowance (flat)", 40000, "Rs 40,000"]],
      "max": 45000},
     {"kind": "row", "color": "sky", "label": "Total", "text": "Rs 1,08,500 fixed, plus outstation actuals at the entitled class, plus Daily Allowance at the pre-retirement rate."}],
   "narr": "Ek package dekhiye. Pension 55,000 aur 9 witnesses cited, yaani Category II. Honorarium 70 percent, yaani 38,500. Secretarial assistance Category II ke liye 30,000. Transport allowance 40,000 flat. Total fixed package 1,08,500 rupees hai. Iske upar outstation actual kharch aur Daily Allowance alag se milenge.",
   "spk": "teacher"},

  {"chapter": "Retired IO Add-ons", "tag": "PARA 4(a)(i)+ · TRAVEL CONDITIONS",
   "title": "Outstation travel: three conditions before reimbursement",
   "cards": [
     {"kind": "steps", "color": "green", "steps": [
        "Competent authority approves the journey in advance",
        "Tickets booked through an authorised agency",
        "Cheapest available fare, per DoPT/DoE instructions"]},
     {"kind": "row", "color": "red", "label": "Flexi-fare trap", "text": "A business-class ticket bought without prior approval is at risk of non-reimbursement. This follows from the OM conditions."},
     {"kind": "row", "color": "orange", "label": "NOT VERIFIED", "text": "Booking-agency names such as MMT or BLTC appear only in the guide, as an analogy. The OM does not name them."},
     {"kind": "callout", "color": "yellow", "text": "RULE: approval, authorised agency and cheapest fare are all needed. Missing one puts the travel cost at risk."}],
   "narr": "Outstation travel ke liye teen conditions. Pehla, competent authority ki pehle se approval. Doosra, authorised agency se ticket. Teesra, cheapest available fare, DoPT aur DoE ki instructions ke mutabik. Guide mein MMT aur BLTC jaise naam aaye hain, lekin woh OM mein nahi hain, isliye unhe NOT VERIFIED mark kiya gaya hai.",
   "spk": "teacher"},

  {"chapter": "Serving IO Honorarium", "tag": "PARA 4(a)(ii)–(iii) · OM WORDING",
   "title": "Serving IO: 15% of monthly basic pay drawn, per case",
   "cards": [
     {"kind": "quote", "color": "green", "label": "OM PARA 4(a)(ii)–(iii) (verbatim)",
      "text": "(ii) Serving officers: Rate per case (in rupees): an amount equal to 15% of the monthly basic pay drawn. (iii) In case of common disciplinary proceedings, an additional amount of honorarium of Rs. 5000 will be payable to Inquiry Officer (both retired and serving) for every additional charged officer."},
     {"kind": "stat", "color": "cyan", "head": "15%", "sub": "Of monthly basic pay drawn"},
     {"kind": "stat", "color": "green", "head": "No witness slabs", "sub": "Flat rate for a serving IO"},
     {"kind": "stat", "color": "orange", "head": "Basic pay only", "sub": "Dearness Allowance not in the base"},
     {"kind": "stat", "color": "purple", "head": "One case, one 15%", "sub": "Per case"}],
   "narr": "Serving IO, yaani jo officer apni regular duty ke saath part-time inquiry karta hai, uska honorarium 15 percent of monthly basic pay drawn per case hai. Yahan koi witness slab nahi hai, aur koi pension bracket nahi. Basic pay mein Dearness Allowance nahi jodte. Ek case ka ek 15 percent.",
   "spk": "teacher"},

  {"chapter": "Serving IO Honorarium", "tag": "PARA 4(a)(iii) · CHART",
   "title": "Common proceedings: Rs 5,000 for each extra charged officer",
   "cards": [
     {"kind": "bars", "color": "green", "title": "Serving IO, basic pay Rs 1,00,000, per case",
      "items": [
        ["1 charged officer (no extra)", 15000, "Rs 15,000"],
        ["2 charged officers", 20000, "Rs 20,000"],
        ["3 charged officers", 25000, "Rs 25,000"],
        ["4 charged officers", 30000, "Rs 30,000"],
        ["5 charged officers", 35000, "Rs 35,000"]],
      "max": 35000},
     {"kind": "row", "color": "sky", "label": "Formula", "text": "Honorarium = 15% × basic pay + Rs 5,000 × (number of charged officers − 1)."},
     {"kind": "row", "color": "orange", "label": "IO only", "text": "The Rs 5,000 goes to the Inquiry Officer, retired or serving. The OM gives the Presenting Officer no such add-on."}],
   "narr": "Common proceedings mein ek case mein kai charged officers ho sakte hain. Har additional charged officer par 5,000 rupees extra. Chart mein basic pay 1,00,000 hai. Ek charged officer par sirf 15,000. Chaar par 30,000, yaani 15,000 plus 3 extra, jo 15,000 banta hai. Yeh Rs 5,000 IO ko milta hai, PO ko nahi.",
   "spk": "teacher"},

  {"chapter": "Serving IO Honorarium", "tag": "PARA 4(a)(ii)–(iii) · WORKED EXAMPLES",
   "title": "Worked examples: serving IO and retired IO on the same multi-officer case",
   "cards": [
     {"kind": "table", "color": "green", "title": "Same case, four charged officers",
      "headers": ["Officer", "Base", "Rule", "Honorarium"],
      "rows": [
        ["Serving IO", "Basic pay Rs 1,00,000", "15% × 1,00,000 + Rs 5,000 × (4 − 1)", "Rs 30,000"],
        ["Retired IO", "Pension Rs 60,000; 8 witnesses cited (Category II)", "70% × 60,000 + Rs 5,000 × (4 − 1)", "Rs 57,000"]],
      "widths": [0.18, 0.30, 0.34, 0.18]},
     {"kind": "row", "color": "sky", "label": "Check", "text": "Serving: 15,000 + 15,000 = 30,000. Retired: 42,000 + 15,000 = 57,000. Retired add-ons (transport, secretarial, Daily Allowance) are extra."}],
   "narr": "Do worked examples ek hi case par. Serving IO: basic pay 1,00,000, 15 percent 15,000, plus 4 officers ka 15,000 extra, total 30,000. Retired IO: pension 60,000, 8 witnesses cited, Category II, 70 percent 42,000, plus 15,000 common proceedings, total 57,000. Retired IO ke transport, secretarial aur Daily Allowance is total mein nahi hain.",
   "spk": "teacher"},
]

SCENES += [
  {"chapter": "Presenting Officer", "tag": "PARA 4(b) · OM WORDING",
   "title": "Presenting Officer: 10% of monthly basic pay drawn, per case",
   "cards": [
     {"kind": "quote", "color": "orange", "label": "OM PARA 4(b) (verbatim)",
      "text": "(b) The rates of honorarium payable to the Presenting Officer: Rate per case (in rupees): an amount equal to 10% of the monthly basic pay drawn."},
     {"kind": "bars", "color": "orange", "title": "Same case: one serving IO and one Presenting Officer",
      "items": [
        ["IO: 15% × Rs 95,000 basic pay", 14250, "Rs 14,250"],
        ["PO: 10% × Rs 80,000 basic pay", 8000, "Rs 8,000"]],
      "max": 14250},
     {"kind": "row", "color": "sky", "label": "Reading", "text": "Different bases and different percentages. Each person's rate applies to his or her own basic pay."}],
   "narr": "Presenting Officer, yaani woh officer jo department ki taraf se case present karta hai, uska honorarium 10 percent of monthly basic pay drawn per case hai. Koi witness slab nahi, koi pension bracket nahi. Example: IO ka basic pay 95,000, toh 15 percent 14,250 rupees. PO ka basic pay 80,000, toh 10 percent 8,000 rupees. Dono apne apne basic pay par.",
   "spk": "teacher"},

  {"chapter": "Presenting Officer", "tag": "PARA 4(a)–(b) · IO VERSUS PO",
   "title": "IO and PO side by side: what differs and what does not",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Inquiry Officer and Presenting Officer compared",
      "headers": ["Feature", "Inquiry Officer", "Presenting Officer"],
      "rows": [
        ["Rate per case", "Retired: 90 / 70 / 60% of pension. Serving: 15% of basic pay", "10% of monthly basic pay drawn"],
        ["Witness brackets", "Yes for retired IO; none for serving IO", "None"],
        ["Common proceedings add-on", "Rs 5,000 per extra charged officer", "Not in the OM"],
        ["Transport and secretarial", "Retired IO only: Rs 40,000 transport; secretarial by bracket", "Not in the OM"],
        ["Officer status", "Serving or retired (Para 4(a))", "Para 7 says 'serving or retired', but Para 4(b) has no retired-PO slab. 'PO practically always serving' is NOT VERIFIED"]],
      "widths": [0.24, 0.38, 0.38]},
     {"kind": "callout", "color": "yellow", "text": "EXAM TRAP: the Rs 5,000 and the transport allowance are IO items. The PO gets the 10% only."}],
   "narr": "IO aur PO ka comparison. IO ke paas bracket, add-ons, transport aur secretarial sab hai. PO ke paas sirf 10 percent ka rate hai. Common proceedings wala Rs 5,000 bhi IO ke liye hai. Guide kehti hai ki PO practically hamesha serving hota hai, lekin OM ka Para 4(b) aisa nahi kehta, isliye yeh point NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Conditions of Payment", "tag": "PARA 6 · OM WORDING",
   "title": "Para 6: two conditions for IO and PO honorarium",
   "cards": [
     {"kind": "quote", "color": "sky", "label": "OM PARA 6 (verbatim)",
      "text": "6. The grant of Honorarium in the case of serving Government servants who are appointed as part time Inquiry Officer/ Presenting Officer and retired Government servants appointed as Inquiry Officers will be subject to the following conditions: i. The honorarium will normally be regulated under the financial powers delegated to the Ministries/Departments and taking into account the quantum of work involved in individual disciplinary cases. ii. In the case where serving officers are appointed as IO/PO, the controlling department or the administrative department should make all efforts to relieve the IO/PO of his normal duties to enable him/her to complete the proceedings expeditiously."},
     {"kind": "row", "color": "green", "label": "(i) Financial powers", "text": "Honorarium normally follows the Ministry's delegated financial powers and the quantum of work in each case."},
     {"kind": "row", "color": "sky", "label": "(ii) Relief from duties", "text": "For a serving IO or PO, the department should make all efforts to relieve normal duties, so the inquiry moves fast."}],
   "narr": "Para 6 ki do shartein hain. Pehli, honorarium normally Ministry ki delegated financial powers ke andar hota hai, aur case ke quantum of work ko dekh kar. Doosri, agar serving officer ko IO ya PO banaya gaya hai, toh controlling department ko sabhi efforts karne chahiye ki use normal duties se relieve kiya jaaye, taaki inquiry jaldi khatam ho. Yeh 'all efforts' wala language strong hai, lekin payment ki hard condition nahi hai.",
   "spk": "teacher"},

  {"chapter": "Conditions of Payment", "tag": "PARA 6(ii) · RELIEF FLOW",
   "title": "Flow: a serving officer appointed as IO or PO",
   "cards": [
     {"kind": "steps", "color": "sky", "steps": [
        "Serving officer appointed as IO or PO",
        "Controlling department reviews normal duties",
        "Relief from normal duties recorded where possible",
        "Inquiry runs against the 180-day limit (Para 12)",
        "Honorarium follows the Para 7 gates"]},
     {"kind": "row", "color": "orange", "label": "NOT VERIFIED", "text": "The guide links this to suspension review rules and the 10(4) clause. Those cross-references are not checked against the source, so they are not used here."},
     {"kind": "row", "color": "sky", "label": "Note", "text": "The OM does not make relief a condition of payment. The 180-day clock runs regardless."}],
   "narr": "Flow dekhiye. Serving officer ko IO ya PO banaya, toh department dekhta hai ki uski normal duties kaise relieve ho sakti hain. Relief record hota hai jahan possible ho. Inquiry 180 din ke andar chalti hai. Honorarium Para 7 ke gates ke baad milta hai. Guide mein suspension rules aur 10(4) ka reference hai, lekin woh source se check nahi hua, isliye NOT VERIFIED mark hai.",
   "spk": "teacher"},

  {"chapter": "Payment Gates", "tag": "PARA 7 · OM WORDING",
   "title": "Para 7: three things the IO or PO must do before payment",
   "cards": [
     {"kind": "quote", "color": "red", "label": "OM PARA 7 (verbatim)",
      "text": "7. Before the payment is received by the Inquiry Officer/Presenting Officer, whether serving or retired, it will be the responsibility of IO/PO to ensure that: a. All case records and inquiry report (two ink signed copies) properly documented and arranged is handed over to the office of Disciplinary Authority. b. The report returns findings on each of the Articles of Charge which has been enquired into should specifically deal and address each of the procedural objections, if any, raised by the charged officers as per the extant rules and instructions. c. There should not be any ambiguity in the inquiry report and therefore every care should be taken to ensure that all procedures for conducting departmental inquiries have been followed in accordance with the relevant rules/instructions of disciplinary and appeal Rules to which the delinquent Government officials are governed."}],
   "narr": "Para 7 bahut important hai. Payment receive karne se pehle IO ya PO, chahe serving ho ya retired, teen cheezein ensure karega. Pehla: saare case records aur inquiry report, do ink-signed copies ke saath, Disciplinary Authority ke office mein jama. Doosra: har Article of Charge par findings, aur charged officer ke har procedural objection ka jawab. Teesra: report mein koi ambiguity nahi, aur saari procedures applicable disciplinary aur appeal rules ke mutabik. Ye teen gates hain.",
   "spk": "teacher"},

  {"chapter": "Payment Gates", "tag": "PARA 7 · THE THREE GATES",
   "title": "The three gates, what each requires, and what happens if one is missed",
   "cards": [
     {"kind": "table", "color": "red", "title": "Pre-payment gates under Para 7",
      "headers": ["Gate", "What must be done", "Practical result if missed"],
      "rows": [
        ["(a)", "All case records and the inquiry report handed to the Disciplinary Authority's office, with TWO ink-signed copies, properly documented and arranged", "Payment is not received until the gate is met. A scanned copy alone does not meet the OM text"],
        ["(b)", "Findings on each Article of Charge; each procedural objection by charged officers addressed", "A report silent on an objection is open to challenge; payment is held until it is revised"],
        ["(c)", "No ambiguity; all procedures under the applicable disciplinary and appeal rules followed", "Report sent back for clarification; payment held"]],
      "widths": [0.10, 0.50, 0.40]},
     {"kind": "row", "color": "orange", "label": "NOT VERIFIED", "text": "The 'practical result' column is a reading of 'before the payment is received'. The OM sets no penalty."}],
   "narr": "Teeno gates ek table mein. Gate A: records aur do ink-signed copies. Digital scan se kaam nahi chalta, OM mein ink-signed copies ki baat hai. Gate B: har Article of Charge par finding, aur har objection ka jawab. Gate C: koi ambiguity nahi, aur procedure puri tarah follow hua. Jo 'practical result' column hai, woh hamari reading hai, OM ka penalty nahi, isliye woh NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Payment Gates", "tag": "PARA 7 · WORKED EXAMPLE",
   "title": "Worked example: a payment held at the gate",
   "cards": [
     {"kind": "steps", "color": "red", "steps": [
        "IO emails a PDF of the report only",
        "Registry copy: one signed copy only",
        "Charged officer raises three documents not supplied",
        "Report is silent on that objection",
        "Payment held until revised report and two signed copies"]},
     {"kind": "row", "color": "sky", "label": "Lesson", "text": "Two gates failed: the signed copies, and the unanswered objection. Both are the IO/PO's own duty under Para 7."}],
   "narr": "Ek example. IO ne sirf email PDF bheja, aur registry mein ek hi signed copy gayi. Charged officer ne teen documents supply na hone ka objection uthaya, aur report us par chup thi. Payment hold hua. Jab revised report aayi jo objection ka jawab deti hai, aur do signed copies jama huin, tabhi payment mila. Yeh gate system IO ki zimmedari hai.",
   "spk": "teacher"},

  {"chapter": "Undertaking and Records", "tag": "PARA 8 · UNDERTAKING",
   "title": "Para 8: the IO's undertaking and a certificate for each inquiry",
   "cards": [
     {"kind": "quote", "color": "sky", "label": "OM PARA 8 (verbatim)",
      "text": "8. Terms and conditions for appointment of Inquiry Officer: The designated Inquiry Officer shall be required to give an undertaking as follows: i. that he/she is not a witness or a complainant in the matter to be inquired into or a close relative or a known friend of the delinquent Government officer. A certificate to this effect will be obtained from the Inquiry Officer with respect to every inquiry and placed on record; ii. shall maintain strict secrecy in relation to the documents he/she receives or information/data collected by him/her in connection with the inquiry and utilize the same only for the purpose of inquiry in the case entrusted to him/her."},
     {"kind": "table", "color": "sky", "title": "Undertaking heads",
      "headers": ["Head", "What it covers", "Record"],
      "rows": [
        ["(i)", "Not a witness or complainant; not a close relative or known friend of the delinquent officer", "Certificate for EVERY inquiry, placed on record"],
        ["(ii)", "Strict secrecy on documents and information; used only for the assigned inquiry", "Read with Para 9"]],
      "widths": [0.12, 0.56, 0.32]},
     {"kind": "row", "color": "green", "label": "Practice", "text": "A certificate on record for every inquiry lets a conflict be caught on day one, not mid-inquiry."}],
   "narr": "Para 8 mein IO ka undertaking hai. Woh na witness hona chahiye, na complainant, na delinquent officer ka close relative ya known friend. Yeh certificate har inquiry ke liye lena hai aur record par rakhna hai. Doosra, strict secrecy: jo documents aur information mile, woh sirf us inquiry ke liye use ho sakti hai. Certificate ko formality mat samajhiye, yeh early warning hai.",
   "spk": "teacher"},

  {"chapter": "Undertaking and Records", "tag": "PARA 9 · SECRECY AND RETURN",
   "title": "Para 9: no divulging, and records returned at presentation",
   "cards": [
     {"kind": "quote", "color": "sky", "label": "OM PARA 9 (verbatim)",
      "text": "9. No such documents/information or data shall be divulged to anyone during the Inquiry or after presentation of the Inquiry Report. All the records, reports etc. available with the Inquiry Officer shall be duly returned to the authority which appointed him/her as such, at the time of presentation of the Inquiry Report."},
     {"kind": "stat", "color": "cyan", "head": "During inquiry", "sub": "Nothing divulged to anyone"},
     {"kind": "stat", "color": "green", "head": "After presentation", "sub": "Still nothing divulged"},
     {"kind": "stat", "color": "orange", "head": "Records returned", "sub": "At presentation, to the appointing authority"},
     {"kind": "stat", "color": "purple", "head": "Links to Para 8(ii)", "sub": "Same secrecy duty"}],
   "narr": "Para 9 kehta hai ki inquiry ke dauran aur report submit hone ke baad bhi koi document ya data kisi ko nahi batana hai. Aur presentation ke time saare records appointing authority ko wapas karne hain. Yeh Para 8 ke secrecy undertaking ka hi hissa hai.",
   "spk": "teacher"},

  {"chapter": "Venue, Video Conferencing and Travel", "tag": "PARA 10–11 · VENUE AND TRAVEL",
   "title": "Paras 10 and 11: venue, video conferencing and travel approval",
   "cards": [
     {"kind": "table", "color": "cyan", "title": "How the venue and travel are decided",
      "headers": ["Factor", "What the OM says", "Practical test"],
      "rows": [
        ["Venue", "Availability of records; place where the misconduct occurred; convenience of witnesses and PO", "Choose the venue that serves these three best"],
        ["Video conferencing", "Use it to the maximum extent possible to reduce travel by IO, PO and CO; cadre controlling authorities arrange it", "First option for hearings"],
        ["Travel", "Only in unavoidable circumstances, with approval of an authority nominated by the Ministry or Department", "Get nominated-authority approval before the journey"]],
      "widths": [0.22, 0.46, 0.32]},
     {"kind": "row", "color": "sky", "label": "Link", "text": "Travel is reimbursed under the retired IO add-ons, which also need competent authority approval (Para 4(a)(i)+)."}],
   "narr": "Paras 10 aur 11 mein venue aur travel ki baat hai. Inquiry aisi jagah ho jahan records available hon, misconduct hua ho, aur witnesses aur PO ko convenience ho. Video conferencing ko maximum use karna hai, taaki travel kam ho. Travel tabhi jab unavoidable ho, aur nominated authority ki approval ke saath.",
   "spk": "teacher"},

  {"chapter": "Venue, Video Conferencing and Travel", "tag": "PARA 10–11 · FLOW",
   "title": "Flow: deciding whether a hearing needs travel",
   "cards": [
     {"kind": "steps", "color": "cyan", "steps": [
        "Can the hearing run by video conference?",
        "Yes: run it by VC. No travel",
        "No: is travel unavoidable?",
        "Yes: get approval from the nominated authority",
        "Travel, then claim under the add-ons"]},
     {"kind": "row", "color": "orange", "label": "NOT VERIFIED", "text": "The OM does not name the nominated authority for each Ministry. Check your Department's notice."}],
   "narr": "Flow: pehle video conference ka sawal. Haan toh VC pe hi hearing, travel nahi. Nahi toh dekhiye travel unavoidable hai ya nahi. Haan toh nominated authority se approval lekar travel karein, aur add-ons ke saath claim karein. Nominated authority ka naam har Ministry mein alag ho sakta hai, isliye NOT VERIFIED.",
   "spk": "teacher"},
]

SCENES += [
  {"chapter": "180-Day Deadline", "tag": "PARA 12 · OM WORDING",
   "title": "Para 12: the report is due within 180 days of appointment",
   "cards": [
     {"kind": "quote", "color": "red", "label": "OM PARA 12 (verbatim)",
      "text": "12. The Inquiry Officer shall submit the inquiry report after completing the inquiry within 180 days from the date of his/her appointment as the Inquiry Officer. Extension of time beyond 180 days can be granted only by the Authority as may be prescribed."},
     {"kind": "stat", "color": "cyan", "head": "180 days", "sub": "From the date of appointment as IO"},
     {"kind": "stat", "color": "orange", "head": "Clock starts", "sub": "At appointment, not at the first hearing"},
     {"kind": "stat", "color": "green", "head": "Extension", "sub": "Only by the Authority as may be prescribed"},
     {"kind": "stat", "color": "purple", "head": "No self-extension", "sub": "IO cannot extend on his own"}],
   "narr": "Para 12 ka sabse important clock. IO ko report 180 din ke andar submit karni hai, aur clock appointment ki date se chalta hai, first hearing se nahi. 180 din se aage ka extension sirf wahi authority de sakti hai jo prescribed hai. IO khud ya informal consent se extension nahi le sakta.",
   "spk": "teacher"},

  {"chapter": "180-Day Deadline", "tag": "PARA 12 · MoD(Fin) CLARIFICATION",
   "title": "No 50% cut for an inquiry that runs past 180 days (CGDA letter of 16.08.2023)",
   "cards": [
     {"kind": "table", "color": "green", "title": "Four points from the MoD (Finance) clarification, as quoted by CGDA",
      "headers": ["Point", "Position", "Status"],
      "rows": [
        ["(i)", "Applies prospectively under Para 15. Cases completed before 16.11.2022 with bills later use the old rates", "VERIFIED"],
        ["(ii)", "No 50% reduction for IO/PO if the inquiry runs past 180 days: 'not mentioned anywhere in the OM'", "GAP FILLED"],
        ["(iii)", "Past cases paid at 2012 rates between 16.11.2022 and 02.01.2023 can be reopened on IO/PO request", "GAP FILLED · see Para 15 chapter"],
        ["(iv)", "Basic pay of a serving IO/PO is the pay drawn on the date of nomination (CVC communication 05.12.2022, Para 3)", "GAP FILLED · see Basic Pay chapter"]],
      "widths": [0.10, 0.66, 0.24]},
     {"kind": "callout", "color": "yellow", "text": "Per MoD (Finance), overrunning 180 days does not by itself cut the honorarium under this OM."}],
   "narr": "Ek sawal aata hai: kya inquiry 180 din se zyada chalne par 50 percent cut hota hai? MoD Finance ka clarification, jo CGDA letter dated 16 August 2023 mein quote hua hai, kehta hai ki nahi. Yeh baat OM mein kahin nahi hai. Yahi letter basic pay ki date aur reopening ki window bhi batata hai. Guide mein yeh cheezein nahi thi, isliye yeh gap fill kiya gaya hai.",
   "spk": "teacher"},

  {"chapter": "180-Day Deadline", "tag": "PARA 12 · DATE ARITHMETIC",
   "title": "Date arithmetic: appointed on 1 March, deadline 28 August",
   "cards": [
     {"kind": "table", "color": "red", "title": "Worked example with 2026 dates",
      "headers": ["Event", "Date", "Working"],
      "rows": [
        ["Appointed as IO", "1 March 2026", "Clock starts"],
        ["180th day (deadline)", "28 August 2026", "1 March + 180 days"],
        ["Extension granted in writing", "20 August 2026", "Before expiry, by the prescribed authority"],
        ["Extended deadline", "27 September 2026", "28 August + 30 days"],
        ["Report submitted", "5 September 2026", "Inside the extended period: compliant"]],
      "widths": [0.36, 0.26, 0.38]},
     {"kind": "row", "color": "orange", "label": "NOT VERIFIED", "text": "The day-count convention (whether appointment day is day 0 or day 1) is not stated in the OM. The arithmetic here follows the guide."}],
   "narr": "Date arithmetic. Appointment 1 March 2026, toh 180 din baad 28 August 2026 hai. Extension 20 August ko likhit mein mila, yaani expiry se pehle, toh 30 din aur. Naya deadline 27 September. Report 5 September ko submit hui, toh compliant. Day-count ka convention OM mein nahi hai, isliye woh NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Retired IO Engagement and Disputes", "tag": "PARA 13 · OM WORDING",
   "title": "Para 13: a retired IO needs Disciplinary Authority approval before the letter issues",
   "cards": [
     {"kind": "quote", "color": "purple", "label": "OM PARA 13 (verbatim)",
      "text": "13. Letter regarding engaging a retired officer as the Inquiry Officer will only be issued with the approval of the Disciplinary Authority of the Ministry/Department/ Office concerned."},
     {"kind": "steps", "color": "purple", "steps": [
        "Propose a retired officer as IO",
        "Disciplinary Authority of the Ministry, Department or Office approves",
        "Engagement letter issued",
        "IO signs the Para 8 undertaking",
        "Inquiry starts; Para 12 clock runs"]},
     {"kind": "row", "color": "orange", "label": "NOT VERIFIED", "text": "The guide calls an engagement without DA approval 'ultra vires'. The OM says only that the letter 'will only be issued' with approval."}],
   "narr": "Para 13 ke mutabik, retired officer ko IO banane ka letter tabhi jaari hoga jab Disciplinary Authority, yaani concerned Ministry ya Office ka DA, approve kare. Flow dekhiye: proposal, DA approval, letter, Para 8 ka undertaking, aur phir inquiry. Guide 'ultra vires' jaisa strong word use karti hai, lekin OM ka text itna nahi kehta, isliye yeh NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Retired IO Engagement and Disputes", "tag": "PARA 14 · DISPUTES",
   "title": "Para 14: disputes under this OM go to the Secretary, DoPT, whose decision is final",
   "cards": [
     {"kind": "quote", "color": "purple", "label": "OM PARA 14 (verbatim)",
      "text": "14. Any issue arising out of this O.M. between the Inquiring Officer and the Disciplinary Authority will be decided by the Secretary, DoPT whose decision shall be final and binding on both parties."},
     {"kind": "table", "color": "purple", "title": "Which disputes go to the Secretary, DoPT?",
      "headers": ["Dispute", "In scope?", "Route"],
      "rows": [
        ["IO and DA disagree on how the honorarium is computed under this OM (for example the witness count)", "Yes", "Secretary, DoPT; final and binding on both"],
        ["IO and DA disagree on the rate for a bill processed after 16.11.2022", "Yes", "Secretary, DoPT"],
        ["Dispute unrelated to this OM", "No", "Normal channel. NOT VERIFIED for the forum"]],
      "widths": [0.50, 0.12, 0.38]},
     {"kind": "callout", "color": "yellow", "text": "FINAL AND BINDING: the Secretary's decision binds both the IO and the Disciplinary Authority."}],
   "narr": "Para 14 mein dispute resolution hai. IO aur Disciplinary Authority ke beech is OM se judi koi bhi baat Secretary, DoPT decide karenge, aur unka faisla dono par final aur binding hai. Witness count ya rate ka jhagda isme aata hai. Lekin is OM se unrelated dispute ka forum NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Prospective Application", "tag": "PARA 15 · OM WORDING AND GUIDE FIX",
   "title": "Para 15: prospective for bills, and the guide's 'closed bills' line corrected",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "OM PARA 15 (verbatim)",
      "text": "15. These instructions will be applicable prospectively for processing the Bill submitted by the IOs / POs."},
     {"kind": "row", "color": "red", "label": "GUIDE FIX", "text": "The guide says bills already settled at old rates 'dobara nahi khula jaata' and that the arrears window 'generally' closes. That is too absolute. See the next card."},
     {"kind": "row", "color": "green", "label": "Practical rule", "text": "A bill processed after 16.11.2022 takes the new rates. A bill settled earlier: check the reopening window before closing it."}],
   "narr": "Para 15 kehta hai ki yeh instructions prospectively apply hongi, yaani un bills par jo process hongi. Guide ne kaha tha ki purane rates par settle bill dobara nahi khulte. Yeh bahut absolute hai, aur ek exception hai, jo agle card mein hai. Practical rule: 16 November 2022 ke baad process hone wala bill naye rates par, aur pehle settle bill par reopening window check karein.",
   "spk": "teacher"},

  {"chapter": "Prospective Application", "tag": "PARA 15 · REOPENING · CGDA",
   "title": "Reopening window: bills paid at 2012 rates between 16.11.2022 and 02.01.2023",
   "cards": [
     {"kind": "table", "color": "cyan", "title": "Bill position by processing date",
      "headers": ["Situation", "Position", "Source"],
      "rows": [
        ["Bill processed before 16.11.2022 at old rates", "Settled under old rules. Para 15 is prospective, so the OM does not reopen it", "Reading of OM Para 15"],
        ["Bill paid at 2012 rates between 16.11.2022 and 02.01.2023", "Can be reopened for the difference on IO/PO request", "CGDA letter 16.08.2023, item iii"],
        ["Bill paid at old rates after 02.01.2023", "No reopening point found in the clarification. NOT VERIFIED", "No source found"]],
      "widths": [0.36, 0.42, 0.22]},
     {"kind": "callout", "color": "red", "text": "GUIDE FIX: the reopening applies only to the window 16.11.2022 to 02.01.2023, and only on request."}],
   "narr": "Sir, agar bill 16 November 2022 aur 2 January 2023 ke beech 2012 rates par paid hua tha, toh kya woh reopen ho sakta hai? Haan, IO ya PO ki request par difference reopen ho sakta hai, sirf is window mein paid bills ke liye. Lekin 2 January 2023 ke baad koi aisa point clarification mein nahi mila, isliye woh NOT VERIFIED hai. Guide ka 'band hota hai' wala statement is window ko miss karta hai.",
   "spk": "student"},

  {"chapter": "Circulation and Concurrence", "tag": "PARA 16–17 · OM WORDING",
   "title": "Paras 16 and 17: circulation to all concerned, and the Department of Expenditure concurrence",
   "cards": [
     {"kind": "quote", "color": "sky", "label": "OM PARA 16–17 (verbatim)",
      "text": "16. All the Ministries/Departments are requested to bring these instructions to the notice of all concerned under their control. 17. This issues with the concurrence of Department of Expenditure, Ministry of Finance vide their I. D. Note No. 14/4/2009-E.II(B) dated 26/10/2022. (Sign of Authority) Rupesh Kumar, Under Secretary to the Govt. of India."},
     {"kind": "row", "color": "green", "label": "Concurrence", "text": "Department of Expenditure, dated 26.10.2022. The I.D. number is as printed in the guide's OM text; not checked against a second copy (NOT VERIFIED)."},
     {"kind": "row", "color": "sky", "label": "Distribution", "text": "All Ministries and Departments of the Government of India, and the other offices in the OM's distribution list."}],
   "narr": "Para 16 mein OM ki instructions ko apne control ke saare concerned logon tak pahunchana hai. Para 17 mein Department of Expenditure ka concurrence hai, 26 October 2022 ka I.D. note. I.D. note ka number guide ke text se liya gaya hai, doosri copy se check nahi hua, isliye NOT VERIFIED. Signatory Rupesh Kumar, Under Secretary hain.",
   "spk": "teacher"},

  {"chapter": "Basic Pay and CVC Communication", "tag": "GAP FILL · CGDA / CVC",
   "title": "Which basic pay counts for a serving IO or PO: the nomination-date rule",
   "cards": [
     {"kind": "table", "color": "cyan", "title": "Basic pay reference for serving IO and PO",
      "headers": ["Item", "Rule", "Status"],
      "rows": [
        ["Base for serving IO and PO", "15% (IO) or 10% (PO) of monthly basic pay drawn (Para 4)", "VERIFIED (OM)"],
        ["Reference date", "Basic pay drawn on the date of nomination as IO/PO", "VERIFIED (MoD Finance via CGDA, item iv)"],
        ["Source of that rule", "CVC communication dated 05.12.2022, Para 3", "VERIFIED as quoted in the CGDA letter"],
        ["Guide's wording", "'Basic pay drawn' with no date: ambiguous", "GUIDE FIX (gap filled)"]],
      "widths": [0.28, 0.48, 0.24]},
     {"kind": "row", "color": "sky", "label": "Practice", "text": "Record the basic pay on the nomination order. A later pay revision does not change the base for that appointment."},
     {"kind": "callout", "color": "yellow", "text": "The nomination-date basic pay is the base. Keep the nomination order on file."}],
   "narr": "Basic pay kaunsa count hoga? Guide mein sirf 'basic pay drawn' likha hai, date nahi. CGDA letter mein MoD Finance ka clarification hai ki serving officer ke liye yeh basic pay hai jo nomination ki date par drawn tha, aur yeh CVC ke 5 December 2022 ke communication ke Para 3 se aata hai. Isliye nomination order ko file par rakhein.",
   "spk": "teacher"},
]

SCENES += [
  {"chapter": "Calculator and Master Flow", "tag": "MASTER FLOW · ALL SECTIONS",
   "title": "Master flow: from appointment to payment in five steps",
   "cards": [
     {"kind": "steps", "color": "cyan", "steps": [
        "Appointment: note the date; 180-day clock starts (Para 12)",
        "Who is the IO? Retired: DA approval (Para 13). Serving: relief (Para 6)",
        "Pick the rate rule: Para 4(a)(i), 4(a)(ii), or 4(b)",
        "Add-ons and travel approval (Para 4(a)(i)+, Para 10–11)",
        "Gates (Para 7), then payment; reopening only per CGDA item iii"]},
     {"kind": "row", "color": "sky", "label": "Note", "text": "Each step carries its paragraph reference. Steps flagged NOT VERIFIED need a check against your own orders."}],
   "narr": "Master flow, ek hi slide par. Appointment se clock start hota hai. Phir decide karein ki IO retired hai ya serving, aur uske hisaab se DA approval ya relief dekhein. Teesra, rate rule chunein. Chautha, add-ons aur travel approval. Paanchvan, Para 7 ke gates, aur phir payment. Reopening sirf CGDA item iii ke window mein.",
   "spk": "teacher"},

  {"chapter": "Calculator and Master Flow", "tag": "CALCULATOR · WHICH FORMULA",
   "title": "Calculator: which formula applies to which officer",
   "cards": [
     {"kind": "table", "color": "green", "title": "Formula and worked number for each case",
      "headers": ["Officer", "Formula", "Worked number"],
      "rows": [
        ["Retired IO", "% by witness count × monthly basic pension; + Rs 40,000 transport; + secretarial by bracket; + outstation actuals; + Daily Allowance", "Pension Rs 55,000, 9 witnesses: Rs 38,500 + Rs 40,000 + Rs 30,000 = Rs 1,08,500 fixed"],
        ["Serving IO", "15% × basic pay drawn on nomination date; + Rs 5,000 × (charged officers − 1)", "Basic Rs 1,00,000, 4 officers: Rs 30,000"],
        ["Presenting Officer", "10% × basic pay drawn on nomination date", "Basic Rs 80,000: Rs 8,000"],
        ["IO with common proceedings", "Rs 5,000 for each additional charged officer. PO not included", "Retired IO, 4 officers: + Rs 15,000"]],
      "widths": [0.18, 0.46, 0.36]},
     {"kind": "callout", "color": "yellow", "text": "BEFORE YOU COMPUTE: confirm the rule set (Para 4), the date (nomination), and the gates (Para 7)."}],
   "narr": "Calculator table. Retired IO ka formula: witness bracket ka percentage, pension par. Uske upar transport, secretarial, outstation actuals aur Daily Allowance. Serving IO: 15 percent basic pay par, aur common proceedings ka 5,000 per extra officer. PO: 10 percent. Compute karne se pehle teen cheezein confirm karein: rule set, nomination date, aur Para 7 ke gates.",
   "spk": "teacher"},

  {"chapter": "Calculator and Master Flow", "tag": "QUICK REFERENCE · RATES",
   "title": "Quick reference: every rate and amount in the OM",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Rates and amounts, as on 25 October 2026",
      "headers": ["Item", "Rate or amount", "Para", "Status"],
      "rows": [
        ["Retired IO, more than 10 witnesses cited", "90% of monthly basic pension drawn", "4(a)(i)", "VERIFIED"],
        ["Retired IO, 6 to 10 witnesses cited", "70% of monthly basic pension drawn", "4(a)(i)", "VERIFIED"],
        ["Retired IO, fewer than 6 witnesses cited", "60% of monthly basic pension drawn", "4(a)(i)", "VERIFIED"],
        ["Retired IO transport allowance", "Rs 40,000 per case, plus outstation actuals", "4(a)(i)+", "VERIFIED"],
        ["Retired IO secretarial assistance", "Rs 40,000 / 30,000 / 20,000 by bracket", "4(a)(i)+", "VERIFIED"],
        ["Serving IO", "15% of monthly basic pay drawn", "4(a)(ii)", "VERIFIED"],
        ["Common proceedings", "Rs 5,000 per additional charged officer (IO only)", "4(a)(iii)", "VERIFIED"],
        ["Presenting Officer", "10% of monthly basic pay drawn", "4(b)", "VERIFIED"],
        ["Report deadline", "180 days from appointment; extension only by prescribed authority", "12", "VERIFIED"]],
      "widths": [0.34, 0.40, 0.10, 0.16]}],
   "narr": "Quick reference, sab rates ek table mein. Retired IO 90, 70 aur 60 percent. Transport 40,000. Secretarial 40,000, 30,000 aur 20,000. Serving IO 15 percent. Common proceedings 5,000, sirf IO ke liye. PO 10 percent. Deadline 180 din. Har row ka paragraph bhi diya gaya hai.",
   "spk": "teacher"},

  {"chapter": "Recap and Sources", "tag": "RECAP · PART 1",
   "title": "Recap part 1: rates, scope and the guide corrections",
   "cards": [
     {"kind": "table", "color": "cyan", "title": "Ten points to remember",
      "headers": ["#", "Point"],
      "rows": [
        ["1", "The OM dated 16.11.2022 governs. The 2012 and 2017 OMs are superseded (Para 3)"],
        ["2", "ICC sexual-harassment inquiries are covered (Para 5). Funded autonomous bodies may keep their own rules only if not more beneficial"],
        ["3", "Retired IO: 90 / 70 / 60% of monthly basic pension, by the number of witnesses cited (Para 4(a)(i))"],
        ["4", "Retired IO add-ons: Rs 40,000 transport, Daily Allowance, secretarial Rs 40,000 / 30,000 / 20,000, outstation actuals with approval"],
        ["5", "Serving IO: 15% of monthly basic pay drawn, plus Rs 5,000 for each extra charged officer (Para 4(a)(ii)–(iii))"],
        ["6", "Presenting Officer: 10% of monthly basic pay drawn (Para 4(b))"],
        ["7", "Para 7: records and two ink-signed copies, every Article of Charge, every objection addressed, no ambiguity"],
        ["8", "Para 8: undertaking, and a certificate on record for every inquiry. Para 9: no divulging, records returned"],
        ["9", "Para 12: 180 days from appointment. No 50% cut under MoD (Finance) clarification; extension only by the prescribed authority"],
        ["10", "Para 15: prospective. Reopening for 2012-rate bills paid 16.11.2022 to 02.01.2023, on request (CGDA item iii)"]],
      "widths": [0.08, 0.92]}],
   "narr": "Recap part 1. Dus points. OM 16.11.2022 governs, aur purane dono OMs superseded hain. ICC inquiries bhi covered hain. Retired IO ka 90, 70, 60 percent, witness count ke hisaab se. Retired IO ke add-ons. Serving IO ka 15 percent aur 5,000 per extra officer. PO ka 10 percent. Para 7 ke gates. Para 8 aur 9 ka undertaking aur secrecy. Para 12 ka 180 din. Aur Para 15 mein reopening ki window.",
   "spk": "teacher"},

  {"chapter": "Recap and Sources", "tag": "RECAP · PART 2",
   "title": "Recap part 2: venue, disputes, circulation and basic pay",
   "cards": [
     {"kind": "table", "color": "cyan", "title": "Seven more points",
      "headers": ["#", "Point"],
      "rows": [
        ["11", "Para 10: venue by records, place of misconduct, and witness convenience. Video conferencing first"],
        ["12", "Para 11: travel only if unavoidable, with approval of the nominated authority"],
        ["13", "Para 13: a retired IO's engagement letter is issued only with Disciplinary Authority approval"],
        ["14", "Para 14: disputes under the OM are decided by the Secretary, DoPT, final and binding on both parties"],
        ["15", "Paras 16 and 17: circulation to all concerned; Department of Expenditure concurrence dated 26.10.2022"],
        ["16", "Serving IO and PO base: basic pay drawn on the nomination date (CVC 05.12.2022, Para 3, via CGDA item iv)"],
        ["17", "Guide corrections: 'DA' written in full; reopening window; basic pay date; MMT/BLTC removed; PO status NOT VERIFIED"]],
      "widths": [0.08, 0.92]}],
   "narr": "Recap part 2. Venue ke liye records aur witness convenience, aur video conference pehle. Travel ke liye nominated authority ki approval. Retired IO ke engagement letter ke liye DA approval. Disputes ke liye Secretary, DoPT. Circulation aur DoE concurrence. Basic pay nomination date par. Aur guide ki corrections, jo is video mein tag hain.",
   "spk": "teacher"},

  {"chapter": "Recap and Sources", "tag": "SOURCES · CHECKLIST",
   "title": "Sources, their status, and a checklist before any claim",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Sources used",
      "headers": ["Source", "Used for", "Status"],
      "rows": [
        ["DoPT O.M. DOPT-1668597747466, 16.11.2022 (doptcirculars.nic.in; search copies)", "All rates; Paras 1–17", "VERIFIED"],
        ["MoD (Finance) clarification quoted in CGDA letter No. AN/XIII/13006/2A/Vol-XXII dated 16.08.2023", "Prospective point; 180-day point; reopening; basic pay date", "VERIFIED (text reviewed)"],
        ["CVC communication 05.12.2022, Para 3 (as quoted in the CGDA letter)", "Nomination-date basic pay", "VERIFIED as quoted"],
        ["DoPT O.M. 142/40/2015-AVD.I dated 15.09.2017 (superseded)", "Contrast only: 8 cases a year; 50% on report", "NOT VERIFIED for current use"],
        ["Ministry letters (MIB 2024 empanelment; institute letter with staged payment)", "Time-based amounts; staged payment", "NOT VERIFIED; ministry-specific"]],
      "widths": [0.46, 0.32, 0.22]},
     {"kind": "callout", "color": "yellow", "text": "BEFORE CLAIM: check the appointment order, nomination date, witnesses cited, charged officers, and Para 7 gates."}],
   "narr": "Sources. OM ka text aur CGDA letter mein quote hua MoD Finance clarification verified hain. CVC ka 5 December 2022 ka communication bhi quote ke roop mein verified hai. 2017 ka OM superseded hai, aur uske cases-per-year wali shartein sirf comparison ke liye dikhayi gayi hain. Ministry letters ki time-based amounts NOT VERIFIED hain. Claim se pehle appointment order, nomination date, cited witnesses, charged officers aur Para 7 gates check karein.",
   "spk": "teacher"},
]

# @@CONTENT_END@@

def check_scenes():
    errs = []
    for i, sc in enumerate(SCENES):
        for key in ("chapter", "tag", "title", "cards", "narr", "spk"):
            if key not in sc:
                errs.append(f"scene {i}: missing {key}")
        if sc.get("spk") not in ("teacher", "student"):
            errs.append(f"scene {i}: bad spk")
        if re.search(r"[\u0900-\u097F]", sc.get("narr", "")):
            errs.append(f"scene {i}: Devanagari found in narration")
        if re.search(r"[\u0900-\u097F]", sc.get("title", "")):
            errs.append(f"scene {i}: Devanagari found in title")
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true")
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--check-clips", action="store_true")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--reference", action="store_true")
    ap.add_argument("--only", type=str, default="", help="comma list of scene indices to render")
    args = ap.parse_args()

    if not SCENES:
        print("no scenes defined")
        return 1
    errs = check_scenes()
    if errs:
        print("\n".join(errs))
        return 1

    n = len(SCENES)
    only = {int(x) for x in args.only.split(",") if x.strip()} if args.only else set(range(n))

    if args.audit:
        worst = []
        for i, sc in enumerate(SCENES):
            s, total = fit_scale(sc)
            worst.append((total, s, i, sc["title"]))
            words = len(sc["narr"].split())
            print(f"{i:03d} [{sc['chapter'][:22]:22s}] cards={len(sc['cards'])} scale={s:.2f} "
                  f"height={total:4d} words={words:3d} {sc['spk']:7s} {sc['title'][:60]}")
        print(f"TOTAL scenes={n}  narration words={sum(len(s['narr'].split()) for s in SCENES)}")
        return 0

    if args.reference:
        out = ["# Honorarium to IO/PO — Master Explainer: card reference sheet", "",
               "Source: DoPT O.M. DOPT-1668597747466 dated 16.11.2022. Narration is Hinglish; this sheet is English only.", ""]
        cur = None
        for i, sc in enumerate(SCENES):
            if sc["chapter"] != cur:
                cur = sc["chapter"]
                out += [f"## {cur}", ""]
            out += [f"### {i+1}. {sc['title']}", f"*{sc['tag']}*", ""]
            for c in sc["cards"]:
                if c["kind"] == "stat":
                    out.append(f"- **{c['head']}** — {c.get('sub', '')}")
                elif c["kind"] == "row":
                    out.append(f"- **{c['label']}:** {c['text']}")
                elif c["kind"] == "callout":
                    out.append(f"> {c['text']}")
                elif c["kind"] == "steps":
                    out.append("- Flow: " + " → ".join(c["steps"]))
                elif c["kind"] == "bars":
                    out += ["", f"**{c['title']}**", ""]
                    out += [f"- {lb}: {vt}" for lb, _, vt in c["items"]]
                    out.append("")
                elif c["kind"] == "quote":
                    out.append(f"> **{c['label']}** {c['text']}")
                elif c["kind"] == "table":
                    out += ["", f"**{c['title']}**", "", "| " + " | ".join(c["headers"]) + " |",
                            "|" + "---|" * len(c["headers"])]
                    out += ["| " + " | ".join(str(x) for x in r) + " |" for r in c["rows"]]
                    out.append("")
            out.append("")
        REFERENCE_MD.write_text("\n".join(out))
        print(f"wrote {REFERENCE_MD}")
        return 0

    for d in (SLIDE_DIR, CLIP_DIR, SEG_DIR, OUT_DIR):
        d.mkdir(parents=True, exist_ok=True)

    if args.preview or args.build:
        stage_map = {}
        for i in sorted(only):
            sc = SCENES[i]
            n_stages = max(1, len(sc["cards"]))
            pngs = []
            for k in range(1, n_stages + 1):
                p = SLIDE_DIR / f"s{i:03d}_{k:02d}.png"
                render_stage(sc, i + 1, n, sc["chapter"], k, p)
                pngs.append(p)
            stage_map[i] = pngs
        print(f"rendered slides for {len(stage_map)} scenes")
        if args.preview:
            return 0

    if args.check_clips or args.build:
        missing = [i for i in range(n) if not scene_clip(i).exists()]
        if missing:
            print(f"missing narration clips: {missing[:20]}{' ...' if len(missing) > 20 else ''} ({len(missing)} total)")
            if args.build:
                return 1
        if args.check_clips:
            total = 0.0
            for i in range(n):
                if scene_clip(i).exists():
                    total += probe_duration(scene_clip(i))
            print(f"clips present: {n - len(missing)}/{n}; narration total {total/60:.2f} min")
            return 0

    if args.build:
        seg_list = []
        total = 0.0
        for i in range(n):
            sc = SCENES[i]
            n_stages = max(1, len(sc["cards"]))
            pngs = [SLIDE_DIR / f"s{i:03d}_{k:02d}.png" for k in range(1, n_stages + 1)]
            if not all(p.exists() for p in pngs):
                for k in range(1, n_stages + 1):
                    render_stage(sc, i + 1, n, sc["chapter"], k, pngs[k - 1])
            dur = probe_duration(scene_clip(i))
            total += dur
            seg_list.append(build_scene_video(i, sc, n_stages, pngs, dur))
            print(f"scene {i:03d} {dur:6.2f}s  {sc['title'][:60]}", flush=True)
        lst = SEG_DIR / "concat.txt"
        lst.write_text("\n".join(f"file '{p.resolve()}'" for p in seg_list) + "\n")
        out = OUT_DIR / f"{OUT_STEM}.mp4"
        run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
             "-movflags", "+faststart", str(out)])
        print(f"built {out}  {total/60:.2f} min  {out.stat().st_size/1e6:.1f} MB")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
