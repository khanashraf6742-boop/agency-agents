#!/usr/bin/env python3
"""
CCS (Pension) Rules 2021 - BATCH 4 - Rules 42 to 52 (Chapters VI-IX)
EXPLAINER MASTERCLASS COMPILER - 43 chapters, screenshot-style slides.

SCREEN LANGUAGE : English (Roman script only; no Devanagari anywhere)
NARRATION       : Hinglish (Roman script only) - teacher + student
VISUALS         : label-and-row cards (the reference layout), data tables,
                  bar charts, comparison splits, flow maps, trap strip.

=====================================================================================
WHAT THIS BUILD IS
=====================================================================================
A single self-contained compiler that renders every slide, synthesises the
narration, burns subtitles and muxes one MP4. No asset files, no network reads
at render time. Three content layers are kept strictly apart on every card:

    Layer 1  the Rule text          (Rules 42-52 of G.S.R. 868(E))
    Layer 2  Gazette amendments     (G.S.R. 770(E), 410(E), 340(E))
    Layer 3  executive O.M.s        (DoPPW / DoPT orders 2022-2026)

=====================================================================================
SOURCES READ FOR THIS BUILD (October 2026)
=====================================================================================
  [S1] Full text of the CCS (Pension) Rules, 2021, Rules 1-70, as reproduced by
       TaxGuru from G.S.R. 868(E) dated 20.12.2021 - rules 42 to 52 read
       clause by clause for this audit (chunks covering rules 40-55).
  [S2] DoPPW O.M. F.No. 38/10(03)/2025-P&PW(A) dated 30.10.2025 on Rule 44(4)
       (compulsory retirement pension / service gratuity).
  [S3] DoPPW O.M. F.No. 1/1(1)/2022-P&PW(E) dated 26.10.2022 on Rule 51
       (missing Government servant / pensioner / family pensioner).
  [S4] DoPPW O.M. dated 01.01.2024 on family pension where a request is pending
       for the spouse to be charged with the murder of the servant.
  [S5] DoPPW O.M. F.No. 28/03/2024-P&PW(B)/Gratuity/9559 dated 30.05.2024 -
       gratuity ceiling raised to Rs 25 lakh w.e.f. 01.01.2024.
  [S6] DoPPW O.M. No. 1/1(90)/2024-P&PW(E)-Part(1)/10344 dated 27.10.2025 -
       enhanced family pension rate.
  [S7] gconnect.in reproduction of Rule 52 and the DR orders, plus the
       DoPPW/e-PP0 DR circular of 22.04.2026 (DR 60% w.e.f. 01.01.2026).
  [S8] The earlier batch-4 source podcast script and the 226-item verification
       ledger that this build inherits its corrections from.

=====================================================================================
WHAT THE AUDIT CHANGED (all of it is now IN the cards)
=====================================================================================
 1. Rule 42(2) reads "may give a notice ... or three months' pay and allowances
    in lieu". The old card said notice is compulsory. Corrected: the sub-rule
    offers a choice of two forms; departmental practice treats one of the two
    as mandatory.
 2. Rule 43(1) first proviso is a CERTIFICATE OF 20 YEARS requested BEFORE the
    notice and issued within 15 days; if not issued, the notice may be given
    without it. Old card implied a "no administrative difficulty" certificate.
 3. Rule 43(1) third proviso (ITEC / foreign posting / foreign contract) needs
    one year of service in India after return. Now on its own card.
 4. Rule 43(2) proviso: silence for the whole notice period = retirement takes
    effect on the expiry date. Now explicit.
 5. Rule 43(3) proviso: if the authority wants to accept the notice despite
    suspension / charge sheet / judicial proceedings, PRESIDENT'S approval is
    needed. Was missing.
 6. Rule 44(6) illustration (born 20.08.1942 and 01.08.1942 both get additional
    pension from 01.08.2022) was missing. Added - it is the exam favourite.
 7. Rule 44(1) illustration of "eligible for grant" vs "sanctioned" kept.
 8. Rule 45(1) first proviso ceiling is Rs 20 lakh in the Rule text; the O.M. of
    30.05.2024 raised it to Rs 25 lakh w.e.f. 01.01.2024. Both now on the card.
 9. Rule 45(6) Explanation (the 11-clause definition of "family" for rules 45 to
    49) was only name-checked. Now a full 11-clause table.
10. Rule 46(4) provisos, 46(5)(b), 46(8), 46(9)(b) proviso and 46(10) were
    flagged "not seen". They are read in [S1] and are now taught.
11. Rule 47(4) to (8) - post-death marriage / age 18, minor through guardian,
    guardianship certificate, the 20% indemnity-bond exception (Format 7) and
    the Form 9 independence rule - were MISSING. Now two chapters.
12. Rule 50(8)(a) to (k) is eleven clauses; the old build had one card. Now a
    clause-by-clause table plus a dedicated multiple-widow chapter.
13. Rule 50(9)(d) to (p) - order of birth, twins, disability for life with the
    seven sub-conditions, the daughter-beyond-25 route, children of more than
    one widow, and the annual certificates - were thin. Now three chapters.
14. Rule 50(14) - the family-pension murder-charge provision, the guardian bar
    and the acquittal date - was COMPLETELY MISSING. Now a chapter.
15. Rule 50(15) Form 4 / Form 5 / Form 10 flow and 50(16) re-employment
    exclusion were missing. Now a chapter.
16. Rule 51(4) to (7) and 51(9) to (11) - gratuity on going missing, claim
    papers, pay determination, arrears and GPF, the fraud exclusion, and the
    bar on paying a non-family member - were MISSING. Now a chapter.
17. Rule 51(1)(b) limb (ii) is "the date up to which pay and allowances have
    been paid", NOT "the day after". Corrected.
18. Rule 51(8)(a) proviso - interest under Rule 65 for delay beyond six months
    FROM THE DATE OF CLAIM - was flagged unverified. It is in [S1] and [S3].
19. Rule 52(2) proviso clause (i) is the Group 'A' post test. Now on the card.
20. Rule 52(3) certificate (three limbs) and the annual November certificate
    practice are now taught.

=====================================================================================
STILL UNVERIFIED - the cards say so out loud
=====================================================================================
  * The Gazette PDF itself was not opened; [S1] is a faithful reproduction of
    G.S.R. 868(E). Wording is quoted as a close restatement, not as certified
    text.
  * Rule 52: the July 2026 DR revision was not announced as of mid-October
    2026; 60% from 01.01.2026 is the last confirmed rate.
  * No notification codifying the 01.01.2024 marital-discord O.M. or the
    Rs 25 lakh ceiling into the Rules was found.
  * The 8th CPC was constituted 03.11.2025; its report (about May 2027) can
    change the floor and ceiling.
  * G.S.R. 775(E) of 2026 was seen only through an earlier batch note.

=====================================================================================
USAGE
=====================================================================================
    python build_pension_b4.py --audit        # coverage + density + readability
    python build_pension_b4.py --preview      # slides only (no ffmpeg needed)
    python build_pension_b4.py --no-tts       # silent timing run (needs ffmpeg)
    python build_pension_b4.py --part 1       # chapters 1..15 only
    python build_pension_b4.py --list         # the chapter map
    python build_pension_b4.py                # full build (edge-tts + ffmpeg)

Needs: Pillow. Optional: edge-tts (pip), ffmpeg + ffprobe with libass.
"""
import argparse
import asyncio
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont


# ============================================================================
# CANVAS / PATHS
# ============================================================================
W, H = 1920, 1080
BUILD_DIR = Path("pension_b4_build")
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
OUT_STEM = "pension_b4_masterclass"
OUTPUT_MP4 = Path(OUT_STEM + ".mp4")

# Density budget (px). The build FAILS if a card must go below these.
BODY_START, BODY_MIN = 34, 25
TITLE_START, TITLE_MIN = 30, 21
ROW_START, ROW_MIN = 33, 23
TABLE_START, TABLE_MIN = 30, 20
LABEL_START, LABEL_MIN = 25, 18

# ============================================================================
# PALETTE - matched to the reference screenshot (deep navy, muted neon edges)
# ============================================================================
BG_TOP = (8, 12, 26)
BG_BOT = (18, 26, 52)
GRID = (26, 36, 66)
GLOW = (58, 40, 110)
CARD_BG = (16, 23, 43)
CARD_BG2 = (21, 29, 52)
TEXT_WHITE = (242, 246, 253)
MUTED = (162, 175, 200)
DIMTXT = (120, 134, 162)
BORDER = (44, 58, 92)

ORANGE = (226, 154, 24)     # amber  - rules / cautions
AMBER = ORANGE
GREEN = (34, 160, 107)      # teal   - money / grants
TEAL = (31, 158, 138)
BLUE = (59, 130, 196)       # blue   - text of the rule
SKY = (96, 176, 232)
RED = (214, 88, 76)         # red    - traps
YELLOW = (240, 205, 60)     # strip
PINK = (198, 120, 176)
PURPLE = (150, 118, 245)    # left labels in the reference layout
VIOLET = (122, 92, 210)
WHITE_T = TEXT_WHITE

# ============================================================================
# VOICES - English-on-screen, Hinglish-in-ear
# ============================================================================
DEFAULT_TEACHER = "en-IN-PrabhatNeural"   # male, Indian English, reads Roman Hindi well
DEFAULT_STUDENT = "en-IN-NeerjaNeural"    # female, Indian English
HI_TEACHER = "hi-IN-MadhurNeural"         # only if you allow Devanagari text
HI_STUDENT = "hi-IN-SwaraNeural"

# Word-level respellings that make an en-IN neural voice speak Roman Hinglish
# naturally. Everything here stays in ROMAN script - no Devanagari is ever used.
_HINGLISH_FIXES = [
    (r"\bnahi\b", "naheen"), (r"\bnahin\b", "naheen"), (r"\bkyunki\b", "kyonki"),
    (r"\bkyonki\b", "kyonki"), (r"\bkarein\b", "karain"), (r"\bkarain\b", "karain"),
    (r"\bchahiye\b", "chaahiye"), (r"\bhoti\b", "hoti"), (r"\bhota\b", "hota"),
    (r"\bmatlab\b", "matlab"), (r"\byaani\b", "yaani"), (r"\bwajah\b", "wajah"),
    (r"\bdekho\b", "dekho"), (r"\bsamjho\b", "samjho"), (r"\btheek\b", "theek"),
    (r"\bdhyaan\b", "dhyaan"), (r"\bzaroori\b", "zaroori"), (r"\bzarurat\b", "zaroorat"),
    (r"\bpehle\b", "pehle"), (r"\bbaad\b", "baad"), (r"\bbad\b", "baad"),
    (r"\bkam\b", "kam"), (r"\bzyada\b", "zyaada"), (r"\bzyaada\b", "zyaada"),
    (r"\blekin\b", "lekin"), (r"\bphir\b", "phir"), (r"\bwahi\b", "wahee"),
    (r"\bkaise\b", "kaise"), (r"\bkya\b", "kya"), (r"\bkaun\b", "kaun"),
    (r"\bjab\b", "jab"), (r"\btab\b", "tab"), (r"\bab\b", "ab"),
    (r"\bhamesha\b", "hamesha"), (r"\bsirf\b", "sirf"), (r"\bkaafi\b", "kaafi"),
    (r"\bhum\b", "hum"), (r"\baap\b", "aap"), (r"\bmujhe\b", "mujhe"),
    (r"\bbatao\b", "batao"), (r"\bbolo\b", "bolo"), (r"\bsuno\b", "suno"),
]

# Acronyms and reference forms, spelled out so the voice says the letters.
_TTS_FIXES = [
    (r"\bUPSC\b", "U.P.S.C."), (r"\bSSC\b", "S.S.C."), (r"\bCVC\b", "C.V.C."), (r"\bCBI\b", "C.B.I."),
    (r"\bDoPT\b", "D.O.P.T."), (r"\bDOPT\b", "D.O.P.T."), (r"\bMHA\b", "M.H.A."),
    (r"\bOMs\b", "O.M.s"), (r"\bOM\b", "O.M."), (r"\bCCS\b", "C.C.S."), (r"\bCCA\b", "C.C.A."),
    (r"\bCAG\b", "C.A.G."), (r"C&AG", "C.A.G."), (r"\bGOI\b", "G.O.I."), (r"\bGPF\b", "G.P.F."),
    (r"\bPSU\b", "P.S.U."), (r"\bITEC\b", "I.T.E.C."), (r"\bDoPPW\b", "D.O.P.P.W."),
    (r"\bRPwD\b", "R.P.w.D."), (r"\bCPC\b", "C.P.C."), (r"\bNPS\b", "N.P.S."),
    (r"\bRTI\b", "R.T.I."), (r"\bFR\b", "F.R."), (r"\bG\.S\.R\.", "G.S.R."),
    (r"\bw\.e\.f\.", "with effect from"), (r"\bW\.E\.F\.", "with effect from"),
    (r"\bRs\b\.?", "Rupees"),
    # rule references - deepest nesting first
    (r"Rule\s+(\d+)\((\d+)\)\(([a-z])\)\(([ivx]+)\)", r"Rule \1, sub rule \2, clause \3, sub clause \4"),
    (r"Rule\s+(\d+)\((\d+)\)\(([a-z])\)", r"Rule \1, sub rule \2, clause \3"),
    (r"Rule\s+(\d+)\(([a-z])\)\(([ivx]+)\)", r"Rule \1, clause \2, sub clause \3"),
    (r"Rule\s+(\d+)\((\d+)\)", r"Rule \1, sub rule \2"),
    (r"Rule\s+(\d+)\(([a-z])\)", r"Rule \1, clause \2"),
    (r"\bsub-rules\b", "sub rules"), (r"\bsub-rule\b", "sub rule"),
    (r"[\u2014\u2013]", ","),
]

DEVANAGARI = re.compile(r"[\u0900-\u097F]")
LATIN_WORD = re.compile(r"[A-Za-z']+")


def normalize_for_tts(text: str, hinglish: bool = True) -> str:
    """Roman in, Roman out. Never introduces a Devanagari character."""
    if DEVANAGARI.search(text):
        raise ValueError(f"Devanagari found in narration: {text[:60]!r}")
    for pat, rep in _TTS_FIXES:
        text = re.sub(pat, rep, text)
    if hinglish:
        for pat, rep in _HINGLISH_FIXES:
            text = re.sub(pat, rep, text)
    return re.sub(r"[ \t]+", " ", text).strip()


# ============================================================================
# INLINE MARKUP  (used on screen; never spoken)
# ============================================================================
#   **bold white**      ==yellow bold==      [[teal]]
#   {{purple}}          <<red>>              //blue//
#   ~~amber~~           __green__            plain = body white
_RICH_TOKENS = [
    ("**", TEXT_WHITE, True), ("==", YELLOW, True), ("[[", TEAL, True),
    ("{{", PURPLE, True), ("<<", RED, True), ("//", BLUE, True),
    ("~~", ORANGE, True), ("__", GREEN, True), ("@@", MUTED, False),
]
_RICH_RE = re.compile(r"(\*\*|==|\[\[|\]\]|\{\{|\}\}|<<|>>|//|~~|__|@@)")
_RICH_CLOSE = {"**": "**", "==": "==", "[[": "]]", "{{": "}}", "<<": ">>",
               "//": "//", "~~": "~~", "__": "__", "@@": "@@"}
_CLOSERS = {"]]", "}}", ">>"}


def parse_rich(raw: str):
    """'Rule 44 and ==Nair== with [[teal]]' -> [(text, colour, bold), ...]."""
    runs, buf, mode = [], "", None

    def flush(colour, bold):
        nonlocal buf
        if buf:
            runs.append((buf, colour, bold))
            buf = ""

    for tok in _RICH_RE.split(raw):
        if mode is None and tok in _RICH_CLOSE:
            flush(TEXT_WHITE, False)
            mode = tok
        elif mode is not None and (tok == _RICH_CLOSE[mode] or tok in _CLOSERS):
            col, bold = next((c, b) for m, c, b in _RICH_TOKENS if m == mode)
            flush(col, bold)
            mode = None
        elif mode is not None:
            buf += tok
        else:
            buf += tok
    flush(TEXT_WHITE, False)
    return [r for r in runs if r[0]]


def strip_rich(raw: str) -> str:
    return "".join(t for t, _c, _b in parse_rich(raw))


# ============================================================================
# FONTS AND LOW-LEVEL TEXT
# ============================================================================
_FONT_CACHE = {}
_FONT_NAMES = {
    False: ["DejaVuSans.ttf", "LiberationSans-Regular.ttf", "NotoSans-Regular.ttf",
            "arial.ttf", "segoeui.ttf"],
    True: ["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "NotoSans-Bold.ttf",
           "arialbd.ttf", "segoeuib.ttf"],
}


def font(size: int, bold: bool = False):
    key = (size, bold)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    f = None
    for name in _FONT_NAMES[bold]:
        try:
            f = ImageFont.truetype(name, size)
            break
        except Exception:
            continue
    if f is None:
        try:
            f = ImageFont.load_default(size)
        except TypeError:
            f = ImageFont.load_default()
    _FONT_CACHE[key] = f
    return f


def text_w(d, s, f):
    b = d.textbbox((0, 0), s, font=f)
    return b[2] - b[0]


def wrap_plain(d, text, f, max_w):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split(" "):
            t = f"{cur} {word}".strip()
            if text_w(d, t, f) <= max_w:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def fit_plain(d, text, bold, max_w, max_h, start, min_size, spacing=1.28):
    for size in range(start, min_size - 1, -1):
        f = font(size, bold)
        lines = wrap_plain(d, text, f, max_w)
        lh = int(size * spacing)
        if len(lines) * lh <= max_h:
            return f, lines, lh, size
    raise ValueError(f"TEXT TOO DENSE (needs < {min_size}px): {text[:70]!r}")


def draw_plain(d, x, y, lines, f, lh, colour):
    for i, ln in enumerate(lines):
        d.text((x, y + i * lh), ln, font=f, fill=colour)


class Rich:
    """Wrapped, multi-colour text block with its own measurement."""

    def __init__(self, raw, base=TEXT_WHITE):
        self.runs = parse_rich(raw) if base is TEXT_WHITE else [
            (t, c if c != TEXT_WHITE else base, b) for t, c, b in parse_rich(raw)]
        self.raw = raw
        self.lines = []
        self.size = 0
        self.lh = 0

    def layout(self, d, max_w, size, spacing=1.30):
        self.size, self.lh = size, int(size * spacing)
        # token stream: (word, colour, bold, trailing_space)
        toks = []
        for text, colour, bold in self.runs:
            parts = re.split(r"(\s+)", text)
            for part in parts:
                if not part:
                    continue
                if part.isspace():
                    if toks:
                        w, c, b, _sp = toks[-1]
                        toks[-1] = (w, c, b, True)
                else:
                    toks.append((part, colour, bold, False))
        lines, cur, cur_w = [], [], 0
        space_w = text_w(d, " ", font(size, False))
        prev_tail = False
        for word, colour, bold, tail in toks:
            f = font(size, bold)
            ww = text_w(d, word, f)
            sp_before = prev_tail and bool(cur)
            prev_tail = tail
            add = ww + (space_w if (sp_before or (cur and not sp_before and False)) else 0)
            if cur and cur_w + add > max_w:
                lines.append(cur)
                cur, cur_w = [(word, colour, bold, False)], ww
            else:
                cur.append((word, colour, bold, sp_before))
                cur_w += add
        if cur:
            lines.append(cur)
        self.lines = lines
        return self

    def height(self):
        return len(self.lines) * self.lh

    def draw(self, d, x, y, spacing_px=None, ink=None):
        sp = spacing_px if spacing_px is not None else text_w(d, " ", font(self.size, False))
        for i, line in enumerate(self.lines):
            cx = x
            for j, (word, colour, bold, sp_before) in enumerate(line):
                if sp_before:
                    cx += sp
                col = ink(colour, bold) if ink else colour
                d.text((cx, y + i * self.lh), word, font=font(self.size, bold), fill=col)
                cx += text_w(d, word, font(self.size, bold))
        return y + self.height()

    def fit(self, d, max_w, max_h, start, min_size, spacing=1.30):
        for size in range(start, min_size - 1, -1):
            self.layout(d, max_w, size, spacing)
            if self.height() <= max_h:
                return self
        raise ValueError(f"TEXT TOO DENSE (needs < {min_size}px): {self.raw[:70]!r}")


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def dim(c, t=0.30):
    return lerp(CARD_BG, c, t)


def readable_on(colour):
    """Dark text on bright fills, white on dark fills."""
    r, g, b = colour
    return (10, 14, 26) if (0.299 * r + 0.587 * g + 0.114 * b) > 132 else TEXT_WHITE


# ============================================================================
# CANVAS
# ============================================================================
def background():
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(H):
        d.line([(0, y), (W, y)], fill=lerp(BG_TOP, BG_BOT, y / H))
    # faint violet glow across the top, like the reference frame
    for i in range(90):
        t = i / 90
        d.line([(0, i * 2), (W, i * 2)], fill=lerp(BG_TOP, GLOW, 0.16 * (1 - t)))
    # 60px grid
    for x in range(60, W, 60):
        d.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(120, H, 60):
        d.line([(0, y), (W, y)], fill=GRID, width=1)
    return img, d


def pill(d, x, y, text, fg, bg, pad_x=18, pad_y=8, radius=None):
    f = font(19, True)
    tw = text_w(d, text, f)
    w = tw + pad_x * 2
    h = 19 + pad_y * 2
    r = radius if radius is not None else h // 2
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=bg, outline=fg, width=2)
    d.text((x + pad_x, y + pad_y - 1), text, font=f, fill=fg)
    return w, h


def header(d, scene, idx, total):
    """Breadcrumb pill + title + badge, as in the reference frame."""
    acc = scene["accent"]
    crumb = scene["crumb"]
    f = font(19, True)
    tw = text_w(d, crumb, f)
    d.rounded_rectangle([70, 28, 70 + tw + 40, 68], radius=20,
                        fill=lerp(CARD_BG, VIOLET, 0.30), outline=lerp(VIOLET, BG_TOP, 0.15), width=2)
    d.text((90, 38), crumb, font=f, fill=(206, 196, 255))

    title = scene["title"]
    ft, lt, lht, _ = fit_plain(d, title, True, W - 520, 104, 46, 30, 1.10)
    for i, ln in enumerate(lt):
        d.text((70, 86 + i * lht), ln, font=ft, fill=TEXT_WHITE)

    badge = scene["badge"]
    fb = font(20, True)
    bw = text_w(d, badge, fb) + 44
    d.rounded_rectangle([W - 70 - bw, 96, W - 70, 142], radius=10, fill=dim(acc, 0.55),
                        outline=acc, width=2)
    d.text((W - 70 - bw + 22, 108), badge, font=fb, fill=acc)
    return 86 + len(lt) * lht + 16


def question_line(d, scene, y):
    q = scene["q"]
    r = Rich(q)
    f_q = None
    for size in (30, 28, 26, 24):
        r.layout(d, W - 300, size, 1.20)
        if r.height() <= 46:
            f_q = size
            break
    if f_q is None:
        r.layout(d, W - 300, 22, 1.15)
    d.rounded_rectangle([70, y, 70 + 44, y + 44], radius=12, fill=lerp(CARD_BG, YELLOW, 0.22))
    d.text((80, y + 8), "Q", font=font(24, True), fill=YELLOW)
    r.draw(d, 132, y + 2)
    return y + max(48, r.height() + 10)


# ============================================================================
# BLOCK DRAWING
# ============================================================================
def draw_heads(d, heads, x0, y0, width, acc, reveal):
    """Row of 2-4 concept tiles (the four coloured boxes in the reference)."""
    n = len(heads)
    if not n or reveal < 1:
        return y0
    gap = 16
    tw = (width - gap * (n - 1)) // n
    th = 96
    for i, (title, sub, colour) in enumerate(heads[:n]):
        x = x0 + i * (tw + gap)
        live = False
        d.rounded_rectangle([x, y0, x + tw, y0 + th], radius=12,
                            fill=lerp(CARD_BG, colour, 0.10 if not live else 0.16),
                            outline=colour if live else dim(colour, 0.75), width=3 if live else 2)
        f1, l1, lh1, _ = fit_plain(d, title, True, tw - 30, 34, 27, 19, 1.12)
        for k, ln in enumerate(l1[:2]):
            d.text((x + 15, y0 + 14 + k * lh1), ln, font=f1, fill=colour)
        fs = font(15, True)
        subs = wrap_plain(d, sub.upper(), fs, tw - 30)
        for k, ln in enumerate(subs[:2]):
            d.text((x + 15, y0 + 58 + k * 19), ln, font=fs, fill=(150, 140, 210))
    return y0 + th + gap


def draw_rows(d, rows, x0, y0, width, height, reveal, acc, label_w):
    """The reference layout: purple label card + wide rich-text card per row."""
    n = len(rows)
    if not n:
        return y0
    gap = 12
    avail = height - gap * (n - 1)
    per = avail / n
    y = y0
    for i, (label, colour, rich_raw) in enumerate(rows):
        if i + 1 > reveal:
            y += per + gap
            continue
        live = (i + 1) == reveal
        hh = per
        # label card
        lab_col = PURPLE if colour in (PURPLE, VIOLET) else colour
        d.rounded_rectangle([x0, y, x0 + label_w, y + hh], radius=12,
                            fill=lerp(CARD_BG, lab_col, 0.13),
                            outline=lab_col if live else dim(lab_col, 0.7), width=2)
        f_l, l_l, lh_l, _ = fit_plain(d, label, True, label_w - 30, hh - 24,
                                      LABEL_START, LABEL_MIN, 1.18)
        ty = y + (hh - len(l_l) * lh_l) // 2
        for k, ln in enumerate(l_l):
            d.text((x0 + 15, ty + k * lh_l), ln, font=f_l, fill=lab_col)
        # content card
        cx = x0 + label_w + 12
        cw = width - label_w - 12
        d.rounded_rectangle([cx, y, cx + cw, y + hh], radius=12,
                            fill=CARD_BG if not live else lerp(CARD_BG, acc, 0.10),
                            outline=acc if live else BORDER, width=3 if live else 2)
        d.rectangle([cx, y + 8, cx + 6, y + hh - 8],
                    fill=acc if live else dim(acc, 0.5))
        r = Rich(rich_raw)
        r.fit(d, cw - 46, hh - 22, ROW_START, ROW_MIN, 1.30)
        r.draw(d, cx + 22, y + (hh - r.height()) // 2)
        y += hh + gap
    return y0 + height


def draw_table(d, spec, x0, y0, width, height, reveal, acc):
    """Auto-fitting table. Tries progressively tighter type; raises if it cannot fit."""
    head = spec["head"]
    rows = spec["rows"]
    widths = spec.get("w") or [1] * len(head)
    total_w = sum(widths)
    cols = [int(width * w / total_w) for w in widths]
    cols[-1] = width - sum(cols[:-1])
    title = spec.get("title")
    head_h_extra = 34 if title else 0

    layout = None
    for size, pad, hs in ((24, 12, 22), (22, 11, 21), (21, 10, 20), (20, 9, 19),
                          (19, 8, 18), (18, 7, 17), (17, 6, 16)):
        fh = font(hs, True)
        fb = font(size, False)
        head_lines = [wrap_plain(d, h, fh, cols[i] - pad * 2) for i, h in enumerate(head)]
        head_h = max(len(l) for l in head_lines) * int(hs * 1.18) + pad * 2
        cell_lines, row_hs, need = [], [], 0
        for row in rows:
            ls = [wrap_plain(d, str(c), fb, cols[i] - pad * 2) for i, c in enumerate(row)]
            cell_lines.append(ls)
            rh = max(len(l) for l in ls) * int(size * 1.30) + pad * 2
            row_hs.append(rh)
            need += rh
        if head_h + need + head_h_extra <= height:
            layout = (size, pad, hs, fh, fb, head_lines, head_h, cell_lines, row_hs)
            break
    if layout is None:
        raise ValueError(f"TABLE TOO DENSE: {len(rows)} rows do not fit in {height}px "
                         f"(shorten the cells or split the chapter)")
    size, pad, hs, fh, fb, head_lines, head_h, cell_lines, row_hs = layout

    ty = y0
    if title:
        d.text((x0, ty), title.upper(), font=font(20, True), fill=acc)
        ty += head_h_extra
    d.rounded_rectangle([x0, ty, x0 + width, ty + head_h], radius=8, fill=lerp(CARD_BG, acc, 0.30))
    cx = x0
    for i, lines in enumerate(head_lines):
        for k, ln in enumerate(lines):
            d.text((cx + pad, ty + pad + k * int(hs * 1.18)), ln, font=fh, fill=(12, 16, 30))
        cx += cols[i]
    ty += head_h
    for ri, row in enumerate(rows):
        if ri + 1 > reveal:
            break
        rh = row_hs[ri]
        z = lerp(CARD_BG, CARD_BG2, 0.9) if ri % 2 == 0 else CARD_BG
        d.rectangle([x0, ty, x0 + width, ty + rh], fill=z)
        if ri + 1 == reveal:
            d.rectangle([x0, ty, x0 + width, ty + rh], outline=acc, width=2)
        cx = x0
        for ci, cell in enumerate(row):
            lines = cell_lines[ri][ci]
            bold = (ci == 0)
            col = TEXT_WHITE if ci else lerp(acc, TEXT_WHITE, 0.45)
            for k, ln in enumerate(lines):
                d.text((cx + pad, ty + pad + k * int(size * 1.30)), ln,
                       font=font(size, bold), fill=col)
            cx += cols[ci]
        ty += rh
        d.line([(x0, ty), (x0 + width, ty)], fill=BORDER, width=1)
    return ty


def draw_chart(d, spec, x0, y0, width, height, reveal, acc):
    bars = spec["bars"]
    unit = spec.get("unit", "%")
    vmax = spec.get("max") or max(b[1] for b in bars)
    label_w = spec.get("label_w", 360)
    title = spec.get("title")
    ty = y0
    if title:
        d.text((x0, ty), title.upper(), font=font(21, True), fill=acc)
        ty += 34
    n = len(bars)
    gap = 14
    bh = min(86, (height - (n - 1) * gap) // max(n, 1))
    ty += max(0, (height - (n * bh + (n - 1) * gap)) // 2)
    bw_max = width - label_w - 210
    for i, bar in enumerate(bars):
        if i + 1 > reveal:
            continue
        label, value, colour = bar[0], bar[1], bar[2]
        note = bar[3] if len(bar) > 3 else ""
        y = ty + i * (bh + gap)
        live = (i + 1) == reveal
        d.rounded_rectangle([x0, y, x0 + label_w - 16, y + bh], radius=8,
                            fill=CARD_BG, outline=dim(colour, 0.7) if not live else colour,
                            width=2)
        f_l, l_l, lh_l, _ = fit_plain(d, label, True, label_w - 44, bh - 16, 23, 17, 1.15)
        for k, ln in enumerate(l_l):
            d.text((x0 + 12, y + (bh - len(l_l) * lh_l) // 2 + k * lh_l), ln,
                   font=f_l, fill=TEXT_WHITE)
        track_x = x0 + label_w
        track_w = bw_max
        d.rounded_rectangle([track_x, y + bh // 2 - 11, track_x + track_w, y + bh // 2 + 11],
                            radius=11, fill=(24, 33, 58))
        frac = max(0.02, min(1.0, value / vmax))
        d.rounded_rectangle([track_x, y + bh // 2 - 11, track_x + int(track_w * frac), y + bh // 2 + 11],
                            radius=11, fill=colour if live else dim(colour, 0.8))
        val_txt = f"{value:g}{unit}" if isinstance(value, (int, float)) else str(value)
        vt_x = min(track_x + int(track_w * frac) + 14, track_x + track_w - 70)
        d.text((vt_x, y + bh // 2 - 15), val_txt, font=font(24, True), fill=colour)
    return ty + n * (bh + gap)


def draw_compare(d, spec, x0, y0, width, height, reveal, acc):
    """Side-by-side split. The cards take only the height the text needs, centred."""
    cols = spec["cols"]
    n = len(cols)
    gap = 18
    cw = (width - gap * (n - 1)) // n
    body = [Rich(raw) for _t, raw, _c in cols]
    size = None
    for cand in range(32, 17, -1):
        hs = [r.layout(d, cw - 40, cand, 1.34).height() for r in body]
        if max(hs) <= height - 74:
            size = cand
            break
    if size is None:
        raise ValueError(f"COMPARE TOO DENSE: {strip_rich(cols[0][1])[:50]!r}")
    ch = height
    top = y0
    for i, (title, _raw, colour) in enumerate(cols):
        if i + 1 > reveal:
            continue
        x = x0 + i * (cw + gap)
        live = (i + 1) == reveal
        d.rounded_rectangle([x, top, x + cw, top + ch], radius=12,
                            fill=lerp(CARD_BG, colour, 0.10),
                            outline=colour if live else dim(colour, 0.7), width=3 if live else 2)
        d.text((x + 22, top + 18), title.upper(), font=font(22, True), fill=colour)
        d.line([(x + 22, top + 54), (x + cw - 22, top + 54)], fill=BORDER, width=2)
        ty = top + 54 + max(12, (ch - 74 - body[i].height()) // 2)
        body[i].draw(d, x + 22, ty)
    return top + ch


def draw_banner(d, raw, x0, y0, width, colour, reveal):
    h = 92
    d.rounded_rectangle([x0, y0, x0 + width, y0 + h], radius=12,
                        fill=lerp(CARD_BG, colour, 0.13), outline=colour, width=2)
    r = Rich(raw)
    r.fit(d, width - 44, h - 22, 28, 20, 1.25)
    r.draw(d, x0 + 22, y0 + (h - r.height()) // 2)
    return y0 + h


def ink_on_yellow(colour, bold):
    """On the yellow strip every run becomes dark ink; weight carries the emphasis."""
    if not bold:
        return (52, 44, 16)
    if colour in (RED, ORANGE):
        return (124, 22, 12)
    return (22, 18, 4)


def draw_trap(d, raw):
    """The yellow bottom strip of the reference frame."""
    y0, h = H - 96, 56
    d.rounded_rectangle([70, y0, W - 70, y0 + h], radius=10, fill=YELLOW)
    r = Rich(raw)
    for size in range(27, 17, -1):
        r.layout(d, W - 210, size, 1.12)
        if len(r.lines) == 1:
            r.draw(d, 92, y0 + (h - r.height()) // 2, ink=ink_on_yellow)
            return
    raise ValueError(f"TRAP strip wraps even at 18px: {strip_rich(raw)!r}")


def footer(d, idx, total, reveal, nblocks, scene):
    # segmented progress bar, one segment per chapter, above the footer strip
    seg = W / max(total, 1)
    base = seg * (idx - 1)
    frac = min(1.0, reveal / max(nblocks, 1))
    d.rectangle([0, H - 42, W, H - 26], fill=(22, 30, 52))
    d.rectangle([int(base), H - 42, int(base + seg * frac), H - 26], fill=scene["accent"])
    for k in range(1, total):
        d.line([(int(seg * k), H - 42), (int(seg * k), H - 26)], fill=(8, 12, 24), width=1)
    d.rectangle([0, H - 24, W, H], fill=(6, 9, 20))
    d.text((70, H - 21), f"{idx:02d} / {total:02d}", font=font(15, True), fill=(150, 165, 195))
    d.text((W - 470, H - 21), "STUDIO VOGEL-90  •  CITY HINGLISH",
           font=font(15, True), fill=(150, 165, 195))


# ============================================================================
# CONTENT
# ----------------------------------------------------------------------------
# box tuple = (label, on-screen rich text, full examinable text, colour, Hinglish narration)
#   label            - the left-hand pill (short; 1-3 words)
#   on-screen text   - English, supports inline markup, ONE to three lines
#   full text        - English, the reference-sheet / audit layer
#   colour           - accent used for the row
#   narration        - HINGLISH in Roman script ONLY (never Devanagari)
# ============================================================================
SCENES = [
    {
        "id": "b4_01_map",
        "part": "BATCH 4 MAP • RULES 42 TO 52",
        "title": "RULES 42 TO 52 — THE WHOLE BATCH ON ONE SCREEN",
        "accent": RED, "badge": "RULES 42 • 52",
        "crumb": "CCS (PENSION) RULES 2021  •  BATCH 4  •  CHAPTERS VI-IX",
        "q": "What does this batch cover, and how do the four chapters fit together?",
        "q_say": "Sir, is batch mein kya kya aata hai, aur ye chaar chapters aapas mein kaise jude hain?",
        "intro": ("Namaste aur swagat hai Batch 4 mein. CCS Pension Rules, 2021 ke Rules forty-two se fifty-two, "
                  "yaani sabse bada batch. Yahan hum teen layers alag rakhenge: pehle Rule ka text, phir Gazette amendment, "
                  "aur phir O.M. yaani office memorandum. Jahan official source se confirm nahi hua, card par flag lagega."),
        "heads": [("CHAPTER VI", "Rules 42-43 • leave early", BLUE),
                  ("CHAPTER VII", "Rules 44-49 • the money", ORANGE),
                  ("CHAPTER VIII", "Rules 50-51 • family", GREEN),
                  ("CHAPTER IX", "Rule 52 • dearness relief", PURPLE)],
        "boxes": [
            ("RETIRE EARLY",
             "Rule 42: Government retires you after ==30 years==. Rule 43: you retire yourself after ==20 years==.",
             "Chapter VI, Rules 42-43: premature retirement in the public interest after thirty years qualifying service (Rule 42) and voluntary retirement after twenty years (Rule 43). Both give a retiring pension calculated under Rule 44. Layer 1 (Rule text), read in S1.",
             BLUE,
             "Chapter six mein jaldi service chhodne ke rules hain. Rule forty-two mein Government public interest mein thirty years ke baad retire kar sakti hai. Rule forty-three mein aap khud twenty years ke baad retire ho sakte hain."),
            ("THE MONEY",
             "Rules 44-49: pension, the three gratuities, nomination, who receives, murder charge, lapse.",
             "Chapter VII, Rules 44-49: Rule 44 pension and service gratuity; Rule 45 retirement, death and residuary gratuity; Rule 46 nomination; Rule 47 persons to whom gratuity is payable; Rule 48 debarring on a murder charge; Rule 49 lapse. Layer 1 (Rule text), read in S1.",
             ORANGE,
             "Chapter seven paisa ka chapter hai. Rule forty-four pension ka amount, Rule forty-five teen gratuities, Rule forty-six nomination, Rule forty-seven kis ko milega, Rule forty-eight murder charge, aur Rule forty-nine lapse."),
            ("FAMILY & MISSING",
             "Rule 50 family pension. Rule 51 a missing servant, pensioner or family pensioner.",
             "Chapter VIII: Rule 50 family pension - gateways, rates, additional family pension, order of precedence, widows, children, parents, siblings, caps, forms; Rule 51 missing Government servant, pensioner or family pensioner. Amended by G.S.R. 770(E) (Rule 50(9)(h)(iii)) and G.S.R. 410(E) (Rule 50(15)(e)).",
             GREEN,
             "Chapter eight parivaar ka hai. Rule fifty family pension deta hai, yaani servant ya pensioner ke baad parivaar ko pension. Rule fifty-one missing person ka case hai."),
            ("DEARNESS RELIEF",
             "Rule 52: DR is an add-on, at rates the Central Government fixes. ==60% from 1 Jan 2026==.",
             "Chapter IX, Rule 52: dearness relief on pension and family pension, at such rates and conditions as the Central Government specifies. DR is a dynamic figure: 60 percent w.e.f. 01.01.2026 is the last confirmed rate; the July 2026 revision was not announced as of mid-October 2026 (S7).",
             PURPLE,
             "Chapter nine Rule fifty-two hai, dearness relief. Ye pension ke upar ek add-on hai jo mehngai se bachata hai. Rate Rule mein nahi likha, isliye hamesha latest O.M. dekho."),
        ],
        "trap": "<<REMEMBER:>> 42-43 early exit  •  44-49 money  •  50-51 family  •  52 dearness relief",
        "trap_say": ("Yaad rakho: Rules forty-two aur forty-three jaldi retirement, forty-four se forty-nine paisa, "
                     "fifty aur fifty-one parivaar, aur fifty-two dearness relief."),
        "covers": ["MAP4", "GSR-868E-2021", "GSR-770E-2022", "GSR-410E-2024"],
    },
    {
        "id": "b4_02_rule42",
        "part": "RULE 42 • RETIREMENT IN THE PUBLIC INTEREST",
        "title": "RULE 42 — GOVERNMENT CAN RETIRE YOU AFTER THIRTY YEARS",
        "accent": ORANGE, "badge": "RULE 42",
        "crumb": "CHAPTER VI  •  PREMATURE RETIREMENT",
        "q": "Who can retire a servant in the public interest, and what notice must be given?",
        "q_say": "Sir, Rule forty-two mein public interest retirement kaun kar sakta hai, aur notice ka kya rule hai?",
        "heads": [("30 YEARS", "Qualifying service", BLUE),
                  ("APPOINTING AUTHORITY", "Passes the order", ORANGE),
                  ("3 MONTHS", "Notice, or pay in lieu", GREEN),
                  ("FR 56", "Procedure to follow", PURPLE)],
        "boxes": [
            ("42(1): 30 YEARS",
             "After ==thirty years== of qualifying service the appointing authority may retire him in the public interest. He then gets a ==retiring pension== under Rule 44.",
             "Rule 42(1): at any time after a Government servant has completed thirty years qualifying service, he may be required by the appointing authority to retire in the public interest, and shall be entitled to a retiring pension calculated in accordance with Rule 44. Qualifying service means service that counts for pension (Rule 3(1)(w)); the initiative is the Government's, not the servant's.",
             BLUE,
             "Pehle rule ka text. Thirty years qualifying service ke baad appointing authority public interest mein retire kar sakti hai. Us case mein retiring pension Rule forty-four se banti hai. Note karo, order Government ki taraf se hota hai, servant ki request nahi."),
            ("42(2): NOTICE",
             "Written notice of ==at least 3 months== before the date of retirement, or ==3 months' pay and allowances== in lieu.",
             "Rule 42(2): the appointing authority may give a notice in writing at least three months before the date on which he is required to retire, or three months pay and allowances in lieu of such notice. The sub-rule offers a CHOICE of two forms - notice or pay in lieu. It is written as may, but departmental practice treats one of the two as compulsory; the power to dispense with both is not in the text.",
             GREEN,
             "Ab notice. Teen mahine ka written notice, ya teen mahine ka pay and allowances in lieu. Rule ke words may hain, lekin in dono mein se ek dena padta hai. Podcast ne kaha tha notice optional hai, wo galat tha."),
            ("42(3): PROCEDURE",
             "The procedure is the one ==DoPT== lays down for retirement under ==Fundamental Rule 56==. Nothing new is invented here.",
             "Rule 42(3): for retirement under this rule the same procedure as laid down by the Department of Personnel and Training for retirement under rule 56 of the Fundamental Rules, 1922 shall apply. So the FR 56 review machinery, the notice and the review committee practice travel into Rule 42.",
             PURPLE,
             "Sub-rule three kehta hai procedure apna naya nahi hai. DoPT ne Fundamental Rule fifty-six ke liye jo procedure banaya hai, wahi yahan chalega."),
            ("EXPLANATION",
             "Appointing authority = the authority ==competent to appoint== to the service or post from which he retires.",
             "Explanation to Rule 42: appointing authority means the authority competent to make appointments to the service or post from which the Government servant retires. Do not confuse it with the authority that sanctions pension, or the Head of Office who processes the papers.",
             RED,
             "Explanation appointing authority define karti hai. Matlab wo authority jo us service ya post par appointment kar sakti hai, jisse retirement ho rahi hai. Pension sanction karne wali authority alag hoti hai."),
        ],
        "trap": "<<TRAP:>> Thirty years is ==qualifying service==, not total service — and the pension is a retiring pension under ==Rule 44==.",
        "trap_say": ("Trap ye hai: thirty years qualifying service hai, total service nahi. Aur pension retiring pension hai, "
                     "jo Rule forty-four se calculate hoti hai."),
        "covers": ["R42-1", "R42-2", "R42-3", "R42-EXPL", "LIMIT-R42-30Y", "TL-R42-NOTICE-3M"],
    },
    {
        "id": "b4_03_rule43_certificate",
        "part": "RULE 43(1) • VOLUNTARY RETIREMENT AFTER TWENTY YEARS",
        "title": "RULE 43(1) — YOU MAY RETIRE AFTER TWENTY YEARS, BUT PROVE IT FIRST",
        "accent": GREEN, "badge": "RULE 43(1)",
        "crumb": "CHAPTER VI  •  VOLUNTARY RETIREMENT",
        "q": "How does a servant apply for voluntary retirement, and what must the office do first?",
        "q_say": "Sir, voluntary retirement ke liye apply kaise karte hain, aur office ko pehle kya karna hota hai?",
        "heads": [("20 YEARS", "Qualifying service", BLUE),
                  ("3 MONTHS", "Written notice", ORANGE),
                  ("15 DAYS", "Service certificate", GREEN),
                  ("SILENCE", "Deemed acceptance", PURPLE)],
        "boxes": [
            ("43(1): THE RIGHT",
             "After ==twenty years== he may retire by giving ==three months' notice in writing== to the appointing authority; pension under Rule 44.",
             "Rule 43(1): at any time after a Government servant has completed twenty years qualifying service, he may, by giving notice of not less than three months in writing to the appointing authority, retire from service, and shall be entitled to a retiring pension calculated in accordance with Rule 44. Here the initiative is the servant's, unlike Rule 42.",
             BLUE,
             "Rule forty-three mein initiative aapki hai. Twenty years qualifying service ke baad, appointing authority ko teen mahine ka written notice dekar retire ho sakte hain. Pension phir bhi Rule forty-four se hi banegi."),
            ("PROVISO 1: CERTIFICATE",
             "Before the notice, ask for a ==certificate of 20 years==. The office must issue it in ==15 days==; if it does not, give the notice without it.",
             "First proviso to Rule 43(1): before giving notice of voluntary retirement the servant shall request the appropriate administrative authority for a certificate regarding completion of twenty years qualifying service on the intended date of retirement; the authority shall issue it within fifteen days; if no certificate is issued within fifteen days, the servant may give the notice without such certificate (TL-R43-CERT-15D).",
             GREEN,
             "Pehla proviso: notice dene se pehle twenty years ka certificate maango. Office ko pandrah din mein dena hota hai. Agar na de, aap bina certificate ke notice de sakte ho. Yaad rakho, pandrah din ka clock request se chalta hai."),
            ("PROVISO 2: CHECK",
             "Before accepting the notice, the authority must ==check for itself== that twenty years are complete.",
             "Second proviso to Rule 43(1): before accepting the notice and passing orders, the appointing authority shall satisfy itself that the Government servant has completed the qualifying service of twenty years. So the certificate helps the servant, but the statutory duty to verify sits on the authority.",
             ORANGE,
             "Doosra proviso: notice accept karne se pehle appointing authority ko khud satisfy hona padega ki twenty years pure hue hain. Certificate servant ki help ke liye hai, lekin check karna authority ka duty hai."),
            ("43(2): ACCEPTANCE",
             "The notice needs ==acceptance==. If the authority does not refuse before the notice expires, retirement takes effect ==on the expiry date==.",
             "Rule 43(2): the notice of voluntary retirement shall require acceptance by the appointing authority. Proviso: where the appointing authority does not refuse permission before the expiry of the period specified in the notice, the retirement becomes effective from the date of expiry of that period. Silence is therefore acceptance, not rejection.",
             PURPLE,
             "Sub-rule two: notice ko acceptance chahiye. Proviso kehta hai agar authority notice ki period khatam hone se pehle refuse nahi karti, to retirement expiry date se effective ho jaati hai. Yaani silence matlab acceptance."),
        ],
        "trap": "<<TRAP:>> The 15-day certificate is ==proviso one==; the authority's own verification duty is ==proviso two==. Never merge them.",
        "trap_say": ("Trap ye hai: pandrah din ka certificate pehla proviso hai, aur authority ka apna verification duty doosra proviso. "
                     "Dono ko mix mat karo."),
        "covers": ["R43-1", "R43-1-P1", "TL-R43-CERT-15D", "R43-1-P2", "R43-2", "R43-2-P1", "LIMIT-R43-20Y"],
    },
    {
        "id": "b4_04_rule43_provisos",
        "part": "RULE 43(1) • PROVISOS THREE AND FOUR",
        "title": "THE FOREIGN POSTING BAR AND THE NO-ROUNDING RULE",
        "accent": ORANGE, "badge": "RULE 43(1) P3-P4",
        "crumb": "CHAPTER VI  •  TWO PROVISOS THE PODCAST MISSED",
        "q": "Who is kept out of the twenty-year route, and how is the twenty years counted?",
        "q_say": "Sir, kis ko twenty-year route se bahar rakha gaya hai, aur twenty years ka count kaise hota hai?",
        "heads": [("ITEC / ABROAD", "Three foreign situations", BLUE),
                  ("ONE YEAR", "Service in India after return", ORANGE),
                  ("NO ROUNDING", "Rule 44(7) is switched off", GREEN),
                  ("INTENDED DATE", "Twenty years on that day", PURPLE)],
        "boxes": [
            ("PROVISO 3: WHO",
             "Not for a servant on ==ITEC== assignment, posted abroad in a foreign-based office, or on a contract with a foreign Government.",
             "Third proviso to Rule 43(1): the sub-rule shall not apply to a Government servant, including a scientist or technical expert, who is (i) on an assignment under the Indian Technical and Economic Cooperation Programme of the Ministry of External Affairs or other aid programmes, or (ii) posted abroad in foreign-based offices of Ministries or Departments, or (iii) on a specific contract assignment to a foreign Government.",
             BLUE,
             "Teesra proviso ek bar lagata hai. Agar servant ITEC assignment par hai, ya foreign based office mein posted hai, ya kisi foreign Government ke saath contract assignment par hai, to twenty-year route nahi milega."),
            ("PROVISO 3: THE WAY BACK",
             "Unless, after transfer to India, he has ==resumed charge in India== and served ==not less than one year==.",
             "Third proviso, concluding words: unless, after having been transferred to India, he has resumed the charge of the post in India and served for a period of not less than one year. So the bar lifts only after one full year of duty in India following the return.",
             ORANGE,
             "Bahar jaane par bar lagta hai, lekin India wapas aane par wo hat jaata hai. Shart ye hai ki India mein charge sambhala ho aur kam se kam ek saal service ki ho. Ye ek saal wala point podcast mein nahi tha."),
            ("PROVISO 4: NO ROUNDING",
             "He must complete twenty years ==on the intended date==, and the ==Rule 44(7)== three-month rounding does ==not== apply.",
             "Fourth proviso to Rule 43(1): a servant is eligible only if he has completed, or will complete, a qualifying service of twenty years on the intended date of retirement, and the provision in Rule 44(7) for treating a fraction of a year of three months or more as a completed six-monthly period shall not be applicable for determining qualifying service under this rule. Nineteen years and nine months is therefore not twenty years here.",
             GREEN,
             "Chautha proviso sabse bada trap hai. Twenty years intended date par pure hone chahiye, aur Rule forty-four ka three-month rounding yahan band hai. Yaani nineteen saal nau mahine yahan twenty saal nahi bante."),
            ("EXPLANATION",
             "The appointing authority is the one that can ==appoint== to the post he is leaving.",
             "Explanation to Rule 43: appointing authority means the authority competent to make appointments to the service or post from which the Government servant seeks voluntary retirement. Same idea as the Rule 42 Explanation, but keyed to the post he is leaving, not to the post he is going to.",
             PURPLE,
             "Explanation kehti hai appointing authority wahi hai jo us post par appointment kar sakti hai jis se voluntary retirement maangi ja rahi hai. Rule forty-two jaisa hi idea, bas post wahi hai jise chhoda ja raha hai."),
        ],
        "trap": "<<TRAP:>> 19 years 9 months = 20 years under ==Rule 44(8)==, but ==not== under Rule 43 — the fourth proviso switches the rounding off.",
        "trap_say": ("Trap ye hai: nineteen saal nau mahine Rule forty-four ke under twenty saal ban jaate hain, "
                     "lekin Rule forty-three mein nahi. Chautha proviso rounding band kar deta hai."),
        "covers": ["R43-1-P3", "TL-R43-ONEYR", "R43-1-P4", "TL-R43-NOROUND", "R43-EXPL"],
    },
    {
        "id": "b4_05_rule43_refusal",
        "part": "RULE 43(3) • WHEN PERMISSION CAN BE WITHHELD",
        "title": "THREE GROUNDS TO WITHHOLD, AND ONE APPROVAL THAT OVERRIDES THEM",
        "accent": RED, "badge": "RULE 43(3)",
        "crumb": "CHAPTER VI  •  SUSPENSION, CHARGE SHEET, COURT CASE",
        "q": "When may the authority refuse voluntary retirement, and who can still allow it?",
        "q_say": "Sir, voluntary retirement kab rok sakte hain, aur rok ke baad bhi kaun allow kar sakta hai?",
        "heads": [("SUSPENSION", "Ground one", BLUE),
                  ("CHARGE SHEET", "Ground two", ORANGE),
                  ("COURT CASE", "Ground three", GREEN),
                  ("PRESIDENT", "Approval to override", PURPLE)],
        "boxes": [
            ("43(3)(i): SUSPENSION",
             "Permission may be withheld if the servant is ==under suspension==.",
             "Rule 43(3)(i): it shall be open to the appropriate appointing authority to withhold permission to a Government servant who seeks to retire under this rule if the Government servant is under suspension. Withholding is discretionary, not automatic.",
             BLUE,
             "Sub-rule three ke teen grounds hain. Pehla: agar servant suspension par hai. Dhyaan do, ye authority ka option hai, automatic stop nahi."),
            ("43(3)(ii) & (iii): PENDING",
             "Withhold if a ==charge sheet== has been issued and disciplinary proceedings are pending, or if ==judicial proceedings== for grave misconduct are pending.",
             "Rule 43(3)(ii) and (iii): permission may be withheld if a charge sheet has been issued and disciplinary proceedings are pending, or if judicial proceedings on charges which may amount to grave misconduct are pending. Explanation: judicial proceedings are deemed pending if a complaint or a police report, of which the Magistrate takes cognizance, has been made or filed in a criminal proceeding.",
             ORANGE,
             "Doosra aur teesra ground: charge sheet issue ho chuki hai aur disciplinary proceedings pending hain, ya grave misconduct ke charges par judicial proceedings pending hain. Explanation kehti hai Magistrate cognizance le le to proceedings pending maane jaate hain."),
            ("43(3) PROVISO",
             "If the authority still wants to accept the notice, the ==approval of the President== must be obtained.",
             "Proviso to Rule 43(3): in cases where the appointing authority proposes to accept the notice of voluntary retirement in spite of the circumstances referred to in this sub-rule, approval of the President shall be obtained. The President acts through the administrative Ministry, but the file must record that approval.",
             GREEN,
             "Proviso: agar authority in circumstances ke bawajood notice accept karna chahti hai, to President ki approval leni padegi. Ye approval file par record honi chahiye."),
            ("43(1) vs 43(3)",
             "Rule 43(1) is the ==right==. Rule 43(3) is the ==gate==. A pending case does not cancel the twenty years; it only lets the gate stay shut.",
             "Reading Rule 43(1) with Rule 43(3): completing twenty years creates eligibility, not an absolute right to walk out. Suspension, a charge sheet or a criminal case lets the authority keep the gate shut; the President can still open it. Contrast Rule 42, where the Government itself is the moving party.",
             PURPLE,
             "Dono ko saath padho. Twenty years puri hone se eligibility banti hai, absolute right nahi. Suspension, charge sheet ya criminal case ho to authority gate band rakh sakti hai, aur President chaahe to khol sakta hai."),
        ],
        "trap": "<<TRAP:>> A pending case does ==not== make the servant ineligible. It only gives the authority a discretion to ==withhold permission==.",
        "trap_say": ("Trap ye hai: pending case se servant ineligible nahi ho jaata. Sirf authority ko discretion milta hai "
                     "ki permission rok de."),
        "covers": ["R43-3", "R43-3-I", "R43-3-II", "R43-3-III", "R43-3-P1", "R43-3-EXPL"],
    },
    {
        "id": "b4_06_rule43_exits",
        "part": "RULE 43(4) TO (7) • SHORTER NOTICE, DISABILITY, WITHDRAWAL, EXCLUSIONS",
        "title": "THE FOUR EXIT DOORS OF RULE 43 — AND THE ONE THAT IS LOCKED",
        "accent": BLUE, "badge": "RULE 43(4)-(7)",
        "crumb": "CHAPTER VI  •  THE PRACTICAL PROVISIONS",
        "q": "Can the notice be shortened, can it be taken back, and who is outside the rule?",
        "q_say": "Sir, notice chhota ho sakta hai, wapas liya ja sakta hai, aur is rule se bahar kaun hai?",
        "heads": [("43(4)", "Shorter notice", BLUE),
                  ("43(5)", "Disability option", ORANGE),
                  ("43(6)", "Withdrawal", GREEN),
                  ("43(7)", "Who is outside", PURPLE)],
        "boxes": [
            ("43(4): SHORTER NOTICE",
             "A ==written request with reasons==. The authority may relax it if there is ==no administrative inconvenience==, on condition that he does not apply to ==commute== before three months end.",
             "Rule 43(4)(a): the servant may request in writing that a notice of less than three months be accepted, giving reasons. (b) The appointing authority may consider the request on merits and, if satisfied that curtailment will not cause administrative inconvenience, may relax the three-month requirement on the condition that the servant shall not apply for commutation of a part of his pension before the expiry of the three-month notice period (R43-4-COMMUTE).",
             BLUE,
             "Sub-rule four: agar jaldi jaana hai to reasons ke saath written request do. Authority manzoor kare to teen mahine ki notice kam ho sakti hai, lekin ek shart par, ki teen mahine khatam hone se pehle commutation ki application nahi denge."),
            ("43(5): DISABILITY",
             "If he has acquired a ==section 20 RPwD Act== disability, he must be ==advised== he can stay on the same pay scale and benefits.",
             "Rule 43(5): where a Government servant acquiring a disability to which section 20 of the Rights of Persons with Disabilities Act, 2016 applies gives notice of voluntary retirement, he shall be advised that he has the option of continuing in service with the same pay scale and service benefits; if he does not withdraw the notice, his request may be processed.",
             ORANGE,
             "Sub-rule five ek safety net hai. Agar servant ko aisi disability ho gayi hai jo RPwD Act ke section twenty mein aati hai, to use batana padega ki wo same pay scale aur benefits par service continue kar sakta hai. Agar phir bhi withdraw na kare, request process hogi."),
            ("43(6): WITHDRAWAL",
             "Notice once given can be withdrawn only with the ==specific approval== of the authority, and the request must come ==15 days== before the intended date.",
             "Rule 43(6): a servant who has elected to retire and given notice is precluded from withdrawing it except with the specific approval of the appointing authority. Proviso: the request for withdrawal shall be made not less than fifteen days before the intended date of voluntary retirement (TL-R43-WITHDRAW-15D).",
             GREEN,
             "Sub-rule six: notice de dene ke baad usse wapas lena aasan nahi. Appointing authority ki specific approval chahiye, aur request intended date se kam se kam pandrah din pehle aani chahiye."),
            ("43(7): OUTSIDE",
             "Not for ==Special VRS== surplus staff, and not for ==permanent or immediate absorption== in an autonomous body or PSU. Their routes are Rules 35 to 38.",
             "Rule 43(7): this rule shall not apply to a servant who (a) retires under the Special Voluntary Retirement Scheme relating to voluntary retirement of surplus employees, or (b) retires for being absorbed permanently in an autonomous body or public sector undertaking to which he is on deputation, or for joining such a body or undertaking on immediate absorption basis. Those cases go under Rules 35 to 38 (Batch 3).",
             PURPLE,
             "Sub-rule seven batata hai kaun bahar hai. Special VRS wale surplus staff, aur autonomous body ya PSU mein permanent ya immediate absorption wale, is rule mein nahi aate. Unka route Rules thirty-five se thirty-eight hai."),
        ],
        "trap": "<<TRAP:>> Rule ==44(7)== rounding is barred by Rule 43(1) P4, but Rule ==44(8)== (9 years 9 months) is untouched by Rule 43.",
        "trap_say": ("Trap ye hai: Rule forty-three chautha proviso Rule forty-four ka three-month rounding band karta hai, "
                     "lekin nine years nine months wala Rule forty-four aath chhoota rehta hai."),
        "covers": ["R43-4", "R43-4-COMMUTE", "R43-5", "R43-6", "TL-R43-WITHDRAW-15D", "R43-7"],
    },
    {
        "id": "b4_07_rule44_1",
        "part": "RULE 44(1) • HOW MUCH PENSION",
        "title": "RULE 44(1) — FIFTY PERCENT OF THE BETTER BASE, WITH A FLOOR AND A CEILING",
        "accent": RED, "badge": "RULE 44(1)",
        "crumb": "CHAPTER VII  •  REGULATION OF PENSION AND GRATUITY",
        "q": "How is the pension amount fixed, and what are the minimum and maximum?",
        "q_say": "Sir, pension ka amount kaise tay hota hai, aur minimum aur maximum kya hai?",
        "heads": [("10 YEARS", "Minimum qualifying service", BLUE),
                  ("50 PERCENT", "Of the better base", ORANGE),
                  ("Rs 9,000", "Minimum per month", GREEN),
                  ("Rs 1,25,000", "Maximum per month", PURPLE)],
        "boxes": [
            ("44(1): THE RATE",
             "Ten years qualifying service. Pension = ==50 per cent== of ==emoluments or average emoluments==, whichever is more beneficial.",
             "Rule 44(1): a Government servant who retires under Rule 33, 34, 35, 36, 37, 38 or 39 after completing qualifying service of not less than ten years shall become eligible for a pension calculated at fifty per cent of emoluments or average emoluments, whichever is more beneficial, subject to a minimum of Rs 9,000 and a maximum of Rs 1,25,000 per month. Emoluments: Rule 31. Average emoluments: Rule 32, the average of the last ten months.",
             BLUE,
             "Rule forty-four ka core. Das saal qualifying service, aur pension fifty percent hogi emoluments ya average emoluments mein se jo zyada fayda de. Emoluments Rule thirty-one se, average emoluments Rule thirty-two se, yaani last das mahine ka average."),
            ("FLOOR AND CEILING",
             "Minimum ==Rs 9,000== and maximum ==Rs 1,25,000== a month. These figures sit inside the Rule, so a Pay Commission can move them.",
             "Rule 44(1): pension shall not be less than Rs 9,000 per month and not more than Rs 1,25,000 per month. These are figures written in the Rule (7th CPC scale). No change was found up to 21.10.2026. The 8th CPC was constituted on 03.11.2025 and its report is due in about eighteen months, so re-check both figures afterwards (S8).",
             ORANGE,
             "Rule mein floor aur ceiling bhi likhi hai. Minimum nau hazaar rupees mahina, maximum ek lakh pachchees hazaar rupees mahina. Ye figures Rule ke andar hain, isliye naye Pay Commission ke baad badal sakti hain. Aathva Pay Commission November twenty twenty-five mein bana tha."),
            ("THE PROVISO",
             "Only an ==invalid pension== case under Rule 39 that meets ==Rule 39(9)== escapes the ten-year condition.",
             "Proviso to Rule 44(1): a Government servant who retires under Rule 39 before completing ten years but fulfils the conditions in Rule 39(9) shall also be eligible for invalid pension at fifty per cent of emoluments or average emoluments, whichever is more beneficial, and the ten-year condition shall not apply. Nobody else is excused.",
             GREEN,
             "Proviso ek hi exception deta hai. Rule thirty-nine ke under invalid pension, jo Rule thirty-nine ke sub-rule nine ki conditions poori kare, use das saal ki shart se chhoot milti hai. Kisi aur ko nahi."),
            ("EXPLANATION",
             "The words are ==eligible for grant==, not sanctioned. Rule 44 fixes the amount; sanction is a separate process.",
             "Rule 44(1) says the servant shall become eligible for grant of a pension. Eligibility is not sanction: the amount is fixed by Rule 44 but the sanction, the PPO and the payment run through the pension papers procedure of Chapter X (Rules 53 to 70, Batch 5).",
             PURPLE,
             "Ek fine point. Rule kehta hai eligible for grant, yaani haq ban jaata hai. Sanction alag process hai, PPO alag, payment alag. Wo Chapter ten mein aata hai, jo Batch five hai."),
        ],
        "trap": "<<TRAP:>> Take the ==HIGHER== of emoluments and average emoluments. 50 per cent of Rs 72,000 is ==Rs 36,000==, never Rs 40,000.",
        "trap_say": ("Trap ye hai: emoluments aur average emoluments mein se jo zyada ho wahi lo. BAHATTAR hazaar ka fifty percent "
                     "chhattis hazaar hota hai, chalees hazaar nahi."),
        "covers": ["R44-1", "LIMIT-R44-50", "LIMIT-PENSION-FLOOR", "LIMIT-PENSION-CEIL", "R44-1-P1", "R44-1-ELIGIBLE"],
    },
    {
        "id": "b4_08_rule44_2_5",
        "part": "RULE 44(2) TO (5) • SERVICE GRATUITY AND PENALTY CASES",
        "title": "UNDER TEN YEARS, COMPULSORY RETIREMENT, AND DISMISSAL",
        "accent": GREEN, "badge": "RULE 44(2)-(5)",
        "crumb": "CHAPTER VII  •  FOUR SUB-RULES IN ONE SCREEN",
        "q": "What does a servant with under ten years get, and what happens on compulsory retirement or dismissal?",
        "q_say": "Sir, das saal se kam service par kya milta hai, aur compulsory retirement ya dismissal mein kya hota hai?",
        "heads": [("44(2)", "Service gratuity", BLUE),
                  ("44(3)", "Reduced emoluments", ORANGE),
                  ("44(4)", "Compulsory retirement", GREEN),
                  ("44(5)", "Dismissal", PURPLE)],
        "boxes": [
            ("44(2): SERVICE GRATUITY",
             "Under ten years: ==half a month's emoluments== for every ==completed six-monthly period== of qualifying service.",
             "Rule 44(2): a servant who retires under any of the Rules in sub-rule (1) but has not become eligible for pension shall be eligible for service gratuity, calculated at half a month's emoluments for every completed six-monthly period of qualifying service. There is no maximum multiple in this sub-rule; the Rs 25 lakh ceiling belongs to Rule 45, not here.",
             BLUE,
             "Sub-rule two: agar das saal nahi hue aur pension nahi bani, to service gratuity milegi. Har complete six-monthly period par aadha mahina emoluments. Isme sixteen times jaisi koi cap nahi hai, wo Rule forty-five ka rule hai."),
            ("44(3): REDUCED PAY",
             "If emoluments were reduced in the ==last ten months==, use ==average emoluments==, and DA on the retirement date counts as emoluments.",
             "Rule 44(3): where the emoluments of a servant have been reduced during the last ten months of his service, average emoluments as referred to in Rule 32 shall be treated as emoluments for the purpose of sub-rule (2), and the dearness allowance admissible on the date of retirement shall also be treated as part of emoluments.",
             ORANGE,
             "Sub-rule three: agar last das mahine mein pay kam hui thi, to average emoluments ko emoluments maana jayega. Aur retirement date par jo dearness allowance milta hai, wo bhi emoluments ka hissa hai."),
            ("44(4): COMPULSORY",
             "(a) Ten years or more: such ==portion of superannuation pension== as the authority sanctions under Rule 40. (b) Under ten years: same idea on service gratuity.",
             "Rule 44(4)(a): a servant compulsorily retired after ten years or more who has become eligible for compulsory retirement pension under Rule 40 gets such portion or percentage of the superannuation pension calculated under sub-rule (1) as the competent authority may sanction under Rule 40. (b) A servant compulsorily retired before ten years gets such portion of the superannuation service gratuity under sub-rule (2) as may be sanctioned under Rule 40. Rule 40 caps the choice between two-thirds and full (S2, O.M. 30.10.2025).",
             GREEN,
             "Sub-rule four compulsory retirement ka hai. Das saal ya zyada ho to Rule forty ke under superannuation pension ka kuch portion, aur das saal se kam ho to service gratuity ka portion. Rule forty kehta hai do-tihai se lekar poori pension tak."),
            ("44(5): DISMISSAL",
             "Compassionate allowance is a ==portion of the pension== he would have got on superannuation; under ten years, a portion of the ==service gratuity==.",
             "Rule 44(5)(a): a servant dismissed or removed after ten years or more who is sanctioned compassionate allowance under Rule 41 gets such portion or percentage of the pension admissible on superannuation as the competent authority may sanction. (b) A servant dismissed or removed before ten years gets such portion of the service gratuity which would have been admissible. Rule 41 caps it at two-thirds (R41-CAP).",
             PURPLE,
             "Sub-rule five dismissal ka hai. Das saal se zyada ho to superannuation pension ka portion compassionate allowance ke roop mein, aur kam ho to service gratuity ka portion. Rule forty-one kehta hai ye do-tihai se zyada nahi ho sakta."),
        ],
        "trap": "<<TRAP:>> A ==service gratuity== under Rule 44(2) has no 16.5-times cap. The cap and the ==Rs 25 lakh== ceiling belong to ==Rule 45==.",
        "trap_say": ("Trap ye hai: Rule forty-four ki service gratuity par sixteen point five times ka cap nahi hai. "
                     "Cap aur pachchees lakh ki ceiling Rule forty-five ki hain."),
        "covers": ["R44-2", "LIMIT-R44-SG-HALF", "R44-3", "R44-4A", "R44-4B", "R44-5A", "R44-5B", "R41-CAP", "OM-30.10.2025-COMP"],
    },
    {
        "id": "b4_09_rule44_6",
        "part": "RULE 44(6) • ADDITIONAL PENSION AFTER EIGHTY",
        "title": "RULE 44(6) — THE FIVE-SLAB TABLE AND THE BIRTHDAY TRAP",
        "accent": ORANGE, "badge": "RULE 44(6)",
        "crumb": "CHAPTER VII  •  ADDITIONAL PENSION",
        "q": "How much extra pension comes after eighty, and from which day is it paid?",
        "q_say": "Sir, assi saal ke baad extra pension kitni milti hai, aur kis din se milti hai?",
        "heads": [("80-85", "20 per cent", BLUE),
                  ("85-90", "30 per cent", ORANGE),
                  ("90-95", "40 per cent", GREEN),
                  ("95-100", "50 per cent", PURPLE)],
        "chart": {
            "title": "Additional pension as a percentage of basic pension",
            "unit": "%", "max": 100, "label_w": 330,
            "bars": [("80 to under 85 years", 20, BLUE, "twenty per cent"),
                     ("85 to under 90 years", 30, ORANGE, "thirty per cent"),
                     ("90 to under 95 years", 40, GREEN, "forty per cent"),
                     ("95 to under 100 years", 50, PURPLE, "fifty per cent"),
                     ("100 years or more", 100, RED, "hundred per cent")],
        },
        "boxes": [
            ("THE TABLE",
             "==20 / 30 / 40 / 50 / 100== per cent of basic pension at 80 / 85 / 90 / 95 / 100 years. ==No 60 per cent slab exists==.",
             "Rule 44(6)(a): after completion of eighty years, additional pension is payable in five slabs - 20 per cent from 80 to under 85, 30 per cent from 85 to under 90, 40 per cent from 90 to under 95, 50 per cent from 95 to under 100, and 100 per cent at 100 years or more, of basic pension or basic compassionate allowance. There is no 60 per cent slab; the source podcast invented one.",
             BLUE,
             "Table yaad karo: assi se pachattar tak twenty percent, pachattar se nabbe tak thirty, nabbe se pachannev tak chalees, pachannev se sau tak pachaas, aur sau saal par hundred percent. Saath percent ka koi slab nahi hai, wo podcast ki galti thi."),
            ("THE BASE",
             "It is a percentage of ==basic pension==, or basic ==compassionate allowance==, not of pension plus DR.",
             "Rule 44(6): the slabs apply to basic pension or basic compassionate allowance. Dearness relief is calculated on pension separately and is not part of the base for additional pension. Adding DR into the base inflates the figure and is a common examination error.",
             ORANGE,
             "Base basic pension hai, ya basic compassionate allowance. Dearness relief isme add nahi hota. DR alag se pension par lagta hai. Agar DR ko base mein jod diya to figure galat ho jayega."),
            ("THE DAY",
             "Payable from the ==first day of the calendar month== in which it falls due.",
             "Rule 44(6)(b): the additional pension or additional compassionate allowance shall be payable from the first day of the calendar month in which it falls due. Illustration in the Rule: a pensioner born on 20.08.1942 and a pensioner born on 01.08.1942 both get 20 per cent from 01.08.2022. The birthday itself does not split the month.",
             GREEN,
             "Payment kis din se? Us calendar month ki pehli tareekh se, jisme wo due hota hai. Rule ka illustration: bees August aur pehli August, dono ka janmadin, dono ko pehli August se twenty percent. Birthday se mahina nahi tootta."),
            ("THE TRAP",
             "Age is taken on the ==birthday==, but the money starts on the ==first of that month==. Two different dates, one card.",
             "Trap: the qualifying event is the birthday, the payment start date is the first of the calendar month in which the birthday falls. The source podcast also wrongly placed additional pension from the first of the FOLLOWING month; the Rule says the calendar month in which it falls due (S8 closes this point with the O.M. of 30.10.2025).",
             PURPLE,
             "Trap ye hai: age birthday par count hoti hai, lekin paisa us mahine ki pehli tareekh se shuru hota hai. Do alag dates hain. Podcast ne agle mahine ki pehli tareekh kaha tha, wo galat tha."),
        ],
        "trap": "<<TRAP:>> ==No 60 per cent slab.== At 100 years it is ==100 per cent==, starting from the first of that calendar month.",
        "trap_say": ("Trap ye hai: saath percent ka slab nahi hai. Sau saal par hundred percent milta hai, "
                     "aur wo us calendar month ki pehli tareekh se shuru hota hai."),
        "covers": ["R44-6", "R44-6-SLAB-80", "R44-6-SLAB-85", "R44-6-SLAB-90", "R44-6-SLAB-95", "R44-6-SLAB-100",
                   "R44-6-BASE", "R44-6-DAY", "R44-6-ILLUS", "OM-30.10.2025-ADDL"],
    },
    {
        "id": "b4_10_rule44_7_10",
        "part": "RULE 44(7) TO (10) • ROUNDING AND NEAR MISSES",
        "title": "THREE MONTHS, NINE YEARS NINE MONTHS, AND THE RUPEE",
        "accent": PURPLE, "badge": "RULE 44(7)-(10)",
        "crumb": "CHAPTER VII  •  THE ARITHMETIC SUB-RULES",
        "q": "How are fractions of a year and fractions of a rupee treated?",
        "q_say": "Sir, saal ke fraction aur rupee ke paise ka kya rule hai?",
        "heads": [("44(7)", "3 months = half year", BLUE),
                  ("44(8)", "9y 9m = 10 years", ORANGE),
                  ("44(9)", "Round up the rupee", GREEN),
                  ("44(10)", "Mid-month stop", PURPLE)],
        "boxes": [
            ("44(7): FRACTIONS",
             "A fraction of a year of ==three months or more== counts as a completed ==six-monthly period==.",
             "Rule 44(7): in calculating the length of qualifying service, a fraction of a year equal to three months and above shall be treated as a completed six-monthly period and reckoned as qualifying service. Two years and three months therefore counts as two years and six months. But Rule 43(1) fourth proviso switches this off for the twenty-year test.",
             BLUE,
             "Sub-rule seven: teen mahine ya usse zyada ka fraction ek complete six-monthly period maana jayega. Yaani do saal teen mahine, do saal chhah mahine ban jaate hain. Lekin Rule forty-three ke twenty saal ke test mein ye band hai."),
            ("44(8): NEAR MISS",
             "==Nine years and nine months== or more is treated as ==ten years==, so pension is payable.",
             "Rule 44(8): where a servant has rendered qualifying service of nine years and nine months or more but less than ten years, his qualifying service for the purpose of this rule shall be ten years and he shall be eligible for pension under sub-rule (1). This is the pension near miss; the gratuity near miss is four years nine months under Rule 45(5).",
             ORANGE,
             "Sub-rule eight ek near miss bachata hai. Nau saal nau mahine ya usse zyada service ko das saal mana jayega, aur pension mil jayegi. Gratuity mein aisa near miss chaar saal nau mahine par hai, Rule forty-five mein."),
            ("44(9): RUPEE",
             "Every amount - pension, gratuity, allowance - is expressed in ==whole rupees== and any fraction is rounded ==up== to the next rupee.",
             "Rule 44(9): the amount of pension, service gratuity, compassionate allowance, additional pension or additional compassionate allowance finally determined shall be expressed in whole rupees and any fraction of a rupee shall be rounded off to the next higher rupee separately for each such amount. Rounding is per amount, not on the total.",
             GREEN,
             "Sub-rule nine: har amount poore rupee mein likhi jayegi, aur paisa ho to agle rupee tak badha diya jayega. Rounding har amount par alag hoti hai, total par nahi."),
            ("44(10): MID-MONTH",
             "Where pension is discontinued ==in the middle of a month==, the part-month amount is rounded up to the next rupee.",
             "Rule 44(10): where pension is discontinued in the middle of a calendar month, the amount payable for the fraction of that month shall also be rounded off to the next higher rupee. This covers death, absorption and any other mid-month stoppage.",
             PURPLE,
             "Sub-rule das: agar pension mahine ke beech mein band ho, to us adhoore mahine ka amount bhi agle rupee tak round up hoga. Ye death, absorption, ya kisi bhi beech mein rukne par lagta hai."),
        ],
        "trap": "<<TRAP:>> ==Rule 44(8)== saves nine years nine months. ==Rule 43(1) P4== refuses that same mercy for the twenty-year test.",
        "trap_say": ("Trap ye hai: Rule forty-four nau saal nau mahine ko bacha leta hai, lekin Rule forty-three "
                     "chautha proviso twenty saal ke test mein ye chhoot nahi deta."),
        "covers": ["R44-7", "TL-R44-ROUND-3M", "R44-8", "TL-R44-NEARMISS-9Y9M", "R44-9", "R44-10"],
    },
    {
        "id": "b4_11_rule45_retirement",
        "part": "RULE 45(1)(a) • RETIREMENT GRATUITY",
        "title": "RULE 45(1)(a) — ONE QUARTER PER HALF YEAR, CAPPED AT 16.5 TIMES",
        "accent": GREEN, "badge": "RULE 45(1)(a)",
        "crumb": "CHAPTER VII  •  THE LUMP SUM",
        "q": "How much retirement gratuity is payable, and what caps apply?",
        "q_say": "Sir, retirement gratuity kitni milti hai, aur uspar kya caps hain?",
        "heads": [("5 YEARS", "Minimum qualifying service", BLUE),
                  ("ONE QUARTER", "Per six-monthly period", ORANGE),
                  ("16.5 TIMES", "Cap on emoluments", GREEN),
                  ("Rs 25 LAKH", "Money ceiling", PURPLE)],
        "boxes": [
            ("THE RATE",
             "Five years qualifying service, then ==one-fourth of emoluments== for each ==completed six-monthly period==, capped at ==16.5 times== emoluments.",
             "Rule 45(1)(a): a servant who has completed five years qualifying service and has become eligible for service gratuity or pension under Rule 44 shall, on retirement, be granted retirement gratuity equal to one-fourth of his emoluments for each completed six-monthly period of qualifying service, subject to a maximum of 16.5 times the emoluments. Thirty-three half-years reach the cap; anything beyond thirty-three is free service as far as gratuity is concerned.",
             BLUE,
             "Rule forty-five ek(a): paanch saal qualifying service ke baad, har complete six-monthly period par emoluments ka chauthai, aur maximum solah point paanch guna emoluments. Tetees half-years ke baad cap lag jaata hai."),
            ("THE EXAMPLE",
             "Ravi: 22 years, emoluments Rs 60,000. 44 half-years x one-fourth = ==11 times== = ==Rs 6,60,000==.",
             "Worked Example (arithmetic recomputed): Ravi retires with twenty-two years qualifying service and emoluments of Rs 60,000. Completed six-monthly periods: 44. Gratuity = 44 x 1/4 x 60,000 = 11 x 60,000 = Rs 6,60,000, well inside the 16.5-times cap (Rs 9,90,000) and the money ceiling.",
             ORANGE,
             "Ek example. Ravi ke paas baees saal service hai aur emoluments saath hazaar. Chaalis half-years, har ek par chauthai, yaani gyarah guna, chhe lakh saath hazaar rupees. Cap se neeche hai, theek hai."),
            ("THE 16.5 CAP",
             "At ==33 half-years== the cap is reached. More service adds nothing to gratuity, though it keeps adding to pension.",
             "Rule 45(1)(a): the maximum of 16.5 times emoluments is reached at 33 completed six-monthly periods, that is 16 years 6 months of qualifying service. Service beyond that does not increase retirement gratuity; it does keep increasing pension, because Rule 44 has no multiple cap of this kind.",
             GREEN,
             "Solah point paanch guna cap tetees half-years par pahunch jaata hai, yaani solah saal chhah mahine. Uske baad gratuity nahi badhti. Pension badhti rehti hai, kyunki Rule forty-four mein aisa multiple cap nahi hai."),
            ("THE CEILING",
             "Rule text says ==Rs 20 lakh==. The O.M. of ==30.05.2024== raised it to ==Rs 25 lakh== with effect from 01.01.2024.",
             "First proviso to Rule 45(1): retirement gratuity or death gratuity shall in no case exceed twenty lakh rupees. DoPPW O.M. F.No. 28/03/2024-P&PW(B)/Gratuity/9559 dated 30.05.2024 raised the ceiling to Rs 25 lakh with effect from 01.01.2024 and said the Rules would be amended separately (S5). Up to October 2026 no such amendment was found, so the figure lives in the O.M. and the Rule still reads twenty lakh.",
             PURPLE,
             "Rule ka text bees lakh kehta hai. Lekin tirish May do hazaar chaubees ke O.M. ne ceiling pachchees lakh kar di, pehli January do hazaar chaubees se. Rule amendment abhi tak nahi aaya, isliye figure O.M. se quote karo, Rule se nahi."),
        ],
        "trap": "<<TRAP:>> Rule text = ==Rs 20 lakh==; current figure = ==Rs 25 lakh== from 01.01.2024. Quote the ==O.M. date== with the number.",
        "trap_say": ("Trap ye hai: Rule mein bees lakh likha hai, lekin aaj pachchees lakh chalta hai, pehli January do hazaar chaubees se. "
                     "Figure ke saath O.M. ki date zaroor bolo."),
        "covers": ["R45-1A", "LIMIT-RG-5Y", "LIMIT-RG-CAP165", "LIMIT-RG-33HALF", "R45-EX1", "R45-1-P1",
                   "LIMIT-GRATUITY-CEILING", "OM-30.05.2024-GRAT"],
    },
    {
        "id": "b4_12_rule45_death",
        "part": "RULE 45(1)(b) AND (2) • DEATH GRATUITY",
        "title": "DEATH GRATUITY — FIVE SLABS, NO FIVE-YEAR CONDITION",
        "accent": RED, "badge": "RULE 45(1)(b)",
        "crumb": "CHAPTER VII  •  DEATH IN SERVICE",
        "q": "How much death gratuity is payable for each length of service?",
        "q_say": "Sir, death gratuity service ki length ke hisaab se kitni milti hai?",
        "heads": [("UNDER 1 YEAR", "2 times", BLUE),
                  ("1 TO 5 YEARS", "6 times", ORANGE),
                  ("5 TO 11 YEARS", "12 times", GREEN),
                  ("11 TO 20 YEARS", "20 times", PURPLE)],
        "chart": {
            "title": "Death gratuity multiples of emoluments",
            "unit": "x", "max": 33, "label_w": 380,
            "bars": [("Less than 1 year", 2, BLUE, "2 times"),
                     ("1 year to under 5 years", 6, ORANGE, "6 times"),
                     ("5 years to under 11 years", 12, GREEN, "12 times"),
                     ("11 years to under 20 years", 20, PURPLE, "20 times"),
                     ("20 years or more", 33, RED, "half month per half year, max 33")],
        },
        "boxes": [
            ("THE TABLE",
             "==2 / 6 / 12 / 20== times of emoluments for the first four slabs, then ==half a month per six-monthly period== up to ==33 times==.",
             "Rule 45(1)(b): if a servant dies while in service, death gratuity is paid to his family in the manner in Rule 47(1) at these rates - less than one year: 2 times; one year or more but less than five years: 6 times; five years or more but less than eleven years: 12 times; eleven years or more but less than twenty years: 20 times; twenty years or more: half of emoluments for every completed six-monthly period, subject to a maximum of 33 times.",
             BLUE,
             "Table yaad karo. Ek saal se kam par do guna, paanch saal se kam par chhah guna, gyarah saal se kam par baarah guna, bees saal se kam par bees guna, aur bees saal se zyada par har six-monthly period par aadha mahina, maximum tetees guna."),
            ("NO FIVE-YEAR RULE",
             "Death gratuity has ==no five-year minimum==. A servant who dies after six months still gets ==2 times==.",
             "Rule 45(1)(b) contains no minimum qualifying service condition; the table begins at less than one year. The five-year condition in Rule 45(1)(a) applies to retirement gratuity only. This is the single most common error in the source podcast, which applied the five years to both.",
             ORANGE,
             "Sabse bada point: death gratuity par paanch saal ki koi shart nahi hai. Chhah mahine ki service par death ho to bhi do guna milega. Paanch saal ki shart sirf retirement gratuity ki hai."),
            ("THE EXAMPLE",
             "Isha dies with 6 years 3 months and emoluments Rs 45,000. Slab 3: ==12 times== = ==Rs 5,40,000==.",
             "Worked Example (invented): Isha dies in service with six years and three months qualifying service and emoluments of Rs 45,000. Six years and three months falls in the third slab, five years or more but less than eleven years, so death gratuity is 12 x 45,000 = Rs 5,40,000, rounded to the next rupee under the second proviso.",
             GREEN,
             "Isha ka example. Chhah saal teen mahine service, emoluments paintaalees hazaar. Teesra slab lagta hai, baarah guna, yaani paanch lakh chalees hazaar rupees. Fraction ho to agle rupee tak round up."),
            ("45(2): SUICIDE",
             "Death by ==suicide== is covered by the same death-gratuity provision. Clause (b) applies.",
             "Rule 45(2): the provision of clause (b) of sub-rule (1) shall also be applicable in the case of death of a Government servant by suicide. So the family is not denied death gratuity on that ground alone. Rule 48's murder charge is a different question and turns on a criminal proceeding.",
             PURPLE,
             "Sub-rule two kehta hai suicide se death par bhi death gratuity ka clause lagta hai. Yaani sirf is wajah se parivaar ko gratuity se nahi roka jayega. Rule forty-eight ka murder charge alag mamla hai, wo criminal case par chalta hai."),
        ],
        "trap": "<<TRAP:>> The third slab ends at ==11 years==, not 10. Death gratuity never asks for ==5 years==; retirement gratuity does.",
        "trap_say": ("Trap ye hai: teesra slab gyarah saal par khatam hota hai, das par nahi. Aur death gratuity mein paanch saal "
                     "ki shart nahi hoti, wo retirement gratuity mein hoti hai."),
        "covers": ["R45-1B-SLAB1", "R45-1B-SLAB2", "R45-1B-SLAB3", "R45-1B-SLAB4", "R45-1B-SLAB5",
                   "R45-1B-NO5YR", "R45-1B-EX", "R45-2"],
    },
    {
        "id": "b4_13_rule45_residuary",
        "part": "RULE 45(3) TO (6) • RESIDUARY GRATUITY AND THE BASE",
        "title": "RULE 45(3) — DEATH WITHIN FIVE YEARS, AND THE TWELVE-TIMES FLOOR",
        "accent": PURPLE, "badge": "RULE 45(3)-(6)",
        "crumb": "CHAPTER VII  •  THE FORGOTTEN GRATUITY",
        "q": "What is residuary gratuity, and how is the gratuity base calculated?",
        "q_say": "Sir, residuary gratuity kya hai, aur gratuity ka base kaise nikalta hai?",
        "heads": [("5 YEARS", "Death window", BLUE),
                  ("12 TIMES", "The floor", ORANGE),
                  ("4y 9m", "Gratuity near miss", GREEN),
                  ("RULE 31", "The emoluments base", PURPLE)],
        "boxes": [
            ("45(3): THE TEST",
             "Dies within ==five years of retiring==? Add the pension received, the gratuity and the commuted value. Below ==12 times emoluments==, the gap is residuary gratuity.",
             "Rule 45(3): where a servant who on retirement became eligible for service gratuity or pension dies within five years from the date of retirement, including compulsory retirement as a penalty, and the sums actually received by him on account of such gratuity or pension, together with the retirement gratuity under sub-rule (1) and the commuted value of any portion commuted, are less than twelve times his emoluments, a residuary gratuity equal to the deficiency may be granted to his family in the manner in Rule 47(1).",
             BLUE,
             "Sub-rule three: agar retirement ke paanch saal ke andar death ho jaye, to jo kuch mila, retirement gratuity aur commuted value, sab jodo. Agar total emoluments ke baarah guna se kam ho, to kami residuary gratuity ke roop mein parivaar ko milegi."),
            ("THE EXAMPLE",
             "Rs 60,000 emoluments, floor ==Rs 7,20,000==. He received Rs 5,40,000 gratuity + Rs 90,000 pension. Residuary = ==Rs 90,000==.",
             "Worked Example (arithmetic recomputed): emoluments Rs 60,000, so twelve times is Rs 7,20,000. On retirement he received Rs 5,40,000 retirement gratuity and, before death, Rs 90,000 of pension; nothing was commuted. Total Rs 6,30,000. Deficiency = 7,20,000 - 6,30,000 = Rs 90,000, payable as residuary gratuity.",
             ORANGE,
             "Example dekho. Emoluments saath hazaar, barah guna sat lakh bees hazaar. Gratuity paanch lakh chalees hazaar mili, pension nabbe hazaar mili, total chhe lakh tees hazaar. Kami nabbe hazaar, wahi residuary gratuity hai."),
            ("45(4) & 45(5): FRACTIONS",
             "Three months or more counts as a half year (==45(4)==), and ==four years nine months== is treated as five years for gratuity (==45(5)==).",
             "Rule 45(4): in calculating qualifying service under this rule a fraction of a year equal to three months and above is treated as a completed six-monthly period. Rule 45(5): a servant with four years and nine months or more but less than five years is treated as having five years and is eligible for retirement gratuity under sub-rule (1)(a).",
             GREEN,
             "Sub-rule chaar aur paanch. Teen mahine ya zyada ka fraction aadha saal maana jayega. Aur chaar saal nau mahine ya zyada ko paanch saal maana jayega, gratuity ke liye. Ye gratuity ka near miss hai."),
            ("45(6): THE BASE",
             "Emoluments per ==Rule 31==; if pay was reduced in the last ten months, ==average emoluments==; DA on the retirement or death date counts.",
             "Rule 45(6): emoluments for gratuity are reckoned under Rule 31. First proviso: if emoluments were reduced during the last ten months, average emoluments under Rule 32 are treated as emoluments. Second proviso: dearness allowance admissible on the date of retirement or death shall also be treated as emoluments. Second proviso to sub-rule (1) rounds any fraction of a rupee to the next higher rupee.",
             PURPLE,
             "Sub-rule chhah base batata hai. Emoluments Rule thirty-one se. Agar last das mahine mein pay kam hui, to average emoluments. Aur retirement ya death date ka DA bhi emoluments mein ginega."),
        ],
        "trap": "<<TRAP:>> Residuary gratuity compares against ==12 times emoluments== and includes the ==commuted value==. It is not 12 times pension.",
        "trap_say": ("Trap ye hai: residuary gratuity barah guna emoluments se compare hoti hai, aur usme commuted value bhi judti hai. "
                     "Ye barah guna pension nahi hai."),
        "covers": ["R45-3", "LIMIT-RESID-12X", "TL-R45-3-5YR", "R45-3-EX", "R45-4", "R45-5",
                   "TL-R45-NEARMISS-4Y9M", "R45-6", "R45-6-P1", "R45-6-P2", "R45-RUPEE"],
    },
    {
        "id": "b4_14_four_gratuities",
        "part": "THE FOUR LUMP SUMS SIDE BY SIDE",
        "title": "FOUR GRATUITIES, FOUR DIFFERENT ANSWERS",
        "accent": TEAL, "badge": "COMPARISON",
        "crumb": "CHAPTER VII  •  ONE TABLE THAT SETTLES THE CONFUSION",
        "q": "There are four gratuities in these rules. How do I stop mixing them up?",
        "q_say": "Sir, in rules mein chaar gratuities hain. Inko mix hone se kaise rokein?",
        "heads": [("SERVICE", "Rule 44(2)", BLUE),
                  ("RETIREMENT", "Rule 45(1)(a)", ORANGE),
                  ("DEATH", "Rule 45(1)(b)", GREEN),
                  ("RESIDUARY", "Rule 45(3)", PURPLE)],
        "table": {
            "title": "One table, four gratuities",
            "head": ["Gratuity", "When it is paid", "Rate", "Ceiling"],
            "w": [2.0, 3.2, 4.4, 2.0],
            "rows": [
                ["Service gratuity", "Retirement with under 10 years qualifying service (Rule 44(2))",
                 "Half a month's emoluments per completed six-monthly period", "No 16.5-times cap in this sub-rule"],
                ["Retirement gratuity", "Retirement with 5 years or more and pension or service gratuity admissible (Rule 45(1)(a))",
                 "One-fourth of emoluments per completed six-monthly period; 16.5 times at 33 half-years", "Rs 25 lakh (O.M. 30.05.2024); Rule text Rs 20 lakh"],
                ["Death gratuity", "Death while in service, including suicide (Rule 45(1)(b) and 45(2))",
                 "2, 6, 12, 20 times, then half a month per half year up to 33 times", "Rs 25 lakh"],
                ["Residuary gratuity", "Death within 5 years of retirement, where 12 times emoluments is not exhausted (Rule 45(3))",
                 "The deficiency below 12 times emoluments", "Falls inside the Rs 25 lakh ceiling"],
            ],
        },
        "boxes": [
            ("SERVICE",
             "Under ten years. ==Half month== per half year. Rule 44(2). No multiple cap.",
             "Service gratuity under Rule 44(2) is the substitute for pension when qualifying service is under ten years. Half a month's emoluments per completed six-monthly period. Rule 44 itself sets no multiple cap; the Rs 25 lakh ceiling is in Rule 45 and so does not apply to this sub-rule.",
             BLUE,
             "Pehli service gratuity. Das saal se kam service par, har half year par aadha mahina. Rule forty-four ka, aur ispar sixteen point paanch guna cap nahi hai."),
            ("RETIREMENT",
             "Five years or more. ==One-fourth== per half year, 16.5 times at 33 half-years. Rule 45(1)(a).",
             "Retirement gratuity needs five years qualifying service and pension or service gratuity eligibility. One-fourth of emoluments per completed six-monthly period, maximum 16.5 times, reached at 33 half-years, and inside the Rs 25 lakh money ceiling.",
             ORANGE,
             "Doosri retirement gratuity. Paanch saal ya zyada service par, har half year par chauthai, aur tetees half-years par solah point paanch guna cap. Rule forty-five ek(a)."),
            ("DEATH",
             "Death in service. ==Slabs 2/6/12/20== then 33 times. No five-year condition. Rule 45(1)(b).",
             "Death gratuity is paid when the servant dies while in service, including by suicide under Rule 45(2). The table starts at less than one year, so no minimum service is needed. Twenty years or more gives half a month per completed six-monthly period up to 33 times.",
             GREEN,
             "Teesri death gratuity. Service ke dauran death par, slabs do, chhah, baarah, bees, phir tetees guna tak. Koi paanch saal ki shart nahi. Rule forty-five ek(b)."),
            ("RESIDUARY",
             "Death within five years of retirement. Pay the ==deficiency== below 12 times. Rule 45(3).",
             "Residuary gratuity is the forgotten one. If the servant dies within five years of retirement and the pension plus gratuity plus commuted value actually received is less than twelve times emoluments, the family gets the deficiency. It is paid in the manner of Rule 47(1).",
             PURPLE,
             "Chauthi residuary gratuity, jo log bhool jaate hain. Retirement ke paanch saal ke andar death par, agar mila hua total barah guna emoluments se kam hai, to kami parivaar ko milegi."),
        ],
        "trap": "<<TRAP:>> ==Service== gratuity has no 16.5 cap. ==Retirement== gratuity has. ==Death== gratuity has no 5 years. ==Residuary== needs a death.",
        "trap_say": ("Trap ye hai: service gratuity par cap nahi, retirement gratuity par cap hai, death gratuity mein paanch saal ki shart nahi, "
                     "aur residuary ke liye death honi chahiye."),
        "covers": ["R45-FOURTYPES", "R44-DA-EMOL"],
    },
    {
        "id": "b4_15_gratuity_scope",
        "part": "THE GRATUITY CEILING AND WHO IT COVERS",
        "title": "Rs 25 LAKH — WHICH RULE, WHICH ORDER, WHICH EMPLOYEE",
        "accent": AMBER, "badge": "O.M. 30.05.2024",
        "crumb": "CHAPTER VII  •  LAYER 3 (EXECUTIVE ORDERS)",
        "q": "The Rule says twenty lakh but the office pays twenty-five. Which document wins?",
        "q_say": "Sir, Rule mein bees lakh likha hai lekin office pachchees lakh deta hai. Kaun sa document chalta hai?",
        "heads": [("RULE TEXT", "Rs 20 lakh", BLUE),
                  ("O.M. 30.05.2024", "Rs 25 lakh from 01.01.2024", ORANGE),
                  ("COVERAGE", "Who is inside", GREEN),
                  ("AMENDMENT", "Still awaited", PURPLE)],
        "boxes": [
            ("THE TWO FIGURES",
             "Rule 45 first proviso reads ==twenty lakh==. The O.M. of ==30.05.2024== raised it to ==twenty-five lakh== with effect from ==01.01.2024==.",
             "Rule 45(1) first proviso: the amount of retirement gratuity or death gratuity shall in no case exceed twenty lakh rupees. DoPPW O.M. F.No. 28/03/2024-P&PW(B)/Gratuity/9559 dated 30.05.2024 raised the ceiling to Rs 25 lakh with effect from 01.01.2024 (S5). Up to October 2026 no Gazette amendment of Rule 45 was found, so the Rule still prints twenty lakh while the operative figure is twenty-five.",
             BLUE,
             "Rule mein bees lakh likha hai. Lekin tirish May do hazaar chaubees ke O.M. ne pachchees lakh kar diya, pehli January do hazaar chaubees se. Rule amendment abhi tak nahi aaya, isliye aaj pachchees lakh hi chalta hai."),
            ("HOW TO QUOTE",
             "Quote the ==principle== from the Rule and the ==figure== from the O.M., with its ==number and date==. Never quote a figure without its order.",
             "Answer-writing rule: state the Rule for the proposition (Rule 45(1) first proviso caps gratuity) and then the order that moved the number (O.M. dated 30.05.2024, File No. 28/03/2024-P&PW(B)/Gratuity/9559). A bare figure with no date is an incomplete answer, because the ceiling has moved more than once.",
             ORANGE,
             "Answer likhne ka tareeka: principle Rule se lo, figure O.M. se lo, aur O.M. ka number aur date zaroor likho. Sirf figure likhna adhoora answer hai, kyunki ceiling pehle bhi badalti rahi hai."),
            ("WHO IS COVERED",
             "Retirement and death gratuity under ==Rule 45==. Not the ==service gratuity== under Rule 44(2), which has no money ceiling of its own.",
             "The Rs 25 lakh ceiling is in Rule 45, so it applies to retirement gratuity under Rule 45(1)(a) and death gratuity under Rule 45(1)(b), and to residuary gratuity which is worked out inside that rule. Service gratuity under Rule 44(2) is not governed by Rule 45 and carries no statutory money ceiling. NPS employees are outside these Rules and are governed by the CCS (Payment of Gratuity under NPS) Rules, 2021, G.S.R. 258(E).",
             GREEN,
             "Ceiling Rule forty-five ki hai. Isliye retirement gratuity aur death gratuity par lagti hai, aur residuary gratuity bhi isi ke andar hai. Rule forty-four ki service gratuity par apni money ceiling nahi hai. NPS wale in rules mein nahi aate."),
            ("THE GAP",
             "Two amendments are still ==awaited==: the ceiling, and the ==marital discord== order of 01.01.2024. Teach them as orders, not as Rule numbers.",
             "Both the Rs 25 lakh ceiling and the marital-discord family pension provision rest on executive orders that say the Rules will be amended separately. No such Gazette notification was found up to October 2026. For the exam, cite the O.M.; for the office, follow the O.M. because that is what the Pay and Accounts Office applies.",
             PURPLE,
             "Do amendments abhi baaki hain. Ek pachchees lakh ki ceiling, doosri pehli January do hazaar chaubees ka marital discord order. Dono O.M. par chal rahe hain. Exam mein O.M. cite karo, Rule number mat banao."),
        ],
        "trap": "<<TRAP:>> Never write ==Rs 25 lakh under Rule 45==. Write ==Rule 45 read with the O.M. dated 30.05.2024==.",
        "trap_say": ("Trap ye hai: pachchees lakh ko Rule forty-five ke andar mat likho. "
                     "Likho Rule forty-five read with O.M. thirty May do hazaar chaubees."),
        "covers": ["OM-24.10.2025-COVERAGE", "OM-24.10.2025-ELIG", "NPSG-258E-2025", "LIMIT-GRATUITY-CEILING",
                   "OM-30.05.2024-GRAT", "MARITAL-CODIFIED"],
    },
    {
        "id": "b4_16_family_definition",
        "part": "RULE 45(6) EXPLANATION • WHO IS FAMILY",
        "title": "THE ELEVEN-CLAUSE DEFINITION OF FAMILY (RULES 45 TO 49)",
        "accent": PURPLE, "badge": "RULE 45(6) EXPL",
        "crumb": "CHAPTER VII  •  THE KEY THAT OPENS RULES 46 TO 49",
        "q": "Who exactly counts as family for gratuity, and why does the order of the list matter?",
        "q_say": "Sir, gratuity ke liye family mein kaun kaun aata hai, aur list ka order kyun matter karta hai?",
        "heads": [("GROUP 1", "Clauses (i) to (v)", BLUE),
                  ("GROUP 2", "Clauses (vi) to (xi)", ORANGE),
                  ("EQUAL SHARES", "Inside each group", GREEN),
                  ("NO CROSSING", "Group 1 shuts Group 2", PURPLE)],
        "table": {
            "title": "Rule 45(6) Explanation — family, for Rules 45, 46, 47, 48 and 49",
            "head": ["Clause", "Member of the family", "Group"],
            "w": [1.1, 9.2, 1.4],
            "rows": [
                ["(i)", "Wife or wives, including a judicially separated wife", "1"],
                ["(ii)", "Husband, including a judicially separated husband", "1"],
                ["(iii)", "Sons, including stepsons and adopted sons", "1"],
                ["(iv)", "Unmarried daughters, including step and adopted", "1"],
                ["(v)", "Widowed or divorced daughters, including step and adopted", "1"],
                ["(vi)", "Father, including adoptive parents where personal law permits", "2"],
                ["(vii)", "Mother, including adoptive parents where personal law permits", "2"],
                ["(viii)", "Brothers: disabled any age; others below eighteen", "2"],
                ["(ix)", "Unmarried, widowed and divorced sisters, including step", "2"],
                ["(x)", "Married daughters", "2"],
                ["(xi)", "Children of a pre-deceased son", "2"],
            ],
        },
        "boxes": [
            ("GROUP 1",
             "Clauses ==(i) to (v)==: spouse, sons, unmarried daughters, widowed or divorced daughters. They take ==equal shares== and shut out Group 2.",
             "Rule 45(6) Explanation clauses (i) to (v) form the first group for Rule 47(1)(b)(i). If one or more of them survives, the whole gratuity is divided among them in equal shares, and clauses (vi) to (xi) get nothing. Note that sons carry no age limit in this definition, unlike family pension under Rule 50(9).",
             BLUE,
             "Group one mein clause ek se paanch: spouse, bete, unmarried betiyan, aur widowed ya divorced betiyan. Agar inme se koi bhi zinda hai to poori gratuity inme barabar bantegi, aur Group two ko kuch nahi milega."),
            ("GROUP 2",
             "Clauses ==(vi) to (xi)==: parents, brothers, sisters, ==married daughters==, children of a pre-deceased son. Only if Group 1 is empty.",
             "Rule 45(6) Explanation clauses (vi) to (xi) form the second group for Rule 47(1)(b)(ii). They are reached only when no member of Group 1 survives. Married daughters sit in clause (x), so a married daughter shares with grandparents and siblings but never with the widow.",
             ORANGE,
             "Group two mein clause chhah se gyarah: maa baap, bhai, behen, married betiyan, aur pre-deceased bete ke bachche. Ye tabhi milte hain jab Group one bilkul khali ho. Married beti clause das mein hai."),
            ("THE TWO TRAPS",
             "Sons have ==no age 25 limit== here, and brothers are ==under 18== only in the second limb of clause (viii).",
             "Trap one: the age of twenty-five belongs to family pension under Rule 50(9), not to gratuity; a son of any age is in clause (iii) for Rule 47. Trap two: clause (viii) has two limbs - a brother with a mental or physical disability without any limit of age, and any other brother below eighteen.",
             GREEN,
             "Do traps. Pehla: pachchees saal ki age family pension ki hai, gratuity ki nahi, yahan bete ki koi age limit nahi. Doosra: clause aath ke do hisse hain, disability wale bhai ki koi age limit nahi, baaki bhai atharah se kam."),
            ("WHY IT MATTERS",
             "This one list decides ==Rule 47==, ==Rule 48== and ==Rule 49==. Get the list wrong and three rules collapse.",
             "The Explanation says it applies for the purposes of Rule 45 and Rules 46, 47, 48 and 49. So the same eleven clauses decide who may be nominated (Rule 46), who receives (Rule 47), who can be debarred on a murder charge (Rule 48) and whether the gratuity lapses for want of family (Rule 49). Family pension has its own, different list.",
             PURPLE,
             "Ye ek list Rule forty-seven, forty-eight aur forty-nine, teeno decide karti hai. Explanation khud kehti hai ki ye Rule forty-five ke saath forty-six se forty-nine ke liye hai. Family pension ki list alag hai."),
        ],
        "trap": "<<TRAP:>> ==Married daughters== are family (clause x), but only in ==Group 2==. Sons here have ==no age limit==.",
        "trap_say": ("Trap ye hai: married betiyan family mein aati hain, clause das mein, lekin sirf Group two mein. "
                     "Aur yahan beton ki koi age limit nahi hai."),
        "covers": ["R45-EXPL-FAMILY", "R45-EXPL-G1", "R45-EXPL-G2", "R45-EXPL-G3"],
    },
    {
        "id": "b4_17_rule46_nomination",
        "part": "RULE 46(1) TO (4) • NOMINATION",
        "title": "FORM 3 — HOW A SERVANT NOMINATES FOR HIS GRATUITY",
        "accent": BLUE, "badge": "RULE 46(1)-(4)",
        "crumb": "CHAPTER VII  •  NOMINATION AND ALTERNATE NOMINATION",
        "q": "Who can be nominated, what shares must be stated, and who is the alternate nominee?",
        "q_say": "Sir, nomination kisse ki jaati hai, share likhna zaroori hai kya, aur alternate nominee kaun hota hai?",
        "heads": [("FORM 3", "The nomination form", BLUE),
                  ("FAMILY FIRST", "If family exists", ORANGE),
                  ("SHARES", "Must cover the whole", GREEN),
                  ("ALTERNATE", "Second line", PURPLE)],
        "boxes": [
            ("46(1): FORM 3",
             "On ==initial appointment== he shall nominate in ==Form 3==, conferring the right to receive ==retirement and death gratuity==.",
             "Rule 46(1): a Government servant shall, on his initial appointment in a service or post, make a nomination in Form 3 conferring on one or more persons the right to receive the retirement gratuity and death gratuity payable under Rule 45. Nomination covers gratuity only; family pension is not nominated, it follows Rule 50.",
             BLUE,
             "Rule forty-six ek: initial appointment par hi Form three mein nomination dena hota hai. Isse retirement gratuity aur death gratuity receive karne ka haq milta hai. Dhyaan do, nomination sirf gratuity ki hoti hai, family pension ki nahi."),
            ("46(2): WHO",
             "If he has a ==family==, nominate any member or members of that family. If he has ==no family==, he may nominate any person or body of individuals.",
             "Rule 46(2)(i): where the servant has one or more members of family as in the Rule 45(6) Explanation, the nomination shall be in favour of any member or members of his family. (ii) Where he has no family, the nomination may be in favour of a person or persons, or a body of individuals, whether incorporated or not.",
             ORANGE,
             "Sub-rule do: agar family hai to family ke member ya members ke naam par nomination. Agar family nahi hai to kisi bhi person ya body of individuals ke naam par ho sakti hai."),
            ("46(3): SHARES",
             "With more than one nominee, he must ==specify the share== of each, in a way that covers the ==entire gratuity==.",
             "Rule 46(3): if a servant nominates more than one person under sub-rule (2), he shall specify in the nomination the share payable to each nominee, in such manner as to cover the entire gratuity. A nomination that leaves a gap is defective, and the gap is filled by Rule 47(2) rather than by the nomination.",
             GREEN,
             "Sub-rule teen: ek se zyada nominee ho to har ek ka share likhna zaroori hai, aur share poore gratuity ko cover karna chahiye. Agar gap chhoda to wo gap Rule forty-seven do bharega, nomination nahi."),
            ("46(4): ALTERNATE",
             "He may name an ==alternate== for a nominee who dies first, subject to two provisos: normally the alternate must be ==family==; with only one family member, anyone may be named.",
             "Rule 46(4)(i): the nomination may provide that for a specified nominee who predeceases the servant, or dies after the servant's death but before receiving payment, the right passes to such other person as specified. First proviso: if the servant has a family of more than one member, the person specified shall not be a person other than a member of his family. Second proviso: where he has only one family member and the nomination is in his favour, he may nominate any person or body of individuals as alternate nominee. (ii) The nomination may provide that it becomes invalid on the happening of a stated contingency.",
             PURPLE,
             "Sub-rule chaar alternate nominee deta hai. Agar nominee pehle mar jaye to uski jagah kisi aur ka naam. Pehla proviso kehta hai family ek se zyada ho to alternate bhi family se hi ho. Doosra proviso kehta hai family mein sirf ek member ho to koi bhi alternate ho sakta hai."),
        ],
        "trap": "<<TRAP:>> Nomination covers ==gratuity only==. There is no nomination for ==family pension== — Rule 50 has its own list.",
        "trap_say": ("Trap ye hai: nomination sirf gratuity ki hoti hai. Family pension ki koi nomination nahi hoti, "
                     "uske liye Rule fifty ki apni list hai."),
        "covers": ["R46-1", "FORM-3", "R46-2", "R46-3", "R46-4", "R46-4-P1", "R46-4-P2", "R46-4-II"],
    },
    {
        "id": "b4_18_rule46_validity",
        "part": "RULE 46(5) TO (10) • WHEN A NOMINATION DIES",
        "title": "CANCELLATION, MARRIAGE, COUNTERSIGNATURE AND THE DATE IT BITES",
        "accent": AMBER, "badge": "RULE 46(5)-(10)",
        "crumb": "CHAPTER VII  •  THE FIVE WAYS A NOMINATION FAILS",
        "q": "When does a nomination become invalid, and from which date does a valid one operate?",
        "q_say": "Sir, nomination kab invalid ho jaati hai, aur valid nomination kis date se chalti hai?",
        "heads": [("ACQUIRING FAMILY", "46(5)(a)", BLUE),
                  ("ONE MEMBER", "46(5)(b)", ORANGE),
                  ("MARRIAGE", "46(6)", GREEN),
                  ("HEAD OF OFFICE", "46(9) and 46(10)", PURPLE)],
        "boxes": [
            ("46(5): THE TWO FAILURES",
             "(a) A non-family nomination dies the moment he ==acquires a family==. (b) An ==alternate== nomination dies when a second family member appears, but the family nomination survives.",
             "Rule 46(5)(a): where the servant had no family when he made the nomination, a nomination in favour of a person or body of individuals becomes invalid on his subsequently acquiring a family. (b) Where he had only one family member and nominated him, and later acquires an additional family member, the alternate nomination under the second proviso to Rule 46(4)(i) becomes invalid, but the nomination in favour of the family member is not affected.",
             BLUE,
             "Sub-rule paanch ke do hisse. Pehla: family nahi thi to bahar wale ko nomination di; family aa gayi to wo nomination khatam. Doosra: family mein ek hi member tha, alternate diya; doosra member aaya to alternate khatam, lekin family wali nomination chalti rahegi."),
            ("46(6): MARRIAGE",
             "An ==unmarried== servant's nomination in favour of a family member does ==not== die on marriage, unless he cancels it and files a fresh one.",
             "Rule 46(6): a nomination made by an unmarried Government servant, under clause (i) of sub-rule (2), in favour of any member of his family shall not become invalid on his or her marriage, unless the servant cancels the earlier nomination and files a fresh nomination under sub-rule (7). So marriage is not an automatic cancellation.",
             ORANGE,
             "Sub-rule chhah: unmarried servant ne family member ke naam par nomination di thi, to shaadi hone se wo apne aap khatam nahi hoti. Haan, agar wo khud cancel karke nayi nomination de, to baat alag hai."),
            ("46(7) & 46(8): CHANGE",
             "He may cancel at any time by ==notice in writing== to the Head of Office, and must send a ==fresh nomination== with it. Same duty when a nominee dies.",
             "Rule 46(7): a servant may at any time cancel a nomination by sending a notice in writing to the Head of Office, provided that he sends a fresh nomination along with the notice. Rule 46(8): immediately on the death of a nominee for whom no special provision was made under Rule 46(4)(i), or on the occurrence of an event making the nomination invalid under Rule 46(4)(ii), the servant shall send a written notice cancelling the nomination together with a fresh nomination.",
             GREEN,
             "Sub-rule saat aur aath: cancellation possible hai, lekin notice ke saath nayi nomination bhi bhejni padegi. Aur agar nominee mar jaye, to bhi notice aur nayi nomination bhejni hoti hai."),
            ("46(9) & 46(10): OFFICE",
             "The Head of Office ==verifies and countersigns== with the date of receipt, makes a service-book entry, returns a copy; it takes effect ==from the date of receipt==.",
             "Rule 46(9)(a): every nomination and every notice of cancellation shall be sent to the Head of Office. (b) He shall verify that it accords with the rule and is in favour of family where a family exists, then countersign indicating the date of receipt and keep it in custody; proviso: he may authorise subordinate Gazetted Officers to countersign nominations of non-gazetted servants. (c) An entry shall be made in the service book. (d) A duly signed copy shall be returned to the servant. Rule 46(10): every nomination and cancellation takes effect, to the extent valid, from the date it is received by the Head of Office (R46-EFFECTIVE).",
             PURPLE,
             "Sub-rule nau aur das office ka kaam. Head of Office check karke countersign karta hai, receipt date likhta hai, service book mein entry karta hai, aur ek copy servant ko wapas deta hai. Effect receipt date se hota hai, file par sign karne ki date se nahi."),
        ],
        "trap": "<<TRAP:>> A nomination takes effect from the ==date the Head of Office receives it==, not the date on the form.",
        "trap_say": ("Trap ye hai: nomination ka effect us date se hota hai jab Head of Office ko milti hai, "
                     "form par likhi date se nahi."),
        "covers": ["R46-5A", "R46-5B", "R46-6", "R46-7", "R46-8", "R46-9A", "R46-9B", "R46-9C", "R46-9D", "R46-10", "R46-EFFECTIVE"],
    },
    {
        "id": "b4_19_rule47_who",
        "part": "RULE 47(1) • WHO RECEIVES THE GRATUITY",
        "title": "RULE 47(1) — NOMINATION FIRST, THEN THE TWO FAMILY GROUPS",
        "accent": GREEN, "badge": "RULE 47(1)",
        "crumb": "CHAPTER VII  •  THE PAYMENT LADDER",
        "q": "If there is no nomination, who is paid the gratuity and in what shares?",
        "q_say": "Sir, nomination na ho to gratuity kisko milegi, aur share kaise bantenge?",
        "heads": [("NOMINATION", "Step one", BLUE),
                  ("GROUP 1", "Clauses (i) to (v)", ORANGE),
                  ("GROUP 2", "Only if Group 1 is empty", GREEN),
                  ("EQUAL SHARES", "Within the group", PURPLE)],
        "boxes": [
            ("47(1)(a): NOMINEE",
             "The gratuity goes first to the person or persons on whom the ==nomination== under Rule 46 conferred the right.",
             "Rule 47(1)(a): the gratuity payable under Rule 45 shall be paid to the person or persons on whom the right to receive it is conferred by a nomination under Rule 46. The nomination speaks first; the family list is only a fallback.",
             BLUE,
             "Rule forty-seven ek(a): gratuity pehle un logon ko jayegi jinke naam Rule forty-six ki nomination ne haq diya hai. Nomination pehle bolti hai, family list baad mein aati hai."),
            ("47(1)(b)(i): GROUP 1",
             "No nomination, or it does not subsist: pay all members in clauses ==(i) to (v)== in ==equal shares==.",
             "Rule 47(1)(b)(i): where there is no nomination, or the nomination does not subsist, if there are one or more surviving members of the family in clauses (i), (ii), (iii), (iv) and (v) of the Rule 45(6) Explanation, the gratuity is paid to all such members in equal shares. Presence of even one such member excludes the whole of Group 2.",
             ORANGE,
             "Agar nomination nahi hai ya khatam ho gayi, to pehle Group one dekho: clause ek se paanch. Inme se jo bhi zinda hain, sabko barabar hissa. Ek bhi zinda ho to Group two poora bahar."),
            ("47(1)(b)(ii): GROUP 2",
             "Only if no Group 1 member survives: pay clauses ==(vi) to (xi)== in equal shares.",
             "Rule 47(1)(b)(ii): if there are no such surviving members as in sub-clause (i), but there are one or more members in clauses (vi), (vii), (viii), (ix), (x) and (xi), the gratuity is paid to all such members in equal shares. Parents, brothers, sisters, married daughters and children of a pre-deceased son share equally among themselves.",
             GREEN,
             "Group two tabhi aata hai jab Group one ka koi member zinda na ho. Phir clause chhah se gyarah wale, sab barabar hissa. Maa baap, bhai, behen, married betiyan, aur pre-deceased bete ke bachche."),
            ("THE KEY",
             "==Group 1 blocks Group 2 entirely==. There is no mixing and no ladder inside a group.",
             "Rule 47(1)(b) is a two-step ladder, not a ladder of individuals: the whole of Group 1 takes equally, and only if it is empty does the whole of Group 2 take equally. Any suggestion that a parent gets a smaller share than a widow, or that a brother ranks after a mother, is wrong; inside a group the shares are equal.",
             PURPLE,
             "Yaad rakho, Group one Group two ko poora block karta hai. Andar koi ladder nahi hai. Sab barabar. Ye kehna galat hai ki maa ko kam ya bhai ko behen ke baad milta hai."),
        ],
        "trap": "<<TRAP:>> One surviving ==Group 1== member pays the whole gratuity to Group 1. Group 2 is ==not== a residual sharing group.",
        "trap_say": ("Trap ye hai: Group one ka ek bhi member zinda ho to poori gratuity Group one mein bantegi. "
                     "Group two residual sharing group nahi hai."),
        "covers": ["R47-1A", "R47-1B", "R47-GROUP1", "R47-GROUP2", "R47-STRICT"],
    },
    {
        "id": "b4_20_rule47_shares",
        "part": "RULE 47(2) AND (3) • FAILED NOMINEE, LATE DEATH",
        "title": "THE PRE-DECEASED NOMINEE AND THE UNPAID RETIREMENT GRATUITY",
        "accent": BLUE, "badge": "RULE 47(2)-(3)",
        "crumb": "CHAPTER VII  •  TWO QUIET SUB-RULES",
        "q": "What happens to a dead nominee's share, and what if he dies after retirement without receiving the gratuity?",
        "q_say": "Sir, nominee ka share kya hota hai agar wo pehle mar jaye, aur retirement ke baad gratuity na mili ho to?",
        "heads": [("PRE-DECEASE", "No alternate named", BLUE),
                  ("ALIVE ON DEATH", "The test date", ORANGE),
                  ("AFTER RETIREMENT", "Unpaid gratuity", GREEN),
                  ("SAME LADDER", "Rule 47(1)", PURPLE)],
        "boxes": [
            ("47(2): THE SHARE",
             "If a nominee pre-deceases and no alternate was named, his share is divided ==equally among the other eligible family members alive on the date of death==.",
             "Rule 47(2): where a nominee pre-deceases the servant and the right has not passed to another person under Rule 46(4), or the nomination does not subsist or has become invalid, the share of gratuity in respect of that nominee shall be disbursed equally to all other members of the family who were eligible and alive on the date of death of the servant, including the members in whose favour a nomination was made for the remaining gratuity.",
             BLUE,
             "Sub-rule do: agar nominee pehle mar gaya aur alternate nahi tha, to uska hissa baaki eligible family members mein barabar bantega. Test date hai servant ki death ki date, aaj ki date nahi."),
            ("THE DATE TEST",
             "Eligibility is tested on the ==date of the servant's death==. A member who becomes eligible later is not brought in.",
             "Rule 47(2) uses the words eligible and alive on the date of death of the Government servant. So a child born after the death, or a person who becomes a family member later, does not share in the pre-deceased nominee's portion. This is the narrow point the source material left unresolved; the Rule text is explicit.",
             ORANGE,
             "Sub-rule do mein likha hai eligible and alive on the date of death. Yaani death ke baad paida hone wala bachcha ya baad mein family member bana, wo is hisse mein nahi aata. Rule ka text yahan bilkul clear hai."),
            ("47(3): AFTER RETIREMENT",
             "If he dies after retirement ==without receiving== the retirement gratuity, it is paid to the family in the manner of ==Rule 47(1)==.",
             "Rule 47(3): where a servant dies after retirement without receiving the retirement gratuity admissible under Rule 45(1), the gratuity shall be disbursed to the family in the manner indicated in Rule 47(1). The same nomination-first, then Group 1, then Group 2 ladder applies.",
             GREEN,
             "Sub-rule teen: agar retirement ke baad gratuity receive kiye bina death ho gayi, to wo gratuity parivaar ko Rule forty-seven ek ke tareeke se milegi. Wahi ladder, pehle nomination, phir Group one, phir Group two."),
            ("WHY IT IS ASKED",
             "It links ==Rule 46(4)== (alternate), ==Rule 47(2)== (failed nominee) and ==Rule 48== (murder charge) into one chain.",
             "These three provisions are examined together. Rule 46(4) lets the servant plug the gap in advance; Rule 47(2) fills the gap if he did not; Rule 48 suspends the share of a person charged with the servant's murder. All three operate on the same share, so a single fact pattern can touch all of them.",
             PURPLE,
             "Teen provisions saath padhaye jaate hain. Rule forty-six chaar pehle se alternate de deta hai, Rule forty-seven do gap bharta hai, aur Rule forty-eight murder charge wale ka hissa rok deta hai. Teeno ek hi hisse par kaam karte hain."),
        ],
        "trap": "<<TRAP:>> The date for Rule 47(2) is the ==date of death==, not the date of the claim. A later-born child does not enter.",
        "trap_say": ("Trap ye hai: Rule forty-seven do ki date death ki date hai, claim ki date nahi. "
                     "Baad mein paida hone wala bachcha is hisse mein nahi aata."),
        "covers": ["R47-2", "R47-2-DATETEST", "R47-3"],
    },
    {
        "id": "b4_21_rule47_minors",
        "part": "RULE 47(4) TO (8) • MINORS, MARRIAGE AND SEPARATE CLAIMS",
        "title": "THE GUARDIAN, THE 20 PER CENT RULE AND FORM 9",
        "accent": GREEN, "badge": "RULE 47(4)-(8)",
        "crumb": "CHAPTER VII  •  THE SUB-RULES THAT WERE MISSING",
        "q": "How is a minor's share paid, and what if one family member has not filed a claim?",
        "q_say": "Sir, minor ka hissa kaise milta hai, aur agar ek member ne claim nahi diya to kya hota hai?",
        "heads": [("MARRIAGE", "47(4)", BLUE),
                  ("GUARDIAN", "47(5) and 47(6)", ORANGE),
                  ("20 PER CENT", "47(7)", GREEN),
                  ("FORM 9", "47(8)", PURPLE)],
        "boxes": [
            ("47(4): LATER EVENTS",
             "A female member marrying or re-marrying, or a brother turning ==18 after the death but before receiving== the share, does ==not== lose it.",
             "Rule 47(4): the right of a female member of the family, or of a brother, of a servant who dies while in service or after retirement, to receive the share of gratuity shall not be affected if the female member marries or re-marries, or the brother attains the age of eighteen years, after the death of the servant and before receiving the share. The right crystallises at death.",
             BLUE,
             "Sub-rule chaar: agar servant ki death ke baad, hissa milne se pehle, female member ki shaadi ho jaye ya bhai atharah ka ho jaye, to haq khatam nahi hota. Haq death ke waqt hi ban jaata hai."),
            ("47(5) & (6): GUARDIAN",
             "A minor's share is paid to the ==guardian==. First the ==natural guardian==; in his absence, the person with a ==certificate of guardianship==.",
             "Rule 47(5): where gratuity is granted to a minor member, it shall be payable to the guardian on behalf of the minor. Rule 47(6): payment of the minor's share shall be made to the natural guardian, if any; in the absence of a natural guardian, to the person who furnishes a certificate of guardianship.",
             ORANGE,
             "Sub-rule paanch aur chhah: minor ka hissa guardian ko milega. Pehle natural guardian. Natural guardian na ho to us person ko jo guardianship certificate deta hai."),
            ("47(7): THE 20 PER CENT",
             "Without a natural guardian, up to ==20 per cent of the minor's share== may be paid on an ==Indemnity Bond in Format 7==; the balance only on the guardianship certificate.",
             "Rule 47(7): in the absence of a natural guardian, payment of an amount not exceeding twenty per cent of the minor's share of gratuity may be made to the guardian without production of a guardianship certificate, but on production of an indemnity bond in Format 7; the balance may be paid to the guardian on production of the certificate of guardianship. This is a hardship clause, not a general permission.",
             GREEN,
             "Sub-rule saat: natural guardian na ho to minor ke hisse ka maximum bees percent guardianship certificate ke bina diya ja sakta hai, aur uske liye Format seven ka indemnity bond chahiye. Baaki paisa certificate milne par hi."),
            ("47(8): FORM 9",
             "If one eligible member has not filed a claim in ==Form 9==, the others' cases are ==processed without waiting== for him.",
             "Rule 47(8): if there is more than one family member eligible for gratuity and one has not submitted his claim in Form 9, the case for sanction to him may be processed after his claim is received, and the cases of the other eligible members may be processed without linking them to the case of the member who has not submitted the claim.",
             PURPLE,
             "Sub-rule aath: agar ek eligible member ne Form nine mein claim nahi diya, to baaki members ke case uske intezaar mein nahi rukenge. Sabka case alag chalta hai."),
        ],
        "trap": "<<TRAP:>> The ==20 per cent== limit is only for the absence of a *natural* guardian, and only on ==Format 7==. It is not a general advance.",
        "trap_say": ("Trap ye hai: bees percent ki limit sirf natural guardian na hone par hai, aur Format seven ke indemnity bond par. "
                     "Ye general advance nahi hai."),
        "covers": ["R47-4", "R47-5", "R47-6", "R47-7", "FORMAT-7", "R47-8", "FORM-9"],
    },
    {
        "id": "b4_22_rules48_49",
        "part": "RULES 48 AND 49 • MURDER CHARGE AND LAPSE",
        "title": "SUSPEND THE SHARE, OR LAPSE THE GRATUITY",
        "accent": RED, "badge": "RULES 48-49",
        "crumb": "CHAPTER VII  •  THE TWO ENDINGS",
        "q": "What happens to the share of a person charged with murder, and when does gratuity lapse?",
        "q_say": "Sir, murder charge wale ka hissa kya hota hai, aur gratuity kab lapse ho jaati hai?",
        "heads": [("MURDER CHARGE", "Suspended", BLUE),
                  ("CONVICTION", "Debarred", ORANGE),
                  ("ACQUITTAL", "Paid to him", GREEN),
                  ("NO FAMILY", "Lapses to Government", PURPLE)],
        "boxes": [
            ("48(1): SUSPEND",
             "A person eligible under Rule 47 who is charged with ==murdering the servant== or ==abetting== it has his claim ==suspended== till the criminal case ends.",
             "Rule 48(1): if a person eligible to receive gratuity under Rule 47 on the death of a servant in service is charged with the offence of murdering the servant, or of abetting in the commission of such an offence, his claim to receive his share shall remain suspended till the conclusion of the criminal proceedings. Suspension is not forfeiture.",
             BLUE,
             "Rule forty-eight ek: jo person Rule forty-seven ke under eligible hai, agar uspar servant ke murder ya abetment ka charge hai, to uska claim criminal case khatam hone tak suspend rahega. Suspend ka matlab forfeit nahi."),
            ("48(2): THE TWO ENDINGS",
             "(a) ==Convicted==: debarred, and the share goes to the other eligible members. (b) ==Acquitted==: the share is paid to him.",
             "Rule 48(2)(a): if convicted for the murder or abetting the murder, he shall be debarred from receiving his share, which shall be payable to other eligible members of the family, if any. (b) If acquitted, his share of gratuity shall be payable to him. There is no discretion: the criminal finding decides.",
             ORANGE,
             "Sub-rule do ke do endings. Conviction ho to debar, aur hissa baaki eligible members ko. Acquittal ho to hissa usi ko milega. Yahan koi discretion nahi, criminal case ka result decide karta hai."),
            ("48(3) & EXPLANATION",
             "It also covers the ==unpaid gratuity== after retirement, and ==abetting suicide== is inside the charge.",
             "Rule 48(3): sub-rules (1) and (2) also apply to the undisbursed gratuity referred to in Rule 47(3), so a death after retirement is covered. Explanation: the charge of murder or abetting in the murder includes the charge of abetting death by suicide. That is why Rule 45(2) and Rule 48 live together without conflict.",
             GREEN,
             "Sub-rule teen: ye Rule forty-seven teen ki undisbursed gratuity par bhi lagta hai, yaani retirement ke baad ki death par bhi. Explanation kehti hai suicide ke liye abetment bhi isme aata hai. Isliye Rule forty-five do aur Rule forty-eight mein takraav nahi hai."),
            ("49: LAPSE",
             "If he dies leaving ==no family== and no subsisting nomination, the gratuity ==lapses to the Government== — unless a ==Succession Certificate== is produced.",
             "Rule 49: where a servant dies while in service or after retirement without receiving the gratuity and leaves behind no family and either has made no nomination or the nomination does not subsist, the retirement or death gratuity shall lapse to the Government. Proviso: it shall be payable to the person in whose favour a Succession Certificate in respect of the gratuity has been granted by a court of law.",
             PURPLE,
             "Rule forty-nine: agar death par koi family nahi aur koi subsisting nomination nahi, to gratuity Government ko lapse ho jaati hai. Lekin proviso kehta hai agar court se Succession Certificate mila hai to us person ko milegi."),
        ],
        "trap": "<<TRAP:>> Rule 48 ==suspends== the share, Rule 49 ==lapses== the gratuity. One waits for a verdict; the other waits for a Succession Certificate.",
        "trap_say": ("Trap ye hai: Rule forty-eight hissa suspend karta hai, Rule forty-nine gratuity lapse karta hai. "
                     "Ek verdict ka intezaar karta hai, doosra Succession Certificate ka."),
        "covers": ["R48-1", "R48-2A", "R48-2B", "R48-3", "R48-EXPL", "R49-1", "R49-SUCC", "R49-SCOPE"],
    },
    {
        "id": "b4_23_rule50_1",
        "part": "RULE 50(1) • THE THREE GATEWAYS TO FAMILY PENSION",
        "title": "RULE 50(1) — WHEN DOES FAMILY PENSION BECOME PAYABLE?",
        "accent": GREEN, "badge": "RULE 50(1)",
        "crumb": "CHAPTER VIII  •  FAMILY PENSION BEGINS",
        "q": "Who is entitled to family pension, and from which date does it start?",
        "q_say": "Sir, family pension kisko milti hai, aur kis date se shuru hoti hai?",
        "compare": {"cols": [
            ("AFTER 1 YEAR", "Continuous service of ==one year==. No medical test needed. Rate under Rule 50(2).", BLUE),
            ("BEFORE 1 YEAR", "Only if he was ==medically examined and declared fit== before appointment.", ORANGE),
            ("AFTER RETIREMENT", "He was, on the date of death, ==drawing pension== or compassionate allowance.", GREEN),
            ("START DATE", "==The day after death==, in all three gateways. No waiting period here.", PURPLE),
        ]},
        "boxes": [
            ("GATEWAY (i)",
             "Death ==after one year of continuous service==. Nothing else is needed.",
             "Rule 50(1)(i): where a Government servant dies after completion of one year of continuous service, the family of the deceased shall be entitled to family pension from the date following the date of death. One year of continuous service is the ordinary gateway, and it does not require any medical examination.",
             BLUE,
             "Pehla gateway: ek saal ki continuous service ke baad death. Isme koi medical examination nahi chahiye. Family pension death ke agle din se shuru hogi."),
            ("GATEWAY (ii)",
             "Death ==before one year==, if he had been ==medically examined and declared fit== before appointment.",
             "Rule 50(1)(ii): where death occurs before completion of one year of continuous service, family pension is payable provided the deceased servant, immediately prior to his appointment, was examined by the appropriate medical authority and declared fit for Government service. The rule protects families of short-service employees who entered through the medical gate.",
             ORANGE,
             "Doosra gateway: ek saal se pehle death, lekin shart ye hai ki appointment se pehle medical examination hua ho aur fit declare kiya gaya ho. Isse chhoti service wale employees ke parivaar bach jaate hain."),
            ("GATEWAY (iii)",
             "Death ==after retirement==, where he was on the date of death ==in receipt of pension or compassionate allowance==.",
             "Rule 50(1)(iii): where the servant dies after retirement and was, on the date of death, in receipt of a pension or compassionate allowance referred to in these rules, the family is entitled to family pension. A retired servant who had commuted part of his pension is still in receipt of pension.",
             GREEN,
             "Teesra gateway: retirement ke baad death, aur death ki date par pension ya compassionate allowance mil rahi ho. Commutation kiya ho to bhi pension to mil rahi hai, isliye ye gateway khulta hai."),
            ("THE DATE",
             "From the ==date following the date of death==, in all three gateways.",
             "Rule 50(1): in all three cases the family pension is payable from the date following the date of death of the Government servant or the retired Government servant. The day of death is not a pension day, and there is no waiting period, unlike Rule 51 where the six-month bar applies before payment.",
             PURPLE,
             "Start date: teeno gateway mein death ke agle din se. Death wala din pension ka din nahi hai. Aur yahan Rule fifty-one jaisa chhah mahine ka payment bar nahi hai."),
        ],
        "trap": "<<TRAP:>> ==One year== of continuous service is enough for family pension, though ==ten years== is needed for pension. Two different gates.",
        "trap_say": ("Trap ye hai: family pension ke liye ek saal continuous service kaafi hai, jabki pension ke liye das saal chahiye. "
                     "Do alag gates hain."),
        "covers": ["R50-1-I", "R50-1-II", "R50-1-III", "R50-1-DATE", "LIMIT-FP-1Y"],
    },
    {
        "id": "b4_24_rule50_2",
        "part": "RULE 50(2) • ORDINARY AND ENHANCED RATES",
        "title": "THIRTY PER CENT FOR LIFE, FIFTY PER CENT FOR A WINDOW",
        "accent": ORANGE, "badge": "RULE 50(2)",
        "crumb": "CHAPTER VIII  •  THE TWO RATES",
        "q": "What is the ordinary rate, what is the enhanced rate, and how long does the enhanced rate last?",
        "q_say": "Sir, ordinary rate kya hai, enhanced rate kya hai, aur enhanced rate kitne din chalti hai?",
        "heads": [("30 PER CENT", "Ordinary rate", BLUE),
                  ("Rs 9,000 - 75,000", "Ordinary band", ORANGE),
                  ("50 PER CENT", "Enhanced rate", GREEN),
                  ("10 / 7 YEARS", "Enhanced window", PURPLE)],
        "boxes": [
            ("(a)(i): 30 PER CENT",
             "Family pension = ==30 per cent of pay==, minimum ==Rs 9,000== and maximum ==Rs 75,000== a month.",
             "Rule 50(2)(a)(i): subject to sub-clauses (ii) and (iii), the amount of family pension shall be determined at a uniform rate of thirty per cent of pay, subject to a minimum of Rs 9,000 per month and a maximum of Rs 75,000 per month. Pay here means the more beneficial of emoluments under Rule 31 and average emoluments under Rule 32 (Explanation 1).",
             BLUE,
             "Ordinary rate thirty percent of pay hai. Minimum nau hazaar, maximum pachattar hazaar mahina. Pay ka matlab emoluments ya average emoluments mein se jo zyada ho, Explanation ek kehta hai."),
            ("(a)(ii): DEATH IN SERVICE",
             "==50 per cent== of pay, from the day after death, for ==ten years==.",
             "Rule 50(2)(a)(ii): where a servant dies while in service, the rate of family pension shall be equal to fifty per cent of pay, payable from the date following the date of death for a period of ten years. The enhanced rate is time-bound; after ten years sub-rule (2)(b) drops it to thirty per cent.",
             ORANGE,
             "Agar service ke dauran death ho, to pachaas percent pay, death ke agle din se, das saal tak. Das saal ke baad rate thirty percent par aa jaata hai, sub-rule do(b) kehta hai."),
            ("(a)(iii): AFTER RETIREMENT",
             "==50 per cent== for ==seven years==, or until the retired servant would have turned ==67==, whichever is ==less==.",
             "Rule 50(2)(a)(iii): in the event of death after retirement, the family pension determined under sub-clause (ii) shall be payable for seven years, or up to the date on which the retired deceased servant would have attained the age of sixty seven years had he survived, whichever is less. The source material printed twenty-seven years; that is a typographical error.",
             GREEN,
             "Retirement ke baad death par pachaas percent, lekin saat saal ke liye, ya jab tak retired servant seven-sixty-seven saal ka hota, jo kam ho. Podcast mein twenty-seven chhap gaya tha, wo typo hai."),
            ("(a)(iii) PROVISOS",
             "The enhanced amount can never exceed the ==pension authorised on retirement==; if that pension is below the 30 per cent floor, pay the ==30 per cent amount==.",
             "First proviso to Rule 50(2)(a)(iii): the family pension under this sub-clause shall in no case exceed the pension authorised on retirement or dismissal. Second proviso: where the pension authorised is less than the family pension admissible under sub-clause (i), the amount shall be limited to the family pension admissible under sub-clause (i). So the enhanced rate is doubly capped, above and below.",
             PURPLE,
             "Iske do provisos hain. Pehla: enhanced amount retirement par authorised pension se zyada nahi ho sakti. Doosra: agar authorised pension thirty percent se kam hai, to thirty percent wala amount hi milega. Upar aur neeche dono taraf cap hai."),
        ],
        "trap": "<<TRAP:>> Enhanced rate is ==10 years== for death in service but ==7 years or age 67, whichever is LESS== after retirement. Never 27 years.",
        "trap_say": ("Trap ye hai: service ke dauran death par das saal, retirement ke baad saat saal ya sixty-seven saal ki age, "
                     "jo kam ho. Twenty-seven saal kabhi nahi."),
        "covers": ["R50-2A-I", "LIMIT-FP-ORD-RATE", "LIMIT-FP-ORD-FLOOR", "LIMIT-FP-ORD-CEIL",
                   "R50-2A-II", "TL-FP-ENH-10Y", "R50-2A-III", "TL-FP-ENH-7Y-67", "LIMIT-FP-ENH-CEIL",
                   "R50-2A-III-P1", "R50-2A-III-P2", "R50-2A-EXPL1", "R50-2A-EXPL2", "R50-2A-EXPL3", "R50-2B"],
    },
    {
        "id": "b4_25_rule50_3_4",
        "part": "RULE 50(3) AND (4) • ADDITIONAL FAMILY PENSION",
        "title": "AFTER EIGHTY, THE FAMILY PENSIONER GETS HER OWN SLAB",
        "accent": PURPLE, "badge": "RULE 50(3)-(4)",
        "crumb": "CHAPTER VIII  •  AGE, NOT THE SERVANT'S AGE",
        "q": "Is additional family pension based on the age of the servant or of the family pensioner?",
        "q_say": "Sir, additional family pension servant ki age par milti hai ya family pensioner ki age par?",
        "heads": [("80-85", "20 per cent", BLUE),
                  ("85-90", "30 per cent", ORANGE),
                  ("90-95", "40 per cent", GREEN),
                  ("95-100", "50 per cent", PURPLE)],
        "chart": {
            "title": "Additional family pension as a percentage of basic family pension",
            "unit": "%", "max": 100, "label_w": 340,
            "bars": [("80 to under 85 years", 20, BLUE, "twenty per cent"),
                     ("85 to under 90 years", 30, ORANGE, "thirty per cent"),
                     ("90 to under 95 years", 40, GREEN, "forty per cent"),
                     ("95 to under 100 years", 50, PURPLE, "fifty per cent"),
                     ("100 years or more", 100, RED, "hundred per cent")],
        },
        "boxes": [
            ("50(3): THE TABLE",
             "Same five slabs, but on the ==family pensioner's own age==: 20 / 30 / 40 / 50 / 100 per cent.",
             "Rule 50(3)(a): in addition to family pension under sub-rule (2), additional family pension is payable to the family pensioner after completion of eighty years - 20 per cent from 80 to under 85, 30 per cent from 85 to under 90, 40 per cent from 90 to under 95, 50 per cent from 95 to under 100, and 100 per cent at 100 years or more, of basic family pension.",
             BLUE,
             "Rule fifty teen ka table wahi hai jo pension ka tha, lekin yahan ginti family pensioner ki apni age se hoti hai. Assi se pachattar twenty, nabbe thirty, pachannev chalees, sau pachaas, aur sau par hundred."),
            ("WHOSE AGE",
             "The ==family pensioner's== age decides. A widow of 82 gets the slab even if her husband died at 60.",
             "Rule 50(3) is triggered by the age of the family pensioner, not by the age the deceased servant would have reached. The source podcast tested the deceased servant's age, which is wrong. For Rule 44(6) the pensioner's own age is used; for Rule 50(3) the family pensioner's own age is used. The principle is the same: the person drawing the money must be eighty.",
             ORANGE,
             "Age kiska? Family pensioner ka. Agar widow bayaasi saal ki hai, to use slab milega, chahe husband saath saal ki age mein guzre. Podcast ne deceased servant ki age li thi, wo galat hai."),
            ("THE DAY",
             "From the ==first day of the calendar month== in which it falls due. The Rule carries the ==same illustration== as Rule 44(6).",
             "Rule 50(3)(b): additional family pension shall be payable from the first day of the calendar month in which it falls due. Illustration in the Rule: a family pensioner born on 20.08.1942 and one born on 01.08.1942 both get 20 per cent from 01.08.2022. The same illustration appears under Rule 44(6), which is why the two are taught together.",
             GREEN,
             "Payment us calendar month ki pehli tareekh se jisme wo due hota hai. Rule mein wahi illustration hai jo Rule forty-four chhah mein tha. Bees August aur pehli August, dono ko pehli August se."),
            ("50(4): ROUNDING",
             "Fixed at monthly rates, expressed in ==whole rupees==, fraction rounded ==up==; the maximum still binds.",
             "Rule 50(4): family pension under sub-rule (2) and additional family pension under sub-rule (3) shall be fixed at monthly rates and expressed in whole rupees; any fraction of a rupee shall be rounded off to the next higher rupee. Proviso: in no case shall family pension under sub-rule (2) be allowed in excess of the maximum prescribed under the rule.",
             PURPLE,
             "Sub-rule chaar: amount monthly rate par tay hoga, poore rupee mein, aur paisa ho to agle rupee tak badhega. Proviso yaad rakho, maximum se zyada kabhi nahi."),
        ],
        "trap": "<<TRAP:>> Additional ==family== pension uses the ==family pensioner's== age. Additional ==pension== under Rule 44(6) uses the ==pensioner's== age.",
        "trap_say": ("Trap ye hai: additional family pension family pensioner ki age par hai, aur Rule forty-four chhah ki additional pension "
                     "pensioner ki apni age par."),
        "covers": ["R50-3", "R50-3-SLABS", "R50-3-DAY", "R50-3-ILLUS", "R50-4", "R50-4-P1"],
    },
    {
        "id": "b4_26_rule50_5_7",
        "part": "RULE 50(5) TO (7) • EOP, PRECEDENCE AND SHARES",
        "title": "THE ORDER OF PRECEDENCE AND THE ONE-PENSION-AT-A-TIME RULE",
        "accent": BLUE, "badge": "RULE 50(5)-(7)",
        "crumb": "CHAPTER VIII  •  WHO STANDS WHERE",
        "q": "In what order do family members receive family pension, and can two of them receive it together?",
        "q_say": "Sir, family pension kis order mein milti hai, aur do log saath le sakte hain kya?",
        "heads": [("EOP 1939", "No double award", BLUE),
                  ("SPOUSE", "Step one", ORANGE),
                  ("CHILDREN", "Step two", GREEN),
                  ("PARENTS, SIBLINGS", "Steps three and four", PURPLE)],
        "boxes": [
            ("50(5): EOP",
             "While an award under the ==CCS (Extraordinary Pension) Rules, 1939== runs, no family pension under Rule 50. If EOP is later sanctioned, the Rule 50 pension is ==discontinued==.",
             "Rule 50(5)(a): where an award of family pension under the CCS (Extraordinary Pension) Rules, 1939 is authorised, no family pension under this rule shall be payable during the currency of that award. (b) Where a claim for EOP is under consideration, family pension may be authorised under these rules; if EOP is later sanctioned, a revised Pension Payment Authority is issued and the Rule 50 pension is discontinued. (c) Family pension under this rule is not subject to any limitation with reference to family pension admissible for service in any other organisation, including the armed forces.",
             BLUE,
             "Sub-rule paanch: EOP yaani Extraordinary Pension Rules nineteen thirty-nine ka award chal raha ho to Rule fifty ki family pension nahi milegi. Baad mein EOP sanction ho jaye to Rule fifty wali band. Aur clause (c) kehta hai doosri organisation ki family pension se koi limitation nahi."),
            ("50(6): PRECEDENCE",
             "The order is ==spouse, then children, then dependent parents, then dependent disabled siblings==.",
             "Rule 50(6): family pension is payable in this order - (i) widow or widower, including a post-retiral spouse and a judicially separated wife or husband, subject to sub-rule (8); (ii) children, including adopted children, step children and children born after retirement, subject to sub-rule (9); (iii) dependent parents, including adoptive parents, subject to sub-rule (10); (iv) dependent siblings suffering from a mental or physical disability, subject to sub-rule (11). Explanation: widow and widower mean a spouse legally wedded to the deceased.",
             ORANGE,
             "Sub-rule chhah order deta hai. Pehle spouse, phir bachche, phir dependent parents, aur phir dependent disabled siblings. Har step apne sub-rule ke subject hai, isliye order aur eligibility alag cheez hai."),
            ("50(7): ONE AT A TIME",
             "Normally ==only one member== draws at a time, subject to listed exceptions; where more than one draws, the pension is split in ==equal shares==.",
             "Rule 50(7)(a): subject to the proviso to clause (b), clauses (c), (d), (e), (f) and (g) of sub-rule (8), clause (g) and the proviso to sub-clause (iii) of clause (h), and clause (k) of sub-rule (9), family pension shall not be payable to more than one member at the same time. (b) Where it is payable to more than one, it is paid in equal shares, any fraction of a rupee rounded up; proviso: the maximum prescribed shall not be exceeded and any excess from rounding is ignored.",
             GREEN,
             "Sub-rule saat: normal rule ek time par ek hi member. Lekin jo exceptions list mein hain, unme do ya zyada le sakte hain, aur phir barabar share. Rounding se maximum cross ho jaye to wo fraction chhod diya jaata hai."),
            ("THE STRUCTURE",
             "Rule 50 is built as ==gateways (1), rates (2-4), precedence (6), then one chapter per class== - (8) spouse, (9) children, (10) parents, (11) siblings.",
             "Read Rule 50 as a machine: sub-rule (1) opens the gate, sub-rule (2) fixes the money, sub-rules (3) and (4) add the age slabs and rounding, sub-rule (5) deals with EOP, sub-rule (6) sets the queue, sub-rule (7) sets one-at-a-time, and sub-rules (8) to (11) are the detailed rules for each class in the queue. Sub-rule (12) to (16) then deal with two pensions, forms and exclusions.",
             PURPLE,
             "Rule fifty ko machine ki tarah padho. Ek gateway kholta hai, do paisa tay karta hai, teen chaar age slab aur rounding, paanch EOP, chhah queue, saat ek time par ek, aur aath se gyarah har class ke detail. Phir baarah se solah forms aur exclusions."),
        ],
        "trap": "<<TRAP:>> ==Precedence== is not ==eligibility==. A person can be in the queue and still fail the income or age test in his own sub-rule.",
        "trap_say": ("Trap ye hai: precedence aur eligibility alag hain. Queue mein hona kaafi nahi, "
                     "apne sub-rule ka income ya age test bhi pass karna padta hai."),
        "covers": ["R50-5A", "R50-5B", "R50-5C", "R50-6", "R50-6-I", "R50-6-II", "R50-6-III", "R50-6-IV",
                   "R50-6-EXPL", "R50-7A", "R50-7B", "R50-7B-P1"],
    },
    {
        "id": "b4_27_rule50_8_spouse",
        "part": "RULE 50(8)(a) TO (f) • THE SPOUSE",
        "title": "WIDOW, WIDOWER, RE-MARRIAGE AND MORE WIVES THAN ONE",
        "accent": GREEN, "badge": "RULE 50(8)",
        "crumb": "CHAPTER VIII  •  CLAUSE BY CLAUSE",
        "q": "How does the spouse's family pension work on re-marriage, and what if there are two wives?",
        "q_say": "Sir, re-marriage par spouse ki family pension ka kya hota hai, aur do biwiyan hon to?",
        "heads": [("TILL DEATH", "8(a)", BLUE),
                  ("CHILDLESS WIDOW", "8(b)", ORANGE),
                  ("EQUAL SHARES", "8(c)", GREEN),
                  ("NO LAPSE", "8(d)", PURPLE)],
        "table": {
            "title": "Rule 50(8) — the spouse clauses",
            "head": ["Clause", "Situation", "What the Rule does"],
            "w": [1.0, 4.0, 8.0],
            "rows": [
                ["(a)", "Servant or pensioner survived by a widow or widower",
                 "Pension to that spouse up to death or re-marriage, whichever is earlier; income from other sources does not affect it"],
                ["(b)", "Childless widow re-marries",
                 "Pension continues if her income from all sources is less than the minimum family pension plus DR; it stops if her income reaches that level"],
                ["(c)", "More widows than one",
                 "Paid to the widows in equal shares; on death or ineligibility of a widow, her share goes to her child or children who satisfy Rule 50(9)"],
                ["(d)", "Widow with no child",
                 "Her share does not lapse; it goes to the other widows in equal shares, or in full to the only other widow"],
                ["(e)", "Widow without an eligible child, but children of another wife who is not alive",
                 "Those children take the share their mother would have taken; shares do not lapse but move to the other widows or children"],
                ["(f)", "Widow without an eligible child, but children of a divorced wife",
                 "Same as (e), taking the share the divorced mother would have taken had she not been divorced"],
            ],
        },
        "boxes": [
            ("8(a): THE SPOUSE",
             "Pension to the widow or widower ==up to death or re-marriage==, whichever is earlier. ==Her income is irrelevant==.",
             "Rule 50(8)(a): if the deceased servant or pensioner is survived by a widow or widower, family pension at the sub-rule (2) rate is payable to that spouse up to the date of death or re-marriage, whichever is earlier, and eligibility is not affected by the amount of income from other sources. Contrast the childless widow in clause (b), where income does matter.",
             BLUE,
             "Clause a: spouse ko pension death ya re-marriage tak, jo pehle ho. Uske doosre source ki income se koi farq nahi padta. Lekin clause b wali childless widow mein income dekhi jaati hai."),
            ("8(b): CHILDLESS WIDOW",
             "On re-marriage her pension ==continues== if her income is below the ==minimum family pension plus DR==; it ==stops== if her income reaches that level.",
             "Rule 50(8)(b): where a deceased servant is survived by a childless widow, on her re-marriage family pension shall continue to be payable to her if her income from all other sources is less than the amount of minimum family pension under sub-rule (2) and the dearness relief admissible thereon. Proviso: if, after re-marriage, her income becomes equal to or exceeds that amount, her pension shall stop and become payable to the other eligible member of the family, if any.",
             ORANGE,
             "Clause b: childless widow re-marriage ke baad bhi pension le sakti hai, agar uski doosri income minimum family pension plus DR se kam ho. Agar income us level par pahunch jaye to pension band, aur agle eligible member ko."),
            ("8(c) & (d): TWO WIVES",
             "More widows than one: ==equal shares==. A widow's share goes to ==her own children==; if she has none, it goes to the ==other widows==.",
             "Rule 50(8)(c): where the deceased is survived by more widows than one, family pension shall be paid to the widows in equal shares and, on the death or ineligibility of a widow, her share shall become payable to her child or children who fulfil the eligibility conditions in sub-rule (9). (d) Where the widow is not survived by any child, her share shall not lapse but shall be payable to the other widows in equal shares, or in full to the only other widow.",
             GREEN,
             "Clause c aur d: ek se zyada widow ho to barabar share. Kisi widow ki death ya ineligibility par uska share uske apne bachchon ko. Agar uske bachche nahi hain, to share lapse nahi hota, baaki widows ko chala jaata hai."),
            ("8(e) & (f): OTHER MOTHERS",
             "Children of a ==dead wife== or of a ==divorced wife== take the share their mother would have taken. Shares ==never lapse==; they move within the family.",
             "Rule 50(8)(e) and (f): where the widow has no eligible child but the servant left eligible children from another wife who is not alive, or from a divorced wife, those children are entitled to the share of family pension which their mother would have received had she been alive, or had she not been divorced. On any share ceasing to be payable, it does not lapse but is payable to the other widow or widows and the other eligible children in equal shares, or in full to the only one.",
             PURPLE,
             "Clause e aur f: doosri marhoom biwi ya divorced biwi ke bachche, apni maa ka share lete hain. Aur koi share lapse nahi hota, wo parivaar ke andar hi shift hota hai."),
        ],
        "trap": "<<TRAP:>> A widow's own income is ==irrelevant== under 8(a). Income matters only for a ==childless widow who re-marries== under 8(b).",
        "trap_say": ("Trap ye hai: clause a mein widow ki income se koi farq nahi padta. Income sirf clause b mein dekhi jaati hai, "
                     "jab childless widow re-marriage kare."),
        "covers": ["R50-8A", "R50-8B", "R50-8B-P1", "R50-8C", "R50-8D", "R50-8E", "R50-8F", "R50-8-EQ"],
    },
    {
        "id": "b4_28_rule50_8_rest",
        "part": "RULE 50(8)(g) TO (k) • VOID MARRIAGE, JUDICIAL SEPARATION",
        "title": "THE HARD CASES — VOID MARRIAGE, SEPARATION AND THE ANNUAL CERTIFICATE",
        "accent": RED, "badge": "RULE 50(8)(g)-(k)",
        "crumb": "CHAPTER VIII  •  THE FIVE REMAINING CLAUSES",
        "q": "What about children of a void marriage, and a judicially separated spouse?",
        "q_say": "Sir, void marriage ke bachche aur judicially separated spouse ka kya hota hai?",
        "heads": [("VOID MARRIAGE", "8(g)", BLUE),
                  ("SEPARATED, NO CHILD", "8(h)", ORANGE),
                  ("SEPARATED, MINOR CHILD", "8(i)", GREEN),
                  ("ANNUAL CERTIFICATE", "8(k)", PURPLE)],
        "boxes": [
            ("8(g): VOID MARRIAGE",
             "Children of a ==void or voidable marriage== take the share their mother would have taken. Their shares ==do not lapse==.",
             "Rule 50(8)(g): where the deceased is survived by a widow without an eligible child but has left eligible children from a void or voidable marriage, those children are entitled to the share of family pension which the mother would have received had the marriage not been void or voidable; on their share ceasing to be payable it does not lapse but is payable to the widow or the other eligible children in equal shares.",
             BLUE,
             "Clause g: void ya voidable marriage ke bachche bhi apni maa ka share lete hain, jaise marriage valid hoti. Aur share lapse nahi hota, widow ya baaki eligible bachchon ko chala jaata hai."),
            ("8(h): SEPARATED, NO CHILD",
             "Judicially separated widow or widower with ==no child==: the family pension goes to ==the surviving person==.",
             "Rule 50(8)(h): where a male or female servant or pensioner dies leaving behind a judicially separated widow or widower and no child or children, the family pension shall be payable to the person surviving. Judicial separation is recognised in the Rule 45(6) family definition as well, so the separated spouse is family for gratuity too.",
             ORANGE,
             "Clause h: judicially separated spouse ho aur koi bachcha na ho, to family pension us surviving person ko milegi. Judicial separation Rule forty-five chhah ki family definition mein bhi maani gayi hai."),
            ("8(i): SEPARATED, MINOR",
             "With a ==minor or disabled child==, the separated spouse draws ==only as guardian==. Once the child is major and still eligible, it moves to the child.",
             "Rule 50(8)(i): where the deceased leaves a judicially separated spouse with a minor child or a child suffering from a disorder or disability of mind, family pension is payable to the surviving spouse provided he or she is the guardian of that child; if the spouse ceases to be the guardian, it is payable to the actual guardian. Proviso: where the minor child, after attaining majority, remains eligible, the pension becomes payable to the child from that date, and after the child ceases to be eligible it reverts to the separated spouse till death or re-marriage.",
             GREEN,
             "Clause i: minor ya disabled bachcha ho to separated spouse ko pension sirf tab milegi jab wo guardian ho. Bachcha major hone par eligible rahe to pension us bachche ko. Uske baad phir separated spouse ko, death ya re-marriage tak."),
            ("8(j) & 8(k): MAJOR CHILD, CERTIFICATE",
             "A ==major eligible child== takes first, then it reverts to the separated spouse. A ==childless widow== must give an annual certificate.",
             "Rule 50(8)(j): where the separated spouse has a child who has attained majority but is eligible for family pension, the pension becomes payable to that child after the death of the servant, and when the child ceases to be eligible it becomes payable to the separated spouse till death or re-marriage. Rule 50(8)(k): a childless widow after re-marriage must furnish a certificate to the Pension Disbursing Authority once a year that she has not started earning her livelihood; Explanation: she is deemed to be earning if her income from other sources is equal to or more than the minimum family pension plus DR.",
             PURPLE,
             "Clause j aur k: major eligible bachcha pehle, phir separated spouse. Aur clause k: childless widow ko re-marriage ke baad har saal certificate dena hota hai ki usne apni livelihood shuru nahi ki. Income minimum family pension plus DR ke barabar ho jaye to earning maana jayega."),
        ],
        "trap": "<<TRAP:>> A separated spouse is family, but under 8(i) the pension is tied to being the ==guardian==. Lose guardianship, lose the pension.",
        "trap_say": ("Trap ye hai: separated spouse family mein aata hai, lekin clause i mein pension guardian hone se bandhi hai. "
                     "Guardianship gayi to pension gayi."),
        "covers": ["R50-8G", "R50-8H", "R50-8I", "R50-8I-P1", "R50-8J", "R50-8K", "R50-8K-EXPL"],
    },
    {
        "id": "b4_29_rule50_9_elig",
        "part": "RULE 50(9)(a) TO (c) • CHILDREN AND THE EARNING TEST",
        "title": "SON, DAUGHTER, DISABLED CHILD — THREE DIFFERENT GATES",
        "accent": AMBER, "badge": "RULE 50(9)(a)-(c)",
        "crumb": "CHAPTER VIII  •  WHO IS AN ELIGIBLE CHILD",
        "q": "What are the eligibility conditions for a son, a daughter and a disabled child?",
        "q_say": "Sir, bete, beti aur disabled bachche ke liye eligibility ki kya shartein hain?",
        "heads": [("SON", "Under 25, unmarried, not earning", BLUE),
                  ("DAUGHTER", "Unmarried, widowed or divorced", ORANGE),
                  ("DISABLED CHILD", "For life", GREEN),
                  ("EARNING TEST", "Income vs minimum FP", PURPLE)],
        "boxes": [
            ("(a)(i): SON",
             "He must be ==unmarried, under 25 and not earning==. Adopted, step and post-retirement sons count.",
             "Rule 50(9)(a)(i): in the case of a son, other than a son suffering from a mental or physical disability, including an adopted son, step son and a son born after retirement of the pensioner - he must be unmarried, below the age of twenty-five years and not earning his livelihood. All three conditions must hold at the same time.",
             BLUE,
             "Clause a(i): beta unmarried ho, pachchees saal se kam ho, aur apni livelihood nahi kama raha ho. Teen shartein saath chahiye. Adopted, step aur retirement ke baad paida hone wala beta bhi shamil hai."),
            ("(a)(ii): DAUGHTER",
             "==Unmarried, widowed or divorced== and not earning. The clause itself sets ==no age limit== for a daughter.",
             "Rule 50(9)(a)(ii): in the case of a daughter, other than a disabled daughter, including an adopted daughter, step daughter and a daughter born after retirement - she must be unmarried, widowed or divorced and not earning her livelihood. Unlike the son, this clause carries no age limit; the sequencing rules in clauses (d), (e) and (j) do the age work.",
             ORANGE,
             "Clause a(ii): beti unmarried, widowed ya divorced ho, aur livelihood nahi kama rahi ho. Is clause mein beti ki koi age limit nahi hai. Age ka kaam clause d, e aur j karte hain."),
            ("(a)(iii): DISABLED",
             "A son or daughter with a ==mental or physical disability==, not earning his livelihood. No age limit.",
             "Rule 50(9)(a)(iii): in the case of a son or daughter suffering from a mental or physical disability, including an adopted, step or post-retirement child, he or she must not be earning his or her livelihood. There is no age limit and no marital condition in this clause; clause (h) then makes the pension payable for life subject to its conditions, and clause (i) says marriage does not disqualify.",
             GREEN,
             "Clause a(iii): mentally ya physically disabled beta ya beti, jo livelihood nahi kama raha. Yahan na age limit hai na shaadi ki shart. Clause h ise life-long karta hai, aur clause i kehta hai shaadi se disqualification nahi."),
            ("(b) & (c): EARNING",
             "An ordinary child is ==earning== at or above the minimum family pension plus DR. A disabled child is ==not earning== below the entitled pension plus DR.",
             "Rule 50(9)(b): a son or daughter other than a disabled one is deemed to be earning his livelihood if his income from other sources is equal to or more than the minimum family pension under sub-rule (2) and the dearness relief admissible thereon. (c) A child suffering from a mental or physical disability is deemed NOT to be earning if his overall income from sources other than family pension is less than the entitled family pension under sub-clause (i) of clause (a) of sub-rule (2) plus DR.",
             PURPLE,
             "Earning test do tarah ka hai. Aam bachche ke liye income minimum family pension plus DR ke barabar ya zyada ho to earning maana jayega. Disabled bachche ke liye ulta hai, agar overall income entitled family pension plus DR se kam ho to not earning."),
        ],
        "trap": "<<TRAP:>> The ==25-year cap applies to sons only==. A daughter's clause has no age limit; her limits come from clauses (d), (e) and (j).",
        "trap_say": ("Trap ye hai: pachchees saal ki limit sirf bete par hai. Beti ke clause mein koi age limit nahi, "
                     "uski limits clause d, e aur j se aati hain."),
        "covers": ["R50-9-SON", "TL-FP-SON-25", "R50-9-DAUGHTER", "R50-9-DISABLED", "R50-9-EARN",
                   "R50-9-EARN-DISABLED", "LIMIT-FP-INCOME-14400"],
    },
    {
        "id": "b4_30_rule50_9_sequence",
        "part": "RULE 50(9)(d) TO (i) • ORDER, TWINS AND DISABILITY FOR LIFE",
        "title": "BIRTH ORDER, TWINS AND DISABILITY FOR LIFE",
        "accent": BLUE, "badge": "RULE 50(9)(d)-(i)",
        "crumb": "CHAPTER VIII  •  SEQUENCING",
        "q": "If there are several children, who draws first, and how does a disabled child get it for life?",
        "q_say": "Sir, kai bachche hon to pehle kaun leta hai, aur disabled bachche ko life-long kaise milta hai?",
        "heads": [("BIRTH ORDER", "9(d)", BLUE),
                  ("TILL 25", "9(e)", ORANGE),
                  ("TWINS", "9(g)", GREEN),
                  ("FOR LIFE", "9(h)", PURPLE)],
        "boxes": [
            ("(d) & (e): ORDER",
             "First to children ==below twenty-five== in the ==order of their birth==. The elder draws till 25, marriage, re-marriage, earning or death — whichever is ==earliest==.",
             "Rule 50(9)(d): where the deceased leaves more than one child, family pension shall first be payable to children below the age of twenty-five years who fulfil the eligibility conditions, in the order of their birth. (e) The elder child is entitled till he or she attains twenty-five, or marries or re-marries, or starts earning, or dies, whichever is earliest; the younger becomes eligible after the elder next above him or her falls away.",
             BLUE,
             "Clause d aur e: pehle pachchees saal se kam umar ke bachche, aur unme bhi birth order. Bada bachcha pachchees saal, shaadi, earning ya death, jo sabse pehle ho, tab tak leta hai. Uske baad chhota."),
            ("(f) & (g): MINOR, TWINS",
             "A ==minor== receives through the guardian. ==Twins== share equally, and one twin's share reverts to the other.",
             "Rule 50(9)(f): where family pension is granted to a minor, it shall be payable through the guardian. (g) Where family pension is payable to twin children, it shall be paid to them in equal shares; when one twin ceases to be eligible, his or her share reverts to the other, and when both cease to be eligible it goes to the next eligible single child or twin children.",
             ORANGE,
             "Clause f aur g: minor ko guardian ke through. Twins ko barabar share, aur ek twin ineligible ho jaye to uska share doosre ko. Dono ineligible ho jaye to agle eligible child ya twins ko."),
            ("(h): DISABILITY FOR LIFE",
             "Pension for life to a disabled child, subject to ==seven conditions==, including that the disability ==existed before the death== and is certified by a ==competent authority or Medical Board==.",
             "Rule 50(9)(h): where no child below twenty-five is eligible, family pension is payable for life to a child with a disorder or disability of mind or a physical disability rendering him unable to earn a living, subject to (i) the disability existed before the death of the servant or pensioner and his or her spouse; (ii) if there are other children, the pension goes to them in birth order until the last child attains twenty-five and then resumes for the disabled child; (iii) with more than one disabled child, birth order applies; (iv) payment through the guardian for a mental disability, and directly for a physically disabled major; (v) the appointing authority must be satisfied, evidenced by a certificate from an authority competent under the RPwD Act, 2016 or a Medical Board; (vi) a continuing certificate once if permanent, once every five years if temporary; (vii) for a mentally retarded child, payment to a person nominated by the servant, or by the spouse, and a Guardianship Certificate under section 14 of the National Trust Act, 1999 is also accepted.",
             GREEN,
             "Clause h sabse bada hai. Disabled bachche ko life-long pension, saat conditions ke saath. Disability death se pehle ki honi chahiye, aur RPwD Act ke competent authority ya Medical Board ka certificate chahiye. Permanent ho to ek baar, temporary ho to har paanch saal. Mental retardation mein National Trust Act ka guardianship certificate bhi chalta hai."),
            ("(i): MARRIAGE",
             "Marriage of a ==disabled== child does ==not== make him or her ineligible.",
             "Rule 50(9)(i): marriage by a child who is suffering from a disability referred to in clause (h) shall not render him or her ineligible for family pension under this sub-rule. Contrast clause (n), which ends the pension of an ordinary son or daughter from the date of marriage.",
             PURPLE,
             "Clause i: disabled bachche ki shaadi hone se wo ineligible nahi hota. Iske ulta clause n hai, jahan aam bete ya beti ki pension shaadi ki date se band ho jaati hai."),
        ],
        "trap": "<<TRAP:>> A disabled child waits behind the ordinary children until the ==last one turns 25==, and then the pension ==resumes== for life.",
        "trap_say": ("Trap ye hai: disabled bachcha aam bachchon ke peeche wait karta hai, jab tak aakhri bachcha pachchees ka na ho jaye. "
                     "Uske baad life-long pension shuru."),
        "covers": ["R50-9-D", "R50-9-E", "R50-9-F", "R50-9-G", "R50-9-H", "R50-9-H-C1", "R50-9-H-C2",
                   "R50-9-H-C5", "R50-9-H-C6", "R50-9-H-C7", "R50-9-I", "GSR-770E-2022"],
    },
    {
        "id": "b4_31_rule50_9_daughter",
        "part": "RULE 50(9)(j) • THE DAUGHTER BEYOND TWENTY-FIVE",
        "title": "THE SIX CONDITIONS THAT KEEP A DAUGHTER ON THE PENSION",
        "accent": PINK, "badge": "RULE 50(9)(j)",
        "crumb": "CHAPTER VIII  •  THE LONGEST CLAUSE IN RULE 50",
        "q": "How does an unmarried, widowed or divorced daughter keep family pension after twenty-five?",
        "q_say": "Sir, unmarried, widowed ya divorced beti pachchees saal ke baad family pension kaise leti hai?",
        "heads": [("NO DISABLED CHILD", "Condition two", BLUE),
                  ("DEPENDENT", "Condition three", ORANGE),
                  ("BIRTH ORDER", "Condition four", GREEN),
                  ("DIVORCE DATE", "Condition six", PURPLE)],
        "boxes": [
            ("THE ROUTE",
             "No eligible son or daughter under (d) or (h)? An ==unmarried, widowed or divorced daughter past 25== gets it, till marriage, re-marriage or earning.",
             "Rule 50(9)(j): where the deceased is not survived by a son or daughter eligible under clause (d) or clause (h), or where such a child dies or ceases to be eligible, family pension shall be granted or continued to an unmarried, widowed or divorced daughter beyond the age of twenty-five for life, or until she gets married or re-married, or until she starts earning her livelihood, whichever is the earliest, subject to the six conditions in sub-clauses (i) to (vi).",
             PINK,
             "Clause j ek raasta deta hai. Agar clause d ya h wala koi bachcha eligible nahi hai, to unmarried, widowed ya divorced beti pachchees saal ke baad bhi family pension le sakti hai. Life-long, ya shaadi, re-marriage ya earning tak, jo pehle ho."),
            ("CONDITIONS 1-3",
             "(i) Children in birth order draw first till the last turns 25. (ii) ==No disabled child== is eligible. (iii) She was ==dependent== on the parent when he was alive.",
             "Rule 50(9)(j)(i): family pension shall initially be payable to the children in the order set out in clause (d) until the last child attains twenty-five years. (ii) There is no disabled child eligible to receive family pension under clause (e) as printed, read with clause (h). (iii) The unmarried, widowed or divorced daughter was dependent on her parent or parents when he or she or they were alive.",
             BLUE,
             "Pehli teen conditions. Clause d ke bachche birth order mein pehle, jab tak aakhri bachcha pachchees ka na ho. Koi disabled bachcha eligible na ho. Aur beti apne maa baap par dependant thi jab wo zinda the."),
            ("CONDITIONS 4-5",
             "(iv) More than one such daughter: ==birth order==. (v) The elder draws till marriage, re-marriage or earning; the younger follows.",
             "Rule 50(9)(j)(iv): where more than one unmarried, widowed or divorced daughter beyond twenty-five survives, family pension shall first be payable in the order of their birth. (v) The elder daughter is entitled until she marries or re-marries or starts earning, whichever is earlier, and the younger becomes eligible after the elder next above her falls away or dies.",
             ORANGE,
             "Chauthi aur paanchvi condition. Ek se zyada aisi betiyan hon to birth order. Badi beti shaadi, re-marriage ya earning tak, jo pehle ho. Uske baad chhoti beti."),
            ("CONDITION 6: THE DATE",
             "For a widowed daughter, the ==husband's death==; for a divorced daughter, the ==divorce during the servant's or spouse's lifetime==. Two provisos govern the date.",
             "Rule 50(9)(j)(vi): in the case of a widowed daughter, the death of her husband, and in the case of a divorced daughter, her divorce, took place during the lifetime of the servant or pensioner or his or her spouse. First proviso: family pension is payable to a divorced daughter from the date of divorce if the divorce proceedings were filed in a competent court during the lifetime of the servant or pensioner or spouse but the divorce took place after their death. Second proviso: if, consequent on the death, family pension to another eligible member became payable before the date of divorce, the divorced daughter's pension shall not commence before that member ceases to be eligible or dies.",
             PURPLE,
             "Chhati condition date ki hai. Widowed beti ke liye husband ki death, aur divorced beti ke liye divorce, servant ya spouse ke jeevan kal mein hona chahiye. Pehla proviso kehta hai proceedings jeevan kal mein file hue aur divorce baad mein hua, to divorce ki date se pension. Doosra proviso kehta hai koi doosra member pehle se le raha hai to wo hatne tak intezaar."),
        ],
        "trap": "<<TRAP:>> A divorced daughter can draw ==from the date of divorce==, even after the servant's death — if the case was filed in his lifetime.",
        "trap_say": ("Trap ye hai: divorced beti ki pension divorce ki date se shuru ho sakti hai, chahe divorce servant ki death ke baad hua ho. "
                     "Shart ye hai ki proceedings uske jeevan kal mein file hui hon."),
        "covers": ["R50-9-J", "R50-9-J-C1", "R50-9-J-C2", "R50-9-J-C3", "R50-9-J-C4", "R50-9-J-C5",
                   "R50-9-J-C6", "R50-9-J-P1", "R50-9-J-P2"],
    },
    {
        "id": "b4_32_rule50_9_end",
        "part": "RULE 50(9)(k) TO (p) • SHARES, MARRIAGE, EARNING, CERTIFICATES",
        "title": "MORE MOTHERS THAN ONE, AND THE FOUR WAYS A CHILD'S PENSION ENDS",
        "accent": TEAL, "badge": "RULE 50(9)(k)-(p)",
        "crumb": "CHAPTER VIII  •  CLOSING THE CHILDREN'S CHAPTER",
        "q": "How are shares fixed among children of different mothers, and when does a child's pension stop?",
        "q_say": "Sir, alag alag maa ke bachchon ka share kaise tay hota hai, aur bachche ki pension kab band hoti hai?",
        "heads": [("MOTHER'S SHARE", "9(k)", BLUE),
                  ("NO LAPSE", "9(m)", ORANGE),
                  ("MARRIAGE", "9(n)", GREEN),
                  ("EARNING", "9(o)", PURPLE)],
        "boxes": [
            ("(k) & (l): OTHER MOTHERS",
             "Children of ==more than one widow==, or of a widow and a divorced wife, or of a void marriage, take the share their mother would have taken.",
             "Rule 50(9)(k): where the deceased leaves children from more than one widow, or from a widow and a divorced wife, or from a widow or divorced wife and a void or voidable marriage, the eligible children are entitled to the share of family pension which their mother would have received at the time of death had she been alive, or had she not been divorced, or had the marriage not been void or voidable. (l) Where there are more than one child from such a mother, the share is payable in the manner specified in the sub-rule.",
             BLUE,
             "Clause k aur l: ek se zyada widow, ya widow aur divorced wife, ya void marriage ke bachche, apni maa ka share lete hain, jaise maa zinda hoti. Aur ek hi maa ke ek se zyada bachche hon to share usi tareeke se bantega."),
            ("(m): NO LAPSE",
             "When such a share ceases to be payable it ==does not lapse==; it moves to the children of the other widow or divorced wife, in equal shares.",
             "Rule 50(9)(m): where the share or shares of family pension payable to such a child or children cease to be payable, they shall not lapse but shall be payable to the child or children from the other widow or divorced wife or void or voidable marriage, otherwise eligible, in equal shares, or in full to the only such child. Explanation: son or daughter includes a posthumous son or posthumous daughter.",
             ORANGE,
             "Clause m: aisa share band ho jaye to lapse nahi hota. Wo doosri widow ya divorced wife ke eligible bachchon ko barabar chala jaata hai, ya ek hi ho to poora. Explanation kehti hai son aur daughter mein posthumous bachcha bhi aata hai."),
            ("(n) & (o): TWO STOPS",
             "An ordinary son or daughter becomes ineligible ==from the date of marriage or re-marriage== (n), and the pension ==stops if he or she starts earning== (o).",
             "Rule 50(9)(n): an unmarried son, or an unmarried, widowed or divorced daughter, except a disabled son or daughter, shall become ineligible for family pension from the date he or she gets married or re-married. (o) Family pension payable to a son or daughter shall be stopped if he or she starts earning his or her livelihood. Note the difference: marriage disqualifies from its date, earning stops the pension when it happens, and clause (i) exempts disabled children from the marriage bar.",
             GREEN,
             "Clause n aur o, do stop points. Aam beta ya beti shaadi ya re-marriage ki date se ineligible. Aur earning shuru ho to pension band. Dhyaan do, disabled bachche par shaadi ka bar nahi lagta, clause i."),
            ("(p): THE CERTIFICATE",
             "A ==yearly certificate== to the Pension Disbursing Authority: not earning, and not married or re-married. A disabled child certifies only that he is ==not earning==.",
             "Rule 50(9)(p): it shall be the duty of the son or daughter, or the guardian, to furnish a certificate to the Pension Disbursing Authority once in a year that (i) he or she has not started earning his livelihood and (ii) he or she has not yet married or re-married; a similar certificate shall be furnished by a son or daughter suffering from a mental or physical disability once a year that he or she has not started earning his livelihood. Failure invites stoppage of the pension.",
             PURPLE,
             "Clause p: har saal Pension Disbursing Authority ko certificate dena hota hai ki earning shuru nahi ki aur shaadi nahi ki. Disabled bachcha sirf earning wala certificate deta hai. Na dene par pension rok di jaati hai."),
        ],
        "trap": "<<TRAP:>> Marriage disqualifies an ordinary child ==from the date of marriage==; earning ==stops== the pension. Two different mechanics in the same sub-rule.",
        "trap_say": ("Trap ye hai: aam bachche ke liye shaadi ki date se ineligibility, aur earning par pension stop. "
                     "Ek hi sub-rule mein do alag mechanics."),
        "covers": ["R50-9-K", "R50-9-L", "R50-9-M", "R50-9-M-EXPL", "R50-9-N", "R50-9-O", "R50-9-P"],
    },
    {
        "id": "b4_33_rule50_10_11",
        "part": "RULE 50(10) AND (11) • PARENTS AND SIBLINGS",
        "title": "THE LAST TWO STEPS OF THE QUEUE",
        "accent": PURPLE, "badge": "RULE 50(10)-(11)",
        "crumb": "CHAPTER VIII  •  DEPENDENCE IS THE KEY",
        "q": "When do dependent parents, and then dependent disabled siblings, get family pension?",
        "q_say": "Sir, dependent parents aur dependent disabled siblings ko family pension kab milti hai?",
        "heads": [("PARENTS", "For life", BLUE),
                  ("MOTHER FIRST", "Then father", ORANGE),
                  ("SIBLINGS", "For life", GREEN),
                  ("DEPENDENCE", "Income test", PURPLE)],
        "boxes": [
            ("10(a): PARENTS",
             "Only if no spouse or child is eligible. Parents take ==for life== if they were ==dependent immediately before death==.",
             "Rule 50(10)(a): where the deceased is not survived by a widow or widower or a child eligible for family pension, or where the spouse and all children cease to be eligible, family pension at the sub-rule (2) rate shall be payable to the parents for life if the parents were dependent on the servant or pensioner immediately before his or her death.",
             BLUE,
             "Clause das(a): parents tabhi jab koi spouse ya eligible bachcha na ho. Aur shart ye hai ki death se pehle wo dependant the. Phir parents ko life-long family pension."),
            ("10(b) & EXPLANATION",
             "Payable to the ==mother first==, failing which the father. Dependent means combined income ==less than minimum family pension plus DR==.",
             "Rule 50(10)(b): family pension wherever admissible to parents shall be payable to the mother of the deceased, failing which to the father. Explanation: parents shall be deemed to be dependent if their combined income is less than the minimum family pension under sub-rule (2) and the dearness relief admissible thereon. Note the test is on combined income, and the mother has the prior claim.",
             ORANGE,
             "Clause das(b): pehle maa ko, maa na ho to pitaji ko. Explanation dependence define karti hai: combined income minimum family pension plus DR se kam ho. Yaani combined income dekhi jaati hai, aur pehla haq maa ka hai."),
            ("10(c) & 11: SIBLINGS",
             "Parents must give a ==yearly certificate==. Siblings get it ==only if disabled==, wholly dependent, and the disability ==existed before the death==.",
             "Rule 50(10)(c): parents must furnish a yearly certificate that they have not started earning their livelihood, and the pension stops if they do. Rule 50(11)(a): where no spouse, child or parent is eligible, family pension is payable for life to dependent siblings suffering from a mental or physical disability, if they were wholly dependent on the servant or pensioner immediately before death. (b) They are judged by the same disability criteria and conditions as clauses (h) and (i) of sub-rule (9); proviso: the disability must have existed before the death.",
             GREEN,
             "Clause das(c) aur gyarah. Parents ko har saal certificate dena hota hai. Siblings ko pension sirf tab jab wo disabled hon, poori tarah dependent hon, aur disability death se pehle ki ho. Same disability criteria jo clause h aur i mein hai."),
            ("11 EXPLANATION",
             "A disabled sibling is dependent if his overall income is ==less than the entitled family pension plus DR==. A ==yearly certificate== follows.",
             "Explanation to Rule 50(11): a sibling suffering from a mental or physical disability is deemed dependent if his or her overall income from sources other than family pension is less than the entitled family pension under sub-clause (i) of clause (a) of sub-rule (2) plus DR. Rule 50(11)(c): the sibling must furnish a yearly certificate that he or she has not started earning, and the pension stops if he or she does. The general Explanation to the rule then distinguishes the earning tests for children and siblings from those for other family members.",
             PURPLE,
             "Clause gyarah ki Explanation: disabled sibling dependent maana jayega agar family pension ke alawa uski income entitled family pension plus DR se kam ho. Aur clause c kehta hai har saal certificate, warna pension band."),
        ],
        "trap": "<<TRAP:>> Siblings must be ==disabled==. A healthy brother never enters Rule 50, however dependent he is.",
        "trap_say": ("Trap ye hai: siblings disabled hone chahiye. Healthy bhai ya behen Rule fifty mein kabhi nahi aate, chahe kitne bhi dependent hon. "
                     "Wo gratuity ka rule hai, family pension ka nahi."),
        "covers": ["R50-10A", "R50-10B", "R50-10-EXPL", "R50-10C", "R50-11A", "R50-11B", "R50-11B-P1",
                   "R50-11-EXPL", "R50-11C"],
    },
    {
        "id": "b4_34_rule50_12_13",
        "part": "RULE 50(12) AND (13) • TWO PENSIONS, ONE PERSON",
        "title": "TWO FAMILY PENSIONS AT ONCE — THE TWO CEILINGS",
        "accent": ORANGE, "badge": "RULE 50(12)-(13)",
        "crumb": "CHAPTER VIII  •  THE COMBINED CAP",
        "q": "Can a person draw two family pensions, and what is the combined ceiling?",
        "q_say": "Sir, ek person do family pensions le sakta hai, aur combined ceiling kya hai?",
        "heads": [("NOT INCOME", "50(12)(a)", BLUE),
                  ("ITR FIRST", "50(12)(b)", ORANGE),
                  ("Rs 1,25,000", "Two enhanced pensions", GREEN),
                  ("Rs 75,000", "Two ordinary pensions", PURPLE)],
        "boxes": [
            ("12(a): NOT INCOME",
             "A family pension is ==not treated as income== when testing eligibility for another family pension — but the ==sum must stay within the sub-rule (13) limits==.",
             "Rule 50(12)(a): the family pension admissible to a person consequent on the death of a servant or pensioner shall not be considered as income for the purpose of determining eligibility for family pension consequent on the death of another servant or pensioner, subject to the condition that the sum of both family pensions shall not exceed the limits specified in sub-rule (13).",
             BLUE,
             "Clause baarah(a): pehli family pension ko income nahi maana jayega jab doosri family pension ki eligibility check ho rahi hai. Lekin dono ka total clause terah ki limits ke andar rehna chahiye."),
            ("12(b): PROOF",
             "Income proof order: ==Income Tax Return== first, then a ==sub-divisional magistrate certificate==, then any other document the Head of Office accepts.",
             "Rule 50(12)(b)(i): a family member other than the widow or widower must submit, with the claim, a copy of the last Income Tax Return filed. (ii) If he or she has not filed a return, a certificate of income from a sub-divisional magistrate. (iii) If neither is available, the Head of Office may rely on any other document produced in support of the claim and decide eligibility accordingly. The old source material put an employer certificate first; that is not the order in the Rule.",
             ORANGE,
             "Clause baarah(b): proof ka order. Pehle Income Tax Return ki copy. Na ho to sub-divisional magistrate ka income certificate. Wo bhi na ho to Head of Office koi doosra document le sakta hai. Employer certificate pehle nahi aata."),
            ("12(c) & (d)",
             "The claimant must declare in ==Form 10== whether he already draws another family pension, and the Head of Office must ==enforce the cap==.",
             "Rule 50(12)(c): a person claiming family pension shall indicate against the specific column in Form 10 whether or not he or she is already in receipt of a family pension in respect of another servant or pensioner and, if so, its amount. (d) The Head of Office shall take that information into account and ensure that the sum of family pensions does not exceed the limits in sub-rule (13).",
             GREEN,
             "Clause c aur d: claim karte waqt Form ten mein batana padta hai ki doosri family pension mil rahi hai ya nahi, aur kitni. Head of Office ko dekhna hota hai ki total clause terah ki limit ke andar rahe."),
            ("13: THE CAPS",
             "Two ==enhanced== pensions: cap ==Rs 1,25,000==. One enhanced falling to ordinary: still ==Rs 1,25,000==. Both ==ordinary==: cap ==Rs 75,000==.",
             "Rule 50(13): where both wife and husband are Government servants and one dies, family pension is payable to the survivor and, on the survivor's death, the child or children get both family pensions subject to these limits - (i) where the child is eligible to draw two family pensions at the enhanced rate under sub-clause (ii) or (iii), the total is limited to Rs 1,25,000 per month; (ii) where one enhanced pension ceases and the ordinary rate becomes payable in its place, the total is also limited to Rs 1,25,000; (iii) where both are payable at the ordinary rate, the total is limited to Rs 75,000 per month.",
             PURPLE,
             "Clause terah ki teen limits. Dono enhanced ho to ek lakh pachchees hazaar. Ek enhanced khatam ho kar ordinary ho jaye to bhi ek lakh pachchees hazaar. Aur dono ordinary ho to pachattar hazaar. Yahi combined cap hai."),
        ],
        "trap": "<<TRAP:>> The combined cap is ==Rs 75,000== when both pensions are ordinary, but ==Rs 1,25,000== while either is enhanced.",
        "trap_say": ("Trap ye hai: dono ordinary ho to combined cap pachattar hazaar, lekin jab tak koi ek enhanced hai "
                     "tab tak ek lakh pachchees hazaar."),
        "covers": ["R50-12A", "R50-12-B1", "R50-12-B2", "R50-12-B3", "R50-12C", "R50-12D", "FORM-10",
                   "R50-13-I", "R50-13-II", "R50-13-III", "LIMIT-FP-COMBINED-125", "LIMIT-FP-COMBINED-75"],
    },
    {
        "id": "b4_35_rule50_14",
        "part": "RULE 50(14) • MURDER CHARGE IN FAMILY PENSION",
        "title": "THE SUB-RULE THE OLD BUILD MISSED ENTIRELY",
        "accent": RED, "badge": "RULE 50(14)",
        "crumb": "CHAPTER VIII  •  RULE 48'S TWIN",
        "q": "What if the person claiming family pension is charged with the servant's murder?",
        "q_say": "Sir, agar family pension claim karne wale par servant ke murder ka charge ho to kya hota hai?",
        "heads": [("CHARGE", "Pension withheld", BLUE),
                  ("OTHER MEMBER", "Paid meanwhile", ORANGE),
                  ("GUARDIAN BAR", "Spouse cannot act", GREEN),
                  ("ACQUITTAL", "From that date", PURPLE)],
        "boxes": [
            ("14(c): THE CHARGE",
             "Family pension is ==not paid== to a person charged with murdering the servant or ==abetting== it, till the criminal proceedings end.",
             "Rule 50(14)(c): if a person who, in the event of the death of a servant while in service, is eligible to receive family pension under this rule is charged with the offence of murdering the servant or of abetting in the commission of such an offence, the family pension shall not be paid to that person till the conclusion of the criminal proceedings instituted against him. This is the family-pension twin of Rule 48.",
             BLUE,
             "Clause chaudah(c): jo person family pension ka eligible hai, agar uspar servant ke murder ya abetment ka charge ho, to criminal case khatam hone tak usko family pension nahi milegi. Ye Rule forty-eight ka family pension wala jodi hai."),
            ("14(d): WHO GETS IT",
             "The pension is paid to the ==other eligible member== from the day after death. If that member is a ==minor child==, the spouse charged with murder ==cannot act as guardian==.",
             "Rule 50(14)(d): during the period the family pension is not paid to that person, it shall be paid to the other eligible member of the family, if any, from the date following the date of death of the servant. Proviso: if the spouse is charged with murder or abetment and the other eligible member is a minor child, the pension shall be paid through a duly appointed guardian, and the mother or father of the minor child shall not act as guardian for the purpose of drawal of family pension.",
             ORANGE,
             "Clause chaudah(d): jab tak us person ko pension nahi mil rahi, wo doosre eligible member ko milegi, death ke agle din se. Proviso bahut important hai: agar spouse par charge hai aur bachcha minor hai, to spouse guardian nahi ban sakta. Duly appointed guardian chahiye."),
            ("14(e): CONVICTION",
             "Convicted: ==debarred for good==, and the pension continues with the other eligible member.",
             "Rule 50(14)(e)(i): if on conclusion of the proceedings the person is convicted of murder or abetment, such person shall be debarred from receiving family pension, which shall be continued to be paid to the other eligible member of the family, if any. The debarment is permanent, unlike the temporary withholding pending trial.",
             GREEN,
             "Clause chaudah(e)(i): conviction ho jaye to wo hamesha ke liye debar. Family pension doosre eligible member ko milti rahegi. Ye temporary withholding se alag hai, ye permanent debarment hai."),
            ("14(e) & (f): ACQUITTAL",
             "Acquitted: pension to him ==from the date of acquittal==, and the other member's pension is ==discontinued from that date==, with a proviso for the gap.",
             "Rule 50(14)(a): a child claiming family pension shall indicate in Form 10 whether he or she is eligible for another family pension in respect of the other parent and, if so, its amount. (b) The Head of Office shall take that into account and ensure the sum does not exceed the sub-rule (13) limits. (e)(ii) If acquitted, family pension becomes payable to such person from the date of acquittal and the family pension to the other member shall be discontinued from that date. Proviso: if there was no other eligible member, or the other member's pension ceased before the acquittal, the pension is payable to the acquitted person from the date following the death, or from the date the other member's pension ceased, as the case may be. (f) Clauses (c) to (e) also apply to family pension becoming payable on the death of a servant after retirement. Explanation: the charge includes abetting death by suicide.",
             PURPLE,
             "Acquittal par ulta hota hai. Pension usko acquittal ki date se, aur doosre member ki pension usi date se band. Proviso kehta hai agar koi doosra member tha hi nahi, to death ke agle din se milegi. Clause f kehta hai ye retirement ke baad ki death par bhi lagta hai."),
        ],
        "trap": "<<TRAP:>> On acquittal the pension switches ==from the date of acquittal==, not from the date of death — unless no other member ever drew it.",
        "trap_say": ("Trap ye hai: acquittal par pension acquittal ki date se switch hoti hai, death ki date se nahi. "
                     "Haan, agar koi doosra member kabhi tha hi nahi to death ke agle din se."),
        "covers": ["R50-14-A", "R50-14-B", "R50-14-C", "R50-14-D", "R50-14-D-P1", "R50-14-E1",
                   "R50-14-E2", "R50-14-E2-P1", "R50-14-F", "R50-14-EXPL"],
    },
    {
        "id": "b4_36_rule50_15_16",
        "part": "RULE 50(15) AND (16) • FORMS, DISABILITY AND RE-EMPLOYMENT",
        "title": "FORM 4, FORM 5, FORM 10 — AND WHO IS OUTSIDE RULE 50",
        "accent": BLUE, "badge": "RULE 50(15)-(16)",
        "crumb": "CHAPTER VIII  •  THE PAPER TRAIL",
        "q": "Which forms must a servant file, and who is excluded from family pension altogether?",
        "q_say": "Sir, kaun se forms file karne hote hain, aur Rule fifty se kaun bahar hai?",
        "heads": [("FORM 4", "At entry and at retirement", BLUE),
                  ("FORM 5", "Change after retirement", ORANGE),
                  ("FORM 10", "At claim", GREEN),
                  ("EXCLUSION", "50(16)", PURPLE)],
        "boxes": [
            ("15(a) & (b): FORM 4",
             "Form 4 with ==all family details== on entering service, and again ==before retirement==. Any change in the family must be reported.",
             "Rule 50(15)(a)(i): as soon as a servant enters service he shall give details of his family in Form 4 to the Head of Office, including all relevant details of spouse, all children, parents and disabled siblings, whether or not eligible for family pension. (ii) If he has no family, he shall furnish Form 4 as soon as he acquires one. (b) He shall communicate any subsequent change in the size of his family, including the marriage of his child. (e) He shall submit up-to-date family details in Form 4 again with the pension papers before retirement.",
             BLUE,
             "Clause pandrah: Form chaar. Service join karte hi family ki poori detail, spouse, saare bachche, parents, disabled siblings, chahe wo eligible hon ya na hon. Family na ho to family banne par Form chaar. Aur retirement se pehle pension papers ke saath phir Form chaar."),
            ("15(c) & (d): DISABILITY",
             "When a disability ==manifests==, it must be reported with a ==medical certificate== from an RPwD authority or a Medical Board. The Head of Office records it.",
             "Rule 50(15)(c): as and when the disability referred to in Rule 50(9)(h) manifests in a child or dependent sibling, the fact shall be brought to the notice of the Head of Office, supported by a medical certificate from an authority competent to issue a disability certificate under the RPwD Act, 2016 and the Rules of 2017, or from a Medical Board of a Medical Superintendent or Head of Institution with two members, at least one a specialist. (d) The Head of Office shall verify Form 4, acknowledge it with the date of receipt, paste it in the service book and record later changes.",
             ORANGE,
             "Clause pandrah(c) aur (d): jab disability manifest ho, Head of Office ko batana hota hai, RPwD authority ya Medical Board ke certificate ke saath. Head of Office Form chaar verify karke, receipt date ke saath service book mein lagata hai."),
            ("15(f), (g), (h): FORM 5",
             "After retirement, a ==marriage, re-marriage or birth== is intimated in ==Form 5== with the certificate; other changes go by written intimation.",
             "Rule 50(15)(f): where a servant marries or re-marries, or a child is born after retirement, he shall intimate the Head of Office in Form 5 with a copy of the marriage or birth certificate. (g) Where the family undergoes a change after retirement making a member eligible - birth of a child, disability of a child or sibling, divorce of a daughter, death of a daughter's husband - the retired servant, or after his death the spouse or the family pensioner, may intimate the Head of Office with supporting documents. (h) Form 4 must include the spouse, all children including those from a deceased or divorced wife or a void marriage, parents and disabled siblings. (i) A claim shall not be rejected merely because the member is not mentioned in Form 4 or the office records, if the Head of Office is otherwise satisfied about eligibility.",
             GREEN,
             "Clause pandrah(f), (g), (h): retirement ke baad shaadi, re-marriage ya bachche ka janm Form paanch mein, certificate ke saath. Baaki changes written intimation se. Aur clause i raahat deta hai: Form chaar mein naam nahi hai to bhi claim reject nahi hoga, agar Head of Office satisfied hai."),
            ("16: WHO IS OUTSIDE",
             "A ==re-employed== servant who retired from civil or military service, and who on re-employment is ==not eligible for pension or service gratuity== under these rules, is outside Rule 50.",
             "Rule 50(16): nothing contained in this rule shall apply to a re-employed Government servant who had retired from civil service or military service if, on such re-employment, he is not eligible for a pension or service gratuity under these rules. Read it with Rule 52(4): a family pensioner who is employed still draws dearness relief, so exclusion from Rule 50 does not by itself answer the DR question.",
             PURPLE,
             "Clause solah: re-employed servant jo civil ya military service se retire hua tha, aur re-employment par in rules ke under pension ya service gratuity ka eligible nahi hai, wo Rule fifty se bahar hai. Lekin Rule fifty-two chaar alag baat hai, employed family pensioner ko DR milta rehta hai."),
        ],
        "trap": "<<TRAP:>> A missing entry in ==Form 4== is not a ground to reject a claim under ==50(15)(i)==. Eligibility decides, not the register.",
        "trap_say": ("Trap ye hai: Form chaar mein entry nahi hai to claim reject nahi hota, clause pandrah(i) kehta hai. "
                     "Eligibility decide karti hai, register nahi."),
        "covers": ["R50-15A", "R50-15B", "R50-15C", "R50-15D", "R50-15E", "GSR-410E-2024", "FORM-4",
                   "R50-15F", "R50-15G", "FORM-5", "R50-15H", "R50-15I", "R50-16"],
    },
    {
        "id": "b4_37_marital_discord",
        "part": "MARITAL DISCORD • CHILD BEFORE SPOUSE",
        "title": "THE ORDER OF 01.01.2024 — NOT A RULE, STILL BINDING",
        "accent": PINK, "badge": "O.M. 01.01.2024",
        "crumb": "CHAPTER VIII  •  WHEN THE SPOUSE IS THE ACCUSED",
        "q": "If the spouse is accused of the servant's murder, does the child wait for the trial?",
        "q_say": "Sir, agar spouse par servant ke murder ka charge ho, to bachcha trial ka intezaar karega?",
        "heads": [("WRITTEN REQUEST", "From the family", BLUE),
                  ("PENDING CASE", "Charge not decided", ORANGE),
                  ("CHILD PAID", "Family pension", GREEN),
                  ("NO GAZETTE", "Still an order", PURPLE)],
        "boxes": [
            ("THE PROBLEM",
             "==Rule 50(6)== puts the spouse first. ==Rule 50(14)(d)== says a spouse charged with murder cannot be guardian. Between them sits a gap.",
             "Rule 50(6)(i) places the widow or widower first in the queue. Rule 50(14)(d) proviso bars a spouse charged with murder from acting as guardian for a minor child. If the only claimant is the accused spouse, the pension can neither be paid nor be routed through him; the order of 01.01.2024 (S4) fills that gap.",
             PINK,
             "Problem samjho. Rule fifty chhah spouse ko pehle rakhta hai. Rule fifty chaudah(d) kehta hai murder charge wala spouse guardian nahi ban sakta. Beech mein gap hai, aur wahi gap pehli January do hazaar chaubees ka order bharta hai."),
            ("THE REQUEST",
             "If the family makes a ==written request== while the ==criminal case is pending==, the family pension may be paid to the ==eligible child==.",
             "DoPPW O.M. dated 01.01.2024 (S4): where a request in writing is received from the family of the deceased servant while the case against the spouse is pending, family pension may be authorised in favour of the eligible child, subject to the conditions in the order. The payment is provisional in the sense that it depends on the outcome of the trial.",
             BLUE,
             "Order kehta hai: agar parivaar likhit request kare, aur spouse ke against case pending hai, to family pension eligible bachche ko di ja sakti hai. Ye request likhit honi chahiye, oral kaafi nahi."),
            ("THE FIVE CONDITIONS",
             "Written request, pending case, eligible child, ==provisional payment==, and ==adjustment on the outcome==. Miss one and the file comes back.",
             "The order is applied as a package: (i) a written request from the family; (ii) the criminal case against the spouse is pending; (iii) the child is otherwise eligible under Rule 50(9); (iv) payment is provisional and subject to the result of the trial; (v) on the outcome, the position is adjusted - if the spouse is acquitted, Rule 50(14)(e)(ii) takes over and the pension moves to the spouse from the date of acquittal.",
             ORANGE,
             "Paanch conditions saath chalti hain. Likhit request, case pending, bachcha eligible, payment provisional, aur result par adjustment. Ek bhi missing ho to file wapas aayegi. Acquittal ho to Rule fifty chaudah(e) lagta hai."),
            ("THE FLAG",
             "The order says Rule 50 will be ==amended separately==. No such notification was found up to October 2026, so cite the ==O.M.==, not a Rule number.",
             "MARITAL-CODIFIED (unverified): the order records that a formal amendment of Rule 50 will be notified separately. Searches up to 21.10.2026 found no such Gazette notification. Until it appears, the O.M. is the operative instrument and Rule 50(6) still prints the spouse first. Quote the order by date and number in an answer.",
             PURPLE,
             "Flag ye hai: order khud kehta hai Rule fifty alag se amend hoga. October do hazaar chhabbis tak aisa notification nahi mila. Isliye O.M. cite karo, Rule number mat banao. Rule fifty chhah mein spouse aaj bhi pehle likha hai."),
        ],
        "trap": "<<TRAP:>> This is an ==order, not a Rule==. Written request + pending case + eligible child, or the child gets nothing.",
        "trap_say": ("Trap ye hai: ye Rule nahi, order hai. Likhit request, pending case aur eligible bachcha, teeno chahiye, "
                     "warna bachche ko kuch nahi milega."),
        "covers": ["OM-01.01.2024-MARITAL", "MARITAL-5CLAUSES", "MARITAL-CODIFIED", "OM-27.10.2025-TWOWIVES"],
    },
    {
        "id": "b4_38_rule51_start",
        "part": "RULE 51(1) TO (3) • MISSING PERSONS",
        "title": "WHEN A SERVANT, PENSIONER OR FAMILY PENSIONER GOES MISSING",
        "accent": GREEN, "badge": "RULE 51(1)-(3)",
        "crumb": "CHAPTER VIII  •  THREE CLASSES, THREE DATE RULES",
        "q": "If a person goes missing, from which date does family pension start?",
        "q_say": "Sir, agar koi missing ho jaye to family pension kis date se shuru hoti hai?",
        "heads": [("SERVANT", "Three dates, latest", BLUE),
                  ("PENSIONER", "Two dates, later", ORANGE),
                  ("FAMILY PENSIONER", "Two dates, later", GREEN),
                  ("POLICE REPORT", "FIR, DD or GD", PURPLE)],
        "boxes": [
            ("51(1): THE SERVANT",
             "Three dates: the day after ==sanctioned leave ends==; the date up to which ==pay and allowances were paid==; the ==police report== date. Take the ==latest==.",
             "Rule 51(1)(a): where a servant goes missing, family pension is payable at the Rule 50(2) rate, in the manner and subject to the eligibility conditions applicable on death in service. (b) It is payable from the date following the date up to which leave was sanctioned before he went missing, or from the date up to which pay and allowances have been paid, or from the date on which a report was lodged with the police in the form of an FIR, a Daily Diary Entry or a General Diary Entry, whichever is the latest.",
             BLUE,
             "Rule fifty-one ek: missing servant ke liye teen dates. Pehli, sanctioned leave khatam hone ke agle din. Doosri, jis date tak pay and allowances mila. Teesri, police report ki date. Inme se jo sabse baad ki ho, wahi start date. Report FIR, DD ya GD koi bhi ho."),
            ("THE CORRECTION",
             "Only the ==leave== limb says day after. The ==pay== limb is the date up to which pay was paid, not the day after it.",
             "Audit correction: the earlier build wrote the day after for both the leave and the pay limbs. Rule 51(1)(b) says from the date following the date up to which leave was sanctioned, or from the date up to which pay and allowances have been paid, or from the date on which a report has been lodged, whichever is the latest. The words date following attach only to the leave limb. The answer to a worked example usually does not change, but the reasoning must be exact.",
             ORANGE,
             "Ek correction. Pehle build ne pay wali limb mein bhi agla din likh diya tha. Rule kehta hai leave wali limb mein agla din, lekin pay wali limb mein jis date tak pay mila wahi date. Answer badalta nahi, lekin reasoning exact honi chahiye."),
            ("51(2) & (3): THE OTHER TWO",
             "Missing pensioner or family pensioner: only ==two dates== — the day after pension was last paid, or the ==police report== date, ==whichever is later==.",
             "Rule 51(2)(a): if a pensioner goes missing, family pension is payable to an eligible member at the Rule 50(2) rate and on the conditions applicable on the death of a pensioner. (b) Payable from the date following the date up to which pension was paid, or from the date on which the police report was lodged, whichever is later. Rule 51(3) applies the same two-date test to a missing family pensioner, and the pension then moves to the next eligible member.",
             GREEN,
             "Rule fifty-one do aur teen: missing pensioner ya family pensioner ke liye sirf do dates. Pension jis date tak mili uska agla din, ya police report ki date, jo baad mein ho. Family pensioner missing ho to pension agle eligible member ko."),
            ("THE EXAMPLE",
             "Vihaan: leave to 15.06.2025, pay to 20.06.2025, FIR 25.06.2025. Dates ==16, 20 and 25== June. Latest = ==25.06.2025==.",
             "Worked Example (dates recomputed on the corrected reading): leave sanctioned up to 15.06.2025 gives 16.06.2025; pay and allowances paid up to 20.06.2025 gives 20.06.2025; the FIR was lodged on 25.06.2025. The latest is 25.06.2025, so family pension starts on 25.06.2025. The six-month bar under Rule 51(8) then runs to 25.12.2025 and the seven-year date is 25.06.2032.",
             PURPLE,
             "Vihaan ka example. Leave pandrah June tak, to solah June. Pay bees June tak, to bees June. FIR pachchees June ko. Inme sabse baad pachchees June, isliye family pension pachchees June do hazaar pachchees se. Chhah mahine ka bar pachchees December tak."),
        ],
        "trap": "<<TRAP:>> Rule 51 takes the ==LATEST== date for a start. Rule 51(8)(b) takes the ==EARLIER== for death gratuity. Same rule, two directions.",
        "trap_say": ("Trap ye hai: Rule fifty-one start date ke liye latest leta hai, lekin death gratuity ke liye earlier leta hai. "
                     "Ek hi rule, do directions."),
        "covers": ["R51-1A", "R51-1B-DATES", "R51-1B-CORRECT", "R51-POLICE-FORMS", "R51-2", "R51-3", "R51-EX17", "OM-26.10.2022-MISSING"],
    },
    {
        "id": "b4_39_rule51_gratuity",
        "part": "RULE 51(4) TO (7) • GRATUITY, CLAIMS AND THE PAY BASE",
        "title": "WHAT THE FAMILY GETS BESIDES THE PENSION",
        "accent": ORANGE, "badge": "RULE 51(4)-(7)",
        "crumb": "CHAPTER VIII  •  THE REST OF RULE 51",
        "q": "What gratuity is payable when a person goes missing, and what papers are needed?",
        "q_say": "Sir, missing person ke case mein gratuity kya milegi, aur kya papers chahiye?",
        "heads": [("GRATUITY", "51(4)", BLUE),
                  ("CLAIM", "51(5)", ORANGE),
                  ("PAY BASE", "51(6)", GREEN),
                  ("PENSIONER", "51(7)", PURPLE)],
        "boxes": [
            ("51(4): GRATUITY",
             "Retirement gratuity is payable to the family as if the servant ==died after retirement without receiving it==.",
             "Rule 51(4): in the case of a servant who goes missing, or a retired servant who goes missing without receiving the retirement gratuity admissible under Rule 45(1), the retirement gratuity shall be payable to the family in the manner and subject to the conditions applicable in the case of a servant who dies after retirement without receiving the retirement gratuity, that is Rule 47(3) read with Rule 47(1).",
             BLUE,
             "Clause chaar: retirement gratuity parivaar ko milegi, jaise servant retirement ke baad bina gratuity liye guzar gaya ho. Matlab Rule forty-seven teen aur forty-seven ek ka raasta."),
            ("51(5): CLAIM",
             "Claim to the ==Head of Office== after the police report, with an ==Indemnity Bond in Format 8==, a copy of the report, and a police certificate that the person is still untraced.",
             "Rule 51(5)(a): claims for family pension and gratuity shall be submitted to the Head of Office by the eligible family members and nominees or family members eligible for gratuity, after a report has been lodged with the police. (b) The claims shall be accompanied by an Indemnity Bond in Format 8, a copy of the report lodged with the police, and the report obtained from the police that the servant, pensioner or family pensioner could not be traced so far despite all efforts.",
             ORANGE,
             "Clause paanch: claim Head of Office ko, police report ke baad. Saath mein Format aath ka Indemnity Bond, police report ki copy, aur police ka certificate ki ab tak trace nahi hua. Teeno zaroori hain."),
            ("51(6) & (7): THE BASE",
             "For a missing servant, pay for family pension and emoluments for gratuity are taken from the ==last date on duty==, or the date the ==leave expired==.",
             "Rule 51(6): in the case of a missing servant, pay for family pension and emoluments for retirement gratuity shall be determined in accordance with Explanation 1 below Rule 50(2) and Rule 45(6), based on the pay and emoluments on the last date on which he was on duty before he went missing or, if he was on leave, the date on which the leave sanctioned to him expired. (7) In the case of a retired servant, emoluments for retirement gratuity are reckoned under Rule 45(6).",
             GREEN,
             "Clause chhah aur saat: missing servant ke liye pay aur emoluments kis date ke? Jo last date par wo duty par tha, ya leave par tha to leave khatam hone ki date. Retired servant ke liye emoluments Rule forty-five chhah se."),
            ("WHY IT MATTERS",
             "Without 51(6) the family and the office argue about the ==date of pay fixation==. The Rule picks one date and ends the argument.",
             "Rule 51(6) exists because a missing person has no retirement date and no last pay certificate. Fixing the base at the last day on duty, or the day the leave expired, gives the Pay and Accounts Office a determinate figure for both the family pension and the gratuity, and prevents a higher figure being claimed from the date of the police report.",
             PURPLE,
             "Clause chhah kyun hai? Missing person ka na retirement date hai na last pay certificate. Isliye Rule ek date pakadta hai, last day on duty ya leave expiry. Isse family pension aur gratuity dono ka figure fix ho jaata hai."),
        ],
        "trap": "<<TRAP:>> The base date under 51(6) is ==the last day on duty==, not the date of the police report. A later report does not raise the pay.",
        "trap_say": ("Trap ye hai: clause chhah ki base date last day on duty hai, police report ki date nahi. "
                     "Baad ki report se pay nahi badhti."),
        "covers": ["R51-4", "R51-5A", "R51-5B", "FORMAT-8", "R51-6", "R51-7"],
    },
    {
        "id": "b4_40_rule51_bars",
        "part": "RULE 51(8) TO (11) • BARS, INTEREST, ARREARS AND EXCLUSIONS",
        "title": "SIX MONTHS, SEVEN YEARS, AND THE MONEY THAT COMES LATER",
        "accent": YELLOW, "badge": "RULE 51(8)-(11)",
        "crumb": "CHAPTER VIII  •  THE PAYMENT BARS",
        "q": "How long must the family wait, what interest applies, and who is excluded?",
        "q_say": "Sir, parivaar ko kitna intezaar karna padta hai, interest milta hai kya, aur kaun bahar hai?",
        "heads": [("6 MONTHS", "No payment", BLUE),
                  ("7 YEARS", "Death gratuity", ORANGE),
                  ("3 MONTHS", "Difference payment", GREEN),
                  ("RULE 65", "Interest on delay", PURPLE)],
        "boxes": [
            ("8(a): SIX MONTHS",
             "No family pension, no arrears and no gratuity before ==six months from the police report==. Delay beyond six months from the ==claim== attracts ==interest under Rule 65==.",
             "Rule 51(8)(a): the payment of family pension, including arrears from the start date up to the commencement of payment, and the amount of gratuity shall not be made before the expiry of six months from the date of lodging the report with the police. Proviso: if the payment of gratuity is delayed and the delay is attributable to administrative lapses, interest shall be payable for the period of delay beyond six months from the date of submission of the claim, and responsibility shall be fixed, in accordance with Rule 65.",
             BLUE,
             "Clause aath(a): police report se chhah mahine tak family pension, arrears aur gratuity kuch nahi. Aur agar gratuity ke payment mein administrative delay ho, to claim ki date se chhah mahine ke baad interest milega, Rule sixty-five ke hisaab se, aur responsibility fix hogi."),
            ("8(b): SEVEN YEARS",
             "Death gratuity becomes payable when death is ==conclusively established== or ==seven years== pass, ==whichever is earlier==.",
             "Rule 51(8)(b): in the case of a missing servant, death gratuity shall become payable after the death is conclusively established or on the expiry of seven years from the date of lodging the report with the police, whichever is earlier. Note the direction: earlier here, latest in sub-rule (1)(b).",
             ORANGE,
             "Clause aath(b): death gratuity tab jab death conclusively establish ho jaye, ya police report se saat saal poore ho jayein, jo pehle ho. Yahan earlier lagta hai, jabki start date mein latest lagta tha."),
            ("8(c) & (d): THREE MONTHS",
             "The difference between death gratuity and the retirement gratuity already paid is paid within ==three months of the claim==, with interest for later delay.",
             "Rule 51(8)(c): the difference between the amount of death gratuity and retirement gratuity shall be paid to the persons eligible for death gratuity not later than three months from the date of submission of the claim for that difference. (d) If that payment is delayed and the delay is attributable to administrative lapses, interest shall be payable for the period of delay beyond six months from the date of submission of the claim for the difference.",
             GREEN,
             "Clause aath(c) aur (d): death gratuity aur pehle di gayi retirement gratuity ka difference claim se teen mahine ke andar. Aur agar wo delay ho, to claim se chhah mahine ke baad interest."),
            ("9 TO 11: THE REST",
             "Also paid: ==pay arrears, leave salary, its cash equivalent and GPF==. But not where ==fraud== is under investigation, and never to a ==non-family member==.",
             "Rule 51(9): in addition to family pension and retirement gratuity, the family is entitled to arrears of pay and allowances or leave salary, cash equivalent to leave salary, and the amount in the General Provident Fund, as applicable on death in service. (10) Nothing in Rule 51 applies where the person disappears and an allegation of fraud or embezzlement or any other crime is under investigation, or he has been charged or convicted for such crimes. (11) No payment under the rule shall be authorised to a person other than a member or members of the family eligible to receive it.",
             PURPLE,
             "Clause nau se gyarah: arrears of pay, leave salary, leave salary ka cash equivalent, aur GPF bhi milega. Lekin fraud ya embezzlement ki investigation ho, ya charge ho chuka ho, to Rule fifty-one lagta hi nahi. Aur payment sirf eligible family member ko, kisi aur ko nahi."),
        ],
        "trap": "<<TRAP:>> The six-month bar runs from the ==police report==; the interest clock runs from the ==claim==. Two different starting points.",
        "trap_say": ("Trap ye hai: chhah mahine ka bar police report se chalta hai, aur interest ka clock claim se. "
                     "Do alag starting points."),
        "covers": ["R51-8A", "TL-R51-6M", "R51-8A-P1", "R51-INTEREST", "R51-8B", "TL-R51-7Y",
                   "R51-8C", "TL-R51-3M-DIFF", "R51-8D", "R51-9", "R51-10", "R51-11"],
    },
    {
        "id": "b4_41_rule52",
        "part": "RULE 52 • DEARNESS RELIEF",
        "title": "RULE 52 — WHO GETS DR, AND WHO LOSES IT ON RE-EMPLOYMENT",
        "accent": TEAL, "badge": "RULE 52",
        "crumb": "CHAPTER IX  •  DEARNESS RELIEF",
        "q": "Who is entitled to dearness relief, and when does re-employment take it away?",
        "q_say": "Sir, dearness relief kisko milta hai, aur re-employment par kab band ho jaata hai?",
        "heads": [("PENSIONERS", "And family pensioners", BLUE),
                  ("RE-EMPLOYED", "DR stops", ORANGE),
                  ("GROUP A", "No relief", GREEN),
                  ("CERTIFICATE", "Three limbs", PURPLE)],
        "boxes": [
            ("52(1): THE GRANT",
             "Money against price rise, at rates the ==Central Government== fixes. For pensioners, compassionate allowance holders and ==family pensioners==.",
             "Rule 52(1): relief against price rise may be granted to pensioners, including persons drawing compassionate allowance under Rule 41, and to family pensioners, in the form of dearness relief at such rates and subject to such conditions as the Central Government may specify from time to time. The rate is nowhere in the Rule; it comes from periodic O.M.s, so the Rule is only the enabling power.",
             BLUE,
             "Rule fifty-two ek: mehngai ke against relief, Central Government jo rate aur condition tay kare. Pensioners, compassionate allowance wale, aur family pensioners, sabko. Rate Rule mein nahi hai, wo O.M. se aata hai."),
            ("52(2): RE-EMPLOYMENT",
             "Re-employed under the Central or State Government, or a corporation, company, body or bank under them, in India or abroad, including ==absorption==: ==no DR== during that period.",
             "Rule 52(2): if a pensioner drawing pension or compassionate allowance is re-employed under the Central Government or a State Government, or a corporation, company, body or bank under them, in India or abroad, including permanent or immediate absorption in such body, he shall not be eligible to draw dearness relief on the pension or compassionate allowance during the period of such re-employment or absorption.",
             ORANGE,
             "Clause do: agar pensioner Central ya State Government ke under, ya unke corporation, company, body ya bank mein re-employed ho, India ya bahar, permanent ya immediate absorption bhi shamil, to us period mein DR nahi milega."),
            ("THE PROVISO: GROUP A",
             "DR continues only if ==all three== pass: no ==Group A== post; pay at the ==scale minimum==, below his old pay; and the ==whole pension ignored==.",
             "Proviso to Rule 52(2): dearness relief shall continue to be payable on re-employment, permanent absorption or immediate absorption if (i) before such re-employment he was not holding a post included or classified as Group A; (ii) in accordance with the relevant rules or orders his pay was fixed at the minimum of the scale of pay of the re-employed post and that minimum was less than the pay he was drawing immediately before retirement or absorption; and (iii) while fixing his pay the entire amount of pension sanctioned by the Central Government was ignored.",
             GREEN,
             "Proviso ke teen tests. Pehla: pehle Group A post par nahi tha. Doosra: re-employed post ki pay scale ke minimum par pay fix hui, aur wo minimum retirement se pehle ki pay se kam tha. Teesra: pay fixation mein poori pension ignore hui. Teeno pass ho to DR chalta rahega."),
            ("52(3) & (4): CERTIFICATE",
             "The employer's certificate must cover the ==three limbs==. But a ==family pensioner== who is employed ==keeps DR==.",
             "Rule 52(3): to claim DR while re-employed or absorbed, the pensioner must obtain a certificate from the department, office, corporation, company, body or bank stating (i) he was holding a civil post not included or classified as Group A before such re-employment; (ii) his pay was fixed at the minimum of the scale and that minimum was less than the pay drawn immediately before retirement or absorption; and (iii) the entire pension was ignored in fixation and no part of it was taken into account. Rule 52(4): sub-rules (2) and (3) do not apply to a family pensioner who is employed and eligible to draw family pension; such a person continues to be eligible for DR on family pension.",
             PURPLE,
             "Clause teen: certificate chahiye, aur usme teen baatein likhi hon. Clause chaar: family pensioner jo employed hai, uspar clause do aur teen lagte hi nahi, usko family pension par DR milta rahega. Ye bahut important exception hai."),
        ],
        "trap": "<<TRAP:>> A ==family pensioner== keeps DR even while employed (52(4)). Only the ==pensioner== loses it on re-employment (52(2)).",
        "trap_say": ("Trap ye hai: family pensioner employed hone par bhi DR leta hai, clause chaar. Sirf pensioner ka DR "
                     "re-employment par band hota hai, clause do."),
        "covers": ["R52-1", "R52-1-COMP", "R52-2", "R52-2-PROV", "R52-2-PROV-I", "R52-2-PROV-II", "R52-2-PROV-III",
                   "R52-3", "R52-4"],
    },
    {
        "id": "b4_42_dr_currency",
        "part": "THE DR RATE TODAY AND HOW CURRENT THIS BUILD IS",
        "title": "SIXTY PER CENT FROM 1 JANUARY 2026 — AND WHAT COMES NEXT",
        "accent": PURPLE, "badge": "DR • 2026",
        "crumb": "CHAPTER IX  •  DYNAMIC FIGURES",
        "q": "What is the current DR rate, and which figures must I re-check before an exam?",
        "q_say": "Sir, aaj DR ka rate kya hai, aur exam se pehle kaun se figures dobara check karne chahiye?",
        "heads": [("60 PER CENT", "From 01.01.2026", BLUE),
                  ("NOVEMBER", "Annual certificate", ORANGE),
                  ("JULY 2026", "Not announced", GREEN),
                  ("8th CPC", "Report due 2027", PURPLE)],
        "boxes": [
            ("THE RATE",
             "DR is ==60 per cent== from 01.01.2026. The July 2026 revision had ==not been announced== by mid-October 2026.",
             "The last confirmed dearness relief rate is 60 per cent with effect from 01.01.2026 (S7, DoPPW circular of 22.04.2026). Searches in October 2026 found no order revising DR from 01.07.2026. Treat 60 per cent as the working figure and check the newest O.M. before quoting it, because DR moves twice a year.",
             BLUE,
             "Aaj ka rate: pehli January do hazaar chhabbis se saath percent. July do hazaar chhabbis ki revision October tak announce nahi hui thi. Exam mein saath percent likho, lekin saath hi likho ki newest O.M. check karna hai, kyunki DR saal mein do baar badalta hai."),
            ("THE PROGRESSION",
             "Only the ==58 to 60== step was confirmed in this build. Earlier steps were not read, so do not recite a full history.",
             "DR-PROGRESSION (partly unverified): the build confirms the step to 60 per cent from 01.01.2026. Earlier steps in the source podcast were not verified against orders, so the cards teach the current rate and the principle, not a sequence of historical percentages. A full history belongs in an appendix once each O.M. is read.",
             ORANGE,
             "Progression ka sirf fifty-aath se saath wala step confirm hua. Pehle ke steps verify nahi hue, isliye poora history mat sunao. Current rate aur principle padhao, history baad mein."),
            ("THE ANNUAL CERTIFICATE",
             "A ==certificate in November== each year: employed or not. Miss it, and ==DR from December may stop== while the pension continues.",
             "Practice under Rule 52: the pensioner furnishes a certificate of non-employment or of employment or re-employment, including absorption, under the Central or State Government or a corporation, company, body or bank, in the month of November each year. If the certificate is not submitted, banks may stop crediting the DR element from December onwards while continuing to credit the pension. Where employment is declared with emoluments that include dearness allowance, Rule 52 is enforced.",
             GREEN,
             "Practical point. Pensioner ko har saal November mein certificate dena hota hai, ki wo employed hai ya nahi. Na de to bank December se DR dena band kar sakta hai, pension chalta rahega. Aur agar employment declare ho aur usme DA shamil ho, to Rule fifty-two lagta hai."),
            ("WHAT TO RE-CHECK",
             "Four dynamic figures: ==DR rate==, ==gratuity ceiling==, ==pension floor and ceiling==, ==family pension ceilings==. All four move by order, not by amendment.",
             "Dynamic figures in this batch: the DR rate (60 per cent from 01.01.2026); the gratuity ceiling (Rs 25 lakh by O.M. of 30.05.2024, Rule text still Rs 20 lakh); the pension floor and ceiling (Rs 9,000 and Rs 1,25,000, inside Rule 44(1), exposed to the 8th CPC); the family pension ordinary ceiling Rs 75,000 and enhanced ceiling Rs 1,25,000 inside Rule 50; and the earning limit Rs 14,400 used in practice for income tests. Quoting any of them without a date is an incomplete answer.",
             PURPLE,
             "Chaar dynamic figures yaad rakho. DR rate, gratuity ceiling, pension floor aur ceiling, aur family pension ceilings. Ye chaar order se badalte hain, amendment se nahi. Kisi bhi figure ko date ke bina quote karna adhoora answer hai."),
        ],
        "trap": "<<TRAP:>> DR is ==not part of pension==. It is an add-on at a rate fixed by order, and it can be ==withheld== for a re-employed pensioner.",
        "trap_say": ("Trap ye hai: DR pension ka hissa nahi hai. Wo order se tay hone wala add-on hai, "
                     "aur re-employed pensioner ke liye rok diya ja sakta hai."),
        "covers": ["DR-60-2026", "OM-22.04.2026-DR", "OM-24.04.2026-DOPPW-DR", "DR-PROGRESSION", "DR-JULY2026",
                   "DR-NOV-CERT", "NOCHANGE-42-52", "GSR-340E-2025", "NEW-8CPC"],
    },
    {
        "id": "b4_43_recap",
        "part": "RECAP • EVERY NUMBER IN ONE TABLE",
        "title": "THE BATCH IN ONE SCREEN — NUMBERS, TRAPS AND THE NEXT STEP",
        "accent": GREEN, "badge": "RECAP",
        "crumb": "CHAPTER X  •  WHAT COMES NEXT",
        "q": "Can you give me every number and every trap in one go?",
        "q_say": "Sir, saare numbers aur saare traps ek saath mil sakte hain?",
        "heads": [("NUMBERS", "Learn these", BLUE),
                  ("TRAPS", "Avoid these", ORANGE),
                  ("CURRENCY", "Checked to Oct 2026", GREEN),
                  ("NEXT", "Rules 53 to 70", PURPLE)],
        "table": {
            "title": "Every figure in Rules 42 to 52",
            "head": ["Rule", "Figure", "What it governs"],
            "w": [1.3, 3.2, 8.4],
            "rows": [
                ["42", "30 years, 3 months", "Premature retirement, with notice or pay in lieu"],
                ["43", "20 years, 15 days", "Voluntary retirement, certificate and withdrawal"],
                ["44(1)", "10 years, 50 per cent", "Pension, floor Rs 9,000, ceiling Rs 1,25,000"],
                ["44(6)", "20/30/40/50/100", "Additional pension at 80/85/90/95/100"],
                ["44(8)", "9 years 9 months", "Treated as ten years for pension"],
                ["45(1)(a)", "5 years, 1/4, 16.5x", "Retirement gratuity"],
                ["45(1)(b)", "2/6/12/20, then 33x", "Death gratuity, no five-year condition"],
                ["45(3)", "12 times, 5 years", "Residuary gratuity"],
                ["45 and 50", "Rs 25 lakh", "Gratuity ceiling, O.M. of 30.05.2024"],
                ["50(2)", "30 and 50 per cent", "Ordinary and enhanced family pension"],
                ["50(13)", "1,25,000 and 75,000", "Combined cap for two family pensions"],
                ["51(8)", "6 months, 7 years", "Payment bar and death gratuity"],
                ["52", "60 per cent", "Dearness relief from 01.01.2026"],
            ],
        },
        "boxes": [
            ("THE NUMBERS",
             "==30 and 20== years. ==50 per cent== pension. ==1/4== per half year, ==16.5== times. ==2/6/12/20/33==. ==30 and 50== per cent.",
             "Rule 42: thirty years. Rule 43: twenty years. Rule 44: ten years, fifty per cent, floor Rs 9,000, ceiling Rs 1,25,000; service gratuity half a month per half year; additional pension 20/30/40/50/100 at 80/85/90/95/100; near miss nine years nine months. Rule 45: one-fourth per half year, 16.5 times, five years; death gratuity 2/6/12/20 then 33 times; residuary twelve times within five years; near miss four years nine months. Rule 50: thirty per cent and fifty per cent, ceilings Rs 75,000 and Rs 1,25,000. Rule 51: six months and seven years. Rule 52: sixty per cent from 01.01.2026.",
             BLUE,
             "Numbers ek saath. Tees aur bees saal, pachaas percent pension, chauthai aur solah point paanch guna, do chhah baarah bees tetees, tees aur pachaas percent family pension, chhah mahine aur saat saal, aur saath percent DR."),
            ("THE TRAPS",
             "No ==60 per cent== slab. No rounding for the ==twenty years==. ==Group 1 blocks Group 2==. Family pension age is the ==pensioner's==. ==Latest== date, not earlier.",
             "Ten traps: (1) additional pension has no sixty per cent slab; (2) Rule 43(1) fourth proviso switches off the Rule 44(7) rounding; (3) nine years nine months saves pension, four years nine months saves gratuity, and they are different; (4) death gratuity needs no five years and the third slab ends at eleven years; (5) Group 1 excludes the whole of Group 2 and brothers are under eighteen; (6) the age for additional family pension is the family pensioner's; (7) enhanced family pension is seven years or age sixty-seven, whichever is less; (8) Rule 51 takes the latest date, but death gratuity takes the earlier; (9) Rule 48 suspends, Rule 49 lapses; (10) DR is not part of pension and a family pensioner keeps it while employed.",
             ORANGE,
             "Das traps. Saath percent ka slab nahi, twenty saal par rounding nahi, Group one Group two ko block karta hai, family pension mein pensioner ki age, Rule fifty-one latest leta hai lekin death gratuity earlier, Rule forty-eight suspend karta hai aur Rule forty-nine lapse, aur DR pension ka hissa nahi."),
            ("THE CURRENCY",
             "Checked to ==21.10.2026==. Six items remain ==flagged== on their cards. Read the flag before you teach the card.",
             "Currency statement: Rules 42 to 52 were read clause by clause from a faithful reproduction of G.S.R. 868(E) (S1); the Gazette PDF itself was not opened, so wording is a close restatement. Flagged items: the July 2026 DR revision; Gazette codification of the marital-discord order and of the Rs 25 lakh ceiling; the 8th CPC effect on the floor and ceiling; G.S.R. 775(E) seen only indirectly; and the historical DR sequence before 60 per cent.",
             GREEN,
             "Currency: twenty-first October do hazaar chhabbis tak check kiya. Rule ka text ek faithful reproduction se padha, Gazette PDF khud nahi kholi, isliye wording close restatement hai. Chhah items par flag laga hua hai, padhane se pehle flag padho."),
            ("WHAT NEXT",
             "Batch 5: ==Chapter X, Rules 53 to 70== — Bhavishya, the retirement list, the PPO timeline, and Rule 56's earlier-date rule.",
             "Next batch: Chapter X, Rules 53 to 70, determination and authorisation of pension and gratuity - Rule 53 processing through Bhavishya, Rule 54 the retirement list prepared by the 15th of every month for the next fifteen months, Rule 55 the No Demand Certificate from the Directorate of Estates, and the pension papers timeline of Rules 56 to 70, including Rule 56, which the source contrasts with Rule 51 on the earlier and later date tests.",
             PURPLE,
             "Agla batch: Chapter ten, Rules fifty-three se seventy. Bhavishya, retirement list, No Demand Certificate, aur PPO ki timeline. Rule fifty-six bhi, jise Rule fifty-one se compare karte hain, earlier aur later date ke liye."),
        ],
        "trap": "<<RECAP:>> ==30/20 years== • ==50 per cent== • ==16.5 times== • ==33 times== • ==30/50 per cent== • ==6 months and 7 years== • ==60 per cent DR==.",
        "trap_say": ("Recap: tees aur bees saal, pachaas percent, solah point paanch guna, tetees guna, tees aur pachaas percent, "
                     "chhah mahine aur saat saal, aur saath percent DR."),
        "covers": ["RECAP4", "NEW-GSR-775E-2026", "NEW-NO-42-52-AMEND", "NEW-GRAT-RULE-AMEND", "MAP4"],
    },
]


# ============================================================================
# STATUTORY TREE - every provision of Rules 42 to 52 that must be taught
# ----------------------------------------------------------------------------
# The --audit run proves, mechanically, that each tag below is present in at
# least one scene's "covers" list. Nothing is checked by eye.
# ============================================================================
RULE_TREE = {
    "42": [
        ("42(1) thirty years, public interest, retiring pension", "R42-1"),
        ("42(1) thirty-year threshold", "LIMIT-R42-30Y"),
        ("42(2) three months notice or pay in lieu", "R42-2"),
        ("42(2) three-month notice window", "TL-R42-NOTICE-3M"),
        ("42(3) procedure laid down for FR 56", "R42-3"),
        ("42 Explanation: appointing authority", "R42-EXPL"),
    ],
    "43": [
        ("43(1) twenty years, three months notice", "R43-1"),
        ("43(1) twenty-year threshold", "LIMIT-R43-20Y"),
        ("43(1) first proviso: certificate before notice", "R43-1-P1"),
        ("43(1) first proviso: fifteen-day limit", "TL-R43-CERT-15D"),
        ("43(1) second proviso: authority must satisfy itself", "R43-1-P2"),
        ("43(1) third proviso: ITEC, foreign office, foreign contract", "R43-1-P3"),
        ("43(1) third proviso: one year in India after return", "TL-R43-ONEYR"),
        ("43(1) fourth proviso: Rule 44(7) rounding switched off", "R43-1-P4"),
        ("43(1) fourth proviso: no rounding label", "TL-R43-NOROUND"),
        ("43(2) notice requires acceptance", "R43-2"),
        ("43(2) proviso: silence means acceptance on expiry", "R43-2-P1"),
        ("43(3) power to withhold permission", "R43-3"),
        ("43(3)(i) suspension", "R43-3-I"),
        ("43(3)(ii) charge sheet and disciplinary proceedings", "R43-3-II"),
        ("43(3)(iii) judicial proceedings", "R43-3-III"),
        ("43(3) proviso: President's approval", "R43-3-P1"),
        ("43(3) Explanation: when judicial proceedings are pending", "R43-3-EXPL"),
        ("43(4)(a) request for shorter notice with reasons", "R43-4"),
        ("43(4)(b) no commutation before three months", "R43-4-COMMUTE"),
        ("43(5) disability under section 20 RPwD Act", "R43-5"),
        ("43(6) withdrawal only with specific approval", "R43-6"),
        ("43(6) proviso: fifteen days before the date", "TL-R43-WITHDRAW-15D"),
        ("43(7)(a) Special VRS surplus employees", "R43-7"),
        ("43 Explanation: appointing authority", "R43-EXPL"),
    ],
    "44": [
        ("44(1) fifty per cent of the better base", "R44-1"),
        ("44(1) fifty per cent rate", "LIMIT-R44-50"),
        ("44(1) minimum pension Rs 9,000", "LIMIT-PENSION-FLOOR"),
        ("44(1) maximum pension Rs 1,25,000", "LIMIT-PENSION-CEIL"),
        ("44(1) proviso: invalid pension under Rule 39(9)", "R44-1-P1"),
        ("44(1) eligible for grant is not sanction", "R44-1-ELIGIBLE"),
        ("44(2) service gratuity, half month per half year", "R44-2"),
        ("44(2) half-month rate", "LIMIT-R44-SG-HALF"),
        ("44(3) reduced emoluments and dearness allowance", "R44-3"),
        ("44(4)(a) compulsory retirement pension", "R44-4A"),
        ("44(4)(b) compulsory retirement service gratuity", "R44-4B"),
        ("44(5)(a) compassionate allowance on pension", "R44-5A"),
        ("44(5)(b) compassionate allowance on service gratuity", "R44-5B"),
        ("rule 41 two-thirds cap on compassionate allowance", "R41-CAP"),
        ("44(6) additional pension, five slabs", "R44-6"),
        ("44(6) slab 80 to under 85", "R44-6-SLAB-80"),
        ("44(6) slab 85 to under 90", "R44-6-SLAB-85"),
        ("44(6) slab 90 to under 95", "R44-6-SLAB-90"),
        ("44(6) slab 95 to under 100", "R44-6-SLAB-95"),
        ("44(6) slab 100 and above", "R44-6-SLAB-100"),
        ("44(6) base is basic pension", "R44-6-BASE"),
        ("44(6)(b) first day of the calendar month", "R44-6-DAY"),
        ("44(6) illustration of 20.08.1942 and 01.08.1942", "R44-6-ILLUS"),
        ("44(7) three months equals a six-monthly period", "R44-7"),
        ("44(7) rounding of three months", "TL-R44-ROUND-3M"),
        ("44(8) nine years nine months treated as ten", "R44-8"),
        ("44(8) near miss label", "TL-R44-NEARMISS-9Y9M"),
        ("44(9) whole rupees, rounded up", "R44-9"),
        ("44(10) mid-month discontinuation", "R44-10"),
        ("44(3) dearness allowance as emoluments", "R44-DA-EMOL"),
    ],
    "45": [
        ("45(1)(a) retirement gratuity, one-fourth", "R45-1A"),
        ("45(1)(a) five years qualifying service", "LIMIT-RG-5Y"),
        ("45(1)(a) 16.5 times cap", "LIMIT-RG-CAP165"),
        ("45(1)(a) cap reached at 33 half-years", "LIMIT-RG-33HALF"),
        ("45(1)(a) worked example", "R45-EX1"),
        ("45(1) first proviso: twenty lakh in the Rule text", "R45-1-P1"),
        ("45(1) first proviso: Rs 25 lakh ceiling by order", "LIMIT-GRATUITY-CEILING"),
        ("45(1)(b) slab less than one year", "R45-1B-SLAB1"),
        ("45(1)(b) slab one to under five years", "R45-1B-SLAB2"),
        ("45(1)(b) slab five to under eleven years", "R45-1B-SLAB3"),
        ("45(1)(b) slab eleven to under twenty years", "R45-1B-SLAB4"),
        ("45(1)(b) slab twenty years and above", "R45-1B-SLAB5"),
        ("45(1)(b) no five-year condition", "R45-1B-NO5YR"),
        ("45(1)(b) worked example", "R45-1B-EX"),
        ("45(2) death by suicide", "R45-2"),
        ("45(3) residuary gratuity", "R45-3"),
        ("45(3) twelve times emoluments", "LIMIT-RESID-12X"),
        ("45(3) five-year window", "TL-R45-3-5YR"),
        ("45(3) worked example", "R45-3-EX"),
        ("45(4) three-month fraction", "R45-4"),
        ("45(5) four years nine months treated as five", "R45-5"),
        ("45(5) gratuity near miss label", "TL-R45-NEARMISS-4Y9M"),
        ("45(6) emoluments under Rule 31", "R45-6"),
        ("45(6) first proviso: average emoluments", "R45-6-P1"),
        ("45(6) second proviso: dearness allowance", "R45-6-P2"),
        ("45(1) second proviso: rounding of a rupee", "R45-RUPEE"),
        ("45(6) Explanation: family, clause (i)", "R45-EXPL-FAMILY"),
        ("45(6) Explanation: group 1, clauses (i) to (v)", "R45-EXPL-G1"),
        ("45(6) Explanation: group 2, clauses (vi) to (xi)", "R45-EXPL-G2"),
        ("45(6) Explanation: married daughters in clause (x)", "R45-EXPL-G3"),
        ("the four gratuities compared", "R45-FOURTYPES"),
    ],
    "46": [
        ("46(1) nomination in Form 3", "R46-1"),
        ("Form 3", "FORM-3"),
        ("46(2) nomination within or outside the family", "R46-2"),
        ("46(3) shares must cover the whole gratuity", "R46-3"),
        ("46(4)(i) alternate nominee", "R46-4"),
        ("46(4)(i) first proviso: alternate must be family", "R46-4-P1"),
        ("46(4)(i) second proviso: single member family", "R46-4-P2"),
        ("46(4)(ii) nomination invalid on a stated contingency", "R46-4-II"),
        ("46(5)(a) nomination fails on acquiring a family", "R46-5A"),
        ("46(5)(b) alternate fails when a member is added", "R46-5B"),
        ("46(6) marriage does not cancel", "R46-6"),
        ("46(7) cancellation with a fresh nomination", "R46-7"),
        ("46(8) notice on the death of a nominee", "R46-8"),
        ("46(9)(a) nomination to the Head of Office", "R46-9A"),
        ("46(9)(b) verification and countersignature", "R46-9B"),
        ("46(9)(c) entry in the service book", "R46-9C"),
        ("46(9)(d) signed copy returned", "R46-9D"),
        ("46(10) effect from the date of receipt", "R46-10"),
        ("46(10) effective-date label", "R46-EFFECTIVE"),
    ],
    "47": [
        ("47(1)(a) payment to the nominee", "R47-1A"),
        ("47(1)(b) payment where there is no nomination", "R47-1B"),
        ("47(1)(b)(i) group 1 in equal shares", "R47-GROUP1"),
        ("47(1)(b)(ii) group 2 in equal shares", "R47-GROUP2"),
        ("47(1)(b) group 1 excludes group 2", "R47-STRICT"),
        ("47(2) pre-deceased nominee's share", "R47-2"),
        ("47(2) test date is the date of death", "R47-2-DATETEST"),
        ("47(3) death after retirement without receiving gratuity", "R47-3"),
        ("47(4) marriage or age 18 after death", "R47-4"),
        ("47(5) minor through the guardian", "R47-5"),
        ("47(6) natural guardian and guardianship certificate", "R47-6"),
        ("47(7) twenty per cent on an indemnity bond", "R47-7"),
        ("Indemnity Bond Format 7", "FORMAT-7"),
        ("47(8) claims processed independently", "R47-8"),
        ("Form 9", "FORM-9"),
    ],
    "48": [
        ("48(1) suspension of the claim", "R48-1"),
        ("48(2)(a) conviction debars", "R48-2A"),
        ("48(2)(b) acquittal pays", "R48-2B"),
        ("48(3) undisbursed gratuity", "R48-3"),
        ("48 Explanation: abetting suicide", "R48-EXPL"),
    ],
    "49": [
        ("49 lapse where there is no family and no nomination", "R49-1"),
        ("49 proviso: Succession Certificate", "R49-SUCC"),
        ("49 scope: death in service or after retirement", "R49-SCOPE"),
    ],
    "50": [
        ("50(1)(i) one year of continuous service", "R50-1-I"),
        ("50(1)(ii) medically examined before one year", "R50-1-II"),
        ("50(1)(iii) death after retirement in receipt of pension", "R50-1-III"),
        ("50(1) date following the date of death", "R50-1-DATE"),
        ("50(1) one-year gateway label", "LIMIT-FP-1Y"),
        ("50(2)(a)(i) thirty per cent ordinary rate", "R50-2A-I"),
        ("50(2)(a)(i) ordinary rate label", "LIMIT-FP-ORD-RATE"),
        ("50(2)(a)(i) minimum Rs 9,000", "LIMIT-FP-ORD-FLOOR"),
        ("50(2)(a)(i) maximum Rs 75,000", "LIMIT-FP-ORD-CEIL"),
        ("50(2)(a)(ii) fifty per cent for ten years", "R50-2A-II"),
        ("50(2)(a)(ii) ten-year window label", "TL-FP-ENH-10Y"),
        ("50(2)(a)(iii) seven years or age 67", "R50-2A-III"),
        ("50(2)(a)(iii) seven-year or age-67 label", "TL-FP-ENH-7Y-67"),
        ("50(2)(a)(iv) maximum Rs 1,25,000", "LIMIT-FP-ENH-CEIL"),
        ("50(2)(a)(iii) first proviso: cap at authorised pension", "R50-2A-III-P1"),
        ("50(2)(a)(iii) second proviso: floor of the 30 per cent amount", "R50-2A-III-P2"),
        ("50(2) Explanation 1: pay", "R50-2A-EXPL1"),
        ("50(2) Explanation 2: commuted part", "R50-2A-EXPL2"),
        ("50(2) Explanation 3: compulsory retirement and compassionate allowance", "R50-2A-EXPL3"),
        ("50(2)(b) drop to the ordinary rate", "R50-2B"),
        ("50(3)(a) additional family pension slabs", "R50-3"),
        ("50(3)(a) five slab values", "R50-3-SLABS"),
        ("50(3)(b) first day of the calendar month", "R50-3-DAY"),
        ("50(3) illustration", "R50-3-ILLUS"),
        ("50(4) rounding and maximum", "R50-4"),
        ("50(4) proviso: never above the maximum", "R50-4-P1"),
        ("50(5)(a) EOP award bars family pension", "R50-5A"),
        ("50(5)(b) EOP claim under consideration", "R50-5B"),
        ("50(5)(c) no limitation for other service", "R50-5C"),
        ("50(6) order of precedence", "R50-6"),
        ("50(6)(i) widow or widower", "R50-6-I"),
        ("50(6)(ii) children", "R50-6-II"),
        ("50(6)(iii) dependent parents", "R50-6-III"),
        ("50(6)(iv) dependent disabled siblings", "R50-6-IV"),
        ("50(6) Explanation: legally wedded spouse", "R50-6-EXPL"),
        ("50(7)(a) one member at a time", "R50-7A"),
        ("50(7)(b) equal shares", "R50-7B"),
        ("50(7)(b) proviso: maximum on rounding", "R50-7B-P1"),
        ("50(8)(a) spouse till death or re-marriage", "R50-8A"),
        ("50(8)(b) childless widow who re-marries", "R50-8B"),
        ("50(8)(b) proviso: income test", "R50-8B-P1"),
        ("50(8)(c) more widows than one", "R50-8C"),
        ("50(8)(d) widow without a child", "R50-8D"),
        ("50(8)(e) children of another wife who is not alive", "R50-8E"),
        ("50(8)(f) children of a divorced wife", "R50-8F"),
        ("50(8) equal shares label", "R50-8-EQ"),
        ("50(8)(g) children of a void or voidable marriage", "R50-8G"),
        ("50(8)(h) judicially separated, no child", "R50-8H"),
        ("50(8)(i) judicially separated, minor child", "R50-8I"),
        ("50(8)(i) proviso: child attains majority", "R50-8I-P1"),
        ("50(8)(j) judicially separated, major eligible child", "R50-8J"),
        ("50(8)(k) childless widow's annual certificate", "R50-8K"),
        ("50(8)(k) Explanation: earning her livelihood", "R50-8K-EXPL"),
        ("50(9)(a)(i) son under 25, unmarried, not earning", "R50-9-SON"),
        ("50(9)(a)(i) age 25 label", "TL-FP-SON-25"),
        ("50(9)(a)(ii) daughter unmarried, widowed or divorced", "R50-9-DAUGHTER"),
        ("50(9)(a)(iii) disabled son or daughter", "R50-9-DISABLED"),
        ("50(9)(b) earning test for an ordinary child", "R50-9-EARN"),
        ("50(9)(c) earning test for a disabled child", "R50-9-EARN-DISABLED"),
        ("practice income limit Rs 14,400 label", "LIMIT-FP-INCOME-14400"),
        ("50(9)(d) children below 25 in birth order", "R50-9-D"),
        ("50(9)(e) elder child till 25, marriage or earning", "R50-9-E"),
        ("50(9)(f) minor through the guardian", "R50-9-F"),
        ("50(9)(g) twin children", "R50-9-G"),
        ("50(9)(h) disabled child for life", "R50-9-H"),
        ("50(9)(h)(i) disability existed before death", "R50-9-H-C1"),
        ("50(9)(h)(ii) other children first", "R50-9-H-C2"),
        ("50(9)(h)(v) competent authority or Medical Board", "R50-9-H-C5"),
        ("50(9)(h)(vi) continuing certificate", "R50-9-H-C6"),
        ("50(9)(h)(vii) nominated guardian and National Trust", "R50-9-H-C7"),
        ("50(9)(i) marriage of a disabled child", "R50-9-I"),
        ("50(9)(j) daughter beyond twenty-five", "R50-9-J"),
        ("50(9)(j)(i) children first till the last turns 25", "R50-9-J-C1"),
        ("50(9)(j)(ii) no disabled child eligible", "R50-9-J-C2"),
        ("50(9)(j)(iii) dependence", "R50-9-J-C3"),
        ("50(9)(j)(iv) birth order among daughters", "R50-9-J-C4"),
        ("50(9)(j)(v) elder daughter till marriage or earning", "R50-9-J-C5"),
        ("50(9)(j)(vi) widowed or divorced during the lifetime", "R50-9-J-C6"),
        ("50(9)(j) first proviso: divorce date", "R50-9-J-P1"),
        ("50(9)(j) second proviso: earlier member", "R50-9-J-P2"),
        ("50(9)(k) children of more than one mother", "R50-9-K"),
        ("50(9)(l) more than one child of such a mother", "R50-9-L"),
        ("50(9)(m) shares do not lapse", "R50-9-M"),
        ("50(9) Explanation: posthumous child", "R50-9-M-EXPL"),
        ("50(9)(n) ineligible from the date of marriage", "R50-9-N"),
        ("50(9)(o) pension stops on earning", "R50-9-O"),
        ("50(9)(p) annual certificate", "R50-9-P"),
        ("50(10)(a) parents for life", "R50-10A"),
        ("50(10)(b) mother first, then father", "R50-10B"),
        ("50(10) Explanation: dependent parents", "R50-10-EXPL"),
        ("50(10)(c) parents' annual certificate", "R50-10C"),
        ("50(11)(a) dependent disabled siblings", "R50-11A"),
        ("50(11)(b) same criteria as clause (h)", "R50-11B"),
        ("50(11)(b) proviso: disability before death", "R50-11B-P1"),
        ("50(11) Explanation: sibling income test", "R50-11-EXPL"),
        ("50(11)(c) sibling's annual certificate", "R50-11C"),
        ("50(12)(a) family pension is not income", "R50-12A"),
        ("50(12)(b)(i) Income Tax Return", "R50-12-B1"),
        ("50(12)(b)(ii) sub-divisional magistrate certificate", "R50-12-B2"),
        ("50(12)(b)(iii) any other document", "R50-12-B3"),
        ("50(12)(c) Form 10 declaration", "R50-12C"),
        ("Form 10", "FORM-10"),
        ("50(12)(d) Head of Office enforces the cap", "R50-12D"),
        ("50(13)(i) two enhanced pensions capped at 1,25,000", "R50-13-I"),
        ("50(13)(ii) enhanced falling to ordinary", "R50-13-II"),
        ("50(13)(iii) two ordinary pensions capped at 75,000", "R50-13-III"),
        ("combined ceiling Rs 1,25,000", "LIMIT-FP-COMBINED-125"),
        ("combined ceiling Rs 75,000", "LIMIT-FP-COMBINED-75"),
        ("50(14)(a) Form 10 for the other parent", "R50-14-A"),
        ("50(14)(b) Head of Office checks both parents", "R50-14-B"),
        ("50(14)(c) murder charge withholds family pension", "R50-14-C"),
        ("50(14)(d) paid to the other eligible member", "R50-14-D"),
        ("50(14)(d) proviso: guardian bar", "R50-14-D-P1"),
        ("50(14)(e)(i) conviction debars", "R50-14-E1"),
        ("50(14)(e)(ii) acquittal from that date", "R50-14-E2"),
        ("50(14)(e)(ii) proviso: no other member", "R50-14-E2-P1"),
        ("50(14)(f) death after retirement", "R50-14-F"),
        ("50(14) Explanation: abetting suicide", "R50-14-EXPL"),
        ("50(15)(a) Form 4 at entry", "R50-15A"),
        ("50(15)(b) change in the family", "R50-15B"),
        ("50(15)(c) disability certificate", "R50-15C"),
        ("50(15)(d) Head of Office records Form 4", "R50-15D"),
        ("50(15)(e) Form 4 with the pension papers", "R50-15E"),
        ("Form 4", "FORM-4"),
        ("50(15)(f) Form 5 after retirement", "R50-15F"),
        ("50(15)(g) change of family after retirement", "R50-15G"),
        ("Form 5", "FORM-5"),
        ("50(15)(h) contents of Form 4", "R50-15H"),
        ("50(15)(i) claim not to be rejected for a missing entry", "R50-15I"),
        ("50(16) re-employed servant excluded", "R50-16"),
    ],
    "51": [
        ("51(1)(a) missing servant, rate and conditions", "R51-1A"),
        ("51(1)(b) three dates, whichever is latest", "R51-1B-DATES"),
        ("51(1)(b) pay limb is not the day after", "R51-1B-CORRECT"),
        ("51(1)(b) FIR, Daily Diary or General Diary", "R51-POLICE-FORMS"),
        ("51(2) missing pensioner", "R51-2"),
        ("51(3) missing family pensioner", "R51-3"),
        ("51(1)(b) worked example", "R51-EX17"),
        ("51(4) retirement gratuity to the family", "R51-4"),
        ("51(5)(a) claim after the police report", "R51-5A"),
        ("51(5)(b) Indemnity Bond and police report", "R51-5B"),
        ("Indemnity Bond Format 8", "FORMAT-8"),
        ("51(6) pay and emoluments on the last day on duty", "R51-6"),
        ("51(7) retired servant, emoluments under Rule 45(6)", "R51-7"),
        ("51(8)(a) six-month bar", "R51-8A"),
        ("51(8)(a) six-month label", "TL-R51-6M"),
        ("51(8)(a) proviso: interest under Rule 65", "R51-8A-P1"),
        ("interest on delayed gratuity", "R51-INTEREST"),
        ("51(8)(b) seven years or proof of death, whichever is earlier", "R51-8B"),
        ("51(8)(b) seven-year label", "TL-R51-7Y"),
        ("51(8)(c) difference within three months", "R51-8C"),
        ("51(8)(c) three-month label", "TL-R51-3M-DIFF"),
        ("51(8)(d) interest on the difference", "R51-8D"),
        ("51(9) arrears, leave salary and GPF", "R51-9"),
        ("51(10) fraud or embezzlement exclusion", "R51-10"),
        ("51(11) no payment to a non-family member", "R51-11"),
    ],
    "52": [
        ("52(1) dearness relief, rate fixed by the Central Government", "R52-1"),
        ("52(1) compassionate allowance holders included", "R52-1-COMP"),
        ("52(2) no DR during re-employment or absorption", "R52-2"),
        ("52(2) proviso: three tests", "R52-2-PROV"),
        ("52(2) proviso (i) Group A post", "R52-2-PROV-I"),
        ("52(2) proviso (ii) minimum of the scale", "R52-2-PROV-II"),
        ("52(2) proviso (iii) pension ignored", "R52-2-PROV-III"),
        ("52(3) employer's certificate", "R52-3"),
        ("52(4) family pensioner keeps DR while employed", "R52-4"),
    ],
}

# Non-statutory material carried on the cards: Gazette layers, O.M.s and labels.
EXTRA_TAGS = {
    "MAP4": "batch map",
    "GSR-868E-2021": "principal Rules, G.S.R. 868(E) dated 20.12.2021",
    "GSR-770E-2022": "G.S.R. 770(E) dated 07.10.2022 - Rules 46(5)(a) and 50(9)(h)(iii)",
    "GSR-410E-2024": "G.S.R. 410(E) dated 16.07.2024 - Rule 50(15)(e)",
    "GSR-340E-2025": "G.S.R. 340(E) dated 22.05.2025 - does not touch Rules 42-52",
    "OM-30.05.2024-GRAT": "O.M. 28/03/2024-P&PW(B)/Gratuity/9559 dated 30.05.2024 - Rs 25 lakh",
    "OM-30.10.2025-COMP": "O.M. 38/10(03)/2025-P&PW(A) dated 30.10.2025 - Rule 44(4)",
    "OM-30.10.2025-ADDL": "O.M. dated 30.10.2025 - additional pension payable month",
    "OM-24.10.2025-COVERAGE": "O.M. dated 24.10.2025 - coverage",
    "OM-24.10.2025-ELIG": "O.M. dated 24.10.2025 - eligibility",
    "NPSG-258E-2025": "CCS (Payment of Gratuity under NPS) Rules, 2021, G.S.R. 258(E)",
    "OM-01.01.2024-MARITAL": "DoPPW O.M. dated 01.01.2024 - marital discord",
    "MARITAL-5CLAUSES": "the five conditions of that order",
    "MARITAL-CODIFIED": "no Gazette codification found up to 21.10.2026",
    "OM-27.10.2025-TWOWIVES": "O.M. dated 27.10.2025 - enhanced family pension rate",
    "OM-26.10.2022-MISSING": "O.M. 1/1(1)/2022-P&PW(E) dated 26.10.2022 - Rule 51",
    "DR-60-2026": "60 per cent from 01.01.2026",
    "OM-22.04.2026-DR": "DR order of 22.04.2026",
    "OM-24.04.2026-DOPPW-DR": "DoPPW DR circular of 24.04.2026",
    "DR-PROGRESSION": "DR progression, partly unverified",
    "DR-JULY2026": "July 2026 revision not announced",
    "DR-NOV-CERT": "annual certificate in November",
    "NOCHANGE-42-52": "no amendment of Rules 42-52 found after G.S.R. 410(E)",
    "NEW-8CPC": "8th CPC constituted 03.11.2025",
    "NEW-GSR-775E-2026": "G.S.R. 775(E) of 2026 - outside this batch",
    "NEW-NO-42-52-AMEND": "no amendment of Rules 42-52",
    "NEW-GRAT-RULE-AMEND": "gratuity ceiling amendment still awaited",
    "RECAP4": "recap",
}

AUDIT_SCENES = {s["id"]: s for s in SCENES}


def flatten_ledger():
    rows = []
    for rule in sorted(RULE_TREE, key=int):
        for clause, tag in RULE_TREE[rule]:
            rows.append((rule, clause, tag))
    return rows


def coverage_index():
    idx = {}
    for s in SCENES:
        for tag in s["covers"]:
            idx.setdefault(tag, []).append(s["id"])
    return idx


# ============================================================================
# FRAME
# ============================================================================
def render_frame(scene, idx, total, reveal, kind, out_path=None):
    img, d = background()
    acc = scene["accent"]
    n = len(scene["boxes"])

    y = header(d, scene, idx, total)
    d.line([(70, y - 6), (W - 70, y - 6)], fill=BORDER, width=2)
    y = question_line(d, scene, y + 2) + 6

    if scene.get("heads"):
        draw_heads(d, scene["heads"], 70, y, W - 140, acc, 1 if reveal >= 1 else 0)
        y += 108

    bottom = H - 112
    if "table" in scene:
        spec = scene["table"]
        shown = 0 if reveal <= 0 else max(1, round(reveal * len(spec["rows"]) / max(n, 1)))
        draw_table(d, spec, 70, y, W - 140, bottom - y, shown, acc)
    elif "chart" in scene:
        spec = scene["chart"]
        shown = 0 if reveal <= 0 else max(1, round(reveal * len(spec["bars"]) / max(n, 1)))
        draw_chart(d, spec, 70, y, W - 140, bottom - y, shown, acc)
    elif "compare" in scene:
        draw_compare(d, scene["compare"], 70, y, W - 140, bottom - y, reveal, acc)
    else:
        rows = [(b[0], b[3], b[1]) for b in scene["boxes"]]
        draw_rows(d, rows, 70, y, W - 140, bottom - y, reveal, acc, label_w=330)

    if reveal >= n - 1 or kind == "hook":
        draw_trap(d, scene["trap"])
    footer(d, idx, total, reveal, n, scene)

    if out_path is not None:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        img.save(out_path)
    return img


# ============================================================================
# AUDIT
# ============================================================================
def _syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and n > 1:
        n -= 1
    return max(1, n)


def readability(text):
    """Flesch Reading Ease on the English on-screen text."""
    plain = strip_rich(text)
    sentences = max(1, len(re.findall(r"[.!?;:]", plain)) or 1)
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", plain)
    if len(words) < 12:
        # Flesch is not meaningful on a six-word label; report a neutral score.
        return 60.0, len(words) / sentences, 0.0
    syl = sum(_syllables(w) for w in words)
    fre = 206.835 - 1.015 * (len(words) / sentences) - 84.6 * (syl / len(words))
    long_words = sum(1 for w in words if _syllables(w) > 3)
    return fre, len(words) / sentences, long_words / len(words)


HINDI_MARKERS = {
    "hai", "hain", "ho", "hota", "hoti", "hoga", "hogi", "hua", "hui", "nahi", "na",
    "aur", "ya", "yaani", "matlab", "lekin", "kyunki", "kyonki", "jab", "tab", "phir",
    "bhi", "sirf", "ka", "ki", "ke", "ko", "mein", "se", "par", "wala", "wali", "wale",
    "kya", "kaun", "kaise", "kitna", "kitni", "kab", "kahan", "dekho", "samjho", "yaad",
    "rakho", "bolo", "suno", "chahiye", "padega", "padta", "padti", "sakte", "sakta",
    "sakti", "milta", "milti", "milega", "milegi", "karta", "karti", "karte", "hoga",
    "rahega", "rahegi", "rahe", "dena", "lena", "aata", "aati", "jaata", "jaati", "ab",
    "toh", "to", "hi", "ek", "do", "teen", "saal", "mahine", "paisa", "paise", "baat",
    "cheez", "alag", "saath", "andar", "bahar", "upar", "neeche", "baad", "pehle",
    "saath", "hazaar", "lakh", "crore", "guna", "banta", "banti", "hota", "hoti",
    "ek", "do", "teen", "chaar", "paanch", "chhah", "saat", "aath", "nau", "das",
    "bees", "tees", "chalees", "pachaas", "saath", "pachattar", "nabbe", "sau",
    "barah", "pandrah", "pachchees", "tetees", "aadha", "pauna", "poore", "puri",
    "wajah", "tarah", "hisaa", "hissa", "bant", "bantta", "milta", "milti",
}


def hinglish_score(text):
    toks = [t.lower() for t in LATIN_WORD.findall(text)]
    if not toks:
        return 0.0
    hits = sum(1 for t in toks if t in HINDI_MARKERS)
    return hits / len(toks)


def row_metrics(sc):
    """(label, chosen body px, number of lines) for every row of a scene."""
    img, d = background()
    n = len(sc["boxes"])
    out = []
    if "table" in sc or "chart" in sc or "compare" in sc:
        return out
    label_w = 300
    avail_h = (H - 112) - (86 + 2 * 46 + 78 + 106 + 40)
    per = (avail_h - 12 * (n - 1)) / n
    for _lab, short, _full, _c, _nar in sc["boxes"]:
        r = Rich(short)
        r.fit(d, (W - 140) - label_w - 12 - 46, per - 22, ROW_START, ROW_MIN, 1.30)
        out.append((strip_rich(short)[:44], r.size, len(r.lines)))
    return out


def audit_density():
    bad = []
    print("=" * 96)
    print("DENSITY / LAYOUT AUDIT - rendering the densest frame of every chapter")
    print("=" * 96)
    for i, sc in enumerate(SCENES, 1):
        n = len(sc["boxes"])
        try:
            render_frame(sc, i, len(SCENES), n, "hook", None)
            print(f"  {i:02d} {sc['id']:<34} rows={n:<2} table={'Y' if 'table' in sc else '-'} "
                  f"chart={'Y' if 'chart' in sc else '-'}  OK")
        except ValueError as exc:
            bad.append((sc["id"], str(exc)))
            print(f"  {i:02d} {sc['id']:<34} OVER BUDGET -> {exc}")
    tight = []
    print("\n  rows that dropped below 30px or ran past two lines:")
    for i, sc in enumerate(SCENES, 1):
        for txt, size, nlines in row_metrics(sc):
            if size < 30 or nlines > 2:
                tight.append((sc["id"], txt, size, nlines))
                print(f"    {i:02d} {sc['id']:<34} {size}px x{nlines}  {txt!r}")
    print(f"  tight rows: {len(tight)}")
    return bad


def audit_coverage():
    print()
    print("=" * 96)
    print("COVERAGE AUDIT - every provision of Rules 42 to 52")
    print("=" * 96)
    idx = coverage_index()
    missing = []
    for rule in sorted(RULE_TREE, key=int):
        items = RULE_TREE[rule]
        gaps = [(c, t) for c, t in items if t not in idx]
        missing += gaps
        flag = "OK" if not gaps else f"MISSING {len(gaps)}"
        print(f"  Rule {rule:<3} provisions {len(items):>3}   covered {len(items)-len(gaps):>3}   {flag}")
        for clause, tag in gaps:
            print(f"        - {tag:<28} {clause}")
    orphans = sorted(set(idx) - {t for _r, _c, t in flatten_ledger()} - set(EXTRA_TAGS))
    print(f"\n  statutory provisions tracked : {len(flatten_ledger())}")
    print(f"  provisions without a card    : {len(missing)}")
    print(f"  unexplained tags             : {len(orphans)}")
    for o in orphans:
        print(f"        - {o}")
    return missing, orphans


def audit_content():
    print()
    print("=" * 96)
    print("CONTENT AUDIT - readability, Hinglish, script purity, duplicates")
    print("=" * 96)
    bad = []
    for sc in SCENES:
        for label, short, full, _c, nar in sc["boxes"]:
            fre, wps, longf = readability(short)
            hs = hinglish_score(nar)
            if DEVANAGARI.search(nar) or DEVANAGARI.search(short) or DEVANAGARI.search(full):
                bad.append((sc["id"], label, "DEVANAGARI in text"))
            if fre < 18:
                bad.append((sc["id"], label, f"obscure on-screen text (Flesch {fre:.0f})"))
            if hs < 0.10:
                bad.append((sc["id"], label, f"narration may not be Hinglish (score {hs:.2f})"))
        for k in ("q", "q_say", "trap", "trap_say"):
            if DEVANAGARI.search(sc.get(k, "")):
                bad.append((sc["id"], k, "DEVANAGARI"))
    scores = []
    for sc in SCENES:
        for _l, short, _f, _c, _n in sc["boxes"]:
            scores.append(readability(short)[0])
    print(f"  cards                 : {len(scores)}")
    print(f"  mean Flesch ease      : {sum(scores)/len(scores):.1f}  (higher is plainer)")
    print(f"  hardest card          : {min(scores):.0f}")
    for b in bad:
        print(f"  ISSUE {b[0]} / {b[1]}: {b[2]}")
    return bad


def write_audit_report(path=Path("pension_b4_audit_report.md")):
    idx = coverage_index()
    L = ["# Audit report - CCS (Pension) Rules 2021, Batch 4 (Rules 42-52)",
         "", "Generated by `build_pension_b4.py --audit`. Every line below is machine-checked against the",
         "`covers` tags in the scene data; nothing is asserted by hand.", "",
         "## 1. Provision-by-provision coverage", "",
         "| Rule | Provision | Tag | Chapter(s) | Status |", "|---|---|---|---|---|"]
    for rule in sorted(RULE_TREE, key=int):
        for clause, tag in RULE_TREE[rule]:
            where = ", ".join(f"c{SCENES.index(AUDIT_SCENES[s])+1:02d}" for s in idx.get(tag, []))
            status = "covered" if tag in idx else "**MISSING**"
            L.append(f"| {rule} | {clause} | `{tag}` | {where} | {status} |")
    L += ["", "## 2. Chapter map", "", "| # | Chapter | Rule focus | Cards |", "|---|---|---|---|"]
    for i, sc in enumerate(SCENES, 1):
        L.append(f"| {i} | {sc['part']} | {sc['badge']} | {len(sc['boxes'])} |")
    L += ["", "## 3. Readability of the on-screen text", ""]
    vals = [(sc["id"], readability(b[1])[0]) for sc in SCENES for b in sc["boxes"]]
    L.append(f"Mean Flesch Reading Ease: **{sum(v for _i, v in vals)/len(vals):.1f}** "
             f"(min {min(v for _i, v in vals):.0f}, max {max(v for _i, v in vals):.0f}).")
    L += ["", "## 4. Items that remain unverified", "",
          "- Gazette PDF of G.S.R. 868(E) not opened; wording is a close restatement from a faithful reproduction.",
          "- DR revision from 01.07.2026 not announced as of mid-October 2026.",
          "- No Gazette codification of the 01.01.2024 marital-discord order or of the Rs 25 lakh ceiling.",
          "- 8th CPC report pending; floor and ceiling may move.",
          "- G.S.R. 775(E) of 2026 seen only through an earlier batch note.",
          "- Historical DR percentages before the 60 per cent step not verified order by order."]
    path.write_text("\n".join(L) + "\n", encoding="utf-8")
    return path


# ============================================================================
# ASSEMBLY CHECKS AND DERIVED DATA
# ============================================================================
def assign_chapter_numbers():
    for i, sc in enumerate(SCENES, 1):
        sc["chapter"] = f"CHAPTER {i:02d}  •  {sc['part']}"
        sc.setdefault("crumb", "CCS (PENSION) RULES 2021  •  BATCH 4")


def validate_scenes():
    assert len({s["id"] for s in SCENES}) == len(SCENES), "duplicate scene id"
    for sc in SCENES:
        assert sc["boxes"], f"{sc['id']}: no boxes"
        assert len(strip_rich(sc["trap"])) < 190, f"{sc['id']}: trap strip too long"
        assert len({b[0] for b in sc["boxes"]}) == len(sc["boxes"]), f"{sc['id']}: duplicate label"
        for b in sc["boxes"]:
            assert len(b) == 5, f"{sc['id']}: box must be a 5-tuple"
            if DEVANAGARI.search(" ".join(str(x) for x in b[:4])):
                raise ValueError(f"{sc['id']}: Devanagari in on-screen text")
            if DEVANAGARI.search(b[4]):
                raise ValueError(f"{sc['id']}: Devanagari in narration -> {b[4][:60]!r}")
        for k in ("q", "q_say", "trap", "trap_say", "title", "part"):
            assert sc.get(k), f"{sc['id']}: missing {k}"
            assert not DEVANAGARI.search(sc[k]), f"{sc['id']}: Devanagari in {k}"


assign_chapter_numbers()
validate_scenes()

FULL = {}
for _sc in SCENES:
    for (_label, _short, _full, _c, _nar) in _sc["boxes"]:
        FULL[(_sc["id"], _label)] = _full


def write_reference_sheet(path=Path("pension_b4_reference_sheet.md")):
    out = ["# CCS (Pension) Rules 2021 - Batch 4 - Rules 42-52",
           "", "Full-wording reference sheet. Every on-screen row is a short key point; the examinable",
           "wording behind it is here, in the same order as the video.", ""]
    for i, sc in enumerate(SCENES, 1):
        out += [f"## {i:02d}. {sc['part']}", f"**{sc['title']}**  ({sc['badge']})", "",
                f"Q: {sc['q']}", ""]
        for (label, short, _f, _c, _n) in sc["boxes"]:
            out += [f"### {label}", f"*On screen:* {strip_rich(short)}", "",
                    FULL[(sc["id"], label)], ""]
        out += [f"> {strip_rich(sc['trap'])}", ""]
    path.write_text("\n".join(out), encoding="utf-8")
    return path


# ============================================================================
# SEGMENTS / AUDIO / SUBTITLES
# ============================================================================
def build_segments(scene):
    """(speaker, text, reveal_index, kind) - reveal drives the slide state."""
    n = len(scene["boxes"])
    segs = []
    if scene.get("intro"):
        segs.append(("teacher", scene["intro"], 0, "intro"))
    segs.append(("student", scene["q_say"], 0, "question"))
    for i, b in enumerate(scene["boxes"]):
        segs.append(("teacher", b[4], i + 1, "answer"))
    segs.append(("teacher", scene["trap_say"], n, "hook"))
    return segs


def probe_duration(path: Path) -> float:
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)], text=True).strip()
    return float(out)


def silent_audio(text: str, out: Path) -> float:
    dur = max(1.5, len(text.split()) / 2.6)
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono",
                    "-t", f"{dur:.2f}", "-c:a", "libmp3lame", str(out)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return dur


async def tts_segment(text, voice, out: Path, rate, sem):
    import edge_tts
    text = normalize_for_tts(text)
    async with sem:
        last = None
        for attempt in range(4):
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
            except Exception as e:            # noqa: BLE001 - retry any transport error
                last = e
                await asyncio.sleep(1.5 * (attempt + 1))
        raise RuntimeError(f"edge-tts failed for {out.name}: {last}")


def fmt_ass(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def write_ass(cues, path: Path):
    head = (
        "[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, "
        "BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, "
        "Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
        "Style: Default,DejaVu Sans,38,&H00FFFFFF,&H0000E6FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,160,160,84,1\n"
        "Style: Student,DejaVu Sans,38,&H0042E4F0,&H0000E6FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,160,160,84,1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"
    )
    lines = [head]
    for s, e, style, txt in cues:
        lines.append(f"Dialogue: 0,{fmt_ass(s)},{fmt_ass(e)},{style},,0,0,0,,{txt}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def make_cues(words, offset, style, chunk=8):
    cues, buf = [], []
    for w in words:
        buf.append(w)
        if len(buf) >= chunk or w[0].endswith((".", "?", "!", ":")):
            cues.append((offset + buf[0][1], offset + buf[-1][2] + 0.12, style,
                         " ".join(x[0] for x in buf)))
            buf = []
    if buf:
        cues.append((offset + buf[0][1], offset + buf[-1][2] + 0.15, style,
                     " ".join(x[0] for x in buf)))
    return cues


def even_words(text, dur):
    toks = text.split()
    step = dur / max(len(toks), 1)
    return [(t, i * step, (i + 1) * step) for i, t in enumerate(toks)]


# ============================================================================
# MAIN
# ============================================================================
async def main():
    global SCENES, OUTPUT_MP4
    ap = argparse.ArgumentParser(description="CCS Pension Rules 2021 - Batch 4 video compiler")
    ap.add_argument("--audit", action="store_true", help="coverage + density + content audit, then exit")
    ap.add_argument("--preview", action="store_true", help="render slides only (no ffmpeg, no network)")
    ap.add_argument("--no-tts", action="store_true", help="silent timing run (needs ffmpeg)")
    ap.add_argument("--list", action="store_true", help="print the chapter map and exit")
    ap.add_argument("--teacher", default=DEFAULT_TEACHER)
    ap.add_argument("--student", default=DEFAULT_STUDENT)
    ap.add_argument("--rate", default="-4%")
    ap.add_argument("--part", type=int, choices=[1, 2, 3],
                    help="1 = chapters 1-15, 2 = 16-30, 3 = 31-end")
    args = ap.parse_args()

    if args.list:
        for i, sc in enumerate(SCENES, 1):
            print(f"{i:02d}  {sc['part']:<62} {sc['badge']}")
        return

    if args.audit:
        write_reference_sheet()
        density = audit_density()
        missing, orphans = audit_coverage()
        content = audit_content()
        rep = write_audit_report()
        print()
        print("=" * 96)
        print("VERDICT")
        print("=" * 96)
        print(f"  density failures          : {len(density)}")
        print(f"  statutory gaps            : {len(missing)}")
        print(f"  unexplained tags          : {len(orphans)}")
        print(f"  content issues            : {len(content)}")
        print(f"  report                    : {rep.resolve()}")
        ok = not density and not missing and not orphans and not content
        print(f"  {'PASS - the batch is complete and within budget' if ok else 'FAIL - fix the items above'}")
        sys.exit(0 if ok else 1)

    write_reference_sheet()
    for d in (BUILD_DIR, SLIDES_DIR, AUDIO_DIR):
        d.mkdir(parents=True, exist_ok=True)

    if args.part:
        cuts = [0, 15, 30, len(SCENES)]
        SCENES = SCENES[cuts[args.part - 1]:cuts[args.part]]
        OUTPUT_MP4 = Path(f"{OUT_STEM}_part{args.part}.mp4")
    total = len(SCENES)

    print(f"=== Step 1: rendering {total} chapters ===")
    jobs = []
    for si, sc in enumerate(SCENES):
        for gi, (who, text, reveal, kind) in enumerate(build_segments(sc)):
            sp = SLIDES_DIR / f"{sc['id']}_{gi:02d}_{kind}.png"
            render_frame(sc, si + 1, total, reveal, kind, sp)
            jobs.append((si, who, text, kind, reveal, sp,
                         AUDIO_DIR / f"{sc['id']}_{gi:02d}.mp3"))
        print(f"  {si+1:02d}/{total}  {sc['id']}")
    if args.preview:
        print(f"Preview frames: {SLIDES_DIR.resolve()}")
        return

    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        sys.exit("ERROR: ffmpeg/ffprobe not on PATH (use --preview or --audit)")

    print(f"\n=== Step 2: narration ({'SILENT TEST' if args.no_tts else args.student + ' / ' + args.teacher}) ===")
    words_by_job = {}
    if not args.no_tts:
        try:
            import edge_tts  # noqa: F401
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "edge-tts"])
        sem = asyncio.Semaphore(4)
        tasks = [tts_segment(t, args.student if who == "student" else args.teacher, mp3, args.rate, sem)
                 for (_, who, t, _, _, _, mp3) in jobs]
        results = await asyncio.gather(*tasks)
        for i, w in enumerate(results):
            words_by_job[i] = w

    print("\n=== Step 3: building clips ===")
    clips, cues, cursor = [], [], 0.0
    for i, (si, who, text, kind, reveal, sp, mp3) in enumerate(jobs):
        if args.no_tts:
            sd = silent_audio(text, mp3)
            words = even_words(normalize_for_tts(text), sd)
        else:
            sd = probe_duration(mp3)
            words = words_by_job[i] or even_words(text, sd)
        dur = sd + (0.9 if kind in ("question", "hook", "intro") else 0.5)
        clip = BUILD_DIR / f"clip_{i:03d}.mp4"
        subprocess.run([
            "ffmpeg", "-y", "-loop", "1", "-framerate", "5", "-i", str(sp), "-i", str(mp3),
            "-af", "apad", "-t", f"{dur:.3f}",
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast",
            "-g", "60", "-r", "30", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(clip)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cues += make_cues(words, cursor, "Student" if who == "student" else "Default")
        clips.append(clip)
        cursor += dur
    print(f"  {len(clips)} clips | timeline {cursor/60:.2f} min")

    print("\n=== Step 4: concat + burn subtitles ===")
    concat = BUILD_DIR / "concat.txt"
    concat.write_text("\n".join(f"file '{c.name}'" for c in clips) + "\n", encoding="utf-8")
    raw = BUILD_DIR / "raw_concat.mp4"
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
                    "-c", "copy", str(raw)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ass = BUILD_DIR / "subtitles.ass"
    write_ass(cues, ass)
    ass_esc = str(ass).replace("\\", "/").replace(":", "\\:")
    subprocess.run([
        "ffmpeg", "-y", "-i", str(raw), "-vf", f"subtitles='{ass_esc}'",
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(OUTPUT_MP4)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    dur = probe_duration(OUTPUT_MP4)
    info = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height",
         "-of", "csv=p=0", str(OUTPUT_MP4)], text=True).split()
    print("\n=== Step 5: verification ===")
    print("streams:", info)
    print(f"DONE: {OUTPUT_MP4.resolve()}  |  {dur/60:.2f} min  |  "
          f"{OUTPUT_MP4.stat().st_size/1048576:.1f} MB")
    if not any(s.startswith("audio") for s in info):
        print("WARNING: no audio stream found!")


if __name__ == "__main__":
    asyncio.run(main())
