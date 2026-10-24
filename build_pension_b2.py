#!/usr/bin/env python3
"""
CCS (Pension) Rules 2021 - Batch 2 - Rules 11-30: Qualifying Service
SIMPLE ENGLISH Q&A EXPLANATION MASTERCLASS COMPILER - 34 chapters. Scope: Part 2 (Batch 2): CCS (Pension) Rules 2021, Chapter III Qualifying Service,
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


SCENES = [
    {
        "id": "c02_01_rule11_start",
        "chapter": "CHAPTER 1 • RULE 11: WHEN DOES QUALIFYING SERVICE START?",
        "title": "RULE 11 — WHEN THE QUALIFYING-SERVICE CLOCK STARTS",
        "accent": RED, "badge": "RULE 11",
        "q": "From which day does a Government servant's qualifying service start counting?",
        "intro": ("Welcome back! In Part 1 we covered Rules 1 to 10, the basic ground of the CCS Pension Rules 2021. "
                  "Today is Part 2, Chapter 3 of the Rules, Rules 11 to 30. The whole chapter answers one question: which years of service are counted when pension is worked out, and which are not. "
                  "Pension means the regular monthly money paid after retirement. Qualifying service means the years that the Rules agree to count for that pension. Think of it as a stopwatch, and Rule 11 tells us when it starts."),
        "q_say": "Sir, from which day does a Government servant's qualifying service start counting?",
        "boxes": [
            ("THE RULE",
             "The clock starts the day the servant takes charge of the first post. Substantive, officiating or temporary: all fine.",
             "Rule 11 (close restatement, not verbatim Gazette text): qualifying service of a Government servant begins from the date he takes charge of the post to which he is first appointed, whether in a substantive, officiating or temporary capacity. Read via a page-summarising tool from a secondary reproduction of the Rules; the Gazette or India Code text itself was not read.",
             SKY,
             "Let us take the rule first. Qualifying service begins on the day the servant takes charge of the first post. It does not matter whether that first post was substantive, officiating or temporary. Substantive means permanent. Officiating means holding a post for someone else or on trial. Temporary means a post that is not permanent."),
            ("PROVISO 1: NO BREAK",
             "Officiating or temporary start counts only if a substantive appointment follows WITHOUT a break.",
             "First proviso to Rule 11 (close restatement): service in an officiating or temporary capacity counts only if it is followed, without interruption, by substantive appointment in the same service or post or in another service or post. Ledger R11-PROV1.",
             GREEN,
             "Now the first exception. If the first post was only officiating or temporary, that period counts only when a substantive appointment follows without any break. The substantive post can be in the same service or in a different one. If there is a break and no substantive appointment, that first period does not qualify."),
            ("PROVISO 2: UNDER 18",
             "Service before age 18 does not count. Only exception: military service counted under Rule 20.",
             "Second proviso to Rule 11 (close restatement): service rendered before the age of 18 years is not counted, except military service that is counted for civil pension under Rule 20. Ledger R11-PROV2. Reading that counting starts from the 18th birthday and the earlier stretch is simply left out is consistent with the proviso (R11-AGE18-INTERP).",
             ORANGE,
             "Now the second exception. Service before the age of eighteen does not count. The only exception is military service counted for civil pension under Rule 20, which we reach soon. This does not wipe out everything. The counting simply begins when the person turns eighteen."),
            ("REAL EXAMPLES",
             "Bilal: officiating 2010, substantive 2012, no gap: counts from 2010. Charu joined at 17y5m: counts from her 18th birthday.",
             "Example 1 (invented): Bilal, a clerk, is appointed officiating on 01.07.2010 and gets a substantive appointment in the same department on 01.07.2012 with no gap. His qualifying service runs from 01.07.2010, not 2012. Example 2 (invented): Charu, born 10.01.1985, joins on 01.07.2002 at 17 years 5 months. Counting starts on her 18th birthday, 10.01.2003; the earlier 6 months 9 days are left out.",
             ORANGE,
             "Here are two real examples. Bilal was appointed officiating on first July 2010 and made substantive on first July 2012 with no gap. His count starts in 2010. Charu, born tenth January 1985, joined on first July 2002 at seventeen years and five months. Her count starts on her eighteenth birthday, tenth January 2003, and the first six months and nine days are left out."),
            ("THE TRAP",
             "Officiating start is NOT lost, if substantive follows. Do not teach a fixed meaning of interruption: not confirmed.",
             "Trap and flag. Q: if the first appointment was not substantive, is the service lost? A: No, officiating and temporary service count if a substantive appointment follows without interruption. UNVERIFIED (R11-INTERRUPTION-DEF): the source's gloss that 'interruption' means any gap, authorised or unauthorised, was not confirmed against an official source; Rule 27 treats authorised leave as an exception, so do not teach that gloss as a rule.",
             RED,
             "Be careful, this is the trap. A first post that is officiating or temporary is not lost, as long as a substantive appointment follows without a break. One more caution. The source gives a neat meaning of the word interruption, any gap at all, but we could not confirm that wording from an official source, so do not treat it as the rule."),
        ],
        "hook": "REMEMBER: clock starts at first charge-taking; no break before substantive; nothing before 18!",
        "hook_say": "Remember: the clock starts when you take charge of the first post, officiating service needs a substantive post with no break, and nothing before age eighteen counts.",
        "covers": ["R11-MAIN", "R11-PROV1", "R11-PROV2", "R11-EX1", "R11-QA", "R11-AGE18-INTERP", "R11-INTERRUPTION-DEF"],
    },
    {
        "id": "c02_02_chapter_map",
        "chapter": "CHAPTER 2 • CHAPTER III MAP: COUNT, LOSE, SAVE, PROVE",
        "title": "HOW CHAPTER III IS BUILT — FOUR JOBS IN RULES 11 TO 30",
        "accent": SKY, "badge": "RULES 11 TO 30",
        "q": "How is this chapter organised, so that twenty rules do not feel like a heap?",
        "q_say": "Sir, twenty rules is a lot. How is Chapter III organised so I do not get lost?",
        "flow": "ch3map",
        "boxes": [
            ("STEP 1: WHAT COUNTS",
             "Rules 11 to 23 and 29 say which kinds of service count, and on what condition.",
             "Counting rules: Rule 11 (start), 12 (duties and pay regulated by Government), 13 (State), 14 (autonomous body), 15 (temporary status), 16 (probation), 17 (apprentice), 18 (contract), 19 (civil pensioner re-employed), 20 (military), 21 (leave), 22 (training), 23 (suspension), 29 (international organisations). Rules 25, 27 and 28 also decide counting after a gap. Ledger CH3-STRUCTURE (fair summary of Rules 24 to 28 as read).",
             SKY,
             "Step one is what counts. Rules 11 to 23, and Rule 29, say which kinds of service are counted and on what condition. State service, probation, contract service, military service, leave, training and suspension all have their own rule."),
            ("STEP 2: WHAT IS LOST",
             "Rule 24 dismissal or removal, Rule 26 resignation, Rule 27 interruption: past service can be forfeited.",
             "Forfeiture rules: Rule 24 (dismissal or removal), Rule 26 (resignation, general rule in 26(1)), Rule 27(1) (general rule: interruption forfeits past service). Forfeiture means the earlier service is wiped out for pension.",
             RED,
             "Step two is what can be lost. Forfeiture means the earlier service is wiped out for pension. Rule 24 forfeits it on dismissal or removal, Rule 26 on resignation, and Rule 27 on an interruption in service."),
            ("STEP 3: WHAT IS SAVED",
             "Rule 25 reinstatement, Rule 26(2) permitted resignation, Rule 27 exceptions, Rule 28 condonation.",
             "Saving rules: Rule 25 (reinstatement on appeal or review), Rule 26(2) (resignation with proper permission for another Government appointment), Rule 27(1)(a) to (e) and 27(2) (exceptions and commutation of absence), Rule 28 (condonation of interruption). Condonation means the authority forgives the gap.",
             GREEN,
             "Step three is what can be saved. Reinstatement in Rule 25, permitted resignation in Rule 26, the exceptions in Rule 27, and condonation in Rule 28. Condonation simply means the authority forgives the gap so the earlier service survives."),
            ("STEP 4: PROOF",
             "Rule 30 makes the Head of Office check and certify the service in Format 4, at fixed times.",
             "Proof rule: Rule 30 (verification of qualifying service by the Head of Office with the Accounts Officer, communicated in Format 4, after 18 years of service and when five years remain before superannuation). Do NOT memorise a count of 'seventeen routes': the source's count does not add up (range 27 to 30 already includes Rule 28), so it is dropped (CH3-COUNT17).",
             BLUE,
             "Step four is proof. Rule 30 makes the Head of Office check the service and give a certificate in Format 4 at fixed points in a career. One tip: do not memorise any count of routes. The source gave one, but the arithmetic does not add up, so ignore it."),
        ],
        "hook": "REMEMBER: Count (11-23, 29) • Lose (24, 26, 27) • Save (25, 26(2), 27-28) • Prove (30)!",
        "hook_say": "Remember: count, lose, save, prove. Counting is Rules 11 to 23 and 29, losing is Rules 24, 26 and 27, saving is Rules 25 to 28, and proving is Rule 30.",
        "covers": ["CH3-STRUCTURE", "CH3-COUNT17"],
    },
    {
        "id": "c02_03_amendments_currency",
        "chapter": "CHAPTER 3 • WHAT HAS AMENDED CHAPTER III, AND HOW CURRENT IS THIS?",
        "title": "WHICH GAZETTE AMENDMENTS TOUCH RULES 11 TO 30?",
        "accent": ORANGE, "badge": "AMENDMENTS • CURRENCY",
        "q": "Which of the four Gazette notifications actually changed Rules 11 to 30?",
        "q_say": "Sir, the source lists four Gazette notifications. Which of them actually changed Rules 11 to 30?",
        "boxes": [
            ("THE ORIGINAL AND 2022",
             "Original Rules: G.S.R. 868(E), 20.12.2021. Only G.S.R. 770(E) of 07.10.2022 changed Chapter III (Rule 20).",
             "G.S.R. 868(E) dated 20.12.2021 is the original notification of the CCS (Pension) Rules 2021 (GSR-868E). G.S.R. 770(E) dated 07.10.2022 substituted Explanation 1 clause (ii) of Rule 20; the same notification also amended Rules 8, 46(5)(a), 50(9)(h)(iii) and 76, but only Rule 20 lies in Chapter III (GSR-770E-R20, CH3-AMENDED-BY).",
             SKY,
             "The original Rules came in by G.S.R. 868(E) of twentieth December 2021. After that, only one later Gazette notification changed anything inside Chapter III: G.S.R. 770(E) of seventh October 2022, which changed one clause in Rule 20. We study that change in detail soon."),
            ("2024: NOT IN THIS CHAPTER",
             "G.S.R. 410(E) of 16.07.2024 does not amend Rules 11-30. It changed Rule 57 (Form 6-A), which Rule 30(2) points to.",
             "G.S.R. 410(E) dated 16.07.2024 (F.No. 55/13/2023-P&PW(C)) amends Rules 50, 53, 57, 58, 59, 60, 62, 63, 80 and Forms and Formats; it does not amend Rules 11 to 30 (GSR-410E-DATE). Rule 30(2) points to the procedure of Rule 57(1)(a), and Rule 57 was amended by this notification (R30(2)). The source says it took effect on 16.11.2024. UNVERIFIED (GSR-410E-EFFECTIVE): Rule 1(2) says 120 days after Gazette publication; 120 days from 16.07.2024 is 13.11.2024, secondary sites say 16.11.2024, and the Gazette publication date was not read. Say about mid-November 2024 unless confirmed.",
             ORANGE,
             "The 2024 notification, G.S.R. 410(E) of sixteenth July 2024, did not change Rules 11 to 30. It changed Rule 57, which Rule 30 points to. Be careful with its start date. The source says sixteenth November 2024, but counting one hundred twenty days gives thirteenth November, and I could not read the Gazette. So say about mid November 2024."),
            ("2025: RULE 37 ONLY",
             "G.S.R. 340(E) of 22.05.2025 amends only Rule 37 (PSU-absorbed employees). Not Chapter III.",
             "G.S.R. 340(E) dated 22.05.2025 amends Rule 37 only (employees absorbed in public sector undertakings); its Explanation applies Rules 7, 8, 41 and 44(5) analogously. Two pages give the sub-rule number differently (37(29)(c) versus 37(7)), so cite as Rule 37 only (GSR-340E). Rule 37 is for the next batch.",
             GREEN,
             "The 2025 notification, G.S.R. 340(E) of twenty-second May 2025, amends only Rule 37, about employees absorbed in public sector undertakings. That belongs to the next batch. When you cite it, say Rule 37 only, because two pages disagree on the sub-rule number."),
            ("HOW CURRENT IS THIS?",
             "No amendment to Rules 11-30 after Oct 2022 was found up to 21.10.2026. Source's claim of checking on 12.09.2026 is unverified.",
             "Currency note. The source says it was verified on 12 September 2026 and cites O.M.s up to 22.06.2026; this cannot be verified (VERIFIED-12SEP2026), and the 22.06.2026 O.M. is not cited in Batch 2. No amendment to Rules 11 to 30 after G.S.R. 770(E) of 2022 was found in the pages read, up to 21.10.2026; that is a negative result from search-engine results only, because the Gazette and DoPPW site were not read. Rule wording in this batch is a close restatement from secondary reproductions, not Gazette text. A 2026 amendment, G.S.R. 775(E) (about 7 Sept 2026; date unclear; seen on a re-hosted PDF), concerns Rule 37(7) for ex-Ordnance Factory Board employees and belongs to the next batch.",
             RED,
             "Here is the honest currency note. The source says it was checked on twelfth September 2026, but we cannot verify that. We searched up to twenty-first October 2026 and found no amendment to Rules 11 to 30 after 2022, but that search was through search results, not the Gazette itself. So treat all wording in this part as a close restatement and confirm exam answers against the Gazette."),
        ],
        "hook": "REMEMBER: only G.S.R. 770(E) of 2022 changed Chapter III; check the Gazette for exact words!",
        "hook_say": "Remember: only G.S.R. 770(E) of 2022 changed anything in Chapter III, and for exact words always check the Gazette.",
        "covers": ["GSR-868E", "GSR-770E-R20", "GSR-410E-DATE", "GSR-410E-EFFECTIVE", "GSR-340E", "CH3-AMENDED-BY", "VERIFIED-12SEP2026"],
    },
    {
        "id": "c02_04_rule12_duties_pay",
        "chapter": "CHAPTER 4 • RULE 12: DUTIES AND PAY MUST BOTH BE GOVERNMENT-REGULATED",
        "title": "RULE 12 — DUTIES AND PAY, BOTH REGULATED BY GOVERNMENT",
        "accent": GREEN, "badge": "RULE 12",
        "q": "What two things must be true before service qualifies, and what does 'service' mean here?",
        "q_say": "Sir, what must be true before a service qualifies under Rule 12, and what exactly does service mean here?",
        "boxes": [
            ("THE RULE: BOTH LIMBS",
             "Service qualifies only if duties AND pay are both regulated by Government, or by conditions Government fixes.",
             "Rule 12 (close restatement): the service of a Government servant does not qualify unless his duties and his pay are both regulated by the Government, or are under conditions prescribed by the Government. The two limbs are cumulative: AND, not OR.",
             SKY,
             "Let us take the rule first. Service qualifies only if two things are both true: the duties are regulated by Government and the pay is regulated by Government, or both are under conditions the Government fixes. It is AND, not OR. Duties alone are not enough, and pay alone is not enough."),
            ("THE EXPLANATION",
             "Service means service under Government, paid from the Consolidated Fund of India or a Local Fund the Government administers.",
             "Explanation to Rule 12 (close restatement): 'service' means service under Government and paid by Government from the Consolidated Fund of India or from a Local Fund administered by Government. 'Local Fund administered by Government' is defined in Rule 3(1)(r): a body under Government control by force of law or rule, with Government having full and direct control over its spending. Ledger R12-EXPL-SERVICE, R12-LOCALFUND-R3(1)(r).",
             GREEN,
             "Now the Explanation. Service here means service under Government, and paid by Government, either from the Consolidated Fund of India, which is the Government's main account, or from a Local Fund that the Government itself administers. The meaning of a Local Fund is in Rule 3, clause 1, sub-clause r: Government must have full and direct control over how it spends."),
            ("THE EXCLUSION",
             "Service in an establishment with no non-contributory pension scheme is left out, unless Government treats it as qualifying.",
             "Explanation exclusion (close restatement): service in an establishment where a non-contributory pension scheme is not available is not included, unless the Government treats that service as qualifying (R12-EXPL-EXCL). UNVERIFIED gloss (R12-BONUS13-CPF): the source adds that establishments with a CPF-type contributory arrangement fall outside; the rule speaks only of an establishment where a non-contributory pension scheme is not available, and the CPF label is the source's own gloss, not confirmed. Non-contributory means the employee pays nothing towards the pension.",
             ORANGE,
             "Now the exclusion. Service in an establishment that has no non-contributory pension scheme is left out, unless the Government decides to treat it as qualifying. Non-contributory means the employee pays nothing towards the pension. The source calls such places contributory provident fund type establishments, but that label is the source's own gloss, not confirmed."),
            ("REAL EXAMPLE",
             "Dev's office follows Government rules, but his pay came from a society fund with no Government control: that period does not qualify.",
             "Example (invented): Dev works in an office whose duties are regulated by Government rules, but his pay comes from a society fund over which Government has no direct control. Duties limb met, pay limb not met, so that period is not qualifying service (R12-EX1). Q: does pay from a Local Fund count? A: yes, if the fund is administered by Government and both duties and pay are regulated (R12-QA).",
             ORANGE,
             "Here is a real example. Dev works in an office whose duties follow Government rules, but his salary comes from a society fund that Government does not control. One limb is met and one is not, so that period does not qualify. If his salary had come from a Local Fund administered by Government, with duties and pay both regulated, it could count."),
            ("THE TRAP: RULE 2 OR 12?",
             "Rule 2 asks: do the Rules apply to me? Rule 12 asks: does THIS service count? Two different questions.",
             "Look-alike (R2-VS-R12, reasonable reading; Rule 2 is in Batch 1): Rule 2 tells to whom the Rules apply; Rule 12 tells which service is counted as qualifying. One servant can be inside both, but the questions differ. In practice the service book and appointment letter are the evidence for who regulated duties and pay and from which fund.",
             RED,
             "Be careful, this is the trap. Rule 2 asks whether the Rules apply to a person at all. Rule 12 asks whether a particular stretch of service counts. A person can pass the first test and fail the second. In practice the service book and the appointment letter are the evidence."),
        ],
        "hook": "REMEMBER: Rule 12 = duties AND pay regulated by Government; Rule 2 = who, Rule 12 = which service!",
        "hook_say": "Remember: Rule 12 needs duties and pay both regulated by Government. Rule 2 asks who is covered, and Rule 12 asks which service counts.",
        "covers": ["R12-MAIN", "R12-EXPL-SERVICE", "R12-EXPL-EXCL", "R12-LOCALFUND-R3(1)(r)", "R12-EX1", "R12-QA", "R2-VS-R12", "R12-BONUS13-CPF"],
    },
    {
        "id": "c02_05_rule13_state_service",
        "chapter": "CHAPTER 5 • RULE 13: SERVICE UNDER A STATE GOVERNMENT",
        "title": "RULE 13 — STATE SERVICE BEFORE JOINING THE CENTRE",
        "accent": BLUE, "badge": "RULE 13",
        "q": "Can service under a State Government be counted, and who pays for it?",
        "q_say": "Sir, if someone worked under a State Government first, can that service be counted, and who pays?",
        "boxes": [
            ("ROUTE ONE: 13(1)",
             "State servant first appointed on or before 31.12.2003 and permanently transferred to a post under these Rules: State service counts.",
             "Rule 13(1) (close restatement): a Government servant whose initial appointment in a State Government pensionable establishment was on or before 31.12.2003, and who is permanently transferred to a service or post to which these Rules apply, has his continuous service under the State Government counted as qualifying. Proviso: officiating or temporary State service counts only if followed without interruption by substantive appointment in the State or the Central Government. 31.12.2003 is the old-pension cut-off: the New Pension System began on 01.01.2004 (TL-31.12.2003).",
             SKY,
             "Let us take route one. A State servant first appointed in a State pensionable establishment on or before thirty-first December 2003, who is then permanently transferred to a Central post covered by these Rules, gets the continuous State service counted. That date matters because the New Pension System began on first January 2004. The proviso: officiating or temporary service needs a substantive appointment after it with no break, in the State or the Centre."),
            ("ROUTE TWO: 13(2)",
             "Resigned the State job with PROPER permission and joined a Central post: State service counts, same no-break condition.",
             "Rule 13(2) (close restatement): where a person is appointed to a post under these Rules after his resignation from State service was accepted with proper permission, his continuous State service qualifies, subject to the same condition of uninterrupted substantive appointment (R13(2)). Explanation (R13-EXPL): proper permission means (i) he applied for the Central post with the State Government's previous permission, AND (ii) the State's order accepting the resignation says that he resigns to join the Central post with proper permission.",
             GREEN,
             "Now route two. If the person resigned from the State job and then joined the Central post, the State service still counts, but only if the resignation had proper permission. The Explanation gives two tests. First, he applied for the Central post after taking the State Government's previous permission. Second, the State's order says he is resigning to join the Central post with proper permission."),
            ("WHO PAYS: 13(3)",
             "The Central Government bears pension and gratuity. No share is recovered from the State.",
             "Rule 13(3) (close restatement): the liability for pension and gratuity is borne entirely by the Central Government; no proportionate pension is recovered from the State Government (R13(3)). Gratuity is a one-time lump sum paid on retirement or death. Contrast Rule 14, where the autonomous body pays a lump sum.",
             ORANGE,
             "Now the money. Under Rule 13(3), the Central Government bears the full pension and gratuity. Gratuity is a one-time lump sum paid on retirement or death. The Centre does not recover any share from the State. Remember this, because Rule 14 works differently."),
            ("EXAMPLE AND THE LINK",
             "Asha: State Assistant Engineer from 1999, moved to the Centre in 2007: all State service counts, Centre pays. Without permission papers, Rule 26(1) forfeits it.",
             "Example (invented): Asha joined a State pensionable establishment as Assistant Engineer in 1999 and was permanently transferred to a Central post in 2007. Her whole State service counts and the Centre bears the cost (R13-EX1). Link (R13-R26-LINK): Rule 13(2) rests on the Rule 26(2) exception to forfeiture on resignation; without the permission papers the case falls under Rule 26(1) and the State service can be forfeited. Q: does the Centre recover proportionate pension from the State? A: no, Rule 13(3).",
             RED,
             "Here is a real example. Asha joined a State pensionable post as an Assistant Engineer in 1999 and was permanently transferred to a Central post in 2007. Her whole State service counts, and the Centre carries the cost. Be careful, this is the trap: Rule 13(2) depends on the Rule 26 exception for permitted resignation. Without the permission papers, the State service can be forfeited."),
        ],
        "hook": "REMEMBER: on or before 31.12.2003 • permanent transfer, or resignation WITH permission • Centre pays all!",
        "hook_say": "Remember: first appointment on or before thirty-first December 2003, permanent transfer or resignation with proper permission, and the Centre pays everything.",
        "covers": ["R13(1)", "TL-31.12.2003", "R13(1)-PROV", "R13(2)", "R13-EXPL", "R13(3)", "R13-EX1", "R13-R26-LINK"],
    },
    {
        "id": "c02_06_rule14_autonomous_body",
        "chapter": "CHAPTER 6 • RULE 14: SERVICE IN AN AUTONOMOUS BODY (AND WHY A PSU IS DIFFERENT)",
        "title": "RULE 14 — AUTONOMOUS BODY SERVICE AND THE LUMP SUM",
        "accent": ORANGE, "badge": "RULE 14",
        "q": "When does service in an autonomous body count, and what must the body pay?",
        "q_say": "Sir, when does service in an autonomous body count, and what does the body have to pay?",
        "boxes": [
            ("THE RULE: 14(1)",
             "First appointed on or before 31.12.2003 in an autonomous body with a similar non-contributory pension scheme; joined a Central post with proper permission.",
             "Rule 14(1) (close restatement): where a person's initial appointment was on or before 31.12.2003 in an autonomous body, under the Central or a State Government, that has a non-contributory pension scheme similar to these Rules, and after his resignation was accepted with proper permission he is appointed to a service or post to which these Rules apply, his service in the body (officiating, temporary or substantive) qualifies, subject to clauses (a) to (d). An autonomous body is an organisation set up by Government but run with its own management.",
             SKY,
             "Let us take the rule first. An autonomous body is an organisation set up by Government but run with its own management. If a person was first appointed in such a body on or before thirty-first December 2003, in a body with a similar non-contributory pension scheme, and later joined a Central post with proper permission after resigning, the body service can count. Four conditions, clauses a to d, must all be met."),
            ("THE FOUR CONDITIONS",
             "(a) no break before substantive post; (b) no separate pension from the body; (c) body pays a lump sum; (d) lump sum worked out by the 1981 commutation table.",
             "Rule 14(1)(a): after officiating or temporary appointment in the Central Government, substantive appointment without interruption. (b): the Government servant is not drawing a separate pension from the body for that service. (c): the body pays a lump sum covering pension or service gratuity, plus retirement gratuity. (d): the lump sum is worked out with the commutation table of the CCS (Commutation of Pension) Rules, 1981. Commutation means converting part of a pension into a one-time sum.",
             GREEN,
             "Now the four conditions. A: after any officiating or temporary Central appointment, a substantive appointment must follow without a break. B: the servant must not draw a separate pension from the body for that service. C: the body pays a lump sum that covers pension or service gratuity and also retirement gratuity. D: that lump sum is worked out with the commutation table of the 1981 Commutation of Pension Rules."),
            ("THE EXPLANATION: PERMISSION",
             "Proper permission is presumed only if he applied with the body's prior permission AND its order says he resigns to join the Centre.",
             "Explanation to Rule 14 (close restatement, read in full on 24.10.2026; ledger R14-EXPL): a Government servant is deemed to have been appointed in the Government with proper permission if (i) he had applied for the service or post in the Government with the previous permission of the autonomous body, AND (ii) the order of the autonomous body clearly indicates that the employee is resigning to join the post in the Government with proper permission of that body. Both limbs are needed; an after-the-fact letter of no objection does not satisfy the Explanation.",
             GREEN,
             "There is an Explanation to Rule 14, and it is the part most notes miss. Proper permission is not proved by a friendly letter afterwards. It is deemed only when two things are true. First, he applied for the Central post after taking the body's previous permission. Second, the body's own order says clearly that he is resigning to join the Central post with proper permission. Both limbs, or the service in the body is not counted."),
            ("14(2): RECIPROCAL ARRANGEMENT",
             "For a State-level body, the lump-sum condition binds it only through the Centre-State reciprocal arrangement. Centre pays under 13(3); the body pays under 14.",
             "Rule 14(2) (close restatement, read in full on 24.10.2026; ledger R14(2), RECIPROCAL): the condition for discharge of pension liability by an autonomous body under a State Government, having a non-contributory pension scheme similar to these rules, shall be binding on that autonomous body in accordance with the reciprocal arrangement entered into by the Central Government with the concerned State Government. Design note (R14-LOGIC): the body settles its own liability by a lump sum, so the Centre does not pay twice; under Rule 13(3) the Centre bears the cost instead.",
             PINK,
             "Now sub-rule two, the sentence that this build used to flag as unverified. For an autonomous body under a State Government, the duty to pay a lump sum does not fall from the sky. It becomes binding on that body through a reciprocal arrangement between the Central Government and that State. This is the mirror image of Rule 13. There the Centre pays the whole cost. Here the body pays its own share by a lump sum."),
            ("THE TRAP: 14(3) PSU",
             "PSU service before the Central appointment does NOT count. Same dates: Central body counts, nationalised bank does not.",
             "Rule 14(3) (close restatement): service in a Public Sector Undertaking, including a nationalised bank or a financial institution, before appointment to the Central Government is not qualifying service (R14(3)). Example (invented, R14-EX1): Esha joined a Central autonomous body in 2001, which had a similar non-contributory scheme, and moved to a Central post with proper permission in 2009; the body paid the lump sum, so her body service counts. With the same dates in a nationalised bank, it would not count. Q: can PSU service be counted? A: no.",
             RED,
             "Be careful, this is the trap. Service in a public sector undertaking, including a nationalised bank or financial institution, is not qualifying service. Take Esha, who joined a Central autonomous body in 2001 and a Central post in 2009 with the lump sum paid: her service counts. With exactly the same dates in a nationalised bank, it would not count at all."),
        ],
        "hook": "REMEMBER: body counts on proper permission plus a lump sum; State body binds by reciprocal arrangement; PSU never!",
        "hook_say": "Remember: an autonomous body's service counts if the body pays the lump sum, but PSU, nationalised bank and financial institution service never counts.",
        "covers": ["R14(1)", "R14(1)(a)", "R14(1)(b)", "R14(1)(c)", "R14(1)(d)", "R14(2)", "R14(3)", "R14-EX1", "R14-LOGIC"],
    },
    {
        "id": "c02_07_rules15_17_status_probation_apprentice",
        "chapter": "CHAPTER 7 • RULES 15 TO 17: TEMPORARY STATUS, PROBATION, APPRENTICE",
        "title": "RULES 15-17 — HALF, FULL OR NOTHING?",
        "accent": GREEN, "badge": "RULES 15 • 16 • 17",
        "q": "How much of temporary-status, probation and apprentice service is counted?",
        "q_say": "Sir, how much of temporary-status service, probation and apprentice service is counted?",
        "boxes": [
            ("RULE 15: HALF",
             "Temporary status granted on or before 31.12.2003, then regularised: only 50 percent of that service counts.",
             "Rule 15 (close restatement, source of the flag cleared on 24.10.2026): a Government servant who was conferred temporary status on or before 31.12.2003 under the Casual Labourers (Grant of Temporary Status and Regularisation) Scheme of Government of India, 1993, notified by the Ministry of Personnel, Public Grievances and Pensions (Department of Personnel and Training), and who was subsequently regularised in Government service, has fifty percent of the service rendered in temporary status counted as qualifying service (R15, LIMIT-R15-50PCT, R15-DOPT). The notifying authority is now read in the rule text; the exact O.M. number and date of 1993 are still not read, and the 10.09.1993 date remains unconfirmed.",
             SKY,
             "Rule 15 first. A casual labourer who was given temporary status on or before thirty-first December 2003 under the 1993 Casual Labourers Scheme, notified by the Department of Personnel and Training, and who was later regularised, gets only fifty percent of the temporary-status service counted. Not all of it, just half. The rule itself names that notifying department, though the original 1993 order number and date are still not read."),
            ("RULE 16: PROBATION",
             "Probation service counts if confirmation follows, in the same post or another post.",
             "Rule 16 (close restatement): service rendered on probation against a post counts as qualifying service if the person is subsequently confirmed in the same or another post (R16). Two things are needed: probation against a post, and later confirmation. Probation is a trial period before a job is made permanent; confirmation is the order making it permanent.",
             GREEN,
             "Rule 16 is about probation, a trial period before the job is made permanent. Probation service counts if the person is later confirmed, which means made permanent, in that post or in a different one. Two things are needed: probation against a post, and then confirmation."),
            ("RULE 17: APPRENTICE",
             "Apprentice service does not count. One exception: Subordinate Accounts Service apprentice in IA&AD or Defence Accounts.",
             "Rule 17 (close restatement): apprentice service is not qualifying service, except the service of an apprentice in the Subordinate Accounts Service in the Indian Audit and Accounts Department or the Defence Accounts Department (R17). An apprentice is a person learning a trade or work under a training arrangement.",
             ORANGE,
             "Rule 17 is about apprentices, people learning a trade under a training arrangement. The general rule is that apprentice service does not count. There is one narrow exception: an apprentice in the Subordinate Accounts Service, and only in the Indian Audit and Accounts Department or the Defence Accounts Department."),
            ("REAL EXAMPLE",
             "Gopal got temporary status 01.04.2002, regularised 01.04.2006: 4 years, so 2 years count.",
             "Example (invented, R15-EX1): Gopal, a casual labourer, was granted temporary status on 01.04.2002 and regularised on 01.04.2006. The temporary-status stretch is 4 years; 50 percent is 2 years, which count as qualifying service. A temporary-status date of 31.12.2003 or earlier is needed for Rule 15. Q: does apprentice service count? A: generally not; only the Subordinate Accounts Service apprentice in IA&AD or Defence Accounts.",
             ORANGE,
             "Here is a real example. Gopal was given temporary status on first April 2002 and regularised on first April 2006. That is four years of temporary-status service. Half of four is two years, so two years count, not four."),
            ("THE PATTERN AND TRAP",
             "Benefit comes only when the sequence completes. Trap: do not claim full service under Rule 15.",
             "Pattern (R15-17-PATTERN, a teaching device, not a rule): probation counts only after confirmation; temporary status counts (at half) only after regularisation; apprentice service does not count except the one narrow stream. Keep three dates in the service book: 31.12.2003, the temporary-status date and the regularisation date. Trap: asking for full credit under Rule 15; always check the type of service and the percentage.",
             RED,
             "Be careful, this is the trap. A handy pattern is that a benefit comes only when the sequence is complete: probation then confirmation, temporary status then regularisation. The common mistake is asking for the full period under Rule 15. Always check two things: the type of service and the percentage."),
        ],
        "hook": "REMEMBER: temporary status = 50 percent • probation needs confirmation • apprentice = no, except IA&AD or Defence Accounts!",
        "hook_say": "Remember: temporary status counts at fifty percent, probation needs confirmation, and apprentice service does not count except in the Indian Audit and Accounts or Defence Accounts departments.",
        "covers": ["R15", "LIMIT-R15-50PCT", "R15-EX1", "R15-DOPT", "R16", "R17", "R15-17-PATTERN"],
    },
    {
        "id": "c02_08_rule18_contract",
        "chapter": "CHAPTER 8 • RULE 18: SERVICE ON CONTRACT BEFORE REGULAR APPOINTMENT",
        "title": "RULE 18 — CONTRACT SERVICE NEEDS TWO LIMBS, BOTH OF THEM",
        "accent": BLUE, "badge": "RULE 18",
        "q": "When does earlier contract service count, and what must the person give back?",
        "q_say": "Sir, when does contract service before a regular appointment count, and what must the person give back?",
        "boxes": [
            ("LIMB ONE: A CLEAN SWITCH",
             "Engaged on contract for a fixed period, then on or before 31.12.2003 appointed to a covered post, with no break in duty.",
             "Rule 18(i) (close restatement): the person was first engaged by the Government on contract for a specified period; and then, on or before 31.12.2003, was appointed to the same or another post, in a temporary, officiating or substantive capacity, in an establishment to which these Rules apply, with no interruption in duty (R18(i)).",
             SKY,
             "Let us take limb one. The person was first hired by Government on contract for a fixed period, and then, on or before thirty-first December 2003, was appointed to the same or another post in an establishment covered by these Rules, with no break in duty. It must be a clean switch from contract to regular service."),
            ("LIMB TWO: GIVE BACK THE CPF",
             "Refund the Government's CPF contribution with interest, and any other compensation for that service, as per the 1972 Rules option.",
             "Rule 18(ii) (close restatement): he has refunded to the Government, as per the option exercised under the CCS (Pension) Rules, 1972, the Government's contribution to the Contributory Provident Fund with interest, and any other compensation received for that service (R18(ii)). The two limbs are cumulative: both must be met. A Contributory Provident Fund is a savings fund to which both employee and employer pay.",
             GREEN,
             "Now limb two. The person must also refund to the Government, as per the option under the 1972 Rules, the Government's share of the Contributory Provident Fund, which is a savings fund both sides pay into, with interest, and any other compensation received for that service. Both limbs are needed. One alone is not enough."),
            ("REAL EXAMPLE",
             "Farid: 2-year contract from 1998, regular post in 2000, no gap, CPF share refunded: counts.",
             "Example (invented, R18-EX1): Farid, an engineer, was engaged on a two-year contract in 1998, was appointed to a regular post in the same department in 2000 with no gap, and refunded the Government's CPF contribution with interest as per his 1972 option. His contract period counts. Q: if the CPF contribution is not refunded? A: the service does not qualify, because limb two is cumulative.",
             ORANGE,
             "Here is a real example. Farid, an engineer, was on a two-year contract from 1998, was made regular in the same department in 2000 with no gap, and refunded the Government's provident fund share with interest. His contract period counts. Had he not refunded it, it would not count."),
            ("THE TRAP",
             "Trap: one limb is not enough. Both: no break AND refund.",
             "Trap (R18): limb (i) and limb (ii) are cumulative. A clean transition without a refund fails; a refund without a clean transition also fails. The appointment must also be on or before 31.12.2003, the same cut-off line as in Rules 13, 14, 15, 19 and 20.",
             RED,
             "Be careful, this is the trap. Candidates remember the clean switch and forget the refund, or the other way round. Both limbs must be met, and the regular appointment must be on or before thirty-first December 2003."),
        ],
        "hook": "REMEMBER: Rule 18 = contract, then regular by 31.12.2003 with no break, AND refund the CPF share!",
        "hook_say": "Remember: Rule 18 needs a clean move from contract to regular service by thirty-first December 2003, and also a refund of the Government provident fund share.",
        "covers": ["R18(i)", "R18(ii)", "R18-EX1"],
    },
    {
        "id": "c02_09_no_break_family",
        "chapter": "CHAPTER 9 • THE SAME CONDITION IN FOUR RULES: NO BREAK BEFORE SUBSTANTIVE",
        "title": "THE 'NO INTERRUPTION, THEN SUBSTANTIVE' FAMILY — RULES 11, 13, 14, 18",
        "accent": PINK, "badge": "RULES 11 • 13 • 14 • 18",
        "q": "Which rules share the 'no break, then a substantive post' condition?",
        "q_say": "Sir, I keep hearing no break, then a substantive post. Which rules share that condition?",
        "boxes": [
            ("RULES 11 AND 13",
             "Rule 11: substantive post in the same or another service. Rule 13: substantive in the State or the Centre.",
             "Rule 11 first proviso: officiating or temporary service counts if followed without interruption by substantive appointment in the same service or post or another. Rule 13(1) proviso and 13(2): officiating or temporary State service counts if followed without interruption by substantive appointment in the State or Central Government. Ledger FAMILY-INTERRUPT-SUBST.",
             SKY,
             "Let us trace the family. In Rule 11, officiating or temporary service counts if a substantive appointment follows without a break, in the same service or another. In Rule 13, State officiating or temporary service counts if a substantive appointment follows without a break, in the State or in the Centre."),
            ("RULES 14 AND 18",
             "Rule 14(1)(a): Central appointment then substantive with no break. Rule 18: 'no interruption in duty'.",
             "Rule 14(1)(a): after officiating or temporary appointment in the Central Government, substantive appointment without interruption. Rule 18: carries the idea in different words, as 'no interruption in duty' between the contract and the regular appointment (the source treats all four alike; Rule 18 uses different wording, so quote it in its own words).",
             GREEN,
             "In Rule 14, clause a, the Central officiating or temporary appointment must be followed by a substantive one without a break. Rule 18 carries the same idea in different words: no interruption in duty. So four rules, one idea, though Rule 18 is worded differently."),
            ("THE BRIDGES",
             "Gaps can be bridged: Rule 22(3) joining time, Rule 26(4) joining time plus leave due, then formal condonation.",
             "Bridging tools: Rule 22(3) (interruption between training and appointment at different stations counts up to the permissible joining time); Rule 26(4) (gap within joining time covered by leave due on the date of relief, the rest by formal condonation). Rule 28 deals with condonation of interruption between civil spells.",
             ORANGE,
             "Gaps can sometimes be bridged. Rule 22, sub-rule 3, counts a gap up to the joining time when training and appointment are at different stations. Rule 26, sub-rule 4, covers a gap within joining time by leave due, and the rest needs formal condonation. If a gap is bridged, the earlier service stays safe."),
            ("THE TRAP",
             "Trap: no anchor, no credit. Officiating or temporary service has no value until a substantive post follows without a gap.",
             "Principle: service held in an officiating, temporary, State, body or contract capacity does not qualify until the substantive (or regular) appointment anchors it without a gap, unless the gap is bridged or condoned. Exam use: when asked 'does this earlier service count', first look for the anchor.",
             RED,
             "Be careful, this is the trap. Earlier officiating, temporary, State or contract service is like a boat that needs an anchor: the substantive appointment. If there is a gap and nothing bridges or condones it, the earlier service is not counted."),
        ],
        "hook": "REMEMBER: officiating or temporary service needs a substantive anchor with no gap!",
        "hook_say": "Remember: officiating or temporary service needs a substantive appointment as its anchor, with no gap, unless the gap is bridged or condoned.",
        "covers": ["FAMILY-INTERRUPT-SUBST"],
    },
    {
        "id": "c02_10_rule19_reemployed_civil_pensioner",
        "chapter": "CHAPTER 10 • RULE 19: A RE-EMPLOYED CIVIL PENSIONER'S EARLIER SERVICE",
        "title": "RULE 19 — OLD SERVICE COUNTS ONLY AFTER A FULL REFUND",
        "accent": ORANGE, "badge": "RULE 19(1)-(4)",
        "q": "Who can count earlier service after re-employment, and what must be refunded?",
        "q_say": "Sir, who can count earlier service after being re-employed, and what has to be refunded?",
        "boxes": [
            ("THE ENTRY GATE: 19(1)",
             "Retired on compensation or invalid pension or gratuity, re-employed on or before 31.12.2003, stopped the pension and refunded: old service counts.",
             "Rule 19(1) (close restatement): a Government servant who retired on compensation pension, invalid pension, compensation gratuity or invalid gratuity, and was re-employed on or before 31.12.2003 in a service or post to which these Rules apply, and who in accordance with his option under the CCS (Pension) Rules, 1972 discontinued the pension on re-employment and refunded (or agreed to refund) the pension drawn, the commuted value of part of pension, and the retirement gratuity including service gratuity, may count his earlier service (R19(1)). Entry gate (R19-ENTRY-GATE): the text names only these four; superannuation and retiring pension cases are outside by implication, with no express words.",
             SKY,
             "Let us take the entry gate. Rule 19 is only for people who retired on compensation pension, invalid pension, compensation gratuity or invalid gratuity. Invalid pension is paid to someone retired for ill health. If such a person was re-employed on or before thirty-first December 2003 and stopped the pension and refunded, the old service counts. People who retired on superannuation or retiring pension are not named, so they fall outside by implication."),
            ("WHAT IS REFUNDED: 19(2)",
             "(i) pension drawn before: no refund. (ii) pension element ignored at pay fixation: refund. (iii) other items set off, balance refunded.",
             "Rule 19(2) (close restatement): (i) pension drawn before re-employment need not be refunded (R19(2)(i)). (ii) The PENSION element that was ignored or not taken into account at pay fixation was to be refunded (R19(2)(ii)). The source called it a 'gratuity element'; that is wrong, so do not use that wording. (iii) The pension equivalent of gratuity and of commuted pension that was taken into account at pay fixation is set off against the retirement gratuity and commuted value, and the balance is refunded (R19(2)(iii)); the source omitted this clause.",
             GREEN,
             "Now what is refunded. Clause one: the pension already drawn before re-employment need not be refunded. Clause two: the pension element that was ignored when the pay was fixed on re-employment has to be refunded. The source called it a gratuity element, but the rule text speaks of the pension element. Clause three: what was taken into account at pay fixation is set off against the retirement gratuity and commuted value, and the balance is refunded."),
            ("HOW AND WHEN: 19(3), 19(4)",
             "Up to 36 monthly instalments, first from the month AFTER the option month. Old service counts only after the full refund. Death: the balance is cut from death gratuity.",
             "Rule 19(3) (close restatement): refund in monthly instalments, maximum 36 (LIMIT-36-INSTALMENTS), the first instalment from the month after the month in which the option was exercised (R19-INSTALMENT-START); the right to count the earlier service revives only after the full refund. Rule 19(4): if he dies before the full refund, the unrefunded part is adjusted against the death gratuity payable to the family (R19(4)). Death gratuity is the lump sum paid to the family if a servant dies.",
             ORANGE,
             "Now how and when. The refund goes in monthly instalments, at most thirty-six, and the first instalment starts in the month after the month of the option. The right to count the old service comes alive only after the full refund. If the person dies before the refund is finished, the unrefunded part is adjusted against the death gratuity, the lump sum paid to the family."),
            ("REAL EXAMPLE",
             "Gita: option June 1999, refund Rs 72,000 in 36 instalments of Rs 2,000, July 1999 to June 2002. After that, her old service counts.",
             "Example (invented, R19-EX1): Gita, an invalid-pension clerk, was re-employed in 1999 and exercised her option in June 1999. She refunds Rs 72,000 in 36 equal instalments of Rs 2,000 (36 x 2,000 = 72,000); the first is July 1999 (month after the option month) and the last is June 2002. Only then does her old service count. If she died after 20 instalments (Rs 40,000 paid), Rs 32,000 would remain, to be adjusted against the death gratuity. Q: superannuation pension then re-employed, does old service count? A: no, outside the entry gate.",
             ORANGE,
             "Here is a real example with numbers. Gita, a clerk on invalid pension, was re-employed in 1999 and exercised her option in June 1999. She owes seventy-two thousand rupees, so she pays thirty-six instalments of two thousand rupees, from July 1999 to June 2002. Only after the last instalment does her old service count. If she had died after twenty instalments, forty thousand rupees would be paid and thirty-two thousand would be cut from the death gratuity."),
            ("THE TRAP",
             "Trap: the instalments start the NEXT month, and counting revives only after the LAST instalment.",
             "Traps: (1) first instalment is the month after the option month, not the option month itself; (2) the right to count is not revived by merely agreeing to refund; it needs the full refund (R19(3)); (3) do not call the clause (ii) item a gratuity element; (4) superannuation or retiring pension is not in the gate. Changed items: R19(2)(ii), R19(2)(iii).",
             RED,
             "Be careful, this is the trap. The first instalment is in the month after the option, not in the option month. Agreeing to refund is not enough, because counting revives only after the final instalment. And remember, only compensation or invalid pension and gratuity can enter this gate."),
        ],
        "hook": "REMEMBER: 36 instalments • start the month AFTER the option • count only after the full refund!",
        "hook_say": "Remember: at most thirty-six instalments, starting the month after the option, and the old service counts only after the full refund.",
        "covers": ["R19(1)", "R19-ENTRY-GATE", "R19(2)(i)", "R19(2)(ii)", "R19(2)(iii)", "R19(3)", "LIMIT-36-INSTALMENTS", "R19-INSTALMENT-START", "R19(4)", "R19-EX1"],
    },
    {
        "id": "c02_11_rule19_5_vs_20_5",
        "chapter": "CHAPTER 11 • RULE 19(5) AGAINST RULE 20(5): LATER PENSION AND OLD BENEFITS",
        "title": "RULE 19(5) v RULE 20(5) — SET-OFF FOR CIVIL, NONE FOR MILITARY",
        "accent": PINK, "badge": "RULE 19(5) • 20(5)",
        "q": "What happens to the later pension when old benefits were kept: civil versus military?",
        "q_say": "Sir, when a re-employed person kept the old benefits, how does the later pension work for civil and for military cases?",
        "boxes": [
            ("RULE 19(5): A CAP",
             "Civil case: if old pension or gratuity was kept and old service not counted, the later benefit is capped by the difference.",
             "Rule 19(5) (close restatement, filled in after the source gave only a conclusion; R19(5)): where the Government servant kept the earlier pension or gratuity and the old service is not counted, the service gratuity, or the capital value of pension plus retirement gratuity, payable for the later service cannot exceed the difference between what the combined service would have given and what was already granted. The capital value is worked out with the commutation table at final retirement, and an Explanation deals with capital value. Capital value means the one-time worth of a pension.",
             SKY,
             "Let us take Rule 19, sub-rule 5. If a re-employed civil pensioner kept the earlier pension or gratuity, and the old service is not counted, then the later benefit is capped. It cannot be more than the difference between what the combined service would give and what was already granted. Capital value means the one-time worth of a pension, worked out by the commutation table at final retirement."),
            ("RULE 20(5): NO CAP",
             "Military case: later civil pension and gratuity are NOT limited by the military pension or gratuity drawn.",
             "Rule 20(5) (close restatement): the pension and gratuity admissible for the later civil service are not subject to any limitation by reference to the military pension and gratuity drawn (R20(5)). It is the opposite of Rule 19(5). Rule 20(3), which the source did not quote, is now confirmed: if he dies before full refund, the unrefunded part is adjusted against the death gratuity (R20(3)).",
             GREEN,
             "Now Rule 20, sub-rule 5, the opposite. For a military case, the pension and gratuity for the later civil service are not limited by the military pension and gratuity already drawn. So civil to civil has a set-off cap, and military to civil has none."),
            ("REAL EXAMPLE",
             "Simplified: combined service would give Rs 10 lakh gratuity, Rs 4 lakh already granted: the later civil gratuity is capped at Rs 6 lakh.",
             "Simplified illustration (invented numbers, only to show the arithmetic of the cap in Rule 19(5); the real calculation uses the commutation table and capital values): combined service would give Rs 10,00,000 and Rs 4,00,000 was already granted, so the later benefit cannot exceed 10,00,000 minus 4,00,000 = Rs 6,00,000. Under Rule 20(5) the same figures would give no cap from the military side.",
             ORANGE,
             "Here is a simple illustration with invented numbers. Say the combined service would give ten lakh rupees and four lakh were already granted. Under Rule 19 the later benefit is capped at six lakh. Under Rule 20, there would be no such cap. The real calculation also uses commutation tables, so treat this only as the idea."),
            ("THE TRAP",
             "19(5) = limitation. 20(5) = no limitation. Exact words of both: check the Gazette.",
             "Memory line: 19(5) limits, 20(5) does not (ADD-B2-2, BONUS-18). Both are close restatements from a secondary reproduction; the exact wording and the limits should be confirmed from the Gazette. Also remember that the refund instalments start the month after the option month, not the option month.",
             RED,
             "Be careful, this is the trap. Mix these two up and you lose marks: nineteen five has a limit, twenty five has none. Both texts are close restatements here, so check the Gazette for the exact words."),
        ],
        "hook": "REMEMBER: 19(5) = limitation applies • 20(5) = no limitation!",
        "hook_say": "Remember: Rule 19 sub-rule 5 has a limitation, and Rule 20 sub-rule 5 has none.",
        "covers": ["R19(5)", "R20(5)", "R20(3)"],
    },
    {
        "id": "c02_12_rule20_military",
        "chapter": "CHAPTER 12 • RULE 20: MILITARY SERVICE COUNTED FOR CIVIL PENSION",
        "title": "RULE 20 — WHEN MILITARY SERVICE COUNTS FOR A CIVIL PENSION",
        "accent": GREEN, "badge": "RULE 20",
        "q": "When can earlier military service be counted for civil pension?",
        "q_say": "Sir, when can earlier military service be counted for a civil pension?",
        "boxes": [
            ("THE RULE: 20(1)",
             "Military service, then civil re-employment on or before 31.12.2003, military pension stopped and the old benefits refunded: military service counts.",
             "Rule 20(1) (close restatement): a Government servant who rendered military service and was re-employed in a civil service or post on or before 31.12.2003, and who in accordance with his option under the CCS (Pension) Rules, 1972 discontinued the pension on re-employment and refunded (or agreed to refund) the pension drawn, the commuted value of part of pension, and the retirement gratuity including service gratuity, may count the military service as qualifying service (R20(1)). This is the exception mentioned in the second proviso to Rule 11.",
             SKY,
             "Let us take the rule first. A person did military service and was re-employed in a civil post on or before thirty-first December 2003. He stopped the military pension on re-employment, as per his option under the 1972 Rules, and refunded the pension drawn, the commuted value of any part of pension, and the retirement gratuity including service gratuity. Then the military service can be counted. This is the exception that Rule 11 pointed to."),
            ("REFUND AND GAPS: 20(2), 20(4)",
             "Refund in up to 36 monthly instalments. The counting order also condones the gap between military and civil service.",
             "Rule 20(2) (close restatement): refund of pension, bonus or gratuity in monthly instalments, maximum 36; the right to count revives after the full refund (R20(2); the start month is the month after the option). Rule 20(4): the order counting military service includes condonation of the interruption between military service and civil service (R20(4)). The source adds that interruption inside the military service is also condoned; that was not seen in the restatement read, so it is not confirmed. Condonation means forgiving the gap.",
             GREEN,
             "Now the refund and the gaps. Under sub-rule 2, the refund is in monthly instalments, at most thirty-six, and the right to count comes alive after the full refund. Under sub-rule 4, the order that counts the military service also forgives, or condones, the gap between military and civil service. The source adds the gaps inside military service too, but we could not confirm that part."),
            ("THE TWO EXPLANATIONS",
             "Kept the military pension and gratuity under the 1972 option: military service NOT counted. Joined military after 31.12.2003: NPS rules, pension stays.",
             "Explanation 2 (R20-EXPL2): if the servant opted under Rule 19 of the 1972 Rules to keep his military pension and gratuity, his military service is not counted. Explanation 3 (R20-EXPL3): a person who joined the military after 31.12.2003 keeps his military pension and is governed by the NPS rules (the New Pension System). So the refund-and-stop route in Rule 20(1) is the real option.",
             ORANGE,
             "Two Explanations to remember. Explanation 2: if the person chose to keep his military pension and gratuity, his military service is not counted. Explanation 3: a person who joined the military after thirty-first December 2003 is under the New Pension System, and he keeps his military pension. So the refund-and-stop route is the real option."),
            ("REAL EXAMPLE",
             "Imran: military 01.01.1985 to 31.12.1998 = 14 years, civil from 01.03.1999. Refunded; the order condones 2 months: 14 years count.",
             "Example (invented, R20-EX1): Imran served in the military from 01.01.1985 to 31.12.1998, exactly 14 years, and was re-employed in a civil post on 01.03.1999, a gap of two months. He stopped his military pension, and refunded as required. The counting order under Rule 20(4) condoned the two-month gap. All 14 years count as qualifying service; the two months themselves do not count as service. Q: what if he opted to keep the military pension? A: then military service is not counted (Explanation 2).",
             ORANGE,
             "Here is a real example. Imran served in the military from first January 1985 to thirty-first December 1998, which is exactly fourteen years. He joined a civil post on first March 1999, after a two-month gap. He stopped his military pension and refunded as required. The counting order forgave the gap, and all fourteen years count."),
        ],
        "hook": "REMEMBER: military service counts only by refund-and-stop, joined by 31.12.2003!",
        "hook_say": "Remember: military service counts only if the person stopped the military pension and refunded, and was re-employed by thirty-first December 2003.",
        "covers": ["R20(1)", "R20(2)", "R20(4)", "R20-EXPL1(i)", "R20-EXPL2", "R20-EXPL3", "R20-EX1"],
    },
    {
        "id": "c02_13_rule20_2022_amendment",
        "chapter": "CHAPTER 13 • RULE 20: THE 2022 AMENDMENT THAT REVERSED A CLAUSE",
        "title": "RULE 20 EXPLANATION 1(ii) — 'NOT REFUNDED' BECAME 'REFUNDED'",
        "accent": RED, "badge": "G.S.R. 770(E) • 2022",
        "q": "What exactly did the 2022 amendment change in Rule 20, and what is obsolete now?",
        "q_say": "Sir, what exactly did the 2022 amendment change in Rule 20, and what has become obsolete?",
        "boxes": [
            ("THE AMENDMENT",
             "G.S.R. 770(E), 07.10.2022, substituted Explanation 1, clause (ii) of Rule 20.",
             "G.S.R. 770(E) dated 07.10.2022 substituted Explanation 1 clause (ii) of Rule 20 (GSR-770E-R20, R20-EXPL1(ii)). It took effect from publication. The same notification also amended Rules 8, 46(5)(a), 50(9)(h)(iii) and 76; only Rule 20 lies in Chapter III.",
             SKY,
             "Let us take the amendment first. G.S.R. 770(E) of seventh October 2022 substituted clause two of Explanation 1 to Rule 20. This is the only Gazette amendment that touches Chapter III."),
            ("OBSOLETE / OLD WORDING",
             "OBSOLETE / HISTORY ONLY: 'was not required to be refunded'. Replaced by 'was to be refunded' from 07.10.2022.",
             "OBSOLETE / HISTORY ONLY (R20-EXPL1(ii)-OLD): the old wording said that the pension element ignored at pay fixation 'was not required to be refunded'. This was replaced by 'was to be refunded' with effect from publication of G.S.R. 770(E) on 07.10.2022. Current text: refund is required. Close restatement; the Gazette text was not read.",
             RED,
             "This is history only. The old wording said that the pension element ignored when the pay was fixed on re-employment was not required to be refunded. That wording is obsolete. From seventh October 2022 it says the element was to be refunded. The meaning has turned completely around."),
            ("THE CURRENT PACKAGE",
             "Now: (i) pension drawn before re-employment needs no refund; (ii) the ignored element IS refunded; (iii) set-off, balance refunded.",
             "Current Rule 20 Explanation 1 (close restatement): (i) pension drawn before re-employment need not be refunded (R20-EXPL1(i)); (ii) the pension element ignored at pay fixation was to be refunded (R20-EXPL1(ii), changed); (iii) the pension equivalent of gratuity and commuted pension taken into account at pay fixation is set off against the retirement gratuity and commuted value, and the balance is refunded (R20-EXPL1(iii); the source omitted this clause). This mirrors the clauses of Rule 19(2).",
             GREEN,
             "Here is the current package. Clause one: pension drawn before re-employment need not be refunded. Clause two: the ignored pension element is now refunded. Clause three, which the source left out: what was taken into account at pay fixation is set off against the retirement gratuity and commuted value, and the balance is refunded. It mirrors Rule 19, sub-rule 2."),
            ("THE TRAP",
             "A candidate quoting old notes writes 'not refunded': now wrong. The source also wrongly said 'gratuity element'.",
             "Exam use (BONUS-19): a direct question, 'what did the 2022 amendment do to Rule 20 Explanation 1(ii)': it replaced 'was not required to be refunded' by 'was to be refunded'. Also a comparison question, Rule 19 against Rule 20. Discipline: never treat a one-word amendment as neutral; always answer on the current Gazette position. The source's phrase 'gratuity element' is wrong: it is the pension element.",
             RED,
             "Be careful, this is the trap. Someone using old notes would write that this element need not be refunded, and that is now wrong. Also, the source wrongly called it a gratuity element; it is the pension element. A one-word amendment can reverse a whole meaning, so always answer on the current position."),
        ],
        "hook": "REMEMBER: since 07.10.2022 the pay-fixation pension element IS refunded!",
        "hook_say": "Remember: since seventh October 2022 the pension element ignored at pay fixation has to be refunded.",
        "covers": ["R20-EXPL1(ii)", "R20-EXPL1(ii)-OLD", "R20-EXPL1(iii)"],
    },
    {
        "id": "c02_14_cutoff_and_refund_logic",
        "chapter": "CHAPTER 14 • THE 31 DECEMBER 2003 LINE AND THE REFUND IDEA",
        "title": "THE 31.12.2003 LINE AND WHY RULES 18, 19, 20 MAKE YOU REFUND",
        "accent": SKY, "badge": "TIMELINE • REFUNDS",
        "q": "Which rules use the 31 December 2003 date, and why do refunds keep appearing?",
        "q_say": "Sir, which rules use the thirty-first December 2003 date, and why do refunds keep coming up?",
        "boxes": [
            ("THE DATE LINE",
             "31.12.2003 appears in Rules 13, 14, 15, 18, 19 and 20. The New Pension System starts on 01.01.2004.",
             "TL-31.12.2003: the same cut-off date appears in Rule 13 (first appointment in State pensionable establishment), Rule 14 (first appointment in autonomous body), Rule 15 (temporary status granted), Rule 18 (regular appointment after contract), Rule 19 (re-employment) and Rule 20 (re-employment; and Explanation 3, military joining after the date). The New Pension System (NPS) starts on 01.01.2004.",
             SKY,
             "Here is the timeline. The date thirty-first December 2003 appears in Rules 13, 14, 15, 18, 19 and 20. After that date, new joiners are under the New Pension System, which starts on first January 2004. So these outside-service routes are for the old-pension generation."),
            ("THE REFUND IDEA",
             "Refund exists to stop double benefit: what you got once is not paid twice.",
             "REFUND-LOGIC and BONUS-17: if Government already gave something for a service (CPF contribution, pension or gratuity), counting the same service again would pay twice. So the person must give back what was received. Rule 18: Government's CPF contribution with interest and other compensation. Rule 19: pension drawn, commuted value, retirement gratuity (with the Rule 19(2) clauses). Rule 20: the same items for military pension.",
             GREEN,
             "Now the refund idea. If Government has already paid something for a service, as provident fund share, pension or gratuity, then counting the same service again would pay twice. So the person gives back what was received. Rule 18 is about the provident fund share, Rule 19 about civil pension, and Rule 20 about military pension."),
            ("INSTALMENTS",
             "Rules 19 and 20: refund up to 36 monthly instalments, first in the month after the option. Counting revives only after the full refund.",
             "Rule 19(3) and Rule 20(2): monthly instalments, maximum 36, the first instalment from the month after the month in which the option was exercised; the right to count the earlier service revives only after the full refund (LIMIT-36-INSTALMENTS, R19-INSTALMENT-START). Rule 18 states no instalment scheme in the text read.",
             ORANGE,
             "On instalments: Rules 19 and 20 allow up to thirty-six monthly instalments, starting the month after the option. Counting revives only after the last one. Rule 18, in the text we read, says nothing about instalments."),
            ("THE TRAP",
             "Do not mix: Rule 18 = CPF share. Rule 19 = civil pension. Rule 20 = military pension. Refund is a pre-condition, not a formality.",
             "Trap: candidates treat the refund as a formality. It is a precondition (R19(3), R20(2)); until the full refund, the old service stays uncounted. And do not apply Rules 19 and 20 to superannuation pensioners (outside the Rule 19 gate).",
             RED,
             "Be careful, this is the trap. The refund is not a formality. It is a pre-condition for counting. And keep the three rules apart: Rule 18 is the provident fund share, Rule 19 is a civil pensioner, and Rule 20 is a military pensioner."),
        ],
        "hook": "REMEMBER: 31.12.2003 • refund = no double benefit • 36 instalments • count only after the last one!",
        "hook_say": "Remember: the date is thirty-first December 2003, refunds stop double benefit, there are at most thirty-six instalments, and counting starts only after the last one.",
        "covers": ["TL-31.12.2003", "REFUND-LOGIC", "LIMIT-36-INSTALMENTS"],
    },
    {
        "id": "c02_15_rule21_leave",
        "chapter": "CHAPTER 15 • RULE 21: PERIODS OF LEAVE",
        "title": "RULE 21 — WHICH LEAVE COUNTS, AND WHAT IF NOTHING IS WRITTEN?",
        "accent": ORANGE, "badge": "RULE 21",
        "q": "Does leave count as qualifying service, and what if the service book is silent?",
        "q_say": "Sir, does leave count as qualifying service, and what if the service book says nothing?",
        "boxes": [
            ("THE RULE",
             "All leave with leave salary counts. Extraordinary leave on a medical certificate counts too.",
             "Rule 21 (close restatement): all periods of leave for which leave salary is payable, and extraordinary leave granted on a medical certificate, count as qualifying service (R21-MAIN). Leave salary is the pay received while on leave. Extraordinary leave (EOL) is leave without pay.",
             SKY,
             "Let us take the rule first. All leave for which leave salary is paid counts as qualifying service. Leave salary is simply the pay received while on leave. Extraordinary leave, which is leave without pay, also counts if it was granted on a medical certificate."),
            ("THE PROVISO",
             "Other EOL does not count, but the appointing authority may allow it when granting it: civil commotion, or higher scientific or technical studies.",
             "Proviso to Rule 21 (close restatement): extraordinary leave other than on medical certificate does not count; but the appointing authority may, when granting the leave, allow it to count where the servant was prevented by civil commotion from joining or rejoining duty, or where the leave was for prosecuting higher scientific or technical studies (R21-PROV).",
             GREEN,
             "Now the exception. Other extraordinary leave does not count. But the appointing authority, at the time of granting it, may allow it to count in two cases: the servant could not join or rejoin duty because of civil commotion, or the leave was for higher scientific or technical studies."),
            ("THE EXPLANATION: SILENCE",
             "A non-counting EOL needs a definite service-book entry at the time. Late entry is allowed up to six months before superannuation. No entry means it counts.",
             "Explanation to Rule 21 (close restatement): for extraordinary leave that was neither on medical certificate nor allowed under the proviso, a definite entry must be made in the service book at the time that the period will not count as qualifying service. The entry may be made later but not later than six months before superannuation (LIMIT-R21-6MONTHS). If there is no such entry, the extraordinary leave counts as qualifying service (R21-EXPL).",
             ORANGE,
             "Now the Explanation, the real gold. If an extraordinary leave is not covered by a medical certificate or the proviso, the service book needs a definite entry at the time saying that the period will not count. It may be made later, but not later than six months before superannuation. If there is no entry, the leave counts."),
            ("REAL EXAMPLE",
             "Hari: 2015 EOL, no entry: counts. If he retires 30.11.2030, the latest late entry is 30.05.2030, not after.",
             "Example (invented, R21-EX1): Hari took extraordinary leave in 2015 for personal reasons; no entry was ever made in his service book, so the period counts. Had the department wished to exclude it, and Hari's superannuation is 30.11.2030, the latest date for a late entry is 30.05.2030 (six calendar months before superannuation; counting method is an assumption, check the exact reckoning in the rule). Q: does EOL on a medical certificate count? A: yes, always.",
             ORANGE,
             "Here is a real example. Hari took extraordinary leave in 2015, and nobody made an entry in his service book. So that period counts. If the department wanted to exclude it, and Hari retires on thirtieth November 2030, a late entry must be made by thirtieth May 2030, six months before."),
            ("THE TRAP: SILENCE",
             "In Rule 21 silence helps the employee. In Rule 23 silence hurts. In Rule 28 silence means forgiven.",
             "Comparison (R21-SILENCE, BONUS-20): Rule 21 Explanation, silence means the EOL counts; Rule 23(2), silence means the suspension period does not count; Rule 28(1), silence in the service book means the interruption is condoned. Three rules, three silent positions. Practical risk: an audit objection arises when an EOL was never regularised yet counted; keep timely entries.",
             RED,
             "Be careful, this is the trap. Silence means different things in different rules. In Rule 21, silence helps the employee, and the leave counts. In Rule 23, silence hurts, and the suspension does not count. In Rule 28, silence means the gap is forgiven."),
        ],
        "hook": "REMEMBER: Rule 21 silence = EOL counts • entry up to 6 months before retirement!",
        "hook_say": "Remember: in Rule 21 silence means the extraordinary leave counts, and a late entry is allowed only up to six months before superannuation.",
        "covers": ["R21-MAIN", "R21-PROV", "R21-EXPL", "LIMIT-R21-6MONTHS", "R21-EX1", "R21-SILENCE"],
    },
    {
        "id": "c02_16_rule22_training",
        "chapter": "CHAPTER 16 • RULE 22: DEPARTMENTAL TRAINING BEFORE APPOINTMENT",
        "title": "RULE 22 — TRAINING PERIOD, JOINING TIME AND THE HEAD OF DEPARTMENT",
        "accent": GREEN, "badge": "RULE 22",
        "q": "Does training before a Group C appointment count, and how are gaps handled?",
        "q_say": "Sir, does training before a Group C appointment count, and how are gaps between training and appointment handled?",
        "boxes": [
            ("THE RULE: 22(1), 22(2)",
             "Group C departmental training counts if pay in scale, stipend or nominal allowance was received. Other cases: Government decides by order.",
             "Rule 22(1) (close restatement): where a Government servant had to undergo departmental training before regular appointment to a Group C post, and during the training received pay in the pay scale, a stipend or a nominal allowance, the training period counts as qualifying service (R22(1)). Rule 22(2): in cases not covered by sub-rule (1), the Government decides by order whether the training period immediately preceding the appointment counts (R22(2)). A stipend is a small fixed payment made to a trainee.",
             SKY,
             "Let us take the rule first. If a Government servant had to undergo departmental training before regular appointment to a Group C post, and received pay in the scale, a stipend or a nominal allowance during it, the training period counts. A stipend is a small fixed payment made to a trainee. For cases not covered by that, sub-rule 2 says the Government decides by an order whether the training immediately before the appointment counts."),
            ("JOINING-TIME GAPS: 22(3), 22(4)",
             "Gap between training and appointment at different stations counts up to the permitted joining time. The excess is regularised by leave, or by EOL from the Head of Department.",
             "Rule 22(3) (close restatement): where training counts and training and regular appointment were at different stations, the interruption caused thereby counts up to the permissible joining time under the transfer rules (R22(3)). Rule 22(4): if the interruption exceeds joining time for administrative reasons, the excess is regularised by granting leave due; if no leave is due, the Head of Department grants extraordinary leave, and the period regularised by EOL counts as qualifying service (R22(4)). Joining time is the time allowed to travel and join the new place.",
             GREEN,
             "Now the gaps. When training and the regular appointment were at different stations, the gap counts up to the permitted joining time, which is the time allowed to travel and join the new place. If the gap is longer, for administrative reasons, the excess is regularised by granting leave that is due, and if no leave is due, the Head of Department grants extraordinary leave. That extraordinary leave period counts."),
            ("REAL EXAMPLE",
             "Jaya, Group C clerk: 6 days beyond joining time, administrative reasons, no leave due: the Head of Department grants 6 days EOL, and they count.",
             "Example (invented, R22-EX1): Jaya was sent for training to another station in 2005. She took 6 days more than the permitted joining time, for administrative reasons, and had no leave due. The Head of Department granted 6 days of extraordinary leave, and those 6 days count as qualifying service. This works only if no leave was due; if leave was due, that leave is used first. Q: when does training not count? A: when no pay, stipend or allowance was received, or when it is outside Rule 22(1) and the Government order does not count it.",
             ORANGE,
             "Here is a real example. Jaya, a Group C clerk, was sent for training to another station in 2005. She took six days more than the permitted joining time, for administrative reasons, and had no leave due. The Head of Department granted six days of extraordinary leave, and those days count. If she had leave due, that leave would be used first."),
            ("WHO IS THE HEAD OF DEPARTMENT?",
             "HoD = the authority named in Schedule I of the Delegation of Financial Powers Rules, 1978, or one designated by the President. Rule 3(1)(p).",
             "Rule 3(1)(p) (R3(1)(p)-HOD, close restatement): Head of Department means the authority specified in Schedule I of the Delegation of Financial Powers Rules, 1978, or an authority designated by the President. In Rule 22(4) it is the HoD who grants the extraordinary leave. Different actors in this chapter (BONUS-21): appointing authority decides on EOL under Rule 21; the Head of Department acts under Rule 22(4); the Head of Office verifies under Rule 30.",
             BLUE,
             "Who is the Head of Department? Rule 3, clause 1, sub-clause p, says it is the authority named in Schedule I of the 1978 Delegation of Financial Powers Rules, or one designated by the President. Remember the actors: under Rule 21 it is the appointing authority, under Rule 22 sub-rule 4 it is the Head of Department, and under Rule 30 it is the Head of Office."),
            ("THE TRAP",
             "Rule 21 ordinary EOL does NOT count; Rule 22(4) EOL DOES count, because it is the regularising mechanism.",
             "Contrast: the ordinary EOL of Rule 21 does not count (unless on medical certificate or allowed under the proviso), but EOL granted under Rule 22(4) to regularise excess joining time does count. Do not send the file to the wrong authority: Rule 21 appointing authority, Rule 22(4) Head of Department.",
             RED,
             "Be careful, this is the trap. The ordinary extraordinary leave of Rule 21 does not count, but the extraordinary leave under Rule 22 sub-rule 4 does, because it is the regularising tool. Also check which authority acts, or the file goes to the wrong desk."),
        ],
        "hook": "REMEMBER: Rule 22(4) EOL counts — unlike ordinary EOL in Rule 21!",
        "hook_say": "Remember: the extraordinary leave under Rule 22 sub-rule 4 counts, unlike ordinary extraordinary leave under Rule 21.",
        "covers": ["R22(1)", "R22(2)", "R22(3)", "R22(4)", "R22-EX1", "R3(1)(p)-HOD"],
    },
    {
        "id": "c02_17_rule23_suspension",
        "chapter": "CHAPTER 17 • RULE 23: THE SUSPENSION PERIOD",
        "title": "RULE 23 — WHEN A SUSPENSION PERIOD COUNTS",
        "accent": ORANGE, "badge": "RULE 23",
        "q": "When does the period of suspension count as qualifying service?",
        "q_say": "Sir, when does the period of suspension count as qualifying service?",
        "boxes": [
            ("THE TEST: 23(1)",
             "At the end of the inquiry: fully exonerated or only a minor penalty, AND suspension held wholly unjustified. Both needed.",
             "Rule 23(1) (close restatement): at the end of the inquiry, the period of suspension counts as qualifying service if (i) the Government servant is fully exonerated or is only awarded a minor penalty, AND (ii) the suspension is held to have been wholly unjustified (R23(1)). The two limbs are cumulative. Suspension means being kept away from duty while an inquiry goes on. Exonerated means cleared of the charge.",
             SKY,
             "Let us take the rule first. Suspension means being kept away from duty while an inquiry goes on. At the end of the inquiry, the period counts only if two things are both true: the servant is fully exonerated, which means cleared, or got only a minor penalty, and the suspension was held to be wholly unjustified. Exoneration alone is not enough."),
            ("THE OTHER CASES: 23(2)",
             "Every other case: the period does NOT count unless the competent authority expressly declares it, and to what extent.",
             "Rule 23(2) (close restatement): in cases not covered by sub-rule (1), the period does not count as qualifying service unless the competent authority, at the time of passing the orders, expressly declares that it counts, to the extent it declares (R23(2)). Silence means it does not count. Note: the source's authority map lists Rule 23(2) under 'Appointing Authority'; the rule text names the Competent Authority, so the map is corrected (ADD-B2-3-AUTH-MAP-23(2)).",
             GREEN,
             "Now all other cases. The period does not count unless the competent authority, when passing the orders, expressly declares that it counts, and to what extent. Silence means it does not count. Note that the rule names the competent authority, not the appointing authority."),
            ("THE ORDER: 23(3)",
             "In every case, the competent authority passes an order stating how much counts, and a definite entry goes in the service book.",
             "Rule 23(3) (close restatement): in every case of suspension, the competent authority shall pass an order specifying the extent, if any, to which the period counts as qualifying service, and a definite entry shall be made in the service book (R23(3)).",
             BLUE,
             "Under sub-rule 3, in every suspension case the competent authority must pass an order saying how much of the period, if any, counts, and a definite entry must be made in the service book."),
            ("REAL EXAMPLE",
             "Kiran: 100 days suspended, fully exonerated, held wholly unjustified: all 100 days count. Exonerated but not held unjustified: none, unless the authority declares, say, 60.",
             "Example (invented, R23): Kiran, a clerk, is suspended for 100 days. After the inquiry he is fully exonerated and the suspension is held wholly unjustified: all 100 days count, and the order and service book entry follow. If he was exonerated but the suspension was not held wholly unjustified, none of the 100 days counts unless the competent authority expressly declares, for example, that 60 days count. Q: exonerated but not unjustified? A: not counted without an express declaration, Rule 23(2).",
             ORANGE,
             "Here is a real example. Kiran is suspended for one hundred days. If he is fully exonerated and the suspension is held wholly unjustified, all one hundred days count. If he is exonerated but the suspension was not held wholly unjustified, none counts unless the authority expressly declares, say, sixty days, and then sixty count."),
            ("THE TRAP: SILENCE HURTS",
             "AND, not OR. In Rule 23 silence means NOT counted, the opposite of Rule 21.",
             "Traps (BONUS-20, R21-SILENCE): (1) the two limbs of Rule 23(1) are AND, not OR; (2) silence under Rule 23(2) means the period does not count, the opposite of Rule 21; (3) the order and the service book entry are mandatory in every case under Rule 23(3).",
             RED,
             "Be careful, this is the trap. The two conditions are joined by AND. And silence here hurts: if the competent authority does not expressly declare, the suspension period does not count. That is the opposite of Rule 21."),
        ],
        "hook": "REMEMBER: Rule 23 = exonerated AND wholly unjustified; otherwise only by express declaration!",
        "hook_say": "Remember: Rule 23 needs exoneration and a wholly unjustified suspension, otherwise the period counts only if the competent authority expressly declares it.",
        "covers": ["R23(1)", "R23(2)", "R23(3)", "ADD-B2-3-AUTH-MAP-23(2)"],
    },
    {
        "id": "c02_18_rules24_25_dismissal_reinstatement",
        "chapter": "CHAPTER 18 • RULES 24 AND 25: DISMISSAL, REMOVAL AND REINSTATEMENT",
        "title": "RULES 24-25 — LOSING PAST SERVICE, AND GETTING IT BACK",
        "accent": RED, "badge": "RULES 24 • 25",
        "q": "What happens to past service on dismissal or removal, and when does it come back?",
        "q_say": "Sir, what happens to past service on dismissal or removal, and when does it come back?",
        "boxes": [
            ("RULE 24: FORFEITURE",
             "Dismissal or removal forfeits past service. Compulsory retirement is NOT named.",
             "Rule 24 (close restatement): dismissal or removal of a Government servant from a service or post entails forfeiture of his past service (R24). Compulsory retirement is not mentioned in the rule (R24, R22-24-ARCH). Forfeiture means the earlier service is wiped out for pension.",
             RED,
             "Let us take Rule 24 first. If a Government servant is dismissed or removed from service, his past service is forfeited, which means wiped out for pension. Rule 24 does not mention compulsory retirement at all."),
            ("NOT COMPULSORY RETIREMENT",
             "Rule 24 names only dismissal and removal.",
             "Reading (BONUS-22, R22-24-ARCH, a fair summary, not rule text): the two events in Rule 24 are dismissal and removal; compulsory retirement is deliberately not named, so Rule 24 does not forfeit service on compulsory retirement. Practice: always check the order to see which penalty was actually imposed.",
             ORANGE,
             "Why is compulsory retirement left out? It is a penalty, but the rule does not forfeit service for it. It is a reading of the rule, so always check which penalty the order actually imposed."),
            ("RULE 25(1)",
             "Reinstated on appeal or review: the past service counts again.",
             "Rule 25(1) (close restatement): a Government servant who was dismissed, removed or compulsorily retired and is later reinstated on appeal or review may count his past service as qualifying service (R25(1)). Reinstatement means being taken back into service.",
             GREEN,
             "Now Rule 25. If a person who was dismissed, removed or compulsorily retired is later reinstated, which means taken back, on appeal or review, the past service counts again."),
            ("RULE 25(2): GAP",
             "The gap and any suspension do not count, unless regularised by a specific order.",
             "Rule 25(2) (close restatement): the interruption between the dismissal, removal or compulsory retirement and the reinstatement, and the period of suspension if any, do not count as qualifying service unless regularised as duty or leave by a specific order of the authority that reinstated him (R25(2)). Compare Rule 26(7): both restore continuity, but the gap does not count (R26-BONUS23-COMPARE).",
             BLUE,
             "Sub-rule 2 draws the line. The gap between the dismissal and the reinstatement, and any suspension period, do not count unless the reinstating authority specifically orders them regularised as duty or leave. Past service returns, but the gap does not."),
            ("REAL EXAMPLE",
             "Mohan: 10 years served, dismissed 2015, reinstated 2017. The 10 years count; the gap does not.",
             "Example (invented): Mohan had 10 years of service when dismissed on 01.03.2015. Under Rule 24 that service was forfeited. On appeal he is reinstated on 01.09.2017. Under Rule 25(1) his 10 years count again. The gap from 01.03.2015 to 01.09.2017 is 2 years 6 months; under Rule 25(2) it counts only if the reinstating authority regularises it as duty or leave by a specific order. Qualifying service therefore stays 10 years, plus any period so regularised.",
             ORANGE,
             "Here is a real example. Mohan had ten years of service when he was dismissed on first March 2015. Under Rule 24 that was forfeited. He was reinstated on appeal on first September 2017, so under Rule 25 his ten years count again. The gap of two years and six months does not count, unless the reinstating authority regularises it by a specific order."),
        ],
        "hook": "REMEMBER: Rule 24 forfeits on dismissal or removal, NOT compulsory retirement; Rule 25 restores, minus the gap!",
        "hook_say": "Remember: Rule 24 forfeits on dismissal or removal, not compulsory retirement, and Rule 25 gives past service back on reinstatement, but the gap does not count.",
        "covers": ["R24", "R22-24-ARCH", "R25(1)", "R25(2)", "R26-BONUS23-COMPARE"],
    },
    {
        "id": "c02_19_rule26_resignation_forfeiture",
        "chapter": "CHAPTER 19 • RULE 26(1)-(4): RESIGNATION AND PERMITTED RESIGNATION",
        "title": "RULE 26 (1)-(4) — RESIGNATION FORFEITS, UNLESS PROPERLY PERMITTED",
        "accent": PINK, "badge": "RULE 26(1)-(4)",
        "q": "Does resignation wipe out past service, and how can that be avoided?",
        "q_say": "Sir, does resignation wipe out past service, and how can that be avoided?",
        "boxes": [
            ("THE GENERAL RULE: 26(1)",
             "Resignation forfeits past service, unless the appointing authority permits withdrawal of the resignation in public interest.",
             "Rule 26(1) (close restatement): resignation from a service or post entails forfeiture of past service, unless the resignation is allowed to be withdrawn in public interest by the appointing authority (R26(1)). Note the correct count: Rule 26 has 8 sub-rules as read, not 26; the source's 'twenty-six sub-rules' is wrong (R26-SUBRULE-COUNT, changed). Appointing authority is the authority that made the appointment.",
             RED,
             "Let us take the general rule. Resignation forfeits past service, unless the appointing authority allows the resignation to be withdrawn in public interest. A small correction: the source said Rule 26 has twenty-six sub-rules. That is wrong. Rule 26 has eight sub-rules."),
            ("THE SAVING: 26(2)",
             "No forfeiture if the resignation was with proper permission, to take another Government appointment where the service qualifies. Temporary or permanent does not matter.",
             "Rule 26(2) (close restatement): resignation does not entail forfeiture if it was submitted to take up, with proper permission, another appointment under the Government where service qualifies, whether temporary or permanent (R26(2)). This is the door through which Rule 13(2) and Rule 14(1) work.",
             GREEN,
             "Now the saving. There is no forfeiture if the resignation was submitted with proper permission, in order to take another appointment under the Government where service qualifies. It does not matter whether the new appointment is temporary or permanent."),
            ("THE PAPERS: 26(3)",
             "The acceptance order must say that he resigns to join another post with proper permission. The Head of Office makes a specific service-book entry.",
             "Rule 26(3) (close restatement): the order accepting the resignation must clearly indicate that the Government servant is resigning to take up another appointment with proper permission, and the Head of Office shall make a specific entry in the service book (R26(3)). Chain of three links: permission, indication in the order, service-book entry. A weak link invites an audit objection. Example (invented, R26-EX1): Meena, an Assistant, resigns with permission to join another Central post; the order says so and the entry is made, so her past service is safe.",
             BLUE,
             "Sub-rule 3 is about papers. The order accepting the resignation must clearly say that the person resigns to join another post with proper permission, and the Head of Office makes a specific entry in the service book. Permission, order, entry: three links. Take Meena, an Assistant, who resigns with permission to join another Central post. With the order and entry in place, her past service is safe."),
            ("THE GAP: 26(4)",
             "Different stations: the gap within joining time is covered by leave due on the relief date. The rest needs formal condonation.",
             "Rule 26(4) (close restatement): where the old and new posts are at different stations, the gap within the joining time is covered by leave due on the date of relief, and the remaining gap needs formal condonation (R26(4)). Illustration (invented numbers): gap of 11 days, joining time 6 days: 6 days covered by leave due, 5 days need condonation. Link: without the permission papers the case falls in Rule 26(1) (R13-R26-LINK).",
             ORANGE,
             "Sub-rule 4 deals with the gap between the two posts when they are at different stations. The part within joining time is covered by leave due on the date of relief, and the remaining part needs formal condonation. For instance, with an eleven-day gap and six days of joining time, six days are covered and five need condonation."),
        ],
        "hook": "REMEMBER: resignation forfeits • proper permission saves • order plus service-book entry!",
        "hook_say": "Remember: resignation forfeits past service, proper permission to join another Government post saves it, and the order and the service book entry must say so.",
        "covers": ["R26(1)", "R26-SUBRULE-COUNT", "R26(2)", "R26(3)", "R26(4)", "R26-EX1", "R13-R26-LINK"],
    },
    {
        "id": "c02_20_rule26_withdrawal",
        "chapter": "CHAPTER 20 • RULE 26(5)-(8): WITHDRAWING A RESIGNATION",
        "title": "RULE 26 (5)-(8) — FOUR CONDITIONS, ONE BAR AND ONE SPECIAL SAVING",
        "accent": SKY, "badge": "RULE 26(5)-(8)",
        "q": "On what conditions can a resignation be withdrawn, and what does withdrawal give back?",
        "q_say": "Sir, on what conditions can a resignation be withdrawn, and what exactly does withdrawal give back?",
        "boxes": [
            ("FOUR CONDITIONS: 26(5)",
             "(i) compelling reasons, clean record, material change; (ii) no improper conduct in between; (iii) absence not over 90 days; (iv) post available.",
             "Rule 26(5) (close restatement; all four needed): (i) the resignation was for compelling reasons without any stain on integrity, efficiency or conduct, and circumstances have materially changed; (ii) the conduct in the intervening period was not improper; (iii) the absence from duty did not exceed 90 days (LIMIT-R26-90DAYS); (iv) the post resigned from, or a comparable post, is available (R26(5)).",
             SKY,
             "Let us take the four conditions for withdrawal. One: the resignation was for compelling reasons with no stain on integrity, efficiency or conduct, and circumstances have materially changed. Two: the conduct in between was not improper. Three: the absence did not exceed ninety days. Four: the same post or a comparable post is available."),
            ("THE BAR: 26(6)",
             "No withdrawal if the resignation was for a private commercial company, or a corporation or company that Government owns or controls.",
             "Rule 26(6) (close restatement): withdrawal is not allowed if the resignation was for the purpose of taking up an appointment in a private commercial company, or in a corporation or company wholly or substantially owned or controlled by the Government. The rule text read also adds a body controlled or financed by Government; the source omitted this limb (R26(6)).",
             RED,
             "Now the bar. Withdrawal is not allowed if the resignation was to join a private commercial company, or a corporation or company owned or controlled by Government. The rule text we read also adds a body controlled or financed by Government, which the source left out."),
            ("WHAT WITHDRAWAL GIVES: 26(7)",
             "The withdrawal order includes condonation of the interruption, but the interruption period itself does not count.",
             "Rule 26(7) (close restatement): when withdrawal is allowed, the order includes condonation of the interruption in service; the period of interruption does not count as qualifying service (R26(7), R26-BONUS23-COMPARE). Continuity returns, the gap is not counted. Same theme as reinstatement under Rule 25(2).",
             GREEN,
             "When withdrawal is allowed, the order automatically includes condonation of the interruption, so continuity is saved. But the interruption period itself does not count. Continuity comes back; the gap does not."),
            ("SPECIAL: 26(8)",
             "Resignation made for Rule 35 or 36 purposes does not forfeit past Government service. Gazette not read.",
             "Rule 26(8) (close restatement; R26(8), changed because the source never mentions it): a resignation made for the purposes of Rule 35 or Rule 36 (dealt with in a later batch) does not forfeit past Government service. FLAG: seen on two secondary reproductions (a page and the staffnews book PDF, both read through a summarising tool, which gave the wording 'A resignation submitted for the purpose of rule 35 or rule 36 shall not entail forfeiture of past service'); not confirmed against the Gazette; verify before final use. Rule 26(8) is one of the 8 sub-rules.",
             ORANGE,
             "There is one more sub-rule that the source never mentioned. Rule 26, sub-rule 8, says a resignation made for the purposes of Rules 35 or 36, which we meet in a later part, does not forfeit past Government service. We saw it in two secondary copies of the Rules, not in the Gazette, so check the Gazette before final use."),
            ("THE TRAP",
             "Trap: 'withdrawal allowed' does not mean the gap counts. The 90-day limit is hard, and the bar for private companies is absolute.",
             "Traps (BONUS-23): (1) the withdrawal order saves continuity but the gap does not count; (2) the 90-day absence limit in 26(5)(iii) is a hard condition; (3) the private commercial company bar in 26(6) applies however clean the record. Example: absence of 80 days can pass condition (iii); 95 days cannot. Q: can a resignation be withdrawn? A: yes, in public interest by the appointing authority, on four conditions, except the barred cases.",
             RED,
             "Be careful, this is the trap. Many think that once withdrawal is allowed, the gap also counts. It does not. The ninety days limit is hard: eighty days of absence can pass, ninety-five cannot. And the bar for private commercial companies applies however clean the record is."),
        ],
        "hook": "REMEMBER: 4 conditions, 90 days max • no withdrawal for a private company • gap never counts!",
        "hook_say": "Remember: four conditions, ninety days at most, no withdrawal when the resignation was for a private company, and the gap never counts.",
        "covers": ["R26(5)", "LIMIT-R26-90DAYS", "R26(6)", "R26(7)", "R26(8)", "R26-BONUS23-COMPARE"],
    },
    {
        "id": "c02_21_rule27_interruption",
        "chapter": "CHAPTER 21 • RULE 27: WHAT AN INTERRUPTION DOES TO PAST SERVICE",
        "title": "RULE 27 — INTERRUPTION FORFEITS, EXCEPT FIVE CASES",
        "accent": ORANGE, "badge": "RULE 27",
        "q": "What does an interruption in service do to past service, and what are the exceptions?",
        "q_say": "Sir, what does an interruption in service do to past service, and what are the exceptions?",
        "boxes": [
            ("GENERAL RULE, CASES (a) AND (b)",
             "Interruption forfeits past service, except: (a) authorised leave; (b) unauthorised absence after authorised leave, while the post is not substantively filled.",
             "Rule 27(1) (close restatement): interruption in service entails forfeiture of past service except in these cases (R27(1)). (a) Authorised leave of absence (R27(1)(a)). (b) Unauthorised absence in continuation of authorised leave of absence, so long as the post is not substantively filled (R27(1)(b)). Unauthorised absence is absence without sanction.",
             SKY,
             "Let us take the general rule. An interruption in service forfeits past service, except in five cases. Case a: authorised leave of absence. Case b: unauthorised absence that continues authorised leave, but only so long as no one has been substantively appointed to that post."),
            ("CASES (c), (d), (e)",
             "(c) suspension then reinstatement, or death, permitted retirement or superannuation during suspension; (d) transfer to non-qualifying service in public interest; (e) joining time.",
             "Rule 27(1)(c) (read as: reinstated, or dies or retires while under suspension; R27(1)(c)): suspension immediately followed by reinstatement in the same or another post, or death, permitted retirement or retirement on superannuation during suspension. (d) Transfer to a non-qualifying service in an establishment under Government control, ordered by the competent authority in public interest (R27(1)(d)). (e) Joining time on transfer from one post to another (R27(1)(e)).",
             GREEN,
             "Case c: a suspension that is immediately followed by reinstatement, or the servant dies, is allowed to retire, or retires on superannuation while under suspension. Case d: a transfer to non-qualifying service in an establishment under Government control, ordered by the competent authority in public interest. Case e: joining time on transfer."),
            ("POWER AND EXAMPLE: 27(2)",
             "The appointing authority may, by order, turn unauthorised absence into extraordinary leave, with retrospective effect.",
             "Rule 27(2) (close restatement): the appointing authority may, by order, commute retrospectively unauthorised absence into extraordinary leave (R27(2)). Example (invented, R27-EX1): Omar, a clerk, went on authorised leave and then stayed away for 6 days without sanction; his post had not been substantively filled, so case (b) saved his past service. Had the post been substantively filled, the same absence would have forfeited the past service.",
             ORANGE,
             "Sub-rule 2 gives the appointing authority a power: by an order it can turn unauthorised absence into extraordinary leave, with retrospective effect. Here is an example. Omar went on authorised leave and then stayed away six more days without sanction. His post had not been substantively filled, so his past service stayed safe. If the post had been filled, that absence would have forfeited it."),
            ("THE TRAP",
             "Do not learn '5 exceptions, 2 conditions' as a rule. Conditions sit in (b), (c) and (d). Anything outside the five forfeits.",
             "Flag (R27-MNEMONIC, UNVERIFIED as a rule): the source's mnemonic '5 exceptions, 2 conditions' is a memory device only; clause (c) also carries conditions, so do not teach it as a rule. Reasoning on (b) and (d) (BONUS-24, source reasoning, not rule text): clause (b) protects only while the post is not substantively filled; clause (d) needs the transfer to be ordered by the competent authority in public interest. Any interruption outside the five forfeits past service.",
             RED,
             "Be careful, this is the trap. The source teaches a mnemonic, five exceptions and two conditions, but that is only a memory device. Clause c also has conditions. Clause b depends on the post not being substantively filled, and clause d needs a competent authority's public interest order. Any other interruption forfeits past service."),
        ],
        "hook": "REMEMBER: Rule 27 = interruption forfeits, five exceptions (a)-(e), and 27(2) can commute absence into EOL!",
        "hook_say": "Remember: interruption forfeits past service except in five cases, and sub-rule 2 lets the appointing authority commute absence into extraordinary leave.",
        "covers": ["R27(1)", "R27(1)(a)", "R27(1)(b)", "R27(1)(c)", "R27(1)(d)", "R27(1)(e)", "R27(2)", "R27-EX1", "R27-MNEMONIC"],
    },
    {
        "id": "c02_22_rule28_condonation",
        "chapter": "CHAPTER 22 • RULE 28: CONDONATION OF INTERRUPTION",
        "title": "RULE 28 — WHEN A GAP IS FORGIVEN, AND WHEN IT IS NOT",
        "accent": GREEN, "badge": "RULE 28",
        "q": "When is a gap between two civil spells forgiven, and can the authority refuse?",
        "q_say": "Sir, when is a gap between two spells of civil service forgiven, and can the authority refuse?",
        "boxes": [
            ("AUTOMATIC: 28(1)",
             "A gap between two spells of civil service is automatically forgiven, and the earlier service qualifies, unless the service book shows otherwise.",
             "Rule 28(1) (close restatement): interruption between two spells of civil service under the Government is, unless the service book indicates otherwise, deemed to be condoned automatically, and the service before the interruption qualifies. Civil service paid from Defence Services Estimates or Railway Estimates is included (R28(1)). Condonation means the gap is forgiven.",
             SKY,
             "Let us take the automatic route first. A gap between two spells of civil service under the Government is deemed forgiven, or condoned, unless the service book shows the opposite. The service before the gap then qualifies. Civil service paid from the Defence Services Estimates or the Railway Estimates is included."),
            ("THE LIMITS: 28(2), 28(3)",
             "Not for gaps caused by resignation, dismissal, removal or strike. And the gap period itself never counts.",
             "Rule 28(2) (close restatement): automatic condonation does not apply to interruption caused by resignation, dismissal, removal or participation in a strike (R28(2)). Rule 28(3): the period of interruption itself does not count as qualifying service (R28(3)). Only the earlier service is saved.",
             RED,
             "Now the limits. Automatic condonation does not apply when the gap was caused by resignation, dismissal, removal or taking part in a strike. And under sub-rule 3 the gap period itself never counts. Only the service before the gap is saved."),
            ("DISCRETION: 28(4)-(6)",
             "Otherwise the appointing authority may consider condonation. Refusal only in exceptional and grave circumstances, and only after a fair hearing in person.",
             "Rule 28(4) (close restatement): the appointing authority may consider condonation of interruption (R28(4)). 28(5): refusal only in exceptional and grave circumstances (R28(5)). 28(6): before refusing, the servant must be given a reasonable opportunity to make a representation and to be heard in person (R28(6)). In short: 28(1) is silence means forgiven; 28(4) is when silence is not enough, the authority decides.",
             GREEN,
             "Sub-rules 4 to 6 give the discretionary route. The appointing authority may consider condonation. Refusal is possible only in exceptional and grave circumstances, and before refusing, the servant must be given a reasonable chance to represent and be heard in person."),
            ("EXAMPLE AND TRAP",
             "Nisha: 6-month gap between two civil spells, no contrary entry: condoned, earlier service safe, the 6 months do not count.",
             "Example (invented, R28-EX1): Nisha left one civil post and joined another after a gap of 6 months; the service book has no contrary entry. The gap is condoned automatically and her earlier service qualifies, but the 6 months themselves do not count. Q: does automatic condonation make the gap count? A: no, Rule 28(3). Link (BONUS-25): Rule 27 says what an interruption does, Rule 28 says how to undo it, Rule 30 says how it is verified.",
             ORANGE,
             "Here is a real example. Nisha left one civil post and joined another six months later, with no contrary entry in the service book. The gap is condoned automatically and her earlier service is safe, but the six months themselves do not count. Be careful, this is the trap: condonation saves the earlier service, it does not count the gap."),
        ],
        "hook": "REMEMBER: Rule 28 saves earlier service, never the gap; not for resignation, dismissal, removal or strike!",
        "hook_say": "Remember: Rule 28 saves the earlier service but never counts the gap, and automatic condonation does not cover resignation, dismissal, removal or strike.",
        "covers": ["R28(1)", "R28(2)", "R28(3)", "R28(4)", "R28(5)", "R28(6)", "R28-EX1"],
    },
    {
        "id": "c02_23_rule29_international",
        "chapter": "CHAPTER 23 • RULE 29: DEPUTATION TO THE UN AND OTHER INTERNATIONAL BODIES",
        "title": "RULE 29 — SERVICE ABROAD IN AN INTERNATIONAL ORGANISATION",
        "accent": BLUE, "badge": "RULE 29",
        "q": "If a servant is sent to an international organisation, does that service count?",
        "q_say": "Sir, if a Government servant is sent to the United Nations or another international body, does that service count?",
        "boxes": [
            ("WHO IS COVERED",
             "A servant on foreign service in the UN Secretariat or UN bodies, IMF, IBRD, ADB, Commonwealth Secretariat or any other international organisation.",
             "Rule 29 (close restatement): a Government servant who is on foreign service in the United Nations Secretariat or other United Nations bodies, the International Monetary Fund, the International Bank for Reconstruction and Development, the Asian Development Bank, the Commonwealth Secretariat, or any other international organisation. Foreign service means service outside the Government's own cadre, on loan. Deputation means being sent on temporary posting elsewhere.",
             SKY,
             "Let us take who is covered. Rule 29 is for a Government servant on foreign service, which means on loan outside the Government's own cadre, in the United Nations Secretariat or other UN bodies, the IMF, the World Bank group's IBRD, the Asian Development Bank, the Commonwealth Secretariat, or any other international organisation."),
            ("THE OPTION",
             "He chooses: pay pension contribution and count the service, or do not pay and do not count it.",
             "Rule 29 (R29): the servant may opt either (1) to pay pension contribution for that foreign service and have it counted as qualifying service, or (2) not to pay the contribution and not have the service counted.",
             GREEN,
             "He has an option. Either he pays pension contribution for that foreign service and the service counts, or he does not pay and the service does not count."),
            ("THE REFUND",
             "If he chooses not to count it, the contributions he already paid are refunded.",
             "Rule 29 (R29-REFUND): if the servant opts not to have the service counted, the contributions already paid by him are refunded to him.",
             ORANGE,
             "If he chooses not to have the service counted, the contributions he has already paid are refunded to him."),
            ("THE TRAP",
             "It is the servant's option, not a decision of the Government or the department.",
             "Trap (ADD-B2-3): the door in Rule 29 is in the Government servant's hand, not the Government's. It is not an administrative decision. Q: who chooses? A: the Government servant.",
             RED,
             "Be careful, this is the trap. The choice belongs to the Government servant, not to the department. It is not an administrative decision."),
        ],
        "hook": "REMEMBER: Rule 29 = the servant's option: pay and count, or don't pay and get a refund!",
        "hook_say": "Remember: under Rule 29 it is the servant's option: pay and count, or do not pay and get the contributions refunded.",
        "covers": ["R29", "R29-REFUND"],
    },
    {
        "id": "c02_24_rule30_verification_triggers",
        "chapter": "CHAPTER 24 • RULE 30(1)-(2): VERIFYING QUALIFYING SERVICE AND FORMAT 4",
        "title": "RULE 30 (1)-(2) — WHEN SERVICE IS VERIFIED, AND BY WHOM",
        "accent": PINK, "badge": "RULE 30(1)-(2)",
        "q": "When must qualifying service be verified, who does it, and how is it communicated?",
        "q_say": "Sir, when must qualifying service be verified, who does it, and how is it communicated?",
        "boxes": [
            ("THE TWO TRIGGERS",
             "After 18 years of service, and again when 5 years remain before superannuation.",
             "Rule 30(1) (close restatement): the service is verified after the Government servant completes 18 years of service, and again when five years remain before the date of superannuation (R30(1), LIMIT-R30-18YRS, LIMIT-R30-5YRS). The source says 'on each occasion'; a summarising tool reading the staffnews book PDF later quoted it as the opening words of Rule 30(1), but the Gazette was not read, so treat the phrase as likely but not Gazette-confirmed (R30-ON-EACH-OCCASION); the two triggers themselves are confirmed. Superannuation means retirement on reaching the age of retirement.",
             SKY,
             "Let us take the rule first. Qualifying service is verified at two points: after the Government servant completes eighteen years of service, and again when five years remain before superannuation, which is retirement on reaching the age of retirement. The source says the check is done on each occasion. A summary of the Rules book shows that phrase, but we have not read the Gazette, so treat it as likely, not confirmed."),
            ("WHO AND HOW",
             "The Head of Office, with the Accounts Officer, verifies and tells the servant in Format 4.",
             "Rule 30(1) (close restatement): the Head of Office, in consultation with the Accounts Officer, verifies the service, determines the qualifying service and communicates it in Format 4 (R30(1), FORMAT-4). Rule 30(2): the Head of Office follows the procedure of Rule 57(1)(a) (R30(2)); Rule 57 was amended by G.S.R. 410(E) of 2024, which introduced Form 6-A, so check the current Rule 57. The source did not give 30(2).",
             GREEN,
             "Who does it? The Head of Office, in consultation with the Accounts Officer, verifies the service, works out the qualifying service and communicates it in Format 4. Sub-rule 2 says the Head of Office follows the procedure in Rule 57, clause 1, sub-clause a. Rule 57 was amended in 2024 and introduced Form 6-A, so check the current Rule 57. The source did not give sub-rule 2."),
            ("REAL EXAMPLE",
             "Lata joined 01.07.2005: first check at 18 years on 01.07.2023. If she retires on 30.06.2035, the second check falls on 30.06.2030.",
             "Example (invented, R30-EX1; superannuation date assumed): Lata, a senior assistant, joined on 01.07.2005. Eighteen years are complete on 01.07.2023, which is the first verification, and Format 4 goes to her. If her superannuation is on 30.06.2035, five years before is 30.06.2030, the second verification, after which the two records are matched. Q: what is Format 4? A: the format in which the Head of Office tells the servant the verified qualifying service.",
             ORANGE,
             "Here is a real example. Lata, a senior assistant, joined on first July 2005. Her eighteen years are complete on first July 2023, so the first verification falls then, and she gets Format 4. Assume she retires on thirtieth June 2035. Five years before is thirtieth June 2030, so the second verification falls then, and the two records are matched."),
            ("THE TRAP",
             "Two triggers, not one. A verification is a duty on the office, not a favour on request.",
             "Traps: (1) there are two triggers, 18 years and 5 years before superannuation; (2) the communication is in Format 4, not in Form 6-A (a different document, Rule 57); (3) 'on each occasion' is likely but not Gazette-confirmed. The source's later remark that the whole scheme leans on service-book entries (BONUS-26) is practical advice, not rule text.",
             RED,
             "Be careful, this is the trap. There are two triggers, not one. The certificate to the servant is in Format 4; Form 6-A is a different document under Rule 57. And the phrase on each occasion is likely, but not yet Gazette-confirmed."),
        ],
        "hook": "REMEMBER: verify at 18 years and at 5 years before retirement • Head of Office with Accounts Officer • Format 4!",
        "hook_say": "Remember: verify at eighteen years and again five years before retirement, by the Head of Office with the Accounts Officer, and communicate in Format 4.",
        "covers": ["R30(1)", "FORMAT-4", "LIMIT-R30-18YRS", "LIMIT-R30-5YRS", "R30(2)", "R30-EX1", "R30-ON-EACH-OCCASION"],
    },
    {
        "id": "c02_25_rule30_finality_report",
        "chapter": "CHAPTER 25 • RULE 30(3)-(5): SPECIAL EVENTS, FINALITY AND THE 31 JANUARY REPORT",
        "title": "RULE 30 (3)-(5) — EXTRA OCCASIONS, FINAL VERIFICATION, YEARLY REPORT",
        "accent": SKY, "badge": "RULE 30(3)-(5)",
        "q": "Beyond the two fixed checks, when else is verification done, and is it final?",
        "q_say": "Sir, apart from the two fixed checks, when else is verification done, and is it final?",
        "boxes": [
            ("EXTRA EVENTS: 30(3)",
             "Verification also on transfer from a temporary department, closure of a department, or a post declared surplus.",
             "Rule 30(3) (close restatement): verification may also be done on (i) transfer from a temporary department, (ii) closure of a department, or (iii) a post being declared surplus (R30(3)). A surplus post is one no longer needed.",
             SKY,
             "Let us take sub-rule 3. Verification is also done on three special events: transfer from a temporary department, closure of a department, or the post being declared surplus, which means it is no longer needed."),
            ("FINAL: 30(4)",
             "A verification is final. It is reopened only if a later rule or order changes the conditions for qualifying.",
             "Rule 30(4) (close restatement): the verification, once done, is final and is not reopened, except when a later rule or order changes the conditions for service to qualify (R30(4)). Q: is verification final? A: yes, subject to that one exception.",
             GREEN,
             "Sub-rule 4 makes the verification final. It is reopened only if a later rule or order changes the conditions for service to qualify. That one exception, and nothing else."),
            ("YEARLY REPORT: 30(5)",
             "By 31 January each year, a report to the Secretary of the Administrative Ministry: who was due a certificate, who got one, and why not for the rest.",
             "Rule 30(5) (close restatement): by 31 January each year (TL-31JAN), a report to the Secretary of the Administrative Ministry: the Government servants due to receive a certificate under Rule 30(1) in the previous calendar year, those who actually received it, and the reasons for the cases where it was not given (R30(5)).",
             ORANGE,
             "Sub-rule 5 is a yearly report. By thirty-first January each year, a report goes to the Secretary of the Administrative Ministry, saying who was due a certificate in the previous calendar year, who actually received it, and the reasons for the others."),
            ("THE TRAP",
             "Final does not mean never: a changed rule or order reopens it. And the report date is 31 January, for the PREVIOUS calendar year.",
             "Traps: (1) 'final' has one exception, a later change in rules or orders about conditions of qualifying (R30(4)); (2) the report is due by 31 January and covers the previous calendar year (R30(5), TL-31JAN); (3) Rule 30(2) refers to Rule 57, which was amended in 2024.",
             RED,
             "Be careful, this is the trap. Final does not mean never: a later change in rules or orders can reopen it. And the report is due by thirty-first January, covering the previous calendar year."),
        ],
        "hook": "REMEMBER: 30(3) three events • 30(4) final • 30(5) report by 31 January!",
        "hook_say": "Remember: three special events, verification is final unless the rules change, and the report goes to the Secretary by thirty-first January.",
        "covers": ["R30(3)", "R30(4)", "R30(5)", "TL-31JAN", "R30-EX1"],
    },
    {
        "id": "c02_26_sep2025_guidelines",
        "chapter": "CHAPTER 26 • THE SEPTEMBER 2025 DoPPW GUIDELINES AND RULE 30",
        "title": "O.M. 4/35/2024-P&PW(D)/10377 — MAKING RULE 30 A MONITORED DUTY",
        "accent": RED, "badge": "O.M. SEPT 2025",
        "q": "How do the 2025 DoPPW guidelines strengthen the Rule 30 verification chain?",
        "q_say": "Sir, how do the 2025 DoPPW guidelines strengthen the Rule 30 verification chain?",
        "boxes": [
            ("THE O.M.",
             "DoPPW O.M. No. 4/35/2024-P&PW(D)/10377: comprehensive guidelines for timely payment of retirement dues and issue of PPOs. Month: Sept 2025; exact day unreadable.",
             "Office Memorandum No. 4/35/2024-P&PW(D)/10377 of the Department of Pension and Pensioners' Welfare, 'Comprehensive Guidelines for timely payment of retirement dues (pension and pensionary dues) and issue of Pension Payment Orders (PPOs)'. Number and subject confirmed from the PDF read (OM-SEP2025-4/35/2024-10377). UNVERIFIED (OM-SEP2025-DATE): month Sept 2025 taken from the PDF path only; the day was illegible, so do not give a full date. A PPO is the order that authorises the pension.",
             SKY,
             "Let us take the O.M. This is DoPPW Office Memorandum number 4 slash 35 slash 2024 hyphen P and PW bracket D slash 10377, called comprehensive guidelines for timely payment of retirement dues and issue of Pension Payment Orders. A PPO is the order that authorises the pension. The month is September 2025, but the exact day was unreadable, so we give no full date."),
            ("HEAD OF DEPARTMENT DUTY",
             "The HoD ensures verification certificates at 18 years and 5 years before retirement, with a compliance report to the Secretary by 31 January.",
             "Section F(g) of the O.M. (OM-SEP2025-HOD-VERIF): the Head of Department is to ensure that verification certificates of qualifying service are issued at 18 years of service and five years before retirement, and a compliance report goes to the Secretary of the Ministry or Department by 31 January each year. Ties to the Rule 30(5) report.",
             GREEN,
             "The O.M. puts the duty on the Head of Department. He must ensure verification certificates are issued after eighteen years of service and five years before retirement, and a compliance report goes to the Secretary every year by thirty-first January. That ties directly to Rule 30."),
            ("RECORDS AND ESCALATION",
             "100 percent e-HRMS adoption; CAPF on the full Employee Payroll System; files returned more than twice are escalated; Nodal Officer meets PAOs monthly.",
             "Para 1(A): 100 percent e-HRMS adoption, and for CAPF personnel full adoption of the Employee Payroll System (EPS) (OM-SEP2025-EHRMS). Section F(c),(i): files returned more than twice for missing documents are escalated to a higher level (OM-SEP2025-ESCALATE). Section F(i): the Nodal Officer meets Pay and Accounts Offices every month (OM-SEP2025-NODAL). UNVERIFIED (OM-SEP2025-MANUAL): the source says electronically verified records will be preferred and manual records gradually discouraged; this was not seen in the parts of the O.M. read.",
             ORANGE,
             "Other points: one hundred percent e-HRMS adoption, which means digital service records, and for the central armed police forces the full Employee Payroll System. A pension file returned more than twice for missing documents is escalated higher. A Nodal Officer meets the Pay and Accounts Offices every month. The source also says manual records will be discouraged, but we did not see that in the pages we read."),
            ("THE LINK AND THE TRAP",
             "Rule 30 gives the trigger. The O.M. adds accountability. The PPO is due not later than two months before retirement (Rule 63(1)(a), quoted in the O.M., next batches).",
             "Link: Rule 30 is the statutory trigger (18 years and 5 years); the O.M. binds it to accountability (HoD duty, annual report, digitised records, escalation). The O.M. para 2 quotes Rule 63(1)(a): PPO not later than two months before retirement (R63(1)(a)-2MONTHS); Rule 63 itself is for Batch 5. Q: whom does the compliance report go to, and when? A: the Secretary of the Ministry or Department, by 31 January each year. Trap: it is an O.M. (administrative layer), not a rule amendment.",
             RED,
             "Be careful, this is the trap. This is an Office Memorandum, an administrative instruction, not an amendment to the Rules. Rule 30 gives the trigger, and the O.M. adds accountability. The same O.M. quotes Rule 63, that the PPO is due not later than two months before retirement; that rule belongs to a later part."),
        ],
        "hook": "REMEMBER: Rule 30 = the trigger • the O.M. = HoD duty and report to the Secretary by 31 January!",
        "hook_say": "Remember: Rule 30 gives the trigger, the O.M. makes the Head of Department responsible, and the compliance report goes to the Secretary by thirty-first January.",
        "covers": ["OM-SEP2025-4/35/2024-10377", "OM-SEP2025-DATE", "OM-SEP2025-HOD-VERIF", "OM-SEP2025-EHRMS", "OM-SEP2025-ESCALATE", "OM-SEP2025-NODAL", "OM-SEP2025-MANUAL", "R63(1)(a)-2MONTHS"],
    },
    {
        "id": "c02_27_authority_map_open_flags",
        "chapter": "CHAPTER 27 • CHAPTER III: WHO DECIDES WHAT, AND WHAT IS STILL UNCONFIRMED",
        "title": "THE AUTHORITY MAP FOR RULES 11-30 AND THE OPEN-FLAG LIST",
        "accent": ORANGE, "badge": "AUTHORITIES • FLAGS",
        "q": "Which authority acts in which rule, and which points are still not confirmed?",
        "q_say": "Sir, which authority acts in which rule, and which points are still not confirmed?",
        "boxes": [
            ("APPOINTING AUTHORITY",
             "Rule 21 (allow EOL), 26(1) and 26(5) (withdrawal), 27(2) (commute absence), 28(4)-(6) (condonation, hearing before refusal).",
             "Appointing authority (ADD-B2-3-AUTH-MAP-REST): Rule 21 proviso, Rule 26 (withdrawal of resignation), Rule 27(2), Rule 28(4) to (6). The source's list put Rule 23(2) here; the rule text names the Competent Authority, so Rule 23 is under the next card (ADD-B2-3-AUTH-MAP-23(2)).",
             SKY,
             "The appointing authority acts in Rule 21, to allow certain extraordinary leave to count; in Rule 26, on withdrawal of resignation; in Rule 27, sub-rule 2, to commute absence; and in Rule 28, sub-rules 4 to 6, on condonation, where a hearing is required before refusal."),
            ("OTHER AUTHORITIES",
             "Competent authority: Rule 23. Head of Department: Rule 22(4). Head of Office: Rule 26(3) and 30(1). Accounts Officer: consulted in 30(1). Government: Rule 22(2). The servant: Rule 29.",
             "Competent authority: Rule 23(2) and 23(3) (extent of suspension period, service book entry). Head of Department: Rule 22(4) (EOL when no leave is due). Head of Office: Rule 26(3) (service book entry) and Rule 30(1) (verification, with the Accounts Officer). Government: Rule 22(2) (training by order). Rule 29: the option is the Government servant's. Liability: Rule 13(3), the Centre; Rule 14(1)(c), the autonomous body by lump sum.",
             GREEN,
             "The competent authority acts in Rule 23. The Head of Department acts in Rule 22, sub-rule 4. The Head of Office acts in Rule 26 sub-rule 3 and in Rule 30, with the Accounts Officer. The Government decides in Rule 22 sub-rule 2. In Rule 29 the choice is the servant's. On liability, the Centre pays in Rule 13 and the autonomous body pays a lump sum in Rule 14."),
            ("STILL NOT CONFIRMED",
             "Now closed: Rule 14(2), Rule 15 notifying authority, Rule 26(8), Rule 30 'on each occasion'. Still open: Gazette wording, Sept 2025 O.M. date, G.S.R. 410(E) date.",
             "Flag audit of 24.10.2026, after reading the whole of Chapter III. CLOSED (the text is now read, so the flag is removed): Rule 14(2) reciprocal arrangement; the Explanation to Rule 14; the notifying authority and scheme name in Rule 15; Rule 26(8) (resignation for Rule 35 or 36); the words on each occasion in Rule 30(1); Rule 20(3) and Rule 30(2). STILL OPEN: (1) every rule is a close restatement, not the Gazette PDF or India Code text; (2) the exact day of the Sept 2025 DoPPW O.M.; (3) the effective date of G.S.R. 410(E), 16.11.2024 on secondary sites against 13.11.2024 on a 120-day count; (4) the 1993 O.M. number and date behind Rule 15; (5) the six-month method used in the Rule 21 example; (6) the source's glosses R11-INTERRUPTION-DEF, R12-BONUS13-CPF and R27-MNEMONIC, which are teaching devices, not rule text. Flags that belong to Batch 1 (Rules 4, 6 and 7) stay there: ADD-B2-3-OPENFLAGS-B1.",
             RED,
             "Now the honest flag list, revised after our clause by clause audit. Several old flags are now closed, because we read the full chapter text. Rule 14 sub-rule 2 is taught. The Explanation to Rule 14 is taught. The notifying department in Rule 15 is taught. Rule 26 sub-rule 8 and the words on each occasion in Rule 30 are confirmed. What stays open is this. All rule wording here is a close restatement, not the Gazette text. The exact day of the 2025 O.M. is not legible. The effective date of the 2024 notification is unsettled. And the six month method in our Rule 21 example is an assumption.",),
            ("CROSS-LINK AND CURRENCY",
             "Rule 37 comes next. 2025 Explanation applies Rules 7, 8, 41 and 44(5) to PSU-absorbed employees. A 2026 Rule 37(7) proviso is for the next batch.",
             "Cross-link: G.S.R. 340(E) of 22.05.2025 amends Rule 37 only; its Explanation applies Rules 7, 8, 41 and 44(5) analogously to PSU-absorbed employees (GSR-340E). A 2026 amendment, G.S.R. 775(E) (about 7 Sept 2026, date unclear, seen on a re-hosted PDF, not the Gazette), adds a proviso to Rule 37(7) for ex-Ordnance Factory Board employees who do not opt for DPSU absorption (deemed deputation until retirement). It lies outside Rules 11 to 30. Flags for ledger items that were carried to Batch 1: ADD-B2-3-OPENFLAGS-B1.",
             BLUE,
             "A cross-link for later. The 2025 amendment to Rule 37 applies Rules 7, 8, 41 and 44, sub-rule 5, to employees absorbed into public sector undertakings. A 2026 amendment, G.S.R. 775(E), adds a proviso to Rule 37 for ex-Ordnance Factory Board employees. We saw it only on a re-hosted PDF, so it is for the next part and unconfirmed."),
        ],
        "hook": "REMEMBER: know the actor in each rule — appointing, competent, HoD, Head of Office!",
        "hook_say": "Remember: always know which authority acts in each rule, appointing authority, competent authority, Head of Department or Head of Office.",
        "covers": ["ADD-B2-3-AUTH-MAP-REST", "ADD-B2-3-AUTH-MAP-23(2)", "ADD-B2-3-OPENFLAGS-B1", "GSR-340E"],
    },
    {
        "id": "c02_28_decision_chain",
        "chapter": "CHAPTER 28 • DECISION CHAIN: DOES THIS SERVICE COUNT?",
        "title": "FOUR STEPS TO DECIDE IF A STRETCH OF SERVICE COUNTS",
        "accent": GREEN, "badge": "DECISION CHAIN",
        "q": "Given a stretch of earlier service, how do we decide step by step if it counts?",
        "q_say": "Sir, given a stretch of earlier service, how do we decide step by step whether it counts?",
        "flow": "countchain",
        "boxes": [
            ("STEP 1: ANCHOR AND START",
             "Rule 11 and 12: duties and pay regulated; substantive anchor with no break; not before 18.",
             "Check Rule 11 (start, anchor, age 18) and Rule 12 (duties and pay both regulated by Government). Is there a substantive appointment after any officiating or temporary stretch, with no break?",
             SKY,
             "Step one: check the start and the anchor. Are duties and pay both regulated by Government? Is there a substantive appointment after any officiating or temporary stretch with no break, and is it after age eighteen?"),
            ("STEP 2: WHICH ROUTE?",
             "State 13, body 14, temp status 15, probation 16, apprentice 17, contract 18, civil pensioner 19, military 20, leave 21, training 22, suspension 23, international 29.",
             "Pick the route: Rules 13 to 23 and 29; check the 31.12.2003 line, the percentage (Rule 15: 50 percent), refunds (Rules 18, 19, 20) and instalments (36).",
             BLUE,
             "Step two: pick the route. State, autonomous body, temporary status, probation, apprentice, contract, re-employed pensioner, military, leave, training, suspension or international organisation. For each, check the date line, the percentage and any refund."),
            ("STEP 3: ANY LOSS EVENT?",
             "Dismissal or removal (24), resignation (26), interruption (27): past service can be forfeited.",
             "Check for loss events: Rule 24 (dismissal, removal), Rule 26(1) (resignation), Rule 27(1) (interruption).",
             RED,
             "Step three: look for a loss event. Dismissal or removal under Rule 24, resignation under Rule 26, or an interruption under Rule 27. Any of these can wipe out the earlier service."),
            ("STEP 4: SAVE AND PROVE",
             "Saves: 25, 26(2), 27 exceptions, 28. Proof: Rule 30, Format 4, at 18 years and 5 years before retirement.",
             "Check the saving tools: Rule 25 (reinstatement), Rule 26(2), (7), Rule 27(1)(a)-(e), 27(2), Rule 28. Then proof: Rule 30 verification in Format 4 at 18 years and five years before superannuation, with the 31 January report. Three questions in one line: does it count (Rules 11-23, 25, 27-30)? Did I lose it (24, 26)? Can I get it back (25, 28, 27(2))?",
             GREEN,
             "Step four: see what saves it and then prove it. Reinstatement, permitted resignation, the exceptions in Rule 27 and condonation in Rule 28. Then the Head of Office verifies in Format 4. In short: does it count, did I lose it, can I get it back."),
        ],
        "hook": "REMEMBER: anchor, route, loss, save and prove!",
        "hook_say": "Remember: check the anchor, pick the route, look for a loss event, then see what saves it and prove it.",
        "covers": ["CH3-STRUCTURE", "R11-MAIN", "R12-MAIN"],
    },
    {
        "id": "c02_29_table_counting_routes",
        "chapter": "CHAPTER 29 • REVISION TABLE 1: EVERY COUNTING ROUTE IN RULES 11 TO 23 AND 29",
        "title": "TABLE 1 — WHICH SERVICE COUNTS, AND ON WHAT CONDITION",
        "accent": SKY, "badge": "REVISION • TABLE",
        "layout": "table", "col1": "RULES", "col2": "WHAT THEY DECIDE, IN SIMPLE ENGLISH", "lab_w": 430,
        "q": "Put the whole chapter on one table: which service counts, and what must be true for it?",
        "q_say": "Sir, can we have the whole chapter on one table, so I can see every counting route at once?",
        "intro": ("Let us revise, and from here the screen changes shape. Instead of cards, you will see the rows of a revision table, "
                  "laid out the way a printed revision sheet is laid out. This first table gathers every rule that gives credit."),
        "rows": [
            ("RULES 11 • 12 — START",
             "Charge of the first post starts the clock; officiating or temporary needs a substantive post with no break; nothing before age 18. Duties AND pay regulated by Government.",
             SKY,
             "Rows one and two give the foundation. Rule 11 starts the clock on the day he takes charge of the first post. If that post was officiating or temporary, a substantive post must follow with no break, and nothing before the age of eighteen counts, except military service under Rule 20. Rule 12 adds the control test: duties and pay must both be regulated by the Government, and the service must be paid from the Consolidated Fund of India or a Local Fund."),
            ("RULES 13 • 14 — TRANSFER",
             "State or autonomous body service, appointed by 31.12.2003, proper permission, no break, body pays a lump sum. A PSU, bank or financial institution never counts.",
             GREEN,
             "Row three covers the two transfers. Under Rule 13, State service from a pensionable establishment counts on permanent transfer or on resignation with proper permission, and the Central Government bears the cost. Under Rule 14, service in an autonomous body counts if the body's scheme is similar, permission is proper, the four conditions are met, and the body pays a lump sum worked out on the commutation table of 1981. But sub-rule 3 of Rule 14 shuts out a public sector undertaking, a nationalised bank and a financial institution."),
            ("RULES 15 • 16 • 17",
             "Temporary status of a casual labourer: 50 percent only. Probation: counts once confirmed. Apprentice: nil, except Subordinate Accounts Service.",
             ORANGE,
             "Row four is the shortest trio. Rule 15 gives just fifty percent of the service rendered in temporary status, where the status came by the end of 2003 and regularisation followed. Rule 16 counts probation when confirmation follows. Rule 17 gives nothing at all for apprentice service, except the Subordinate Accounts Service apprentice in the Audit or Defence Accounts Department."),
            ("RULES 18 • 19 • 20 — REFUND",
             "Contract before 31.12.2003 with the CPF share refunded; earlier civil service of a re-employed pensioner; military service. Refund in at most 36 instalments.",
             RED,
             "Row five holds the three refund routes. Rule 18 counts contract service before a regular appointment by the end of 2003, provided the Government share in the contributory provident fund is refunded. Rule 19 counts the earlier civil service of a re-employed pensioner, and Rule 20 counts military service. All three need the money settled, the refund may run for at most thirty-six monthly instalments, and the cap in sub-rule 5 of Rule 19 has no twin in Rule 20."),
            ("RULES 21 • 22 • 23 • 29",
             "Leave with leave salary and medical EOL; Group C training; suspension only if exonerated or minor penalty AND wholly unjustified; foreign service by option.",
             PINK,
             "Row six closes the credit side. Rule 21 counts all leave with leave salary and extraordinary leave on a medical certificate. Rule 22 counts departmental training before a Group C appointment. Rule 23 counts suspension only if he is fully exonerated or gets a minor penalty, and the suspension is held wholly unjustified. Rule 29 lets the servant opt to count foreign service by paying the pension contributions."),
        ],
        "footer": "CLASSIC UPSC TRAP: a route counts only when its own condition is met - no anchor, no credit, and a PSU is never an autonomous body!",
        "hook": "REMEMBER: five rows hold every counting route in the chapter!",
        "hook_say": "Remember the five rows of Table one: start and control, State and body, status and probation, the refund routes, and leave, training, suspension and foreign service.",
    },
    {
        "id": "c02_30_table_loss_save_prove",
        "chapter": "CHAPTER 30 • REVISION TABLE 2: LOSS, SAVE AND PROVE IN RULES 24 TO 30",
        "title": "TABLE 2 — WHAT IS FORFEITED, WHAT IS SAVED, AND WHAT MUST BE PROVED",
        "accent": RED, "badge": "REVISION • TABLE",
        "layout": "table", "col1": "RULES", "col2": "WHAT THEY DO TO PAST SERVICE", "lab_w": 430,
        "q": "Which events take past service away, which save it, and who finally certifies it?",
        "q_say": "Sir, and the other side of the chapter? What takes service away, what saves it, and who proves it in the end?",
        "rows": [
            ("RULE 24 • 25 — LOSS, REPAIR",
             "Dismissal or removal forfeits past service; compulsory retirement is not named. Reinstated, he counts it again; the gap only if regularised as duty or leave.",
             RED,
             "Table two opens with loss and repair. Rule 24 is short and severe: dismissal or removal entails forfeiture of past service, and compulsory retirement is not named there. Rule 25 repairs: reinstated on appeal or review, he counts his past service again, but the gap, and any suspension in it, count only where the very authority that reinstated him regularises that period as duty or leave by a specific order."),
            ("RULE 26 — RESIGNATION",
             "Resignation forfeits, unless withdrawn in the public interest or made with proper permission for another qualifying post. 90 days; never for a private company.",
             ORANGE,
             "Row two, Rule 26, resignation. Resignation forfeits past service unless it is withdrawn in the public interest, or was submitted with proper permission to take up another Government appointment where service qualifies. Withdrawal needs four conditions, including an absence of not more than ninety days, and it is barred where the resignation was to join a private commercial company."),
            ("RULE 27 — INTERRUPTION",
             "Interruption forfeits, except (a) authorised leave, (b) certain unauthorised absence, (c) specified suspension, (d) public-interest transfer, (e) joining time. 27(2): commutation.",
             BLUE,
             "Row three, Rule 27, interruption. An interruption forfeits past service except in five cases: authorised leave; unauthorised absence in continuation of authorised leave while the post is not substantively filled; suspension followed by reinstatement, or death, permitted retirement or superannuation during suspension; transfer to non-qualifying service in the public interest; and joining time. Sub-rule 2 lets the appointing authority commute unauthorised absence into extraordinary leave, retrospectively."),
            ("RULE 28 — CONDONATION",
             "A gap between two civil spells is condoned automatically if the service book is silent. Never after resignation, dismissal, removal or strike; the gap never counts.",
             PINK,
             "Row four, Rule 28, condonation. Where the service book says nothing to the contrary, a gap between two spells of civil service is condoned automatically and the earlier service stays qualifying, and service paid out of Defence Services Estimates or Railway Estimates is included. But this never applies to a gap caused by resignation, dismissal, removal or participation in a strike, and the gap itself never counts."),
            ("RULE 30 — PROOF",
             "Head of Office with the Accounts Officer verifies at 18 years and at five years before superannuation, in Format 4; final. Report to the Secretary by 31 January.",
             SKY,
             "Row five, Rule 30, proof. The Head of Office, in consultation with the Accounts Officer, verifies the service and communicates the qualifying service in Format 4, on each occasion after eighteen years of service and again when five years are left before superannuation. That verification is final unless a change in the rules or orders requires a fresh look, and a report goes to the Secretary by thirty-first January every year."),
        ],
        "footer": "CLASSIC UPSC TRAP: Rule 28 condones the interruption and saves the earlier service, but the gap itself never becomes qualifying service!",
        "hook": "REMEMBER: lose (24, 26, 27), save (25, 26(2), 27(1), 28), prove (30)!",
        "hook_say": "Remember the second table: loss in Rules 24, 26 and 27, rescue in Rules 25, 26 sub-rule 2, the five exceptions in Rule 27 and condonation in Rule 28, and proof in Rule 30.",
    },
    {
        "id": "c02_31_chart_how_much_counts",
        "chapter": "CHAPTER 31 • BAR CHART: HOW MUCH OF EACH KIND OF SERVICE IS COUNTED",
        "title": "CHART — THE SHARE OF SERVICE THAT COUNTS, RULE BY RULE",
        "accent": GREEN, "badge": "BAR CHART • SHARE COUNTED",
        "layout": "chart",
        "q": "If the service counts, does the whole period count, or only a part of it?",
        "q_say": "Sir, when a kind of service does count, is it the whole period, or only some percentage of it?",
        "intro": ("A chart answers the question that prose hides: how much. Each bar is one route, and the length of the bar is the share of that service "
                  "that becomes qualifying service. Full bars take the whole period. One half bar is Rule 15. Empty bars give nothing at all."),
        "rows": [
            ("Rule 16 • probation, then confirmation", 100, GREEN,
             "Rule 16 is a full bar. Once confirmation follows, the whole period on probation counts, in the same post or in another post."),
            ("Rule 21 • leave with leave salary", 100, SKY,
             "Rule 21 is a full bar. All leave for which leave salary is payable counts, and so does extraordinary leave granted on a medical certificate."),
            ("Rule 18 • contract, CPF share refunded", 100, BLUE,
             "Rule 18 is a full bar with a price. The whole contract period counts if he was appointed to a covered post by the end of 2003 without a break, and refunded the Government share in the provident fund."),
            ("Rule 19 or 20 • earlier service, refunded", 100, ORANGE,
             "Rules 19 and 20 are full bars once the money is settled. The earlier civil or military service counts in full only after the pension and gratuity already taken are refunded, or the option to stop drawing them is exercised."),
            ("Rule 15 • temporary status, casual labour", 50, YELLOW,
             "Rule 15 is the only half bar in the chapter. Fifty percent of the service rendered in temporary status counts, provided the status was conferred by the end of 2003 and regularisation followed."),
            ("Rule 17 • apprentice service", 0, PINK,
             "Rule 17 is an empty bar. Apprentice service counts for nothing, with two narrow exceptions, a Subordinate Accounts Service apprentice in the Indian Audit and Accounts Department or the Defence Accounts Department."),
            ("Rule 14(3) • PSU or nationalised bank", 0, RED,
             "Rule 14 sub-rule 3 is an empty bar. Service in a public sector undertaking, including a nationalised bank or financial institution, before joining the Central Government never becomes qualifying service."),
            ("Rule 27 • the interruption itself", 0, SKY,
             "The gap itself is always an empty bar. Even where Rule 27 saves the past service, and even where Rule 28 condones the interruption, the period of the gap does not count as qualifying service."),
        ],
        "footer": "CLASSIC UPSC TRAP: a rule can save the PAST service and still give nothing for the gap - check both bars, not one!",
        "hook": "REMEMBER: one half bar (Rule 15), three empty bars (17, 14(3), the gap), everything else full!",
        "hook_say": "Remember the chart: Rule 15 is the only half bar, Rules 17, 14 sub-rule 3 and the gap itself are empty bars, and every other counting rule takes the full period.",
    },
    {
        "id": "c02_32_table_provisos_explanations",
        "chapter": "CHAPTER 32 • REVISION TABLE 3: EVERY PROVISO AND EXPLANATION IN ONE PLACE",
        "title": "TABLE 3 — THE FINE PRINT OF CHAPTER III, CLAUSE BY CLAUSE",
        "accent": ORANGE, "badge": "REVISION • FINE PRINT",
        "layout": "table", "col1": "FINE PRINT", "col2": "WHAT THE PROVISO OR EXPLANATION ACTUALLY SAYS", "lab_w": 430,
        "q": "Where does a senior examiner look first? Which provisos and Explanations carry the marks?",
        "q_say": "Sir, where do the marks actually sit? Which provisos and Explanations do examiners love?",
        "rows": [
            ("RULE 11 — TWO PROVISOS",
             "Officiating or temporary service must be followed without interruption by substantive appointment; nothing before 18 counts except military service under Rule 20.",
             SKY,
             "Rule 11 carries two provisos in one breath. The first is the anchor: officiating or temporary service must be followed without interruption by a substantive appointment, in the same or in another service or post. The second is the age line: service before eighteen does not count, except military service counted for civil pension under Rule 20."),
            ("RULES 12 • 13 — EXPLAINED",
             "Service means paid from the Consolidated Fund of India or a Local Fund, excluding an establishment without a non-contributory scheme. Proper permission: prior permission taken, order reciting it.",
             GREEN,
             "Rule 12 has an Explanation that defines service: service under Government, paid from the Consolidated Fund of India or a Local Fund, and it excludes service in an establishment that has no non-contributory pension scheme, unless the Government treats it as qualifying. Rule 13 has an Explanation that defines proper permission: he applied with the State's previous permission, and the State's order says he resigns to join with proper permission."),
            ("RULE 14 — 14(2) AND EXPL.",
             "Four conditions (a) to (d), lump sum on the 1981 commutation table. 14(2): a State-level body is bound by the reciprocal arrangement. Explanation: two limbs of permission.",
             ORANGE,
             "Rule 14 is the heaviest rule of the chapter. Four conditions in sub-rule 1, ending with the lump sum calculated on the 1981 commutation table. Sub-rule 2 makes that condition binding on an autonomous body under a State Government through the reciprocal arrangement between the Centre and that State. And the Explanation defines proper permission from the body, both limbs together."),
            ("RULE 19(5) • 20 — MONEY",
             "19(5) caps the later benefit by the difference between combined benefits and what was granted. 20(5) has no cap; the three Explanations settle military service.",
             PINK,
             "Two fine-print clusters on money. Rule 19 sub-rule 5 caps the later pension or gratuity by the difference between the value of the combined service and the benefits already granted, worked out on the commutation table, and Rule 20 sub-rule 5 deliberately has no such cap. The three Explanations to Rule 20 settle the military cases, including service joined after thirty-first December 2003, which goes to the National Pension System."),
            ("RULES 26 • 27 • 28 — PROCESS",
             "EOL counts only if allowed at grant, for civil commotion or higher studies; entry within six months of retirement. 90 days; Rules 35 and 36 saved; refusal only after a hearing.",
             SKY,
             "The procedural fine print. Rule 21: extraordinary leave other than on a medical certificate counts only if the appointing authority allows it at the time of grant, for civil commotion or for higher scientific and technical studies, and the non-counting entry must be made at the time or at latest six months before superannuation. Rule 26 sub-rule 5 gives four conditions and ninety days, sub-rule 6 the private company bar, sub-rule 8 saves a resignation for Rules 35 and 36. Rule 27 sub-rule 2 permits retrospective commutation into extraordinary leave. Rule 28 allows refusal only in exceptional and grave circumstances, and after a hearing in person."),
        ],
        "footer": "CLASSIC UPSC TRAP: the Explanation to Rule 14 and sub-rule 2 of Rule 14 are new to most notes - quote the two limbs of proper permission!",
        "hook": "REMEMBER: the marks live in the provisos, the Explanations and the two limbs of proper permission!",
        "hook_say": "Remember Table three: the marks live in the fine print, the two provisos of Rule 11, the Explanations to Rules 12, 13, 14, 19, 20 and 21, and the procedural fine print of Rules 26, 27 and 28.",
    },
    {
        "id": "c02_33_panel_four_numbers",
        "chapter": "CHAPTER 33 • PANEL: THE FOUR NUMBERS THAT DECIDE CHAPTER III",
        "title": "FOUR NUMBERS, THREE SILENCES — THE CHAPTER AT A GLANCE",
        "accent": PINK, "badge": "SUMMARY PANEL", "lab_w": 340,
        "layout": "panel",
        "headers": [("31.12.2003", "the cut-off date", ORANGE),
                    ("50 PERCENT", "only Rule 15", GREEN),
                    ("36 INSTALMENTS", "Rules 19 and 20", SKY),
                    ("18 AND 5 YEARS", "the Rule 30 checks", PINK)],
        "q": "If I forget everything else, which four numbers and which silences still decide the answer?",
        "q_say": "Sir, if I forget everything else on the day of the exam, which numbers still decide the answer?",
        "intro": ("This last panel is built the way a revision slide should be built: four numbers across the top, then the habits that turn those numbers into marks. "
                  "Say each number out loud, then say what it controls."),
        "rows": [
            ("THE DATE",
             "Rules 13, 14, 15, 18, 19 and 20 all hinge on appointment or re-employment by 31.12.2003. The NPS starts on 01.01.2004.",
             ORANGE,
             "Number one, thirty-first December 2003. Six rules turn on it: State service, autonomous body service, temporary status, contract service, re-employed civil pensioners and military service. Miss the date and the whole answer falls. The National Pension System starts the next day, first January 2004."),
            ("THE HALF",
             "Rule 15 takes only 50 percent of temporary-status service. Every other counting rule takes the whole period.",
             GREEN,
             "Number two, fifty percent. Rule 15 is the only rule of the chapter that gives half. A casual labourer with temporary status by the end of 2003, later regularised, gets half of that stretch. Every other counting rule takes the whole period once its own condition is satisfied."),
            ("THE REFUND",
             "Rules 19 and 20: at most 36 monthly instalments, the first in the month after the option; counting revives only after the last one.",
             SKY,
             "Number three, thirty-six instalments. In Rules 19 and 20 the refund may be spread over at most thirty-six monthly instalments, the first falling in the month after the option, and the right to count revives only when the last rupee is paid. Remember the asymmetry too: sub-rule 5 of Rule 19 caps the later benefit, and sub-rule 5 of Rule 20 does not."),
            ("THE SILENCES",
             "Rule 21 silence: the leave counts. Rule 23 silence: the suspension does not. Rule 28 silence: the gap is forgiven.",
             YELLOW,
             "Habit one, read the silences. In Rule 21, if the service book has no entry, the extraordinary leave counts. In Rule 23, if the competent authority does not declare, the suspension does not count. In Rule 28, if the service book says nothing, the gap is condoned automatically. The same silence produces three opposite results."),
            ("THE CHECKS",
             "Rule 30: verification at 18 years and at five years before superannuation, in Format 4, and a report by 31 January.",
             BLUE,
             "Number four, eighteen and five. Rule 30 asks the Head of Office, with the Accounts Officer, to verify the service after eighteen years and again when five years remain before superannuation, and to communicate the result in Format 4. That verification is final unless a change in the rules reopens it, and the yearly report reaches the Secretary by thirty-first January."),
        ],
        "footer": "CLASSIC UPSC TRAP: 31.12.2003 is a cut-off for APPOINTMENT, not for retirement - and the gap never counts, even when the past service is saved!",
        "hook": "REMEMBER: one date, one half, one instalment limit, one pair of checks, three silences!",
        "hook_say": "Remember the panel: the date thirty-first December 2003, the half in Rule 15, the thirty-six instalments in Rules 19 and 20, the two checks in Rule 30, and the three silences that pull in three different directions.",
    },    {
        "id": "c02_34_recap",
        "chapter": "CHAPTER 34 • RECAP OF PART 2: RULES 11 TO 30",
        "title": "RECAP — KEY NUMBERS, TOP TRAPS AND CURRENCY NOTE",
        "accent": PINK, "badge": "PART 2 RECAP",
        "q": "In one chapter, what must I remember from Rules 11 to 30?",
        "q_say": "Sir, in one short recap, what must I remember from Rules 11 to 30?",
        "boxes": [
            ("KEY NUMBERS",
             "Age 18 • 31.12.2003 • 50 percent (Rule 15) • 36 instalments • 90 days (Rule 26) • 6 months (Rule 21) • 18 years and 5 years (Rule 30) • 31 January.",
             "Key numbers: age 18 (Rule 11); 31.12.2003 (Rules 13, 14, 15, 18, 19, 20); 50 percent of temporary status service (Rule 15); at most 36 monthly instalments (Rules 19, 20), first from the month after the option; 90 days absence (Rule 26(5)); six months before superannuation for a late service-book entry (Rule 21); 18 years and five years before superannuation (Rule 30); 31 January report (Rule 30(5)). Forms: Format 4 (Rule 30). Also: Rule 27(1) has five exceptions (a) to (e); Rule 26 has eight sub-rules.",
             SKY,
             "Key numbers: age eighteen in Rule 11; thirty-first December 2003 in six rules; fifty percent in Rule 15; thirty-six instalments in Rules 19 and 20; ninety days in Rule 26; six months in Rule 21; eighteen years and five years in Rule 30; and thirty-first January for the report. Rule 27 has five exceptions, and Rule 26 has eight sub-rules."),
            ("TOP TRAPS",
             "Officiating needs an anchor • Rule 12 is AND • 19(5) limits, 20(5) does not • silence differs in Rules 21, 23, 28 • gap never counts • compulsory retirement not in Rule 24.",
             "Top traps: (1) officiating or temporary service needs a substantive anchor with no break; (2) Rule 12 limbs are AND; (3) Rule 14(3): PSU and nationalised bank service never counts; (4) Rule 15: only half; (5) Rule 19(5) limitation, Rule 20(5) none; (6) Rule 20 Explanation 1(ii) since 07.10.2022: refund required; (7) silence: Rule 21 counts, Rule 23 does not, Rule 28 condoned; (8) a gap never counts under Rules 25(2), 26(7), 28(3); (9) Rule 24 omits compulsory retirement; (10) Rule 26 has 8 sub-rules.",
             RED,
             "Top traps: officiating service needs an anchor; Rule 12 is AND; PSU service never counts; Rule 15 gives only half; nineteen five limits and twenty five does not; the 2022 change makes the refund compulsory; silence means different things in Rules 21, 23 and 28; a gap never counts; and compulsory retirement is not in Rule 24."),
            ("CURRENCY NOTE",
             "Only G.S.R. 770(E) of 2022 changed Chapter III. No later change found up to 21.10.2026, but the Gazette was not read. Wording here is a close restatement.",
             "Currency note: G.S.R. 868(E) of 20.12.2021 original; G.S.R. 770(E) of 07.10.2022 changed Rule 20 Explanation 1(ii) only; G.S.R. 410(E) of 16.07.2024 (effective date about mid-November 2024, unconfirmed) and G.S.R. 340(E) of 22.05.2025 do not amend Rules 11 to 30. No amendment to Rules 11 to 30 was found up to 21.10.2026, from search results only. Sept 2025 O.M. 4/35/2024-P&PW(D)/10377 read from a PDF, day unreadable. All Rule wording is a close restatement from secondary reproductions. Check the Gazette and the latest DoPPW O.M. for exam or live files.",
             ORANGE,
             "Currency note. Only G.S.R. 770(E) of 2022 changed anything in Chapter III. We found no later change up to twenty-first October 2026, but we did not read the Gazette itself. So every rule here is a close restatement. For an exam answer or a live file, check the Gazette and the latest DoPPW O.M."),
            ("NEXT PART",
             "Part 3 covers Chapter IV on emoluments (Rules 31-32) and Chapter V on the classes of pension (Rules 33-41).",
             "Next: Batch 3, Chapter IV (Emoluments, Rules 31 to 32) and Chapter V (Classes of pension, Rules 33 to 41). Revise first: the Rule 19 and Rule 20 comparison and the Rule 21 silence principle.",
             GREEN,
             "In the next part we move to Chapter 4, emoluments, which is the pay that goes into the pension calculation, in Rules 31 and 32, and Chapter 5, the classes of pension, in Rules 33 to 41. Before that, revise the Rule 19 and 20 comparison, and the silence principle of Rule 21."),
        ],
        "hook": "REMEMBER: count, lose, save, prove — and check the Gazette for exact words!",
        "hook_say": "Remember: count, lose, save and prove, and always check the Gazette for the exact words.",
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
           "Every row or card on screen is a short key-point; the full wording / examinable facts behind it are listed here.\n"
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

