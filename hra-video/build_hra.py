#!/usr/bin/env python3
"""
DoPT Technical Resignation & Lien - SIMPLE ENGLISH Q&A VIDEO MASTERCLASS COMPILER
=====================================================================================================
Scope: Full Consolidated DoPT O.M. No. DOPT-1669266628362 dated 24.11.2022 (Paras 2.1 to 5)
       16 chapters | 64 cards | Riya (student) asks one question per chapter, the teacher
       answers it card by card, and the chapter closes on a "trap / remember" strip.

SOURCES READ / CHECKED IN THIS BUILD:
  * DoPT O.M. No. DOPT-1669266628362 dated 24.11.2022 (Technical Resignation and Lien)
  * Ministry of Finance O.M. No. 3379-E.III(B)/65 dated 17.06.1965 (Technical formality & Pay protection)
  * DoPT O.M. No. 13/24/92-Estt(Pay-I) dated 22.01.1993 (Carry forward of leave)
  * DoPT O.M. No. 18011/1/86-Estt(D) dated 28.03.1998 (Lien definition & confirmation)
  * DoPT O.M. No. 8/4/70-Estt(C) dated 06.03.1974 (Retention of lien for 2/3 years)
  * DoPT Notification No. 28020/1/96-Estt(C) dated 09.02.1998 (Termination & transfer of lien)
  * Department of Pension & Pensioners Welfare O.M. No. 28/30/2004-P&PW(B) dated 26.07.2005 (Old Pension)

CHANGES VERSUS THE SOURCE (outdated / superseded / corrected):
  * None: All instructions are consolidated as per the latest 24.11.2022 compendium.

KEY FACTS:
  * Technical Resignation requires applying through proper channel; word 'Technical' not mandatory
    if conditions met (Para 2.1.1).
  * Pre-joining applications can qualify if intimated immediately on joining and accepted by
    authority (Para 2.1.2).
  * All unutilized leaves (including CCL) carry forward under Rule 9(2); 300 days EL/HPL cash
    equivalent on PSU absorption (Rule 39-D).
  * LTC: An employee resigning within 8 years of initial appointment gets fresh recruit LTC
    benefit for the remainder of 8 years (Para 2.3).
  * Pay Protection: Granted under MoF OM 17.06.1965 read with proviso to FR 22-B; draws
    presumptive pay under FR 9(24).
  * Seniority & Reversion: Substantive seniority protected, but time spent in the new department
    does NOT count toward promotion qualifying service in the parent cadre (Para 2.6).
  * Pre-2004 Entrants: Continue under CCS (Pension) Rules, 1972 on technical resignation to a
    pensionable establishment (Para 2.7).
  * Lien (FR 9(13)): Acquired on confirmation or completion of probation; can never be
    terminated if the employee is left without a lien on a permanent post (Para 3.4.1).
  * Retention of Lien: Maximum 2 years, extendable by 1 year (total 3 years) in exceptional
    unconfirmed cases (Para 3.3).
  * Joining Time (CCS Joining Time Rules 1979): Transfer TA is barred for temporary employees
    with under 3 years service (Para 3.6.3).

NOT VERIFIED (flagged on the cards - quote the official text in an answer sheet):
  * (none recorded)

-----------------------------------------------------------------------------------------------------
ENGINE REVISION NOTES (this revision changes presentation only - no rule content was altered)
  * TTS backend: edge-tts needs Microsoft's speech endpoint, which is unreachable from a
    restricted network. Narration is now pre-rendered with studio Indian-English voices and
    split into per-card audio by ANCHORED SILENCE ALIGNMENT (character-weighted prediction
    snapped onto real detected pauses), so every card still changes exactly on its own words.
  * Pronunciation layer rewritten for Indian English and applied in a strictly ordered pass:
    clause expansions run BEFORE bare acronym expansion, 'Para' -> 'Paragraph', 'yrs' -> 'years',
    'lien' -> 'lee-en', and spelled-out acronyms for CCS/DoPT/NPS/LTC/GPF/CCL/PSU etc.
  * Subtitles use length-weighted in-segment timing with readable 2-line chunks, colour-coded
    per speaker (teacher = white, Riya = cyan).
  * Added an opening title card, a spoken closing card, per-chapter MP4 export, a narration
    manifest dump, and a post-build A/V verification pass.
-----------------------------------------------------------------------------------------------------

Usage
    python3 build_technical_resignation.py --audit            # card-density check (no ffmpeg, no audio)
    python3 build_technical_resignation.py --dump-narration   # write narration/<...>.txt + manifest json
    python3 build_technical_resignation.py --align            # split studio_raw/ clips into per-card audio
    python3 build_technical_resignation.py --preview          # render slide images only
    python3 build_technical_resignation.py --build            # full render + mux (main + per-chapter mp4)
"""
import argparse
import json
import os
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

# ---------------------------------------------------------------------------------------------
# Canvas / layout constants
# ---------------------------------------------------------------------------------------------
W, H = 1920, 1080
ROOT = Path(__file__).resolve().parent
BUILD_DIR = ROOT / "work"
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
CLIPS_DIR = BUILD_DIR / "clips"
STUDIO_DIR = ROOT / "studio_raw"
NARR_DIR = ROOT / "narration"
OUT_STEM = "hra_masterclass"

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

# Pacing: extra air after a slide flips, so the eye lands before the words start.
# Tightened from the first cut (0.85/0.95/0.45/1.00/1.20) - the original gaps read as
# hesitation on a revision video, and this reclaims ~36s without touching the voice.
PAD_QUESTION = 0.32
PAD_HOOK = 0.38
PAD_ANSWER = 0.18
PAD_TITLE = 0.55
PAD_OUTRO = 0.70

TITLE_HEAD = "HOUSE RENT ALLOWANCE"
TITLE_SUB = "DoE O.M. No. 2/4/2022-E.II(B)  •  dated 30.12.2022"
TITLE_META = "Complete Masterclass  •  17 Chapters  •  Updated to October 2026"

COURSE_INTRO = (
    "Welcome to the complete masterclass on House Rent Allowance. We will walk through the "
    "consolidated instructions of the Department of Expenditure, dated the thirtieth of "
    "December, twenty twenty two, paragraph by paragraph. We will also flag, very clearly, "
    "where the printed rate is no longer the rate you actually draw today. Let us begin with "
    "Riya's first question."
)

COURSE_OUTRO = (
    "That brings us to the end of this masterclass. Keep three things in mind. First, House "
    "Rent Allowance follows your place of duty, not where you live. Second, the printed "
    "twenty four, sixteen and eight per cent is only the base rate; today you draw thirty, "
    "twenty and ten per cent. And third, the Eighth Pay Commission figures you see online are "
    "demands, not law. Keep revising, and see you in the next chapter."
)

# ---------------------------------------------------------------------------------------------
# INDIAN-ENGLISH PRONUNCIATION LAYER
# Order matters: specific clause expansions must run BEFORE bare acronym expansion, otherwise
# "FR 9(24)" becomes "F.R. 9(24)" and the clause rule can never match.
# ---------------------------------------------------------------------------------------------
_TTS_FIXES = [
    # --- 1. clause / rule references (most specific first) -----------------------------------
    (r"\bFR\s+(\d+)\s*\(\s*(\d+)\s*\)", r"F.R. \1 clause \2"),
    (r"\bF\.R\.\s*(\d+)\s*\(\s*(\d+)\s*\)", r"F.R. \1 clause \2"),
    (r"\bFR\s+(\d+)\s*-\s*([A-Za-z])\b", r"F.R. \1 \2"),
    (r"\bSR\s+(\d+)\s*\(\s*(\d+)\s*\)", r"S.R. \1 clause \2"),
    (r"\bS\.R\.\s*(\d+)\s*\(\s*(\d+)\s*\)", r"S.R. \1 clause \2"),
    (r"\bRule\s+(\d+)\s*\(\s*(\d+)\s*\)", r"Rule \1 sub rule \2"),
    (r"\bRule\s+(\d+)\s*-\s*([A-Za-z])\b", r"Rule \1 \2"),
    (r"\bPara\s+(\d+(?:\.\d+)*)", r"Paragraph \1"),
    (r"\bParas\b", "Paragraphs"),
    (r"\bPara\b", "Paragraph"),
    # --- 2. plain-English expansions ---------------------------------------------------------
    (r"\byrs\b\.?", "years"),
    (r"\byr\b\.?", "year"),
    (r"\bvs\.\b", "versus"),
    (r"\bapprox\.?", "approximately"),
    (r"\bw\.e\.f\.\b", "with effect from"),
    (r"\bi\.e\.\b", "that is"),
    (r"\be\.g\.\b", "for example"),
    (r"\bNo\.\s*(\d)", r"Number \1"),
    (r"&", " and "),
    # --- 3. the word exam candidates most often hear mis-pronounced --------------------------
    (r"\bliens\b", "lee enz"),
    (r"\blien\b", "lee en"),
    (r"\bLien\b", "Lee en"),
    # --- 4. acronyms -> spoken letters -------------------------------------------------------
    (r"\bPSUs\b", "public sector undertakings"),
    (r"\bPSU\b", "public sector undertaking"),
    (r"\bABs\b", "autonomous bodies"),
    (r"\bUPSC\b", "U.P.S.C."), (r"\bSSC\b", "S.S.C."), (r"\bCVC\b", "C.V.C."),
    (r"\bDoPT\b", "D.O.P.T."), (r"\bDOPT\b", "D.O.P.T."),
    (r"\bMoF\b", "Ministry of Finance"),
    (r"\bCCL\b", "child care leave"),
    (r"\bLTC\b", "L.T.C."),
    (r"\bTTA\b", "transfer T.A."),
    (r"\bTA\b", "T.A."),
    (r"\bHPL\b", "half pay leave"),
    (r"\bHRA\b", "H.R.A."),
    (r"\bGPF\b", "G.P.F."), (r"\bCPF\b", "C.P.F."),
    (r"\bNPS\b", "N.P.S."), (r"\bPRAN\b", "P.R.A.N."), (r"\bPRA\b", "P.R.A."),
    (r"\bEL\b", "earned leave"),
    (r"\bFR\b", "F.R."), (r"\bSR\b", "S.R."),
    (r"\bCPC\b", "C.P.C."), (r"\bRP\b", "revised pay"),
    (r"\bCCS\b", "C.C.S."),
    (r"\bOMs\b", "O.M.s"), (r"\bOM\b", "O.M."),
    # --- 4b. HRA / pay-commission vocabulary -------------------------------------------------
    (r"\bHRA\b", "H.R.A."),
    (r"\bDA\b", "D.A."),
    (r"\bCPC\b", "C.P.C."),
    (r"\bDoE\b", "D.O.E."),
    (r"\bMoD\b", "Ministry of Defence"),
    (r"\bMoR\b", "Ministry of Railways"),
    (r"\bIA&AD\b", "I.A. and A.D."),
    (r"\bUA\b", "U.A."),
    (r"\bTB\b", "T.B."),
    (r"\bDDO\b", "D.D.O."),
    (r"\bLIC\b", "L.I.C."),
    (r"\bNGO\b", "non-gazetted officer"),
    (r"\bRs\.?\s*", "rupees "),
    (r"\bkm\b", "kilometres"),
    # Office Memorandum file numbers: 1/1(i)/2026-E.II(B) -> "1 slash 1 sub one slash 2026 E two B"
    (r"-E\.II\(B\)", " E two B"),
    (r"E\.II\(B\)", "E two B"),
    (r"E\.IIB", "E two B"),
    (r"\(i\)", " sub one "),
    (r"\(ii\)", " sub two "),
    (r"\(iii\)", " sub three "),
    (r"/", " slash "),
    # --- 5. typography -----------------------------------------------------------------------
    (r"[\u2014\u2013\u2212]", ","),
    (r"\s+", " "),
]


def normalize_for_tts(text: str) -> str:
    """Deterministic text -> speech normalisation. Applied to BOTH the audio request and the
    subtitle track so what is spoken and what is read on screen never disagree."""
    for pat, rep in _TTS_FIXES:
        text = re.sub(pat, rep, text)
    return text.strip()



# ===============================================================================================
# SCENE DATA  (rule content - verified against the O.M., do not edit without re-checking)
# ===============================================================================================

SCENES = [
    {
        "id": "h01_scope_of_master_om",
        "chapter": "CHAPTER 1 \u2022 SCOPE OF APPLICATION",
        "title": "PARA A \u2014 WHOM DOES THIS MASTER O.M. ACTUALLY COVER?",
        "accent": SKY, "badge": "PARA A",
        "q": "Whom does the HRA compendium apply to, and who is left out?",
        "intro": ("Welcome to the complete masterclass on House Rent Allowance. We will walk through the "
                  "consolidated instructions of the Department of Expenditure, dated the thirtieth of "
                  "December, twenty twenty two, paragraph by paragraph. We will also flag, very clearly, "
                  "where the printed rate is no longer the rate you actually draw today. Let us begin with "
                  "Riya's first question."),
        "q_say": "Sir, before we start the rates, whom does this House Rent Allowance compendium actually apply to?",
        "boxes": [
            ("THE MASTER O.M.",
             "DoE O.M. 2/4/2022-E.II(B) dated 30.12.2022 consolidates and supersedes all earlier HRA instructions.",
             "Para A: These consolidated instructions issued by the Ministry of Finance, Department of Expenditure, "
             "supersede all earlier instructions on House Rent Allowance. They are the single governing reference "
             "as of the date of issue, and remained the newest HRA compendium on the Department's website when "
             "checked in October 2026.",
             SKY,
             "Let us begin with the document itself. This is Department of Expenditure Office Memorandum number "
             "2 slash 4 slash 2022 E two B, dated the thirtieth of December, twenty twenty two. It supersedes "
             "every earlier instruction on House Rent Allowance."),
            ("WHO IS COVERED",
             "All civilian employees of the Central Government, and civilian employees paid from the Defence Services Estimates.",
             "Para A: The compendium applies to all civilian employees of the Central Government. It also applies "
             "to civilian employees paid from the Defence Services Estimates, that is, civilian defence personnel "
             "borne on defence estimates rather than on civil estimates.",
             GREEN,
             "The compendium applies to all civilian employees of the Central Government. It also applies to "
             "civilian employees paid from the Defence Services Estimates."),
            ("THE FORGOTTEN GROUP",
             "The orders also apply to persons serving in the Indian Audit and Accounts Department.",
             "Para A: The orders also apply to persons serving in the Indian Audit and Accounts Department. This is "
             "the limb candidates most often omit, because the Audit and Accounts Department is headed by the "
             "Comptroller and Auditor General and is not a line Ministry.",
             ORANGE,
             "There is one group students often forget: these orders also apply to persons serving in the Indian "
             "Audit and Accounts Department."),
            ("THE TRAP: TWO EXCLUSIONS",
             "Ad hoc or personal-rate appointees (unless the order allows HRA); staff paid from contingencies \u2014 casual employees and labour.",
             "Para A: The compendium does not apply to employees appointed on ad hoc basis or on personal rates of "
             "pay, unless their terms of appointment specifically provide for grant of House Rent Allowance. It "
             "also does not apply to staff paid out of contingencies, that is, casual employees and labour.",
             RED,
             "Now the trap. Two groups are outside these rules: employees appointed on ad hoc or personal rates of "
             "pay, unless their appointment order specifically allows House Rent Allowance; and staff paid out of "
             "contingencies, that is casual employees and labour."),
        ],
        "hook": "REMEMBER: CIVILIANS + DEFENCE CIVILIANS + AUDIT & ACCOUNTS \u2014 BUT NOT AD HOC OR CONTINGENCY!",
        "hook_say": "Remember: the compendium covers all civilian Central Government staff, Defence civilians, and "
                    "Audit and Accounts Department staff, but excludes ad hoc and contingency paid employees.",
        "covers": ["PA"],
    },
    {
        "id": "h02_pay_and_family",
        "chapter": "CHAPTER 2 \u2022 PARAS 1.1 & 1.2: 'PAY' AND 'FAMILY'",
        "title": "PARAS 1.1\u20131.2 \u2014 HOW 'PAY' AND 'FAMILY' ARE DEFINED",
        "accent": GREEN, "badge": "1.1-1.2",
        "q": "Why do the definitions of 'pay' and 'family' matter so much?",
        "q_say": "Sir, the compendium defines pay and family. Why do those two definitions matter so much?",
        "boxes": [
            ("PAY MEANS PAY MATRIX LEVEL",
             "Pay = pay drawn in the prescribed Level in the Pay Matrix under the 7th Central Pay Commission.",
             "Para 1.1: Pay, for the purpose of computing House Rent Allowance, means the pay drawn in the "
             "prescribed Level in the Pay Matrix applicable to the Government servant under the Seventh Central "
             "Pay Commission. It is the matrix level, not the individual's total emoluments.",
             SKY,
             "Paragraph 1.1 is short but decisive. Pay, for calculating House Rent Allowance, means the pay drawn "
             "in the prescribed Level in the Pay Matrix under the Seventh Central Pay Commission."),
            ("WHAT IS EXCLUDED FROM PAY",
             "No other type of pay counts; special pay and similar additions stay out of the calculation.",
             "Para 1.1: No other type of pay is taken into account for computing House Rent Allowance. Special pay "
             "and similar additions are expressly excluded, so they do not inflate the HRA base.",
             GREEN,
             "And note the exclusion: no other type of pay is counted. Special pay, and similar additions, stay "
             "out of the House Rent Allowance calculation."),
            ("WHO COUNTS AS FAMILY",
             "Wife or husband, children, and other persons residing with and wholly dependent on the Government servant.",
             "Para 1.2: Family means the Government servant's wife or husband, his or her children, and other "
             "persons residing with and wholly dependent upon the Government servant.",
             ORANGE,
             "Now family. Paragraph 1.2 says family means the Government servant's wife or husband, children, and "
             "other persons residing with and wholly dependent upon him or her."),
            ("THE TRAP: THE Rs 9,000 TEST",
             "A relative with independent income above Rs 9,000 p.m. (including pension) is not treated as family.",
             "Para 1.2: A husband, wife, child or parent having an independent source of income is not treated as "
             "family for this purpose, unless that income, including pension and its benefits, does not exceed "
             "nine thousand rupees per month. Dependence is therefore tested by an income cut-off, not by "
             "relationship alone.",
             RED,
             "Here is the trap examiners love. A husband, wife, child or parent with an independent source of "
             "income is not treated as family, unless that income, including pension and its benefits, does not "
             "exceed nine thousand rupees per month."),
        ],
        "hook": "REMEMBER: PAY = PAY MATRIX LEVEL ONLY \u2022 FAMILY CUT-OFF Rs 9,000 PER MONTH!",
        "hook_say": "Remember: pay for House Rent Allowance is the Pay Matrix level alone, and the family income "
                    "cut off is nine thousand rupees per month.",
        "covers": ["P1.1", "P1.2"],
    },
    {
        "id": "h03_same_station_ua",
        "chapter": "CHAPTER 3 \u2022 PARAS 1.3 & 1.4: 'SAME STATION' & UA",
        "title": "PARAS 1.3\u20131.4 \u2014 WHAT COUNTS AS THE 'SAME STATION'",
        "accent": ORANGE, "badge": "1.3-1.4",
        "q": "What exactly does 'same station' cover, and where does the UA definition come from?",
        "q_say": "Sir, House Rent Allowance rules keep referring to the same station. What exactly does that cover?",
        "boxes": [
            ("THREE LIMBS OF SAME STATION",
             "Contiguous places (Para 3.2) + dependent places (Para 3.4) + places inside the Urban Agglomeration.",
             "Para 1.3: Same station means all places contiguous to the qualified city as defined in Para 3.2, "
             "together with all places dependent on it as defined in Para 3.4, and it also includes places which "
             "are inside the Urban Agglomeration of that city.",
             SKY,
             "Paragraph 1.3 gives three limbs. Same station means all places contiguous to the qualified city "
             "under Paragraph 3.2, plus places dependent on it under Paragraph 3.4, plus places inside the Urban "
             "Agglomeration of that city."),
            ("WHERE THE UA DEFINITION COMES FROM",
             "The latest Census Report of the Registrar General and Census Commissioner of India.",
             "Para 1.4: The expressions Urban Agglomeration and other related expressions are as defined in the "
             "latest Census Report published by the Registrar General and Census Commissioner of India. The "
             "compendium borrows the Census meaning rather than inventing its own.",
             GREEN,
             "Paragraph 1.4 takes the definition from the latest Census Report of the Registrar General and "
             "Census Commissioner of India."),
            ("WHAT AN URBAN AGGLOMERATION IS",
             "A continuous urban spread: a town plus its adjoining outgrowths, or two or more contiguous towns.",
             "Para 1.4: An Urban Agglomeration is a continuous urban spread constituted by a town and its "
             "adjoining outgrowths, or by two or more physically contiguous towns together with their outgrowths. "
             "It is an urban extent, not an administrative one.",
             ORANGE,
             "An Urban Agglomeration is a continuous urban spread made of a town and its adjoining outgrowths, or "
             "contiguous towns. Why does this matter? Because during leave, deputation abroad, training or "
             "suspension, your House Rent Allowance depends on retaining a house at the same station. These two "
             "definitions decide what counts."),
            ("THE TRAP: CENSUS, NOT MUNICIPAL",
             "The UA is determined by the Census Report, not by municipal boundaries and not by local usage.",
             "Exam Trap (Para 1.4): An Urban Agglomeration is determined by the Census Report, not by municipal "
             "boundaries and not by local usage. Two different tests, and they produce two different consequences "
             "for whether a place counts as the same station.",
             RED,
             "Be careful with this trap. An Urban Agglomeration is determined by the Census Report, not by "
             "municipal boundaries and not by local usage. Two different tests, two different consequences."),
        ],
        "hook": "REMEMBER: CONTIGUOUS + DEPENDENT + URBAN AGGLOMERATION \u2022 UA COMES FROM THE CENSUS REPORT!",
        "hook_say": "Remember: same station covers contiguous, dependent and Urban Agglomeration areas, and the "
                    "Urban Agglomeration comes from the Census Report.",
        "covers": ["P1.3", "P1.4"],
    },
    {
        "id": "h04_city_classification",
        "chapter": "CHAPTER 4 \u2022 PARA 2.1: CLASSIFICATION OF CITIES",
        "title": "PARA 2.1 \u2014 WHO DECIDES X, Y AND Z CLASSIFICATION?",
        "accent": BLUE, "badge": "PARA 2.1",
        "q": "Who decides the X, Y and Z classification of cities?",
        "q_say": "Sir, everybody talks about X, Y and Z class cities. Who decides that classification?",
        "boxes": [
            ("THE TEST IS POPULATION",
             "Classification is by population of the area, as per the latest Census Report.",
             "Para 2.1: The classification of cities and towns for grant of House Rent Allowance is based on the "
             "population of the area as per the latest Census Report. Population is the sole criterion laid down "
             "in the compendium.",
             SKY,
             "Paragraph 2.1 is clear. Classification of cities for House Rent Allowance is based on the "
             "population of the area, as per the latest Census Report."),
            ("X CLASS",
             "Any city or town with a population of fifty lakh and above falls in X class.",
             "Para 2.1: Cities and towns with a population of fifty lakh and above are classified as X class. "
             "These attract the highest rate of House Rent Allowance.",
             GREEN,
             "The first class is X. Any city or town with a population of fifty lakh and above falls in X class."),
            ("Y AND Z CLASS",
             "Y: five lakh up to fifty lakh. Z: below five lakh. Anything not listed as X or Y is treated as Z.",
             "Para 2.1: Cities and towns with a population of five lakh and above but below fifty lakh are "
             "classified as Y class. All other cities and towns, that is those below five lakh, fall in Z class. "
             "A place not listed as X or Y is treated as Z.",
             ORANGE,
             "Y class covers populations from five lakh up to fifty lakh. Z class covers everything below five "
             "lakh. Any place not listed as X or Y is treated as Z."),
            ("THE TRAP: LISTS ARE SEPARATE",
             "This compendium fixes the criteria only; the actual city lists come from separate DoE orders.",
             "Exam Trap (Para 2.1): The compendium fixes only the population criteria. The city-wise lists are "
             "notified separately by the Department of Expenditure \u2014 most recently the re-classification on "
             "Census-2011 figures vide O.M. No. 2/5/2017-E.IIB dated 07.12.2019, with specific changes such as "
             "Mathura-Vrindavan to Y class vide O.M. No. 02/04/2018-E.IIB dated 25.02.2020.",
             RED,
             "Now the trap. This compendium only fixes the population criteria. The actual list of cities in each "
             "class is notified by separate Department of Expenditure orders, the latest being the Census twenty "
             "eleven reclassification of December twenty nineteen."),
        ],
        "hook": "REMEMBER: X = 50 LAKH+ \u2022 Y = 5 TO 50 LAKH \u2022 Z = BELOW 5 LAKH \u2022 ALWAYS LATEST CENSUS!",
        "hook_say": "Remember: X is fifty lakh and above, Y is five to fifty lakh, Z is below five lakh, and the "
                    "test always comes from the latest Census.",
        "covers": ["P2.1"],
    },
    {
        "id": "h05_rates_and_da_ladder",
        "chapter": "CHAPTER 5 \u2022 PARA 2.1 NOTE: RATES & DA LADDER",
        "title": "PARA 2.1 NOTE \u2014 THE RATES REVISE WHEN DA CROSSES 25% AND 50%",
        "accent": RED, "badge": "2.1 NOTE",
        "q": "This compendium says 24%, 16% and 8%. But my payslip shows 30%. Which is correct?",
        "q_say": "Sir, this compendium says twenty four, sixteen and eight per cent. But my payslip shows thirty "
                 "per cent. Which one is correct?",
        "flow": "hra_ladder",
        "boxes": [
            ("THE PRINTED TABLE IS THE BASE",
             "24% for X, 16% for Y, 8% for Z \u2014 these are the base Seventh Pay Commission rates, NOT today's rates.",
             "Para 2.1 (table): The rates printed in the compendium are twenty four per cent for X class, sixteen "
             "per cent for Y class and eight per cent for Z class. These are the base rates adopted on the "
             "implementation of the Seventh Central Pay Commission with effect from 1.1.2016. They are the floor "
             "of the ladder, not the current rate.",
             SKY,
             "Excellent question, and this is the single most important correction in the whole course. The table "
             "printed in the Office Memorandum gives the base Seventh Pay Commission rates: twenty four per cent "
             "for X, sixteen for Y, and eight for Z."),
            ("FIRST TRIGGER: DA CROSSES 25%",
             "Rates rise automatically to 27% (X), 18% (Y) and 9% (Z) when DA crosses 25%.",
             "Para 2.1 (Note): When Dearness Allowance crosses twenty five per cent, the rates of House Rent "
             "Allowance are revised to twenty seven per cent for X, eighteen per cent for Y and nine per cent for "
             "Z. This trigger fired with effect from 1.7.2021.",
             GREEN,
             "But read the note below that table. When Dearness Allowance crosses twenty five per cent, the rates "
             "automatically rise to twenty seven, eighteen and nine per cent."),
            ("SECOND TRIGGER: DA CROSSES 50%",
             "Rates rise again to 30% (X), 20% (Y) and 10% (Z) when DA crosses 50% \u2014 in force from 1.1.2024.",
             "Para 2.1 (Note): When Dearness Allowance crosses fifty per cent, the rates are revised again, to "
             "thirty per cent for X, twenty per cent for Y and ten per cent for Z. This trigger fired with effect "
             "from 1.1.2024, and 30/20/10 is the rate in force today.",
             ORANGE,
             "And when Dearness Allowance crosses fifty per cent, they rise again, to thirty, twenty and ten per "
             "cent. Both of those triggers have already fired."),
            ("THE TRAP: NO SEPARATE ORDER",
             "The revision is automatic \u2014 DoE confirmed in August 2021 that no separate HRA order is issued at each threshold.",
             "Exam Trap (Para 2.1 Note): The revision is self-operating. The Department of Expenditure clarified "
             "vide ID Note No. 2/5/2017-E.II(B) dated 04.08.2021 that no separate order is issued revising HRA "
             "when DA crosses these levels. That is why no order stating thirty per cent exists, and why the "
             "2022 table is so often mistaken for the current rate.",
             RED,
             "Here is the trap. The revision is automatic. The Department of Expenditure confirmed in August "
             "twenty twenty one that no separate House Rent Allowance order is issued when Dearness Allowance "
             "crosses these levels. So you will never find an order saying thirty per cent."),
        ],
        "hook": "REMEMBER: 24/16/8 IS ONLY THE BASE \u2022 BOTH DA TRIGGERS FIRED \u2014 TODAY IT IS 30/20/10!",
        "hook_say": "Remember: twenty four, sixteen and eight is only the base rate. Both Dearness Allowance "
                    "triggers have already fired, so today's rate is thirty, twenty and ten per cent.",
        "covers": ["P2.1N"],
    },
    {
        "id": "h06_position_today_2026",
        "chapter": "CHAPTER 6 \u2022 CURRENT POSITION: WHERE THE RATES STAND TODAY",
        "title": "CURRENT POSITION \u2014 THE RATE IN FORCE AS OF OCTOBER 2026",
        "accent": PINK, "badge": "TODAY",
        "q": "What is the exact position as of today, and is anything still pending?",
        "q_say": "Sir, then what is the exact position as of today, and is anything still pending?",
        "boxes": [
            ("CROSSING THE 50% THRESHOLD",
             "DA crossed 50% w.e.f. 1.1.2024, so HRA moved to 30%, 20% and 10% of basic pay.",
             "Dearness Allowance crossed fifty per cent with effect from 1 January 2024. That crossed the second "
             "and final threshold in the Note to Para 2.1, moving House Rent Allowance to thirty per cent (X), "
             "twenty per cent (Y) and ten per cent (Z) of basic pay. This is the rate in force today.",
             SKY,
             "Here is the current position. Dearness Allowance crossed fifty per cent with effect from first "
             "January, twenty twenty four. That crossed the second and final threshold, so House Rent Allowance "
             "moved to thirty, twenty and ten per cent of basic pay."),
            ("DEARNESS ALLOWANCE TODAY",
             "DA is 60% of basic pay w.e.f. 1.1.2026 \u2014 DoE O.M. 1/1(i)/2026-E.II(B) dated 22.04.2026.",
             "Dearness Allowance stands at sixty per cent of basic pay with effect from 1 January 2026, raised "
             "from fifty eight per cent by DoE O.M. No. 1/1(i)/2026-E.II(B) dated 22 April 2026 following Cabinet "
             "approval on 18 April 2026. The instalment due from 1 July 2026 had not been notified as of "
             "21 October 2026.",
             GREEN,
             "Dearness Allowance today is sixty per cent of basic pay, with effect from first January, twenty "
             "twenty six. That is Office Memorandum 1 slash 1 sub one slash 2026 E two B, dated twenty second "
             "April, twenty twenty six."),
            ("THE MINIMUM FLOOR",
             "HRA is never less than Rs 5,400 (X), Rs 3,600 (Y) and Rs 1,800 (Z) per month.",
             "Minimum House Rent Allowance is five thousand four hundred rupees in X class, three thousand six "
             "hundred rupees in Y class and one thousand eight hundred rupees in Z class per month. These are "
             "thirty, twenty and ten per cent of the minimum pay of eighteen thousand rupees in Level 1 of the "
             "Seventh Pay Commission Pay Matrix.",
             ORANGE,
             "And there is a floor. House Rent Allowance is never less than five thousand four hundred rupees in "
             "X class, three thousand six hundred in Y, and one thousand eight hundred in Z. Those figures are "
             "thirty, twenty and ten per cent of the minimum pay of eighteen thousand."),
            ("THE TRAP: THERE IS NO THIRD RUNG",
             "DA at 60% does not give a further HRA step \u2014 the ladder has only two rungs, at 25% and 50%.",
             "Exam Trap: The ladder has only two rungs, at twenty five per cent and fifty per cent, and both are "
             "behind us. Dearness Allowance at sixty per cent, or any future instalment, does not create a further "
             "House Rent Allowance step. House Rent Allowance stays at thirty, twenty and ten per cent.",
             RED,
             "And here is the trap. Dearness Allowance at sixty per cent does not give you a further House Rent "
             "Allowance step. The ladder has only two rungs, at twenty five and fifty per cent, and both are "
             "behind us."),
        ],
        "hook": "REMEMBER: 30/20/10 SINCE JAN 2024 \u2022 DA 60% SINCE JAN 2026 \u2022 NO THIRD RUNG!",
        "hook_say": "Remember: House Rent Allowance is thirty, twenty and ten per cent since January twenty twenty "
                    "four, Dearness Allowance is sixty per cent since January twenty twenty six, and there is no "
                    "third rung on the ladder.",
        "covers": ["TODAY"],
    },
    {
        "id": "h07_eighth_cpc",
        "chapter": "CHAPTER 7 \u2022 8TH CPC: IS 40% HRA OFFICIAL YET?",
        "title": "8TH PAY COMMISSION \u2014 STATUS, AND THE 40/35/30 DEMAND TRAP",
        "accent": YELLOW, "badge": "8TH CPC",
        "q": "Everyone is sharing messages about 40% HRA under the 8th Pay Commission. Is that official now?",
        "q_say": "Sir, everyone is sharing messages about a forty per cent House Rent Allowance under the Eighth "
                 "Pay Commission. Is that official now?",
        "boxes": [
            ("CONSTITUTED, NOT REPORTED",
             "Formally constituted by Gazette resolution dated 3 November 2025; chaired by Justice Ranjana Prakash Desai.",
             "The Eighth Central Pay Commission was formally constituted by Gazette resolution dated 3 November "
             "2025, following Cabinet approval on 16 January 2025 and approval of its Terms of Reference on "
             "28 October 2025. It is chaired by Justice Ranjana Prakash Desai. Its term is eighteen months from "
             "constitution.",
             SKY,
             "Short answer: no, not official. The Eighth Central Pay Commission was formally constituted by "
             "Gazette resolution dated third November, twenty twenty five. It is chaired by Justice Ranjana "
             "Prakash Desai."),
            ("NO RECOMMENDATIONS YET",
             "Lok Sabha reply dated 10 August 2026: no recommendations submitted. Report due around May 2027.",
             "In a written reply to the Lok Sabha on 10 August 2026, the Ministry of Finance confirmed that the "
             "Commission has not submitted its recommendations. With an eighteen month term running from "
             "constitution on 3 November 2025, the report falls due around May 2027.",
             GREEN,
             "In a written reply to the Lok Sabha on tenth August, twenty twenty six, the Ministry of Finance "
             "confirmed the Commission has not submitted its recommendations yet. It has eighteen months from "
             "constitution, so the report is due around May, twenty twenty seven."),
            ("STILL IN CONSULTATION",
             "Meetings held at Chandigarh, Puducherry and Bengaluru; Mumbai scheduled for 22\u201323 October 2026.",
             "The Commission remains in its consultation phase. Meetings were held at Chandigarh, Puducherry and "
             "Bengaluru during September and October 2026, with Mumbai scheduled for 22 and 23 October 2026. No "
             "pay or allowance figures have been settled at any of them.",
             ORANGE,
             "It is still in the consultation phase. Meetings were held at Chandigarh, Puducherry and Bengaluru, "
             "with Mumbai scheduled for twenty second and twenty third October, twenty twenty six."),
            ("THE TRAP: 40/35/30 ARE DEMANDS",
             "Those figures are staff-side demands, not recommendations \u2014 and no Government order has been issued on them.",
             "Exam Trap: The forty, thirty five and thirty per cent House Rent Allowance figures circulating "
             "online are demands submitted to the Commission by staff bodies, including the National Council "
             "(JCM). They are not recommendations, they have not been accepted, and no Government order has been "
             "issued on them. In an examination answer, quote only notified rates.",
             RED,
             "Now the trap, and it is a big one. The forty, thirty five and thirty per cent figures circulating "
             "online are demands submitted to the Commission by staff bodies. They are not recommendations, and "
             "no Government order has been issued on them. In an exam answer, quote only notified rates."),
        ],
        "hook": "REMEMBER: CONSTITUTED 3.11.2025 \u2022 REPORT DUE ~MAY 2027 \u2022 40/35/30 ARE DEMANDS, NOT LAW!",
        "hook_say": "Remember: the Eighth Pay Commission was constituted on third November twenty twenty five, its "
                    "report is due around May twenty twenty seven, and the House Rent Allowance figures "
                    "circulating online are demands, not law.",
        "covers": ["8CPC"],
    },
    {
        "id": "h08_place_of_duty",
        "chapter": "CHAPTER 8 \u2022 PARAS 3.1\u20133.3: PLACE OF DUTY",
        "title": "PARAS 3.1\u20133.3 \u2014 PLACE OF DUTY, NOT PLACE OF RESIDENCE",
        "accent": SKY, "badge": "3.1-3.3",
        "q": "An officer works in a classified city but lives 30 km away. What happens to his HRA?",
        "q_say": "Sir, if an officer works in a classified city but lives in a village thirty kilometres away, "
                 "what happens to his House Rent Allowance?",
        "boxes": [
            ("PLACE OF DUTY GOVERNS",
             "HRA is admissible with reference to the place of duty, irrespective of where the servant resides.",
             "Para 3.1: House Rent Allowance is admissible with reference to the place of duty of the Government "
             "servant, irrespective of whether he is residing at that place or anywhere else. Residence is not "
             "the test.",
             SKY,
             "The answer is the place of duty. Paragraph 3.1 says House Rent Allowance is admissible with "
             "reference to the place of duty of the Government servant, irrespective of whether he is residing at "
             "that place or anywhere else."),
            ("THE BOUNDARY (PARA 3.2)",
             "The named municipality or corporation, plus contiguous suburban municipalities, notified areas and cantonments.",
             "Para 3.2: The locality for this purpose is the named municipality or corporation, and it also "
             "includes such suburban municipalities, notified areas or cantonments as are contiguous to it, and "
             "any other area that the Central Government may by order notify.",
             GREEN,
             "Paragraph 3.2 fixes the boundary. The locality is the named municipality or corporation, and it "
             "also includes suburban municipalities, notified areas or cantonments that are contiguous to it, "
             "plus any other area the Central Government notifies."),
            ("BOUNDARY CHANGES (PARA 3.3)",
             "A State Government inclusion or exclusion applies automatically from that very date.",
             "Para 3.3: Where a State Government includes an area within, or excludes it from, a municipality or "
             "an Urban Agglomeration, these instructions automatically apply to, or cease to apply to, that area "
             "from the date of such inclusion or exclusion. No separate Central order is needed.",
             ORANGE,
             "Paragraph 3.3 removes any doubt about change. If a State Government includes an area within, or "
             "excludes it from, the municipality or Urban Agglomeration, these instructions automatically apply "
             "or cease to apply from that very date."),
            ("THE TRAP: RESIDENCE IS IRRELEVANT",
             "Living elsewhere does not defeat the claim \u2014 but the separate conditions in Para 5 can still bar it.",
             "Exam Trap (Paras 3.1 and 5): Living outside the classified city does not by itself defeat the "
             "claim, because the test is the place of duty. However, the conditions in Para 5 operate "
             "independently and can still bar the allowance on other grounds.",
             RED,
             "So the trap is this: living elsewhere does not by itself defeat your claim. What matters is the "
             "place of duty. But remember, the separate conditions in Paragraph 5 can still bar you on other "
             "grounds."),
        ],
        "hook": "REMEMBER: HRA FOLLOWS THE PLACE OF DUTY, NOT WHERE YOU SLEEP!",
        "hook_say": "Remember: House Rent Allowance follows the place of duty, not where you sleep, and boundary "
                    "changes apply automatically from the date the State Government makes them.",
        "covers": ["P3.1", "P3.2", "P3.3"],
    },
    {
        "id": "h09_eight_km_rule",
        "chapter": "CHAPTER 9 \u2022 PARA 3.4: THE 8 KM RULE",
        "title": "PARA 3.4 \u2014 THE 8 KM CONCESSION AND ITS CERTIFICATE",
        "accent": GREEN, "badge": "PARA 3.4",
        "q": "Our office is 8 km outside the municipal limit. Do we still get the city rate?",
        "q_say": "Sir, our office is eight kilometres outside the municipal limit. Do we still get the city rate "
                 "of House Rent Allowance?",
        "boxes": [
            ("THE CONCESSION",
             "Establishments within 8 km of the periphery of the municipal limits get that city's rates.",
             "Para 3.4: Staff working in Central Government establishments located within eight kilometres of the "
             "periphery of the municipal limits of a qualified city are allowed House Rent Allowance at the rates "
             "admissible for that city, even if they do not reside within those limits.",
             SKY,
             "Yes, possibly. Paragraph 3.4 says staff working in Central Government establishments within eight "
             "kilometres of the periphery of the municipal limits of a qualified city get that city's House Rent "
             "Allowance rates, even if they do not reside within those limits."),
            ("THE CERTIFICATE",
             "An Annexure-I certificate must be obtained from the Collector or Deputy Commissioner having jurisdiction.",
             "Para 3.4: A certificate in the format at Annexure-I has to be obtained from the Collector or Deputy "
             "Commissioner having jurisdiction over the area. The certificate of dependency is likewise obtained "
             "from the Collector.",
             GREEN,
             "But there are conditions. First, a certificate in the Annexure One format must be obtained from the "
             "Collector or Deputy Commissioner having jurisdiction, and the Administrative Ministry must refer it "
             "to the Department of Expenditure for initial sanction for a period of three years."),
            ("THE SANCTION",
             "Administrative Ministry refers it to DoE for initial sanction for three years; extensions by the Ministry with its Financial Adviser.",
             "Para 3.4: The Administrative Ministry refers the proposal to the Department of Expenditure for "
             "initial sanction for a period of three years. Extensions beyond the initial three years may be "
             "allowed by the Administrative Ministry in consultation with its Financial Adviser, and by the "
             "Comptroller and Auditor General for staff serving under him.",
             ORANGE,
             "Extensions beyond the initial three years may be allowed by the Administrative Ministry in "
             "consultation with its Financial Adviser, and by the Comptroller and Auditor General for staff "
             "serving under him. The certificate of dependency is obtained from the Collector."),
            ("THE TRAP: IT IS RESIDUAL",
             "It continues only where the place is NOT included in the Urban Agglomeration of any city.",
             "Exam Trap (Para 3.4): The eight kilometre rule continues only at places within eight kilometres of "
             "the municipal limits which are not included within the Urban Agglomeration of any city. Where the "
             "place already falls inside a Urban Agglomeration, the Urban Agglomeration rule applies instead and "
             "this concession is not resorted to.",
             RED,
             "Here is the precise trap. The eight kilometre rule continues only at places within eight kilometres "
             "of the municipal limits which are NOT included in the Urban Agglomeration of any city. If the place "
             "is inside a Urban Agglomeration, the Urban Agglomeration rule applies instead."),
        ],
        "hook": "REMEMBER: 8 KM + COLLECTOR'S CERTIFICATE + 3-YEAR SANCTION \u2014 ONLY OUTSIDE A UA!",
        "hook_say": "Remember: eight kilometres, a Collector's certificate and a three year sanction, but only "
                    "where the place is not already inside a Urban Agglomeration.",
        "covers": ["P3.4"],
    },
    {
        "id": "h10_who_cannot_draw",
        "chapter": "CHAPTER 10 \u2022 PARAS 4.1\u20134.5: WHO CANNOT DRAW HRA",
        "title": "PARAS 4.1\u20134.5 \u2014 WHEN GOVERNMENT ACCOMMODATION BARS HRA",
        "accent": ORANGE, "badge": "4.1-4.5",
        "q": "If an officer gets a Government quarter, does his HRA stop immediately?",
        "q_say": "Sir, if an officer gets a Government quarter, does his House Rent Allowance stop immediately?",
        "boxes": [
            ("GENERAL POOL ACCOMMODATION (4.1)",
             "HRA is not admissible to those who occupy General Pool Residential Accommodation provided by the Government.",
             "Para 4.1: House Rent Allowance is not admissible to a Government servant who occupies General Pool "
             "Residential Accommodation provided by the Government. Occupation of Government accommodation is the "
             "fundamental bar.",
             SKY,
             "Paragraph 4.1 is the starting point. The allowance is not admissible to those who occupy General "
             "Pool Residential accommodation provided by the Government."),
            ("DEPARTMENTAL POOLS (4.2)",
             "Where departmental quarters exist, the prescribed procedure for applying for allotment must be followed.",
             "Para 4.2: Where Government residential accommodation is available for the staff of specified "
             "Departments or for specified categories of staff under departmental pools, the prescribed procedure "
             "for applying for allotment of such accommodation has to be followed.",
             GREEN,
             "Paragraph 4.2 covers departmental pools. Where Government quarters are available for the staff of "
             "specified Departments or for specified categories of staff, the prescribed procedure for applying "
             "for allotment has to be followed."),
            ("WHEN IT STOPS (4.3)",
             "It stops from the date the accommodation is actually handed over in an immediately habitable condition.",
             "Para 4.3: House Rent Allowance ceases to be admissible from the date the accommodation is actually "
             "handed over to the Government servant in an immediately habitable condition, and on surrender it "
             "becomes payable again from the date of surrender. Habitable condition, not the offer letter, is the "
             "test.",
             ORANGE,
             "Paragraph 4.3 answers your question precisely. House Rent Allowance stops from the date the "
             "accommodation is actually handed over in an immediately habitable condition. And on surrender, it "
             "becomes payable again from the date of surrender."),
            ("THE TRAPS (4.4\u20134.5)",
             "A debarred officer still gets HRA; a subsidised hostel bars it, a commercial-rent hostel does not.",
             "Paras 4.4 and 4.5: An officer debarred from allotment on account of unauthorised sub-letting "
             "continues to draw House Rent Allowance during the period of debarment. Residence in a Government "
             "run or subsidised hostel bars the allowance, but where the hostel charges market rent on commercial "
             "lines it does not.",
             RED,
             "Two traps here. First, an officer debarred from allotment for unauthorised sub letting still gets "
             "House Rent Allowance during the debarment. Second, a Government run or subsidised hostel bars the "
             "allowance, but if the hostel charges market rent on commercial lines, it does not."),
        ],
        "hook": "REMEMBER: GOVT QUARTER BARS HRA \u2022 STOPS ON HANDING OVER \u2022 SUBSIDISED HOSTEL ALSO BARS IT!",
        "hook_say": "Remember: a Government quarter ends the allowance, it stops on handing over in habitable "
                    "condition, and a subsidised hostel also bars it, while a commercial rent hostel does not.",
        "covers": ["P4.1", "P4.2", "P4.3", "P4.4", "P4.5"],
    },
    {
        "id": "h11_transfer_retention",
        "chapter": "CHAPTER 11 \u2022 PARAS 4.6\u20134.9: TRANSFER & RETENTION",
        "title": "PARAS 4.6\u20134.9 \u2014 RETAINING THE OLD QUARTER ON TRANSFER",
        "accent": BLUE, "badge": "4.6-4.9",
        "q": "On transfer I keep my old quarter for a few months. Can I also claim HRA at the new station?",
        "q_say": "Sir, on transfer I am allowed to keep my old quarter for a few months. Can I also claim House "
                 "Rent Allowance at the new station?",
        "boxes": [
            ("THE EIGHT MONTH WINDOW (4.6)",
             "Retaining the old quarter on normal, penal or market rent allows HRA at the new station up to 8 months.",
             "Para 4.6: Where a Government servant retains Government accommodation at the old station on payment "
             "of normal rent, penal rent, or even unauthorisedly on payment of market rent, House Rent Allowance "
             "may be drawn at the new station for a period not exceeding eight months from the date of transfer.",
             SKY,
             "Paragraph 4.6 gives you a window. If you retain Government accommodation at the old station on "
             "normal rent, penal rent, or even unauthorisedly on market rent, you may draw House Rent Allowance "
             "at the new station for up to eight months from the date of transfer."),
            ("FAMILY LEFT BEHIND (4.7)",
             "With no old quarter, eligibility continues at the new station until accommodation is allotted there.",
             "Para 4.7: Where the Government servant had no Government accommodation at the old station and "
             "leaves his family there because he has neither rented accommodation nor been allotted Government "
             "accommodation at the new station, he continues to be eligible at the new station until he is "
             "allotted accommodation there.",
             GREEN,
             "Paragraph 4.7 covers a different case. If you had no Government accommodation at the old station "
             "and leave your family behind because you have not rented a house or been allotted one at the new "
             "station, you stay eligible at the new station until you are allotted accommodation there."),
            ("THE HARD STOP (4.8)",
             "In either case HRA is not admissible beyond the date accommodation is allotted at the new station.",
             "Para 4.8: In either of the above cases, House Rent Allowance under these provisions is not "
             "admissible beyond the date on which Government accommodation is allotted to the Government servant "
             "at the new station. Allotment is an absolute cut-off.",
             ORANGE,
             "Paragraph 4.8 is the hard stop. In either case, House Rent Allowance under these provisions is not "
             "admissible beyond the date on which Government accommodation is allotted to you at the new "
             "station."),
            ("THE TRAP: THE 90-DAY SWITCH",
             "90 days or less draws the old rate; beyond that the rate follows the new place of posting.",
             "Exam Trap: Where the transfer is for ninety days or less, House Rent Allowance is drawn at the rate "
             "admissible at the old station. Where it exceeds ninety days, the rate follows the new place of "
             "posting. If a short transfer is later extended, the switch takes place from the date of the "
             "extension order and not from the date of the original transfer.",
             RED,
             "And the ninety day trap. For a transfer of ninety days or less, you draw the old rate. Beyond "
             "ninety days, the rate follows the new place of posting. If a short transfer is later extended, the "
             "switch happens from the date of the extension order, not from the date of transfer."),
        ],
        "hook": "REMEMBER: 8 MONTHS ON RETENTION \u2022 STOPS ON ALLOTMENT \u2022 90 DAYS SWITCHES THE RATE!",
        "hook_say": "Remember: eight months if you retain the old quarter, it stops on allotment at the new "
                    "station, and ninety days is the point at which the rate switches.",
        "covers": ["P4.6", "P4.7", "P4.8", "P4.9"],
    },
    {
        "id": "h12_sharing_rules",
        "chapter": "CHAPTER 12 \u2022 PARAS 5.1\u20135.4: SHARING ACCOMMODATION",
        "title": "PARAS 5.1\u20135.4 \u2014 WHEN SHARING IS ALLOWED AND WHEN IT IS FATAL",
        "accent": PINK, "badge": "5.1-5.4",
        "q": "Two Government servants share a rented flat and both pay rent. Can both draw HRA?",
        "q_say": "Sir, two Government servants share a rented flat and both pay rent. Can both of them draw House "
                 "Rent Allowance?",
        "boxes": [
            ("THREE ABSOLUTE BARS (5.1)",
             "Sharing another servant's Government accommodation; living in a parent's, son's or daughter's allotted accommodation; or a spouse allotted accommodation at the same station.",
             "Para 5.1: House Rent Allowance is not admissible where the Government servant shares Government "
             "accommodation allotted to another Government servant, or resides in accommodation allotted to his "
             "parent, son or daughter by Government or a public body, or where his or her spouse has been "
             "allotted accommodation at the same station, whether they live together or separately.",
             SKY,
             "Paragraph 5.1 sets three absolute bars. You cannot draw House Rent Allowance if you share "
             "Government accommodation allotted to another Government servant, or live in accommodation allotted "
             "to your parent, son or daughter by Government or a public body, or if your spouse has been "
             "allotted accommodation at the same station, whether you live there or separately."),
            ("SHARING IS FINE IF YOU PAY (5.2)",
             "Sharing private accommodation is allowed if you pay rent, or contribute to rent, house tax or property tax.",
             "Para 5.2: A Government servant sharing private residential accommodation with another Government "
             "servant remains eligible, provided he pays rent or contributes towards rent, house tax or property "
             "tax. The amount contributed is immaterial.",
             GREEN,
             "Now your case. Paragraph 5.2 says you remain eligible if you share private accommodation with "
             "another Government servant, provided you pay rent or contribute towards rent, house tax or property "
             "tax. The amount does not matter."),
            ("ONLY ONE OF TWO SHARERS (5.3)",
             "Where two share accommodation allotted to another Government servant, HRA goes to only one, at their choice.",
             "Para 5.3: Where two Government servants share accommodation allotted to another Government "
             "servant, House Rent Allowance is admissible to only one of them, at their option. Both cannot draw "
             "it on the strength of the same accommodation.",
             ORANGE,
             "But there is a limit. Where two employees share accommodation allotted to another Government "
             "servant, House Rent Allowance is admissible to only one of them, at their choice."),
            ("THE TRAP: THE SPOUSE CONTRAST",
             "Both spouses in hired or owned accommodation both draw HRA \u2014 unlike the Para 5.1 bar.",
             "Exam Trap: Where husband and wife are both Government servants and live in hired or owned "
             "accommodation, both draw House Rent Allowance according to their own entitlement. This is entirely "
             "different from the Para 5.1 bar, which bites only where the spouse has been allotted Government "
             "accommodation at the same station.",
             RED,
             "And here is the contrast examiners test. If husband and wife are both Government servants living in "
             "hired or owned accommodation, both draw House Rent Allowance as per their own entitlement. That is "
             "completely different from the Paragraph 5.1 bar, where the spouse has been allotted Government "
             "accommodation at the same station."),
        ],
        "hook": "REMEMBER: PAY RENT AND SHARING IS FINE \u2022 AN ALLOTTED SPOUSE QUARTER IS FATAL!",
        "hook_say": "Remember: paying rent makes sharing acceptable, an allotted spouse quarter is fatal to the "
                    "claim, but both spouses in a hired or owned house both get paid.",
        "covers": ["P5.1", "P5.2", "P5.3", "P5.4"],
    },
    {
        "id": "h13_guest_house",
        "chapter": "CHAPTER 13 \u2022 PARA 5.5: GUEST HOUSE STAY",
        "title": "PARA 5.5 \u2014 GUEST HOUSE RENT: REIMBURSEMENT, NOT HRA",
        "accent": YELLOW, "badge": "PARA 5.5",
        "q": "I stayed in a State Bhavan for a few months on posting. Am I paid anything?",
        "q_say": "Sir, on posting to a new station I stayed in a State Bhavan for a few months. Am I paid anything?",
        "boxes": [
            ("RENT CAN BE REIMBURSED",
             "Rent actually paid for a temporary stay in a State Bhavan, Guest House or Departmental Guest House may be reimbursed.",
             "Para 5.5: Reimbursement of the rent actually paid is admissible to a Government servant for a "
             "temporary stay in a State Bhavan, Guest House or Departmental Guest House. The reimbursement is of "
             "actual rent, not a percentage of pay.",
             SKY,
             "Yes, but not as House Rent Allowance. Paragraph 5.5 allows reimbursement of the rent actually paid "
             "when you stay temporarily in a State Bhavan, Guest House or Departmental Guest House run by the "
             "Central Government, a State Government or an Autonomous Organisation."),
            ("WHO MUST RUN IT",
             "The Central Government, a State Government, or an Autonomous Organisation.",
             "Para 5.5: The concession covers guest houses run by the Central Government, by a State Government, "
             "or by an Autonomous Organisation. A purely private hotel or lodge is outside Para 5.5 altogether.",
             GREEN,
             "There are five conditions. You must not have been allotted Government accommodation, the guest "
             "house must be at your place of posting, you must produce rent receipts, the reimbursement runs for "
             "a maximum of six months, and no House Rent Allowance is paid during this period."),
            ("SIX MONTHS, THEN STOP",
             "Maximum six months; beyond that the concession simply does not run.",
             "Para 5.5: Reimbursement is admissible for a maximum period of six months. Beyond six months the "
             "concession is not available, and the Government servant must fall back on the ordinary rules.",
             ORANGE,
             "So the outer limit is six months. Beyond that, the concession simply does not run."),
            ("THE TRAP: IT REPLACES HRA",
             "You get the reimbursement instead of HRA, never both \u2014 one is a percentage of pay, the other is actual rent.",
             "Exam Trap (Para 5.5): No House Rent Allowance is paid during the period for which rent "
             "reimbursement is allowed. It is an either-or: one is computed as a percentage of pay, the other on "
             "the rent actually paid supported by receipts. They never run together.",
             RED,
             "The trap is the either-or. During this period you get the reimbursement instead of House Rent "
             "Allowance, never both together. One is based on the percentage of pay, the other on the rent "
             "actually paid with receipts."),
        ],
        "hook": "REMEMBER: GUEST-HOUSE RENT REIMBURSED UP TO 6 MONTHS \u2014 AND NO HRA DURING THAT PERIOD!",
        "hook_say": "Remember: guest house rent is reimbursed for up to six months, and no House Rent Allowance "
                    "is paid during that period.",
        "covers": ["P5.5"],
    },
    {
        "id": "h14_during_leave",
        "chapter": "CHAPTER 14 \u2022 PARA 6.1: HRA DURING LEAVE",
        "title": "PARA 6.1 \u2014 HOW LONG DOES HRA CONTINUE ON LEAVE?",
        "accent": SKY, "badge": "PARA 6.1",
        "q": "If I take a long leave, for how many months does my HRA continue?",
        "q_say": "Sir, if I take a long leave, for how many months does my House Rent Allowance continue?",
        "boxes": [
            ("THE 180-DAY RULE",
             "Same rate for leave up to 180 days, and for the first 180 days of any longer spell. Terminal leave excluded.",
             "Para 6.1.1: House Rent Allowance continues to be drawn during leave at the same rate as before, for "
             "leave not exceeding one hundred and eighty days, and for the first one hundred and eighty days of "
             "leave of any longer duration. Terminal leave is excluded from this concession.",
             SKY,
             "Paragraph 6.1.1 gives the general rule. You draw House Rent Allowance during leave at the same rate "
             "as before, for leave not exceeding one hundred and eighty days, and for the first one hundred and "
             "eighty days of any longer spell. Terminal leave is excluded."),
            ("BEYOND 180 DAYS NEEDS A CERTIFICATE",
             "Beyond the first 180 days on non-medical grounds, the Annexure-III certificate must be furnished.",
             "Para 6.1.5: Beyond the first one hundred and eighty days of leave, on grounds other than the "
             "medical grounds specified in Para 6.1.6, the Government servant must furnish the certificate "
             "prescribed in Annexure-III in order to continue drawing House Rent Allowance.",
             GREEN,
             "Paragraph 6.1.5 adds the paperwork. Beyond the first one hundred and eighty days, on grounds other "
             "than the medical grounds in 6.1.6, you must furnish the certificate prescribed in Annexure Three."),
            ("TB, CANCER \u2014 8 MONTHS",
             "For tuberculosis, cancer or similar ailments on prescribed medical certificates, the limit extends to 8 months.",
             "Para 6.1.6: Employees suffering from tuberculosis, cancer, or similar ailments of like nature, on "
             "the basis of medical certificates in the prescribed form, are allowed House Rent Allowance for a "
             "period extended from one hundred and eighty days to eight months.",
             ORANGE,
             "Paragraph 6.1.6 is the humane exception. For employees suffering from tuberculosis, cancer or "
             "similar ailments on medical certificates in the prescribed form, the limit extends from one "
             "hundred and eighty days to eight months."),
            ("THE TRAP: RESIGNATION AFTER LEAVE",
             "Resigning without joining duty triggers recovery of the whole HRA; retirement on invalidity does not.",
             "Exam Trap: Where a Government servant proceeds on leave and then resigns from service without "
             "joining duty, the competent authority must recover the entire House Rent Allowance drawn during "
             "that leave before accepting the resignation. However, where leave on medical grounds beyond one "
             "hundred and eighty days ends in retirement on invalidity, no recovery is made.",
             RED,
             "Two final traps. If you take leave and then resign without joining duty, the authority must recover "
             "the entire House Rent Allowance drawn before accepting the resignation. But if leave on medical "
             "grounds beyond one hundred and eighty days ends in retirement on invalidity, no recovery is made."),
        ],
        "hook": "REMEMBER: 180 DAYS GENERALLY \u2022 8 MONTHS FOR TB AND CANCER \u2022 ANNEXURE-III BEYOND!",
        "hook_say": "Remember: one hundred and eighty days is the general limit, eight months for tuberculosis "
                    "and cancer, Annexure Three beyond that, and full recovery if you resign instead of rejoining.",
        "covers": ["P6.1"],
    },
    {
        "id": "h15_other_circumstances",
        "chapter": "CHAPTER 15 \u2022 PARAS 6.2\u20136.9: OTHER CIRCUMSTANCES",
        "title": "PARAS 6.2\u20136.9 \u2014 JOINING TIME, DEPUTATION, TRAINING, SUSPENSION",
        "accent": GREEN, "badge": "6.2-6.9",
        "q": "What happens to HRA during joining time, or if I go abroad on deputation?",
        "q_say": "Sir, what happens to my House Rent Allowance during joining time, or if I go abroad on deputation?",
        "boxes": [
            ("JOINING TIME AND DEPUTATION ABROAD",
             "Joining time: rate of the station transferred from. Deputation abroad: while the family remains at the last place of duty in India.",
             "Para 6.2: During joining time, House Rent Allowance is drawn at the rate admissible at the station "
             "from which the Government servant was transferred. Para 6.3: On deputation abroad, it continues to "
             "be drawn for as long as his family remains at his last place of duty in India, subject to the "
             "Annexure-III certificate.",
             SKY,
             "Paragraph 6.2 covers joining time: you continue at the rate of the station from which you were "
             "transferred. Paragraph 6.3 covers deputation abroad: you stay eligible for as long as your family "
             "remains at your last place of duty in India, subject to the Annexure Three certificate."),
            ("TRAINING ABROAD AND IN INDIA",
             "Abroad: rate of the station deputed from, and leave during training earns nothing. In India: the better of the two.",
             "Para 6.4: For training abroad, House Rent Allowance is drawn at the rate admissible at the station "
             "from which the Government servant was deputed for training, and no allowance is admissible for the "
             "period of leave taken during such training. Para 6.5: For training in India, the Government "
             "servant may draw at whichever is more favourable, the place of training or his place of duty.",
             GREEN,
             "For training abroad, Paragraph 6.4 gives you the rate of the station you were deputed from, and "
             "leave during the training earns nothing. For training in India, Paragraph 6.5 is generous: you may "
             "take whichever is more favourable, the place of training or your place of duty."),
            ("SUSPENSION AND TOUR",
             "Suspension: continues, with Annexure-III beyond 180 days. Tour: regulated with reference to the headquarters.",
             "Para 6.6: During suspension, House Rent Allowance continues to be drawn, but beyond one hundred "
             "and eighty days the Annexure-III certificate is required. Para 6.9: During tour, the entitlement is "
             "regulated with reference to the Government servant's headquarters.",
             ORANGE,
             "Paragraph 6.6 covers suspension: the allowance continues, but beyond one hundred and eighty days "
             "you need the Annexure Three certificate. Paragraph 6.9 is simple: during tour, your entitlement is "
             "regulated with reference to your headquarters."),
            ("THE TRAP: RE-EMPLOYED PENSIONERS",
             "HRA for re-employed pensioners is on pay plus pension, capped at the maximum of the post; non-FR staff get only 40 days.",
             "Paras 6.7 and 6.8: For re-employed pensioners, House Rent Allowance is computed on pay plus "
             "pension, subject to the ceiling of the maximum pay of the post in which re-employed. For employees "
             "outside the Fundamental Rules and the CCS (Leave) Rules, the concession is limited to forty days, "
             "extended to one hundred and eighty days for tuberculosis, cancer and similar ailments.",
             RED,
             "And the two traps. For re-employed pensioners, Paragraph 6.7 computes House Rent Allowance on pay "
             "plus pension, subject to the ceiling of the maximum pay of the post. And for employees outside the "
             "Fundamental Rules and the C.C.S. Leave Rules, Paragraph 6.8 allows only forty days, extended to "
             "one hundred and eighty for tuberculosis, cancer and similar ailments."),
        ],
        "hook": "REMEMBER: TRAINING IN INDIA = BETTER OF TWO \u2022 TOUR = HEADQUARTERS \u2022 NON-FR STAFF ONLY 40 DAYS!",
        "hook_say": "Remember: training in India gives you the better of two rates, tour follows your "
                    "headquarters, and staff outside the Fundamental Rules get only forty days.",
        "covers": ["P6.2", "P6.3", "P6.4", "P6.5", "P6.6", "P6.7", "P6.8", "P6.9"],
    },
    {
        "id": "h16_certificates",
        "chapter": "CHAPTER 16 \u2022 PARA 7: CERTIFICATES",
        "title": "PARA 7 \u2014 WHICH CERTIFICATES MUST ACTUALLY BE SUBMITTED",
        "accent": ORANGE, "badge": "PARA 7",
        "q": "What certificates do I actually have to submit to draw HRA?",
        "q_say": "Sir, what certificates do I actually have to submit to draw House Rent Allowance?",
        "boxes": [
            ("ANNEXURE-II WITH THE FIRST CLAIM",
             "Every Government servant must furnish a certificate in Annexure-II form along with the first HRA claim.",
             "Para 7.2.1: Every Government servant has to furnish a certificate in the form prescribed at "
             "Annexure-II along with the first claim for House Rent Allowance. It accompanies the first claim, "
             "not every subsequent one.",
             SKY,
             "Paragraph 7.2.1 is the main one. Every Government servant must furnish a certificate in the "
             "Annexure Two form along with the first claim for House Rent Allowance."),
            ("WHO RECEIVES THE CERTIFICATE",
             "Non-gazetted officers furnish it to their Head of Office; gazetted officers to their Accounts Officer.",
             "Para 7.2.2: Non-gazetted Government servants furnish the certificate to their Head of Office, while "
             "gazetted Government servants furnish it to their Accounts Officer. The addressee depends on the "
             "class of the employee.",
             GREEN,
             "Paragraph 7.2.2 splits the audience. Non-gazetted officers furnish the certificate to their Head of "
             "Office; gazetted officers furnish it to their Accounts Officer."),
            ("THE DDO ENDORSEMENT",
             "The Drawing and Disbursing Officer endorses two certificates on the bill.",
             "Para 7.2.3: The Drawing and Disbursing Officer has to endorse two certificates on the bill: first, "
             "that eligibility has been verified with reference to the Ministry of Finance order; and second, "
             "that the prescribed certificates have been obtained and the claims are in order.",
             ORANGE,
             "Paragraph 7.2.3 puts the duty on the Drawing and Disbursing Officer, who must endorse two "
             "certificates on the bill: that eligibility has been verified against the Ministry of Finance order, "
             "and that the prescribed certificates have been obtained and the claims are in order."),
            ("THE TRAP: NO-ACCOMMODATION CERTIFICATE",
             "Abolished \u2014 applying for Government accommodation and the No Accommodation Certificate were dispensed with on 3.5.2019.",
             "Exam Trap: There is no longer any requirement to apply for Government accommodation or to furnish a "
             "No Accommodation Certificate. That condition was dispensed with by the Department of Expenditure "
             "vide O.M. No. 2/5/2017-E.IIB dated 3 May 2019. Annexure-III is still required for the specific "
             "cases listed in Para 7.3.",
             RED,
             "And the most valuable trap of this chapter. You no longer need to apply for Government "
             "accommodation or furnish a No Accommodation Certificate. That condition was dispensed with by the "
             "Department of Expenditure order of third May, twenty nineteen. Annexure Three is still required for "
             "the specific cases listed in Paragraph 7.3."),
        ],
        "hook": "REMEMBER: ANNEXURE-II WITH FIRST CLAIM \u2022 DDO ENDORSES \u2022 NO-ACCOMMODATION CERTIFICATE ABOLISHED!",
        "hook_say": "Remember: Annexure Two goes with your first claim, the Drawing and Disbursing Officer "
                    "endorses the bill, and the No Accommodation Certificate has been abolished.",
        "covers": ["P7"],
    },
    {
        "id": "h17_master_recap",
        "chapter": "CHAPTER 17 \u2022 RAPID-FIRE RECAP",
        "title": "RAPID-FIRE RECAP \u2014 THE WHOLE COMPENDIUM IN FOUR CARDS",
        "accent": RED, "badge": "RECAP",
        "q": "Can we do a rapid-fire recap of the whole compendium?",
        "q_say": "Sir, before we finish, can we do a rapid-fire recap of the whole compendium?",
        "boxes": [
            ("SCOPE, PAY AND DEFINITIONS",
             "Civilians, Defence civilians and Audit & Accounts. Pay = Pay Matrix level. Family cut-off Rs 9,000 a month.",
             "Recap: The compendium covers all civilian Central Government employees, civilian employees paid "
             "from the Defence Services Estimates, and persons serving in the Indian Audit and Accounts "
             "Department. Pay for HRA is the pay drawn in the prescribed Level in the Pay Matrix and nothing "
             "else. Family excludes any relative with independent income above nine thousand rupees a month.",
             SKY,
             "Card one. Scope covers civilians, Defence civilians and the Audit and Accounts Department. Pay "
             "means the Pay Matrix level alone. And family excludes any relative with independent income above "
             "nine thousand rupees a month."),
            ("CLASSIFICATION AND CURRENT RATES",
             "X 50 lakh+, Y 5 to 50 lakh, Z below 5 lakh. Base 24/16/8 \u2014 today 30/20/10. DA 60%.",
             "Recap: Classification is by population in the latest Census Report. The printed base rates of "
             "twenty four, sixteen and eight per cent have been superseded by operation of the Note to Para 2.1: "
             "today the rates are thirty, twenty and ten per cent with effect from 1.1.2024, and Dearness "
             "Allowance stands at sixty per cent with effect from 1.1.2026.",
             GREEN,
             "Card two. X is fifty lakh and above, Y is five to fifty lakh, Z is below five lakh. The base rates "
             "were twenty four, sixteen and eight. Today they are thirty, twenty and ten, and Dearness Allowance "
             "stands at sixty per cent."),
            ("ADMISSIBILITY AND THE CONDITIONS",
             "Place of duty governs; the 8 km rule is residual; sharing is fine if you pay rent or contribute to tax.",
             "Recap: House Rent Allowance follows the place of duty, not the place of residence. The eight "
             "kilometre concession in Para 3.4 is residual, needing a Collector's certificate, and applies only "
             "outside a Urban Agglomeration. Government accommodation bars the allowance, but sharing private "
             "accommodation is permitted where rent or tax is contributed.",
             ORANGE,
             "Card three. House Rent Allowance follows the place of duty. The eight kilometre rule is residual "
             "and needs a Collector's certificate. Government accommodation bars the allowance, but sharing is "
             "fine if you pay rent or contribute to tax."),
            ("LEAVE, CERTIFICATES AND THE APPENDIX",
             "180 days leave, 8 months for TB and cancer, 40 days for non-FR staff. Annexure-II and Annexure-III. Appendix lists superseded orders.",
             "Recap: Leave runs one hundred and eighty days generally, eight months for tuberculosis and cancer, "
             "and forty days for staff outside the Fundamental Rules. Annexure-II accompanies the first claim and "
             "Annexure-III covers the listed cases. The Appendix to the compendium records the earlier orders "
             "consolidated and superseded by this Office Memorandum.",
             RED,
             "Card four. One hundred and eighty days of leave generally, eight months for tuberculosis and "
             "cancer, forty days for staff outside the Fundamental Rules. Annexure Two with the first claim, "
             "Annexure Three for the listed cases, and the Appendix records the earlier orders now superseded."),
        ],
        "hook": "REMEMBER: PLACE OF DUTY GOVERNS \u2022 30/20/10 TODAY \u2022 180 DAYS LEAVE \u2022 ANNEXURE-II FIRST CLAIM!",
        "hook_say": "Remember: place of duty governs, thirty, twenty and ten per cent applies today, one hundred "
                    "and eighty days on leave, and Annexure Two goes with your first claim.",
        "covers": ["RECAP"],
    },
]


FLOWS = {
    "hra_ladder": {
        "nodes": [
            (80, 300, 400, 80, "BASE RATE", "24% / 16% / 8% from 1.1.2016", SKY, 1),
            (560, 300, 420, 80, "DA CROSSES 25%", "27% / 18% / 9% from 1.7.2021", GREEN, 2),
            (1060, 300, 420, 80, "DA CROSSES 50%", "30% / 20% / 10% from 1.1.2024", ORANGE, 3),
            (1560, 300, 340, 80, "TODAY", "DA 60% - no third rung", RED, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, GREEN, 3), (2, 3, ORANGE, 4)],
    },
}


PART_STARTS = [
    "h01_scope_of_master_om",
    "h05_rates_and_da_ladder",
    "h08_place_of_duty",
    "h10_who_cannot_draw",
    "h14_during_leave",
]


# ===============================================================================================
# ENGINE
# ===============================================================================================

assert len({s["id"] for s in SCENES}) == len(SCENES), "duplicate scene id"

FULL = {}
for _sc_ in SCENES:
    _new, _seen = [], set()
    for (_t, _short, _full, _c, _n) in _sc_["boxes"]:
        assert _t not in _seen, f"duplicate card title in {_sc_['id']}: {_t}"
        _seen.add(_t)
        FULL[(_sc_["id"], _t)] = _full
        _new.append((_t, _short, _c, _n))
    _sc_["boxes"] = _new


def write_reference_sheet():
    out = ["# DoPT Technical Resignation & Lien Guidelines - full-wording reference sheet", "",
           "Every card on screen is a short key-point; the full wording / examinable facts of each card",
           "are listed here, in chapter order, so the video can be cross-checked against the O.M.", ""]
    for i, sc in enumerate(SCENES, 1):
        out += [f"## Chapter {i} - {sc['chapter']}", f"**{sc['title']}**  ({sc['badge']})", "",
                f"Q: {sc['q']}", ""]
        for (t, _b, _c, _n) in sc["boxes"]:
            out += [f"### {t}", FULL[(sc["id"], t)], ""]
        out += [f"> {sc['hook']}", ""]
    (ROOT / "hra_reference_sheet.md").write_text("\n".join(out), encoding="utf-8")


# =============================================================================================
# Drawing helpers
# =============================================================================================
_FONT_CACHE = {}


def font(size: int, bold: bool = False):
    key = (size, bold)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    names = (["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "arialbd.ttf", "NotoSans-Bold.ttf"]
             if bold else
             ["DejaVuSans.ttf", "LiberationSans-Regular.ttf", "arial.ttf", "NotoSans-Regular.ttf"])
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


def card_boxes(scene):
    n = len(scene["boxes"])
    top = 290
    if "flow" in scene:
        gap = 20
        bw_ = (W - 160 - gap * (n - 1)) // n
        return [(80 + i * (bw_ + gap), 490, bw_, 300) for i in range(n)]
    if n == 4:
        return [(80, top, 860, 245), (980, top, 860, 245),
                (80, top + 255, 860, 245), (980, top + 255, 860, 245)]
    gap = 20
    bw_ = (W - 160 - gap * (n - 1)) // n
    return [(80 + i * (bw_ + gap), top, bw_, 480) for i in range(n)]


def render_frame(scene, qno, total, reveal, kind, out_path: Path):
    img, d = background()
    acc = scene["accent"]
    n = len(scene["boxes"])

    d.rectangle([0, 0, W, 10], fill=acc)
    d.text((80, 34), scene["chapter"], font=font(22, True), fill=ORANGE)
    f_t, l_t, _, _ = fit_block(d, scene["title"], True, 1440, 50, TITLE_START, TITLE_MIN, 1.1)
    if len(l_t) > 1:      # a wrapped title would be silently clipped - fail loudly instead
        raise ValueError(f"CHAPTER TITLE WRAPS (shorten it): {scene['title']!r}")
    d.text((80, 76), l_t[0], font=f_t, fill=TEXT_WHITE)
    bd = scene["badge"]
    fb = font(20, True)
    bw = text_w(d, bd, fb) + 50
    d.rounded_rectangle([W - 80 - bw, 45, W - 80, 95], radius=10, fill=acc)
    d.text((W - 80 - bw + 25, 59), bd, font=fb,
           fill=(10, 16, 36) if acc in (ORANGE, SKY, GREEN) else TEXT_WHITE)
    d.line([(80, 150), (W - 80, 150)], fill=(51, 65, 85), width=2)

    asking = kind in ("question",)
    bt, bb = 162, 272
    d.rounded_rectangle([80, bt, W - 80, bb], radius=18, fill=lerp(CARD_BG, acc, 0.20 if asking else 0.10),
                        outline=YELLOW if asking else lerp(CARD_BG, acc, 0.5), width=5 if asking else 2)
    d.ellipse([100, bt + 20, 170, bt + 90], fill=acc)
    qs = f"Q{qno}"
    fq = font(30 if len(qs) < 3 else 24, True)
    d.text((135 - text_w(d, qs, fq) // 2, bt + 36), qs, font=fq,
           fill=(10, 16, 36) if acc in (ORANGE, SKY, GREEN) else TEXT_WHITE)
    f_q, l_q, lh_q, _ = fit_block(d, scene["q"], True, 1250, 92, 38, 22, 1.22)
    ty = bt + (bb - bt - len(l_q) * lh_q) // 2
    for i, ln in enumerate(l_q):
        d.text((200, ty + i * lh_q), ln, font=f_q, fill=TEXT_WHITE)
    draw_skyline(d, 1560, bb - 8, acc)
    chip, chip_col = (("RIYA ASKS (Student)", YELLOW) if kind == "question" else ("THE TEACHER EXPLAINS", GREEN))
    fc = font(17, True)
    cw = text_w(d, chip, fc) + 30
    d.rounded_rectangle([W - 100 - cw, bt + 10, W - 100, bt + 40], radius=14, fill=chip_col)
    d.text((W - 100 - cw + 15, bt + 14), chip, font=fc, fill=(10, 16, 36))

    if "flow" in scene:
        draw_flow(d, scene["flow"], reveal)
    boxes = card_boxes(scene)

    for i, ((bt_, body, col, _), (x, y, w, h)) in enumerate(zip(scene["boxes"], boxes)):
        if i >= reveal:
            continue
        newest = (i == reveal - 1) and kind == "answer"
        c = col if newest or kind in ("hook",) else dim(col, 0.8)
        if newest:
            d.rounded_rectangle([x - 6, y - 6, x + w + 6, y + h + 6], radius=20, outline=YELLOW, width=4)
        d.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=CARD_BG, outline=c, width=3 if newest else 2)
        d.rectangle([x, y + 8, x + 12, y + h - 8], fill=c)
        f_bt, l_bt, lh_bt, _ = fit_block(d, bt_, True, w - 60, 62, TITLE_START, TITLE_MIN, 1.15)
        for k, ln in enumerate(l_bt):
            d.text((x + 32, y + 16 + k * lh_bt), ln, font=f_bt, fill=c)
        body_top = y + 16 + len(l_bt) * lh_bt + 10
        f_b, l_b, lh_b, _ = fit_block(d, body, False, w - 60, y + h - body_top - 14, BODY_START, BODY_MIN, 1.25)
        for k, ln in enumerate(l_b):
            d.text((x + 32, body_top + k * lh_b), ln, font=f_b, fill=TEXT_WHITE)

    if kind == "hook":
        d.rounded_rectangle([80, 796, W - 80, 846], radius=12, fill=YELLOW)
        f_h, l_h, _, _ = fit_block(d, scene["hook"], True, W - 200, 36, 24, 20, 1.1)
        if len(l_h) > 1:
            raise ValueError(f"Hook strip wraps (shorten): {scene['hook']!r}")
        d.text((100, 807), l_h[0], font=f_h, fill=(10, 16, 36))

    _footer(d, acc, qno, total, reveal + (1 if kind == "hook" else 0), n + 1)
    img.save(out_path)


def _footer(d, acc, qno, total, done, of):
    d.rectangle([0, 855, W, 1070], fill=(7, 11, 24))
    d.line([(80, 855), (W - 80, 855)], fill=(30, 41, 59), width=2)
    d.rectangle([0, 1068, W, H], fill=(20, 28, 50))
    seg_w = W / total
    d.rectangle([0, 1068, int(seg_w * (qno - 1) + seg_w * min(1.0, done / of)), H], fill=ORANGE)
    for k in range(1, total):
        d.line([(int(seg_w * k), 1068), (int(seg_w * k), H)], fill=(7, 11, 24), width=2)


def render_title_card(total, out_path: Path):
    img, d = background()
    d.rectangle([0, 0, W, 10], fill=ORANGE)
    acc = SKY
    d.rounded_rectangle([140, 250, W - 140, 470], radius=28, fill=(16, 24, 46), outline=acc, width=4)
    d.text((180, 286), "DoPT MASTERCLASS", font=font(26, True), fill=ORANGE)
    f_h, l_h, lh_h, _ = fit_block(d, TITLE_HEAD, True, W - 400, 120, 84, 48, 1.08)
    y = 330
    for ln in l_h:
        d.text((180, y), ln, font=f_h, fill=TEXT_WHITE)
        y += lh_h
    d.text((180, y + 12), TITLE_SUB, font=font(32, True), fill=SKY)
    d.text((180, y + 62), TITLE_META, font=font(28), fill=MUTED)

    # a compact road-map of the 16 chapters, two columns
    cx = [180, 990]
    fy = 530
    per_col = (len(SCENES) + 1) // 2
    for i, sc in enumerate(SCENES):
        col = 0 if i < per_col else 1
        row = i if col == 0 else i - per_col
        x = cx[col]
        yy = fy + row * 30
        d.ellipse([x, yy + 8, x + 10, yy + 18], fill=sc["accent"])
        label = f"{i + 1:02d}  {sc['chapter'].split('•', 1)[-1].strip()}"[:58]
        d.text((x + 22, yy), label, font=font(21), fill=MUTED)
    _footer(d, ORANGE, 1, total, 0, 1)
    img.save(out_path)


OUTRO_BULLETS = [
    "HRA follows the PLACE OF DUTY, not the place where you reside.",
    "The printed 24/16/8% is the base - today it is 30%/20%/10% of basic pay.",
    "Leave: 180 days generally, 8 months for TB and cancer, 40 days for non-FR staff.",
    "Annexure-II with the first claim; the No Accommodation Certificate is abolished.",
]


def render_outro_card(total, out_path: Path):
    img, d = background()
    d.rectangle([0, 0, W, 10], fill=GREEN)
    d.rounded_rectangle([160, 200, W - 160, 760], radius=28, fill=(16, 24, 46), outline=GREEN, width=4)
    d.text((200, 240), "MASTERCLASS COMPLETE", font=font(26, True), fill=ORANGE)
    d.text((200, 300), "Technical Resignation & Lien", font=font(58, True), fill=TEXT_WHITE)
    d.text((200, 378), TITLE_SUB, font=font(30, True), fill=SKY)
    y = 452
    for b in OUTRO_BULLETS:
        d.ellipse([204, y + 10, 224, y + 30], fill=GREEN)
        f_b, l_b, lh_b, _ = fit_block(d, b, False, W - 520, 60, 32, 24, 1.25)
        for k, ln in enumerate(l_b):
            d.text((244, y + k * lh_b), ln, font=f_b, fill=TEXT_WHITE)
        y += max(60, len(l_b) * lh_b) + 18
    _footer(d, ORANGE, total, total, 1, 1)
    img.save(out_path)


def audit_density():
    img, d = background()
    bad = 0
    print(f"{'scene':30s} {'card':38s} title body  chars")
    for sc in SCENES:
        # chapter title must fit on ONE line, or render would clip it
        try:
            _, l_t, _, ts = fit_block(d, sc["title"], True, 1440, 50, TITLE_START, TITLE_MIN, 1.1)
            if len(l_t) > 1:
                raise ValueError("title wraps")
            if ts < 27:
                print(f"{sc['id'][:30]:30s} {'[CHAPTER TITLE]':38s} {ts:>4d}       "
                      f"{len(sc['title']):>4d}  (small)")
        except ValueError:
            bad += 1
            print(f"{sc['id'][:30]:30s} {'[CHAPTER TITLE]':38s}  FAIL  "
                  f"{sc['title']!r} ({len(sc['title'])} chars) does not fit on one line")
        # the question must fit the box
        try:
            _, l_q, _, qs = fit_block(d, sc["q"], True, 1250, 92, 38, 22, 1.22)
            if len(l_q) > 3:
                raise ValueError("question wraps past 3 lines")
        except ValueError:
            bad += 1
            print(f"{sc['id'][:30]:30s} {'[QUESTION]':38s}  FAIL  {sc['q']!r}")
        for (t, body, _c, _n), (x, y, w, h) in zip(sc["boxes"], card_boxes(sc)):
            try:
                _, l_bt, lh_bt, ts = fit_block(d, t, True, w - 60, 62, TITLE_START, TITLE_MIN, 1.15)
                body_top = y + 16 + len(l_bt) * lh_bt + 10
                _, _, _, bs = fit_block(d, body, False, w - 60, y + h - body_top - 14, BODY_START, BODY_MIN, 1.25)
                flag = "" if bs >= 28 else "  (tight)"
                print(f"{sc['id'][:30]:30s} {t[:38]:38s} {ts:>4d} {bs:>4d}  {len(body):>4d}{flag}")
            except ValueError as e:
                bad += 1
                print(f"{sc['id'][:30]:30s} {t[:38]:38s}  FAIL  {e}")
        try:
            _, l_h, _, hs = fit_block(d, sc["hook"], True, W - 200, 36, 24, 20, 1.1)
            if len(l_h) > 1:
                raise ValueError("hook wraps")
        except ValueError:
            bad += 1
            print(f"{sc['id']}: HOOK does not fit on one line at >=20px ({len(sc['hook'])} chars)")
    print(f"\n{'ALL CARDS WITHIN BUDGET' if not bad else str(bad) + ' CARD(S) OVER BUDGET'}")
    return bad


# =============================================================================================
# Timeline model
# =============================================================================================
def segment_plan():
    """Ordered list of every on-screen beat of the finished video."""
    segs = [{"key": "00_title", "who": "teacher", "text": COURSE_INTRO, "kind": "title",
             "reveal": 0, "scene": None, "qno": 0}]
    for si, sc in enumerate(SCENES, start=1):
        segs.append({"key": f"{sc['id']}__00_question", "who": "student", "text": sc["q_say"],
                     "kind": "question", "reveal": 0, "scene": sc, "qno": si})
        for i, b in enumerate(sc["boxes"]):
            segs.append({"key": f"{sc['id']}__{i + 1:02d}_answer", "who": "teacher", "text": b[3],
                         "kind": "answer", "reveal": i + 1, "scene": sc, "qno": si})
        segs.append({"key": f"{sc['id']}__{len(sc['boxes']) + 1:02d}_hook", "who": "teacher",
                     "text": sc["hook_say"], "kind": "hook", "reveal": len(sc["boxes"]),
                     "scene": sc, "qno": si})
    segs.append({"key": "99_outro", "who": "teacher", "text": COURSE_OUTRO, "kind": "outro",
                 "reveal": 0, "scene": None, "qno": len(SCENES)})
    return segs


def narration_manifest(segs):
    """Group beats into the handful of long audio clips the studio voice will read."""
    by_key = {s["key"]: s for s in segs}
    clips = []
    title = segs[0]
    clips.append({"key": "00_title", "voice": "teacher", "text": normalize_for_tts(title["text"]),
                  "segment_keys": [title["key"]],
                  "segment_texts": [normalize_for_tts(title["text"])]})
    for si, sc in enumerate(SCENES, start=1):
        grp = [s for s in segs if s["scene"] is sc and s["kind"] in ("answer", "hook")]
        txts = [normalize_for_tts(s["text"]) for s in grp]
        clips.append({"key": f"{si:02d}_answer_{sc['id']}", "voice": "teacher",
                      "text": " ".join(txts), "segment_keys": [s["key"] for s in grp],
                      "segment_texts": txts})
    qs = [s for s in segs if s["kind"] == "question"]
    pack = 2
    for gi in range(0, len(qs), pack):
        grp = qs[gi:gi + pack]
        txts = [normalize_for_tts(s["text"]) for s in grp]
        clips.append({"key": f"q{gi // pack:02d}_questions", "voice": "student",
                      "text": " ".join(txts), "segment_keys": [s["key"] for s in grp],
                      "segment_texts": txts})
    outro = segs[-1]
    clips.append({"key": "99_outro", "voice": "teacher", "text": normalize_for_tts(outro["text"]),
                  "segment_keys": [outro["key"]], "segment_texts": [normalize_for_tts(outro["text"])]})
    for c in clips:
        if len(c["text"]) > 1500:
            raise SystemExit(f"clip {c['key']} is {len(c['text'])} chars - over the 1500 TTS limit")
        for k in c["segment_keys"]:
            assert k in by_key, k
    return clips


def dump_narration(segs):
    NARR_DIR.mkdir(parents=True, exist_ok=True)
    clips = narration_manifest(segs)
    (NARR_DIR / "manifest.json").write_text(json.dumps(clips, indent=2, ensure_ascii=False), encoding="utf-8")
    lines = ["# Narration sent to the studio voices",
             "# Every line below is the EXACT text that was spoken (after the Indian-English",
             "# pronunciation pass). Subtitles are generated from this same text.",
             ""]
    for c in clips:
        (NARR_DIR / f"{c['key']}.txt").write_text(c["text"], encoding="utf-8")
        lines += [f"## {c['key']}   [{c['voice']}]   ({len(c['text'])} chars)", c["text"], ""]
    (NARR_DIR / "ALL_NARRATION.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"narration manifest: {NARR_DIR / 'manifest.json'}  ({len(clips)} clips)")
    return clips


# =============================================================================================
# ffmpeg plumbing
# =============================================================================================
def ffmpeg_bin():
    exe = os.environ.get("FFMPEG") or shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


FFMPEG = ffmpeg_bin()


def run(cmd, quiet=True):
    return subprocess.run(cmd, check=True,
                          stdout=subprocess.DEVNULL if quiet else None,
                          stderr=subprocess.DEVNULL if quiet else None)


def probe_duration(path: Path) -> float:
    r = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True)
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", r.stderr)
    if not m:
        raise RuntimeError(f"cannot probe duration: {path}")
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def detect_silences(path: Path, noise=-42.0, min_dur=0.14):
    r = subprocess.run([FFMPEG, "-i", str(path), "-af",
                        f"silencedetect=noise={noise}dB:d={min_dur}", "-f", "null", "-"],
                       capture_output=True, text=True)
    starts = [float(x) for x in re.findall(r"silence_start:\s*([\d.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end:\s*([\d.]+)", r.stderr)]
    out = []
    for i, s in enumerate(starts):
        out.append((s, ends[i] if i < len(ends) else s + min_dur))
    return out


def predict_boundaries(texts, total):
    """Character-weighted estimate of where each beat ends inside a longer clip."""
    w = []
    for t in texts:
        base = len(t) + 1.0
        base += 0.34 * len(re.findall(r"[.!?](?:\s|$)", t))
        base += 0.10 * len(re.findall(r"[,;:](?:\s|$)", t))
        w.append(max(base, 1.0))
    s = sum(w)
    bounds, cum = [], 0.0
    for x in w[:-1]:
        cum += x
        bounds.append(total * cum / s)
    return bounds


def find_studio_audio(key: str):
    for ext in (".wav", ".mp3", ".m4a", ".flac", ".ogg"):
        p = STUDIO_DIR / f"{key}{ext}"
        if p.exists():
            return p
    hits = sorted(STUDIO_DIR.glob(f"{key}.*")) if STUDIO_DIR.exists() else []
    return hits[0] if hits else None


def pick_boundary(sil, p, window=2.0):
    """Snap a predicted beat boundary onto a real pause.

    Beat-boundary pauses are systematically longer than the pauses between sentences inside a
    beat, so score candidates by (pause length - distance penalty) instead of distance alone.
    """
    cands = []
    for a, b in sil:
        mid = (a + b) / 2.0
        dist = abs(mid - p)
        if dist <= window:
            cands.append((mid, (b - a) - 0.5 * dist, dist))
    if not cands:
        return p, None
    mid, _score, dist = max(cands, key=lambda x: x[1])
    return mid, round(mid - p, 3)


def align_all(clips, noise=-42.0, min_dur=0.14, window=2.0, force=False):
    """Split each long studio clip into one audio file per on-screen beat.

    Prediction keeps the split from drifting; detected silence snaps it onto the real
    sentence pause so a card never flips mid-word.
    """
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    report, missing, written = [], [], 0
    for c in clips:
        src = find_studio_audio(c["key"])
        if src is None:
            missing.append(c["key"])
            continue
        total = probe_duration(src)
        texts = c["segment_texts"]
        if len(texts) == 1 and not force:
            cuts = [0.0, total]
            snapped = []
        else:
            sil = detect_silences(src, noise, min_dur)
            pred = predict_boundaries(texts, total)
            cuts, snapped, last = [0.0], [], 0.0
            for p in pred:
                t, off = pick_boundary(sil, p, window)
                t = max(t, last + 0.45)          # keep beats strictly ordered
                last = t
                snapped.append(off)
                cuts.append(t)
            cuts.append(total)
        for i, key in enumerate(c["segment_keys"]):
            out = AUDIO_DIR / f"{key}.wav"
            s = max(0.0, cuts[i] - 0.06)
            e = min(total, cuts[i + 1] + 0.16)
            if out.exists() and not force:
                pass
            else:
                written += 1
                # trim dead air at BOTH ends: a silent tail would otherwise stretch the
                # caption timing for that beat and leave the slide hanging with no words.
                run([FFMPEG, "-y", "-i", str(src),
                     "-af", f"atrim=start={s:.3f}:end={e:.3f},asetpts=N/SR/TB,"
                            f"silenceremove=start_periods=1:start_threshold=-48dB:"
                            f"start_silence=0.02:detection=peak,"
                            f"areverse,"
                            f"silenceremove=start_periods=1:start_threshold=-48dB:"
                            f"start_silence=0.02:detection=peak,"
                            f"areverse",
                     "-ar", "48000", "-ac", "2", str(out)])
            dur = probe_duration(out)
            report.append({"segment": key, "clip": c["key"], "chars": len(texts[i]),
                           "dur": round(dur, 3), "cps": round(len(texts[i]) / max(dur, .01), 1),
                           "snap_offset": (snapped[i] if i < len(snapped) else None)})
    if missing:
        print(f"  SKIPPED {len(missing)} clip(s) with no audio yet: {', '.join(missing)}")
    report.append({"_written": written, "_missing": missing})
    return report


# =============================================================================================
# Subtitles
# =============================================================================================
def timed_words(text, dur):
    toks = text.split()
    if not toks:
        return []
    w = [len(t) + 1.0 for t in toks]
    s = sum(w)
    out, t0 = [], 0.0
    for tok, ww in zip(toks, w):
        seg = dur * ww / s
        out.append((tok, t0, t0 + seg))
        t0 += seg
    return out


_SENT_END = re.compile(r'[.!?]["\')]?$')


def timed_words_anchored(text, audio: Path, dur: float, window: float = 1.2):
    """Word timings for captions, anchored onto the pauses the voice actually took.

    A purely length-weighted spread ignores that sentence-final words are followed by a
    real pause, so it runs progressively late within a beat (measured bias -0.17 s, up to
    2 s on the worst beat). Splitting the beat at sentence ends and snapping those
    boundaries onto detected silence removes the drift (bias -0.07 s).
    """
    toks = text.split()
    if not toks:
        return []
    wl = [len(t) + 1.0 for t in toks]
    groups, cur = [], []
    for i, t in enumerate(toks):
        cur.append(i)
        if _SENT_END.search(t):
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    if len(groups) <= 1:
        return timed_words(text, dur)

    tw = sum(wl)
    preds, cum = [], 0.0
    for grp in groups[:-1]:
        cum += sum(wl[i] for i in grp)
        preds.append(dur * cum / tw)

    sil = detect_silences(audio, -40.0, 0.05)
    bounds, last = [], 0.0
    for p in preds:
        cands = [((a + b) / 2.0, (b - a) - 0.5 * abs((a + b) / 2.0 - p))
                 for a, b in sil if abs((a + b) / 2.0 - p) <= window]
        t = max(cands, key=lambda x: x[1])[0] if cands else p
        t = max(t, last + 0.15)
        last = t
        bounds.append(t)

    out, start = [], 0.0
    for gi, grp in enumerate(groups):
        end = bounds[gi] if gi < len(bounds) else dur
        span = max(end - start, 0.05)
        span_w = max(span - min(0.20, span * 0.12), 0.05)   # leave the trailing pause
        sw = sum(wl[i] for i in grp)
        t0 = start
        for i in grp:
            s = span_w * wl[i] / sw
            out.append((toks[i], t0, t0 + s))
            t0 += s
        start = end
    return out


def make_cues(words, style, total=None, max_words=9, max_chars=44, min_dur=0.75):
    """Chunk timed words into readable captions.

    Cues must TILE the timeline with no overlap: libass treats overlapping events as a
    collision and silently stacks them vertically, which makes captions jump around the
    frame. So every cue ends exactly where the next one begins (less 1 ms).
    """
    chunks, buf = [], []
    for w in words:
        buf.append(w)
        joined = " ".join(x[0] for x in buf)
        if len(buf) >= max_words or len(joined) >= max_chars or w[0].endswith((".", "?", "!")):
            chunks.append(buf)
            buf = []
    if buf:
        chunks.append(buf)

    # merge captions too short to read comfortably
    merged = []
    for ch in chunks:
        if merged:
            pn = len(merged[-1])
            pc = sum(len(x[0]) for x in merged[-1])
            cc = sum(len(x[0]) for x in ch)
            if pn + len(ch) <= max_words + 3 and pc + cc <= max_chars + 10:
                merged[-1] = merged[-1] + ch
                continue
        merged.append(ch)

    last = total if total else (words[-1][2] + 0.12 if words else 0.0)
    cues = []
    for i, ch in enumerate(merged):
        start = ch[0][1]
        end = (merged[i + 1][0][1] - 0.001) if i + 1 < len(merged) else last
        cues.append((start, end, style, " ".join(x[0] for x in ch)))

    # drop any sliver too brief to render (should not happen after merging)
    out = []
    for i, (s, e, st, txt) in enumerate(cues):
        if e - s < 0.12 and out:
            out[-1] = (out[-1][0], e, out[-1][2], out[-1][3] + " " + txt)
        else:
            out.append((s, e, st, txt))
    return out


def _two_line(s, max_chars=42):
    if len(s) <= max_chars:
        return s
    words = s.split()
    best, bestd = None, 10 ** 9
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        d = abs(len(a) - len(b))
        if d < bestd:
            best, bestd = (a, b), d
    return best[0] + "\\N" + best[1]


def fmt_ass(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def write_ass(cues, path: Path):
    head = (
        "[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\nWrapStyle: 2\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, "
        "BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, "
        "Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
        "Style: Default,DejaVu Sans,40,&H00FFFFFF,&H0000E6FF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,3,1,2,170,170,58,1\n"
        "Style: Student,DejaVu Sans,40,&H00F0E442,&H0000E6FF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,3,1,2,170,170,58,1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"
    )
    lines = [head]
    for s, e, style, txt in cues:
        txt = _two_line(txt).replace("{", "(").replace("}", ")")
        lines.append(f"Dialogue: 0,{fmt_ass(s)},{fmt_ass(e)},{style},,0,0,0,,{txt}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def ass_filter_arg(path: Path) -> str:
    p = str(path).replace("\\", "/").replace(":", "\\:")
    return f"subtitles='{p}':fontsdir=/usr/share/fonts/truetype/dejavu"


# =============================================================================================
# Build
# =============================================================================================
PAD = {"question": PAD_QUESTION, "hook": PAD_HOOK, "answer": PAD_ANSWER,
       "title": PAD_TITLE, "outro": PAD_OUTRO}


def render_slides(segs, total):
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)
    for s in segs:
        out = SLIDES_DIR / f"{s['key']}.png"
        if s["kind"] == "title":
            render_title_card(total, out)
        elif s["kind"] == "outro":
            render_outro_card(total, out)
        else:
            render_frame(s["scene"], s["qno"], total, s["reveal"], s["kind"], out)
    return [SLIDES_DIR / f"{s['key']}.png" for s in segs]


def build_clips(segs, slides):
    CLIPS_DIR.mkdir(parents=True, exist_ok=True)
    clips = []
    for s, slide in zip(segs, slides):
        aud = AUDIO_DIR / f"{s['key']}.wav"
        if not aud.exists():
            raise SystemExit(f"missing audio for {s['key']} - run --align first")
        adur = probe_duration(aud)
        dur = adur + PAD[s["kind"]]
        ass = CLIPS_DIR / f"{s['key']}.ass"
        words = timed_words_anchored(normalize_for_tts(s["text"]), aud, adur)
        cues = make_cues(words, "Student" if s["who"] == "student" else "Default", total=adur)
        write_ass(cues, ass)
        out = CLIPS_DIR / f"{s['key']}.mp4"
        run([FFMPEG, "-y", "-loop", "1", "-framerate", "30", "-i", str(slide), "-i", str(aud),
             "-vf", ass_filter_arg(ass), "-af", "apad", "-t", f"{dur:.3f}",
             "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-crf", "17",
             "-g", "60", "-r", "30", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(out)])
        clips.append(out)
    return clips


def mux(clips, out_path: Path):
    lst = BUILD_DIR / f"{out_path.stem}_concat.txt"
    lst.write_text("\n".join(f"file '{c.resolve()}'" for c in clips) + "\n", encoding="utf-8")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
         # loudnorm's internal rate is 192 kHz; resample back so we do not ship 96 kHz audio.
         # Do NOT ask for resampler=soxr here: it trips an assertion in ffmpeg's filter graph.
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out_path)])
    return out_path


def add_chapter_marks(video: Path, segs, clip_durs):
    """Embed chapter metadata so players show a navigable chapter list."""
    meta = BUILD_DIR / f"{video.stem}_chapters.txt"
    lines = [";FFMETADATA1"]
    t = 0.0
    starts = {}
    for s, d in zip(segs, clip_durs):
        if s["kind"] in ("title", "outro"):
            t += d
            continue
        q = s["qno"]
        if q not in starts:
            starts[q] = t
        t += d
    order = sorted(starts)
    for i, q in enumerate(order):
        st = starts[q]
        en = starts[order[i + 1]] if i + 1 < len(order) else t
        sc = SCENES[q - 1]
        label = sc["chapter"].split("•", 1)[-1].strip().title()
        lines += ["[CHAPTER]", "TIMEBASE=1/1000",
                  f"START={int(st * 1000)}", f"END={int(en * 1000)}",
                  f"title=Chapter {q} - {label}", ""]
    meta.write_text("\n".join(lines), encoding="utf-8")
    tmp = video.with_suffix(".chapters.mp4")
    run([FFMPEG, "-y", "-i", str(video), "-i", str(meta),
         "-map_metadata", "1", "-map_chapters", "1", "-codec", "copy", str(tmp)])
    shutil.move(str(tmp), str(video))
    return len(order)


def verify(path: Path, expected_min: float):
    d = probe_duration(path)
    r = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True)
    has_v = "Stream #" in r.stderr and "Video:" in r.stderr
    has_a = "Audio:" in r.stderr
    size = path.stat().st_size / 1048576
    ok = has_v and has_a and abs(d - expected_min * 60) < 60
    print(f"  {path.name}: {d/60:.2f} min | video={has_v} audio={has_a} | {size:.1f} MB | "
          f"{'OK' if ok else 'CHECK'}")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true", help="card-density table and exit")
    ap.add_argument("--dump-narration", action="store_true", help="write narration manifest + text files")
    ap.add_argument("--align", action="store_true", help="split studio_raw clips into per-beat audio")
    ap.add_argument("--align-force", action="store_true", help="re-split even if audio exists")
    ap.add_argument("--preview", action="store_true", help="render slide PNGs only")
    ap.add_argument("--build", action="store_true", help="render + mux main video and per-chapter cuts")
    ap.add_argument("--chapter-wise", action="store_true", help="also export one mp4 per chapter")
    args = ap.parse_args()

    if not (args.audit or args.dump_narration or args.align or args.align_force
            or args.preview or args.build):
        ap.print_help()
        return

    if args.audit:
        sys.exit(1 if audit_density() else 0)

    write_reference_sheet()
    if audit_density():
        sys.exit("Build stopped: fix the over-dense cards listed above.")

    segs = segment_plan()
    total = len(SCENES)
    print(f"{len(SCENES)} chapters | {sum(len(s['boxes']) for s in SCENES)} cards | "
          f"{len(segs)} timeline beats")

    if args.dump_narration:
        clips = dump_narration(segs)
        print(f"total narration: {sum(len(c['text']) for c in clips)} chars")
        return

    if args.align or args.align_force:
        if not FFMPEG:
            sys.exit("ffmpeg not found (set FFMPEG=... or pip install imageio-ffmpeg)")
        clips = json.loads((NARR_DIR / "manifest.json").read_text(encoding="utf-8"))
        raw = align_all(clips, force=args.align_force)
        meta = [r for r in raw if "_written" in r]
        rep = [r for r in raw if "_written" not in r]
        (BUILD_DIR / "alignment_report.json").write_text(json.dumps(rep, indent=2), encoding="utf-8")
        cps = [r["cps"] for r in rep if r["dur"] > 0.6]
        med = sorted(cps)[len(cps) // 2] if cps else 0
        bad = [r for r in rep if r["dur"] > 0.6 and not (0.55 * med <= r["cps"] <= 1.8 * med)]
        print(f"aligned {len(rep)} beats | median {med:.1f} chars/sec | "
              f"{sum(1 for r in rep if r['snap_offset'] is not None)} snapped to silence")
        for r in bad:
            print(f"  OUTLIER {r['segment']}: {r['cps']} cps ({r['dur']}s, {r['chars']} chars)")
        return

    if not FFMPEG:
        sys.exit("ffmpeg not found (set FFMPEG=... or pip install imageio-ffmpeg)")

    slides = render_slides(segs, total)
    print(f"rendered {len(slides)} slides -> {SLIDES_DIR}")
    if args.preview:
        return

    if args.build:
        print("building clips (subtitles burned per beat)...")
        clips = build_clips(segs, slides)
        mins = sum(probe_duration(c) for c in clips) / 60
        print(f"  {len(clips)} clips | timeline {mins:.2f} min")
        main_mp4 = ROOT / f"{OUT_STEM}.mp4"
        mux(clips, main_mp4)
        n_ch = add_chapter_marks(main_mp4, segs, [probe_duration(c) for c in clips])
        print(f"  embedded {n_ch} chapter markers")
        print("verifying...")
        verify(main_mp4, mins)
        if args.chapter_wise:
            by_ch = {}
            for s, c in zip(segs, clips):
                if s["kind"] in ("title", "outro"):
                    continue
                by_ch.setdefault(s["qno"], []).append(c)
            outdir = ROOT / "chapters"
            outdir.mkdir(exist_ok=True)
            for qno in sorted(by_ch):
                name = f"ch{qno:02d}_{SCENES[qno - 1]['id']}.mp4"
                mux(by_ch[qno], outdir / name)
                verify(outdir / name, sum(probe_duration(c) for c in by_ch[qno]) / 60)


if __name__ == "__main__":
    main()
