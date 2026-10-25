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
