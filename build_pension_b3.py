#!/usr/bin/env python3
"""
CCS (Pension) Rules 2021 - Batch 3 - Rules 31 to 41
DASHBOARD EXPLAINER COMPILER - English board, Hinglish voice
=============================================================
32 chapters | 130 cards | 134 provisions tracked | 5116 spoken words
Board language: English. Narration language: Hinglish (Roman script only, no Devanagari anywhere).
Visual target: the studio dashboard in the reference frame - meta strip, violet code pill, panel
title, four accent tiles, labelled ledger rows, one amber takeaway row and an amber trap band,
with burned-in Hinglish subtitles over the progress bar.

WHAT WAS AUDITED THIS ROUND
  Rule-by-rule audit of Rules 31 to 41 against the VERBATIM Gazette text of the CCS (Pension)
  Rules, 2021, read from a CAG-hosted copy of the Gazette notification (gazette pages carrying
  Chapter IV and Chapter V), not from a page-summarising tool. Every sub-rule, clause, proviso
  and Explanation from Rule 31(1) to Rule 41(6) is tracked in PROVISIONS below and printed by
  --audit, with a status of COVERED, FIXED (added or rewritten this round), OPEN (still needs the
  document itself) or EXTERNAL (belongs to Batch 4).

  Defects found in the previous build and repaired here:
   1. Rule 31(3) was reduced to "a higher appointment during leave" and dropped the certificate
      that the servant would have continued in the higher post but for the leave.
   2. Rule 31(6) dropped the Armed Forces limb and the whole proviso on leave after release from
      an ex-cadre post.
   3. Rule 31(8) and 31(9) were single words ("re-employed pensioner", "converted PSU"); the
      pension-element condition in (8) and the retain-the-benefits OPTION in (9) were missing.
   4. Rules 37(30)-(31), 38(26)-(29) were absent: the 51% disinvestment safeguards and the
      Prasar Bharati carve-out (38(29)) had no card at all.
   5. Four cards carried "not confirmed" flags that the Gazette text settles: 37(2) two clocks,
      39(4) both ages, 39(9) before or after appointment, 40(2) original/appellate/review.
   6. The renderer and the data disagreed about tuple width; the card tuple is now fixed at
      (title, short, full, colour, narration) everywhere and asserted at import.

  Six new chapters close the gaps: 26 Rule 31 conditions, 27 Rule 32 fractions (table),
  28 Rules 37(30)-(31) and 38(26)-(29) (the clauses nobody quotes), 29 four flags closed (table),
  30 Rules 35/36/37/38 on one grid (table), 31 two-thirds floor vs ceiling (chart).

LANGUAGE POLICY
  On screen: English, Indian urban register, short labelled phrases.
  Spoken: Hinglish in Roman script ("Rule thirty-one, sub rule teen me ek condition chhupi hai").
  Subtitles: the spoken Hinglish, cut from the neural voice word boundaries.
  The TTS normaliser leaves Roman Hinglish alone and only rewrites references and acronyms.

SOURCES
  * Gazette text of Rules 31-41: https://agwb.cag.gov.in/files/agae/circular_order/Circular_CCS_Pension_Rules_2021.pdf
  * G.S.R. 868(E) of 20.12.2021 (notification), G.S.R. 340(E) of 22.05.2025 (Rule 37(29)(c)),
    G.S.R. 775(E) of 02.09.2026 (Rule 37(7) proviso, read in full), O.M. of 30.10.2025
    F.No. 38/10(03)/2025-P&PW(A), DoPT O.M. 25013/6/2001-Estt.(A) of 28.02.2002 (Special VRS).
  * Figures not re-read this round: Rs 9,000 minimum, Rs 1,25,000 maximum, Rs 54,000 medical
    threshold. Quote them with the date of the O.M. you rely on.

TOOLING
  ffmpeg is taken from PATH, and if it is absent the static binary shipped by the
  `imageio-ffmpeg` wheel is used (ffmpeg 7.0.2 static does carry the subtitles filter).
  ffprobe is optional: when it is missing, durations are parsed out of ffmpeg's own
  progress report, so clip timing still matches the audio exactly.
  Voices are `edge-tts` (en-IN-PrabhatNeural teacher, en-IN-NeerjaNeural student) and it
  needs outbound HTTPS to speech.platform.bing.com. If that is blocked the build stops
  with a clear message instead of quietly shipping a silent film - ask for --no-tts if a
  silent rehearsal is what you actually want.

CAPTIONS
  --captions burn (default) draws the Hinglish subtitle into the picture with libass.
  --captions soft muxes the same cues as a movable subtitle track.
  --captions none leaves them out; the board then draws the line itself in a lower third.

USAGE
    python build_pension_b3.py --verify      # which ffmpeg / ffprobe / libass this build gets
    python build_pension_b3.py --audit       # density + provision matrix, no ffmpeg, no internet
    python build_pension_b3.py --preview     # one PNG per scene
    python build_pension_b3.py --no-tts      # silent dry run with real layout and timing
    python build_pension_b3.py --part 2      # middle third of the chapters
    python build_pension_b3.py --layout table  # force one layout everywhere
    python build_pension_b3.py --only c3_13_rule37_chain
    python build_pension_b3.py --captions soft
    python build_pension_b3.py               # full build (edge-tts + ffmpeg with libass)
"""
import argparse
import asyncio
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


# ============================================================================
# TOOLING: ffmpeg / ffprobe discovery
# Works with a system ffmpeg + ffprobe pair, or with the static ffmpeg that the
# `imageio-ffmpeg` wheel ships (7.0.2 static does carry the subtitles filter).
# ============================================================================
def _resolve_ffmpeg():
    exe = shutil.which("ffmpeg") or shutil.which("ffmpeg.exe")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"


def _resolve_ffprobe(ffmpeg_exe):
    exe = shutil.which("ffprobe") or shutil.which("ffprobe.exe")
    if exe:
        return exe
    guess = str(Path(ffmpeg_exe).with_name("ffprobe"))
    return guess if Path(guess).exists() else None


FFMPEG = _resolve_ffmpeg()
FFPROBE = _resolve_ffprobe(FFMPEG)
HAVE_SUBTITLE_FILTER = True      # set for real by probe_ffmpeg()


def probe_ffmpeg():
    """Returns (ok, has_subtitles, message). Never raises."""
    global HAVE_SUBTITLE_FILTER
    try:
        out = subprocess.run([FFMPEG, "-hide_banner", "-filters"],
                             capture_output=True, text=True, timeout=90).stdout
    except Exception as e:
        return False, False, f"ffmpeg not runnable ({FFMPEG}): {e}"
    HAVE_SUBTITLE_FILTER = "subtitles" in out
    return True, HAVE_SUBTITLE_FILTER, FFMPEG


# ============================================================================
# CANVAS / BUILD CONFIG
# ============================================================================
W, H = 1920, 1080
BUILD_DIR = Path("pension_b3_build")
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
OUT_STEM = "pension_b3_masterclass"
OUTPUT_MP4 = Path(OUT_STEM + ".mp4")
REFERENCE_SHEET = Path("pension_b3_reference_sheet.md")

# Density budget (px). The build fails rather than shrinking below these.
ROW_BODY_START, ROW_BODY_MIN = 30, 21
ROW_LABEL_START, ROW_LABEL_MIN = 30, 20
TILE_TITLE_START, TILE_TITLE_MIN = 34, 22
TABLE_START, TABLE_MIN = 26, 16
PANEL_TITLE_START, PANEL_TITLE_MIN = 50, 30

# Screenshot palette (deep indigo board, cyan / amber / green / violet accents)
BG_TOP = (9, 11, 30)
BG_BOT = (22, 22, 54)
GLOW_A = (58, 34, 108)
GLOW_B = (16, 40, 92)
CARD_BG = (20, 24, 44)
CARD_BG_2 = (26, 31, 54)
TEXT_WHITE = (244, 246, 252)
MUTED = (150, 160, 186)
FAINT = (90, 100, 126)
ORANGE = (232, 162, 32)
GREEN = (34, 176, 132)
BLUE = (86, 140, 240)
SKY = (86, 196, 232)
RED = (236, 112, 74)
YELLOW = (238, 214, 92)
PINK = (206, 132, 200)
VIOLET = (150, 130, 240)

ACCENTS = (ORANGE, GREEN, BLUE, SKY, RED, YELLOW, PINK, VIOLET)
LIGHT_ACCENTS = (ORANGE, GREEN, SKY, YELLOW)          # dark text sits on these
TEXT_ON_LIGHT = (12, 14, 30)

DEFAULT_TEACHER = "en-IN-PrabhatNeural"
DEFAULT_STUDENT = "en-IN-NeerjaNeural"
DEFAULT_RATE = "+6%"

# ============================================================================
# TTS NORMALISER
# Longer patterns first, otherwise "Rule 15(3)" swallows "Rule 15(3)(a)".
# Roman Hinglish passes through untouched; only references and acronyms change.
# ============================================================================
_TTS_FIXES = [
    (r'\bUPSC\b', 'U.P.S.C.'), (r'\bDoPT\b', 'D.O.P.T.'), (r'\bDOPT\b', 'D.O.P.T.'),
    (r'\bCCS\b', 'C.C.S.'), (r'\bCAG\b', 'C.A.G.'), (r'\bGOI\b', 'G.O.I.'),
    (r'\bFR\b', 'F.R.'), (r'\bCPC\b', 'C.P.C.'), (r'\bDPC\b', 'D.P.C.'),
    (r'\bBSNL\b', 'B.S.N.L.'), (r'\bMTNL\b', 'M.T.N.L.'), (r'\bPSU\b', 'P.S.U.'),
    (r'\bPSUs\b', 'P.S.U.s'), (r'\bOFB\b', 'O.F.B.'), (r'\bNPA\b', 'N.P.A.'),
    (r'\bIDA\b', 'I.D.A.'), (r'\bRPwD\b', 'R.P.W.D.'), (r'\bIIS\b', 'I.I.S.'),
    (r'\bCSS\b', 'C.S.S.'), (r'\bCAB\b', 'C.A.B.'), (r'\bO\.M\.', 'O.M.'),
    (r'\bRs\.?\s*', 'Rupees '), (r'G\.S\.R\.', 'G.S.R.'),
    (r'Rule\s+(\d+)\((\d+)\)\(([a-z])\)', r'Rule \1, sub rule \2, clause \3'),
    (r'Rule\s+(\d+)\(([a-z])\)', r'Rule \1, clause \2'),
    (r'Rule\s+(\d+)\((\d+)\)', r'Rule \1, sub rule \2'),
    (r'Rules\s+(\d+)\s*&\s*(\d+)', r'Rules \1 and \2'),
    (r'(\d+)\s*/\s*(\d+)\s*/\s*(\d{4})', r'\1 \2 \3'),
    (r'[—–]', ','),
]


def normalize_for_tts(text: str) -> str:
    for pat, rep in _TTS_FIXES:
        text = re.sub(pat, rep, text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\.{2,}', '.', text)
    return text.strip()


# ============================================================================
# FONTS
# ============================================================================
_FONT_CACHE = {}
_BOLD_FILES = ("Inter-Bold.ttf", "Manrope-Bold.ttf", "SegoeUIBold.ttf", "segoeuib.ttf",
               "arialbd.ttf", "DejaVuSans-Bold.ttf")
_REG_FILES = ("Inter-Regular.ttf", "Manrope-Regular.ttf", "segoeui.ttf", "arial.ttf",
              "DejaVuSans.ttf")
_MONO_FILES = ("JetBrainsMono-Regular.ttf", "consola.ttf", "DejaVuSansMono.ttf")


def _load(files, size):
    for name in files:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    try:
        return ImageFont.load_default(size)
    except TypeError:
        return ImageFont.load_default()


def font(size: int, bold: bool = False, mono: bool = False):
    key = (size, bold, mono)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    f = _load(_MONO_FILES if mono else (_BOLD_FILES if bold else _REG_FILES), size)
    _FONT_CACHE[key] = f
    return f


def text_w(d, s, f):
    b = d.textbbox((0, 0), s, font=f)
    return b[2] - b[0]


def wrap_text(d, text, f, max_w):
    out = []
    for para in str(text).split("\n"):
        cur = ""
        for word in para.split(" "):
            t = f"{cur} {word}".strip()
            if text_w(d, t, f) <= max_w:
                cur = t
            else:
                if cur:
                    out.append(cur)
                cur = word
        out.append(cur)
    return out


def fit(d, text, bold, max_w, max_h, start, min_size, spacing=1.28, mono=False):
    """Shrink until every line fits. Raises instead of truncating."""
    for size in range(start, min_size - 1, -1):
        f = font(size, bold, mono)
        lines = wrap_text(d, text, f, max_w)
        lh = int(size * spacing)
        if len(lines) * lh <= max_h:
            return f, lines, lh, size
    raise ValueError(f"OVER BUDGET (needs < {min_size}px): {str(text)[:90]!r}")


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def dim(c, t=0.55):
    return lerp(CARD_BG, c, t)


def blend(c1, c2, t):
    return lerp(c1, c2, t)


# ============================================================================
# BOARD BACKGROUND (screenshot parity: indigo gradient + two soft glows)
# ============================================================================
def background(accent=BLUE):
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(H):
        d.line([(0, y), (W, y)], fill=lerp(BG_TOP, BG_BOT, y / H))
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([-360, -430, 980, 470], fill=lerp(GLOW_A, accent, 0.18))
    gd.ellipse([1240, 640, 2360, 1560], fill=GLOW_B)
    glow = glow.filter(ImageFilter.GaussianBlur(150))
    img = ImageChops.add(img, glow)
    d = ImageDraw.Draw(img)
    for x in range(48, W, 64):
        for y in range(150, H - 60, 64):
            d.point((x, y), fill=(30, 36, 62))
    return img, d


def wave_bars(d, x, y, n=46, colour=None):
    """Little audio-meter strip, as in the reference screenshot."""
    colour = colour or (54, 120, 150)
    for i in range(n):
        hgt = 3 + int(9 * abs(math.sin(i * 0.55)) + 4 * abs(math.sin(i * 0.21)))
        d.rectangle([x + i * 9, y + (12 - hgt) // 2, x + i * 9 + 4, y + (12 + hgt) // 2], fill=colour)


def chip(d, x_right, y, text, colour, size=17, solid=False):
    f = font(size, True)
    w = text_w(d, text, f) + 30
    box = [x_right - w, y, x_right, y + 30]
    if solid:
        d.rounded_rectangle(box, radius=15, fill=colour)
        d.text((box[0] + 15, y + 6), text, font=f, fill=TEXT_ON_LIGHT)
    else:
        d.rounded_rectangle(box, radius=15, fill=lerp(CARD_BG, colour, 0.20), outline=colour, width=2)
        d.text((box[0] + 15, y + 6), text, font=f, fill=colour)
    return w



# ============================================================================
# SCENES - the board. One dict per chapter; every card is
# (title, short on-screen text, full wording, colour, Hinglish narration).
# ============================================================================
SCENES = [
    {
        "id": "c3_01_rule31_emoluments",
        "chapter": "CHAPTER 1 • RULE 31: EMOLUMENTS",
        "title": "RULE 31(1) — WHAT COUNTS AS EMOLUMENTS?",
        "badge": "RULE 31(1)",
        "q": "What exactly are emoluments, and which pay figure and which date do we use?",
        "q_say": "Sir, Rule thirty-one me emoluments exactly kya hai, aur pay kis date par dekhte hain?",
        "hook": "REMEMBER: Emoluments = basic pay (+ NPA for doctors) just before retirement or death. No DA!",
        "hook_say": (
            "Yaad rakhiye: emoluments matlab basic pay, doctor ke liye NPA bhi, retirement ya death se thik pehle. DA "
            "bilkul nahi."
        ),
        "intro": (
            "Namaste doston, welcome back. Ye Part three hai Central Civil Services Pension Rules, two thousand "
            "twenty-one ka. Is part me Rules thirty-one se forty-one tak: pehle pay kaise napa jata hai pension ke "
            "liye, aur phir pension ki alag alag kismein. Riya sawaal poochhegi, main simple Hinglish me jawab dunga. "
            "Chaliye Rule thirty-one se shuru karein."
        ),
        "layout": "dashboard",
        "boxes": [
            (
                "THE RULE • RULE 31(1)",
                (
                "Emoluments means BASIC PAY drawn just before retirement (or on the date of death), plus a medical "
                "officer's non-practising allowance."
            ),
                (
                "Rule 31(1): 'emoluments' means basic pay as defined in Fundamental Rule 9(21)(a)(i), which a Government "
                "servant was drawing immediately before his retirement or on the date of his death, and includes "
                "non-practising allowance granted to a medical officer. The word is 'means', not 'includes', so the list "
                "is exhaustive. [Verbatim Gazette text, Rule 31(1) and its Explanation (G.S.R. 868(E) of 20.12.2021).]"
            ),
                SKY,
                (
                "Chaliye Rule thirty-one se shuru karein. Emoluments matlab wahi basic pay jo retirement se thik pehle, "
                "ya death ki date par mil rahi thi, plus medical officer ka non-practising allowance. Ye allowance aise "
                "doctor ko milta hai jo private practice nahi kar sakta."
            ),
            ),
            (
                "THE EXPLANATION",
                "A stagnation increment is also treated as emoluments for retirement benefits.",
                (
                "Explanation to Rule 31(1): stagnation increment is treated as emoluments for the calculation of "
                "retirement benefits. A stagnation increment is the extra increment given to someone who has reached the "
                "top of the pay scale and cannot go higher. [Verbatim Gazette text.]"
            ),
                GREEN,
                (
                "Ab Explanation. Stagnation increment bhi emoluments me ginega. Ye wo extra increment hai jo pay scale ke "
                "top par pahunchne ke baad milta hai, aage badhne ki jagah nahi bachti. To retirement benefits me ise "
                "zaroor jodna hai."
            ),
            ),
            (
                "REAL EXAMPLE",
                (
                "Charu retires on basic pay of rupees 62,000: emoluments = 62,000. Dr Dev: basic 1,00,000 + NPA 12,000 = "
                "1,12,000."
            ),
                (
                "Example (invented names and amounts, recomputed): Charu's basic pay just before retirement is Rs 62,000; "
                "her dearness allowance, house rent allowance and transport allowance are NOT added, so her emoluments "
                "are Rs 62,000. Dr Dev, a medical officer, has basic pay Rs 1,00,000 and non-practising allowance Rs "
                "12,000, so his emoluments are 1,00,000 + 12,000 = Rs 1,12,000. Time test: the pay drawn immediately "
                "before retirement, or on the date of death. Q&A from the source: is a medical officer's non-practising "
                "allowance emoluments? Yes, Rule 31(1) says so expressly."
            ),
                ORANGE,
                (
                "Example dekhiye. Charu ki basic pay sixty-two hazaar hai, to emoluments sixty-two hazaar, koi allowance "
                "nahi judta. Dr Dev: basic one lakh plus NPA twelve hazaar, total one lakh twelve hazaar."
            ),
            ),
            (
                "THE TRAP",
                (
                "Dearness allowance, house rent and travel allowance are NOT emoluments. One guide note saying 'basic pay "
                "plus DA' is wrong."
            ),
                (
                "DA, HRA, TA and LTC are not emoluments: only basic pay (plus NPA for a medical officer). The source "
                "guide's worked-example annotation 'emoluments = basic pay + DA' conflicts with Rule 31(1), which has no "
                "DA; do not use it (divergence confirmed against the rule text). Look-alike: Rule 31 DEFINES emoluments; "
                "Rule 32 AVERAGES them over ten months. Do not mix the two."
            ),
                RED,
                (
                "Yahan trap hai. Rule me shabd means likha hai, matlab list poori hai. DA, HRA, TA emoluments nahi hain. "
                "Kisi note me basic plus DA likha ho to galat. Aur yaad rakhiye, Rule thirty-one define karta hai, Rule "
                "thirty-two average nikalta hai."
            ),
            ),
        ],
        "covers": ["R31-MAIN", "R31-EXPL1", "R31-NODA", "R31-DIVERGE-DA", "R31-TIMETEST", "R31-EX-ASO", "R31-NPA-QA"],
    },
    {
        "id": "c3_02_rule31_subrules",
        "chapter": "CHAPTER 2 • RULE 31(2) TO (11): SPECIAL CASES",
        "title": "RULE 31(2)-(11) — WHEN THE PAY ACTUALLY DRAWN IS NOT THE WHOLE STORY",
        "badge": "RULE 31(2)-(11)",
        "q": "What do sub-rules 2 to 11 of Rule 31 add, for leave, suspension, deputation and late pay revision?",
        "q_say": "Sir, guide ne Rule thirty-one ke sub-rules two se eleven chhode the. Ye kehte kya hain?",
        "hook": "REMEMBER: Rule 31 has 11 sub-rules; (2) is about leave and suspension, (10)-(11) are about notional pay!",
        "hook_say": (
            "Yaad rakhiye: Rule thirty-one me gyarah sub-rules hain. Do leave aur suspension, aur das-gyarah notional "
            "pay."
        ),
        "layout": "dashboard",
        "boxes": [
            (
                "SUB-RULE (2): LEAVE, SUSPENSION",
                (
                "Pay he WOULD have drawn counts during paid leave, sick-certificate extraordinary leave, or suspension "
                "that ended in reinstatement."
            ),
                (
                "Rule 31(2) (resolved from a rule summary): the pay he would have drawn during leave with salary, "
                "extraordinary leave on medical certificate, or suspension that ended in reinstatement is counted. "
                "Increases not actually drawn are excluded, except the increments or notional increases covered by "
                "sub-rules (5), (10) and (11). The source guide called this a 'notional increments trigger'; that "
                "description is not right (status: changed). Second-hand summary: read the Gazette for the exact words."
            ),
                SKY,
                (
                "Sub-rule two: paid leave, medical certificate wali extraordinary leave, ya suspension ke baad "
                "reinstatement. In sab me jo pay milta rehta tha wo count hoga. Jo increase actually nahi mila wo chhut "
                "jayega, sirf sub-rules five, ten aur eleven chhodkar."
            ),
            ),
            (
                "SUB-RULES (3) TO (9)",
                (
                "Higher post during leave; pay before non-qualifying leave; increment during leave; ex-cadre post; State "
                "or foreign service; re-employed pensioner; converted PSU."
            ),
                (
                "Rule 31(3): where the servant, immediately before retirement or death while in service, had proceeded on "
                "leave with leave salary after holding a higher appointment (officiating or temporary), the higher-post "
                "emoluments count ONLY if it is certified that he would have continued to hold that higher appointment "
                "but for proceeding on leave. Rule 31(4): where the absence was extraordinary leave or suspension that "
                "does not count as service, the emoluments drawn immediately before proceeding on leave or being placed "
                "under suspension count. Rule 31(5): an increment earned during leave, not withheld, counts though not "
                "drawn. Rule 31(6): pay drawn on deputation to an ex-cadre post in the same or another Department OR to "
                "the Armed Forces of India is emoluments; proviso: where he is on leave after release from the ex-cadre "
                "post on completion of the deputation period, the pay he would have drawn in the parent department "
                "counts. Rule 31(7): pay on deputation to a State Government or on foreign service does NOT count; only "
                "the Central pay he would have drawn counts. Rule 31(8): a re-employed pensioner who elected to retain "
                "his earlier pension and whose re-employment pay was reduced by an amount not exceeding that pension, the "
                "element of pension by which pay was reduced is emoluments. Rule 31(9): a servant transferred to a PSU or "
                "autonomous body on conversion who OPTS to retain Government pensionary benefits has the PSU or body pay "
                "treated as emoluments. [Verbatim Gazette text, Rules 31(3) to 31(9).]"
            ),
                BLUE,
                (
                "Baaki sub-rules ek line me. Teen: leave ke dauraan higher post. Chaar: non-qualifying leave ya "
                "suspension se pehle ki pay. Paanch: leave me earned increment. Chhah: ex-cadre post ya Armed Forces. "
                "Saat: State ya foreign service me Central pay. Aath: re-employed pensioner. Nau: converted PSU ka "
                "employee."
            ),
            ),
            (
                "SUB-RULES (10) AND (11)",
                (
                "(10) pay revised backwards after retirement: notional pay counts. (11) died while a penalty cut his pay: "
                "pay without the cut counts."
            ),
                (
                "Rule 31(10): notional pay from a retrospective revision after retirement (retrospective scale increase, "
                "or retrospective promotion by a review DPC, exoneration or court order). Rule 31(11): death during a "
                "penalty that reduced pay: notional pay ignoring the penalty. Example (invented, recomputed): Bilal "
                "retires on 31 January 2026 on Rs 80,000; a review Departmental Promotion Committee later promotes him "
                "from 1 October 2025 to a post paying Rs 84,000 from that date; his notional emoluments are Rs 84,000."
            ),
                GREEN,
                (
                "Sub-rule das ka example. Bilal thirty-first January ko eighty hazaar par retire hua. Baad me review DPC "
                "ne first October se eighty-four hazaar deni thi, to emoluments eighty-four hazaar maane jayenge. Gyarah: "
                "death ke waqt penalty chal rahi thi, to penalty ke bina wali pay."
            ),
            ),
            (
                "THE TRAP",
                "The source never mentioned (3)-(11). Sub-rule (2) is NOT a 'notional increments trigger'.",
                (
                "Gap in the source guide: Rule 31(3)-(11) were never mentioned and are added here; the guide's 'notional "
                "increments trigger' label for Rule 31(2) is wrong. Cross-link: sub-rule (10) and (11) feed Rule 32(5) "
                "and (6) for the average. [Verbatim Gazette text, Rules 31(10), 31(11), 32(5) and 32(6).]"
            ),
                RED,
                (
                "Trap ye hai. Guide ne sub-rules teen se gyarah chhod diye the. Aur sub-rule two ko notional increments "
                "trigger kehna galat hai, wo leave aur suspension ka rule hai. Exact words Gazette se confirm kar lein."
            ),
            ),
        ],
        "covers": ["R31-SUB2", "R31-SUB3-11"],
    },
    {
        "id": "c3_03_rule32_average",
        "chapter": "CHAPTER 3 • RULE 32(1): AVERAGE EMOLUMENTS",
        "title": "RULE 32(1) — AVERAGE EMOLUMENTS OF THE LAST TEN MONTHS",
        "badge": "RULE 32(1)",
        "q": "What are average emoluments, and when do we use them instead of plain emoluments?",
        "q_say": "Sir, average emoluments kya hai, aur kab hum ise emoluments ki jagah use karte hain?",
        "hook": "REMEMBER: Average = last 10 months; pension uses the BETTER of emoluments or average; fractions go UP!",
        "hook_say": "Yaad rakhiye: average aakhri das mahine ka, pension me jo behtar ho wo, aur fraction upar round.",
        "layout": "dashboard",
        "boxes": [
            (
                "THE RULE • RULE 32(1)",
                "Average emoluments = emoluments drawn in the LAST TEN MONTHS of service, added up and divided by ten.",
                (
                "Rule 32(1): average emoluments shall be determined with reference to the emoluments drawn by a "
                "Government servant during the last ten months of his service. The base is the Rule 31 emoluments only. "
                "Rule 32 has no Explanation, only an Illustration (confirmed). [Verbatim Gazette text, Rules 32(1) to "
                "32(6).]"
            ),
                SKY,
                (
                "Rule thirty-two, one: average emoluments matlab service ke aakhri das mahino ki emoluments, jodkar das "
                "se divide. Pay wahi Rule thirty-one wali, matlab basic plus doctor ka NPA, DA nahi."
            ),
            ),
            (
                "WHICH ONE WINS? RULE 44(1)",
                (
                "Pension is 50 percent of emoluments OR average emoluments, whichever is MORE beneficial. Floor 9,000, "
                "ceiling 1,25,000 a month."
            ),
                (
                "Rule 44(1): pension at 50% of emoluments or average emoluments, whichever is more beneficial to the "
                "Government servant, subject to a minimum of Rs 9,000 and a maximum of Rs 1,25,000 per month. Dynamic "
                "figures: effective dates not re-confirmed here; check the latest O.M. Full treatment of Rule 44 is in "
                "the next batch. Average emoluments are an option, not always the best."
            ),
                GREEN,
                (
                "Ab choice. Rule forty-four, one: pension fifty percent emoluments ya average emoluments ka, jo zyada "
                "faydemand ho. Minimum nau hazaar, maximum one lakh twenty-five hazaar per month, par latest O.M. se "
                "confirm kar lein."
            ),
            ),
            (
                "ROUNDING • RULE 44(9)",
                "Amounts are in whole rupees; any fraction is rounded UP to the next rupee.",
                (
                "Rule 44(9): amounts are expressed in whole rupees and any fraction is rounded up to the next higher "
                "rupee (confirmed, close restatement). The source guide cited this as the rounding rule for Rule 32 "
                "averages. Example: 77,222.22 becomes 77,223."
            ),
                ORANGE,
                (
                "Chhoti baat, par exam me poochi jaati hai. Rule forty-four, nine: rakam poore rupaye me, aur fraction "
                "upar round hota hai. To seventy-seven thousand two hundred twenty-two point twenty-two banega "
                "seventy-seven thousand two hundred twenty-three."
            ),
            ),
            (
                "THE TRAP",
                "Rule 32(2) does NOT say 'a fall in pay is ignored'. An ordinary pay fall counts as actually drawn.",
                (
                "The source said Rule 32(2) means 'if pay fell in the last ten months, average is computed as if no "
                "reduction'. That is a wrong attribution (status: changed). Rule 32(2) deals with the pay he would have "
                "drawn during leave with salary, extraordinary leave on medical certificate, or suspension ending in "
                "reinstatement. Ignoring a penalty reduction is Rule 32(6), only where the officer dies while a "
                "penalty-reduced pay was running. An ordinary pay fall counts as actually drawn; the average can still "
                "win through the Rule 44(1) choice, not through Rule 32(2). Do not teach the source version."
            ),
                RED,
                (
                "Trap: Rule thirty-two, two ye nahi kehta ki pay girne par purani pay maan lo. Wo leave aur suspension ka "
                "rule hai. Pay girna normal tarike se count hoga, average sirf isliye jeetta hai ki Rule forty-four "
                "better figure chunne deta hai."
            ),
            ),
        ],
        "covers": ["R32-1", "R32-NOEXPL", "R32-R44CHOICE", "R32-ROUND", "R32-DIVERGE-2"],
    },
    {
        "id": "c3_04_rule32_subrules",
        "chapter": "CHAPTER 4 • RULE 32(2) TO (6): THE TEN-MONTH WINDOW",
        "title": "RULE 32(2)-(6) — LEAVE, SUSPENSION AND THE 30-DAY MONTH",
        "badge": "RULE 32(2)-(6)",
        "q": "How is the ten-month window handled when there is leave, suspension or a late pay revision?",
        "q_say": "Sir, das mahine ki window me leave, suspension ya late pay revision ho to kya karte hain?",
        "hook": "REMEMBER: Skip bad months, add earlier ones, still divide by TEN; a month = 30 days!",
        "hook_say": (
            "Yaad rakhiye: jo mahine nahi ginte unhe hatao, barabar ke pehle ke jodo, das se divide karo, mahina "
            "thirty din."
        ),
        "layout": "dashboard",
        "boxes": [
            (
                "SUB-RULE (2) AND ITS PROVISO",
                (
                "Pay he would have drawn on paid leave, sick-certificate leave or reinstated suspension counts. Pay never "
                "actually drawn does not, with exceptions."
            ),
                (
                "Rule 32(2): pay he would have drawn during leave with salary, extraordinary leave on medical "
                "certificate, or suspension ending in reinstatement is included. The PROVISO belongs to sub-rule (2), not "
                "(3): increases not actually drawn are excluded, except those in sub-rules (4), (5) and (6). [Verbatim "
                "Gazette text.]"
            ),
                SKY,
                (
                "Pehle sub-rule two. Paid leave, medical extraordinary leave, ya reinstatement wali suspension, in me jo "
                "pay milta wo count hota hai. Proviso: jo increase actually nahi mila wo nahi jodenge, sirf sub-rules "
                "four, five aur six ke cases me."
            ),
            ),
            (
                "SUB-RULE (3): THE WINDOW SLIDES",
                (
                "Extraordinary leave or suspension that does not count is skipped and an EQUAL earlier period is added. "
                "It stays ten months. A month = 30 days."
            ),
                (
                "Rule 32(3): periods of extraordinary leave or suspension that do not count as service are disregarded, "
                "and an equal period earlier is added in, so the window is still ten months and the divisor stays ten. "
                "For fractions of a month, a month is taken as 30 days. Illustration: retirement on 16 July 2019 gives "
                "nine full months (October 2018 to June 2019) plus 14/30 of September 2018 plus 16/30 of July 2019, which "
                "together make ten months."
            ),
                BLUE,
                (
                "Ab sub-rule three, jise log galat karte hain. Jo EOL ya suspension service me nahi ginta, wo mahine hata "
                "do, aur barabar ke pehle ke mahine jod do. Window das mahine hi rehti hai, divisor das hi. Ek mahina "
                "thirty din. Sixteenth July two thousand nineteen par retirement, to nau poore mahine, September ke "
                "fourteen-thirtieth aur July ke sixteen-thirtieth."
            ),
            ),
            (
                "SUB-RULES (4), (5), (6)",
                (
                "(4) increment earned in leave, not withheld, counts. (5) late notional increase counts. (6) died under a "
                "penalty cut: pay without the cut."
            ),
                (
                "Rule 32(4): an increment earned during leave in the last ten months, not withheld, is included though "
                "not drawn. Rule 32(5): retrospective notional pay increases within the last ten months, in the same "
                "circumstances as Rule 31(10), are included. Rule 32(6): where a penalty reduced pay and the officer dies "
                "during it, notional pay ignoring the penalty is used for the last ten months. These match Rule 31(5), "
                "(10), (11)."
            ),
                GREEN,
                (
                "Sub-rules four, five, six exceptions hain. Chaar: leave me earned increment, jo rokha na gaya ho. "
                "Paanch: backdated notional pay increase. Chhah: penalty ke dauraan death ho gayi to penalty ke bina wali "
                "pay."
            ),
            ),
            (
                "THE TRAP",
                "Old notes shrink the divisor to 9 or 8. Wrong: it stays ten. The exclusion is in (3), not (4).",
                (
                "Source errors corrected: (a) the source said the excluded months are dropped and the average is taken "
                "over the remaining months, so the denominator shrinks; that is wrong (status: changed). (b) The source's "
                "mismatch over sub-rule (4) (bullet said increment, bare text said extraordinary leave or suspension "
                "exclusion) is resolved: (4) is the increment; the exclusion is in (3). (c) Source examples (promotion "
                "benefit from outside the window; arrears of 'Chhath Pay Commission', a slip for Sixth or Seventh CPC) "
                "are the source's own, not in the rule; arrears of a retrospective revision after retirement may still "
                "count through Rule 32(5) and Rule 31(10). Those two source examples remain unverified."
            ),
                RED,
                (
                "Trap: purane notes kehte hain ki hataye gaye mahine divisor ghata dete hain, to nau ya aath se divide "
                "karo. Galat. Window peeche khiskti hai aur divisor das hi rehta hai. Aur exclusion sub-rule three me "
                "hai, four me nahi."
            ),
            ),
        ],
        "covers": ["R32-3", "R32-30DAY", "R32-4", "R32-5", "R32-6", "R32-PROV"],
    },
    {
        "id": "c3_05_rule32_example9",
        "chapter": "CHAPTER 5 • RULE 32: WORKED EXAMPLE WITH LEAVE",
        "title": "RULE 32 — A FULL WORKED EXAMPLE WITH EXTRAORDINARY LEAVE",
        "badge": "RULE 32 • EXAMPLE",
        "q": "Can you walk me through a complete average-emoluments sum when part of the time was extraordinary leave?",
        "q_say": "Sir, ek poora sum batayein jisme teen mahine extraordinary leave thi?",
        "hook": "REMEMBER: Build ten months, divide by ten, compare with actual pay, take the better; round UP!",
        "hook_say": (
            "Yaad rakhiye: das mahine banao, das se divide karo, actual pay se compare karo, behtar lo, upar round "
            "karo."
        ),
        "layout": "dashboard",
        "boxes": [
            (
                "THE FACTS (INVENTED)",
                (
                "Bilal retires on 31 March 2027. Last months: Dec-Mar at 80,000. Sep-Nov extraordinary leave. Before "
                "that, Mar-Aug at 75,000."
            ),
                (
                "Example (invented, flagged as the card writer's own numbers): Bilal retires on 31 March 2027. December "
                "to March: 4 months at Rs 80,000. September to November: 3 months of extraordinary leave that does not "
                "count as qualifying service. Before that, March to August: pay Rs 75,000. Why rebuilt: the source's own "
                "Example 9 (Ashok Kumar, 75,000 for 5 months, 3 months leave, 80,000 for 4 months, dividing by 9) uses "
                "the wrong method and its 12 months from April do not fit a ten-month window."
            ),
                SKY,
                (
                "Worked example, naam aur numbers apne. Bilal thirty-first March two thousand twenty-seven ko retire hota "
                "hai. Aakhri chaar mahine, December se March, eighty hazaar. September se November EOL, jo service me "
                "nahi ginti. Us se pehle March se August, seventy-five hazaar."
            ),
            ),
            (
                "STEP 1 AND 2: BUILD THE WINDOW",
                "Take 4 months at 80,000. Skip the 3 leave months. Add 6 earlier months at 75,000. That is ten months.",
                (
                "Under Rule 32(3): window = Dec, Jan, Feb, Mar (4 months) + the three leave months skipped + Aug, Jul, "
                "Jun, May, Apr, Mar of the earlier year (6 months) = 10 months. Total = 4 x 80,000 + 6 x 75,000 = "
                "3,20,000 + 4,50,000 = Rs 7,70,000. Divisor stays ten."
            ),
                BLUE,
                (
                "Pehle window banao. Chaar mahine eighty hazaar ke. Teen leave mahine hata do. Phir pehle ke chhah mahine "
                "seventy-five hazaar ke jod do, kul das mahine. Total: chaar into eighty hazaar, three lakh twenty "
                "hazaar, plus chhah into seventy-five hazaar, four lakh fifty hazaar, seven lakh seventy hazaar."
            ),
            ),
            (
                "STEP 3 TO 5: COMPARE",
                (
                "Average = 7,70,000 / 10 = 77,000. Actual emoluments 80,000 are higher, so pension at 50 percent = 40,000 "
                "(average would give 38,500)."
            ),
                (
                "Average emoluments = 7,70,000 / 10 = Rs 77,000 (no fraction, so no rounding). Emoluments at retirement = "
                "Rs 80,000. Under Rule 44(1) take the more beneficial: 80,000. Pension at 50% = Rs 40,000 per month; with "
                "the average it would be 50% of 77,000 = Rs 38,500. The 50 percent rate is the Rule 44(1) rate as "
                "confirmed here; qualifying-service scaling is in the next batch, so assume full service for this "
                "example."
            ),
                GREEN,
                (
                "Ab comparison. Seven lakh seventy hazaar divided by ten, seventy-seven hazaar, yahi average. Actual "
                "emoluments eighty hazaar, jo zyada hai. To Rule forty-four, one se eighty hazaar lenge, pension fifty "
                "percent, forty hazaar. Average se sirf thirty-eight hazaar five hundred milta."
            ),
            ),
            (
                "THE TRAP",
                (
                "The old method divided 6,95,000 by 9 = 77,223. Wrong divisor. And 38,611.5 rounds UP to 38,612, not "
                "38,611."
            ),
                (
                "Source's method (wrong): 9 qualifying months, total 6,95,000 divided by 9 = 77,222.22, rounded up to "
                "77,223, wrong-average pension 38,611.5. Arithmetic matched the source, but the method is wrong under "
                "Rule 32(3). Rounding correction: 38,611.5 rounds UP to Rs 38,612 under Rule 44(9), not 38,611."
            ),
                RED,
                (
                "Trap: guide ne leave mahine hata kar nau se divide kiya. Sahi tarika window khiskana aur das se divide "
                "karna hai. Aur thirty-eight thousand six hundred eleven point five rupaye upar round hokar thirty-eight "
                "thousand six hundred twelve banega."
            ),
            ),
        ],
        "covers": ["R32-EX9-NUMBERS"],
    },
    {
        "id": "c3_06_rule32_cases",
        "chapter": "CHAPTER 6 • RULE 32: PROMOTION CASES AND WHEN THE AVERAGE WINS",
        "title": "RULE 32 — FOUR PROMOTION CASES, AND THE ONE TIME AVERAGE WINS",
        "badge": "RULE 32 • CASES",
        "q": "When pay changes in the last ten months, which is better, emoluments or the average?",
        "q_say": "Sir, aakhri das mahino me pay badle to kaun behtar hai, emoluments ya average?",
        "hook": "REMEMBER: Promotion in the window, actual pay wins; no change, equal; pay fell, average wins!",
        "hook_say": (
            "Yaad rakhiye: promotion ho to actual jeetta hai, kuch na badle to barabar, pay gire to average jeetta "
            "hai."
        ),
        "layout": "dashboard",
        "boxes": [
            (
                "CASES 1 AND 2",
                (
                "Case 1: 3 months at 60,000, 7 at 85,000: average 77,500, pension 42,500. Case 2: 5 and 5 at 65,000 and "
                "90,000: 77,500, pension 45,000."
            ),
                (
                "Case 1 (early promotion): 3 x 60,000 = 1,80,000; 7 x 85,000 = 5,95,000; total 7,75,000; /10 = 77,500; "
                "actual 85,000 is better; 50% = Rs 42,500. Case 2 (mid promotion): 5 x 65,000 = 3,25,000; 5 x 90,000 = "
                "4,50,000; total 7,75,000; average 77,500; actual 90,000; 50% = Rs 45,000. Source's four cases are its "
                "own illustrations; arithmetic recomputed here."
            ),
                SKY,
                (
                "Chaar log, jinka promotion aakhri das mahino me hai. Case one: teen mahine sixty hazaar, saat mahine "
                "eighty-five hazaar. Average seventy-seven hazaar five hundred, actual eighty-five hazaar, pension "
                "forty-two hazaar five hundred. Case two: paanch aur paanch, sixty-five aur ninety hazaar, average phir "
                "seventy-seven hazaar five hundred, actual ninety hazaar, pension forty-five hazaar."
            ),
            ),
            (
                "CASES 3 AND 4",
                (
                "Case 3: 8 at 70,000, 2 at 95,000: average 75,000, pension 47,500. Case 4: no promotion, 78,000 both "
                "ways: pension 39,000."
            ),
                (
                "Case 3 (late promotion): 8 x 70,000 = 5,60,000; 2 x 95,000 = 1,90,000; total 7,50,000; average 75,000; "
                "actual 95,000; 50% = Rs 47,500; gap between actual and average = Rs 20,000. Case 4 (no promotion): 10 x "
                "78,000; average and actual both 78,000; 50% = Rs 39,000."
            ),
                BLUE,
                (
                "Case three: aath mahine seventy hazaar, do mahine ninety-five hazaar. Average seventy-five hazaar, "
                "actual ninety-five hazaar, pension forty-seven hazaar five hundred. Case four: promotion nahi, dono "
                "seventy-eight hazaar, pension thirty-nine hazaar."
            ),
            ),
            (
                "WHEN THE AVERAGE WINS",
                (
                "When pay FELL: 5 months at 90,000, then 5 at 70,000. Average 80,000 beats actual 70,000. Pension 40,000 "
                "against 35,000."
            ),
                (
                "Source Q&A: 5 x 90,000 = 4,50,000; 5 x 70,000 = 3,50,000; total 8,00,000; /10 = 80,000. Actual at "
                "retirement 70,000. Average is better: 50% = Rs 40,000 against Rs 35,000. Principle holds through the "
                "Rule 44(1) 'whichever is more beneficial' choice, not through Rule 32(2). Takeaway: promotion in the "
                "window, emoluments win; no change, both equal; pay fall, the average wins."
            ),
                GREEN,
                (
                "Ab wo ek case jahan average jeetta hai, jab pay giri ho. Paanch mahine ninety hazaar, phir paanch mahine "
                "seventy hazaar. Average eighty hazaar, actual seventy hazaar. Pension average par forty hazaar, actual "
                "par thirty-five hazaar. Ye Rule forty-four ke better-of choice se hota hai, Rule thirty-two, two se "
                "nahi."
            ),
            ),
            (
                "THE TRAP",
                "The guide table said Case 1 average = 78,250. The right figure is 77,500. The pension is unchanged.",
                (
                "Divergence confirmed: the guide table shows 78,250 for Case 1; recomputing from its own numbers gives "
                "77,500. Final results of all four cases do not change because actual emoluments are higher in each. Case "
                "2 average 77,500, Case 3 75,000 and Case 4 78,000 match the guide. These are illustrative figures; the "
                "principle is permanent, the numbers come from the current O.M."
            ),
                RED,
                (
                "Trap: guide table me case one ka average seventy-eight hazaar two hundred fifty tha. Sahi seventy-seven "
                "hazaar five hundred hai. Pension same rehti hai, par sum khud karna sikhiye."
            ),
            ),
        ],
        "covers": ["R32-EX9A-C1", "R32-EX9A-C2", "R32-EX9A-C3", "R32-EX9A-C4", "R32-EX9A-DIVERGE", "R32-QA-FALL"],
    },
    {
        "id": "c3_07_rule33_34_routes",
        "chapter": "CHAPTER 7 • RULES 33 AND 34(1): RETIRING ON TIME OR EARLY",
        "title": "RULES 33 AND 34(1) — SUPERANNUATION PENSION AND RETIRING PENSION",
        "badge": "RULES 33 • 34(1)",
        "q": "What is superannuation pension, and what are the three routes to retiring pension?",
        "q_say": "Sir, superannuation pension kya hai, aur retiring pension ke teen raaste kaun se hain?",
        "hook": "REMEMBER: Rule 33 = retire on time. Rule 34(1) = early: you choose, Special VRS, or Government decides!",
        "hook_say": (
            "Yaad rakhiye: Rule thirty-three age par, Rule thirty-four age se pehle, teen raaste — khud, surplus, ya "
            "Government."
        ),
        "layout": "dashboard",
        "boxes": [
            (
                "RULE 33: SUPERANNUATION",
                (
                "Retire at the retiring age, or when an extension ends: superannuation pension or service gratuity under "
                "Rule 44."
            ),
                (
                "Rule 33: superannuation pension or superannuation service gratuity, as the case may be, shall be granted "
                "under Rule 44 to a Government servant who retires on attaining the age of superannuation or, if his "
                "service was extended beyond that age, on the expiry of the extension. Two triggers: reaching the age, or "
                "the end of the extension. 'Superannuation' simply means retirement on reaching the fixed retiring age. "
                "[Verbatim Gazette text.]"
            ),
                SKY,
                (
                "Pehle Rule thirty-three. Superannuation matlab fixed retiring age par retirement. Rule thirty-three "
                "superannuation pension ya superannuation service gratuity deta hai, Rule forty-four ke hisaab se. Do "
                "triggers: age aa gayi, ya extension khatam ho gayi."
            ),
            ),
            (
                "RULE 34(1): THREE ROUTES",
                (
                "(a) You choose to retire early, Rule 43 or FR 56. (b) Special VRS after being declared surplus. (c) "
                "Government retires you, Rule 42 or FR 56."
            ),
                (
                "Rule 34(1): retiring pension (or service gratuity) is granted to a Government servant who retires before "
                "superannuation (a) voluntarily, under Rule 43 or Fundamental Rule 56; (b) under the Special Voluntary "
                "Retirement Scheme, on being declared surplus (DoPT O.M. No. 25013/6/2001-Estt.(A) dated 28.02.2002, as "
                "amended from time to time); or (c) when retired by the Government under Rule 42 or FR 56. Rules 42 and "
                "43 are covered in the next batch. [Verbatim Gazette text.]"
            ),
                ORANGE,
                (
                "Ab Rule thirty-four, one. Retiring pension un logon ke liye jo age se pehle nikalte hain, teen raaste. "
                "Clause a: khud retire karein, Rule forty-three ya Fundamental Rule fifty-six. Clause b: surplus declare "
                "hokar Special VRS lein. Clause c: Government retire kare, Rule forty-two ya FR fifty-six."
            ),
            ),
            (
                "REAL EXAMPLE",
                (
                "Asha retires at the fixed age: Rule 33. Dev chooses early retirement: 34(1)(a). Esha is retired by the "
                "Government: 34(1)(c)."
            ),
                (
                "Example (invented): Asha retires on reaching the age of superannuation, so Rule 33 applies. Dev applies "
                "to retire before that age under Rule 43, so Rule 34(1)(a). A clerk Esha is declared surplus and opts for "
                "the Special VRS, so Rule 34(1)(b). Farid is retired by the Government in the public interest under Rule "
                "42, so Rule 34(1)(c)."
            ),
                GREEN,
                (
                "Example: Asha age par retire hoti hai, Rule thirty-three. Dev Rule forty-three se jaldi nikalta hai, "
                "clause a. Esha surplus hokar Special VRS leti hai, clause b. Farid ko Government retire karta hai Rule "
                "forty-two se, clause c."
            ),
            ),
            (
                "THE TRAP",
                (
                "Clause (a) and clause (c) look alike. Who decides? (a) the employee. (c) the Government. Rule 42 "
                "details: check next batch."
            ),
                (
                "Look-alike: (a) is the employee's choice (Rule 43 or FR 56); (c) is the Government's decision (Rule 42 "
                "or FR 56). The guide's claim that Rule 42 is a Government-initiated premature retirement after thirty "
                "years, with no ex-gratia like Rule 34(2), is UNVERIFIED here: Rule 42 was not read for this batch; "
                "verify it in Batch 4. All three routes lead to a retiring pension worked out under Rule 44."
            ),
                RED,
                (
                "Trap: clause a aur clause c ek jaise lagte hain. Faisla kaun karta hai? Clause a me employee, clause c "
                "me Government. Rule forty-two ki detail agle batch me."
            ),
            ),
        ],
        "covers": ["R33-1", "R34-1A", "R34-1B", "R34-1C", "R34-BONUS30-R42"],
    },
    {
        "id": "c3_08_rule34_svrs",
        "chapter": "CHAPTER 8 • RULE 34(2): THE SPECIAL VOLUNTARY RETIREMENT SCHEME",
        "title": "RULE 34(2) — EX-GRATIA ON TOP OF PENSION UNDER THE SPECIAL VRS",
        "badge": "RULE 34(2)",
        "q": "Under the Special VRS, does the ex-gratia replace the pension, and who can use it?",
        "q_say": "Sir, Special VRS me ex-gratia pension ki jagah leta hai ya uske upar, aur kaun le sakta hai?",
        "hook": "REMEMBER: Special VRS = permanent + surplus. Ex-gratia is ADDED to pension and retirement gratuity!",
        "hook_say": "Yaad rakhiye: ex-gratia pension ke upar milta hai, aur permanent plus surplus, dono chahiye.",
        "layout": "dashboard",
        "boxes": [
            (
                "THE RULE • RULE 34(2)",
                (
                "A PERMANENT servant declared SURPLUS who opts for the Special VRS gets ex-gratia under the Scheme IN "
                "ADDITION to the Rule 44 and Rule 45 benefits."
            ),
                (
                "Rule 34(2): a permanent Government servant declared surplus in his establishment, who opts for the "
                "Special Voluntary Retirement Scheme, is entitled to ex-gratia as per the Scheme in addition to the "
                "retiring pension or service gratuity under Rule 44 and the retirement gratuity under Rule 45. [Verbatim "
                "Gazette text.] Ex-gratia means a payment made as a favour or kindness, not as a legal right to a fixed "
                "sum."
            ),
                SKY,
                (
                "Rule thirty-four, two: permanent servant, jo surplus declare hua ho, Special Voluntary Retirement Scheme "
                "chune to ex-gratia milta hai. Keyword hai in addition. Rule forty-four ki pension ya service gratuity, "
                "aur Rule forty-five ki retirement gratuity, dono ke upar."
            ),
            ),
            (
                "THE SCHEME O.M.",
                (
                "DoPT O.M. No. 25013/6/2001-Estt.(A) dated 28 February 2002, as amended. Check the latest amended O.M. "
                "for the scheme terms."
            ),
                (
                "The O.M. number 25013/6/2001-Estt.(A) is confirmed from the text of Rule 34; the date 28.02.2002 is "
                "confirmed on the DoPT page. Scheme terms as reported there (NOT confirmed against the latest amended "
                "O.M.; add only after checking it): option within 3 months of being declared surplus; ex-gratia of 35 "
                "days pay plus DA for each completed year of service and 25 days for each year of service left, service "
                "capped at 33 years, minimum Rs 25,000 or 250 days; 5 years added to qualifying service for those with 15 "
                "or more years (1972 Rules wording)."
            ),
                BLUE,
                (
                "Scheme DoPT ke office memorandum number twenty-five thousand thirteen by six by two thousand one, "
                "Establishment A, twenty-eighth February two thousand two se aati hai, samay samay par amended. Payment "
                "ke figures latest amended O.M. se confirm karein."
            ),
            ),
            (
                "REAL EXAMPLE",
                (
                "Esha is a permanent clerk whose post is cut. She opts for the Special VRS: ex-gratia + retiring pension "
                "+ retirement gratuity."
            ),
                (
                "Example (invented, no amounts because the Scheme figures are unconfirmed): Esha, a permanent clerk in an "
                "office that is being closed, is declared surplus. She opts for the Special VRS. She receives (1) "
                "retiring pension or service gratuity under Rule 44, (2) retirement gratuity under Rule 45 and (3) the "
                "ex-gratia under the Scheme. Surplus means the post itself has become excess; the Special VRS is a "
                "dignified route (source gloss, consistent with the Scheme)."
            ),
                ORANGE,
                (
                "Example: Esha permanent clerk hai, uska post cut ho gaya, surplus declare hui. Special VRS liya, to "
                "retiring pension, retirement gratuity, aur ex-gratia, teeno mile."
            ),
            ),
            (
                "THE TRAP",
                "Ex-gratia is NOT a substitute for pension. BOTH words matter: permanent AND surplus.",
                (
                "Trap: the ex-gratia does not replace the Rule 44 and Rule 45 benefits; it is additional. Rule 34(2) "
                "needs both conditions: permanent servant and declared surplus. Three flavours of early exit: 34(1)(a) "
                "the employee chose, no surplus; 34(1)(b) the employee chose after being declared surplus (ex-gratia "
                "available); 34(1)(c) the Government chose. The guide's contrast with Rule 42 (Government's own "
                "initiative) is unverified here; see Batch 4."
            ),
                RED,
                (
                "Trap: ex-gratia pension ka substitute nahi, addition hai. Aur do conditions saath chahiye, permanent "
                "bhi, surplus bhi. Teen early-exit flavours alag rakhein: employee ki choice, surplus ke baad choice, aur "
                "Government ki choice."
            ),
            ),
        ],
        "covers": ["R34-2", "OM-28.02.2002-SVRS", "R34-BONUS30-SURPLUS"],
    },
    {
        "id": "c3_09_rule35_state",
        "chapter": "CHAPTER 9 • RULE 35(1)-(2): ABSORPTION IN A STATE GOVERNMENT",
        "title": "RULE 35(1)-(2) — MOVING TO A STATE GOVERNMENT: DEEMED RETIREMENT",
        "badge": "RULE 35(1)-(2)",
        "q": "What happens to pension when a Central servant is absorbed in a State Government post?",
        "q_say": "Sir, Central servant State Government me absorb ho jaye to pension ka kya hota hai?",
        "hook": (
            "REMEMBER: Absorbed in a State = deemed retired from the Centre on the absorption date; gratuity is "
            "capped!"
        ),
        "hook_say": "Yaad rakhiye: absorption ki date se deemed retired, aur dono gratuities par ek cap.",
        "layout": "dashboard",
        "boxes": [
            (
                "THE RULE • RULE 35(1)",
                (
                "On absorption in the State service, he is DEEMED RETIRED from Central service from that date and is "
                "eligible for pension or gratuity."
            ),
                (
                "Rule 35(1): a Government servant who is permitted to be absorbed in a State Government service or post "
                "shall be deemed to have retired from Central Government service from the date of absorption, and shall "
                "be eligible for pension or service gratuity and retirement gratuity on the qualifying service and "
                "emoluments as on that date, under Rules 44 and 45, subject to sub-rule (6). Absorption means being taken "
                "on permanently in the new employer's service. [Verbatim Gazette text, Rule 35(1) and its proviso.]"
            ),
                SKY,
                (
                "Pehle rule. Absorption matlab naye employer dwara permanently liya jaana. State Government me absorption "
                "par wo Central service se deemed retired ho jata hai, usi date se. Deemed matlab maan liya gaya. Pension "
                "ya service gratuity, aur retirement gratuity, us date ki qualifying service aur emoluments par."
            ),
            ),
            (
                "THE PROVISO: A GRATUITY CAP",
                (
                "Central plus State gratuity together cannot exceed what he would have got had he stayed Central and "
                "retired on his last State pay."
            ),
                (
                "Proviso to Rule 35(1): the total gratuity from the Central and State services together shall not exceed "
                "the amount that would have been admissible had he continued in Central service and retired on the pay "
                "drawn at retirement from the State service. Example (invented): Hari's Central gratuity plus State "
                "gratuity add up to Rs 16,00,000, but the notional Central gratuity on his last State pay is Rs "
                "14,00,000; only Rs 14,00,000 in total is allowed."
            ),
                GREEN,
                (
                "Ab proviso. Dono services ki gratuity milakar us notional Central figure se zyada nahi ho sakti, jo usse "
                "milta agar wo Central me rehta aur State ki last pay par retire hota. Example: Hari ki dono gratuity "
                "solah lakh, notional Central chaudah lakh, to chaudah lakh hi milega."
            ),
            ),
            (
                "THE DATE • RULE 35(2)",
                (
                "Immediate absorption: the date he actually joins. Deputation first: the date his unqualified resignation "
                "is accepted."
            ),
                (
                "Rule 35(2)(i): in a case of immediate absorption, the date of absorption is the date he actually joins "
                "the State Government service, his technical resignation being accepted for the post applied for with "
                "proper permission. Rule 35(2)(ii): if he was earlier on deputation, the date is the date on which his "
                "unqualified resignation from Central service is accepted. Keyword contrast: Rule 36(2)(ii) uses 'foreign "
                "service terms' for the same idea."
            ),
                ORANGE,
                (
                "Ab date, kyunki deemed retirement wahin se shuru hoti hai. Immediate absorption me jis din wo State me "
                "join karta hai. Pehle deputation par tha, to jis din uska unqualified resignation accept hota hai."
            ),
            ),
            (
                "REAL EXAMPLE AND TRAP",
                "Example: Hari joins the State on 1 July 2026, so he is deemed retired from the Centre on 1 July 2026.",
                (
                "Example (invented): Hari, a Central Section Officer, is permitted to take a State post and joins on 1 "
                "July 2026; his Central pension or gratuity is worked out on qualifying service and emoluments as on 1 "
                "July 2026, under Rules 44 and 45. Trap: do not read the date as the date the permission was granted, and "
                "do not forget that sub-rule (6) lets him choose between two routes (next chapter)."
            ),
                RED,
                (
                "Example: Hari first July two thousand twenty-six ko join karta hai, to usi din Centre se deemed retired. "
                "Central benefits usi date par. Trap: sochna ki yahin khatam, sub-rule six me option bhi hai."
            ),
            ),
        ],
        "covers": ["R35-1", "R35-PROV1", "R35-2I", "R35-2II"],
    },
    {
        "id": "c3_10_rule35_mechanics",
        "chapter": "CHAPTER 10 • RULE 35(3)-(7): RELIEVING ORDER, GAP AND THE OPTION",
        "title": "RULE 35(3)-(7) — FORMAT 5, THE JOINING GAP AND THE TWO ROUTES",
        "badge": "RULE 35(3)-(7)",
        "q": "How is the move done on paper, and what choice does the employee have under sub-rule 6?",
        "q_say": "Sir, paper par ye move kaise hota hai, aur sub-rule six me kya choice milti hai?",
        "hook": "REMEMBER: Format 5 relieving order; gap = leave; sub-rule 6 = choose; no lump sum in Rule 35!",
        "hook_say": "Yaad rakhiye: Format five, gap par leave ya EOL, aur sub-rule six me do routes.",
        "layout": "dashboard",
        "boxes": [
            (
                "SUB-RULES (3) TO (5)",
                (
                "Relieving order in Format 5 states the joining period; gap is leave due, else extraordinary leave; "
                "resignation counts from the day before joining."
            ),
                (
                "Rule 35(3): relieving order in Format 5, stating the joining period; proviso: for reasons beyond control "
                "the relieving authority may extend the joining period in writing. Rule 35(4): the gap is regularised as "
                "leave due, else as extraordinary leave. Rule 35(5): the relieving authority confirms the date of "
                "joining; the resignation is accepted from the day before the joining date. Format 5 is also used in Rule "
                "36(4). [Verbatim Gazette text.]"
            ),
                SKY,
                (
                "Pehle paperwork. Relieving order Format five me, joining period likha hota hai. Control se bahar ki "
                "wajah se der ho to authority likhit me extend kar sakti hai. Gap leave due se, na ho to extraordinary "
                "leave se regularise. Resignation joining se ek din pehle se accept."
            ),
            ),
            (
                "SUB-RULE (6): THE OPTION",
                (
                "If the State has a similar pension scheme he may choose: (a) Central-service benefits under (1), or (b) "
                "count his Central service in the State scheme."
            ),
                (
                "Rule 35(6): where the State Government has a similar pension scheme, the employee may choose (a) "
                "retirement benefits for his Central service under sub-rule (1), or (b) to have his Central service "
                "counted in the State's scheme. The source guide said only 'subject to sub-rule 6' and omitted this "
                "content (status: changed, now added)."
            ),
                GREEN,
                (
                "Ab sub-rule six, jo guide ne chhoda tha. State me similar pension scheme ho to option milta hai. Route "
                "a: Central service ke benefits sub-rule one ke hisaab se. Route b: Central service State ki scheme me "
                "count ho jaye."
            ),
            ),
            (
                "SUB-RULE (7): WHO PAYS",
                "Under route (b), the State pays pension and gratuity for the WHOLE service. The Centre bears no share.",
                (
                "Rule 35(7): under option (b) the State Government pays the pension and gratuity for the full service and "
                "the Central Government bears no proportionate liability. Example (invented): Imran chooses route (b); "
                "the State pays his whole pension on 30 years of service, 12 of them Central; the Centre pays nothing."
            ),
                ORANGE,
                (
                "Sub-rule seven batata hai paisa kaun dega. Route b me State poori service ki pension aur gratuity dega. "
                "Centre ka koi share nahi. Example: Imran ki thirty saal service, twelve Central, phir bhi State poori "
                "thirty ki dega."
            ),
            ),
            (
                "THE TRAP",
                "Rule 35 has NO lump-sum payment. Lump sums are in Rule 36(10)-(12) and Rules 37 and 38.",
                (
                "Trap: the source implied the lump-sum mechanism applies to the Rule 35 family. Rule 35 has no lump-sum "
                "provision; the lump sum is in Rule 36(10) to (12) and in Rules 37 and 38 (confirmed). Do not carry the "
                "lump-sum idea back to State absorption."
            ),
                RED,
                (
                "Trap: Rule thirty-five me lump sum nahi hai. Lump sum Rule thirty-six sub-rules ten se twelve me, aur "
                "Rules thirty-seven aur thirty-eight me aata hai."
            ),
            ),
        ],
        "covers": ["R35-3", "FORMAT-5", "R35-4", "R35-5", "R35-6", "R35-NOLUMP"],
    },
    {
        "id": "c3_11_rule36_body",
        "chapter": "CHAPTER 11 • RULE 36(1)-(8): ABSORPTION IN A CORPORATION OR BODY",
        "title": "RULE 36(1)-(8) — ABSORPTION IN A CORPORATION, COMPANY OR BODY",
        "badge": "RULE 36(1)-(8)",
        "q": "How does Rule 36 differ from Rule 35, and what does it say about lien and joint sector bodies?",
        "q_say": "Sir, Rule thirty-six Rule thirty-five se kaise alag hai, aur lien aur joint sector par kya kehta hai?",
        "hook": "REMEMBER: Rule 36 = Rule 35 with a Corporation or Body; foreign service terms; NO lien!",
        "hook_say": "Yaad rakhiye: Rule thirty-six me lien nahi bachta, sab rishte khatam.",
        "layout": "dashboard",
        "boxes": [
            (
                "THE RULE • RULE 36(1)",
                (
                "Same design as Rule 35, but the new employer is a Corporation, Company or Body owned, controlled or "
                "financed by the Centre or a State."
            ),
                (
                "Rule 36(1): a Government servant permitted to be absorbed in a Corporation, Company or Body wholly or "
                "substantially owned or controlled (or financed) by the Central or a State Government is deemed to have "
                "retired from the date of absorption; the same gratuity proviso applies, but with the pay drawn from the "
                "body at retirement. Explanation: 'Body' means an autonomous body or a statutory body. [Verbatim Gazette "
                "text.]"
            ),
                SKY,
                (
                "Rule thirty-six ka design Rule thirty-five jaisa hi hai, sirf employer badalta hai. Corporation, Company "
                "ya Body, Centre ya State ka. Same deemed retirement, same gratuity cap, par pay us body ki. Explanation "
                "kehti hai body matlab autonomous ya statutory body."
            ),
            ),
            (
                "THE DATE • RULE 36(2)",
                (
                "(i) Immediate absorption: the date he joins. (ii) Foreign service terms: the date his unqualified "
                "resignation is accepted."
            ),
                (
                "Rule 36(2)(i): immediate absorption: the date he joins. Rule 36(2)(ii): foreign service terms: the date "
                "his unqualified resignation is accepted. Keyword contrast with Rule 35(2)(ii), which says 'deputation'. "
                "Foreign service (Rule 3(1)(j)) means service where the pay comes from a source other than the "
                "Consolidated Fund; that definition was covered in Batch 1 and was not re-read here (not re-checked this "
                "round: Batch 1 rule)."
            ),
                BLUE,
                (
                "Date bhi Rule thirty-five jaisi. Immediate absorption me joining ki din. Foreign service terms par tha, "
                "to unqualified resignation accept hone ki din. Note karein: Rule thirty-five deputation kehta hai, Rule "
                "thirty-six foreign service terms."
            ),
            ),
            (
                "SUB-RULES (3) TO (8)",
                (
                "(3) joint sector bodies covered. (4)-(7) Format 5 and joining mechanics. (8) NO LIEN: all ties with "
                "Government end."
            ),
                (
                "Rule 36(3): joint sector undertakings (Centre with State or Union Territory, or two or more States or "
                "Union Territories) are covered. Rule 36(4) to (7): Format 5 relieving order, joining period with "
                "proviso, gap regularised, resignation from the day before joining (the source cited only Rule 35 numbers "
                "for this). Rule 36(8): no lien in the relieving department; all ties with Government cease. Lien means "
                "the right to go back to a permanent post."
            ),
                GREEN,
                (
                "Sub-rule three: joint sector undertakings bhi covered, Centre aur State ya UT ke joint control me, ya do "
                "ya zyada States ke. Chaar se saat paperwork dohraate hain. Aath important hai: lien nahi bachta, "
                "Government se sab rishte khatam."
            ),
            ),
            (
                "REAL EXAMPLE AND TRAP",
                (
                "Jaya joins a Central public sector company on 1 April 2026: deemed retired that day, no lien, no way "
                "back."
            ),
                (
                "Example (invented): Jaya is permitted to be absorbed in a Central public sector company and joins on 1 "
                "April 2026; she is deemed retired from Government from that date and has no lien. Trap: Rule 36(8), no "
                "lien, is a Rule 36 point; do not assume the same words for Rules 37 and 38, which work by deemed "
                "deputation and options."
            ),
                RED,
                (
                "Example: Jaya first April two thousand twenty-six ko Central PSU me join karti hai, usi din deemed "
                "retired, lien nahi, wapas nahi. Trap: in baaton ko Rules thirty-seven aur thirty-eight par mat "
                "chipkayein, wahan deemed deputation aur options hain."
            ),
            ),
        ],
        "covers": ["R36-1", "R36-2", "R36-3", "R36-4-7", "R36-8", "R36-EXPL", "R36-FS-DEF"],
    },
    {
        "id": "c3_12_rule36_options",
        "chapter": "CHAPTER 12 • RULE 36(9)-(12): THE OPTION AND THE LUMP SUM",
        "title": "RULE 36(9)-(12) — THE OPTION, THE LUMP SUM AND A NUMBERING TRAP",
        "badge": "RULE 36(9)-(12)",
        "q": "What choice does a body employee get, how is the lump sum paid, and where is the deeming rule?",
        "q_say": "Sir, body wale employee ko kya choice milti hai, lump sum kaise milta hai, aur deeming rule kahan hai?",
        "hook": "REMEMBER: Rule 36(9) is the OPTION. Deemed absorption is Rule 37(4) and 38(3), not Rule 36!",
        "hook_say": "Yaad rakhiye: Rule thirty-six me deeming nahi hai, wo thirty-seven aur thirty-eight me hai.",
        "layout": "dashboard",
        "boxes": [
            (
                "SUB-RULE (9): THE OPTION",
                (
                "Rule 36(9) is the option: (a) Central-service benefits, or (b) count the service in the body's scheme. "
                "It is NOT a deeming rule."
            ),
                (
                "Rule 36(9): the employee has the option between (a) retirement benefits for his Central service and (b) "
                "having his service counted in the body's scheme. The source said the deeming of absorption if no option "
                "is given sits in Rule 36(9); that is wrong. No 'deemed absorption' provision was seen in Rule 36 "
                "(status: changed). [Verbatim Gazette text.]"
            ),
                SKY,
                (
                "Sub-rule nine option deta hai. Route a: Central service ke retirement benefits. Route b: service body ki "
                "apni scheme me count. Source ne kaha isme silence ki deeming bhi hai, par Rule thirty-six me aisa kuch "
                "nahi mila."
            ),
            ),
            (
                "SUB-RULES (10) TO (12)",
                (
                "Option (b): Government settles its liability with a one-time lump sum, worked out with the 1981 "
                "commutation table."
            ),
                (
                "Rule 36(10) and (11): under option (b) the Government's liability is met by a lump-sum one-time payment "
                "of the capitalised value of pension or service gratuity and of retirement gratuity. Rule 36(12): the "
                "capitalised value is worked out with the commutation table of the CCS (Commutation of Pension) Rules, "
                "1981. Capitalised value means today's lump-sum worth of pension to be paid in future years. Commutation "
                "means giving up part of a pension for a lump sum."
            ),
                BLUE,
                (
                "Ab lump sum. Route b chuni to Government apna pension bojh ek hi baar me chukati hai. Isme pension ya "
                "service gratuity ki capitalised value, aur retirement gratuity, dono aate hain. Table wahi Commutation "
                "of Pension Rules nineteen eighty-one ki."
            ),
            ),
            (
                "THE NUMBERING TRAP",
                "No deemed-absorption rule in Rule 36. Silence means deemed absorption in Rule 37(4) and Rule 38(3).",
                (
                "Corrected numbering: the deeming rule 'no option given, deemed to have opted for permanent absorption' "
                "is Rule 37(4) and Rule 38(3); Rule 36 has none (status: changed). Before answering 'what if no option is "
                "given?', check whether you are in Rule 36, 37 or 38. Only Rules 37 and 38 deem absorption."
            ),
                RED,
                (
                "Numbering trap. Silence par deemed absorption Rule thirty-seven, four aur Rule thirty-eight, three me "
                "hai, Rule thirty-six me nahi. Answer se pehle check karein aap kaunse rule me hain."
            ),
            ),
            (
                "REAL EXAMPLE",
                (
                "Kabir picks route (b): the Government pays one lump sum, not a monthly pension, and the body's scheme "
                "pays him later."
            ),
                (
                "Example (invented, no amounts because the table values were not read): Kabir is absorbed in a statutory "
                "body and picks option (b). The Government works out the capitalised value of his pension and his "
                "retirement gratuity with the 1981 commutation table and pays that single amount; the body's scheme then "
                "covers his pension. Also note the cross-link: the same 'lump sum plus 1981 table' idea reappears in "
                "Rules 37 and 38 (Rule 38(19)-(21))."
            ),
                GREEN,
                (
                "Example: Kabir statutory body me route b chunta hai. Government nineteen eighty-one table se capitalised "
                "value nikalkar ek lump sum deti hai, aage body ki scheme pension degi. Yahi idea Rules thirty-seven aur "
                "thirty-eight me dobara aata hai."
            ),
            ),
        ],
        "covers": ["R36-9", "R36-10-11", "R36-12", "R37-DEEM-TRAP"],
    },
    {
        "id": "c3_13_rule37_chain",
        "chapter": "CHAPTER 13 • RULE 37(1)-(8): A DEPARTMENT BECOMES A PSU",
        "title": "RULE 37(1)-(8) — FROM DEPARTMENT TO PSU, STEP BY STEP",
        "badge": "RULE 37(1)-(8)",
        "q": "When a Central department becomes a PSU, what happens to its staff and their pension, step by step?",
        "q_say": "Sir, Central department PSU ban jaye to staff aur pension ka step by step kya hota hai?",
        "hook": "REMEMBER: 5 years for rules, 3 months to opt, silence = absorbed, 2 years to return!",
        "hook_say": "Yaad rakhiye: paanch saal rules, teen mahine option, do saal wapsi.",
        "layout": "dashboard",
        "boxes": [
            (
                "STEP 1: DEEMED DEPUTATION",
                "All staff move together, as if lent on foreign service terms, with no deputation allowance. 37(1)",
                (
                "Rule 37(1): when a Central Government department is converted into a Public Sector Undertaking (PSU, a "
                "company owned by the Government), all its Government servants are transferred en masse to the body on "
                "deemed deputation on foreign-service terms, without any deputation allowance, from the date the "
                "Government notifies. Deemed deputation means treated as if lent for a time. [Verbatim Gazette text.]"
            ),
                SKY,
                (
                "Step one. Department PSU ban gaya to poori staff ek saath jati hai, deemed deputation par, foreign "
                "service terms par, bina deputation allowance. Jis date se Government notify kare. Ye sub-rule one."
            ),
            ),
            (
                "STEP 2: RULES AND OPTION",
                (
                "PSU makes rules in 5 years at most. Option window 3 months at most. No option means deemed to opt for "
                "absorption. 37(2)-(4)"
            ),
                (
                "Rule 37(2) has TWO clocks, not one. First: the PSU frames its own rules and regulations within a time "
                "frame not exceeding five years. Second: after those rules are notified, all Government servants on "
                "deemed deputation shall be asked, within a period not exceeding three months from the date of "
                "notification of the rules, to exercise the option to revert to Government or to seek permanent "
                "absorption. Third: those servants shall exercise the option within three months from the date of the "
                "communication asking them to opt. Rule 37(3): the option is exercised in the manner specified by the "
                "Government. Rule 37(4): a servant who does not exercise any option within the prescribed time is deemed "
                "to have opted for permanent absorption in the PSU. [Now settled against the verbatim Gazette text of "
                "Rule 37(2); the earlier flag on which date the three months run from is closed.]"
            ),
                BLUE,
                (
                "Step two. PSU apne rules paanch saal ke andar banati hai. Uske baad teen mahine ke andar staff se option "
                "maanga jata hai, aur employee ko phir teen mahine milte hain. Do clocks alag hain, agle chapter me "
                "detail. Sub-rule four: time par option na diya to deemed absorption."
            ),
            ),
            (
                "STEP 3: ABSORPTION",
                (
                "From the day the Government accepts the options they are no longer Government servants, deemed retired. "
                "Posts are abolished. 37(5)-(6)"
            ),
                (
                "Rule 37(5): absorption takes effect from the date the Government accepts the options; from that date "
                "they cease to be Government servants and are deemed retired. Rule 37(6): their posts are abolished."
            ),
                GREEN,
                (
                "Step three. Absorption us din se jab Government options accept karti hai. Us din se wo Government "
                "servants nahi rahte, deemed retired ho jate hain. Sub-rule six: unke posts abolish ho jate hain."
            ),
            ),
            (
                "STEP 4: RETURN, AND THE 2026 OFB PROVISO",
                (
                "Return within 2 years through the surplus cell. NEW proviso, 02.09.2026: ex-OFB staff who did NOT opt "
                "for DPSU absorption stay on deemed deputation till retirement."
            ),
                (
                "Rule 37(7): a servant who wishes to go back is repatriated within two years of the date he exercised the "
                "option and is redeployed through the surplus cell. Rule 37(8): the period between the option and the "
                "reversion continues as deemed deputation, on foreign service terms, without deputation allowance. "
                "PROVISO (inserted by G.S.R. 775(E), CCS (Pension) Amendment Rules, 2026, notified 2 September 2026, "
                "published 7 September 2026, File No. 4/27/2026-P&PW(D), in force from publication): nothing in sub-rule "
                "(7) applies to employees of the erstwhile Ordnance Factory Board, OTHER THAN OF Schools and OF "
                "Hospitals, who do NOT opt for absorption in the DPSUs; such employees continue on deemed deputation till "
                "retirement to the DPSUs created from conversion of its production units, on terms of foreign service "
                "without any deputation allowance. Verbatim Gazette text, G.S.R. 775(E)."
            ),
                RED,
                (
                "Step four. Wapas aana chahte hain to do saal ke andar repatriation, surplus cell se, beech me deemed "
                "deputation. Aur G.S.R. seven hundred seventy-five E, do September two thousand twenty-six, Rule "
                "thirty-seven, seven ke neeche naya proviso: Ordnance Factory Board ke jo employees DPSU me absorb nahi "
                "hue, wo retirement tak deemed deputation par rahenge, foreign service terms par, bina deputation "
                "allowance. OF Schools aur OF Hospitals isme nahi aate."
            ),
            ),
        ],
        "covers": ["R37-1", "R37-2-5YR", "R37-2-3MO", "R37-2-3MO-COMM", "R37-3", "R37-4", "R37-5", "R37-6", "R37-7", "R37-8", "GSR-775E-2026", "TL-R37"],
    },
    {
        "id": "c3_14_rule37_rest",
        "chapter": "CHAPTER 14 • RULE 37(9)-(29): PAY, DEARNESS RELIEF AND FUNDS",
        "title": "RULE 37(9)-(29) AND THE DEARNESS RELIEF CONTRAST WITH RULE 38",
        "badge": "RULE 37(9)-(29)",
        "q": "What do the rest of Rule 37's sub-rules say, and how does its dearness relief differ from Rule 38?",
        "q_say": (
            "Sir, Rule thirty-seven ke baaki sub-rules kya kehte hain, aur dearness relief Rule thirty-eight se kaise "
            "alag hai?"
        ),
        "hook": "REMEMBER: Rule 37 DR = IDA pattern. Rule 38 DR = Central DA pattern!",
        "hook_say": "Yaad rakhiye: thirty-seven me IDA pattern, thirty-eight me Central DA pattern.",
        "layout": "dashboard",
        "boxes": [
            (
                "SUB-RULES (9) TO (15)",
                (
                "(9) pay he would have drawn is emoluments. (10) Ministry fixes payment. (11) absorbed staff follow PSU "
                "rules. (12) options (a)/(b). (13)-(15) calculation."
            ),
                (
                "Rule 37(9): the pay he would have drawn is emoluments if he retires or dies on deemed deputation. (10): "
                "the Ministry specifies the payment. (11): absorbed staff (temporary staff included, casual labour "
                "excluded) follow the PSU's rules. (12): options (a) and (b). (13) to (15): calculation of benefits. "
                "Source covered Rule 37 only up to sub-rules (7)-(8) and (29)(c); this is from a rule summary, not the "
                "Gazette text (gap filled)."
            ),
                SKY,
                (
                "Aage chalkar. Sub-rule nine: deemed deputation me retirement ya death ho to jo Central pay milti, wahi "
                "emoluments. Payment ka tarika Ministry tay karti hai. Absorbed staff PSU rules follow karte hain, "
                "temporary included, casual labour excluded. Sub-rule twelve do options, aur thirteen se fifteen "
                "calculation."
            ),
            ),
            (
                "SUB-RULES (16) TO (21)",
                (
                "(16) option (b) staff get dearness relief on the IDA pattern. (17) voluntary retirement after 10 years "
                "of combined service. (18)-(21) pension fund trust and lump sum."
            ),
                (
                "Rule 37(16): employees under option (b) get dearness relief on the Industrial Dearness Allowance (IDA) "
                "pattern (resolved: the source only said it contrasts with Rule 38(15)). Rule 37(17): voluntary "
                "retirement after ten years' combined service under option (b). Rule 37(18) to (21): a Pension Fund "
                "trust, with the Secretary chairing the board, and a lump sum worked out with the 1981 table. Dearness "
                "relief (DR) is the pensioner's counterpart of dearness allowance."
            ),
                BLUE,
                (
                "Sub-rule sixteen favourite hai. Option b walon ko dearness relief industrial dearness allowance pattern "
                "par. Seventeen: dus saal ki combined service ke baad voluntary retirement. Eighteen se twenty-one: "
                "pension fund trust, aur nineteen eighty-one table se lump sum."
            ),
            ),
            (
                "SUB-RULES (22) TO (29)",
                (
                "(22)-(25) liability sharing, contributions, shortfall. (26)-(28) BSNL and MTNL. (29)(a) PF transfer, "
                "(29)(b) leave transfer, (29)(c) forfeiture, see next chapter."
            ),
                (
                "Rule 37(22) to (25): liability sharing, contributions, shortfall, and pre-conversion pensioners. Rule "
                "37(26) to (28): BSNL and MTNL. Rule 37(29)(a): provident fund transfer; (29)(b): earned leave and half "
                "pay leave transfer; (29)(c): the forfeiture clause amended by G.S.R. 340(E) of 22.05.2025 (next "
                "chapter). [Verbatim Gazette text, Rules 37(22) to 37(29)(c).]"
            ),
                GREEN,
                (
                "Twenty-two se twenty-five: liability sharing, contribution, aur shortfall. Twenty-six se twenty-eight: "
                "BSNL aur MTNL. Twenty-nine: clause a provident fund transfer, clause b earned aur half pay leave, clause "
                "c forfeiture, jo two thousand twenty-five me badla."
            ),
            ),
            (
                "THE TRAP: DR PATTERN",
                "Rule 37(16): IDA pattern. Rule 38(15): CENTRAL DA pattern. Silence = absorbed: 37(4), 38(3).",
                (
                "Contrast confirmed: Rule 37(16) IDA pattern against Rule 38(15) Central DA pattern. Numbering: deemed "
                "absorption on silence is Rule 37(4) and Rule 38(3); nothing equivalent in Rule 36. Cross-link: Rule "
                "38(14) Explanation and 38(19)-(21) lump sum."
            ),
                RED,
                (
                "Trap: Rule thirty-seven, sixteen IDA pattern, par Rule thirty-eight, fifteen Central DA pattern. Inhe "
                "alag rakhein. Aur silence par absorption, thirty-seven four aur thirty-eight three me."
            ),
            ),
        ],
        "covers": ["R37-9-15", "R37-16"],
    },
    {
        "id": "c3_15_rule38_body",
        "chapter": "CHAPTER 15 • RULE 38: A DEPARTMENT BECOMES A CENTRAL AUTONOMOUS BODY",
        "title": "RULE 38 — CONVERSION TO A CENTRAL AUTONOMOUS BODY",
        "badge": "RULE 38",
        "q": "How does Rule 38 treat a department that becomes a Central autonomous body?",
        "q_say": "Sir, Rule thirty-eight Central autonomous body wale conversion ko kaise dekhta hai?",
        "hook": "REMEMBER: Rule 38 = like 37, but Central DA pattern; temporary IN, casual labour OUT!",
        "hook_say": "Yaad rakhiye: Rule thirty-eight me Central DA pattern, temporary in, casual out.",
        "layout": "dashboard",
        "boxes": [
            (
                "THE MECHANICS: 38(1)-(13)",
                (
                "Same en-masse transfer and deemed deputation as Rule 37. Rules in 5 years, option in 3 months, silence = "
                "absorbed (38(3)). Temporary in, casual out."
            ),
                (
                "Rule 38(1): on conversion of a Department into an autonomous body, all Government servants of that "
                "Department are transferred en-masse to that body on deemed deputation on terms of foreign service "
                "without any deputation allowance, until they get absorbed, with effect from the date notified by the "
                "Government. Rule 38(2): the body frames its rules and regulations within a time frame not exceeding five "
                "years; after that, all employees on deemed deputation shall be asked, within three months of "
                "notification of those rules, to exercise the option to revert or to seek permanent absorption, and shall "
                "exercise it within three months of that communication. Rule 38(3): the option is exercised in the manner "
                "specified by the Government, and an employee who does not exercise any option within the prescribed time "
                "is DEEMED to have opted for permanent absorption in the body. Rule 38(4): absorption takes effect from "
                "the date the options are accepted, and from that date the employees cease to be Government servants and "
                "are deemed to have retired. Rule 38(5): the posts they held stand abolished. Rule 38(6): those who opt "
                "to revert are repatriated within two years of exercising the option, through the surplus cell. Rule "
                "38(7): the period between the option and the reversion continues as deemed deputation without deputation "
                "allowance. Rule 38(8): if an employee retires or dies during that deemed deputation, the Central pay he "
                "would have drawn is treated as emoluments. Rule 38(9): the benefits are drawn and paid in the manner "
                "specified by the administrative Ministry. Rule 38(10): employees, including temporary employees but "
                "EXCLUDING casual labourers, who opt for absorption are governed by the body's own rules from the date of "
                "absorption. Rule 38(11)(a),(b): the absorbed employee may opt either for Central pension or service "
                "gratuity and retirement gratuity under Rules 44 and 45, or to count the Central service in the body for "
                "pension and gratuity. Rules 38(12) and 38(13): under option (a) the Central pay he would have drawn is "
                "the emoluments, paid in the manner the Ministry specifies. [Verbatim Gazette text, Rule 38(1)-(13).]"
            ),
                SKY,
                (
                "Rule thirty-eight Rule thirty-seven ka pattern dohrata hai, sirf body Central autonomous body hoti hai. "
                "Staff deemed deputation par. Body paanch saal me rules banati hai, option teen mahine me. Chup rahe to "
                "deemed absorption, sub-rule three. Temporary in, casual labour out."
            ),
            ),
            (
                "PENSION AND RELIEF: 38(14)-(15)",
                (
                "Pension is worked out as if he retired from Central service that very day. Dearness relief follows the "
                "Central DA pattern."
            ),
                (
                "Rule 38(14) Explanation: pension is calculated as if he were a servant retiring (or dying) from Central "
                "service on the same day. Rule 38(15): dearness relief on the Central DA pattern (contrast Rule 37(16), "
                "IDA)."
            ),
                BLUE,
                (
                "Explanation to sub-rule fourteen: pension aise nikalti hai jaise usi din Central service se retirement "
                "hua ho. Sub-rule fifteen: dearness relief Central dearness allowance pattern par, industrial par nahi."
            ),
            ),
            (
                "THE FUND AND THE LUMP SUM",
                (
                "A Pension Fund trust is set up; the Secretary of the Ministry chairs its board. The Government may pay a "
                "lump sum by the 1981 table."
            ),
                (
                "Rule 38(16): Pension Fund trust. Rule 38(17): the Secretary of the administrative Ministry chairs the "
                "Board of Trustees. Rule 38(18): procedure. Rule 38(19) to (21): the Government makes a lump-sum one-time "
                "payment, the capitalised value taken from the 1981 commutation table."
            ),
                GREEN,
                (
                "Sub-rules sixteen aur seventeen Pension Fund trust banate hain, board ka chairperson Ministry ka "
                "Secretary. Nineteen se twenty-one me Government ek hi baar ke lump sum se apni liability clear kar sakti "
                "hai, nineteen eighty-one table se capitalised value."
            ),
            ),
            (
                "LIABILITY: 38(22)-(25)",
                (
                "The body pays into the Fund to stand on its own feet. If the Fund falls short, the Government is "
                "responsible. Earlier pensioners remain the Government's burden."
            ),
                (
                "Rule 38(22): liability sharing. Rule 38(23) to (25): the body contributes to the Fund so that it becomes "
                "self-supporting; a shortfall is met by the Government; pensioners who retired before the conversion "
                "remain the Government's liability. Q&A from the source: who is included and who is excluded? Temporary "
                "employees are included; casual labourers are excluded (Rule 38(10))."
            ),
                ORANGE,
                (
                "Aur liability. Body Fund me contribute karti hai taaki wo khud khadi ho. Shortfall ho to Government "
                "bharegi. Aur conversion se pehle retired logon ki zimmedari Government ki hi rehti hai."
            ),
            ),
        ],
        "covers": ["R37-38-ENMASSE", "R38-10", "R38-14-EXPL", "R38-15", "R38-16-17", "R38-19-21", "R38-23-25", "R38-GAP"],
    },
    {
        "id": "c3_16_rule37_29c_2025",
        "chapter": "CHAPTER 16 • RULE 37(29)(c): THE 2025 AMENDMENT",
        "title": "RULE 37(29)(c) — THE 2025 AMENDMENT THAT REMOVED THE SHIELD",
        "badge": "G.S.R. 340(E)",
        "q": "What changed in Rule 37(29)(c) in 2025, and what is the old note that is now wrong?",
        "q_say": (
            "Sir, Rule thirty-seven, twenty-nine, c me two thousand twenty-five me kya badla, aur kaunsa purana note "
            "ab galat hai?"
        ),
        "hook": "REMEMBER: Since 22.05.2025, dismissal or removal by the PSU forfeits Government-service benefits too!",
        "hook_say": (
            "Yaad rakhiye: May two thousand twenty-five se PSU dismissal Government service ke benefits bhi kha jati "
            "hai."
        ),
        "layout": "dashboard",
        "boxes": [
            (
                "THE CITATION",
                (
                "G.S.R. 340(E) dated 22 May 2025, File No. 04/17/2023-P&PW(D), CCS (Pension) Amendment Rules, 2025. In "
                "force from publication."
            ),
                (
                "G.S.R. 340(E) of 22 May 2025, Central Civil Services (Pension) Amendment Rules, 2025, F.No. "
                "04/17/2023-P&PW(D), signed by the Joint Secretary; in force on the date of publication in the Official "
                "Gazette. It substitutes only Rule 37(29)(c). Substitution read from the PIB release and a re-hosted copy "
                "of the notification; the Gazette PDF was not opened."
            ),
                SKY,
                (
                "Citation: G.S.R. three hundred forty E, twenty-second May two thousand twenty-five, Central Civil "
                "Services Pension Amendment Rules two thousand twenty-five, file number zero four by seventeen by two "
                "thousand twenty-three, P and PW D. Publication ki date se lagu, aur sirf ek clause badla, Rule "
                "thirty-seven, twenty-nine, c."
            ),
            ),
            (
                "OLD AGAINST NEW",
                (
                "OLD: dismissal or removal after absorption did NOT take away the Government-service benefits. NEW: it "
                "DOES (forfeiture)."
            ),
                (
                "Old position (pre-2025 text): dismissal or removal for later misconduct after absorption in the PSU was "
                "not a forfeiture of the retirement benefits earned in Government service. New position: if the PSU "
                "dismisses or removes the employee for subsequent misconduct after absorption, the retirement benefits "
                "for Government service are forfeited too. Forfeited means lost. Example (invented): Lata, absorbed in a "
                "PSU in 2024, is dismissed there for misconduct in 2026; under the new clause her pension for her "
                "Government years can also be forfeited."
            ),
                ORANGE,
                (
                "Pehle: absorption ke baad PSU ne dismiss ya remove kiya to Government service ke benefits safe the. Ab: "
                "wo bhi forfeit. Example: Lata two thousand twenty-four me PSU me absorbed hui, two thousand twenty-six "
                "me misconduct par dismissed, ab uske Government ke saalon ki pension bhi ja sakti hai."
            ),
            ),
            (
                "TRIGGERS AND REVIEW",
                (
                "Only DISMISSAL and REMOVAL trigger forfeiture. Retrenchment does not. The administrative Ministry "
                "reviews the PSU decision."
            ),
                (
                "Triggers: dismissal and removal only. Retrenchment is not a forfeiture trigger; it appears only in the "
                "review limb. The PSU's decision on dismissal, removal or retrenchment is subject to review by the "
                "Ministry administratively connected with the undertaking. New Explanation: the relevant provisions of "
                "Rules 7 and 8, Rule 41 and Rule 44(5) apply analogously to the PSU employee as to a Government servant."
            ),
                GREEN,
                (
                "Triggers dhyan se. Sirf dismissal aur removal se forfeiture hoti hai. Retrenchment trigger nahi hai, wo "
                "sirf review wale hisse me aata hai. PSU ka decision administrative Ministry review karti hai."
            ),
            ),
            (
                "THE TRAP AND THE LINK",
                (
                "Notes saying 'Government pension stays safe' are now WRONG. Rule 8 was rewritten in 2022 (G.S.R. 770(E), "
                "07.10.2022)."
            ),
                (
                "Trap: older notes that say the Government-service pension stays safe after PSU dismissal are obsolete "
                "(OBSOLETE / HISTORY ONLY, replaced by the 2025 clause). Link: G.S.R. 770(E) of 07.10.2022 substituted "
                "sub-rule (1) of Rule 8, amended sub-rules (2), (4) and (6) and inserted (6A); that notification also "
                "amended Rules 20, 46, 50 and 76 and did not touch Rules 31 to 41 directly. The 2025 Explanation imports "
                "the rewritten Rule 8. The source's 'three authorities under Rule 8' was not re-checked here (see Batch "
                "1)."
            ),
                RED,
                (
                "Trap: purane note jo kehte hain Government pension safe rehti hai, ab galat hain. October two thousand "
                "twenty-two me G.S.R. seven hundred seventy E ne Rule eight rewrite kiya, aur two thousand twenty-five ki "
                "Explanation us Rule eight ko PSU employees par le aayi."
            ),
            ),
        ],
        "covers": ["R37-29C-OLD", "R37-29C-NEW", "GSR-340E-2025", "R37-29C-RETRENCH", "R37-29C-EXPL", "GSR-770E-2022"],
    },
    {
        "id": "c3_17_rule39_gateway",
        "chapter": "CHAPTER 17 • RULE 39(1)-(2): INVALID PENSION, THE TWO GATEWAYS",
        "title": "RULE 39(1)-(2) — INVALID PENSION: WHICH GATEWAY APPLIES?",
        "badge": "RULE 39(1)-(2)",
        "q": "Who can ask for invalid pension, and what is the first check under Rule 39?",
        "q_say": "Sir, invalid pension kaun maang sakta hai, aur Rule thirty-nine me pehla check kya hai?",
        "hook": "REMEMBER: Check RPwD Section 20 first; if it does not apply, apply to the Head of Department!",
        "hook_say": "Yaad rakhiye: pehla sawaal Section twenty, tabhi sub-rule two.",
        "layout": "dashboard",
        "boxes": [
            (
                "GATEWAY 1: THE RPwD ACT • 39(1)",
                (
                "If Section 20 of the RPwD Act, 2016 applies, THAT section governs, with a disability certificate from "
                "the authority under the RPwD Rules, 2017."
            ),
                (
                "Rule 39(1): where Section 20 of the Rights of Persons with Disabilities Act, 2016 applies, the case is "
                "dealt with under that section, and under its proviso the employee must produce a disability certificate "
                "from the competent authority prescribed in the RPwD Rules, 2017. [Verbatim Gazette text of Rule 39(1). "
                "The RPwD Act, 2016 itself was not re-read this round.]"
            ),
                SKY,
                (
                "Pehle gateway ek. Sabse pehle check karein, Rights of Persons with Disabilities Act, two thousand "
                "sixteen ki Section twenty lagti hai ya nahi. Lagti hai to wahi section chalega, aur RPwD Rules two "
                "thousand seventeen ke competent authority ka disability certificate chahiye. Ye Rule thirty-nine, one."
            ),
            ),
            (
                "GATEWAY 2: INVALID PENSION • 39(2)",
                (
                "If Section 20 does NOT apply and a body or mind problem permanently stops him working, he may apply to "
                "the Head of Department for invalid pension."
            ),
                (
                "Rule 39(2): where Section 20 does not apply and a Government servant is permanently incapacitated for "
                "service by bodily or mental infirmity, he may apply to the Head of Department for retirement on invalid "
                "pension. Invalid pension means pension for someone who has to leave service because of permanent ill "
                "health. [Verbatim Gazette text.]"
            ),
                BLUE,
                (
                "Ab gateway do, sub-rule two. Section twenty nahi lagti, aur koi bodily ya mental infirmity permanently "
                "service ke liye unfit kar deti hai, to Head of Department ko invalid pension ki application. Invalid "
                "pension matlab permanent ill health ki wajah se retirement."
            ),
            ),
            (
                "THE TWO PROVISOS",
                (
                "(1) If he cannot apply himself, his spouse, else a family member, may. (2) If Section 20 applies but he "
                "still wants invalid pension, he is advised he can stay on the same scale and benefits."
            ),
                (
                "First proviso to Rule 39(2): if the Head of Department is satisfied the servant cannot apply because of "
                "his condition, the spouse, or failing that a family member, may apply. Second proviso: if Section 20 "
                "applies but the servant still wishes to retire under this rule, he shall be advised that he may continue "
                "in service on the same pay scale and service benefits; only if he does not withdraw the request does the "
                "matter proceed. Example (invented): Dev has a severe condition and cannot sign; his wife applies."
            ),
                GREEN,
                (
                "Do provisos. Pehla: khud apply nahi kar sakta to spouse, na ho to family ka member. Example: Dev sign "
                "nahi kar sakta, to patni apply karti hai. Doosra: Section twenty lagti hai par wo phir bhi invalid "
                "pension chahta hai, to use bataya jata hai ki same pay scale aur benefits par service continue kar sakta "
                "hai."
            ),
            ),
            (
                "THE TRAP",
                "Do not skip gateway 1. Check Section 20 FIRST. Rule 39(2) is the fallback.",
                (
                "Trap: candidates skip the RPwD gateway and go straight to invalid pension. Rule 39(1) comes first; Rule "
                "39(2) applies only where Section 20 does not. Reference ids: RPwD Act 2016, Section 20; RPwD Rules 2017."
            ),
                RED,
                (
                "Trap: log seedha invalid pension par kood jaate hain. Pehla sawaal hamesha Section twenty hai. Nahi "
                "lagti, tabhi sub-rule two."
            ),
            ),
        ],
        "covers": ["R39-1", "R39-2", "R39-2-PROV1", "R39-2-PROV2", "RPWD-S20"],
    },
    {
        "id": "c3_18_rule39_timeline",
        "chapter": "CHAPTER 18 • RULE 39(3)-(7): THE MEDICAL PROCESS AND ITS CLOCKS",
        "title": "RULE 39(3)-(7) — WHO EXAMINES, AND THE 15, 30 AND 45 DAY CLOCKS",
        "badge": "RULE 39(3)-(7)",
        "q": "What is the step-by-step medical process for invalid pension, and who runs which clock?",
        "q_say": "Sir, invalid pension ka medical process step by step kya hai, aur kaun kaun si clock chalti hai?",
        "hook": "REMEMBER: 15 days from application, 30 from request, 45 from Format 6!",
        "hook_say": "Yaad rakhiye: pandrah, tees, paintalis — teen clocks, teen shuruaat.",
        "layout": "dashboard",
        "boxes": [
            (
                "STEP 1: APPLY",
                "Servant, spouse or family member applies to the Head of Department. 39(2)",
                "Step 1 (Rule 39(2) with provisos): the application goes to the Head of Department.",
                SKY,
                "Step one. Servant, ya spouse, ya family ka member, Head of Department ko apply karta hai.",
            ),
            (
                "STEP 2: REQUEST IN 15 DAYS",
                "Within 15 days of the application the Head of Office or Department sends the medical request. 39(3)",
                (
                "Rule 39(3): the Head of Office or Head of Department shall, within fifteen days of the receipt of the "
                "application, request the medical authority for examination of the Government servant, not later than "
                "thirty days from the date of receipt of that request. Rule 39(4): the Head of Office or Department "
                "supplies the medical authority with a statement of what appears from official records to be the age of "
                "the applicant, and, if a service book is maintained, the age recorded in it must also be reported; a "
                "copy of the letter requesting the examination is endorsed to the Government servant. So BOTH ages travel "
                "with the file. [Now settled against the verbatim Gazette text; the earlier flag is closed.]"
            ),
                BLUE,
                (
                "Step two. Application ke pandrah din ke andar Head of Office ya Department medical examination ki "
                "request bhejta hai. Official record wali age saath jati hai, service book maintain hoti hai to uski age "
                "bhi report hoti hai, aur letter ki copy employee ko milti hai."
            ),
            ),
            (
                "STEP 3: EXAMINE IN 30 DAYS",
                (
                "Exam within 30 days of the request. Medical Board if Gazetted or pay above Rs 54,000; else Civil "
                "Surgeon."
            ),
                (
                "Rule 39(3): the examination must take place within 30 days of the request. Authority map: a Medical "
                "Board for Gazetted Government servants and for non-Gazetted servants whose pay is above Rs 54,000 per "
                "month; for all others the Civil Surgeon, District Medical Officer or Medical Officer of equivalent "
                "status. The Rs 54,000 figure is dynamic: seen in the rule summary; no revision found up to 21.10.2026 in "
                "a limited search; check the latest O.M. Clock 2: 30 days from the request."
            ),
                GREEN,
                (
                "Step three. Request ke tees din ke andar examination. Gazetted, ya fifty-four hazaar se zyada pay wale "
                "non-Gazetted ke liye Medical Board, baaki ke liye Civil Surgeon ya District Medical Officer. Threshold "
                "Fundamental Rule nine, twenty-one ki pay par hai, Rule thirty-one emoluments par nahi."
            ),
            ),
            (
                "STEP 4: THE OUTCOME",
                (
                "Fit, or fit for lighter work. No certificate without the Head's request. Lady doctor for a woman. "
                "39(5)-(7)"
            ),
                (
                "Rule 39(5): the examination decides whether he is fit, or fit for lighter work. Rule 39(6): no "
                "certificate can be given without a request from the Head of Office or Head of Department, so an employee "
                "cannot bring his own doctor's certificate. Rule 39(7): when a woman is examined, the Medical Board must "
                "include a lady doctor. Then pension in 45 days of Format 6 (next chapter)."
            ),
                ORANGE,
                (
                "Step four, outcome. Fit, ya halke kaam ke liye fit. Head ki request ke bina koi certificate nahi, "
                "private certificate kaam nahi aayega. Aur mahila ki examination me Board me lady doctor zaroori hai."
            ),
            ),
            (
                "THE TRAP: WHEN DOES 45 START?",
                "The 45 days run from receiving the Format 6 certificate, NOT from the application.",
                (
                "Trap: three clocks with three different starting points. 15 days from the application; 30 days from the "
                "request; 45 days from receipt of the Format 6 certificate. Candidates count 45 days from the "
                "application, which is wrong. Remember: figure from the current O.M., principle from the Rule."
            ),
                RED,
                (
                "Trap: teen clocks, teen shuruaat. Pandrah din application se, tees din request se, paintalis din Format "
                "six certificate milne se. Paintalis din application se mat ginein."
            ),
            ),
        ],
        "covers": ["R39-3-15", "R39-3-30", "R39-3-AUTH", "LIMIT-39-54000", "R39-4", "R39-5", "R39-6", "R39-7", "TL-R39"],
    },
    {
        "id": "c3_19_rule39_pension",
        "chapter": "CHAPTER 19 • RULE 39(8)-(10): THE CERTIFICATE AND THE PENSION",
        "title": "RULE 39(8)-(10) — FORMAT 6, THE 50 PERCENT PENSION AND NO 10-YEAR TEST",
        "badge": "RULE 39(8)-(10)",
        "q": "How much invalid pension is paid, and is ten years of qualifying service needed?",
        "q_say": "Sir, invalid pension kitni milti hai, aur kya das saal ki qualifying service chahiye?",
        "hook": "REMEMBER: Invalid pension = 50% of the better of emoluments or average; NO 10-year test!",
        "hook_say": "Yaad rakhiye: invalid pension me das saal ka test nahi.",
        "layout": "dashboard",
        "boxes": [
            (
                "SUB-RULE (8): FORMAT 6",
                (
                "The medical certificate is in Format 6. If he is unfit for further service, invalid pension is granted "
                "within 45 days of receiving it."
            ),
                (
                "Rule 39(8): the medical certificate is in Format 6 (a medical-board format, not to be confused with the "
                "general Form 6 that G.S.R. 410(E) of 2024 changed to Form 6-A). If he is found unfit for further "
                "service, invalid pension is granted under Rule 44 within 45 days of receipt of the Format 6 certificate. "
                "[Verbatim Gazette text.]"
            ),
                SKY,
                (
                "Pehle sub-rule eight. Medical certificate Format six me hota hai. Further service ke liye unfit mile, to "
                "Format six milne ke paintalis din ke andar Rule forty-four se invalid pension. Ye Format six medical "
                "wala hai, general Form six nahi jo two thousand twenty-four me Form six A ban gaya."
            ),
            ),
            (
                "SUB-RULE (9): THE AMOUNT",
                (
                "Invalid pension is paid even with LESS than 10 years of qualifying service, at 50 percent of emoluments "
                "or average emoluments, whichever is better."
            ),
                (
                "Rule 39(9): a Government servant who retires even before completing ten years of qualifying service is "
                "also granted invalid pension, calculated at fifty per cent of emoluments or average emoluments, "
                "whichever is more beneficial, under Rule 44. Proviso conditions: (a) he has been examined by the "
                "appropriate medical authority EITHER before his appointment OR after his appointment to Government "
                "service and declared fit for Government service; and (b) he fulfils all other conditions of Rule 39 for "
                "grant of invalid pension. The words are 'either before his appointment or after his appointment'. [Now "
                "settled against the verbatim Gazette text; the earlier flag is closed.]"
            ),
                ORANGE,
                (
                "Ab amount, sub-rule nine. Das saal se kam qualifying service par bhi invalid pension milti hai. Fifty "
                "percent emoluments ya average emoluments ka, jo behtar ho. Condition: pehle medical authority ne "
                "Government service ke liye fit declare kiya ho, aur baaki conditions poori hon. Appointment se pehle ya "
                "baad, dono chalega."
            ),
            ),
            (
                "SUB-RULE (10) AND AN EXAMPLE",
                (
                "Fit for lighter work and willing? He is placed on a lower post. If none, he may be admitted to invalid "
                "pension."
            ),
                (
                "Rule 39(10): if he is found fit for lighter work and is willing, he is placed on a lower post; if there "
                "is no such post, he may be admitted to invalid pension. Example (invented, recomputed): Charu, a "
                "non-Gazetted employee with pay of Rs 60,000 a month (above Rs 54,000), has seven years of qualifying "
                "service; a Medical Board finds her unfit; Format 6 is issued; her pension is 50% of Rs 60,000 = Rs "
                "30,000 a month (if her average emoluments are not higher), above the Rs 9,000 floor, granted within 45 "
                "days of the Format 6."
            ),
                BLUE,
                (
                "Sub-rule ten dayalu hai. Halke kaam ke liye fit aur willing ho to lower post par rakha jayega, post na "
                "ho to invalid pension. Example: Charu non-Gazetted, pay sixty hazaar, saat saal service. Board ne unfit "
                "kaha, Format six mila, invalid pension thirty hazaar per month, paintalis din me."
            ),
            ),
            (
                "THE TRAP",
                "No 10-year rule here. A 2023 DoPPW O.M. on a different 1972-Rules point is NOT part of this rule.",
                (
                "Trap: invalid pension needs no ten-year qualifying service under Rule 39(9). Peripheral note, not needed "
                "for the card: DoPPW 38/03(03)/2023-P&PW(A) of 16.01.2023 (MHA reference) dispensed with certain "
                "1972-Rules provisions from 04.01.2019 and says the 10-year condition does not apply to disability "
                "pension under the Extraordinary Pension Rules; do not mix it with Rule 39 of the 2021 Rules. Wording of "
                "the O.M. itself not read."
            ),
                RED,
                (
                "Trap: invalid pension me das saal ka test nahi hai. Two thousand twenty-three ka DoPPW office memorandum "
                "kisi doosre point par hai, use is rule me mat milayein."
            ),
            ),
        ],
        "covers": ["R39-8-45", "FORMAT-6", "R39-9", "R39-10", "R39-EX", "OM-16.01.2023-INVALID"],
    },
    {
        "id": "c3_20_rule40_rule",
        "chapter": "CHAPTER 20 • RULE 40: COMPULSORY RETIREMENT PENSION, THE RULE",
        "title": "RULE 40(1)-(5) — PENSION AFTER COMPULSORY RETIREMENT AS A PENALTY",
        "badge": "RULE 40",
        "q": "If a servant is compulsorily retired as a penalty, how much pension can he get, and who decides?",
        "q_say": (
            "Sir, penalty ke taur par compulsory retirement ho to pension kitni mil sakti hai, aur faisla kaun karta "
            "hai?"
        ),
        "hook": "REMEMBER: Rule 40 = two-thirds is the FLOOR; provisional two-thirds at once; final order in 3 months!",
        "hook_say": "Yaad rakhiye: Rule forty me do-tihai floor hai, aur UPSC poore se kam par.",
        "layout": "dashboard",
        "boxes": [
            (
                "THE RULE • RULE 40(1)",
                (
                "The authority may grant pension, gratuity or both, not less than TWO-THIRDS and not more than the FULL "
                "superannuation amount."
            ),
                (
                "Rule 40(1): a Government servant compulsorily retired as a penalty may be granted, by the authority "
                "competent to impose that penalty, pension or retirement gratuity or both at a rate not less than "
                "two-thirds and not more than the full amount of the superannuation pension or gratuity admissible on the "
                "date of compulsory retirement. Floor two-thirds, ceiling full. Compulsory retirement means being made to "
                "retire as a punishment. [Verbatim Gazette text.]"
            ),
                SKY,
                (
                "Pehle rule. Yahan compulsory retirement ek penalty hai. Jo authority penalty laga sakti hai wahi "
                "pension, retirement gratuity, ya dono de sakti hai. Superannuation pension ya gratuity ke kam se kam "
                "do-tihai, aur poore amount se zyada nahi. Floor do-tihai, ceiling poora."
            ),
            ),
            (
                "SUB-RULE (2): THE PRESIDENT AND UPSC",
                (
                "If the President gives LESS than the full amount, the Union Public Service Commission is consulted "
                "BEFORE the order. 'Pension' includes retirement gratuity here."
            ),
                (
                "Rule 40(2): whenever, in the case of a Government servant, the President passes an order (whether "
                "ORIGINAL, APPELLATE or in exercise of the power of REVIEW) awarding a pension less than the full "
                "superannuation pension admissible under these rules, the Union Public Service Commission shall be "
                "consulted before such order is passed. Explanation to Rule 40(2): for this sub-rule, 'pension' includes "
                "retirement gratuity. So all three order-types are expressly covered. [Now settled against the verbatim "
                "Gazette text; the earlier flag is closed.]"
            ),
                BLUE,
                (
                "Sub-rule two. President poore se kam amount ka order dein to UPSC se pehle consult karna hoga. "
                "Explanation kehti hai yahan pension me retirement gratuity bhi hai. Aur Gazette text confirm karta hai, "
                "order original ho, appellate ho, ya review me, teeno."
            ),
            ),
            (
                "SUB-RULES (3) AND (4): THE CLOCK",
                (
                "The amount may be fixed with the penalty. If not, two-thirds is paid at once as PROVISIONAL pension. "
                "Final order within 3 months."
            ),
                (
                "Rule 40(3): the quantum order may be passed with the penalty order; if not, provisional pension or "
                "gratuity at two-thirds is sanctioned immediately. Rule 40(4): the final order is passed within three "
                "months of the penalty order, after consulting the UPSC if needed; provisional payment continues until "
                "then. Provisional means temporary until the final order."
            ),
                GREEN,
                (
                "Sub-rule three. Amount penalty order ke saath hi tay ho sakta hai. Na ho to turant do-tihai provisional "
                "pension aur gratuity. Sub-rule four: final order penalty order ke teen mahine ke andar, UPSC se consult "
                "karke. Provisional tab tak chalta rahega."
            ),
            ),
            (
                "SUB-RULE (5) AND THE TRAP",
                "The amount can never fall below the Rule 44 minimum pension (Rs 9,000 a month, check the latest O.M.).",
                (
                "Rule 40(5): the amount shall not be less than the minimum pension under Rule 44 (Rs 9,000 per month "
                "under Rule 44(1), a dynamic figure; check the latest O.M.). Trap: two-thirds is a floor in Rule 40 but a "
                "ceiling in Rule 41 (see chapter 22)."
            ),
                RED,
                (
                "Sub-rule five safety net hai: Rule forty-four ke minimum pension se kam nahi, abhi nau hazaar per month, "
                "latest O.M. check kar lein. Trap: do-tihai yahan Rule forty me floor hai, Rule forty-one me ceiling."
            ),
            ),
        ],
        "covers": ["R40-1", "R40-2", "R40-2-ORIG", "R40-3", "R40-4", "R40-5"],
    },
    {
        "id": "c3_21_rule40_examples",
        "chapter": "CHAPTER 21 • RULE 40: TWO WORKED EXAMPLES",
        "title": "RULE 40 — RAMESH'S THREE CASES AND SURESH'S PROVISIONAL PENSION",
        "badge": "RULE 40 • EXAMPLES",
        "q": "Can you show Rule 40 with numbers, including the provisional pension?",
        "q_say": "Sir, Rule forty ko numbers ke saath dikhayein, provisional pension ke saath?",
        "hook": "REMEMBER: Floor = 2/3 of the superannuation figure; less than full means UPSC first!",
        "hook_say": "Yaad rakhiye: pehle admissible superannuation figure, phir do-tihai, neeche nahi.",
        "layout": "dashboard",
        "boxes": [
            (
                "RAMESH: CASE A AND B",
                (
                "Pension 60,000 and gratuity 18,00,000. Full: 60,000 and 18,00,000, no UPSC. Two-thirds: 40,000 and "
                "12,00,000, UPSC first."
            ),
                (
                "Source example (the facts 'Under Secretary, compulsorily retired on 31.12.2025' are invented): "
                "admissible superannuation pension Rs 60,000 a month; retirement gratuity Rs 18,00,000. Case A, President "
                "gives full benefit: pension Rs 60,000, gratuity Rs 18,00,000; no UPSC consultation needed. Case B, "
                "two-thirds: 60,000 x 2/3 = Rs 40,000; 18,00,000 x 2/3 = Rs 12,00,000; UPSC consultation needed before "
                "the order."
            ),
                SKY,
                (
                "Shri Ramesh, thirty-first December two thousand twenty-five ko compulsorily retired. Superannuation "
                "pension sixty hazaar, gratuity eighteen lakh. Case A: poora benefit, sixty hazaar aur eighteen lakh, "
                "UPSC ki zaroorat nahi. Case B: do-tihai, forty hazaar aur twelve lakh, ab UPSC consult hogi."
            ),
            ),
            (
                "RAMESH: CASE C",
                "Fifty percent is NOT allowed: it is below the two-thirds floor.",
                (
                "Case C: the President wishes to give 50 percent: pension Rs 30,000, gratuity Rs 9,00,000. NOT ALLOWED, "
                "because it falls below the two-thirds floor of Rule 40(1). Check: two-thirds of 60,000 is 40,000, and "
                "30,000 is less."
            ),
                RED,
                (
                "Case C: President aadha dena chahein. Aadha matlab tees hazaar, jo forty hazaar se kam hai, allowed "
                "nahi, kyunki do-tihai floor hai."
            ),
            ),
            (
                "SURESH: THE PROVISIONAL CLOCK",
                (
                "Penalty order 1 Jan 2026, quantum order 15 Mar 2026 at two-thirds. Provisional pension 33,334 from 1 "
                "Jan; final amount the same."
            ),
                (
                "Example 15: Suresh, admissible pension Rs 50,000; penalty order 1 January 2026; quantum order 15 March "
                "2026 at two-thirds (within the three months of Rule 40(4)). Provisional two-thirds from 1 January 2026: "
                "50,000 x 2/3 = 33,333.33; under Rule 44(9) a fraction is rounded up, so Rs 33,334 (the source said "
                "33,333; status: changed). UNVERIFIED point: whether Rule 44(9) rounding applies to a provisional "
                "pension; it says amounts are in whole rupees with the fraction rounded up. After the quantum order the "
                "same amount becomes final."
            ),
                ORANGE,
                (
                "Ab Suresh, admissible pension fifty hazaar. Penalty order first January two thousand twenty-six, quantum "
                "order fifteenth March, teen mahine ke andar. Pehli January se provisional pension. Fifty hazaar ka "
                "do-tihai thirty-three thousand three hundred thirty-three point three, Rule forty-four, nine se upar "
                "round, thirty-three thousand three hundred thirty-four."
            ),
            ),
            (
                "THE TRAP",
                (
                "Always do the sum from the admissible superannuation figure, and remember the order may not drop below "
                "2/3."
            ),
                (
                "Check method: (1) find the admissible superannuation pension and gratuity on the date of compulsory "
                "retirement; (2) multiply by 2/3 for the floor; (3) anything between 2/3 and full is allowed; (4) below "
                "2/3 is not; (5) UPSC first whenever the President gives less than full. Q&A from the source: President "
                "gives less than full, what is needed? UPSC consultation before the order, and half or less is not "
                "allowed."
            ),
                GREEN,
                (
                "Trap: hamesha admissible superannuation figure se shuru karein, phir do-tihai. Do-tihai se poore tak "
                "kuch bhi chalega, neeche kuch nahi. Aur poore se kam dete waqt UPSC pehle."
            ),
            ),
        ],
        "covers": ["R40-EX-RAMESH", "R40-EX-SURESH"],
    },
    {
        "id": "c3_22_rule40_vs_41",
        "chapter": "CHAPTER 22 • RULE 40 AGAINST RULE 41: FLOOR AGAINST CEILING",
        "title": "RULES 40 AND 41 — TWO-THIRDS AS A FLOOR AND AS A CEILING",
        "badge": "RULES 40 vs 41",
        "q": "Both rules use two-thirds. How do we keep them apart, and what do they share?",
        "q_say": "Sir, dono rules me do-tihai hai. Inhe alag kaise rakhein, aur kya common hai?",
        "hook": (
            "REMEMBER: Rule 40 = at least 2/3 (floor). Rule 41 = at most 2/3 (ceiling). Both: 3 months, Rule 44 "
            "minimum!"
        ),
        "hook_say": "Yaad rakhiye: forty me floor, forty-one me ceiling.",
        "layout": "dashboard",
        "boxes": [
            (
                "FLOOR AGAINST CEILING",
                "Rule 40: not LESS than two-thirds, not more than full. Rule 41: NOT MORE than two-thirds.",
                (
                "Rule 40(1): compulsory retirement: two-thirds is a FLOOR (not less than two-thirds, not more than the "
                "whole). Rule 41(1) proviso: compassionate allowance: two-thirds is a CEILING (not more than two-thirds "
                "of the pension or gratuity that would have been admissible on superannuation). Confirmed. [Verbatim "
                "Gazette text.]"
            ),
                SKY,
                (
                "Yahi key difference hai. Rule forty me do-tihai floor hai, neeche nahi ja sakte. Rule forty-one me "
                "do-tihai ceiling hai, upar nahi ja sakte. Ek neeche rokta hai, doosra upar."
            ),
            ),
            (
                "THE SAME THREE-MONTH WINDOW",
                "Both need the final decision within 3 months of the penalty order: Rule 40(4) and Rule 41(2).",
                (
                "Time limits: Rule 40(4): final order within three months of the penalty order. Rule 41(2): decision "
                "within three months of the penalty order. Rule 41(4) and (5) add a separate six-month transitional "
                "window for cases undecided at commencement of the Rules. Summary of time limits: 3 months in 40(4) and "
                "41(2); 6 months in 41(4)."
            ),
                BLUE,
                (
                "Dono me teen mahine ki window hai, Rule forty, four aur Rule forty-one, two. Rule forty-one me purane "
                "undecided cases ke liye alag chhah mahine bhi hain."
            ),
            ),
            (
                "THE SAME SAFETY NET",
                "Both are subject to the Rule 44 minimum pension: Rule 40(5) and Rule 41(6).",
                (
                "Rule 40(5) and Rule 41(6): the amount is never less than the minimum pension under Rule 44 (Rs 9,000 per "
                "month under Rule 44(1), dynamic; check the latest O.M.). Both also act at the end of a penalty: Rule 40 "
                "compulsory retirement, Rule 41 dismissal or removal."
            ),
                GREEN,
                (
                "Dono me ek hi safety net hai, Rule forty-four ka minimum pension, Rule forty, five aur Rule forty-one, "
                "six. Dono penalty case ke end me lagte hain."
            ),
            ),
            (
                "PROVISIONAL TWO-THIRDS",
                "Only Rule 40 guarantees an immediate provisional two-thirds while the final amount is decided (40(3)).",
                (
                "Rule 40(3) provisional two-thirds: the employee gets a predictable amount immediately after the penalty "
                "while the final quantum is decided. Rule 41 has no equivalent automatic provisional payment in the "
                "sub-rules read. Memory line: Rule 40, the employee chose nothing and keeps at least two-thirds; Rule 41, "
                "he lost everything and can get at most two-thirds."
            ),
                ORANGE,
                (
                "Ek aur farq. Rule forty me sub-rule three se turant provisional do-tihai milta hai, to amount "
                "predictable hota hai. Rule forty-one, one poori forfeiture se shuru hota hai, aur allowance ek favour "
                "hai, do-tihai tak. Floor forty me, ceiling forty-one me."
            ),
            ),
        ],
        "covers": ["R40-VS-R41", "R40-R41-3MONTH", "R40-R41-MIN", "R40-3-PROVISIONAL", "LIMIT-2THIRDS", "TL-R40-41"],
    },
    {
        "id": "c3_23_rule41_allowance",
        "chapter": "CHAPTER 23 • RULE 41: COMPASSIONATE ALLOWANCE",
        "title": "RULE 41 — DISMISSED OR REMOVED: FORFEITURE AND COMPASSIONATE ALLOWANCE",
        "badge": "RULE 41",
        "q": "If a servant is dismissed or removed, does he lose everything, and what is a compassionate allowance?",
        "q_say": "Sir, dismissal ya removal par sab kuch chala jata hai, aur compassionate allowance kya hai?",
        "hook": "REMEMBER: Dismissal or removal = forfeiture; special case = allowance up to 2/3, within 3 months!",
        "hook_say": "Yaad rakhiye: allowance automatic nahi, aur do-tihai ceiling hai.",
        "layout": "dashboard",
        "boxes": [
            (
                "THE RULE AND PROVISO • 41(1)",
                (
                "Dismissal or removal forfeits pension AND gratuity. Proviso: in a special case a compassionate allowance "
                "up to two-thirds may be sanctioned."
            ),
                (
                "Rule 41(1): a Government servant who is dismissed or removed from service forfeits his pension and "
                "gratuity. Proviso: the authority competent to dismiss or remove him may, if the case is deserving of "
                "special consideration, sanction a compassionate allowance not exceeding two-thirds of the pension or "
                "gratuity or both that would have been admissible to him had he retired on superannuation pension. "
                "Forfeit means lose. A compassionate allowance is a kindness payment, not a right. [Verbatim Gazette "
                "text.]"
            ),
                SKY,
                (
                "Pehle rule. Rule forty-one, one sakht shuru hota hai: dismissal ya removal par pension aur gratuity dono "
                "forfeit. Lekin proviso rehmat ka darwaza kholta hai. Case special consideration ke layak ho to wahi "
                "authority compassionate allowance sanction kar sakti hai, superannuation par milne wali pension ke "
                "do-tihai se zyada nahi."
            ),
            ),
            (
                "SUB-RULES (2) AND (3)",
                (
                "The authority can act on its own or on his representation, within 3 months. Each case on its merits: "
                "misconduct, kind of service, and in exceptional cases his dependent family."
            ),
                (
                "Rule 41(2): the authority may act on its own or on his representation and must decide within three "
                "months of the penalty order. Rule 41(3), clauses (a), (b), (c): each case is decided on merits, looking "
                "at the actual misconduct, the nature of the service rendered, and in exceptional circumstances the "
                "dependent family members."
            ),
                BLUE,
                (
                "Sub-rules two aur three. Authority khud ya uski representation par, penalty order ke teen mahine ke "
                "andar decide karegi. Har case apni merit par. Actual misconduct kya tha, kis tarah ki service di, aur "
                "exceptional cases me dependent family."
            ),
            ),
            (
                "SUB-RULES (4), (5), (6)",
                (
                "Old cases undecided at commencement: decide within 6 months, and no later ones. The allowance never "
                "falls below the Rule 44 minimum."
            ),
                (
                "Rule 41(4) and (5): transitional rule: cases undecided at commencement of the Rules are decided within "
                "six months; after that no compassionate allowance is given in such cases. Rule 41(6): the amount is not "
                "less than the minimum pension under Rule 44 (dynamic figure; Rs 9,000 under Rule 44(1); check the latest "
                "O.M.)."
            ),
                GREEN,
                (
                "Sub-rules four aur five transition hain. Rules shuru hone ke waqt jo orders undecided the, unke liye "
                "chhah mahine, uske baad aise cases me allowance nahi. Sub-rule six: Rule forty-four ke minimum pension "
                "se kam nahi."
            ),
            ),
            (
                "REAL EXAMPLE AND TRAP",
                (
                "Example: removed clerk Lata applies, is granted an allowance of 20,000 where the full pension would have "
                "been 36,000. Cap 24,000, floor 9,000."
            ),
                (
                "Example (invented, recomputed): Lata, a clerk, is removed from service. Her superannuation pension would "
                "have been Rs 36,000. She submits a representation and the authority decides within three months. "
                "Two-thirds of 36,000 = Rs 24,000, so the ceiling is 24,000; the floor is the Rs 9,000 minimum. An "
                "allowance of Rs 20,000 is within limits. Q&A: does dismissal mean nothing at all? The proviso allows up "
                "to two-thirds in a special case; the normal right to pension and gratuity is forfeited. Trap: do not "
                "treat the allowance as automatic or as a pension right."
            ),
                RED,
                (
                "Example: Lata clerk, removed from service. Superannuation pension banti thi thirty-six hazaar. Do-tihai "
                "twenty-four hazaar, yahi ceiling. Minimum nau hazaar, yahi floor. Bees hazaar ka allowance limits ke "
                "andar hai. Trap: ye automatic nahi hai, aur normal pension-gratuity ka haq khatam ho jata hai."
            ),
            ),
        ],
        "covers": ["R41-1", "R41-2", "R41-3", "R41-4-5", "R41-6", "R41-EX", "R41-QA"],
    },
    {
        "id": "c3_24_om_30_10_2025",
        "chapter": "CHAPTER 24 • THE 30 OCTOBER 2025 O.M. ON COMPULSORY RETIREMENT AND ALLOWANCE",
        "title": "O.M. OF 30.10.2025 — PENSION OR GRATUITY BY LENGTH OF SERVICE",
        "badge": "O.M. 30.10.2025",
        "q": (
            "What did the 30 October 2025 office memorandum say about compulsory retirement and compassionate "
            "allowance?"
        ),
        "q_say": (
            "Sir, thirtieth October two thousand twenty-five ke O.M. ne compulsory retirement aur allowance par kya "
            "kaha?"
        ),
        "hook": (
            "REMEMBER: 10 years or more = pension portion. Under 10 years = service gratuity portion. O.M. "
            "30.10.2025!"
        ),
        "hook_say": "Yaad rakhiye: das saal se upar pension ka hissa, das se kam par service gratuity ka hissa.",
        "layout": "dashboard",
        "boxes": [
            (
                "WHICH O.M., WHICH RULE",
                (
                "DoPPW F.No. 38/10(03)/2025-P&PW(A) parts (i) and (ii), dated 30.10.2025. It quotes Rule 44(4) and Rule "
                "44(5)."
            ),
                (
                "O.M. F.No. 38/10(03)/2025-P&PW(A) parts (i) and (ii), dated 30.10.2025, of the Department of Pension and "
                "Pensioners' Welfare, signed by Under Secretary Madhu Mankotia; part (i) quotes Rule 44(4) (compulsory "
                "retirement), part (ii) quotes Rule 44(5) (compassionate allowance). Layer 3 (executive O.M.). Read "
                "through a page summary; the O.M. PDF itself was not read. Status: confirmed, as a clarification of the "
                "existing structure, not a new rule."
            ),
                SKY,
                (
                "Ye layer three ka item hai, executive office memorandum. Number F dot No. thirty-eight by ten, bracket "
                "zero three, by two thousand twenty-five, P and PW A, thirtieth October two thousand twenty-five. Ye Rule "
                "forty-four, four compulsory retirement ke liye, aur forty-four, five compassionate allowance ke liye "
                "quote karta hai."
            ),
            ),
            (
                "TEN YEARS OR MORE",
                (
                "With 10 or more years of qualifying service: a PENSION that is a portion or percentage of the "
                "superannuation pension, as the authority sanctions."
            ),
                (
                "With ten or more years of qualifying service: compulsory retirement PENSION, a portion or percentage of "
                "the superannuation pension sanctioned under Rule 40 (Rule 44(4)); and compassionate allowance as a "
                "portion or percentage of the PENSION admissible on superannuation (Rule 44(5)). Portion or percentage is "
                "as the competent authority sanctions."
            ),
                BLUE,
                (
                "Pehla case: das saal ya zyada qualifying service. Compulsory retirement me pension, jo superannuation "
                "pension ka portion ya percentage ho, jitna authority sanction kare. Compassionate allowance me "
                "allowance, jo superannuation par milne wali pension ka portion ya percentage ho."
            ),
            ),
            (
                "LESS THAN TEN YEARS",
                (
                "Under 10 years: no pension. A SERVICE GRATUITY that is a portion or percentage of the superannuation "
                "service gratuity."
            ),
                (
                "Under ten years of qualifying service: compulsory retirement SERVICE GRATUITY, a portion or percentage "
                "of the superannuation service gratuity; and compassionate allowance as a portion or percentage of the "
                "SERVICE GRATUITY admissible on superannuation. Example (invented): Farid, compulsorily retired with "
                "eight years' service, gets no pension; he gets a service gratuity that is a portion of the "
                "superannuation service gratuity, as sanctioned. Service gratuity is a lump sum paid in place of pension "
                "when service is short. Q&A: pension or gratuity under ten years? Service gratuity."
            ),
                GREEN,
                (
                "Doosra case: das saal se kam. Pension nahi. Service gratuity, jo superannuation service gratuity ka "
                "portion ya percentage ho. Example: Farid aath saal service ke saath compulsorily retired, to pension "
                "nahi, service gratuity ka hissa."
            ),
            ),
            (
                "THE TRAPS AND OPEN FLAGS",
                (
                "The O.M. quotes Rule 44(4) and 44(5), NOT Rule 41(2) or (3). It says nothing about a two-thirds ceiling. "
                "Rule text still governs."
            ),
                (
                "Corrections and flags: (1) the source called this an operational summary of Rule 41(2) and (3); wrong, "
                "the O.M. quotes Rule 44(4) and 44(5) (status: changed); Rule 41(2) and (3) are the time limit and merit "
                "factors. (2) The O.M. does not mention a two-thirds ceiling; that sits in the Rule 41(1) proviso. (3) "
                "UNVERIFIED tension: the O.M. leaves the percentage to the authority, while Rule 40(1) sets two-thirds to "
                "full; the Rule text governs, and no post-2021 amendment of Rule 40 was found. (4) UNVERIFIED: same-day "
                "O.M.s on Rule 44(6), Rule 50(3) and Rule 66 were not read; they belong to Batches 4 and 5."
            ),
                RED,
                (
                "Trap: ye memorandum Rule forty-four, four aur five quote karta hai, Rule forty-one, two ya three nahi. "
                "Do-tihai ceiling ka zikr nahi karta, wo Rule forty-one me hi hai. Ek tension abhi bhi hai: memorandum "
                "percentage authority par chhodta hai, Rule forty floor do-tihai rakhta hai. Rule text hi chalega."
            ),
            ),
        ],
        "covers": ["OM-30.10.2025-R40", "OM-30.10.2025-R41", "OM-30.10.2025-SUBRULE", "OM-30.10.2025-OTHERS", "R44-4-NEW", "R41-VS-O.M."],
    },
    {
        "id": "c3_25_chapter5_map",
        "chapter": "CHAPTER 25 • CHAPTER V ON ONE PAGE: THE KINDS OF PENSION",
        "title": "CHAPTER V — ALL THE CLASSES OF PENSION ON ONE PAGE",
        "badge": "CHAPTER V MAP",
        "q": "Can you put all of Chapter V, Rules 33 to 41, on one page, and how many classes are there?",
        "q_say": "Sir, Chapter five, Rules thirty-three se forty-one, ek page par rakh sakte hain? Classes kitni hain?",
        "hook": "REMEMBER: Chapter V: on time (33-34), moved out (35-38), ill (39), punished (40-41)!",
        "hook_say": "Yaad rakhiye: Chapter five me teen groups, aur saat classes ka claim abhi confirm nahi.",
        "layout": "dashboard",
        "boxes": [
            (
                "RETIRE ON TIME OR EARLY",
                "Rule 33 superannuation. Rule 34 retiring pension: your choice, Special VRS, or Government's decision.",
                (
                "Rule 33: superannuation pension. Rule 34: retiring pension, with 34(1)(a) voluntary (Rule 43 or FR 56), "
                "34(1)(b) Special VRS, 34(1)(c) retired by Government (Rule 42 or FR 56), and 34(2) ex-gratia on top."
            ),
                SKY,
                (
                "Group one: time par ya jaldi retirement. Rule thirty-three superannuation pension. Rule thirty-four "
                "retiring pension, teen raaste, aur Special VRS ka ex-gratia."
            ),
            ),
            (
                "MOVE OUT OF SERVICE",
                (
                "Rules 35 and 36: absorbed in a State or a body. Rules 37 and 38: the department itself converts to a PSU "
                "or autonomous body."
            ),
                (
                "Rules 35 and 36: absorption in a State Government, and in a Corporation, Company or Body. Rules 37 and "
                "38: conversion of a department into a Public Sector Undertaking or a Central Autonomous Body. Rule "
                "37(29)(c) forfeiture amended by G.S.R. 340(E) of 22.05.2025; G.S.R. 775(E) of 02.09.2026, the proviso to "
                "37(7)."
            ),
                BLUE,
                (
                "Group two: service se bahar jaana. Rules thirty-five aur thirty-six individual absorption, State ya body "
                "me. Rules thirty-seven aur thirty-eight poora department PSU ya autonomous body ban jaye."
            ),
            ),
            (
                "ILL HEALTH AND PUNISHMENT",
                (
                "Rule 39 invalid pension. Rule 40 compulsory retirement pension (floor two-thirds). Rule 41 compassionate "
                "allowance (ceiling two-thirds)."
            ),
                (
                "Rule 39: invalid pension. Rule 40: compulsory retirement pension (floor two-thirds). Rule 41: "
                "compassionate allowance (ceiling two-thirds). Group three covers ill health and punishment."
            ),
                GREEN,
                (
                "Group three: bimari aur punishment. Rule thirty-nine invalid pension. Rule forty compulsory retirement "
                "pension, floor do-tihai. Rule forty-one compassionate allowance, ceiling do-tihai."
            ),
            ),
            (
                "THE TRAPS: THE COUNT AND THE TABLE",
                (
                "'Seven classes' is the guide's claim, NOT confirmed. The guide table's Rule 40 and 41 rows are wrong. "
                "Rules 42-43 are not classes: check Batch 4."
            ),
                (
                "(1) CNT-7CLASSES: the count of seven classes is the source's claim and was not independently verified; "
                "recounting gives superannuation, retiring, absorption, invalid, compulsory retirement and compassionate "
                "allowance, plus PSU conversion (Rules 37 and 38). (2) The guide's Chapter V table calls Rule 40 "
                "'compassionate allowance' and Rule 41 'special pension or special compassionate allowance'; the rule "
                "cards are right (Rule 40 compulsory retirement pension, Rule 41 compassionate allowance); the table row "
                "has no basis in Rules 40 and 41 (divergence confirmed). (3) The statement that Rules 42 and 43 are not "
                "classes was not checked here (Rules 42 and 43 not read); check in Batch 4."
            ),
                RED,
                (
                "Trap: guide ka saat classes ka claim confirm nahi hua. Guide table me Rules forty aur forty-one ke "
                "labels galat hain, rule cards par bharosa karein. Rules forty-two aur forty-three classes nahi hain, wo "
                "Batch four me."
            ),
            ),
        ],
        "covers": ["CH5-RECAP", "CH5-TABLE-DIVERGE", "CNT-7CLASSES"],
    },
    {
        "id": "c3_27_rule31_conditions",
        "chapter": "CHAPTER 26 • RULE 31(3), (6), (8), (9), (11): THE FIVE CONDITIONS",
        "title": "RULE 31 — THE FIVE CONDITIONS EVERY NOTE SKIPS",
        "badge": "RULE 31 • CONDITIONS",
        "q": "Which quiet conditions inside Rule 31 change the answer in a real pension file?",
        "q_say": (
            "Sir, Rule thirty-one ke sub-rules me kaun si chhupi hui conditions hain jo asli file me answer badal "
            "deti hain?"
        ),
        "hook": (
            "REMEMBER: certificate for 31(3), Armed Forces plus proviso in 31(6), options in 31(8)-(9), penalty only "
            "while it runs in 31(11)."
        ),
        "hook_say": (
            "Yaad rakhiye: thirty-one, three ke liye certificate, thirty-one, six me Armed Forces aur proviso, "
            "aath-nau me options, aur gyarah me penalty sirf apne dauraan."
        ),
        "layout": "dashboard",
        "boxes": [
            (
                "31(3) • THE CERTIFICATE",
                (
                "A higher post held just before leave pays ONLY if it is certified that he would have continued in it but "
                "for the leave."
            ),
                (
                "Rule 31(3): where a Government servant, immediately before retirement or death while in service, had "
                "proceeded on leave for which leave salary is payable after having held a higher appointment whether in "
                "an officiating or temporary capacity, the benefit of the emoluments drawn in that higher appointment "
                "shall be given ONLY if it is certified that he would have continued to hold the higher appointment but "
                "for his proceeding on leave. No certificate, no higher pay: the lower post's pay is used. [Verbatim "
                "Gazette text.]"
            ),
                SKY,
                (
                "Sub-rule teen me ek condition chhupi hai. Leave se pehle higher post par tha, to uski pay tabhi milegi "
                "jab certificate ho ki leave na hoti to wo usi higher post par hota. Certificate nahi, to neeche wali "
                "post ki pay hi ginegi."
            ),
            ),
            (
                "31(6) • ARMED FORCES + THE PROVISO",
                (
                "An ex-cadre post in any Department OR the Armed Forces counts. Proviso: leave after release from the "
                "ex-cadre post gives parent-department pay."
            ),
                (
                "Rule 31(6): pay drawn while on deputation to an ex-cadre post in the same or some other Department of "
                "the Government OR to the Armed Forces of India shall be treated as emoluments. Proviso: in the case of a "
                "servant on leave after release from the ex-cadre post on completion of the period of deputation, the pay "
                "he would have drawn in the parent department had he not been on leave shall be treated as emoluments. "
                "The Armed Forces limb and the proviso are both usually missed. [Verbatim Gazette text.]"
            ),
                GREEN,
                (
                "Sub-rule chhah: ex-cadre post ho, kisi bhi Department me, ya Armed Forces me, dono ki pay emoluments "
                "hai. Aur proviso: ex-cadre deputation khatam hone ke baad leave par gaya, to parent department ki pay "
                "ginegi, us ex-cadre ki nahi."
            ),
            ),
            (
                "31(8) AND 31(9) • TWO HIDDEN OPTIONS",
                (
                "31(8) re-employed pensioner: the pension slice that cut his pay counts. 31(9) converted PSU or body: "
                "only if he OPTS to keep Government benefits."
            ),
                (
                "Rule 31(8): where a pensioner re-employed in Government service elected to retain his pension for "
                "earlier service and his pay on re-employment was reduced by an amount not exceeding his pension, the "
                "element of pension by which his pay is reduced shall be treated as emoluments. Rule 31(9): where a "
                "servant was transferred to a PSU or autonomous body consequent on conversion of a Department and OPTS to "
                "retain the pensionary benefits under the Government rules, the emoluments drawn under that PSU or body "
                "shall be treated as emoluments. The option in 31(9) is the condition; without it the limb does not fire. "
                "[Verbatim Gazette text.]"
            ),
                BLUE,
                (
                "Do chhupi hui conditions. Aath: re-employed pensioner ne purani pension rakhi aur uski pay usse kam ho "
                "gayi, to pay me se jitna pension ka hissa kata, wo emoluments hai. Nau: converted PSU me jaane par PSU "
                "ki pay tabhi ginegi jab usne Government benefits rakhne ka option liya ho."
            ),
            ),
            (
                "THE TRAP • ONLY WHILE THE PENALTY RUNS",
                (
                "31(11) and 32(6) need a penalty that cut pay only during its currency. A permanent reduction is outside "
                "both."
            ),
                (
                "Rule 31(11) and Rule 32(6) both speak of a penalty which has the effect of reducing pay ONLY during the "
                "currency of that penalty and on expiry of which the servant would have regained the pay admissible "
                "without the impact of the penalty. The notional pay ignoring the penalty is then used. A penalty that "
                "permanently reduces pay (for example a reduction to a lower stage for a specified number of years with "
                "cumulative effect) does not fit this wording, so do not read 31(11) as a general 'ignore every penalty' "
                "rule. [Verbatim Gazette text; the reading of 'cumulative effect' penalties is the standard departmental "
                "one.]"
            ),
                RED,
                (
                "Trap: sub-rule gyarah aur Rule thirty-two, chhah sirf us penalty par lagte hain jo pay sirf penalty ke "
                "dauraan ghatati hai aur khatam hone par pay wapas mil jati. Permanent ya cumulative effect wali "
                "reduction isme nahi aati, to ise har penalty par mat lagayein."
            ),
            ),
        ],
        "covers": ["R31-3-CERT", "R31-6-AF", "R31-6-PROV", "R31-8", "R31-9-OPT", "R31-11-LIMIT"],
    },
    {
        "id": "c3_28_rule32_fractions",
        "chapter": "CHAPTER 27 • RULE 32(3): THE FRACTION RULES",
        "title": "RULE 32 — THE FRACTION RULES: 14/30, 16/30 AND FEBRUARY",
        "badge": "RULE 32(3) • FRACTIONS",
        "q": "How exactly do you count a broken month, and what happens to February?",
        "q_say": "Sir, adhoora mahina exactly kaise ginte hain, aur February ka kya hota hai?",
        "hook": "REMEMBER: fractions are days over 30, February is always 30, and the divisor never moves off ten.",
        "hook_say": "Yaad rakhiye: fraction matlab din by thirty, February hamesha thirty, aur divisor das se hilta nahi.",
        "layout": "table",
        "boxes": [
            (
                "14/30 AND 16/30",
                (
                "Retirement on 16 July 2019: nine full months + 14/30 of September 2018 + 16/30 of July 2019 = ten "
                "months."
            ),
                (
                "Illustration to Rule 32(3), verbatim: a Government servant retires on 16th July 2019. The last ten "
                "months comprise nine full months and fractions of fourteen days of September 2018 and sixteen days of "
                "July 2019. The emoluments for the fractional periods are computed by multiplying the emolument by the "
                "factor 14/30 and 16/30 respectively, irrespective of the number of days in the month. Note the "
                "arithmetic: 9 + 14/30 + 16/30 = 10 exactly. The two broken ends at the start and the finish add up to "
                "one whole month."
            ),
                SKY,
                (
                "Illustration rule me hi diya hai. Sixteenth July two thousand nineteen par retirement. Nau poore mahine, "
                "plus September two thousand eighteen ke fourteen-thirtieth, plus July ke sixteen-thirtieth. Total "
                "exactly das mahine. Factors din se bante hain, mahine ke actual dinon se nahi."
            ),
            ),
            (
                "FEBRUARY IS ALWAYS 30",
                "Whether February has 28 days or 29, the factor stays over 30. The illustration says so in terms.",
                (
                "The Illustration to Rule 32(3) ends with: 'This formula shall also apply in the case of the month of "
                "February, irrespective of whether the month has twenty eight days or twenty nine days.' So a February "
                "slice is never given a 28 or 29 denominator, and a leap year changes nothing. This is the single most "
                "common arithmetic slip in average-emoluments answers."
            ),
                YELLOW,
                (
                "February ka special case. Rule kehta hai chahe twenty-eight din ho ya twenty-nine, factor thirty hi "
                "rahega. Isliye February kabhi average ko tilt nahi karta, aur leap year se kuch nahi badalta."
            ),
            ),
            (
                "THE DIVISOR NEVER MOVES",
                "Five situations, one divisor: ten. What slides is the WINDOW, not the number you divide by.",
                (
                "Five situations and one divisor. (1) Ten clean months: divide by ten. (2) Extraordinary leave or "
                "suspension that does not count: the period is disregarded and an equal period earlier is added, still "
                "ten. (3) A broken month at either end: days/30, still ten. (4) February anywhere in the window: still "
                "/30, still ten. (5) An increment earned during leave and not withheld: included though not drawn, still "
                "ten. Rule 44(9) then rounds the final rupee amount up."
            ),
                GREEN,
                (
                "Table dekhiye. Paanch situations, divisor ek hi, das. Jo badalta hai wo window hai, divide karne wali "
                "sankhya nahi. Yahi is rule ka core hai, aur yahi sabse zyada galat hota hai."
            ),
            ),
            (
                "THE TRAP",
                (
                "A 30-day month does NOT mean 30 days of pay. The factor applies only to FRACTIONS; whole months use the "
                "pay actually drawn."
            ),
                (
                "Rule 32(3) treats a month as thirty days only 'in order that the fractions of a month, when added, "
                "worked out to one full month'. It is a fractions device, not a pay device. A whole month's emoluments "
                "are the emoluments actually drawn in that month, and a whole month is not converted to 30/30 of "
                "anything. Confusing the two produces a wrong average that still looks arithmetically neat."
            ),
                RED,
                (
                "Trap: thirty din ka mahina ka matlab thirty din ki pay nahi. Ye factor sirf adhoore mahino ke liye hai, "
                "taaki fractions jodkar poora mahina ban jaye. Poore mahine me jo pay actually mili wahi ginegi."
            ),
            ),
        ],
        "covers": ["R32-3-ILLUS", "R32-FEB", "R32-DIVISOR", "R32-FRAC-TRAP"],
        "table": {
            "cols": ["Situation in the last ten months", "Divisor", "Month length", "What happens"],
            "widths": [
                0.36,
                0.11,
                0.15,
                0.38,
            ],
            "rows": [
                ["Ten clean months, no break", "10", "actual pay", "Plain average of what was drawn"],
                ["EOL or suspension not counting", "10", "actual pay", "Period dropped, equal earlier period added"],
                ["Broken month at either end", "10", "30 days", "Multiply by days/30 (14/30, 16/30)"],
                ["February anywhere in the window", "10", "30 days", "28 or 29 days ignored by the rule"],
                ["Increment earned during leave", "10", "—", "Counted though it was never drawn"],
            ],
            "accent_col": 1,
        },
    },
    {
        "id": "c3_29_rule37_38_clauses",
        "chapter": "CHAPTER 28 • RULES 37(30)-(31) AND 38(26)-(29)",
        "title": "THE CLAUSES NOBODY QUOTES: DISINVESTMENT AND THE PRASAR BHARATI CARVE-OUT",
        "badge": "RULES 37(30) • 38(29)",
        "q": "Which closing sub-rules of Rules 37 and 38 are never in a guide, and why do they matter?",
        "q_say": (
            "Sir, Rules thirty-seven aur thirty-eight ke aakhri sub-rules jo kisi guide me nahi hote, wo kya kehte "
            "hain?"
        ),
        "hook": (
            "REMEMBER: 51% disinvestment needs safeguards, and Rule 38 does not touch IIS or CSS officers in "
            "Akashvani and Doordarshan."
        ),
        "hook_say": (
            "Yaad rakhiye: fifty-one percent disinvestment par safeguards zaroori, aur Rule thirty-eight IIS ya CSS "
            "walon par nahi lagta."
        ),
        "layout": "dashboard",
        "boxes": [
            (
                "37(30) AND 38(27) • THE 51 PER CENT TRIGGER",
                (
                "If the Government disinvests 51 per cent or more of its equity in the PSU or the body, it MUST specify "
                "adequate safeguards for the absorbed employees."
            ),
                (
                "Rule 37(30): in case the Government disinvests its equity in any public sector undertaking to the extent "
                "of fifty-one per cent or more, it shall specify adequate safeguards for protecting the interest of the "
                "absorbed employees of such undertaking. Rule 38(27) carries the identical duty for an autonomous body. "
                "The duty is mandatory ('shall'), and it is triggered by the size of the disinvestment, not by a request "
                "from the employees. [Verbatim Gazette text.]"
            ),
                ORANGE,
                (
                "Rule thirty-seven, thirty, aur Rule thirty-eight, twenty-seven. Government apni equity fifty-one percent "
                "ya usse zyada bech de, to absorbed employees ke liye adequate safeguards dena zaroori hai. Ye clause koi "
                "note nahi likhta, par duty mandatory hai."
            ),
            ),
            (
                "37(31) AND 38(28) • WHAT A SAFEGUARD IS",
                (
                "Option of voluntary retirement or continued service, benefits on Government or body terms by his choice, "
                "assured earned pension with relaxation of qualifying service."
            ),
                (
                "Rule 37(31): the safeguards shall include option for voluntary retirement or continued service in the "
                "undertaking or retirement benefits on terms applicable to Government employees or employees of the PSU "
                "as per the option of the employee, and assured payment of earned pensionary benefits with relaxation in "
                "period of qualifying service, as may be decided by the Government. Rule 38(28) is the parallel provision "
                "for a body. So 'adequate safeguards' is not a blank cheque: the rule itself lists the menu."
            ),
                SKY,
                (
                "Safeguards me kya hoga? Voluntary retirement ya service continue karne ka option, Government ya body ke "
                "terms par benefits jaisa employee chune, aur earned pensionary benefits ki assured payment, qualifying "
                "service me relaxation ke saath."
            ),
            ),
            (
                "38(26) • PF, LEAVE, AND A LATER DISMISSAL",
                (
                "Provident fund and leave balances travel to the body. A later dismissal by the body does NOT forfeit "
                "Government-service benefits, and the Ministry reviews."
            ),
                (
                "Rule 38(26)(a): the balance of provident fund credited to absorbed employees is, with the consent of the "
                "body, transferred to the new PF account. (b): earned leave and half pay leave stand transferred to the "
                "body. (c): dismissal or removal by the body after absorption for subsequent misconduct shall NOT amount "
                "to forfeiture of the retirement benefits for Government service, and a dismissal, removal or "
                "retrenchment decision is subject to review by the Ministry administratively concerned. Rule "
                "37(29)(a)-(c) is the PSU twin, but with (c) rewritten by G.S.R. 340(E) of 22.05.2025 so that dismissal "
                "or removal by the PSU DOES forfeit. [Verbatim Gazette text, Rule 38(26); Rule 37(29)(c) as substituted.]"
            ),
                GREEN,
                (
                "Rule thirty-eight, twenty-six Rule thirty-seven, twenty-nine ka mirror hai, par ek bada farq. Rule "
                "thirty-eight me body ki dismissal se Government service ke benefits forfeit nahi hote, aur Ministry "
                "review karti hai. Rule thirty-seven me two thousand twenty-five ke baad wo forfeiture ho gayi."
            ),
            ),
            (
                "38(29) • THE PRASAR BHARATI CARVE-OUT",
                (
                "Nothing in Rule 38 applies to IIS or CSS officers, or to persons on cadres outside Akashvani and "
                "Doordarshan, serving in those organisations."
            ),
                (
                "Rule 38(29): nothing contained in Rule 38 shall be applicable to officers or employees including members "
                "of the Indian Information Service, Central Secretariat Service or any other service, or to persons borne "
                "on cadres outside Akashvani and Doordarshan, serving in Akashvani and Doordarshan and engaged in the "
                "performance of functions transferred to Prasar Bharati established under the Prasar Bharati "
                "(Broadcasting Corporation of India) Act, 1990. Rule 37 has no such general carve-out; its carve-out is "
                "the BSNL and MTNL one in Rules 37(26) to 37(28). [Verbatim Gazette text.]"
            ),
                PINK,
                (
                "Sabse anokha exception. Rule thirty-eight, twenty-nine: ye rule IIS aur CSS officers par nahi lagta, aur "
                "Akashvani ya Doordarshan me kaam karne wale bahar ke cadre walon par bhi nahi. Prasar Bharati wale isi "
                "clause me aate hain. Rule thirty-seven me aisa carve-out nahi, wahan BSNL aur MTNL ka exception hai."
            ),
            ),
        ],
        "covers": ["R37-30", "R37-31", "R38-26", "R38-27", "R38-28", "R38-29"],
    },
    {
        "id": "c3_30_flags_resolved",
        "chapter": "CHAPTER 29 • FIVE FLAGS NOW CLOSED",
        "title": "FIVE 'NOT VERIFIED' FLAGS — NOW SETTLED BY THE GAZETTE TEXT",
        "badge": "AUDIT • FLAGS CLOSED",
        "q": "Which open flags from the first build can now be closed, and what does the rule actually say?",
        "q_say": "Sir, pehle build ke kaunse flags ab band ho sakte hain, aur rule actually kya kehta hai?",
        "hook": (
            "REMEMBER: two clocks in 37(2), both ages in 39(4), before OR after appointment in 39(9), three "
            "order-types in 40(2), and the 2026 proviso for ex-OFB opt-outs."
        ),
        "hook_say": (
            "Yaad rakhiye: thirty-seven, two me do clocks, thirty-nine, four me dono ages, thirty-nine, nine me pehle "
            "ya baad, aur forty, two me teen order types."
        ),
        "layout": "table",
        "boxes": [
            (
                "37(2) • TWO CLOCKS, NOT ONE",
                (
                "The PSU must ASK within 3 months of notifying its rules; the servant must OPT within 3 months of that "
                "communication."
            ),
                (
                "Rule 37(2), verbatim: the PSU frames its rules and regulations within a time frame not exceeding five "
                "years. After such rules are framed, all Government servants on deemed deputation shall be asked, within "
                "a period not exceeding three months from the date of notification of the rules, to exercise their option "
                "to revert to the Government or to seek permanent absorption. Such servants shall be asked to exercise "
                "this option within a period of three months from the date of the communication asking them to exercise "
                "the option. So: five years to make rules, three months to ask, three months to answer. Rule 38(2) merges "
                "the same three clocks into one sub-rule."
            ),
                SKY,
                (
                "Pehla flag band. Rule thirty-seven, two me ek nahi, do clocks hain. PSU ko apne rules notify hone ke "
                "teen mahine ke andar staff se option maangna hai, aur staff ko us communication se teen mahine milte "
                "hain. Pehle confusion yahi thi ki teen mahine kab se ginte hain."
            ),
            ),
            (
                "39(4) • BOTH AGES GO WITH THE FILE",
                (
                "The age in the official records AND the age recorded in the service book, plus a copy of the request to "
                "the servant."
            ),
                (
                "Rule 39(4), verbatim: the medical authority shall also be supplied by the Head of Office or Head of "
                "Department with a statement of what appears from official records to be the age of the applicant, and if "
                "a service book is being maintained for the applicant, the age recorded therein should be reported, and a "
                "copy of the letter requesting examination by the medical authority shall be endorsed to the Government "
                "servant. So both ages travel, and the servant gets a copy. This matters because invalid pension is "
                "age-linked at the margins."
            ),
                BLUE,
                (
                "Doosra flag band. Rule thirty-nine, four: medical authority ko official records wali age, aur service "
                "book maintain ho to uski age bhi, dono bhejni hain, aur request letter ki copy employee ko. To dono ages "
                "jati hain, sirf ek nahi."
            ),
            ),
            (
                "39(9) • BEFORE OR AFTER APPOINTMENT",
                (
                "The fit certificate may be from before appointment or after appointment. Either timing satisfies limb "
                "(a); limb (b) still needs the other conditions."
            ),
                (
                "Rule 39(9), verbatim: a Government servant who retires even before completing qualifying service of ten "
                "years shall also be granted invalid pension, calculated at fifty per cent of emoluments or average "
                "emoluments, whichever is more beneficial, in accordance with Rule 44. Proviso: the servant (a) has been "
                "examined by the appropriate medical authority EITHER BEFORE his appointment OR AFTER his appointment to "
                "the Government service and declared fit by such authority for Government service; AND (b) fulfils all "
                "other conditions mentioned in Rule 39. Both limbs are required; only the timing of the fit certificate "
                "is flexible."
            ),
                GREEN,
                (
                "Teesra flag band. Rule thirty-nine, nine ka proviso: fit certificate appointment se pehle ka ho ya baad "
                "ka, dono chalega. Lekin doosri condition bhi chahiye, rule ki baaki saari conditions poori hon. Sirf "
                "timing flexible hai."
            ),
            ),
            (
                "40(2) • ORIGINAL, APPELLATE, REVIEW",
                (
                "The UPSC must be consulted before ANY order below full superannuation pension, whether original, "
                "appellate or in review. 'Pension' includes gratuity."
            ),
                (
                "Rule 40(2), verbatim: whenever in the case of a Government servant the President passes an order "
                "(whether original, appellate or in exercise of power of review) awarding a pension less than the full "
                "superannuation pension admissible under these rules, the Union Public Service Commission shall be "
                "consulted before such order is passed. Explanation: for this sub-rule, 'pension' includes retirement "
                "gratuity. So the UPSC door is not limited to the first order."
            ),
                ORANGE,
                (
                "Chautha flag band. Rule forty, two: President poore se kam pension ka order dein, to UPSC se pehle "
                "consult karna hoga, chahe order original ho, appellate ho, ya review me. Aur pension me retirement "
                "gratuity bhi shaamil hai."
            ),
            ),
            (
                "THE TRAP • A FLAG IS NOT A FACT",
                (
                "Five flags are closed. One caution is left: the rupee figures (Rs 9,000, Rs 1,25,000, Rs 54,000), "
                "because the latest amending O.M. has not been re-read."
            ),
                (
                "House discipline: 'not verified' never means 'wrong', it means the wording was not yet seen. Five flags "
                "are now closed against the verbatim Gazette text: the three clocks of 37(2), the two ages of 39(4), the "
                "either-timing fit certificate of 39(9), the three order-types of 40(2), and the 2026 proviso to Rule "
                "37(7). One caution remains and must still be dated in an answer: the Rs 9,000 floor, the Rs 1,25,000 "
                "ceiling and the Rs 54,000 medical-board threshold, because the latest amending O.M. has not been "
                "re-read."
            ),
                RED,
                (
                "Trap: not verified ka matlab galat nahi hota, bas wording dekhi nahi thi. Chaar flags ab band hain. Do "
                "khule hain: G.S.R. seven hundred seventy-five E ki exact date, aur rupaye ke figures, kyunki latest O.M. "
                "abhi nahi padha. Answer sheet me figure ke saath date likhein."
            ),
            ),
        ],
        "covers": ["R37-2-TWOCLOCK", "R39-4-BOTH", "R39-9-EITHER", "R40-2-THREE", "FLAG-DISCIPLINE"],
        "table": {
            "cols": ["Flag in the first build", "What was said", "What the Gazette text now says"],
            "widths": [
                0.26,
                0.3,
                0.44,
            ],
            "rows": [
                [
                    "Rule 37(2) option clock",
                    "One 3-month window, start date unclear",
                    "Three clocks: 5 years, 3 months to ask, 3 months to opt",
                ],
                [
                    "Rule 39(4) ages sent",
                    "Only the recorded age confirmed",
                    "Records age + service-book age, copy to the servant",
                ],
                [
                    "Rule 39(9) fit certificate",
                    "Before or after appointment not checked",
                    "Either before OR after appointment, plus other conditions",
                ],
                [
                    "Rule 40(2) UPSC orders",
                    "Original, appellate, review not seen",
                    "All three order-types expressly covered",
                ],
                [
                    "Rule 37(7) proviso, 2026",
                    "Only the existence of a proviso was known",
                    "G.S.R. 775(E), notified 02.09.2026: ex-OFB opt-outs stay on deemed deputation till retirement",
                ],
            ],
            "accent_col": 2,
        },
    },
    {
        "id": "c3_31_absorption_table",
        "chapter": "CHAPTER 30 • RULES 35, 36, 37 AND 38 ON ONE GRID",
        "title": "FOUR ABSORPTION RULES, ONE GRID: WHO MOVES, WHO PAYS, WHO FORFEITS",
        "badge": "RULES 35 • 36 • 37 • 38",
        "q": "Can you put all four absorption routes side by side so the differences stop blurring?",
        "q_say": "Sir, chaaron absorption routes ek saath dikhaayein, taaki differences blur na hon?",
        "hook": (
            "REMEMBER: one servant goes by 35 or 36, a whole department goes by 37 or 38; only 37 and 38 have the "
            "deeming clause."
        ),
        "hook_say": (
            "Yaad rakhiye: ek banda thirty-five ya thirty-six se, poora department thirty-seven ya thirty-eight se; "
            "deeming sirf thirty-seven aur thirty-eight me hai."
        ),
        "layout": "table",
        "boxes": [
            (
                "ONE SERVANT AGAINST A WHOLE DEPARTMENT",
                (
                "Rules 35 and 36 move ONE servant to a State or a body. Rules 37 and 38 move the WHOLE department into a "
                "PSU or a CAB."
            ),
                (
                "Rules 35 and 36 are individual: a servant permitted to be absorbed in a State Government, or in a "
                "Corporation, Company or Body. The trigger is his own move and his resignation is accepted from the date "
                "preceding joining. Rules 37 and 38 are collective: a Department of the Central Government is converted "
                "into a PSU or a Central Autonomous Body, and every servant of that Department is transferred en-masse on "
                "deemed deputation until absorption. This single difference explains every other difference on the grid."
            ),
                SKY,
                (
                "Sabse bada farq. Rules thirty-five aur thirty-six individual hain, ek banda State ya body me absorb hota "
                "hai, uska resignation joining se ek din pehle accept hota hai. Rules thirty-seven aur thirty-eight "
                "collective hain, poora department PSU ya autonomous body ban jata hai, sab deemed deputation par."
            ),
            ),
            (
                "WHO PAYS UNDER OPTION (b)",
                (
                "35(7): the State pays the WHOLE pension. 36(10): the Centre pays a ONE-TIME lump sum. 37 and 38: a "
                "Pension Fund trust pays."
            ),
                (
                "Under option (b) the money moves differently in each rule. Rule 35(7): the State pays pension and "
                "gratuity for the entire service including the Central spell, and the Centre bears no proportionate "
                "liability. Rule 36(10): the Government discharges its liability by paying in lump sum as a one-time "
                "payment, computed on the capitalised value plus retirement gratuity under the 1981 commutation table. "
                "Rules 37 and 38: a Pension Fund in the form of a trust is created, the Government pays its share in lump "
                "sum into the Fund, and the PSU or body contributes so the Fund is self-supporting."
            ),
                GREEN,
                (
                "Option b me paisa alag alag chalta hai. Rule thirty-five, seven: State poori service ki pension degi, "
                "Centre ka share nahi. Rule thirty-six, ten: Government ek one-time lump sum dekar apni liability khatam "
                "karti hai, nineteen eighty-one table se. Rules thirty-seven aur thirty-eight: Pension Fund trust banta "
                "hai, Government usme lump sum daalti hai."
            ),
            ),
            (
                "THE DEARNESS RELIEF SPLIT",
                (
                "Only Rules 37 and 38 have a DR clause: IDA pattern for a PSU, CENTRAL DA pattern for a CAB. Rules 35 and "
                "36 have none."
            ),
                (
                "Rule 37(16): an employee who opts for pension on the basis of combined service is also eligible to "
                "dearness relief as per the Industrial Dearness Allowance pattern, and Rule 37(15) Explanation bases "
                "emoluments and average emoluments on PSU pay on the IDA pattern. Rule 38(15): dearness relief as per the "
                "Central Dearness Allowance pattern. Rules 35 and 36 contain no dearness relief clause at all, because "
                "the pension there is settled at absorption and the State or body scheme takes over."
            ),
                BLUE,
                (
                "Dearness relief ka clause sirf thirty-seven aur thirty-eight me hai. Rule thirty-seven, sixteen: IDA "
                "pattern. Rule thirty-eight, fifteen: Central DA pattern. Rules thirty-five aur thirty-six me DR ka koi "
                "clause nahi, kyunki wahan pension absorption par settle ho jati hai."
            ),
            ),
            (
                "THE TRAP • NO DEEMING IN 35 AND 36",
                (
                "Silence means absorption only in 37(4) and 38(3). Rules 35 and 36 have no silence rule, and Rule 36 has "
                "no deeming at all."
            ),
                (
                "The deeming provision is narrow. Rule 37(4): a servant who does not exercise any option within the "
                "prescribed time is deemed to have opted for permanent absorption in the PSU. Rule 38(3): the same for a "
                "body. Rules 35(6) and 36(9) grant an option but contain no consequence for silence, so silence there "
                "cannot be converted into consent. And Rule 36(8) adds that no lien is retained and all connections with "
                "Government stand severed on absorption."
            ),
                RED,
                (
                "Trap: silence par absorption sirf thirty-seven, four aur thirty-eight, three me hai. Rules thirty-five "
                "aur thirty-six me option hai par silence ka result nahi likha, to wahan chup rehna consent nahi banta. "
                "Aur Rule thirty-six, aath: lien nahi bachta."
            ),
            ),
        ],
        "covers": ["R35-VS-36", "R37-VS-38", "OPTION-B-PAYER", "DR-SPLIT", "NO-DEEMING-3536"],
        "table": {
            "cols": ["Point", "Rule 35 State", "Rule 36 Body", "Rule 37 PSU", "Rule 38 CAB"],
            "widths": [
                0.2,
                0.21,
                0.21,
                0.19,
                0.19,
            ],
            "rows": [
                ["Who moves", "one servant", "one servant", "whole dept", "whole dept"],
                ["Status till absorption", "deemed retired", "deemed retired", "deemed deputation", "deemed deputation"],
                ["Lien", "ends", "ends, 36(8)", "ends on acceptance", "ends on acceptance"],
                ["Option clause", "35(6)", "36(9)", "37(12)", "38(11)"],
                ["Payer under (b)", "State, whole", "Govt lump sum", "Pension Fund", "Pension Fund"],
                ["Dearness relief", "none", "none", "IDA, 37(16)", "Central DA, 38(15)"],
                ["Silence", "no rule", "no rule", "absorbed, 37(4)", "absorbed, 38(3)"],
            ],
            "accent_col": 0,
        },
    },
    {
        "id": "c3_32_floor_ceiling_chart",
        "chapter": "CHAPTER 31 • TWO-THIRDS ON A CHART",
        "title": "TWO-THIRDS, DRAWN: A FLOOR IN RULE 40 AND A CEILING IN RULE 41",
        "badge": "CHART • RULES 40 vs 41",
        "q": "Can one picture fix the difference between a two-thirds floor and a two-thirds ceiling?",
        "q_say": "Sir, ek chart se do-tihai floor aur do-tihai ceiling ka farq pakka ho sakta hai?",
        "hook": (
            "REMEMBER: Rule 40 builds UP from two-thirds, Rule 41 caps DOWN at two-thirds, and both sit above the "
            "Rule 44 minimum."
        ),
        "hook_say": (
            "Yaad rakhiye: Rule forty do-tihai se upar banta hai, Rule forty-one do-tihai par rukta hai, aur dono "
            "Rule forty-four ke minimum se upar."
        ),
        "layout": "chart",
        "boxes": [
            (
                "READ THE BARS",
                (
                "Illustration: superannuation pension Rs 60,000 for Rule 40, and Rs 36,000 for Rule 41. Bars are monthly "
                "rupees."
            ),
                (
                "Chart assumptions, stated openly so the arithmetic can be checked. Rule 40: the full superannuation "
                "pension admissible is Rs 60,000 a month, so the floor is two-thirds, Rs 40,000, and the ceiling is the "
                "full Rs 60,000: any amount from Rs 40,000 to Rs 60,000 is lawful, and nothing below Rs 40,000 is. Rule "
                "41: the pension that would have been admissible on superannuation is Rs 36,000, so the ceiling is "
                "two-thirds, Rs 24,000, and the floor is the Rule 44 minimum of Rs 9,000: anything from Rs 9,000 to Rs "
                "24,000 may be sanctioned. The two examples use different base pensions on purpose, so that no one can "
                "compare the bars directly and think the rules are the same shape."
            ),
                SKY,
                (
                "Chart ke assumptions khul kar. Rule forty: poori superannuation pension sixty hazaar, to floor do-tihai, "
                "forty hazaar, aur ceiling poore sixty hazaar. Rule forty-one: jo pension banti thi wo thirty-six hazaar, "
                "to ceiling do-tihai, twenty-four hazaar, aur floor Rule forty-four ka minimum nau hazaar."
            ),
            ),
            (
                "RULE 40 IS A BAND",
                "40(1): not less than two-thirds and not more than full. The authority picks a point inside the band.",
                (
                "Rule 40(1): a Government servant compulsorily retired as a penalty may be granted, by the authority "
                "competent to impose the penalty, pension or retirement gratuity or both at a rate not less than "
                "two-thirds and not more than full superannuation pension or gratuity admissible on the date of "
                "compulsory retirement. The band has a hard bottom, which is why Rule 40(3) can safely pay a provisional "
                "two-thirds at once, and Rule 40(5) then lifts the floor to the Rule 44 minimum if that is higher."
            ),
                ORANGE,
                (
                "Rule forty ek band hai. Sub-rule one: do-tihai se kam nahi, poore se zyada nahi. Authority band ke andar "
                "koi bhi point chun sakti hai. Neeche ki limit hard hai, isliye sub-rule teen turant provisional do-tihai "
                "de sakta hai."
            ),
            ),
            (
                "RULE 41 IS A LID",
                (
                "41(1) proviso: a compassionate allowance NOT EXCEEDING two-thirds, and 41(6) keeps it above the Rule 44 "
                "minimum."
            ),
                (
                "Rule 41(1): a servant dismissed or removed forfeits pension and gratuity. Proviso: the authority "
                "competent to dismiss or remove may, if the case is deserving of special consideration, sanction a "
                "compassionate allowance not exceeding two-thirds of pension or gratuity or both which would have been "
                "admissible had he retired on superannuation pension. Rule 41(6): the allowance shall not be less than "
                "the minimum pension under Rule 44. So the same fraction caps instead of floors, and the discretion runs "
                "downward from it, not upward."
            ),
                GREEN,
                (
                "Rule forty-one lid hai. Sub-rule one ka proviso: do-tihai se zyada nahi. Discretion neeche ki taraf "
                "chalta hai, upar nahi. Aur sub-rule six floor lagata hai, Rule forty-four ka minimum. To yahan do-tihai "
                "maximum hai, guaranteed amount nahi."
            ),
            ),
            (
                "THE TRAP • SAME FRACTION, OPPOSITE JOB",
                (
                "Two-thirds is not a number you remember; it is a direction. Say which way it points before you say the "
                "figure."
            ),
                (
                "The examination failure is not arithmetic, it is direction. In Rule 40 two-thirds is the worst case that "
                "the law still permits; in Rule 41 it is the best case that the law permits. A single sentence in an "
                "answer settles it: 'Rule 40 fixes a floor of two-thirds; Rule 41 fixes a ceiling of two-thirds.' Add the "
                "shared safety net, Rule 44's minimum pension, which applies through 40(5) and 41(6) to both."
            ),
                RED,
                (
                "Trap: do-tihai yaad rakhne wali sankhya nahi, ek direction hai. Rule forty me wo sabse kharab allowed "
                "case hai, Rule forty-one me sabse behtar. Answer me ek line likhein: Rule forty floor, Rule forty-one "
                "ceiling. Aur dono par Rule forty-four ka minimum."
            ),
            ),
        ],
        "covers": ["CHART-40", "CHART-41", "R40-BAND", "R41-LID", "FLOOR-CEILING-DIRECTION"],
        "chart": {
            "bars": [
                [
                    "Rule 40 • full superannuation",
                    60000,
                    SKY,
                ],
                [
                    "Rule 40 • FLOOR, two-thirds",
                    40000,
                    ORANGE,
                ],
                [
                    "Rule 41 • pension that would have been",
                    36000,
                    SKY,
                ],
                [
                    "Rule 41 • CEILING, two-thirds",
                    24000,
                    GREEN,
                ],
                [
                    "Rule 44 • minimum pension",
                    9000,
                    YELLOW,
                ],
            ],
            "max": 60000,
            "unit": "Rs per month",
            "note": "Illustration: Rule 40 base Rs 60,000, Rule 41 base Rs 36,000, two bases on purpose.",
        },
    },
    {
        "id": "c3_26_recap",
        "chapter": "CHAPTER 32 • RECAP OF PART 3: RULES 31 TO 41",
        "title": "RECAP — KEY NUMBERS, TOP TRAPS AND WHAT IS CURRENT",
        "badge": "RECAP • RULES 31-41",
        "q": "Can you recap Rules 31 to 41: the key numbers, the top traps, and how current this is?",
        "q_say": "Sir, Rules thirty-one se forty-one ka recap, key numbers, top traps, aur ye kitna current hai?",
        "hook": (
            "REMEMBER: Ten months, divide by ten, 2/3 floor in 40 and ceiling in 41, 15-30-45 days, check the latest "
            "O.M.!"
        ),
        "hook_say": "Yaad rakhiye: das mahine, das ka divisor, do-tihai, aur teen mahine — yahi poora part hai.",
        "layout": "dashboard",
        "boxes": [
            (
                "KEY NUMBERS",
                (
                "Average = last 10 months. Rule 37: 5 years, 3 months, 2 years. Rule 39: 15, 30, 45 days; Rs 54,000. "
                "Rules 40 and 41: 2/3, 3 months, 6 months."
            ),
                (
                "Rule 32: last ten months; month = 30 days; fractions rounded up (Rule 44(9)). Rule 44(1): 50% of "
                "emoluments or average, floor Rs 9,000, ceiling Rs 1,25,000 (dynamic; check the latest O.M.). Rule 37: 5 "
                "years for PSU rules, 3 months to opt, 2 years to repatriate. Rule 39: 15 days (request), 30 days "
                "(examination), 45 days (pension from Format 6); Medical Board threshold Rs 54,000 a month (dynamic). "
                "Rule 40: floor 2/3, final order in 3 months. Rule 41: ceiling 2/3, 3 months, 6 months transitional. "
                "Forms: Format 5 (relieving order, Rules 35 and 36), Format 6 (medical certificate, Rule 39). No DR or DA "
                "figure is in this batch."
            ),
                SKY,
                (
                "Key numbers. Average aakhri das mahine. Rule thirty-seven me paanch saal, teen mahine, do saal. Rule "
                "thirty-nine me pandrah, tees, paintalis din, aur fifty-four hazaar. Rules forty aur forty-one me "
                "do-tihai, teen mahine, chhah mahine. Format five relieving order, Format six medical certificate."
            ),
            ),
            (
                "TOP TRAPS",
                (
                "No DA in emoluments. Divisor stays ten. Rule 36 has no deeming rule. 2025 forfeiture. 45 days from "
                "Format 6. Floor in 40, ceiling in 41."
            ),
                (
                "Top traps: (1) emoluments exclude DA. (2) Rule 32(3) slides the window; divisor stays ten. (3) Rule "
                "32(2) is not a pay-fall shield. (4) Deemed absorption on silence is Rule 37(4) and 38(3), not Rule 36. "
                "(5) Since G.S.R. 340(E) of 22.05.2025 PSU dismissal or removal forfeits Government-service benefits. (6) "
                "The 45 days run from Format 6. (7) Two-thirds is a floor in Rule 40 and a ceiling in Rule 41. (8) Rule "
                "37(16) IDA against Rule 38(15) Central DA."
            ),
                RED,
                (
                "Top traps. Emoluments me DA nahi. Divisor das hi rehta hai. Rule thirty-six me deeming nahi. Two "
                "thousand twenty-five se PSU dismissal Government benefits bhi khatam. Paintalis din Format six se. Forty "
                "me floor, forty-one me ceiling."
            ),
            ),
            (
                "CURRENCY NOTE",
                "Current to G.S.R. 775(E) of 02.09.2026. Rules 31-41 read in the verbatim Gazette text.",
                (
                "Layers: (1) Rules 31 to 41 as notified by G.S.R. 868(E) of 20.12.2021, read this round in the verbatim "
                "Gazette text carried by the CAG-hosted copy - not a page summary; (2) amendments touching this part: "
                "G.S.R. 340(E) of 22.05.2025 (Rule 37(29)(c) forfeiture on PSU dismissal or removal), the O.M. of "
                "30.10.2025 (F.No. 38/10(03)/2025-P&PW(A)), and G.S.R. 775(E), the CCS (Pension) Amendment Rules, 2026, "
                "notified 2 September 2026 and published 7 September 2026, File No. 4/27/2026-P&PW(D), inserting the "
                "proviso to Rule 37(7) for erstwhile Ordnance Factory Board employees who do not opt for DPSU absorption; "
                "(3) G.S.R. 770(E) of 07.10.2022 and G.S.R. 410(E) of 16.07.2024 do not amend Rules 31 to 41 directly, so "
                "nothing in this part turns on them. Still to date against the latest O.M.: the Rs 9,000 floor, the Rs "
                "1,25,000 ceiling and the Rs 54,000 medical-board threshold."
            ),
                GREEN,
                (
                "Currency note. Ye part current hai do September do hazaar chhabbis tak, G.S.R. seven hundred "
                "seventy-five E, Rule thirty-seven, seven ka proviso. Is baar humne Rules thirty-one se forty-one tak ka "
                "asli Gazette text padha, summary nahi, isliye cards ka wording official text se check hai. Jo abhi bhi "
                "date ke saath likhna hai: rupaye nau hazaar ka floor, ek lakh pachchis hazaar ka ceiling, aur chauvan "
                "hazaar ka medical threshold, kyunki latest O.M. dobara nahi padha."
            ),
            ),
            (
                "NEXT BATCH",
                (
                "Part 4 covers Rules 42 to 52: premature retirement, gratuity, nomination, family pension and dearness "
                "relief."
            ),
                (
                "Next batch: Rules 42 and 43 (Chapter VI), Rules 44 to 49 (gratuity and nomination), Rules 50 and 51 "
                "(family pension and missing persons) and Rule 52 (dearness relief). Rule 44 will settle the minimum and "
                "maximum pension figures used in this part, and Rule 42 will check the claims flagged unverified here."
            ),
                ORANGE,
                (
                "Aage Part four: Rules forty-two se fifty-two, premature retirement, gratuity, nomination, family pension "
                "aur dearness relief. Rule forty-four yahan use kiye figures settle karega. Milte hain wahan."
            ),
            ),
        ],
        "covers": ["GSR-868E-2021", "GSR-410E-2024", "NEWER-NONE", "OM-22.06.2026", "DR-NONE"],
    },
]

PROVISIONS = [
    ("R31(1)", "Definition of emoluments + medical officer NPA", "COVERED", "ch1"),
    ("R31(1)-Expl", "Stagnation increment is emoluments", "COVERED", "ch1"),
    ("R31(2)", "Pay during leave / medical EOL / reinstated suspension", "COVERED", "ch2"),
    ("R31(2)-Prov", "Increases not actually drawn excluded, save (5), (10), (11)", "COVERED", "ch2"),
    ("R31(3)", "Higher post before leave needs a continuation certificate", "FIXED", "ch26"),
    ("R31(4)", "Pay drawn before non-qualifying EOL or suspension", "COVERED", "ch2"),
    ("R31(5)", "Increment earned during leave, not withheld", "COVERED", "ch2"),
    ("R31(6)", "Ex-cadre deputation or Armed Forces deputation", "FIXED", "ch26"),
    ("R31(6)-Prov", "Leave after release from the ex-cadre post", "FIXED", "ch26"),
    ("R31(7)", "State Government / foreign service: Central pay counts", "COVERED", "ch2"),
    ("R31(8)", "Re-employed pensioner, pension slice that cut pay", "FIXED", "ch26"),
    ("R31(9)", "Converted PSU/body pay only if he opts to retain benefits", "FIXED", "ch26"),
    ("R31(10)(i)", "Retrospective pay-scale increase, notional", "COVERED", "ch2"),
    ("R31(10)(ii)", "Retrospective promotion / exoneration / court order", "COVERED", "ch2"),
    ("R31(11)", "Death during a penalty that cut pay only while it ran", "FIXED", "ch26"),
    ("R32(1)", "Average of emoluments over the last ten months", "COVERED", "ch3"),
    ("R32(2)", "Leave with salary, medical EOL, reinstated suspension", "COVERED", "ch4"),
    ("R32(2)-Prov", "Increases not drawn excluded, save (4), (5), (6)", "COVERED", "ch4"),
    ("R32(3)", "Disregard the bad period, add an equal earlier period", "COVERED", "ch4"),
    ("R32(3)-Illus", "14/30 and 16/30 factors, retirement on 16 July 2019", "FIXED", "ch27"),
    ("R32(3)-Feb", "February is 30 days whether 28 or 29", "FIXED", "ch27"),
    ("R32(4)", "Increment earned during leave, not withheld", "COVERED", "ch4"),
    ("R32(5)(i),(ii)", "Notional retrospective increase inside the window", "COVERED", "ch4"),
    ("R32(6)", "Death during a penalty that cut pay only while it ran", "COVERED", "ch4"),
    ("R33", "Superannuation pension on age or on expiry of extension", "COVERED", "ch7"),
    ("R34(1)(a)", "Own volition: Rule 43 or FR 56", "COVERED", "ch7"),
    ("R34(1)(b)", "Declared surplus: Special VRS", "COVERED", "ch7"),
    ("R34(1)(c)", "Retired by Government: Rule 42 or FR 56", "COVERED", "ch7"),
    ("R34(2)", "SVRS ex-gratia is IN ADDITION to Rule 44 and 45", "COVERED", "ch8"),
    ("R35(1)", "Deemed retirement on absorption in a State", "COVERED", "ch9"),
    ("R35(1)-Prov", "Combined gratuity cap against a notional Central figure", "COVERED", "ch9"),
    ("R35(2)(i)", "Immediate absorption: date of joining", "COVERED", "ch9"),
    ("R35(2)(ii)", "After deputation: date resignation is accepted", "COVERED", "ch9"),
    ("R35(3)", "Relieving order in Format 5 with a joining period", "COVERED", "ch10"),
    ("R35(3)-Prov", "Joining period extendable in writing", "COVERED", "ch10"),
    ("R35(4)", "Gap regularised by leave due, else EOL", "COVERED", "ch10"),
    ("R35(5)", "Resignation accepted from the date preceding joining", "COVERED", "ch10"),
    ("R35(6)(a),(b)", "Option: Central benefits, or count service in the State", "COVERED", "ch10"),
    ("R35(7)", "Route (b): the State pays for the whole service", "COVERED", "ch10"),
    ("R36(1)", "Deemed retirement on absorption + gratuity cap", "COVERED", "ch11"),
    ("R36(2)(i),(ii)", "Date of absorption: joining, or foreign-service resignation", "COVERED", "ch11"),
    ("R36(3)", "Joint sector undertakings covered", "COVERED", "ch11"),
    ("R36(4)-(7)", "Format 5, joining period, leave for the gap, resignation", "COVERED", "ch11"),
    ("R36(8)", "No lien retained, connections severed", "COVERED", "ch11"),
    ("R36(9)(a),(b)", "Option: Central benefits or count service in the body", "COVERED", "ch12"),
    ("R36(10)", "Government pays a lump sum, one time", "COVERED", "ch12"),
    ("R36(11)", "Capitalised value + retirement gratuity up to absorption", "COVERED", "ch12"),
    ("R36(12)", "Computed on the 1981 commutation table", "COVERED", "ch12"),
    ("R36-Expl", "'Body' means autonomous body or statutory body", "COVERED", "ch11"),
    ("R37(1)", "En-masse deemed deputation, no deputation allowance", "COVERED", "ch13"),
    ("R37(2)", "5 years for rules, 3 months to ask, 3 months to opt", "FIXED", "ch29"),
    ("R37(3)", "Option exercised in the manner the Government specifies", "COVERED", "ch13"),
    ("R37(4)", "Silence = deemed permanent absorption", "COVERED", "ch13"),
    ("R37(5)", "Absorption effective from acceptance of options", "COVERED", "ch13"),
    ("R37(6)", "Posts stand abolished", "COVERED", "ch13"),
    ("R37(7)", "Repatriation within two years through the surplus cell", "COVERED", "ch13"),
    ("R37(7)-Prov26", "G.S.R. 775(E) proviso for ex-OFB employees", "COVERED", "ch13"),
    ("R37(8)", "Period till reversion is still deemed deputation", "COVERED", "ch13"),
    ("R37(9)", "Retire or die on deemed deputation: Central pay counts", "COVERED", "ch14"),
    ("R37(10)", "Payment in the manner the Ministry specifies", "COVERED", "ch14"),
    ("R37(11)", "Temporary in, casual labourers out", "COVERED", "ch14"),
    ("R37(12)(a),(b)", "Option: Central benefits or count PSU service", "COVERED", "ch14"),
    ("R37(13)", "Option (a): Central pay is the emoluments", "COVERED", "ch14"),
    ("R37(14)", "Option (b): combined service, incl. family pension", "COVERED", "ch14"),
    ("R37(15)(a)-Expl", "Emoluments on the IDA pattern", "COVERED", "ch14"),
    ("R37(16)", "Dearness relief on the Industrial DA pattern", "COVERED", "ch14"),
    ("R37(17)", "Voluntary retirement after 10 years of combined service", "COVERED", "ch14"),
    ("R37(18)", "Pension Fund created as a trust", "COVERED", "ch14"),
    ("R37(19)(a),(b)", "Board of Trustees, Ministry Secretary chairs", "COVERED", "ch14"),
    ("R37(20)", "Procedure on the recommendation of the Board", "COVERED", "ch14"),
    ("R37(21)(a)-(c)", "One-time lump sum, capitalised value, commutation table", "COVERED", "ch14"),
    ("R37(22)-(25)", "Liability sharing, contributions, shortfall, old pensioners", "COVERED", "ch14"),
    ("R37(26)-(28)", "BSNL and MTNL carve-out and its arrangements", "COVERED", "ch14"),
    ("R37(29)(a),(b)", "PF balance and leave balances transfer", "COVERED", "ch14"),
    ("R37(29)(c)", "2025 substitution: PSU dismissal forfeits Govt benefits", "COVERED", "ch16"),
    ("R37(30)", "51% disinvestment: adequate safeguards mandatory", "FIXED", "ch28"),
    ("R37(31)", "What the safeguards must contain", "FIXED", "ch28"),
    ("R38(1)", "En-masse transfer on deemed deputation", "COVERED", "ch15"),
    ("R38(2)", "5 years for rules, 3 months to ask, 3 months to opt", "COVERED", "ch15"),
    ("R38(3)", "Silence = deemed permanent absorption", "COVERED", "ch15"),
    ("R38(4)", "Absorption effective from acceptance", "COVERED", "ch15"),
    ("R38(5)", "Posts stand abolished", "FIXED", "ch15"),
    ("R38(6)", "Repatriation within two years", "FIXED", "ch15"),
    ("R38(7)", "Deemed deputation continues till reversion", "FIXED", "ch15"),
    ("R38(8)", "Retire or die during deemed deputation", "COVERED", "ch15"),
    ("R38(9)", "Payment in the manner the Ministry specifies", "COVERED", "ch15"),
    ("R38(10)", "Temporary in, casual labourers out", "COVERED", "ch15"),
    ("R38(11)(a),(b)", "Option: Central benefits or count service in the body", "COVERED", "ch15"),
    ("R38(12)", "Option (a): Central pay is the emoluments", "COVERED", "ch15"),
    ("R38(13)", "Manner of drawal", "COVERED", "ch15"),
    ("R38(14)-Expl", "Pension computed as if he retired from the Centre that day", "COVERED", "ch15"),
    ("R38(15)", "Dearness relief on the Central DA pattern", "COVERED", "ch15"),
    ("R38(16)-(21)", "Pension Fund, trustees, lump sum, commutation table", "COVERED", "ch15"),
    ("R38(22)-(25)", "Liability sharing, contributions, shortfall, old pensioners", "COVERED", "ch15"),
    ("R38(26)(a)-(c)", "PF, leave, and a later dismissal by the body", "FIXED", "ch28"),
    ("R38(27)", "51% disinvestment: adequate safeguards", "FIXED", "ch28"),
    ("R38(28)", "What the safeguards must contain", "FIXED", "ch28"),
    ("R38(29)", "Prasar Bharati / IIS / CSS carve-out", "FIXED", "ch28"),
    ("R39(1)", "RPwD Act section 20 cases are governed by that section", "COVERED", "ch17"),
    ("R39(1)-Prov", "Disability certificate under the RPwD Rules, 2017", "COVERED", "ch17"),
    ("R39(2)", "Application for invalid pension to the Head of Department", "COVERED", "ch17"),
    ("R39(2)-Prov1", "Spouse, or a family member, may apply", "COVERED", "ch17"),
    ("R39(2)-Prov2", "Option to continue on the same scale must be explained", "COVERED", "ch17"),
    ("R39(3)", "Request for examination within 15 days", "COVERED", "ch18"),
    ("R39(3)-30", "Examination not later than 30 days from the request", "COVERED", "ch18"),
    ("R39(3)(a),(b)", "Medical Board or Civil Surgeon; Rs 54,000 threshold", "COVERED", "ch18"),
    ("R39(4)", "Records age AND service-book age go to the medical authority", "FIXED", "ch29"),
    ("R39(5)", "Fit, or fit for less laborious work", "COVERED", "ch18"),
    ("R39(6)", "No certificate without the Head's request", "COVERED", "ch18"),
    ("R39(7)", "Lady doctor on the Board for a woman candidate", "COVERED", "ch18"),
    ("R39(8)", "Format 6 certificate; pension within 45 days", "COVERED", "ch19"),
    ("R39(9)", "Invalid pension below ten years of service", "COVERED", "ch19"),
    ("R39(9)-Prov", "Examined before OR after appointment and declared fit", "FIXED", "ch29"),
    ("R39(10)", "Lower post if fit for lighter work, else invalid pension", "COVERED", "ch19"),
    ("R40(1)", "Not less than two-thirds, not more than full", "COVERED", "ch20"),
    ("R40(2)", "UPSC before any order below full pension", "FIXED", "ch29"),
    ("R40(2)-Expl", "'Pension' includes retirement gratuity", "COVERED", "ch20"),
    ("R40(3)", "Provisional pension and gratuity at two-thirds at once", "COVERED", "ch20"),
    ("R40(4)", "Final order within three months; provisional continues", "COVERED", "ch20"),
    ("R40(5)", "Not below the Rule 44 minimum pension", "COVERED", "ch20"),
    ("R41(1)", "Dismissal or removal forfeits pension and gratuity", "COVERED", "ch23"),
    ("R41(1)-Prov", "Compassionate allowance not exceeding two-thirds", "COVERED", "ch23"),
    ("R41(2)", "Decision within three months of the penalty order", "COVERED", "ch23"),
    ("R41(3)(a)-(c)", "Merits, actual misconduct, dependants in exceptional cases", "COVERED", "ch23"),
    ("R41(4)", "Pre-commencement cases decided within six months", "COVERED", "ch23"),
    ("R41(5)", "No allowance after those six months", "COVERED", "ch23"),
    ("R41(6)", "Not below the Rule 44 minimum pension", "COVERED", "ch23"),
    ("R44(1)", "50% of the better of emoluments or average, floor and cap", "COVERED", "ch3"),
    ("R44(9)", "Rupee amounts rounded up, no fractions", "COVERED", "ch3"),
    ("O.M. 30.10.2025", "Portion of pension (10+ years) or of gratuity (under 10)", "COVERED", "ch24"),
    ("G.S.R. 340(E) 2025", "Substituted Rule 37(29)(c)", "COVERED", "ch16"),
    ("FR 9(21)(a)(i)", "Basic pay, the base of Rule 31 emoluments", "COVERED", "ch1"),
    ("R42 / R43", "Thirty-year and twenty-year exits, cited by Rule 34(1)", "EXTERNAL", "batch4"),
    ("FR 56", "Premature retirement, cited by Rule 34(1)", "EXTERNAL", "batch4"),
]


# ============================================================================
# LAYOUT GEOMETRY
# ============================================================================
META_H = 48
PILL_Y = 58
TITLE_Y = 100
TILES_Y = 176
TILES_H = 112
BODY_Y = 296
BODY_BOTTOM = 812
BAND_Y = 828
BAND_H = 76
BAR_Y = 1046


def tiles_geom(n=4, x0=40, x1=1880, gap=18):
    n = max(1, min(4, n))
    w = (x1 - x0 - gap * (n - 1)) // n
    return [(x0 + i * (w + gap), TILES_Y, w, TILES_H) for i in range(n)]


def rows_geom(n, x0=40, x1=1880, top=BODY_Y, bottom=BODY_BOTTOM, gap=14):
    if n <= 0:
        return []
    h = min(126, (bottom - top - gap * (n - 1)) // n)
    return [(x0, top + i * (h + gap), x1 - x0, h) for i in range(n)]


def tile_sub(text, limit=36):
    """One-line fragment under a tile heading, cut at a word boundary."""
    raw = re.sub(r"\s+", " ", str(text)).strip().replace("'", "").replace('"', "")
    s = raw
    for cut in (". ", "; ", ", "):
        if cut in s[:limit + 12]:
            s = s.split(cut)[0]
            break
    if len(s) > limit:
        s = s[:limit].rsplit(" ", 1)[0].rstrip(",;:.")
    if len(s) < len(raw):
        s = s.rstrip(",;:.") + " ..."
    return s


def pretty_money(v):
    v = int(round(v))
    s = str(v)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts + [tail])


# ============================================================================
# BOARD CHROME
# ============================================================================
def draw_chrome(d, sc, ctx, reveal, total_steps):
    accent = sc.get("accent") or sc["boxes"][0][3]

    # meta strip
    d.rectangle([0, 0, W, META_H], fill=(6, 8, 20))
    pair = f"{ctx['idx']:02d}/{ctx['total']:02d}"
    fm = font(19, True, mono=True)
    d.text((40, 14), pair, font=fm, fill=ORANGE)
    mx = 40 + text_w(d, pair, fm) + 20
    label = sc["chapter"].upper()
    fl = font(16, True)
    cut = False
    while text_w(d, label, fl) > (W - 1180 - mx) and len(label) > 8:
        label = label[:-2].rstrip(" •-")
        cut = True
    if cut:
        label = label.rstrip(" .") + " ..."
    d.text((mx, 16), label, font=fl, fill=MUTED)
    wave_bars(d, W - 1075, 16, 34, (40, 74, 110))

    right = W - 40
    tc = ctx.get("timecode", "00:00/00:00")
    f_tc = font(18, True, mono=True)
    w = text_w(d, tc, f_tc) + 30
    d.rounded_rectangle([right - w, 9, right, 39], radius=15, fill=lerp(CARD_BG, ORANGE, 0.18), outline=ORANGE, width=2)
    d.text((right - w + 15, 15), tc, font=f_tc, fill=ORANGE)
    right -= w + 10
    right -= chip(d, right, 9, "BATCH 3 • RULES 31-41", GREEN) + 10
    right -= chip(d, right, 9, "VOICE • CITY HINGLISH", BLUE) + 10

    # violet code pill
    pill = ctx.get("pill", "")
    fp = font(16, True)
    pw = text_w(d, pill, fp) + 34
    d.rounded_rectangle([40, PILL_Y, 40 + pw, PILL_Y + 32], radius=16,
                        fill=lerp(CARD_BG, VIOLET, 0.30), outline=VIOLET, width=2)
    d.text((57, PILL_Y + 7), pill, font=fp, fill=(226, 220, 255))

    # badge chip, right aligned on the pill row
    bd = sc["badge"].upper()
    fb = font(18, True)
    bw = text_w(d, bd, fb) + 34
    solid = accent in LIGHT_ACCENTS
    d.rounded_rectangle([W - 40 - bw, PILL_Y, W - 40, PILL_Y + 32], radius=16, fill=accent)
    d.text((W - 40 - bw + 17, PILL_Y + 7), bd, font=fb,
           fill=TEXT_ON_LIGHT if solid else TEXT_WHITE)

    # panel title
    f_t, l_t, lh_t, _ = fit(d, sc["title"], True, 1660, 62, PANEL_TITLE_START, PANEL_TITLE_MIN, 1.06)
    for i, ln in enumerate(l_t[:2]):
        d.text((40, TITLE_Y + i * lh_t), ln, font=f_t, fill=TEXT_WHITE)
    d.line([(40, TITLE_Y + len(l_t[:2]) * lh_t + 6), (W - 40, TITLE_Y + len(l_t[:2]) * lh_t + 6)],
           fill=(44, 52, 82), width=1)


def draw_tiles(d, sc, rows, active=None):
    boxes = sc["boxes"][:4]
    for i, (x, y, w, h), b in zip(range(4), tiles_geom(len(boxes)), boxes):
        col = b[3]
        hot = active is not None and i == active
        fill = lerp(CARD_BG, col, 0.30 if hot else 0.12)
        d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=fill, outline=col, width=3 if hot else 2)
        f1, l1, lh1, _ = fit(d, b[0], True, w - 44, 56, TILE_TITLE_START, TILE_TITLE_MIN, 1.10)
        ty = y + 14
        for k, ln in enumerate(l1[:2]):
            d.text((x + 22, ty + k * lh1), ln, font=f1, fill=col)
        ty += len(l1[:2]) * lh1 + 6
        room = h - (ty - y) - 8
        f2, l2, lh2, _ = fit(d, tile_sub(b[1]), False, w - 44, max(room, 16), 21, 14, 1.14)
        d.text((x + 22, ty), l2[0], font=f2, fill=MUTED)


def draw_rows(d, rows, n_visible, hook_at=None, show_band=False):
    geo = rows_geom(len(rows), bottom=BODY_BOTTOM - (BAND_H + 22 if show_band else 0))
    for i, (card, (x, y, w, h)) in enumerate(zip(rows, geo)):
        if i >= n_visible:
            d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=(14, 17, 32),
                                outline=(30, 36, 58), width=1)
            for k in range(3):
                d.ellipse([x + 28 + k * 16, y + h // 2 - 3, x + 34 + k * 16, y + h // 2 + 3],
                          fill=(40, 48, 74))
            continue
        label, text, col = card[0], card[1], card[3]
        is_hook = (hook_at is not None and i == hook_at)
        if is_hook:
            label = "KEY TAKEAWAY"
            text = re.sub(r"^\s*REMEMBER\s*[:\-]?\s*", "", str(text), flags=re.I)
            text = text[:1].upper() + text[1:] if text else text
        newest = (i == n_visible - 1)
        if is_hook:
            d.rounded_rectangle([x, y, x + w, y + h], radius=14,
                                fill=lerp(CARD_BG, YELLOW, 0.12), outline=YELLOW, width=2)
        else:
            d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=CARD_BG_2,
                                outline=lerp(CARD_BG, col, 0.55 if not newest else 0.95),
                                width=2 if not newest else 3)
        d.rectangle([x, y + 10, x + 6, y + h - 10], fill=YELLOW if is_hook else col)
        lab_w = 430
        f_l, l_l, lh_l, _ = fit(d, label, True, lab_w - 40, h - 20, ROW_LABEL_START, ROW_LABEL_MIN, 1.16)
        ly = y + (h - len(l_l) * lh_l) // 2
        for k, ln in enumerate(l_l[:3]):
            d.text((x + 26, ly + k * lh_l), ln, font=f_l, fill=YELLOW if is_hook else col)
        f_b, l_b, lh_b, _ = fit(d, text, False, w - lab_w - 40, h - 24, ROW_BODY_START, ROW_BODY_MIN, 1.24)
        ty = y + (h - len(l_b) * lh_b) // 2
        d.text((x + lab_w, ty), "\n".join(l_b), font=f_b, fill=TEXT_WHITE, spacing=int(lh_b * 0.16))


def draw_band(d, text, prefix="CLASSIC UPSC TRAP:"):
    x0, y0, x1 = 40, BAND_Y, W - 40
    d.rounded_rectangle([x0, y0, x1, y0 + BAND_H], radius=16,
                        fill=lerp(CARD_BG, ORANGE, 0.14), outline=ORANGE, width=3)
    f_p = font(19, True)
    pw = text_w(d, prefix, f_p) + 28
    d.rounded_rectangle([x0 + 18, y0 + 14, x0 + 18 + pw, y0 + 46], radius=15,
                        fill=lerp(CARD_BG, ORANGE, 0.32), outline=ORANGE, width=2)
    d.text((x0 + 32, y0 + 21), prefix, font=f_p, fill=ORANGE)
    bx = x0 + 18 + pw + 22
    if prefix.upper().startswith("REMEMBER"):
        text = re.sub(r"^\s*REMEMBER\s*[:\-]?\s*", "", str(text), flags=re.I)
        text = text[:1].upper() + text[1:] if text else text
    f_b, l_b, lh_b, size = fit(d, text, True, x1 - bx - 30, BAND_H - 22, 25, 15, 1.18)
    ty = y0 + (BAND_H - len(l_b) * lh_b) // 2
    for k, ln in enumerate(l_b[:2]):
        d.text((bx, ty + k * lh_b), ln, font=f_b, fill=TEXT_WHITE)


SHOW_FOOTER = True     # off when burned captions occupy the same band


def draw_footer(d, sc, ctx):
    if not SHOW_FOOTER:
        return
    y = BAND_Y + BAND_H + 8
    d.line([(40, y), (W - 40, y)], fill=(34, 40, 66), width=1)
    nxt = ctx.get("next")
    f = font(17, True)
    if nxt:
        d.text((40, y + 14), "NEXT", font=font(15, True), fill=FAINT)
        d.text((104, y + 12), nxt[:96], font=f, fill=MUTED)
    right = "RULES 31-41  •  PART 3 OF 6  •  ENGLISH BOARD, HINGLISH VOICE"
    d.text((W - 40 - text_w(d, right, font(15, True)), y + 14), right,
           font=font(15, True), fill=(70, 80, 106))


def draw_lower_third(d, sc, ctx):
    """Caption lane for the --captions none path: the line being spoken, on a dark plate."""
    if SHOW_LOWER_THIRD is None:
        return
    text = SHOW_LOWER_THIRD
    if not text:
        return
    y0 = BAR_Y - 108
    f, l, lh, size = fit(d, text, True, W - 320, 70, 34, 20, 1.18)
    l = l[:2]
    box_w = max(text_w(d, ln, f) for ln in l) + 60
    x0 = (W - box_w) // 2
    d.rounded_rectangle([x0, y0, x0 + box_w, y0 + len(l) * lh + 22], radius=12,
                        fill=(6, 8, 18), outline=(44, 52, 82), width=1)
    for k, ln in enumerate(l):
        d.text((x0 + 30, y0 + 11 + k * lh), ln, font=f, fill=(250, 250, 255))


SHOW_LOWER_THIRD = None    # set per frame when captions are produced by the board


def draw_progress(d, sc, ctx, step, steps):
    d.rectangle([0, BAR_Y, W, BAR_Y + 13], fill=(16, 20, 38))
    seg = W / max(ctx["total"], 1)
    d.rectangle([0, BAR_Y, int(seg * (ctx["idx"] - 1)), BAR_Y + 13], fill=lerp(ORANGE, (255, 255, 255), 0.25))
    inner = min(1.0, step / max(steps, 1))
    d.rectangle([int(seg * (ctx["idx"] - 1)), BAR_Y,
                 int(seg * (ctx["idx"] - 1) + seg * inner), BAR_Y + 13], fill=ORANGE)
    for k in range(ctx["total"] + 1):
        d.line([(int(seg * k), BAR_Y), (int(seg * k), BAR_Y + 13)], fill=(9, 11, 30), width=1)
    d.rectangle([0, BAR_Y + 13, W, H], fill=(8, 10, 22))


# ============================================================================
# TABLE / CHART BODIES
# ============================================================================
def draw_table(d, spec, focus=-1):
    cols, rows = spec["cols"], spec["rows"]
    fracs = spec.get("widths") or [1 / len(cols)] * len(cols)
    x0, x1 = 40, W - 40
    total_w = x1 - x0
    widths = [int(total_w * f) for f in fracs]
    widths[-1] = total_w - sum(widths[:-1])
    y = BODY_Y
    avail = BODY_BOTTOM - BODY_Y
    n = len(rows)
    head_h = 44
    row_h = min(96, (avail - head_h - n * 6) // max(n, 1))
    accent_col = spec.get("accent_col", 0)

    # header
    f_h = font(19, True)
    cx = x0
    for i, c in enumerate(cols):
        d.text((cx + 16, y + 13), c.upper(), font=f_h, fill=MUTED)
        cx += widths[i]
    d.line([(x0, y + head_h - 4), (x1, y + head_h - 4)], fill=(58, 66, 96), width=2)
    y += head_h

    for r, row in enumerate(rows):
        hot = (r == focus)
        if hot:
            d.rounded_rectangle([x0 - 6, y - 2, x1 + 6, y + row_h - 4], radius=10,
                                fill=lerp(CARD_BG, ORANGE, 0.16), outline=ORANGE, width=2)
        elif r % 2 == 0:
            d.rounded_rectangle([x0 - 6, y - 2, x1 + 6, y + row_h - 4], radius=10, fill=CARD_BG)
        cx = x0
        for i, cell in enumerate(row):
            f_c, l_c, lh_c, size = fit(d, str(cell), i == 0, widths[i] - 30, row_h - 14,
                                       TABLE_START, TABLE_MIN, 1.2)
            col = TEXT_WHITE
            if i == 0:
                col = RED if str(cell).upper().startswith("STILL OPEN") else SKY
            elif i == accent_col:
                col = GREEN
            ty = y + (row_h - len(l_c) * lh_c) // 2
            for k, ln in enumerate(l_c[:3]):
                d.text((cx + 16, ty + k * lh_c), ln, font=f_c, fill=col)
            cx += widths[i]
        y += row_h
    d.line([(x0, min(y, BODY_BOTTOM)), (x1, min(y, BODY_BOTTOM))], fill=(58, 66, 96), width=1)


def draw_chart(d, spec, focus=-1):
    bars = spec["bars"]
    vmax = float(spec.get("max") or max(b[1] for b in bars))
    x0, x1 = 40, W - 40
    lab_right = x0 + 600
    bar_x = lab_right + 30
    bar_max = (x1 - 230) - bar_x
    top = BODY_Y + 42
    bottom = BAND_Y - 46
    n = len(bars)
    gap = 14
    bh = min(74, (bottom - top - gap * (n - 1)) // max(n, 1))
    y = top + max(0, ((bottom - top) - (n * bh + (n - 1) * gap)) // 2)

    # gridlines + axis
    for g in range(0, 5):
        gx = bar_x + int(bar_max * g / 4)
        d.line([(gx, top - 8), (gx, bottom + 2)], fill=(38, 44, 70), width=1)
        f_g = font(15, False)
        lab = pretty_money(vmax * g / 4)
        d.text((gx - text_w(d, lab, f_g) // 2, bottom + 8), lab, font=f_g, fill=FAINT)
    f_u = font(16, True)
    d.text((x0 + 8, BODY_Y - 2), spec.get("unit", "Rs per month").upper(), font=f_u, fill=MUTED)
    note = spec.get("note")
    if note:
        f_n = font(15, False)
        d.text((x1 - 8 - text_w(d, note, f_n), BODY_Y - 1), note, font=f_n, fill=FAINT)

    for i, (label, value, colour) in enumerate(bars):
        hot = (i == focus)
        f_l, l_l, lh_l, _ = fit(d, label, True, lab_right - x0 - 20, bh - 6, 26, 16, 1.12)
        ly = y + (bh - len(l_l) * lh_l) // 2
        for k, ln in enumerate(l_l[:2]):
            d.text((x0 + 14, ly + k * lh_l), ln, font=f_l, fill=TEXT_WHITE if not hot else YELLOW)
        bw = max(8, int(bar_max * (value / vmax)))
        d.rounded_rectangle([bar_x, y + (bh - 34) // 2, bar_x + bw, y + (bh + 34) // 2],
                            radius=8, fill=colour, outline=YELLOW if hot else None, width=3)
        f_v = font(24 if hot else 22, True)
        d.text((bar_x + bw + 14, y + (bh - 24) // 2), pretty_money(value), font=f_v,
               fill=YELLOW if hot else TEXT_WHITE)
        y += bh + gap




# ============================================================================
# FRAME RENDERER
# ============================================================================
def scene_parts(sc):
    """Split the house cards into ledger rows, the amber hook row and the trap band."""
    rows, trap = [], None
    for b in sc["boxes"]:
        if trap is None and re.search(r"\bTRAP", b[0]):
            trap = b
        else:
            rows.append(b)
    if len(rows) > 4:
        rows = rows[:4]
    hook_row = None
    if len(rows) < 4 and sc.get("hook"):
        hook_row = ("KEY TAKEAWAY", sc["hook"], sc["hook"], YELLOW, sc.get("hook_say", ""))
    return rows, hook_row, trap


def steps_for(sc):
    rows, hook_row, trap = scene_parts(sc)
    return len(rows) + (1 if hook_row else 0) + (1 if (trap or not hook_row) else 0)


def render_frame(sc, ctx, reveal, kind, out_path: Path):
    accent = sc.get("accent") or sc["boxes"][0][3]
    rows, hook_row, trap = scene_parts(sc)
    img, d = background(accent)
    draw_chrome(d, sc, ctx, reveal, steps_for(sc))

    layout = sc.get("layout", "dashboard")
    draw_tiles(d, sc, rows, active=(reveal - 1 if kind == "answer" and reveal else None))

    all_rows = list(rows) + ([hook_row] if hook_row else [])
    if kind in ("trap", "hook"):
        visible_rows = len(all_rows)
    elif kind == "answer":
        visible_rows = reveal
    else:
        visible_rows = 0

    if layout == "table" and sc.get("table"):
        draw_table(d, sc["table"], focus=(reveal - 1) if kind == "answer" else -1)
        # the table fills the board; rows still narrate underneath via the band
        if visible_rows and kind in ("trap", "hook"):
            pass
    elif layout == "chart" and sc.get("chart"):
        draw_chart(d, sc["chart"], focus=(reveal - 1) if kind == "answer" else -1)
    else:
        draw_rows(d, all_rows, visible_rows, hook_at=(len(rows) if hook_row else None),
                  show_band=(kind == "hook" and not hook_row))

    def tight_band(text, colour=YELLOW, outline=YELLOW):
        text = re.sub(r"^\s*REMEMBER\s*[:\-]?\s*", "", str(text), flags=re.I)
        text = text[:1].upper() + text[1:] if text else text
        d.rounded_rectangle([40, BAND_Y, W - 40, BAND_Y + BAND_H], radius=16,
                            fill=lerp(CARD_BG, colour, 0.10), outline=outline, width=2)
        f, l, lh, size = fit(d, text, True, W - 140, BAND_H - 16, 24, 15, 1.18)
        for k, ln in enumerate(l[:2]):
            d.text(((W - text_w(d, ln, f)) // 2, BAND_Y + (BAND_H - len(l) * lh) // 2 + k * lh),
                   ln, font=f, fill=YELLOW)

    if kind == "trap" and trap:
        draw_band(d, trap[1])
    elif kind == "hook":
        if hook_row:
            summary = (f"{sc['chapter'].split(' • ', 1)[-1]}  •  "
                       f"{len(sc['boxes'])} cards  •  {len(sc['covers'])} tagged points checked")
            draw_band(d, summary, prefix="CHAPTER CLOSED")
        else:
            tight_band(sc["hook"])
    elif kind in ("intro", "question") and not trap:
        tight_band(sc["hook"])

    draw_footer(d, sc, ctx)
    draw_lower_third(d, sc, ctx)
    draw_progress(d, sc, ctx, reveal + (1 if kind in ("trap", "hook") else 0), steps_for(sc))
    img.save(out_path)


# ============================================================================
# SEGMENTS / AUDIO / SUBTITLES
# ============================================================================
def build_segments(sc):
    rows, hook_row, trap = scene_parts(sc)
    segs = []
    if sc.get("intro"):
        segs.append(("teacher", sc["intro"], 0, "intro"))
    segs.append(("student", sc["q_say"], 0, "question"))
    for i, b in enumerate(rows):
        segs.append(("teacher", b[4], i + 1, "answer"))
    if trap:
        segs.append(("teacher", trap[4], len(rows) + 1, "trap"))
    if hook_row:
        segs.append(("teacher", hook_row[4], len(rows) + (1 if trap else 0) + 1, "hook"))
    elif sc.get("hook_say"):
        segs.append(("teacher", sc["hook_say"], len(rows) + (1 if trap else 0) + 1, "hook"))
    return segs


def probe_duration(path: Path) -> float:
    """ffprobe when available, else ffmpeg's own progress report, else a byte estimate."""
    if FFPROBE and Path(FFPROBE).exists():
        try:
            out = subprocess.check_output(
                [FFPROBE, "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=noprint_wrappers=1:nokey=1", str(path)], text=True).strip()
            return float(out)
        except Exception:
            pass
    try:
        rep = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path), "-f", "null", "-"],
                             capture_output=True, text=True).stderr
        marks = re.findall(r"time=(\d+):(\d\d):(\d\d\.\d+)", rep)
        if marks:
            h, m, sec = marks[-1]
            return int(h) * 3600 + int(m) * 60 + float(sec)
    except Exception:
        pass
    return max(1.0, path.stat().st_size / 16000.0)


def silent_audio(text: str, out: Path) -> float:
    dur = max(1.6, len(text.split()) / 2.45)
    subprocess.run([FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono",
                    "-t", f"{dur:.2f}", "-c:a", "libmp3lame", str(out)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return dur


async def tts_segment(text, voice, out: Path, rate, sem, retries=4):
    import edge_tts
    text = normalize_for_tts(text)
    async with sem:
        last = None
        for attempt in range(retries):
            try:
                try:
                    com = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
                except TypeError:
                    com = edge_tts.Communicate(text, voice, rate=rate)
                words = []
                with open(out, "wb") as f:
                    async for ch in com.stream():
                        if ch["type"] == "audio":
                            f.write(ch["data"])
                        elif ch["type"] == "WordBoundary":
                            s = ch["offset"] / 1e7
                            words.append((ch["text"], s, s + ch["duration"] / 1e7))
                if out.stat().st_size < 500:
                    raise RuntimeError("empty audio returned")
                return words
            except Exception as e:
                last = e
                await asyncio.sleep(1.5 * (attempt + 1))
        raise RuntimeError(f"edge-tts failed for {out.name}: {last}")


def fmt_ass(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def ass_escape(s: str) -> str:
    return s.replace("{", "(").replace("}", ")").replace("\n", " ")


def write_ass(cues, path: Path):
    head = (
        "[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\n"
        "WrapStyle: 0\nScaledBorderAndShadow: yes\n\n"
        "[V4+ Styles]\n"
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding\n"
        "Style: Teacher,DejaVu Sans,38,&H00FFFFFF,&H00E8A220,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,3,1,2,120,120,54,1\n"
        "Style: Student,DejaVu Sans,38,&H00E8C456,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,3,1,2,120,120,54,1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"
    )
    lines = [head]
    for s, e, style, txt in cues:
        lines.append(f"Dialogue: 0,{fmt_ass(s)},{fmt_ass(e)},{style},,0,0,0,,{ass_escape(txt)}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def make_cues(words, offset, style, max_words=7, max_chars=48):
    cues, buf = [], []

    def flush(end_extra=0.12):
        if not buf:
            return
        cues.append((offset + buf[0][1], offset + buf[-1][2] + end_extra, style,
                     " ".join(w[0] for w in buf)))
        buf.clear()

    for w in words:
        buf.append(w)
        joined = " ".join(x[0] for x in buf)
        if len(buf) >= max_words or len(joined) > max_chars or w[0].endswith((".", "?", "!", ":")):
            flush()
    flush(0.15)
    return cues


def even_words(text, dur):
    toks = text.split()
    step = dur / max(len(toks), 1)
    return [(t, i * step, (i + 1) * step) for i, t in enumerate(toks)]


def write_reference_sheet(scenes):
    out = ["# CCS (Pension) Rules 2021 — Batch 3 (Rules 31–41) — full-wording reference sheet", "",
           "Every card on screen is a short key point. The examinable wording behind each card is here,",
           "checked against the verbatim Gazette text of Rules 31 to 41.", ""]
    for sc in scenes:
        out += [f"## {sc['chapter']}", f"**{sc['title']}**  ({sc['badge']})", "", f"Q: {sc['q']}", ""]
        for b in sc["boxes"]:
            out += [f"### {b[0]}", b[2], ""]
            out += [f"*Spoken (Hinglish):* {b[4]}", ""]
        out += [f"> {sc['hook']}", ""]
    REFERENCE_SHEET.write_text("\n".join(out), encoding="utf-8")
    return REFERENCE_SHEET


# ============================================================================
# AUDIT
# ============================================================================
def audit_density():
    img, d = background()
    bad = 0
    print(f"{'scene':30s} {'layout':10s} {'cards':>5s} rows trap  note")
    for sc in SCENES:
        rows, hook_row, trap = scene_parts(sc)
        note = ""
        try:
            for b in rows:
                fit(d, b[0], True, 430 - 44, 150, ROW_LABEL_START, ROW_LABEL_MIN, 1.16)
                fit(d, b[1], False, (W - 80) - 430 - 44, 150, ROW_BODY_START, ROW_BODY_MIN, 1.26)
            if hook_row:
                fit(d, hook_row[1], False, (W - 80) - 430 - 44, 150, ROW_BODY_START, ROW_BODY_MIN, 1.26)
            fit(d, sc["title"], True, 1660, 62, PANEL_TITLE_START, PANEL_TITLE_MIN, 1.06)
            for b in sc["boxes"][:4]:
                fit(d, b[0], True, 446 - 44, 56, TILE_TITLE_START, TILE_TITLE_MIN, 1.10)
                fit(d, tile_sub(b[1]), False, 446 - 44, 26, 21, 14, 1.14)
            if sc.get("layout") == "table" and sc.get("table"):
                for r in sc["table"]["rows"]:
                    for i, cell in enumerate(r):
                        fit(d, str(cell), i == 0, 300, 60, TABLE_START, TABLE_MIN, 1.2)
            note = "ok"
        except ValueError as e:
            bad += 1
            note = f"FAIL {e}"
        print(f"{sc['id'][:30]:30s} {sc.get('layout','dashboard'):10s} {len(sc['boxes']):5d} "
              f"{len(rows):4d} {'yes' if trap else ' - ':4s}  {note}")
    print()
    by = {}
    for code, label, status, _where in PROVISIONS:
        by[status] = by.get(status, 0) + 1
    print("PROVISION COVERAGE (Rules 31-41, verbatim Gazette text)")
    print("-" * 108)
    for code, label, status, where in PROVISIONS:
        print(f"  {code:16s} {status:9s} {label[:62]:62s} {where}")
    print("-" * 108)
    total = len(PROVISIONS)
    covered = by.get("COVERED", 0) + by.get("FIXED", 0)
    print(f"  {total} provisions tracked | {covered} covered | "
          f"{by.get('OPEN', 0)} open | {by.get('EXTERNAL', 0)} outside this batch")
    print(f"\n{'ALL CARDS WITHIN BUDGET' if not bad else str(bad) + ' CARD(S) OVER BUDGET'}")
    return bad


def audit_only_failures():
    return audit_density()


# ============================================================================
# MAIN
# ============================================================================
async def main():
    ap = argparse.ArgumentParser(description="Batch 3 dashboard explainer (English board, Hinglish voice)")
    ap.add_argument("--audit", action="store_true", help="density + provision coverage report, no ffmpeg needed")
    ap.add_argument("--preview", action="store_true", help="render one slide per scene, no audio")
    ap.add_argument("--no-tts", action="store_true", help="silent audio for layout/timing tests")
    ap.add_argument("--part", type=int, choices=(1, 2, 3), help="build one third of the chapters")
    ap.add_argument("--layout", choices=("dashboard", "table", "chart"), help="force one layout everywhere")
    ap.add_argument("--voice", help="override the teacher voice")
    ap.add_argument("--rate", default=DEFAULT_RATE)
    ap.add_argument("--only", help="build a single scene id")
    ap.add_argument("--captions", choices=("burn", "soft", "none"), default="burn",
                    help="burn into the picture (needs libass), soft-mux, or leave them out")
    ap.add_argument("--verify", action="store_true", help="report the ffmpeg / ffprobe this build will use")
    ap.add_argument("--build-dir", default=None,
                    help="scratch directory for slides, audio and clips (default pension_b3_build)")
    args = ap.parse_args()

    global SCENES
    if args.verify or args.audit:
        ok, subs, info = probe_ffmpeg()
        print(f"ffmpeg   : {info}")
        print(f"ffprobe  : {FFPROBE or 'missing (duration falls back to ffmpeg parsing)'}")
        print(f"libass   : {'yes (subtitles burned into the picture)' if subs else 'no (captions soft-muxed)'}")
        if not ok:
            print(f"WARNING  : {info}\n           --audit, --preview and the PNG slides still work")
    if args.verify and not (args.audit or args.preview or args.no_tts or args.only or args.part):
        return
    if args.audit:
        sys.exit(1 if audit_density() else 0)

    if args.part:
        starts = [0, len(SCENES) // 3, 2 * len(SCENES) // 3]
        SCENES = SCENES[starts[args.part - 1]: (starts + [len(SCENES)])[args.part]]
    if args.only:
        SCENES = [s for s in SCENES if s["id"] == args.only]
        if not SCENES:
            sys.exit(f"no scene id {args.only!r}")
        globals()["OUTPUT_MP4"] = Path(f"{OUT_STEM}_{args.only}.mp4")

    if args.layout:
        for sc in SCENES:
            sc["layout"] = args.layout

    global SHOW_FOOTER
    SHOW_FOOTER = False        # in the film the caption lane owns that strip

    if getattr(args, "build_dir", None):
        global BUILD_DIR, SLIDES_DIR, AUDIO_DIR
        BUILD_DIR = Path(args.build_dir)
        SLIDES_DIR = BUILD_DIR / "slides"
        AUDIO_DIR = BUILD_DIR / "audio"

    teacher = args.voice or DEFAULT_TEACHER
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    write_reference_sheet(SCENES)

    total = len(SCENES)
    ctx_of = {sc["id"]: {"idx": i + 1, "total": total,
                         "next": SCENES[i + 1]["title"] if i + 1 < total else None,
                         "pill": f"CCS (PENSION) RULES 2021  •  PART 3  •  RULES 31-41  •  {len(sc['covers'])} TAGGED POINTS"}
              for i, sc in enumerate(SCENES)}

    if args.preview:
        print(f"=== preview: {total} slides -> {SLIDES_DIR}")
        for sc in SCENES:
            rows_, hook_, trap_ = scene_parts(sc)
            kind = "trap" if trap_ else "hook"
            render_frame(sc, ctx_of[sc["id"]], len(rows_), kind, SLIDES_DIR / f"{sc['id']}.png")
        print("done")
        return

    print(f"=== Step 1: {total} scenes, {sum(len(s['boxes']) for s in SCENES)} cards")
    sem = asyncio.Semaphore(4)
    plan, durations, tts_failures = [], {}, 0
    for sc in SCENES:
        segs = build_segments(sc)
        per = []
        for i, (speaker, text, reveal, kind) in enumerate(segs):
            out = AUDIO_DIR / f"{sc['id']}_{i:02d}.mp3"
            if args.no_tts:
                dur = silent_audio(text, out)
                words = even_words(normalize_for_tts(text), dur)
            else:
                try:
                    words = await tts_segment(text, teacher if speaker == "teacher" else DEFAULT_STUDENT,
                                              out, args.rate, sem)
                except Exception as e:
                    tts_failures += 1
                    if tts_failures <= 3:
                        print(f"  !! {sc['id']} seg {i}: {e}")
                    dur = silent_audio(text, out)
                    words = even_words(normalize_for_tts(text), dur)
                dur = probe_duration(out)
                if not words:
                    words = even_words(normalize_for_tts(text), dur)
            per.append((out, dur, words, speaker, reveal, kind))
        plan.append((sc, per))
        durations[sc["id"]] = sum(p[1] for p in per)

    grand = sum(durations.values())
    print(f"    total narration {grand/60:.1f} min")
    if tts_failures:
        print(f"\n!! {tts_failures} narration segments could NOT be voiced (edge-tts unavailable).")
        print("   This run would produce a SILENT video with even-paced placeholder captions.")
        print("   Install the voice engine and re-run:   pip install edge-tts")
        print("   edge-tts needs outbound HTTPS to speech.platform.bing.com.")
        print("   To rehearse layout and timing offline on purpose, use:  --no-tts\n")
        sys.exit(2)

    print("=== Step 2: slides")
    offset = 0.0
    cues, clips = [], []
    for sc, per in plan:
        ctx = dict(ctx_of[sc["id"]])
        t0 = offset
        ctx["timecode"] = f"{int(t0//60):02d}:{int(t0%60):02d}/" \
                          f"{int((t0+durations[sc['id']])//60):02d}:{int((t0+durations[sc['id']])%60):02d}"
        steps = steps_for(sc)
        for (out, dur, words, speaker, reveal, kind) in per:
            idx = max(0, min(steps, reveal + (1 if kind in ("trap", "hook") else 0)))
            png = SLIDES_DIR / f"{sc['id']}_{kind}_{reveal:02d}.png"
            render_frame(sc, ctx, reveal, kind, png)
            clip = BUILD_DIR / f"clip_{sc['id']}_{kind}_{reveal:02d}.mp4"
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-i", str(png),
                            "-i", str(out), "-t", f"{dur:.3f}", "-r", "25",
                            "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-pix_fmt", "yuv420p",
                            "-c:a", "aac", "-b:a", "192k", "-shortest", str(clip)], check=True)
            clips.append(clip)
            cues.extend(make_cues(words, offset, "Teacher" if speaker == "teacher" else "Student"))
            offset += dur

    print("=== Step 3: concat + burn subtitles")
    concat = BUILD_DIR / "concat.txt"
    concat.write_text("\n".join(f"file '{c.name}'" for c in clips) + "\n", encoding="utf-8")
    raw = BUILD_DIR / "raw_concat.mp4"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", str(concat), "-c", "copy", str(raw)], check=True)
    ass = BUILD_DIR / "subtitles.ass"
    write_ass(cues, ass)

    def burn(path_out: Path, mode: str) -> None:
        base_audio = ["-af", "loudnorm=I=-16:TP=-1.5:LRA=11"]
        enc = ["-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p",
               "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "1",
               "-movflags", "+faststart"]
        if mode == "burn":
            esc = str(ass.resolve()).replace("\\", "/").replace(":", "\\:").replace("'", "\\'")
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(raw),
                            "-vf", f"subtitles=filename='{esc}'", *base_audio, *enc, str(path_out)],
                           check=True)
        elif mode == "soft":
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(raw), "-i", str(ass),
                            "-map", "0:v", "-map", "0:a", "-map", "1:s", *base_audio, *enc,
                            "-c:s", "mov_text", "-metadata:s:s:0", "language=hin",
                            str(path_out)], check=True)
        else:
            subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(raw), *base_audio, *enc,
                            str(path_out)], check=True)

    mode = "burn" if (args.captions == "burn" and HAVE_SUBTITLE_FILTER) else args.captions
    if args.captions == "burn" and not HAVE_SUBTITLE_FILTER:
        print("    note: this ffmpeg has no libass, so the captions are soft-muxed instead")
        mode = "soft"
    burn(OUTPUT_MP4, mode)

    dur = probe_duration(OUTPUT_MP4)
    info = ["video", "audio"]
    if FFPROBE and Path(FFPROBE).exists():
        try:
            info = subprocess.check_output([FFPROBE, "-v", "error", "-show_entries",
                                            "stream=codec_type,width,height", "-of", "csv=p=0",
                                            str(OUTPUT_MP4)], text=True).split()
        except Exception:
            pass
    print(f"=== Step 4: verification  (captions: {mode}, cues: {len(cues)})")
    print("streams:", info)
    print(f"DONE: {OUTPUT_MP4.resolve()} | {dur/60:.2f} min | {OUTPUT_MP4.stat().st_size/1048576:.1f} MB")
    if not any(s.startswith("audio") for s in info):
        print("WARNING: no audio stream found")


if __name__ == "__main__":
    asyncio.run(main())
