#!/usr/bin/env python3
"""
CCS (Leave Travel Concession) Rules, 1988 - BATCH 2 - Rules 7 to 11 (admissibility, types of LTC, block years, counting, carry-over, places)
CITY HINGLISH Q&A EXPLANATION MASTERCLASS COMPILER. Narration: Roman-script Hinglish. Subtitles: Roman script (the script refuses to build if any Devanagari character appears).
SCOPE: strictly the CCS (LTC) Rules, 1988 and the DoPT orders issued under them. Other services' LTC rules are not covered; superseded provisions are left out.
Batch 2 covers Rule 7 (1)-(2) and its Notes 1 to 5, Rule 8 (a)-(c) with proviso, the FAQ block-year answers Q13 to Q20, Rule 9, Rule 10, Rule 11, the FAQ leave answers Q25 to Q27, scenarios, recap, MCQs and flashcards.
=====================================================================================================
SOURCES (28 Oct 2026):
  * DoPT consolidated Guidelines O.M. DOPT-1752820096240 dated 03.09.2025 (full text supplied by the user): Rule 7 and its Notes, Rules 8 to 11 as printed
  * DoPT FAQ O.M. F.No.31011/07/2025-PP.A-IV dated 01.07.2025 (full text supplied): Q13 to Q20 (block year), Q25 to Q27 (leave). This source has no Q28.
CHANGES / DECISIONS:
  * Block years: the FAQ (01.07.2025) shows 2022-25 as current and 2026-29 as next. On 28.10.2026 the block 2026-29 (sub-blocks 2026-27 and 2028-29) is running; this is read from the FAQ's own table and is flagged as a derivation, not a quoted order.
  * Dated illustrations in FAQ Q16/Q17 (2022, 2024) are taught only through their pattern; the 2026 case is shown.
  * Obsolete or purely historical material is left out; FAQ Q56 style dated trivia is not used.
NOT VERIFIED (flagged on the cards - quote the official text in an answer sheet):
  * Rule 8(b) proviso plus Rule 10 carry-forward combination: no official worked example is in the sources supplied.
  * Conditions of the hometown-outside-India concession (Rule 7 Note 5): the Guidelines only say 'limited Government assistance'.
  * Contents of O.M. 28020/1/2010-Estt.(C) of 17.08.2016 beyond what the Guidelines print.
Usage
    python build_ltc_b2.py --audit                                  # density + coverage check only (no ffmpeg / internet)
    python build_ltc_b2.py --preview                                # slides only
    python build_ltc_b2.py --no-tts                                 # silent dry run (also writes subtitles and chapter times)
    python build_ltc_b2.py --part 1                                 # one third of the chapters (1, 2 or 3)
    python build_ltc_b2.py --teacher <voice> --student <voice>      # full build (needs internet for edge-tts; ffmpeg+ffprobe with libass on PATH)
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
BUILD_DIR = Path("ltc_b2_build")
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
OUT_STEM = "ltc_b2_masterclass"
OUTPUT_MP4 = Path(OUT_STEM + ".mp4")

# VISUAL BUDGET (px). LTC cards carry many numbers, dates and O.M. citations, so the body text
# is kept large (34 down to 26) and every on-screen card is a short key-point; the full wording goes to the reference sheet.
# The build fails if any card needs to go below these sizes.
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

STUDENT_NAME = "RIYA"

_MONTHS = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December"]


def _date_words(m):
    d, mo, y = int(m.group(1)), int(m.group(2)), m.group(3)
    if 1 <= mo <= 12 and 1 <= d <= 31:
        return f"{d} {_MONTHS[mo]} {y}"
    return m.group(0)


# Pronunciation fixes applied ONLY to the audio text. Subtitles always show the original Roman Hinglish text.
# NOTE: longer patterns first, otherwise "Rule 4(d)" would swallow "Rule 4(d)(i)".
_TTS_FIXES = [
    (r'\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b', _date_words),
    (r'\bRs\.?\s*(\d)', r'Rupees \1'),
    (r'(\d),(\d{3})', r'\1\2'),
    (r'%', ' percent'),
    (r'(\d{4})\s?[–\-]\s?(\d{2,4})', r'\1 to \2'),
    (r'(?<=\d)/(?=\d)', ' slash '),
    (r'-Estt\.?', ' Estt '), (r'Ests\.', 'Ests '),
    (r'\bLTC\b', 'L.T.C.'), (r'\bCCS\b', 'C.C.S.'), (r'\bCCA\b', 'C.C.A.'), (r'\bDoPT\b', 'D.O.P.T.'), (r'\bDOPT\b', 'D.O.P.T.'),
    (r'\bDoP&T\b', 'D.O.P. and T.'), (r'\bOMs\b', 'O.M.s'), (r'\bOM\b', 'O.M.'), (r'\bHoD\b', 'Head of Department'),
    (r'\bHQ\b', 'Headquarters'), (r'\bHT\b', 'Hometown'), (r'\bATA\b', 'A.T.A.'), (r'\bATAs\b', 'A.T.A.s'),
    (r'\bNER\b', 'N.E.R.'), (r'J&K', 'J and K'), (r'A&N', 'A and N'), (r'\bDR\b', 'D.R.'), (r'\bCPC\b', 'C.P.C.'),
    (r'\bEPC\b', 'E.P.C.'), (r'\bIRCTC\b', 'I.R.C.T.C.'), (r'\bITDC\b', 'I.T.D.C.'), (r'\bSTDCs?\b', 'S.T.D.C.'), (r'\bPNR\b', 'P.N.R.'),
    (r'\bDDO\b', 'D.D.O.'), (r'\bPAO\b', 'P.A.O.'), (r'\bFA\b', 'F.A.'), (r'\bPSUs?\b', 'P.S.U.'), (r'\bNCR\b', 'N.C.R.'),
    (r'\bCCL\b', 'C.C.L.'), (r'\bBLCL\b', 'B.L.C.L.'), (r'\bATT\b', 'A.T.T.'), (r'\bTA\b', 'T.A.'), (r'\bUT\b', 'U.T.'), (r'\bUTs\b', 'U.T.s'),
    (r'\bIMS\b', 'I.M.S.'), (r'\bCAG\b', 'C.A.G.'), (r'\bFR\s+9', 'Fundamental Rule 9'), (r'\bSTDC\b', 'S.T.D.C.'),
    (r'\bLPR\b', 'L.P.R.'), (r'\bFAQs\b', 'F.A.Q.s'), (r'\bFAQ\b', 'F.A.Q.'), (r'\bMCQ\b', 'M.C.Q.'), (r'\bMCQs\b', 'M.C.Q.s'),
    (r'\bS\.O\.\s', 'S.O. '), (r'G\.S\.R\.', 'G.S.R.'), (r'\bw\.e\.f\.', 'with effect from'),
    (r'\bSR\s+(\d+)', r'Supplementary Rule \1'),
    # rule / paragraph references (3 levels first)
    (r'Rule\s+(\d+)\((\d+)\)\(([a-z]+|[ivx]+)\)\(([ivx]+)\)', r'Rule \1, sub rule \2, clause \3, sub clause \4'),
    (r'Rule\s+(\d+)\((\d+)\)\(([a-z]+|[ivx]+)\)', r'Rule \1, sub rule \2, clause \3'),
    (r'Rule\s+(\d+)\(([a-z])\)\(([ivx]+)\)', r'Rule \1, clause \2, sub clause \3'),
    (r'Rule\s+(\d+)\((\d+)\)', r'Rule \1, sub rule \2'),
    (r'Rule\s+(\d+)\(([a-z])\)', r'Rule \1, clause \2'),
    (r'\bsub-rules\b', 'sub rules'), (r'\bsub-rule\b', 'sub rule'),
    (r'[—–]', ','),
]


def normalize_for_tts(text: str) -> str:
    for pat, rep in _TTS_FIXES:
        text = re.sub(pat, rep, text)
    return re.sub(r'[ \t]+', ' ', text).strip()


# box tuple = (card title, SHORT on-screen text, FULL text for the reference sheet, colour, Hinglish narration)
# Every scene is one Q&A chapter: intro (optional) -> student question -> one narrated reveal per card -> hook line.
SCENES = [

    {
        "id": "b2_00_title_card",
        "chapter": "BATCH 2 • TITLE CARD: WHAT THIS VIDEO GIVES YOU",
        "title": "CCS (LTC) RULES 1988 — BATCH 2: RULES 7 TO 11",
        "accent": SKY, "badge": "BATCH 2",
        "q": "What will I learn in Batch 2, and how current is it?",
        "intro": ("Namaste dosto! Batch 1 mein humne Rules 1 se 6 padhe, yaani kaun covered hai aur Family kise kehte hain. Ab Batch 2 mein sawaal ye hai: LTC kab milti hai, kitni baar milti hai, aur kis block year mein kaun si milti hai. "
                  "Yahan Rule 7 se Rule 11 tak sab kuch aayega, aur official FAQ ke block year answers bhi."),
        "q_say": "Sir, Batch 2 mein mujhe kya milega, aur ye content kitna latest hai?",
        "boxes": [
            ("WHAT YOU GET",
             "Rules 7 to 11 of the CCS (LTC) Rules 1988 only: admissibility, leave, types of LTC, block years, counting, carry-over, places. Plus FAQ Q13 to Q20 and Q25 to Q27.",
             "Batch 2 scope: Rule 7(1) and (2) with Notes 1 to 5; Rule 8(a), (b) with proviso, (c); FAQ block-year answers Q13 to Q20; Rules 9, 10 and 11; FAQ leave answers Q25 to Q27; scenarios, recap, MCQ drills and flashcards. Strictly the CCS (LTC) Rules 1988 and DoPT orders under them; other services' LTC rules are not covered and superseded items are left out. Ledger V2-TITLE.",
             SKY,
             "Batch 2 mein aapko milega sirf CCS LTC Rules 1988 ke Rule 7 se Rule 11 tak: admissibility, leave, LTC ke types, block years, counting, carry-over aur places. Saath mein FAQ ke block year aur leave ke answers. Kisi aur service ke rules ya purane provisions nahi hain."),
            ("HOW CURRENT IS IT",
             "Checked on the full DoPT Guidelines (03.09.2025) and FAQ (01.07.2025) texts supplied, up to 28.10.2026. The running block is 2026-29. Open items are flagged.",
             "Currency [KNOWN as checked, see the header of the script]: DoPT consolidated Guidelines O.M. dated 03.09.2025 and FAQ O.M. dated 01.07.2025, full texts supplied. The FAQ shows 2022-25 as its current block and 2026-29 as the next; as on 28.10.2026 the block 2026-29 is the running one (derivation, flagged). Ledger V2-TITLE.",
             GREEN,
             "Content 28 October 2026 tak DoPT ke poore Guidelines aur FAQ se check kiya gaya hai. FAQ ke hisaab se agla block 2026 se 29 hai, aur aaj ki date par wahi chal raha hai. Ye ek derivation hai, isliye flagged hai. Exam mein official wording quote kijiye."),
            ("HOW TO USE THIS VIDEO",
             "Pause at every drill. Answer first, then listen. In exams, quote the official wording.",
             "Study method: attempt each MCQ and flashcard before the answer is revealed; revisit the cards you missed. This video is a learning aid and not legal advice; the DoPT order governs. Ledger V2-TITLE.",
             ORANGE,
             "Ek tip. Har drill par video pause kijiye, pehle khud jawab sochiye, phir suniye. Ye video padhai ka saadhan hai, legal advice nahi. Final authority DoPT ka order hai."),
        ],
        "hook": "REMEMBER: Rule 7 gate, Rule 8 types, then block years. Pause at every drill!",
        "hook_say": "Yaad rakhiye: Rule 7 ka gate, Rule 8 ke types, phir block years. Har drill par pause kijiye.",
        "covers": ["V2-TITLE"],
    },
    {
        "id": "b2_01_rule7_1_gate",
        "chapter": "CHAPTER 1 • RULE 7(1): WHO CAN ACTUALLY TRAVEL ON LTC — THE ONE-YEAR GATE",
        "title": "RULE 7(1) — ONE YEAR OF CONTINUOUS SERVICE ON THE DATE OF JOURNEY",
        "accent": SKY, "badge": "RULE 7(1)",
        "q": "From when is LTC admissible, and which categories does Rule 7(1) cover?",
        "q_say": "Sir, Rule 7 ke hisaab se LTC kab se milti hai, aur kin categories par ye lagta hai?",
        "boxes": [
            ("THE TEXT",
             "LTC is admissible to categories (i) and (iii) of Rule 1(3) only if they have completed one year's continuous Central Government service on the date of journey.",
             "Rule 7(1) as printed in the 2025 Guidelines [VERIFIED]: the Leave Travel Concession shall be admissible to persons of the categories specified in clauses (i) and (iii) of sub-rule (3) of Rule 1 only, if they have completed one year's continuous service under the Central Government on the date of journey performed by him or his family, as the case may be, to avail of the concession. Ledger R7(1).",
             SKY,
             "Rule 7 sub rule 1. LTC sirf Rule 1 ke sub rule 3 ki clause i aur clause iii wali categories ko milti hai, aur tab milti hai jab Central Government ki ek saal ki continuous service poori ho chuki ho, journey ki date par. Ye journey employee ki ho ya uski Family ki."),
            ("TWO CATEGORIES NAMED",
             "Rule 7(1) names categories (i) civil servants and (iii) contract appointees. Categories (ii) and (iv) get their gate from Rule 2(1) (Batch 1); (iii) is read with both.",
             "Reading of the text [VERIFIED, wording of Rule 7(1) in the Guidelines]: only clauses (i) and (iii) of Rule 1(3) are named in Rule 7(1). Clauses (ii), (iii) and (iv) carry their own one-year-plus-certificate gate in Rule 2(1), which was taught in Batch 1; so clause (iii) is read with both Rule 7(1) and Rule 2(1). Ledger R7(1)-CAT.",
             GREEN,
             "Rule 7 sub rule 1 mein sirf do categories ka naam hai: clause i, civil services aur posts, aur clause iii, contract appointees. Categories do aur chaar ka gate Rule 2 sub rule 1 mein hai, jo humne Batch 1 mein padha. Clause teen par Rule 2 sub rule 1 bhi lagta hai, to dono ko jodkar padhna hai."),
            ("ON THE DATE OF JOURNEY",
             "The gate is tested on the date the journey is performed, by the employee or by the Family member. Not on the date of applying.",
             "Reading of the text [VERIFIED, 'on the date of journey performed by him or his family, as the case may be']: the one-year test is applied to the date on which the journey is performed. A Family member's journey is therefore tested against the employee's service on the date of that journey. Ledger R7(1)-DATE.",
             ORANGE,
             "Gate ki date journey ki date hai, application ki nahi. Aur agar Family ka member alag se travel kar raha hai, to bhi dekha jayega ki us journey ki date par employee ki ek saal ki service poori hui ya nahi."),
            ("TRAP: AN EARLY FAMILY JOURNEY",
             "Spouse travels in month 10 of service: gate not met on that date. The same journey in month 13 is fine.",
             "Teaching example [follows from the Rule 7(1) wording]: because the test is the date of journey performed by him or his family, a Family journey that starts before the employee has completed one year of continuous service fails the gate, while the same journey after the first anniversary passes. Ledger R7(1)-DATE.",
             RED,
             "Ek trap. Employee ko service mein das mahine hue aur uski wife journey kar leti hai. Us date par gate nahi khula, to wo journey admissible nahi. Wahi journey terahwe mahine mein ho, to theek hai."),
        ],
        "hook": "REMEMBER: one year of continuous Central service, tested on the date of journey — employee's or Family's!",
        "hook_say": "Yaad rakhiye: ek saal ki continuous Central service, aur test journey ki date par lagta hai, employee ki ho ya Family ki.",
        "covers": ["R7(1)", "R7(1)-CAT", "R7(1)-DATE"],
    },
    {
        "id": "b2_02_rule7_2_leave",
        "chapter": "CHAPTER 2 • RULE 7(2) AND THE FAQ ON LEAVE: WHICH LEAVE, AND WHEN IS LEAVE NEEDED?",
        "title": "RULE 7(2) — LTC DURING ANY PERIOD OF LEAVE, BUT NOT ON A WEEKEND ALONE",
        "accent": GREEN, "badge": "RULE 7(2)",
        "q": "Which leave is needed for LTC, and is leave needed when only the Family travels?",
        "q_say": "Sir, LTC ke liye kaun si leave chahiye? Aur agar sirf family ja rahi ho to kya employee ko leave leni padegi?",
        "boxes": [
            ("RULE 7(2): ANY LEAVE",
             "LTC is admissible during any period of leave, including casual leave and special casual leave. FAQ Q25 adds child care leave.",
             "Rule 7(2) [VERIFIED in the Guidelines]: the leave travel concession shall be admissible during any period of leave, including casual leave and special casual leave. FAQ Q25 [VERIFIED, FAQ O.M. 01.07.2025 full text supplied]: travel on LTC is admissible during any kind of leave, including casual leave, special casual leave and child care leave; O.M. No. 13018/6/2013-Estt(L) dated 03.04.2018. Ledger R7(2), FAQ-Q25.",
             SKY,
             "Rule 7 sub rule 2. LTC kisi bhi tarah ki leave ke dauraan admissible hai, casual leave aur special casual leave bhi. FAQ Q25 mein child care leave ka naam bhi likha hai. Matlab leave ka type kam, leave ka hona zyada zaroori hai."),
            ("NO LEAVE, NO LTC: WEEKENDS",
             "Not admissible for a journey on weekend holidays without any leave. FAQ Q27: LTC cannot be availed on week-ends or holidays alone; some leave due and admissible is needed.",
             "Rule 7 Note 2 [VERIFIED in the Guidelines]: not admissible for journeys during the weekend holidays without any leave. FAQ Q27 [VERIFIED]: LTC cannot be availed during week-end or holidays alone; it is necessary to avail of any kind of leave due and admissible when the LTC is availed of by the Government employee. Ledger R7-N2, FAQ-Q27.",
             ORANGE,
             "Ek aur point. Sirf weekend ya holiday par LTC nahi hoti. Employee ko koi na koi leave leni hi padti hai, jo due aur admissible ho. Note do aur FAQ Q27, dono yahi kehte hain."),
            ("WHEN ONLY FAMILY TRAVELS",
             "FAQ Q26: when only the Family travels, the employee need not take leave.",
             "FAQ Q26 [VERIFIED]: is it necessary to avail leave by the Government employee when only his or her family members are travelling? Answer: No. Ledger FAQ-Q26.",
             GREEN,
             "Agar sirf Family ke members ja rahe hain aur employee nahi, to employee ko leave lene ki zaroorat nahi. FAQ Q26 ka seedha jawab hai: No."),
            ("CCL AND STUDY LEAVE",
             "Note 3: LTC is also admissible during child care leave and study leave (O.M.s 03.04.2018 and 30.03.1988).",
             "Rule 7 Note 3 [VERIFIED in the Guidelines]: LTC also admissible during CCL and study leave; O.M. No. 13018/6/2013-Estt(L) dated 03.04.2018 and O.M. No. 31011/1/88-Estt.(A) dated 30.03.1988. The fare mechanics of the study-leave O.M. were taught in Batch 1 (Chapter 16). Ledger R7-N3.",
             RED,
             "Note teen. Child care leave aur study leave ke dauraan bhi LTC admissible hai. Study leave ka fare kaise nikalta hai, wo Batch 1 mein humne dekha tha: headquarters wale fare ya actual mein jo kam ho."),
        ],
        "hook": "REMEMBER: any leave works, but no leave means no LTC. Family-only travel needs no leave!",
        "hook_say": "Yaad rakhiye: koi bhi leave chalegi, lekin bina leave ke LTC nahi. Sirf Family ja rahi ho, to employee ko leave nahi chahiye.",
        "covers": ["R7(2)", "R7-N2", "R7-N3", "R7-LEAVE-FAQ", "FAQ-Q25", "FAQ-Q26", "FAQ-Q27"],
    },
    {
        "id": "b2_03_rule7_notes_conduct",
        "chapter": "CHAPTER 3 • RULE 7 NOTE 1: VACATION, CLASS OF TRAVEL, INFORMING THE OFFICER, SERVICE RECORD",
        "title": "RULE 7 NOTE 1 — FOUR PRACTICAL RULES BEFORE YOU TRAVEL",
        "accent": ORANGE, "badge": "RULE 7 NOTE 1",
        "q": "What are the four practical conditions under Note 1 to Rule 7?",
        "q_say": "Sir, Rule 7 ke Note 1 mein kaun si chaar practical baatein hain jo journey se pehle yaad rakhni chahiye?",
        "boxes": [
            ("1(i) VACATION DEPARTMENT",
             "For staff of a vacation department, vacation is treated as regular leave for LTC.",
             "Rule 7 Note 1(i) [VERIFIED in the Guidelines; O.M. No. 43/1/55-Estt.(A) Part-II dated 11.10.1956]: in the case of a Government servant serving in a vacation department, vacation will be treated as regular leave for the purpose of this concession. Ledger R7-N1(i).",
             SKY,
             "Note 1 ka pehla point. Jo employee vacation department mein hai, unke liye vacation ko regular leave maana jata hai. To vacation mein LTC le sakte hain."),
            ("1(ii) CLASS OF TRAVEL",
             "The class of railway accommodation is the class to which he is entitled under the normal rules at the time the journeys are undertaken.",
             "Rule 7 Note 1(ii) [VERIFIED]: the class of railway accommodation to which a Government servant and his family will be entitled is the class to which he is entitled under the normal rules at the time the journeys are undertaken. Ledger R7-N1(ii).",
             GREEN,
             "Doosra point. Train ka class wahi milega jo journey ke samay normal rules ke hisaab se employee ki entitlement hai. Pehle ka class ya promotion ke pehle ka nahi, journey ki date wala."),
            ("1(iii) INFORM AND PROVE",
             "Inform the Controlling Officer before the journey; produce evidence of having actually performed it.",
             "Rule 7 Note 1(iii) [VERIFIED]: Government servants should inform the Controlling Officer before journeys for which assistance under this scheme will be claimed are undertaken. They should also produce evidence of their having actually performed the journey. Ledger R7-N1(iii).",
             ORANGE,
             "Teesra point. Journey se pehle Controlling Officer ko inform karna hai, aur journey ke baad saboot dena hai ki journey sach mein hui. Ye do cheezein claim ki neev hain."),
            ("1(iv) SERVICE RECORD ENTRY",
             "The authority keeping the service record must note on every leave entry whether travel assistance was availed or not.",
             "Rule 7 Note 1(iv) [VERIFIED]: the authority responsible for the maintenance of the service record shall ensure that on every occasion a Government servant proceeds on leave which is entered in that record, the fact whether or not he availed of the travel assistance under these orders is indicated. Ledger R7-N1(iv).",
             RED,
             "Chautha point. Service record sambhalne wali authority ko har leave ki entry par likhna hai ki us bar LTC li gayi ya nahi. Isse block year ka hisaab record mein rehta hai."),
        ],
        "hook": "REMEMBER: vacation = leave; class at time of journey; inform before, prove after; note it in the service record!",
        "hook_say": "Yaad rakhiye: vacation ko leave maana jata hai, class journey ke samay ki, pehle inform kijiye aur baad mein saboot dijiye, aur service record mein entry hogi.",
        "covers": ["R7-N1(i)", "R7-N1(ii)", "R7-N1(iii)", "R7-N1(iv)"],
    },
    {
        "id": "b2_04_rule7_notes_special",
        "chapter": "CHAPTER 4 • RULE 7 NOTES 4 AND 5: TECHNICAL RESIGNATION AND HOMETOWN OUTSIDE INDIA",
        "title": "RULE 7 NOTES 4-5 — TWO SPECIAL CASES THAT CHANGE THE ENTITLEMENT",
        "accent": BLUE, "badge": "RULE 7 NOTES 4-5",
        "q": "What happens to LTC on a technical resignation, and what if the Hometown is outside India?",
        "q_say": "Sir, technical resignation ke baad LTC ka kya hota hai? Aur agar Hometown India ke bahar ho to?",
        "boxes": [
            ("NOTE 4: TECHNICAL RESIGNATION",
             "LTC entitlement carries forward. A person who resigns within 8 years of appointment and joins another Government post after technical resignation is treated as a fresh recruit from the date of initial appointment. (Rest of O.M. not read, flagged.)",
             "Rule 7 Note 4 [VERIFIED in the Guidelines; O.M. No. 28020/1/2010-Estt.(C) dated 17.08.2016]: the entitlement of LTC may be carried forward in the case of a Central Government servant who joins another post after having submitted technical resignation. A Government servant who resigns within 8 years of his appointment and joins another post in the Government after technical resignation will be treated as a fresh recruit from the date of his initial appointment. UNVERIFIED: the rest of the 2016 O.M. was not read. Ledger R7-N4.",
             SKY,
             "Note 4. Agar Central Government employee technical resignation dekar doosri Government post join karta hai, to LTC entitlement aage carry hoti hai. Aur jo aath saal ke andar resign karke join kare, use initial appointment ki date se fresh recruit maana jata hai. Is O.M. ka baaki text maine nahi padha, ye flag hai."),
            ("WHY THIS MATTERS",
             "Fresh recruit status keeps the special 8-LTC cycle running from the first joining date (taught in Batch 3).",
             "Link [teaching note]: fresh-recruit status means the special first-eight-years cycle of FAQ Q64 to Q70 continues to be reckoned from the initial date of joining, as FAQ Q65 says for a change of job within Government. The cycle itself is taught in Batch 3. Ledger R7-N4.",
             GREEN,
             "Isse kya farak padta hai? Fresh recruit ka special cycle, yaani pehle aath saal ke aath LTC, initial joining ki date se hi chalta rehta hai, chahe naukri badal jaye. Wo cycle hum Batch 3 mein padhenge."),
            ("NOTE 5: HOMETOWN OUTSIDE INDIA",
             "If the employee declares a Hometown outside India and the Controlling Officer is satisfied, LTC to that Hometown is allowed with limited Government assistance. Conditions flagged.",
             "Rule 7 Note 5 [VERIFIED in the Guidelines]: a Government servant who declares, subject to the satisfaction of the Controlling Officer, that his hometown is outside India, will also be entitled to the Leave Travel Concession for visiting his hometown, but with limited government's assistance. UNVERIFIED: the Guidelines do not print how the limit is worked out, so the formula is not taught here. Ledger R7-N5.",
             ORANGE,
             "Note 5. Agar employee declare kare ki uska Hometown India ke bahar hai, aur Controlling Officer satisfy ho, to us Hometown ke liye bhi LTC milti hai, lekin limited Government assistance ke saath. Limit kaise nikalti hai, ye Guidelines nahi batate, isliye wo formula yahan flagged hai aur nahi sikhaya."),
            ("EXAM ANGLE",
             "Note 4: 'within 8 years'. Note 5: 'limited assistance'. Do not claim a formula the text does not give.",
             "Exam angle [teaching construct]: the two numbers and phrases to remember are 'within 8 years of appointment' (Note 4) and 'limited government's assistance' (Note 5). Where a question asks for a rupee limit on a hometown outside India, quote the Guidelines wording and say the limit is set by the relevant O.M. Ledger R7-N5.",
             RED,
             "Exam ke liye do phrase yaad rakhiye. Note 4 mein within 8 years of appointment. Note 5 mein limited assistance. Agar paisa kitna milega pooche, to Guidelines ka wording likhiye aur kahiye ki limit relevant O.M. se tay hoti hai."),
        ],
        "hook": "REMEMBER: technical resignation within 8 years = fresh recruit from first appointment; outside-India Hometown = limited assistance!",
        "hook_say": "Yaad rakhiye: aath saal ke andar technical resignation par fresh recruit status pehli appointment se, aur India ke bahar ke Hometown par limited assistance.",
        "covers": ["R7-N4", "R7-N5"],
    },
    {
        "id": "b2_05_rule8_types",
        "chapter": "CHAPTER 5 • RULE 8: THE TYPES OF LTC — HOMETOWN, ANY PLACE IN INDIA, AND THE YEARLY SELF VISIT",
        "title": "RULE 8 — (a) HOMETOWN, (b) ANY PLACE IN INDIA WITH PROVISO, (c) YEARLY SELF-ONLY VISIT",
        "accent": GREEN, "badge": "RULE 8",
        "q": "What are the types of LTC under Rule 8 and how often can each be availed?",
        "q_say": "Sir, Rule 8 mein LTC ke kaun se types hain, aur har type kitni baar milta hai?",
        "boxes": [
            ("8(a): HOMETOWN LTC",
             "Hometown LTC: once in a block of two calendar years (e.g. 1986-87, 1988-89), irrespective of distance between headquarters and Hometown.",
             "Rule 8(a) [VERIFIED in the Guidelines]: LTC to hometown shall be admissible irrespective of the distance between the headquarters of the Government servant and his hometown, once in a block of two calendar years, such as 1986-87, 1988-89 and so on. Ledger R8(a).",
             SKY,
             "Rule 8 clause a. Hometown LTC do calendar years ke block mein ek baar milti hai, distance chahe kitni bhi ho. Block jaise 1986-87, 1988-89, aur isi tarah aage. Aaj ke blocks 2026-27 aur 2028-29 hain."),
            ("8(b): ANY PLACE IN INDIA",
             "Any-place LTC: once in a block of four calendar years (e.g. 1986-89, 1990-93), irrespective of distance.",
             "Rule 8(b) [VERIFIED]: LTC to any place in India admissible irrespective of the distance of the place of visit from the headquarters of the Government servant, once in a block of four calendar years, such as 1986-89, 1990-93 and so on. Ledger R8(b).",
             GREEN,
             "Clause b. Any place in India LTC chaar calendar years ke block mein ek baar milti hai, distance se koi matlab nahi. Aaj ka chaar saal ka block 2026 se 2029 hai."),
            ("8(b) PROVISO: IN LIEU OF",
             "If Hometown LTC is admissible to the employee, any-place LTC availed is in lieu of, and adjusted against, the Hometown LTC available at the start of the journey. (Official illustration flagged.)",
             "Proviso to Rule 8(b) [VERIFIED]: in the case of a Government servant to whom Leave Travel Concession to hometown is admissible, the Leave Travel Concession to any place in India availed of by him shall be in lieu of, and adjusted against, the Leave Travel Concession to hometown available to him at the time of commencement of the journey. UNVERIFIED: no official worked illustration of how this combines with Rule 10 is in the sources supplied. Ledger R8(b)-PROV.",
             ORANGE,
             "Proviso ye kehta hai: jis employee ko Hometown LTC milti hai, wo agar any place in India LTC leta hai to wo Hometown LTC ke badle mein aur uske against adjust hoti hai, us Hometown LTC ke against jo journey shuru hone ke samay available thi. Rule 10 ke saath iska combination kaise chalta hai, uska official example sources mein nahi hai, isliye wo flagged hai."),
            ("8(c): YEARLY SELF-ONLY VISIT",
             "If the Family lives at his Hometown, the employee may choose, in lieu of all LTC concessions, a visit for self only to the Hometown every year.",
             "Rule 8(c) [VERIFIED]: a Government servant whose family lives away from him at his hometown may, in lieu of all concessions under this scheme, including the Leave Travel Concession to visit any place in India once in a block of four years which would otherwise be admissible to him and members of his family, choose to avail of leave travel concession for self only to visit the hometown every year. Ledger R8(c).",
             RED,
             "Clause c. Jis employee ki Family uske Hometown par rehti hai, wo chahe to saari concessions ke badle, any place in India wali bhi, sirf apne liye har saal Hometown jaane ki LTC choose kar sakta hai. Family ke liye phir kuch nahi milta."),
        ],
        "hook": "REMEMBER: Hometown 2-yr block; Any place 4-yr block, in lieu of Hometown; Family at Hometown: yearly self visit!",
        "hook_say": "Yaad rakhiye: Hometown LTC do saal ke block mein, any place LTC chaar saal ke block mein aur Hometown LTC ke badle mein, aur Family Hometown par ho to har saal sirf self ki LTC.",
        "covers": ["R8(a)", "R8(b)", "R8(b)-PROV", "R8(c)"],
    },
    {
        "id": "b2_06_block_years",
        "chapter": "CHAPTER 6 • FAQ Q13, Q15, Q18: WHAT IS A BLOCK YEAR, AND WHAT IS THE RUNNING BLOCK?",
        "title": "BLOCK YEARS — FOUR CALENDAR YEARS, SPLIT INTO TWO SUB-BLOCKS FOR HOMETOWN HOLDERS",
        "accent": SKY, "badge": "FAQ Q13-Q18",
        "q": "What is a block year, how is it split, and which block is running now?",
        "q_say": "Sir, block year kya hota hai, usme sub-blocks kaise bante hain, aur abhi kaun sa block chal raha hai?",
        "boxes": [
            ("Q13: THE BLOCK YEAR",
             "A block year is four calendar years. FAQ shows 2022-25 as its current block and 2026-29 as the next. Hometown holders get two sub-blocks of two years.",
             "FAQ Q13 [VERIFIED on the FAQ O.M. 01.07.2025 full text supplied]: block year is a period of 4 calendar years; for employees having an approved Home Town, the block of 4 years is divided in two sub-blocks, e.g. 2022-23 and 2024-25, and the employee can avail either Any Place in India or Home Town in each sub-block (Table-2). Table-1 lists the blocks 2018-21, 2022-25 and 2026-29. Ledger FAQ-Q13.",
             SKY,
             "Q13. Block year chaar calendar years ka period hota hai. FAQ ke table mein 2018 se 21, 2022 se 25 aur 2026 se 29 diye hain. Jinke paas approved Hometown hai, unka chaar saal ka block do sub-blocks mein bantta hai, jaise 2022-23 aur 2024-25."),
            ("TODAY: BLOCK 2026-29",
             "On 28.10.2026 the running block is 2026-29: sub-blocks 2026-27 and 2028-29. Derived from the FAQ's block table, flagged.",
             "Derivation [flagged]: the FAQ (01.07.2025) shows 2022-25 as its current block and 2026-29 as the next block in Table-1 and Q16/Q17. Calendar-year blocks follow the Rule 8 pattern of four years, so on 28.10.2026 the running block is 2026-29 with sub-blocks 2026-27 and 2028-29. This is read from the FAQ's own tables and is not quoted from a separate 2026 order. Ledger BLOCK-NOW.",
             GREEN,
             "Aaj ki date, 28 October 2026 ko, chalta hua block 2026 se 2029 hai, aur sub-blocks 2026-27 aur 2028-29. Ye maine FAQ ke apne tables se nikala hai, kisi alag 2026 ke order se nahi, isliye ye ek flagged derivation hai."),
            ("Q15: CHOOSING THE ORDER",
             "Where HQ and Hometown differ: either Hometown or Any Place in the first sub-block, the other in the second sub-block, as per choice.",
             "FAQ Q15 [VERIFIED]: where Headquarters and Home Town are different, the employee can avail either 'Any Place in India' or 'Home Town' LTC in the first sub-block and the remaining one in the second sub-block, as per his choice. Table-2: Option 1: Home Town then Any Place; Option 2: Any Place then Home Town. Ledger FAQ-Q15.",
             ORANGE,
             "Q15. Jinka Headquarters aur Hometown alag hain, wo pehle sub-block mein Hometown ya any place chun sakte hain, aur baaki wala doosre sub-block mein. Option ek: pehle Hometown, phir any place. Option do: pehle any place, phir Hometown."),
            ("Q18: EXTENSION BY ONE YEAR",
             "Blocks and sub-blocks automatically extend by one year, up to 31 December of the next calendar year.",
             "FAQ Q18 [VERIFIED]: block of four years and sub-block of two years automatically gets extended by one year (up to 31st of December of next calendar year). This works with Rule 10 on carry-over. Ledger FAQ-Q18.",
             RED,
             "Q18. Chaar saal ka block aur do saal ka sub-block apne aap ek saal badh jate hain, yaani agle calendar year ki 31 December tak. Ye Rule 10 ke carry-over se jura hai, jo hum aage dekhenge."),
        ],
        "hook": "REMEMBER: block = 4 calendar years; Hometown holders get 2 sub-blocks; today's block is 2026-29; extension by one year!",
        "hook_say": "Yaad rakhiye: block chaar calendar years ka, Hometown wale ke do sub-blocks, aaj ka block 2026 se 29, aur ek saal ka automatic extension.",
        "covers": ["FAQ-Q13", "FAQ-Q15", "FAQ-Q18", "BLOCK-NOW"],
    },
    {
        "id": "b2_07_same_hq_ht",
        "chapter": "CHAPTER 7 • FAQ Q14, Q17, Q19, Q20: WHEN HEADQUARTERS AND HOMETOWN ARE THE SAME",
        "title": "SAME HEADQUARTERS AND HOMETOWN — ONE ANY-PLACE LTC PER BLOCK, NO HOMETOWN LTC",
        "accent": ORANGE, "badge": "FAQ Q14-Q20",
        "q": "What do employees get when Headquarters and Hometown are the same, and what about NCR towns?",
        "q_say": "Sir, jab Headquarters aur Hometown ek hi ho to LTC kaise milti hai? Aur NCR ke shehron ka kya?",
        "boxes": [
            ("Q14 AND Q19: ONE ANY-PLACE LTC",
             "Same HQ and Hometown: not eligible for Hometown LTC; eligible for one Any Place in India LTC per four-year block.",
             "FAQ Q14 [VERIFIED]: the Government employee is eligible for one Anywhere All India LTC in the four-year block (Table-1). FAQ Q19 [VERIFIED; O.M. No. 31011/4/2007-Estt.(A-IV) dated 18.05.2015]: employees whose headquarters/place of posting and Home Town are the same are not eligible for Home Town LTC. Ledger FAQ-Q14, FAQ-Q19.",
             SKY,
             "Q14 aur Q19 saath dekhte hain. Jab Headquarters aur Hometown ek hi jagah hon, to Hometown LTC nahi milti, kyunki Hometown LTC ka matlab hi alag jagah ka hona hai. Bas chaar saal ke block mein ek any place in India LTC milti hai."),
            ("Q17: TWO IN THE FIRST YEAR",
             "Same HQ and Hometown: two any-place LTCs can be availed in the first year of a block: one unavailed from the previous block and one of the new block.",
             "FAQ Q17 [VERIFIED]: yes, he or she can avail 2 LTCs in the first year of each block of 4 years. Case 2: in calendar year 2026, one unavailed LTC of the block 2022-25 and one of the next block 2026-29 can be availed. (Case 1, calendar year 2022, shows the same pattern with block 2018-21.) Ledger FAQ-Q17.",
             GREEN,
             "Q17. Jinke Headquarters aur Hometown same hain, wo block ke pehle saal mein do LTC le sakte hain. Ek pichhle block ki jo unavailed rahi, aur ek naye block ki. FAQ ka case do: calendar year 2026 mein 2022-25 wali bachi hui LTC aur 2026-29 wali LTC."),
            ("Q20: NCR TOWNS ARE NOT DELHI",
             "Delhi HQ but living in a town of another NCR State: that is not Delhi headquarters, so Hometown LTC is allowed.",
             "FAQ Q20 [VERIFIED; O.M. No. 31011/4/2007-Estt.(A-IV) dated 18.05.2015]: cities and towns outside Delhi that fall in other States of the National Capital Region are not to be treated as Delhi headquarters; employees whose headquarters are Delhi and who reside in such towns of other NCR States are eligible for Home Town concession. Ledger FAQ-Q20.",
             ORANGE,
             "Q20. Delhi ke bahar ke wo shehar jo doosre NCR states mein aate hain, unhe Delhi headquarters nahi maana jata. To jis employee ka headquarters Delhi hai aur wo aise shehar ka rehne wala hai, uski Hometown LTC allowed hai."),
            ("TRAP: SAME PLACE, NO HOMETOWN LTC",
             "Delhi HQ and Delhi Hometown: no Hometown LTC. Delhi HQ and Ghaziabad Hometown: Hometown LTC allowed (Q19 versus Q20).",
             "Teaching contrast [follows from FAQ Q19 and Q20]: if both are the same place, no Hometown LTC; if the Hometown is a town in another NCR State, the places differ for this purpose and Hometown LTC is allowed. Ledger FAQ-Q19, FAQ-Q20.",
             RED,
             "Trap. Delhi headquarters aur Delhi hi Hometown, to Hometown LTC nahi. Lekin Delhi headquarters aur Hometown doosre NCR state ka koi shehar, jaise Ghaziabad, to Hometown LTC milti hai. Q19 aur Q20 ka farak yahi hai."),
        ],
        "hook": "REMEMBER: same HQ and Hometown = no Hometown LTC; two any-place LTCs only in a block's first year; NCR towns are not Delhi!",
        "hook_say": "Yaad rakhiye: Headquarters aur Hometown same ho to Hometown LTC nahi, block ke pehle saal mein do any place LTC ho sakti hain, aur doosre NCR states ke shehar Delhi nahi maane jaate.",
        "covers": ["FAQ-Q14", "FAQ-Q17", "FAQ-Q19", "FAQ-Q20"],
    },
    {
        "id": "b2_08_two_in_one_year",
        "chapter": "CHAPTER 8 • FAQ Q16: TWO LTCs IN ONE CALENDAR YEAR FOR HOMETOWN HOLDERS",
        "title": "TWO LTCs IN ONE YEAR — THE FIRST YEAR OF A SUB-BLOCK",
        "accent": BLUE, "badge": "FAQ Q16",
        "q": "Can a Hometown holder take two LTCs in a single calendar year?",
        "q_say": "Sir, jis employee ne Hometown declare kiya hai, kya wo ek hi calendar year mein do LTC le sakta hai?",
        "boxes": [
            ("Q16: YES, AT THE START OF A SUB-BLOCK",
             "A Hometown holder can take two LTCs (Any Place and Hometown) in one year, at the beginning of each sub-block: one unavailed from the previous sub-block and one of the new one.",
             "FAQ Q16 [VERIFIED]: yes. He can take two LTCs in the beginning of each sub-block. Case 1: calendar year 2022, one unavailed LTC of the previous block year (2020-21) and one of the current block (2022-23). Case 2: 2024, one unavailed of 2022-23 and one of 2024-25. Case 3: calendar year 2026, one unavailed LTC of 2024-25 and one of the current block 2026-27. Ledger FAQ-Q16.",
             SKY,
             "Q16. Haan, sub-block ki shuruaat mein do LTC ho sakti hain. Ek pichhle sub-block ki jo unavailed rahi, aur ek naye sub-block ki. Case teen, calendar year 2026: 2024-25 ki bachi hui LTC aur 2026-27 ki LTC."),
            ("TODAY'S CASE: CALENDAR YEAR 2026",
             "In 2026: one unavailed LTC of sub-block 2024-25 plus one of sub-block 2026-27.",
             "Current illustration [VERIFIED, FAQ Q16 Case 3]: in the calendar year 2026, one unavailed LTC of the previous block year (2024-25) and one of the current block (2026-27) can be availed. Ledger FAQ-Q16.",
             GREEN,
             "Aaj ka example. 2026 mein employee ek wo LTC le sakta hai jo 2024-25 sub-block mein unavailed rahi, aur ek 2026-27 wale sub-block ki. Dono ek hi calendar year mein."),
            ("WHY THE EXTENSION MATTERS",
             "Unavailed LTC can be used in the first year of the next block (Rule 10); Q18 extends blocks by one year to the same effect.",
             "Link [teaching note]: FAQ Q18 extends each block and sub-block by one year, and Rule 10 lets an unavailed LTC be availed within the first year of the next block. FAQ Q16 and Q17 show the combined effect: two LTCs in the first year, one carried over and one fresh. Ledger FAQ-Q16, R10.",
             ORANGE,
             "Ye possible kyun hai? Q18 har block aur sub-block ko ek saal badha deta hai, aur Rule 10 kehta hai ki unavailed LTC agle block ke pehle saal mein li ja sakti hai. Dono mil kar pehle saal mein do LTC ka rasta banate hain."),
            ("TRAP: SECOND YEAR OF THE SUB-BLOCK",
             "A carried-over LTC must be used in the FIRST year of the next block or sub-block. Year two does not give a second chance.",
             "Trap [follows from Rule 10, 'within the first year of the next block']: the carry-over window is the first year only. Fresh recruits have a different rule (no carry-over, taught in Batch 3). Ledger R10.",
             RED,
             "Trap. Carry-over wali LTC agle block ya sub-block ke pehle saal mein hi leni hoti hai. Doosre saal mein dobara mauka nahi milta. Fresh recruits ka alag rule hai, wo Batch 3 mein."),
        ],
        "hook": "REMEMBER: two LTCs in one year only in the first year of a sub-block — one carried over, one fresh!",
        "hook_say": "Yaad rakhiye: ek saal mein do LTC sirf sub-block ke pehle saal mein, ek carry-over wali aur ek nayi.",
        "covers": ["FAQ-Q16"],
    },
    {
        "id": "b2_09_rule9_10_11",
        "chapter": "CHAPTER 9 • RULES 9, 10 AND 11: COUNTING, CARRY-OVER AND PLACES VISITED",
        "title": "RULES 9, 10, 11 — OUTWARD JOURNEY DECIDES THE BLOCK; CARRY OVER ONE YEAR; DIFFERENT PLACES",
        "accent": ORANGE, "badge": "RULES 9-11",
        "q": "Which block does a journey count against, how does carry-over work, and can everyone visit different places?",
        "q_say": "Sir, journey kis block mein ginti jati hai, carry-over kaise chalta hai, aur kya sab alag alag jagah ja sakte hain?",
        "boxes": [
            ("RULE 9: COUNTING",
             "Family may travel in different groups at different times. LTC counts against the block in which the OUTWARD journey commenced, even if the return falls after the block ends.",
             "Rule 9 [VERIFIED in the Guidelines]: a Government servant and members of his family availing of LTC may travel in different groups at different times during a block of two or four years, as the case may be. The concession so availed of will be counted against the block of two years or four years within which the outward journey commenced, even if the return journey was performed after the expiry of the block. This will apply to LTC carried forward in terms of Rule 10. Ledger R9.",
             SKY,
             "Rule 9. Employee aur Family alag alag groups mein, alag alag samay par travel kar sakte hain. LTC us block mein ginti jati hai jisme outward journey shuru hui, chahe return journey block khatam hone ke baad ho. Ye carried forward LTC par bhi lagta hai."),
            ("RULE 10: CARRY OVER",
             "Unable to avail within a block: may avail within the first year of the next block of two or four years.",
             "Rule 10 first sentence [VERIFIED]: a Government servant who is unable to avail of the leave travel concession within a particular block of two years or four years, may avail of the same within the first year of the next block of two years or four years. Ledger R10.",
             GREEN,
             "Rule 10. Jo employee kisi block mein LTC nahi le paya, wo use agle block ke pehle saal ke andar le sakta hai, chahe do saal ka block ho ya chaar saal ka."),
            ("RULE 10: THE HOMETOWN LINK",
             "If entitled to Hometown LTC, any-place LTC can be carried forward only if the Hometown LTC of the second two-year block was carried forward. Official illustration: flagged.",
             "Rule 10 second sentence [VERIFIED]: if a Government servant is entitled to leave travel concession to home town, he can carry forward the leave travel concession to any place in India for a block of four years only if he has carried forward the leave travel concession to home town in respect of the second block of two years within the block of four years. UNVERIFIED: no official worked illustration of this combination is in the sources supplied, so only the wording is taught. Ledger R10-HT-LINK.",
             ORANGE,
             "Rule 10 ka doosra sentence. Jo Hometown LTC ka hakdaar hai, wo any place in India LTC chaar saal ke block ke liye tabhi carry forward kar sakta hai jab usne us chaar saal ke block ke andar doosre do saal ke block ki Hometown LTC bhi carry forward ki ho. Iska official example sources mein nahi hai, isliye sirf wording sikhai jayegi, aur wo flagged hai."),
            ("RULE 11: DIFFERENT PLACES",
             "Employee and each Family member may visit different places of their choice in a four-year block. Family need not go where the employee went.",
             "Rule 11 [VERIFIED, heading: places under LTC to any place in India]: a Government servant and each member of his family may visit different places of their choice during a block of four years. It shall not be necessary for members of family of a Government servant to visit the same place as that visited by the Government servant himself at any time earlier during the same block. Place declaration under Rule 6 was taught in Batch 1. Ledger R11.",
             RED,
             "Rule 11. Employee aur Family ka har member chaar saal ke block mein alag alag jagah ja sakte hain. Family ko wahi jagah jaana zaroori nahi jahan employee pehle gaya ho. Har baar jagah ka declaration Rule 6 ke hisaab se Controlling Officer ko karna hai, jo Batch 1 mein tha."),
        ],
        "hook": "REMEMBER: outward journey fixes the block; carry over to the first year only; places can differ for each person!",
        "hook_say": "Yaad rakhiye: outward journey block tay karti hai, carry-over sirf agle block ke pehle saal mein, aur har member alag jagah ja sakta hai.",
        "covers": ["R9", "R10", "R10-HT-LINK", "R11"],
    },
    {
        "id": "b2_10_traps_and_scenarios",
        "chapter": "CHAPTER 10 • SCENARIO BANK AND TRAPS FOR RULES 7 TO 11",
        "title": "FOUR SCENARIOS — APPLY THE RULES ONE STEP AT A TIME",
        "accent": RED, "badge": "SCENARIOS",
        "q": "How do I apply the gate, the block, the counting rule and carry-over to real cases?",
        "q_say": "Sir, in rules ko real cases par kaise lagayein? Kuch scenarios dekh lete hain.",
        "boxes": [
            ("SCENARIO 1: DECEMBER AND JANUARY",
             "Outward 28.12.2027, return 04.01.2028: the LTC counts against the block of the OUTWARD journey, sub-block 2026-27, not 2028-29.",
             "Scenario 1 [teaching case using Rule 9 and FAQ Q13]: an employee with an approved Hometown starts the outward journey on 28.12.2027 and returns on 04.01.2028. By Rule 9 the concession is counted against the block within which the outward journey commenced, which is the sub-block 2026-27. Ledger SCEN-B2, R9.",
             SKY,
             "Scenario ek. Employee 28 December 2027 ko outward journey shuru karta hai aur 4 January 2028 ko wapas aata hai. Rule 9 ke hisaab se ginti outward journey ke block mein hogi, yaani sub-block 2026-27, na ki 2028-29."),
            ("SCENARIO 2: UNUSED 2026-27 LTC",
             "Hometown holder did not travel in 2026-27: the unavailed LTC can still be used in the first year of the next sub-block, 2028.",
             "Scenario 2 [teaching case using Rule 10 and FAQ Q16]: the unavailed LTC of 2026-27 may be availed within the first year of the next sub-block, calendar year 2028, along with the fresh LTC of 2028-29. Ledger SCEN-B2, R10, FAQ-Q16.",
             GREEN,
             "Scenario do. Hometown wale employee ne 2026-27 mein LTC nahi li. Wo unavailed LTC agle sub-block ke pehle saal, yaani 2028 mein, 2028-29 ki apni LTC ke saath li ja sakti hai. Doosre saal 2029 mein nahi."),
            ("SCENARIO 3: SAME HQ AND HOMETOWN",
             "Posted at Pune, Hometown Pune: no Hometown LTC; one Any Place LTC in 2026-29, and in 2026 an unavailed one of 2022-25 can also be taken.",
             "Scenario 3 [teaching case using FAQ Q14, Q17 and Q19]: Headquarters and Home Town are the same, so Hometown LTC is not admissible; the employee has one Any Place in India LTC in block 2026-29, and in calendar year 2026 can also use one unavailed LTC of block 2022-25 (FAQ Q17 Case 2). Ledger SCEN-B2.",
             ORANGE,
             "Scenario teen. Posting Pune, Hometown bhi Pune. Hometown LTC nahi milegi. 2026 se 2029 ke block mein ek any place LTC milti hai, aur 2026 mein agar 2022-25 wali LTC bachi ho to wo bhi li ja sakti hai."),
            ("SCENARIO 4: THE EARLY JOURNEY",
             "Joined 15.03.2026. Spouse travels on 20.12.2026: gate not met. The same journey on 20.03.2027 passes the one-year test.",
             "Scenario 4 [teaching case using Rule 7(1)]: the one-year continuous service gate is tested on the date of journey; for an employee who joined on 15.03.2026 it is met only from 15.03.2027. Fresh-recruit special cycles are taught in Batch 3. Ledger SCEN-B2, R7(1).",
             RED,
             "Scenario chaar. Employee ne 15 March 2026 ko join kiya. Spouse 20 December 2026 ko jati hai, to gate nahi khula. Wahi journey 20 March 2027 ko ho to ek saal ka test pass hota hai. Fresh recruit ka special cycle Batch 3 mein padhenge."),
        ],
        "hook": "REMEMBER: test the gate, find the block by the outward journey, then check carry-over!",
        "hook_say": "Yaad rakhiye: pehle gate dekhiye, phir outward journey se block, aur phir carry-over.",
        "covers": ["SCEN-B2", "R9-11-TRAPS", "R8-TRAP"],
    },
    {
        "id": "b2_11_recap_drill",
        "chapter": "CHAPTER 11 • BATCH 2 RECAP AND RAPID-FIRE DRILL",
        "title": "RECAP — RULES 7 TO 11 IN FIVE CARDS, AND THE TOP TRAPS",
        "accent": SKY, "badge": "RECAP",
        "q": "Can you recall Rules 7 to 11 in one go?",
        "q_say": "Sir, ab poore Batch 2 ka quick recap ek saath ho jaye, aur sabse zyada poochhe jaane wale traps bhi.",
        "boxes": [
            ("RULE 7",
             "One year continuous service on the date of journey. Any leave incl. CL and SCL. No weekend-only. Family-only travel needs no leave.",
             "Recap: Rule 7(1) one year continuous service on the date of journey, categories (i) and (iii); Rule 7(2) any leave including casual and special casual leave; Notes: vacation, class at the time of journey, inform and prove, service record; weekend not allowed; CCL and study leave allowed; technical resignation within 8 years; Hometown outside India with limited assistance. Ledger RECAP-B2.",
             SKY,
             "Recap ek, Rule 7. Journey ki date par ek saal ki continuous service. Koi bhi leave, casual aur special casual bhi. Sirf weekend nahi. Sirf Family jaye to leave zaroori nahi. Notes mein vacation, class, inform aur prove, aur service record."),
            ("RULE 8",
             "Hometown: 2-year sub-block. Any place: 4-year block, in lieu of Hometown LTC. Family at Hometown: yearly self-only visit.",
             "Recap: Rule 8(a) Hometown LTC once in a two-year block irrespective of distance; Rule 8(b) any place once in a four-year block, in lieu of and adjusted against Hometown LTC under the proviso; Rule 8(c) yearly self-only visit in lieu of all concessions. Ledger RECAP-B2.",
             GREEN,
             "Recap do, Rule 8. Hometown LTC do saal ke block mein. Any place LTC chaar saal ke block mein, aur Hometown LTC ke badle mein adjust. Aur agar Family Hometown par rehti hai to har saal sirf self ki visit, baaki saari concessions ke badle."),
            ("BLOCK YEARS",
             "Block 2026-29, sub-blocks 2026-27 and 2028-29. Same HQ and Hometown: no Hometown LTC. Extension by one year. Two LTCs only in a first year.",
             "Recap: block year of four calendar years; Hometown holders have two two-year sub-blocks with option 1 or option 2; blocks and sub-blocks extend by one year; same HQ and Hometown: one any-place LTC per block and no Hometown LTC; NCR towns outside Delhi do not count as Delhi; two LTCs in the first year only. Ledger RECAP-B2.",
             ORANGE,
             "Recap teen, block years. Block 2026-29, sub-blocks 2026-27 aur 2028-29. Same Headquarters aur Hometown to Hometown LTC nahi. Ek saal ka extension. Do LTC sirf pehle saal mein."),
            ("RULES 9 TO 11",
             "Outward journey decides the block. Carry over to the first year of the next block. Hometown link on any-place carry-forward (flagged). Different places allowed.",
             "Recap: Rule 9 counting by the outward journey, different groups allowed; Rule 10 carry over within the first year of the next block, with the Hometown link for the any-place carry-forward; Rule 11 each member may visit different places. Ledger RECAP-B2.",
             BLUE,
             "Recap char. Rule 9 outward journey se block. Rule 10 agle block ke pehle saal mein carry-over, Hometown wale ke liye link ke saath, jo flagged hai. Rule 11 mein har member ki alag jagah."),
            ("TOP FIVE TRAPS",
             "1) Gate tested on date of journey. 2) Weekend alone: no. 3) Outward journey fixes the block. 4) Same HQ and Hometown: no Hometown LTC. 5) Carry over: first year only.",
             "Top five traps: (1) the one-year gate is tested on the date of journey, including Family journeys; (2) weekends or holidays alone do not qualify without leave; (3) the outward journey fixes the block even if the return falls later; (4) when Headquarters and Hometown are the same, no Hometown LTC; (5) carry-over is limited to the first year of the next block. Ledger RECAP-B2.",
             RED,
             "Top paanch traps. Ek, gate journey ki date par. Do, sirf weekend se LTC nahi. Teen, outward journey block tay karti hai. Char, Headquarters aur Hometown same to Hometown LTC nahi. Paanch, carry-over sirf pehle saal mein. Agle batch mein special categories aur fresh recruits aayenge."),
        ],
        "hook": "REMEMBER: gate on journey date • leave needed • outward journey fixes block • first-year carry-over only!",
        "hook_say": "Yaad rakhiye: gate journey ki date par, leave zaroori, outward journey se block, aur carry-over sirf pehle saal mein.",
        "covers": ["RECAP-B2"],
    },
    {
        "id": "b2_12_mcq_drill_a",
        "chapter": "CHAPTER 12 • MCQ DRILL A: RULES 7 AND 8",
        "title": "MCQ DRILL A — THINK FIRST, THEN LISTEN TO THE ANSWER",
        "accent": ORANGE, "badge": "MCQ A",
        "q": "Can you answer four MCQs on Rules 7 and 8 before I reveal the answer?",
        "q_say": "Sir, ab main khud jawab dene ki koshish karunga. Pehle MCQ aaye, phir answer.",
        "think_gap": 4.0,
        "boxes": [
            ("MCQ 1: WHEN IS THE GATE TESTED?",
             "The one-year service gate of Rule 7(1) is tested on? A) date of application  B) date of journey  C) date of joining ## ANS: B.",
             "Source: Rule 7(1) [VERIFIED in the Guidelines]: one year's continuous service on the date of journey performed by him or his family. Ledger V2-MCQ-A.",
             SKY,
             "MCQ ek. Rule 7 sub rule 1 ka ek saal ka gate kis date par dekha jata hai? Option A, application ki date. Option B, journey ki date. Option C, joining ki date. Pause kijiye. || Jawab option B. Journey ki date par."),
            ("MCQ 2: WHICH LEAVE?",
             "Which leave can be used for LTC? A) only earned leave  B) any leave incl. CL, SCL, child care leave  C) only half pay leave ## ANS: B.",
             "Source: Rule 7(2) and FAQ Q25 [VERIFIED]. Ledger V2-MCQ-A.",
             GREEN,
             "MCQ do. LTC ke liye kaun si leave chalti hai? Option A, sirf earned leave. Option B, koi bhi leave, casual, special casual aur child care leave bhi. Option C, sirf half pay leave. Pause kijiye. || Jawab option B. Koi bhi leave."),
            ("MCQ 3: HOMETOWN LTC BLOCK",
             "Hometown LTC under Rule 8(a) is admissible once in a block of? A) one year  B) two calendar years  C) four calendar years ## ANS: B.",
             "Source: Rule 8(a) [VERIFIED in the Guidelines]. Ledger V2-MCQ-A.",
             ORANGE,
             "MCQ teen. Rule 8 clause a ke hisaab se Hometown LTC kitne saal ke block mein ek baar? Option A, ek saal. Option B, do calendar years. Option C, chaar calendar years. Pause kijiye. || Jawab option B. Do calendar years."),
            ("MCQ 4: FAMILY AT HOMETOWN",
             "Family lives at his Hometown. Rule 8(c) lets him choose? A) a yearly visit for self only, in lieu of all concessions  B) two visits in a block  C) nothing ## ANS: A.",
             "Source: Rule 8(c) [VERIFIED]. Ledger V2-MCQ-A.",
             RED,
             "MCQ chaar. Family Hometown par rehti hai. Rule 8 clause c kya choose karne deti hai? Option A, har saal sirf self ke liye visit, baaki saari concessions ke badle. Option B, block mein do visit. Option C, kuch nahi. Pause kijiye. || Jawab option A."),
        ],
        "hook": "REMEMBER: attempt first, reveal second — that is how recall is built!",
        "hook_say": "Yaad rakhiye: pehle khud koshish kijiye, phir answer suniye. Isi se yaad pakka hota hai.",
        "covers": ["V2-MCQ-A"],
    },
    {
        "id": "b2_13_mcq_drill_b",
        "chapter": "CHAPTER 13 • MCQ DRILL B: BLOCK YEARS, COUNTING AND CARRY-OVER",
        "title": "MCQ DRILL B — BLOCKS, COUNTING, CARRY-OVER",
        "accent": GREEN, "badge": "MCQ B",
        "q": "Can you answer four more MCQs on blocks, counting and carry-over?",
        "q_say": "Sir, ab block years, counting aur carry-over par chaar MCQ ho jayein.",
        "think_gap": 4.0,
        "boxes": [
            ("MCQ 5: THE RUNNING BLOCK",
             "On 28.10.2026 the running four-year block is? A) 2022-25  B) 2026-29  C) 2027-30 ## ANS: B (derived from the FAQ tables; flagged).",
             "Source: FAQ Q13 Table-1 lists 2022-25 then 2026-29; derivation flagged. Ledger V2-MCQ-B.",
             SKY,
             "MCQ paanch. 28 October 2026 ko chalta hua chaar saal ka block kaun sa hai? Option A, 2022 se 25. Option B, 2026 se 29. Option C, 2027 se 30. Pause kijiye. || Jawab option B, 2026 se 29. Ye FAQ ke tables se nikala hua hai, flagged derivation."),
            ("MCQ 6: COUNTING",
             "Outward 28.12.2027, return 04.01.2028 counts against? A) block of the return journey  B) block of the outward journey  C) both blocks ## ANS: B.",
             "Source: Rule 9 [VERIFIED]. Ledger V2-MCQ-B.",
             GREEN,
             "MCQ chhe. Outward 28 December 2027, return 4 January 2028, to ginti kis block mein hogi? Option A, return wale block mein. Option B, outward wale block mein. Option C, dono mein. Pause kijiye. || Jawab option B. Outward journey wale block mein."),
            ("MCQ 7: SAME HQ AND HOMETOWN",
             "Same HQ and Hometown: which LTC is admissible? A) Hometown LTC  B) one Any Place LTC per four-year block  C) both ## ANS: B.",
             "Source: FAQ Q14 and Q19 [VERIFIED]. Ledger V2-MCQ-B.",
             ORANGE,
             "MCQ saat. Headquarters aur Hometown ek hi jagah ho to kaun si LTC milti hai? Option A, Hometown LTC. Option B, chaar saal ke block mein ek any place LTC. Option C, dono. Pause kijiye. || Jawab option B."),
            ("MCQ 8: CARRY-OVER WINDOW",
             "An unavailed LTC can be availed within? A) the first year of the next block  B) any year of the next block  C) two years after ## ANS: A.",
             "Source: Rule 10 [VERIFIED]. Ledger V2-MCQ-B.",
             RED,
             "MCQ aath. Unavailed LTC kab tak li ja sakti hai? Option A, agle block ke pehle saal ke andar. Option B, agle block ke kisi bhi saal mein. Option C, do saal baad tak. Pause kijiye. || Jawab option A."),
        ],
        "hook": "REMEMBER: derive the block, count by the outward journey, carry over in year one!",
        "hook_say": "Yaad rakhiye: block nikaliye, outward journey se ginti kijiye, aur carry-over pehle saal mein.",
        "covers": ["V2-MCQ-B"],
    },
    {
        "id": "b2_14_flashcards",
        "chapter": "CHAPTER 14 • FLASHCARDS: RULES 7 TO 11 AT A GLANCE",
        "title": "FLASHCARDS — SAY THE ANSWER BEFORE IT APPEARS",
        "accent": PINK, "badge": "FLASHCARDS",
        "q": "Can I revise Rules 7 to 11 with quick flashcards?",
        "q_say": "Sir, ab quick flashcards se Rule 7 se 11 revise kar lete hain.",
        "think_gap": 3.0,
        "boxes": [
            ("CARD 1",
             "Which categories does Rule 7(1) name? ## ANS: clauses (i) and (iii) of Rule 1(3).",
             "Source: Rule 7(1) [VERIFIED in the Guidelines]. Ledger V2-FLASH.",
             SKY,
             "Card ek. Rule 7 sub rule 1 kaun si categories ka naam leta hai? || Jawab. Rule 1 sub rule 3 ki clause i aur clause iii."),
            ("CARD 2",
             "Technical resignation: within how many years is the person treated as a fresh recruit? ## ANS: within 8 years of appointment.",
             "Source: Rule 7 Note 4 [VERIFIED; rest of the 2016 O.M. not read]. Ledger V2-FLASH.",
             GREEN,
             "Card do. Technical resignation mein kitne saal ke andar fresh recruit maana jata hai? || Jawab. Appointment se aath saal ke andar."),
            ("CARD 3",
             "Rule 8(b) proviso? ## ANS: any-place LTC is in lieu of, and adjusted against, the Hometown LTC available at the start.",
             "Source: proviso to Rule 8(b) [VERIFIED]. Ledger V2-FLASH.",
             ORANGE,
             "Card teen. Rule 8 clause b ka proviso kya kehta hai? || Jawab. Any place LTC Hometown LTC ke badle mein hai aur usi ke against adjust hoti hai."),
            ("CARD 4",
             "NCR rule (FAQ Q20)? ## ANS: towns of other NCR States are not Delhi headquarters, so Hometown LTC is allowed.",
             "Source: FAQ Q20 [VERIFIED]. Ledger V2-FLASH.",
             RED,
             "Card chaar. NCR ke baare mein Q20 kya kehta hai? || Jawab. Doosre NCR states ke shehar Delhi headquarters nahi maane jaate, to wahan ke Hometown par Hometown LTC allowed hai."),
            ("CARD 5",
             "Rule 11 in one line? ## ANS: employee and each Family member may visit different places; family need not follow the employee's place.",
             "Source: Rule 11 [VERIFIED]. Ledger V2-FLASH.",
             PINK,
             "Card paanch. Rule 11 ek line mein? || Jawab. Employee aur Family ka har member alag alag jagah ja sakta hai."),
        ],
        "hook": "REMEMBER: revise the cards you missed — retrieval beats re-reading!",
        "hook_say": "Yaad rakhiye: jo cards galat hue, unhe dobara revise kijiye. Dobara yaad karna, sirf dobara padhne se behtar hota hai.",
        "covers": ["V2-FLASH"],
    },
    {
        "id": "b2_15_end_card",
        "chapter": "CHAPTER 15 • END CARD: NEXT BATCH AND IMPORTANT NOTICE",
        "title": "END OF BATCH 2 — WHAT COMES NEXT",
        "accent": SKY, "badge": "END",
        "q": "What is next, and what should I do before the next batch?",
        "q_say": "Sir, Batch 2 poora hua. Ab aage kya hai?",
        "boxes": [
            ("NEXT: BATCH 3",
             "Special categories under the Notes: deputation, training, PSU, NER options, fresh recruits, spouses, escort, suspension.",
             "Roadmap: Batch 3 covers the Notes 6 to 17 printed after Rule 7 in the Guidelines plus the fresh-recruit FAQs Q64 to Q70. Later batches: Rule 12 entitlements, air travel and Rule 13, the Special Dispensation Scheme, Rules 14 and 15, Rules 16 to 19. Ledger V2-END.",
             SKY,
             "Agla batch Batch 3 hai. Isme special categories aayengi: deputation, training, PSU, NER ke options, fresh recruits, dono spouses Government servant, escort aur suspension."),
            ("BEFORE YOU MOVE ON",
             "Redo the MCQs and flashcards you missed. Then revisit the chapters that carry flags.",
             "Learning loop: attempt, check, revisit weak items first, then move on. Ledger V2-END.",
             GREEN,
             "Aage badhne se pehle jo MCQ aur flashcards galat hue unhe dobara kijiye, aur jin chapters mein flag laga tha unhe ek baar aur dekh lijiye."),
            ("IMPORTANT NOTICE",
             "Learning aid, not legal advice. The DoPT order governs. Flagged items: quote the official text.",
             "Notice: this video is an educational aid. The text of the Rules and the DoPT orders governs; items flagged as not verified (see script header) should be checked against the official order before relying on them. Ledger V2-END.",
             ORANGE,
             "Ek zaroori baat. Ye video padhai ka saadhan hai, legal advice nahi. Rules ka text aur DoPT ka order hi final hai. Jin items par flag hai, unka official text dekh kar hi use kijiye."),
        ],
        "hook": "THANK YOU! Batch 3 next: special categories. Pause, practise, and see you there!",
        "hook_say": "Dhanyavaad dosto! Agle batch mein special categories par milte hain. Tab tak practise kijiye.",
        "covers": ["V2-END"],
    },
]

FLOWS = {}

# Thirds for --part 1, 2, 3
PART_STARTS = ["b2_00_title_card", "b2_05_rule8_types", "b2_09_rule9_10_11"]

MANIFEST = {
    "R7(1)": "Rule 7(1) one year", "R7(1)-CAT": "categories (i) and (iii)", "R7(1)-DATE": "date of journey", "R7(2)": "Rule 7(2) leave",
    "R7-N1(i)": "vacation department", "R7-N1(ii)": "class at time of journey", "R7-N1(iii)": "inform Controlling Officer", "R7-N1(iv)": "service record entry",
    "R7-N2": "weekend holidays", "R7-N3": "CCL and study leave", "R7-N4": "technical resignation", "R7-N5": "hometown outside India", "R7-LEAVE-FAQ": "FAQ Q25 to Q27",
    "R8(a)": "Rule 8(a) hometown", "R8(b)": "Rule 8(b) any place", "R8(b)-PROV": "Rule 8(b) proviso", "R8(c)": "Rule 8(c) yearly self visit", "R8-TRAP": "Rule 8 traps",
    "FAQ-Q25": "FAQ Q25", "FAQ-Q26": "FAQ Q26", "FAQ-Q27": "FAQ Q27", "FAQ-Q13": "FAQ Q13 block year", "FAQ-Q14": "FAQ Q14", "FAQ-Q15": "FAQ Q15", "FAQ-Q16": "FAQ Q16", "FAQ-Q17": "FAQ Q17", "FAQ-Q18": "FAQ Q18", "FAQ-Q19": "FAQ Q19", "FAQ-Q20": "FAQ Q20",
    "BLOCK-NOW": "block 2026-29 derivation",
    "R9": "Rule 9 counting", "R10": "Rule 10 carry-over", "R10-HT-LINK": "Rule 10 hometown link", "R11": "Rule 11 places", "R9-11-TRAPS": "Rules 9 to 11 traps",
    "SCEN-B2": "scenario bank",
    "RECAP-B2": "recap", "V2-TITLE": "title card", "V2-MCQ-A": "MCQ drill A", "V2-MCQ-B": "MCQ drill B", "V2-FLASH": "flashcards", "V2-END": "end card",
}

# ============================================================================
# INTEGRITY GUARDS (run on import)
# ============================================================================
assert len({s["id"] for s in SCENES}) == len(SCENES), "duplicate scene id"
_DEVANAGARI = re.compile('[' + chr(0x0900) + '-' + chr(0x097F) + ']')


def _walk_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _walk_strings(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from _walk_strings(v)


for _s in _walk_strings(SCENES):
    assert not _DEVANAGARI.search(_s), f"Devanagari script found (Roman Hinglish only): {_s[:70]!r}"

FULL = {}
for _sc_ in SCENES:
    _new, _seen = [], set()
    for (_t, _short, _full, _c, _n) in _sc_["boxes"]:
        assert _t not in _seen, f"duplicate card title in {_sc_['id']}: {_t}"
        _seen.add(_t)
        FULL[(_sc_["id"], _t)] = _full
        _new.append((_t, _short, _c, _n))
    _sc_["boxes"] = _new


def evidence_tag(full: str) -> str:
    """Zero-hallucination tag per card, derived from the verification marks inside its full text.
    KNOWN = read on the bare act / DoPT Guidelines / FAQ copy; UNKNOWN = a flagged part could not be confirmed;
    INFERRED = taught from the study guide or a secondary page only (no [VERIFIED] mark)."""
    has_v = "[VERIFIED" in full or "[KNOWN" in full
    has_u = "UNVERIFIED" in full or "not confirmed" in full.lower() or "could not be confirmed" in full.lower()
    if has_v and has_u:
        return "KNOWN + UNKNOWN (flagged part)"
    if has_u:
        return "UNKNOWN (flagged)"
    if has_v:
        return "KNOWN"
    return "INFERRED (study guide / teaching construct)"


def write_reference_sheet():
    counts = {}
    for sc in SCENES:
        for (t, _b, _c, _n) in sc["boxes"]:
            k = evidence_tag(FULL[(sc["id"], t)])
            counts[k] = counts.get(k, 0) + 1
    out = ["# CCS (LTC) Rules 1988 - Batch 2 - full-wording reference sheet", "",
           "Every card on screen is a short key-point; the full wording, citations and verification status of each card are listed here.",
           "Evidence tags: KNOWN = read on the bare act / DoPT Guidelines / FAQ copy; UNKNOWN (flagged) = could not be confirmed, quote the official text in an answer; "
           "INFERRED = taught from the study guide or a teaching construct with no [VERIFIED] mark.", "",
           "Evidence summary: " + "; ".join(f"{k}: {v} cards" for k, v in sorted(counts.items())), ""]
    for sc in SCENES:
        out += [f"## {sc['chapter']}", f"**{sc['title']}**  ({sc['badge']})", "", f"Q: {sc['q']}", ""]
        for (t, _b, _c, _n) in sc["boxes"]:
            out += [f"### {t}", f"Evidence: {evidence_tag(FULL[(sc['id'], t)])}", "", FULL[(sc["id"], t)], ""]
        out += [f"> {sc['hook']}", ""]
    Path("ltc_b2_reference_sheet.md").write_text("\n".join(out), encoding="utf-8")


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


def card_body(body, hide_answer=False):
    """Drill cards store 'cue ## answer'. While the cue is being read only the cue shows; afterwards both show."""
    if "##" not in body:
        return body
    cue, ans = body.split("##", 1)
    return cue.strip() if hide_answer else cue.strip() + "  >>  " + ans.strip()


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
    f_ch, l_ch, _, _ = fit_block(d, scene["chapter"], True, 1500, 30, 22, 18, 1.1)
    d.text((80, 34), l_ch[0], font=f_ch, fill=ORANGE)
    f_t, l_t, _, _ = fit_block(d, scene["title"], True, 1440, 50, 40, 22, 1.1)
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
    chip, chip_col = ((f"{STUDENT_NAME} ASKS (Student)", YELLOW) if kind == "question" else ("THE TEACHER EXPLAINS", GREEN))
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
        newest = (i == reveal - 1) and kind in ("answer", "answer_q")
        c = col if newest or kind in ("hook",) else dim(col, 0.8)
        if newest:
            d.rounded_rectangle([x - 6, y - 6, x + w + 6, y + h + 6], radius=20, outline=YELLOW, width=4)
        d.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=CARD_BG, outline=c, width=3 if newest else 2)
        d.rectangle([x, y + 8, x + 12, y + h - 8], fill=c)
        f_bt, l_bt, lh_bt, _ = fit_block(d, bt_, True, w - 60, 62, TITLE_START, TITLE_MIN, 1.15)
        for k, ln in enumerate(l_bt):
            d.text((x + 32, y + 16 + k * lh_bt), ln, font=f_bt, fill=c)
        body_top = y + 16 + len(l_bt) * lh_bt + 10
        body = card_body(body, hide_answer=(newest and kind == "answer_q"))
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
        try:
            fit_block(d, sc["chapter"], True, 1500, 30, 22, 18, 1.1)
            fit_block(d, sc["title"], True, 1440, 50, 40, 22, 1.1)
            fit_block(d, sc["q"], True, 1250, 92, 38, 22, 1.22)
        except ValueError as e:
            bad += 1
            print(f"{sc['id']}: HEADER FAIL {e}")
        for (t, body, _c, _n), (x, y, w, h) in zip(sc["boxes"], card_boxes(sc)):
            try:
                _, l_bt, lh_bt, ts = fit_block(d, t, True, w - 60, 62, TITLE_START, TITLE_MIN, 1.15)
                body_top = y + 16 + len(l_bt) * lh_bt + 10
                _, _, _, bs = fit_block(d, card_body(body), False, w - 60, y + h - body_top - 14, BODY_START, BODY_MIN, 1.25)
                flag = "" if bs >= 28 else "  (tight)"
                print(f"{sc['id'][:26]:26s} {t[:36]:36s} {ts:>4d} {bs:>4d}  {len(body):>4d}{flag}")
            except ValueError as e:
                bad += 1
                print(f"{sc['id'][:26]:26s} {t[:36]:36s}  FAIL  {e}")
        if "flow" in sc:
            try:
                im2, d2 = background()
                for (x, y, w, h, t, s, c, step) in FLOWS[sc["flow"]]["nodes"]:
                    draw_node(d2, x, y, w, h, t, s, c, False)
            except ValueError as e:
                bad += 1
                print(f"{sc['id']}: FLOW FAIL {e}")
        try:
            _, l_h, _, hs = fit_block(d, sc["hook"], True, W - 200, 36, 24, 20, 1.1)
            if len(l_h) > 1:
                raise ValueError("hook wraps")
        except ValueError:
            bad += 1
            print(f"{sc['id']}: HOOK does not fit on one line at >=20px ({len(sc['hook'])} chars)")
    print(f"\n{'ALL CARDS WITHIN BUDGET' if not bad else str(bad) + ' CARD(S) OVER BUDGET'}")
    return bad


_FLAG_WORDS = re.compile(r"(?i)unverif|flag|unconfirm|not confirm|confirm nahi|study guide|per guide|guide se|guide ke|guide ka|guide mein|reported|secondary|not read|not re-read|nahi padh|saaf nahi|gazette")


def audit_flags():
    """On-screen honesty lint: a card whose full text carries UNVERIFIED must also say so on screen (short text) and
    in the narration; and the unconfirmed 21 May date may only appear next to a 'guide'/'unconfirmed' qualifier."""
    bad = 0
    for sc in SCENES:
        for (t, short, _c, narr) in sc["boxes"]:
            full = FULL[(sc["id"], t)]
            if "UNVERIFIED" in full:
                if not _FLAG_WORDS.search(short):
                    bad += 1
                    print(f"  FLAG LINT: short text hides an UNVERIFIED flag: {sc['id']} / {t}")
                if not _FLAG_WORDS.search(narr):
                    bad += 1
                    print(f"  FLAG LINT: narration hides an UNVERIFIED flag: {sc['id']} / {t}")
            for txt, where in ((short, "short"), (narr, "narration")):
                if re.search(r"21 May|21\.05\.1988", txt) and not _FLAG_WORDS.search(txt):
                    bad += 1
                    print(f"  FLAG LINT: unconfirmed date 21 May stated flatly ({where}): {sc['id']} / {t}")
    print(f"\nFLAG LINT: {'clean' if not bad else str(bad) + ' problem(s)'}")
    return bad


def audit_coverage():
    """Every ID in MANIFEST must be covered by at least one scene. Returns the number of problems."""
    covered = set()
    for sc in SCENES:
        covered.update(sc.get("covers", []))
    missing = [k for k in MANIFEST if k not in covered]
    unknown = sorted(covered - set(MANIFEST))
    print(f"\nCOVERAGE: {len(MANIFEST) - len(missing)}/{len(MANIFEST)} manifest items covered across {len(SCENES)} chapters, "
          f"{sum(len(s['boxes']) for s in SCENES)} cards")
    for k in missing:
        print(f"  NOT COVERED: {k} ({MANIFEST[k]})")
    for k in unknown:
        print(f"  covered but not in manifest (add it): {k}")
    return len(missing) + len(unknown)


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
        if "||" in b[3]:
            q_part, a_part = [x.strip() for x in b[3].split("||", 1)]
            segs.append(("teacher", q_part, i + 1, "answer_q"))
            segs.append(("teacher", a_part, i + 1, "answer"))
        else:
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


def fmt_srt(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


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


def write_srt(cues, path: Path):
    out = []
    for i, (s, e, _style, txt) in enumerate(cues, 1):
        out += [str(i), f"{fmt_srt(s)} --> {fmt_srt(e)}", txt, ""]
    path.write_text("\n".join(out), encoding="utf-8")


def align_original(text, span_start, span_end):
    """Subtitles must show the ORIGINAL Roman Hinglish text (not the TTS-normalised text).
    Tokens are spread across the spoken span in proportion to their length."""
    toks = text.split()
    if not toks:
        return []
    weights = [len(t) + 1 for t in toks]
    total = float(sum(weights))
    out, acc = [], 0.0
    span = max(span_end - span_start, 0.2)
    for t, wgt in zip(toks, weights):
        s = span_start + span * acc / total
        acc += wgt
        out.append((t, s, span_start + span * acc / total))
    return out


def align_with_boundaries(text, boundaries, span_start, span_end):
    """Subtitles show the ORIGINAL Roman text, but timing comes from the real edge-tts WordBoundary events.
    Each original token is mapped onto the spoken-word timeline in proportion to its estimated spoken length
    (acronyms, dates and rule numbers are spoken as several words, so a plain token count would drift)."""
    toks = text.split()
    if not toks:
        return []
    if not boundaries or len(boundaries) < 2:
        return align_original(text, span_start, span_end)
    est = [max(1, len(normalize_for_tts(t).split())) for t in toks]
    total_est = float(sum(est))
    m = len(boundaries)
    out, acc = [], 0.0
    for t, e in zip(toks, est):
        i0 = min(m - 1, int(round(acc / total_est * m)))
        acc += e
        i1 = max(i0, min(m - 1, int(round(acc / total_est * m)) - 1))
        out.append((t, boundaries[i0][1], max(boundaries[i1][2], boundaries[i0][1] + 0.05)))
    return out


def make_cues(words, offset, style, chunk=8):
    cues, buf = [], []
    for w in words:
        buf.append(w)
        if len(buf) >= chunk or w[0].endswith((".", "?", "!", ":")):
            cues.append((offset + buf[0][1], offset + buf[-1][2] + 0.12, style, " ".join(x[0] for x in buf)))
            buf = []
    if buf:
        cues.append((offset + buf[0][1], offset + buf[-1][2] + 0.15, style, " ".join(x[0] for x in buf)))
    # never let one cue overlap the next (overlaps would stack two subtitle lines on screen)
    fixed = []
    for i, (s, e, st, tx) in enumerate(cues):
        if i + 1 < len(cues):
            e = min(e, cues[i + 1][0] - 0.01)
        fixed.append((s, max(e, s + 0.2), st, tx))
    return fixed


# ============================================================================
# MAIN
# ============================================================================
async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true", help="print card-density + coverage tables and exit (no ffmpeg needed)")
    ap.add_argument("--preview", action="store_true", help="render slides only")
    ap.add_argument("--no-tts", action="store_true", help="silent audio (offline layout/timing test)")
    ap.add_argument("--teacher", default=None, help="TTS voice name for the teacher segments (required for a full build)")
    ap.add_argument("--student", default=None, help="TTS voice name for the student segments (required for a full build)")
    ap.add_argument("--rate", default="+0%")
    ap.add_argument("--part", type=int, choices=[1, 2, 3], help="1..3 = first, middle, last third of the chapters")
    args = ap.parse_args()

    write_reference_sheet()
    if args.audit:
        bad = audit_density() + audit_coverage() + audit_flags()
        sys.exit(1 if bad else 0)
    if audit_density() or audit_coverage() or audit_flags():
        sys.exit("Build stopped: fix the over-dense cards / coverage gaps listed above.")

    for d in (BUILD_DIR, SLIDES_DIR, AUDIO_DIR):
        d.mkdir(parents=True, exist_ok=True)
    global SCENES, OUTPUT_MP4
    tag = ""
    if args.part:
        _idx = [next(i for i, x in enumerate(SCENES) if x["id"] == pid) for pid in PART_STARTS] + [len(SCENES)]
        SCENES = SCENES[_idx[args.part - 1]:_idx[args.part]]
        tag = f"_part{args.part}"
        OUTPUT_MP4 = Path(f"{OUT_STEM}{tag}.mp4")
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
    if not args.no_tts and not (args.teacher and args.student):
        sys.exit("ERROR: pass --teacher <voice> and --student <voice> for a full build (or use --no-tts for a silent test).")

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
    chapter_marks, seen_scene = [], set()
    for i, (si, who, text, kind, reveal, sp, mp3) in enumerate(jobs):
        if args.no_tts:
            sd = silent_audio(text, mp3)
            span = (0.0, sd)
        else:
            sd = probe_duration(mp3)
            wb = words_by_job[i]
            span = (wb[0][1], wb[-1][2]) if wb else (0.0, sd)
        dur = sd + (0.9 if kind in ("question", "hook") else 0.5)
        if kind == "answer_q":
            dur += SCENES[si].get("think_gap", 4.0)  # silent think-time: viewer answers before the reveal
        if si not in seen_scene:
            seen_scene.add(si)
            chapter_marks.append((cursor, SCENES[si]["chapter"]))
        clip = BUILD_DIR / f"clip_{i:03d}.mp4"
        subprocess.run([
            "ffmpeg", "-y", "-loop", "1", "-framerate", "5", "-i", str(sp), "-i", str(mp3),
            "-af", "apad", "-t", f"{dur:.3f}",
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-g", "60", "-r", "30", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(clip)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cues += make_cues(align_with_boundaries(text, None if args.no_tts else words_by_job[i], span[0], span[1]), cursor, "Student" if who == "student" else "Default")
        clips.append(clip)
        cursor += dur
    print(f"  {len(clips)} clips | timeline {cursor/60:.2f} min")

    srt_path = Path(f"{OUT_STEM}{tag}_subtitles_roman.srt")
    write_srt(cues, srt_path)
    chap_path = Path(f"{OUT_STEM}{tag}_chapters.txt")
    chap_path.write_text("\n".join(
        f"{int(t // 3600):02d}:{int((t % 3600) // 60):02d}:{int(t % 60):02d} {name.title()}" for t, name in chapter_marks) + "\n",
        encoding="utf-8")
    print(f"  wrote {srt_path} and {chap_path}")

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