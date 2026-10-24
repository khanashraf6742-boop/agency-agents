#!/usr/bin/env python3
"""
CCS (Pension) Rules 2021 - Batch 5 - Rules 53-70: Determination of Pension on Retirement
SIMPLE ENGLISH Q&A EXPLANATION MASTERCLASS COMPILER - 32 chapters (31 rule chapters plus 1 senior audit chapter). Scope: Batch 5 = Part 5, Chapter X (Rules 53-70): online pension case, retirement lists, NDC, preparation, Rule 57 three stages, Rule 58, Form 7, sending the case, provisional pension, PPO, deputation, interest, revision, Government dues, housing dues, notification of retirement, plus Sept 2025 DoPPW calendar O.M. and related O.M.s. Explanation only, 31 rule chapters, recap, and a senior audit chapter at the end.
=====================================================================================================
SOURCES READ / CHECKED IN THIS BUILD:
  * src/B5.txt and src/preamble.txt (podcast source, read completely)
  * ledger/B5_verified.json (224 items from the earlier verification pass; every id is covered by a card)
  * https://www.gconnect.in/orders-in-brief/pension/determination-pension-gratuity-central-civil-services-pension-rules-2021.html (secondary rule summary, via ledger)
  * https://www.staffnews.in/2024/07/central-civil-services-pension-amendment-rules-2024.html (G.S.R. 410(E) reproduction, via ledger)
  * https://www.staffnews.in/2025/10/comprehensive-guidelines-for-timely-payment-of-retirement-dues.html (O.M. of 29.09.2025, via ledger)
  * https://www.gconnect.in/orders-in-brief/pension/interest-delayed-payment-gratuity-family-pension-ccs-pension-rules-2021.html (read in this pass: Rule 65(5) start dates, GPF rate basis; matches the card)
  * Finance Ministry GPF rate resolutions for Q2 and Q3 2026-27 via staffnews pages (via ledger)
CHANGES VERSUS THE SOURCE (outdated / superseded / corrected):
  * Rule 57 vs 58 infirmity tier: source says Rule 58 is broader (any other member); current is both provisos say spouse or any other family member plus a gratuity nominee tier; evidence staffnews 2024 reproduction of G.S.R. 410(E)
  * Rule 57(1)(c)(iii): source says Form 6-A and remaining old forms; current is advise Form 6-A only; Forms 4 and 6, Format 9 undertaking, Form A, medical option form are obsolete history
  * Rule 60(1)(i): Form 4, Form 6 and Format 9 undertaking replaced by Form 6-A; the fourteenth substitution and nine forms merged claims are not confirmed
  * Rule 63(4): source says it is the only clause replaced in 2024; wrong, G.S.R. 410(E) amended Rules 53, 57, 58, 59, 60, 62(6)(a), 63(4)(a)(b), 80(5), Form 4, Form 7 check list and Format 10
  * Rule 65(5): source omitted it; interest starts the day after three months (superannuation from retirement), not from the due date; Worked Example 18 recomputed as 01.07.2025 to 31.12.2025, six months, Rs 53,250, total Rs 15,53,250 instead of Rs 79,875 and Rs 15,79,875; evidence gconnect Rule 65(5) page
  * Rule 62 scope: source names Rule 64 for proceedings delays; Rule 64 is the deputation rule, proceedings are Rules 8 and 63(5)
  * Rule 68(1)(c) and 68(5): source links silence to the 10 percent hold; wrong, 68(5) applies where the Directorate cannot fix the fee
  * Sub-rules the source omitted and now added: 55(4)-(6) and Explanation, 57(2)(b), 59(2), 62(5), 63(1)(e)-(h), 63(2)-(3), 63(4)(b)-(c), 63(5)(b), 65(5), 67(3), 68(7)(b)-(c), 68(8) Explanation, 70(1) proviso exception
  * Rule 59(1) Rule 58 limb resolved: within two months after Form 6-A; Rule 63(1)(d) second proviso resolved
  * CPAO seal: Rule 63(4)(b) says 21 days of receiving the PPO; Sept 2025 calendar says by the 20th of the retirement month; both kept, each with its layer
  * GPF rate: 7.1 percent for 01.10.2026 to 31.12.2026 (Finance Ministry resolution 05.10.2026) and for Q2 2026-27; changes quarterly
  * Rule 56 example: LPR timing made realistic and flagged; leave length not checked
  * Rule 66(1): the words or otherwise after Central Pay Commission are now flagged unverified
  * No amendment of Rules 53-70 found after G.S.R. 410(E); G.S.R. 770(E) and 340(E) do not touch them
KEY FACTS:
  * Online by default (Bhavishya or e-HRMS); 53(2)(a) whole case manual, 53(2)(b) one step manual
  * Preparation starts one year before or at leave, whichever is earlier (Rules 56, 69)
  * Eight months: service verified, certificate, dues assessed; six months: Form 6-A; four months: case to Accounts Officer; two months: PPO
  * Other retirements: Form 6-A immediately; case within two months of forms; PPO within 45 days of papers
  * Emoluments verified for the last 24 months only
  * Provisional pension 100 percent from next day, gratuity 100 percent less 10 percent held, up to six months from the later of retirement or Form 6-A; excess pension recovered, excess gratuity not refunded
  * Interest at the GPF rate starts after three months, needs administrative delay, Secretary or not below Joint Secretary sanctions, paid in two months
  * Revision: only clerical error against the pensioner; after two years DoPPW concurrence; refund in two months
  * Silence helps: no reply in two months means period qualifies; no DoE reply means no fee
  * Directorate of Estates replies in two months or one month; NDC within 14 days of application after actual vacation; last resort recovery from dearness relief
NOT VERIFIED (flagged on the cards - quote the official text in an answer sheet):
  * Rule wording is a close restatement; Gazette, India Code and DoPPW originals were not read directly (secondary pages via a summarising tool)
  * G.S.R. 410(E) effective date 16.11.2024: 120 days from 16.07.2024 is 13.11.2024, Gazette publication date not read
  * Rule 55(1) details prescribed by the Directorate of Estates: not seen in summary
  * Rule 57(1)(b) mention of last ten months: single secondary mention
  * Rule 58 scope including resignation: not confirmed
  * Rule 65(2) word shall: not confirmed
  * Rule 66(1) words or otherwise: not confirmed
  * Rule 67 grounds of damages: not seen
  * Format 9 staying separate for death cases: not re-read
  * Corrigendum of 25.07.2024: not found
  * O.M. of 23.10.2024: file found contains the 2016 Bhavishya O.M. only
  * Sept 2025 O.M. Nodal Officer duties, e-PPO definition, manual processing line: not seen
  * PDA and bank circulation of the 30.10.2025 O.M.: not seen
  * Links to Rule 51, Rule 78 and Rule 84: those rules belong to other batches
  * O.M. of 22.06.2026 cited by the source: not found
  * Absence of newer amendments up to 21.10.2026: limited web search only
  * Length of leave preparatory to retirement used in the Rule 56 example: not checked
Usage
    python build_pension_b5.py --audit      # density check only (no ffmpeg / internet)
    python build_pension_b5.py --preview    # slides only
    python build_pension_b5.py --no-tts     # silent dry run
    python build_pension_b5.py --part 1     # one third of the chapters (1, 2 or 3)
    python build_pension_b5.py              # full build (needs internet for edge-tts; ffmpeg+ffprobe with libass on PATH)
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
BUILD_DIR = Path("pension_b5_build")
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
OUT_STEM = "pension_b5_masterclass"
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
SCENES = [
    {
        "id": "c5_01_rule53",
        "chapter": "CHAPTER 1 • RULE 53: THE PENSION CASE GOES ONLINE",
        "title": "RULE 53 — ONLINE BY DEFAULT, AND THE TWO KINDS OF EXEMPTION",
        "accent": RED, "badge": "RULE 53",
        "q": "How is a pension case processed, and what happens if an office cannot go online?",
        "intro": ("Welcome back! This is batch five. We now enter Chapter ten of the Central Civil Services (Pension) Rules, 2021, "
                  "which covers Rules fifty-three to seventy: how a pension is worked out when a government servant retires. "
                  "This chapter is mostly about who must do what, and by which date. A pension case simply means the file of papers that must be "
                  "ready so the pension starts on time. Let us hear Riya's first question."),
        "q_say": "Sir, how is a pension case processed these days, and what happens if an office cannot work online?",
        "boxes": [
            ("THE DEFAULT • RULE 53(1)",
             "Unless exempted by a general or special order, the case is processed online (Bhavishya or e-HRMS).",
             "Rule 53(1), as substituted by G.S.R. 410(E) of 16.07.2024: unless exempted by a general or special order of the Government, the pension case is processed through online mode (Bhavishya/e-HRMS). Before 2024 the word was only 'Bhavishya'. Bhavishya is defined in Rule 3(1)(d) as the online system for sanction and tracking of retirement benefits. Ledger: R53(1)-DEFAULT, R53-EXEMPTION-ORDER, R53-2024-WORDING, R53-BHAVISHYA-DEF. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "Let us take the rule first. A pension case is processed online unless the Government exempts someone by a general or special order. Since the 2024 amendment, the rule says online mode, which means Bhavishya or e-HRMS. Bhavishya is the government's online system for sanctioning and tracking retirement benefits, as defined in Rule three, sub-rule one, clause d."),
            ("WHICH PORTAL? • RULE 53(1)",
             "e-HRMS is only for superannuation cases of people on e-HRMS. Everyone else uses Bhavishya.",
             "Rule 53(1) text: retiring officials who are on e-HRMS submit Form 6-A through e-HRMS, and this applies only to superannuation cases. The plain-words summary 'all others go through Bhavishya' is NOT in the quoted rule text; it comes from a summary of the notification and from the DoPPW O.M.s of 15.10.2024 and 04.11.2024 (Form 6-A online via Bhavishya/e-HRMS). Treat that part as a close restatement. Ledger: R53(1)-ROUTING (changed). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Now the routing. Superannuation means retiring on reaching the retirement age. Only for such cases, and only for staff who are already on e-HRMS, the form can go through e-HRMS. Every other case goes online through Bhavishya. Please note that this second sentence comes from a summary and from two office memoranda, not from the exact rule text, so treat it as a close restatement."),
            ("EXEMPTION (a): STATUS • 53(2)(a)",
             "If a Department, Office or Person is exempted, papers go physically and the WHOLE case is manual.",
             "Rule 53(2)(a): where a Department, Office or Person is exempted, the documents are sent in physical mode and the whole case is processed manually. After the 2024 amendment, 'Bhavishya' in Rule 53(2)(a) and (b) reads 'online mode (Bhavishya/e-HRMS)'. Ledger: R53(2)(a). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "Now the first kind of exemption, in clause a. If a whole Department, an Office, or even one Person is exempted, then the documents travel on paper and the entire case is handled manually. Think of it as an exemption of status: who you are decides the route."),
            ("EXEMPTION (b): ACTIVITY • 53(2)(b)",
             "If ONE action cannot be done online, only that step is manual. The rest stays online.",
             "Rule 53(2)(b): where any particular action cannot be performed on Bhavishya (online mode), that action alone is done manually and the rest of the case stays online. Example (made up by the script author, not from any rule or O.M.): an office with no digital signature uses the physical route for that one step only. Ledger: R53(2)(b), R53-EX-DIGSIG (unverified, invented illustration). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Here is the second kind, in clause b. If a single action cannot be done online, only that one step goes manual and everything else stays online. For example, say Bilal's office has no digital signature. Only the signing step goes on paper. This example is made up for teaching and is not from the rules."),
            ("THE TRAP",
             "Trap: 'exempt' does NOT always mean the whole case is manual. First find which clause applies.",
             "Trap: clause (a) is a status exemption and makes the whole case manual; clause (b) is an activity fallback and makes only one step manual. Writing 'exemption means the full case is manual' is wrong. Ledger: QA-R53. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             YELLOW,
             "Be careful, this is the trap. Many students write that an exemption makes the whole case manual. That is true only under clause a. Under clause b, just one step is manual. So always check which clause applies before you answer."),
        ],
        "hook": "REMEMBER: online is the default; clause (a) = whole case manual, clause (b) = one step only!",
        "hook_say": "Remember: online is the default. Clause a makes the whole case manual, but clause b makes only one step manual.",
        "covers": ["R53(1)-DEFAULT", "R53(1)-ROUTING", "R53-BHAVISHYA-DEF", "R53(2)(a)", "R53(2)(b)", "R53-EXEMPTION-ORDER", "R53-2024-WORDING", "R53-EX-DIGSIG", "QA-R53"],
    },
    {
        "id": "c5_02_form6a_online",
        "chapter": "CHAPTER 2 • FORM 6-A ONLINE: THE O.M.s AND THE START DATE",
        "title": "FORM 6-A ONLINE — THE O.M.s, BHAVISHYA SINCE 2017, AND A DATE FLAG",
        "accent": ORANGE, "badge": "RULE 53 • O.M.s",
        "q": "Which orders put Form 6-A online, and from which date does it apply?",
        "q_say": "Sir, which orders put Form 6-A online, and from which date does all this apply?",
        "boxes": [
            ("BHAVISHYA SINCE 2017",
             "Bhavishya has been mandatory for pension cases from 01.01.2017 (Railways, Defence, P&T excluded).",
             "DoPPW O.M. No. 55/14/2014/P&PW(C)Pali-1 (November 2016; the day is illegible in the scan read): all pension cases to be processed only through Bhavishya with effect from 01.01.2017; excludes Railways, Defence and P&T. The file name of a PDF read suggested a 23.10.2024 circulation, but the text read was the 2016 O.M. Ledger: OM-BHAVISHYA-2017. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "First, some background. Under a DoPPW office memorandum of November two thousand sixteen, all pension cases had to be processed only through Bhavishya from the first of January two thousand seventeen. Railways, Defence and Posts and Telecom were left out."),
            ("O.M. OF 15.10.2024",
             "F.No. 55/13/2023-P&PW(C)(Part1), 15.10.2024: Form 6-A to be filled online on Bhavishya or e-HRMS.",
             "DoPPW O.M. F.No. 55/13/2023-P&PW(C)(Part1) dated 15.10.2024: Form 6-A to be filled online through Bhavishya/e-HRMS; the form was added to the systems from 15.10.2024. Not in the source script; added from a reproduction of the O.M. Ledger: OM-15.10.2024-6A. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Now a newer order. An office memorandum of fifteenth October two thousand twenty-four, file number fifty-five slash thirteen slash two thousand twenty-three, says Form 6-A is to be filled online, through Bhavishya or e-HRMS."),
            ("O.M. OF 04.11.2024",
             "Same file number, 04.11.2024: only online filing; form open from 06.11.2024; training of HoOs follows.",
             "DoPPW O.M. F.No. 55/13/2023-P&PW(C)(Part1) dated 04.11.2024: retiring employees to complete Form 6-A only online on Bhavishya or e-HRMS 2.0; the form is accessible from 06.11.2024; training of Heads of Office and Nodal Officers to follow. The two O.M.s give different go-live days (15.10.2024 and 06.11.2024); both were read as secondary reproductions. Ledger: OM-04.11.2024-6A. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "A second memorandum, dated fourth November two thousand twenty-four, repeats this: retiring employees complete Form 6-A only online. It says the form is open from sixth November, and training of Heads of Office will follow. Notice that the two orders give slightly different go-live days, so quote each with its own date."),
            ("THE DATE FLAG",
             "Amendment effective 16.11.2024 per the O.M.s. But 120 days from 16.07.2024 is 13.11.2024. Not confirmed.",
             "G.S.R. 410(E) of 16.07.2024: the DoPPW O.M.s of 15.10.2024 and 04.11.2024 give the start as 16.11.2024. Rule 1(2) says the amendment applies 'after one hundred twenty days from the date of publication in the Official Gazette'. 16.07.2024 plus 120 days is 13.11.2024, so the actual Gazette publication date must be checked. UNVERIFIED: say 'effective 16.11.2024 per DoPPW O.M.s'. Ledger: FORM-6A-EFFECTIVE (unverified). Gazette not read directly.",
             RED,
             "Be careful with the start date. The memoranda say the amendment starts on sixteenth November two thousand twenty-four. But the rule says one hundred twenty days after publication, and sixteenth July plus one hundred twenty days is thirteenth November. So the Gazette publication date must be checked. Until then, say effective sixteenth November per the DoPPW memoranda, and mark it not confirmed."),
        ],
        "hook": "REMEMBER: Form 6-A online (O.M.s 15.10.2024 and 04.11.2024); effective date 16.11.2024 is not confirmed!",
        "hook_say": "Remember: Form 6-A goes online under the memoranda of fifteenth October and fourth November two thousand twenty-four, and the sixteenth November start date is not yet confirmed from the Gazette.",
        "covers": ["OM-BHAVISHYA-2017", "OM-15.10.2024-6A", "OM-04.11.2024-6A", "FORM-6A-EFFECTIVE"],
    },
    {
        "id": "c5_03_rule54",
        "chapter": "CHAPTER 3 • RULE 54: THE LIST OF THOSE WHO ARE ABOUT TO RETIRE",
        "title": "RULE 54 — WHO MAKES THE LIST, WHEN, AND WHO IS TOLD",
        "accent": BLUE, "badge": "RULE 54",
        "q": "Who prepares the list of retiring staff, how often, and who gets it?",
        "q_say": "Sir, who prepares the list of people who are about to retire, how often, and who receives it?",
        "boxes": [
            ("THE LIST • RULE 54(1)",
             "Head of DEPARTMENT: by the 15th of every month, list everyone retiring in the next 15 months.",
             "Rule 54(1): the Head of Department prepares, by the 15th of every month, a list of the Government servants retiring within the next fifteen months. It is a rolling monthly job, not a yearly one. Ledger: R54(1). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "Let us take the rule first. Every month, by the fifteenth, the Head of Department prepares a list of everyone who will retire in the next fifteen months. A Head of Department is the senior officer heading a department. This is a rolling job, done every month, not once a year."),
            ("SENDING IT • RULE 54(2)",
             "A copy goes to the Accounts Officer before the last day of the month.",
             "Rule 54(2): a copy of the list goes to the Accounts Officer before the last day of the month. The Accounts Officer is the officer of the pay and accounts office who checks the pension case and issues the Pension Payment Order. Ledger: R54(2). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Now, whom do we tell? A copy goes to the Accounts Officer before the last day of that month. The Accounts Officer is the accounts-side officer who will later check the case and issue the pension payment order. So two dates: list by the fifteenth, copy out before month-end."),
            ("OTHER RETIREMENTS • 54(3)",
             "Other kinds of retirement: Head of OFFICE tells the Accounts Officer within 10 days of the order.",
             "Rule 54(3): where the retirement is other than superannuation, the Head of Office informs the Accounts Officer within ten days of the retirement order. Ledger: R54(3), R54-ACTOR-TRAP, TL-ELEVEN-DAYS-HOO-DOE. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Here is the change of actor. For retirement other than superannuation, it is the Head of Office, not the Head of Department, who informs the Accounts Officer, and the time limit is ten days from the retirement order."),
            ("REAL EXAMPLE",
             "Example: Charu retires 31 Dec 2027. She is on the HoD's list of 15 Nov 2026, sent before 30 Nov.",
             "Example (invented): Charu retires on superannuation on 31 December 2027. The 15 November 2026 list covers retirements up to 15 February 2028, so she appears on it, and the copy goes to the Accounts Officer before 30 November 2026. If Dev instead takes voluntary retirement by an order dated 5 March 2027, the Head of Office tells the Accounts Officer by 15 March 2027. Ledger: R54(1)-(3).",
             SKY,
             "Here is a real example. Charu retires on thirty-first December two thousand twenty-seven. The list of fifteenth November two thousand twenty-six already includes her, and the copy goes out before the thirtieth. Now Dev takes voluntary retirement by an order of fifth March two thousand twenty-seven. His Head of Office must inform the Accounts Officer within ten days, that is by fifteenth March."),
            ("THE TRAP: TWO CALENDARS",
             "Rule 54 = monthly, 15th. The Sept 2025 O.M. calendar uses 1 Jan/Apr/Jul/Oct. Different layers.",
             "Layer 3 (administrative): Comprehensive Guidelines O.M. No. 4/35/2024-P&PW(D)/10377 dated 29.09.2025, annexure stages 1 and 2: the Head of Department lists employees retiring in the next 12 to 15 months on 1 January, 1 April, 1 July and 1 October; the Head of Office sends the list to the PAO by 31 January, 30 April, 31 July and 31 October; for non-superannuation retirement, immediately. This sits beside the Rule 54 monthly list and does not change Rule 54 (layer 1). Ledger: OM-SEP2025-STAGE1-2, R54-ACTOR-TRAP.",
             RED,
             "Be careful, this is the trap. Rule fifty-four is the monthly list. The September two thousand twenty-five guidelines add a separate administrative calendar with fixed dates: first January, April, July and October for the list, and thirty-first January, April, July and October for sending it to the pay and accounts office. Read the two together, but do not mix their layers."),
        ],
        "hook": "REMEMBER: HoD lists by the 15th monthly (15 months ahead); other retirements: HoO within 10 days!",
        "hook_say": "Remember: the Head of Department lists by the fifteenth every month, looking fifteen months ahead. For other retirements, the Head of Office informs within ten days.",
        "covers": ["R54(1)", "R54(2)", "R54(3)", "R54-ACTOR-TRAP", "OM-SEP2025-STAGE1-2", "TL-ELEVEN-DAYS-HOO-DOE"],
    },
    {
        "id": "c5_04_rule55a",
        "chapter": "CHAPTER 4 • RULE 55(1)-(3): THE NO DEMAND CERTIFICATE PROCESS",
        "title": "RULE 55(1)-(3) — GOVERNMENT HOUSE DETAILS AND THE ONE YEAR AND EIGHT MONTHS",
        "accent": GREEN, "badge": "RULE 55(1)-(3)",
        "q": "What must the office do about government housing before a retirement?",
        "q_say": "Sir, what must the office do about government housing before someone retires, and what are the one year and eight months?",
        "boxes": [
            ("THE RULE • RULE 55(1)",
             "Right after the 54(1) list: collect housing details and send them to the Directorate of Estates 1 year ahead.",
             "Rule 55(1) (superannuation): immediately after the Rule 54(1) list, the Head of Office collects details of accommodation from those who were or are allottees and sends them to the Directorate of Estates at least one year before the expected date of retirement; the No Demand Certificate covers the eight months before retirement. 'Allottee' is defined in Rule 3(1)(b). Ledger: R55(1), R55(1)-ALLOTTEE-DEF, TL-DOE-ONEYEAR. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Rule fifty-five is about the No Demand Certificate, the NDC. It is a paper from the housing authority saying the retiree owes nothing for government housing. Under sub-rule one, as soon as the Rule fifty-four list is ready, the Head of Office collects housing details from everyone who was or is an allottee, meaning a person allotted government accommodation. The details go to the Directorate of Estates at least one year before the expected retirement."),
            ("WHO PRESCRIBES THE DETAILS?",
             "Details are those the Directorate of Estates prescribes. Not confirmed from the rule text.",
             "The source script says the details are those prescribed by the Directorate of Estates. This was NOT seen in the summary of Rule 55(1) read, and the wording of 55(1) beyond the one-year and eight-month points was not read in full. UNVERIFIED: check the Gazette. Ledger: R55(1)-DOE-PRESCRIBES (unverified).",
             PINK,
             "One small point. The source guide says the details are those the Directorate of Estates prescribes. We could not confirm that wording from the rule summary we read, so please treat it as not confirmed and check the Gazette."),
            ("OTHER RETIREMENTS • 55(2)-(3)",
             "Other retirements: collect details after the order; HoO forwards them within 10 days.",
             "Rule 55(2): after a non-superannuation retirement order, the Head of Office collects accommodation details. Rule 55(3): the Head of Office forwards the details to the Directorate of Estates within ten days of receiving them, along with the Rule 54(3) intimation to the Accounts Officer if the person was or is an allottee. Ledger: R55(2), R55(3). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "For retirements other than superannuation, sub-rule two says the Head of Office collects the housing details after the retirement order. Sub-rule three says he forwards them within ten days of receiving them."),
            ("ONE YEAR OR EIGHT MONTHS?",
             "One year = how early the details go. Eight months = the period the NDC covers. Fee after that: from pay.",
             "One year is the lead time for sending details to the Directorate of Estates; eight months before retirement is the period the NDC licence-fee report covers. Licence fee after the eight-month cut-off is recovered by the Head of Office from pay (Rule 55(1) and Rule 68(1)(a), (2)). Ledger: R55-ONEYEAR-8MONTHS, LIMIT-DOE-EIGHT-MONTHS. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "Be careful, this is the trap. Students mix up one year and eight months. One year is how early the details must reach the Directorate. Eight months is how far back before retirement the certificate covers the licence fee. The licence fee for the last eight months is then recovered from pay by the Head of Office."),
            ("REAL EXAMPLE",
             "Example: Esha, a Section Officer in a government flat, retires 31 Dec 2027. Her details reach the DoE by 31 Dec 2026.",
             "Example (invented, not from any rule): Esha, a Section Officer living in a government flat, retires on 31 December 2027. Her Head of Office sends the housing details to the Directorate of Estates by 31 December 2026 at the latest. The NDC report covers licence fee up to 30 April 2027 (eight months before retirement); fee from May to December 2027 is recovered from her pay each month. Ledger: R55-EX-SO (unverified, invented illustration).",
             SKY,
             "Here is a real example, invented for teaching. Esha lives in a government flat and retires on thirty-first December two thousand twenty-seven. Her office must send the details by thirty-first December two thousand twenty-six at the latest. The certificate covers the fee up to the end of April two thousand twenty-seven, and the later months are recovered from her pay."),
        ],
        "hook": "REMEMBER: details to the Directorate 1 YEAR before; NDC covers 8 MONTHS before; others within 10 days!",
        "hook_say": "Remember: housing details go to the Directorate one year before; the certificate covers eight months before retirement; and in other cases the office forwards within ten days.",
        "covers": ["R55(1)", "R55(1)-DOE-PRESCRIBES", "R55(1)-ALLOTTEE-DEF", "R55(2)", "R55(3)", "R55-ONEYEAR-8MONTHS", "LIMIT-DOE-EIGHT-MONTHS", "TL-DOE-ONEYEAR", "R55-EX-SO", "QA-R55"],
    },
    {
        "id": "c5_05_rule55b",
        "chapter": "CHAPTER 5 • RULE 55(4)-(6): NO HOUSING EVER, AND THE EXPLANATION",
        "title": "RULE 55(4)-(6) — THE DECLARATION, THE HoO'S OWN NDC, AND THE EXPLANATION",
        "accent": PINK, "badge": "RULE 55(4)-(6)",
        "q": "What if the retiring person never had government housing? Who gives the NDC then?",
        "q_say": "Sir, what if the retiring person never had government housing, and who issues the certificate then?",
        "boxes": [
            ("AT RETIREMENT AGE • 55(4)",
             "Never had official housing? Give the HoO a declaration one year before retirement.",
             "Rule 55(4): a Government servant who has never occupied or been allotted accommodation gives a declaration to the Head of Office one year before superannuation. This sub-rule was missing from the source script (which only had a gist of Rule 55). Close restatement from a page-summarising tool; Gazette text not read. Ledger: R55(4) (changed: added).",
             PINK,
             "The source guide missed three sub-rules, so here they are. Sub-rule four says that if a government servant has never occupied or been allotted government housing, he gives a declaration to the Head of Office one year before superannuation."),
            ("OTHER RETIREMENTS • 55(5)",
             "Same housing declaration, right after the retirement is approved or takes effect.",
             "Rule 55(5): the same kind of no-accommodation declaration is given for non-superannuation retirement, right after the retirement is approved or takes effect. Close restatement; Gazette text not read. Ledger: R55(5) (changed: added).",
             ORANGE,
             "Sub-rule five is the same declaration for the other kinds of retirement. It is given right after the retirement is approved or takes effect, because there is no calendar date to count back from."),
            ("THE HoO ISSUES THE NDC • 55(6)",
             "In those cases the Head of Office checks records and issues the NDC himself. No separate DoE certificate.",
             "Rule 55(6): after checking the records, the Head of Office himself issues the No Demand Certificate for the cases in sub-rules (4) and (5); no separate certificate from the Directorate of Estates is needed. Close restatement; Gazette text not read. Ledger: R55(6) (changed: added).",
             GREEN,
             "Sub-rule six: for these no-housing cases, the Head of Office checks the records and issues the No Demand Certificate himself. The Directorate of Estates need not issue a separate certificate."),
            ("THE EXPLANATION",
             "'Directorate of Estates' includes any other office or agency that handles allotment and upkeep of housing.",
             "Explanation to Rule 55: 'Directorate of Estates' includes any other office or agency that handles allotment and maintenance of accommodation in a Department or office. Close restatement; Gazette text not read. Ledger: R55-EXPL (changed: added).",
             SKY,
             "The Explanation widens the name. Directorate of Estates also means any other office or agency that looks after allotment and upkeep of housing in a department. So a department with its own housing cell is covered."),
            ("EXAMPLE AND TRAP",
             "Example: Asha never took official housing. She gives a declaration; her HoO issues the NDC.",
             "Example (invented): Asha always lived in her own house and never applied for official housing. One year before her superannuation she gives the declaration; her Head of Office checks the records and issues the NDC himself. Trap: do not wait for a Directorate of Estates certificate in such a case; and do not confuse these sub-rules with Rule 55(1) (allottees). The source script had only a gist of Rule 55, so sub-rules 55(4)-(6) and the Explanation were added from the rule summary.",
             RED,
             "Here is an example. Asha always lived in her own house. One year before retiring she gives the declaration, and her Head of Office issues the certificate himself. The trap is to wait for a Directorate certificate that is not needed in this case."),
        ],
        "hook": "REMEMBER: never had housing = declaration, and the Head of Office issues the NDC himself!",
        "hook_say": "Remember: if a person never had government housing, he gives a declaration, and the Head of Office issues the no demand certificate himself.",
        "covers": ["R55(4)", "R55(5)", "R55(6)", "R55-EXPL"],
    },
    {
        "id": "c5_06_rule56",
        "chapter": "CHAPTER 6 • RULE 56: WHEN PREPARATION STARTS",
        "title": "RULE 56 — PREPARATION STARTS ONE YEAR BEFORE, OR AT LEAVE, WHICHEVER IS EARLIER",
        "accent": SKY, "badge": "RULE 56",
        "q": "From which day must the office start preparing a retiring person's pension case?",
        "q_say": "Sir, from which day must the office start preparing the pension case of a person who is about to retire?",
        "boxes": [
            ("THE RULE • RULE 56",
             "Start the pension work one year before retirement, or on the day leave before retirement begins, whichever is EARLIER.",
             "Rule 56: the Head of Office starts the preparatory work of the pension case from the day one year before the Government servant is due to retire on superannuation, or from the day he proceeds on leave preparatory to retirement, whichever is earlier. Ledger: R56. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "Let us take the rule first. The Head of Office begins the preparatory work from one year before superannuation, or from the day the servant goes on leave preparatory to retirement, which we shorten to LPR. LPR is leave taken just before retiring. Whichever of the two days comes first is the starting day."),
            ("EARLIER, NOT LATEST",
             "Rule 56 says earlier. The source says Rule 51 says latest. Not re-checked in this batch.",
             "The source script contrasts Rule 56 ('whichever is earlier') with Rule 51 ('whichever is latest'). Rule 51 was not re-read in this batch; check the Batch 4 ledger before quoting the contrast. The reason for 'earlier' is a teaching reading: preparation should begin at the first warning. Ledger: R56-VS-R51 (unverified).",
             ORANGE,
             "The source contrasts this with Rule fifty-one, which it says uses the word latest. We did not re-read Rule fifty-one in this batch, so treat that contrast as not confirmed here. The reasoning is simple: preparation should begin at the first warning, so the earlier day wins."),
            ("REAL EXAMPLE",
             "Example: Bilal retires 30 June 2027. One year before is 30 June 2026. If his leave began earlier, work starts then.",
             "Example (invented; the logic follows the source's own example, recomputed): Bilal is due to retire on superannuation on 30 June 2027. One year before is 30 June 2026. If he goes on leave preparatory to retirement from 1 March 2026, that day is earlier, so the preparatory work starts on 1 March 2026. If his leave begins after 30 June 2026 or he takes none, work starts on 30 June 2026. Note: how long leave preparatory to retirement can last is a Leave Rules matter that was not checked here; the dates only show the 'earlier' test. Ledger: R56-EX, QA-R56.",
             GREEN,
             "Here is a real example. Bilal retires on thirtieth June two thousand twenty-seven, so one year before is thirtieth June two thousand twenty-six. Suppose he went on leave preparatory to retirement from the first of March two thousand twenty-six. That is earlier, so the work would start on the first of March. If the leave began later, or never, the work starts on thirtieth June. The dates only show the earlier test; the allowed length of such leave was not checked here."),
            ("THE TRAP: THE DATES OF 54-56",
             "Before retirement: 15 months, the 15th, month-end, 10 days, 1 year, 8 months.",
             "Recap of the pre-retirement timelines in Rules 54 to 56: Rule 54: fifteen-month window, list by the 15th, copy before month-end, other retirements within ten days; Rule 55: details to the Directorate of Estates at least one year ahead, eight months of NDC coverage, ten days to forward; Rule 56: one year or LPR, whichever is earlier. Everything here happens BEFORE retirement so no file is empty on the day. Ledger: BONUS-49-SIXDATES. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "Remember the dates of Rules fifty-four to fifty-six. Fifteen months ahead, the fifteenth of the month, month-end, ten days, one year, and eight months. All of them are about getting ready before the retirement day arrives."),
        ],
        "hook": "REMEMBER: Rule 56 = one year before or LPR date, whichever is EARLIER!",
        "hook_say": "Remember: Rule fifty-six starts the work one year before retirement or on the leave date, whichever is earlier.",
        "covers": ["R56", "R56-VS-R51", "R56-EX", "QA-R56", "BONUS-49-SIXDATES"],
    },
    {
        "id": "c5_07_rule57_stage1",
        "chapter": "CHAPTER 7 • RULE 57(1)(a): STAGE ONE, VERIFYING THE SERVICE",
        "title": "RULE 57(1)(a) — STAGE ONE: VERIFY EVERY PERIOD OF SERVICE",
        "accent": ORANGE, "badge": "RULE 57(1)(a)",
        "q": "In stage one of Rule 57, how is the service verified, and what if records are missing?",
        "q_say": "Sir, in the first stage of Rule 57, how is the service checked, and what happens if some records are missing or the other office does not reply?",
        "boxes": [
            ("CHECK THE BOOK • (a)(i)-(ii)",
             "HoO checks the service book for service after the Rule 30 check. Gaps: pay bills, last pay certificate, April pay slip.",
             "Rule 57(1)(a)(i): the Head of Office checks the service book for the service after the period already verified under Rule 30. (ii): service not verified is checked from other records such as pay bills, acquittance rolls, the last pay certificate and the April pay slip, and certificates recorded in the service book. Link to Rule 30: Rule 57(1)(a)(i) is confirmed; the 18-year and 5-year figures of Rule 30 belong to Batch 2 and were not re-read here. Ledger: R57(1)-3STAGES, R57(1)(a)(i), R57(1)(a)(ii), R56-R57-R30 (unverified: Rule 30 figures). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Rule fifty-seven splits the one year of preparation into three stages. Stage one is service verification. The service book is the record of a servant's career. Under sub-clause one, the Head of Office checks the service after the period already verified under Rule thirty. Under sub-clause two, any unverified part is checked from other records: pay bills, acquittance rolls, which are signed pay receipts, the last pay certificate and the April pay slip."),
            ("OTHER OFFICE • (a)(iii)-(v)",
             "Service in another office: ask that office. It must reply in 2 months. No reply: the period counts as qualifying.",
             "Rule 57(1)(a)(iii): service in another office is referred to the Head of Office there. (iv): that office replies within two months and states at the same time what cannot be verified. (v): if no reply comes, the period is treated as qualifying for pension (deemed qualifying, silence in the servant's favour). Ledger: R57(1)(a)(iii), (iv), (v). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "If part of the service was in another office, the Head of Office there is asked. That office must reply within two months and must also say what it cannot verify. If no reply comes, the period is treated as qualifying for pension. Qualifying service is the service that counts for working out the pension. So silence helps the servant."),
            ("LATE FINDS, 8-MONTH FINISH • (vi)-(vii)",
             "A non-qualifying period found later: the Ministry's Secretary fixes responsibility. All steps end 8 months before.",
             "Rule 57(1)(a)(vi): if a non-qualifying period is found later that was not communicated, the Secretary of the Ministry fixes responsibility on the Head of Office and the other concerned authorities. (vii): these steps are to be completed eight months before superannuation. Ledger: R57(1)(a)(vi), R57(1)(a)(vii), TL-SVC-VERIF-8M. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "If a non-qualifying period is found later and nobody had reported it, the Secretary of the Ministry fixes the responsibility. And the whole of stage one must be finished eight months before superannuation."),
            ("THE SAFETY NET • (a)(viii)-(x)",
             "Cannot verify a portion? The servant gives a plain-paper statement within 1 month. HoO may admit it. Lying = grave misconduct.",
             "Rule 57(1)(a)(viii): for a portion that still cannot be verified, the servant files a written statement on plain paper within one month, with a declaration of truth. (ix): the Head of Office considers the statement and may admit that service for the pension calculation. (x): wilfully giving wrong information is grave misconduct. Ledger: R57(1)(a)(viii), (ix), (x). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "For a part that cannot be verified at all, the servant files a statement on plain paper within one month, with a declaration that it is true. The Head of Office considers it and may admit that service for the pension calculation. But wilfully giving wrong information is grave misconduct."),
            ("REAL EXAMPLE",
             "Example: Asha's old-office reply does not come in 2 months. That period counts as qualifying.",
             "Example (invented): Asha, a senior assistant, once served in another department. Her Head of Office writes there; no reply comes in two months, so the period is treated as qualifying. A small stretch cannot be verified anywhere, so she files a plain-paper statement within one month with a declaration of truth, and the Head of Office admits it for the pension calculation. Ledger: R57-EX-SENIORASST, QA-R57.",
             RED,
             "Here is a real example. Asha served earlier in another department. That office does not reply in two months, so the period is treated as qualifying. One small stretch cannot be verified anywhere, so she files a statement within one month, and the Head of Office admits it."),
        ],
        "hook": "REMEMBER: no reply in 2 months = qualifying; unverified bit = 1-month statement; lying = grave misconduct!",
        "hook_say": "Remember: no reply in two months means the period qualifies, an unverified bit needs a one month statement, and lying is grave misconduct.",
        "covers": ["R57(1)-3STAGES", "R57(1)(a)(i)", "R57(1)(a)(ii)", "R57(1)(a)(iii)", "R57(1)(a)(iv)", "R57(1)(a)(v)", "R57(1)(a)(vi)", "R57(1)(a)(vii)", "R57(1)(a)(viii)", "R57(1)(a)(ix)", "R57(1)(a)(x)", "R57-EX-SENIORASST", "QA-R57", "TL-SVC-VERIF-8M", "R56-R57-R30"],
    },
    {
        "id": "c5_08_rule57_stage23",
        "chapter": "CHAPTER 8 • RULE 57(1)(b)-(c): STAGES TWO AND THREE",
        "title": "RULE 57(1)(b)-(c) — FIX THE GAPS, THEN GIVE THE CERTIFICATE AND ASK FOR FORM 6-A",
        "accent": BLUE, "badge": "RULE 57(1)(b)-(c)",
        "q": "What happens in stages two and three of Rule 57, and which figures matter?",
        "q_say": "Sir, what happens in stages two and three of Rule 57, and which figures matter?",
        "boxes": [
            ("STAGE TWO • 57(1)(b)",
             "Scrutinise certificates, find and fix omissions. Cannot fix? Ignore; use the service book entries.",
             "Rule 57(1)(b): the Head of Office scrutinises the certificates and identifies omissions and defects affecting emoluments and qualifying service, and makes them good as far as possible. What cannot be corrected, and what the servant has not covered by a statement, is ignored, and qualifying service is determined from the service book entries. Ledger: R57(1)(b)-OMISSIONS. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "Stage two is making good the omissions. The Head of Office scrutinises the certificates and finds the gaps and defects that affect emoluments and qualifying service. Emoluments means the pay that counts for pension. Gaps are corrected as far as possible. What cannot be corrected is ignored, and qualifying service is then fixed from the service book entries."),
            ("24 MONTHS ONLY • 57(1)(b)",
             "Emoluments are verified for the last 24 months only. A 'last ten months' mention is NOT confirmed.",
             "Rule 57(1)(b): verification of emoluments is limited to the last twenty-four months. The Accounts Officer has the same limit in Rule 63(1)(c), so the two checks match. One secondary summary also mentions emoluments of the last ten months checked against the service book; this is a single mention, not in the source script, and UNVERIFIED: do not quote it on a card as fact. Ledger: R57(1)(b)-24MONTHS, TL-EMOL-24M, R57(1)(b)-TENMONTHS (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Remember the limit: emoluments are verified only for the last twenty-four months. The Accounts Officer has the same limit later, in Rule sixty-three, so both sides match. One summary also mentioned ten months. We saw it only once and it is not confirmed, so do not quote it."),
            ("STAGE THREE • 57(1)(c)(i)-(ii)",
             "At least 8 months before retirement the HoO gives a certificate. Not acceptable? Give reasons within 2 months.",
             "Rule 57(1)(c)(i): at least eight months before retirement the Head of Office gives the servant a certificate of the proposed qualifying service, emoluments and average emoluments. (ii): if the servant does not accept the certificate, he may give his reasons within two months. Ledger: R57(1)(c)(i), R57(1)(c)(ii), TL-CERT-8M. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Stage three is the certificate and the forms. At least eight months before retirement, the Head of Office gives the servant a certificate showing the proposed qualifying service, emoluments and average emoluments. If the servant does not accept it, he can give his reasons within two months."),
            ("FORM 6-A NOW • 57(1)(c)(iii)",
             "Advise the servant to submit Form 6-A. OBSOLETE / HISTORY ONLY: old Forms 4 and 6, Format 9 and Form A.",
             "Rule 57(1)(c)(iii) now reads that the Head of Office advises the retiring Government servant to submit Form 6-A (substituted by G.S.R. 410(E)). The source script said 'Form 6-A and the old forms that remain'; no such 'remaining old forms' limb exists now, so that source flag is closed. OBSOLETE / HISTORY ONLY: the pre-2024 text named Forms 4 and 6, the Format 9 undertaking, the Form A nomination and the medical option form; all replaced by Form 6-A. Ledger: R57(1)(c)(iii) (changed), R57(1)(c)(iii)-OLD (obsolete). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "The last step of stage three is to advise the servant to submit Form 6-A. This is the change from 2024. Before that, the rule named several old forms, such as Forms four and six and a Format nine undertaking. That is history only; Form 6-A replaced them, and no limb about remaining old forms exists now."),
        ],
        "hook": "REMEMBER: stage 2 fixes gaps (24 months only); stage 3 = certificate at 8 months, then Form 6-A!",
        "hook_say": "Remember: stage two fixes the gaps with a twenty-four month limit, and stage three is the certificate at eight months, followed by Form 6-A.",
        "covers": ["R57(1)(b)-OMISSIONS", "R57(1)(b)-24MONTHS", "R57(1)(b)-TENMONTHS", "R57(1)(c)(i)", "R57(1)(c)(ii)", "R57(1)(c)(iii)", "R57(1)(c)(iii)-OLD", "TL-CERT-8M", "TL-EMOL-24M"],
    },
    {
        "id": "c5_09_rule57_form",
        "chapter": "CHAPTER 9 • RULE 57(2)-(3): FORM 6-A, SIX MONTHS BEFORE",
        "title": "RULE 57(2)-(3) — WHEN FORM 6-A IS DUE, AND WHO FILES IT IF THE SERVANT CANNOT",
        "accent": GREEN, "badge": "RULE 57(2)-(3)",
        "q": "When must the retiring servant file Form 6-A, and who can file it if he is unwell?",
        "q_say": "Sir, when must the retiring servant file Form 6-A, and who can file it if he is unable to?",
        "boxes": [
            ("THE DEADLINE • RULE 57(2)(a)",
             "The servant gives a completed Form 6-A to the HoO not later than SIX months before retirement.",
             "Rule 57(2)(a), exact text as quoted in the 2024 notification reproduction: 'duly completed Form 6-A ... not later than six months prior to his date of retirement'. The six months did not change in 2024. Ledger: R57(2)(a), TL-6A-SUPER. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Let us take the rule first. The servant must give the Head of Office a duly completed Form 6-A not later than six months before the date of retirement. Form 6-A is the single pension application form. The six months did not change in the 2024 amendment."),
            ("COMMUTATION • RULE 57(2)(b)",
             "He may also apply for commutation. After 2024, 'Form 6' is read as Form 6-A. Exact words: check the Gazette.",
             "Rule 57(2)(b) (omitted by the source script): if he wishes, the Government servant also applies, in Form 6, for commutation under the Commutation of Pension Rules, 1981. After 2024, 'Form 6' is read as 'Form 6-A' throughout the Rules (Rule 12 of the amendment). The exact current wording of 57(2)(b) should be checked in the Gazette. Commutation means taking part of the pension as a lump sum. Ledger: R57(2)(b) (changed: added). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "The source guide left out sub-rule two, clause b. If he wishes, the servant also applies for commutation under the Commutation of Pension Rules of nineteen eighty-one. Commutation means taking part of the pension as a lump sum now. After 2024, the old Form six is read as Form 6-A. Please check the Gazette for the exact current wording."),
            ("IF HE CANNOT FILE • 57(3)",
             "Unable through infirmity? First the spouse or another eligible family member; if none, the gratuity nominee.",
             "Rule 57(3): if the servant cannot submit the form because of infirmity, it is submitted by (a) the spouse or any other eligible family member, or (b) if there is no such member, a person nominated for gratuity. The source script had only two tiers (spouse, then 'the member') and missed the nominee tier. Proviso (substituted in 2024): where the form is submitted by the spouse or any other family member, the Government servant is not entitled to commutation of a percentage of pension until he himself later applies under the Commutation of Pension Rules, 1981. Ledger: R57(3)-TIERS (changed), R57(3)-PROVISO. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "If the servant cannot file because of infirmity, the spouse or another eligible family member files it. If there is no such member, the person nominated for gratuity files it. The source guide missed this last tier. The proviso says that when someone else files, the servant gets no commutation until he himself applies later under the nineteen eighty-one rules."),
            ("EXAMPLE AND TRAP",
             "Example: Bilal is in hospital; his wife files Form 6-A. No commutation until he applies himself.",
             "Example (invented): Bilal is seriously ill in hospital six months before his retirement. His wife Charu files Form 6-A for him. His pension is worked out as usual, but he is not entitled to commutation until he himself later applies under the 1981 Rules. Trap: Rule 58 uses the same tiers, so the claim that Rule 58 is 'broader' is not supported (see the next chapter).",
             RED,
             "Here is a real example. Bilal is in hospital six months before his retirement, so his wife Charu files Form 6-A. His pension is worked out as usual, but he cannot take commutation until he applies himself later. And remember, the trap: Rule fifty-eight uses the same tiers, as we shall see."),
        ],
        "hook": "REMEMBER: Form 6-A at 6 months; if infirm, spouse or family, then the gratuity nominee!",
        "hook_say": "Remember: Form 6-A is due six months before; if the servant is infirm, the spouse or family files, and then the gratuity nominee.",
        "covers": ["R57(2)(a)", "R57(2)(b)", "R57(3)-TIERS", "R57(3)-PROVISO", "TL-6A-SUPER"],
    },
    {
        "id": "c5_10_rule58",
        "chapter": "CHAPTER 10 • RULE 58: OTHER RETIREMENTS, AND RULE 57 SIDE BY SIDE",
        "title": "RULE 58 VERSUS RULE 57 — SAME FORM, DIFFERENT CLOCK",
        "accent": PINK, "badge": "RULES 57 • 58",
        "q": "How does Rule 58 differ from Rule 57 for a retirement that is not superannuation?",
        "q_say": "Sir, how does Rule 58 differ from Rule 57 for a retirement that is not superannuation?",
        "boxes": [
            ("THE RULE • RULE 58(1)",
             "Retiring for a reason other than superannuation? Submit Form 6-A to the HoO immediately after approval or effect.",
             "Rule 58(1), exact text: the Government servant 'shall submit Form 6-A to the Head of Office, immediately after the competent authority has approved such retirement or the retirement has become effective'. The rule covers one 'retiring or has retired for reasons other than superannuation'. The source's list (voluntary, compulsory, invalid, resignation) is a teaching list; whether a resignation case belongs here depends on the pension rules for resignation (Batches 2 and 3), so do not list resignation without checking. Ledger: R58(1), R58-SCOPE-EXAMPLES (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "Rule fifty-eight is for a person retiring for a reason other than superannuation, such as voluntary retirement. There is no calendar clock. The form is submitted immediately after the competent authority approves the retirement, or after it takes effect. The source also lists resignation here; we could not confirm that, so do not rely on it."),
            ("INFIRMITY • 58(2) AND PROVISO",
             "Same tiers as Rule 57(3): spouse or family member, then the gratuity nominee. Same commutation proviso.",
             "Rule 58(2) has the same tiers as Rule 57(3): the spouse or any other eligible family member, then the gratuity nominee. The Rule 58 proviso: if the form is submitted by the spouse or any other family member, no commutation of pension until he himself applies under the 1981 Rules. The source claimed Rule 58 says 'ANY OTHER member' and so is broader than Rule 57 ('the member'); that is NOT supported: both substituted provisos say 'spouse or any other member of the family'. Drop the claimed difference. Ledger: R58(2) (changed), R58-PROVISO, R57-VS-58-INFIRMITY (changed). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "The infirmity tiers are the same as in Rule fifty-seven: the spouse or another eligible family member, and then the gratuity nominee. The proviso on commutation is also the same. The source guide claimed Rule fifty-eight is broader because of the words any other member. That is not supported, because both rules use the same words, so please drop that claim."),
            ("SIDE BY SIDE",
             "Form: 6-A in both. Rule 57: six months BEFORE. Rule 58: IMMEDIATELY after the event.",
             "Rule 57 versus Rule 58. Form: Form 6-A in both (consensus after 2024). When: Rule 57, not later than six months before retirement; Rule 58, immediately after approval or effect. Clock: Rule 57 counts backward from a known date (the script's teaching label: calendar clock); Rule 58 counts forward from an event (teaching label: event clock). The labels are teaching words, not rule words; the timings are confirmed. Ledger: R57-VS-58-FORM-TIMING, R57-58-CLOCK-LABELS, TL-6A-NONSUPER. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Now put them side by side. The form is Form 6-A in both. In Rule fifty-seven it is due six months before retirement, and in Rule fifty-eight it is due immediately after approval. As a memory aid, Rule fifty-seven is a calendar clock counted back from a known date, and Rule fifty-eight is an event clock counted forward from the event. Those two labels are teaching words, not rule words."),
            ("EXAMPLE AND TRAP",
             "Example: Dev's voluntary retirement is approved on 10 May. His Form 6-A goes in at once. No six-month window.",
             "Example (invented): Dev's voluntary retirement is approved on 10 May 2027 and takes effect on 31 July 2027. He submits Form 6-A immediately after the approval or once it takes effect, as Rule 58(1) says, and does not wait for any six-month window. Trap: expecting a six-month window in Rule 58 cases; the delay makes Form 6-A late and holds up the provisional pension and gratuity. Ledger: QA-R58.",
             RED,
             "Here is a real example. Dev's voluntary retirement is approved on the tenth of May two thousand twenty-seven. He submits Form 6-A at once, because the rule says immediately. The trap is to expect a six month window in such cases. There is none, and a late form delays the provisional pension and gratuity."),
        ],
        "hook": "REMEMBER: same Form 6-A; Rule 57 = 6 months before, Rule 58 = immediately!",
        "hook_say": "Remember: the form is the same Form 6-A; Rule fifty-seven needs it six months before, and Rule fifty-eight needs it immediately.",
        "covers": ["R58(1)", "R58(2)", "R58-PROVISO", "R58-SCOPE-EXAMPLES", "R57-VS-58-INFIRMITY", "R57-VS-58-FORM-TIMING", "R57-58-CLOCK-LABELS", "TL-6A-NONSUPER", "QA-R58"],
    },
    {
        "id": "c5_11_rule59",
        "chapter": "CHAPTER 11 • RULE 59: FORM 7, PART I",
        "title": "RULE 59 — THE HEAD OF OFFICE FILLS PART I OF FORM 7",
        "accent": RED, "badge": "RULE 59",
        "q": "What does Rule 59 ask the Head of Office to prepare, and by when?",
        "q_say": "Sir, what does Rule 59 ask the Head of Office to prepare, and by when?",
        "boxes": [
            ("THE RULE • RULE 59(1)",
             "HoO completes Part I of Form 7, with the check list and the calculation sheet.",
             "Rule 59(1): the Head of Office completes Part I of Form 7 together with the check list and the pension calculation sheet. Form 7 is the pension case form; Part I is the Head of Office's part, and Part II is filled by the Accounts Officer (Rule 63(1)(a)). Ledger: R59(1)-SUPER, R59-PARTI-PARTII. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "Let us take the rule first. Form 7 is the pension case form. Under Rule fifty-nine, the Head of Office completes Part one of it, with a check list and a pension calculation sheet. Part two will be filled later by the Accounts Officer."),
            ("THE TIME LIMITS • 59(1)",
             "Rule 57 cases: not later than 4 months before retirement. Rule 58 cases: within 2 months after Form 6-A.",
             "Rule 59(1): in Rule 57 (superannuation) cases, not later than four months before retirement; in Rule 58 cases, within two months after the Form 6-A is submitted. The source script's Rule 58 limb was truncated; it is resolved here, and Rule 60(4) uses the same two months. Ledger: R59(1)-SUPER, R59(1)-NONSUPER, TL-PARTI-FORM7. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Now the time limits. For superannuation cases, Part one must be ready not later than four months before retirement. For the other cases, it must be ready within two months after Form 6-A is submitted. The source guide did not show the second limit, but it is now confirmed, and Rule sixty uses the same two months."),
            ("IF THE PENSIONER DIES • 59(2)",
             "A retired servant dies before the forms are in? Action follows Rule 80(5).",
             "Rule 59(2) (omitted by the source script): if a retired Government servant dies before the forms are submitted, action follows Rule 80(5) (a Batch 6 rule). In 2024, 59(1) replaced 'Form 4 and Form 6' with 'Form 6-A', and 59(2) replaced 'have' with 'has'. Items 9 and 10 of the Form 7 check list (timely processing of retirement dues) were omitted by Rule 13 of the 2024 amendment; the wording of those items was not read. Ledger: R59(2) (changed), R59-2024, FORM7-CHECKLIST-2024 (changed). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "The source guide missed sub-rule two. If a retired servant dies before the forms are submitted, the case follows Rule eighty, sub-rule five, which we will meet in batch six. The 2024 amendment also changed Rule fifty-nine to say Form 6-A, and it removed items nine and ten from the Form 7 check list. We did not read the wording of those two items."),
            ("EXAMPLE AND TRAP",
             "Example: Esha retires 31 May 2027. Her HoO must finish Part I and the sheet by 31 Jan 2027. Part II is the AO's.",
             "Example (invented): Esha retires on 31 May 2027. Her Head of Office completes Part I of Form 7 with the check list and calculation sheet by 31 January 2027 (four months before). Trap: Part I belongs to the Head of Office and Part II to the Accounts Officer; the Form 7 split is explained again in Rule 63. A rule of thumb (a memory aid, not a rule): whoever knows the servant fills Part I, whoever knows the accounts fills Part II.",
             SKY,
             "Here is a real example. Esha retires on thirty-first May two thousand twenty-seven. Her Head of Office must finish Part one, with the check list and calculation sheet, by thirty-first January two thousand twenty-seven. The trap is to mix up the two parts: Part one is the Head of Office's, and Part two is the Accounts Officer's."),
        ],
        "hook": "REMEMBER: Form 7 Part I = Head of Office, 4 months before (or 2 months after Form 6-A)!",
        "hook_say": "Remember: Part one of Form 7 belongs to the Head of Office, four months before retirement, or two months after Form 6-A in other cases.",
        "covers": ["R59(1)-SUPER", "R59(1)-NONSUPER", "R59(2)", "R59-PARTI-PARTII", "R59-2024", "FORM7-CHECKLIST-2024", "TL-PARTI-FORM7"],
    },
    {
        "id": "c5_12_rule60",
        "chapter": "CHAPTER 12 • RULE 60: SENDING THE CASE TO THE ACCOUNTS OFFICER",
        "title": "RULE 60 — WHAT GOES TO THE ACCOUNTS OFFICER, AND BY WHEN",
        "accent": ORANGE, "badge": "RULE 60",
        "q": "What must the Head of Office send to the Accounts Officer, and what is the deadline?",
        "q_say": "Sir, what must the Head of Office send to the Accounts Officer, and what is the deadline?",
        "boxes": [
            ("THE THREE ITEMS • RULE 60(1)",
             "After Rules 57, 58, 59 are done: (i) Form 6-A, (ii) Form 7 + check list + sheet + Format 10 letter, (iii) service book.",
             "Rule 60(1): before sending, Rules 57, 58 and 59 must have been complied with. Items: (i) Form 6-A; (ii) copies of Form 7, the check list and the calculation sheet, with a covering letter in Format 10; (iii) the complete, up-to-date service book and the other documents used for verification. Ledger: R60(1)-PRECOND, R60(1)(i), R60(1)(ii), R60(1)(iii), R60-FORMAT10. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Let us take the rule first. Before sending the case, Rules fifty-seven, fifty-eight and fifty-nine must be complied with. Then three items go. One, Form 6-A. Two, copies of Form 7 with the check list and the calculation sheet, under a covering letter in Format ten. Three, the complete and up-to-date service book and the papers used for verification."),
            ("WHAT FORM 6-A REPLACED",
             "OBSOLETE / HISTORY ONLY: Form 4, Form 6 and the Format 9 bank undertaking. Replaced by Form 6-A.",
             "OBSOLETE / HISTORY ONLY: before 2024, item (i) was copies of Form 4, Form 6 and an undertaking to the Bank in Format 9; replaced by Form 6-A under G.S.R. 410(E). The source script called this the amendment's 'fourteenth substitution' and said Form 6-A merged nine forms. The notification has 14 numbered items, but 'fourteenth substitution' and 'nine forms merged' are NOT confirmed (see GSR410-1 in Batch 1): say only that Form 6-A replaces the Form 4/6/Format 9 undertaking in Rule 60(1)(i). Format 10 was also amended in 2024 (item 2 'Form 6-A or Form 10'; item 3 Form 10 family details and Format 9 undertaking; item 4 'Form 7 or Form 11'). The source says Format 9 stays separate for death cases; Format 10 item 3 still names Format 9 for Form 10 cases, but the broader claim was not re-read: unverified. Ledger: R60(1)(i)-OLD (obsolete), R60-CHAUDHA-CLAIM (unverified), R60-FORMAT9-DEATH (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "Before 2024, item one was copies of Form four, Form six and a bank undertaking in Format nine. That is history only. Form 6-A replaced them. The source guide called this the fourteenth substitution and said nine forms were merged, but we could not confirm either claim, so just say that Form 6-A replaces those old forms in Rule sixty. Also, whether Format nine stays separate for death cases was not re-checked."),
            ("GOVERNMENT DUES • 60(2)-(3)",
             "Also send the Government dues details; the HoO himself assesses them. HoO keeps a copy of every form.",
             "Rule 60(2): the Government dues under Rule 67, and the intimation under Rule 68(5), are sent in Format 10; the Head of Office ascertains and assesses the dues (not the Accounts Officer), so recovery from gratuity can happen before payment is authorised. Rule 60(3): the Head of Office keeps a copy of each form and format (2024 wording: 'copies of Form and Format' replaces 'a copy of each of the Forms'). Ledger: R60(2), R60(3). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Sub-rule two adds the Government dues. The details of dues under Rule sixty-seven, and the housing intimation under Rule sixty-eight, sub-rule five, are sent along. It is the Head of Office who ascertains and assesses the dues, not the Accounts Officer. The aim is to recover dues from the gratuity before it is paid. Sub-rule three says the Head of Office keeps a copy of every form."),
            ("THE DEADLINE • RULE 60(4)",
             "At retirement age: send 4 months before. Other cases: within 2 months after receiving the forms.",
             "Rule 60(4): in superannuation cases, not later than four months before retirement; in other cases, within two months after the forms are received. The 2024 amendment changed only the form reference to Form 6-A. Ledger: R60(4), TL-CASE-AO. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "The deadline is in sub-rule four. For superannuation, the case must reach the Accounts Officer not later than four months before retirement. For other cases, within two months after the forms are received. The 2024 amendment only changed the form name to Form 6-A."),
            ("EXAMPLE AND TRAP",
             "Q: who assesses the dues, AO or HoO? Answer: the Head of Office. The AO only authorises.",
             "Question: who prepares the Government dues details, the Accounts Officer or the Head of Office? Answer: the Head of Office, under Rule 60(2); the Accounts Officer only authorises payment. Example (invented): Bilal retires on 30 September 2027; his Head of Office must send the full case, with the dues details, by 31 May 2027. Ledger: QA-R60.",
             RED,
             "Here is a typical question. Who prepares the dues details, the Accounts Officer or the Head of Office? The Head of Office does, under sub-rule two; the Accounts Officer only authorises. For example, if Bilal retires on thirtieth September two thousand twenty-seven, his case must reach the Accounts Officer by thirty-first May."),
        ],
        "hook": "REMEMBER: Rule 60 = Form 6-A + Form 7 set + service book, 4 months before; HoO assesses the dues!",
        "hook_say": "Remember: Rule sixty sends Form 6-A, the Form 7 set and the service book, four months before retirement, and the Head of Office assesses the dues.",
        "covers": ["R60(1)-PRECOND", "R60(1)(i)", "R60(1)(i)-OLD", "R60(1)(ii)", "R60(1)(iii)", "R60(2)", "R60(3)", "R60(4)", "R60-CHAUDHA-CLAIM", "R60-FORMAT10", "R60-FORMAT9-DEATH", "TL-CASE-AO", "QA-R60"],
    },
    {
        "id": "c5_13_rule61",
        "chapter": "CHAPTER 13 • RULE 61: CHANGES AFTER THE CASE HAS BEEN SENT",
        "title": "RULE 61 — TELL THE ACCOUNTS OFFICER PROMPTLY IF ANYTHING CHANGES",
        "accent": GREEN, "badge": "RULE 61",
        "q": "What if something changes, or new dues appear, after the case has gone to the Accounts Officer?",
        "q_say": "Sir, what if something changes, or new dues appear, after the case has already gone to the Accounts Officer?",
        "boxes": [
            ("EVENTS AFTER SENDING • 61(1)",
             "Anything that happens after the case is forwarded: report it to the Accounts Officer promptly.",
             "Rule 61(1): events occurring after the case has been forwarded are reported promptly by the Head of Office to the Accounts Officer. Ledger: R61(1). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Let us take the rule first. After the case is forwarded, things can change. Under sub-rule one, the Head of Office must report such events to the Accounts Officer promptly."),
            ("NEW DUES • 61(2)",
             "New Government dues found after the Rule 60(2) intimation are reported the same way.",
             "Rule 61(2): if additional Government dues come to light after the Rule 60(2) intimation, they are also reported promptly. The rule sets no day limit; the word is 'promptly'. Ledger: R61(2). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Sub-rule two covers new dues. If more Government dues turn up after the earlier intimation, the Head of Office reports them in the same way. There is no number of days here; the word is simply promptly."),
            ("EXAMPLE AND TRAP",
             "Example: two months later Charu's old house building advance balance appears. HoO reports it at once.",
             "Example (invented): after Charu's case is forwarded, the Head of Office finds a balance on her house building advance. He writes to the Accounts Officer at once, and the amount is adjusted before the gratuity is paid. Trap: expecting a fixed number of days in Rule 61; there is none. Ledger: R61-EX (the logic is fine; invented example).",
             RED,
             "Here is a real example. Two months after Charu's case is sent, the office finds a balance on her house building advance. The Head of Office writes at once, and the amount is adjusted before her gratuity is paid. The trap is to look for a fixed number of days; Rule sixty-one has none."),
        ],
        "hook": "REMEMBER: Rule 61 = report changes and new dues PROMPTLY, no day limit!",
        "hook_say": "Remember: Rule sixty-one says report changes and new dues promptly, with no fixed number of days.",
        "covers": ["R61(1)", "R61(2)", "R61-EX"],
    },
    {
        "id": "c5_14_rule62a",
        "chapter": "CHAPTER 14 • RULE 62(1)-(4): PROVISIONAL PENSION WHEN THE FILE IS LATE",
        "title": "RULE 62(1)-(4) — WHEN AND HOW A PROVISIONAL PENSION IS SANCTIONED",
        "accent": SKY, "badge": "RULE 62(1)-(4)",
        "q": "If the final pension cannot be fixed in time, what does the retiree get meanwhile?",
        "q_say": "Sir, if the final pension cannot be fixed in time, what does the retiring person get in the meantime?",
        "boxes": [
            ("WHEN IT APPLIES • 62(1)",
             "For delays NOT caused by disciplinary or court cases. Case not sent on time, or AO asks for more details.",
             "Rule 62 scope: delays for reasons other than departmental or judicial proceedings (those are dealt with under Rule 8 and Rule 63(5); the source script named Rule 64 here, but Rule 64 is the deputation rule). Rule 62(1) (superannuation): despite Rule 57 being followed, the case cannot be forwarded in the Rule 60(4) period, or the Accounts Officer returned it asking for information before the PPO or gratuity order; and the servant is likely to retire before final assessment. The Head of Office then acts on the information available in the official records and does not wait. Provisional pension means an interim pension paid while the final calculation is pending. Ledger: R62-SCOPE, R62(1). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "Rule sixty-two is about provisional pension, an interim pension paid while the final amount is still being worked out. It applies to delays that are not caused by disciplinary or court proceedings. Under sub-rule one, for superannuation, it applies if the case could not be sent within the Rule sixty period, or if the Accounts Officer sent it back asking for more information, and the servant is about to retire. The Head of Office then works from the official records he has."),
            ("OTHER RETIREMENTS • 62(2), 62(4)",
             "Same treatment after Rule 58 forms. Sanction within 10 days of retirement, or 1 month of the forms.",
             "Rule 62(2): the same treatment for non-superannuation retirement, once the Rule 58 forms are received. Rule 62(4): sanction is issued within ten days of retirement in a sub-rule (1) case, and within one month of receiving the forms in a sub-rule (2) case. Ledger: R62(2), R62(4), TL-PROV-LETTER. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "Sub-rule two gives the same treatment to other retirements, once the Rule fifty-eight forms are received. Sub-rule four sets the time for the sanction: within ten days of retirement in a sub-rule one case, and within one month of receiving the forms in a sub-rule two case."),
            ("THE LETTER OF SANCTION • 62(3)(a)",
             "100% pension from the day AFTER retirement; 100% gratuity, with 10% withheld.",
             "Rule 62(3)(a): a letter of sanction is issued, addressed to the Government servant with a copy to the Accounts Officer, authorising 100 per cent of the pension as provisional pension from the day after retirement, and 100 per cent of the gratuity as provisional gratuity, of which ten per cent is withheld. The floor is 100 per cent, not less. Ledger: R62(3)(a), R62-FLOOR-100, LIMIT-PROV-10PCT. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Here is the heart of the rule. A letter of sanction is issued, addressed to the servant, with a copy to the Accounts Officer. It authorises one hundred percent of the pension as provisional pension from the day after retirement, and one hundred percent of the gratuity as provisional gratuity, of which ten percent is held back. So the provisional pension is never less than the full pension."),
            ("DRAWING THE MONEY • 62(3)(b)",
             "The letter states the Rule 67 recovery. Amounts are drawn like pay and allowances. Gratuity: less 10% and Rule 68 dues.",
             "Rule 62(3)(b): the sanction letter states the amount of recovery assessed under Rule 67; and the provisional pension and provisional gratuity are drawn as pay and allowances of the establishment, so no new mechanism is needed. The gratuity actually drawn is after deducting the ten per cent withheld and the Rule 68 accommodation dues. Three numbers sit in one letter: 100 per cent pension, 100 per cent gratuity less 10 per cent withheld, and the Rule 67 recovery. Ledger: R62(3)(b). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Sub-rule three, clause b adds two things. The letter must state the recovery amount assessed under Rule sixty-seven. And the provisional pension and gratuity are drawn like the establishment's pay and allowances, in the regular bill, so no new mechanism is needed. The gratuity drawn is after the ten percent hold-back and any Rule sixty-eight housing dues."),
            ("REAL EXAMPLE",
             "Esha's gratuity Rs 12,00,000: hold back 10% = Rs 1,20,000. Rs 30,000 housing dues. She receives Rs 10,50,000.",
             "Example (invented figures, recomputed): Esha retires and her PPO is delayed. Provisional gratuity 100 per cent = Rs 12,00,000; ten per cent withheld = Rs 1,20,000; suppose Rule 68 accommodation dues of Rs 30,000. Gratuity drawn now = 12,00,000 minus 1,20,000 minus 30,000 = Rs 10,50,000. Her provisional pension is 100 per cent of her pension from the day after retirement. Ledger: R62-EX (numbers follow the rule; invented).",
             RED,
             "Here is a real example. Esha's PPO is delayed. Her provisional gratuity is twelve lakh rupees. Ten percent, one lakh twenty thousand, is held back. Suppose she also has thirty thousand rupees of housing dues. She receives ten lakh fifty thousand rupees now. Her pension starts in full from the day after retirement."),
        ],
        "hook": "REMEMBER: provisional = 100% pension from next day, 100% gratuity less 10% held back!",
        "hook_say": "Remember: provisional means one hundred percent pension from the next day, and one hundred percent gratuity less ten percent held back.",
        "covers": ["R62-SCOPE", "R62(1)", "R62(2)", "R62(3)(a)", "R62(3)(b)", "R62(4)", "R62-FLOOR-100", "LIMIT-PROV-10PCT", "R62-EX", "TL-PROV-LETTER"],
    },
    {
        "id": "c5_15_rule62b",
        "chapter": "CHAPTER 15 • RULE 62(5)-(10): LIMITS, RECOVERY AND THE ASYMMETRY",
        "title": "RULE 62(5)-(10) — SIX MONTHS, THE ASYMMETRY, AND RELEASING THE 10%",
        "accent": PINK, "badge": "RULE 62(5)-(10)",
        "q": "How long does a provisional pension last, and what if too much was paid?",
        "q_say": "Sir, how long can a provisional pension continue, and what happens if too much was paid?",
        "boxes": [
            ("SIX MONTHS • 62(5), 62(6)(a)",
             "Revise after scrutiny. Provisional pension lasts up to 6 months, counted from the LATER of retirement or Form 6-A.",
             "Rule 62(5) (omitted by the source script): provisional amounts are revised, if needed, after detailed scrutiny of records. Rule 62(6)(a): provisional pension does not continue beyond six months, counted from the date of retirement or the date of submission of Form 6-A, whichever is later. After 2024 'Form 4 and Form 6' is read as Form 6-A there. If the final amounts are fixed in the period, the Accounts Officer issues the PPO and the Head of Office pays the gratuity difference after adjusting dues found later. Ledger: R62(5) (changed: added), R62(6)(a), TL-PROV-MAX-6M. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "Sub-rule five says the provisional amounts are revised after detailed scrutiny. Sub-rule six, clause a, caps the provisional pension at six months, counted from the date of retirement or the date Form 6-A was submitted, whichever is later. If the final amounts are fixed within that time, the Accounts Officer issues the PPO and the Head of Office pays the gratuity difference."),
            ("EXCESS PENSION • 62(6)(b)",
             "Provisional PENSION paid too much? It IS recovered, from the withheld gratuity or from future pension.",
             "Rule 62(6)(b): if the provisional pension paid exceeds the final pension, the excess is recovered from the gratuity that was withheld or by short payment from the future pension. Ledger: R62(6)(b). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Now the famous asymmetry, in two halves. First half: if too much provisional pension was paid, it is recovered, either from the gratuity that was held back or from the future pension."),
            ("EXCESS GRATUITY • 62(6)(c)",
             "Provisional GRATUITY paid too much? NO refund asked from the retiree. HoO must reduce such cases; officials answer for them.",
             "Rule 62(6)(c): no refund is required from the retired servant of any excess provisional gratuity; the Heads of Office are to minimise such cases, and the officials responsible are held accountable. So the system does not put its own error on the pensioner. Ledger: R62(6)(c), QA-R62. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "Second half: if too much provisional gratuity was paid, the retired servant is not asked for a refund. Instead, Heads of Office must keep such cases to a minimum, and the responsible officials are held accountable. Two overpayments, two opposite treatments."),
            ("FINAL STEPS • 62(7)-(10)",
             "Not final in 6 months? AO treats it as final and issues the PPO. 10% released after the PPO; allottees need an NDC.",
             "Rule 62(7): if the amounts are not finalised in six months, the Accounts Officer treats the provisional figures as final and issues the PPO immediately. 62(8): the withheld ten per cent is released after the PPO is issued, after adjusting any dues that surface later. 62(9): if the servant was or is an allottee, the withheld amount is released only on the No Demand Certificate. 62(10): the Head of Office must ensure that provisional sanction is issued whenever the PPO is delayed. Ledger: R62(7), R62(8), R62(9), R62(10). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "If the amounts are still not final after six months, the Accounts Officer treats the provisional figures as final and issues the PPO immediately. The held-back ten percent is then released, after adjusting any dues found later. But if the servant was an allottee of government housing, it is released only on the No Demand Certificate. And sub-rule ten makes it the Head of Office's duty to see that provisional sanction is issued whenever the PPO is late."),
            ("EXAMPLE AND TRAP",
             "Example: Esha retires 31 Jan 2027, files Form 6-A on 15 Feb 2027. Her 6 months run from 15 Feb.",
             "Example (invented): Esha retires on 31 January 2027 but her Form 6-A is submitted on 15 February 2027. The six-month limit runs from 15 February 2027, the later date. Question: does an excess provisional gratuity have to be refunded? No, under Rule 62(6)(c); only the excess provisional pension is recovered. Trap: saying both excesses are recovered. This is the finest asymmetry in the Rules.",
             YELLOW,
             "Here is a real example. Esha retires on thirty-first January two thousand twenty-seven, but Form 6-A comes in on fifteenth February. The six months run from fifteenth February, the later date. And the trap: do not say both excesses are recovered. Only the excess pension is recovered. The excess gratuity is not."),
        ],
        "hook": "REMEMBER: provisional pension max 6 months (from the LATER date); excess pension recovered, excess gratuity NOT!",
        "hook_say": "Remember: provisional pension lasts at most six months from the later date. Excess pension is recovered, but excess gratuity is not refunded.",
        "covers": ["R62(5)", "R62(6)(a)", "R62(6)(b)", "R62(6)(c)", "R62(7)", "R62(8)", "R62(9)", "R62(10)", "QA-R62", "TL-PROV-MAX-6M", "LIMIT-GRATUITY-WITHHELD-10PCT"],
    },
    {
        "id": "c5_16_rule63a",
        "chapter": "CHAPTER 16 • RULE 63(1): THE ACCOUNTS OFFICER AND THE PPO",
        "title": "RULE 63(1) — THE ACCOUNTS OFFICER ISSUES THE PPO: TWO MONTHS OR 45 DAYS",
        "accent": BLUE, "badge": "RULE 63(1)",
        "q": "What does the Accounts Officer do with the case, and by when must the PPO be issued?",
        "q_say": "Sir, what does the Accounts Officer do with the case, and by when must the pension payment order be issued?",
        "boxes": [
            ("SUPERANNUATION • 63(1)(a)",
             "AO checks, fills Part II of Form 7, assesses pension, family pension AND gratuity, and issues the PPO 2 months BEFORE retirement.",
             "Rule 63(1)(a): in a superannuation case the Accounts Officer applies the requisite checks, records the account enfacement in Part II of Form 7, assesses the pension, family pension and gratuity, and issues the Pension Payment Order (PPO) two months before the date of superannuation. The PPO is one package of three assessments. Part I of Form 7 was filled by the Head of Office under Rule 59. Ledger: R63(1)(a), TL-PPO-SUPER-2M. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "Let us take the rule first. The PPO, the Pension Payment Order, is the order that authorises the pension. In a superannuation case, the Accounts Officer checks the case, fills Part two of Form 7, and assesses three things together: the pension, the family pension and the gratuity. The PPO is issued two months before the date of superannuation."),
            ("OTHER CASES • 63(1)(b)",
             "Other retirements: PPO within 45 days of receiving the papers. This clock runs FORWARD from receipt.",
             "Rule 63(1)(b): in other cases, the PPO is issued within forty-five days of receiving the papers. Superannuation counts backward from a known date; this counts forward from the date of receipt. Ledger: R63(1)(b), TL-PPO-OTHER-45D, QA-R63. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "For all other cases, the PPO must be issued within forty-five days of receiving the papers. See the contrast: for superannuation the clock counts back from the retirement date, and for other cases it counts forward from the day the papers arrive."),
            ("24 MONTHS • 63(1)(c)",
             "The AO also verifies emoluments only for the last 24 months, the same limit as the HoO in Rule 57(1)(b).",
             "Rule 63(1)(c): the Accounts Officer verifies the emoluments only for the last twenty-four months, the same limit that applies to the Head of Office under Rule 57(1)(b), so the two verifications match. Ledger: R63(1)(c), TL-EMOL-24M. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Clause c gives the Accounts Officer the same limit as the Head of Office: only the last twenty-four months of emoluments are verified. The same limit on both sides keeps the two checks consistent."),
            ("THE FAMILY PENSIONER • 63(1)(d)",
             "The living spouse is named as family pensioner in the PPO. More than one wife? All named, with shares.",
             "Rule 63(1)(d): the PPO names the spouse, if alive, as the family pensioner. First proviso: if more than one wife is alive, all are named with their shares. Second proviso (resolved): where a living wife exists along with children of a deceased wife, a divorced wife, or a void or voidable marriage, only the living wife is named at first; after the Head of Office's communication, the Accounts Officer issues a revised order (the summary reads 'PPA') naming all eligible members under Rule 50. Family pension is the pension paid to the family after the pensioner dies. Ledger: R63(1)(d), R63(1)(d)-PROV1, R63(1)(d)-PROV2 (changed: resolved). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "Clause d says the PPO names the spouse, if alive, as the family pensioner. Family pension is the pension paid to the family after the pensioner's death. If more than one wife is alive, all are named, with their shares. The second proviso, which the source guide left truncated, says that if a living wife exists along with other claimants, such as children of a deceased wife, only the living wife is named first, and later a revised order names all the eligible members under Rule fifty."),
            ("CLAUSES (e) TO (h)",
             "Disabled children, parents, siblings only when no one ahead of them. Also Form 8 requests, remarriage reports, payment under Rule 79.",
             "Rule 63(1)(e)-(h) (omitted by the source script): (e) permanently disabled children, dependent parents and disabled siblings are named only where no other eligible member comes before them; (f) the same, on a Form 8 request by an existing pensioner; (g) marriage or remarriage is reported under Rule 50(15)(f); (h) the Pension Disbursing Authority pays the family pension under Rule 79 in the Rule 50 order. Example (invented): Dev's PPO names his wife Charu as family pensioner. Ledger: R63(1)(e)-(h) (changed: added), R63-EX (invented). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "The source guide left out clauses e to h. Disabled children, dependent parents and disabled siblings are named only where nobody ranked ahead of them is eligible. The same applies on a Form eight request by an existing pensioner. Marriage or remarriage is reported under Rule fifty, and the Pension Disbursing Authority pays the family pension under Rule seventy-nine in the order of Rule fifty."),
        ],
        "hook": "REMEMBER: PPO 2 months BEFORE (retirement age) or 45 days AFTER receipt (others); AO checks only 24 months!",
        "hook_say": "Remember: the PPO is due two months before retirement at retirement age, or forty-five days after the papers arrive in other cases, and the Accounts Officer checks only twenty-four months.",
        "covers": ["R63(1)(a)", "R63(1)(b)", "R63(1)(c)", "R63(1)(d)", "R63(1)(d)-PROV1", "R63(1)(d)-PROV2", "R63(1)(e)-(h)", "TL-PPO-SUPER-2M", "TL-PPO-OTHER-45D", "R63-EX", "QA-R63"],
    },
    {
        "id": "c5_17_rule63b",
        "chapter": "CHAPTER 17 • RULE 63(2)-(5): GRATUITY, CPAO SEAL, PENDING PROCEEDINGS",
        "title": "RULE 63(2)-(5) — PAYING THE GRATUITY, THE CPAO SEAL AND PENDING PROCEEDINGS",
        "accent": ORANGE, "badge": "RULE 63(2)-(5)",
        "q": "After the PPO, how is the gratuity paid, who seals the PPO, and what if proceedings are pending?",
        "q_say": "Sir, after the PPO, how is the gratuity paid, who seals the PPO, and what if disciplinary proceedings are pending?",
        "boxes": [
            ("PAYING THE GRATUITY • 63(2)-(3)",
             "AO tells the HoO the gratuity. HoO pays after Rule 67 dues and any 68(5) hold.",
             "Rule 63(2) (omitted by the source script): the Accounts Officer tells the Head of Office the gratuity; the Head of Office pays after deducting Rule 67 dues and any amount withheld on the Directorate of Estates intimation under Rule 68(5). Rule 63(3): gratuity withheld under Rule 68(5) is adjusted against outstanding licence fee and the balance is refunded. Ledger: R63(2), R63(3) (changed: added). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "The source guide left out sub-rules two and three. The Accounts Officer tells the Head of Office the gratuity amount. The Head of Office pays it after deducting Government dues under Rule sixty-seven and any amount withheld on the housing intimation under Rule sixty-eight, sub-rule five. If gratuity was withheld, it is first set against the outstanding licence fee, and the balance is refunded."),
            ("CPAO COPY • 63(4)(a)",
             "PPO copy to the CPAO within 2 months, with the bank undertaking (now in Form 6-A).",
             "Rule 63(4)(a): the Accounts Officer sends a copy of the PPO to the Central Pension Accounting Office (CPAO) within two months of receiving the papers, with the undertaking to the bank. After G.S.R. 410(E) the words 'Format 9' became 'Form 6-A'. OBSOLETE / HISTORY ONLY: the Format 9 undertaking, replaced by Form 6-A. Ledger: R63(4)(a) (changed). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Sub-rule four, clause a: the Accounts Officer sends a copy of the PPO to the Central Pension Accounting Office, the CPAO, within two months of receiving the papers, with the bank undertaking. After 2024 that undertaking is part of Form 6-A, instead of the old Format nine."),
            ("THE CPAO SEAL: THREE LAYERS",
             "Rule text: seal within 21 days of receiving the PPO. Sept 2025 calendar: by the 20th of the retirement month.",
             "Rule 63(4)(b) (omitted by the source script): the CPAO issues the Special Seal of Authority and sends it to the Pension Disbursing Authority within 21 days of receiving the PPO (rule text, layer 1). The O.M. No. 11(15)/2022-P&PW(H)-8363(1) dated 28.10.2022 carried an earlier timeline table with the same 21 days; whether the Sept 2025 O.M. withdrew it was not stated in the pages read. The Sept 2025 calendar (O.M. No. 4/35/2024-P&PW(D)/10377 dated 29.09.2025, annexure step 10) says the CPAO sends it by the 20th of the retirement month (layer 3). Quote each with its own layer. Rule 63(4)(c): the Pension Disbursing Authority pays the pension on the due date as per CGA and CPAO orders. Ledger: R63(4)(b), R63(4)(c), OM-28.10.2022-TIMELINES, OM-SEP2025-STAGE10. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "Clause b says the CPAO issues the Special Seal of Authority and sends it to the Pension Disbursing Authority within twenty-one days of receiving the PPO. An older memorandum of twenty-eighth October two thousand twenty-two used the same twenty-one days. The September two thousand twenty-five calendar says by the twentieth of the retirement month. These are different layers, so quote each with its own source. Clause c: the paying authority, usually a bank, pays on the due date."),
            ("PENDING PROCEEDINGS • 63(5)",
             "Proceedings pending: provisional pension (Rule 8(5)); gratuity waits. Final orders with Form 7-A in 30 days.",
             "Rule 63(5)(a): where departmental or judicial proceedings are pending, provisional pension is authorised under Rule 8(5) and gratuity is withheld; the Head of Office sends the final orders with Form 7-A within thirty days of their issue. Rule 63(5)(b) (omitted by the source script): the Accounts Officer authorises the final pension within thirty days of receiving Form 7-A. Ledger: R63(5)(a), R63(5)(b) (changed: added). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "Sub-rule five covers pending proceedings. If departmental or court proceedings are pending, a provisional pension is authorised under Rule eight, sub-rule five, and the gratuity is held back. When the final orders come, the Head of Office sends them with Form 7-A within thirty days, and the Accounts Officer authorises the final pension within thirty days of receiving it."),
            ("THE TRAP: 'ONLY CLAUSE REPLACED'",
             "WRONG claim: 63(4) is not the only clause replaced in 2024. Many Rules were amended.",
             "The source script says Rule 63(4) is the only clause 'replaced' in the 2024 amendment. This is wrong. G.S.R. 410(E) amended Rules 50(15)(e), 53, 57, 58, 59, 60, 62(6)(a), 63(4)(a) and (b), 80(5), Form 4, the Form 7 check list and Format 10. In Rule 63(4) the words 'Format 9' became 'Form 6-A'. Ledger: R63(4)-ONLY-REPLACED (changed). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "Be careful, this is the trap. The source guide says Rule sixty-three, sub-rule four, is the only clause replaced in 2024. That is wrong. The amendment touched many rules, including fifty-three, fifty-seven to sixty, sixty-two and eighty. In Rule sixty-three, sub-rule four, the words Format nine simply became Form 6-A."),
        ],
        "hook": "REMEMBER: gratuity paid after dues; CPAO seal 21 days (rule) vs 20th (2025 calendar); 63(4) is NOT the only change!",
        "hook_say": "Remember: the gratuity is paid after dues; the CPAO seal is twenty-one days under the rule but the twentieth under the 2025 calendar; and Rule sixty-three, sub-rule four, was not the only change.",
        "covers": ["R63(2)", "R63(3)", "R63(4)(a)", "R63(4)(b)", "R63(4)(c)", "R63(4)-ONLY-REPLACED", "R63(5)(a)", "R63(5)(b)", "OM-28.10.2022-TIMELINES", "OM-SEP2025-STAGE10"],
    },
    {
        "id": "c5_18_sep2025_calendar",
        "chapter": "CHAPTER 18 • THE SEPTEMBER 2025 CALENDAR: STEP BY STEP",
        "title": "THE 29.09.2025 GUIDELINES — THE TWELVE-STEP RETIREMENT CALENDAR",
        "accent": GREEN, "badge": "O.M. 29.09.2025",
        "q": "What does the September 2025 calendar of DoPPW say, step by step?",
        "q_say": "Sir, what does the September two thousand twenty-five calendar from the pension department say, step by step?",
        "boxes": [
            ("THE ORDER ITSELF",
             "O.M. No. 4/35/2024-P&PW(D)/10377 dated 29.09.2025: Comprehensive Guidelines for timely retirement dues and PPOs.",
             "DoPPW O.M. No. 4/35/2024-P&PW(D)/10377 dated 29.09.2025 (date confirmed in this check), titled 'Comprehensive Guidelines for timely payment of retirement dues (pension and pensionary dues) and issue of Pension Payment Orders (PPOs) at the time of retirement of Central Civil Services Employees'. It is an administrative calendar (layer 3) that sits beside the Rules. Ledger: OM-SEP2025-ID. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Here is the calendar. It comes from an office memorandum of the Department of Pension and Pensioners' Welfare, number four slash thirty-five slash two thousand twenty-four, dated twenty-ninth September two thousand twenty-five. It is called Comprehensive Guidelines for timely payment of retirement dues. It is an administrative calendar sitting beside the Rules, not a change to them."),
            ("STEPS 1 TO 7: BEFORE RETIREMENT",
             "Lists (1 Jan, 1 Apr, 1 Jul, 1 Oct). DoE 12 months; verify from 12, done by 8; certificate at 8; Form 6A at 6; case to PAO at 4.",
             "Annexure stages: (1) Head of Department lists those retiring in the next 12 to 15 months on 1 Jan, 1 Apr, 1 Jul, 1 Oct. (2) Head of Office sends the list to the PAO by 31 Jan, 30 Apr, 31 Jul, 31 Oct; for non-superannuation, immediately. (3) General Pool accommodation: intimation to the Directorate of Estates 12 months before retirement. (4) Qualifying service verification and average emoluments determination start 12 months before and are complete by 8 months before. (5) Head of Office gives the qualifying service and emoluments certificate 8 months before, and advises Form 6A. (6) Employee submits Form 6A and documents 6 months before. (7) Head of Office sends the case to the PAO 4 months before; non-superannuation, within 2 months of Form 6A. Ledger: OM-SEP2025-STAGE1-2, OM-SEP2025-STAGE3-7. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Steps one and two are the lists we met in Rule fifty-four. Step three: for staff in General Pool housing, the Directorate of Estates is informed twelve months before. Step four: service verification starts twelve months before and is done by eight months before. Step five: the certificate at eight months. Step six: Form 6A at six months. Step seven: the case goes to the pay and accounts office, the PAO, four months before, or within two months of Form 6A in other cases."),
            ("STEPS 8 TO 12: THE PPO TRAVELS",
             "PAO forwards PPO 2 months before (45 days others); to CPAO last working day of prior month; seal by the 20th; pension by month-end.",
             "Stage (8): the PAO checks and forwards the PPO/e-PPO to the paying authority 2 months before retirement; in non-superannuation cases the PPO is issued within 45 days of receiving papers. (9) PAO sends the PPO/e-PPO to the CPAO on the last working day of the month before the retirement month. (10) CPAO issues the Special Seal of Authority and sends it to the PDA with the PPO half copy by the 20th of the retirement month. (11) Head of Office hands the pensioner's half copy on the day of retirement. (12) The paying branch credits the pension by the last day of the month. Ledger: OM-SEP2025-STAGE8-12, OM-SEP2025-STAGE10. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "Step eight: the PAO checks and forwards the PPO two months before retirement, or within forty-five days of receipt in other cases. Step nine: the PAO sends it to the CPAO on the last working day of the month before the retirement month. Step ten: the CPAO sends the Special Seal and the PPO half copy to the paying authority by the twentieth of the retirement month. Step eleven: the pensioner gets his half copy on the retirement day. Step twelve: the bank credits the pension by the last day of the month."),
            ("THE TRAP: TWO CLOCKS",
             "Rule 63's clock is the legal one. The calendar is the working timetable that keeps the legal clock from being missed.",
             "Rule 63 has its own clock (layer 1): PPO two months before retirement for superannuation, and within 45 days of receipt of papers in other cases. The guidelines calendar (layer 3) is the administrative timeline to be met at each stage so the statutory clock is not missed. In practice the 45-day clock starts where the PAO receives the papers; in superannuation it runs backward from the retirement date. Treating the two as one is the biggest mistake. Ledger: OM-SEP2025-TRAP. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "Be careful, this is the trap. Rule sixty-three has its own legal clock. The calendar is the working timetable, with a date for every stage, designed so that the legal clock is not missed. Do not treat them as one. And remember, the forty-five days start from receipt of papers, but in superannuation cases the clock counts back from the retirement date."),
        ],
        "hook": "REMEMBER: 12, 8, 6, 4, 2 months before retirement, then the PPO travels PAO, CPAO, bank!",
        "hook_say": "Remember: twelve, eight, six, four and two months before retirement, and then the PPO travels from the pay office to the CPAO to the bank.",
        "covers": ["OM-SEP2025-ID", "OM-SEP2025-STAGE3-7", "OM-SEP2025-STAGE8-12", "OM-SEP2025-TRAP", "OM-SEP2025-STAGE1-2", "OM-SEP2025-STAGE10"],
    },
    {
        "id": "c5_19_sep2025_support",
        "chapter": "CHAPTER 19 • THE SEPTEMBER 2025 O.M.: VIGILANCE CLEARANCE AND NEW STRUCTURES",
        "title": "VIGILANCE CLEARANCE, PENSION MITRAS, THE HLOC AND NODAL OFFICERS",
        "accent": PINK, "badge": "O.M. 29.09.2025",
        "q": "Can pension be held back waiting for vigilance clearance, and who monitors the process?",
        "q_say": "Sir, can pension be held back while waiting for vigilance clearance, and who monitors the whole process?",
        "boxes": [
            ("VIGILANCE CLEARANCE",
             "Issue VC 3 months before retirement; valid 3 months. Pension must NOT be held back waiting for it.",
             "O.M. of 29.09.2025: vigilance clearance (VC) should be issued three months before retirement; its validity is three months; pension is not to be held back waiting for VC. Where proceedings are pending, Rule 63(5)(a) applies: provisional pension is authorised under Rule 8(5) and gratuity is not paid until the final orders. Vigilance clearance is a certificate from the vigilance wing that no inquiry is pending. Ledger: OM-SEP2025-VC. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "Vigilance clearance is a certificate from the vigilance wing that no inquiry is pending against the retiring person. The memorandum says it should be issued three months before retirement, and it is valid for three months. But pension must not be held back waiting for it. If proceedings are pending, Rule sixty-three, sub-rule five, a, applies, and a provisional pension is paid."),
            ("PENSION MITRAS",
             "Every retiring employee gets a Welfare Officer who helps with the forms and later with family pension papers.",
             "The Head of Office deputes a Welfare Officer (Pension Mitra) for each retiring employee to help with filling forms and, on the pensioner's death, to hand-hold the family through documentation and verification for family pension. A separate circular on their roles was to follow (not found). Ledger: OM-SEP2025-MITRA. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Each retiring employee gets a Welfare Officer, called a Pension Mitra, appointed by the Head of Office. The Mitra helps fill the forms, and after the pensioner's death helps the family with the family pension documents."),
            ("HLOC AND NODAL OFFICERS",
             "HLOC: Secretary (Pension) chairs; reviews every 2 months. Each Ministry has a Nodal Officer, JS or Director level.",
             "High Level Oversight Committee (HLOC) in DoPPW: Secretary (Pension) is chairperson; members CGA, DG CGHS, DG NIC, Pr CCA/CCA (MHA), Pr CCA/CCA (MoF) and CPAO; Joint Secretary (Pension) is convenor. It reviews pendency every two months and issues a monthly performance report of Ministries. Each Ministry has a Nodal Officer of Joint Secretary/Director level. The rank and role are confirmed generally, but the details (employee-wise mapping on Bhavishya, monthly meetings with PAOs, escalation of files returned more than twice) were not seen in the page read: not confirmed. Ledger: OM-SEP2025-HLOC, OM-SEP2025-NODAL (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "At the top is a High Level Oversight Committee in the pension department. The Secretary for Pension chairs it, and it reviews pending cases every two months. Each Ministry also has a Nodal Officer at Joint Secretary or Director level. The detailed duties of the Nodal Officer, such as monthly meetings and escalation, were not confirmed in what we read."),
            ("BHAVISHYA NUMBERS, TWO UNCONFIRMED LINES",
             "O.M. figures: 99 Ministries, 1036 offices, 9536 DDOs, 2,93,644 PPOs. 'PPO includes e-PPO' is not confirmed.",
             "Bhavishya figures stated in the O.M.: 99 Ministries/Departments, 1036 offices, 9536 DDOs and 2,93,644 PPOs issued. Two further lines in the source were not seen in the page read, so they are UNVERIFIED: that 'PPO' in the O.M. includes e-PPO, and that manual processing is allowed only as per Rule 53 with the same timelines. These are the O.M.'s own figures for its date and will have moved on. Ledger: OM-SEP2025-BHAV-STATS, OM-SEP2025-EPPO (unverified), OM-SEP2025-MANUAL (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "The memorandum quotes figures for Bhavishya: ninety-nine Ministries, one thousand thirty-six offices, nine thousand five hundred thirty-six drawing officers and two lakh ninety-three thousand six hundred forty-four PPOs issued. These were true on that date and will have grown. Two other lines, that a PPO includes an e-PPO and that manual processing follows Rule fifty-three, were not confirmed."),
        ],
        "hook": "REMEMBER: VC 3 months before, valid 3 months, and NEVER hold the pension for VC!",
        "hook_say": "Remember: vigilance clearance is issued three months before, is valid three months, and pension is never held back waiting for it.",
        "covers": ["OM-SEP2025-VC", "OM-SEP2025-MITRA", "OM-SEP2025-HLOC", "OM-SEP2025-NODAL", "OM-SEP2025-BHAV-STATS", "OM-SEP2025-EPPO", "OM-SEP2025-MANUAL"],
    },
    {
        "id": "c5_20_rule64",
        "chapter": "CHAPTER 20 • RULE 64: THE SERVANT WHO WAS ON DEPUTATION",
        "title": "RULE 64 — WHO PROCESSES THE CASE OF A SERVANT ON DEPUTATION",
        "accent": SKY, "badge": "RULE 64",
        "q": "If the retiring servant is on deputation, which office prepares the pension case?",
        "q_say": "Sir, if the retiring servant is on deputation, which office prepares the pension case?",
        "boxes": [
            ("CENTRAL DEPUTATION • 64(1)",
             "On deputation to another CENTRAL department and retires there? The BORROWING department's HoO does the work.",
             "Rule 64(1): where a Government servant on deputation to another Central Department retires from there, the pension case work is done by the Head of Office of the borrowing Department, that is, the department he was deputed to. Deputation means working for a time in another department. Ledger: R64(1). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "Let us take the rule first. Deputation means working for some time in another department. Under sub-rule one, if the servant is on deputation to another Central department and retires from there, the Head of Office of the borrowing department does the pension case work."),
            ("STATE OR FOREIGN • 64(2)",
             "On deputation to a State Government or foreign service? The HoO or cadre authority that SANCTIONED it, the lending side.",
             "Rule 64(2): where the servant is on deputation to a State Government or in foreign service, the work is done by the Head of Office or the cadre authority that sanctioned the deputation, that is, the lending side. Cadre authority is the authority that controls the service he belongs to. Ledger: R64(2), QA-R64. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Sub-rule two is the other way around. If the servant is with a State Government or in foreign service, the work is done by the Head of Office or the cadre authority that sanctioned the deputation. That is the lending side. A memory aid, which is a teaching device and not a rule: Central deputation goes to the borrowing side, while State or foreign deputation stays with the lending side."),
            ("WHO, NOT WHAT",
             "Rule 64 says who does the work. It does not change qualifying service, emoluments or the pension.",
             "The source script says Rule 64 only decides who acts and changes nobody's entitlement. This is the script author's interpretation; the rule text only says who processes the case. Present it as a reading, not as a rule line. The source also calls Rule 78 the death-case mirror of Rule 64; Rule 78 belongs to Batch 6 and was not read here: unverified. Ledger: R64-WHO-NOT-WHAT (unverified), R64-R78-MIRROR (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "The source guide adds that Rule sixty-four only says who does the work, not what the servant gets. That is a fair reading of the rule text, but it is the author's interpretation, so present it as a reading. The source guide also says Rule seventy-eight is the same idea for death cases; we will check that in batch six."),
            ("EXAMPLE AND TRAP",
             "Example: Dev, on deputation to a State Government, retires. His own cadre authority prepares the case.",
             "Example (invented): Charu is deputed to another Central ministry and superannuates there; that ministry's Head of Office prepares her case. Dev is on deputation to a State Government and superannuates; the cadre authority that sent him prepares his case. Trap: the sides are opposite; mixing them up is the usual error. Ledger: R64(1), R64(2), QA-R64.",
             RED,
             "Here is a real example. Charu is deputed to another Central ministry and retires there, so that ministry prepares her case. Dev is on deputation to a State Government, so the cadre authority that sent him prepares his case. The trap is mixing up the two directions."),
        ],
        "hook": "REMEMBER: Central deputation = borrowing side; State or foreign = lending side!",
        "hook_say": "Remember: for Central deputation the borrowing side works the case; for State or foreign deputation the lending side does.",
        "covers": ["R64(1)", "R64(2)", "R64-WHO-NOT-WHAT", "R64-R78-MIRROR", "QA-R64"],
    },
    {
        "id": "c5_21_rule65a",
        "chapter": "CHAPTER 21 • RULE 65(1)-(4): INTEREST FOR ADMINISTRATIVE DELAY",
        "title": "RULE 65(1)-(4) — WHEN INTEREST IS PAYABLE AND WHO SANCTIONS IT",
        "accent": RED, "badge": "RULE 65(1)-(4)",
        "q": "If the pension or gratuity is paid late, when does the retiree get interest, and who approves it?",
        "q_say": "Sir, if the pension or gratuity is paid late, when does the retiree get interest, and who approves it?",
        "boxes": [
            ("WHEN INTEREST IS DUE • 65(1)",
             "Provisional or final pension, family pension or gratuity not sanctioned, or paid late, for ADMINISTRATIVE reasons: interest at the GPF rate.",
             "Rule 65(1): where the provisional or final pension, family pension or gratuity is not sanctioned, or is authorised after the due date, interest is payable, but only if it is clearly established that the delay was for administrative reasons or lapses. The rate and method are those of the General Provident Fund; the rule itself gives no percentage. The rule also reaches retirements other than superannuation. Ledger: R65(1). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "Let us take the rule first. Interest is payable if the provisional or final pension, family pension or gratuity is not sanctioned, or is authorised after the due date. But only if it is clearly shown that the delay was caused by administrative reasons or lapses. The rate is the General Provident Fund rate. The rule gives no percentage of its own."),
            ("THE PROVISO",
             "No interest if the delay was the claimant's own fault, such as not completing the required formalities.",
             "Proviso to Rule 65(1): no interest where the delay is due to the default of the Government servant, the pensioner or the family member, that is, where the prescribed procedure was not followed by the claimant. Ledger: R65(1)-PROV. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Now the proviso. If the delay was the claimant's own fault, for example the formalities were not completed, there is no interest. This applies whether the claimant is the servant, the pensioner or the family member."),
            ("WHO SANCTIONS • 65(2)",
             "The Secretary, or an officer authorised by the Secretary and not below Joint Secretary, examines the case and sanctions.",
             "Rule 65(2): the case is examined by the Secretary of the Ministry or Department, or an officer authorised by him who is not below the rank of Joint Secretary, who sanctions the interest if satisfied that the delay was administrative; Ministry's attached and subordinate offices are included. The source script says he 'shall' sanction (not 'may'); the word 'shall' is NOT confirmed. The summary read says he sanctions interest if the delay is administrative. Ledger: R65(2). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Sub-rule two says who decides. It is the Secretary, or an officer authorised by the Secretary who is not below the rank of Joint Secretary. If the delay was administrative, interest is sanctioned. The source guide says the word is shall rather than may; we could not confirm that exact word."),
            ("PAY IN 2 MONTHS • 65(3)-(4)",
             "Formal sanction by the Ministry; payment within 2 months. Fix responsibility, but do NOT wait for the disciplinary result.",
             "Rule 65(3): formal sanction is then issued by the Ministry or Department, and payment is made within two months. Rule 65(4): the Ministry fixes responsibility and takes disciplinary action; the proviso says the payment of interest is not to wait for the outcome of disciplinary proceedings. Ledger: R65(3), R65(4), TL-INTEREST-PAY-2M, QA-R66-WAIVER. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "Sub-rule three: the Ministry issues the formal sanction, and the payment is made within two months. Sub-rule four: the Ministry fixes responsibility and takes disciplinary action, but the proviso says the interest is paid without waiting for the outcome of the disciplinary proceedings. The pensioner is not made to wait for an inquiry."),
            ("THREE TESTS, ONE LINK",
             "Test: administrative lapse. Level: Secretary or not below JS. Time: 2 months. Link to Rule 51 not re-checked.",
             "Memory chain: (1) trigger: not sanctioned, or authorised after the due date; (2) test: delay was administrative, and not the claimant's fault; (3) rate: GPF rate; (4) authority: Secretary, or an officer not below Joint Secretary; (5) formal sanction by the Ministry; payment in two months; (6) accountability, without delaying the payment. The source also says gratuity delay for a missing person under Rule 51 attracts interest under Rule 65; Rule 51 is a Batch 4 rule and was not re-read here: unverified. Ledger: R65-LINK-R51 (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             YELLOW,
             "To remember the chain: the trigger is a missing or late sanction; the test is an administrative lapse, not the claimant's fault; the rate is the General Provident Fund rate; the authority is the Secretary or an officer not below Joint Secretary; and payment is within two months. The source guide also links this to missing-person gratuity under Rule fifty-one; that link was not re-checked here."),
        ],
        "hook": "REMEMBER: administrative delay = interest at GPF rate; Secretary or JS sanctions; pay in 2 months!",
        "hook_say": "Remember: an administrative delay earns interest at the provident fund rate; the Secretary or a Joint Secretary sanctions it; and it is paid in two months.",
        "covers": ["R65(1)", "R65(1)-PROV", "R65(2)", "R65(3)", "R65(4)", "TL-INTEREST-PAY-2M", "QA-R66-WAIVER", "R65-LINK-R51"],
    },
    {
        "id": "c5_22_rule65b",
        "chapter": "CHAPTER 22 • RULE 65(5): WHEN INTEREST STARTS, AND A CORRECTED EXAMPLE",
        "title": "RULE 65(5) AND THE WORKED EXAMPLE — INTEREST STARTS AFTER THREE MONTHS",
        "accent": ORANGE, "badge": "RULE 65(5)",
        "q": "From which day is interest counted, what is the rate now, and how do we compute it?",
        "q_say": "Sir, from which day is interest counted, what is the rate now, and how do we compute it?",
        "boxes": [
            ("START DATES • RULE 65(5)",
             "Interest starts the day after THREE months from retirement (or the other triggering date).",
             "Rule 65(5) (omitted by the source script): interest starts on (a) superannuation: the day after three months from retirement; (b) other retirement, absorption in a PSU or death: the day after three months from that date; (c) exonerated after Rule 8(4)(c) withholding: the day after three months from retirement; (d) not fully exonerated, Rule 8(5)(c): the day after three months from the final order; (e) proceedings dropped on death: the day after three months from death; (f) retrospective revision: the day after three months from the revising order. Ledger: R65(5) (changed: added). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "The source guide missed sub-rule five, which says when interest starts. For superannuation, it is the day after three months from retirement. For other retirement, absorption in a public sector undertaking or death, it is the day after three months from that date. After proceedings, it is three months from the final order, or from death if the proceedings were dropped on death, and for a retrospective revision it is three months from the revising order."),
            ("THE RATE: GPF, NOW 7.1%",
             "GPF rate for Oct-Dec 2026 is 7.1% a year (Finance Ministry, 05.10.2026). It changes every quarter.",
             "Rule: the General Provident Fund rate. Current rate: 7.1% per year for Q3 of 2026-27 (01.10.2026 to 31.12.2026), per Finance Ministry resolution of 05.10.2026, F.No. 5(3)-B(PD)/2023. The same 7.1% applied to Q2 of 2026-27 (01.07.2026 to 30.09.2026, resolution of 03.07.2026). The rate is dynamic: always take the figure from the current quarter's notification. Ledger: R65-RATE-GPF, QA-R65. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "The rate is the General Provident Fund rate. For October to December two thousand twenty-six it is seven point one percent a year, under a Finance Ministry resolution of fifth October two thousand twenty-six. It was also seven point one percent in the previous quarter. But it changes every quarter, so always check the current notification."),
            ("THE SOURCE'S EXAMPLE",
             "Source: Rs 15,00,000 gratuity x 7.1% x 9/12 = Rs 79,875. The sum is right, but its starting date is wrong.",
             "Source's Worked Example 18 (retirement 31.03.2025, gratuity admissible Rs 15,00,000, paid 31.12.2025, delay nine months, rate 7.1%): 15,00,000 x 0.071 = 1,06,500; x 9/12 = Rs 79,875; total Rs 15,79,875. The arithmetic is correct, but the premise that interest runs from the due date (the retirement date) is NOT supported by Rule 65(5). Ledger: R65-EX18-ARITHMETIC (confirmed), R65-EX18-START (changed). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "The source guide gives a worked example. Ramesh retires on thirty-first March two thousand twenty-five, with gratuity of fifteen lakh rupees, paid on thirty-first December. It counts nine months at seven point one percent and gets seventy-nine thousand eight hundred seventy-five rupees. The arithmetic is correct. But the starting point, the retirement date, is not supported by Rule sixty-five, sub-rule five."),
            ("THE CORRECTED EXAMPLE",
             "Interest runs from 01.07.2025 to 31.12.2025 = 6 months. Rs 15,00,000 x 7.1% x 6/12 = Rs 53,250. Total Rs 15,53,250.",
             "Corrected computation under Rule 65(5)(a): retirement 31.03.2025; interest starts the day after three months, i.e. 01.07.2025; paid 31.12.2025; six months. 15,00,000 x 0.071 = 1,06,500; x 6/12 = Rs 53,250. Total paid = 15,00,000 + 53,250 = Rs 15,53,250. Assumes a 7.1% rate throughout and simple monthly counting; in practice use the rate in force for each quarter. Ledger: R65-EX18-START. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Here is the corrected version. Interest starts the day after three months, which is the first of July two thousand twenty-five, and runs to thirty-first December. That is six months. Fifteen lakh times seven point one percent is one lakh six thousand five hundred a year, and half of that is fifty-three thousand two hundred fifty rupees. The total paid is fifteen lakh fifty-three thousand two hundred fifty rupees, assuming a seven point one percent rate throughout."),
            ("THE O.M. OF 25.10.2024",
             "O.M. of 25.10.2024: release all dues early; delay attracts interest under Rule 65.",
             "DoPPW O.M. No. 1/15/2024-P&PW(F)/9809 dated 25.10.2024 on implementation of pension rules and timely release of retirement benefits: administrative Ministries are to release all retirement benefits (including extraordinary pension) early; delay attracts interest under Rule 65. It does not mention Bhavishya or timelines. Ledger: OM-25.10.2024. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "An office memorandum of twenty-fifth October two thousand twenty-four tells Ministries to release all retirement benefits, including extraordinary pension, early. It says delay attracts interest under Rule sixty-five. It does not mention Bhavishya or any timeline."),
        ],
        "hook": "REMEMBER: interest starts after 3 months; GPF rate (7.1% now, check quarterly); corrected example Rs 53,250!",
        "hook_say": "Remember: interest starts after three months, at the provident fund rate, which is seven point one percent now but changes quarterly. The corrected example gives fifty-three thousand two hundred fifty rupees.",
        "covers": ["R65(5)", "R65-RATE-GPF", "R65-EX18-ARITHMETIC", "R65-EX18-START", "OM-25.10.2024", "QA-R65"],
    },
    {
        "id": "c5_23_rule66",
        "chapter": "CHAPTER 23 • RULE 66: REVISING A PENSION AFTER IT HAS BEEN AUTHORISED",
        "title": "RULE 66 — REVISION OF PENSION, CLERICAL ERRORS, WAIVER AND REFUND",
        "accent": GREEN, "badge": "RULE 66",
        "q": "Can a pension be changed after it is authorised, and what if too much was paid?",
        "q_say": "Sir, can a pension be changed after it is authorised, and what happens if too much was paid?",
        "boxes": [
            ("GENERAL REVISION • 66(1)",
             "Pension and family pension can be revised by general order. The REVISED figure becomes the basic pension.",
             "Rule 66(1): the pension under Rule 44 and the family pension under Rule 50 may be revised by a general order, on the recommendation of the Central Pay Commission (the words 'or otherwise' in the source guide were not confirmed from the rule summary read: UNVERIFIED); the revised figure becomes the basic pension on which additional pension (Rule 44(5)), additional family pension (Rule 50(3)) and dearness relief (Rule 52) are calculated. Ledger: R66(1). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Let us take the rule first. Pension and family pension can be revised by a general order, for example on the Pay Commission's recommendation. The source guide adds the words or otherwise, which we could not confirm. The revised figure becomes the basic pension. Additional pension, additional family pension and dearness relief are then worked out on that revised figure, not added on top."),
            ("NO CUT BACK • 66(2)",
             "No revision against the pensioner after final assessment, except a CLERICAL error. After 2 years: DoPPW.",
             "Rule 66(2): a pension authorised after final assessment is not revised to the disadvantage of the pensioner, the only exception being a clerical error, and this is subject to Rules 7 and 8. Proviso: if the clerical error is detected after two years, no revision to the disadvantage is made without the concurrence of the Department of Pension and Pensioners' Welfare (DoPPW). Ledger: R66(2). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Sub-rule two protects the pensioner. After final assessment, the pension is not reduced, except to correct a clerical error. And if the clerical error is found after two years, even that needs the concurrence of the pension department. All of this is subject to Rules seven and eight."),
            ("WHO DECIDES, WAIVER • 66(3)-(4)",
             "The Administrative Ministry decides what is a clerical error. Waiver after consulting Expenditure.",
             "Rule 66(3): whether an error is a clerical error is decided by the Administrative Ministry or Department, not the Accounts Officer. Rule 66(4): the question of waiving recovery of an excess payment is considered after consulting the Department of Expenditure, Ministry of Finance, and only if the excess was not caused by misrepresentation of facts by the pensioner. Ledger: R66(3), R66(4). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "Sub-rule three says the Administrative Ministry decides whether an error is clerical, not the Accounts Officer. Sub-rule four allows recovery to be waived, after consulting the Department of Expenditure, but only if the excess payment was not caused by the pensioner's misrepresentation."),
            ("REFUND • 66(5)-(6)",
             "No waiver? Notice; refund in 2 months; else deduct from future pension.",
             "Rule 66(5): if waiver is refused, the Head of Office issues a notice, and the refund is due within two months of the notice. Rule 66(6): failing refund, the Head of Office adjusts it from future pension in instalments by a written order. Example (invented): Dev was overpaid Rs 24,000 by a clerical error found in year one; waiver is refused; notice is issued; if he does not refund within two months, the Head of Office deducts it in instalments from later pension by a written order. Ledger: R66(5), R66(6), TL-REFUND-2M. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "If waiver is refused, the Head of Office gives a notice, and the pensioner must refund within two months. If he does not, the Head of Office adjusts the amount from future pension in instalments, by a written order. For example, Dev was overpaid twenty-four thousand rupees by a clerical error and waiver is refused. He gets a notice and has two months to refund."),
            ("TWO O.M.s ON RULE 66",
             "O.M.s of 18.10.2024 and 30.10.2025 repeat the same chain. No new rule.",
             "DoPPW O.M. No. 38/10(04)/2024-P&PW(A) dated 18.10.2024 (number taken from the 30.10.2025 O.M.) and F.No. 38/10(03)/2025-P&PW(A) dated 30.10.2025, titled 'Revision of pension after authorisation under CCS (Pension) Rules 2021': both restate Rule 66(2) to (6); no new rule. The source says the 30.10.2025 O.M. went to 'all Ministries and PDAs/banks'; the pages read say only that Ministries/Departments should bring it to notice, so the PDA/bank circulation is UNVERIFIED. Ledger: OM-18.10.2024, OM-30.10.2025-R66, OM-30.10.2025-PDA-BANKS (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             YELLOW,
             "Two office memoranda, dated eighteenth October two thousand twenty-four and thirtieth October two thousand twenty-five, restate the same chain under the title Revision of pension after authorisation. They add no new rule. The source guide says the second went to banks and pension disbursing authorities as well; we saw only that Ministries were to bring it to notice."),
        ],
        "hook": "REMEMBER: revised pension = new basic; only clerical errors; after 2 years need DoPPW; refund in 2 months!",
        "hook_say": "Remember: a revised pension becomes the new basic pension; only clerical errors can be corrected against the pensioner; after two years the pension department must agree; and a refund is due within two months of the notice.",
        "covers": ["R66(1)", "R66(2)", "R66(3)", "R66(4)", "R66(5)", "R66(6)", "TL-REFUND-2M", "OM-18.10.2024", "OM-30.10.2025-R66", "OM-30.10.2025-PDA-BANKS"],
    },
    {
        "id": "c5_24_rule67",
        "chapter": "CHAPTER 24 • RULE 67: GOVERNMENT DUES",
        "title": "RULE 67 — WHICH GOVERNMENT DUES ARE RECOVERED FROM THE GRATUITY",
        "accent": BLUE, "badge": "RULE 67",
        "q": "What are Government dues, who works them out, and from what are they recovered?",
        "q_say": "Sir, what are Government dues, who works them out, and from what are they recovered?",
        "boxes": [
            ("THE RULE • RULE 67(1)-(3)",
             "The HoO ascertains and assesses dues for every retirement. Dues left on the retirement date are taken from the gratuity.",
             "Rule 67(1): the Head of Office ascertains and assesses the Government dues, for superannuation and for other retirements. Rule 67(2): dues outstanding on the date of retirement are adjusted from the retirement gratuity. Rule 67(3) (omitted by the source script): only these Government dues may be recovered from gratuity. Ledger: R67(1), R67(2), R67(3) (changed: added). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "Let us take the rule first. Government dues are amounts the retiring servant owes the Government. Under sub-rule one, the Head of Office ascertains and assesses them, for every kind of retirement. Under sub-rule two, dues outstanding on the retirement date are adjusted from the retirement gratuity. Sub-rule three, which the source guide missed, says only these Government dues may be recovered from gratuity."),
            ("EXPLANATION (a): ACCOMMODATION",
             "Housing dues: licence fee arrears, damages, and electricity, water and PNG charges.",
             "Explanation (a): accommodation dues are arrears of licence fee; damages; and charges for electricity, water and PNG (piped natural gas). The source script says damages are charged for overstay beyond the permissible period, subletting, unauthorised occupation and transfer to an ineligible person; those four grounds are not shown in the summary read and are UNVERIFIED: read the Gazette text. Licence fee is the rent-like charge for government housing. Ledger: R67-EXPL-A, R67-EXPL-A-DAMAGES-GROUNDS (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Explanation clause a covers housing dues: licence fee arrears, which is the rent-like charge for government housing, damages, and the electricity, water and piped gas charges. The source guide lists four grounds for damages: overstay, subletting, unauthorised occupation and transfer to an ineligible person. We could not see those grounds in what we read, so they are not confirmed."),
            ("EXPLANATION (b): ALL OTHER DUES",
             "House building and conveyance advances; overpaid pay, allowances or leave salary; income tax arrears.",
             "Explanation (b): all other dues, namely advances such as house building advance and conveyance advance; overpayments of pay, allowances or leave salary; and arrears of income tax. Ledger: R67-EXPL-B. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Clause b covers everything else: advances, such as house building and conveyance advances; overpayments of pay, allowances or leave salary; and income tax arrears."),
            ("EXAMPLE AND TRAP",
             "Example: Bilal owes Rs 40,000 house building advance and Rs 18,000 licence fee. Rs 58,000 comes off his gratuity.",
             "Example (invented): Bilal's assessed dues on the retirement date are a house building advance balance of Rs 40,000 and licence fee arrears of Rs 18,000; total Rs 58,000, adjusted from his retirement gratuity. Trap: Rule 67 lists WHAT dues count (the heads); Rule 68 gives the Directorate of Estates procedure for housing dues. Do not treat them as the same rule.",
             RED,
             "Here is a real example. Bilal owes a house building advance balance of forty thousand rupees and licence fee arrears of eighteen thousand. That is fifty-eight thousand rupees, taken from his retirement gratuity. The trap: Rule sixty-seven lists what counts as a due, while Rule sixty-eight gives the procedure for housing dues."),
        ],
        "hook": "REMEMBER: HoO assesses dues; (a) housing dues, (b) everything else; recovered from the gratuity!",
        "hook_say": "Remember: the Head of Office assesses the dues; clause a is housing dues and clause b is everything else; and they are recovered from the gratuity.",
        "covers": ["R67(1)", "R67(2)", "R67(3)", "R67-EXPL-A", "R67-EXPL-A-DAMAGES-GROUNDS", "R67-EXPL-B"],
    },
    {
        "id": "c5_25_rule68a",
        "chapter": "CHAPTER 25 • RULE 68(1)-(5): GOVERNMENT HOUSING DUES, PART ONE",
        "title": "RULE 68(1)-(5) — THE DIRECTORATE OF ESTATES' CLOCK AND HOW THE FEE IS RECOVERED",
        "accent": ORANGE, "badge": "RULE 68(1)-(5)",
        "q": "How does the Directorate of Estates report the licence fee, and how is it recovered?",
        "q_say": "Sir, how does the Directorate of Estates report the licence fee, and how is it recovered from the retiring servant?",
        "boxes": [
            ("THE DoE'S CLOCK • 68(1)(a)-(b)",
             "At retirement age: DoE replies in 2 months, fee up to 8 months before retirement. Other cases: 1 month, fee up to retirement.",
             "Rule 68(1)(a): on the Rule 55(1) intimation, the Directorate of Estates informs the Head of Office within two months of the licence fee for the period up to eight months before retirement. Rule 68(1)(b): in non-superannuation cases, within one month, and the report runs up to the date of retirement; the eight-month cut does not apply. Ledger: R68(1)(a), R68(1)(b), TL-DOE-2M-1M. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Let us take the rule first. When the housing details reach the Directorate of Estates under Rule fifty-five, the Directorate tells the Head of Office the licence fee within two months, for the period up to eight months before retirement. In cases other than superannuation, it must reply in one month, and the report runs up to the retirement date, with no eight month cut."),
            ("SILENCE HELPS THE RETIREE • 68(1)(c)",
             "No reply in time? It is presumed that NO licence fee is recoverable.",
             "Rule 68(1)(c): if the Directorate of Estates does not reply in time, it is presumed that no licence fee is recoverable. The source script's Q&A says that if dues come out later they are withheld under Rule 68(5); that link is wrong: Rule 68(5) is for the case where the Directorate cannot determine the fee; it is not a cure after the silence presumption in 68(1)(c). Re-word. Ledger: R68(1)(c), R68-QA-SILENCE (changed). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "Clause c is a benefit of silence. If the Directorate does not reply in time, it is presumed that no licence fee is recoverable. The source guide says that if dues appear later, ten percent of the gratuity is withheld under sub-rule five. That is not right, because sub-rule five is for the case where the Directorate cannot work out the fee, not a cure after the silence presumption."),
            ("RECOVERY FROM PAY • 68(2)-(3)",
             "HoO recovers the last 8 months' fee monthly from pay. Intimated fee: instalments from pay, rest from gratuity before payment.",
             "Rule 68(2): in a superannuation case the Head of Office recovers the licence fee of the last eight months, up to the date of retirement, month by month from pay and allowances. Rule 68(3): the licence fee intimated by the Directorate is recovered in instalments from current pay and allowances, and any balance is recovered from the gratuity before the gratuity payment is authorised. Ledger: R68(2), R68(3). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Sub-rule two: in a superannuation case, the Head of Office himself recovers the licence fee of the last eight months, month by month, from pay and allowances. Sub-rule three: the fee the Directorate reported is recovered in instalments from current pay, and whatever cannot be recovered that way is taken from the gratuity before it is authorised."),
            ("AFTER RETIREMENT, AND 10% • 68(4)-(5)",
             "Fee for allowed stay after retirement: from the gratuity. DoE cannot fix the fee? It asks to withhold 10% of the gratuity.",
             "Rule 68(4): the Directorate of Estates also informs the fee for permissible retention after retirement, and the Head of Office adjusts it from the gratuity. Rule 68(5): if the Directorate cannot determine the outstanding fee, it asks that ten per cent of the gratuity be withheld. Ledger: R68(4), R68(5), LIMIT-GRATUITY-WITHHELD-10PCT. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "Sub-rule four: the Directorate also tells the fee for any permitted stay after retirement, and the Head of Office adjusts it from the gratuity. Sub-rule five: if the Directorate cannot work out the outstanding fee, it asks the office to withhold ten percent of the gratuity."),
            ("EXAMPLE",
             "Example: Asha retires 31 Dec 2027. Fee to 30 Apr 2027 comes from the DoE. May to Dec is cut from her pay.",
             "Example (invented): Asha, a superannuating allottee, retires on 31 December 2027. The Directorate's report covers licence fee up to 30 April 2027 (eight months before) and must come within two months of the Rule 55(1) intimation. The fee for May to December 2027, eight months, is recovered by her Head of Office from her pay each month. If the Directorate does not reply in time, it is presumed that no fee is due for the reported period. Ledger: R68(1)-(5).",
             RED,
             "Here is a real example. Asha retires on thirty-first December two thousand twenty-seven. The Directorate reports the fee up to thirtieth April, within two months of the intimation. Her Head of Office recovers the fee for May to December from her pay, month by month. If the Directorate stays silent, no fee is presumed due for the reported period."),
        ],
        "hook": "REMEMBER: DoE replies in 2 months (1 month for others); silence = no fee; last 8 months from pay!",
        "hook_say": "Remember: the Directorate replies in two months, or one month in other cases; silence means no fee is due; and the last eight months are recovered from pay.",
        "covers": ["R68(1)(a)", "R68(1)(b)", "R68(1)(c)", "R68(2)", "R68(3)", "R68(4)", "R68(5)", "R68-QA-SILENCE", "TL-DOE-2M-1M", "LIMIT-GRATUITY-WITHHELD-10PCT"],
    },
    {
        "id": "c5_26_rule68b",
        "chapter": "CHAPTER 26 • RULE 68(6)-(8): THE NDC, INTEREST AND DEARNESS RELIEF",
        "title": "RULE 68(6)-(8) — RELEASING THE WITHHELD GRATUITY AND THE LAST RESORT",
        "accent": GREEN, "badge": "RULE 68(6)-(8)",
        "q": "When is the withheld gratuity released, and what if dues remain even after that?",
        "q_say": "Sir, when is the withheld gratuity released, and what happens if dues still remain after the gratuity is adjusted?",
        "boxes": [
            ("WHO RECOVERS • 68(6)",
             "DoE recovers the fee and damages, not the HoO. Withheld gratuity is released at once on the NDC, issued after ACTUAL vacation.",
             "Rule 68(6): recovery of the licence fee and damages is the responsibility of the Directorate of Estates, not of the Head of Office; the withheld gratuity is released immediately on receipt of the No Demand Certificate, and the NDC is issued on actual vacation of the accommodation, not merely on application. Ledger: R68(6). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Let us take sub-rule six. Recovering the licence fee and damages is the Directorate's responsibility, not the Head of Office's. The withheld gratuity is released at once when the No Demand Certificate arrives. And the certificate comes after the house is actually vacated, not just after an application is made."),
            ("THE 14 DAYS • 68(7)(a)",
             "The DoE issues the NDC within 14 days of the application, made after the house is vacated.",
             "Rule 68(7)(a): the Directorate of Estates issues the NDC within fourteen days of the application made after actual vacation. Ledger: R68(7)(a), TL-NDC-14D. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "Sub-rule seven, clause a, sets the time: the Directorate issues the certificate within fourteen days of the application, made after actual vacation."),
            ("INTEREST FOR ITS DELAY • 68(7)(b)-(c)",
             "DoE misses the 14 days? The retiree gets interest at the GPF rate on the gratuity held back.",
             "Rule 68(7)(b) and (c) (omitted by the source script): if the Directorate misses the fourteen days, the allottee is entitled to interest at the GPF rate on the excess gratuity withheld, and the Directorate pays it through the Account Officer. Ledger: R68(7)(b)(c) (changed: added). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "The source guide missed clauses b and c. If the Directorate misses the fourteen days, the allottee gets interest at the General Provident Fund rate on the gratuity that stayed withheld, and the Directorate pays it through the Account Officer."),
            ("LAST RESORT • 68(8)",
             "Dues still left? DoE may recover from dearness relief WITHOUT consent. No DR is paid until it is fully recovered.",
             "Rule 68(8): if anything remains after adjustment, the Directorate of Estates may order recovery from the dearness relief without the pensioner's consent, and no dearness relief is paid until the amount is fully recovered. The Explanation adds that licence fee includes charges for damage or loss to the accommodation. Dearness relief (DR) is the cost-of-living addition to pension. Ledger: R68(8) (changed: Explanation added). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "Be careful with sub-rule eight. If dues still remain, the Directorate may order recovery from the dearness relief, which is the cost-of-living addition to pension, without the pensioner's consent. No dearness relief is paid until the full amount is recovered. The Explanation adds that licence fee includes charges for damage or loss to the accommodation."),
        ],
        "hook": "REMEMBER: NDC only after ACTUAL vacation, in 14 days; DoE late = GPF interest; last resort = DR recovery!",
        "hook_say": "Remember: the certificate comes only after actual vacation, within fourteen days; if the Directorate is late the retiree gets interest; and the last resort is recovery from dearness relief.",
        "covers": ["R68(6)", "R68(7)(a)", "R68(7)(b)(c)", "R68(8)", "TL-NDC-14D"],
    },
    {
        "id": "c5_27_rule69",
        "chapter": "CHAPTER 27 • RULE 69: ASSESSING THE OTHER DUES",
        "title": "RULE 69 — STARTING ONE YEAR BEFORE AND FINISHING EIGHT MONTHS BEFORE",
        "accent": SKY, "badge": "RULE 69",
        "q": "When must the other Government dues, apart from housing, be assessed?",
        "q_say": "Sir, when must the other Government dues, apart from housing, be assessed?",
        "boxes": [
            ("WHEN TO START • 69(1)",
             "At retirement age: start 1 year before, or at LPR, whichever is EARLIER. Others: at retirement or when the HoO learns of it.",
             "Rule 69(1): in a superannuation case the Head of Office starts assessing dues from one year before retirement or from the date the servant goes on leave preparatory to retirement, whichever is earlier; in other retirements, immediately on retirement or when the Head of Office learns of the retirement, whichever is earlier. Ledger: R69(1). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             SKY,
             "Rule sixty-nine is about dues other than housing. In a superannuation case, the Head of Office starts assessing them one year before retirement, or from the date of leave preparatory to retirement, whichever is earlier. In other retirements, the work starts at retirement, or when the Head of Office learns of it, whichever is earlier."),
            ("WHEN TO FINISH • 69(2)",
             "Superannuation: finished 8 months before. Other retirements: within 30 days of retirement.",
             "Rule 69(2): the assessment is completed eight months before superannuation, or within thirty days after other retirements. Ledger: R69(2), TL-DUES-ASSESS. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Sub-rule two sets the finish line. Eight months before superannuation, or within thirty days after other kinds of retirement."),
            ("LATER FINDS • 69(3)",
             "Dues found later are also adjusted, if they were outstanding on the retirement date, from the gratuity.",
             "Rule 69(3): dues found later are also adjusted if they were outstanding on the date of retirement; the adjustment is from the retirement gratuity. Ledger: R69(3). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "Sub-rule three covers late discoveries. Dues found later are also adjusted from the gratuity, but only if they were outstanding on the retirement date."),
            ("EXAMPLE AND TRAP",
             "Example: Charu retires 31 Dec 2027. Work starts 31 Dec 2026 and must end by 30 Apr 2027.",
             "Example (invented): Charu superannuates on 31 December 2027 and takes no early leave. Her Head of Office starts assessing her non-housing dues on 31 December 2026 and completes it by 30 April 2027 (eight months before). Trap: the pattern, one year to start and eight months to finish, is the same shape as Rules 55 and 56; do not mix Rule 69 (other dues) with Rule 68 (housing dues).",
             RED,
             "Here is a real example. Charu retires on thirty-first December two thousand twenty-seven. Her Head of Office starts assessing her other dues on thirty-first December two thousand twenty-six and must finish by thirtieth April two thousand twenty-seven. The trap is mixing Rule sixty-nine, which covers other dues, with Rule sixty-eight, which covers housing dues."),
        ],
        "hook": "REMEMBER: dues assessment starts 1 year before (earlier of LPR) and ends 8 months before!",
        "hook_say": "Remember: the assessment of other dues starts one year before, or at leave if earlier, and ends eight months before retirement.",
        "covers": ["R69(1)", "R69(2)", "R69(3)", "TL-DUES-ASSESS"],
    },
    {
        "id": "c5_28_rule70",
        "chapter": "CHAPTER 28 • RULE 70: NOTIFYING THE DATE OF RETIREMENT",
        "title": "RULE 70 — THE RETIREMENT NOTIFICATION, AND WHAT IF NONE IS ISSUED",
        "accent": PINK, "badge": "RULE 70",
        "q": "Must the retirement date be notified, and what if no notification is issued?",
        "q_say": "Sir, must the retirement date be notified, and what happens if no notification is issued?",
        "boxes": [
            ("THE NOTIFICATION • 70(1)",
             "Gazetted: Gazette notification. Non-gazetted: office order. It states the date, within one week, copy to the AO.",
             "Rule 70(1): the retirement is notified, for a gazetted Government servant in the Official Gazette and for a non-gazetted servant by an office order; the notification states the date of retirement, is issued within a week, and a copy goes to the Accounts Officer promptly. The starting point of the week was not stated in the ledger summary; check the text. A gazetted officer is one whose appointment is notified in the Gazette. Ledger: R70(1), TL-RULE70-WEEK. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             PINK,
             "Let us take the rule first. A gazetted servant is one whose appointment is published in the Official Gazette. For such a servant, the retirement is notified in the Gazette. For a non-gazetted servant, an office order is issued. It states the retirement date, is issued within a week, and a copy goes to the Accounts Officer promptly. Please check the exact starting point of that week in the text."),
            ("THE PROVISO • 70(1)",
             "A leave notification already issued? No second notice, unless the leave is cut short and retirement moves.",
             "Proviso to Rule 70(1): if a notification or order was already issued for leave preparatory to retirement, a second notification is not needed. The ledger adds the exception: a further notice is needed if the leave is curtailed and the retirement is advanced or postponed. Ledger: R70(1)-PROV (changed: exception added). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             ORANGE,
             "The proviso says that if the notification for leave preparatory to retirement is already out, no second one is needed. But the exception, which the source guide missed, is that a further notice is needed if the leave is cut short and the retirement is advanced or postponed."),
            ("DEEMED RETIREMENT • 70(2)",
             "No extension order? He retires on reaching the age. No notification gives him no right to stay.",
             "Rule 70(2): unless there are specific orders of extension of service, the servant is deemed to have retired on reaching the age of superannuation; the office's failure to issue a notification gives him no right to continue in service. Ledger: R70(2). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "Sub-rule two says that unless there is a specific order extending his service, the servant is deemed to have retired on reaching the age. If the office forgets to issue the notification, that gives him no right to stay."),
            ("A TEACHING LABEL",
             "'Declaratory, not constitutive' is the author's label: the notice records the date; it does not create retirement.",
             "The source script says Rule 70 is 'declaratory, not constitutive': the notification records a retirement that happens by age or by order; it does not create it. This is the script author's teaching label; the rule only says the date must be notified. Use it as a plain reading, not as a rule line. Example (invented): Bilal reaches the age of superannuation and no office order is issued; he is still deemed retired on reaching the age. Ledger: R70-DECLARATORY (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "The source guide calls Rule seventy declaratory, not constitutive. In plain words, the notification records the retirement; it does not create it. That is a teaching label, not rule wording. For example, if Bilal reaches the retirement age and no order is issued, he is still deemed retired on reaching it."),
        ],
        "hook": "REMEMBER: notify the date (Gazette or office order); no extension order = deemed retired on reaching the age!",
        "hook_say": "Remember: the retirement date is notified in the Gazette or by office order, and without an extension order the servant is deemed retired on reaching the age.",
        "covers": ["R70(1)", "R70(1)-PROV", "R70(2)", "R70-DECLARATORY", "TL-RULE70-WEEK"],
    },
    {
        "id": "c5_29_amendments",
        "chapter": "CHAPTER 29 • WHAT CHANGED IN CHAPTER X: THE 2024 AMENDMENT AND AFTER",
        "title": "WHAT G.S.R. 410(E) CHANGED, THE NOMINATION O.M., AND WHAT IS STILL OPEN",
        "accent": YELLOW, "badge": "AMENDMENTS",
        "q": "Which amendments touch Rules 53 to 70, and what is still not confirmed?",
        "q_say": "Sir, which amendments touch Rules fifty-three to seventy, and what is still not confirmed?",
        "boxes": [
            ("WHAT G.S.R. 410(E) TOUCHED",
             "Rules 53, 57, 58, 59, 60, 62(6)(a) and 63(4) now say Form 6-A or online mode. Rule 80(5) is for batch six.",
             "G.S.R. 410(E) of 16.07.2024 (effective 16.11.2024 per DoPPW O.M.s; see the date flag in Chapter 2): Rule 53 substituted and 53(2)(a),(b) reworded; Rule 57: (1)(c)(iii), (2)(a), (3)(a),(b) and proviso; Rule 58: (1), (2)(a),(b) and proviso; Rule 59(1),(2); Rule 60(1)(i),(3),(4); Rule 62(6)(a); Rule 63(4)(a),(b); and Rule 80(5) (Form 6-A in place of Form 10 for the gratuity nominee; list in 80(5)(c)), which belongs to Batch 6. Rule 12 of the amendment: 'Form 6' is read as 'Form 6-A'. Rule 13: items 9 and 10 of the Form 7 check list omitted. Ledger: R2024-R57, R2024-R58, R2024-R59, R2024-R60, R2024-R62, R2024-R63, R2024-R80-5 (changed). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             YELLOW,
             "The 2024 amendment, notification four hundred ten E, touched Rules fifty-three, fifty-seven, fifty-eight, fifty-nine, sixty, sixty-two, sixty-three and eighty. Mostly, it replaced old forms with Form 6-A or the word Bhavishya with online mode. The change in Rule eighty, sub-rule five, belongs to batch six."),
            ("NOTHING NEWER FOUND",
             "G.S.R. 770(E) of 2022 and 340(E) of 2025 do not touch Rules 53-70. No newer amendment found up to 21.10.2026.",
             "G.S.R. 770(E) of 07.10.2022 (Rules 8, 20, 46, 50, 76) and G.S.R. 340(E) of 22.05.2025 (Rule 37(29)(c)) do not touch Rules 53-70; G.S.R. 410(E) is the only amendment found that touches Chapter X. No amendment of Rules 53-70 was found after G.S.R. 410(E) up to 21.10.2026, on a limited web search; the official Gazette was not searched directly. G.S.R. 775(E) of September 2026 (see Batch 3) concerns Rule 37(7). The O.M. dated 22.06.2026 cited by the source script was not found or read. The source's own claim of verification on 12 September 2026 was not assumed. Ledger: GSR-868E-770E-340E-CURRENCY, NEWER-NONE-CH10. Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             BLUE,
             "The other amendments, notification seven seventy E of two thousand twenty-two and three forty E of two thousand twenty-five, do not touch these rules. We found no amendment of Rules fifty-three to seventy after the 2024 one, up to twenty-first October two thousand twenty-six. But that search was limited and did not cover the official Gazette directly, so please check before relying on it."),
            ("THE NOMINATION O.M. OF 11.09.2024",
             "Retirees give the arrears and commutation nomination in Form 6-A. Form A is not needed with it.",
             "DoPPW O.M. F.No. 55/13/2023-P&PW(C)(Part1) dated 11.09.2024 ('Submission of nomination for Arrears of Pension and Commutation of Pension after introduction of Single Pension Application Form Form 6-A'): retiring employees give the nomination details for arrears of pension and for commutation in Form 6-A; the Common Nomination Form 'Form A' need not be submitted with it; pensioners still use Form A for later nominations or changes. Formal amendments of the 1981 and 1983 Rules were to follow. The source links this to Rule 84; Rule 84 was not read here, so that link is unverified. Ledger: OM-11.09.2024-NOMINATION, FORM-A-RULE84 (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             GREEN,
             "An office memorandum of eleventh September two thousand twenty-four says retiring employees give their nomination for arrears of pension and for commutation inside Form 6-A. So the separate Form A is not needed with it. But pensioners still use Form A later to make or change a nomination. The source guide links this to Rule eighty-four; that link was not checked."),
            ("TWO LINES TO TREAT AS POINTERS",
             "A corrigendum of 25.07.2024 and an O.M. of 23.10.2024 could not be confirmed. Do not rely on them.",
             "The source cites a Corrigendum dated 25.07.2024 to G.S.R. 410(E): not found in the pages read (the gconnect page says nothing of it): UNVERIFIED. The source also cites an O.M. dated 23.10.2024 re-circulating the 31.10.2022 O.M.s on mandatory Bhavishya: a PDF named 'OMdated23102024' was read, but its text is the November 2016 Bhavishya O.M. (No. 55/14/2014/P&PW(C)Pali-1); a 23.10.2024 date and a 31.10.2022 reference were not seen: UNVERIFIED. Ledger: CORRIGENDUM-25.07.2024 (unverified), OM-23.10.2024 (unverified). Close restatement from a secondary source read through a page-summarising tool; Gazette or India Code text not read directly.",
             RED,
             "Two items from the source guide could not be confirmed. One is a corrigendum dated twenty-fifth July two thousand twenty-four to the 2024 amendment. The other is a memorandum dated twenty-third October two thousand twenty-four on Bhavishya. The document we found under that name was actually the November two thousand sixteen memorandum. Treat both as pointers, not as authority."),
        ],
        "hook": "REMEMBER: only G.S.R. 410(E) touches Chapter X; the corrigendum and the 23.10.2024 O.M. are unconfirmed!",
        "hook_say": "Remember: only the 2024 amendment touches Chapter ten, and the corrigendum and the twenty-third October two thousand twenty-four memorandum are not confirmed.",
        "covers": ["R2024-R57", "R2024-R58", "R2024-R59", "R2024-R60", "R2024-R62", "R2024-R63", "R2024-R80-5", "GSR-868E-770E-340E-CURRENCY", "NEWER-NONE-CH10", "OM-11.09.2024-NOMINATION", "FORM-A-RULE84", "CORRIGENDUM-25.07.2024", "OM-23.10.2024"],
    },
    {
        "id": "c5_30_timeline",
        "chapter": "CHAPTER 30 • THE MASTER TIMELINE OF CHAPTER X",
        "title": "THE COUNTDOWN — EVERY DEADLINE OF RULES 53 TO 70 IN ONE PLACE",
        "accent": SKY, "badge": "TIMELINE",
        "q": "Can we see all the deadlines of Chapter X in one countdown?",
        "q_say": "Sir, can we see all the deadlines of Chapter ten in one countdown?",
        "flow": "countdown",
        "boxes": [
            ("1 YEAR BEFORE",
             "Rules 55(1), 56, 69(1): housing details to DoE; preparation starts; dues assessment starts.",
             "One year before retirement (or LPR, if earlier for Rules 56 and 69): housing details to the Directorate of Estates, Rule 55(1); preparatory work starts, Rule 56; assessment of other dues starts, Rule 69(1). Rule 54 list: by the 15th each month for 15 months ahead. Ledger: TL-DOE-ONEYEAR, R56, R69(1).",
             SKY,
             "One year before: housing details go to the Directorate of Estates, the pension work starts under Rule fifty-six, and the assessment of other dues starts under Rule sixty-nine."),
            ("8 AND 6 MONTHS",
             "8 months: service checked, certificate, dues done, DoE cut. 6 months: Form 6-A.",
             "Eight months before: service verification complete, Rule 57(1)(a)(vii); certificate at least eight months before, Rule 57(1)(c)(i); dues assessment complete, Rule 69(2); the Directorate's licence fee report runs up to this point, Rule 68(1)(a). Six months before: Form 6-A due, Rule 57(2)(a). Emoluments verified for the last 24 months, Rules 57(1)(b) and 63(1)(c). Ledger: TL-SVC-VERIF-8M, TL-CERT-8M, TL-6A-SUPER, TL-EMOL-24M.",
             ORANGE,
             "Eight months before: service is verified, the certificate is given, other dues are assessed, and the housing fee report ends. Six months before: Form 6-A is due. Throughout, emoluments are verified only for the last twenty-four months."),
            ("4 MONTHS BEFORE",
             "Rules 59 and 60: Part I of Form 7 and the whole case go to the AO.",
             "Four months before: Head of Office completes Part I of Form 7, Rule 59(1); the case is sent to the Accounts Officer, Rule 60(4). For other retirements: two months after the forms are received, Rules 59 and 60. Ledger: TL-PARTI-FORM7, TL-CASE-AO.",
             GREEN,
             "Four months before: Part one of Form 7 is complete, and the whole case goes to the Accounts Officer. In other cases, both happen within two months after the forms are received."),
            ("2 MONTHS AND AFTER",
             "PPO 2 months before (45 days others). After: 10 days, 6 months, 14 days, 2 months, one week.",
             "Two months before: PPO for superannuation, Rule 63(1)(a); other cases within 45 days of papers, Rule 63(1)(b). After or around retirement: provisional sanction within 10 days or one month, Rule 62(4); provisional pension at most six months, Rule 62(6)(a); DoE reply two months or one month, Rule 68(1); NDC within 14 days, Rule 68(7); interest paid within two months of sanction, Rule 65(3); refund notice two months, Rule 66(5); retirement notification within a week, Rule 70(1). Ledger: TL-PPO-SUPER-2M, TL-PPO-OTHER-45D, TL-PROV-LETTER, TL-PROV-MAX-6M, TL-DOE-2M-1M, TL-NDC-14D, TL-INTEREST-PAY-2M, TL-REFUND-2M, TL-RULE70-WEEK.",
             RED,
             "Two months before: the PPO, or forty-five days from receipt in other cases. Around and after retirement: provisional sanction in ten days or a month, provisional pension for at most six months, the certificate in fourteen days, interest within two months, refund within two months, and the notification within a week."),
        ],
        "hook": "REMEMBER: 12, 8, 6, 4, 2 months — the five numbers of Chapter X!",
        "hook_say": "Remember the five numbers of Chapter ten: twelve, eight, six, four and two months before retirement.",
        "covers": ["TL-FIVE-NUMBERS", "TL-DOE-ONEYEAR", "TL-SVC-VERIF-8M", "TL-CERT-8M", "TL-6A-SUPER", "TL-PARTI-FORM7", "TL-CASE-AO", "TL-PPO-SUPER-2M", "TL-PPO-OTHER-45D", "TL-EMOL-24M"],
    },
    {
        "id": "c5_31_recap",
        "chapter": "CHAPTER 31 • RECAP OF BATCH FIVE",
        "title": "RECAP — KEY NUMBERS, TOP TRAPS AND WHAT COMES NEXT",
        "accent": GREEN, "badge": "RECAP • RULES 53-70",
        "q": "Can you recap Chapter X in a few lines, with the traps and the currency note?",
        "q_say": "Sir, can you recap Chapter ten in a few lines, with the traps and the currency note?",
        "boxes": [
            ("KEY NUMBERS",
             "1 year, 8, 6, 4, 2 months. PPO 45 days. Emoluments 24 months. Provisional: 100% pension, 10% gratuity held, 6 months.",
             "Key numbers: Rule 54 list by the 15th for 15 months; Rule 55/56/69 one year; Rule 57 service verification and certificate eight months, Form 6-A six months; Rules 59/60 four months; Rule 63 PPO two months before or 45 days after papers; emoluments last 24 months; Rule 62 provisional pension 100%, gratuity 10% withheld, up to six months; Rule 65 interest after three months at the GPF rate (7.1% for Oct-Dec 2026); Rule 66 refund two months, two-year DoPPW rule; Rule 68 DoE two months or one month, NDC 14 days; Rule 70 notification within a week. Ledger: TL-FIVE-NUMBERS.",
             GREEN,
             "Here are the key numbers. One year, eight months, six months, four months and two months before retirement. The pension payment order in forty-five days for other cases. Emoluments checked for twenty-four months. A provisional pension of one hundred percent, ten percent of gratuity held back, and six months at most."),
            ("TOP TRAPS",
             "Exemption (a) vs (b). Rule 56 is EARLIER. Silence helps. Excess gratuity not refunded. Interest from 3 months, not the due date.",
             "Top traps: (1) Rule 53(2)(a) whole case manual, (b) one step only; (2) Rule 56 'whichever is earlier'; (3) silence helps the servant: no reply in two months means the period qualifies (Rule 57), no DoE reply means no fee (Rule 68(1)(c)); (4) Rule 62(6): excess provisional pension is recovered, excess provisional gratuity is not; (5) Rule 65(5): interest starts after three months, not from the due date; (6) Rule 63(4) is not the only clause changed in 2024; (7) Rule 57 versus Rule 58: same form and tiers, different clock; (8) the Rules' legal clock is not the same as the 2025 administrative calendar.",
             RED,
             "The top traps. Exemption under clause a is the whole case; clause b is one step. Rule fifty-six uses whichever is earlier. Silence helps the servant. An excess provisional gratuity is not refunded, but excess pension is recovered. Interest starts after three months, not from the due date. And the legal clock of Rule sixty-three is not the same as the administrative calendar."),
            ("CURRENCY NOTE",
             "Current to G.S.R. 410(E) of 2024. No newer change found to 21.10.2026. Wording is a close restatement. Check dynamic figures.",
             "Currency: Chapter X is touched only by G.S.R. 410(E) of 16.07.2024 (effective 16.11.2024 per DoPPW O.M.s; Gazette publication date to be checked). No newer amendment found up to 21.10.2026 on a limited search. No Gazette, India Code or DoPPW page was read directly: rule wording is a close restatement from secondary reproductions read through a page-summarising tool. Dynamic items: the GPF rate (7.1% for 01.10.2026 to 31.12.2026) and the administrative calendar. Items marked unverified in the chapters: Rule 55(1) 'prescribed by DoE'; the 'last ten months' mention in Rule 57(1)(b); the grounds of damages in Rule 67; the Rule 65(2) word 'shall'; the corrigendum of 25.07.2024; the O.M. of 23.10.2024; the Nodal Officer duties; e-PPO and manual processing lines; the Rule 51 and Rule 78 links; and the PDA/bank circulation of the 30.10.2025 O.M. Principle from the Rule, figure from the O.M.",
             BLUE,
             "A currency note. This chapter is changed only by the 2024 amendment. We found nothing newer up to twenty-first October two thousand twenty-six, but the search was limited, and we read no official Gazette page directly, so the rule wording is a close restatement. The provident fund rate and the administrative calendar can change, so check the latest memorandum. Items marked not confirmed in the chapters are still open."),
            ("NEXT: BATCH SIX",
             "Next: Chapter XI death in service (Rules 71-78), then Rules 79-87.",
             "Next batch (Batch 6): Chapter XI, death in service (Rules 71 to 78); Chapter XII, deceased and missing pensioners (Rules 79 and 80); Chapter XIII, payment (Rules 81 to 84); Chapter XIV (Rules 85 to 87).",
             ORANGE,
             "In the next batch we move to Chapter eleven, death in service, Rules seventy-one to seventy-eight, and then Rules seventy-nine to eighty-seven. Until then, keep the five numbers in mind: twelve, eight, six, four and two."),
        ],
        "hook": "REMEMBER: 12, 8, 6, 4, 2 months; silence helps; check the latest O.M. for dynamic figures!",
        "hook_say": "Remember: twelve, eight, six, four and two months; silence helps the servant; and always check the latest memorandum for figures that change.",
        "covers": ["TL-FIVE-NUMBERS", "GSR-868E-770E-340E-CURRENCY", "NEWER-NONE-CH10"],
    },
    {
        "id": "c5_32_audit_ledger",
        "chapter": "CHAPTER 32 • SENIOR AUDIT — RULES 53 TO 70 COVERAGE CHECK",
        "title": "AUDIT VERDICT: EVERY RULE, CLAUSE AND PROVISO IS ON A CARD",
        "accent": YELLOW, "badge": "AUDIT • 53-70",
        "q": "Did the compiler cover every rule, sub-rule, clause, proviso and exception from Rule 53 to Rule 70?",
        "q_say": "Sir, did the compiler cover every rule, sub-rule, clause, proviso and exception from Rule fifty-three to Rule seventy?",
        "intro": ("Before we close batch five, here is the senior audit. I went through Rules fifty-three to seventy of the "
                  "Central Civil Services (Pension) Rules, 2021, clause by clause, and checked each one against the cards above. "
                  "Here is what the audit found."),
        "boxes": [
            ("COVERAGE • RULES 53-70",
             "Every rule, sub-rule, clause, proviso and exception from Rule 53 to Rule 70 is on a card — none skipped.",
             "Coverage check, rule by rule: Rule 53 (1, 2(a), 2(b)); Rule 54 (1, 2, 3); Rule 55 (1, 2, 3, 4, 5, 6 and its Explanation); Rule 56; Rule 57 (1(a)(i-x), (b), (c)(i-iii), 2(a), 2(b), 3); Rule 58 (1, 2 and proviso); Rule 59 (1, 2); Rule 60 (1(i-iii), 2, 3, 4); Rule 61 (1, 2); Rule 62 (1 to 10); Rule 63 (1(a-h), 2, 3, 4(a-c), 5(a-b)); Rule 64 (1, 2); Rule 65 (1 and proviso, 2, 3, 4, 5(a-f)); Rule 66 (1 to 6); Rule 67 (1-3 and Explanation (a)-(b)); Rule 68 (1(a-c), 2-8); Rule 69 (1-3); Rule 70 (1, proviso, 2). Nothing from Rule fifty-three to Rule seventy is left out. Ledger: AUDIT-COVERAGE-COMPLETE.",
             YELLOW,
             "The audit confirms: every rule, sub rule, clause, proviso and exception from Rule fifty-three to Rule seventy appears on at least one card. Nothing in that range was skipped."),
            ("GAPS AND FLAGS",
             "No rule gaps. Some wordings are flagged 'not confirmed' — cross-check them against the Gazette.",
             "There are no coverage gaps. The items marked NOT VERIFIED or UNVERIFIED on individual cards are wording-quality flags, not missing rules: Rule 55(1) details prescribed by the Directorate of Estates; the 'last ten months' mention in Rule 57(1)(b); the damage grounds in Rule 67; the word 'shall' in Rule 65(2); the start of the week in Rule 70(1); the corrigendum of 25.07.2024; the O.M. of 23.10.2024; the nodal officer duties and e-PPO lines of the September 2025 O.M.; and the PDA/bank circulation of the 30.10.2025 O.M. Quote the official text for these before an exam answer sheet. Ledger: AUDIT-FLAGS.",
             ORANGE,
             "No gaps were found in the rule range. But a few wordings could not be confirmed from the official text, so they stay flagged. Cross-check those flagged lines against the Gazette before you quote them."),
            ("MASTER TIMELINE TABLE",
             "Table: 1 yr → Rules 55, 56, 69 start | 8 mo → verify, certificate, dues done | 6 mo → Form 6-A | 4 mo → Form 7 Part I, case to AO | 2 mo → PPO",
             "Master table of Chapter X deadlines: One year before — Rule 55(1) housing details to the Directorate of Estates; Rule 56 preparation starts; Rule 69(1) other-dues assessment starts; Rule 54 list by the 15th for fifteen months ahead. Eight months before — Rule 57(1)(a)(vii) service verification done; Rule 57(1)(c)(i) certificate; Rule 69(2) dues assessment done; Rule 68(1)(a) licence-fee report cut-off. Six months before — Rule 57(2)(a) Form 6-A due. Four months before — Rule 59(1) Part I of Form 7; Rule 60(4) case to the Accounts Officer. Two months before — Rule 63(1)(a) PPO for superannuation; other cases forty-five days from receipt. After retirement — Rule 62(4) provisional sanction in ten days or one month; Rule 62(6)(a) provisional pension at most six months; Rule 68(7) No Demand Certificate in fourteen days; Rule 65(3) interest paid within two months; Rule 66(5) refund within two months; Rule 70(1) notification within a week. Ledger: AUDIT-TIMELINE.",
             SKY,
             "Here is the master timeline table in plain words: one year, eight months, six months, four months, two months — then the pension payment order travels from the pay office to the CPAO to the bank."),
            ("NON-OBSCURE CHECK",
             "Plain city English only. Short on-screen text; full wording in narration and reference sheet.",
             "Obscurity check: no legalese, no Devanagari script, no unexplained acronyms. Every card carries a short on-screen key point and a full simple-English narration. Acronyms are spelled out (Bhavishya, e-HRMS, PPO, NDC, HoO, HoD, AO, CPAO, PDA, DoE, DoPPW, GPF, DR, LPR, VC). The reference sheet, pension_b5_reference_sheet.md, gives the full wording of every card for quote-accurate answers. Ledger: AUDIT-PLAIN-ENGLISH.",
             GREEN,
             "The content is non-obscure. It is plain city English throughout. Short text on screen, full wording spoken, and every acronym is spelled out the first time."),
        ],
        "hook": "REMEMBER: audit says complete coverage of Rules 53-70; only a few wordings are flagged for Gazette cross-check!",
        "hook_say": "Remember: the audit finds complete coverage from Rule fifty-three to Rule seventy; only a few wordings need a Gazette cross-check.",
        "covers": ["AUDIT-COVERAGE-COMPLETE", "AUDIT-FLAGS", "AUDIT-TIMELINE", "AUDIT-PLAIN-ENGLISH"],
    },
]

FLOWS = {
    "countdown": {
        "nodes": [
            (80, 300, 420, 80, "1 YEAR BEFORE", "Rules 55, 56, 69", SKY, 1),
            (570, 300, 430, 80, "8 AND 6 MONTHS", "Rules 57, 68, 69", ORANGE, 2),
            (1070, 300, 360, 80, "4 MONTHS", "Rules 59, 60", GREEN, 3),
            (1500, 300, 340, 80, "2 MONTHS", "Rule 63 PPO", RED, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, ORANGE, 3), (2, 3, GREEN, 4)],
    },
}
PART_STARTS = ["c5_01_rule53", "c5_11_rule59", "c5_21_rule65a"]



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
    out = ["# CCS (Pension) Rules 2021 - Batch 5 - Rules 53-70: Determination of Pension on Retirement - full-wording reference sheet", "",
           "Every card on screen is a short key-point; the full wording / examinable facts of each card are listed here.", ""]
    for sc in SCENES:
        out += [f"## {sc['chapter']}", f"**{sc['title']}**  ({sc['badge']})", "", f"Q: {sc['q']}", ""]
        for (t, _b, _c, _n) in sc["boxes"]:
            out += [f"### {t}", FULL[(sc["id"], t)], ""]
        out += [f"> {sc['hook']}", ""]
    Path("pension_b5_reference_sheet.md").write_text("\n".join(out), encoding="utf-8")


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


def card_boxes(scene):
    n = len(scene["boxes"])
    top = 290
    if "flow" in scene:
        gap = 20
        bw_ = (W - 160 - gap * (n - 1)) // n
        return [(80 + i * (bw_ + gap), 490, bw_, 300) for i in range(n)]
    if n == 4:
        return [(80, top, 860, 245), (980, top, 860, 245), (80, top + 255, 860, 245), (980, top + 255, 860, 245)]
    gap = 20
    bw_ = (W - 160 - gap * (n - 1)) // n
    return [(80 + i * (bw_ + gap), top, bw_, 480) for i in range(n)]


def render_frame(scene, qno, total, reveal, kind, out_path: Path):
    img, d = background()
    acc = scene["accent"]
    n = len(scene["boxes"])

    d.rectangle([0, 0, W, 10], fill=acc)
    d.text((80, 34), scene["chapter"], font=font(22, True), fill=ORANGE)
    f_t, l_t, _, _ = fit_block(d, scene["title"], True, 1440, 50, 40, 26, 1.1)
    d.text((80, 76), l_t[0], font=f_t, fill=TEXT_WHITE)
    bd = scene["badge"]
    fb = font(20, True)
    bw = text_w(d, bd, fb) + 50
    d.rounded_rectangle([W - 80 - bw, 45, W - 80, 95], radius=10, fill=acc)
    d.text((W - 80 - bw + 25, 59), bd, font=fb, fill=(10, 16, 36) if acc in (ORANGE, SKY, GREEN) else TEXT_WHITE)
    d.line([(80, 150), (W - 80, 150)], fill=(51, 65, 85), width=2)

    asking = kind in ("question",)
    bt, bb = 162, 272
    d.rounded_rectangle([80, bt, W - 80, bb], radius=18, fill=lerp(CARD_BG, acc, 0.20 if asking else 0.10),
                        outline=YELLOW if asking else lerp(CARD_BG, acc, 0.5), width=5 if asking else 2)
    d.ellipse([100, bt + 20, 170, bt + 90], fill=acc)
    qs = f"Q{qno}"
    fq = font(30 if len(qs) < 3 else 24, True)
    d.text((135 - text_w(d, qs, fq) // 2, bt + 36), qs, font=fq, fill=(10, 16, 36) if acc in (ORANGE, SKY, GREEN) else TEXT_WHITE)
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

    d.rectangle([0, 855, W, 1070], fill=(7, 11, 24))
    d.line([(80, 855), (W - 80, 855)], fill=(30, 41, 59), width=2)
    d.rectangle([0, 1068, W, H], fill=(20, 28, 50))
    seg_w = W / total
    d.rectangle([0, 1068, int(seg_w * (qno - 1) + seg_w * min(1.0, (reveal + (1 if kind == "hook" else 0)) / (n + 1))), H], fill=ORANGE)
    for k in range(1, total):
        d.line([(int(seg_w * k), 1068), (int(seg_w * k), H)], fill=(7, 11, 24), width=2)
    img.save(out_path)


def audit_density():
    """Prints the font size every card ends up with. Returns the number of failing cards."""
    img, d = background()
    bad = 0
    print(f"{'scene':26s} {'card':36s} title body  chars")
    for sc in SCENES:
        for (t, body, _c, _n), (x, y, w, h) in zip(sc["boxes"], card_boxes(sc)):
            try:
                _, l_bt, lh_bt, ts = fit_block(d, t, True, w - 60, 62, TITLE_START, TITLE_MIN, 1.15)
                body_top = y + 16 + len(l_bt) * lh_bt + 10
                _, _, _, bs = fit_block(d, body, False, w - 60, y + h - body_top - 14, BODY_START, BODY_MIN, 1.25)
                flag = "" if bs >= 28 else "  (tight)"
                print(f"{sc['id'][:26]:26s} {t[:36]:36s} {ts:>4d} {bs:>4d}  {len(body):>4d}{flag}")
            except ValueError as e:
                bad += 1
                print(f"{sc['id'][:26]:26s} {t[:36]:36s}  FAIL  {e}")
        try:
            _, l_h, _, hs = fit_block(d, sc["hook"], True, W - 200, 36, 24, 20, 1.1)
            if len(l_h) > 1:
                raise ValueError("hook wraps")
        except ValueError:
            bad += 1
            print(f"{sc['id']}: HOOK does not fit on one line at >=20px ({len(sc['hook'])} chars)")
    print(f"\n{'ALL CARDS WITHIN BUDGET' if not bad else str(bad) + ' CARD(S) OVER BUDGET'}")
    return bad


# ============================================================================
# SEGMENTS / AUDIO / SUBTITLES
# ============================================================================
def build_segments(scene):
    n = len(scene["boxes"])
    segs = []
    if scene.get("intro"):
        segs.append(("teacher", scene["intro"], 0, "intro"))
    segs.append(("student", scene["q_say"], 0, "question"))
    if scene.get("lead"):
        segs.append(("teacher", scene["lead"], 0, "lead"))
    for i, b in enumerate(scene["boxes"]):
        segs.append(("teacher", b[3], i + 1, "answer"))
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
    ap.add_argument("--audit", action="store_true", help="print card-density table and exit (no ffmpeg needed)")
    ap.add_argument("--preview", action="store_true", help="render slides only")
    ap.add_argument("--no-tts", action="store_true", help="silent audio (offline layout/timing test)")
    ap.add_argument("--teacher", default=DEFAULT_TEACHER)
    ap.add_argument("--student", default=DEFAULT_STUDENT)
    ap.add_argument("--rate", default="-4%")
    ap.add_argument("--part", type=int, choices=[1, 2, 3], help="1..3 = first, middle, last third of the chapters")
    args = ap.parse_args()

    write_reference_sheet()
    if args.audit:
        sys.exit(1 if audit_density() else 0)
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

