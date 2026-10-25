#!/usr/bin/env python3
"""
DoPT Information Document on Suspension (updated 04.11.2022) — Master Study Guide video compiler.
Source: DoPT Information Document on Suspension (Establishment Division), CCS (CCA) Rules 1965 Rule 10,
FR 53/54/54-B/55, CCS (Pension) Rules 2021 Rules 8, 23, 43, OM 11012/17/2013-Estt.(A) dated 02.01.2014 and
the other OMs in its Annexure, plus DoPT notification dated 12.01.2026 (G.S.R. 21(E)) amending Rule 10(1) and 12(4).

Pipeline (same method as the honorarium, CEA and pension videos):
  1. SCENES (below, between the content markers) hold every card, table, chart, flowchart and Hinglish narration line.
  2. --preview  renders 1920x1080 PNG slides (one per reveal stage) into BUILD_DIR/slides
  3. narration clips are generated with the session voices (teacher = voice-00, student = voice-01)
     and saved as BUILD_DIR/clips/NNN.mp3 (NNN = scene index, 0-based)
  4. --build    assembles slides + clips into one H.264/AAC MP4 (BUILD_DIR/out/)
  5. --reference writes the English card reference sheet (markdown)
  6. --audit    checks every card fits its slide and prints density (no ffmpeg needed)
  7. --plan     writes BUILD_DIR/../narration.json (scene plan: spk, narr, card kinds)

Card kinds: stat, row, table, steps, callout, bars, quote.
  bars   {"kind":"bars","color","title","items":[(label, value, value_text), ...],"max":optional}
  quote  {"kind":"quote","color","label","text"}

On-screen text is English only. Narration is Hinglish in Roman script (no Devanagari).
Status tags on screen: VERIFIED, PARTLY VERIFIED, NOT VERIFIED, GUIDE FIX, 2026 UPDATE.

Usage:
  python3 build_suspension_video.py --audit
  python3 build_suspension_video.py --preview
  python3 build_suspension_video.py --check-clips
  python3 build_suspension_video.py --build
  python3 build_suspension_video.py --reference
  python3 build_suspension_video.py --plan
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
OUT_STEM = "suspension_dopt_masterclass"
BUILD_DIR = Path(os.environ.get("SUSP_BUILD_DIR", "/home/user/suspension_video/build"))
SLIDE_DIR = BUILD_DIR / "slides"
CLIP_DIR = BUILD_DIR / "clips"
SEG_DIR = BUILD_DIR / "segments"
OUT_DIR = BUILD_DIR / "out"
REFERENCE_MD = Path(__file__).with_name("suspension_reference_sheet.md")
PLAN_JSON = BUILD_DIR.parent / "narration.json"

TITLE_TOP = "Suspension (DoPT Information Document, updated 04.11.2022) — Master Study Guide with 2026 update"
FOOTER = "Source: DoPT Information Document on Suspension (04.11.2022) · CCS (CCA) Rules 1965 Rule 10 · GSR 156 (2022) · DoPT notification 12.01.2026 (G.S.R. 21(E))"

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
        label_w = int(max(f_l.getlength(lb) for lb, _, _ in card["items"]) + 28 * s)
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
  {"chapter": "Start Here", "tag": "INTRO · DOPT SUSPENSION INFORMATION DOCUMENT",
   "title": "Suspension, card by card: the DoPT information document, checked against the rules and the 2026 amendment",
   "cards": [
     {"kind": "stat", "color": "cyan", "head": "28 sections", "sub": "Preamble, A to Z and Annexure of the uploaded guide, all covered"},
     {"kind": "stat", "color": "orange", "head": "2026 UPDATE", "sub": "DoPT notification dated 12.01.2026 amends Rule 10(1) and 12(4)"},
     {"kind": "row", "color": "sky", "label": "Scope", "text": "Every rule, sub-rule, clause, proviso and exception. Each card carries one tag: VERIFIED, GUIDE FIX, or NOT VERIFIED."}],
   "narr": "Namaste dosto. Aaj hum Suspension par DoPT ka information document dekhenge, jo 4 November 2022 ko update hua tha. Guide ke 28 sections, yani Preamble, A se Z, aur Annexure, ek ek karke cover honge. Lekin pehle ek baat: January 2026 mein DoPT ne Rule 10(1) aur Rule 12(4) mein amendment notify kiya hai, aur guide mein kai galtiyan bhi hain. Har card par ek tag hoga: VERIFIED, GUIDE FIX, ya NOT VERIFIED.",
   "spk": "teacher"},

  {"chapter": "Start Here", "tag": "WHAT CHANGED SINCE THE GUIDE · 2026 UPDATE",
   "title": "What changed after the guide was last updated on 04.11.2022",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Currency check: guide (04.11.2022) against the position in October 2026",
      "headers": ["Item", "Guide says", "Current position", "Status"],
      "rows": [
        ["Rule 10(7) caps", "270 days; 2 years; deemed: 2 years from release", "Same, notified 19.10.2022 (GSR 156, gazette 22.10.2022)", "VERIFIED"],
        ["Rule 10(1) proviso", "C&AG exception: IA&AS member; AAG or equivalent", "Notification 12.01.2026 substitutes the proviso; adds General Central Service Group A", "GUIDE FIX"],
        ["Rule 12(4)(a)", "Not covered", "Substituted by the same notification (text partly legible)", "NOT VERIFIED"],
        ["Vigilance clearance", "OMs of 2007, 2012, 2015, 2020", "Revised OMs dated 09.10.2024 and 06.02.2025 listed by DTF", "GUIDE FIX (currency)"],
        ["Statute names", "IPC 304-B; CrPC 173(2)", "BNS s.80 and BNSS s.193 from 01.07.2024", "GUIDE FIX"]],
      "widths": [0.18, 0.30, 0.36, 0.16]}],
   "narr": "Pehle dekhte hain ki guide ke baad kya badla hai. Rule 10(7) ke 270 din aur do saal wale caps verified hain. Rule 10(1) ke proviso mein January 2026 wali notification ne badlaav kiya hai, jisme General Central Service Group A bhi shamil hua hai. Vigilance clearance wali OMs 2024 aur 2025 mein revise hui hain, aur 2024 se criminal law ke naam bhi badal gaye. Guide ko isi table ke saath padhna zaroori hai.",
   "spk": "teacher"},

  {"chapter": "Preamble and A", "tag": "SECTION A · WHAT SUSPENSION IS",
   "title": "What suspension is: temporary withdrawal of duties, not a penalty",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "OM 02.01.2014 (definition):", "text": "Suspension, in the context of disciplinary proceedings, may be defined as temporary withdrawal of duties from a government servant, pending inquiry into his/her conduct, with simultaneous reduction in pay and withdrawal of some rights/privileges."},
     {"kind": "row", "color": "green", "label": "Not a penalty", "text": "Suspension, though not a penalty, is to be resorted to sparingly. The government loses services, pays for no work, and the order carries a stigma (Para 3)."},
     {"kind": "callout", "color": "yellow", "text": "Guide Section A cites OM 11012/17/2013-Estt.(A) dated 02.01.2014, Para 3. Verified: the wording matches Para 3."}],
   "narr": "Suspension ki definition OM dated 2 January 2014 mein di gayi hai. Yeh temporary withdrawal of duties hai, pending inquiry, aur saath mein pay kam ho jaati hai aur kuch rights band ho jaate hain. Yeh penalty nahi hai, lekin sparingly use karna hai, kyunki sarkar ko service bhi nahi milti aur pay bhi deni padti hai. Guide ka Para 3 reference verified hai.",
   "spk": "student"},

  {"chapter": "Preamble and A", "tag": "SECTION B · RULE 10(1) GROUNDS",
   "title": "The three grounds for suspension under Rule 10(1), with the guide's labels mapped",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Rule 10(1) grounds: rule letter is what goes on the order",
      "headers": ["Rule clause", "Ground (in brief)", "Guide label", "Status"],
      "rows": [
        ["10(1)(a)", "Disciplinary proceeding contemplated or pending", "(a)", "VERIFIED"],
        ["10(1)(aa)", "Engaged in activities prejudicial to security of the State, in the authority's opinion", "(b)", "VERIFIED"],
        ["10(1)(b)", "Criminal case under investigation, inquiry or trial", "(c)", "VERIFIED"]],
      "widths": [0.18, 0.52, 0.14, 0.16]},
     {"kind": "callout", "color": "yellow", "text": "Use rule letters (a), (aa), (b) on the order. The guide's (a), (b), (c) labels are study labels only."}],
   "narr": "Rule 10(1) mein teen grounds hain. Clause (a) mein disciplinary proceeding contemplated ya pending hona chahiye. Clause (aa) mein security of State ka issue hota hai. Clause (b) mein criminal case investigation, inquiry ya trial mein hota hai. Guide ke labels alag hain, isliye order mein hamesha rule letter likhein. Teeno clauses verified hain.",
   "spk": "teacher"},

  {"chapter": "Preamble and A", "tag": "SECTION B · WHICH CLOCK APPLIES",
   "title": "The ground decides the hard cap later: 270 days or two years",
   "cards": [
     {"kind": "steps", "color": "green", "steps": ["Identify the ground: 10(1)(a), 10(1)(aa) or 10(1)(b)", "Record the rule clause in the suspension order", "No charge-sheet: cap 270 days for 10(1)(a)", "No charge-sheet: cap 2 years for 10(1)(aa) or 10(1)(b)", "Deemed suspension under 10(2): cap 2 years from release or intimation"]},
     {"kind": "row", "color": "orange", "label": "Why it matters", "text": "The cap depends on the ground recorded at the start. A wrong ground at the start is a wrong cap later (see Section H)."}],
   "narr": "Yeh section ka practical point hai. Suspension ka ground order mein sahi likhna zaroori hai, kyunki isi se aage ka cap tay hota hai. Agar charge-sheet nahi bani, to 10(1)(a) par 270 din, aur 10(1)(aa) ya 10(1)(b) par do saal ka cap lagta hai. Deemed suspension mein do saal release ya intimation ki date se gine jaate hain.",
   "spk": "student"},

  {"chapter": "Section C", "tag": "SECTION C · DEEMED SUSPENSION UNDER RULE 10(2)",
   "title": "Deemed suspension: the 48-hour triggers that apply without a fresh order",
   "cards": [
     {"kind": "table", "color": "red", "title": "Rule 10(2): when a Government servant is deemed suspended",
      "headers": ["Trigger", "Effective from", "Status"],
      "rows": [
        ["Detained in custody, criminal charge or otherwise, for more than 48 hours", "Date of detention", "VERIFIED"],
        ["Convicted, sentenced to more than 48 hours, and not forthwith dismissed or removed", "Date of conviction", "VERIFIED"],
        ["Explanation: 48 hours counted from start of imprisonment; intermittent periods added", "Applies to (b)", "VERIFIED"]],
      "widths": [0.52, 0.28, 0.20]},
     {"kind": "row", "color": "sky", "label": "Who orders", "text": "The appointing authority issues the formal order under Rule 10(2), even though suspension is automatic. (Guide Section F.)"}],
   "narr": "Rule 10(2) ke under deemed suspension hota hai. Agar koi officer custody mein 48 ghante se zyada rehta hai, to suspension detention ki date se maana jaata hai. Conviction ke case mein bhi 48 ghante se zyada sazaa ho aur turant dismiss na ho, to conviction ki date se. Explanation ke mutabik 48 ghante imprisonment ke start se ginte hain, aur intermittent periods bhi jorte hain.",
   "spk": "teacher"},

  {"chapter": "Section C", "tag": "SECTION C · 48-HOUR WORKED EXAMPLES",
   "title": "Worked examples: when the 48-hour rule is crossed and when it is not",
   "cards": [
     {"kind": "table", "color": "purple", "title": "Detention timing (arithmetic checked)",
      "headers": ["Case", "Detention", "Over 48 hours?", "Result"],
      "rows": [
        ["Arrest Friday 21:00, bail Monday 22:00", "73 hours", "Yes", "Deemed suspension from Friday 21:00"],
        ["Custody for about 10 hours, then released", "About 10 hours", "No", "No deemed suspension; discretionary order under 10(1) still possible"],
        ["Arrest, then released on bail after 30 hours", "About 30 hours", "No", "No 10(2) trigger; the guide's dowry example uses 10(1) instead"]],
      "widths": [0.34, 0.16, 0.16, 0.34]}],
   "narr": "Worked example se samjhte hain. Friday raat 9 baje arrest aur Monday raat 10 baje bail ka matlab hai 73 ghante. Yeh 48 ghante se zyada hai, to suspension Friday se maana jaayega. Lekin 10 ghante ki custody par deemed suspension nahi lagta, sirf discretionary order possible hai.",
   "spk": "student"},

  {"chapter": "Section C", "tag": "SECTION C · RULE 10(4) AND 10(5)",
   "title": "Rule 10(4) and 10(5): suspension after a court sets aside a penalty, and how an order continues",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "Rule 10(4), proviso (text checked):", "text": "No such further inquiry shall be ordered unless it is intended to meet a situation where the Court has passed an order purely on technical grounds without going into the merits of the case."},
     {"kind": "table", "color": "green", "title": "Rule 10(5): three limbs",
      "headers": ["Limb", "Rule in brief", "Status"],
      "rows": [
        ["10(5)(a)", "Order continues until modified or revoked, subject to 10(7)", "VERIFIED"],
        ["10(5)(b)", "If another proceeding starts during suspension, authority may continue suspension for written reasons", "VERIFIED"],
        ["10(5)(c)", "Modified or revoked by the maker or any authority above it", "VERIFIED"]],
      "widths": [0.16, 0.66, 0.18]}],
   "narr": "Rule 10(4) mein agar court penalty ko set aside kare aur department further inquiry kare, to officer ko suspended maana jaata hai. Lekin further inquiry sirf technical grounds par court ke order ke case mein hi allow hai. Rule 10(5) mein teen limbs hain: order tab tak chalta hai jab tak modify ya revoke na ho, naye proceedings ke time suspension continue ho sakta hai, aur modify ya revoke karne ka power maker ya uske upar wale authority ka hai.",
   "spk": "teacher"},

  {"chapter": "Section C", "tag": "SECTION C · ARREST INTIMATION (1955 OM)",
   "title": "Arrest must be reported to superiors: the 1955 instruction at the root of Section C",
   "cards": [
     {"kind": "row", "color": "sky", "label": "Source", "text": "MHA letter 39/59/54-Ests.(A) dated 25.02.1955, as listed in the guide's Annexure (row 1) and cited in CCS(CCA) compilations."},
     {"kind": "row", "color": "orange", "label": "Status", "text": "PARTLY VERIFIED. The subject and date match secondary sources. The full text was not fetched, so the exact duty wording is not verified."},
     {"kind": "callout", "color": "yellow", "text": "Exam point: an arrest must be intimated to the departmental superior. Silence is treated as suppression."}],
   "narr": "Section C ka pehla point arrest intimation ka hai. Yeh 1955 ke ek instruction se aaya hai, jo Annexure mein row 1 par hai. Date aur subject secondary sources se match karte hain. Lekin poora text maine fetch nahi kiya, isliye exact wording NOT VERIFIED hai.",
   "spk": "student"},

  {"chapter": "Section C", "tag": "SECTION C · GUIDE FIX · HINGLISH WORDING",
   "title": "GUIDE FIX: garbled Hinglish phrase in Section C removed",
   "cards": [
     {"kind": "table", "color": "red", "title": "Correction made in this video",
      "headers": ["Guide text (garbled)", "Corrected meaning", "Basis"],
      "rows": [
        ["'civil/polio-type detention'", "Detention whether on a criminal charge or otherwise", "Rule 10(2)(a) wording, VERIFIED"],
        ["Worked Example 3: unclosed parenthesis", "Typo; no legal effect", "Editorial"]],
      "widths": [0.34, 0.40, 0.26]}],
   "narr": "Guide mein Section C ka ek phrase ghalat tha: civil ya polio type detention. Rule 10(2)(a) mein sirf itna likha hai ki detention criminal charge par ho ya kisi aur wajah se. Yeh video us phrase ko theek karta hai. Worked example 3 mein ek bracket band nahi tha, jo sirf typo hai.",
   "spk": "student"},

  {"chapter": "Section C", "tag": "SECTION C · NOT VERIFIED · RAJIV KUMAR",
   "title": "NOT VERIFIED: Rajiv Kumar citation and the 2003 OM in Section C(f)",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Citations in Section C(f) and the Annexure",
      "headers": ["Item", "Guide", "What was checked", "Status"],
      "rows": [
        ["Case", "Union of India v. Rajiv Kumar, 2003 (5) SCALE 297", "Search results show D. Surendran Pillai v. Rajiv Kumar, (2003) 6 SCC 516", "NOT VERIFIED"],
        ["OM", "11012/8/2003-Estt.(A) dated 23.10.2003", "Listed in Annexure row 13 only", "NOT VERIFIED"],
        ["Rule reference", "Sub-rule 5(c) and 5(a)", "5(a) and 5(c) text verified (2013 amendment); guide's use of 5(a) for deemed suspension not verified", "PARTLY VERIFIED"]],
      "widths": [0.14, 0.34, 0.36, 0.16]}],
   "narr": "Section C(f) mein Rajiv Kumar ka case aur 23 October 2003 ka OM aata hai. Search mein case ka naam aur citation alag mile: D. Surendran Pillai v. Rajiv Kumar, 2003 ki SCC citation. Isliye guide ka citation NOT VERIFIED hai. Rule 10(5)(c) verified hai, lekin 10(5)(a) ka wording poori tarah verify nahi hua.",
   "spk": "teacher"},
]

SCENES += [
  {"chapter": "Section D", "tag": "SECTION D · CIRCUMSTANCES · PARA 4",
   "title": "When suspension may be ordered: the four circumstances in Para 4 of OM 02.01.2014",
   "cards": [
     {"kind": "table", "color": "cyan", "title": "Para 4: circumstances (guidance, not mandatory)",
      "headers": ["Circumstance", "Gist", "Status"],
      "rows": [
        ["(i)", "Continuance in office will prejudice investigation, trial or inquiry (for example, witness tampering)", "VERIFIED"],
        ["(ii)", "Continuance likely to prejudice where prosecution would be justified or departmental proceedings are likely to end in conviction or removal (source text partly garbled)", "PARTLY VERIFIED"],
        ["(iii)", "Government policy to deal strictly with officers involved in scandals, particularly corruption (source text partly garbled)", "PARTLY VERIFIED"],
        ["(iv)", "Prima facie case made out, and proceedings likely to end in conviction, dismissal, removal or compulsory retirement", "VERIFIED"]],
      "widths": [0.14, 0.66, 0.20]},
     {"kind": "callout", "color": "yellow", "text": "Circumstances (i) to (iii) may be used even before a prima facie case is established, as Note (a) allows."}],
   "narr": "Para 4 mein char circumstances hain jab disciplinary authority suspension par vichar kar sakti hai. Pehla, jab continuance se investigation ya inquiry prejudice hogi. Chautha, jab prima facie case ban chuka ho aur proceedings se removal ya dismissal ki sambhavna ho. Yeh guidance hai, mandatory nahi. Do circumstances ke wording partly verified hain.",
   "spk": "teacher"},

  {"chapter": "Section D", "tag": "SECTION D · GUIDE FIX · NOTE (b) LABELS",
   "title": "GUIDE FIX: the misdemeanour list is Note (b)(i) to (v), not v(a) to (e)",
   "cards": [
     {"kind": "table", "color": "red", "title": "Misdemeanours where suspension may be desirable (Note (b))",
      "headers": ["Source label", "Misdemeanour", "Status"],
      "rows": [
        ["Note (b)(i)", "Any offence or conduct involving moral turpitude", "VERIFIED"],
        ["Note (b)(ii)", "Corruption, embezzlement or misappropriation; disproportionate assets; misuse of office for gain", "VERIFIED"],
        ["Note (b)(iii)", "Serious negligence or dereliction causing considerable loss", "VERIFIED"],
        ["Note (b)(iv)", "Desertion of duty", "VERIFIED"],
        ["Note (b)(v)", "Refusal or deliberate failure to carry out written orders of superiors", "VERIFIED"]],
      "widths": [0.18, 0.62, 0.20]},
     {"kind": "row", "color": "sky", "label": "Source", "text": "Note (b) list is from DoP&AR O.M. 42014/7/83-Ests.(A) dated 18.02.1984, quoted in the 2014 OM. The guide's v(a) to (e) labels were wrong."}],
   "narr": "Guide mein misdemeanour list ko v(a) se v(e) label kiya gaya tha, jo ghalat hai. Asli OM mein yeh Note (b) ke under (i) se (v) hai. List 1984 ke OM se li gayi hai. Teeno rows ke content verified hain, sirf label fix hua hai.",
   "spk": "student"},

  {"chapter": "Section E", "tag": "SECTION E · DOWRY DEATH · RULE 10(1)",
   "title": "Dowry death cases: arrest or police report triggers immediate suspension",
   "cards": [
     {"kind": "steps", "color": "red", "steps": ["Police register case under 304-B IPC (dowry death)", "Arrested? Suspend at once, regardless of how long custody lasts", "Not arrested? Suspend on the day the police report under 173(2) CrPC reaches the Magistrate", "Prima facie indication of the officer's offence is the trigger", "Order must be reported to the next higher authority; void unless confirmed within one month"]},
     {"kind": "row", "color": "orange", "label": "Status", "text": "VERIFIED against the 2022 information document. The OM number 11012/8/87 dated 22.06.1987 is listed in the Annexure but its text was not fetched (NOT VERIFIED)."}],
   "narr": "Dowry death ke case mein policy alag hai. Agar officer ki arrest hui hai, to detention kitni bhi ho, turant suspension hai. Agar arrest nahi hui, to police report, jo 173(2) CrPC ke under Magistrate ko jaati hai, aur prima facie offence dikhaye, usi din suspension hota hai. Yeh 10(1) ke under hai, isliye 48 ghante wala test yahan nahi lagta. OM ka number NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Section E", "tag": "SECTION E · GUIDE FIX · BNS AND BNSS",
   "title": "GUIDE FIX: IPC and CrPC references updated to BNS section 80 and BNSS section 193",
   "cards": [
     {"kind": "table", "color": "red", "title": "Statute references in Section E",
      "headers": ["Guide cites", "Current law (from 01.07.2024)", "Status"],
      "rows": [
        ["304-B IPC (dowry death)", "Section 80 BNS, same definition and punishment", "VERIFIED"],
        ["173(2) CrPC (police report)", "Section 193 BNSS", "VERIFIED"],
        ["Offence before 01.07.2024", "IPC 304-B and CrPC 173 still apply to the offence and procedure as of that date", "VERIFIED"],
        ["OM 11012/8/87 dated 22.06.1987", "Date and number not fetched", "NOT VERIFIED"]],
      "widths": [0.30, 0.50, 0.20]}],
   "narr": "Guide ne IPC aur CrPC ke sections use kiye hain. 1 July 2024 se naye law lagu hain. 304-B IPC ab section 80 BNS hai, aur words same hain. 173(2) CrPC ab section 193 BNSS hai. Pehle ke offence par purana law lagega. OM ka date aur number NOT VERIFIED hai.",
   "spk": "student"},

  {"chapter": "Section F", "tag": "SECTION F · WHO CAN SUSPEND · RULE 10(1)",
   "title": "Who may place a Government servant under suspension: four authorities",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Competent authorities under Rule 10(1)",
      "headers": ["Authority", "Meaning", "Status"],
      "rows": [
        ["Appointing Authority (AA)", "Authority that appoints the officer", "VERIFIED"],
        ["Authority above the AA", "Any authority to which the AA is subordinate", "VERIFIED"],
        ["Disciplinary Authority (DA)", "Authority that can start and decide proceedings", "VERIFIED"],
        ["Any other authority", "Empowered by the President, by general or special order", "VERIFIED"]],
      "widths": [0.30, 0.52, 0.18]},
     {"kind": "callout", "color": "yellow", "text": "An order by any other authority is ultra vires, and the order is void."}],
   "narr": "Rule 10(1) ke mutabik suspension order chaar authority de sakti hain: appointing authority, uske upar wali koi bhi authority, disciplinary authority, aur President ki general ya special order se empower koi aur authority. Is list ke bahar ka order valid nahi hai. Sab row verified hain.",
   "spk": "teacher"},

  {"chapter": "Section F", "tag": "SECTION F · PROVISO · 2026 UPDATE",
   "title": "2026 UPDATE: the lower-authority proviso now covers General Central Service Group A",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Proviso to Rule 10(1): before and after notification dated 12.01.2026",
      "headers": ["Element", "Before (guide)", "After (G.S.R. 21(E))", "Status"],
      "rows": [
        ["C&AG exception", "Orders on IA&AS members; AAG or equivalent", "Same, plus members of General Central Service Group A", "GUIDE FIX (2026)"],
        ["Regular IA&AS members", "Excluded from the AAG limb", "Still excluded", "VERIFIED (both)"],
        ["Duty of lower authority", "Report forthwith to AA the circumstances", "Unchanged", "VERIFIED"],
        ["Exact new wording", "Not in guide", "Gazette text partly illegible; the Hindi text may also name Group B", "NOT VERIFIED"]],
      "widths": [0.20, 0.30, 0.32, 0.18]}],
   "narr": "Yeh 2026 ka sabse important update hai. Rule 10(1) ke proviso mein C&AG wale exception mein ab General Central Service Group A ke members bhi aate hain, jo regular IA&AS nahi hain. Lower authority ka duty to report forthwith wahi hai. Gazette ki Hindi aur English text kuch jagah illegible hai, isliye exact wording NOT VERIFIED hai, aur gazette se confirm karna zaroori hai.",
   "spk": "student"},

  {"chapter": "Section F", "tag": "SECTION F · FIELD OFFICERS · OM 9.08.1974",
   "title": "Field supervisors can be empowered, but only for gross dereliction and with a one-month check",
   "cards": [
     {"kind": "steps", "color": "green", "steps": ["Headquarters is far away: field supervisory officer in an away-from-HQ office", "Special order in the name of the President is needed", "Only for gross dereliction of duties", "Suspending authority reports the facts immediately to the next higher authority", "Void ab initio unless reviewing authority confirms within one month"]},
     {"kind": "row", "color": "sky", "label": "Source", "text": "OM 7/4/74-Ests.(A) dated 09.08.1974, listed as Annexure row 3. The one-month rule also appears in the 2022 document's footnote to Section E, which supports the attribution."}],
   "narr": "Headquarters se door field offices ke supervisory officer ko President ke naam ke special order se empower kiya ja sakta hai. Lekin sirf gross dereliction ke cases mein. Har case ki report turant next higher authority ko deni hai, aur order ek mahine mein confirm na ho to ab initio void ho jaata hai. Yeh OM 1974 ka hai, aur Annexure row 3 mein listed hai.",
   "spk": "teacher"},

  {"chapter": "Section F", "tag": "SECTION F · WORKED EXAMPLE · GUIDE FIX",
   "title": "GUIDE FIX: the confirmation deadline is one month from the order date, not 31 May",
   "cards": [
     {"kind": "table", "color": "red", "title": "Field suspension of 5 May: confirmation window",
      "headers": ["Event", "Date", "Effect"],
      "rows": [
        ["Order passed; facts reported to Regional HQ", "5 May", "Clock runs from order date"],
        ["Confirmation on 20 May (guide's valid case)", "20 May", "Valid, within the one-month window"],
        ["Guide said void if not confirmed by 31 May", "31 May", "WRONG: still inside the window"],
        ["One month from 5 May", "5 June (end date convention NOT VERIFIED)", "Void ab initio if not confirmed by then"]],
      "widths": [0.46, 0.26, 0.28]}],
   "narr": "Guide ka example ghalat tha. Ek order 5 May ko pass hua, aur guide ne kaha ki 31 May tak confirm na ho to void hai. Lekin 31 May abhi ek mahine ke andar hai. Correct deadline 5 June hai. End date ka convention NOT VERIFIED hai, isliye hard date ke liye ek din ka buffer rakhna samajhdari hai.",
   "spk": "student"},

  {"chapter": "Section F", "tag": "SECTION F · DEEMED ORDER AND REPORTING",
   "title": "Who writes the deemed-suspension order, and when a lower authority must report forthwith",
   "cards": [
     {"kind": "table", "color": "purple", "title": "Authority mapping in the two worked examples",
      "headers": ["Case", "AA", "Order-maker", "Result"],
      "rows": [
        ["Deemed suspension (10(2)) after detention", "Joint Secretary", "AA issues the formal order", "Effective date from detention; AA order records it"],
        ["Under Secretary suspends a Section Officer", "Joint Secretary", "Under Secretary (lower than AA)", "Proviso applies: report to JS forthwith"]],
      "widths": [0.30, 0.18, 0.26, 0.26]},
     {"kind": "row", "color": "yellow", "label": "Missing report", "text": "A missing forthwith report is a procedural defect in the suspension file."}],
   "narr": "Deemed suspension mein formal order appointing authority hi banati hai, chahe suspension law ke zariye pehle se lag gayi ho. Agar Under Secretary jaisi lower authority Section Officer ko suspend karti hai, to proviso ke mutabik turant AA ko report karna hai. Report na karne par file mein defect aata hai.",
   "spk": "teacher"},

  {"chapter": "Section G", "tag": "SECTION G · REASONS WITHIN THREE MONTHS",
   "title": "Reasons for suspension must be communicated within three months if not in the order",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "OM 02.01.2014, Para 5:", "text": "Reasons for Suspension, if not indicated in the suspension order itself, should be communicated within three months."},
     {"kind": "row", "color": "green", "label": "Best practice", "text": "Write the grounds in the suspension order itself. Silence starts a three-month clock that ends in a stronger challenge."},
     {"kind": "callout", "color": "yellow", "text": "Worked example: a 1 Feb order is safe if reasons go by 30 April (or 1 May; convention NOT VERIFIED). Use the earlier date."}],
   "narr": "Reasons ka rule Para 5 mein hai. Agar suspension order mein reasons nahi likhe, to teen mahine ke andar communicate karne hain. Best practice yeh hai ki order mein hi grounds likhe jaayein. Teen mahine ki end date ka convention NOT VERIFIED hai, isliye earlier date hi safe hai.",
   "spk": "teacher"},

  {"chapter": "Section H", "tag": "SECTION H · MODIFY OR REVOKE",
   "title": "Review (i): who may modify or revoke a suspension at any time",
   "cards": [
     {"kind": "row", "color": "sky", "label": "Rule", "text": "An order made or deemed made under Rule 10 may at any time be modified or revoked by the authority that made it, or by any authority to which that authority is subordinate. (Rule 10(5)(c), VERIFIED.)"},
     {"kind": "callout", "color": "yellow", "text": "Guide says deemed suspension ends only this way, not automatically. The 'Rajiv Kumar' note in (i) is NOT VERIFIED."}],
   "narr": "Review ka pehla point Rule 10(5)(c) hai. Suspension kisi bhi waqt modify ya revoke ho sakta hai, usi authority ke dwara, ya uske upar wali authority ke dwara. Guide ka Rajiv Kumar note NOT VERIFIED hai, isliye use exam ya bill mein confirm karke hi likhein.",
   "spk": "student"},

  {"chapter": "Section H", "tag": "SECTION H · 90-DAY REVIEW · RULE 10(6) AND 10(7)",
   "title": "The 90-day review and the 180-day extension",
   "cards": [
     {"kind": "table", "color": "green", "title": "Review ladder (verified text of Rule 10(6) and 10(7))",
      "headers": ["Step", "Rule", "Deadline"],
      "rows": [
        ["First review", "10(6), by the authority competent to revoke, on Review Committee recommendation", "Before 90 days from effective date"],
        ["Order without review", "10(7): not valid after 90 days", "Invalid after 90 days"],
        ["Extension", "10(6): one extension at a time", "Maximum 180 days at a time"],
        ["Next review", "10(6): before the extended period ends", "Rolling cycle"]],
      "widths": [0.22, 0.52, 0.26]},
     {"kind": "callout", "color": "yellow", "text": "Review must produce an order (extend or revoke). A meeting without an order does not save the suspension."}],
   "narr": "Rule 10(6) aur 10(7) ke mutabik suspension ko effective date se 90 din ke andar review karna hai, aur review Review Committee ki recommendation par hona chahiye. Agar review na ho, to order 90 din ke baad valid nahi rehta. Extension ek baar mein 180 din se zyada nahi ho sakta. Review ka matlab sirf meeting nahi, order pass karna hai.",
   "spk": "teacher"},

  {"chapter": "Section H", "tag": "SECTION H · 2022 CAPS · GSR 156",
   "title": "2022 caps where no charge-sheet is issued: 270 days, two years, and two years for deemed suspension",
   "cards": [
     {"kind": "table", "color": "red", "title": "Proviso to Rule 10(7), substituted by GSR 156 (notification 19.10.2022)",
      "headers": ["Suspension ground", "Total cap (no charge-sheet)", "Status"],
      "rows": [
        ["10(1)(a): contemplated or pending proceedings", "270 days from order date", "VERIFIED"],
        ["10(1)(aa) or 10(1)(b): security or criminal case", "2 years from order date", "VERIFIED"],
        ["Deemed suspension under 10(2)", "2 years from later of release or intimation", "VERIFIED"],
        ["Charge-sheet issued", "Caps do not apply; 90/180 cycle continues", "VERIFIED"]],
      "widths": [0.44, 0.38, 0.18]},
     {"kind": "row", "color": "orange", "label": "Includes extensions", "text": "The cap counts the original period plus every extension under sub-rule (6)."}],
   "narr": "2022 ke amendment ne caps diye hain, jab charge-sheet nahi bani ho. Disciplinary proceedings contemplated ya pending hon, to 270 din. Security ya criminal case mein do saal. Deemed suspension mein release ya intimation, jo bhi baad ki ho, us date se do saal. Charge-sheet aa jaaye to yeh caps nahi lagte. Sab verified hai.",
   "spk": "teacher"},

  {"chapter": "Section H", "tag": "SECTION H · DETENTION PROVISO · 2022",
   "title": "Deemed suspension with continuing detention: no review needed, and the clock starts later",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "2022 proviso (text checked):", "text": "No review of suspension shall be necessary in the case of deemed suspension, if the Government servant continues to be under detention; the ninety days period shall be computed from the date he is released or the date his release is intimated to the appointing authority, whichever is later."},
     {"kind": "row", "color": "green", "label": "Status", "text": "VERIFIED. Source: DoPT information document, as amended by GSR 156."}],
   "narr": "Deemed suspension mein agar officer abhi bhi detention mein hai, to review zaroori nahi. 90 din ki ginti release ki date se, ya appointing authority ko release ki intimation ki date se, jo bhi later ho, se shuru hogi. Yeh 2022 ka proviso hai, aur text verified hai.",
   "spk": "student"},

  {"chapter": "Section H", "tag": "SECTION H · COURTS' CONCERN · OM 18.11.2014",
   "title": "Why timely review matters: courts' criticism of prolonged suspension",
   "cards": [
     {"kind": "row", "color": "sky", "label": "Courts", "text": "Prolonged suspension leaves the officer under hardship, the Government pays subsistence without work, and full salary may follow exoneration."},
     {"kind": "row", "color": "green", "label": "Instruction", "text": "Timely, just review; expeditious finalisation of proceedings. OM 11012/17/2013-Estt.(A) dated 18.11.2014 (the 2022 document cites this date before Section I)."}],
   "narr": "Courts ne baar baar kaha hai ki lamba suspension officer par hardship daalta hai, aur sarkar bina kaam ke subsistence deti hai. Exoneration par poori salary bhi deni padti hai. Isliye 18 November 2014 ke OM mein timely review aur jaldi proceedings khatam karne ki baat hai. Date verified hai.",
   "spk": "teacher"},

  {"chapter": "Section H", "tag": "SECTION H · WORKED EXAMPLES",
   "title": "Worked examples: 90/180 ladder with the caps, and deemed suspension clock",
   "cards": [
     {"kind": "table", "color": "purple", "title": "Day-count arithmetic (convention: day 0 = order date; checked)",
      "headers": ["Case", "Order", "Review by", "Hard cap"],
      "rows": [
        ["Mr A, 10(1)(a), no charge-sheet", "1 Jan", "31 Mar (90th day is 1 Apr)", "270th day: 28 Sep"],
        ["Extension of 180 days from 31 Mar", "31 Mar", "27 Sep (next review)", "Still capped at 28 Sep"],
        ["Mr B, 10(1)(b), no charge-sheet", "1 Jan", "31 Mar", "Two years from 1 Jan"],
        ["Ms C, deemed, detained 1 Mar, released 18 Sep, intimated 25 Sep", "1 Mar", "Clock from 25 Sep (later date)", "Two years from 25 Sep"]],
      "widths": [0.36, 0.12, 0.28, 0.24]},
     {"kind": "callout", "color": "yellow", "text": "Day-count convention (day 0 or day 1) is NOT VERIFIED. Set the file diary by the earlier date."}],
   "narr": "Mr A ka case 1 January ko 10(1)(a) par suspend hua. Review 31 March se pehle, aur extension ke baad 27 September tak. Lekin 270 din ka cap 28 September ko khatam hota hai. Ms C ka deemed suspension 1 March ko shuru hua, aur clock 25 September se chalega, kyunki intimation later hai. Day-count convention NOT VERIFIED hai.",
   "spk": "student"},
]

SCENES += [
  {"chapter": "Section I", "tag": "SECTION I · REVIEW COMMITTEE · THREE TEMPLATES",
   "title": "Review Committee composition: three templates set by where the President sits",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Composition (OM 07.01.2004, as reflected in the 2014 OM)",
      "headers": ["Template", "Condition", "Members", "Status"],
      "rows": [
        ["(a)", "President is neither DA nor Appellate Authority", "DA + Appellate Authority + one more officer of DA/appellate level (same or another CG office)", "VERIFIED"],
        ["(b)", "Appellate Authority is the President", "DA + two officers of Secretary/Addl. Secretary/JS level, equal or higher than DA", "VERIFIED"],
        ["(c)", "DA is the President", "Three officers of Secretary/Addl. Secretary/JS level, higher than the suspended official", "VERIFIED"]],
      "widths": [0.10, 0.30, 0.44, 0.16]},
     {"kind": "row", "color": "green", "label": "Permanent or ad hoc", "text": "The ministry or department may constitute committees on a permanent or ad hoc basis."}],
   "narr": "Review Committee ki composition teen templates mein hai. Agar President na DA hai na Appellate Authority, to template (a): DA, Appellate Authority, aur ek aur officer. Agar Appellate Authority President hai, to template (b): DA ke saath do officers. Agar DA President hai, to template (c): teen officers jo suspended officer se senior hon. Yeh sab verified hai.",
   "spk": "teacher"},

  {"chapter": "Section I", "tag": "SECTION I · ONE-YEAR RULE · OM 07.01.2004",
   "title": "The one-year rule: ordinary reinstatement, with three exceptions",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "OM 07.01.2004 (text checked):", "text": "If the officer has been under suspension for one year without any charges being filed in a court of law or no charge-memo has been issued in a departmental enquiry, he shall ordinarily be reinstated in service without prejudice to the case against him."},
     {"kind": "table", "color": "orange", "title": "Exceptions: continuation may be recommended",
      "headers": ["Exception", "Status"],
      "rows": [
        ["Police or judicial custody", "VERIFIED"],
        ["Accused of a serious crime", "VERIFIED"],
        ["Matter involving national security", "VERIFIED"]],
      "widths": [0.7, 0.3]}],
   "narr": "One year wala rule OM 7 January 2004 se hai. Agar officer ek saal se suspended hai, aur na court mein charge file hua hai, na departmental charge-memo mein, to use ordinarily reinstate karna hai, bina case ko prejudice kiye. Teen exceptions hain: police ya judicial custody, serious crime ka accuse hona, aur national security. Teeno verified hain.",
   "spk": "student"},

  {"chapter": "Section I", "tag": "SECTION I · PROCEDURE · WORKED EXAMPLE",
   "title": "Picking the template and running the one-year check: worked example",
   "cards": [
     {"kind": "steps", "color": "green", "steps": ["Find where the President sits in the chain", "Pick template (a), (b) or (c)", "Committee weighs facts, hardship and subsistence cost", "Check the one-year test: any court charge or charge-memo?", "Recommendation goes to the competent authority, who passes the order within the Section H timeframe"]},
     {"kind": "row", "color": "purple", "label": "Example", "text": "Under Secretary suspended; DA is Joint Secretary; Appellate Authority is Additional Secretary. President not involved: template (a)."}],
   "narr": "Committee banane ke liye pehle dekhna hai ki President kahan baithta hai. Under Secretary ka case, DA Joint Secretary, Appellate Authority Additional Secretary, aur President involved nahi hai, to template (a). Committee ki recommendation ke baad competent authority ko Section H ke time limit mein order pass karna hai.",
   "spk": "teacher"},

  {"chapter": "Section J", "tag": "SECTION J · SUBSISTENCE · FR 53(1)(ii)(a)",
   "title": "Subsistence allowance: leave salary on half pay, plus DA on that amount",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "2014 OM, Para 9 (text checked):", "text": "A Government servant under suspension is not paid any pay but is allowed a Subsistence Allowance at an amount equivalent to the leave salary which he would have drawn if on leave on half average pay or half pay, and in addition dearness allowance, if admissible on the basis of such leave salary."},
     {"kind": "row", "color": "green", "label": "Status", "text": "VERIFIED. FR 53(1)(ii)(a) referenced in the same paragraph."}],
   "narr": "Suspension mein pay nahi milti, subsistence allowance milta hai. Yeh leave salary ke barabar hota hai, jo half average pay ya half pay par banta hai, plus DA agar us leave salary par admissible ho. Text verified hai, aur reference FR 53(1)(ii)(a) hai.",
   "spk": "teacher"},

  {"chapter": "Section J", "tag": "SECTION J · VARIATION AFTER THREE MONTHS",
   "title": "After three months the authority may vary subsistence by up to 50 per cent",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Variation after the first three months (FR 53(1)(ii)(a), checked)",
      "headers": ["Limb", "Trigger", "Limit", "Status"],
      "rows": [
        ["Increase", "Prolongation not directly attributable to the officer; reasons in writing", "Up to 50% of first-3-months amount", "VERIFIED"],
        ["Reduce", "Prolongation directly attributable to the officer; reasons in writing", "Up to 50% of first-3-months amount", "VERIFIED"],
        ["DA", "DA recomputed on the increased or reduced amount", "Follows the varied figure", "VERIFIED"]],
      "widths": [0.14, 0.44, 0.26, 0.16]}],
   "narr": "Teen mahine ke baad authority subsistence ko badha ya ghata sakti hai, par 50 percent se zyada nahi. Badhaane ke liye prolongation officer ki wajah se nahi honi chahiye. Ghatane ke liye officer ki wajah se honi chahiye. Dono cases mein reasons likhna zaroori hai, aur DA naye amount par chalega.",
   "spk": "student"},

  {"chapter": "Section J", "tag": "SECTION J · OTHER ALLOWANCES · FR 53(2)",
   "title": "Other compensatory allowances, and the no-other-employment certificate",
   "cards": [
     {"kind": "row", "color": "sky", "label": "FR 53(1)(ii)(b)", "text": "Other compensatory allowances continue on the pay drawn on the date of suspension, subject to their own conditions. (Guide text; the 2014 OM text was not fetched in full.)"},
     {"kind": "quote", "color": "cyan", "label": "FR 53(2) (text checked):", "text": "No payment shall be made unless the Government servant furnishes a certificate that he is not engaged in any other employment, business, profession or vocation."},
     {"kind": "callout", "color": "red", "text": "Side business while suspended means no subsistence payment without the certificate."}],
   "narr": "Compensatory allowances bhi milte hain, lekin unki apni shartein hoti hain. FR 53(2) mein saaf likha hai ki payment tabhi hogi jab officer certificate de ki woh koi doosri employment, business, profession ya vocation nahi kar raha. FR 53(2) ka text verified hai, aur FR 53(1)(ii)(b) ka wording partly verified hai.",
   "spk": "teacher"},

  {"chapter": "Section J", "tag": "SECTION J · RECOVERIES · 2014 OM PARA 14",
   "title": "Recoveries from subsistence: compulsory, optional, and never",
   "cards": [
     {"kind": "table", "color": "green", "title": "Para 14 of OM 02.01.2014 (buckets checked)",
      "headers": ["Bucket", "Items", "Status"],
      "rows": [
        ["Compulsory", "Income tax; house rent (licence fee) and allied charges; repayment of Government loans (rate by HoD); CGHS contribution; CGEGIS subscription", "VERIFIED"],
        ["Optional (officer's choice)", "PLI premia; dues to co-operative stores or societies; refund of GPF advance", "VERIFIED"],
        ["Not to be made", "GPF subscription; amounts due under court attachment; recovery of loss to Government", "NOT VERIFIED (list not fetched in full)"]],
      "widths": [0.22, 0.56, 0.22]}],
   "narr": "Subsistence se recovery ke teen buckets hain. Compulsory: income tax, licence fee, loans ki repayment jiska rate HoD tay karega, CGHS aur CGEGIS. Optional: PLI, co-op dues, aur GPF advance ki refund. Teesra bucket, yani kaatna nahi: GPF subscription, court attachment, aur loss recovery. Pehle do buckets verified hain, teesra bucket NOT VERIFIED hai.",
   "spk": "student"},

  {"chapter": "Section J", "tag": "SECTION J · WORKED ARITHMETIC · BARS",
   "title": "Worked arithmetic: pay of Rs 80,000 plus 50 per cent DA on the half-pay base",
   "cards": [
     {"kind": "bars", "color": "cyan", "title": "Monthly subsistence (Rs), guide example",
      "items": [("Months 1 to 3: half pay 40,000 + DA 20,000", 60000, "Rs 60,000"),
                ("Reduced by 40%: 24,000 + DA 12,000", 36000, "Rs 36,000"),
                ("Increased by 40%: 56,000 + DA 28,000", 84000, "Rs 84,000")],
      "max": 90000},
     {"kind": "row", "color": "yellow", "label": "Assumption", "text": "DA at 50% is the guide's assumption (rate NOT VERIFIED). Each figure is 40% of Rs 60,000, applied to total subsistence."}],
   "narr": "Worked example: pay 80,000 rupees, half pay 40,000, aur DA 50 percent, yani 20,000. Pehle teen mahine 60,000. Reduction 40 percent ho to 36,000, aur increase 40 percent ho to 84,000. Arithmetic check ho gaya. DA ka 50 percent rate guide ka assumption hai, isliye NOT VERIFIED.",
   "spk": "student"},

  {"chapter": "Section J", "tag": "SECTION J · PAY FLOW",
   "title": "Subsistence flow: from suspension to the final order",
   "cards": [
     {"kind": "steps", "color": "green", "steps": ["Suspension: subsistence = leave salary on half pay plus DA", "Before payment: certificate of no other employment (FR 53(2))", "Month 4 onward: authority decides increase or reduction with written reasons", "Recoveries: compulsory bucket enforced; optional at officer's choice; never bucket excluded", "Proceedings end: FR 54-B order fixes pay and status (Section W)"]},
     {"kind": "row", "color": "orange", "label": "Floor", "text": "Under FR 54-B(9), any amount below full pay cannot be less than the subsistence already paid (VERIFIED)."}],
   "narr": "Subsistence ka flow yeh hai. Suspension ke baad subsistence half pay aur DA par chalta hai. Payment se pehle certificate chahiye. Teen mahine ke baad variation possible hai, reasons ke saath. Recoveries teen buckets mein hain. Final order FR 54-B se hota hai, aur floor yeh hai ki kam amount bhi subsistence se kam nahi ho sakta.",
   "spk": "teacher"},

  {"chapter": "Section K", "tag": "SECTION K · SEALED COVER · PROCEDURE",
   "title": "Promotion during suspension: DPC meets, recommendation goes in a sealed cover",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Sealed-cover rules (procedure as stated in the guide)",
      "headers": ["Point", "Rule", "Status"],
      "rows": [
        ["DPC", "Officer is considered with others; name is not dropped", "NOT VERIFIED (OM 14.09.1992 not fetched)"],
        ["Recommendation", "Placed in sealed cover; not acted upon", "NOT VERIFIED"],
        ["Opening", "Depends on outcome of disciplinary or criminal case", "NOT VERIFIED"],
        ["Suspension after DPC, before promotion", "Recommendation is deemed to be in the sealed cover", "NOT VERIFIED"]],
      "widths": [0.26, 0.48, 0.26]},
     {"kind": "row", "color": "sky", "label": "Corroborated", "text": "OM 22011/4/91-Estt.(A) dated 14.09.1992 is in Annexure row 10 with the same subject. The 2014 Para 11 cross-reference is NOT VERIFIED."}],
   "narr": "Promotion ke case mein officer DPC mein consider hota hai, lekin recommendation sealed cover mein rehti hai. Sealed cover kholna ya na kholna outcome par depend karta hai. Yeh 1992 ke OM ka procedure hai, jo Annexure mein listed hai, lekin procedure ka text aur 2014 Para 11 ka cross-reference NOT VERIFIED hain.",
   "spk": "teacher"},

  {"chapter": "Section K", "tag": "SECTION K · SEALED COVER · WORKED TIMELINE",
   "title": "Sealed cover in practice: exoneration opens the cover, an adverse finding does not",
   "cards": [
     {"kind": "steps", "color": "purple", "steps": ["1 June: DPC places officer on panel; recommendation sealed", "Officer is under suspension, so the cover stays closed", "15 November: proceedings end in exoneration; suspension wholly unjustified", "Cover opens; recommendation acted upon with consequential benefits from the panel date", "Adverse conclusion instead: cover stays closed; recommendation unacted"]},
     {"kind": "callout", "color": "yellow", "text": "Outcome-based opening rule is NOT VERIFIED against the OM text. Confirm before quoting in a file."}],
   "narr": "Worked timeline dekhte hain. 1 June ko DPC ne panel banaya, recommendation sealed hui. 15 November ko exoneration hua, to cover khulega aur promotion panel date se consequential benefit ke saath hoga. Adverse finding ho to cover nahi khulega. Lekin outcome-based rule ka OM text abhi NOT VERIFIED hai.",
   "spk": "student"},

  {"chapter": "Section L", "tag": "SECTION L · ACR WRITING · WINDOW",
   "title": "ACR writing by an officer under suspension: the later of two dates",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Window for a suspended reporting or reviewing officer (OM 01.08.1978)",
      "headers": ["Clock", "Rule", "Status"],
      "rows": [
        ["Limb A", "Two months from the date of suspension", "NOT VERIFIED (1978 OM text not fetched)"],
        ["Limb B", "One month from the date the report fell due", "NOT VERIFIED"],
        ["Test", "Use whichever is later; no CR writing after that date", "NOT VERIFIED"]],
      "widths": [0.18, 0.50, 0.32]},
     {"kind": "row", "color": "sky", "label": "Corroborated", "text": "OM 21011/2/78-Estt.(A) dated 01.08.1978 is in Annexure row 5, with the same subject."}],
   "narr": "Suspended officer ACR likh sakta hai, lekin do clocks dekhne hain: suspension se do mahine, ya report due date se ek mahina. Jo later ho, woh window hai. Date aur subject Annexure se match karte hain, lekin 1978 OM ka text NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Section L", "tag": "SECTION L · MAJOR-PART RULE · WORKED EXAMPLE",
   "title": "Major-part rule (2000) and the 'later date' worked example",
   "cards": [
     {"kind": "table", "color": "purple", "title": "Worked example: CR due 30 April, suspended 20 March (arithmetic checked)",
      "headers": ["Option", "Calculation", "Result"],
      "rows": [
        ["A: from suspension", "20 March + 2 months", "20 May"],
        ["B: from due date", "30 April + 1 month", "31 May"],
        ["Later date applies", "Later of A and B", "31 May"],
        ["Suspended 1 June (after due date)", "A: 1 Aug; B: 31 May", "1 Aug (later)"]],
      "widths": [0.34, 0.36, 0.30]},
     {"kind": "row", "color": "red", "label": "Major-part rule", "text": "If suspended for the major part of the writing period, the officer may not write or review subordinates' ACRs (OM 25.10.2000, Annexure row 12; text NOT VERIFIED)."}],
   "narr": "Worked example mein CR 30 April ko due thi, aur suspension 20 March ko hua. Option A se 20 May, option B se 31 May, to later date 31 May hai. Dusra case, 1 June ko suspension, to 1 August. Major-part rule 2000 ke OM se hai, aur uska text NOT VERIFIED hai.",
   "spk": "student"},

  {"chapter": "Section M", "tag": "SECTION M · LTC · PARA 12",
   "title": "LTC during suspension: the officer cannot claim it, but the family can",
   "cards": [
     {"kind": "row", "color": "sky", "label": "Officer", "text": "Cannot avail LTC, because no leave (including casual leave) can be granted during suspension (FR 55 bar, VERIFIED)."},
     {"kind": "row", "color": "green", "label": "Family", "text": "Remains entitled, because the officer continues in service (guide: Para 12 of the 2014 OM; the paragraph number is NOT VERIFIED)."},
     {"kind": "callout", "color": "yellow", "text": "Worked example: officer's advance is rejected; spouse and children's hometown LTC is admissible."}],
   "narr": "LTC ke liye leave chahiye, aur suspension mein leave nahi milti. Isliye officer khud LTC nahi le sakta. Lekin officer service mein rehta hai, isliye family ka LTC entitlement rehta hai. FR 55 ka bar verified hai, aur Para 12 ka reference NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Section N", "tag": "SECTION N · FR 55 · LEAVE BAR",
   "title": "FR 55: no leave of any kind during suspension, and what the guide claims about hospitalisation",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "FR 55 (text checked):", "text": "Leave may not be granted to a Government servant under suspension."},
     {"kind": "table", "color": "orange", "title": "Hospitalisation example in the guide",
      "headers": ["Claim", "Status"],
      "rows": [
        ["Medical leave is not sanctioned during suspension", "VERIFIED (FR 55 bar)"],
        ["Special leave for hospitalisation is regularised administratively", "NOT VERIFIED"],
        ["Final regularisation under FR 54-B order", "VERIFIED (consistent with FR 54-B)"]],
      "widths": [0.6, 0.4]}],
   "narr": "FR 55 mein koi carve out nahi hai. Suspended officer ko koi leave nahi milti, medical bhi nahi. Guide kehta hai ki hospitalisation ka period administrative route se regularise hota hai, lekin yeh NOT VERIFIED hai. Final settlement FR 54-B order se hota hai.",
   "spk": "student"},

  {"chapter": "Section O", "tag": "SECTION O · HEADQUARTERS · PARA 10",
   "title": "Headquarters during suspension: the last place of duty, changed only on two conditions",
   "cards": [
     {"kind": "steps", "color": "green", "steps": ["Default: headquarters is the last place of duty", "Suspension order must state the headquarters clearly", "Officer may not leave the station without prior permission", "On officer's request: change allowed only if no extra expenditure (TA etc.)", "And no other complications for the inquiry"]},
     {"kind": "row", "color": "sky", "label": "Source", "text": "Para 10 of OM 02.01.2014 (VERIFIED). Annexure row 2 gives the 1956 OM as the parent source (NOT VERIFIED text)."}],
   "narr": "Headquarters ka default last place of duty hota hai. Suspension order mein headquarters saaf likhna chahiye. Station chhodne ke liye prior permission zaroori hai. Officer request kare to change ho sakta hai, lekin do conditions ke saath: koi extra kharcha nahi, aur inquiry mein koi complication nahi. Para 10 verified hai.",
   "spk": "teacher"},

  {"chapter": "Section O", "tag": "SECTION O · HEADQUARTERS · WORKED EXAMPLE",
   "title": "Worked example: moving headquarters on medical grounds",
   "cards": [
     {"kind": "table", "color": "purple", "title": "Two conditions, tested separately",
      "headers": ["Condition", "Case A (Jaipur shift)", "Case B (weekly court date)"],
      "rows": [
        ["No extra expenditure to Government", "Yes", "Yes"],
        ["No other complications", "Yes: inquiry not linked to the shift", "No: weekly appearance in Delhi"],
        ["Decision", "Shift allowed if both are met", "Shift refused"]],
      "widths": [0.34, 0.33, 0.33]}],
   "narr": "Worked example: officer Lucknow mein posted hai aur medical grounds par Jaipur headquarters chahta hai. Case A mein dono conditions meet hoti hain, to shift allowed. Case B mein weekly court appearance ki complication hai, to refuse. Dono conditions alag-alag file par likhni chahiye.",
   "spk": "student"},

  {"chapter": "Section P", "tag": "SECTION P · VIGILANCE CLEARANCE · PURPOSE MAP",
   "title": "Vigilance clearance withheld during suspension: the purposes and the OMs the guide cites",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Purpose and guide OM (content NOT VERIFIED)",
      "headers": ["Purpose", "Guide's OM", "Status"],
      "rows": [
        ["Promotion", "22034/4/2012-Estt.(D) dated 02.11.2012", "Listed in Annexure row 17"],
        ["Empanelment; deputation; sensitive posts; training (except mandatory)", "11012/11/2007-Estt.(A) dated 14.12.2007", "Listed in Annexure row 16"],
        ["Passport", "11012/7/2017-Estt.A-III dated 18.02.2020", "Listed in Annexure row 24"],
        ["Private visit abroad", "11013/8/2015-Estt.A-III dated 27.07.2015", "Listed in Annexure row 22"]],
      "widths": [0.36, 0.42, 0.22]},
     {"kind": "callout", "color": "yellow", "text": "Mandatory training is an explicit exception to the training bar (NOT VERIFIED against the 2007 text)."}],
   "narr": "Vigilance clearance suspension mein chaar purposes ke liye rokti hai: promotion, empanelment aur deputation ya sensitive posts, training, passport, aur private visit abroad. Har purpose ka OM Annexure mein listed hai. Mandatory training ka exception guide mein hai, lekin 2007 OM ka text NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Section P", "tag": "SECTION P · GUIDE FIX · REVISED OMS",
   "title": "GUIDE FIX: vigilance clearance rules were revised in 2024 and 2025",
   "cards": [
     {"kind": "table", "color": "red", "title": "Revised instructions listed on DTF (titles checked; content NOT VERIFIED)",
      "headers": ["Date", "Subject (as listed)", "Status"],
      "rows": [
        ["09.10.2024", "Revised guidelines on vigilance clearance for AIS officers and Central Civil Services", "Title VERIFIED; content NOT VERIFIED"],
        ["06.02.2025", "Revised vigilance clearance guidelines for AIS officers and Central Civil Services", "Title VERIFIED; content NOT VERIFIED"]],
      "widths": [0.18, 0.56, 0.26]},
     {"kind": "row", "color": "green", "label": "Action", "text": "Use the 2025 OM for current clearance decisions. The guide's 2007 to 2020 list is out of date."}],
   "narr": "Guide mein vigilance clearance ki OMs 2007 se 2020 tak ki hain, lekin DTF ki list mein 2024 aur 2025 ke revised guidelines dikhte hain. Isliye current decision ke liye 2025 ka OM dekhna chahiye. Titles verified hain, lekin content abhi NOT VERIFIED hai.",
   "spk": "student"},
]

SCENES += [
  {"chapter": "Section Q", "tag": "SECTION Q · APPLICATIONS · PARA 15",
   "title": "Applications for another post: no consideration or forwarding while under suspension",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "Para 15, OM 02.01.2014 (text checked):", "text": "Application of a Government servant for appointment, whether by Direct Recruitment, transfer on deputation or transfer, to any other post should not be considered/forwarded if he is under suspension."},
     {"kind": "row", "color": "green", "label": "Three modes", "text": "Direct recruitment, deputation, and transfer. All three are blocked; the rule has no carve-out in the text."}],
   "narr": "Para 15 ke mutabik suspended officer ki koi bhi application, chahe direct recruitment ki ho, deputation ki ho ya transfer ki, consider ya forward nahi karni hai. Yeh text verified hai, aur isme koi carve-out nahi dikhta.",
   "spk": "teacher"},

  {"chapter": "Section R", "tag": "SECTION R · RESIGNATION · DEFAULT AND EXCEPTIONS",
   "title": "Resignation of a suspended officer: normally not accepted, with three exceptions",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Test and exceptions (as stated in the guide)",
      "headers": ["Point", "Rule", "Status"],
      "rows": [
        ["Test", "Public interest, with reference to the merits of the pending case", "NOT VERIFIED"],
        ["Default", "Normally not accepted, since suspension is for grave delinquency", "NOT VERIFIED"],
        ["Exception (i)", "Offence does not involve moral turpitude", "NOT VERIFIED"],
        ["Exception (ii)", "Evidence not strong enough for removal or dismissal", "NOT VERIFIED"],
        ["Exception (iii)", "Proceedings so long that accepting resignation is cheaper", "NOT VERIFIED"]],
      "widths": [0.20, 0.56, 0.24]},
     {"kind": "row", "color": "sky", "label": "Corroborated", "text": "OM 28034/4/94-Estt.(A) dated 31.05.1994, Annexure row 11, same subject. The 2014 Para 16(c) cross-reference is NOT VERIFIED."}],
   "narr": "Suspended officer ka resignation normally accept nahi hota, kyunki suspension aksar serious cases mein hota hai. Test public interest ka hai, merits ko dekh kar. Teen exceptions: moral turpitude nahi, evidence weak, aur proceedings itne lambe ki resignation sasta pade. Subject Annexure se match karta hai, lekin exceptions ka text NOT VERIFIED hai.",
   "spk": "student"},

  {"chapter": "Section R", "tag": "SECTION R · RESIGNATION · WORKED EXAMPLES",
   "title": "Worked examples: accept or reject, with reasons recorded on file",
   "cards": [
     {"kind": "table", "color": "purple", "title": "Three cases (guide examples)",
      "headers": ["Case", "Facts", "Decision"],
      "rows": [
        ["A", "Embezzlement; bank trail and two witnesses strong", "Reject: inquiry must finish"],
        ["B", "Single ambiguous noting; six years; officer 59", "Accept possible: exceptions (ii) and (iii)"],
        ["C", "Technical irregularity; no dishonesty", "Accept possible: exception (i)"]],
      "widths": [0.10, 0.52, 0.38]},
     {"kind": "callout", "color": "yellow", "text": "Each decision must record the exception and the public-interest reasoning on file."}],
   "narr": "Case A mein embezzlement hai aur evidence strong hai, to resignation reject hoga. Case B mein weak evidence aur lamba case hai, to accept possible. Case C mein technical irregularity hai, to exception (i) lagta hai. Har decision mein reasons file par likhna zaroori hai.",
   "spk": "teacher"},

  {"chapter": "Section S", "tag": "SECTION S · PROVISIONAL PENSION · RULE 8(4)(a)",
   "title": "Retirement during suspension: provisional pension up to the day before suspension",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "CCS (Pension) Rules 2021, Rule 8(4)(a) (text checked):", "text": "The provisional pension shall be equal to the maximum pension admissible on the basis of qualifying service up to the date of retirement, or if he was under suspension on the date of retirement, up to the date immediately preceding the date on which he was placed under suspension."},
     {"kind": "row", "color": "green", "label": "Status", "text": "VERIFIED. Gratuity is withheld until the proceedings conclude (Rule 8(4)(c))."}],
   "narr": "Agar officer suspension mein retire ho, to provisional pension milti hai. Yeh maximum pension hoti hai, jo suspension se pehle ki date tak ki qualifying service par banti hai. Rule 8(4)(a) ka text verified hai, aur gratuity proceedings ke khatam hone tak rukti hai.",
   "spk": "teacher"},

  {"chapter": "Section T", "tag": "SECTION T · COUNTING AS QUALIFYING SERVICE · RULE 23",
   "title": "Counting suspension as qualifying service: automatic in two cases, otherwise by declaration",
   "cards": [
     {"kind": "table", "color": "green", "title": "Rule 23, CCS (Pension) Rules 2021 (text checked)",
      "headers": ["Sub-rule", "Rule", "Status"],
      "rows": [
        ["(1)", "Counts if fully exonerated, or only a minor penalty and suspension held wholly unjustified", "VERIFIED"],
        ["(2)", "Otherwise does not count unless the competent authority expressly declares the extent", "VERIFIED"],
        ["(3)", "Competent authority must pass an order on the extent; definite entry in the service book", "VERIFIED"]],
      "widths": [0.14, 0.70, 0.16]}],
   "narr": "Rule 23 ke teen sub-rules hain. Sub-rule 1 mein automatic count hota hai, agar officer fully exonerated ho, ya sirf minor penalty ho aur suspension wholly unjustified ho. Sub-rule 2 mein baaki cases mein count nahi hota, jab tak declaration na ho. Sub-rule 3 mein har case mein order aur service book entry zaroori hai. Sab verified hai.",
   "spk": "student"},

  {"chapter": "Section T", "tag": "SECTION T · WORKED EXAMPLE",
   "title": "Worked example: a two-year suspension, counted or not counted",
   "cards": [
     {"kind": "table", "color": "purple", "title": "Two outcomes for the same two-year suspension",
      "headers": ["Outcome", "Sub-rule", "Count as qualifying service"],
      "rows": [
        ["Only a minor penalty; suspension held wholly unjustified", "(1)", "All two years count"],
        ["Major penalty; no express declaration", "(2)", "Zero, unless declared"],
        ["Major penalty; authority declares 50% extent", "(2) and (3)", "50% of the period, with written order and service-book entry"]],
      "widths": [0.46, 0.14, 0.40]},
     {"kind": "row", "color": "yellow", "label": "Order", "text": "Under (3), a written order and service-book entry are needed in every case, count or not."}],
   "narr": "Worked example: do saal ki suspension. Agar sirf minor penalty hai aur suspension wholly unjustified hai, to poore do saal count honge. Agar major penalty hai aur declaration nahi, to zero. Agar authority 50 percent declare kare, to order aur service book entry chahiye. Yeh sub-rules 1 se 3 ke saath match karta hai.",
   "spk": "teacher"},

  {"chapter": "Section U", "tag": "SECTION U · VRS · FR 56(k), FR 56(m), RULE 43(3)",
   "title": "Voluntary retirement during suspension: the appropriate authority can withhold permission",
   "cards": [
     {"kind": "row", "color": "sky", "label": "Guide claim", "text": "The appropriate authority may withhold permission for a suspended officer seeking retirement under FR 56(k), FR 56(m) or Rule 43(3) of the 2021 Pension Rules."},
     {"kind": "table", "color": "orange", "title": "Status of each reference",
      "headers": ["Reference", "Status"],
      "rows": [
        ["Rule 43(3), CCS (Pension) Rules 2021", "PARTLY VERIFIED (secondary source: suspension, charge-sheet or judicial case bars acceptance unless President approves)"],
        ["FR 56(k) and FR 56(m)", "NOT VERIFIED (amendment notification 17.01.2014 not fetched)"]],
      "widths": [0.34, 0.66]}],
   "narr": "VRS ke liye guide kehta hai ki appropriate authority permission withhold kar sakti hai. Rule 43(3) ke baare mein secondary source se lagta hai ki suspension mein bina President ki approval ke acceptance nahi hota. FR 56(k) aur 56(m) ka 2014 notification NOT VERIFIED hai.",
   "spk": "student"},

  {"chapter": "Section V", "tag": "SECTION V · PAY AFTER REVOCATION · FR 54-B(1)",
   "title": "After revocation or reinstatement: a specific order on pay and on duty status is mandatory",
   "cards": [
     {"kind": "steps", "color": "green", "steps": ["Officer is reinstated, or would have been but for retirement", "Authority competent to reinstate passes a specific order", "Limb (a): pay and allowances for the suspension period", "Limb (b): whether the period counts as duty", "Outcomes in Section W are applied through this order"]},
     {"kind": "row", "color": "orange", "label": "Status", "text": "FR 54-B(1) text NOT VERIFIED (not fetched). The two-limb structure matches the 2022 document's heading (V)."}],
   "narr": "Revocation ya reinstatement ke baad authority ko specific order banana hai. Do limbs hain: suspension period ka pay aur allowances, aur period duty maana jaayega ya nahi. Yeh order Section W ke outcomes ka gateway hai. FR 54-B(1) ka text NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Section V", "tag": "SECTION V · WORKED EXAMPLE",
   "title": "Worked example: two limbs for a 14-month suspension and a superannuated officer",
   "cards": [
     {"kind": "table", "color": "purple", "title": "What the order must say",
      "headers": ["Officer", "Limb (a): pay", "Limb (b): duty?"],
      "rows": [
        ["Mr P, reinstated after 14 months, exonerated", "Full pay and allowances", "Treated as duty for all purposes"],
        ["Mrs Q, retired during suspension", "Still needs FR 54-B(1) order", "Heirs' and pension case depend on it"]],
      "widths": [0.40, 0.30, 0.30]},
     {"kind": "callout", "color": "red", "text": "Reinstated with no specific order is a defect in audit and appeal."}],
   "narr": "Mr P 14 mahine ke baad reinstate hua, aur exonerate hua. Order mein full pay aur duty dono likhne hain. Mrs Q retire ho gayi, phir bhi FR 54-B(1) ka order chahiye, kyunki uske heirs ka case isi par tika hai. Specific order na ho to audit mein defect hota hai.",
   "spk": "student"},

  {"chapter": "Section W", "tag": "SECTION W · OUTCOME · EXONERATED",
   "title": "Outcome: exonerated means full pay if suspension was wholly unjustified, with a delay haircut",
   "cards": [
     {"kind": "table", "color": "green", "title": "Exonerated (FR 54-B(3) and (4); sub-limbs not individually verified)",
      "headers": ["Element", "Rule as stated", "Status"],
      "rows": [
        ["Full pay", "Where suspension is wholly unjustified", "PARTLY VERIFIED"],
        ["Reduced amount", "Where delay is due to the officer; after notice and representation", "PARTLY VERIFIED"],
        ["Duty status", "Period treated as duty for all purposes", "PARTLY VERIFIED"]],
      "widths": [0.22, 0.56, 0.22]}],
   "narr": "Exonerated hone par, agar suspension wholly unjustified tha, to full pay aur allowances mil sakte hain. Lekin agar delay officer ki wajah se hua, to notice aur representation ke baad reduced amount ho sakta hai. Duty status ka rule bhi hai. FR 54-B(3) aur (4) ke sub-limbs ko partly verify kiya gaya hai.",
   "spk": "teacher"},

  {"chapter": "Section W", "tag": "SECTION W · OUTCOME · MINOR PENALTY AND OTHERS",
   "title": "Minor penalty means full pay; other outcomes need notice, duty order, and a floor",
   "cards": [
     {"kind": "table", "color": "sky", "title": "Minor penalty and other outcomes",
      "headers": ["Outcome", "Rule", "Status"],
      "rows": [
        ["Only minor penalty", "Suspension treated as wholly unjustified; full pay (1985 OM, date and text not verified)", "PARTLY VERIFIED"],
        ["Other outcomes", "Amount fixed after notice and representation (FR 54-B(5))", "PARTLY VERIFIED"],
        ["Duty status (other)", "Not duty unless specifically directed", "PARTLY VERIFIED"],
        ["Option to convert", "Leave of kind due; may exceed 3 months (temporary) or 5 years (permanent)", "VERIFIED (FR 54-B(7))"],
        ["Floor", "Not less than subsistence already paid", "VERIFIED (FR 54-B(9))"]],
      "widths": [0.22, 0.56, 0.22]}],
   "narr": "Sirf minor penalty ho to suspension wholly unjustified treat hota hai, aur full pay milta hai. Other outcomes mein amount notice aur representation ke baad tay hota hai, aur duty status specifically direct karne par hi milta hai. Leave conversion ki ceilings aur subsistence ka floor verified hain.",
   "spk": "student"},

  {"chapter": "Section W", "tag": "SECTION W · WORKED EXAMPLES",
   "title": "Worked examples: delay haircut, minor penalty arrears, and the subsistence floor",
   "cards": [
     {"kind": "table", "color": "purple", "title": "Three guide cases, arithmetic checked where numbers are given",
      "headers": ["Case", "Facts", "Result"],
      "rows": [
        ["Mr D", "Exonerated after 18 months; 6 months of delay due to his adjournments", "Full pay, with the 6-month part reduced after notice"],
        ["Ms E", "Only censure after 10 months' suspension", "Full pay for 10 months; differential arrears over subsistence paid"],
        ["Mr F", "Compulsory retirement; authority fixes 60% of pay; Rs 40,000 subsistence paid per month", "Amount cannot fall below subsistence paid; conversion to leave possible"]],
      "widths": [0.12, 0.50, 0.38]}],
   "narr": "Mr D ka case: exonerated, lekin 6 mahine ki delay uski wajah se, to us part ka amount reduce ho sakta hai. Ms E ka case: sirf censure, to 10 mahine ki full pay, subsistence ke upar arrears. Mr F ka case: compulsory retirement, 60 percent amount, lekin floor subsistence ka hai. Teeno guide examples hain.",
   "spk": "teacher"},

  {"chapter": "Section X", "tag": "SECTION X · DEATH · FR 54-B(2)",
   "title": "Death during suspension: family gets full pay for the period, minus subsistence paid",
   "cards": [
     {"kind": "quote", "color": "cyan", "label": "FR 54-B(2) (text checked, DoPT document):", "text": "Where a Government servant under suspension dies before the disciplinary or court proceedings are concluded, the period between the date of suspension and the date of death shall be treated as duty for all purposes, and his family shall be paid the full pay and allowances, subject to adjustment of subsistence allowance already paid."},
     {"kind": "table", "color": "purple", "title": "Worked arithmetic (checked)",
      "headers": ["Step", "Calculation", "Result"],
      "rows": [
        ["Full pay entitlement, 8 months", "8 x Rs 90,000", "Rs 7,20,000"],
        ["Subsistence already paid", "8 x Rs 50,000", "Rs 4,00,000"],
        ["Arrears to family", "7,20,000 minus 4,00,000", "Rs 3,20,000"]],
      "widths": [0.40, 0.34, 0.26]}],
   "narr": "Death ke case mein period duty maana jaata hai, aur family ko full pay milti hai, jo subsistence ke adjustment ke baad bachti hai. Example: 8 mahine, 90,000 ka full pay, aur subsistence 50,000 paid. Arrears 3,20,000 rupees. Arithmetic check ho gaya, aur text verified hai.",
   "spk": "student"},

  {"chapter": "Section Y", "tag": "SECTION Y · CHARGE-SHEET WITHIN THREE MONTHS",
   "title": "Contemplated proceedings: charge-sheet within three months, or reasons immediately after",
   "cards": [
     {"kind": "steps", "color": "green", "steps": ["(a) Order normally states the grounds", "(b) Ground is contemplated proceedings: serve charge-sheet within 3 months", "(c) No charge-sheet by then: reasons communicated immediately on expiry of 3 months", "2022 caps: a charge-sheet switches off the caps for no-charge-sheet cases"]},
     {"kind": "row", "color": "orange", "label": "OM citation", "text": "Guide cites OM 35014/1/81 dated 09.11.1982. Annexure row 6 describes that OM as the appeal opportunity. The mapping is NOT VERIFIED."}],
   "narr": "Contemplated proceedings par suspension hua ho, to teen mahine mein charge-sheet deni hai. Agar nahi di, to teen mahine khatam hote hi reasons turant communicate karne hain. Subclauses (b) aur (c) ka text verified hai. Lekin guide ne jo OM number cite kiya hai, woh Annexure mein appeal ka OM hai, isliye mapping NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Section Y", "tag": "SECTION Y · WORKED EXAMPLE · TWO WALLS",
   "title": "Worked example: the 3-month reasons wall and the charge-sheet wall run together",
   "cards": [
     {"kind": "table", "color": "purple", "title": "Suspension on 1 October, contemplated proceedings",
      "headers": ["Deadline", "Requirement", "Date (convention NOT VERIFIED)"],
      "rows": [
        ["Charge-sheet (Y(b))", "Serve within 3 months", "31 Dec (guide); 1 Jan under another convention"],
        ["Reasons (G)", "Communicate if not in order", "Same window"],
        ["If no charge-sheet", "Reasons immediately on expiry (Y(c))", "Caps apply under Rule 10(7)"]],
      "widths": [0.26, 0.38, 0.36]},
     {"kind": "callout", "color": "yellow", "text": "Mark the earlier date in the file diary. Do not rely on a day count that is not verified."}],
   "narr": "1 October ka suspension, contemplated proceedings. Charge-sheet aur reasons, dono ki 3 mahine ki deadline hai. Guide 31 December kehta hai, lekin 1 January bhi convention ho sakta hai. Isliye earlier date file mein mark karein. Agar charge-sheet na ho, to 2022 ke caps lagte hain.",
   "spk": "student"},

  {"chapter": "Section Z", "tag": "SECTION Z · APPEAL AGAINST SUSPENSION",
   "title": "Appeal against a suspension order: Rule 23, 45 days, and the appellate authority",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Appeal route (status by item)",
      "headers": ["Item", "Rule", "Status"],
      "rows": [
        ["Right of appeal", "Rule 23 of CCS (CCA) Rules 1965 (guide: sub-rule (i))", "PARTLY VERIFIED (secondary source: Rule 23)"],
        ["Appellate authority", "Rule 24", "NOT VERIFIED"],
        ["Time limit", "45 days (Rule 25); count from reasons communicated", "PARTLY VERIFIED (45 days)"],
        ["Form and copy", "Rule 26; copy to DA; no disrespectful language", "NOT VERIFIED"]],
      "widths": [0.22, 0.52, 0.26]}],
   "narr": "Suspension order ke against appeal ho sakti hai, Rule 23 ke under. Appellate authority Rule 24 mein hai, aur time limit 45 din ki hai. Secondary source se 45 din verified hai, lekin sub-rule, Rule 24, aur Rule 26 ka form NOT VERIFIED hain. Form mein copy DA ko jaane ki guide ki baat NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Section Z", "tag": "SECTION Z · GUIDE FIX · 45-DAY DATE",
   "title": "GUIDE FIX: 45 days from 1 July ends on 15 August, not 14 August",
   "cards": [
     {"kind": "table", "color": "red", "title": "Arithmetic check (day 0 = 1 July)",
      "headers": ["Step", "Date", "Status"],
      "rows": [
        ["Order received", "1 July", "Start"],
        ["Day 30", "31 July", "Arithmetic VERIFIED"],
        ["Day 45", "15 August", "Corrected: guide said 14 August"],
        ["Start convention", "Receipt or communication date (NOT VERIFIED)", "Confirm before filing"]],
      "widths": [0.26, 0.40, 0.34]},
     {"kind": "row", "color": "sky", "label": "Note", "text": "The guide's own worked example is otherwise internally consistent."}],
   "narr": "Guide mein 1 July se 45 din ka deadline 14 August likha hai. Arithmetic ke mutabik 1 July se 45 din baad 15 August hota hai. Ye GUIDE FIX hai. Lekin start date kaunsi hogi, receipt ya communication, yeh convention NOT VERIFIED hai, isliye confirm karna chahiye.",
   "spk": "student"},
]

SCENES += [
  {"chapter": "Annexure", "tag": "ANNEXURE · RULES AND OMS 1 TO 9",
   "title": "Annexure, part 1: rules and OMs 1 to 9, with status against each row",
   "cards": [
     {"kind": "table", "color": "sky", "title": "OMs and notifications (1 to 9)",
      "headers": ["No.", "OM number and date", "Subject (short)", "Status"],
      "rows": [
        ["1", "39/59/54-Ests.(A) 25.02.1955", "Arrest on criminal charge: intimate superiors", "PARTLY VERIFIED"],
        ["2", "39/5/56-Ests.(A) 08.09.1956", "HQ of suspended officer (clarification)", "NOT VERIFIED"],
        ["3", "7/4/74-Ests.(A) 09.08.1974", "Field supervisors: empowerment, one-month check", "PARTLY VERIFIED"],
        ["4", "11012/24/77-Estt.(A) 18.03.1978", "Scope of Rule 10(4)", "NOT VERIFIED"],
        ["5", "21011/2/78-Estt.(A) 01.08.1978", "CR writing by suspended officers", "NOT VERIFIED"],
        ["6", "35014/1/81-Estt.(A) 09.11.1982", "Opportunity to appeal against suspension", "PARTLY VERIFIED"],
        ["7", "11012/15/85-Estt.(A) 03.12.1985", "Minor penalty: duty and full pay (JCM)", "PARTLY VERIFIED"],
        ["8", "11012/8/87-Estt.(A) 22.06.1987", "Dowry death suspension", "PARTLY VERIFIED"],
        ["9", "28034/25/87-Estt.(A) 11.02.1988", "Resignation from service: procedure", "NOT VERIFIED"]],
      "widths": [0.07, 0.36, 0.40, 0.17]}],
   "narr": "Annexure ka pehla part rows 1 se 9 tak hai. Row 1 se 9 mein verified kuch nahi hai poori tarah, zyadatar sirf partly verified hain, kyunki unke subject ya date secondary sources se match hote hain. Row 3 ka one-month check 2022 document ke footnote se bhi support hota hai. Row 6 ka subject appeal ka hai, isliye Section Y ka mapping NOT VERIFIED hai.",
   "spk": "teacher"},

  {"chapter": "Annexure", "tag": "ANNEXURE · RULES AND OMS 10 TO 17",
   "title": "Annexure, part 2: OMs 10 to 17, with status and the clearance update",
   "cards": [
     {"kind": "table", "color": "sky", "title": "OMs (10 to 17)",
      "headers": ["No.", "OM number and date", "Subject (short)", "Status"],
      "rows": [
        ["10", "22011/4/91-Estt.(A) 14.09.1992", "Promotion while proceedings pending: sealed cover", "NOT VERIFIED"],
        ["11", "28034/4/94-Estt.(A) 31.05.1994", "Acceptance of resignation of suspended officer", "NOT VERIFIED"],
        ["12", "21011/8/2000-Estt.(A) 25.10.2000", "ACR writing by suspended officers: major-part bar", "NOT VERIFIED"],
        ["13", "11012/8/2003-Estt.(A) 23.10.2003", "Deemed suspension: Rajiv Kumar decision", "NOT VERIFIED"],
        ["14", "11012/4/2003-Estt.(A) 07.01.2004", "Review Committee; one-year rule", "VERIFIED"],
        ["15", "11012/4/2003-Estt.(A) 19.03.2004", "Follow-up review instruction", "NOT VERIFIED"],
        ["16", "11012/11/2007-Estt.(A) 14.12.2007", "Vigilance clearance guidelines (superseded in part, 2024 to 2025)", "NOT VERIFIED"],
        ["17", "22034/4/2012-Estt.(D) 02.11.2012", "Vigilance clearance for promotion (superseded in part, 2024 to 2025)", "NOT VERIFIED"]],
      "widths": [0.07, 0.36, 0.40, 0.17]}],
   "narr": "Row 10 se 17 tak sirf row 14, yaani 7 January 2004 ka OM, verified hai. Row 10, 11, 12 aur 13 ke text NOT VERIFIED hain. Row 16 aur 17 ke clearance OMs ko 2024 aur 2025 ke revised guidelines ne update kiya hai, isliye unhe current rule ki tarah na padhein.",
   "spk": "student"},

  {"chapter": "Annexure", "tag": "ANNEXURE · RULES AND OMS 18 TO 25",
   "title": "Annexure, part 3: OMs 18 to 25, including the 2022 notification that ties the caps together",
   "cards": [
     {"kind": "table", "color": "sky", "title": "OMs and notifications (18 to 25)",
      "headers": ["No.", "OM or notification", "Subject (short)", "Status"],
      "rows": [
        ["18", "11012/17/2013-Estt.(A) 02.01.2014", "Consolidated instructions on suspension", "VERIFIED"],
        ["19", "25013/3/2010-Estt.(A-IV) 17.01.2014", "Amendment to FR 56(k) and FR 56(m)", "NOT VERIFIED"],
        ["20", "11012/17/2013-Estt.(A) 18.11.2014", "Timely review of suspension", "PARTLY VERIFIED"],
        ["21", "11012/17/2013-Estt.(A) 03.07.2015", "Timely issue of charge-sheet", "NOT VERIFIED"],
        ["22", "11013/8/2015-Estt.A-III 27.07.2015", "Prior permission to go abroad", "NOT VERIFIED"],
        ["23", "11012/04/2016-Estt.(A) 23.08.2016", "Timely issue of charge-sheet (repeat)", "NOT VERIFIED"],
        ["24", "11012/7/2017-Estt.A-IIII 18.02.2020", "Vigilance clearance for passport (guide typo: A-IIII)", "NOT VERIFIED"],
        ["25", "11012/04/2016, notified 19.10.2022; GSR 156 dated 22.10.2022", "Amendment of Rule 10(7) (caps)", "VERIFIED"]],
      "widths": [0.07, 0.40, 0.36, 0.17]}],
   "narr": "Row 18 ka consolidated OM verified hai. Row 25 wali notification bhi verified hai, jisme 19.10.2022 notify hua aur GSR 156 gazette mein 22.10.2022 ko dated hai. Row 20 ki date partly verified hai. Baaki rows, jaise charge-sheet timing aur passport OM, NOT VERIFIED hain. Row 24 mein guide ka typo A-IIII bhi hai.",
   "spk": "teacher"},

  {"chapter": "Corrections", "tag": "GUIDE FIX · PART 1 · SECTIONS C TO F",
   "title": "GUIDE FIX: corrections made in this video, part 1",
   "cards": [
     {"kind": "table", "color": "red", "title": "Errors in the uploaded guide (Sections C to F)",
      "headers": ["Section", "Guide said", "Corrected to"],
      "rows": [
        ["C", "'civil/polio-type detention' (garbled)", "Detention on a criminal charge or otherwise (Rule 10(2)(a))"],
        ["C", "Worked Example 3: unclosed parenthesis", "Typo; no legal effect"],
        ["D", "Misdemeanours labelled v(a) to (e)", "Note (b)(i) to (v) of OM 02.01.2014"],
        ["E", "304-B IPC; 173(2) CrPC", "Section 80 BNS; Section 193 BNSS (from 01.07.2024)"],
        ["F", "C&AG exception: IA&AS and AAG only", "Adds General Central Service Group A (notification 12.01.2026)"],
        ["F", "Confirmation void if not by 31 May (order 5 May)", "One month from order date: 5 June"]],
      "widths": [0.10, 0.42, 0.48]}],
   "narr": "Guide ki galtiyan. Section C mein garbled phrase, aur ek typo. Section D mein misdemeanour list ke labels. Section E mein IPC aur CrPC ki jagah BNS aur BNSS. Section F mein 2026 ka C&AG proviso update, aur confirmation ka example, jisme 31 May ki jagah 5 June sahi deadline hai.",
   "spk": "student"},

  {"chapter": "Corrections", "tag": "GUIDE FIX · PART 2 · SECTIONS H TO Z",
   "title": "GUIDE FIX: corrections made in this video, part 2",
   "cards": [
     {"kind": "table", "color": "red", "title": "Errors and currency points (Sections F to Annexure)",
      "headers": ["Section", "Guide said", "Corrected to"],
      "rows": [
        ["F", "Hinglish: 'char_monthbuffer' (garbled)", "Plain wording used in the video"],
        ["H", "GSR 156 'dated 19.10.2022'", "Notification dated 19.10.2022; gazette GSR 156 dated 22.10.2022"],
        ["P", "Vigilance OMs of 2007 to 2020 only", "Revised OMs of 09.10.2024 and 06.02.2025 also apply"],
        ["Z", "45 days from 1 July: 14 August", "15 August (day-count convention NOT VERIFIED)"],
        ["Annex", "Row 24 'Estt.A-IIII'", "Typo in the guide; not corrected in the source"],
        ["Whole", "Updated 04.11.2022; compiled 'July 2026'", "Read with the 12.01.2026 notification"]],
      "widths": [0.10, 0.42, 0.48]}],
   "narr": "Guide ki baaki galtiyan. Hinglish ka garbled phrase, Section H mein gazette ki date, Section P ka purana clearance list, Section Z mein 45 din ki date, aur Annexure ka typo. Sabse bada point yeh hai ki guide 2022 ka hai, aur 2026 ke amendment ke saath padhna zaroori hai.",
   "spk": "teacher"},

  {"chapter": "Not Verified", "tag": "NOT VERIFIED · PART 1",
   "title": "NOT VERIFIED list, part 1: text, citation and scope items",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Items to confirm before use",
      "headers": ["No.", "Item", "Why not verified"],
      "rows": [
        ["N1", "Exact new Rule 10(1) proviso and Rule 12(4)(a) wording (12.01.2026)", "Gazette OCR partly illegible; title says 'Amendment Rules, 2025'"],
        ["N2", "Arrest intimation OM (25.02.1955) text", "Subject and date only, from secondary sources"],
        ["N3", "HQ OM (08.09.1956); Rule 10(4) OM (18.03.1978)", "Listed in Annexure; text not fetched"],
        ["N4", "Rajiv Kumar citation (2003 (5) SCALE 297) and 23.10.2003 OM", "Search shows (2003) 6 SCC 516 for the case name"],
        ["N5", "Para 4(ii) and (iii) wording (2014 OM)", "Source text partly garbled"],
        ["N6", "Dowry OM 22.06.1987 number and text", "Annexure only"],
        ["N7", "Sealed-cover OM 14.09.1992 and its Para 11 cross-reference", "Not fetched"],
        ["N8", "ACR OMs of 1978 and 2000 (window and bar)", "Not fetched"],
        ["N9", "LTC Para 12; hospitalisation leave claim", "Paragraph number and claim not verified"]],
      "widths": [0.08, 0.50, 0.42]}],
   "narr": "NOT VERIFIED list ka pehla part. Pehla item 2026 ka notification ka exact wording hai, jo gazette mein partly illegible hai. Phir arrest, HQ, Rule 10(4) ke OMs, Rajiv Kumar ka citation, Para 4 ka partly garbled wording, dowry OM ka number, sealed cover, ACR, aur LTC wale items. Inhe bill ya file mein use karne se pehle confirm karein.",
   "spk": "student"},

  {"chapter": "Not Verified", "tag": "NOT VERIFIED · PART 2",
   "title": "NOT VERIFIED list, part 2: pay, appeal, clearance and day-count items",
   "cards": [
     {"kind": "table", "color": "orange", "title": "Items to confirm before use",
      "headers": ["No.", "Item", "Why not verified"],
      "rows": [
        ["N10", "Resignation OM (31.05.1994) text, three exceptions, Para 16(c)", "Not fetched"],
        ["N11", "Vigilance clearance OM texts (2007 to 2020) and 2024 to 2025 revisions", "Titles seen; content not read"],
        ["N12", "Mandatory-training exception in the 2007 clearance OM", "Not fetched"],
        ["N13", "FR 54-B(1), (3), (4), (5) sub-limbs; 1985 minor-penalty OM date", "Only (7) and (9) checked in text"],
        ["N14", "FR 53(1)(ii)(b) text; 'not to be made' recovery list", "Not fetched in full"],
        ["N15", "Rule 43(3); FR 56(k), (m); notification 17.01.2014", "Secondary source only"],
        ["N16", "Rule 23(i), Rule 22(ii), Rule 24, Rule 26; appeal start date", "Secondary source only; Rule 25 45 days partly"],
        ["N17", "Day-count conventions (90 days, 3 months, 1 month, 45 days)", "Convention not stated in the rules"],
        ["N18", "DA at 50% in the subsistence example; Rule 10(3) paraphrase", "Assumption and guide paraphrase"]],
      "widths": [0.08, 0.52, 0.40]}],
   "narr": "NOT VERIFIED list ka doosra part. Resignation ka text, vigilance clearance ka content, mandatory training exception, FR 54-B ke sub-limbs, FR 53 ki other allowances aur recovery list. Phir Rule 43(3), FR 56, appeal ke rules, aur day-count conventions. Akhri item DA ka 50 percent assumption aur Rule 10(3) ka paraphrase hai.",
   "spk": "teacher"},

  {"chapter": "Close", "tag": "CLOSE · SUMMARY",
   "title": "Summary: what is verified, what changed, and what to check before any use",
   "cards": [
     {"kind": "stat", "color": "green", "head": "VERIFIED", "sub": "Core rules: 10(1), 10(2), 10(4), 10(5), 10(6), 10(7) caps, FR 53(2), FR 54-B(2), (7), (9), Rule 8(4)(a), Rule 23, OM 02.01.2014 paras"},
     {"kind": "stat", "color": "orange", "head": "2026 UPDATE", "sub": "Rule 10(1) proviso: General Central Service Group A added"},
     {"kind": "stat", "color": "red", "head": "GUIDE FIX", "sub": "Garbled phrase, Note labels, BNS and BNSS, 31 May and 14 August dates, currency"},
     {"kind": "row", "color": "sky", "label": "Next", "text": "Confirm the 12.01.2026 gazette wording first. Then confirm the NOT VERIFIED list before any file or bill."}],
   "narr": "Summary. Core rules verified hain: 10(1), 10(2), 10(4), 10(5), 10(6), aur 10(7) ke 2022 caps. FR 53(2), FR 54-B ke kuch parts, Rule 8(4)(a), Rule 23 aur OM 2014 ke paras verified hain. 2026 ka update Rule 10(1) mein General Central Service Group A ko add karta hai. Guide ki galtiyan fix ho gayi hain, aur NOT VERIFIED list pehle gazette aur OM text se confirm karein.",
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
    ap.add_argument("--plan", action="store_true")
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

    if args.plan:
        import json
        plan = {str(i): {"spk": sc["spk"], "narr": sc["narr"], "title": sc["title"],
                         "cards": [c["kind"] for c in sc["cards"]]} for i, sc in enumerate(SCENES)}
        PLAN_JSON.parent.mkdir(parents=True, exist_ok=True)
        PLAN_JSON.write_text(json.dumps(plan, ensure_ascii=False, indent=1))
        print(f"wrote {PLAN_JSON}  ({len(plan)} scenes)")
        return 0

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
        out = ["# Suspension — DoPT Information Document (04.11.2022) with 2026 update: card reference sheet", "",
               "Source: DoPT Information Document on Suspension (updated 04.11.2022); DoPT notification dated 12.01.2026 (G.S.R. 21(E)). Narration is Hinglish; this sheet is English only.", ""]
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
