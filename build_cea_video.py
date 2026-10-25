#!/usr/bin/env python3
"""
CEA & Hostel Subsidy — Master Explainer video compiler.

Pipeline (same method as the Batch 5 pension video):
  1. SCENES (below) hold every card, table, flowchart and Hinglish narration line.
  2. --preview  renders 1920x1080 PNG slides (one per reveal stage) into BUILD_DIR/slides
  3. narration clips are generated with the session voices (teacher = voice-00,
     student = voice-01) and saved as BUILD_DIR/clips/NNN.mp3 (NNN = scene index, 0-based)
  4. --build    assembles slides + clips into one H.264/AAC MP4 (BUILD_DIR/out/)
  5. --reference writes the English card reference sheet (markdown)
  6. --audit    checks every card fits its slide and prints density (no ffmpeg needed)

On-screen text is English only. Narration is Hinglish in Roman script (no Devanagari).
Unverified guide claims are tagged on screen as NOT VERIFIED; guide errors are tagged GUIDE FIX.

Usage:
  python3 build_cea_video.py --audit
  python3 build_cea_video.py --preview
  python3 build_cea_video.py --check-clips
  python3 build_cea_video.py --build
  python3 build_cea_video.py --reference
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
OUT_STEM = "cea_hostel_subsidy_masterclass"
BUILD_DIR = Path(os.environ.get("CEA_BUILD_DIR", "/home/user/cea_video/build"))
SLIDE_DIR = BUILD_DIR / "slides"
CLIP_DIR = BUILD_DIR / "clips"
SEG_DIR = BUILD_DIR / "segments"
OUT_DIR = BUILD_DIR / "out"
REFERENCE_MD = Path(__file__).with_name("cea_hostel_subsidy_reference_sheet.md")

TITLE_TOP = "Children Education Allowance (CEA) & Hostel Subsidy — Master Explainer"
FOOTER = "Source: DoPT O.M. 17.07.2018 · 25.04.2024 · Corrigendum 30.06.2026 · DoP FAQ O.M. 02.04.2026 · Rates as on 2026-10-25"

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
         "-tune", "stillimage", "-crf", "30",
         "-c:a", "aac", "-b:a", "96k", "-ar", "48000", "-ac", "2",
         "-t", f"{dur:.3f}", "-movflags", "+faststart", str(out)])
    return out


# ---------------------------------------------------------------- content
SCENES = []
SCENES += [
  {"chapter": "Start Here", "tag": "INTRO · MASTER GUIDE",
   "title": "CEA & Hostel Subsidy: complete explainer, rates as on 25 October 2026",
   "cards": [
     {"kind": "stat", "color": "cyan", "head": "CEA Rs 2,812.50", "sub": "per child per month, fixed"},
     {"kind": "stat", "color": "orange", "head": "Divyang Rs 5,625", "sub": "double rate, per child per month"},
     {"kind": "stat", "color": "green", "head": "Hostel Rs 8,437.50", "sub": "or actual boarding and lodging, whichever LOWER"},
     {"kind": "stat", "color": "purple", "head": "Child Care Rs 3,750", "sub": "women with disabilities; separate allowance"}],
   "narr": "Namaste dosto. Aaj hum Children Education Allowance, yaani CEA, aur Hostel Subsidy ko poori tarah samjhenge. Ye video Central Government ke employees ke liye hai. Har clause, har sub-rule, har proviso aur har exception ko hum ek-ek card me cover karenge. Aur jahan guide me galti thi, wahan hum use sudhaar kar denge.",
   "spk": "teacher"},
  {"chapter": "Start Here", "tag": "SOURCE CHAIN",
   "title": "Five official instruments decide every rule in this video",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Instruments in force, in date order",
      "headers": ["Instrument", "Date", "Issuer", "What it does"],
      "widths": [0.34, 0.14, 0.22, 0.30],
      "rows": [
        ["O.M. A-27012/02/2017-Estt.(AL)", "17.07.2018", "DoPT", "Consolidated CEA and Hostel Subsidy rules; base of all clauses"],
        ["O.M. A-27012/01/2023-Pers.Policy(Allowance)", "25.04.2024", "DoPT", "DA-linked 25% revision of rates"],
        ["O.M. on one-time NEP-2020 repeat relaxation", "14.03.2024", "DoPT", "Repeat-class relaxation, effective 2023-24"],
        ["Corrigendum O.M. A-27012/01/2023-Pers.Policy(AL)", "30.06.2026", "DoPT", "Hostel Subsidy: actual or ceiling, whichever lower"],
        ["O.M. PP-33/1/2022-PAP-DOP (consolidated FAQ)", "02.04.2026", "Dept of Posts, Ministry of Communications", "FAQ on NEP, dies non, suspension, retirement"]]}],
   "narr": "Pehle source samjhiye. Ye paanch instruments hain jo saare rules tay karte hain. Dhyan rahe, 02.04.2026 wala FAQ O.M. DoPT ka nahi, Department of Posts ka hai. Guide me ye galti thi. Video me ise sudhaar diya gaya hai, aur aage bhi har rule ka source dikhaya jayega.",
   "spk": "teacher"},
  {"chapter": "Start Here", "tag": "HOW TO READ THE TAGS",
   "title": "Every claim carries one of four status tags",
   "cards": [
     {"kind": "stat", "color": "green", "head": "VERIFIED", "sub": "Matched to O.M. text or a reliable reproduction"},
     {"kind": "stat", "color": "red", "head": "GUIDE FIX", "sub": "Error in the uploaded guide, corrected here"},
     {"kind": "stat", "color": "orange", "head": "NOT VERIFIED", "sub": "Guide claim not confirmed; check with DDO before use"},
     {"kind": "stat", "color": "cyan", "head": "ON-SCREEN", "sub": "English only. Narration is Hinglish, Roman script"}],
   "narr": "Video me char tags dikhenge. Verified matlab rule official O.M. ya bharosemand reproduction se mila. Guide fix matlab guide ki galti sudhari gayi. Not verified matlab claim abhi confirm nahi hua, isliye use karne se pehle apne DDO se check karein. Screen par text English me hai, aur narration Hinglish me hai.",
   "spk": "teacher"},
  {"chapter": "Start Here", "tag": "GUIDE FIX · PART 1",
   "title": "Five corrections to the uploaded master guide",
   "cards": [
     {"kind": "table", "color": "red", "title": "Guide errors and their correction",
      "headers": ["#", "Guide says", "Correct position", "Status"],
      "widths": [0.05, 0.35, 0.42, 0.18],
      "rows": [
        ["1", "FAQ O.M. PP-33/1/2022-PAP-DoP of 02.04.2026 is a DoPT order", "Issued by the Department of Posts (Ministry of Communications), not DoPT", "GUIDE FIX"],
        ["2", "2018 O.M. dated 16/17.07.2018", "Date is 17.07.2018", "GUIDE FIX"],
        ["3", "Hostel Subsidy lower-of test compares annual totals (Rs 95,000 vs Rs 1,01,250)", "Test is monthly: each month's actual boarding and lodging vs Rs 8,437.50", "GUIDE FIX"],
        ["4", "NEP-2020 repeat relaxation sourced to the FAQ alone", "Source is DoPT O.M. of 14.03.2024; effective from academic year 2023-24", "GUIDE FIX"],
        ["5", "Claim made once a year after the financial year", "O.M. year is the academic year (2018 O.M. text); guide mixes both", "NOT VERIFIED"]]}],
   "narr": "Ab guide ki galtiyan. Pehli: FAQ O.M. DoP ka hai, DoPT ka nahi. Doosri: 2018 O.M. ki date 17.07.2018 hai. Teesri, sabse important: Hostel Subsidy ka lower-of test har mahine ke hisaab se hota hai, saalana total se nahi. Chauthi: NEP repeat relaxation ka source DoPT O.M. 14.03.2024 hai. Paanchvi, claim cycle ka financial year wala statement verify nahi hua.",
   "spk": "teacher"},
  {"chapter": "Start Here", "tag": "NOT VERIFIED · PART 2",
   "title": "Five guide claims still unconfirmed: flagged, not hidden",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Unconfirmed guide claims and their treatment",
      "headers": ["#", "Guide claim", "Status", "How this video treats it"],
      "widths": [0.05, 0.42, 0.18, 0.35],
      "rows": [
        ["6", "Normal child: under 20 years or until Class XII, whichever is earlier", "NOT VERIFIED", "Shown with tag; check the age rule in the full O.M."],
        ["7", "Income-tax CEA exemption: Rs 100 per child per month (max 2); Rs 300 hostel", "NOT VERIFIED", "Amounts shown only as guide claims"],
        ["8", "Divyang O.M. dated 17.02.2023 (education at residence, double rate)", "NOT VERIFIED", "Rule kept with tag; O.M. text not seen"],
        ["9", "Anganwadi clarification citing DoPT O.M. dated 14.08.2024", "NOT VERIFIED", "Not treated as a rule; refer to departmental letter"],
        ["10", "Polytechnic/ITI diploma: first two years after Class X", "VERIFIED (core)", "Matches 2018 O.M. text; 'not already claimed' proviso NOT VERIFIED"]]}],
   "narr": "Kuch claims official text se confirm nahi hue. Normal child ki 20 saal ya Class XII wali age limit, income-tax wale Rs 100 aur Rs 300, Divyang O.M. 17.02.2023, aur Anganwadi wala letter. Ye sab screen par NOT VERIFIED tag ke saath hain. Polytechnic diploma ka core rule 2018 ke text se match karta hai, lekin already claimed nahi hona chahiye wali shart abhi confirm nahi hui.",
   "spk": "teacher"},
  {"chapter": "Rates & Escalator", "tag": "CURRENT RATES · 2026",
   "title": "Current rates after the 30.06.2026 corrigendum",
   "cards": [
     {"kind": "row", "color": "cyan", "label": "CEA (normal child)", "text": "Rs 2,812.50 per child per month, fixed. Paid irrespective of actual tuition or fee. A self-attested report card or fee receipt supports the claim."},
     {"kind": "row", "color": "orange", "label": "Divyang CEA", "text": "Rs 5,625 per child per month, double the normal rate. Upper age limit 22 years, no minimum age (NOT VERIFIED)."},
     {"kind": "row", "color": "green", "label": "Hostel Subsidy", "text": "Rs 8,437.50 per month OR actual boarding and lodging expenditure, whichever is LOWER. Applies from 30.06.2026. No longer a flat amount."},
     {"kind": "row", "color": "purple", "label": "Child-care allowance", "text": "Rs 3,750 per month for a woman Government employee with a disability, to care for her child. A separate scheme, not CEA."},
     {"kind": "callout", "color": "yellow", "text": "CLASSIC TRAP: CEA is fixed. Hostel Subsidy is no longer fixed. The corrigendum changed only the Hostel Subsidy."}],
   "narr": "Ab current rates. CEA Rs 2,812.50 per bachche per month, fixed hai. Divyang bachche ke liye Rs 5,625. Hostel Subsidy ab Rs 8,437.50 ya asli kharcha, jo bhi kam ho. Child care allowance ek alag scheme hai, jo divyang mahila karmchari ko milta hai. Yaad rakhiye, sirf CEA fixed hai, Hostel Subsidy nahi.",
   "spk": "teacher"},
  {"chapter": "Rates & Escalator", "tag": "RATE HISTORY",
   "title": "How the rates moved: 2017 base, 2024 revision, 2026 corrigendum",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Rate history (per month)",
      "headers": ["Effective from", "CEA per child", "Divyang CEA", "Hostel Subsidy"],
      "widths": [0.40, 0.18, 0.18, 0.24],
      "rows": [
        ["7th CPC base, O.M. 16.08.2017 (superseded)", "Rs 2,250", "Rs 4,500", "Rs 6,750 fixed"],
        ["O.M. 25.04.2024 (DA over 50%, from 01.01.2024)", "Rs 2,812.50", "Rs 5,625", "Rs 8,437.50 fixed"],
        ["Corrigendum O.M. 30.06.2026 (current)", "Rs 2,812.50", "Rs 5,625", "Rs 8,437.50 or actual, whichever LOWER"]]},
     {"kind": "row", "color": "green", "label": "Check", "text": "The 2024 revision raised every rate by exactly 25%. The 2026 corrigendum left CEA and Divyang CEA unchanged."}],
   "narr": "Rate history dekhiye. 2017 me CEA Rs 2,250 tha, Divyang Rs 4,500, aur hostel Rs 6,750. 2024 me DA 50 percent cross hua, toh rates 25 percent badhe. 2026 ke corrigendum me CEA aur Divyang rate same rahe, lekin Hostel Subsidy me asli kharcha wala rule aaya.",
   "spk": "teacher"},
  {"chapter": "Rates & Escalator", "tag": "CLAUSE 5 · AUTOMATIC ESCALATOR",
   "title": "The 25% escalator works every time DA crosses a 50% multiple",
   "cards": [
     {"kind": "steps", "color": "cyan", "steps": [
        "Base: O.M. 16.08.2017. CEA Rs 2,250",
        "DA over 50% (01.01.2024): CEA Rs 2,812.50 (+25%)",
        "DA over 100%: next +25% step on the same rule",
        "Each later 50% multiple: +25% again"]},
     {"kind": "row", "color": "sky", "label": "Rule text", "text": "Limits are raised by 25% every time DA on the revised pay goes up by 50%. The rule is automatic; each step is confirmed by a DoPT O.M."}],
   "narr": "Ye escalator samajhiye. Har baar DA 50 percent ka multiple cross karega, toh CEA aur Hostel Subsidy ki limits khud 25 percent badh jaati hain. Pehla trigger 01.01.2024 tha. Agla trigger DA 100 percent par hoga. Har step ko DoPT ka O.M. confirm karta hai.",
   "spk": "teacher"},
  {"chapter": "Rates & Escalator", "tag": "DIVYANG vs NORMAL",
   "title": "Divyang child versus normal child: side by side",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Feature comparison",
      "headers": ["Feature", "Normal child", "Divyang child"],
      "widths": [0.24, 0.38, 0.38],
      "rows": [
        ["CEA rate", "Rs 2,812.50 per month (fixed)", "Rs 5,625 per month (double)"],
        ["Upper age limit", "20 years or Class XII, whichever earlier (NOT VERIFIED)", "22 years, no minimum age (NOT VERIFIED)"],
        ["Institution", "Must be recognised by Govt or a competent authority", "Aided or approved; recognition not mandatory (NOT VERIFIED)"],
        ["Education at residence", "Not applicable", "Allowed if child cannot attend school; tutor receipt and self-certification (NOT VERIFIED)"]]}],
   "narr": "Divyang aur normal bachche ka farq dekhiye. Rate double hai. Age limit guide me 22 saal likhi hai, aur ghar par padhai ka rule bhi. Ye sab guide ne 17.02.2023 ke O.M. se liya hai, jo abhi verify nahi hua. Isliye screen par NOT VERIFIED tag hai. Normal child ki age limit par bhi same tag lagaya gaya hai.",
   "spk": "teacher"},
  {"chapter": "Rates & Escalator", "tag": "STUDENT QUESTION",
   "title": "Student question: is child-care allowance the same as Divyang CEA?",
   "cards": [
     {"kind": "row", "color": "sky", "label": "Student asks", "text": "Sir, Divyang bachche ka CEA aur women with disabilities ka child-care allowance, kya dono ek hi cheez hain?"}],
   "narr": "Sir, Divyang bachche ka CEA aur women with disabilities ke liye child care allowance, kya dono ek hi cheez hain? Ya inme se koi ek hi mil sakta hai?",
   "spk": "student"},
]
SCENES += [
  {"chapter": "Legal Framework", "tag": "CLAUSE 1 · WHO IS COVERED",
   "title": "Who is covered: all Central Government servants, without any pay limit",
   "cards": [
     {"kind": "stat", "color": "cyan", "head": "All Central servants", "sub": "No pay limit applies"},
     {"kind": "stat", "color": "green", "head": "State staff on deputation IN", "sub": "Covered by Central CEA rules from day one"},
     {"kind": "stat", "color": "orange", "head": "Industrial employees", "sub": "Central Government industrial employees"},
     {"kind": "stat", "color": "purple", "head": "Defence Estimates civilians", "sub": "Civilians paid out of Defence Estimates"},
     {"kind": "row", "color": "sky", "label": "Note", "text": "CAPF and Defence forces may run on separate circulars that mirror this scheme. Check them alongside this guide (NOT VERIFIED)."}],
   "narr": "Ab Clause 1 ka coverage dekhiye. CEA sabhi Central Government servants ke liye hai, chahe pay kitni bhi ho. Isme State Government ke wo officer bhi aate hain jo Centre par deputation par hain. Industrial employees aur Defence Estimates se paid civilian staff bhi covered hain. CAPF aur Defence forces ke liye alag circular ho sakta hai, jise bhi check karna zaroori hai.",
   "spk": "teacher"},
  {"chapter": "Legal Framework", "tag": "CLAUSE 2 · DEPUTATION APPLICABILITY",
   "title": "Clause 2: deputation and foreign service need express provision to carry CEA",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Direction of movement and CEA position",
      "headers": ["Movement", "CEA position", "Who pays"],
      "widths": [0.36, 0.40, 0.24],
      "rows": [
        ["State Govt officer deputed INTO Centre", "Automatic: Central CEA rules from day one", "Central borrowing office"],
        ["Centre officer deputed OUT to State, autonomous body, PSU or local body", "Only if the deputation order expressly provides for drawal of CEA", "Borrowing body, as the order provides"],
        ["Centre officer on foreign service", "Only if the foreign-service terms expressly provide", "As the foreign-service terms provide"],
        ["Centre officer deputed to a PSU with its own scheme", "Employee elects one scheme, not both", "Paying authority of the elected scheme"]]},
     {"kind": "callout", "color": "yellow", "text": "TEST: Is express provision in the deputation or foreign-service terms? If silent, CEA is not admissible from the borrowing body."},
     {"kind": "row", "color": "orange", "label": "Status", "text": "Clause 2 wording and the PSU-scheme election rule come from the guide. Confirm against the full 2018 O.M. text (NOT VERIFIED)."}],
   "narr": "Ab Clause 2, jo deputation aur foreign service ka sabse important rule hai. State se Centre me deputation par aaye officer ko CEA automatic milta hai. Lekin Centre se bahar, yaani State, PSU, autonomous body ya foreign service me jaane par CEA tabhi milega jab deputation ki chitthi me saaf likha ho. Ye clause guide ke text se hai, aur full O.M. se confirm karna zaroori hai.",
   "spk": "teacher"},
  {"chapter": "Legal Framework", "tag": "STUDENT QUESTION",
   "title": "Student question: does a State officer on deputation to the Centre need a separate permission?",
   "cards": [
     {"kind": "row", "color": "sky", "label": "Student asks", "text": "If a State Government officer comes to the Centre on deputation, must he apply separately or get a permission for CEA?"}],
   "narr": "Sir, agar koi State Government ka officer Centre me deputation par aata hai, to kya usko CEA ke liye alag se application ya permission deni padti hai?",
   "spk": "student"},
  {"chapter": "Eligible Children", "tag": "CLAUSE 3 · TWO-ELDEST-SURVIVING RULE",
   "title": "Clause 3: only the two eldest surviving children are covered",
   "cards": [
     {"kind": "row", "color": "cyan", "label": "Rule", "text": "CEA and Hostel Subsidy can be claimed only for the two eldest surviving children of the Government servant. Survivors count, not all births."},
     {"kind": "table", "color": "green", "title": "Worked families",
      "headers": ["Family", "Children history", "Who is covered", "Reason"],
      "widths": [0.10, 0.34, 0.24, 0.32],
      "rows": [
        ["A", "3 born; eldest died in infancy; 2 survive", "Both survivors", "Counts survivors, not birth order of all births"],
        ["B", "1 child, then twins at the second delivery", "All three children", "Twins exception at the second delivery"],
        ["C", "2 children; sterilisation fails; 3rd child born", "3rd child covered too", "Failed-sterilisation exception"],
        ["D", "3 children from 3 normal deliveries", "Only the two eldest", "3rd child gets no CEA"]]}],
   "narr": "Ab Clause 3, sabse bada cap. CEA aur Hostel Subsidy sirf do sabse bade zinda bachchon ke liye hain. Family A me ek bachcha chala gaya, to do survivors covered hain. Family B me doosri delivery me twins hain, to sab cover honge. Family D me teen normal deliveries hain, to teesre bachche ka CEA nahi milega.",
   "spk": "teacher"},
  {"chapter": "Eligible Children", "tag": "CLAUSE 3 · PROVISOS AND EXCEPTIONS",
   "title": "The two exceptions: twins at the second delivery and failed sterilisation",
   "cards": [
     {"kind": "row", "color": "green", "label": "Twins or multiple birth", "text": "Applies only at the second child birth. All children from that birth are covered even if the total exceeds two."},
     {"kind": "row", "color": "orange", "label": "Failed sterilisation", "text": "Children born out of the first instance of such failure are also covered."},
     {"kind": "row", "color": "red", "label": "Not an exception", "text": "A third child from an ordinary pregnancy gets no CEA. Only the two listed exceptions extend the cap."},
     {"kind": "callout", "color": "yellow", "text": "EXAM TRAP: twins at the FIRST delivery are not an exception. The twins exception works only at the second delivery."}],
   "narr": "Do exceptions hain. Pehla, doosri delivery me twins ya multiple birth. Tab saare bachche cover honge. Dusra, sterilisation operation fail hone par jo bachche pehli failure se paida honge, wo cover honge. Exam trap ye hai ki twins sirf doosri delivery par exception hain, pehli par nahi.",
   "spk": "teacher"},
  {"chapter": "Eligible Children", "tag": "CLAUSE 4 · DIVYANG CHILDREN",
   "title": "Clause 4: Divyang children get double rate and wider limits",
   "cards": [
     {"kind": "stat", "color": "orange", "head": "Double rate", "sub": "Rs 5,625 per month"},
     {"kind": "stat", "color": "cyan", "head": "Age up to 22", "sub": "Upper limit (NOT VERIFIED)"},
     {"kind": "stat", "color": "green", "head": "No minimum age", "sub": "Per guide (NOT VERIFIED)"},
     {"kind": "stat", "color": "purple", "head": "Education at residence", "sub": "If the child cannot attend school"},
     {"kind": "row", "color": "sky", "label": "Proof", "text": "Payment receipt from the special educator or tutor, plus self-certification by the Government servant. Source: DoPT O.M. 17.02.2023 as cited in the guide (NOT VERIFIED)."}],
   "narr": "Clause 4, Divyang bachche. Rate double hai, Rs 5,625. Upper age limit 22 saal aur koi minimum age nahi. Agar bachcha school nahi ja sakta, to ghar par education ka kharcha bhi mil sakta hai, tutor ki receipt aur self-certification ke saath. Ye sab guide ke 17.02.2023 O.M. par based hai, isliye NOT VERIFIED hai.",
   "spk": "teacher"},
  {"chapter": "Eligible Children", "tag": "ELIGIBILITY FLOW",
   "title": "Is this child eligible? Five checks in order",
   "cards": [
     {"kind": "steps", "color": "green", "steps": [
        "1. Child of a Government servant",
        "2. One of the two eldest surviving? If not, check twins or sterilisation exception",
        "3. Nursery to XII in a recognised school? If not, check Divyang at-residence rule",
        "4. Divyang? Double rate, age limit 22",
        "5. Eligible for CEA at the applicable rate"]},
     {"kind": "row", "color": "sky", "label": "Note", "text": "Flow follows the master guide. The age limit and at-residence steps are NOT VERIFIED."}],
   "narr": "Ab ek flowchart se samjhiye. Pehle dekhiye bachcha Govt servant ka hai ya nahi. Phir dekhiye wo do sabse bade zinda bachchon me hai. Phir school ya Divyang rule dekhiye. Last me rate Divyang ya normal ke hisaab se tay hoga.",
   "spk": "teacher"},
  {"chapter": "Classes & Institutions", "tag": "CLAUSE 6 · CLASS RANGE",
   "title": "Eligible classes: Nursery to Class XII, plus the one-time NEP-2020 relaxation",
   "cards": [
     {"kind": "stat", "color": "cyan", "head": "Nursery to Class XII", "sub": "Includes XI and XII in junior colleges or affiliated schools"},
     {"kind": "stat", "color": "green", "head": "NEP relaxation", "sub": "One time only, for a repeated class"},
     {"kind": "stat", "color": "orange", "head": "Three pre-primary classes", "sub": "Before Class I, per the 2026 FAQ"},
     {"kind": "stat", "color": "purple", "head": "From 2023-24", "sub": "Relaxation applies from this academic year"},
     {"kind": "row", "color": "sky", "label": "Source", "text": "Class range: 2018 consolidated instructions. NEP relaxation: DoPT O.M. dated 14.03.2024, restated in the DoP FAQ O.M. dated 02.04.2026."}],
   "narr": "Ab classes. CEA Nursery se Class XII tak hai, jisme Class XI aur XII junior colleges ya affiliated schools me bhi aate hain. NEP-2020 ke liye ek baar ki relaxation hai. Agar bachcha NEP ki wajah se koi pre-primary class dobara padhta hai, to wo reimburse hoga. Ye relaxation 2023-24 se lagu hai, aur source DoPT O.M. 14.03.2024 hai.",
   "spk": "teacher"},
  {"chapter": "Classes & Institutions", "tag": "NEP-2020 WORKED EXAMPLE",
   "title": "NEP-2020 repeat year: claimable once, never twice",
   "cards": [
     {"kind": "table", "color": "green", "title": "Worked example: Nursery child, school shifts to NEP-2020 pre-primary",
      "headers": ["Academic year", "Class", "CEA status", "Why"],
      "widths": [0.18, 0.28, 0.28, 0.26],
      "rows": [
        ["2022-23", "Nursery", "Claimable normally", "Normal class before the relaxation year"],
        ["2023-24", "Pre-primary repeat before Class I", "Reimbursed once under the relaxation", "Repeated solely due to NEP-2020 transition"],
        ["2023-24", "Class I onward", "Normal rules", "Regular class"]]},
     {"kind": "callout", "color": "yellow", "text": "ONE-TIME ONLY: the NEP relaxation is available once per child. It cannot be used a second time for the same child."}],
   "narr": "NEP ka worked example dekhiye. Nursery 2022-23 me normal claim hai. Phir 2023-24 me NEP ki wajah se pre-primary year dobara padha, to wo ek baar reimburse hoga. Lekin ye relaxation dobara nahi milega, same child ke liye. Ye FAQ ke Q1 aur Q2 par based hai.",
   "spk": "teacher"},
  {"chapter": "Classes & Institutions", "tag": "CLAUSE 6 · RECOGNITION",
   "title": "Recognition: normal children need a recognised school; Divyang rule is relaxed",
   "cards": [
     {"kind": "row", "color": "cyan", "label": "Normal child", "text": "School must be recognised by the Central or State Government, a UT administration, or a competent authority, including a university-affiliated board. Guide position; confirm in the full O.M."},
     {"kind": "row", "color": "orange", "label": "Divyang child", "text": "Aided or approved school, or fee approved by Government or UT, is enough; formal recognition is not required (NOT VERIFIED)."},
     {"kind": "callout", "color": "yellow", "text": "CHECK BEFORE CLAIM: keep the school recognition or approval document ready for the DDO."}],
   "narr": "Recognition ka rule. Normal bachche ka school recognised hona chahiye, Central ya State Government, UT administration, ya competent authority se. Divyang bachchon ke liye ye shart dheeli hai. Aided ya approved school chalega. Ye sab guide ka position hai, aur full O.M. se confirm karna hai.",
   "spk": "teacher"},
]
SCENES += [
  {"chapter": "Hostel Subsidy", "tag": "CLAUSE 7 · RATE AND ELIGIBILITY",
   "title": "Hostel Subsidy: Rs 8,437.50 per month ceiling, or actual cost if lower",
   "cards": [
     {"kind": "stat", "color": "cyan", "head": "Rs 8,437.50 per month", "sub": "Ceiling, applies from 30.06.2026 with the lower-of rule"},
     {"kind": "stat", "color": "green", "head": "Actual boarding and lodging", "sub": "Pay the lower of this and the ceiling"},
     {"kind": "stat", "color": "orange", "head": "Residential school", "sub": "Child in a hostel away from the posted station"},
     {"kind": "stat", "color": "purple", "head": "Head of Institution", "sub": "Certificate of boarder status and expenditure"},
     {"kind": "row", "color": "sky", "label": "Source", "text": "Rate and lower-of wording: corrigendum O.M. dated 30.06.2026, which modifies Para 2(a) of the O.M. dated 25.04.2024."}],
   "narr": "Ab Hostel Subsidy. Ye tab milta hai jab bachcha residential school ke hostel me rehta hai, aur us jagah se door jahan aap posted hain. Rate Rs 8,437.50 per month hai, lekin ab ye ceiling hai. Asli boarding aur lodging ka kharcha agar kam hai, to wahi milega. Institution ka certificate zaroori hai.",
   "spk": "teacher"},
  {"chapter": "Hostel Subsidy", "tag": "BEFORE vs AFTER 30.06.2026",
   "title": "Before and after the corrigendum: the Hostel Subsidy is no longer flat",
   "cards": [
     {"kind": "table", "color": "green", "title": "Hostel Subsidy: two regimes compared",
      "headers": ["Feature", "O.M. 25.04.2024 (till 30.06.2026)", "Corrigendum 30.06.2026 onward"],
      "widths": [0.22, 0.39, 0.39],
      "rows": [
        ["Amount", "Flat Rs 8,437.50 per month, irrespective of actual spend", "Rs 8,437.50 per month OR actual, whichever is LOWER"],
        ["Proof required", "Institution certificate of boarder status", "Receipt quantifying actual boarding and lodging, plus certificate"],
        ["Practical effect", "Cheaper hostels still receive the full ceiling", "Cheaper hostels are reimbursed only the actual, lower amount"]]},
     {"kind": "callout", "color": "yellow", "text": "EXAM TRAP: 'Hostel Subsidy is fixed like CEA' is no longer true. Only CEA stays fixed."}],
   "narr": "Before aur after dekhiye. 25.04.2024 se 30.06.2026 tak Hostel Subsidy flat tha, chahe kharcha kitna bhi ho. Ab corrigendum ke baad lower-of rule laga hai. Proof bhi badla hai, ab asli receipt chahiye jo kharche ko quantify kare. Exam me ye sabse zyada poocha jaata hai.",
   "spk": "teacher"},
  {"chapter": "Hostel Subsidy", "tag": "GUIDE FIX · MONTHLY TEST",
   "title": "The lower-of test runs month by month, not on annual totals",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Worked example: four months at one hostel (ceiling Rs 8,437.50)",
      "headers": ["Month", "Actual boarding and lodging", "Hostel Subsidy payable (lower of)", "Old flat rule"],
      "widths": [0.16, 0.28, 0.32, 0.24],
      "rows": [
        ["April", "Rs 7,000", "Rs 7,000", "Rs 8,437.50"],
        ["May", "Rs 9,500", "Rs 8,437.50", "Rs 8,437.50"],
        ["June", "Rs 8,437.50", "Rs 8,437.50", "Rs 8,437.50"],
        ["July", "Rs 5,200", "Rs 5,200", "Rs 8,437.50"],
        ["Total", "Rs 30,137.50", "Rs 29,075", "Rs 33,750"]]},
     {"kind": "row", "color": "red", "label": "Guide fix", "text": "The guide compared annual totals (Rs 95,000 against Rs 1,01,250). The O.M. sets the rate per month, so the test is applied to each month."}],
   "narr": "Guide ki ek galti yahan sudhari gayi hai. Guide ne saalana total ka comparison kiya tha. Lekin O.M. me rate per month likha hai, isliye test har mahine ka hota hai. Example me April me Rs 7,000 kharcha hai, to Rs 7,000 milega. May me Rs 9,500 hai, to ceiling Rs 8,437.50 milega.",
   "spk": "teacher"},
  {"chapter": "Hostel Subsidy", "tag": "CLAUSE 8 · CONCURRENCY WITH CEA",
   "title": "CEA and Hostel Subsidy can run together for the same child",
   "cards": [
     {"kind": "steps", "color": "green", "steps": [
        "CEA: flat Rs 2,812.50 per month, two-eldest rule applies",
        "Hostel: each month, lower of actual bill and Rs 8,437.50",
        "Claim both for the same child, if each test is met",
        "CEA for 12 months: Rs 2,812.50 x 12 = Rs 33,750 a year"]},
     {"kind": "row", "color": "orange", "label": "NOT VERIFIED", "text": "Clause 8 (concurrency) is from the guide and search reports. Older sources treated the two as exclusive. Confirm in the full O.M. before a claim."}],
   "narr": "Ab CEA aur Hostel Subsidy ka saath. Guide ke Clause 8 ke hisaab se dono ek hi child ke liye saath claim ho sakte hain, agar dono ki shartein poori hon. CEA flat hai, Rs 2,812.50 ko 12 se guna karke Rs 33,750 saal. Hostel Subsidy monthly lower-of se nikalta hai. Ye concurrency NOT VERIFIED hai, isliye full O.M. se confirm karein.",
   "spk": "teacher"},
  {"chapter": "Hostel Subsidy", "tag": "ELIGIBILITY AND PROOF",
   "title": "Hostel Subsidy conditions: what must be true, and what must be produced",
   "cards": [
     {"kind": "table", "color": "cyan", "title": "Conditions and documents",
      "headers": ["Condition", "Requirement", "Status"],
      "widths": [0.24, 0.50, 0.26],
      "rows": [
        ["Residence", "Child stays in the hostel of a residential school, away from the posted or residing station", "VERIFIED (Clause 7)"],
        ["Distance test", "A '50 km' test appears in the guide's Batch 5 heading only", "NOT VERIFIED"],
        ["Institution certificate", "Head of Institution certifies boarder status and the expenditure", "VERIFIED (Clause 7)"],
        ["Original receipt", "Original fee receipt or e-receipt quantifying boarding and lodging", "Consistent with corrigendum"]]}],
   "narr": "Eligibility aur proof. Bachcha residential school ke hostel me hona chahiye. Guide me 50 kilometre ka test likha hai, jo Clause 7 ke text me nahi hai, isliye ise NOT VERIFIED maana gaya hai. Proof ke liye original fee receipt ya e-receipt, aur Head of Institution ka certificate chahiye jo boarder status aur kharcha dono bataye.",
   "spk": "teacher"},
  {"chapter": "Hostel Subsidy", "tag": "HOSTEL SUBSIDY FLOW",
   "title": "Hostel Subsidy in five steps, with CEA alongside",
   "cards": [
     {"kind": "steps", "color": "green", "steps": [
        "1. Child in a residential-school hostel, away from station?",
        "2. Is the monthly bill below Rs 8,437.50?",
        "3. Yes: Hostel Subsidy = actual bill for that month",
        "4. No: Hostel Subsidy = Rs 8,437.50 ceiling",
        "5. CEA claimed alongside, if its conditions are met"]},
     {"kind": "row", "color": "sky", "label": "Note", "text": "Follows the master guide Batch 5 and the corrigendum. Step 5 depends on the NOT VERIFIED concurrency point."}],
   "narr": "Ek flowchart se pura Hostel Subsidy samjhiye. Pehle dekhiye hostel me rehta hai ya nahi. Phir monthly bill dekhiye. Bill ceiling se kam hai to asli bill milega. Zyada hai to Rs 8,437.50 milega. Aur CEA ke saath dono claim ho sakte hain, agar shartein poori hon.",
   "spk": "teacher"},
  {"chapter": "Procedure & Proof", "tag": "CLAUSE 9 · CLAIM CYCLE",
   "title": "Claim cycle: once a year, after the year closes",
   "cards": [
     {"kind": "stat", "color": "cyan", "head": "Once a year", "sub": "Reimbursement after the year closes (guide Clause 9)"},
     {"kind": "stat", "color": "green", "head": "CEA proof", "sub": "Self-attested report card or self-attested fee receipt"},
     {"kind": "stat", "color": "orange", "head": "Hostel proof", "sub": "Original fee receipt or e-receipt"},
     {"kind": "stat", "color": "purple", "head": "Year is academic", "sub": "2018 O.M. text as reproduced; guide's financial year NOT VERIFIED"}],
   "narr": "Clause 9, claim cycle. Guide ke hisaab se claim saal me ek baar hota hai, saal khatam hone ke baad. Guide ne ise financial year likha hai. Lekin 2018 O.M. ka text year ko academic year batata hai, aur ye point full O.M. se confirm karna baaki hai. CEA ke liye self-attested report card ya fee receipt chalta hai.",
   "spk": "teacher"},
  {"chapter": "Procedure & Proof", "tag": "PROOF MATRIX",
   "title": "Which document supports which claim",
   "cards": [
     {"kind": "table", "color": "green", "title": "Documents by claim type",
      "headers": ["Claim", "Documents needed", "Source status"],
      "widths": [0.28, 0.50, 0.22],
      "rows": [
        ["CEA, normal child", "Self-attested report card OR self-attested fee receipt", "Guide Clause 9"],
        ["CEA, Divyang child at residence", "Payment receipt from special educator or tutor, plus self-certification", "NOT VERIFIED (O.M. 17.02.2023)"],
        ["Hostel Subsidy", "Original fee or e-receipt quantifying boarding and lodging, plus Head of Institution certificate", "Corrigendum 30.06.2026"],
        ["Both-spouse declaration", "Written declaration that the spouse has not and will not claim for the same period", "Guide Clause 13"]]}],
   "narr": "Proof ka matrix dekhiye. CEA normal ke liye self-attested report card ya fee receipt. Divyang bachche ke at-residence case me tutor ki receipt aur self-certification. Hostel Subsidy ke liye original receipt aur institution certificate. Aur dono Government servants ho to spouse ka declaration zaroori hai.",
   "spk": "teacher"},
  {"chapter": "Procedure & Proof", "tag": "DECLARATIONS",
   "title": "Self-certification and the spouse declaration: keep both on file",
   "cards": [
     {"kind": "row", "color": "cyan", "label": "Self-certification", "text": "Annual claim form: the Government servant declares the child's enrolment, class, and that the conditions are met. Often a substitute for third-party proof."},
     {"kind": "row", "color": "orange", "label": "Spouse declaration", "text": "If both spouses are Government servants, the other spouse's written declaration that CEA is not, and will not be, claimed for the same period (guide Clause 13)."},
     {"kind": "callout", "color": "yellow", "text": "KEEP ON FILE: the single-claim rule depends on the declaration. Store it with the annual claim."}],
   "narr": "Declarations ki baat karte hain. Annual claim form me self-certification dena hota hai ki bachche ka enrolment, class aur shartein poori hain. Agar dono spouse Government servants hain, to doosre spouse ka declaration zaroori hai ki wo same period ke liye CEA nahi le raha. Declaration file me rakhiye, ye single-claim rule ka base hai.",
   "spk": "teacher"},
  {"chapter": "Procedure & Proof", "tag": "STUDENT QUESTION",
   "title": "Student question: does CEA need a fee receipt, and does Hostel Subsidy follow the same rule?",
   "cards": [
     {"kind": "row", "color": "sky", "label": "Student asks", "text": "Does CEA need a fee receipt? Does Hostel Subsidy follow the same rule?"},
     {"kind": "row", "color": "green", "label": "Short answer", "text": "CEA: no fee receipt is needed; a self-attested report card or fee receipt is enough. Hostel Subsidy: an original receipt quantifying the actual bill is needed from 30.06.2026."}],
   "narr": "Sir, CEA ke liye fee receipt chahiye ya nahi? Aur Hostel Subsidy ke liye bhi wahi rule hai kya?",
   "spk": "student"},
]
SCENES += [
  {"chapter": "Service Status", "tag": "CLAUSE 10 · ADMISSIBILITY",
   "title": "On duty, leave, and suspension keep CEA alive; dies non stops it",
   "cards": [
     {"kind": "table", "color": "green", "title": "Admissibility by service status",
      "headers": ["Situation", "CEA and Hostel Subsidy", "Source status"],
      "widths": [0.40, 0.30, 0.30],
      "rows": [
        ["On duty", "Admissible", "VERIFIED (2018 O.M.)"],
        ["On leave, including extraordinary leave (EOL)", "Admissible", "VERIFIED (2018 O.M.)"],
        ["Under suspension", "Admissible", "VERIFIED (2018 O.M.)"],
        ["Dies non period", "NOT admissible", "VERIFIED (2018 O.M.)"],
        ["Child fails a class", "Continues unaffected", "Per guide Clause 10"]]}],
   "narr": "Clause 10 ka admissibility rule. CEA aur Hostel Subsidy milte hain jab employee on duty ho, suspension me ho, ya leave par ho, jisme extraordinary leave bhi shamil hai. Dies non period me ye nahi milta. Aur bachcha agar ek class me fail ho jaye, to bhi CEA nahi rukta. Ye table ka saar hai.",
   "spk": "teacher"},
  {"chapter": "Service Status", "tag": "DIES NON",
   "title": "Dies non: the period that does not count for CEA",
   "cards": [
     {"kind": "row", "color": "red", "label": "What it is", "text": "A period treated as if the employee was not in service, usually imposed as a penalty for unauthorised absence (guide glossary)."},
     {"kind": "row", "color": "orange", "label": "Effect on CEA", "text": "No CEA and no Hostel Subsidy for the dies non period. Reimbursement resumes once the period ends."},
     {"kind": "row", "color": "sky", "label": "Failed class", "text": "Failure in a class does not stop CEA (guide Clause 10). Confirm this in the full 2018 O.M. text before relying on it."}],
   "narr": "Dies non ko samjhiye. Ye ek aisa period hai jo service law me naukri ka hissa nahi maana jata, aam taur par unauthorised absence ki penalty ke roop me. Is period ka CEA nahi milta. Dies non khatam hone ke baad CEA phir se chalu hota hai. Fail hone wala point guide ke Clause 10 se hai, aur full O.M. se ek baar aur confirm karna chahiye.",
   "spk": "teacher"},
  {"chapter": "Service Status", "tag": "FAQ Q3 TO Q5",
   "title": "FAQ questions on suspension, leave, restored service and dies non",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Consolidated FAQ O.M. dated 02.04.2026 (Department of Posts)",
      "headers": ["FAQ", "Question", "Answer", "Status"],
      "widths": [0.10, 0.36, 0.34, 0.20],
      "rows": [
        ["Q3", "Period first treated as a break, later restored by court order", "Admissibility follows the final classification: on duty, suspension or leave means payable", "NOT VERIFIED"],
        ["Q4", "CEA during suspension or leave, including EOL?", "Yes, admissible under suspension and leave", "VERIFIED (FAQ and 2018 O.M.)"],
        ["Q5", "CEA for a dies non period?", "No, not admissible", "VERIFIED (FAQ and 2018 O.M.)"]]}],
   "narr": "FAQ ke Q3 se Q5 tak. Department of Posts ka consolidated FAQ O.M., 02.04.2026, batata hai ki suspension aur leave par CEA admissible hai, aur dies non me nahi. Q3 me court order se restored service ka sawal hai. Ye guide me hai, lekin FAQ ka direct text confirm nahi hua, isliye NOT VERIFIED tag hai.",
   "spk": "teacher"},
  {"chapter": "Service Status", "tag": "STUDENT QUESTION",
   "title": "Student question: suspension later ruled as on duty, what happens to CEA?",
   "cards": [
     {"kind": "row", "color": "sky", "label": "Student asks", "text": "If a suspension is later ended by a court order and the period is treated as on duty, what happens to CEA for that period?"},
     {"kind": "row", "color": "green", "label": "Short answer", "text": "The period follows its final classification. If treated as on duty, suspension or leave, CEA is payable for it (guide, FAQ Q3; NOT VERIFIED)."}],
   "narr": "Sir, agar kisi employee ka suspension baad me court order se khatam ho jaye, aur us period ko on duty maan liya jaye, to CEA ka kya hoga?",
   "spk": "student"},
  {"chapter": "Cessation & Death", "tag": "CLAUSE 11 · CESSATION OF SERVICE",
   "title": "Retirement, resignation, dismissal or removal: CEA runs to the academic year-end",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Event and CEA position",
      "headers": ["Event", "CEA position", "Who pays"],
      "widths": [0.34, 0.36, 0.30],
      "rows": [
        ["Retirement", "Admissible to end of that academic year", "Last employing office"],
        ["Resignation", "Admissible to end of that academic year", "Last employing office"],
        ["Discharge, dismissal or removal", "Admissible to end of that academic year", "Last employing office"]]},
     {"kind": "callout", "color": "yellow", "text": "EXAM TRAP: dismissal and removal do not stop CEA on the spot. The academic-year rule applies to all four events."}],
   "narr": "Clause 11 ka rule. Agar employee retirement, resignation, discharge, dismissal ya removal se service se bahar jata hai, to CEA us academic year ke end tak chalta hai jisme event hua. Payment wahi office karega jahan wo pehle kaam karta tha. Ye rule dismissal aur removal par bhi lagu hota hai, ye exam ka important point hai.",
   "spk": "teacher"},
  {"chapter": "Cessation & Death", "tag": "WORKED EXAMPLE",
   "title": "Resignation on 10 November: CEA until the academic year ends",
   "cards": [
     {"kind": "steps", "color": "orange", "steps": [
        "Employee resigns on 10 November, mid academic year",
        "CEA runs to 31 March (guide assumes April to March)",
        "Paid by the last employing office",
        "No CEA in the next academic year: service has ended"]},
     {"kind": "row", "color": "sky", "label": "Note", "text": "Year-end date follows the guide's April to March example. Confirm the academic-year definition in the full O.M. (see Clause 9 NOT VERIFIED)."}],
   "narr": "Example dekhiye. Employee 10 November ko resign karta hai. CEA March tak chalega, kyunki guide academic year April se March maanta hai. Payment last office karega. Agle academic year ka CEA nahi milega, kyunki service khatam ho chuki hai.",
   "spk": "teacher"},
  {"chapter": "Cessation & Death", "tag": "CLAUSE 12 · DEATH IN SERVICE",
   "title": "Death in service: CEA for the children continues, subject to the spouse test",
   "cards": [
     {"kind": "stat", "color": "cyan", "head": "Death in service", "sub": "Children's CEA and Hostel Subsidy admissible, other conditions met"},
     {"kind": "stat", "color": "orange", "head": "Spouse test", "sub": "Applies to the surviving spouse's employment"},
     {"kind": "stat", "color": "red", "head": "Excluded employers", "sub": "Central or State Govt, autonomous body, PSU, semi-Govt or Govt-funded body"},
     {"kind": "row", "color": "green", "label": "Source status", "text": "VERIFIED against the 2018 O.M. death-in-service clause as reproduced in the sources checked."}],
   "narr": "Clause 12, death in service. Agar Government servant service ke dauran guzar jaye, to bachchon ka CEA chalu rehta hai. Shart ye hai ki surviving spouse Central Government, State Government, autonomous body, PSU ya semi-Government body, jaise municipality ya port trust, me employed na ho. Ye 2018 O.M. ke death clause se verified hai.",
   "spk": "teacher"},
  {"chapter": "Cessation & Death", "tag": "SURVIVING SPOUSE TEST",
   "title": "The surviving spouse's employment decides whether CEA continues",
   "cards": [
     {"kind": "table", "color": "purple", "title": "Surviving spouse's status and CEA for the children",
      "headers": ["Surviving spouse's status", "CEA for children", "Note"],
      "widths": [0.40, 0.28, 0.32],
      "rows": [
        ["Not employed (homemaker)", "Continues", "No exclusion applies"],
        ["Employed in private, unfunded organisation", "Continues", "Test is specific to Govt-linked employment"],
        ["Employed in Central or State Govt, autonomous body, PSU, or Govt-funded semi-Govt body (e.g. municipality, port trust)", "Does NOT continue", "Exclusion applies"]]}],
   "narr": "Surviving spouse ka test dekhiye. Agar wo homemaker hai, to CEA chalega. Agar private unfunded organisation me kaam karti hai, to bhi chalega. Lekin agar wo Central ya State Government, autonomous body, PSU ya Govt-funded semi-Government body me hai, to CEA band ho jaayega. Is test par exam me sawal aata hai.",
   "spk": "teacher"},
  {"chapter": "Cessation & Death", "tag": "CESSATION AND DEATH FLOW",
   "title": "Two triggers, two outcomes: which event stops CEA and when",
   "cards": [
     {"kind": "steps", "color": "orange", "steps": [
        "Trigger: retirement, resignation, dismissal or removal",
        "Pay to end of that academic year, through the last office",
        "Trigger: death in service",
        "Spouse employed in a Govt-linked body? Then CEA stops",
        "Spouse not employed there? CEA continues for children"]}],
   "narr": "Ab dono triggers ka flow dekhiye. Retirement, resignation, dismissal ya removal me academic year ke end tak CEA, aur payment last office se. Death in service me pehle spouse ka employment check karein. Govt-linked job ho to rukega, nahi to bachchon ka CEA chalega.",
   "spk": "teacher"},
  {"chapter": "Cessation & Death", "tag": "STUDENT QUESTION",
   "title": "Student question: after a mid-year resignation, is next year's CEA payable?",
   "cards": [
     {"kind": "row", "color": "sky", "label": "Student asks", "text": "If an employee resigns in the middle of the year, will the child's CEA for the next year also be paid?"},
     {"kind": "row", "color": "green", "label": "Short answer", "text": "No. CEA runs only to the end of the academic year in which service ended. Next year's CEA is not payable."}],
   "narr": "Sir, agar employee ne mid-year resign kar diya, to kya us bachche ka agle saal ka CEA bhi milega?",
   "spk": "student"},
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
        out = ["# CEA & Hostel Subsidy — Master Explainer: card reference sheet", "",
               "Rates as on 2026-10-25 (corrigendum O.M. 30.06.2026). Narration is Hinglish; this sheet is English only.", ""]
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
