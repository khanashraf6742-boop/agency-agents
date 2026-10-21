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
BUILD_DIR = ROOT / "build"
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
CLIPS_DIR = BUILD_DIR / "clips"
STUDIO_DIR = ROOT / "studio_raw"
NARR_DIR = ROOT / "narration"
OUT_STEM = "tech_resignation_masterclass"

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

TITLE_HEAD = "TECHNICAL RESIGNATION & LIEN"
TITLE_SUB = "DoPT O.M. No. DOPT-1669266628362  •  dated 24.11.2022"
TITLE_META = "Complete Masterclass  •  16 Chapters  •  64 Exam-Ready Cards"

COURSE_INTRO = (
    "Welcome to the complete masterclass on technical resignation and lien. "
    "We will walk through the entire consolidated DoPT guidelines of twenty fourth November, "
    "twenty twenty two, paragraph by paragraph. Every chapter ends with the exact trap that "
    "examiners love. Let us begin with Riya's first question."
)

COURSE_OUTRO = (
    "That brings us to the end of this masterclass. Revise the four traps we covered, and "
    "remember the golden rule: a technical resignation protects your past service only when "
    "it is submitted through proper channel to take up another government post. "
    "Keep revising, and see you in the next chapter."
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
        "id": "c01_01_tech_resig_definition",
        "chapter": "CHAPTER 1 • PARA 2.1.1: MEANING OF TECHNICAL RESIGNATION",
        "title": "PARA 2.1.1 — WHAT MAKES A RESIGNATION 'TECHNICAL' UNDER RULES?",
        "accent": SKY, "badge": "PARA 2.1.1",
        "q": "What conditions must be satisfied for a resignation to be treated as a Technical Resignation?",
        "intro": ("Welcome to the Masterclass on Technical Resignation and Lien! We will explore the entire "
                  "consolidated guidelines of 24 November 2022 step by step. Let us hear Riya's first question."),
        "q_say": "Sir, when an employee resigns to join another Government post, what makes it a Technical Resignation?",
        "flow": "tech_resig_flow",
        "boxes": [
            ("APPLIED THROUGH PROPER CHANNEL",
             "Must apply through proper channel for a post in same or other Dept, and resign for administrative reasons.",
             "Para 2.1.1: As per Ministry of Finance OM No. 3379-E.III(B)/65 dated 17.06.1965, resignation is treated as a technical formality where a Government servant has applied through proper channel for a post in the same or some other Department, and is on selection, required to resign the previous post for administrative reasons.",
             SKY,
             "Let us take the rule first. Under Para 2.1.1, resignation is a technical formality when an employee applies through proper channel for a post and is required to resign for administrative reasons upon selection."),
            ("WORD 'TECHNICAL' NOT MANDATORY",
             "Treated as technical resignation if conditions are met, even if the word 'Technical' is NOT written.",
             "Para 2.1.1: The resignation will be treated as technical resignation if these conditions are met, even if the Government servant has not mentioned the word 'Technical' while submitting his resignation. Past service benefits are protected.",
             GREEN,
             "Here is a great relief: even if the employee forgets to write the word 'Technical' in his resignation letter, it is still treated as a technical resignation if the conditions are met."),
            ("NO BENEFIT IF UNAPPROVED OR AD-HOC",
             "No technical resignation benefit if application was not through proper channel, or if held on ad-hoc basis.",
             "Para 2.1.1: Resignation where the competent authority has not allowed the Government servant to forward the application through proper channel will not be treated as technical resignation. Also, no benefit of technical resignation arises from an ad-hoc post.",
             ORANGE,
             "Now look at the exclusions. If the competent authority refused permission to forward the application, or if the employee held the post on an ad-hoc basis, no technical resignation benefit is allowed."),
            ("THE TRAP: AD-HOC SERVICE",
             "Trap: Resigning from an ad-hoc post can NEVER be a Technical Resignation, even if selected through UPSC!",
             "Exam Trap (Para 2.1.1): Service rendered on an ad-hoc basis carries no lien and no technical resignation rights. Past service benefits will be forfeited.",
             RED,
             "Be careful of this trap: resignation from a purely ad-hoc appointment can never be treated as technical resignation, and past service benefits are lost."),
        ],
        "hook": "REMEMBER: Applied Through Proper Channel + Administrative Resignation = Technical Resignation!",
        "hook_say": "Remember: Applying through proper channel and resigning for administrative reasons makes it a Technical Resignation, even if the word is omitted.",
        "covers": ["P2.1.1"],
    },
    {
        "id": "c01_02_pre_joining_applications",
        "chapter": "CHAPTER 2 • PARA 2.1.2: POSTS APPLIED FOR BEFORE JOINING GOVERNMENT",
        "title": "PARA 2.1.2 — CAN PRE-JOINING APPLICATIONS QUALIFY FOR TECHNICAL RESIGNATION?",
        "accent": ORANGE, "badge": "PARA 2.1.2",
        "q": "Can an employee get technical resignation benefits for an exam applied for before joining Government service?",
        "q_say": "Sir, what if an officer applied for an exam before joining the Government and gets selected later?",
        "boxes": [
            ("BENEFIT ADMISSIBLE ON CONDITIONS",
             "Benefit of past service is admissible for pre-joining applications, subject to three strict conditions.",
             "Para 2.1.2: This benefit is also admissible to Government servants who have applied before joining the Government service and on that account the application was not routed through proper channel, subject to fulfilling three conditions.",
             SKY,
             "Under Para 2.1.2, you can still claim technical resignation for an exam you applied for before entering Government service, provided you satisfy three mandatory conditions."),
            ("CONDITION 1: INTIMATE IMMEDIATELY",
             "Condition (i): The Government servant must intimate details of such application IMMEDIATELY on joining.",
             "Para 2.1.2(i): 'the Government servant should intimate the details of such application immediately on their joining.' Failure to intimate on joining bars the benefit later.",
             GREEN,
             "Condition number one: you must formally intimate the full details of all pending applications immediately upon joining your new post. Do not wait for interview calls."),
            ("CONDITION 2 & 3: REQUEST & PROPER CHANNEL TEST",
             "Condition (ii): Specific resignation request. Condition (iii): Authority satisfies that it would have forwarded it.",
             "Para 2.1.2(ii)-(iii): (ii) Specific request at resignation stating he is resigning to take up appointment applied before joining; (iii) Accepting authority satisfies itself that had the employee been in service on application date, the application would have been forwarded through proper channel.",
             ORANGE,
             "Conditions two and three: you must submit a specific resignation request naming that exam, and the authority must be satisfied that the application would have been forwarded had you been in service."),
            ("WORKED EXAMPLE: ROHAN'S TIMELINE",
             "Example: Rohan applied for CGL in March, joined Dept in July, intimates in July. Selected next year -> Technical Resignation granted!",
             "Example: Rohan applies for an exam in March 2024 as a private citizen. He joins Department A on 01.07.2024 and submits a written intimation on 02.07.2024. When selected in 2025, his resignation is treated as technical resignation.",
             RED,
             "Here is a real example: Rohan applied for an exam in March and joined Government in July. By intimating his department in July, his resignation next year is fully accepted as technical resignation."),
        ],
        "hook": "REMEMBER: Pre-Joining Applications Qualify ONLY If Intimated Immediately On Joining!",
        "hook_say": "Remember: Pre-joining job applications qualify for technical resignation only if intimated in writing immediately upon joining.",
        "covers": ["P2.1.2"],
        "calc_asserts": ["NO_MATH"],
    },
    {
        "id": "c01_03_leave_carry_forward",
        "chapter": "CHAPTER 3 • PARA 2.2: CARRY FORWARD OF LEAVE & 300-DAY PSU CASH BENEFIT",
        "title": "PARA 2.2 — WHAT HAPPENS TO EARNED LEAVE, HPL AND CHILD CARE LEAVE?",
        "accent": GREEN, "badge": "PARA 2.2 • LEAVE",
        "q": "Does accumulated leave lapse on technical resignation, and what happens on permanent absorption in a PSU?",
        "q_say": "Sir, when an officer submits a technical resignation, does he lose his Earned Leave, and what happens to Child Care Leave?",
        "boxes": [
            ("RULE 9(2): ALL LEAVES CARRIED FORWARD",
             "Rule 9(2) CCS (Leave) Rules: Technical resignation does not cause leave to lapse. CCL and all leaves carry forward.",
             "Para 2.2(i) (DoPT OM 13/24/92-Estt(Pay-I) dated 22.01.1993): In terms of Rule 9(2) of the CCS (Leave) Rules, 1972, technical resignation shall not result in the lapse of leave to the credit of the Government servant. The balance of unutilized Child Care Leave (CCL) as well as all other leaves of the kind due & admissible will be carried forward.",
             SKY,
             "Under Para 2.2 and Rule 9, sub-rule 2 of C.C.S. Leave Rules, technical resignation never lapses your leave. Your entire balance of Earned Leave, Half Pay Leave, and Child Care Leave carries forward intact."),
            ("RULE 39-D: CASH EQUIVALENT ON PSU ABSORPTION",
             "Rule 39-D: On permanent absorption in PSU/Autonomous Body/State Govt, cash equivalent of EL & HPL granted up to 300 days.",
             "Para 2.2(ii): 'As per rule 39-D of the CCS(Leave) Rules, 1972, in case of permanent absorption in PSUs/ Autonomous Bodies/ State Government etc., the Government servant shall be granted cash equivalent of leave salary in respect of EL & HPL at his credit subject to overall limit of 300 days.'",
             GREEN,
             "Now see what happens on permanent absorption into a P.S.U. or State Government under Rule 39-D: the officer is paid the cash equivalent of his accumulated Earned Leave and Half Pay Leave, up to 300 days."),
            ("WORKED EXAMPLE: PRIYA'S LEAVE BALANCE",
             "Example: Priya has 180 days EL, 40 days HPL, 100 days CCL. Technical resignation to Dept B -> all 320 days carry forward!",
             "Example: Priya technical resigns from Ministry of Finance to join Ministry of External Affairs. Her 180 days EL, 40 days HPL, and 100 days CCL are credited in full to her new leave account in MEA.",
             ORANGE,
             "Here is an example: Priya moves to another Ministry on technical resignation with 180 days Earned Leave, 40 days Half Pay Leave, and 100 days Child Care Leave. All 320 days carry forward seamlessly."),
            ("THE TRAP: GENERAL RESIGNATION FORFEITS LEAVE",
             "Trap: A non-technical resignation forfeits all accumulated leave; only Technical Resignation protects leave under Rule 9(2)!",
             "Exam Trap (Para 2.2): If a resignation is not accepted as technical resignation, the entire leave balance lapses immediately under Rule 9(1).",
             RED,
             "Remember the contrast: under ordinary resignation, all leave lapses immediately. Only technical resignation preserves your leave under Rule 9, sub-rule 2."),
        ],
        "hook": "REMEMBER: Technical Resignation Protects ALL Leave (Incl. CCL) • PSU Absorption Encashment Up to 300 Days!",
        "hook_say": "Remember: Technical resignation carries forward all leaves including Child Care Leave, and P.S.U. absorption grants leave encashment up to 300 days.",
        "covers": ["P2.2"],
        "calc_asserts": ["180 + 40 + 100 == 320"],
    },
    {
        "id": "c01_04_ltc_fresh_recruit_rule",
        "chapter": "CHAPTER 4 • PARA 2.3: LTC CARRY FORWARD & THE 8-YEAR FRESH RECRUIT RULE",
        "title": "PARA 2.3 — HOW DOES LTC CARRY FORWARD? THE 8-YEAR FRESH RECRUIT RULE",
        "accent": BLUE, "badge": "PARA 2.3 • LTC",
        "q": "How is LTC entitlement regulated after technical resignation, and how does the 8-year fresh recruit window work?",
        "q_say": "Sir, fresh recruits get Home Town LTC for three years and All India LTC in the fourth year. How does this apply after technical resignation?",
        "boxes": [
            ("LTC ENTITLEMENT CARRIED FORWARD",
             "LTC entitlement carries forward when joining another Central Government post after Technical Resignation.",
             "Para 2.3: Entitlement to LTC may be carried forward in case of a Central Government Servant who joins another post after having submitted Technical Resignation.",
             SKY,
             "Under Para 2.3, your entitlement to Leave Travel Concession carries forward into your new post after technical resignation."),
            ("THE 8-YEAR RULE EXPLAINED",
             "Fresh recruit LTC applies for an aggregate of 8 years from initial appointment. Remainder transfers to new department.",
             "Para 2.3: 'In case of a Government Servant who resigns within 8 years of his appointment and joins another post in the Government after Technical Resignation, the Government Servant will be treated as a fresh recruit for a period of 8 years from the date of his initial appointment under Government.'",
             GREEN,
             "Fresh recruits enjoy special yearly L.T.C. for their first 8 years. If you submit a technical resignation within those 8 years, you are treated as a fresh recruit only for the remaining balance of that 8-year window."),
            ("WORKED EXAMPLE: 4 YEARS + 4 YEARS",
             "Example: Amit serves 4 years in Dept A, then technical resigns to Dept B. He gets fresh recruit LTC for exactly 4 MORE years.",
             "Para 2.3 verbatim example: 'Thus if a Government Servant joins another Department after serving in Government for 4 years, he will be treated as a fresh recruit for 4 years in the new Department.' Total fresh recruit period = 4 + 4 = 8 years.",
             ORANGE,
             "Here is the official example: Amit serves 4 years in his first department and moves on technical resignation. He gets fresh recruit L.T.C. for exactly 4 more years in his new department."),
            ("THE TRAP: DOES NOT RESET TO ZERO",
             "Trap: Technical resignation does NOT reset the 8-year clock back to 8 years! You get 8 minus years already served.",
             "Exam Trap (Para 2.3): Candidates often mistakenly assume the 8-year fresh recruit clock starts afresh from year 1. It does NOT; it runs strictly from the date of initial appointment.",
             RED,
             "Watch out for this exam trap: technical resignation does not give you a brand new 8-year clock. It only gives you the remaining balance of your original 8 years."),
        ],
        "hook": "REMEMBER: Fresh Recruit LTC Window = 8 Years From Initial Appointment • Balance Transfers to New Post!",
        "hook_say": "Remember: The fresh recruit L.T.C. window is 8 years from your first appointment, and only the remaining balance transfers to your new post.",
        "covers": ["P2.3"],
        "calc_asserts": ["8 - 4 == 4"],
    },
    {
        "id": "c01_05_pay_protection_increments",
        "chapter": "CHAPTER 5 • PARA 2.4: PAY PROTECTION & MINIMUM PERIOD FOR ANNUAL INCREMENT",
        "title": "PARA 2.4 — HOW DOES PAY PROTECTION (FR 22-B) & ANNUAL INCREMENT (FR 26) OPERATE?",
        "accent": RED, "badge": "PARA 2.4 • PAY",
        "q": "How is pay protected after technical resignation, and does past service count towards the next annual increment?",
        "q_say": "Sir, if an officer joins a post with lower entry pay, will his salary be reduced? And what happens to his annual increment?",
        "boxes": [
            ("PAY PROTECTION UNDER PROVISO TO FR 22-B",
             "If pay fixed in new post is less than substantive pay in old post, he draws presumptive pay under FR 9(24).",
             "Para 2.4: In cases of appointment of a Government servant to another post in Government on acceptance of technical resignation, protection of pay is given in terms of Ministry of Finance OM No. 3379-E.III(B)/65 dated 17.06.1965 read with proviso to FR 22-B. Thus, if pay fixed in the new post is less than his pay in the post he holds substantively, he will draw the presumptive pay of the post he holds substantively as defined in FR 9(24).",
             SKY,
             "Under Para 2.4 and the proviso to F.R. 22-B, your pay is protected. If the pay fixed in your new post is less than what you substantively earned, you draw presumptive pay under F.R. 9, clause 24."),
            ("PAST SERVICE COUNTS FOR INCREMENT (FR 26)",
             "Past service counts towards the minimum 6-month qualifying period for annual increment under FR 26 & Rule 10 of CCS (RP) Rules.",
             "Para 2.4: 'Past service rendered by such a Government servant is taken into account for reckoning of the minimum period for grant of annual increment in the new post/service/ cadre in Government under the provisions of FR 26 read with Rule 10 of CCS (RP) Rules, 2016.'",
             GREEN,
             "Under F.R. 26 and Rule 10 of the Revised Pay Rules, your past service counts toward the minimum 6 months needed for your annual increment. Your increment clock does not reset."),
            ("INCREMENTS PROTECTED ON REVERSION",
             "If the Government servant rejoins his earlier post, he is entitled to increments for the period of his absence.",
             "Para 2.4: 'In case the Government servant rejoins his earlier posts, he will be entitled to increments for the period of his absence from that post.'",
             ORANGE,
             "And what if you decide to revert to your old post? Under Para 2.4, you are granted all notional increments for the entire period of your absence."),
            ("THE TRAP: SUBSTANTIVE PAY ONLY",
             "Trap: Pay protection applies to substantive pay; officiating pay in an ad-hoc post is NOT protected under FR 22-B!",
             "Exam Trap (Para 2.4): Protection under FR 22-B is strictly anchored to the substantive pay held in the regular parent post.",
             RED,
             "Be careful: pay protection covers only your substantive regular pay. Any officiating pay drawn on an ad-hoc basis is not protected."),
        ],
        "hook": "REMEMBER: Pay Protected Via Presumptive Pay (FR 22-B) • Past Service Counts for Annual Increment (FR 26)!",
        "hook_say": "Remember: Pay is protected via presumptive pay under F.R. 22-B, and past service counts toward your next annual increment.",
        "covers": ["P2.4"],
    },
    {
        "id": "c01_06_seniority_reversion_penalty",
        "chapter": "CHAPTER 6 • PARA 2.6: SUBSTANTIVE SENIORITY & PROMOTION PENALTY ON REVERSION",
        "title": "PARA 2.6 — WHAT HAPPENS TO SENIORITY AND PROMOTION ELIGIBILITY ON REVERSION?",
        "accent": YELLOW, "badge": "PARA 2.6",
        "q": "Is seniority protected after technical resignation, and does time spent in the new department count for promotion back home?",
        "q_say": "Sir, if an officer returns to his parent department within his lien period, does the time spent outside count for promotion?",
        "boxes": [
            ("SUBSTANTIVE SENIORITY PROTECTED",
             "Seniority in the post held on substantive basis continues to be protected upon Technical Resignation.",
             "Para 2.6: 'On technical resignation, seniority in the post held by the Government servant on substantive basis continues to be protected.'",
             SKY,
             "Under Para 2.6, your seniority in your substantive parent post remains fully protected throughout your technical resignation."),
            ("PROMOTION PENALTY ON REVERSION",
             "If deciding to rejoin substantive post, period spent in other department does NOT count for promotion qualifying service!",
             "Para 2.6: 'However, in case of a Government servant deciding to rejoin his substantive post, the period spent in another department which he had joined after submitting his technical resignation will not count for minimum qualifying service for promotion in the higher post.'",
             GREEN,
             "Now look at the major penalty if you return: the time you spent working in the other department will not count toward the qualifying service required for promotion back home."),
            ("WORKED EXAMPLE: VIKAS REVERTS",
             "Example: Vikas needs 5 yrs service for Section Officer. Serves 3 yrs in parent, 2 yrs in new Dept, then reverts. Qualifying service = 3 yrs (NOT 5)!",
             "Example: Vikas has 3 years substantive service as Assistant Section Officer (ASO). He technical resigns, spends 2 years in another Department, and then reverts to his parent cadre. For promotion to Section Officer, his qualifying service is only 3 years. The 2 years spent outside are wiped out.",
             ORANGE,
             "Here is a clear example: Vikas serves 3 years as an A.S.O., spends 2 years in another department, and reverts. For promotion to Section Officer, his qualifying service is only 3 years, not 5."),
            ("THE TRAP: SENIORITY VS QUALIFYING SERVICE",
             "Trap: Substantive seniority list position is retained, BUT promotion qualifying service clock is paused while outside!",
             "Exam Trap (Para 2.6): Do not confuse seniority with eligibility service. Your rank on the seniority list is preserved, but you cannot be promoted until you complete the required physical service years.",
             RED,
             "Spot the distinction: your name stays in its original spot on the seniority list, but your promotion clock stops ticking while you are away."),
        ],
        "hook": "REMEMBER: Substantive Seniority Protected • Time Outside Does NOT Count for Promotion on Reversion!",
        "hook_say": "Remember: Substantive seniority is protected, but time spent outside does not count toward promotion eligibility if you revert.",
        "covers": ["P2.6"],
        "calc_asserts": ["3 + 2 == 5"],
    },
    {
        "id": "c01_07_pension_schemes_and_nps",
        "chapter": "CHAPTER 7 • PARAS 2.5, 2.7 & 2.8: GPF, OLD PENSION (PRE-2004) & NPS PORTABILITY",
        "title": "PARAS 2.5, 2.7 & 2.8 — HOW ARE GPF, PRE-2004 PENSION & NPS PRAN TRANSFERRED?",
        "accent": PINK, "badge": "PENSION & NPS",
        "q": "What happens to Old Pension coverage (pre-2004) and NPS PRAN accounts upon technical resignation?",
        "q_say": "Sir, if an employee appointed before 2004 submits a technical resignation to join a new post today, does he get pushed into NPS?",
        "boxes": [
            ("PRE-2004 ENTRANTS RETAIN OLD PENSION (2.7)",
             "Rule 26(2) CCS (Pension) Rules: Pre-2004 entrants joining a pensionable post continue under CCS (Pension) Rules, 1972.",
             "Para 2.7 (DoP&PW OM 28/30/2004-P&PW(B) dated 26.07.2005): Government servants who originally joined service prior to 01.01.2004, on technical resignation to join another post in a pensionable establishment, continue to be covered under CCS (Pension) Rules, 1972 even if they join the new post after 01.01.2004 under Rule 26(2).",
             SKY,
             "Under Para 2.7 and Rule 26, sub-rule 2 of C.C.S. Pension Rules, officers who originally joined before 1 January 2004 remain under the Old Pension Scheme when they submit a technical resignation to take up a pensionable post today."),
            ("NPS PRAN & BALANCE PORTABILITY (2.8)",
             "NPS employees: Balance in Personal Retirement Account (PRA) along with PRAN is seamlessly carried forward to new office.",
             "Para 2.8: 'In case of 'Technical Resignation' of Government servant covered under National Pension System (NPS), the balance standing to their Personal Retirement Account (PRA) along-with their PRAN will be carried forward to the new office.'",
             GREEN,
             "For N.P.S. employees under Para 2.8, your P.R.A.N. account and entire accumulated balance are seamlessly transferred to your new office without any deduction."),
            ("GPF TRANSFER (PARA 2.5)",
             "Transfer of GPF balance is governed by Rule 35 of General Provident Fund (Central Services) Rules, 1960.",
             "Para 2.5: Transfer of GPF on technical resignation would be governed by Rule 35 of the General Provident Fund (Central Services) Rules, 1960, crediting the balance with accrued interest to the new account.",
             ORANGE,
             "Under Para 2.5, your General Provident Fund balance is transferred along with all accrued interest to your new office under Rule 35 of the G.P.F. Rules."),
            ("THE TRAP: NON-PENSIONABLE BODIES",
             "Trap: Joining an autonomous body with an autonomous CPF scheme may terminate Old Pension coverage under CCS Pension Rules!",
             "Exam Trap (Para 2.7): Para 2.7 applies only if the new post is in a 'pensionable establishment'. If the new post is non-pensionable, Rule 26(2) does not apply.",
             RED,
             "Watch out for this condition: pre-2004 entrants keep Old Pension only if the new department is a pensionable establishment under Government."),
        ],
        "hook": "REMEMBER: Pre-2004 Entrants KEEP Old Pension • NPS PRAN Transfers Seamlessly!",
        "hook_say": "Remember: Pre-2004 entrants keep their Old Pension coverage, and N.P.S. P.R.A.N. accounts transfer seamlessly.",
        "covers": ["P2.5", "P2.7", "P2.8"],
    },
    {
        "id": "c01_08_service_book_medical_character",
        "chapter": "CHAPTER 8 • PARAS 2.9 TO 2.11: SERVICE BOOK, MEDICAL EXAM & ANTECEDENTS",
        "title": "PARAS 2.9 TO 2.11 — ARE FRESH MEDICAL EXAMS AND POLICE VERIFICATIONS REQUIRED?",
        "accent": SKY, "badge": "PARAS 2.9–2.11",
        "q": "Does an officer need a fresh medical examination and police verification upon technical resignation?",
        "q_say": "Sir, when an officer submits a technical resignation, does he have to undergo another medical board and police verification?",
        "boxes": [
            ("SERVICE BOOK TRANSFER (SR 198)",
             "SR 198: Service Book maintained from first appointment, kept in custody of Head of Office, transfers office to office.",
             "Para 2.9 (SR 198): As per SR 198, the Service Book is to be maintained for a Government servant from the date of first appointment, kept in the custody of the Head of Office, and transferred with him from office to office upon technical resignation.",
             SKY,
             "Under Supplementary Rule 198, your original Service Book is maintained from day one and travels with you from department to department."),
            ("NO FRESH MEDICAL IF STANDARDS MATCH (2.10)",
             "If already examined by Medical Board and medical standard for new post is same or lower, NO fresh exam required.",
             "Para 2.10: In cases where a person has already been examined by a Medical Board in respect of his previous appointment and if standard of medical examination prescribed for the new post is the same, then he need not be required to undergo a fresh examination.",
             GREEN,
             "Under Para 2.10, if you were already examined by a Medical Board and the medical standard of your new post is the same, no fresh medical examination is needed."),
            ("POLICE VERIFICATION: 1-YEAR RULE (2.11)",
             "If gap between discharge and new post is LESS than 1 year, reference to old office suffices. Over 1 year = fresh verification.",
             "Para 2.11 (OM 18011/9(s)/78-Estt(B) dated 02.07.1982): If the intervening period between discharge from previous office and securing new appointment is less than 1 year, reference to previous office certifying character/antecedents suffices. If more than 1 year has lapsed, full verification is carried out afresh.",
             ORANGE,
             "Under Para 2.11, if the gap between leaving your old post and joining the new one is under 1 year, a simple verification check with your previous office is enough. Over 1 year requires a fresh verification."),
            ("THE TRAP: DIFFERENT MEDICAL STANDARDS",
             "Trap: If the new post prescribes a higher medical standard (e.g. pilot, field police), a fresh medical exam is MANDATORY!",
             "Exam Trap (Para 2.10): The exemption from a medical exam applies ONLY if the prescribed standard is identical or lower. A higher physical/medical standard demands a fresh board.",
             RED,
             "Remember the limitation in Para 2.10: if your new job requires a higher physical or vision standard, a fresh medical board is mandatory."),
        ],
        "hook": "REMEMBER: Service Book Transfers (SR 198) • No Fresh Medical If Standards Match • 1-Year Antecedents Rule!",
        "hook_say": "Remember: The Service Book transfers with you, no fresh medical is needed if standards match, and police verification follows the 1-year rule.",
        "covers": ["P2.9", "P2.10", "P2.11"],
    },
    {
        "id": "c01_09_lien_definition_acquisition",
        "chapter": "CHAPTER 9 • PARA 3.1: LIEN DEFINITION & CONFIRMATION IN SERVICE",
        "title": "PARA 3.1 — WHAT IS A LIEN (FR 9(13)) AND WHO HOLDS IT?",
        "accent": GREEN, "badge": "PARA 3.1 • LIEN",
        "q": "What is the legal definition of a Lien, and who acquires a lien on a Government post?",
        "q_say": "Sir, we often hear that an officer has a lien on his post. What does 'Lien' mean in law, and who gets it?",
        "boxes": [
            ("LEGAL DEFINITION (FR 9(13))",
             "FR 9(13): Lien is the right of a Government employee to hold a regular post, permanent or temporary, immediately or after absence.",
             "Para 3.1.1 (OM 18011/1/86-Estt(D) dated 28.03.1998): Lien is defined in FR 9(13). It represents the right of a Government employee to hold a regular post, whether permanent or temporary, either immediately or on the termination of the period of absence.",
             SKY,
             "Under Fundamental Rule 9, clause 13, a Lien is your legal right to hold a regular post, whether permanent or temporary, either immediately or upon returning from absence."),
            ("WHO ACQUIRES A LIEN?",
             "Acquired by: (1) Confirmed employees; (2) Promoted employees declared to have completed probation; (3) Regular promotions without probation.",
             "Para 3.1.1: The benefit of having a lien is enjoyed by all employees who are confirmed in the post/service/cadre of entry, or who have been promoted to a higher post and declared as having completed probation where prescribed, or promoted on regular basis where no probation is prescribed.",
             GREEN,
             "Who holds a lien? Anyone confirmed in their entry post, anyone promoted who has completed probation, or anyone regularly promoted where no probation is prescribed."),
            ("JUNIOR-MOST REVERSION CONDITION (3.1.2)",
             "Subject to condition: Junior-most person in cadre is liable to be reverted if number of entitled persons exceeds available posts.",
             "Para 3.1.2: The right of lien is subject to the condition that the junior-most person in the cadre will be liable to be reverted to the lower post/service/cadre if at any time the number of persons so entitled is more than the posts available in that cadre/service.",
             ORANGE,
             "Under Para 3.1.2, if an officer returns from deputation and posts fall short, the junior-most person in that cadre must be reverted to accommodate the returning officer."),
            ("THE TRAP: PROBATIONERS HAVE NO LIEN",
             "Trap: An unconfirmed probationer does NOT have a lien on his entry post; lien is acquired ONLY upon confirmation!",
             "Exam Trap (Para 3.1.1): A direct recruit on probation has no lien under FR 9(13). If he resigns before confirmation, he has no post to revert to.",
             RED,
             "Remember this vital distinction: a direct recruit on probation does not hold a lien. Lien is born only upon successful confirmation in the post."),
        ],
        "hook": "REMEMBER: Lien (FR 9(13)) = Right to Hold a Regular Post • Acquired ONLY Upon Confirmation!",
        "hook_say": "Remember: A lien under F.R. 9(13) is your right to hold a regular post, and it is acquired only upon confirmation.",
        "covers": ["P3.1.1-3.1.2"],
    },
    {
        "id": "c01_10_retention_of_lien_circumstances",
        "chapter": "CHAPTER 10 • PARA 3.2: FIVE CIRCUMSTANCES WHERE LIEN IS RETAINED",
        "title": "PARA 3.2 — IN WHICH FIVE SITUATIONS DOES AN OFFICER RETAIN HIS LIEN?",
        "accent": ORANGE, "badge": "PARA 3.2",
        "q": "Under what circumstances does a Government servant retain a lien on his substantive post?",
        "q_say": "Sir, when an officer is on leave, suspension, or foreign service, does his lien on his parent post continue?",
        "boxes": [
            ("THE FIVE CIRCUMSTANCES (PARA 3.2)",
             "Retains lien: (a) performing duties; (b) foreign service / temporary post; (c) joining time; (d) leave; (e) suspension.",
             "Para 3.2: A Government servant who has acquired a lien on a post retains a lien on that post: (a) while performing the duties of that post; (b) while on foreign service, or holding a temporary post or officiating in another post; (c) during joining time on transfer to another post; (d) while on leave; and (e) while under suspension.",
             SKY,
             "Under Para 3.2, you retain your lien in five situations: performing your duties, on foreign service or temporary posts, during joining time, while on leave, and while under suspension."),
            ("LOWER PAY TRANSFER EXCEPTION (3.2(c))",
             "Exception: If transferred substantively to a lower pay post, lien transfers to new post from date of relief in old post.",
             "Para 3.2(c): During joining time on transfer to another post, lien is retained 'unless he is transferred substantively to a post on lower pay, in which case his lien is transferred to the new post from the date on which he is relieved of his duties in the old post.'",
             GREEN,
             "There is one exception during transfer: if you are substantively transferred to a post on lower pay, your lien transfers to the new post the moment you are relieved from the old one."),
            ("ONLY ONE LIEN AT A TIME",
             "On acquiring a lien on a new post, an employee immediately ceases to hold any lien previously acquired on any other post.",
             "Para 3.2: 'A Government servant on acquiring a lien on a post will cease to hold any lien previously acquired on any other post.' No officer can hold two liens simultaneously.",
             ORANGE,
             "Fundamental Rule 3.2 states clearly that an employee can hold only one lien at a time. The moment you acquire a new lien, your old lien is extinguished."),
            ("THE TRAP: SUSPENSION DOES NOT CANCEL LIEN",
             "Trap: Being placed under suspension does NOT terminate a lien; Para 3.2(e) explicitly protects lien during suspension!",
             "Exam Trap (Para 3.2(e)): Suspension is not a penalty; an employee under suspension continues to hold his substantive lien on the post.",
             RED,
             "Remember for exams: suspension never cancels a lien. Para 3.2, clause e, explicitly protects your lien while under suspension."),
        ],
        "hook": "REMEMBER: Lien Retained On: Duty • Foreign Service • Joining Time • Leave • Suspension!",
        "hook_say": "Remember: You retain your lien on duty, on foreign service, during joining time, on leave, and while under suspension.",
        "covers": ["P3.2"],
    },
    {
        "id": "c01_11_lien_retention_2_plus_1_rule",
        "chapter": "CHAPTER 11 • PARA 3.3: THE 2-YEAR + 1-YEAR LIEN RETENTION TIMELINE",
        "title": "PARA 3.3 — HOW LONG CAN A CONFIRMED OFFICER RETAIN HIS LIEN IN PARENT CADRE?",
        "accent": SKY, "badge": "PARA 3.3 • 2+1 YEARS",
        "q": "For how many years can an employee retain his lien upon appointment in another Department or State Government?",
        "q_say": "Sir, if a permanent officer joins another department, how many years can he keep his lien back home before he must resign?",
        "flow": "lien_timeline",
        "boxes": [
            ("STANDARD PERIOD: 2 YEARS (3.3(i))",
             "Must resign from parent dept unless reverting within 2 YEARS. Undertaking taken when forwarding application.",
             "Para 3.3(i) (DoPT OM 8/4/70-Estt(C) dated 06.03.1974): A permanent Government servant appointed in another Central Government Department/Office/State Government has to resign from his parent department unless he reverts within a period of 2 years. An undertaking to abide by this condition is taken at the time of forwarding his application.",
             SKY,
             "Under Para 3.3, sub-clause 1, a permanent officer appointed in another department must resign unless he reverts to his parent department within 2 years. He signs an undertaking agreeing to this."),
            ("EXCEPTIONAL EXTENSION: 1 MORE YEAR (3.3(ii))",
             "If NOT confirmed in new department within 2 years, lien may be extended for ONE MORE YEAR (total 3 years maximum).",
             "Para 3.3(ii): In exceptional cases where the Government servant is not confirmed in the new department/office within 2 years, he may be permitted to retain his lien in the parent department for one more year (total 3 years), upon giving a fresh undertaking.",
             GREEN,
             "Under sub-clause 2, if you are not confirmed in your new post within 2 years, your parent department can grant an extension of one more year, bringing the maximum lien period to 3 years."),
            ("TIMELY ACTION & BREACH OF UNDERTAKING (3.3(iii))",
             "Departments must take timely action. Failure to revert or resign leads to disciplinary action and termination of lien.",
             "Para 3.3(iii): Timely action must be taken to ensure extension/reversion/resignation on completion of 2/3 years. If the employee does not respond, suitable action should be initiated for violating the undertaking and for termination of lien, after giving adequate opportunity.",
             ORANGE,
             "Sub-clause 3 directs departments to monitor the 2-to-3 year deadline. If an officer ignores instructions, disciplinary action is taken for breaching his undertaking and his lien is terminated."),
            ("TEMPORARY SERVANTS: ZERO LIEN (3.3(iv))",
             "Temporary Government servants must SEVERE ALL CONNECTIONS with Government on outside selection; NO lien retained!",
             "Para 3.3(iv): 'Temporary Government servants will be required to severe connections with the Government in case of their selection for outside posts. No lien will be retained in such cases.'",
             RED,
             "Here is the strict rule in sub-clause 4: temporary employees must sever all connections with the Government on outside selection. They get zero lien."),
        ],
        "hook": "REMEMBER: Lien Retention = 2 Years Standard • Max 3 Years If Unconfirmed • Zero Lien for Temporary Staff!",
        "hook_say": "Remember: Lien retention is 2 years standard, extendable to 3 years if unconfirmed, and temporary employees get zero lien.",
        "covers": ["P3.3"],
        "calc_asserts": ["2 + 1 == 3"],
    },
    {
        "id": "c01_12_termination_of_lien_rules",
        "chapter": "CHAPTER 12 • PARA 3.4: THREE ABSOLUTE RULES ON TERMINATION OF LIEN",
        "title": "PARA 3.4 — WHEN IS A LIEN TERMINATED, AND WHEN CAN IT NEVER BE?",
        "accent": RED, "badge": "PARA 3.4",
        "q": "Can an officer be left without a lien, and in what exact situations is a lien legally terminated?",
        "q_say": "Sir, can a department relieve a confirmed officer with a condition that no lien will be kept? When does a lien end?",
        "boxes": [
            ("CANNOT LEAVE WITHOUT A LIEN (3.4.1)",
             "A lien may in NO circumstances be terminated, even with employee consent, if it leaves him without a lien on a permanent post.",
             "Para 3.4.1 (Notification 28020/1/96-Estt(C) dated 09.02.1998): 'A Government servant's lien on a post may in no circumstances be terminated even with his consent if the result will be to leave him without a lien upon a permanent post.' Unless transferred, substantive lien continues.",
             SKY,
             "Para 3.4.1 lays down a golden constitutional protection: an officer's lien can never be terminated, even with his written consent, if it leaves him without a lien on a permanent post."),
            ("CONDITIONAL RELIEVING PROHIBITED (3.4.1)",
             "Illegal to deny lien because employee did not ask for it, or to relieve with a condition that 'no lien will be retained'.",
             "Para 3.4.1: 'It will not be correct to deny a Government servant lien to a post he was holding substantively on the plea that he had not requested for retention of lien while submitting his Technical Resignation, or to relieve such a Government servant with a condition that no lien will be retained.'",
             GREEN,
             "It is completely illegal for a department to relieve a confirmed officer with a note saying 'no lien retained', or to claim that the officer did not ask for it. Lien is automatic."),
            ("ACQUIRING PERMANENT LIEN ELSEWHERE (3.4.2)",
             "Lien automatically terminates the moment the officer acquires a lien on a permanent post outside his cadre.",
             "Para 3.4.2: 'A Government employee's lien on a post shall stand terminated on his acquiring a lien on a permanent post (whether under the Central Government or a State Government) outside the cadre on which he is borne.'",
             ORANGE,
             "Under Para 3.4.2, your old lien terminates automatically the exact moment you are confirmed and acquire a permanent lien in your new department."),
            ("IMMEDIATE ABSORPTION & DEPUTATION OVERSTAY (3.4.3)",
             "No lien retained: (a) on immediate absorption from date of absorption; (b) on deputation beyond maximum limit.",
             "Para 3.4.3: No lien shall be retained: (a) where a Government servant has proceeded on immediate absorption basis to a post outside Government from the date of absorption; and (b) on foreign service/deputation beyond the maximum limit admissible under Government orders.",
             RED,
             "Under Para 3.4.3, no lien is retained if you take immediate absorption, or if you overstay on deputation beyond the maximum permissible limit."),
        ],
        "hook": "REMEMBER: Never Left Without a Lien (3.4.1) • Conditional Relieving Is ILLEGAL • Ends on Confirmation Elsewhere!",
        "hook_say": "Remember: An officer can never be left without a lien, conditional relieving is illegal, and lien terminates only on permanent confirmation elsewhere.",
        "covers": ["P3.4.1-3.4.3"],
    },
    {
        "id": "c01_13_transfer_of_lien_fr15",
        "chapter": "CHAPTER 13 • PARA 3.5: TRANSFER OF LIEN UNDER FUNDAMENTAL RULE 15",
        "title": "PARA 3.5 — HOW CAN A LIEN BE TRANSFERRED TO ANOTHER POST IN THE SAME CADRE?",
        "accent": GREEN, "badge": "PARA 3.5 • FR 15",
        "q": "Can the competent authority transfer an absent officer's lien to another post in the same cadre?",
        "q_say": "Sir, if an officer is away on deputation, can his parent department shift his lien to another vacant post in the cadre?",
        "boxes": [
            ("TRANSFER OF LIEN UNDER FR 15",
             "Lien of an officer not performing duties of the post can be transferred to another post in the same cadre under FR 15.",
             "Para 3.5 (Notification 28020/1/96-Estt(C) dated 09.02.1998): 'The lien of a Government servant, who is not performing the duties of the post to which the lien pertains, can be transferred to another post in the same cadre subject to the provisions of Fundamental Rule 15.'",
             SKY,
             "Under Para 3.5 and Fundamental Rule 15, if an officer is away from his post, the department can transfer his lien to another post within the same cadre."),
            ("SAME CADRE RESTRICTION",
             "Transfer of lien can happen ONLY within the SAME cadre, never to a post in a completely different cadre or service.",
             "FR 15 Conditions: The transfer of lien is an administrative mechanism within the parent cadre to manage vacancies. It cannot be used to shift an employee's lien to an outside service without his consent.",
             GREEN,
             "Notice the limitation: transfer of lien can happen only within the same cadre. It cannot be used to push an employee into an outside cadre."),
            ("NO REDUCTION IN STATUS OR PAY",
             "Subject to FR 15: Transfer of lien cannot be made to a post carrying lower pay than the post on which lien was held.",
             "FR 15 Protection: Fundamental Rule 15 prohibits transferring an employee or his lien substantively to a post carrying less pay than his substantive post, except on written request or disciplinary penalty.",
             ORANGE,
             "Under F.R. 15, the transfer of lien cannot downgrade you: it cannot be made to a post with lower pay, unless done as a formal penalty or at your own request."),
            ("THE TRAP: ADMINISTRATIVE VACANCY MANAGEMENT",
             "Trap: Transfer of lien does not harm the officer; it allows the department to confirm another junior in the vacated post!",
             "Administrative Purpose: Transferring an absent officer's lien to a floating or vacant post in the cadre frees up the substantive post to confirm a junior waiting in line.",
             RED,
             "Here is the administrative rationale: shifting an absent officer's lien to another vacant post in the cadre frees up the physical post to confirm a deserving junior."),
        ],
        "hook": "REMEMBER: Lien Can Be Transferred Within the Same Cadre Under FR 15 • Never to a Lower Pay Post!",
        "hook_say": "Remember: An absent officer's lien can be transferred to another post in the same cadre under F.R. 15, but never to a post with lower pay.",
        "covers": ["P3.5"],
    },
    {
        "id": "c01_14_joining_time_and_pay",
        "chapter": "CHAPTER 14 • PARAS 3.6.1 & 3.6.2: JOINING TIME, JOINING TIME PAY & ALLOWANCES",
        "title": "PARAS 3.6.1-2 — ARE JOINING TIME AND JOINING TIME PAY GRANTED?",
        "accent": BLUE, "badge": "JOINING TIME",
        "q": "Does an officer who technical resigns on selection through open competition get Joining Time and Joining Time Pay?",
        "q_say": "Sir, if an employee gets selected through an open exam like UPSC or SSC, does he get Joining Time and salary during the transit?",
        "boxes": [
            ("JOINING TIME ENTITLEMENT (3.6.1)",
             "Central employees and permanent State employees appointed on results of competition/interview get Joining Time under 1979 Rules.",
             "Para 3.6.1: For appointment to posts under the Central Government on results of a competition and/or interview open to Government servants and others, Central Government employees and permanent/provisionally permanent State Government employees will be entitled to joining time under CCS (Joining Time) Rules, 1979. Counts as qualifying service.",
             SKY,
             "Under Para 3.6.1, if you are appointed to a Central Government post through an open competition or interview, you are entitled to full Joining Time under the 1979 Rules, and it counts as qualifying service."),
            ("JOINING TIME PAY EQUAL TO OLD PAY (3.6.2)",
             "Treated as ON DUTY during joining time. Entitled to Joining Time Pay equal to pay drawn before relinquishment of old post.",
             "Para 3.6.2: A Government servant on joining time shall be regarded as on duty during that period and shall be entitled to be paid joining time pay equal to the pay which was drawn before relinquishment of charge in the old post, plus appropriate DA.",
             GREEN,
             "Under Para 3.6.2, you are treated as on duty during joining time. Your joining time pay equals the pay you drew in your old post just before handing over charge, plus D.A."),
            ("HRA OF OLD STATION ADMISSIBLE",
             "Entitled to draw HRA as applicable to the OLD station from which transferred. NO Conveyance Allowance or permanent TA.",
             "Para 3.6.2: In addition, he can draw compensatory allowances like House Rent Allowance (HRA) as applicable to the old station from which he was transferred. He shall not be allowed Conveyance Allowance or permanent Travelling Allowance.",
             ORANGE,
             "You also draw compensatory allowances, including H.R.A. at the rates of your old station. However, conveyance allowance and permanent T.A. are not allowed."),
            ("THE TRAP: OPEN COMPETITION INCLUDED",
             "Trap: Candidates think open competition appointments get no joining time; Para 3.6.1 explicitly GRANTS joining time!",
             "Exam Trap (Para 3.6.1): Even though the exam was open to private candidates, serving Government employees are expressly entitled to joining time and joining time pay under Para 3.6.1.",
             RED,
             "Remember this exam trap: even if the appointment is through an open competitive exam open to outsiders, serving Government employees are fully entitled to joining time and pay."),
        ],
        "hook": "REMEMBER: Technical Resignation Gets Joining Time & Pay (Old Basic + DA + Old HRA) • Counts As Duty!",
        "hook_say": "Remember: Technical resignation grants joining time and pay equal to old basic plus D.A. and old H.R.A., and counts as duty.",
        "covers": ["P3.6.1", "P3.6.2"],
    },
    {
        "id": "c01_15_transfer_ta_and_temporary_bar",
        "chapter": "CHAPTER 15 • PARA 3.6.3: TRANSFER TA & THE 3-YEAR SERVICE BAR FOR TEMPORARY STAFF",
        "title": "PARA 3.6.3 — WHO GETS TRANSFER TA, AND WHO IS BARRED UNDER 3 YEARS?",
        "accent": YELLOW, "badge": "PARA 3.6.3 • TTA",
        "q": "Who is entitled to Transfer Travelling Allowance (TTA), and which employees are specifically barred?",
        "q_say": "Sir, can an employee claim Transfer Travelling Allowance for moving his family, and what is the 3-year restriction for temporary staff?",
        "boxes": [
            ("TRANSFER TA ADMISSIBLE (3.6.3)",
             "Central employees and permanent State employees appointed on competition/interview are entitled to Transfer TA (TTA).",
             "Para 3.6.3: For appointments to posts under Central Government on the basis of results of a competition and/or interview open to Government servants and others, Central Government employees and permanent/provisionally permanent State Government employees shall be entitled to Transfer Travelling Allowance (TTA).",
             SKY,
             "Under Para 3.6.3, Central Government employees and permanent State employees appointed through open competition are entitled to Transfer Travelling Allowance to move themselves and their families."),
            ("3-YEAR BAR FOR TEMPORARY EMPLOYEES",
             "Temporary Central employees with LESS THAN 3 YEARS regular continuous service are NOT entitled to Transfer TA!",
             "Para 3.6.3: 'However, temporary Central Government employees with less than 3 years of regular continuous service would not be entitled for TTA, as they are not entitled for joining time pay under Joining Time Rules.'",
             GREEN,
             "Now look at the strict exclusion: temporary Central Government employees with less than 3 years of regular continuous service are completely barred from claiming Transfer T.A."),
            ("RATIONALE: NO JOINING TIME PAY",
             "Because temporary employees under 3 years get no joining time pay under Joining Time Rules, they cannot get TTA.",
             "Para 3.6.3 Legal Nexus: Entitlement to Transfer TA is legally linked to entitlement to joining time pay. Under CCS (Joining Time) Rules, temporary staff with under 3 years service get no joining time pay, and therefore no TTA.",
             ORANGE,
             "Why are they barred? Because under Joining Time Rules, temporary staff with under 3 years service do not get joining time pay. And without joining time pay, Transfer T.A. cannot be granted."),
            ("WORKED EXAMPLE: SUNIL VS ANITA",
             "Example: Sunil (temporary, 2 yrs service) gets NO TTA. Anita (regular, 1 yr service) OR Sunil at 3 yrs gets FULL TTA!",
             "Example: Sunil is a temporary employee with 2 years service; he qualifies for no TTA. Anita is a confirmed permanent employee with 1 year service; she gets full TTA. If Sunil had completed 3 years continuous service, he would get full TTA.",
             RED,
             "Here is a problem scenario: Sunil has 2 years temporary service, so he gets zero Transfer T.A. Anita is confirmed, so she gets full Transfer T.A. even after 1 year. Temporary staff need 3 full years."),
        ],
        "hook": "REMEMBER: Transfer TA Admissible • Temporary Staff Under 3 Years Service Get NO Transfer TA!",
        "hook_say": "Remember: Transfer T.A. is admissible on technical resignation, but temporary staff with less than 3 years service get zero Transfer T.A.",
        "covers": ["P3.6.3"],
        "calc_asserts": ["NO_MATH"],
    },
    {
        "id": "c01_16_master_recap_and_annexure",
        "chapter": "CHAPTER 16 • MASTER RECAP & ANNEXURE: ALL RULES AND EIGHT CONSTITUENT OMs",
        "title": "MASTER RECAP & ANNEXURE — SUMMARY OF TECHNICAL RESIGNATION, LIEN & 8 OMs",
        "accent": PINK, "badge": "RECAP • 8 OMs",
        "q": "Can we summarise all the core principles of Technical Resignation, Lien, and the 8 constituent OMs on one slide?",
        "q_say": "Sir, before we conclude, can we do a rapid-fire recap of all the rules and the eight constituent OMs in this compendium?",
        "boxes": [
            ("TECHNICAL RESIGNATION & BENEFITS (PARAS 2.1–2.4)",
             "Applied through proper channel. Leave carries forward (2.2). LTC fresh recruit 8-yr balance (2.3). Pay protected via FR 22-B (2.4).",
             "Recap Paras 2.1–2.4: Technical resignation protects past service benefits. Pre-joining applications must be intimated immediately on joining. Unutilized leave (including CCL) carries forward; 300 days leave cash equivalent on PSU absorption. LTC fresh recruit status lasts for remainder of 8-year window. Substantive pay protected under FR 22-B as presumptive pay (FR 9(24)); past service counts for annual increment under FR 26.",
             SKY,
             "Rapid-fire recap, card 1: Technical resignation protects past service. Leave carries forward in full, L.T.C. fresh recruit balance transfers within 8 years, and pay is protected as presumptive pay under F.R. 22-B."),
            ("SENIORITY, PENSION & CHECKS (PARAS 2.5–2.11)",
             "Seniority protected but time outside lost for promotion (2.6). Pre-2004 keeps Old Pension (2.7). NPS PRAN transfers (2.8). 1-yr police check (2.11).",
             "Recap Paras 2.5–2.11: Substantive seniority preserved, but time spent outside does not count for promotion qualifying service on reversion. Pre-2004 entrants retain Old Pension under Rule 26(2). NPS PRAN transfers seamlessly. Service book transfers under SR 198. No fresh medical if standards match. Police verification valid if gap under 1 year.",
             GREEN,
             "Card 2: Substantive seniority is kept, but time outside does not count for promotion if you revert. Pre-2004 entrants keep Old Pension, N.P.S. accounts transfer, and police verification holds for 1 year."),
            ("LIEN ACQUISITION, RETENTION & END (PARAS 3.1–3.5)",
             "Lien (FR 9(13)) on confirmation. Retained 2 yrs (extendable to 3 yrs unconfirmed). Never left without lien (3.4.1). Transferred under FR 15.",
             "Recap Paras 3.1–3.5: Lien acquired on confirmation. Retained on duty, foreign service, joining time, leave, suspension. Retained for 2 years on outside appointment, extendable to 3 years in exceptional unconfirmed cases. Zero lien for temporary staff. Officer can never be left without a lien. Terminates on confirmation elsewhere or immediate absorption. Lien transferred within cadre under FR 15.",
             ORANGE,
             "Card 3: Lien is acquired on confirmation and retained for 2 years, extendable to 3 years if unconfirmed. You can never be left without a lien, and temporary employees receive zero lien."),
            ("JOINING TIME & 8 CONSTITUENT OMs (PARAS 3.6–5)",
             "Joining time & pay granted (3.6.1-2). TTA barred for temporary staff <3 yrs (3.6.3). Annexure lists 8 historic OMs from 1963 to 2016.",
             "Recap Paras 3.6–5: Joining time and joining time pay (old pay + DA + old HRA) admissible for open competition selections. Transfer TA barred for temporary staff with under 3 years service. Para 5 lists 8 constituent OMs: #1 OM 17/08/2016 (Consolidated), #2 OM 26/12/2013, #3 OM 09/02/1998 (Lien notification), #4 OM 31/01/1986 (PE absorption), #5 OM 22/07/1980, #6 OM 06/03/1974, #7 OM 14/07/1967, and #8 OM 01/10/1963 (Absorption lien termination).",
             RED,
             "Card 4: Joining time and pay are fully granted, but Transfer T.A. is barred for temporary staff with under 3 years service. Finally, Para 5 anchors this compendium to 8 historic O.M.s dating back to 1963."),
        ],
        "hook": "REMEMBER: Technical Resignation Protects Benefits • Lien Lasts 2+1 Years • Never Left Without a Lien!",
        "hook_say": "Remember: Technical resignation protects your past service, lien lasts 2 plus 1 years, and an officer can never be left without a lien.",
        "covers": ["RECAP-TECH-RESIG", "P5-ANNEXURE"],
    },
]

FLOWS = {
    "tech_resig_flow": {
        "nodes": [
            (80, 300, 420, 80, "APPLY VIA CHANNEL", "Proper Channel Consent", SKY, 1),
            (570, 300, 430, 80, "SELECTION & OFFER", "Administrative Reason", GREEN, 2),
            (1070, 300, 360, 80, "TECHNICAL RESIGN", "Word Not Mandatory", ORANGE, 3),
            (1500, 300, 340, 80, "BENEFITS PROTECTED", "Pay, Leave, Lien, LTC", RED, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, GREEN, 3), (2, 3, ORANGE, 4)],
    },
    "lien_timeline": {
        "nodes": [
            (80, 300, 420, 80, "JOINING NEW DEPT", "Lien Retained in Parent", SKY, 1),
            (570, 300, 430, 80, "YEARS 1 & 2: STANDARD", "Under Undertaking", GREEN, 2),
            (1070, 300, 360, 80, "YEAR 3: EXCEPTIONAL", "If Still Unconfirmed", ORANGE, 3),
            (1500, 300, 340, 80, "CONFIRM / REVERT", "Lien Ends or Reverts", RED, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, GREEN, 3), (2, 3, ORANGE, 4)],
    },
}

PART_STARTS = ["c01_01_tech_resig_definition", "c01_06_seniority_reversion_penalty", "c01_11_lien_retention_2_plus_1_rule"]


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
    (ROOT / "tech_resignation_reference_sheet.md").write_text("\n".join(out), encoding="utf-8")


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
    "Apply through proper channel - that is what makes a resignation 'technical'.",
    "Leave, LTC balance and pay protection all carry forward with you.",
    "Substantive seniority survives; promotion qualifying service does not.",
    "Lien runs 2 years plus 1, and can never leave you without a permanent post.",
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
        words = timed_words(normalize_for_tts(s["text"]), adur)
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
