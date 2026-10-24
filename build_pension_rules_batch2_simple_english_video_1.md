# CCS (Pension) Rules 2021 - Batch 2 - Rules 11-30: Qualifying Service - English-on-screen, Hinglish-narration video compiler (Python script)

Scope: Part 2 (Batch 2): CCS (Pension) Rules 2021, Chapter III Qualifying Service, Rules 11 to 30, plus the amendments and the Sept 2025 DoPPW O.M. that touch it. 34 chapters (28 teaching, 5 revision-visual, 1 recap), 226 narration segments, explanation only, recap at the end.

**Revision 3 (24 October 2026) - language.** On screen everything stays in English: chapter pills, card titles, row text, tables, chart labels and trap strips. Every narration segment is now **Hinglish in Roman script**, the way a classroom in an Indian city actually explains, with rule numbers, dates and legal terms kept in English. No Devanagari script anywhere in the file.

**Revision 2 (24 October 2026) - clause-level audit of the whole chapter.** Read the companion note `PENSION_B2_CLAUSE_AUDIT.md` for the rule-by-rule verdict table. In short: 20 rules, 81 statutory units, all 81 taught. Rule 14(2) and the Explanation to Rule 14 were missing in substance and are now filled; the Rule 15 notifying authority, Rule 26(8) and "on each occasion" in Rule 30(1) are no longer flagged because the text was read. The visuals were rebuilt to the reference screenshot's banded style (violet chapter pill, coloured header panels, full-width label rows, amber trap strip, three revision tables, one bar chart), with one row revealed per narration segment.

Save the code block as `build_pension_b2.py` and run it as described in its docstring.

````python
#!/usr/bin/env python3
"""
CCS (Pension) Rules 2021 - Batch 2 - Rules 11-30: Qualifying Service
ENGLISH-ON-SCREEN, HINGLISH-NARRATION Q&A EXPLANATION MASTERCLASS COMPILER - 34 chapters. Scope: Part 2 (Batch 2): CCS (Pension) Rules 2021, Chapter III Qualifying Service,
Rules 11 to 30, plus the amendments and the Sept 2025 DoPPW O.M. that touch it. Explanation only, recap and revision tables at the end.
=====================================================================================================
SOURCES READ / CHECKED IN THIS BUILD:
  * FULL CHAPTER III TEXT (Rules 11 to 30, every sub-rule, proviso and Explanation read end to end), GConnect reproduction:
    https://www.gconnect.in/orders-in-brief/pension/qualifying-service-central-civil-services-pension-rules-2021.html
    [This is the source of the clause-level audit of 24.10.2026. It is a reproduction, not the Gazette PDF.]
  * https://www.staffnews.in/wp-content/uploads/2021/12/CSS_PensionRules_2021_Book_Eng.pdf
  * https://www.gconnect.in/orders-in-brief/pension/central-civil-services-pension-rules-2021-updated-pension-rules.html
  * https://www.legitquest.com/act/central-civil-services-pension-amendment-rules-2022/C477
  * https://www.staffnews.in/2022/10/central-civil-services-pension-amendment-rules-2022-in-rule-8.html
  * https://www.staffnews.in/2024/07/central-civil-services-pension-amendment-rules-2024.html
  * https://www.staffnews.in/2025/05/central-civil-services-pension-amendment-rules-2025.html
  * https://dot.gov.in/sites/default/files/Central%20Civil%20Services%20%28Pension%29%20Amendment%20Rules%2C%202024.pdf?download=1
  * https://www.gconnect.in/orders-in-brief/pension/central-civil-services-pension-amendment-rules-2024.html
  * https://www.staffnews.in/2024/11/submission-of-pension-case-in-single-pension-application-form-6-a.html
  * https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/sep/doc2025930654001.pdf
  * https://www.gconnect.in/orders-in-brief/pension/doppw-guidelines-timely-pension-ppo.html
  * DoPPW clarifications re-circulated Nov 2024 (Rules 13, 14, 18, 19, 20, 28)
  * Source draft src/B2.txt and src/preamble.txt

CLAUSE-LEVEL COVERAGE AUDIT (24.10.2026) - RESULT: Chapter III is now covered clause by clause
  Ledger: Rules 11 to 30 = 20 rules, 81 sub-rule / clause / proviso / Explanation units, all taught on a row or a card.
  CLAUSE_LEDGER in the code carries one line per unit, and --audit prints the coverage table, so the audit can be re-run. The audit found 1 substantive content gap and 3 stale "unverified" flags, all fixed in this build:
  * GAP 1 (substantive): Rule 14(2) was carried as "UNVERIFIED / wording not confirmed" and its content was never taught.
    The text is now read and taught: the condition for discharge of pension liability by an autonomous body under a STATE
    Government is binding on that body "in accordance with the reciprocal arrangement entered into by the Central Government
    with the concerned State Government" (Chapter 6, card R14(2)).
  * GAP 2 (substantive): the Explanation to Rule 14 (deemed proper permission from the autonomous body - previous permission
    taken, and the body's order reciting that the employee resigns to join with proper permission) was missing altogether.
    Added on the same card and in Table 3 (every proviso and Explanation in one place).
  * FLAG FIX 3: Rule 15 "DoPT notification of the 1993 scheme" was flagged unconfirmed. The rule text names the scheme and the
    notifying authority (Casual Labourers (Grant of Temporary Status and Regularisation) Scheme of Government of India, 1993,
    Ministry of Personnel, Public Grievances and Pensions, DoPT). Flag removed, fact taught.
  * FLAG FIX 4: Rule 26(8) and the words "on each occasion" in Rule 30(1) were flagged as seen only in secondary copies.
    Both are now read in the full chapter text. Flag removed.
  * Word-level corrections kept from the previous build: Rule 19(2)(ii) is the PENSION element (not the gratuity element),
    19(2)(iii) set-off is stated, Rule 20 Explanation 1(ii) is "was to be refunded" after G.S.R. 770(E), Rule 26 has 8 sub-rules.
  * Deliberate non-claims kept (honest flags): rule wording here is a close restatement, not the Gazette text; the exact day of
    the Sept 2025 DoPPW O.M. is illegible; the effective date of G.S.R. 410(E) (16.11.2024 vs 13.11.2024) is unsettled.
CHANGES VERSUS THE SOURCE (outdated / superseded / corrected):
  * Rule 19(2)(ii): source says gratuity element ignored at pay fixation, current text says the PENSION element; clause (iii) set-off was omitted by the source and is added
  * Rule 20 Explanation 1(ii): obsolete wording was not required to be refunded, current wording was to be refunded, by G.S.R. 770(E) of 07.10.2022; Explanation 1(iii) set-off added
  * Rule 19(5): source gave only a conclusion; the cap on later benefit by the difference is now stated as a close restatement
  * Rule 20(3): source did not quote it; death before full refund adjusts unrefunded part against death gratuity
  * Rule 26: source said 26 sub-rules; Rule 26 has 8 sub-rules; 26(8) (Rules 35/36 resignation) was missing in the source and is added
  * Rule 26(6): source omitted the limb a body controlled or financed by Government
  * Rule 23(2) authority: source map said Appointing Authority; rule text names the Competent Authority
  * Rule 14(2) and the Explanation to Rule 14: added in this build (see audit above)
  * Source count of seventeen counting routes does not add up and is dropped
  * Interruption means any gap (BONUS-12), 5 exceptions 2 conditions (BONUS-24) and CPF-type label (BONUS-13) are the source's own glosses, flagged not taught as rules
  * G.S.R. 410(E) effective 16.11.2024: Rule 1(2) 120 days from 16.07.2024 gives 13.11.2024; stated as about mid-November 2024, unconfirmed
  * Rule 21 example: latest late entry for retirement on 30.11.2030 corrected from 31.05.2030 to 30.05.2030 (six calendar months back; method assumed)
  * Only G.S.R. 770(E) touched Chapter III; 410(E) touches Rule 57 which Rule 30(2) refers to; 340(E) touches Rule 37 only
  * VISUALS: cards now sit in a screenshot-style banded layout - rounded violet chapter strip, coloured header panels,
    full-width label + text rows with a thin colour bar, an amber trap strip, plus real TABLE and BAR-CHART scenes
    (Chapters 30, 31, 33, 34). Progressive reveal: one row or bar per narration segment.
KEY FACTS:
  * Qualifying service starts on taking charge of the first post; officiating or temporary needs a substantive post after it with no break; nothing before age 18 except Rule 20 military service
  * 31.12.2003 is the cut-off in Rules 13, 14, 15, 18, 19, 20
  * Rule 15 counts 50 percent of temporary-status service; Rule 14(3): PSU and nationalised bank service never counts
  * Rules 19 and 20: refund in at most 36 monthly instalments, first from the month after the option, counting revives only after full refund; 19(5) limits later benefit, 20(5) does not
  * Rule 20 Explanation 1(ii) since 07.10.2022: pension element ignored at pay fixation was to be refunded
  * Rule 21: EOL not on medical certificate counts unless a definite service-book entry says otherwise, entry allowed up to six months before superannuation
  * Rule 23: suspension counts only if exonerated or minor penalty AND wholly unjustified; otherwise only by express declaration of the competent authority
  * Rule 26(5): withdrawal needs four conditions incl. absence not over 90 days; Rule 26(6) bars private commercial company; Rules 25(2), 26(7), 28(3): the gap never counts
  * Rule 27(1) has five exceptions (a) to (e); Rule 28(2) excludes resignation, dismissal, removal, strike
  * Rule 30: verification at 18 years and five years before superannuation in Format 4; report to Secretary by 31 January; O.M. 4/35/2024-P&PW(D)/10377 (Sept 2025) puts duty on HoD
NOT VERIFIED (flagged on the cards - quote the official text in an answer sheet):
  * All rule wording: close restatement from a full reproduction of Chapter III; the Gazette PDF and India Code were not read
  * No amendment to Rules 11-30 after 07.10.2022 up to 21.10.2026: negative result from search pages only
  * Rule 21 six-month method: counted back as six calendar months, assumed
  * G.S.R. 410(E) effective date 16.11.2024: Gazette publication date not read
  * Sept 2025 O.M. exact date and manual-records line: day illegible, line not seen
  * G.S.R. 775(E) of 2026 (Rule 37(7), about 7 Sept 2026): seen on a re-hosted PDF only, belongs to Batch 3
LANGUAGE POLICY (chosen 24.10.2026):
  * ON SCREEN: simple English only - chapter pills, card titles, row text, tables, chart labels, trap strips.
  * NARRATION: Hinglish (Hindi-English mix) written in ROMAN script only. No Devanagari anywhere in this file.
    The teacher explains in Hinglish; rule numbers, dates, section words and legal terms stay in English, the way a
    classroom in an Indian city actually speaks. The student's questions (q_say) are Hinglish too.
  * The full English wording of every card (FULL) is unchanged and still goes to pension_b2_reference_sheet.md, so an
    answer can be written in English straight from the sheet while the video is heard in Hinglish.
  * TTS: the en-IN voices read Roman Hinglish naturally; numbers and dates in the narration are written in words
    (e.g. thirty-first December 2003) so the voice does not stumble.
Usage
    python build_pension_b2.py --audit      # density + clause-coverage check (no ffmpeg / internet)
    python build_pension_b2.py --preview    # slides only
    python build_pension_b2.py --no-tts     # silent dry run
    python build_pension_b2.py --part 1     # one third of the chapters (1, 2 or 3)
    python build_pension_b2.py              # full build (needs internet for edge-tts; ffmpeg+ffprobe with libass on PATH)
"""
import argparse
import asyncio
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


W, H = 1920, 1080
BUILD_DIR = Path("pension_b2_build")
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
OUT_STEM = "pension_b2_masterclass"
OUTPUT_MP4 = Path(OUT_STEM + ".mp4")

# Density budget (px). Build fails if text needs to go below these.
BODY_START, BODY_MIN = 34, 26
TITLE_START, TITLE_MIN = 30, 22
NODE_T_MIN, NODE_S_MIN = 18, 16

BG_TOP = (10, 16, 36)
BG_BOT = (22, 30, 58)
CARD_BG = (28, 39, 62)
TEXT_WHITE = (248, 250, 252)
MUTED = (148, 163, 184)
ORANGE = (230, 159, 0)
GREEN = (0, 158, 115)
BLUE = (0, 114, 178)
SKY = (86, 180, 233)
RED = (213, 94, 0)
YELLOW = (240, 228, 66)
PINK = (204, 121, 167)

DEFAULT_TEACHER = "en-IN-PrabhatNeural"
DEFAULT_STUDENT = "en-IN-NeerjaNeural"

# Pronunciation fixes for the neural voice. NOTE: longer patterns first, otherwise "Rule 15(3)" would swallow "Rule 15(3)(a)".
# Add acronyms of YOUR source here (spelled with dots so the voice says the letters).
_TTS_FIXES = [
    (r'\bUPSC\b', 'U.P.S.C.'), (r'\bSSC\b', 'S.S.C.'), (r'\bCVC\b', 'C.V.C.'), (r'\bCBI\b', 'C.B.I.'),
    (r'\bDoPT\b', 'D.O.P.T.'), (r'\bDOPT\b', 'D.O.P.T.'), (r'\bDoP&AR\b', 'D.O.P. and A.R.'), (r'\bMHA\b', 'M.H.A.'),
    (r'\bOMs\b', 'O.M.s'), (r'\bOM\b', 'O.M.'), (r'\bGIDs\b', 'Government of India decisions'), (r'\bGID\b', 'Government of India decision'),
    (r'\bCCS\b', 'C.C.S.'), (r'\bCCA\b', 'C.C.A.'), (r'\bCAG\b', 'C.A.G.'), (r'C&AG', 'C.A.G.'), (r'\bGOI\b', 'G.O.I.'),
    (r'\bDPC\b', 'D.P.C.'), (r'\bAPAR\b', 'A.P.A.R.'), (r'\bACR\b', 'A.C.R.'), (r'\bACP\b', 'A.C.P.'), (r'\bMTS\b', 'M.T.S.'),
    (r'\bFR\b', 'F.R.'), (r'\bSR\b', 'S.R.'), (r'\bCPC\b', 'C.P.C.'), (r'\bRR\b', 'R.R.'), (r'\bRTI\b', 'R.T.I.'), (r'\bFCRA\b', 'F.C.R.A.'),
    (r'\bIAS\b', 'I.A.S.'), (r'\bIPS\b', 'I.P.S.'), (r'\bIFS\b', 'I.F.S.'), (r'\bLBSNAA\b', 'L.B.S.N.A.A.'), (r'\bNITI\b', 'Nitee'),
    (r'\bSC/ST\b', 'S.C. and S.T.'), (r'\bOBC\b', 'O.B.C.'), (r'\bw\.e\.f\.', 'with effect from'), (r'\bW\.E\.F\.', 'with effect from'),
    (r'\bRs\.', 'Rupees'), (r'G\.S\.R\.', 'G.S.R.'),
    # rule / paragraph references (3 levels first)
    (r'Rule\s+(\d+)\((\d+)\)\(([a-z]+|[ivx]+)\)\(([ivx]+)\)', r'Rule \1, sub rule \2, clause \3, sub clause \4'),
    (r'Rule\s+(\d+)\((\d+)\)\(([a-z]+|[ivx]+)\)', r'Rule \1, sub rule \2, clause \3'),
    (r'Rule\s+(\d+)\(([a-z])\)\(([ivx]+)\)', r'Rule \1, clause \2, sub clause \3'),
    (r'Rule\s+(\d+)\((\d+)\)', r'Rule \1, sub rule \2'),
    (r'Rule\s+(\d+)\(([a-z])\)', r'Rule \1, clause \2'),
    (r'Rule\s+(\d+)\s?-?([A-Z])\b(?!\()', r'Rule \1 \2'),
    (r'[Pp]ara\s+(\d+(?:\.\d+)*)\(([a-z]+|[ivx]+)\)', r'Para \1, clause \2'),
    (r'Article\s+(\d+)\((\d)\)\(([abc])\)', r'Article \1, clause \2, proviso \3'),
    (r'Article\s+(\d+)\((\d)\)', r'Article \1, clause \2'),
    (r'\bsub-rules\b', 'sub rules'), (r'\bsub-rule\b', 'sub rule'),
    (r'[\u2014\u2013]', ','),
]


def normalize_for_tts(text: str) -> str:
    for pat, rep in _TTS_FIXES:
        text = re.sub(pat, rep, text)
    return re.sub(r'[ \t]+', ' ', text).strip()



# box tuple = (card title, SHORT on-screen text, FULL text, colour, simple English narration)
# PART I: GENERAL (Rules 1-3) | PART II: CLASSIFICATION (Rules 4-7) | PART III: APPOINTING AUTHORITY (Rules 8-9)

# box tuple = (card title, SHORT on-screen text, FULL text, colour, simple English narration)
# ============================================================================
# CLAUSE LEDGER - the audit that can be re-run
# ============================================================================
# (rule, unit, needle that must appear somewhere in the taught content)
# 20 rules, 62 units: every sub-rule, clause, proviso and Explanation of Chapter III.
CLAUSE_LEDGER = [
    ("11", "main", r"Rule 11"),
    ("11", "proviso 1 (no break)", r"PROVISO 1"),
    ("11", "proviso 2 (age 18)", r"PROVISO 2"),
    ("12", "main (duties and pay)", r"duties AND pay|duties and pay"),
    ("12", "Explanation (what service means)", r"Consolidated Fund of India"),
    ("13", "13(1) permanent transfer", r"permanent transfer"),
    ("13", "proviso to 13(1) (no break)", r"without interruption"),
    ("13", "13(2) permitted resignation", r"13\(2\)"),
    ("13", "Explanation (proper permission)", r"proper permission"),
    ("13", "13(3) liability of the Centre", r"13\(3\)"),
    ("14", "14(1) entry gate", r"14\(1\)"),
    ("14", "14(1)(a) no break", r"\(a\)"),
    ("14", "14(1)(b) no separate pension", r"\(b\)"),
    ("14", "14(1)(c) body pays lump sum", r"lump sum"),
    ("14", "14(1)(d) commutation table 1981", r"1981"),
    ("14", "14(2) reciprocal arrangement", r"14\(2\)"),
    ("14", "Explanation (proper permission)", r"EXPLANATION"),
    ("14", "14(3) PSU and nationalised bank", r"14\(3\)"),
    ("15", "main (50 percent)", r"fifty percent|50 percent"),
    ("15", "1993 casual labourers scheme", r"1993"),
    ("16", "probation and confirmation", r"Rule 16"),
    ("17", "apprentice, IAS and Defence Accounts", r"Rule 17"),
    ("18", "18(i) contract, then regular post", r"18\(i\)|contract for a specified period"),
    ("18", "(ii) refund of CPF share", r"CPF"),
    ("19", "19(1) entry gate", r"19\(1\)"),
    ("19", "19(2)(i) pension already drawn", r"19\(2\)"),
    ("19", "19(2)(ii) pension element refunded", r"pension element"),
    ("19", "19(2)(iii) set-off", r"set off"),
    ("19", "19(3) 36 instalments", r"thirty-six|36 "),
    ("19", "19(4) death before refund", r"19\(4\)"),
    ("19", "19(5) cap on later benefit", r"19\(5\)"),
    ("19", "Explanation (capital value)", r"Capital value|capital value"),
    ("20", "20(1) military service", r"20\(1\)"),
    ("20", "Explanation 1(i)", r"Explanation 1"),
    ("20", "Explanation 1(ii) refunded after 2022", r"was to be refunded"),
    ("20", "Explanation 1(iii) set-off", r"set-off|set off"),
    ("20", "Explanation 2 (kept military pension)", r"Explanation 2"),
    ("20", "Explanation 3 (post 2003, NPS)", r"Explanation 3"),
    ("20", "20(2) instalments", r"20\(2\)"),
    ("20", "20(3) death before refund", r"20\(3\)"),
    ("20", "20(4) condonation of interruption", r"20\(4\)"),
    ("20", "20(5) no limitation", r"20\(5\)"),
    ("21", "main (leave with salary)", r"leave salary"),
    ("21", "proviso (commotion, higher studies)", r"civil commotion"),
    ("21", "Explanation (service book entry)", r"service book"),
    ("22", "22(1) Group C training", r"22\(1\)"),
    ("22", "22(2) Government may order", r"22\(2\)|Government decides"),
    ("22", "22(3) joining time gap", r"22\(3\)"),
    ("22", "22(4) excess regularised as EOL", r"22\(4\)"),
    ("23", "23(1) exonerated and unjustified", r"23\(1\)"),
    ("23", "23(2) express declaration", r"23\(2\)"),
    ("23", "23(3) order and service book", r"23\(3\)"),
    ("24", "dismissal and removal", r"Rule 24"),
    ("25", "25(1) reinstatement on appeal", r"25\(1\)"),
    ("25", "25(2) gap regularised as duty or leave", r"25\(2\)"),
    ("26", "26(1) forfeiture", r"26\(1\)"),
    ("26", "26(2) permitted resignation", r"26\(2\)"),
    ("26", "26(3) order and service book entry", r"26\(3\)"),
    ("26", "26(4) joining time and leave due", r"26\(4\)"),
    ("26", "26(5) four conditions", r"26\(5\)"),
    ("26", "26(6) private commercial company", r"26\(6\)"),
    ("26", "26(7) condonation, gap not counted", r"26\(7\)"),
    ("26", "26(8) resignation for Rules 35 and 36", r"26\(8\)"),
    ("27", "27(1)(a) authorised leave", r"27\(1\)"),
    ("27", "27(1)(b) unauthorised absence", r"continuation of authorised leave|unauthorised absence"),
    ("27", "27(1)(c) suspension", r"suspension"),
    ("27", "27(1)(d) public interest transfer", r"public interest|public-interest"),
    ("27", "27(1)(e) joining time", r"joining time"),
    ("27", "27(2) commutation into EOL", r"27\(2\)"),
    ("28", "28(1) automatic condonation", r"28\(1\)"),
    ("28", "28(2) exceptions", r"28\(2\)"),
    ("28", "28(3) gap does not count", r"28\(3\)"),
    ("28", "28(4) condonation considered", r"28\(4\)"),
    ("28", "28(5) exceptional and grave", r"28\(5\)"),
    ("28", "28(6) hearing in person", r"28\(6\)"),
    ("29", "option (a) and (b), refund", r"Rule 29"),
    ("30", "30(1) two triggers, Format 4", r"Format 4"),
    ("30", "30(2) procedure of Rule 57(1)(a)", r"30\(2\)"),
    ("30", "30(3) extra events", r"30\(3\)"),
    ("30", "30(4) verification is final", r"30\(4\)"),
    ("30", "30(5) report by 31 January", r"30\(5\)"),
]


def content_text():
    """Every word the video teaches, for the clause check."""
    parts = []
    for sc in SCENES:
        parts += [sc["chapter"], sc["title"], sc["q"], sc.get("intro", ""), sc.get("q_say", ""),
                  sc.get("hook", ""), sc.get("footer", ""), " ".join(sc.get("covers", []))]
        if sc.get("layout"):
            units = items(sc)
            for u in units:
                parts += [str(u[0]), str(u[1]), str(u[-1])]
        else:
            for b in sc["boxes"]:
                parts += [b[0], b[1], FULL.get((sc["id"], b[0]), ""), b[3]]
    return "\n".join(parts)


def audit_clauses():
    """Checks that every unit of Chapter III is taught. Returns the number of failures."""
    txt = content_text()
    for sc in SCENES:                      # tables carry their wording in rows
        if sc.get("layout"):
            for u in items(sc):
                txt += "\n" + str(u[0]) + " " + str(u[1])
    missing, rule_seen = [], {}
    for rule, unit, needle in CLAUSE_LEDGER:
        rule_seen.setdefault(rule, 0)
        if re.search(needle, txt):
            rule_seen[rule] += 1
        else:
            missing.append((rule, unit, needle))
    print(f"CLAUSE LEDGER: {len(CLAUSE_LEDGER)} units across {len(rule_seen)} rules checked")
    for rule in sorted(rule_seen, key=lambda r: int(r)):
        total = sum(1 for r, _u, _n in CLAUSE_LEDGER if r == rule)
        print(f"  Rule {rule:>2s}: {rule_seen[rule]}/{total} units on screen")
    for rule, unit, needle in missing:
        print(f"  MISSING Rule {rule} - {unit} (looking for /{needle}/)")
    print("ALL CLAUSES TAUGHT" if not missing else f"{len(missing)} CLAUSE(S) NOT FOUND")
    return len(missing)


HINGLISH_MARKERS = re.compile(
    r"\b(hai|hain|ka|ke|ki|ko|mein|aur|nahi|nahin|karo|kijiye|karte|hoti|hota|woh|yeh|tabhi|jab|agar|ya|bhi|kar|"
    r"raha|rahi|rahe|sakta|sakti|padega|padta|padti|hoga|hogi|kya|kaun|kyunki|isliye|lekin|par|se|ek|do|ab|to)\b",
    re.IGNORECASE)
DEVANAGARI = re.compile(r"[\u0900-\u097F]")


def audit_language():
    """Checks the language split chosen on 24.10.2026: English on screen, Hinglish (Roman script) narration."""
    print("LANGUAGE AUDIT: English on screen, Hinglish narration in Roman script")
    bad, segs, hing = 0, 0, 0
    for sc in SCENES:
        for _who, text, _rev, _kind in build_segments(sc):
            segs += 1
            if not text.strip():
                bad += 1
                print(f"  EMPTY narration in {sc['id']}")
            if DEVANAGARI.search(text):
                bad += 1
                print(f"  DEVANAGARI in narration of {sc['id']}: {text[:60]!r}")
            if HINGLISH_MARKERS.search(text):
                hing += 1
        for u in items(sc):
            for field in (u[0], u[1]):
                if DEVANAGARI.search(str(field)):
                    bad += 1
                    print(f"  DEVANAGARI on screen in {sc['id']}: {str(field)[:60]!r}")
    print(f"  {segs} narration segments; {hing} read as Hinglish ({100 * hing // max(segs, 1)} percent)")
    print("  LANGUAGE SPLIT OK" if not bad else f"  {bad} LANGUAGE PROBLEM(S)")
    return bad


SCENES = [
    {
        "id": "c02_01_rule11_start",
        "chapter": "CHAPTER 1 • RULE 11: WHEN DOES QUALIFYING SERVICE START?",
        "title": "RULE 11 — WHEN THE QUALIFYING-SERVICE CLOCK STARTS",
        "accent": RED, "badge": "RULE 11",
        "q": "From which day does a Government servant's qualifying service start counting?",
        "q_say": "Sir, Government servant ki qualifying service kis din se count hona shuru hoti hai?",
        "intro": "Welcome back, doston! Part 1 mein hum Rules 1 se 10 tak kar chuke hain, CCS Pension Rules 2021 ki basic zameen. Aaj Part 2 hai, Rules ke Chapter 3 ka, yani Rules 11 se 30. Yeh poora chapter ek hi sawaal ka jawab deta hai: pension nikalte waqt service ke kaunse saal gine jaate hain, aur kaunse nahi. Pension ka matlab hai retirement ke baad har mahine milne wala paisa. Qualifying service ka matlab hai woh saal jo Rules ginne ko maante hain. Isko ek stopwatch samajhiye, aur Rule 11 batata hai ki stopwatch kab start hoti hai.",
        "boxes": [
            ("THE RULE",
             "The clock starts the day the servant takes charge of the first post. Substantive, officiating or temporary: all fine.",
             "Rule 11 (close restatement, not verbatim Gazette text): qualifying service of a Government servant begins from the date he takes charge of the post to which he is first appointed, whether in a substantive, officiating or temporary capacity. Read via a page-summarising tool from a secondary reproduction of the Rules; the Gazette or India Code text itself was not read.",
             SKY,
             "Pehle rule lete hain. Qualifying service us din se shuru hoti hai jab servant pehla post charge karta hai. Isse koi farq nahi padta ki woh pehla post substantive tha, officiating tha ya temporary. Substantive matlab permanent. Officiating matlab kisi aur ki jagah, ya trial par post sambhalna. Temporary matlab aisa post jo permanent nahi hai."),
            ("PROVISO 1: NO BREAK",
             "Officiating or temporary start counts only if a substantive appointment follows WITHOUT a break.",
             "First proviso to Rule 11 (close restatement): service in an officiating or temporary capacity counts only if it is followed, without interruption, by substantive appointment in the same service or post or in another service or post. Ledger R11-PROV1.",
             GREEN,
             "Ab pehla exception. Agar pehla post sirf officiating ya temporary tha, to woh period tabhi ginta hai jab uske baad bina kisi break ke substantive appointment ho. Substantive post usi service mein ho ya doosri service mein, dono theek. Agar break hai aur substantive appointment nahi, to woh pehla period qualify nahi karta."),
            ("PROVISO 2: UNDER 18",
             "Service before age 18 does not count. Only exception: military service counted under Rule 20.",
             "Second proviso to Rule 11 (close restatement): service rendered before the age of 18 years is not counted, except military service that is counted for civil pension under Rule 20. Ledger R11-PROV2. Reading that counting starts from the 18th birthday and the earlier stretch is simply left out is consistent with the proviso (R11-AGE18-INTERP).",
             ORANGE,
             "Ab doosra exception. Athara saal ki umar se pehle ki service count nahi hoti. Sirf ek exception hai: Rule 20 ke tehat civil pension ke liye gini jaane wali military service, jo hum jald hi padhenge. Iska matlab yeh nahi ki sab kuch khatam. Counting bas us din se shuru hoti hai jab insaan athara saal ka hota hai."),
            ("REAL EXAMPLES",
             "Bilal: officiating 2010, substantive 2012, no gap: counts from 2010. Charu joined at 17y5m: counts from her 18th birthday.",
             "Example 1 (invented): Bilal, a clerk, is appointed officiating on 01.07.2010 and gets a substantive appointment in the same department on 01.07.2012 with no gap. His qualifying service runs from 01.07.2010, not 2012. Example 2 (invented): Charu, born 10.01.1985, joins on 01.07.2002 at 17 years 5 months. Counting starts on her 18th birthday, 10.01.2003; the earlier 6 months 9 days are left out.",
             ORANGE,
             "Ab do real examples. Bilal first July 2010 ko officiating appoint hua, aur first July 2012 ko substantive, bina gap ke. Uski counting 2010 se chalti hai, 2012 se nahi. Charu, janm tenth January 1985, first July 2002 ko join kari, seventeen saal paanch mahine ki umar mein. Uski counting uske eighteenth birthday, tenth January 2003 se shuru hoti hai, aur pehle chhah mahine nau din chhod diye jaate hain."),
            ("THE TRAP",
             "Officiating start is NOT lost, if substantive follows. Do not teach a fixed meaning of interruption: not confirmed.",
             "Trap and flag. Q: if the first appointment was not substantive, is the service lost? A: No, officiating and temporary service count if a substantive appointment follows without interruption. UNVERIFIED (R11-INTERRUPTION-DEF): the source's gloss that 'interruption' means any gap, authorised or unauthorised, was not confirmed against an official source; Rule 27 treats authorised leave as an exception, so do not teach that gloss as a rule.",
             RED,
             "Dhyan dijiye, yahi trap hai. Pehla post officiating ya temporary hone se khatam nahi hota, jab tak uske baad bina break ke substantive appointment aa jaye. Ek aur savdhani. Source interruption ka ek seedha matlab deta hai, yani koi bhi gap, lekin hum woh wording kisi official source se confirm nahi kar paye, isliye ise rule maan kar mat padhiye."),
        ],
        "hook": "REMEMBER: clock starts at first charge-taking; no break before substantive; nothing before 18!",
        "hook_say": "Yaad rakhiye: clock us din chalti hai jab aap pehla post charge karte hain, officiating service ko bina break ke substantive post chahiye, aur athara saal se pehle kuch nahi ginta.",
        "covers": ["R11-MAIN", "R11-PROV1", "R11-PROV2", "R11-EX1", "R11-QA", "R11-AGE18-INTERP", "R11-INTERRUPTION-DEF"],
    },
    {
        "id": "c02_02_chapter_map",
        "chapter": "CHAPTER 2 • CHAPTER III MAP: COUNT, LOSE, SAVE, PROVE",
        "title": "HOW CHAPTER III IS BUILT — FOUR JOBS IN RULES 11 TO 30",
        "accent": SKY, "badge": "RULES 11 TO 30",
        "flow": "ch3map",
        "q": "How is this chapter organised, so that twenty rules do not feel like a heap?",
        "q_say": "Sir, bees rules bahut hote hain. Chapter 3 kaise organise hai taaki main kho na jaun?",
        "boxes": [
            ("STEP 1: WHAT COUNTS",
             "Rules 11 to 23 and 29 say which kinds of service count, and on what condition.",
             "Counting rules: Rule 11 (start), 12 (duties and pay regulated by Government), 13 (State), 14 (autonomous body), 15 (temporary status), 16 (probation), 17 (apprentice), 18 (contract), 19 (civil pensioner re-employed), 20 (military), 21 (leave), 22 (training), 23 (suspension), 29 (international organisations). Rules 25, 27 and 28 also decide counting after a gap. Ledger CH3-STRUCTURE (fair summary of Rules 24 to 28 as read).",
             SKY,
             "Step one, kya ginta hai. Rules 11 se 23, aur Rule 29, batate hain kaunsi service ginti hai aur kis condition par. State service, probation, contract service, military service, leave, training aur suspension, sabka apna rule hai."),
            ("STEP 2: WHAT IS LOST",
             "Rule 24 dismissal or removal, Rule 26 resignation, Rule 27 interruption: past service can be forfeited.",
             "Forfeiture rules: Rule 24 (dismissal or removal), Rule 26 (resignation, general rule in 26(1)), Rule 27(1) (general rule: interruption forfeits past service). Forfeiture means the earlier service is wiped out for pension.",
             RED,
             "Step two, kya kho sakta hai. Forfeiture matlab pehli service pension ke liye mita di jaati hai. Rule 24 dismissal ya removal par mita deta hai, Rule 26 resignation par, aur Rule 27 service mein interruption par."),
            ("STEP 3: WHAT IS SAVED",
             "Rule 25 reinstatement, Rule 26(2) permitted resignation, Rule 27 exceptions, Rule 28 condonation.",
             "Saving rules: Rule 25 (reinstatement on appeal or review), Rule 26(2) (resignation with proper permission for another Government appointment), Rule 27(1)(a) to (e) and 27(2) (exceptions and commutation of absence), Rule 28 (condonation of interruption). Condonation means the authority forgives the gap.",
             GREEN,
             "Step three, kya bach sakta hai. Rule 25 mein reinstatement, Rule 26 mein permitted resignation, Rule 27 ke exceptions, aur Rule 28 mein condonation. Condonation ka simple matlab: authority gap maaf kar deti hai taaki pehli service bachi rahe."),
            ("STEP 4: PROOF",
             "Rule 30 makes the Head of Office check and certify the service in Format 4, at fixed times.",
             "Proof rule: Rule 30 (verification of qualifying service by the Head of Office with the Accounts Officer, communicated in Format 4, after 18 years of service and when five years remain before superannuation). Do NOT memorise a count of 'seventeen routes': the source's count does not add up (range 27 to 30 already includes Rule 28), so it is dropped (CH3-COUNT17).",
             BLUE,
             "Step four, proof. Rule 30 Head of Office se service check karwata hai aur career ke fix points par Format 4 mein certificate deta hai. Ek tip: routes ki koi ginti yaad mat kijiye. Source ne ek ginti di thi, par arithmetic milti nahi, isliye usse chhod dijiye."),
        ],
        "hook": "REMEMBER: Count (11-23, 29) • Lose (24, 26, 27) • Save (25, 26(2), 27-28) • Prove (30)!",
        "hook_say": "Yaad rakhiye: count, lose, save, prove. Counting Rules 11 se 23 aur 29, losing Rules 24, 26 aur 27, saving Rules 25 se 28, aur proving Rule 30.",
        "covers": ["CH3-STRUCTURE", "CH3-COUNT17"],
    },
    {
        "id": "c02_03_amendments_currency",
        "chapter": "CHAPTER 3 • WHAT HAS AMENDED CHAPTER III, AND HOW CURRENT IS THIS?",
        "title": "WHICH GAZETTE AMENDMENTS TOUCH RULES 11 TO 30?",
        "accent": ORANGE, "badge": "AMENDMENTS • CURRENCY",
        "q": "Which of the four Gazette notifications actually changed Rules 11 to 30?",
        "q_say": "Sir, source chaar Gazette notifications ginata hai. Inme se kaunse ne actually Rules 11 se 30 ko badla?",
        "boxes": [
            ("THE ORIGINAL AND 2022",
             "Original Rules: G.S.R. 868(E), 20.12.2021. Only G.S.R. 770(E) of 07.10.2022 changed Chapter III (Rule 20).",
             "G.S.R. 868(E) dated 20.12.2021 is the original notification of the CCS (Pension) Rules 2021 (GSR-868E). G.S.R. 770(E) dated 07.10.2022 substituted Explanation 1 clause (ii) of Rule 20; the same notification also amended Rules 8, 46(5)(a), 50(9)(h)(iii) and 76, but only Rule 20 lies in Chapter III (GSR-770E-R20, CH3-AMENDED-BY).",
             SKY,
             "Original Rules G.S.R. 868(E), twentieth December 2021 se aaye. Uske baad sirf ek Gazette notification ne Chapter 3 ke andar kuch badla: G.S.R. 770(E), seventh October 2022, jisne Rule 20 ki ek clause badli. Woh change hum jald hi detail mein padhenge."),
            ("2024: NOT IN THIS CHAPTER",
             "G.S.R. 410(E) of 16.07.2024 does not amend Rules 11-30. It changed Rule 57 (Form 6-A), which Rule 30(2) points to.",
             "G.S.R. 410(E) dated 16.07.2024 (F.No. 55/13/2023-P&PW(C)) amends Rules 50, 53, 57, 58, 59, 60, 62, 63, 80 and Forms and Formats; it does not amend Rules 11 to 30 (GSR-410E-DATE). Rule 30(2) points to the procedure of Rule 57(1)(a), and Rule 57 was amended by this notification (R30(2)). The source says it took effect on 16.11.2024. UNVERIFIED (GSR-410E-EFFECTIVE): Rule 1(2) says 120 days after Gazette publication; 120 days from 16.07.2024 is 13.11.2024, secondary sites say 16.11.2024, and the Gazette publication date was not read. Say about mid-November 2024 unless confirmed.",
             ORANGE,
             "2024 ka notification, G.S.R. 410(E), sixteenth July 2024, Rules 11 se 30 ko nahi badla. Usne Rule 57 badla, jise Rule 30 point karta hai. Iski start date par dhyan dijiye. Source sixteenth November 2024 kehta hai, par sau bees din ginne se thirteenth November aata hai, aur maine Gazette padhi nahi. Isliye kahein, about mid November 2024."),
            ("2025: RULE 37 ONLY",
             "G.S.R. 340(E) of 22.05.2025 amends only Rule 37 (PSU-absorbed employees). Not Chapter III.",
             "G.S.R. 340(E) dated 22.05.2025 amends Rule 37 only (employees absorbed in public sector undertakings); its Explanation applies Rules 7, 8, 41 and 44(5) analogously. Two pages give the sub-rule number differently (37(29)(c) versus 37(7)), so cite as Rule 37 only (GSR-340E). Rule 37 is for the next batch.",
             GREEN,
             "2025 ka notification, G.S.R. 340(E), twenty-second May 2025, sirf Rule 37 amend karta hai, public sector undertakings mein absorbed employees ke baare mein. Woh agle batch ka hissa hai. Cite karte waqt sirf Rule 37 kahiye, kyunki do pages sub-rule number par alag hain."),
            ("HOW CURRENT IS THIS?",
             "No amendment to Rules 11-30 after Oct 2022 was found up to 21.10.2026. Source's claim of checking on 12.09.2026 is unverified.",
             "Currency note. The source says it was verified on 12 September 2026 and cites O.M.s up to 22.06.2026; this cannot be verified (VERIFIED-12SEP2026), and the 22.06.2026 O.M. is not cited in Batch 2. No amendment to Rules 11 to 30 after G.S.R. 770(E) of 2022 was found in the pages read, up to 21.10.2026; that is a negative result from search-engine results only, because the Gazette and DoPPW site were not read. Rule wording in this batch is a close restatement from secondary reproductions, not Gazette text. A 2026 amendment, G.S.R. 775(E) (about 7 Sept 2026; date unclear; seen on a re-hosted PDF), concerns Rule 37(7) for ex-Ordnance Factory Board employees and belongs to the next batch.",
             RED,
             "Ab honest currency note. Source kehta hai ise twelfth September 2026 ko check kiya gaya, par hum usse verify nahi kar sakte. Humne twenty-first October 2026 tak search kiya aur 2022 ke baad Rules 11 se 30 mein koi amendment nahi mila, lekin woh search search results se tha, Gazette se nahi. Isliye is part ki saari wording ko close restatement maaniye, aur exam answer Gazette se confirm kijiye."),
        ],
        "hook": "REMEMBER: only G.S.R. 770(E) of 2022 changed Chapter III; check the Gazette for exact words!",
        "hook_say": "Yaad rakhiye: Chapter 3 mein sirf G.S.R. 770(E) of 2022 ne kuch badla, aur exact words ke liye hamesha Gazette dekhiye.",
        "covers": ["GSR-868E", "GSR-770E-R20", "GSR-410E-DATE", "GSR-410E-EFFECTIVE", "GSR-340E", "CH3-AMENDED-BY", "VERIFIED-12SEP2026"],
    },
    {
        "id": "c02_04_rule12_duties_pay",
        "chapter": "CHAPTER 4 • RULE 12: DUTIES AND PAY MUST BOTH BE GOVERNMENT-REGULATED",
        "title": "RULE 12 — DUTIES AND PAY, BOTH REGULATED BY GOVERNMENT",
        "accent": GREEN, "badge": "RULE 12",
        "q": "What two things must be true before service qualifies, and what does 'service' mean here?",
        "q_say": "Sir, Rule 12 ke tehat service qualify hone se pehle kya sach hona chahiye, aur yahan service ka matlab kya hai?",
        "boxes": [
            ("THE RULE: BOTH LIMBS",
             "Service qualifies only if duties AND pay are both regulated by Government, or by conditions Government fixes.",
             "Rule 12 (close restatement): the service of a Government servant does not qualify unless his duties and his pay are both regulated by the Government, or are under conditions prescribed by the Government. The two limbs are cumulative: AND, not OR.",
             SKY,
             "Pehle rule. Service tabhi qualify karti hai jab do baatein dono sach hon: duties Government regulate karti ho, aur pay bhi Government regulate karti ho, ya dono aisi conditions par hon jo Government tay karti hai. Yeh AND hai, OR nahi. Sirf duties kaafi nahi, sirf pay kaafi nahi."),
            ("THE EXPLANATION",
             "Service means service under Government, paid from the Consolidated Fund of India or a Local Fund the Government administers.",
             "Explanation to Rule 12 (close restatement): 'service' means service under Government and paid by Government from the Consolidated Fund of India or from a Local Fund administered by Government. 'Local Fund administered by Government' is defined in Rule 3(1)(r): a body under Government control by force of law or rule, with Government having full and direct control over its spending. Ledger R12-EXPL-SERVICE, R12-LOCALFUND-R3(1)(r).",
             GREEN,
             "Ab Explanation. Yahan service ka matlab hai Government ke under service, aur Government dwara pay ki gayi, ya to Consolidated Fund of India se, jo Government ka main account hai, ya us Local Fund se jo Government khud administer karti hai. Local Fund ka matlab Rule 3, clause 1, sub-clause r mein hai: uske kharch par Government ka poora aur direct control hona chahiye."),
            ("THE EXCLUSION",
             "Service in an establishment with no non-contributory pension scheme is left out, unless Government treats it as qualifying.",
             "Explanation exclusion (close restatement): service in an establishment where a non-contributory pension scheme is not available is not included, unless the Government treats that service as qualifying (R12-EXPL-EXCL). UNVERIFIED gloss (R12-BONUS13-CPF): the source adds that establishments with a CPF-type contributory arrangement fall outside; the rule speaks only of an establishment where a non-contributory pension scheme is not available, and the CPF label is the source's own gloss, not confirmed. Non-contributory means the employee pays nothing towards the pension.",
             ORANGE,
             "Ab exclusion. Aisi establishment ki service bahar hai jiske paas non-contributory pension scheme nahi, jab tak Government usse qualifying na maan le. Non-contributory matlab employee pension mein kuch nahi deta. Source aisi jagahon ko contributory provident fund type kehta hai, par woh label source ka apna gloss hai, confirmed nahi."),
            ("REAL EXAMPLE",
             "Dev's office follows Government rules, but his pay came from a society fund with no Government control: that period does not qualify.",
             "Example (invented): Dev works in an office whose duties are regulated by Government rules, but his pay comes from a society fund over which Government has no direct control. Duties limb met, pay limb not met, so that period is not qualifying service (R12-EX1). Q: does pay from a Local Fund count? A: yes, if the fund is administered by Government and both duties and pay are regulated (R12-QA).",
             ORANGE,
             "Ab ek real example. Dev aise office mein hai jahan duties Government rules follow karti hain, par salary society fund se aati hai jise Government control nahi karti. Ek limb poora hua, doosra nahi, isliye woh period qualify nahi karta. Agar salary Local Fund se aati jise Government administer karti, aur duties aur pay dono regulated hote, to ginti ho sakti thi."),
            ("THE TRAP: RULE 2 OR 12?",
             "Rule 2 asks: do the Rules apply to me? Rule 12 asks: does THIS service count? Two different questions.",
             "Look-alike (R2-VS-R12, reasonable reading; Rule 2 is in Batch 1): Rule 2 tells to whom the Rules apply; Rule 12 tells which service is counted as qualifying. One servant can be inside both, but the questions differ. In practice the service book and appointment letter are the evidence for who regulated duties and pay and from which fund.",
             RED,
             "Dhyan dijiye, yahi trap hai. Rule 2 poochta hai ki Rules kisi vyakti par lagte hain ya nahi. Rule 12 poochta hai ki service ka koi khaas hissa ginta hai ya nahi. Vyakti pehla test pass karke doosra fail kar sakta hai. Practice mein service book aur appointment letter hi evidence hain."),
        ],
        "hook": "REMEMBER: Rule 12 = duties AND pay regulated by Government; Rule 2 = who, Rule 12 = which service!",
        "hook_say": "Yaad rakhiye: Rule 12 ke liye duties aur pay dono Government se regulated chahiye. Rule 2 poochta hai kaun cover hai, Rule 12 poochta hai kaunsi service ginti hai.",
        "covers": ["R12-MAIN", "R12-EXPL-SERVICE", "R12-EXPL-EXCL", "R12-LOCALFUND-R3(1)(r)", "R12-EX1", "R12-QA", "R2-VS-R12", "R12-BONUS13-CPF"],
    },
    {
        "id": "c02_05_rule13_state_service",
        "chapter": "CHAPTER 5 • RULE 13: SERVICE UNDER A STATE GOVERNMENT",
        "title": "RULE 13 — STATE SERVICE BEFORE JOINING THE CENTRE",
        "accent": BLUE, "badge": "RULE 13",
        "q": "Can service under a State Government be counted, and who pays for it?",
        "q_say": "Sir, agar koi pehle State Government mein kaam kar chuka hai, to woh service ginti hai kya, aur paisa kaun deta hai?",
        "boxes": [
            ("ROUTE ONE: 13(1)",
             "State servant first appointed on or before 31.12.2003 and permanently transferred to a post under these Rules: State service counts.",
             "Rule 13(1) (close restatement): a Government servant whose initial appointment in a State Government pensionable establishment was on or before 31.12.2003, and who is permanently transferred to a service or post to which these Rules apply, has his continuous service under the State Government counted as qualifying. Proviso: officiating or temporary State service counts only if followed without interruption by substantive appointment in the State or the Central Government. 31.12.2003 is the old-pension cut-off: the New Pension System began on 01.01.2004 (TL-31.12.2003).",
             SKY,
             "Pehle route one. State servant jiska pehla appointment State pensionable establishment mein thirty-first December 2003 ko ya usse pehle hua, aur jise baad mein permanently transfer kiya gaya aise Central post par jo in Rules mein aata hai, uski continuous State service ginti hai. Woh date isliye matter karti hai kyunki New Pension System first January 2004 se shuru hua. Proviso: officiating ya temporary service ke baad bina break ke substantive appointment chahiye, State mein ya Centre mein."),
            ("ROUTE TWO: 13(2)",
             "Resigned the State job with PROPER permission and joined a Central post: State service counts, same no-break condition.",
             "Rule 13(2) (close restatement): where a person is appointed to a post under these Rules after his resignation from State service was accepted with proper permission, his continuous State service qualifies, subject to the same condition of uninterrupted substantive appointment (R13(2)). Explanation (R13-EXPL): proper permission means (i) he applied for the Central post with the State Government's previous permission, AND (ii) the State's order accepting the resignation says that he resigns to join the Central post with proper permission.",
             GREEN,
             "Ab route two. Agar usne State job se resignation diya aur phir Central post join kiya, to State service phir bhi ginti hai, par tabhi jab resignation proper permission ke saath thi. Explanation do test deta hai. Pehla, usne State Government ki previous permission lekar Central post ke liye apply kiya. Doosra, State ka order kehta hai ki woh proper permission ke saath Central post join karne ke liye resign kar raha hai."),
            ("WHO PAYS: 13(3)",
             "The Central Government bears pension and gratuity. No share is recovered from the State.",
             "Rule 13(3) (close restatement): the liability for pension and gratuity is borne entirely by the Central Government; no proportionate pension is recovered from the State Government (R13(3)). Gratuity is a one-time lump sum paid on retirement or death. Contrast Rule 14, where the autonomous body pays a lump sum.",
             ORANGE,
             "Ab paisa. Rule 13(3) ke tehat poora pension aur gratuity Central Government uthati hai. Gratuity matlab retirement ya death par ek baar milne wali lump sum. Centre State se koi hissa recover nahi karta. Yeh yaad rakhiye, kyunki Rule 14 alag tarah kaam karta hai."),
            ("EXAMPLE AND THE LINK",
             "Asha: State Assistant Engineer from 1999, moved to the Centre in 2007: all State service counts, Centre pays. Without permission papers, Rule 26(1) forfeits it.",
             "Example (invented): Asha joined a State pensionable establishment as Assistant Engineer in 1999 and was permanently transferred to a Central post in 2007. Her whole State service counts and the Centre bears the cost (R13-EX1). Link (R13-R26-LINK): Rule 13(2) rests on the Rule 26(2) exception to forfeiture on resignation; without the permission papers the case falls under Rule 26(1) and the State service can be forfeited. Q: does the Centre recover proportionate pension from the State? A: no, Rule 13(3).",
             RED,
             "Ab ek real example. Asha 1999 mein Assistant Engineer ke roop mein State pensionable post par aayi aur 2007 mein permanently Central post par transfer hui. Uski poori State service ginti hai, aur kharch Centre uthati hai. Dhyan dijiye, yahi trap hai: Rule 13(2) Rule 26 ke permitted resignation exception par tika hai. Permission ke papers na hon to State service forfeit ho sakti hai."),
        ],
        "hook": "REMEMBER: on or before 31.12.2003 • permanent transfer, or resignation WITH permission • Centre pays all!",
        "hook_say": "Yaad rakhiye: pehla appointment thirty-first December 2003 ko ya pehle, permanent transfer ya proper permission ke saath resignation, aur poora paisa Centre deta hai.",
        "covers": ["R13(1)", "TL-31.12.2003", "R13(1)-PROV", "R13(2)", "R13-EXPL", "R13(3)", "R13-EX1", "R13-R26-LINK"],
    },
    {
        "id": "c02_06_rule14_autonomous_body",
        "chapter": "CHAPTER 6 • RULE 14: SERVICE IN AN AUTONOMOUS BODY (AND WHY A PSU IS DIFFERENT)",
        "title": "RULE 14 — AUTONOMOUS BODY SERVICE AND THE LUMP SUM",
        "accent": ORANGE, "badge": "RULE 14",
        "q": "When does service in an autonomous body count, and what must the body pay?",
        "q_say": "Sir, autonomous body ki service kab ginti hai, aur body ko kya pay karna hota hai?",
        "boxes": [
            ("THE RULE: 14(1)",
             "First appointed on or before 31.12.2003 in an autonomous body with a similar non-contributory pension scheme; joined a Central post with proper permission.",
             "Rule 14(1) (close restatement): where a person's initial appointment was on or before 31.12.2003 in an autonomous body, under the Central or a State Government, that has a non-contributory pension scheme similar to these Rules, and after his resignation was accepted with proper permission he is appointed to a service or post to which these Rules apply, his service in the body (officiating, temporary or substantive) qualifies, subject to clauses (a) to (d). An autonomous body is an organisation set up by Government but run with its own management.",
             SKY,
             "Pehle rule. Autonomous body woh sanstha hai jise Government banati hai par jo apni management se chalti hai. Agar kisi ka pehla appointment aisi body mein thirty-first December 2003 ko ya pehle hua, aisi body mein jiska non-contributory pension scheme milta julta ho, aur baad mein usne resign karke proper permission ke saath Central post join kiya, to body ki service ginti hai. Chaar conditions, clause a se d, sab poori chahiye."),
            ("THE FOUR CONDITIONS",
             "(a) no break before substantive post; (b) no separate pension from the body; (c) body pays a lump sum; (d) lump sum worked out by the 1981 commutation table.",
             "Rule 14(1)(a): after officiating or temporary appointment in the Central Government, substantive appointment without interruption. (b): the Government servant is not drawing a separate pension from the body for that service. (c): the body pays a lump sum covering pension or service gratuity, plus retirement gratuity. (d): the lump sum is worked out with the commutation table of the CCS (Commutation of Pension) Rules, 1981. Commutation means converting part of a pension into a one-time sum.",
             GREEN,
             "Ab woh chaar conditions. A: officiating ya temporary Central appointment ke baad bina break ke substantive appointment hona chahiye. B: servant us service ke liye body se alag pension nahi le raha ho. C: body ek lump sum deti hai jo pension ya service gratuity aur retirement gratuity, dono cover kare. D: woh lump sum 1981 Commutation of Pension Rules ki commutation table se nikala jaye."),
            ("THE EXPLANATION: PERMISSION",
             "Proper permission is presumed only if he applied with the body's prior permission AND its order says he resigns to join the Centre.",
             "Explanation to Rule 14 (close restatement, read in full on 24.10.2026; ledger R14-EXPL): a Government servant is deemed to have been appointed in the Government with proper permission if (i) he had applied for the service or post in the Government with the previous permission of the autonomous body, AND (ii) the order of the autonomous body clearly indicates that the employee is resigning to join the post in the Government with proper permission of that body. Both limbs are needed; an after-the-fact letter of no objection does not satisfy the Explanation.",
             GREEN,
             "Rule 14 ka ek Explanation hai, aur yahi hissa zyadatar notes miss kar dete hain. Proper permission baad mein aayi friendly letter se prove nahi hoti. Woh tabhi maani jaati hai jab do baatein sach hon. Pehla, usne body ki previous permission lekar Central post ke liye apply kiya. Doosra, body ka khud ka order saaf kahta hai ki woh proper permission ke saath Central post join karne ke liye resign kar raha hai. Dono limb chahiye, warna body ki service nahi ginti."),
            ("14(2): RECIPROCAL ARRANGEMENT",
             "For a State-level body, the lump-sum condition binds it only through the Centre-State reciprocal arrangement. Centre pays under 13(3); the body pays under 14.",
             "Rule 14(2) (close restatement, read in full on 24.10.2026; ledger R14(2), RECIPROCAL): the condition for discharge of pension liability by an autonomous body under a State Government, having a non-contributory pension scheme similar to these rules, shall be binding on that autonomous body in accordance with the reciprocal arrangement entered into by the Central Government with the concerned State Government. Design note (R14-LOGIC): the body settles its own liability by a lump sum, so the Centre does not pay twice; under Rule 13(3) the Centre bears the cost instead.",
             PINK,
             "Ab sub-rule two, woh line jise yeh build pehle unverified flag karta tha. State Government ke under aane wali autonomous body ke liye lump sum dene ki duty aasman se nahi girti. Woh us body par Central Government aur us State ke reciprocal arrangement se binding hoti hai. Yeh Rule 13 ka mirror image hai. Wahan Centre poora kharch uthati hai. Yahan body apna hissa lump sum se chukati hai."),
            ("THE TRAP: 14(3) PSU",
             "PSU service before the Central appointment does NOT count. Same dates: Central body counts, nationalised bank does not.",
             "Rule 14(3) (close restatement): service in a Public Sector Undertaking, including a nationalised bank or a financial institution, before appointment to the Central Government is not qualifying service (R14(3)). Example (invented, R14-EX1): Esha joined a Central autonomous body in 2001, which had a similar non-contributory scheme, and moved to a Central post with proper permission in 2009; the body paid the lump sum, so her body service counts. With the same dates in a nationalised bank, it would not count. Q: can PSU service be counted? A: no.",
             RED,
             "Dhyan dijiye, yahi trap hai. Public sector undertaking ki service, nationalised bank ya financial institution sameta, qualifying service nahi hai. Esha ko dekhiye, jo 2001 mein Central autonomous body mein aayi aur 2009 mein Central post par, lump sum paid: uski service ginti hai. Bilkul wahi dates nationalised bank mein hon to woh ginti hi nahi."),
        ],
        "hook": "REMEMBER: body counts on proper permission plus a lump sum; State body binds by reciprocal arrangement; PSU never!",
        "hook_say": "Yaad rakhiye: autonomous body ki service ginti hai jab body lump sum deti hai, par PSU, nationalised bank aur financial institution ki service kabhi nahi ginti.",
        "covers": ["R14(1)", "R14(1)(a)", "R14(1)(b)", "R14(1)(c)", "R14(1)(d)", "R14(2)", "R14(3)", "R14-EX1", "R14-LOGIC"],
    },
    {
        "id": "c02_07_rules15_17_status_probation_apprentice",
        "chapter": "CHAPTER 7 • RULES 15 TO 17: TEMPORARY STATUS, PROBATION, APPRENTICE",
        "title": "RULES 15-17 — HALF, FULL OR NOTHING?",
        "accent": GREEN, "badge": "RULES 15 • 16 • 17",
        "q": "How much of temporary-status, probation and apprentice service is counted?",
        "q_say": "Sir, temporary status, probation aur apprentice service mein se kitna hissa ginta hai?",
        "boxes": [
            ("RULE 15: HALF",
             "Temporary status granted on or before 31.12.2003, then regularised: only 50 percent of that service counts.",
             "Rule 15 (close restatement, source of the flag cleared on 24.10.2026): a Government servant who was conferred temporary status on or before 31.12.2003 under the Casual Labourers (Grant of Temporary Status and Regularisation) Scheme of Government of India, 1993, notified by the Ministry of Personnel, Public Grievances and Pensions (Department of Personnel and Training), and who was subsequently regularised in Government service, has fifty percent of the service rendered in temporary status counted as qualifying service (R15, LIMIT-R15-50PCT, R15-DOPT). The notifying authority is now read in the rule text; the exact O.M. number and date of 1993 are still not read, and the 10.09.1993 date remains unconfirmed.",
             SKY,
             "Pehle Rule 15. Casual labourer jise thirty-first December 2003 ko ya pehle temporary status mila tha, 1993 Casual Labourers Scheme ke tehat, jise Department of Personnel and Training ne notify kiya, aur jo baad mein regularise hua, uske temporary-status service ka sirf fifty percent ginta hai. Poora nahi, bas aadha. Rule khud us notifying department ka naam leta hai, halanki 1993 ke original order ka number aur date abhi padha nahi gaya."),
            ("RULE 16: PROBATION",
             "Probation service counts if confirmation follows, in the same post or another post.",
             "Rule 16 (close restatement): service rendered on probation against a post counts as qualifying service if the person is subsequently confirmed in the same or another post (R16). Two things are needed: probation against a post, and later confirmation. Probation is a trial period before a job is made permanent; confirmation is the order making it permanent.",
             GREEN,
             "Rule 16 probation ka hai, yani job permanent hone se pehle ka trial period. Probation service tab ginti hai jab baad mein confirmation ho jaye, yani us post par ya doosri post par permanent kar diya jaye. Do cheezein chahiye: kisi post par probation, aur phir confirmation."),
            ("RULE 17: APPRENTICE",
             "Apprentice service does not count. One exception: Subordinate Accounts Service apprentice in IA&AD or Defence Accounts.",
             "Rule 17 (close restatement): apprentice service is not qualifying service, except the service of an apprentice in the Subordinate Accounts Service in the Indian Audit and Accounts Department or the Defence Accounts Department (R17). An apprentice is a person learning a trade or work under a training arrangement.",
             ORANGE,
             "Rule 17 apprentice ka hai, yani woh log jo training arrangement ke tehat koi kaam seekhte hain. General rule yeh hai ki apprentice service ginti nahi. Ek patla exception hai: Subordinate Accounts Service ka apprentice, aur woh bhi sirf Indian Audit and Accounts Department ya Defence Accounts Department mein."),
            ("REAL EXAMPLE",
             "Gopal got temporary status 01.04.2002, regularised 01.04.2006: 4 years, so 2 years count.",
             "Example (invented, R15-EX1): Gopal, a casual labourer, was granted temporary status on 01.04.2002 and regularised on 01.04.2006. The temporary-status stretch is 4 years; 50 percent is 2 years, which count as qualifying service. A temporary-status date of 31.12.2003 or earlier is needed for Rule 15. Q: does apprentice service count? A: generally not; only the Subordinate Accounts Service apprentice in IA&AD or Defence Accounts.",
             ORANGE,
             "Ab ek real example. Gopal ko first April 2002 ko temporary status mila aur first April 2006 ko regularisation hui. Yeh chaar saal ki temporary-status service hai. Chaar ka aadha do saal, isliye do saal ginte hain, chaar nahi."),
            ("THE PATTERN AND TRAP",
             "Benefit comes only when the sequence completes. Trap: do not claim full service under Rule 15.",
             "Pattern (R15-17-PATTERN, a teaching device, not a rule): probation counts only after confirmation; temporary status counts (at half) only after regularisation; apprentice service does not count except the one narrow stream. Keep three dates in the service book: 31.12.2003, the temporary-status date and the regularisation date. Trap: asking for full credit under Rule 15; always check the type of service and the percentage.",
             RED,
             "Dhyan dijiye, yahi trap hai. Ek aasan pattern: benefit tabhi milta hai jab sequence poora ho, probation phir confirmation, temporary status phir regularisation. Aam galti yeh hai ki log Rule 15 ke tehat poora period maang lete hain. Hamesha do cheezein check kijiye: service ka type aur percentage."),
        ],
        "hook": "REMEMBER: temporary status = 50 percent • probation needs confirmation • apprentice = no, except IA&AD or Defence Accounts!",
        "hook_say": "Yaad rakhiye: temporary status fifty percent ginta hai, probation ko confirmation chahiye, aur apprentice service nahi ginti siwaye Indian Audit and Accounts ya Defence Accounts department ke.",
        "covers": ["R15", "LIMIT-R15-50PCT", "R15-EX1", "R15-DOPT", "R16", "R17", "R15-17-PATTERN"],
    },
    {
        "id": "c02_08_rule18_contract",
        "chapter": "CHAPTER 8 • RULE 18: SERVICE ON CONTRACT BEFORE REGULAR APPOINTMENT",
        "title": "RULE 18 — CONTRACT SERVICE NEEDS TWO LIMBS, BOTH OF THEM",
        "accent": BLUE, "badge": "RULE 18",
        "q": "When does earlier contract service count, and what must the person give back?",
        "q_say": "Sir, regular appointment se pehle ki contract service kab ginti hai, aur us vyakti ko kya wapas karna hota hai?",
        "boxes": [
            ("LIMB ONE: A CLEAN SWITCH",
             "Engaged on contract for a fixed period, then on or before 31.12.2003 appointed to a covered post, with no break in duty.",
             "Rule 18(i) (close restatement): the person was first engaged by the Government on contract for a specified period; and then, on or before 31.12.2003, was appointed to the same or another post, in a temporary, officiating or substantive capacity, in an establishment to which these Rules apply, with no interruption in duty (R18(i)).",
             SKY,
             "Pehle limb one. Vyakti ko Government ne pehle ek fix period ke liye contract par liya, aur phir thirty-first December 2003 ko ya pehle usi ya doosri post par appoint kiya, aisi establishment mein jo in Rules mein aati hai, aur duty mein koi break nahi. Contract se regular service tak ka saaf switch hona chahiye."),
            ("LIMB TWO: GIVE BACK THE CPF",
             "Refund the Government's CPF contribution with interest, and any other compensation for that service, as per the 1972 Rules option.",
             "Rule 18(ii) (close restatement): he has refunded to the Government, as per the option exercised under the CCS (Pension) Rules, 1972, the Government's contribution to the Contributory Provident Fund with interest, and any other compensation received for that service (R18(ii)). The two limbs are cumulative: both must be met. A Contributory Provident Fund is a savings fund to which both employee and employer pay.",
             GREEN,
             "Ab limb two. Us vyakti ko 1972 Rules ke option ke hisaab se Government ko refund bhi karna hoga: Contributory Provident Fund mein Government ka jo hissa tha, jisme dono taraf paisa daalti hain, woh interest sameta, aur us service ke liye mila koi doosra compensation bhi. Dono limb chahiye. Ek akela kaafi nahi."),
            ("REAL EXAMPLE",
             "Farid: 2-year contract from 1998, regular post in 2000, no gap, CPF share refunded: counts.",
             "Example (invented, R18-EX1): Farid, an engineer, was engaged on a two-year contract in 1998, was appointed to a regular post in the same department in 2000 with no gap, and refunded the Government's CPF contribution with interest as per his 1972 option. His contract period counts. Q: if the CPF contribution is not refunded? A: the service does not qualify, because limb two is cumulative.",
             ORANGE,
             "Ab ek real example. Farid, ek engineer, 1998 se do saal ke contract par tha, 2000 mein bina gap ke usi department mein regular hua, aur Government ka provident fund hissa interest ke saath refund kar diya. Uski contract period ginti hai. Agar refund na karta, to woh nahi ginti hoti."),
            ("THE TRAP",
             "Trap: one limb is not enough. Both: no break AND refund.",
             "Trap (R18): limb (i) and limb (ii) are cumulative. A clean transition without a refund fails; a refund without a clean transition also fails. The appointment must also be on or before 31.12.2003, the same cut-off line as in Rules 13, 14, 15, 19 and 20.",
             RED,
             "Dhyan dijiye, yahi trap hai. Candidates ko clean switch yaad rehta hai aur refund bhool jaate hain, ya ulta. Dono limb poore chahiye, aur regular appointment thirty-first December 2003 ko ya usse pehle hona chahiye."),
        ],
        "hook": "REMEMBER: Rule 18 = contract, then regular by 31.12.2003 with no break, AND refund the CPF share!",
        "hook_say": "Yaad rakhiye: Rule 18 ke liye contract se regular service tak thirty-first December 2003 tak saaf move chahiye, aur Government ke provident fund hisse ka refund bhi.",
        "covers": ["R18(i)", "R18(ii)", "R18-EX1"],
    },
    {
        "id": "c02_09_no_break_family",
        "chapter": "CHAPTER 9 • THE SAME CONDITION IN FOUR RULES: NO BREAK BEFORE SUBSTANTIVE",
        "title": "THE 'NO INTERRUPTION, THEN SUBSTANTIVE' FAMILY — RULES 11, 13, 14, 18",
        "accent": PINK, "badge": "RULES 11 • 13 • 14 • 18",
        "q": "Which rules share the 'no break, then a substantive post' condition?",
        "q_say": "Sir, main baar baar sunta hoon, no break phir substantive post. Yeh condition kaunse rules mein hai?",
        "boxes": [
            ("RULES 11 AND 13",
             "Rule 11: substantive post in the same or another service. Rule 13: substantive in the State or the Centre.",
             "Rule 11 first proviso: officiating or temporary service counts if followed without interruption by substantive appointment in the same service or post or another. Rule 13(1) proviso and 13(2): officiating or temporary State service counts if followed without interruption by substantive appointment in the State or Central Government. Ledger FAMILY-INTERRUPT-SUBST.",
             SKY,
             "Family ko trace karte hain. Rule 11 mein officiating ya temporary service ginti hai agar uske baad bina break ke substantive appointment ho, usi service mein ya doosri mein. Rule 13 mein State ki officiating ya temporary service ginti hai agar uske baad bina break ke substantive appointment ho, State mein ya Centre mein."),
            ("RULES 14 AND 18",
             "Rule 14(1)(a): Central appointment then substantive with no break. Rule 18: 'no interruption in duty'.",
             "Rule 14(1)(a): after officiating or temporary appointment in the Central Government, substantive appointment without interruption. Rule 18: carries the idea in different words, as 'no interruption in duty' between the contract and the regular appointment (the source treats all four alike; Rule 18 uses different wording, so quote it in its own words).",
             GREEN,
             "Rule 14, clause a mein Central ki officiating ya temporary appointment ke baad bina break ke substantive appointment chahiye. Rule 18 wahi baat alag shabdon mein rakhta hai: duty mein no interruption. Yani chaar rules, ek hi idea, halanki Rule 18 ki wording alag hai."),
            ("THE BRIDGES",
             "Gaps can be bridged: Rule 22(3) joining time, Rule 26(4) joining time plus leave due, then formal condonation.",
             "Bridging tools: Rule 22(3) (interruption between training and appointment at different stations counts up to the permissible joining time); Rule 26(4) (gap within joining time covered by leave due on the date of relief, the rest by formal condonation). Rule 28 deals with condonation of interruption between civil spells.",
             ORANGE,
             "Gaps kabhi kabhi bhare ja sakte hain. Rule 22, sub-rule 3, training aur appointment alag stations par hone par joining time tak ka gap ginta hai. Rule 26, sub-rule 4, joining time ke andar ka gap leave due se cover karta hai, aur baaki ke liye formal condonation chahiye. Gap bhar jaye to pehli service safe rehti hai."),
            ("THE TRAP",
             "Trap: no anchor, no credit. Officiating or temporary service has no value until a substantive post follows without a gap.",
             "Principle: service held in an officiating, temporary, State, body or contract capacity does not qualify until the substantive (or regular) appointment anchors it without a gap, unless the gap is bridged or condoned. Exam use: when asked 'does this earlier service count', first look for the anchor.",
             RED,
             "Dhyan dijiye, yahi trap hai. Pehli officiating, temporary, State ya contract service ek naav jaisi hai jise anchor chahiye: substantive appointment. Agar gap hai aur usse koi bharta ya condone nahi karta, to pehli service nahi ginti."),
        ],
        "hook": "REMEMBER: officiating or temporary service needs a substantive anchor with no gap!",
        "hook_say": "Yaad rakhiye: officiating ya temporary service ko substantive appointment ka anchor chahiye, bina gap ke, jab tak gap bhara ya condone na ho.",
        "covers": ["FAMILY-INTERRUPT-SUBST"],
    },
    {
        "id": "c02_10_rule19_reemployed_civil_pensioner",
        "chapter": "CHAPTER 10 • RULE 19: A RE-EMPLOYED CIVIL PENSIONER'S EARLIER SERVICE",
        "title": "RULE 19 — OLD SERVICE COUNTS ONLY AFTER A FULL REFUND",
        "accent": ORANGE, "badge": "RULE 19(1)-(4)",
        "q": "Who can count earlier service after re-employment, and what must be refunded?",
        "q_say": "Sir, re-employment ke baad purani service kaun ginn sakta hai, aur kya refund karna padta hai?",
        "boxes": [
            ("THE ENTRY GATE: 19(1)",
             "Retired on compensation or invalid pension or gratuity, re-employed on or before 31.12.2003, stopped the pension and refunded: old service counts.",
             "Rule 19(1) (close restatement): a Government servant who retired on compensation pension, invalid pension, compensation gratuity or invalid gratuity, and was re-employed on or before 31.12.2003 in a service or post to which these Rules apply, and who in accordance with his option under the CCS (Pension) Rules, 1972 discontinued the pension on re-employment and refunded (or agreed to refund) the pension drawn, the commuted value of part of pension, and the retirement gratuity including service gratuity, may count his earlier service (R19(1)). Entry gate (R19-ENTRY-GATE): the text names only these four; superannuation and retiring pension cases are outside by implication, with no express words.",
             SKY,
             "Pehle entry gate. Rule 19 sirf un logon ke liye hai jo compensation pension, invalid pension, compensation gratuity ya invalid gratuity par retire hue. Invalid pension buri sehat ke kaaran retire hone wale ko milti hai. Aisa vyakti agar thirty-first December 2003 ko ya pehle re-employed hua aur pension rok kar refund kar diya, to purani service ginti hai. Superannuation ya retiring pension par retire hone wale naam nahi hain, isliye implication se bahar hain."),
            ("WHAT IS REFUNDED: 19(2)",
             "(i) pension drawn before: no refund. (ii) pension element ignored at pay fixation: refund. (iii) other items set off, balance refunded.",
             "Rule 19(2) (close restatement): (i) pension drawn before re-employment need not be refunded (R19(2)(i)). (ii) The PENSION element that was ignored or not taken into account at pay fixation was to be refunded (R19(2)(ii)). The source called it a 'gratuity element'; that is wrong, so do not use that wording. (iii) The pension equivalent of gratuity and of commuted pension that was taken into account at pay fixation is set off against the retirement gratuity and commuted value, and the balance is refunded (R19(2)(iii)); the source omitted this clause.",
             GREEN,
             "Ab kya refund hota hai. Clause one: re-employment se pehle jo pension li ja chuki, woh refund nahi karni. Clause two: re-employment par pay fix karte waqt jo pension element ignore kiya gaya tha, woh refund karna padta hai. Source usse gratuity element kehta tha, par rule text pension element kehta hai. Clause three: jo pay fixation mein count kiya gaya, woh retirement gratuity aur commuted value se set off hota hai, aur balance refund hota hai."),
            ("HOW AND WHEN: 19(3), 19(4)",
             "Up to 36 monthly instalments, first from the month AFTER the option month. Old service counts only after the full refund. Death: the balance is cut from death gratuity.",
             "Rule 19(3) (close restatement): refund in monthly instalments, maximum 36 (LIMIT-36-INSTALMENTS), the first instalment from the month after the month in which the option was exercised (R19-INSTALMENT-START); the right to count the earlier service revives only after the full refund. Rule 19(4): if he dies before the full refund, the unrefunded part is adjusted against the death gratuity payable to the family (R19(4)). Death gratuity is the lump sum paid to the family if a servant dies.",
             ORANGE,
             "Ab kaise aur kab. Refund monthly instalments mein jaata hai, zyada se zyada thirty-six, aur pehli instalment option ke mahine ke agle mahine se. Purani service ginne ka haq poore refund ke baad hi zinda hota hai. Agar refund poora hone se pehle death ho jaye, to bacha hua hissa death gratuity se adjust hota hai, yani family ko milne wali lump sum se."),
            ("REAL EXAMPLE",
             "Gita: option June 1999, refund Rs 72,000 in 36 instalments of Rs 2,000, July 1999 to June 2002. After that, her old service counts.",
             "Example (invented, R19-EX1): Gita, an invalid-pension clerk, was re-employed in 1999 and exercised her option in June 1999. She refunds Rs 72,000 in 36 equal instalments of Rs 2,000 (36 x 2,000 = 72,000); the first is July 1999 (month after the option month) and the last is June 2002. Only then does her old service count. If she died after 20 instalments (Rs 40,000 paid), Rs 32,000 would remain, to be adjusted against the death gratuity. Q: superannuation pension then re-employed, does old service count? A: no, outside the entry gate.",
             ORANGE,
             "Ab numbers ke saath ek real example. Gita, invalid pension par ek clerk, 1999 mein re-employed hui aur June 1999 mein option diya. Us par seventy-two thousand rupees bante hain, to woh thirty-six instalments do-do hazaar ki deti hai, July 1999 se June 2002 tak. Aakhri instalment ke baad hi uski purani service ginti hai. Agar bees instalments ke baad death hoti, to chalees hazaar diye jaate aur battis hazaar death gratuity se kaate jaate."),
            ("THE TRAP",
             "Trap: the instalments start the NEXT month, and counting revives only after the LAST instalment.",
             "Traps: (1) first instalment is the month after the option month, not the option month itself; (2) the right to count is not revived by merely agreeing to refund; it needs the full refund (R19(3)); (3) do not call the clause (ii) item a gratuity element; (4) superannuation or retiring pension is not in the gate. Changed items: R19(2)(ii), R19(2)(iii).",
             RED,
             "Dhyan dijiye, yahi trap hai. Pehli instalment option ke agle mahine, option ke mahine mein nahi. Refund ke liye haan bolna kaafi nahi, kyunki counting aakhri instalment ke baad hi zinda hoti hai. Aur yaad rakhiye, is gate mein sirf compensation ya invalid pension aur gratuity aa sakte hain."),
        ],
        "hook": "REMEMBER: 36 instalments • start the month AFTER the option • count only after the full refund!",
        "hook_say": "Yaad rakhiye: zyada se zyada thirty-six instalments, option ke agle mahine se shuru, aur purani service poore refund ke baad hi ginti hai.",
        "covers": ["R19(1)", "R19-ENTRY-GATE", "R19(2)(i)", "R19(2)(ii)", "R19(2)(iii)", "R19(3)", "LIMIT-36-INSTALMENTS", "R19-INSTALMENT-START", "R19(4)", "R19-EX1"],
    },
    {
        "id": "c02_11_rule19_5_vs_20_5",
        "chapter": "CHAPTER 11 • RULE 19(5) AGAINST RULE 20(5): LATER PENSION AND OLD BENEFITS",
        "title": "RULE 19(5) v RULE 20(5) — SET-OFF FOR CIVIL, NONE FOR MILITARY",
        "accent": PINK, "badge": "RULE 19(5) • 20(5)",
        "q": "What happens to the later pension when old benefits were kept: civil versus military?",
        "q_say": "Sir, jab re-employed vyakti ne purane benefits rakh liye, to civil aur military cases mein baad ka pension kaise chalta hai?",
        "boxes": [
            ("RULE 19(5): A CAP",
             "Civil case: if old pension or gratuity was kept and old service not counted, the later benefit is capped by the difference.",
             "Rule 19(5) (close restatement, filled in after the source gave only a conclusion; R19(5)): where the Government servant kept the earlier pension or gratuity and the old service is not counted, the service gratuity, or the capital value of pension plus retirement gratuity, payable for the later service cannot exceed the difference between what the combined service would have given and what was already granted. The capital value is worked out with the commutation table at final retirement, and an Explanation deals with capital value. Capital value means the one-time worth of a pension.",
             SKY,
             "Pehle Rule 19, sub-rule 5. Agar re-employed civil pensioner ne pehli pension ya gratuity rakhi, aur purani service nahi ginti, to baad ka benefit cap ho jaata hai. Woh us farq se zyada nahi ho sakta jo combined service deti aur jo pehle mil chuka. Capital value matlab pension ki ek baar ki keemat, jo final retirement par commutation table se nikalti hai."),
            ("RULE 20(5): NO CAP",
             "Military case: later civil pension and gratuity are NOT limited by the military pension or gratuity drawn.",
             "Rule 20(5) (close restatement): the pension and gratuity admissible for the later civil service are not subject to any limitation by reference to the military pension and gratuity drawn (R20(5)). It is the opposite of Rule 19(5). Rule 20(3), which the source did not quote, is now confirmed: if he dies before full refund, the unrefunded part is adjusted against the death gratuity (R20(3)).",
             GREEN,
             "Ab Rule 20, sub-rule 5, ulta. Military case mein baad ki civil service ka pension aur gratuity pehle se li ja rahi military pension aur gratuity se limit nahi hote. Yani civil se civil mein set-off cap hai, aur military se civil mein koi cap nahi."),
            ("REAL EXAMPLE",
             "Simplified: combined service would give Rs 10 lakh gratuity, Rs 4 lakh already granted: the later civil gratuity is capped at Rs 6 lakh.",
             "Simplified illustration (invented numbers, only to show the arithmetic of the cap in Rule 19(5); the real calculation uses the commutation table and capital values): combined service would give Rs 10,00,000 and Rs 4,00,000 was already granted, so the later benefit cannot exceed 10,00,000 minus 4,00,000 = Rs 6,00,000. Under Rule 20(5) the same figures would give no cap from the military side.",
             ORANGE,
             "Ab banaye hue numbers se ek simple illustration. Maan lijiye combined service das lakh rupees deti aur chaar lakh pehle mil chuke hain. Rule 19 ke tehat baad ka benefit chhah lakh par cap ho jayega. Rule 20 ke tehat aisa koi cap nahi hoga. Asli calculation commutation tables se hota hai, isliye ise sirf idea samajhiye."),
            ("THE TRAP",
             "19(5) = limitation. 20(5) = no limitation. Exact words of both: check the Gazette.",
             "Memory line: 19(5) limits, 20(5) does not (ADD-B2-2, BONUS-18). Both are close restatements from a secondary reproduction; the exact wording and the limits should be confirmed from the Gazette. Also remember that the refund instalments start the month after the option month, not the option month.",
             RED,
             "Dhyan dijiye, yahi trap hai. In dono ko mix kar diya to marks jaate hain: nineteen five mein limit hai, twenty five mein nahi. Yahan dono texts close restatement hain, isliye exact words Gazette se check kijiye."),
        ],
        "hook": "REMEMBER: 19(5) = limitation applies • 20(5) = no limitation!",
        "hook_say": "Yaad rakhiye: Rule 19 sub-rule 5 mein limitation hai, aur Rule 20 sub-rule 5 mein koi nahi.",
        "covers": ["R19(5)", "R20(5)", "R20(3)"],
    },
    {
        "id": "c02_12_rule20_military",
        "chapter": "CHAPTER 12 • RULE 20: MILITARY SERVICE COUNTED FOR CIVIL PENSION",
        "title": "RULE 20 — WHEN MILITARY SERVICE COUNTS FOR A CIVIL PENSION",
        "accent": GREEN, "badge": "RULE 20",
        "q": "When can earlier military service be counted for civil pension?",
        "q_say": "Sir, pehle ki military service kab civil pension ke liye ginti hai?",
        "boxes": [
            ("THE RULE: 20(1)",
             "Military service, then civil re-employment on or before 31.12.2003, military pension stopped and the old benefits refunded: military service counts.",
             "Rule 20(1) (close restatement): a Government servant who rendered military service and was re-employed in a civil service or post on or before 31.12.2003, and who in accordance with his option under the CCS (Pension) Rules, 1972 discontinued the pension on re-employment and refunded (or agreed to refund) the pension drawn, the commuted value of part of pension, and the retirement gratuity including service gratuity, may count the military service as qualifying service (R20(1)). This is the exception mentioned in the second proviso to Rule 11.",
             SKY,
             "Pehle rule. Kisi ne military service ki aur thirty-first December 2003 ko ya pehle civil post par re-employment hui. Usne re-employment par military pension rok di, 1972 Rules ke apne option ke hisaab se, aur jo pension li thi, pension ke kisi hisse ki commuted value, aur retirement gratuity service gratuity sameta, sab refund kar diya. Tab military service ginti hai. Yahi woh exception hai jise Rule 11 ne point kiya tha."),
            ("REFUND AND GAPS: 20(2), 20(4)",
             "Refund in up to 36 monthly instalments. The counting order also condones the gap between military and civil service.",
             "Rule 20(2) (close restatement): refund of pension, bonus or gratuity in monthly instalments, maximum 36; the right to count revives after the full refund (R20(2); the start month is the month after the option). Rule 20(4): the order counting military service includes condonation of the interruption between military service and civil service (R20(4)). The source adds that interruption inside the military service is also condoned; that was not seen in the restatement read, so it is not confirmed. Condonation means forgiving the gap.",
             GREEN,
             "Ab refund aur gaps. Sub-rule 2 ke tehat refund monthly instalments mein, zyada se zyada thirty-six, aur counting ka haq poore refund ke baad zinda hota hai. Sub-rule 4 ke tehat jo order military service ginta hai woh military aur civil service ke beech ka gap bhi maaf kar deta hai, yani condone. Source military service ke andar ke gaps bhi jodta hai, par woh hissa hum confirm nahi kar paye."),
            ("THE TWO EXPLANATIONS",
             "Kept the military pension and gratuity under the 1972 option: military service NOT counted. Joined military after 31.12.2003: NPS rules, pension stays.",
             "Explanation 2 (R20-EXPL2): if the servant opted under Rule 19 of the 1972 Rules to keep his military pension and gratuity, his military service is not counted. Explanation 3 (R20-EXPL3): a person who joined the military after 31.12.2003 keeps his military pension and is governed by the NPS rules (the New Pension System). So the refund-and-stop route in Rule 20(1) is the real option.",
             ORANGE,
             "Do Explanations yaad rakhiye. Explanation 2: agar vyakti ne military pension aur gratuity rakhni chuni, to uski military service nahi ginti. Explanation 3: jo thirty-first December 2003 ke baad military join karta hai woh New Pension System mein hai, aur military pension rakhta hai. Isliye refund-and-stop hi asli option hai."),
            ("REAL EXAMPLE",
             "Imran: military 01.01.1985 to 31.12.1998 = 14 years, civil from 01.03.1999. Refunded; the order condones 2 months: 14 years count.",
             "Example (invented, R20-EX1): Imran served in the military from 01.01.1985 to 31.12.1998, exactly 14 years, and was re-employed in a civil post on 01.03.1999, a gap of two months. He stopped his military pension, and refunded as required. The counting order under Rule 20(4) condoned the two-month gap. All 14 years count as qualifying service; the two months themselves do not count as service. Q: what if he opted to keep the military pension? A: then military service is not counted (Explanation 2).",
             ORANGE,
             "Ab ek real example. Imran ne first January 1985 se thirty-first December 1998 tak military service ki, bilkul chaudah saal. Woh first March 1999 ko civil post par aaya, do mahine ke gap ke baad. Usne military pension rok di aur refund kar diya. Counting order ne gap maaf kar diya, aur poore chaudah saal ginte hain."),
        ],
        "hook": "REMEMBER: military service counts only by refund-and-stop, joined by 31.12.2003!",
        "hook_say": "Yaad rakhiye: military service tabhi ginti hai jab vyakti ne military pension rok kar refund kiya, aur thirty-first December 2003 tak re-employed hua.",
        "covers": ["R20(1)", "R20(2)", "R20(4)", "R20-EXPL1(i)", "R20-EXPL2", "R20-EXPL3", "R20-EX1"],
    },
    {
        "id": "c02_13_rule20_2022_amendment",
        "chapter": "CHAPTER 13 • RULE 20: THE 2022 AMENDMENT THAT REVERSED A CLAUSE",
        "title": "RULE 20 EXPLANATION 1(ii) — 'NOT REFUNDED' BECAME 'REFUNDED'",
        "accent": RED, "badge": "G.S.R. 770(E) • 2022",
        "q": "What exactly did the 2022 amendment change in Rule 20, and what is obsolete now?",
        "q_say": "Sir, 2022 ke amendment ne Rule 20 mein exactly kya badla, aur kya obsolete ho gaya?",
        "boxes": [
            ("THE AMENDMENT",
             "G.S.R. 770(E), 07.10.2022, substituted Explanation 1, clause (ii) of Rule 20.",
             "G.S.R. 770(E) dated 07.10.2022 substituted Explanation 1 clause (ii) of Rule 20 (GSR-770E-R20, R20-EXPL1(ii)). It took effect from publication. The same notification also amended Rules 8, 46(5)(a), 50(9)(h)(iii) and 76; only Rule 20 lies in Chapter III.",
             SKY,
             "Pehle amendment. G.S.R. 770(E), seventh October 2022, ne Rule 20 ke Explanation 1 ki clause two substitute ki. Chapter 3 ko chhune wala yahi ek Gazette amendment hai."),
            ("OBSOLETE / OLD WORDING",
             "OBSOLETE / HISTORY ONLY: 'was not required to be refunded'. Replaced by 'was to be refunded' from 07.10.2022.",
             "OBSOLETE / HISTORY ONLY (R20-EXPL1(ii)-OLD): the old wording said that the pension element ignored at pay fixation 'was not required to be refunded'. This was replaced by 'was to be refunded' with effect from publication of G.S.R. 770(E) on 07.10.2022. Current text: refund is required. Close restatement; the Gazette text was not read.",
             RED,
             "Yeh sirf history hai. Purani wording kehti thi ki re-employment par pay fix karte waqt jo pension element ignore hua woh refund karne ki zarurat nahi thi. Woh wording obsolete ho gayi. Seventh October 2022 se kehta hai ki woh element refund karna tha. Matlab bilkul palat gaya."),
            ("THE CURRENT PACKAGE",
             "Now: (i) pension drawn before re-employment needs no refund; (ii) the ignored element IS refunded; (iii) set-off, balance refunded.",
             "Current Rule 20 Explanation 1 (close restatement): (i) pension drawn before re-employment need not be refunded (R20-EXPL1(i)); (ii) the pension element ignored at pay fixation was to be refunded (R20-EXPL1(ii), changed); (iii) the pension equivalent of gratuity and commuted pension taken into account at pay fixation is set off against the retirement gratuity and commuted value, and the balance is refunded (R20-EXPL1(iii); the source omitted this clause). This mirrors the clauses of Rule 19(2).",
             GREEN,
             "Ab current package. Clause one: re-employment se pehle li gayi pension refund nahi karni. Clause two: ignore kiya gaya pension element ab refund hota hai. Clause three, jise source ne chhod diya tha: pay fixation mein jo count hua woh retirement gratuity aur commuted value se set off hota hai, aur balance refund hota hai. Yeh Rule 19, sub-rule 2 ko aina dikhata hai."),
            ("THE TRAP",
             "A candidate quoting old notes writes 'not refunded': now wrong. The source also wrongly said 'gratuity element'.",
             "Exam use (BONUS-19): a direct question, 'what did the 2022 amendment do to Rule 20 Explanation 1(ii)': it replaced 'was not required to be refunded' by 'was to be refunded'. Also a comparison question, Rule 19 against Rule 20. Discipline: never treat a one-word amendment as neutral; always answer on the current Gazette position. The source's phrase 'gratuity element' is wrong: it is the pension element.",
             RED,
             "Dhyan dijiye, yahi trap hai. Purane notes wala candidate likhega ki yeh element refund karne ki zarurat nahi, aur woh ab galat hai. Source ne ise galti se gratuity element kaha tha; yeh pension element hai. Ek shabd ka amendment poora matlab palat sakta hai, isliye hamesha current position par answer dijiye."),
        ],
        "hook": "REMEMBER: since 07.10.2022 the pay-fixation pension element IS refunded!",
        "hook_say": "Yaad rakhiye: seventh October 2022 se pay fixation par ignore kiya gaya pension element refund karna padta hai.",
        "covers": ["R20-EXPL1(ii)", "R20-EXPL1(ii)-OLD", "R20-EXPL1(iii)"],
    },
    {
        "id": "c02_14_cutoff_and_refund_logic",
        "chapter": "CHAPTER 14 • THE 31 DECEMBER 2003 LINE AND THE REFUND IDEA",
        "title": "THE 31.12.2003 LINE AND WHY RULES 18, 19, 20 MAKE YOU REFUND",
        "accent": SKY, "badge": "TIMELINE • REFUNDS",
        "q": "Which rules use the 31 December 2003 date, and why do refunds keep appearing?",
        "q_say": "Sir, kaunse rules thirty-first December 2003 date use karte hain, aur refunds baar baar kyun aate hain?",
        "boxes": [
            ("THE DATE LINE",
             "31.12.2003 appears in Rules 13, 14, 15, 18, 19 and 20. The New Pension System starts on 01.01.2004.",
             "TL-31.12.2003: the same cut-off date appears in Rule 13 (first appointment in State pensionable establishment), Rule 14 (first appointment in autonomous body), Rule 15 (temporary status granted), Rule 18 (regular appointment after contract), Rule 19 (re-employment) and Rule 20 (re-employment; and Explanation 3, military joining after the date). The New Pension System (NPS) starts on 01.01.2004.",
             SKY,
             "Yeh timeline hai. Thirty-first December 2003 date Rules 13, 14, 15, 18, 19 aur 20 mein aati hai. Us date ke baad naye joiners New Pension System mein hain, jo first January 2004 se shuru hota hai. Yani yeh outside-service routes purani pension wali generation ke liye hain."),
            ("THE REFUND IDEA",
             "Refund exists to stop double benefit: what you got once is not paid twice.",
             "REFUND-LOGIC and BONUS-17: if Government already gave something for a service (CPF contribution, pension or gratuity), counting the same service again would pay twice. So the person must give back what was received. Rule 18: Government's CPF contribution with interest and other compensation. Rule 19: pension drawn, commuted value, retirement gratuity (with the Rule 19(2) clauses). Rule 20: the same items for military pension.",
             GREEN,
             "Ab refund ka idea. Agar Government us service ke liye kuch de chuki hai, provident fund hissa, pension ya gratuity ke roop mein, to usi service ko dobara ginna double payment ho jayega. Isliye vyakti jo mila tha woh wapas karta hai. Rule 18 provident fund hisse ka hai, Rule 19 civil pension ka, aur Rule 20 military pension ka."),
            ("INSTALMENTS",
             "Rules 19 and 20: refund up to 36 monthly instalments, first in the month after the option. Counting revives only after the full refund.",
             "Rule 19(3) and Rule 20(2): monthly instalments, maximum 36, the first instalment from the month after the month in which the option was exercised; the right to count the earlier service revives only after the full refund (LIMIT-36-INSTALMENTS, R19-INSTALMENT-START). Rule 18 states no instalment scheme in the text read.",
             ORANGE,
             "Instalments par: Rules 19 aur 20 thirty-six monthly instalments tak dete hain, option ke agle mahine se shuru. Counting aakhri instalment ke baad hi zinda hoti hai. Rule 18, jitna text humne padha, instalments ka koi zikr nahi karta."),
            ("THE TRAP",
             "Do not mix: Rule 18 = CPF share. Rule 19 = civil pension. Rule 20 = military pension. Refund is a pre-condition, not a formality.",
             "Trap: candidates treat the refund as a formality. It is a precondition (R19(3), R20(2)); until the full refund, the old service stays uncounted. And do not apply Rules 19 and 20 to superannuation pensioners (outside the Rule 19 gate).",
             RED,
             "Dhyan dijiye, yahi trap hai. Refund koi formality nahi hai. Woh counting ke liye pre-condition hai. Aur teeno rules alag rakhiye: Rule 18 provident fund hissa, Rule 19 civil pensioner, aur Rule 20 military pensioner."),
        ],
        "hook": "REMEMBER: 31.12.2003 • refund = no double benefit • 36 instalments • count only after the last one!",
        "hook_say": "Yaad rakhiye: date thirty-first December 2003 hai, refund double benefit rokte hain, zyada se zyada thirty-six instalments, aur counting aakhri ke baad hi shuru.",
        "covers": ["TL-31.12.2003", "REFUND-LOGIC", "LIMIT-36-INSTALMENTS"],
    },
    {
        "id": "c02_15_rule21_leave",
        "chapter": "CHAPTER 15 • RULE 21: PERIODS OF LEAVE",
        "title": "RULE 21 — WHICH LEAVE COUNTS, AND WHAT IF NOTHING IS WRITTEN?",
        "accent": ORANGE, "badge": "RULE 21",
        "q": "Does leave count as qualifying service, and what if the service book is silent?",
        "q_say": "Sir, leave qualifying service ginti hai kya, aur agar service book kuch na kahe to?",
        "boxes": [
            ("THE RULE",
             "All leave with leave salary counts. Extraordinary leave on a medical certificate counts too.",
             "Rule 21 (close restatement): all periods of leave for which leave salary is payable, and extraordinary leave granted on a medical certificate, count as qualifying service (R21-MAIN). Leave salary is the pay received while on leave. Extraordinary leave (EOL) is leave without pay.",
             SKY,
             "Pehle rule. Har woh leave ginti hai jiske liye leave salary milti hai. Leave salary matlab leave ke dauraan milne wali pay. Extraordinary leave, yani bina pay ki leave, bhi ginti hai agar woh medical certificate par di gayi ho."),
            ("THE PROVISO",
             "Other EOL does not count, but the appointing authority may allow it when granting it: civil commotion, or higher scientific or technical studies.",
             "Proviso to Rule 21 (close restatement): extraordinary leave other than on medical certificate does not count; but the appointing authority may, when granting the leave, allow it to count where the servant was prevented by civil commotion from joining or rejoining duty, or where the leave was for prosecuting higher scientific or technical studies (R21-PROV).",
             GREEN,
             "Ab exception. Doosri extraordinary leave nahi ginti. Par appointing authority, usse grant karte waqt, do cases mein ginne ki permission de sakti hai: servant civil commotion ke kaaran duty join ya rejoin nahi kar paya, ya leave higher scientific ya technical studies ke liye thi."),
            ("THE EXPLANATION: SILENCE",
             "A non-counting EOL needs a definite service-book entry at the time. Late entry is allowed up to six months before superannuation. No entry means it counts.",
             "Explanation to Rule 21 (close restatement): for extraordinary leave that was neither on medical certificate nor allowed under the proviso, a definite entry must be made in the service book at the time that the period will not count as qualifying service. The entry may be made later but not later than six months before superannuation (LIMIT-R21-6MONTHS). If there is no such entry, the extraordinary leave counts as qualifying service (R21-EXPL).",
             ORANGE,
             "Ab Explanation, asli sona. Agar extraordinary leave medical certificate ya proviso se cover nahi hai, to service book mein us waqt definite entry chahiye jo kahe ki yeh period nahi ginega. Woh baad mein bhi ho sakti hai, par superannuation se chhah mahine pehle se zyada late nahi. Agar koi entry nahi, to leave ginti hai."),
            ("REAL EXAMPLE",
             "Hari: 2015 EOL, no entry: counts. If he retires 30.11.2030, the latest late entry is 30.05.2030, not after.",
             "Example (invented, R21-EX1): Hari took extraordinary leave in 2015 for personal reasons; no entry was ever made in his service book, so the period counts. Had the department wished to exclude it, and Hari's superannuation is 30.11.2030, the latest date for a late entry is 30.05.2030 (six calendar months before superannuation; counting method is an assumption, check the exact reckoning in the rule). Q: does EOL on a medical certificate count? A: yes, always.",
             ORANGE,
             "Ab ek real example. Hari ne 2015 mein extraordinary leave li, aur uski service book mein kisi ne entry nahi ki. To woh period ginta hai. Agar department usse bahar rakhna chahta, aur Hari thirtieth November 2030 ko retire hota hai, to late entry thirtieth May 2030 tak, yani chhah mahine pehle, karni hogi."),
            ("THE TRAP: SILENCE",
             "In Rule 21 silence helps the employee. In Rule 23 silence hurts. In Rule 28 silence means forgiven.",
             "Comparison (R21-SILENCE, BONUS-20): Rule 21 Explanation, silence means the EOL counts; Rule 23(2), silence means the suspension period does not count; Rule 28(1), silence in the service book means the interruption is condoned. Three rules, three silent positions. Practical risk: an audit objection arises when an EOL was never regularised yet counted; keep timely entries.",
             RED,
             "Dhyan dijiye, yahi trap hai. Silence ka matlab har rule mein alag hai. Rule 21 mein silence employee ke favour mein hai, leave ginti hai. Rule 23 mein silence nuksaan deta hai, suspension nahi ginta. Rule 28 mein silence ka matlab gap maaf."),
        ],
        "hook": "REMEMBER: Rule 21 silence = EOL counts • entry up to 6 months before retirement!",
        "hook_say": "Yaad rakhiye: Rule 21 mein silence ka matlab extraordinary leave ginti hai, aur late entry superannuation se sirf chhah mahine pehle tak allowed hai.",
        "covers": ["R21-MAIN", "R21-PROV", "R21-EXPL", "LIMIT-R21-6MONTHS", "R21-EX1", "R21-SILENCE"],
    },
    {
        "id": "c02_16_rule22_training",
        "chapter": "CHAPTER 16 • RULE 22: DEPARTMENTAL TRAINING BEFORE APPOINTMENT",
        "title": "RULE 22 — TRAINING PERIOD, JOINING TIME AND THE HEAD OF DEPARTMENT",
        "accent": GREEN, "badge": "RULE 22",
        "q": "Does training before a Group C appointment count, and how are gaps handled?",
        "q_say": "Sir, Group C appointment se pehle ki training ginti hai kya, aur training aur appointment ke beech ke gaps ka kya hota hai?",
        "boxes": [
            ("THE RULE: 22(1), 22(2)",
             "Group C departmental training counts if pay in scale, stipend or nominal allowance was received. Other cases: Government decides by order.",
             "Rule 22(1) (close restatement): where a Government servant had to undergo departmental training before regular appointment to a Group C post, and during the training received pay in the pay scale, a stipend or a nominal allowance, the training period counts as qualifying service (R22(1)). Rule 22(2): in cases not covered by sub-rule (1), the Government decides by order whether the training period immediately preceding the appointment counts (R22(2)). A stipend is a small fixed payment made to a trainee.",
             SKY,
             "Pehle rule. Agar Government servant ko Group C post par regular appointment se pehle departmental training karni padi, aur us dauraan pay scale mein pay, stipend ya nominal allowance mila, to training period ginta hai. Stipend matlab trainee ko milne wali chhoti fix payment. Jo cases isme nahi aate, unke liye sub-rule 2 kehta hai ki Government order se tay karti hai ki appointment se theek pehle ki training ginti hai ya nahi."),
            ("JOINING-TIME GAPS: 22(3), 22(4)",
             "Gap between training and appointment at different stations counts up to the permitted joining time. The excess is regularised by leave, or by EOL from the Head of Department.",
             "Rule 22(3) (close restatement): where training counts and training and regular appointment were at different stations, the interruption caused thereby counts up to the permissible joining time under the transfer rules (R22(3)). Rule 22(4): if the interruption exceeds joining time for administrative reasons, the excess is regularised by granting leave due; if no leave is due, the Head of Department grants extraordinary leave, and the period regularised by EOL counts as qualifying service (R22(4)). Joining time is the time allowed to travel and join the new place.",
             GREEN,
             "Ab gaps. Jab training aur regular appointment alag stations par the, to gap joining time tak ginta hai, yani naye place tak travel aur join karne ka allowed time. Agar gap zyada hai, administrative reasons se, to extra hissa due leave dekar regularise hota hai, aur leave due na ho to Head of Department extraordinary leave deta hai. Woh extraordinary leave period ginta hai."),
            ("REAL EXAMPLE",
             "Jaya, Group C clerk: 6 days beyond joining time, administrative reasons, no leave due: the Head of Department grants 6 days EOL, and they count.",
             "Example (invented, R22-EX1): Jaya was sent for training to another station in 2005. She took 6 days more than the permitted joining time, for administrative reasons, and had no leave due. The Head of Department granted 6 days of extraordinary leave, and those 6 days count as qualifying service. This works only if no leave was due; if leave was due, that leave is used first. Q: when does training not count? A: when no pay, stipend or allowance was received, or when it is outside Rule 22(1) and the Government order does not count it.",
             ORANGE,
             "Ab ek real example. Jaya, Group C clerk, 2005 mein doosre station training par gayi. Usne joining time se chhah din zyada liye, administrative reasons se, aur leave due nahi thi. Head of Department ne chhah din ki extraordinary leave di, aur woh din ginte hain. Agar leave due hoti, woh pehle use hoti."),
            ("WHO IS THE HEAD OF DEPARTMENT?",
             "HoD = the authority named in Schedule I of the Delegation of Financial Powers Rules, 1978, or one designated by the President. Rule 3(1)(p).",
             "Rule 3(1)(p) (R3(1)(p)-HOD, close restatement): Head of Department means the authority specified in Schedule I of the Delegation of Financial Powers Rules, 1978, or an authority designated by the President. In Rule 22(4) it is the HoD who grants the extraordinary leave. Different actors in this chapter (BONUS-21): appointing authority decides on EOL under Rule 21; the Head of Department acts under Rule 22(4); the Head of Office verifies under Rule 30.",
             BLUE,
             "Head of Department kaun hai? Rule 3, clause 1, sub-clause p kehta hai: woh authority jo 1978 Delegation of Financial Powers Rules ke Schedule I mein named hai, ya jo President ne designate kiya. Actors yaad rakhiye: Rule 21 mein appointing authority, Rule 22 sub-rule 4 mein Head of Department, aur Rule 30 mein Head of Office."),
            ("THE TRAP",
             "Rule 21 ordinary EOL does NOT count; Rule 22(4) EOL DOES count, because it is the regularising mechanism.",
             "Contrast: the ordinary EOL of Rule 21 does not count (unless on medical certificate or allowed under the proviso), but EOL granted under Rule 22(4) to regularise excess joining time does count. Do not send the file to the wrong authority: Rule 21 appointing authority, Rule 22(4) Head of Department.",
             RED,
             "Dhyan dijiye, yahi trap hai. Rule 21 ki aam extraordinary leave nahi ginti, par Rule 22 sub-rule 4 ki extraordinary leave ginti hai, kyunki woh regularise karne ka tool hai. Aur check kijiye kaun authority hai, warna file galat desk par chali jayegi."),
        ],
        "hook": "REMEMBER: Rule 22(4) EOL counts — unlike ordinary EOL in Rule 21!",
        "hook_say": "Yaad rakhiye: Rule 22 sub-rule 4 ki extraordinary leave ginti hai, Rule 21 ki aam extraordinary leave ke ulta.",
        "covers": ["R22(1)", "R22(2)", "R22(3)", "R22(4)", "R22-EX1", "R3(1)(p)-HOD"],
    },
    {
        "id": "c02_17_rule23_suspension",
        "chapter": "CHAPTER 17 • RULE 23: THE SUSPENSION PERIOD",
        "title": "RULE 23 — WHEN A SUSPENSION PERIOD COUNTS",
        "accent": ORANGE, "badge": "RULE 23",
        "q": "When does the period of suspension count as qualifying service?",
        "q_say": "Sir, suspension ka period kab qualifying service ginta hai?",
        "boxes": [
            ("THE TEST: 23(1)",
             "At the end of the inquiry: fully exonerated or only a minor penalty, AND suspension held wholly unjustified. Both needed.",
             "Rule 23(1) (close restatement): at the end of the inquiry, the period of suspension counts as qualifying service if (i) the Government servant is fully exonerated or is only awarded a minor penalty, AND (ii) the suspension is held to have been wholly unjustified (R23(1)). The two limbs are cumulative. Suspension means being kept away from duty while an inquiry goes on. Exonerated means cleared of the charge.",
             SKY,
             "Pehle rule. Suspension matlab inquiry chalte waqt duty se door rakha jaana. Inquiry ke ant mein period tabhi ginta hai jab do baatein dono sach hon: servant fully exonerated ho, yani saaf ho jaye, ya usse sirf minor penalty mili ho, aur suspension wholly unjustified thehraya gaya ho. Sirf exoneration kaafi nahi."),
            ("THE OTHER CASES: 23(2)",
             "Every other case: the period does NOT count unless the competent authority expressly declares it, and to what extent.",
             "Rule 23(2) (close restatement): in cases not covered by sub-rule (1), the period does not count as qualifying service unless the competent authority, at the time of passing the orders, expressly declares that it counts, to the extent it declares (R23(2)). Silence means it does not count. Note: the source's authority map lists Rule 23(2) under 'Appointing Authority'; the rule text names the Competent Authority, so the map is corrected (ADD-B2-3-AUTH-MAP-23(2)).",
             GREEN,
             "Ab baaki saare cases. Period nahi ginta jab tak competent authority, orders paas karte waqt, expressly declare na kare ki woh ginta hai, aur kitna ginta hai. Silence ka matlab: nahi ginta. Dhyan dijiye ki rule competent authority ka naam leta hai, appointing authority ka nahi."),
            ("THE ORDER: 23(3)",
             "In every case, the competent authority passes an order stating how much counts, and a definite entry goes in the service book.",
             "Rule 23(3) (close restatement): in every case of suspension, the competent authority shall pass an order specifying the extent, if any, to which the period counts as qualifying service, and a definite entry shall be made in the service book (R23(3)).",
             BLUE,
             "Sub-rule 3 ke tehat har suspension case mein competent authority ko order pass karna hota hai ki period ka kitna hissa, agar koi, ginta hai, aur service book mein definite entry karni hoti hai."),
            ("REAL EXAMPLE",
             "Kiran: 100 days suspended, fully exonerated, held wholly unjustified: all 100 days count. Exonerated but not held unjustified: none, unless the authority declares, say, 60.",
             "Example (invented, R23): Kiran, a clerk, is suspended for 100 days. After the inquiry he is fully exonerated and the suspension is held wholly unjustified: all 100 days count, and the order and service book entry follow. If he was exonerated but the suspension was not held wholly unjustified, none of the 100 days counts unless the competent authority expressly declares, for example, that 60 days count. Q: exonerated but not unjustified? A: not counted without an express declaration, Rule 23(2).",
             ORANGE,
             "Ab ek real example. Kiran sau din suspended hai. Agar woh fully exonerated hai aur suspension wholly unjustified thehra, to poore sau din ginte hain. Agar woh exonerated hai par suspension unjustified nahi thehra, to kuch nahi ginta jab tak authority expressly declare na kare, maan lijiye saath din, aur tab saath ginte hain."),
            ("THE TRAP: SILENCE HURTS",
             "AND, not OR. In Rule 23 silence means NOT counted, the opposite of Rule 21.",
             "Traps (BONUS-20, R21-SILENCE): (1) the two limbs of Rule 23(1) are AND, not OR; (2) silence under Rule 23(2) means the period does not count, the opposite of Rule 21; (3) the order and the service book entry are mandatory in every case under Rule 23(3).",
             RED,
             "Dhyan dijiye, yahi trap hai. Dono conditions AND se judi hain. Aur yahan silence nuksaan deta hai: agar competent authority expressly declare nahi karti, suspension period nahi ginta. Yeh Rule 21 ka ulta hai."),
        ],
        "hook": "REMEMBER: Rule 23 = exonerated AND wholly unjustified; otherwise only by express declaration!",
        "hook_say": "Yaad rakhiye: Rule 23 ke liye exoneration aur wholly unjustified suspension chahiye, warna period tabhi ginta hai jab competent authority expressly declare kare.",
        "covers": ["R23(1)", "R23(2)", "R23(3)", "ADD-B2-3-AUTH-MAP-23(2)"],
    },
    {
        "id": "c02_18_rules24_25_dismissal_reinstatement",
        "chapter": "CHAPTER 18 • RULES 24 AND 25: DISMISSAL, REMOVAL AND REINSTATEMENT",
        "title": "RULES 24-25 — LOSING PAST SERVICE, AND GETTING IT BACK",
        "accent": RED, "badge": "RULES 24 • 25",
        "q": "What happens to past service on dismissal or removal, and when does it come back?",
        "q_say": "Sir, dismissal ya removal par purani service ka kya hota hai, aur woh kab wapas aati hai?",
        "boxes": [
            ("RULE 24: FORFEITURE",
             "Dismissal or removal forfeits past service. Compulsory retirement is NOT named.",
             "Rule 24 (close restatement): dismissal or removal of a Government servant from a service or post entails forfeiture of his past service (R24). Compulsory retirement is not mentioned in the rule (R24, R22-24-ARCH). Forfeiture means the earlier service is wiped out for pension.",
             RED,
             "Pehle Rule 24. Agar Government servant ko dismiss ya remove kiya jata hai, to uski purani service forfeit hoti hai, yani pension ke liye mit jaati hai. Rule 24 compulsory retirement ka zikr hi nahi karta."),
            ("NOT COMPULSORY RETIREMENT",
             "Rule 24 names only dismissal and removal.",
             "Reading (BONUS-22, R22-24-ARCH, a fair summary, not rule text): the two events in Rule 24 are dismissal and removal; compulsory retirement is deliberately not named, so Rule 24 does not forfeit service on compulsory retirement. Practice: always check the order to see which penalty was actually imposed.",
             ORANGE,
             "Compulsory retirement kyun bahar hai? Woh ek penalty hai, par rule uske liye service forfeit nahi karta. Yeh rule ki reading hai, isliye hamesha dekhiye ki order ne asal mein kaunsi penalty lagayi."),
            ("RULE 25(1)",
             "Reinstated on appeal or review: the past service counts again.",
             "Rule 25(1) (close restatement): a Government servant who was dismissed, removed or compulsorily retired and is later reinstated on appeal or review may count his past service as qualifying service (R25(1)). Reinstatement means being taken back into service.",
             GREEN,
             "Ab Rule 25. Agar dismiss, remove ya compulsorily retire kiya gaya vyakti baad mein reinstated hota hai, yani appeal ya review par wapas liya jata hai, to purani service dobara ginti hai."),
            ("RULE 25(2): GAP",
             "The gap and any suspension do not count, unless regularised by a specific order.",
             "Rule 25(2) (close restatement): the interruption between the dismissal, removal or compulsory retirement and the reinstatement, and the period of suspension if any, do not count as qualifying service unless regularised as duty or leave by a specific order of the authority that reinstated him (R25(2)). Compare Rule 26(7): both restore continuity, but the gap does not count (R26-BONUS23-COMPARE).",
             BLUE,
             "Sub-rule 2 line khinchta hai. Dismissal aur reinstatement ke beech ka gap, aur koi bhi suspension period, nahi ginta jab tak reinstating authority khaas order se unhe duty ya leave ke roop mein regularise na kare. Purani service lautti hai, gap nahi."),
            ("REAL EXAMPLE",
             "Mohan: 10 years served, dismissed 2015, reinstated 2017. The 10 years count; the gap does not.",
             "Example (invented): Mohan had 10 years of service when dismissed on 01.03.2015. Under Rule 24 that service was forfeited. On appeal he is reinstated on 01.09.2017. Under Rule 25(1) his 10 years count again. The gap from 01.03.2015 to 01.09.2017 is 2 years 6 months; under Rule 25(2) it counts only if the reinstating authority regularises it as duty or leave by a specific order. Qualifying service therefore stays 10 years, plus any period so regularised.",
             ORANGE,
             "Ab ek real example. Mohan ki service das saal thi jab first March 2015 ko woh dismissed hua. Rule 24 ke tehat woh forfeit ho gayi. First September 2017 ko appeal par reinstatement hui, to Rule 25 ke tehat uske das saal dobara ginte hain. Do saal chhah mahine ka gap nahi ginta, jab tak reinstating authority khaas order se regularise na kare."),
        ],
        "hook": "REMEMBER: Rule 24 forfeits on dismissal or removal, NOT compulsory retirement; Rule 25 restores, minus the gap!",
        "hook_say": "Yaad rakhiye: Rule 24 dismissal ya removal par forfeit karta hai, compulsory retirement par nahi, aur Rule 25 reinstatement par purani service wapas deta hai, gap nahi.",
        "covers": ["R24", "R22-24-ARCH", "R25(1)", "R25(2)", "R26-BONUS23-COMPARE"],
    },
    {
        "id": "c02_19_rule26_resignation_forfeiture",
        "chapter": "CHAPTER 19 • RULE 26(1)-(4): RESIGNATION AND PERMITTED RESIGNATION",
        "title": "RULE 26 (1)-(4) — RESIGNATION FORFEITS, UNLESS PROPERLY PERMITTED",
        "accent": PINK, "badge": "RULE 26(1)-(4)",
        "q": "Does resignation wipe out past service, and how can that be avoided?",
        "q_say": "Sir, resignation purani service mita deti hai kya, aur isse bacha kaise ja sakta hai?",
        "boxes": [
            ("THE GENERAL RULE: 26(1)",
             "Resignation forfeits past service, unless the appointing authority permits withdrawal of the resignation in public interest.",
             "Rule 26(1) (close restatement): resignation from a service or post entails forfeiture of past service, unless the resignation is allowed to be withdrawn in public interest by the appointing authority (R26(1)). Note the correct count: Rule 26 has 8 sub-rules as read, not 26; the source's 'twenty-six sub-rules' is wrong (R26-SUBRULE-COUNT, changed). Appointing authority is the authority that made the appointment.",
             RED,
             "Pehle general rule. Resignation purani service forfeit karti hai, jab tak appointing authority public interest mein resignation withdraw karne ki permission na de. Ek chhota correction: source ne kaha tha Rule 26 mein twenty-six sub-rules hain. Woh galat hai. Rule 26 mein aath sub-rules hain."),
            ("THE SAVING: 26(2)",
             "No forfeiture if the resignation was with proper permission, to take another Government appointment where the service qualifies. Temporary or permanent does not matter.",
             "Rule 26(2) (close restatement): resignation does not entail forfeiture if it was submitted to take up, with proper permission, another appointment under the Government where service qualifies, whether temporary or permanent (R26(2)). This is the door through which Rule 13(2) and Rule 14(1) work.",
             GREEN,
             "Ab saving. Forfeiture nahi hoti agar resignation proper permission ke saath, Government ke andar doosri aisi appointment lene ke liye di gayi thi jahan service qualify karti hai. Nayi appointment temporary ho ya permanent, isse farq nahi padta."),
            ("THE PAPERS: 26(3)",
             "The acceptance order must say that he resigns to join another post with proper permission. The Head of Office makes a specific service-book entry.",
             "Rule 26(3) (close restatement): the order accepting the resignation must clearly indicate that the Government servant is resigning to take up another appointment with proper permission, and the Head of Office shall make a specific entry in the service book (R26(3)). Chain of three links: permission, indication in the order, service-book entry. A weak link invites an audit objection. Example (invented, R26-EX1): Meena, an Assistant, resigns with permission to join another Central post; the order says so and the entry is made, so her past service is safe.",
             BLUE,
             "Sub-rule 3 papers ka hai. Resignation accept karne wale order mein saaf likhna chahiye ki vyakti proper permission ke saath doosri post join karne ke liye resign kar raha hai, aur Head of Office service book mein khaas entry karta hai. Permission, order, entry: teen kadiyan. Meena ko dekhiye, ek Assistant, jo doosri Central post join karne ke liye permission ke saath resign karti hai. Order aur entry sahi hon to uski purani service safe hai."),
            ("THE GAP: 26(4)",
             "Different stations: the gap within joining time is covered by leave due on the relief date. The rest needs formal condonation.",
             "Rule 26(4) (close restatement): where the old and new posts are at different stations, the gap within the joining time is covered by leave due on the date of relief, and the remaining gap needs formal condonation (R26(4)). Illustration (invented numbers): gap of 11 days, joining time 6 days: 6 days covered by leave due, 5 days need condonation. Link: without the permission papers the case falls in Rule 26(1) (R13-R26-LINK).",
             ORANGE,
             "Sub-rule 4 do posts ke beech ke gap ka hai jab woh alag stations par hain. Jo hissa joining time ke andar hai woh relief ki date par due leave se cover hota hai, aur baaki ke liye formal condonation chahiye. Jaise gyarah din ka gap aur chhah din ka joining time: chhah din cover, paanch ke liye condonation."),
        ],
        "hook": "REMEMBER: resignation forfeits • proper permission saves • order plus service-book entry!",
        "hook_say": "Yaad rakhiye: resignation purani service forfeit karti hai, doosri Government post ke liye proper permission use bacha deti hai, aur order aur service book entry mein woh likha hona chahiye.",
        "covers": ["R26(1)", "R26-SUBRULE-COUNT", "R26(2)", "R26(3)", "R26(4)", "R26-EX1", "R13-R26-LINK"],
    },
    {
        "id": "c02_20_rule26_withdrawal",
        "chapter": "CHAPTER 20 • RULE 26(5)-(8): WITHDRAWING A RESIGNATION",
        "title": "RULE 26 (5)-(8) — FOUR CONDITIONS, ONE BAR AND ONE SPECIAL SAVING",
        "accent": SKY, "badge": "RULE 26(5)-(8)",
        "q": "On what conditions can a resignation be withdrawn, and what does withdrawal give back?",
        "q_say": "Sir, resignation kis condition par withdraw ho sakti hai, aur withdrawal se exactly kya wapas milta hai?",
        "boxes": [
            ("FOUR CONDITIONS: 26(5)",
             "(i) compelling reasons, clean record, material change; (ii) no improper conduct in between; (iii) absence not over 90 days; (iv) post available.",
             "Rule 26(5) (close restatement; all four needed): (i) the resignation was for compelling reasons without any stain on integrity, efficiency or conduct, and circumstances have materially changed; (ii) the conduct in the intervening period was not improper; (iii) the absence from duty did not exceed 90 days (LIMIT-R26-90DAYS); (iv) the post resigned from, or a comparable post, is available (R26(5)).",
             SKY,
             "Pehle withdrawal ki chaar conditions. One: resignation compelling reasons se di gayi thi, integrity, efficiency ya conduct par koi daag nahi tha, aur circumstances materially badal gaye. Two: beech ka conduct improper nahi tha. Three: absence ninety din se zyada nahi hui. Four: wahi post ya uske barabar ka post available hai."),
            ("THE BAR: 26(6)",
             "No withdrawal if the resignation was for a private commercial company, or a corporation or company that Government owns or controls.",
             "Rule 26(6) (close restatement): withdrawal is not allowed if the resignation was for the purpose of taking up an appointment in a private commercial company, or in a corporation or company wholly or substantially owned or controlled by the Government. The rule text read also adds a body controlled or financed by Government; the source omitted this limb (R26(6)).",
             RED,
             "Ab bar. Withdrawal allowed nahi hai agar resignation private commercial company, ya Government ki owned ya controlled corporation ya company join karne ke liye di gayi thi. Jitna rule text humne padha usme Government se controlled ya financed body bhi joda gaya hai, jise source ne chhod diya tha."),
            ("WHAT WITHDRAWAL GIVES: 26(7)",
             "The withdrawal order includes condonation of the interruption, but the interruption period itself does not count.",
             "Rule 26(7) (close restatement): when withdrawal is allowed, the order includes condonation of the interruption in service; the period of interruption does not count as qualifying service (R26(7), R26-BONUS23-COMPARE). Continuity returns, the gap is not counted. Same theme as reinstatement under Rule 25(2).",
             GREEN,
             "Jab withdrawal allowed hoti hai, order mein interruption ki condonation apne aap shamil hoti hai, isliye continuity bach jaati hai. Par interruption period khud nahi ginta. Continuity lautti hai, gap nahi."),
            ("SPECIAL: 26(8)",
             "Resignation made for Rule 35 or 36 purposes does not forfeit past Government service. Gazette not read.",
             "Rule 26(8) (close restatement; R26(8), changed because the source never mentions it): a resignation made for the purposes of Rule 35 or Rule 36 (dealt with in a later batch) does not forfeit past Government service. FLAG: seen on two secondary reproductions (a page and the staffnews book PDF, both read through a summarising tool, which gave the wording 'A resignation submitted for the purpose of rule 35 or rule 36 shall not entail forfeiture of past service'); not confirmed against the Gazette; verify before final use. Rule 26(8) is one of the 8 sub-rules.",
             ORANGE,
             "Ek aur sub-rule hai jo source ne kabhi mention nahi kiya. Rule 26, sub-rule 8, kehta hai ki Rules 35 ya 36 ke liye di gayi resignation purani Government service forfeit nahi karti; woh rules agle part mein aate hain. Humne yahi baat do secondary copies mein dekhi, Gazette mein nahi, isliye final use se pehle Gazette check kijiye."),
            ("THE TRAP",
             "Trap: 'withdrawal allowed' does not mean the gap counts. The 90-day limit is hard, and the bar for private companies is absolute.",
             "Traps (BONUS-23): (1) the withdrawal order saves continuity but the gap does not count; (2) the 90-day absence limit in 26(5)(iii) is a hard condition; (3) the private commercial company bar in 26(6) applies however clean the record. Example: absence of 80 days can pass condition (iii); 95 days cannot. Q: can a resignation be withdrawn? A: yes, in public interest by the appointing authority, on four conditions, except the barred cases.",
             RED,
             "Dhyan dijiye, yahi trap hai. Bahut log sochte hain ki withdrawal allowed hui to gap bhi ginta hai. Nahin ginta. Ninety din ki limit sakht hai: assi din ki absence pass ho sakti hai, ninety-five nahi. Aur private commercial company ka bar record jitna saaf ho, phir bhi lagta hai."),
        ],
        "hook": "REMEMBER: 4 conditions, 90 days max • no withdrawal for a private company • gap never counts!",
        "hook_say": "Yaad rakhiye: chaar conditions, zyada se zyada ninety din, private company ke liye withdrawal nahi, aur gap kabhi nahi ginta.",
        "covers": ["R26(5)", "LIMIT-R26-90DAYS", "R26(6)", "R26(7)", "R26(8)", "R26-BONUS23-COMPARE"],
    },
    {
        "id": "c02_21_rule27_interruption",
        "chapter": "CHAPTER 21 • RULE 27: WHAT AN INTERRUPTION DOES TO PAST SERVICE",
        "title": "RULE 27 — INTERRUPTION FORFEITS, EXCEPT FIVE CASES",
        "accent": ORANGE, "badge": "RULE 27",
        "q": "What does an interruption in service do to past service, and what are the exceptions?",
        "q_say": "Sir, service mein interruption purani service ka kya karti hai, aur exceptions kya hain?",
        "boxes": [
            ("GENERAL RULE, CASES (a) AND (b)",
             "Interruption forfeits past service, except: (a) authorised leave; (b) unauthorised absence after authorised leave, while the post is not substantively filled.",
             "Rule 27(1) (close restatement): interruption in service entails forfeiture of past service except in these cases (R27(1)). (a) Authorised leave of absence (R27(1)(a)). (b) Unauthorised absence in continuation of authorised leave of absence, so long as the post is not substantively filled (R27(1)(b)). Unauthorised absence is absence without sanction.",
             SKY,
             "Pehle general rule. Service mein interruption purani service forfeit karti hai, paanch cases ke siwa. Case a: authorised leave of absence. Case b: unauthorised absence jo authorised leave ke baad chalti hai, par tab tak jab tak us post par koi substantively appoint nahi hua."),
            ("CASES (c), (d), (e)",
             "(c) suspension then reinstatement, or death, permitted retirement or superannuation during suspension; (d) transfer to non-qualifying service in public interest; (e) joining time.",
             "Rule 27(1)(c) (read as: reinstated, or dies or retires while under suspension; R27(1)(c)): suspension immediately followed by reinstatement in the same or another post, or death, permitted retirement or retirement on superannuation during suspension. (d) Transfer to a non-qualifying service in an establishment under Government control, ordered by the competent authority in public interest (R27(1)(d)). (e) Joining time on transfer from one post to another (R27(1)(e)).",
             GREEN,
             "Case c: aisa suspension jiske turant baad reinstatement ho, ya servant ki death ho jaye, retire karne diya jaye, ya suspension ke dauraan superannuation par retire ho jaye. Case d: Government control wali establishment mein non-qualifying service par transfer, jo competent authority ne public interest mein order kiya ho. Case e: transfer par joining time."),
            ("POWER AND EXAMPLE: 27(2)",
             "The appointing authority may, by order, turn unauthorised absence into extraordinary leave, with retrospective effect.",
             "Rule 27(2) (close restatement): the appointing authority may, by order, commute retrospectively unauthorised absence into extraordinary leave (R27(2)). Example (invented, R27-EX1): Omar, a clerk, went on authorised leave and then stayed away for 6 days without sanction; his post had not been substantively filled, so case (b) saved his past service. Had the post been substantively filled, the same absence would have forfeited the past service.",
             ORANGE,
             "Sub-rule 2 appointing authority ko power deta hai: order se woh unauthorised absence ko extraordinary leave mein badal sakti hai, retrospective effect ke saath. Ek example. Omar authorised leave par gaya aur phir chhah din bina sanction ke door raha. Uska post substantively bhara nahi gaya tha, isliye purani service safe rahi. Agar post bhar gaya hota, woh absence use forfeit kar deti."),
            ("THE TRAP",
             "Do not learn '5 exceptions, 2 conditions' as a rule. Conditions sit in (b), (c) and (d). Anything outside the five forfeits.",
             "Flag (R27-MNEMONIC, UNVERIFIED as a rule): the source's mnemonic '5 exceptions, 2 conditions' is a memory device only; clause (c) also carries conditions, so do not teach it as a rule. Reasoning on (b) and (d) (BONUS-24, source reasoning, not rule text): clause (b) protects only while the post is not substantively filled; clause (d) needs the transfer to be ordered by the competent authority in public interest. Any interruption outside the five forfeits past service.",
             RED,
             "Dhyan dijiye, yahi trap hai. Source ek mnemonic padhata hai, five exceptions and two conditions, par woh sirf yaad rakhne ka device hai. Clause c mein bhi conditions hain. Clause b post substantively na bharne par tika hai, aur clause d ko competent authority ka public interest order chahiye. Baaki koi bhi interruption purani service forfeit karta hai."),
        ],
        "hook": "REMEMBER: Rule 27 = interruption forfeits, five exceptions (a)-(e), and 27(2) can commute absence into EOL!",
        "hook_say": "Yaad rakhiye: interruption paanch cases ke siwa purani service forfeit karta hai, aur sub-rule 2 appointing authority ko absence ko extraordinary leave mein badalne deta hai.",
        "covers": ["R27(1)", "R27(1)(a)", "R27(1)(b)", "R27(1)(c)", "R27(1)(d)", "R27(1)(e)", "R27(2)", "R27-EX1", "R27-MNEMONIC"],
    },
    {
        "id": "c02_22_rule28_condonation",
        "chapter": "CHAPTER 22 • RULE 28: CONDONATION OF INTERRUPTION",
        "title": "RULE 28 — WHEN A GAP IS FORGIVEN, AND WHEN IT IS NOT",
        "accent": GREEN, "badge": "RULE 28",
        "q": "When is a gap between two civil spells forgiven, and can the authority refuse?",
        "q_say": "Sir, do spells of civil service ke beech ka gap kab maaf hota hai, aur authority mana kar sakti hai?",
        "boxes": [
            ("AUTOMATIC: 28(1)",
             "A gap between two spells of civil service is automatically forgiven, and the earlier service qualifies, unless the service book shows otherwise.",
             "Rule 28(1) (close restatement): interruption between two spells of civil service under the Government is, unless the service book indicates otherwise, deemed to be condoned automatically, and the service before the interruption qualifies. Civil service paid from Defence Services Estimates or Railway Estimates is included (R28(1)). Condonation means the gap is forgiven.",
             SKY,
             "Pehle automatic route. Government ke under civil service ke do spells ke beech ka gap maaf maan liya jaata hai, yani condoned, jab tak service book ulta na dikhaye. Gap se pehle ki service phir qualify karti hai. Defence Services Estimates ya Railway Estimates se pay ki gayi civil service bhi isme aati hai."),
            ("THE LIMITS: 28(2), 28(3)",
             "Not for gaps caused by resignation, dismissal, removal or strike. And the gap period itself never counts.",
             "Rule 28(2) (close restatement): automatic condonation does not apply to interruption caused by resignation, dismissal, removal or participation in a strike (R28(2)). Rule 28(3): the period of interruption itself does not count as qualifying service (R28(3)). Only the earlier service is saved.",
             RED,
             "Ab limits. Automatic condonation tab nahi lagti jab gap resignation, dismissal, removal ya strike mein hissa lene se hua ho. Aur sub-rule 3 ke tehat gap period khud kabhi nahi ginta. Sirf gap se pehle ki service bachti hai."),
            ("DISCRETION: 28(4)-(6)",
             "Otherwise the appointing authority may consider condonation. Refusal only in exceptional and grave circumstances, and only after a fair hearing in person.",
             "Rule 28(4) (close restatement): the appointing authority may consider condonation of interruption (R28(4)). 28(5): refusal only in exceptional and grave circumstances (R28(5)). 28(6): before refusing, the servant must be given a reasonable opportunity to make a representation and to be heard in person (R28(6)). In short: 28(1) is silence means forgiven; 28(4) is when silence is not enough, the authority decides.",
             GREEN,
             "Sub-rules 4 se 6 discretionary route dete hain. Appointing authority condonation par vichaar kar sakti hai. Mana karna sirf exceptional aur grave circumstances mein ho sakta hai, aur mana karne se pehle servant ko reasonable mauka milna chahiye ki woh apna case rakhe aur khud suna jaye."),
            ("EXAMPLE AND TRAP",
             "Nisha: 6-month gap between two civil spells, no contrary entry: condoned, earlier service safe, the 6 months do not count.",
             "Example (invented, R28-EX1): Nisha left one civil post and joined another after a gap of 6 months; the service book has no contrary entry. The gap is condoned automatically and her earlier service qualifies, but the 6 months themselves do not count. Q: does automatic condonation make the gap count? A: no, Rule 28(3). Link (BONUS-25): Rule 27 says what an interruption does, Rule 28 says how to undo it, Rule 30 says how it is verified.",
             ORANGE,
             "Ab ek real example. Nisha ne ek civil post chhodi aur chhah mahine baad doosri join ki, service book mein koi ulti entry nahi thi. Gap apne aap condone ho gaya aur uski pehli service safe hai, par chhah mahine khud nahi ginte. Dhyan dijiye, yahi trap hai: condonation pehli service bachati hai, gap nahi ginti."),
        ],
        "hook": "REMEMBER: Rule 28 saves earlier service, never the gap; not for resignation, dismissal, removal or strike!",
        "hook_say": "Yaad rakhiye: Rule 28 pehli service bachata hai par gap kabhi nahi ginta, aur automatic condonation resignation, dismissal, removal ya strike par nahi lagti.",
        "covers": ["R28(1)", "R28(2)", "R28(3)", "R28(4)", "R28(5)", "R28(6)", "R28-EX1"],
    },
    {
        "id": "c02_23_rule29_international",
        "chapter": "CHAPTER 23 • RULE 29: DEPUTATION TO THE UN AND OTHER INTERNATIONAL BODIES",
        "title": "RULE 29 — SERVICE ABROAD IN AN INTERNATIONAL ORGANISATION",
        "accent": BLUE, "badge": "RULE 29",
        "q": "If a servant is sent to an international organisation, does that service count?",
        "q_say": "Sir, agar Government servant ko United Nations ya kisi doosri international body bheja jaye, to woh service ginti hai?",
        "boxes": [
            ("WHO IS COVERED",
             "A servant on foreign service in the UN Secretariat or UN bodies, IMF, IBRD, ADB, Commonwealth Secretariat or any other international organisation.",
             "Rule 29 (close restatement): a Government servant who is on foreign service in the United Nations Secretariat or other United Nations bodies, the International Monetary Fund, the International Bank for Reconstruction and Development, the Asian Development Bank, the Commonwealth Secretariat, or any other international organisation. Foreign service means service outside the Government's own cadre, on loan. Deputation means being sent on temporary posting elsewhere.",
             SKY,
             "Pehle dekhein kaun cover hai. Rule 29 us Government servant ke liye hai jo foreign service par hai, yani Government ke apne cadre se bahar loan par, United Nations Secretariat ya doosri UN bodies, IMF, World Bank group ka IBRD, Asian Development Bank, Commonwealth Secretariat, ya kisi bhi doosri international organisation mein."),
            ("THE OPTION",
             "He chooses: pay pension contribution and count the service, or do not pay and do not count it.",
             "Rule 29 (R29): the servant may opt either (1) to pay pension contribution for that foreign service and have it counted as qualifying service, or (2) not to pay the contribution and not have the service counted.",
             GREEN,
             "Uske paas option hai. Ya to woh us foreign service ke liye pension contribution deta hai aur service ginti hai, ya woh nahi deta aur service nahi ginti."),
            ("THE REFUND",
             "If he chooses not to count it, the contributions he already paid are refunded.",
             "Rule 29 (R29-REFUND): if the servant opts not to have the service counted, the contributions already paid by him are refunded to him.",
             ORANGE,
             "Agar woh service ginne ka option nahi leta, to usne jo contributions de diye the woh usse refund kar diye jaate hain."),
            ("THE TRAP",
             "It is the servant's option, not a decision of the Government or the department.",
             "Trap (ADD-B2-3): the door in Rule 29 is in the Government servant's hand, not the Government's. It is not an administrative decision. Q: who chooses? A: the Government servant.",
             RED,
             "Dhyan dijiye, yahi trap hai. Choice Government servant ki hai, department ki nahi. Yeh koi administrative decision nahi hai."),
        ],
        "hook": "REMEMBER: Rule 29 = the servant's option: pay and count, or don't pay and get a refund!",
        "hook_say": "Yaad rakhiye: Rule 29 mein servant ka option hai: pay karo aur gino, ya na do aur contributions refund le lo.",
        "covers": ["R29", "R29-REFUND"],
    },
    {
        "id": "c02_24_rule30_verification_triggers",
        "chapter": "CHAPTER 24 • RULE 30(1)-(2): VERIFYING QUALIFYING SERVICE AND FORMAT 4",
        "title": "RULE 30 (1)-(2) — WHEN SERVICE IS VERIFIED, AND BY WHOM",
        "accent": PINK, "badge": "RULE 30(1)-(2)",
        "q": "When must qualifying service be verified, who does it, and how is it communicated?",
        "q_say": "Sir, qualifying service kab verify honi chahiye, kaun karta hai, aur kaise bataya jata hai?",
        "boxes": [
            ("THE TWO TRIGGERS",
             "After 18 years of service, and again when 5 years remain before superannuation.",
             "Rule 30(1) (close restatement): the service is verified after the Government servant completes 18 years of service, and again when five years remain before the date of superannuation (R30(1), LIMIT-R30-18YRS, LIMIT-R30-5YRS). The source says 'on each occasion'; a summarising tool reading the staffnews book PDF later quoted it as the opening words of Rule 30(1), but the Gazette was not read, so treat the phrase as likely but not Gazette-confirmed (R30-ON-EACH-OCCASION); the two triggers themselves are confirmed. Superannuation means retirement on reaching the age of retirement.",
             SKY,
             "Pehle rule. Qualifying service do points par verify hoti hai: Government servant ke athara saal service poore hone par, aur phir jab superannuation se paanch saal bache hon, yani retirement ki umar par retirement se paanch saal pehle. Rule kehta hai, on each occasion. Yeh phrase ab full chapter text mein padha gaya hai, Gazette PDF nahi, isliye wording ko close restatement maaniye."),
            ("WHO AND HOW",
             "The Head of Office, with the Accounts Officer, verifies and tells the servant in Format 4.",
             "Rule 30(1) (close restatement): the Head of Office, in consultation with the Accounts Officer, verifies the service, determines the qualifying service and communicates it in Format 4 (R30(1), FORMAT-4). Rule 30(2): the Head of Office follows the procedure of Rule 57(1)(a) (R30(2)); Rule 57 was amended by G.S.R. 410(E) of 2024, which introduced Form 6-A, so check the current Rule 57. The source did not give 30(2).",
             GREEN,
             "Kaun karta hai? Head of Office, Accounts Officer ke saath consultation mein, service verify karta hai, qualifying service nikalta hai aur Format 4 mein batata hai. Sub-rule 2 kehta hai ki Head of Office Rule 57, clause 1, sub-clause a ki procedure follow karta hai. Rule 57 2024 mein amend hua aur Form 6-A laaya, isliye current Rule 57 check kijiye. Source ne sub-rule 2 diya hi nahi tha."),
            ("REAL EXAMPLE",
             "Lata joined 01.07.2005: first check at 18 years on 01.07.2023. If she retires on 30.06.2035, the second check falls on 30.06.2030.",
             "Example (invented, R30-EX1; superannuation date assumed): Lata, a senior assistant, joined on 01.07.2005. Eighteen years are complete on 01.07.2023, which is the first verification, and Format 4 goes to her. If her superannuation is on 30.06.2035, five years before is 30.06.2030, the second verification, after which the two records are matched. Q: what is Format 4? A: the format in which the Head of Office tells the servant the verified qualifying service.",
             ORANGE,
             "Ab ek real example. Lata, senior assistant, first July 2005 ko join hui. Uske athara saal first July 2023 ko poore hote hain, to pehli verification tabhi padti hai, aur use Format 4 milta hai. Maan lijiye woh thirtieth June 2035 ko retire hoti hai. Paanch saal pehle thirtieth June 2030 hai, to doosri verification tabhi padti hai, aur dono records match hote hain."),
            ("THE TRAP",
             "Two triggers, not one. A verification is a duty on the office, not a favour on request.",
             "Traps: (1) there are two triggers, 18 years and 5 years before superannuation; (2) the communication is in Format 4, not in Form 6-A (a different document, Rule 57); (3) 'on each occasion' is likely but not Gazette-confirmed. The source's later remark that the whole scheme leans on service-book entries (BONUS-26) is practical advice, not rule text.",
             RED,
             "Dhyan dijiye, yahi trap hai. Do triggers hain, ek nahi. Servant ko certificate Format 4 mein milta hai; Form 6-A Rule 57 ke tehat alag document hai. Aur on each occasion wali phrase ab text mein hai, par Gazette PDF nahi padhi gayi."),
        ],
        "hook": "REMEMBER: verify at 18 years and at 5 years before retirement • Head of Office with Accounts Officer • Format 4!",
        "hook_say": "Yaad rakhiye: athara saal par aur retirement se paanch saal pehle verify, Head of Office Accounts Officer ke saath, aur Format 4 mein batao.",
        "covers": ["R30(1)", "FORMAT-4", "LIMIT-R30-18YRS", "LIMIT-R30-5YRS", "R30(2)", "R30-EX1", "R30-ON-EACH-OCCASION"],
    },
    {
        "id": "c02_25_rule30_finality_report",
        "chapter": "CHAPTER 25 • RULE 30(3)-(5): SPECIAL EVENTS, FINALITY AND THE 31 JANUARY REPORT",
        "title": "RULE 30 (3)-(5) — EXTRA OCCASIONS, FINAL VERIFICATION, YEARLY REPORT",
        "accent": SKY, "badge": "RULE 30(3)-(5)",
        "q": "Beyond the two fixed checks, when else is verification done, and is it final?",
        "q_say": "Sir, do fix checks ke alawa verification kab hoti hai, aur kya woh final hai?",
        "boxes": [
            ("EXTRA EVENTS: 30(3)",
             "Verification also on transfer from a temporary department, closure of a department, or a post declared surplus.",
             "Rule 30(3) (close restatement): verification may also be done on (i) transfer from a temporary department, (ii) closure of a department, or (iii) a post being declared surplus (R30(3)). A surplus post is one no longer needed.",
             SKY,
             "Pehle sub-rule 3. Verification teen khaas events par bhi hoti hai: temporary department se transfer, department ka closure, ya post ko surplus declare kiya jaana, yani uski zarurat nahi rahi."),
            ("FINAL: 30(4)",
             "A verification is final. It is reopened only if a later rule or order changes the conditions for qualifying.",
             "Rule 30(4) (close restatement): the verification, once done, is final and is not reopened, except when a later rule or order changes the conditions for service to qualify (R30(4)). Q: is verification final? A: yes, subject to that one exception.",
             GREEN,
             "Sub-rule 4 verification ko final banata hai. Woh sirf tab dobara khulti hai jab baad ka koi rule ya order service qualify hone ki conditions badal de. Bas wahi ek exception, aur kuch nahi."),
            ("YEARLY REPORT: 30(5)",
             "By 31 January each year, a report to the Secretary of the Administrative Ministry: who was due a certificate, who got one, and why not for the rest.",
             "Rule 30(5) (close restatement): by 31 January each year (TL-31JAN), a report to the Secretary of the Administrative Ministry: the Government servants due to receive a certificate under Rule 30(1) in the previous calendar year, those who actually received it, and the reasons for the cases where it was not given (R30(5)).",
             ORANGE,
             "Sub-rule 5 saalana report hai. Har saal thirty-first January tak Administrative Ministry ke Secretary ko report jaati hai, jismein likha hota hai pichle calendar year mein kisko certificate milna tha, kisko asal mein mila, aur baaki ke reasons kya the."),
            ("THE TRAP",
             "Final does not mean never: a changed rule or order reopens it. And the report date is 31 January, for the PREVIOUS calendar year.",
             "Traps: (1) 'final' has one exception, a later change in rules or orders about conditions of qualifying (R30(4)); (2) the report is due by 31 January and covers the previous calendar year (R30(5), TL-31JAN); (3) Rule 30(2) refers to Rule 57, which was amended in 2024.",
             RED,
             "Dhyan dijiye, yahi trap hai. Final ka matlab kabhi nahi nahi hota: baad ka rule ya order ise dobara khol sakta hai. Aur report thirty-first January tak due hai, pichle calendar year ke liye."),
        ],
        "hook": "REMEMBER: 30(3) three events • 30(4) final • 30(5) report by 31 January!",
        "hook_say": "Yaad rakhiye: teen khaas events, verification final jab tak rules na badlein, aur report Secretary ko thirty-first January tak.",
        "covers": ["R30(3)", "R30(4)", "R30(5)", "TL-31JAN", "R30-EX1"],
    },
    {
        "id": "c02_26_sep2025_guidelines",
        "chapter": "CHAPTER 26 • THE SEPTEMBER 2025 DoPPW GUIDELINES AND RULE 30",
        "title": "O.M. 4/35/2024-P&PW(D)/10377 — MAKING RULE 30 A MONITORED DUTY",
        "accent": RED, "badge": "O.M. SEPT 2025",
        "q": "How do the 2025 DoPPW guidelines strengthen the Rule 30 verification chain?",
        "q_say": "Sir, 2025 ki DoPPW guidelines Rule 30 ki verification chain ko kaise mazboot karti hain?",
        "boxes": [
            ("THE O.M.",
             "DoPPW O.M. No. 4/35/2024-P&PW(D)/10377: comprehensive guidelines for timely payment of retirement dues and issue of PPOs. Month: Sept 2025; exact day unreadable.",
             "Office Memorandum No. 4/35/2024-P&PW(D)/10377 of the Department of Pension and Pensioners' Welfare, 'Comprehensive Guidelines for timely payment of retirement dues (pension and pensionary dues) and issue of Pension Payment Orders (PPOs)'. Number and subject confirmed from the PDF read (OM-SEP2025-4/35/2024-10377). UNVERIFIED (OM-SEP2025-DATE): month Sept 2025 taken from the PDF path only; the day was illegible, so do not give a full date. A PPO is the order that authorises the pension.",
             SKY,
             "Pehle O.M. Yeh DoPPW Office Memorandum number 4 slash 35 slash 2024 hyphen P and PW bracket D slash 10377 hai, jiska naam hai comprehensive guidelines for timely payment of retirement dues and issue of Pension Payment Orders. PPO woh order hai jo pension authorise karta hai. Mahina September 2025 hai, par exact din padha nahi ja saka, isliye poora date nahi dete."),
            ("HEAD OF DEPARTMENT DUTY",
             "The HoD ensures verification certificates at 18 years and 5 years before retirement, with a compliance report to the Secretary by 31 January.",
             "Section F(g) of the O.M. (OM-SEP2025-HOD-VERIF): the Head of Department is to ensure that verification certificates of qualifying service are issued at 18 years of service and five years before retirement, and a compliance report goes to the Secretary of the Ministry or Department by 31 January each year. Ties to the Rule 30(5) report.",
             GREEN,
             "O.M. duty Head of Department par daalta hai. Usse pakka karna hai ki athara saal service ke baad aur retirement se paanch saal pehle verification certificates issue hon, aur compliance report har saal thirty-first January tak Secretary ko jaye. Yeh seedha Rule 30 se judta hai."),
            ("RECORDS AND ESCALATION",
             "100 percent e-HRMS adoption; CAPF on the full Employee Payroll System; files returned more than twice are escalated; Nodal Officer meets PAOs monthly.",
             "Para 1(A): 100 percent e-HRMS adoption, and for CAPF personnel full adoption of the Employee Payroll System (EPS) (OM-SEP2025-EHRMS). Section F(c),(i): files returned more than twice for missing documents are escalated to a higher level (OM-SEP2025-ESCALATE). Section F(i): the Nodal Officer meets Pay and Accounts Offices every month (OM-SEP2025-NODAL). UNVERIFIED (OM-SEP2025-MANUAL): the source says electronically verified records will be preferred and manual records gradually discouraged; this was not seen in the parts of the O.M. read.",
             ORANGE,
             "Baaki points: one hundred percent e-HRMS adoption, yani digital service records, aur central armed police forces ke liye poora Employee Payroll System. Missing documents ke kaaran do baar se zyada wapas aayi pension file upar escalate hoti hai. Nodal Officer har mahine Pay and Accounts Offices se milta hai. Source yeh bhi kehta hai ki manual records discourage honge, par humne woh padhe hue pages mein nahi dekha."),
            ("THE LINK AND THE TRAP",
             "Rule 30 gives the trigger. The O.M. adds accountability. The PPO is due not later than two months before retirement (Rule 63(1)(a), quoted in the O.M., next batches).",
             "Link: Rule 30 is the statutory trigger (18 years and 5 years); the O.M. binds it to accountability (HoD duty, annual report, digitised records, escalation). The O.M. para 2 quotes Rule 63(1)(a): PPO not later than two months before retirement (R63(1)(a)-2MONTHS); Rule 63 itself is for Batch 5. Q: whom does the compliance report go to, and when? A: the Secretary of the Ministry or Department, by 31 January each year. Trap: it is an O.M. (administrative layer), not a rule amendment.",
             RED,
             "Dhyan dijiye, yahi trap hai. Yeh ek Office Memorandum hai, administrative instruction, Rules ka amendment nahi. Rule 30 trigger deta hai, aur O.M. accountability jodta hai. Wahi O.M. Rule 63 quote karta hai, ki PPO retirement se do mahine pehle tak due hai; woh rule agle part ka hai."),
        ],
        "hook": "REMEMBER: Rule 30 = the trigger • the O.M. = HoD duty and report to the Secretary by 31 January!",
        "hook_say": "Yaad rakhiye: Rule 30 trigger deta hai, O.M. Head of Department ko responsible banata hai, aur compliance report thirty-first January tak Secretary ko jaati hai.",
        "covers": ["OM-SEP2025-4/35/2024-10377", "OM-SEP2025-DATE", "OM-SEP2025-HOD-VERIF", "OM-SEP2025-EHRMS", "OM-SEP2025-ESCALATE", "OM-SEP2025-NODAL", "OM-SEP2025-MANUAL", "R63(1)(a)-2MONTHS"],
    },
    {
        "id": "c02_27_authority_map_open_flags",
        "chapter": "CHAPTER 27 • CHAPTER III: WHO DECIDES WHAT, AND WHAT IS STILL UNCONFIRMED",
        "title": "THE AUTHORITY MAP FOR RULES 11-30 AND THE OPEN-FLAG LIST",
        "accent": ORANGE, "badge": "AUTHORITIES • FLAGS",
        "q": "Which authority acts in which rule, and which points are still not confirmed?",
        "q_say": "Sir, kaun authority kaunse rule mein act karti hai, aur kaunse points abhi confirm nahi hain?",
        "boxes": [
            ("APPOINTING AUTHORITY",
             "Rule 21 (allow EOL), 26(1) and 26(5) (withdrawal), 27(2) (commute absence), 28(4)-(6) (condonation, hearing before refusal).",
             "Appointing authority (ADD-B2-3-AUTH-MAP-REST): Rule 21 proviso, Rule 26 (withdrawal of resignation), Rule 27(2), Rule 28(4) to (6). The source's list put Rule 23(2) here; the rule text names the Competent Authority, so Rule 23 is under the next card (ADD-B2-3-AUTH-MAP-23(2)).",
             SKY,
             "Appointing authority Rule 21 mein act karti hai, kuch extraordinary leave ginne ki permission dene ke liye; Rule 26 mein resignation withdraw karne par; Rule 27, sub-rule 2 mein absence commute karne ke liye; aur Rule 28, sub-rules 4 se 6 mein condonation par, jahan mana karne se pehle sunwai zaroori hai."),
            ("OTHER AUTHORITIES",
             "Competent authority: Rule 23. Head of Department: Rule 22(4). Head of Office: Rule 26(3) and 30(1). Accounts Officer: consulted in 30(1). Government: Rule 22(2). The servant: Rule 29.",
             "Competent authority: Rule 23(2) and 23(3) (extent of suspension period, service book entry). Head of Department: Rule 22(4) (EOL when no leave is due). Head of Office: Rule 26(3) (service book entry) and Rule 30(1) (verification, with the Accounts Officer). Government: Rule 22(2) (training by order). Rule 29: the option is the Government servant's. Liability: Rule 13(3), the Centre; Rule 14(1)(c), the autonomous body by lump sum.",
             GREEN,
             "Competent authority Rule 23 mein act karti hai. Head of Department Rule 22, sub-rule 4 mein. Head of Office Rule 26 sub-rule 3 mein aur Rule 30 mein, Accounts Officer ke saath. Government Rule 22 sub-rule 2 mein decide karti hai. Rule 29 mein choice servant ki hai. Liability par, Rule 13 mein Centre deti hai aur Rule 14 mein autonomous body lump sum deti hai."),
            ("STILL NOT CONFIRMED",
             "Now closed: Rule 14(2), Rule 15 notifying authority, Rule 26(8), Rule 30 'on each occasion'. Still open: Gazette wording, Sept 2025 O.M. date, G.S.R. 410(E) date.",
             "Flag audit of 24.10.2026, after reading the whole of Chapter III. CLOSED (the text is now read, so the flag is removed): Rule 14(2) reciprocal arrangement; the Explanation to Rule 14; the notifying authority and scheme name in Rule 15; Rule 26(8) (resignation for Rule 35 or 36); the words on each occasion in Rule 30(1); Rule 20(3) and Rule 30(2). STILL OPEN: (1) every rule is a close restatement, not the Gazette PDF or India Code text; (2) the exact day of the Sept 2025 DoPPW O.M.; (3) the effective date of G.S.R. 410(E), 16.11.2024 on secondary sites against 13.11.2024 on a 120-day count; (4) the 1993 O.M. number and date behind Rule 15; (5) the six-month method used in the Rule 21 example; (6) the source's glosses R11-INTERRUPTION-DEF, R12-BONUS13-CPF and R27-MNEMONIC, which are teaching devices, not rule text. Flags that belong to Batch 1 (Rules 4, 6 and 7) stay there: ADD-B2-3-OPENFLAGS-B1.",
             RED,
             "Ab honest flag list, jo humare clause by clause audit ke baad revise hui. Kai purane flags band ho gaye, kyunki humne poora chapter text padha. Rule 14 sub-rule 2 padhaya gaya. Rule 14 ka Explanation padhaya gaya. Rule 15 ka notifying department padhaya gaya. Rule 26 sub-rule 8 aur Rule 30 ke on each occasion confirm hain. Jo khula hai woh yeh. Yahan saari rule wording close restatement hai, Gazette text nahi. 2025 O.M. ka exact din legible nahi. 2024 notification ki effective date tay nahi. Aur Rule 21 wale example ka six month method ek assumption hai."),
            ("CROSS-LINK AND CURRENCY",
             "Rule 37 comes next. 2025 Explanation applies Rules 7, 8, 41 and 44(5) to PSU-absorbed employees. A 2026 Rule 37(7) proviso is for the next batch.",
             "Cross-link: G.S.R. 340(E) of 22.05.2025 amends Rule 37 only; its Explanation applies Rules 7, 8, 41 and 44(5) analogously to PSU-absorbed employees (GSR-340E). A 2026 amendment, G.S.R. 775(E) (about 7 Sept 2026, date unclear, seen on a re-hosted PDF, not the Gazette), adds a proviso to Rule 37(7) for ex-Ordnance Factory Board employees who do not opt for DPSU absorption (deemed deputation until retirement). It lies outside Rules 11 to 30. Flags for ledger items that were carried to Batch 1: ADD-B2-3-OPENFLAGS-B1.",
             BLUE,
             "Aage ke liye ek cross-link. Rule 37 ka 2025 amendment Rules 7, 8, 41 aur 44, sub-rule 5, ko public sector undertakings mein absorbed employees par lagata hai. 2026 ka amendment, G.S.R. 775(E), Rule 37 mein proviso jodta hai, ex-Ordnance Factory Board employees ke liye. Humne woh sirf re-hosted PDF par dekha, isliye woh agle part ka hai aur unconfirmed."),
        ],
        "hook": "REMEMBER: know the actor in each rule — appointing, competent, HoD, Head of Office!",
        "hook_say": "Yaad rakhiye: hamesha jaan lijiye kaun authority kaunse rule mein act karti hai, appointing authority, competent authority, Head of Department ya Head of Office.",
        "covers": ["ADD-B2-3-AUTH-MAP-REST", "ADD-B2-3-AUTH-MAP-23(2)", "ADD-B2-3-OPENFLAGS-B1", "GSR-340E"],
    },
    {
        "id": "c02_28_decision_chain",
        "chapter": "CHAPTER 28 • DECISION CHAIN: DOES THIS SERVICE COUNT?",
        "title": "FOUR STEPS TO DECIDE IF A STRETCH OF SERVICE COUNTS",
        "accent": GREEN, "badge": "DECISION CHAIN",
        "flow": "countchain",
        "q": "Given a stretch of earlier service, how do we decide step by step if it counts?",
        "q_say": "Sir, purani service ka koi hissa dekh kar, step by step kaise tay karein ki woh ginti hai ya nahi?",
        "boxes": [
            ("STEP 1: ANCHOR AND START",
             "Rule 11 and 12: duties and pay regulated; substantive anchor with no break; not before 18.",
             "Check Rule 11 (start, anchor, age 18) and Rule 12 (duties and pay both regulated by Government). Is there a substantive appointment after any officiating or temporary stretch, with no break?",
             SKY,
             "Step one: start aur anchor check kijiye. Duties aur pay dono Government se regulated hain? Kisi officiating ya temporary hisse ke baad bina break ke substantive appointment hai, aur woh athara saal ke baad hai?"),
            ("STEP 2: WHICH ROUTE?",
             "State 13, body 14, temp status 15, probation 16, apprentice 17, contract 18, civil pensioner 19, military 20, leave 21, training 22, suspension 23, international 29.",
             "Pick the route: Rules 13 to 23 and 29; check the 31.12.2003 line, the percentage (Rule 15: 50 percent), refunds (Rules 18, 19, 20) and instalments (36).",
             BLUE,
             "Step two: route chuniye. State, autonomous body, temporary status, probation, apprentice, contract, re-employed pensioner, military, leave, training, suspension ya international organisation. Har ek mein date line, percentage aur refund check kijiye."),
            ("STEP 3: ANY LOSS EVENT?",
             "Dismissal or removal (24), resignation (26), interruption (27): past service can be forfeited.",
             "Check for loss events: Rule 24 (dismissal, removal), Rule 26(1) (resignation), Rule 27(1) (interruption).",
             RED,
             "Step three: loss event dekhiye. Rule 24 mein dismissal ya removal, Rule 26 mein resignation, ya Rule 27 mein interruption. Inme se koi bhi pehli service mita sakta hai."),
            ("STEP 4: SAVE AND PROVE",
             "Saves: 25, 26(2), 27 exceptions, 28. Proof: Rule 30, Format 4, at 18 years and 5 years before retirement.",
             "Check the saving tools: Rule 25 (reinstatement), Rule 26(2), (7), Rule 27(1)(a)-(e), 27(2), Rule 28. Then proof: Rule 30 verification in Format 4 at 18 years and five years before superannuation, with the 31 January report. Three questions in one line: does it count (Rules 11-23, 25, 27-30)? Did I lose it (24, 26)? Can I get it back (25, 28, 27(2))?",
             GREEN,
             "Step four: dekhiye kya bachata hai, aur phir prove kijiye. Reinstatement, permitted resignation, Rule 27 ke exceptions aur Rule 28 mein condonation. Uske baad Head of Office Format 4 mein verify karta hai. Short mein: ginti hai ya nahi, kya maine kho di, kya wapas mil sakti hai."),
        ],
        "hook": "REMEMBER: anchor, route, loss, save and prove!",
        "hook_say": "Yaad rakhiye: anchor check karo, route chuno, loss event dekho, phir dekho kya bachata hai aur prove karo.",
        "covers": ["CH3-STRUCTURE", "R11-MAIN", "R12-MAIN"],
    },
    {
        "id": "c02_29_table_counting_routes",
        "chapter": "CHAPTER 29 • REVISION TABLE 1: EVERY COUNTING ROUTE IN RULES 11 TO 23 AND 29",
        "title": "TABLE 1 — WHICH SERVICE COUNTS, AND ON WHAT CONDITION",
        "accent": SKY, "badge": "REVISION • TABLE",
        "layout": "table",
        "col1": "RULES",
        "col2": "WHAT THEY DECIDE, IN SIMPLE ENGLISH",
        "lab_w": 430,
        "q": "Put the whole chapter on one table: which service counts, and what must be true for it?",
        "q_say": "Sir, poora chapter ek table par mil sakta hai, taaki main saare counting routes ek saath dekh sakun?",
        "intro": "Ab revision karte hain, aur yahan se screen ka shape badal jata hai. Cards ki jagah aapko ek revision table ki rows dikhengi, bilkul waise hi jaise printed revision sheet hoti hai. Yeh pehli table har us rule ko ikattha karti hai jo credit deta hai.",
        "rows": [
            ("RULES 11 • 12 — START",
             "Charge of the first post starts the clock; officiating or temporary needs a substantive post with no break; nothing before age 18. Duties AND pay regulated by Government.",
             SKY,
             "Pehli row foundation deti hai. Rule 11 clock us din start karta hai jab woh pehla post charge karta hai. Agar woh post officiating ya temporary thi, to bina break ke substantive post aana chahiye, aur athara saal se pehle kuch nahi ginta, Rule 20 ki military service ke siwa. Rule 12 control test jodta hai: duties aur pay dono Government se regulated hone chahiye, aur service Consolidated Fund of India ya Local Fund se pay honi chahiye."),
            ("RULES 13 • 14 — TRANSFER",
             "State or autonomous body service, appointed by 31.12.2003, proper permission, no break, body pays a lump sum. A PSU, bank or financial institution never counts.",
             GREEN,
             "Doosri row do transfers cover karti hai. Rule 13 ke tehat State pensionable establishment ki service permanent transfer par ya proper permission ke saath resignation par ginti hai, aur kharch Central Government uthati hai. Rule 14 ke tehat autonomous body ki service ginti hai agar body ki scheme milti julti ho, permission proper ho, chaar conditions poori hon, aur body 1981 ki commutation table se nikala lump sum de. Par Rule 14 ka sub-rule 3 public sector undertaking, nationalised bank aur financial institution ko bahar kar deta hai."),
            ("RULES 15 • 16 • 17",
             "Temporary status of a casual labourer: 50 percent only. Probation: counts once confirmed. Apprentice: nil, except Subordinate Accounts Service.",
             ORANGE,
             "Teesri row sabse chhoti trio hai. Rule 15 temporary status mein ki gayi service ka sirf fifty percent deta hai, woh bhi jab status 2003 ke end tak mila ho aur regularisation hui ho. Rule 16 probation ginta hai jab confirmation ho jaye. Rule 17 apprentice service ke liye kuch bhi nahi deta, siwaye Audit ya Defence Accounts Department ke Subordinate Accounts Service apprentice ke."),
            ("RULES 18 • 19 • 20 — REFUND",
             "Contract before 31.12.2003 with the CPF share refunded; earlier civil service of a re-employed pensioner; military service. Refund in at most 36 instalments.",
             RED,
             "Chauthi row teen refund routes rakhti hai. Rule 18 2003 ke end tak regular appointment se pehle ki contract service ginta hai, bashart ki contributory provident fund mein Government ka hissa refund ho. Rule 19 re-employed pensioner ki purani civil service ginta hai, aur Rule 20 military service. Teeno mein paisa settle hona chahiye, refund zyada se zyada thirty-six monthly instalments tak ja sakta hai, aur Rule 19 ke sub-rule 5 ka cap Rule 20 mein nahi hai."),
            ("RULES 21 • 22 • 23 • 29",
             "Leave with leave salary and medical EOL; Group C training; suspension only if exonerated or minor penalty AND wholly unjustified; foreign service by option.",
             PINK,
             "Paanchvi row credit side band karti hai. Rule 21 leave salary wali saari leave ginta hai, aur medical certificate par di gayi extraordinary leave bhi. Rule 22 Group C appointment se pehle ki departmental training ginta hai. Rule 23 suspension tabhi ginta hai jab woh fully exonerated ho ya minor penalty mile, aur suspension wholly unjustified thehre. Rule 29 servant ko option deta hai ki pension contributions dekar foreign service gine."),
        ],
        "footer": "CLASSIC UPSC TRAP: a route counts only when its own condition is met - no anchor, no credit, and a PSU is never an autonomous body!",
        "hook": "REMEMBER: five rows hold every counting route in the chapter!",
        "hook_say": "Table one ki paanch rows yaad rakhiye: start aur control, State aur body, status aur probation, refund routes, aur leave, training, suspension aur foreign service.",
    },
    {
        "id": "c02_30_table_loss_save_prove",
        "chapter": "CHAPTER 30 • REVISION TABLE 2: LOSS, SAVE AND PROVE IN RULES 24 TO 30",
        "title": "TABLE 2 — WHAT IS FORFEITED, WHAT IS SAVED, AND WHAT MUST BE PROVED",
        "accent": RED, "badge": "REVISION • TABLE",
        "layout": "table",
        "col1": "RULES",
        "col2": "WHAT THEY DO TO PAST SERVICE",
        "lab_w": 430,
        "q": "Which events take past service away, which save it, and who finally certifies it?",
        "q_say": "Sir, aur chapter ka doosra side? Kya service chheenta hai, kya bachata hai, aur aakhir mein prove kaun karta hai?",
        "rows": [
            ("RULE 24 • 25 — LOSS, REPAIR",
             "Dismissal or removal forfeits past service; compulsory retirement is not named. Reinstated, he counts it again; the gap only if regularised as duty or leave.",
             RED,
             "Table two loss aur repair se khulti hai. Rule 24 chhota aur sakht hai: dismissal ya removal purani service ka forfeiture laata hai, aur compulsory retirement ka naam wahan nahi hai. Rule 25 repair karta hai: appeal ya review par reinstatement hone par woh apni purani service dobara ginta hai, par gap, aur usme koi suspension, tabhi ginta hai jab reinstating authority khaas order se us period ko duty ya leave ke roop mein regularise kare."),
            ("RULE 26 — RESIGNATION",
             "Resignation forfeits, unless withdrawn in the public interest or made with proper permission for another qualifying post. 90 days; never for a private company.",
             ORANGE,
             "Row two, Rule 26, resignation. Resignation purani service forfeit karti hai, jab tak woh public interest mein withdraw na ho, ya proper permission ke saath aisi doosri Government appointment ke liye na di gayi ho jahan service qualify kare. Withdrawal ke liye chaar conditions, jisme ninety din se zyada absence nahi, aur jahan resignation private commercial company join karne ke liye thi wahan woh barred hai."),
            ("RULE 27 — INTERRUPTION",
             "Interruption forfeits, except (a) authorised leave, (b) certain unauthorised absence, (c) specified suspension, (d) public-interest transfer, (e) joining time. 27(2): commutation.",
             BLUE,
             "Row three, Rule 27, interruption. Interruption purani service forfeit karta hai, paanch cases ke siwa: authorised leave; authorised leave ke baad ki unauthorised absence jab post substantively bhara na ho; suspension jiske baad reinstatement, ya death, permitted retirement ya suspension ke dauraan superannuation; public interest mein non-qualifying service par transfer; aur joining time. Sub-rule 2 appointing authority ko unauthorised absence ko extraordinary leave mein badalne deta hai, retrospective effect se."),
            ("RULE 28 — CONDONATION",
             "A gap between two civil spells is condoned automatically if the service book is silent. Never after resignation, dismissal, removal or strike; the gap never counts.",
             PINK,
             "Row four, Rule 28, condonation. Jahan service book ulta kuch nahi kehti, wahan do spells ke beech ka gap apne aap condone hota hai aur pehli service qualifying rehti hai, aur Defence Services Estimates ya Railway Estimates se pay ki gayi service bhi isme aati hai. Par yeh gap par kabhi nahi lagta jo resignation, dismissal, removal ya strike se bana ho, aur gap khud kabhi nahi ginta."),
            ("RULE 30 — PROOF",
             "Head of Office with the Accounts Officer verifies at 18 years and at five years before superannuation, in Format 4; final. Report to the Secretary by 31 January.",
             SKY,
             "Row five, Rule 30, proof. Head of Office, Accounts Officer ke saath, service verify karta hai aur qualifying service Format 4 mein batata hai, athara saal ke baad har mauke par aur phir jab superannuation se paanch saal bache hon. Woh verification final hai jab tak rules ya orders badal kar dobara dekhne ki zarurat na paida karein, aur har saal thirty-first January tak Secretary ko report jaati hai."),
        ],
        "footer": "CLASSIC UPSC TRAP: Rule 28 condones the interruption and saves the earlier service, but the gap itself never becomes qualifying service!",
        "hook": "REMEMBER: lose (24, 26, 27), save (25, 26(2), 27(1), 28), prove (30)!",
        "hook_say": "Table two yaad rakhiye: loss Rules 24, 26 aur 27 mein, rescue Rules 25, 26 sub-rule 2, Rule 27 ke paanch exceptions aur Rule 28 mein, aur proof Rule 30 mein.",
    },
    {
        "id": "c02_31_chart_how_much_counts",
        "chapter": "CHAPTER 31 • BAR CHART: HOW MUCH OF EACH KIND OF SERVICE IS COUNTED",
        "title": "CHART — THE SHARE OF SERVICE THAT COUNTS, RULE BY RULE",
        "accent": GREEN, "badge": "BAR CHART • SHARE COUNTED",
        "layout": "chart",
        "q": "If the service counts, does the whole period count, or only a part of it?",
        "q_say": "Sir, jab koi service ginti hai, to poora period ginta hai ya sirf kuch percentage?",
        "intro": "Chart us sawaal ka jawab deta hai jo prose chhupa leta hai: kitna. Har bar ek route hai, aur bar ki lambai batati hai ki us service ka kitna hissa qualifying service banta hai. Poori bars poora period leti hain. Ek aadhi bar Rule 15 hai. Khaali bars kuch bhi nahi deti.",
        "rows": [
            ("Rule 16 • probation, then confirmation",
             100,
             GREEN,
             "Rule 16 poori bar hai. Confirmation ke baad probation ka poora period ginta hai, usi post par ho ya doosri post par."),
            ("Rule 21 • leave with leave salary",
             100,
             SKY,
             "Rule 21 poori bar hai. Jis leave ke liye leave salary milti hai woh saari ginti hai, aur medical certificate par di gayi extraordinary leave bhi."),
            ("Rule 18 • contract, CPF share refunded",
             100,
             BLUE,
             "Rule 18 poori bar hai, par daam ke saath. Poora contract period ginta hai agar 2003 ke end tak covered post par bina break appointment hui, aur provident fund mein Government ka hissa refund hua."),
            ("Rule 19 or 20 • earlier service, refunded",
             100,
             ORANGE,
             "Rules 19 aur 20 poori bars hain, ek baar paisa settle ho jaye. Purani civil ya military service tab poora ginti hai jab pehle li gayi pension aur gratuity refund ho jaye, ya unhe lena band karne ka option exercise ho."),
            ("Rule 15 • temporary status, casual labour",
             50,
             YELLOW,
             "Rule 15 chapter ki akeli aadhi bar hai. Temporary status mein ki gayi service ka fifty percent ginta hai, bashart ki status 2003 ke end tak mila ho aur regularisation hui ho."),
            ("Rule 17 • apprentice service",
             0,
             PINK,
             "Rule 17 khaali bar hai. Apprentice service ke liye kuch nahi, do patle exceptions ke saath, Indian Audit and Accounts Department ya Defence Accounts Department ka Subordinate Accounts Service apprentice."),
            ("Rule 14(3) • PSU or nationalised bank",
             0,
             RED,
             "Rule 14 ka sub-rule 3 khaali bar hai. Public sector undertaking, jisme nationalised bank ya financial institution bhi hai, ki service Central Government join karne se pehle kabhi qualifying service nahi banti."),
            ("Rule 27 • the interruption itself",
             0,
             SKY,
             "Gap khud hamesha khaali bar hai. Jahan Rule 27 purani service bachata hai, aur jahan Rule 28 interruption condone karta hai, wahan bhi gap ka period qualifying service nahi ginta."),
        ],
        "footer": "CLASSIC UPSC TRAP: a rule can save the PAST service and still give nothing for the gap - check both bars, not one!",
        "hook": "REMEMBER: one half bar (Rule 15), three empty bars (17, 14(3), the gap), everything else full!",
        "hook_say": "Chart yaad rakhiye: Rule 15 akeli aadhi bar, Rules 17, 14 sub-rule 3 aur gap khud khaali bars, aur baaki har counting rule poora period leta hai.",
    },
    {
        "id": "c02_32_table_provisos_explanations",
        "chapter": "CHAPTER 32 • REVISION TABLE 3: EVERY PROVISO AND EXPLANATION IN ONE PLACE",
        "title": "TABLE 3 — THE FINE PRINT OF CHAPTER III, CLAUSE BY CLAUSE",
        "accent": ORANGE, "badge": "REVISION • FINE PRINT",
        "layout": "table",
        "col1": "FINE PRINT",
        "col2": "WHAT THE PROVISO OR EXPLANATION ACTUALLY SAYS",
        "lab_w": 430,
        "q": "Where does a senior examiner look first? Which provisos and Explanations carry the marks?",
        "q_say": "Sir, marks asal mein kahan bethe hain? Kaunse provisos aur Explanations examiners ko pasand hain?",
        "rows": [
            ("RULE 11 — TWO PROVISOS",
             "Officiating or temporary service must be followed without interruption by substantive appointment; nothing before 18 counts except military service under Rule 20.",
             SKY,
             "Rule 11 do provisos ek saans mein rakhta hai. Pehla anchor: officiating ya temporary service ke baad bina interruption substantive appointment chahiye, usi ya doosri service ya post mein. Doosra age line: athara saal se pehle ki service nahi ginti, siwaye Rule 20 ke tehat civil pension ke liye gini jaane wali military service."),
            ("RULES 12 • 13 — EXPLAINED",
             "Service means paid from the Consolidated Fund of India or a Local Fund, excluding an establishment without a non-contributory scheme. Proper permission: prior permission taken, order reciting it.",
             GREEN,
             "Rule 12 ka Explanation service define karta hai: Government ke under service, Consolidated Fund of India ya Local Fund se pay, aur aisi establishment ki service bahar, jiske paas non-contributory pension scheme nahi, jab tak Government usse qualifying na maane. Rule 13 ka Explanation proper permission define karta hai: usne State ki previous permission se apply kiya, aur State ka order kehta hai ki woh proper permission ke saath resign kar raha hai."),
            ("RULE 14 — 14(2) AND EXPL.",
             "Four conditions (a) to (d), lump sum on the 1981 commutation table. 14(2): a State-level body is bound by the reciprocal arrangement. Explanation: two limbs of permission.",
             ORANGE,
             "Rule 14 chapter ka sabse bhaari rule hai. Sub-rule 1 mein chaar conditions, jo 1981 commutation table se nikale lump sum par khatam hoti hain. Sub-rule 2 us condition ko State Government ke under wali autonomous body par Centre aur us State ke reciprocal arrangement se binding banata hai. Aur Explanation body se proper permission define karta hai, dono limb ek saath."),
            ("RULE 19(5) • 20 — MONEY",
             "19(5) caps the later benefit by the difference between combined benefits and what was granted. 20(5) has no cap; the three Explanations settle military service.",
             PINK,
             "Paisa par do fine print clusters. Rule 19 sub-rule 5 baad ki pension ya gratuity ko combined service ki value aur pehle diye gaye benefits ke farq par cap karta hai, commutation table se nikaal kar, aur Rule 20 sub-rule 5 mein jaan boojh kar aisa cap nahi hai. Rule 20 ke teen Explanations military cases settle karte hain, jisme thirty-first December 2003 ke baad join ki gayi service bhi hai, jo National Pension System mein jaati hai."),
            ("RULES 26 • 27 • 28 — PROCESS",
             "EOL counts only if allowed at grant, for civil commotion or higher studies; entry within six months of retirement. 90 days; Rules 35 and 36 saved; refusal only after a hearing.",
             SKY,
             "Procedural fine print. Rule 21: medical certificate ke siwa wali extraordinary leave tabhi ginti hai jab appointing authority grant karte waqt allow kare, civil commotion ya higher scientific aur technical studies ke liye, aur non-counting entry us waqt ya superannuation se chhah mahine pehle tak karni hogi. Rule 26 sub-rule 5 chaar conditions aur ninety din deta hai, sub-rule 6 private company ka bar, sub-rule 8 Rules 35 aur 36 ke liye resignation bachata hai. Rule 27 sub-rule 2 retrospective commutation deta hai. Rule 28 refusal sirf exceptional aur grave circumstances mein, aur sunwai ke baad."),
        ],
        "footer": "CLASSIC UPSC TRAP: the Explanation to Rule 14 and sub-rule 2 of Rule 14 are new to most notes - quote the two limbs of proper permission!",
        "hook": "REMEMBER: the marks live in the provisos, the Explanations and the two limbs of proper permission!",
        "hook_say": "Table three yaad rakhiye: marks fine print mein hain, Rule 11 ke do provisos, Rules 12, 13, 14, 19, 20 aur 21 ke Explanations, aur Rules 26, 27 aur 28 ka procedural fine print.",
    },
    {
        "id": "c02_33_panel_four_numbers",
        "chapter": "CHAPTER 33 • PANEL: THE FOUR NUMBERS THAT DECIDE CHAPTER III",
        "title": "FOUR NUMBERS, THREE SILENCES — THE CHAPTER AT A GLANCE",
        "accent": PINK, "badge": "SUMMARY PANEL",
        "layout": "panel",
        "lab_w": 340,
        "q": "If I forget everything else, which four numbers and which silences still decide the answer?",
        "q_say": "Sir, agar exam ke din baaki sab bhool jaun, to kaunse numbers abhi bhi answer tay karte hain?",
        "intro": "Yeh aakhri panel waise banaya gaya hai jaise revision slide banni chahiye: upar chaar numbers, phir woh habits jo in numbers ko marks mein badalti hain. Har number zor se boliye, phir boliye ki woh kya control karta hai.",
        "headers": [("31.12.2003", "the cut-off date", ORANGE), ("50 PERCENT", "only Rule 15", GREEN), ("36 INSTALMENTS", "Rules 19 and 20", SKY), ("18 AND 5 YEARS", "the Rule 30 checks", PINK)],
        "rows": [
            ("THE DATE",
             "Rules 13, 14, 15, 18, 19 and 20 all hinge on appointment or re-employment by 31.12.2003. The NPS starts on 01.01.2004.",
             ORANGE,
             "Number one, thirty-first December 2003. Chhah rules is par palatte hain: State service, autonomous body service, temporary status, contract service, re-employed civil pensioners aur military service. Date miss hui to poora answer gir jata hai. National Pension System agle din, first January 2004 se shuru hota hai."),
            ("THE HALF",
             "Rule 15 takes only 50 percent of temporary-status service. Every other counting rule takes the whole period.",
             GREEN,
             "Number two, fifty percent. Rule 15 chapter ka akela rule hai jo aadha deta hai. Casual labourer jise 2003 ke end tak temporary status mila aur baad mein regularisation hui, usse us hisse ka aadha milta hai. Baaki har counting rule apni condition poori hone par poora period leta hai."),
            ("THE REFUND",
             "Rules 19 and 20: at most 36 monthly instalments, the first in the month after the option; counting revives only after the last one.",
             SKY,
             "Number three, thirty-six instalments. Rules 19 aur 20 mein refund zyada se zyada thirty-six monthly instalments mein ja sakta hai, pehli option ke agle mahine padti hai, aur ginne ka haq tabhi zinda hota hai jab aakhri rupaya chuk jaye. Asymmetry bhi yaad rakhiye: Rule 19 ka sub-rule 5 baad ka benefit cap karta hai, Rule 20 ka sub-rule 5 nahi."),
            ("THE SILENCES",
             "Rule 21 silence: the leave counts. Rule 23 silence: the suspension does not. Rule 28 silence: the gap is forgiven.",
             YELLOW,
             "Habit one, silences padhiye. Rule 21 mein, agar service book mein entry nahi, to extraordinary leave ginti hai. Rule 23 mein, agar competent authority declare nahi kare, to suspension nahi ginta. Rule 28 mein, agar service book kuch na kahe, to gap apne aap condone ho jata hai. Wahi silence teen ulta results deta hai."),
            ("THE CHECKS",
             "Rule 30: verification at 18 years and at five years before superannuation, in Format 4, and a report by 31 January.",
             BLUE,
             "Number four, athara aur paanch. Rule 30 Head of Office se, Accounts Officer ke saath, athara saal ke baad aur phir superannuation se paanch saal bache hone par service verify karwata hai, aur result Format 4 mein batwata hai. Woh verification final hai jab tak rules badal kar use dobara na kholen, aur saalana report thirty-first January tak Secretary tak pahunchti hai."),
        ],
        "footer": "CLASSIC UPSC TRAP: 31.12.2003 is a cut-off for APPOINTMENT, not for retirement - and the gap never counts, even when the past service is saved!",
        "hook": "REMEMBER: one date, one half, one instalment limit, one pair of checks, three silences!",
        "hook_say": "Panel yaad rakhiye: thirty-first December 2003, Rule 15 ka aadha, Rules 19 aur 20 ke thirty-six instalments, Rule 30 ke do checks, aur teen silences jo teen alag directions mein kheenchti hain.",
    },
    {
        "id": "c02_34_recap",
        "chapter": "CHAPTER 34 • RECAP OF PART 2: RULES 11 TO 30",
        "title": "RECAP — KEY NUMBERS, TOP TRAPS AND CURRENCY NOTE",
        "accent": PINK, "badge": "PART 2 RECAP",
        "q": "In one chapter, what must I remember from Rules 11 to 30?",
        "q_say": "Sir, ek chhote recap mein, Rules 11 se 30 se mujhe kya yaad rakhna chahiye?",
        "boxes": [
            ("KEY NUMBERS",
             "Age 18 • 31.12.2003 • 50 percent (Rule 15) • 36 instalments • 90 days (Rule 26) • 6 months (Rule 21) • 18 years and 5 years (Rule 30) • 31 January.",
             "Key numbers: age 18 (Rule 11); 31.12.2003 (Rules 13, 14, 15, 18, 19, 20); 50 percent of temporary status service (Rule 15); at most 36 monthly instalments (Rules 19, 20), first from the month after the option; 90 days absence (Rule 26(5)); six months before superannuation for a late service-book entry (Rule 21); 18 years and five years before superannuation (Rule 30); 31 January report (Rule 30(5)). Forms: Format 4 (Rule 30). Also: Rule 27(1) has five exceptions (a) to (e); Rule 26 has eight sub-rules.",
             SKY,
             "Key numbers: Rule 11 mein umar athara; chhah rules mein thirty-first December 2003; Rule 15 mein fifty percent; Rules 19 aur 20 mein thirty-six instalments; Rule 26 mein ninety din; Rule 21 mein chhah mahine; Rule 30 mein athara saal aur paanch saal; aur report ke liye thirty-first January. Rule 27 mein paanch exceptions, aur Rule 26 mein aath sub-rules."),
            ("TOP TRAPS",
             "Officiating needs an anchor • Rule 12 is AND • 19(5) limits, 20(5) does not • silence differs in Rules 21, 23, 28 • gap never counts • compulsory retirement not in Rule 24.",
             "Top traps: (1) officiating or temporary service needs a substantive anchor with no break; (2) Rule 12 limbs are AND; (3) Rule 14(3): PSU and nationalised bank service never counts; (4) Rule 15: only half; (5) Rule 19(5) limitation, Rule 20(5) none; (6) Rule 20 Explanation 1(ii) since 07.10.2022: refund required; (7) silence: Rule 21 counts, Rule 23 does not, Rule 28 condoned; (8) a gap never counts under Rules 25(2), 26(7), 28(3); (9) Rule 24 omits compulsory retirement; (10) Rule 26 has 8 sub-rules.",
             RED,
             "Top traps: officiating service ko anchor chahiye; Rule 12 AND hai; PSU service kabhi nahi ginti; Rule 15 sirf aadha deta hai; nineteen five limit karta hai aur twenty five nahi; 2022 ka change refund ko compulsory banata hai; silence ka matlab Rules 21, 23 aur 28 mein alag hai; gap kabhi nahi ginta; aur compulsory retirement Rule 24 mein nahi hai."),
            ("CURRENCY NOTE",
             "Only G.S.R. 770(E) of 2022 changed Chapter III. No later change found up to 21.10.2026, but the Gazette was not read. Wording here is a close restatement.",
             "Currency note: G.S.R. 868(E) of 20.12.2021 original; G.S.R. 770(E) of 07.10.2022 changed Rule 20 Explanation 1(ii) only; G.S.R. 410(E) of 16.07.2024 (effective date about mid-November 2024, unconfirmed) and G.S.R. 340(E) of 22.05.2025 do not amend Rules 11 to 30. No amendment to Rules 11 to 30 was found up to 21.10.2026, from search results only. Sept 2025 O.M. 4/35/2024-P&PW(D)/10377 read from a PDF, day unreadable. All Rule wording is a close restatement from secondary reproductions. Check the Gazette and the latest DoPPW O.M. for exam or live files.",
             ORANGE,
             "Currency note. Chapter 3 mein sirf G.S.R. 770(E) of 2022 ne kuch badla. Twenty-first October 2026 tak koi baad ka change nahi mila, par Gazette khud padhi nahi gayi. Isliye yahan har rule close restatement hai. Exam answer ya live file ke liye Gazette aur latest DoPPW O.M. check kijiye."),
            ("NEXT PART",
             "Part 3 covers Chapter IV on emoluments (Rules 31-32) and Chapter V on the classes of pension (Rules 33-41).",
             "Next: Batch 3, Chapter IV (Emoluments, Rules 31 to 32) and Chapter V (Classes of pension, Rules 33 to 41). Revise first: the Rule 19 and Rule 20 comparison and the Rule 21 silence principle.",
             GREEN,
             "Agle part mein hum Chapter 4 par jayenge, emoluments, yani woh pay jo pension calculation mein jaati hai, Rules 31 aur 32 mein, aur Chapter 5, classes of pension, Rules 33 se 41 mein. Us se pehle Rule 19 aur 20 ka comparison, aur Rule 21 ka silence principle revise kar lijiye."),
        ],
        "hook": "REMEMBER: count, lose, save, prove — and check the Gazette for exact words!",
        "hook_say": "Yaad rakhiye: count, lose, save aur prove, aur exact words ke liye hamesha Gazette check kijiye.",
        "covers": ["CH3-STRUCTURE", "VERIFIED-12SEP2026"],
    },
]

FLOWS = {
    "ch3map": {
        "nodes": [
            (80, 300, 420, 80, "WHAT COUNTS", "Rules 11-23, 29", SKY, 1),
            (570, 300, 430, 80, "WHAT IS LOST", "Rules 24, 26, 27", RED, 2),
            (1070, 300, 360, 80, "WHAT IS SAVED", "Rules 25-28", GREEN, 3),
            (1500, 300, 340, 80, "PROOF", "Rule 30", BLUE, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, RED, 3), (2, 3, GREEN, 4)],
    },
    "countchain": {
        "nodes": [
            (80, 300, 420, 80, "ANCHOR AND START", "Rules 11, 12", SKY, 1),
            (570, 300, 430, 80, "WHICH ROUTE", "Rules 13-23, 29", BLUE, 2),
            (1070, 300, 360, 80, "LOSS EVENT?", "Rules 24, 26, 27", RED, 3),
            (1500, 300, 340, 80, "SAVE AND PROVE", "25-28, 30", GREEN, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, BLUE, 3), (2, 3, RED, 4)],
    },
}

PART_STARTS = ["c02_01_rule11_start", "c02_11_rule19_5_vs_20_5", "c02_21_rule27_interruption"]



assert len({s["id"] for s in SCENES}) == len(SCENES), "duplicate scene id"


FULL = {}
for _sc_ in SCENES:
    if _sc_.get("layout"):
        continue
    _new, _seen = [], set()
    for (_t, _short, _full, _c, _n) in _sc_["boxes"]:
        assert _t not in _seen, f"duplicate card title in {_sc_['id']}: {_t}"
        _seen.add(_t)
        FULL[(_sc_["id"], _t)] = _full
        _new.append((_t, _short, _c, _n))
    _sc_["boxes"] = _new


def write_reference_sheet():
    out = ["# CCS (Pension) Rules 2021 - Batch 2 - Rules 11-30: Qualifying Service - full-wording reference sheet", "",
           "Every row or card on screen is a short key-point; the full ENGLISH wording / examinable facts behind it are listed here.\n"
           "On screen the video stays in English; the narration you hear is Hinglish (Roman script). Use this sheet to write an English answer.\n"
           "Revision chapters appear as the tables and the chart that the video shows.", ""]
    for sc in SCENES:
        out += [f"## {sc['chapter']}", f"**{sc['title']}**  ({sc['badge']})", "", f"Q: {sc['q']}", ""]
        if sc.get("layout"):
            if sc.get("headers"):
                out += ["| " + " | ".join(h[0] for h in sc["headers"]) + " |",
                        "|" + "---|" * len(sc["headers"]),
                        "| " + " | ".join(h[1] for h in sc["headers"]) + " |", ""]
            if sc["layout"] == "chart":
                out += ["| Item | Share counted |", "|---|---|"]
                out += [f"| {r[0]} | {r[1]} percent |" for r in sc["rows"]]
            else:
                out += [f"| {sc.get('col1', 'Rule / clause')} | {sc.get('col2', 'Position')} |", "|---|---|"]
                out += [f"| {r[0]} | {r[1]} |" for r in sc["rows"]]
            out += [""]
        else:
            for (t, _b, _c, _n) in sc["boxes"]:
                out += [f"### {t}", FULL[(sc["id"], t)], ""]
        if sc.get("footer"):
            out += [f"**TRAP:** {sc['footer']}", ""]
        out += [f"> {sc['hook']}", ""]
    Path("pension_b2_reference_sheet.md").write_text("\n".join(out), encoding="utf-8")


# ============================================================================
# FONTS / DRAWING HELPERS
# ============================================================================
_FONT_CACHE = {}


def font(size: int, bold: bool = False):
    key = (size, bold)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    names = (["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "arialbd.ttf", "NotoSans-Bold.ttf", "SegoeUIBold.ttf"]
             if bold else
             ["DejaVuSans.ttf", "LiberationSans-Regular.ttf", "arial.ttf", "NotoSans-Regular.ttf", "segoeui.ttf"])
    f = None
    for n in names:
        try:
            f = ImageFont.truetype(n, size)
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


def text_w(draw, s, f):
    b = draw.textbbox((0, 0), s, font=f)
    return b[2] - b[0]


def wrap_text(draw, text, f, max_w):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split(" "):
            t = f"{cur} {w}".strip()
            if text_w(draw, t, f) <= max_w:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def fit_block(draw, text, bold, max_w, max_h, start, min_size=15, spacing=1.30):
    """Shrinks the font until ALL text fits. Never truncates - raises if it cannot fit at min_size."""
    for size in range(start, min_size - 1, -1):
        f = font(size, bold)
        lines = wrap_text(draw, text, f, max_w)
        lh = int(size * spacing)
        if len(lines) * lh <= max_h:
            return f, lines, lh, size
    raise ValueError(f"CARD TOO DENSE (needs < {min_size}px): {text[:80]!r} - shorten the on-screen text")


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def dim(c, t=0.55):
    return lerp(CARD_BG, c, t)


def background():
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(H):
        d.line([(0, y), (W, y)], fill=lerp(BG_TOP, BG_BOT, y / H))
    for x in range(40, W, 60):
        for y in range(180, 850, 60):
            d.point((x, y), fill=(34, 46, 76))
    return img, d


def draw_skyline(d, x0, y_base, accent):
    col = lerp((20, 30, 56), accent, 0.22)
    blocks = [(0, 38), (22, 62), (50, 46), (74, 80), (100, 54), (128, 70), (156, 40), (182, 58), (208, 34)]
    for dx, h in blocks:
        d.rectangle([x0 + dx, y_base - h, x0 + dx + 20, y_base], fill=col)
    d.polygon([(x0 + 74, y_base - 80), (x0 + 84, y_base - 98), (x0 + 94, y_base - 80)], fill=col)


def draw_node(d, x, y, w, h, title, sub, color, newest):
    dark_text = color in (ORANGE, SKY, YELLOW, GREEN)
    tcol = (10, 16, 36) if dark_text else TEXT_WHITE
    if newest:
        d.rounded_rectangle([x - 5, y - 5, x + w + 5, y + h + 5], radius=16, outline=YELLOW, width=3)
    d.rounded_rectangle([x, y, x + w, y + h], radius=12, fill=color, outline=TEXT_WHITE, width=2)
    f1, l1, _, _ = fit_block(d, title, True, w - 28, 34, 24, NODE_T_MIN, 1.1)
    f2, l2, _, _ = fit_block(d, sub, False, w - 28, 28, 18, NODE_S_MIN, 1.1)
    if len(l1) > 1 or len(l2) > 1:
        raise ValueError(f"Flow node text wraps (would be clipped): {title!r} / {sub!r}")
    d.text((x + 14, y + 8), l1[0], font=f1, fill=tcol)
    d.text((x + 14, y + 8 + 34), l2[0], font=f2, fill=tcol)


def draw_flow(d, flow_key, reveal):
    flow = FLOWS[flow_key]
    nodes, edges = flow["nodes"], flow["edges"]
    for (i, j, col, step) in edges:
        if step <= reveal:
            a, b = nodes[i], nodes[j]
            ax, ay = a[0] + a[2], a[1] + a[3] // 2
            bx, by = b[0], b[1] + b[3] // 2
            d.line([(ax, ay), (bx, by)], fill=col, width=5)
            d.polygon([(bx, by), (bx - 14, by - 9), (bx - 14, by + 9)], fill=col)
    for (x, y, w, h, t, s, c, step) in nodes:
        if step <= reveal:
            draw_node(d, x, y, w, h, t, s, c, newest=(step == reveal))


# ============================================================================
# SCREENSHOT-STYLE BANDS: rows, tables, bar charts, trap strip
# ============================================================================
VIOLET = (139, 105, 255)
LAVENDER = (226, 214, 255)
BODY_TOP, BODY_BOT = 292, 782          # content region of every chapter
STRIP_Y = 800                          # one strip sits here: trap, note or remember


def layout_of(scene):
    if "flow" in scene:
        return "flow"
    return scene.get("layout", "rows")


def items(scene):
    """Reveal units of a scene: table / chart / panel rows, or one row per card."""
    lay = layout_of(scene)
    return scene["rows"] if lay in ("table", "chart", "panel") else scene["boxes"]


def row_parts(u, lay):
    """(label, on-screen text, colour) for any kind of reveal unit."""
    if lay in ("table", "chart", "panel"):
        return u[0], u[1], u[2]
    return u[0], u[1], u[2]   # boxes are (title, short, colour, narration) after the ledger pass


def ink(col):
    """Text colour that stays readable on a given fill."""
    lum = (0.299 * col[0] + 0.587 * col[1] + 0.114 * col[2]) / 255
    return (10, 16, 36) if lum > 0.55 else TEXT_WHITE


def band_row(d, x, y, w, h, col, newest, lab_w, label_lines, f_l, lh_l, text_lines, f_b, lh_b):
    """One screenshot-style row: thin colour bar, colour label, white body text."""
    if newest:
        d.rounded_rectangle([x - 5, y - 5, x + w + 5, y + h + 5], radius=16, outline=YELLOW, width=4)
    d.rounded_rectangle([x, y, x + w, y + h], radius=12, fill=CARD_BG, outline=col, width=3 if newest else 2)
    d.rectangle([x, y + 8, x + 10, y + h - 8], fill=col)
    ty = y + (h - len(label_lines) * lh_l) // 2
    for k, ln in enumerate(label_lines):
        d.text((x + 26, ty + k * lh_l), ln, font=f_l, fill=col)
    bx = x + lab_w
    d.line([(bx - 16, y + 12), (bx - 16, y + h - 12)], fill=lerp(CARD_BG, col, 0.45), width=2)
    ty = y + (h - len(text_lines) * lh_b) // 2
    for k, ln in enumerate(text_lines):
        d.text((bx + 6, ty + k * lh_b), ln, font=f_b, fill=TEXT_WHITE)


def plan_rows(d, rows, lay, top, bottom, lab_w, gap=10, max_body=30, min_body=19, max_label=22):
    """Content-aware row heights. Picks the largest body font that fits, then fills the band."""
    for size in range(max_body, min_body - 1, -1):
        plan, total = [], 0
        for u in rows:
            label, text, _c = row_parts(u, lay)
            f_l = font(max_label, True)
            l_l = wrap_text(d, label, f_l, lab_w - 44)
            lh_l = int(max_label * 1.14)
            f_b = font(size, False)
            l_b = wrap_text(d, text, f_b, W - 160 - lab_w - 36)
            lh_b = int(size * 1.22)
            h = max(len(l_l) * lh_l, len(l_b) * lh_b) + 18
            plan.append([h, l_l, f_l, lh_l, l_b, f_b, lh_b])
            total += h
        total += gap * (len(rows) - 1)
        if total <= bottom - top:
            avail = bottom - top
            gap = min(26, gap + (avail - total) // (len(rows) + 1))
            total += (gap - 10) * (len(rows) - 1)
            spare = (avail - total) // len(rows)
            if spare > 0:
                for p in plan:
                    p[0] += spare
                total += spare * len(rows)
            plan.append(("gap", gap))
            return size, plan
    raise ValueError(f"ROWS DO NOT FIT even at {min_body}px: shorten the row text")


def draw_strip(d, txt, y=STRIP_Y, fill=(58, 45, 12), edge=ORANGE, fg=(255, 214, 92)):
    d.rounded_rectangle([80, y, W - 80, y + 46], radius=12, fill=fill, outline=edge, width=3)
    f, lines, _, _ = fit_block(d, txt, True, W - 200, 30, 22, 16, 1.1)
    if len(lines) != 1:
        raise ValueError(f"STRIP wraps (shorten it): {txt[:70]!r}")
    tw = text_w(d, lines[0], f)
    d.text(((W - tw) // 2, y + (46 - f.size) // 2 - 3), lines[0], font=f, fill=fg)


def draw_band_visual(d, scene, reveal):
    lay = layout_of(scene)
    rows = items(scene)
    top, bottom = (406, BODY_BOT) if lay == "flow" else (BODY_TOP, BODY_BOT)
    if lay == "panel":
        heads = scene["headers"]
        n = len(heads)
        gap = 22
        hw = (W - 160 - gap * (n - 1)) // n
        for i, (ht, hs, hc) in enumerate(heads):
            x = 80 + i * (hw + gap)
            d.rounded_rectangle([x, top, x + hw, top + 84], radius=12, fill=hc, outline=TEXT_WHITE, width=2)
            f1, l1, _, _ = fit_block(d, ht, True, hw - 36, 40, 26, 17, 1.1)
            f2, l2, _, _ = fit_block(d, hs, False, hw - 36, 30, 18, 14, 1.1)
            if len(l1) > 1 or len(l2) > 1:
                raise ValueError(f"Panel header wraps (shorten): {ht!r} / {hs!r}")
            d.text((x + 18, top + 12), l1[0], font=f1, fill=ink(hc))
            d.text((x + 18, top + 48), l2[0], font=f2, fill=ink(hc))
        top += 96
    elif lay == "table":
        d.rounded_rectangle([80, top, W - 80, top + 32], radius=8, fill=(19, 27, 49))
        fcap = font(18, True)
        lw = scene.get("lab_w", 400)
        d.text((106, top + 7), scene.get("col1", "RULE / CLAUSE"), font=fcap, fill=MUTED)
        d.text((106 + lw, top + 7), scene.get("col2", "THE POSITION IN SIMPLE ENGLISH"), font=fcap, fill=MUTED)
        top += 40
    n = len(rows)
    gap = 10
    rh = int((bottom - top - gap * (n - 1)) / n)
    if lay == "chart":
        for i, u in enumerate(rows):
            if i >= reveal:
                break
            label, pct, color = u[0], u[1], u[2]
            y = top + i * (rh + gap)
            newest = (i == reveal - 1)
            if newest:
                d.rounded_rectangle([74, y - 5, W - 74, y + rh + 5], radius=14, outline=YELLOW, width=3)
            f_l, lab, lh_l, _ = fit_block(d, label, True, 620, rh - 8, 24, 14, 1.1)
            if len(lab) > 1:
                raise ValueError(f"Chart label wraps (shorten): {label!r}")
            d.text((94, y + (rh - lh_l) // 2), lab[0], font=f_l, fill=color)
            bx0, bx1 = 740, W - 240
            d.rounded_rectangle([bx0, y + rh // 2 - 16, bx1, y + rh // 2 + 16], radius=8, fill=(18, 26, 46))
            fill_w = max(8, int((bx1 - bx0) * pct / 100))
            d.rounded_rectangle([bx0, y + rh // 2 - 16, bx0 + fill_w, y + rh // 2 + 16], radius=8, fill=color)
            fv = font(22, True)
            d.text((bx1 + 22, y + (rh - 26) // 2), f"{pct} percent", font=fv, fill=TEXT_WHITE)
        return
    lab_w = scene.get("lab_w", 400)
    _, plan = plan_rows(d, rows, lay, top, bottom, lab_w, gap=gap)
    gap = plan.pop()[1]
    y = top
    for i, u in enumerate(rows):
        h, l_l, f_l, lh_l, l_b, f_b, lh_b = plan[i]
        if i < reveal:
            band_row(d, 80, y, W - 160, h, u[2], newest=(i == reveal - 1),
                     lab_w=lab_w, label_lines=l_l, f_l=f_l, lh_l=lh_l, text_lines=l_b, f_b=f_b, lh_b=lh_b)
        y += h + gap


def card_boxes(scene):
    n = len(scene["boxes"])
    gap = 20
    bw_ = (W - 160 - gap * (n - 1)) // n
    return [(80 + i * (bw_ + gap), 490, bw_, 300) for i in range(n)]


def render_frame(scene, qno, total, reveal, kind, out_path: Path):
    img, d = background()
    acc = scene["accent"]
    lay = layout_of(scene)
    n = len(items(scene))
    band = lay != "flow"

    d.rectangle([0, 0, W, 10], fill=acc)
    f_ch = font(21, True)
    ch = scene["chapter"]
    while text_w(d, ch, f_ch) > 1080 and f_ch.size > 14:
        f_ch = font(f_ch.size - 1, True)
    cw = text_w(d, ch, f_ch) + 44
    d.rounded_rectangle([80, 26, 80 + cw, 68], radius=10, fill=(23, 20, 54), outline=VIOLET, width=2)
    d.text((102, 36), ch, font=f_ch, fill=LAVENDER)

    bd = scene["badge"]
    fb = font(20, True)
    bw = text_w(d, bd, fb) + 50
    f_t, l_t, _, _ = fit_block(d, scene["title"], True, W - 160 - bw - 60, 50, 40, 26, 1.1)
    if len(l_t) > 1:
        raise ValueError(f"TITLE wraps (shorten it): {scene['title']!r}")
    d.text((80, 76), l_t[0], font=f_t, fill=TEXT_WHITE)
    d.rounded_rectangle([W - 80 - bw, 45, W - 80, 95], radius=10, fill=acc)
    d.text((W - 80 - bw + 25, 59), bd, font=fb, fill=ink(acc))
    d.line([(80, 150), (W - 80, 150)], fill=(51, 65, 85), width=2)

    asking = kind in ("question",)
    bt, bb = 162, 272
    d.rounded_rectangle([80, bt, W - 80, bb], radius=18, fill=lerp(CARD_BG, acc, 0.20 if asking else 0.10),
                        outline=YELLOW if asking else lerp(CARD_BG, acc, 0.5), width=5 if asking else 2)
    d.ellipse([100, bt + 20, 170, bt + 90], fill=acc)
    qs = f"Q{qno}"
    fq = font(30 if len(qs) < 3 else 24, True)
    d.text((135 - text_w(d, qs, fq) // 2, bt + 36), qs, font=fq, fill=ink(acc))
    f_q, l_q, lh_q, _ = fit_block(d, scene["q"], True, 1180, 92, 38, 22, 1.22)
    ty = bt + (bb - bt - len(l_q) * lh_q) // 2
    for i, ln in enumerate(l_q):
        d.text((200, ty + i * lh_q), ln, font=f_q, fill=TEXT_WHITE)
    draw_skyline(d, 1560, bb - 8, acc)
    chip, chip_col = (("RIYA ASKS (Student)", YELLOW) if kind == "question" else ("THE TEACHER EXPLAINS", GREEN))
    fc = font(17, True)
    cw2 = text_w(d, chip, fc) + 30
    d.rounded_rectangle([W - 100 - cw2, bt + 10, W - 100, bt + 40], radius=14, fill=chip_col)
    d.text((W - 100 - cw2 + 15, bt + 14), chip, font=fc, fill=(10, 16, 36))

    if band:
        draw_band_visual(d, scene, reveal)
        if scene.get("footer") and (reveal or kind == "hook"):
            draw_strip(d, scene["footer"], fill=(58, 45, 12), edge=ORANGE, fg=(255, 214, 92))
        elif kind == "hook":
            draw_strip(d, scene["hook"], fill=YELLOW, edge=YELLOW, fg=(10, 16, 36))
    else:
        draw_flow(d, scene["flow"], reveal)
        draw_band_visual(d, scene, reveal)
        if scene.get("footer") and (reveal or kind == "hook"):
            draw_strip(d, scene["footer"], fill=(58, 45, 12), edge=ORANGE, fg=(255, 214, 92))
        elif kind == "hook":
            draw_strip(d, scene["hook"], fill=YELLOW, edge=YELLOW, fg=(10, 16, 36))

    d.rectangle([0, 855, W, 1070], fill=(7, 11, 24))
    d.line([(80, 855), (W - 80, 855)], fill=(30, 41, 59), width=2)
    d.rectangle([0, 1068, W, H], fill=(20, 28, 50))
    seg_w = W / total
    done = min(1.0, (reveal + (1 if kind == "hook" else 0)) / (n + 1))
    d.rectangle([0, 1068, int(seg_w * (qno - 1) + seg_w * done), H], fill=ORANGE)
    for k in range(1, total):
        d.line([(int(seg_w * k), 1068), (int(seg_w * k), H)], fill=(7, 11, 24), width=2)
    img.save(out_path)


def audit_band(d, sc):
    """Density check for a chapter. Returns the number of problems found."""
    bad = 0
    lay = layout_of(sc)
    rows = items(sc)
    top, bottom = (406, BODY_BOT) if lay == "flow" else (BODY_TOP, BODY_BOT)
    if lay == "panel":
        heads = sc["headers"]
        hw = (W - 160 - 22 * (len(heads) - 1)) // len(heads)
        for (ht, hs, _hc) in heads:
            try:
                _, l1, _, _ = fit_block(d, ht, True, hw - 36, 40, 26, 17, 1.1)
                _, l2, _, _ = fit_block(d, hs, False, hw - 36, 30, 18, 14, 1.1)
                if len(l1) > 1 or len(l2) > 1:
                    raise ValueError("header wraps")
            except ValueError as e:
                bad += 1
                print(f"{sc['id'][:26]:26s} PANEL HEADER FAIL {ht!r}: {e}")
        top += 96
    elif lay == "table":
        top += 40
    n = len(rows)
    lab_w = sc.get("lab_w", 400)
    if lay == "chart":
        rh = int((bottom - top - 10 * (n - 1)) / n)
        print(f"{sc['id'][:26]:26s} [chart] {n} bars, bar band {rh}px")
        for u in rows:
            try:
                _, lab, _, _ = fit_block(d, u[0], True, 620, rh - 8, 24, 14, 1.1)
                if len(lab) > 1:
                    raise ValueError("chart label wraps")
            except ValueError as e:
                bad += 1
                print(f"{sc['id'][:26]:26s} CHART LABEL FAIL {u[0]!r}: {e}")
    else:
        try:
            bs, plan = plan_rows(d, rows, lay, top, bottom, lab_w)
            print(f"{sc['id'][:26]:26s} [{lay}] {n} rows, body {bs}px, "
                  f"heights {[p[0] for p in plan]}")
            if bs < 22:
                print(f"{sc['id'][:26]:26s}   note: rows are dense ({bs}px) - consider shortening")
        except ValueError as e:
            bad += 1
            print(f"{sc['id'][:26]:26s} ROW FAIL: {e}")
    try:
        if sc.get("footer"):
            draw_strip(d, sc["footer"])
    except ValueError as e:
        bad += 1
        print(f"{sc['id'][:26]:26s} TRAP STRIP FAIL: {e}")
    try:
        draw_strip(d, sc["hook"], fill=YELLOW, edge=YELLOW, fg=(10, 16, 36))
    except ValueError as e:
        bad += 1
        print(f"{sc['id'][:26]:26s} HOOK STRIP FAIL: {e}")
    return bad


def audit_density():
    """Prints the font size every row ends up with, plus title/hook fits. Returns the number of failures."""
    img, d = background()
    bad = 0
    for sc in SCENES:
        bw = text_w(d, sc["badge"], font(20, True)) + 50
        try:
            _, l_t, _, ts = fit_block(d, sc["title"], True, W - 160 - bw - 60, 50, 40, 26, 1.1)
            if len(l_t) > 1:
                raise ValueError("title wraps")
        except ValueError as e:
            bad += 1
            print(f"{sc['id'][:26]:26s} TITLE FAIL ({len(sc['title'])} chars): {e}")
        bad += audit_band(d, sc)
    print(f"\n{'ALL CHAPTERS WITHIN BUDGET' if not bad else str(bad) + ' PROBLEM(S) OVER BUDGET'}")
    return bad


def build_segments(scene):
    units = items(scene)
    n = len(units)
    segs = []
    if scene.get("intro"):
        segs.append(("teacher", scene["intro"], 0, "intro"))
    segs.append(("student", scene["q_say"], 0, "question"))
    if scene.get("lead"):
        segs.append(("teacher", scene["lead"], 0, "lead"))
    for i, u in enumerate(units):
        segs.append(("teacher", u[-1], i + 1, "answer"))
    segs.append(("teacher", scene["hook_say"], n, "hook"))
    return segs


def probe_duration(path: Path) -> float:
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        text=True).strip()
    return float(out)


def silent_audio(text: str, out: Path) -> float:
    dur = max(1.5, len(text.split()) / 2.6)
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", f"{dur:.2f}",
                    "-c:a", "libmp3lame", str(out)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
            except Exception as e:
                last = e
                await asyncio.sleep(1.5 * (attempt + 1))
        raise RuntimeError(f"edge-tts failed for segment {out.name}: {last}")


def fmt_ass(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def write_ass(cues, path: Path):
    head = (
        "[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, "
        "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
        "MarginR, MarginV, Encoding\n"
        "Style: Default,DejaVu Sans,38,&H00FFFFFF,&H0000E6FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,160,160,70,1\n"
        "Style: Student,DejaVu Sans,38,&H0042E4F0,&H0000E6FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,160,160,70,1\n\n"
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
            cues.append((offset + buf[0][1], offset + buf[-1][2] + 0.12, style, " ".join(x[0] for x in buf)))
            buf = []
    if buf:
        cues.append((offset + buf[0][1], offset + buf[-1][2] + 0.15, style, " ".join(x[0] for x in buf)))
    return cues


def even_words(text, dur):
    toks = text.split()
    step = dur / max(len(toks), 1)
    return [(t, i * step, (i + 1) * step) for i, t in enumerate(toks)]


# ============================================================================
# MAIN
# ============================================================================
async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true", help="print the density table plus the clause-coverage ledger and exit (no ffmpeg needed)")
    ap.add_argument("--preview", action="store_true", help="render slides only")
    ap.add_argument("--no-tts", action="store_true", help="silent audio (offline layout/timing test)")
    ap.add_argument("--teacher", default=DEFAULT_TEACHER)
    ap.add_argument("--student", default=DEFAULT_STUDENT)
    ap.add_argument("--rate", default="-4%")
    ap.add_argument("--part", type=int, choices=[1, 2, 3], help="1..3 = first, middle, last third of the chapters")
    args = ap.parse_args()

    write_reference_sheet()
    if args.audit:
        bad = audit_density()
        print()
        bad += audit_clauses()
        print()
        bad += audit_language()
        sys.exit(1 if bad else 0)
    if audit_density():
        sys.exit("Build stopped: fix the over-dense cards listed above.")

    for d in (BUILD_DIR, SLIDES_DIR, AUDIO_DIR):
        d.mkdir(parents=True, exist_ok=True)
    global SCENES, OUTPUT_MP4
    if args.part:
        _idx = [next(i for i, x in enumerate(SCENES) if x["id"] == pid) for pid in PART_STARTS] + [len(SCENES)]
        SCENES = SCENES[_idx[args.part - 1]:_idx[args.part]]
        OUTPUT_MP4 = Path(f"{OUT_STEM}_part{args.part}.mp4")
    total = len(SCENES)

    print(f"=== Step 1: rendering slides for {total} Q&A scenes ===")
    jobs = []
    for si, sc in enumerate(SCENES):
        for gi, (who, text, reveal, kind) in enumerate(build_segments(sc)):
            sp = SLIDES_DIR / f"{sc['id']}_{gi:02d}_{kind}.png"
            render_frame(sc, si + 1, total, reveal, kind, sp)
            jobs.append((si, who, text, kind, reveal, sp, AUDIO_DIR / f"{sc['id']}_{gi:02d}.mp3"))
        print(f"  scene {si+1:02d}/{total}  {sc['id']}")
    if args.preview:
        print(f"Preview done: {SLIDES_DIR.resolve()}")
        return

    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        sys.exit("ERROR: ffmpeg/ffprobe not on PATH")

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
        dur = sd + (0.9 if kind in ("question", "hook") else 0.5)
        clip = BUILD_DIR / f"clip_{i:03d}.mp4"
        subprocess.run([
            "ffmpeg", "-y", "-loop", "1", "-framerate", "5", "-i", str(sp), "-i", str(mp3),
            "-af", "apad", "-t", f"{dur:.3f}",
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-g", "60", "-r", "30", "-pix_fmt", "yuv420p",
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
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(raw)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ass = BUILD_DIR / "subtitles.ass"
    write_ass(cues, ass)
    ass_esc = str(ass).replace("\\", "/").replace(":", "\\:")
    subprocess.run([
        "ffmpeg", "-y", "-i", str(raw), "-vf", f"subtitles='{ass_esc}'",
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(OUTPUT_MP4)], check=True,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    dur = probe_duration(OUTPUT_MP4)
    info = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height",
                                    "-of", "csv=p=0", str(OUTPUT_MP4)], text=True).split()
    print("\n=== Step 5: verification ===")
    print("streams:", info)
    print(f"DONE: {OUTPUT_MP4.resolve()}  |  {dur/60:.2f} min  |  {OUTPUT_MP4.stat().st_size/1048576:.1f} MB")
    if not any(s.startswith("audio") for s in info):
        print("WARNING: no audio stream found!")


if __name__ == "__main__":
    asyncio.run(main())
````
