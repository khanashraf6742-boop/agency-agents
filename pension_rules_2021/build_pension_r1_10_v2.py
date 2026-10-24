#!/usr/bin/env python3
"""
CCS (Pension) Rules 2021 - BATCH 1 - Rules 1 to 10
"CITY HINGLISH" EXPLAINER COMPILER - screenshot-style row cards + tables, 26 chapters
=====================================================================================
WHAT CHANGED FROM THE OLD SCRIPT (v1 -> v2)
  * VISUAL: every chapter is now a full-width ROW-CARD slide in the house style of the
    reference screenshot - top module bar, section banner, big title, 4 anchor chips,
    one bordered row per rule / sub-rule / proviso, a yellow TRAP strip at the bottom,
    and the segmented progress bar.  No more 2x2 boxes.
  * LANGUAGE: on-screen text is ENGLISH (plain, city English).  Narration is HINGLISH
    written in ROMAN script only - no Devanagari anywhere in this file.
  * COVERAGE: 20 audit gaps closed - Rule 1 preamble (Art. 309 proviso + Art. 148(5)),
    Rule 2 Explanation limb (2) condition, Rule 6(2) four pension categories,
    Rule 7(1)(b) minimum-pension proviso, Rule 7(4)(c) duplicate undertaking,
    Rule 8(2)(d) full-enquiry bar, Rule 8(4)(d) "contemplated only" case,
    Rule 8(5) no-recovery rule, Rule 9 Explanation (a)(i) definition of commercial
    employment, Rule 9 Explanation (a)(ii)(A)-(C) practice/consultancy,
    Rule 9 Explanation (b) date of retirement on re-employment, the two Rule 9(3)
    Explanations, Rule 9(6)(ii)-(iv), Rule 9(7) proviso, Rule 9(8) provisos + factors,
    Rule 9(9) communication, Rule 10(1) "such longer period", the Rule 8 sub-rule (9)
    cross-reference anomaly, and the NPS gateway confirmation.
  * TABLES: Rule 2 exclusions, Rule 7 vs Rule 8, amendments, and a time-limit bar chart.

SOURCES USED FOR THE AUDIT (read 24.10.2026)
  * Gazette text of G.S.R. 868(E) of 20.12.2021 - Rules 1 to 10 read sub-rule by sub-rule
  * Form 1, Form 2, Form 3 of the Rules (commercial employment / checklist / nomination)
  * G.S.R. 770(E) of 07.10.2022, G.S.R. 410(E) of 16.07.2024, G.S.R. 340(E) of 22.05.2025
  * DoPPW O.M. of 22.06.2026 (compassionate appointments - crucial date)
  * DoPPW O.M. of 30.10.2025 and 29.10.2025 (Rule 5 restatement, autonomous bodies)

USAGE
    python build_pension_r1_10_v2.py --audit      # density check + coverage check, no ffmpeg
    python build_pension_r1_10_v2.py --preview    # slides only (PNG)
    python build_pension_r1_10_v2.py --no-tts     # silent timing test, needs ffmpeg
    python build_pension_r1_10_v2.py --part 2     # chapters 10-17 only
    python build_pension_r1_10_v2.py              # full build (edge-tts + ffmpeg with libass)
NOTES
  * Every row carries a FLAG word (EXAM / TRAP / FLAG / NEW) that is drawn as a small pill.
  * "--audit" fails if any row needs a font below the density floor, so a card can never
    silently shrink into unreadable text.
"""
import argparse
import asyncio
import math
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

# ============================================================================
# CANVAS / PATHS / HOUSE PALETTE
# ============================================================================
W, H = 1920, 1080
BUILD_DIR = Path("pension_b1_build")


def _resolve_ffmpeg():
    """FFMPEG_BIN / PATH / the binary bundled inside the imageio-ffmpeg wheel."""
    env = os.environ.get("FFMPEG_BIN")
    if env and Path(env).exists():
        return env
    found = shutil.which("ffmpeg")
    if found:
        return found
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def _resolve_ffprobe():
    env = os.environ.get("FFPROBE_BIN")
    if env and Path(env).exists():
        return env
    return shutil.which("ffprobe")


FFMPEG = _resolve_ffmpeg()
FFPROBE = _resolve_ffprobe()
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
OUT_STEM = "pension_b1_rules_1_to_10_city_hinglish"
OUTPUT_MP4 = Path(OUT_STEM + ".mp4")

TOP_BAR_H = 56
BANNER_Y = 66
TITLE_Y = 104
CHIP_Y = 168
CHIP_H = 104
ROWS_Y = 294
ROWS_BOTTOM = 930
TRAP_Y0, TRAP_Y1 = 944, 1004
PROG_Y = 1016

ROW_X0, ROW_X1 = 48, W - 48
LABEL_X = ROW_X0 + 26
LABEL_W = 320
BODY_X = ROW_X0 + 26 + LABEL_W + 34
BODY_W = ROW_X1 - 34 - BODY_X

# Density budget (px). --audit fails below these.
TITLE_START, TITLE_MIN = 27, 21
BODY_START, BODY_MIN = 27, 21
CHIP_T_START, CHIP_T_MIN = 27, 21
CHIP_S_START, CHIP_S_MIN = 17, 14
TRAP_START, TRAP_MIN = 24, 18
TABLE_START, TABLE_MIN = 23, 17

BG_TOP = (8, 12, 26)
BG_BOT = (16, 22, 44)
CARD_BG = (19, 27, 49)
CARD_BG_ALT = (23, 32, 57)
TEXT_WHITE = (241, 245, 252)
MUTED = (146, 162, 190)
DIM = (96, 110, 138)
ORANGE = (232, 158, 40)
GREEN = (42, 178, 140)
BLUE = (74, 134, 232)
SKY = (96, 190, 232)
RED = (226, 96, 96)
YELLOW = (240, 208, 74)
PINK = (210, 132, 186)
PURPLE = (166, 132, 232)

DEFAULT_TEACHER = "en-IN-PrabhatNeural"
DEFAULT_STUDENT = "en-IN-NeerjaNeural"
BATCH_LABEL = "BATCH 1 / RULES 1-10"
DRAFT_LABEL = "DRAFT 24 OCT 2026"
VOICE_LABEL = "STUDIO VOICE - 40   CITY HINGLISH"

# ============================================================================
# TTS NORMALISATION - Hinglish narration, Roman script only
# Longest patterns first, otherwise "Rule 8(2)(c)(ii)" would be eaten by "Rule 8(2)".
# ============================================================================
_TTS_FIXES = [
    (r'\bG\.S\.R\.\s*(\d+)\(E\)', r'G.S.R. \1 E'),
    (r'\bG\.S\.R\.', 'G.S.R.'),
    (r'\bUPSC\b', 'U.P.S.C.'), (r'\bCAG\b', 'C.A.G.'), (r'C&AG', 'C.A.G.'),
    (r'\bDoPPW\b', 'D.O.P.P.W.'), (r'\bDoPT\b', 'D.O.P.T.'), (r'\bDoE\b', 'D.O.E.'),
    (r'\bCCS\b', 'C.C.S.'), (r'\bCCA\b', 'C.C.A.'), (r'\bCPF\b', 'C.P.F.'),
    (r'\bNPS\b', 'N.P.S.'), (r'\bAIS\b', 'A.I.S.'), (r'\bPSU\b', 'P.S.U.'),
    (r'\bIAS\b', 'I.A.S.'), (r'\bIPS\b', 'I.P.S.'), (r'\bIPS\b', 'I.P.S.'),
    (r'\bO\.M\.', 'O.M.'), (r'\bRTI\b', 'R.T.I.'), (r'\bJCM\b', 'J.C.M.'),
    (r'\bDR\b', 'D.R.'), (r'w\.e\.f\.', 'with effect from'), (r'\bRs\.\s*', 'Rupees '),
    (r'\s*%', ' per cent'), (r'\bNo\.\s*(\d)', r'number \1'), (r'\bHoO\b', 'Head of Office'), (r'\bHoD\b', 'Head of Department'),
    (r'\bPPO\b', 'P.P.O.'), (r'\bDFPR\b', 'D.F.P.R.'),
    (r'Rule\s+(\d+)\((\d+)\)\(([a-z]+)\)\(([ivx]+)\)', r'Rule \1, sub rule \2, clause \3, sub clause \4'),
    (r'Rule\s+(\d+)\((\d+)\)\(([a-z]+|[ivx]+)\)', r'Rule \1, sub rule \2, clause \3'),
    (r'Rule\s+(\d+)\(([a-z])\)', r'Rule \1, clause \2'),
    (r'Rule\s+(\d+)\((\d+)\)', r'Rule \1, sub rule \2'),
    (r'\bsub-rules\b', 'sub rules'), (r'\bsub-rule\b', 'sub rule'),
    (r'[\u2014\u2013]', ','),
]


def normalize_for_tts(text: str) -> str:
    for pat, rep in _TTS_FIXES:
        text = re.sub(pat, rep, text)
    return re.sub(r'[ \t]+', ' ', text).strip()


# ============================================================================
# CONTENT
# scene = dict(id, chapter, title, badge, chips, q, q_say, rows | table, trap, trap_say)
# rows  = (label, english_on_screen, hinglish_narration, colour, flag)
# flag  = "" | "EXAM" | "TRAP" | "FLAG" | "NEW"   (drawn as a small pill)
# table = dict(cols=[...], widths=[...], rows=[[...]], note="...")  -> kind="table"
# bars  = dict(items=[(label, value, max, display)], unit="")       -> kind="bars"
# ============================================================================
SCENES = [
    {
        "id": "c01_rule1",
        "chapter": "CHAPTER 1 - PRELIMINARY - RULE 1: ENABLING POWER, NAME AND COMMENCEMENT",
        "title": "Rule 1 - Where the Power Comes From, What These Rules Are Called, When They Start",
        "badge": "RULE 1",
        "chips": [("Art. 309", "proviso = rule-making power", RED),
                  ("Art. 148(5)", "C&AG consulted for IA&AD", ORANGE),
                  ("G.S.R. 868(E)", "20.12.2021 base notification", BLUE),
                  ("Rule 87", "repeal of the 1972 rules", GREEN)],
        "q": "Where does the power to make these rules come from, what are they called, and from which day do they apply?",
        "q_say": "Sir, ye rules banane ki power kahan se aayi, naam kya hai, aur kab se applicable hain?",
        "rows": [
            ("THE ENABLING POWER", "Proviso to Article 309 and Article 148(5): the President makes these rules, and the C&AG is consulted for the Indian Audit and Accounts Department.", "Sabse pehle power ka source. Article 309 ka proviso President ko rule banane ki power deta hai. Article 148 clause 5 kehta hai ki Indian Audit and Accounts Department ke staff ke liye CAG se consultation zaroori hai.", RED, "EXAM"),
            ("RULE 1(1) - THE NAME", "Central Civil Services (Pension) Rules, 2021. Short form: CCS (Pension) Rules, 2021. One rule book replaces the scattered 1972 instructions.", "Rule 1 sub rule 1 naam deta hai: Central Civil Services Pension Rules, two thousand twenty one. Short mein CCS Pension Rules 2021. Pension matlab retirement ke baad har mahine milne wala paisa.", ORANGE, ""),
            ("RULE 1(2) - THE START", "They come into force with effect from the date of publication in the Official Gazette - 20.12.2021. No later appointed day has to be waited for.", "Rule 1 sub rule 2 bolta hai: jis din Official Gazette mein chhape, usi din se lagu. Gazette government ka official notice hai. Yahan woh date hai twenty December two thousand twenty one.", BLUE, "EXAM"),
            ("THE BASE NOTIFICATION", "G.S.R. 868(E), dated 20.12.2021, Ministry of Personnel, Public Grievances and Pensions, Department of Pension and Pensioners Welfare.", "Base notification hai G.S.R. eight six eight E, twenty December two thousand twenty one. G.S.R. Gazette ka serial number hai. Har amendment apni pehli line mein yahi number repeat karta hai, isliye ise yaad rakho.", GREEN, ""),
            ("RULE 87 - THE OLD RULES", "Rule 87 repeals the CCS (Pension) Rules, 1972 and saves pending cases, so pre-2022 retirements are still decided under the 1972 rules. Full text is read in Batch 6.", "Rule eighty seven purane nineteen seventy two ke rules ko repeal karta hai, lekin pending cases bacha leta hai. Matlab jo log pehle retire ho gaye, unka case purane rules se hi chalega. Iska poora text Batch six mein aayega.", PINK, "FLAG"),
        ],
        "trap": "Rule 1 is not a money rule. It fixes only the NAME and the DATE - the pension arithmetic starts at Rule 44.",
        "trap_say": "Ek baat yaad rakho: Rule one paisa nahi deta. Woh sirf naam aur date fix karta hai. Pension ka calculation Rule forty four se shuru hota hai.",
    },
    {
        "id": "c02_rule2_tests",
        "chapter": "CHAPTER 2 - RULE 2: APPLICATION - THE FOUR TESTS",
        "title": "Rule 2 - The Four Tests Every Central Civil Pension Claim Must Cross",
        "badge": "RULE 2",
        "chips": [("31.12.2003", "appointment cut-off", ORANGE),
                  ("Substantive", "regular, not ad hoc", SKY),
                  ("Pensionable", "establishment", GREEN),
                  ("Defence", "civilians included", BLUE)],
        "q": "Whom do these rules apply to? Which four conditions must a Government servant satisfy to be covered?",
        "q_say": "Sir, ye rules kis par lagte hain, aur kaunse chaar conditions pure karne padte hain?",
        "rows": [
            ("THE OPENING WORDS", "Save as otherwise provided in these rules. Every exception sits inside the rule book itself, so Rule 2 is always read with Rule 19, Rule 20 and its own Explanation.", "Rule 2 ki shuruaat in shabdon se hoti hai: save as otherwise provided in these rules. Matlab agar koi exception khud in rules mein likha hai, woh chalega. Isliye Rule 2 ko Rule nineteen, twenty aur uske Explanation ke saath padho.", MUTED, ""),
            ("TEST 1 - THE DATE", "Appointed on or before 31.12.2003. The test is the date of appointment, and 01.01.2004 onwards is the NPS side of the line.", "Pehla test date ka hai. Appointment thirty one December two thousand three tak honi chahiye. Appointment pehle hui aur joining baad mein, yeh Rule 2 ka test nahi hai. NPS waale first January two thousand four se shuru hote hain.", ORANGE, "EXAM"),
            ("TEST 2 - THE POST", "Appointed substantively to a civil service or post in connection with the affairs of the Union. Substantive means regular and confirmed, not casual or ad hoc.", "Doosra test post ka hai. Appointment substantive honi chahiye, matlab regular aur confirmed, ad hoc ya daily wage nahi. Aur woh post Union ke kaam se juda hona chahiye.", SKY, ""),
            ("TEST 3 - THE ESTABLISHMENT", "The post must be borne on a pensionable establishment, that is, a post that carries pension. Civilian Government servants in the Defence Services are expressly included.", "Teesra test establishment ka hai. Post pensionable honi chahiye, yaani us post par pension milta ho. Defence Services ke civilian employees bhi isme aate hain, yeh Rule 2 mein saaf likha hai.", GREEN, "EXAM"),
            ("TEST 4 - THE UNION", "Service under the Union. A State Government post comes inside only through a transfer route such as Rule 4 or Rule 13, never on its own.", "Chautha test Union ka hai. Seva Union ke under honi chahiye. State government ki post apne aap in rules mein nahi aati. Uske liye Rule four ya Rule thirteen jaisa transfer route chahiye.", BLUE, ""),
        ],
        "trap": "TRAP: Defence is NOT excluded - only railway servants are. A civilian clerk paid from Civil Estimates of the Ministry of Defence is fully covered.",
        "trap_say": "Yahan classic trap hai. Defence Services ka matlab armed forces nahi. Defence ke civilian staff, jo Civil Estimates se pay hote hain, woh in rules mein aate hain. Sirf railway servants bahar hain.",
    },
    {
        "id": "c03_rule2_exclusions",
        "chapter": "CHAPTER 3 - RULE 2: THE EIGHT EXCLUSIONS, CLAUSE BY CLAUSE",
        "title": "Rule 2 - All Eight Exclusions in One Table (Railways to Constitutional Posts)",
        "badge": "RULE 2 (a)-(h)",
        "chips": [("8 exclusions", "clauses (a) to (h)", RED),
                  ("CPF", "fund, not pension", ORANGE),
                  ("AIS", "own pension rules", GREEN),
                  ("Contract", "unless otherwise", BLUE)],
        "q": "Which eight classes are left out of these rules, and what does each exclusion actually mean?",
        "q_say": "Sir, kaunse aath groups bahar hain, aur har clause ka matlab kya hai?",
        "kind": "table",
        "table": {
            "cols": ["Clause", "Class left out", "What it means in practice"],
            "widths": [0.10, 0.30, 0.60],
            "rows": [
                ["(a)", "Railway servants", "Railway Board runs its own pension code; a railway technician is outside even if he is a central employee."],
                ["(b)", "Casual and daily rated employment", "Daily wage and muster-roll staff, no regular pay scale, so no pension under these rules."],
                ["(c)", "Persons paid from contingencies", "Contingency is an office running-cost budget, not a pay scale head."],
                ["(d)", "Persons entitled to CPF benefit", "Contributory Provident Fund: employee and Government both contribute, a lump sum comes back."],
                ["(e)", "Members of the All India Services", "IAS, IPS and Indian Forest Service have their own pension framework."],
                ["(f)", "Locally recruited staff abroad", "Locally hired staff in Indian diplomatic, consular or other establishments in foreign countries."],
                ["(g)", "Persons employed on contract", "Outside, unless the contract itself provides for pension treatment."],
                ["(h)", "Terms fixed by Constitution or other law", "Where another law or the Constitution governs the service conditions, these rules step aside."],
            ],
        },
        "says": [
            "Ab aath exclusions, ek ek karke. Clause a railway servants. Railway ka apna pension code hai, isliye railway technician bahar hai, chahe woh central employee ho.",
            "Clause b casual aur daily rated staff. Clause c woh log jo contingencies se pay hote hain, matlab office ke running cost budget se. Clause d CPF waale: employee aur sarkar dono paisa daalte hain, aur lump sum wapas milta hai.",
            "Clause e All India Services, unka apna framework hai. Clause f videsh mein locally hire kiye gaye staff. Clause g contract staff, jab tak contract mein kuch aur na likha ho. Clause h woh log jinke service terms Constitution ya kisi doosre law se chalte hain.",
        ],
        "trap": "TRAP: this list works both ways. If a class is not in clause (a) to (h) and not excluded by any other rule, the person is INSIDE Rule 2.",
        "trap_say": "Trap yeh hai ki list dono taraf kaam karti hai. Agar koi clause a se h tak nahi aata, aur koi doosra rule bhi use bahar nahi karta, to woh person Rule 2 ke andar hai.",
    },
    {
        "id": "c04_rule2_expl_1_3",
        "chapter": "CHAPTER 4 - RULE 2, EXPLANATION: LIMBS (1) TO (3) - WHEN A LATE APPOINTMENT STILL COUNTS",
        "title": "The Explanation to Rule 2 - Three Doors for People Appointed After 31.12.2003",
        "badge": "EXPL. (1)-(3)",
        "chips": [("Induction", "training before cut-off", ORANGE),
                  ("Other scheme", "CPF or State service", SKY),
                  ("G.O. route", "special or general order", GREEN),
                  ("One Explanation", "six numbered limbs", PINK)],
        "q": "How can a person appointed after 31.12.2003 still come inside these rules?",
        "q_say": "Sir, koi banda thirty one December two thousand three ke baad appoint hua ho, phir bhi in rules mein kaise aa sakta hai?",
        "rows": [
            ("LIMB (1) - TRAINING", "Put on induction training on or before 31.12.2003, then appointed on a regular basis after it. The training must have led to the job, not been a side course.", "Pehla limb induction training ka hai. Training thirty one December two thousand three tak shuru ho, aur uske baad regular appointment ho. Training ke baad hi regular job mili ho, sirf side course na ho.", ORANGE, "EXAM"),
            ("LIMB (1) - THE PROVISO", "Three conditions: completion of training was essential for regular appointment, a salary or stipend was paid during training, and the training period could count as qualifying service under the 1972 rules.", "Isi limb ka proviso teen sharten lagata hai. Training complete karna regular appointment ke liye zaroori tha. Training ke dauran salary ya stipend mila. Aur woh period purane nineteen seventy two rules se qualifying service ginta ja sakta tha.", GREEN, "EXAM"),
            ("LIMB (2) - OTHER SCHEME", "(i) Central establishment on a different pension scheme, or (ii) a State Government or autonomous body with a similar non-contributory scheme, and then a Central post after 31.12.2003.", "Doosra limb do hisson mein hai. Pehla, pehle Central department mein kisi doosre pension scheme ke under appointment. Doosra, State government ya autonomous body jahan milta julta non contributory scheme ho. Uske baad Central post par appointment.", SKY, ""),
            ("LIMB (2) - THE CONDITION", "The servant must fulfil every other condition for counting that earlier service, under these rules or under a general or special order. This is the limb most answers forget.", "Yahan condition hai, aur yahi sabse zyada bhooli jaati hai. Purani service ko count karne ke liye baaki saari conditions bhi poori honi chahiye, chahe in rules se ya kisi general ya special order se.", BLUE, "TRAP"),
            ("LIMB (3) - THE ORDER ROUTE", "Appointed after 31.12.2003 and covered by a special or general Government order that brings him in. The order does the work; the date alone decides nothing.", "Teesra limb order ka hai. Appointment baad mein hui, lekin koi special ya general government order use andar le aata hai. Yahan order kaam karta hai, sirf date se kuch decide nahi hota.", PINK, ""),
        ],
        "trap": "TRAP: the Explanation EXTENDS coverage. It never backdates an appointment, so seniority and pay fixation are untouched.",
        "trap_say": "Trap clear kar dete hain. Yeh Explanation coverage badhata hai, appointment ki date peeche nahi khinchta. Seniority aur pay fixation par iska koi asar nahi hota.",
    },
    {
        "id": "c05_rule2_expl_4_6",
        "chapter": "CHAPTER 5 - RULE 2, EXPLANATION: LIMBS (4) TO (6) AND THE COUNT",
        "title": "Casual Labourers, NPS Staff and Temporary Hands - Limbs (4), (5) and (6)",
        "badge": "EXPL. (4)-(6)",
        "chips": [("1993 scheme", "temporary status", ORANGE),
                  ("Rule 15", "only 50% counts", SKY),
                  ("NPS", "narrow doorway", GREEN),
                  ("1965 rules", "temporary service", PINK)],
        "q": "What happens to casual labourers with temporary status, NPS staff, and temporary appointees?",
        "q_say": "Sir, temporary status waale casual labourers, NPS staff aur temporary appointees ka kya hota hai?",
        "rows": [
            ("LIMB (4) - TEMPORARY STATUS", "Regularly appointed after 31.12.2003 but given temporary status on or before that date under the Casual Labourers (Grant of Temporary Status and Regularisation) Scheme, 1993, followed without a break by regular appointment.", "Chautha limb casual labourers ka hai. Regular appointment baad mein hui ho, lekin temporary status thirty one December two thousand three tak mil gaya ho, nineteen ninety three scheme ke under. Aur uske baad bina break regular appointment ho.", ORANGE, "EXAM"),
            ("LIMB (4) - THE RULE 15 CUT", "Coverage comes with a haircut: under Rule 15 only 50 per cent of the temporary-status service counts as qualifying service.", "Coverage milti hai, par poori nahi. Rule fifteen kehta hai ki temporary status waali service ka sirf fifty percent qualifying service ginega. Aadha service kat jaata hai, isliye pension chhoti ho jaati hai.", SKY, "EXAM"),
            ("LIMB (5) - NPS STAFF", "An NPS-covered servant appointed after 31.12.2003 gets invalid pension under Rule 39 and family pension under Rule 50 on death or invalidation. Full treatment is in the next chapter.", "Paanchva limb NPS walon ke liye chhota darwaza hai. NPS covered banda, jo baad mein appoint hua, death ya invalidation par Rule thirty nine ki invalid pension aur Rule fifty ki family pension le sakta hai. Poora detail agle chapter mein.", GREEN, ""),
            ("LIMB (6) - TEMPORARY HANDS", "A person appointed in a temporary capacity on or before 31.12.2003, who retired before getting a substantive post, gets only what the CCS (Temporary Service) Rules, 1965 allow.", "Chhatha limb temporary appointment ka hai. Temporary capacity mein thirty one December two thousand three tak appointment, aur substantive post milne se pehle retirement. Aise banda ko sirf utna, jitna CCS Temporary Service Rules nineteen sixty five dete hain.", PINK, ""),
            ("THE COUNT", "One Explanation, six numbered limbs - not six Explanations. Say Explanation, limb (5), not Explanation 5, when you write an answer.", "Count yaad rakho. Rule 2 mein ek hi Explanation hai, uske andar chhah numbered limbs hain. Isliye likho Explanation limb five, na ki Explanation five. Yeh chhoti baat answer sheet mein marks laati hai.", YELLOW, "EXAM"),
        ],
        "trap": "TRAP: limbs (4) and (6) both involve temporary service, but (4) gives full coverage with a 50 per cent cut and (6) gives only 1965-rules benefits.",
        "trap_say": "Trap yeh hai ki limb four aur limb six dono temporary service jaise lagte hain. Limb four mein coverage milti hai, par service ka aadha hissa ginega. Limb six mein sirf nineteen sixty five rules ka benefit milta hai.",
    },
    {
        "id": "c06_rule2_expl5_nps",
        "chapter": "CHAPTER 6 - EXPLANATION LIMB (5) IN DEPTH: THE NPS DOORWAY, NOW CONFIRMED",
        "title": "The NPS Doorway - Option under Rule 10 of the NPS Rules, or the Default Option",
        "badge": "EXPL. (5)",
        "chips": [("NPS Rules 2021", "G.S.R. 227(E)", SKY),
                  ("Rule 10 option", "confirmed", GREEN),
                  ("Death / invalid", "only two triggers", RED),
                  ("Rules 39 & 50", "the benefits", ORANGE)],
        "q": "Exactly which NPS-covered employees can claim invalid pension or family pension under these rules?",
        "q_say": "Sir, NPS waale kis employee ko invalid pension ya family pension mil sakti hai, aur kis condition par?",
        "rows": [
            ("THE INSTRUMENT", "The option lives in Rule 10 of the CCS (Implementation of National Pension System) Rules, 2021, notified by G.S.R. 227(E) of 30.03.2021. Confirmed.", "Ab yeh confirm ho gaya hai. Option Central Civil Services Implementation of National Pension System Rules two thousand twenty one ke Rule ten mein hai. Woh rules G.S.R. two two seven E se thirty March two thousand twenty one ko aaye.", SKY, "NEW"),
            ("THE OPTION", "The servant must have exercised an option to this effect under Rule 10 of the NPS Rules, or must fall in the default option that points to these rules or to the 1972 rules.", "Do raaste hain. Ya to employee ne Rule ten ke under option exercise kiya ho, ya woh default option waala case ho jahan by default in rules ya purane nineteen seventy two rules ka benefit milta hai.", GREEN, "EXAM"),
            ("THE TRIGGERS", "Only two: death in service, or discharge from service on the ground of invalidation. Nothing else opens the doorway.", "Sirf do trigger hain. Service ke dauran death, ya invalidation ke ground par discharge. Iske alawa koi raasta nahi khulta, chahe service kitni lambi ho.", RED, "EXAM"),
            ("THE BENEFITS", "Invalid pension under Rule 39 and family pension under Rule 50, paid to the servant or to the family as the case may be. Gratuity follows the NPS gratuity rules.", "Benefit do hain: Rule thirty nine ki invalid pension aur Rule fifty ki family pension, jo servant ya family ko milegi. Gratuity ke liye alag NPS gratuity rules hain, unhe is chapter mein na milao.", ORANGE, ""),
            ("THE LIMIT", "On ordinary superannuation an NPS employee takes NPS benefits only. The Unified Pension Scheme rules, 2025 are a separate track and do not change Rule 2.", "Limit yaad rakho. Normal retirement par NPS employee ko sirf NPS benefit milega, in rules se pension nahi. Unified Pension Scheme ke rules two thousand twenty five alag track hain, Rule two ko woh badalte nahi.", PURPLE, ""),
        ],
        "trap": "TRAP: family pension here is Rule 50 of the CCS (Pension) Rules, not the NPS family pension. Read the option before quoting the rule number.",
        "trap_say": "Trap yeh hai ki yahan family pension ka matlab CCS Pension Rules ka Rule fifty hai, NPS ka family pension nahi. Rule number likhne se pehle option waali condition padho.",
    },
    {
        "id": "c07_cutoff_traps",
        "chapter": "CHAPTER 7 - THE 31.12.2003 CUT-OFF: THREE LIVE TRAPS AND THE 22.06.2026 O.M.",
        "title": "Cut-off Traps - Joining Date, CPF versus NPS, and Compassionate Appointments",
        "badge": "31.12.2003",
        "chips": [("Appointment", "not joining date", ORANGE),
                  ("CPF vs NPS", "two different exits", SKY),
                  ("O.M. 22.06.2026", "crucial date = application", GREEN),
                  ("No OPS rollback", "scope flag", PINK)],
        "q": "Which date is the crucial date, what is the difference between CPF and NPS, and did the 2026 O.M. bring back the old pension scheme?",
        "q_say": "Sir, crucial date kaunsi hai, CPF aur NPS mein farq kya hai, aur kya two thousand twenty six ka O.M. purani pension scheme wapas le aaya?",
        "rows": [
            ("TRAP 1 - WHICH DATE", "The rules test the date of appointment. A late joining letter after 31.12.2003 does not push a person out if the appointment itself was made on or before the cut-off.", "Pehla trap date ka hai. Rules appointment ki date dekhte hain. Agar appointment thirty one December two thousand three tak ho gayi, to joining letter baad mein aaya, isse banda bahar nahi hota.", ORANGE, "TRAP"),
            ("TRAP 2 - CPF IS NOT NPS", "CPF is a contributory provident fund, excluded by clause (d). NPS is the pension system for post-2003 entrants. They are different exits and different rules.", "Doosra trap CPF aur NPS ka mix up hai. CPF ek contributory provident fund hai, jo clause d se bahar hai. NPS un logon ka system hai jo baad mein aaye. Dono alag exit hain, alag rules hain.", SKY, "TRAP"),
            ("THE O.M. OF 22.06.2026", "DoPPW O.M. No. 57/05/2021-P&PW(B)/Compassionate dated 22.06.2026: for compassionate appointment the date of application is the crucial date, if the applicant was then eligible.", "Ab naya order. DoPPW ka O.M. twenty two June two thousand twenty six, compassionate appointment ke liye. Kehta hai crucial date application ki date hai, agar us waqt applicant eligible tha.", GREEN, "NEW"),
            ("WORKED EXAMPLE", "Applied 15.12.2003 while eligible, appointment letter in 2006: these rules apply. Applied in 2005: the crucial date falls after the cut-off, so NPS applies.", "Example le lo. Application fifteen December two thousand three ko, eligible the, appointment letter two thousand six mein aaya. In rules lagenge. Agar application two thousand five mein hoti, to crucial date cut off ke baad, isliye NPS lagta.", BLUE, ""),
            ("WHAT IT IS NOT", "Not a general return to the old pension scheme. Regular recruits are not covered, and the O.M. speaks to Ministries and Departments, not to every autonomous body.", "Yeh samajh lo, yeh OPS ki wapsi nahi hai. Regular recruitment isse cover nahi hoti. O.M. Ministries aur Departments ko address hai, har autonomous body ko nahi. Isliye scope ka daawa na karo.", PINK, "FLAG"),
        ],
        "trap": "TRAP: an O.M. cannot amend a rule. The 22.06.2026 O.M. explains how to apply the cut-off; it does not rewrite Rule 2.",
        "trap_say": "Trap yeh hai ki O.M. se rule amend nahi hota. Twenty two June ka order sirf batata hai ki cut off kaise apply karna hai. Rule two ka text woh badal nahi sakta.",
    },
]


SCENES += [
    {
        "id": "c08_defs_a_f",
        "chapter": "CHAPTER 8 - RULE 3(1): DEFINITIONS (a) TO (f) - THE INSTRUMENT AND THE MONEY WORDS",
        "title": "Rule 3(1)(a) to (f) - Accounts Officer to Dearness Relief",
        "badge": "RULE 3(1)(a)-(f)",
        "chips": [("26 definitions", "clauses (a) to (z)", ORANGE),
                  ("Bhavishya", "online sanction system", SKY),
                  ("Child", "Rules 45 and 50", GREEN),
                  ("DR", "Rule 52, not pension", RED)],
        "q": "What do the first six definitions cover, and why does each one matter?",
        "q_say": "Sir, pehli chhah definitions kya cover karti hain aur har ek kyun matter karti hai?",
        "rows": [
            ("(a) ACCOUNTS OFFICER", "Any officer who maintains the accounts of a Ministry, Department or Union territory office, and it expressly includes an Accountant-General.", "Clause a Accounts Officer. Har woh officer jo Ministry, Department ya Union territory office ka account rakhta hai. Isme Accountant General bhi shaamil hai, yeh rule saaf likhta hai.", ORANGE, "EXAM"),
            ("(b) ALLOTTEE", "A Government servant to whom Government accommodation has been allotted, on payment of licence fee or otherwise.", "Clause b Allottee. Woh sarkari employee jise government ka ghar allot hua ho, chahe licence fee dekar ya bina. Yeh definition aage withheld amount aur No Demand Certificate waale rules mein kaam aati hai.", SKY, ""),
            ("(c) AVERAGE EMOLUMENTS", "As determined under Rule 32, that is, the average of emoluments of the last ten months of service.", "Clause c average emoluments. Iska matlab Rule thirty two se tay hota hai, yaani aakhri das mahine ki emoluments ka average. Pension mein jo beneficial ho, woh liya jaata hai.", GREEN, "EXAM"),
            ("(d) BHAVISHYA", "The online system for sanction of retirement benefits and for tracking the sanction and payment of pension by the servant and by the authorities.", "Clause d Bhavishya. Yeh sarkar ka online system hai jahan retirement benefits sanction hote hain aur pension ka payment track hota hai. Employee aur authority dono ise dekhte hain.", BLUE, ""),
            ("(e) CHILD / (f) DEARNESS RELIEF", "Child: a son or daughter eligible for death gratuity under Rule 45 or family pension under Rule 50. Dearness relief: relief on pension and family pension as specified in Rule 52.", "Clause e child, matlab beta ya beti jo Rule forty five ki death gratuity ya Rule fifty ki family pension ka haqdaar ho. Clause f dearness relief, jo Rule fifty two ke hisaab se pension par milta hai.", PINK, ""),
        ],
        "trap": "TRAP: emoluments (Rule 31) is NOT average emoluments (Rule 32). One is the pay at retirement, the other is a ten-month average.",
        "trap_say": "Trap yeh hai ki emoluments aur average emoluments alag hain. Emoluments Rule thirty one, average emoluments Rule thirty two. Ek retirement ke waqt ki pay hai, doosra das mahine ka average.",
    },
    {
        "id": "c09_defs_g_j",
        "chapter": "CHAPTER 9 - RULE 3(1): DEFINITIONS (g) TO (j) - DEFENCE SERVICE, EMOLUMENTS, FAMILY PENSION, FOREIGN SERVICE",
        "title": "Rule 3(1)(g) to (j) - Why Defence Service Is Not the Armed Forces",
        "badge": "RULE 3(1)(g)-(j)",
        "chips": [("Defence service", "civil side only", GREEN),
                  ("Armed forces", "separate Acts", RED),
                  ("Family pension", "excludes DR", ORANGE),
                  ("Foreign service", "outside the CFI", SKY)],
        "q": "What exactly is Defence Service, and how is it different from service in the Army, Navy or Air Force?",
        "q_say": "Sir, Defence Service exactly kya hai, aur Army, Navy ya Air Force ki service se kaise alag hai?",
        "rows": [
            ("(g) DEFENCE SERVICE", "Service under the Government of India in the Ministry of Defence, including the Defence Accounts Department, paid out of the Civil Estimates of that Ministry.", "Clause g Defence Service. Ministry of Defence ke under service, Defence Accounts Department bhi shaamil. Aur pay Ministry of Defence ke Civil Estimates se hona chahiye. Yeh civil side hai.", GREEN, "EXAM"),
            ("(g) THE NEGATIVE HALF", "And not subject to the Air Force Act 1950, the Army Act 1950 or the Navy Act 1957. That single line keeps the armed forces out of these rules.", "Isi clause ka doosra hissa: woh service Air Force Act, Army Act ya Navy Act ke under na ho. Yahi ek line armed forces ko in rules se bahar rakhti hai.", RED, "EXAM"),
            ("(h) EMOLUMENTS", "Emoluments as defined in Rule 31 - basic pay plus the specified elements, not the gross salary on the pay slip.", "Clause h emoluments. Iska matlab Rule thirty one se hai. Basic pay aur jo elements rule mein likhe hain, woh judte hain. Pay slip ka poora gross nahi, yeh farq samajh lo.", SKY, ""),
            ("(i) FAMILY PENSION", "Family pension admissible under Rule 50, but it does not include dearness relief. DR is a separate add-on under Rule 52.", "Clause i family pension, jo Rule fifty ke under milti hai. Isme dearness relief shaamil nahi hai. DR alag se Rule fifty two ke under milta hai. Isliye family pension ka figure DR ke bina likho.", ORANGE, "EXAM"),
            ("(j) FOREIGN SERVICE", "Service where the servant receives pay, with the sanction of the Government, from a source other than the Consolidated Fund of India, of a State or of a Union territory.", "Clause j foreign service. Yahan employee ko pay sarkar ki sanction se milti hai, lekin source Consolidated Fund of India, State ya Union territory ka nahi hota. Kisi doosre source se aati hai.", PURPLE, ""),
        ],
        "trap": "TRAP: an Army havaldar is outside Rule 2; a civilian clerk in the Defence Accounts Department is inside. Same Ministry, different Acts.",
        "trap_say": "Trap yeh hai ki Army ka havaldar Rule two se bahar hai, lekin Defence Accounts Department ka civilian clerk andar hai. Ministry ek hi, par Acts alag hain, isliye result alag hai.",
    },
    {
        "id": "c10_defs_k_p",
        "chapter": "CHAPTER 10 - RULE 3(1): DEFINITIONS (k) TO (p) - FORM, FORMAT, GRATUITY, HEAD OF DEPARTMENT",
        "title": "Rule 3(1)(k) to (p) - Form versus Format, and the Three Kinds of Gratuity",
        "badge": "RULE 3(1)(k)-(p)",
        "chips": [("Form", "application", ORANGE),
                  ("Format", "template", SKY),
                  ("Gratuity", "Rules 44, 45", GREEN),
                  ("Head of Dept", "DFPR Schedule I", PINK)],
        "q": "What is the difference between a Form and a Format, and what does gratuity include?",
        "q_say": "Sir, Form aur Format mein farq kya hai, aur gratuity mein kya kya aata hai?",
        "rows": [
            ("(k) FORM / (l) FORMAT", "Both are documents appended to these rules. In practice a Form is an application the servant files, and a Format is a template, checklist or undertaking.", "Clause k aur l. Form aur Format dono rules ke saath lagi documents hain. Practice mein Form woh application hai jo employee bharta hai, aur Format ek template, checklist ya undertaking hota hai. Yeh distinction answer mein likho.", ORANGE, "EXAM"),
            ("(m) GOVERNMENT / (n) DUES", "Government means the Central Government. Government dues means dues as defined in Rule 67(2), the recovery chapter.", "Clause m Government ka matlab Central Government. Clause n Government dues, jo Rule sixty seven sub rule two mein define hote hain. Yeh recovery waale chapter ka term hai.", SKY, ""),
            ("(o) GRATUITY - THREE KINDS", "Service gratuity under Rule 44; retirement gratuity or death gratuity under Rule 45(1); and residuary gratuity under Rule 45(3).", "Clause o gratuity ke teen kism. Service gratuity Rule forty four se. Retirement ya death gratuity Rule forty five sub rule one se. Aur residuary gratuity Rule forty five sub rule three se. Teen naam yaad rakho.", GREEN, "EXAM"),
            ("(p) HEAD OF DEPARTMENT", "An authority specified in Schedule I to the Delegation of Financial Powers Rules, 1978, and any other authority or person the President may specify by order.", "Clause p Head of Department. Woh authority jo DFPR nineteen seventy eight ke Schedule one mein likhi hai, aur President ke order se koi doosri authority bhi. President ka power reserve hai.", PINK, ""),
            ("(q) HEAD OF OFFICE - PREVIEW", "A Gazetted Officer declared as such under Rule 14 of the DFPR, 1978, and any other person the competent authority specifies. Note: it is the competent authority here, not the President.", "Agli clause ka preview. Head of Office woh Gazetted Officer jo DFPR Rule fourteen se declare hua ho. Aur koi doosra person jo competent authority specify kare. Yahan President nahi, competent authority likha hai. Yeh gap pehle version mein reh gaya tha.", BLUE, "FLAG"),
        ],
        "trap": "TRAP: 'Form 1' under Rule 9(1) is the pensioner's application. 'Format 1' under Rule 7(4)(b) is the secrecy undertaking. They are not interchangeable.",
        "trap_say": "Classic trap. Rule nine ka Form one pensioner ki application hai. Rule seven ka Format one secrecy undertaking hai. Dono bilkul alag hain, inhe mix na karo.",
    },
    {
        "id": "c11_defs_q_t",
        "chapter": "CHAPTER 11 - RULE 3(1): DEFINITIONS (q) TO (t) - OFFICE, FUND, MINOR, PENSION",
        "title": "Rule 3(1)(q) to (t) - Head of Office, Local Fund, Minor and the Word Pension",
        "badge": "RULE 3(1)(q)-(t)",
        "chips": [("Head of Office", "DFPR Rule 14", BLUE),
                  ("Local Fund", "full Govt control", GREEN),
                  ("Minor", "below 18 years", ORANGE),
                  ("Pension", "excludes DR", RED)],
        "q": "How is pension defined, and why does the definition of a minor matter for family pension?",
        "q_say": "Sir, pension ki definition kya hai, aur minor ki definition family pension ke liye kyun important hai?",
        "rows": [
            ("(q) HEAD OF OFFICE", "A Gazetted Officer declared as such under Rule 14 of the DFPR, 1978, and includes any other authority or person the competent authority may specify by order.", "Clause q Head of Office. Gazetted Officer jo DFPR Rule fourteen se declare hua ho. Aur competent authority kisi doosre ko bhi specify kar sakti hai. Rule two ki listing mein sirf declaration likhna aadha answer hai.", BLUE, "EXAM"),
            ("(r) LOCAL FUND", "A fund administered by a body which, by law or by a rule having the force of law, comes under Government control, and over whose expenditure the Government keeps complete and direct control.", "Clause r local fund administered by Government. Woh fund jiska body law se ya law ke barabar rule se government control mein aaye, aur jiske kharch par government ka poora direct control ho. Aise fund ki service Rule twelve se qualify karti hai.", GREEN, ""),
            ("(s) MINOR", "A person who has not completed eighteen years of age. A minor nominee needs a guardian to receive the amount.", "Clause s minor. Woh person jiski umar eighteen saal poori nahi hui. Family pension aur nomination mein minor ka matlab yahi hai, aur minor ke paise guardian leta hai.", ORANGE, ""),
            ("(t) PENSION - THE WHOLE TRICK", "Pension includes gratuity, except where the word pension is used in contradiction to gratuity. And pension never includes dearness relief.", "Clause t sabse important hai. Pension mein gratuity shaamil hai, lekin sirf tab tak jab tak pension shabd gratuity ke opposite use na ho. Aur pension mein dearness relief kabhi shaamil nahi hota.", RED, "EXAM"),
            ("WHY THIS MATTERS", "Rule 8 says a part of pension may be withheld. Because pension includes gratuity, the withholding power can reach gratuity, except where the rule separates them.", "Yeh definition kyun matter karti hai? Rule eight kehta hai pension ka hissa withhold hoga. Pension mein gratuity shaamil hai, isliye power gratuity tak pahunch sakti hai, siwaay un jagah jahan rule dono ko alag karta hai.", PURPLE, "TRAP"),
        ],
        "trap": "TRAP: DR is not pension. So a withholding order on pension does not automatically touch dearness relief, and a DR order does not touch basic pension.",
        "trap_say": "Trap yeh hai ki DR pension nahi hai. Isliye pension par withholding order ka asar DR par apne aap nahi hota, aur DR ka order basic pension ko chhoota nahi.",
    },
    {
        "id": "c12_defs_u_z",
        "chapter": "CHAPTER 12 - RULE 3(1): DEFINITIONS (u) TO (z) AND RULE 3(2): THE FALLBACK",
        "title": "Rule 3(1)(u) to (z) - Disbursing Authority, PPO, Qualifying Service, Treasury",
        "badge": "RULE 3(1)(u)-(z)",
        "chips": [("4 channels", "who pays pension", GREEN),
                  ("e-PPO", "counts as PPO", SKY),
                  ("Qualifying service", "Rules 11 to 30", ORANGE),
                  ("Rule 3(2)", "Fundamental Rules 1922", PINK)],
        "q": "Who can pay pension, what is a PPO, and what happens if a word is not defined at all?",
        "q_say": "Sir, pension kaun pay kar sakta hai, PPO kya hai, aur agar koi word define hi na ho to kya hota hai?",
        "rows": [
            ("(u) DISBURSING AUTHORITY", "Four channels: banks selected in consultation with the RBI and specified by the Controller General of Accounts, Post Office, Treasury including sub-treasury, or an Accounts Officer.", "Clause u. Pension dene ke chaar channel hain. Pehla, RBI se consultation ke baad chune gaye banks, jinko Controller General of Accounts specify karta hai. Doosra Post Office. Teesra Treasury, sub treasury ke saath. Chautha Accounts Officer.", GREEN, "EXAM"),
            ("(v) PPO / (w) QUALIFYING SERVICE", "PPO includes the e-Pension Payment Order. Qualifying service means service rendered on duty or otherwise which is counted for pension and gratuity.", "Clause v P.P.O. mein e P.P.O. bhi shaamil hai. Clause w qualifying service, yaani woh service jo duty par ya kisi aur tarah di gayi ho aur pension aur gratuity ke liye gini jaati hai. Iski poori detail Rules eleven se thirty mein hai.", SKY, ""),
            ("(x) RETIREMENT BENEFITS", "Pension or service gratuity, and retirement gratuity where it is admissible. The phrase does not include commutation, which has its own 1981 rules.", "Clause x retirement benefits. Isme pension ya service gratuity aati hai, aur retirement gratuity bhi jahan admissible ho. Commutation isme nahi aata, uske apne nineteen eighty one ke rules hain.", ORANGE, ""),
            ("(y) SERVICE BOOK / (z) TREASURY", "Service book includes the service roll, if any. Treasury includes a sub-treasury, so a sub-treasury payment is a valid pension payment.", "Clause y service book, jisme service roll bhi shaamil hai. Clause z treasury, jisme sub treasury bhi aata hai. Matlab sub treasury se pension milna bhi valid payment hai.", BLUE, ""),
            ("RULE 3(2) - THE FALLBACK", "A word used here but not defined takes the meaning given in the Fundamental Rules, 1922. Check Rule 3 first, then the FR, 1922, and only then a dictionary.", "Rule three sub rule two fallback deta hai. Jo word yahan define nahi hai, uska matlab Fundamental Rules nineteen twenty two se liya jaayega. Isliye pehle Rule three dekho, phir FR, aur sabse aakhir mein dictionary.", PINK, "EXAM"),
        ],
        "trap": "TRAP: the count is 26 definitions, clause (a) to clause (z). The old script's '6 Explanations' under Rule 2 is wrong - it is one Explanation with six limbs.",
        "trap_say": "Count yaad rakho, Rule three mein chhabbis definitions hain, clause a se clause z tak. Aur Rule two mein chhah Explanation nahi, ek Explanation ke chhah limb hain. Yeh correction note kar lo.",
    },
    {
        "id": "c13_rule4",
        "chapter": "CHAPTER 13 - RULE 4: TRANSFER FROM A SERVICE THESE RULES DO NOT COVER",
        "title": "Rule 4 - The Six-Month Option, in Writing, and Then Final",
        "badge": "RULE 4",
        "chips": [("6 months", "to elect", ORANGE),
                  ("Whichever later", "order or return from leave", SKY),
                  ("In writing", "to the transfer authority", GREEN),
                  ("Final", "no second change", RED)],
        "q": "A person is permanently transferred into a service covered by these rules. Can he choose to stay under his old pension rules?",
        "q_say": "Sir, agar koi permanently in rules waali service mein transfer hota hai, to kya woh purane pension rules mein reh sakta hai?",
        "rows": [
            ("RULE 4(1) - THE ROUTE", "A Government servant permanently transferred to a service or post covered by these rules, from a service or post not covered, becomes subject to these rules.", "Rule four sub rule one. Agar koi employee permanently aisi service mein transfer hota hai jo in rules mein aati hai, aur pehle aisi service mein tha jo inme nahi aati, to woh in rules ke under aa jaata hai.", ORANGE, "EXAM"),
            ("THE PROVISO - SIX MONTHS", "He may elect to stay under the pension rules that applied to him just before the transfer, within six months of the transfer order or of his return from leave, whichever is later.", "Proviso option deta hai. Woh chah sakta hai ki purane pension rules hi chalte rahein. Time six mahine hai, transfer order se, ya agar us din leave par tha to leave se wapas aane se, jo baad mein aaye.", SKY, "EXAM"),
            ("RULE 4(2) - IN WRITING", "The option must be exercised in writing and communicated to the authority that made the transfer order. An oral choice has no value.", "Sub rule two kehta hai option likhit mein ho, aur us authority ko bheja jaaye jisne transfer order diya. Zubani kaha hua option count nahi hota. Likhkar do, warna option hi nahi.", GREEN, ""),
            ("RULE 4(3) - FINAL", "The option, once exercised, is final. There is no window to switch again when the old rules look more generous later.", "Sub rule three. Option ek baar exercise hua to final. Baad mein purane rules zyada faydemand lagein to dobara badalne ka mauka nahi. Isliye pehle hisaab lagao, phir likho.", RED, "TRAP"),
            ("WORKED EXAMPLE", "Transfer order dated 10.03.2026 while on leave, return from leave 04.04.2026. The later date starts the clock, so the last date is 04.10.2026.", "Example. Transfer order ten March two thousand twenty six ka, us waqt leave par the. Leave se wapsi four April two thousand twenty six ko. Baad waali date se clock chalti hai, isliye last date four October two thousand twenty six.", BLUE, ""),
        ],
        "trap": "TRAP: Rule 4 gives no money. It only decides WHICH rule book applies - and after the option, no change of mind.",
        "trap_say": "Trap yeh hai ki Rule four paisa nahi deta. Woh sirf batata hai kaunsi rule book lagegi. Aur option ke baad mann badalne ka scope nahi hai.",
    },
    {
        "id": "c14_rule5",
        "chapter": "CHAPTER 14 - RULE 5: CLAIMS TO PENSION OR FAMILY PENSION",
        "title": "Rule 5 - Which Version of the Rules Applies, and What Counts as the Last Working Day",
        "badge": "RULE 5",
        "chips": [("Version", "rules in force on that date", ORANGE),
                  ("Last working day", "retirement day counts", SKY),
                  ("Death", "also a completed day", GREEN),
                  ("Proviso", "leave or suspension", PINK)],
        "q": "If the rules change between service and retirement, which version decides the claim?",
        "q_say": "Sir, agar service ke beech rules badal jaayein, to pension kis version se decide hogi?",
        "rows": [
            ("RULE 5(1) - THE VERSION", "A claim to pension or family pension is regulated by the rules in force on the date the servant retires, is retired, is discharged, is allowed to resign, or dies.", "Rule five sub rule one. Claim us waqt laagu rules se decide hogi jab employee retire hua, retire kiya gaya, discharge hua, resign karne diya gaya, ya death hui. Matlab date of event, date of application nahi.", ORANGE, "EXAM"),
            ("WHOLE-RULE SWITCH", "A whole rule book applies, not a mix. If the 1972 rules govern the date, the 2021 rules cannot be picked clause by clause.", "Ek baat samajh lo. Poori rule book lagti hai, mix match nahi. Agar date par nineteen seventy two ke rules lagte hain, to twenty twenty one ke rules se apni pasand ke clause nahi chun sakte.", SKY, "TRAP"),
            ("RULE 5(2) - LAST WORKING DAY", "The day of retirement, discharge or permitted resignation is the last completed working day, and the date of death is also treated as a completed working day.", "Sub rule two. Retirement, discharge ya resign ki date last completed working day maani jaati hai. Aur death ki date bhi completed working day maani jaati hai. Isse ek din ka benefit mil jaata hai.", GREEN, "EXAM"),
            ("THE PROVISO", "If the servant was on leave, absent from duty otherwise, or under suspension just before retirement or death, that day remains part of the leave, absence or suspension.", "Ab proviso. Agar retirement ya death se pehle employee leave par tha, ya kisi aur tarah duty se absent tha, ya suspension mein tha, to woh din usi leave, absence ya suspension ka hissa rehta hai. Ye point pehle version mein nahi tha, ab joda hai.", PINK, "EXAM"),
            ("THE 30.10.2025 O.M.", "The DoPPW O.M. of 30.10.2025 on claims to pension restates Rule 5. It clarifies; it does not create a new rule.", "DoPPW ka thirty October two thousand twenty five ka O.M. Rule five ko dohrata hai. Woh sirf clarification deta hai, naya rule nahi banata. Isliye answer mein O.M. ko rule ke barabar na likho.", PURPLE, "FLAG"),
        ],
        "trap": "TRAP: Rule 4 asks which rule BOOK applies; Rule 5 asks which VERSION applies on the event date. Different questions, different answers.",
        "trap_say": "Dono rules ka sawaal alag hai. Rule four poochhta hai kaunsi rule book lagegi. Rule five poochhta hai us date par kaunsa version chalega. Inhe mix na karo.",
    },
    {
        "id": "c15_rule6",
        "chapter": "CHAPTER 15 - RULE 6: LIMITATIONS ON THE NUMBER OF PENSIONS",
        "title": "Rule 6 - No Two Pensions, Four Categories of Pensioner, Two Provisos, Two Explanations",
        "badge": "RULE 6",
        "chips": [("6(1)", "no double pension", RED),
                  ("6(2)", "re-employment rule", ORANGE),
                  ("31.12.2003", "autonomous body route", SKY),
                  ("Gratuity cap", "combined ceiling", GREEN)],
        "q": "Can a Government servant draw two pensions? What happens when a pensioner is re-employed?",
        "q_say": "Sir, kya ek employee ko do pension mil sakti hain? Aur pensioner ke re-employment par kya hota hai?",
        "rows": [
            ("RULE 6(1) - THE CORE BAN", "A Government servant shall not earn two pensions in the same service or post, at the same time, or by the same continuous service.", "Rule six sub rule one simple hai. Ek hi service ya post par, ek hi waqt, ek hi continuous service se do pension nahi mil sakti. Double dipping band hai.", RED, "EXAM"),
            ("RULE 6(2) - FOUR CATEGORIES", "Except as Rules 19 and 20 allow, anyone who retired on superannuation, retiring or compulsory retirement pension, or holds a compassionate allowance after dismissal or removal, gets no second pension for re-employment.", "Sub rule two kehta hai, Rule nineteen ya twenty ke siwaay, chaar tarah ke logon ko re employment ke period ka alag pension ya gratuity nahi milega. Superannuation pension, retiring pension, compulsory retirement pension, aur dismissal ya removal ke baad milne waali compassionate allowance.", ORANGE, "EXAM"),
            ("FIRST PROVISO", "Autonomous body or PSU service, followed by Government service on or before 31.12.2003 with the proper permission of that body: Government pension plus the body's pension, both allowed.", "Pehla proviso. Autonomous body ya PSU ki service ke baad, thirty one December two thousand three tak government service, aur us body ki proper permission ho. Aise case mein government ki pension aur body ki pension, dono mil sakti hain.", SKY, ""),
            ("SECOND PROVISO - THE CAP", "Combined gratuity for the body service and the Government service cannot exceed what would be admissible if the whole service had been Government service with the same retirement emoluments.", "Doosra proviso cap lagata hai. Body ki service aur government service ki total gratuity us amount se zyada nahi ho sakti jo poori service government ki hoti to milti. Yeh cap double benefit ko rokta hai.", GREEN, "EXAM"),
            ("EXPLANATION 1 AND 2", "1: proper permission is deemed if he applied with the body's prior permission and its order says he resigns to join the Government post with that permission. 2: the body pays its own pension; the Government has no liability for it.", "Ab do Explanation. Pehla: proper permission maani jaayegi agar application body ki prior permission se di, aur body ka order kehta hai woh permission ke saath government post ke liye resign kar raha hai. Doosra: body ki service ki pension body khud degi, government par uski liability nahi.", PINK, ""),
        ],
        "trap": "TRAP: Rule 19 and Rule 20 are the only in-built exceptions. Do not invent a third exception from an O.M. read on its own.",
        "trap_say": "Trap yeh hai ki Rule nineteen aur twenty hi rule ke andar likhe exceptions hain. Kisi akela O.M. padhkar teesra exception mat banao. Pehle rule, phir order.",
    },
]


SCENES += [
    {
        "id": "c16_rule7_good_conduct",
        "chapter": "CHAPTER 16 - RULE 7(1) TO 7(3): PENSION SUBJECT TO FUTURE GOOD CONDUCT",
        "title": "Rule 7 - Good Conduct as a Condition, the Appointing Authority, and 15 + 15 Days",
        "badge": "RULE 7(1)-(3)",
        "chips": [("Implied condition", "7(1)(a)", ORANGE),
                  ("Appointing Authority", "not the President", RED),
                  ("Floor", "Rule 44 minimum", GREEN),
                  ("15 + 15 days", "notice and reply", SKY)],
        "q": "Can pension be withheld for conduct after retirement? Who passes that order, and what process is due?",
        "q_say": "Sir, retirement ke baad ke conduct par pension rok sakte hain? Order kaun pass karta hai, aur process kya hai?",
        "rows": [
            ("7(1)(a) - THE CONDITION", "Future good conduct is an implied condition of every grant of pension and of its continuance under these rules. No separate bond is signed for it.", "Rule seven sub rule one clause a. Achha conduct pension ki implied condition hai, grant ke waqt bhi aur baad mein bhi. Alag se koi bond sign nahi karaya jaata, yeh condition apne aap lagi hui hai.", ORANGE, "EXAM"),
            ("7(1)(b) - WHO AND WHAT", "The Appointing Authority may, by order in writing, withhold or withdraw a pension or part of it, permanently or for a specified period, if the pensioner is convicted of a serious crime or found guilty of grave misconduct.", "Clause b. Appointing Authority likhit order se pension ya uska hissa rokh sakti hai ya withdraw kar sakti hai, hamesha ke liye ya ek period ke liye. Do grounds hain: serious crime mein conviction, ya grave misconduct. Authority Appointing Authority hai, President nahi.", RED, "EXAM"),
            ("7(1)(b) - THE FLOOR", "Proviso: where a part of pension is withheld or withdrawn, the pension cannot be reduced below the minimum pension under Rule 44. The reported figure is Rs 9,000 a month.", "Isi clause ka proviso floor deta hai. Jab pension ka kuch hissa roka jaaye, to pension Rule forty four ke minimum se neeche nahi ja sakti. Reported figure nau hazaar rupaye mahina hai, par latest O.M. se check kar lo.", GREEN, "EXAM"),
            ("7(2) - AFTER CONVICTION", "Where the pensioner is convicted by a Court of Law, action under sub-rule (1) is taken in the light of the judgment relating to that conviction.", "Sub rule two. Agar pensioner court se convicted ho gaya, to action court ke judgment ki roshni mein hoga. Matlab court ne kya kaha, woh dekho. Apni marzi se punishment ka size mat tay karo.", SKY, ""),
            ("7(3) - NO CONVICTION", "Where there is no conviction but grave misconduct is prima facie made out, a notice stating the proposed action and the grounds is served, with 15 days to reply, extendable by up to 15 more, and the reply must be considered.", "Sub rule three. Agar conviction nahi hai, par grave misconduct prima facie dikhta hai, to notice dena padega. Notice mein proposed action aur grounds likhe honge. Reply ke liye pandrah din, aur extend hokar pandrah din aur. Reply ko consider karna zaroori hai.", PINK, "EXAM"),
        ],
        "trap": "TRAP: Rule 7(1)(b) belongs to the Appointing Authority. Write President here and the answer is marked wrong.",
        "trap_say": "Sabse bada trap. Rule seven mein authority Appointing Authority hai. Yahan President likh diya to answer galat. President waala power Rule eight mein hai.",
    },
    {
        "id": "c17_rule7_rest",
        "chapter": "CHAPTER 17 - RULE 7(4) TO 7(7) AND THE EXPLANATION: SECRECY, UPSC AND APPEAL",
        "title": "Rule 7 - RTI Second Schedule Organisations, Format 1 Undertaking, UPSC and Appeal",
        "badge": "RULE 7(4)-(7)",
        "chips": [("Second Schedule", "RTI Act 2005", GREEN),
                  ("Format 1", "undertaking in duplicate", ORANGE),
                  ("Head of Org", "decides sensitivity", SKY),
                  ("President + UPSC", "order and appeal", RED)],
        "q": "Can a retired officer of a security organisation publish a book? Who decides, and what is the appeal route?",
        "q_say": "Sir, security organisation ka retired officer book likh sakta hai? Decision kaun leta hai, aur appeal kahan jaati hai?",
        "rows": [
            ("7(4)(a) - THE BAN", "No servant of an Intelligence or Security related organisation in the Second Schedule to the RTI Act, 2005 may publish material on its domain or on sensitive information without prior clearance from the Head of the Organisation.", "Sub rule four clause a. Jo employee RTI Act ke Second Schedule waali intelligence ya security organisation mein kaam kiya ho, woh organisation ke domain ya sensitive information par kuch publish nahi kar sakta, bina Head of the Organisation ki prior clearance ke.", GREEN, "EXAM"),
            ("7(4)(b) AND (c)", "Such servants give an undertaking in Format 1, and failure is grave misconduct. On transfer out it is taken in duplicate: one copy in the service book with an entry, the other kept by the organisation.", "Clause b aur c. Aise employees Format one mein undertaking dete hain, aur ise todna grave misconduct hai. Transfer hone par undertaking duplicate mein li jaati hai. Ek copy service book mein entry ke saath, doosri organisation ke record ke liye. Format one application nahi hai.", ORANGE, "EXAM"),
            ("7(5) AND 7(6)", "The Head of the Organisation decides whether proposed material is sensitive or non-sensitive and whether it falls in the domain. Where the competent authority is the President, the UPSC must be consulted before the order.", "Clause five aur six. Head of the Organisation decide karta hai material sensitive hai ya nahi, aur organisation ke domain mein aata hai ya nahi. Aur agar competent authority President hai, to order se pehle UPSC se consultation zaroori hai.", SKY, ""),
            ("7(7) - THE APPEAL", "An appeal against an order of any authority other than the President lies to the President, who passes such orders on the appeal as he deems fit, in consultation with the UPSC.", "Clause seven. President ke alawa kisi authority ka order ho, to appeal President ke paas jaati hai. President UPSC se consultation karke jo theek lage woh order pass karte hain. Yahan discretion President ka hai, par UPSC ki salah zaroori hai.", PINK, "EXAM"),
            ("THE EXPLANATION (a) TO (e)", "Pension includes family pension and pensioner includes family pensioner. Serious crime includes an Official Secrets Act offence. Grave misconduct includes disclosure of secret material. Publication and information are widely defined.", "Ab Explanation ke paanch hisse. Pension mein family pension aati hai, aur pensioner mein family pensioner. Serious crime mein Official Secrets Act ka offence. Grave misconduct mein secret material ka disclosure. Aur publication aur information ki wide definition hai.", PURPLE, "EXAM"),
        ],
        "trap": "TRAP: serious crime includes an offence under the Official Secrets Act, 1923. That definition sits in the Explanation, not in the main rule.",
        "trap_say": "Trap yeh hai ki serious crime mein Official Secrets Act nineteen twenty three ka offence bhi shaamil hai. Yeh definition Explanation mein hai, main rule mein nahi. Isliye Explanation padhna zaroori hai.",
    },
    {
        "id": "c18_rule7_vs_8",
        "chapter": "CHAPTER 18 - COMPARISON CHART: RULE 7 VERSUS RULE 8",
        "title": "Rule 7 or Rule 8? Six Points of Difference on One Chart",
        "badge": "RULE 7 vs 8",
        "chips": [("Rule 7", "conduct after retirement", ORANGE),
                  ("Rule 8", "misconduct in service", RED),
                  ("Appointing Authority", "Rule 7", GREEN),
                  ("President / Secy / C&AG", "Rule 8", SKY)],
        "q": "When a pensioner is punished, how do you decide whether Rule 7 or Rule 8 applies?",
        "q_say": "Sir, pensioner par action ho raha hai, to Rule seven lagega ya Rule eight? Decide kaise karein?",
        "kind": "table",
        "table": {
            "cols": ["Point", "Rule 7", "Rule 8"],
            "widths": [0.22, 0.39, 0.39],
            "rows": [
                ["Heading", "Pension and family pension subject to future good conduct", "Power to withhold or withdraw pension"],
                ["Trigger", "Conviction for a serious crime, or finding of grave misconduct", "Guilt for grave misconduct or negligence in departmental or judicial proceedings"],
                ["Authority", "Appointing Authority", "President, or Secretary of the Ministry, or C&AG, depending on the post's appointing authority"],
                ["What can be touched", "Pension or part of it; family pension is included", "Pension or gratuity or both, in full or in part, plus recovery of pecuniary loss"],
                ["UPSC", "Needed only where the President is the competent authority, and on appeal", "Needed before final orders where the President passes them, and on revision or review"],
                ["Appeal", "To the President, who decides with the UPSC", "No appeal from the President's order; other orders go to the President"],
                ["Same floor", "Part withholding cannot go below the Rule 44 minimum pension", "Part withholding cannot go below the Rule 44 minimum pension"],
            ],
        },
        "says": [
            "Dono rules ka pehla farq heading aur trigger ka hai. Rule seven achhe conduct ki condition par chalta hai, aur conviction ya grave misconduct par khulta hai. Rule eight service ke dauran misconduct ya negligence par chalta hai.",
            "Doosra farq authority ka hai. Rule seven mein Appointing Authority. Rule eight mein President, Secretary ya CAG, jo post ki appointing authority par depend karta hai.",
            "Teesra farq power ka hai. Rule seven sirf pension chhoota hai. Rule eight pension, gratuity ya dono, aur sarkar ka nuksaan bhi recover kar sakta hai.",
            "Aur ek cheez dono mein common hai: part withholding se pension Rule forty four ke minimum se neeche nahi ja sakti.",
        ],
        "trap": "TRAP: both rules share the same minimum-pension floor. If an answer says the floor applies only to Rule 8, it is half right.",
        "trap_say": "Trap yeh hai ki floor dono rules mein lagta hai. Agar answer mein likha ho ki floor sirf Rule eight par lagta hai, to woh aadha sahi hai.",
    },
    {
        "id": "c19_rule8_trigger",
        "chapter": "CHAPTER 19 - RULE 8(1) AND 8(6A): THE TRIGGER, THE THREE AUTHORITIES AND THE APPEAL",
        "title": "Rule 8(1) - The President's Reserved Power, Delegated to Three Authorities",
        "badge": "RULE 8(1)",
        "chips": [("Grave misconduct", "during service", ORANGE),
                  ("Or negligence", "pecuniary loss", SKY),
                  ("3 authorities", "post by post", GREEN),
                  ("No appeal", "from the President", RED)],
        "q": "Who can withhold or withdraw pension for misconduct in service, and can that order be appealed?",
        "q_say": "Sir, service ke dauran misconduct par pension kaun rok sakta hai, aur us order ki appeal hoti hai?",
        "rows": [
            ("8(1) - THE POWER", "The President reserves the right to withhold pension or gratuity or both, in full or in part, permanently or for a period, and to order recovery of the whole or part of any pecuniary loss caused to the Government.", "Rule eight sub rule one. President apne paas power rakhte hain pension ya gratuity, ya dono, poora ya hissa rokhne ka, pension withdraw karne ka, hamesha ya ek period ke liye, aur government ke nuksaan ki recovery ka order dene ka.", ORANGE, "EXAM"),
            ("8(1) - THE TRIGGER", "It must be a finding of grave misconduct or negligence during the period of service, in departmental or judicial proceedings, including service rendered on re-employment after retirement.", "Trigger clear hai. Departmental ya judicial proceedings mein grave misconduct ya negligence ka finding hona chahiye, aur woh service ke period ka ho, re employment ki service bhi shaamil hai. Finding ke bina order nahi.", SKY, "EXAM"),
            ("8(1) - THE FLOOR", "Second proviso: where a part of pension is withheld or withdrawn, the amount cannot fall below the minimum pension under Rule 44. First proviso: the UPSC must be consulted before final orders.", "Do proviso hain. Pehla, final order se pehle UPSC se consultation. Doosra, part withholding mein pension Rule forty four ke minimum se neeche nahi. Yeh do lines har answer mein likho.", GREEN, "EXAM"),
            ("8(6A) - THE APPEAL", "Introduced by G.S.R. 770(E) of 2022: no appeal lies against an order passed by the President. An order passed by any other authority is appealable to the President, who decides in consultation with the UPSC.", "Appeal ka rule. Twenty twenty two ke G.S.R. seven seven zero E ne clause six A joda. President ke order ke khilaaf koi appeal nahi. Kisi doosri authority ke order ke khilaaf appeal President ke paas, jo UPSC se consultation karke decide karte hain.", RED, "NEW"),
            ("WHO SITS IN THE CHAIR", "Since the 2022 amendment the power is exercised by the authority competent to appoint the post held: the President, the Secretary of the Ministry or Department, or the C&AG for the Indian Audit and Accounts Department.", "Kaun baithta hai chair par? Twenty twenty two ke amendment ke baad power us authority ke paas hai jo us post ki appointing authority hai. Teesre options hain: President, Ministry ya Department ka Secretary, ya Indian Audit and Accounts Department ke liye CAG. Isliye pehle post dekho, phir authority.", PURPLE, "FLAG"),
        ],
        "trap": "TRAP: the test is the appointing authority of the POST, not the rank of the officer who passed the order.",
        "trap_say": "Trap yeh hai ki test post ki appointing authority hai, order dene waale officer ka rank nahi. Isliye pehle post identify karo.",
    },
    {
        "id": "c20_rule8_procedure",
        "chapter": "CHAPTER 20 - RULE 8(2): WHEN PROCEEDINGS START, AND WHAT MUST BE IN THE FILE",
        "title": "Rule 8(2) - Continuing Proceedings, CCA Rule 16 and the Four-Year Bar",
        "badge": "RULE 8(2)",
        "chips": [("Deemed", "proceedings continue", ORANGE),
                  ("CCA Rule 16", "no effect on pension", RED),
                  ("4 years", "event limit", SKY),
                  ("Format 2 / 3", "sanction and charges", GREEN)],
        "q": "Proceedings began before retirement. Do they survive retirement? And what if they begin only after retirement?",
        "q_say": "Sir, retirement se pehle proceedings shuru hue the. Kya woh retirement ke baad chalenge? Aur agar baad mein shuru hon to?",
        "rows": [
            ("8(2)(a) - CONTINUATION", "Proceedings instituted in service, before retirement or during re-employment, are deemed to be under this rule after final retirement and are continued by the authority that began them, as if service had continued.", "Clause a. Jo proceedings service ke dauran shuru hue, retirement ya re employment ke dauran, woh final retirement ke baad bhi is rule ke under maane jaayenge. Unhi ko shuru karne waali authority continue karegi, jaise service khatam hi na hui ho.", ORANGE, "EXAM"),
            ("8(2)(a) - THE PROVISO", "Where proceedings were instituted by an authority subordinate to the President, that authority submits a report recording its findings, and the final decision is taken under sub-rule (1).", "Isi clause ka proviso. Agar proceedings President se neeche ki koi authority shuru karti hai, to woh apni findings ki report de degi, aur final decision sub rule one ke under hoga. Yeh wording twenty twenty two ke amendment se aayi.", PINK, "EXAM"),
            ("8(2)(b) - CCA RULE 16", "Departmental proceedings instituted under Rule 16 of the CCS (CCA) Rules, 1965 and continued after retirement have no effect on the pension and gratuity of the pensioner.", "Clause b bahut important hai. CCS CCA Rules ke Rule sixteen ke under shuru proceedings, jo retirement ke baad continue hote hain, pension aur gratuity par koi asar nahi daalte. Yeh rule pehle version mein reh gayi thi.", RED, "EXAM"),
            ("8(2)(c) - FRESH PROCEEDINGS", "If not instituted in service, proceedings need the sanction of the President in Format 2, cannot concern an event more than four years before institution, and are conducted by the authority and at the place the President directs.", "Clause c naye proceedings ke liye teen sharten. President ki sanction Format two mein. Woh event four saal se purana na ho. Aur proceedings us authority aur us jagah par ho jo President batayein. Teen sharten, ek bhi chhoot gayi to proceeding weak hai.", SKY, "EXAM"),
            ("8(2)(c) AND 8(2)(d) - PAPERWORK", "Charges are communicated in Format 3. If a full-fledged enquiry was held with a show-cause opportunity under the CCA Rules, no further show-cause is needed before action under sub-rule (1).", "Clause c ka proviso kehta hai charges Format three mein bheje jaayenge. Clause d kehta hai agar poora enquiry hua aur CCA Rules ke under show cause ka mauka mila, to sub rule one ke action se pehle dobara show cause ki zaroorat nahi.", GREEN, ""),
        ],
        "trap": "TRAP: Rule 16 of the CCA Rules is the exception that kills the case. Rule 14 proceedings continue; Rule 16 proceedings do not touch pension.",
        "trap_say": "Yeh trap exam mein aata hai. CCA ke Rule fourteen ke proceedings continue hote hain, par Rule sixteen ke proceedings pension ko chhoote nahi. Number yaad rakho, fourteen haan, sixteen nahi.",
    },
    {
        "id": "c21_rule8_provisional",
        "chapter": "CHAPTER 21 - RULE 8(3) TO 8(5): PROVISIONAL PENSION AND THE NO-RECOVERY RULE",
        "title": "Rule 8(3) to (5) - Provisional Pension, No Gratuity, and What Happens on Conclusion",
        "badge": "RULE 8(3)-(5)",
        "chips": [("Provisional", "maximum admissible", GREEN),
                  ("No gratuity", "until final order", RED),
                  ("Contemplated only", "full pension", ORANGE),
                  ("No recovery", "if final is lower", SKY)],
        "q": "What does the pensioner get while proceedings are pending, and what happens when final orders are passed?",
        "q_say": "Sir, proceedings pending hain to pensioner ko kya milta hai, aur final order ke baad kya hota hai?",
        "rows": [
            ("8(3) - WHEN IT APPLIES", "Where departmental or judicial proceedings are instituted against a pensioner, or CCA Rule 14 proceedings continue under sub-rule (2), provisional pension under sub-rule (4) must be sanctioned.", "Sub rule three. Jab pensioner ke khilaaf departmental ya judicial proceedings shuru hain, ya CCA Rule fourteen ke proceedings continue ho rahe hain, to sub rule four waali provisional pension sanction karni hi hogi. Yeh optional nahi hai.", GREEN, "EXAM"),
            ("8(4)(a) - THE AMOUNT", "The Accounts Officer authorises provisional pension equal to the maximum admissible on qualifying service up to retirement, or if he was under suspension that day, up to the day before suspension.", "Clause a amount batata hai. Accounts Officer provisional pension authorize karta hai, jo retirement tak ki qualifying service par maximum pension banti ho. Aur agar retirement ke din suspension mein tha, to suspension se pehle waale din tak.", ORANGE, "EXAM"),
            ("8(4)(b) AND 8(4)(c)", "It runs from the day after retirement until final orders are passed. No gratuity is paid until the proceedings conclude and final orders are issued.", "Clause b aur c. Payment retirement ke agle din se shuru, aur final order aane tak chalti hai. Gratuity tab tak nahi milegi jab tak proceedings khatam hokar final order na aa jaaye.", RED, "EXAM"),
            ("8(4)(d) - THE EXCEPTION", "Where misconduct is only under investigation, or proceedings are merely contemplated and not instituted or deemed instituted, this sub-rule does not apply: full pension and gratuity are authorised under Rule 63.", "Clause d exception hai. Jab sirf investigation chal rahi ho, ya proceedings sirf sochay gaye hain par shuru nahi hue, to provisional pension waala sub rule lagu nahi hota. Aise case mein poori pension aur gratuity Rule sixty three se authorize hoti hai.", SKY, "EXAM"),
            ("8(5) - THE ADJUSTMENT", "Provisional pension is adjusted against the final benefits, but no recovery is made where the pension finally sanctioned is lower than the provisional pension, or where pension is reduced or withheld.", "Sub rule five adjustment ka rule hai. Provisional pension final benefit ke against adjust hoti hai. Lekin agar final pension provisional se kam nikli, ya pension reduce ya withhold hui, to recovery nahi hogi. Yeh protection pehle version mein nahi tha.", PINK, "EXAM"),
        ],
        "trap": "TRAP: 'contemplated' is not 'instituted'. The moment a charge sheet is issued the provisional-pension regime begins, not before.",
        "trap_say": "Trap yeh hai ki contemplated aur instituted alag hain. Sirf chaar diwaari mein sochna kaafi nahi. Charge sheet issue hui, tab provisional pension waala regime shuru hoga.",
    },
    {
        "id": "c22_rule8_revision",
        "chapter": "CHAPTER 22 - RULE 8(6) TO 8(8), THE EXPLANATIONS AND THE MISSING SUB-RULE (9)",
        "title": "Rule 8 - One-Third Recovery Limit, Revision, Review and Four Explanations",
        "badge": "RULE 8(6)-(8)",
        "chips": [("One-third", "recovery ceiling", ORANGE),
                  ("Revision", "8(7) with UPSC", GREEN),
                  ("Review", "8(8) new material", SKY),
                  ("Sub-rule (9)", "cross-reference anomaly", RED)],
        "q": "How much can be recovered from pension, and can the President reopen a decided case?",
        "q_say": "Sir, pension se kitna recover kar sakte hain, aur kya President decided case dobara khol sakte hain?",
        "rows": [
            ("8(6) AND 8(9)", "Where the President does not withhold pension but orders recovery of a pecuniary loss, recovery shall not ordinarily exceed one-third of the pension admissible on retirement. Every Rule 8 order must be communicated.", "Sub rule six aur nine. Agar President pension rokne ka faisla nahi karte, par nuksaan ki recovery ka order dete hain, to recovery retirement date ki pension ke ek tihai se zyada nahi hogi. Aur Rule eight ka har order pensioner ko communicate karna zaroori hai. Ek tihai aur communication, dono yaad rakho.", ORANGE, "EXAM"),
            ("8(7) - REVISION AND ITS GUARD", "The President may call for the records of any inquiry and revise any order under these rules after consulting the UPSC, and may confirm, modify, set aside or remit it. No order enhancing the amount withheld, in revision or review, without a reasonable opportunity of representation.", "Sub rule seven. President kisi inquiry ka record mangwa kar, UPSC se consultation ke baad, order revise kar sakte hain. Confirm, modify, set aside ya case wapas. Aur revision ya review mein withheld amount badhana hai to employee ko representation ka reasonable mauka dena hoga.", GREEN, "EXAM"),
            ("8(8) - REVIEW", "The President may review any order where extenuating or special circumstances exist, or where new material that could not be produced earlier and that changes the nature of the case has come to notice.", "Sub rule eight review ka hai. President order review kar sakte hain jab koi special ya extenuating circumstance ho, ya naya material mile jo pehle pesh nahi ho sakta tha aur case ki nature badal deta ho. Sirf badalna kaafi nahi, nature badalna chahiye.", SKY, ""),
            ("THE EXPLANATIONS (1) TO (4)", "1: when departmental and judicial proceedings are deemed instituted. 2: misconduct. 3: three situations in which action may be taken. 4: civil proceedings means a civil suit filed by the Government only.", "Chaar Explanation. Pehla, proceedings kab instituted maane jaayenge. Doosra, misconduct kya hai. Teesra, teen situations jahan action ho sakta hai. Chautha, civil proceedings ka matlab sirf government ki filed civil suit. Yeh definitions answer mein marks deti hain.", PINK, "EXAM"),
            ("THE SUB-RULE (9) ANOMALY", "Rule 8(4)(d) refers to proceedings deemed instituted in accordance with sub-rule (9), but the printed Rule 8 ends at sub-rule (8) before the Explanation. Flag it as a drafting cross-reference; do not invent a sub-rule (9).", "Ab ek audit finding. Rule eight ke clause four d mein sub rule nine ka reference hai. Lekin chhape hue rule mein sub rule eight ke baad Explanation shuru ho jaata hai. Isliye ise drafting cross reference likho, aur apne mann se sub rule nine mat banao.", YELLOW, "FLAG"),
        ],
        "trap": "TRAP: one-third is a rate limit on RECOVERY, not a limit on withholding. Withholding is governed by the minimum-pension floor instead.",
        "trap_say": "Trap yeh hai ki ek tihai recovery ki rate ka limit hai, withholding ka nahi. Withholding par Rule forty four ke minimum pension ka floor lagta hai. Dono limit alag hain.",
    },
]


SCENES += [
    {
        "id": "c23_rule9_entry",
        "chapter": "CHAPTER 23 - RULE 9(1) AND 9(2): COMMERCIAL EMPLOYMENT WITHIN ONE YEAR OF RETIREMENT",
        "title": "Rule 9 - The One-Year Window, Two Provisos, and Form 1",
        "badge": "RULE 9(1)-(2)",
        "chips": [("Group A", "central service", ORANGE),
                  ("1 year", "from retirement", SKY),
                  ("Form 1", "application", GREEN),
                  ("2 provisos", "LPR and negotiation", PINK)],
        "q": "Who needs permission to take a commercial job after retirement, and for how long does the restriction run?",
        "q_say": "Sir, retirement ke baad commercial job ke liye permission chahiye ya nahi, aur kitne samay tak?",
        "rows": [
            ("9(1) - WHO AND WHEN", "A pensioner who, immediately before retirement, was a member of Central Service Group A, and who wishes to accept commercial employment before one year from retirement, needs the previous sanction of the Government.", "Rule nine sub rule one. Agar pensioner retirement se pehle Central Service Group A ka member tha, aur retirement se ek saal ke andar commercial employment lena chahta hai, to government ki previous sanction chahiye. Group A important hai, har pensioner par nahi.", ORANGE, "EXAM"),
            ("9(1) - THE FORM", "The application is made in Form 1. The one-year clock runs from the date of retirement, and it is a window for prior permission, not a waiting period after which the job becomes free.", "Application Form one mein hoti hai. Ek saal ka clock retirement ki date se chalta hai. Yeh prior permission ke liye window hai, aisa nahi ki ek saal ruk gaye to job free ho gayi. Window ke andar bhi permission chahiye.", SKY, "EXAM"),
            ("FIRST PROVISO - LPR", "A servant already permitted by the Government to take a particular commercial employment during leave preparatory to retirement or refused leave needs no fresh permission to continue in it.", "Pehla proviso chhoot deta hai. Agar employee ko leave preparatory to retirement ke dauran, ya refused leave mein, kisi particular commercial employment ki permission mil chuki thi, to retirement ke baad usi job ko continue karne ke liye nayi permission nahi chahiye.", GREEN, "EXAM"),
            ("SECOND PROVISO - NEGOTIATION", "A servant shall not negotiate for commercial employment during service without the prior permission of the administrative Ministry or Department, and such permission shall not be given unless there are special reasons.", "Doosra proviso negotiation par rok lagata hai. Service ke dauran commercial employment ke liye baat karna hai, to administrative Ministry ya Department ki prior permission chahiye. Aur woh permission sirf special reasons par milegi. Yeh naya point hai.", PINK, "EXAM"),
            ("9(2) - GRANT OR REFUSE", "The Government may, by written order, grant permission subject to conditions, or refuse it for reasons recorded in the order. Both outcomes must be reasoned.", "Sub rule two. Government likhit order se permission de sakti hai, conditions ke saath, ya refuse kar sakti hai. Refusal ke reasons order mein likhne padenge. Isliye order mein reasoning ka hona zaroori hai.", BLUE, ""),
        ],
        "trap": "TRAP: the second proviso punishes negotiation, not appointment. Talks during service need permission even if no job is ever taken.",
        "trap_say": "Trap yeh hai ki doosra proviso negotiation ko pakadta hai, appointment ko nahi. Service ke dauran baat karna bhi permission maangta hai, chahe job kabhi li hi na ho.",
    },
    {
        "id": "c24_rule9_definition",
        "chapter": "CHAPTER 24 - THE RULE 9 EXPLANATION: WHAT 'COMMERCIAL EMPLOYMENT' ACTUALLY MEANS",
        "title": "Defining Commercial Employment - Employment, Directorship, Partnership and Practice",
        "badge": "EXPL. TO RULE 9",
        "chips": [("Any capacity", "agent too", ORANGE),
                  ("Directorship", "included", SKY),
                  ("Govt body", "excluded", GREEN),
                  ("Practice", "3 sub-clauses", RED)],
        "q": "What counts as commercial employment? Does a directorship count? Does consultancy count?",
        "q_say": "Sir, commercial employment kya hai? Directorship aata hai? Consultancy aati hai?",
        "rows": [
            ("EXPL. (a)(i) - THE EMPLOYMENT", "Employment in any capacity, including as an agent, under a company, co-operative society, firm or individual engaged in trading, commercial, industrial, financial or professional business.", "Explanation a(i). Kisi bhi capacity mein employment, agent ke roop mein bhi, aisi company, cooperative society, firm ya individual ke under jo trading, commercial, industrial, financial ya professional business karte hain. Capacity ka matlab, chhoti-si role bhi count hogi.", ORANGE, "EXAM"),
            ("EXPL. (a)(i) - SOCIETY AND DIRECTORSHIP", "Holding any office in a co-operative society counts, elective or otherwise, such as President, Chairman, Manager, Secretary or Treasurer. Directorship of such a company and partnership of such a firm also count.", "Society mein koi bhi office ho, chuna hua ya nominated, President, Chairman, Manager, Secretary, Treasurer, sab count honge. Aisi company ki directorship bhi commercial employment hai, aur firm ki partnership bhi. Yeh pehle version mein nahi tha.", SKY, "EXAM"),
            ("EXPL. (a)(i) - THE CARVE-OUT", "Employment under a body corporate wholly or substantially owned or controlled by the Central Government or a State Government is NOT commercial employment.", "Ab carve out. Aisi body corporate ke under employment jo poori tarah ya substantially Central ya State government ki owned ya controlled ho, woh commercial employment nahi hai. Isliye PSU mein job Rule nine ke daayre se bahar hai.", GREEN, "EXAM"),
            ("EXPL. (a)(ii) - PRACTICE", "Practice as adviser or consultant, alone or as a partner, is caught in three cases: (A) no professional qualification and official knowledge is used; (B) clients gain an unfair advantage; (C) liaison with Government offices.", "Explanation a(ii). Practice ya consultancy, akela ya firm ke partner ke roop mein, teen cases mein commercial employment hai. A: professional qualification nahi, aur official knowledge use ho raha hai. B: clients ko unfair advantage milega. C: government offices se liaison hai. Koi ek bhi lage to Rule nine lagta hai.", RED, "EXAM"),
            ("EXPL. (b) - DATE OF RETIREMENT", "Where a servant is re-employed without a break in the same or another Group A post under the Government or an equivalent State post, date of retirement means the date he finally ceases to be so re-employed.", "Explanation b date of retirement define karti hai. Agar banda bina break re employ hua, usi ya doosri Group A post par, ya State mein equivalent post par, to date of retirement woh date hogi jab woh aakhri baar re employment se free hota hai. Isse ek saal ka clock aage khisak jaata hai.", PINK, "EXAM"),
        ],
        "trap": "TRAP: consultancy is not automatically outside Rule 9. Sub-clause (C) catches liaison work even for a qualified professional.",
        "trap_say": "Trap yeh hai ki consultancy apne aap Rule nine se bahar nahi hai. Sub clause C kehta hai agar kaam mein government se liaison hai, to woh andar aayega, chahe qualification ho.",
    },
    {
        "id": "c25_rule9_factors",
        "chapter": "CHAPTER 25 - RULE 9(3): THE SEVEN FACTORS, AND THE TWO EXPLANATIONS HIDDEN IN THEM",
        "title": "Rule 9(3) - Seven Factors the Government Must Weigh Before Granting Permission",
        "badge": "RULE 9(3)(a)-(g)",
        "chips": [("7 factors", "clauses (a) to (g)", ORANGE),
                  ("NOC", "cadre + office", SKY),
                  ("3 years", "sensitive info", GREEN),
                  ("2 Explanations", "conflict and pay", PINK)],
        "q": "What does the Government actually look at before granting or refusing permission?",
        "q_say": "Sir, permission dene ya refuse karne se pehle government asal mein kya dekhti hai?",
        "kind": "table",
        "table": {
            "cols": ["Clause", "Factor", "What the officer must show"],
            "widths": [0.09, 0.36, 0.55],
            "rows": [
                ["(a)", "No Objection", "NOC from the cadre controlling authority and from the office where he retired."],
                ["(b)", "Sensitive or strategic information", "Nothing in the last three years of service relates to the new employer's work or his practice area."],
                ["(c)", "Conflict of interest", "No clash between the policies of his last three years and the interests of the new organisation. Explanation: normal economic competition is not conflict of interest."],
                ["(d)", "Hostile organisation", "The employer is not in conflict with India's foreign relations, national security or domestic harmony, and does no intelligence gathering."],
                ["(e)", "Service record", "Clear record, particularly on integrity and dealings with non-Government organisations."],
                ["(f)", "Pay above industry", "Emoluments are not far in excess of industry standards. Explanation: buoyancy in the industry or economy is not 'far in excess'."],
                ["(g)", "Any other factor", "Anything else the administrative Ministry knows, or any specific DoPT instruction in force."],
            ],
        },
        "says": [
            "Rule nine sub rule three mein saat factors hain. Pehla, cadre controlling authority aur retirement office se No Objection. Doosra, last three years mein sensitive ya strategic information mili ya nahi, jo naye employer ke kaam se related ho.",
            "Teesra, conflict of interest. Yahan Explanation kehti hai ki normal economic competition conflict of interest nahi hai. Chautha, kya employer India ke foreign relations, national security ya domestic harmony ke khilaaf hai, ya intelligence gathering karta hai.",
            "Paanchva, service record clear ho, khaaskar integrity aur NGOs ke dealings mein. Chhatha, pay industry se bahut zyada na ho. Yahan bhi Explanation kehti hai ki industry ya economy ki buoyancy ko far in excess mat samjho.",
            "Saatva, koi bhi doosra relevant factor jo Ministry ke knowledge mein ho, ya DoPT ki specific instruction ho.",
        ],
        "trap": "TRAP: the two Explanations are always worth marks - normal economic competition and industry buoyancy are both expressly excluded.",
        "trap_say": "Yeh do Explanation marks laati hain. Normal economic competition conflict of interest nahi hai, aur industry ki buoyancy far in excess nahi hai. Answer mein likho.",
    },
    {
        "id": "c26_rule9_procedure",
        "chapter": "CHAPTER 26 - RULE 9(4) TO 9(9): CHECKLIST, LIBERAL GRANTS, 30 DAYS AND BREACH",
        "title": "Rule 9 - Form 2 Checklist, Liberal Grants, the 30-Day Representation and Breach",
        "badge": "RULE 9(4)-(9)",
        "chips": [("ToB Rules 1961", "processing", SKY),
                  ("Form 2", "checklist", ORANGE),
                  ("30 days", "representation", GREEN),
                  ("Breach", "pension cut", RED)],
        "q": "How is an application processed, when should permission be liberal, and what is the penalty for a breach?",
        "q_say": "Sir, application process kya hai, permission kab liberal honi chahiye, aur breach par kya hota hai?",
        "rows": [
            ("9(4) AND 9(5) - PROCESS", "Applications are considered under the Government of India (Transaction of Business) Rules, 1961 and the instructions issued from time to time. The Ministry maintains a check list in Form 2.", "Sub rule four aur paanch. Applications Government of India Transaction of Business Rules nineteen sixty one aur time to time instructions ke hisaab se dekhi jaati hain. Ministry Form two mein checklist maintain karti hai. Form two government ka internal document hai, employee ki application nahi.", SKY, ""),
            ("9(6) - LIBERAL GRANTS", "Where no clause (b) to (g) factor disqualifies him, the Government may liberally grant directorship, consultancy or professional practice, encourage scientific and cultural work, and treat honorary, paid and self-employment alike.", "Sub rule six kehta hai jab pensioner clause b se g tak disqualified nahi hai, to government liberally permission de sakti hai. Directorship, consultancy ya professional practice, scientific ya cultural kaam, non government sector ki responsible posts. Aur honorary aur paid ya self employment mein farq nahi karegi. Yeh chaar sub clauses pehle version mein nahi the.", GREEN, "EXAM"),
            ("9(7) - THIRTY DAYS", "If permission is granted with conditions or refused, the applicant may represent within thirty days of receiving the order. Proviso: no worse order without a show cause.", "Sub rule seven. Agar permission conditions ke saath mili ya refuse hui, to applicant thirty din ke andar representation de sakta hai. Government jo theek lage order karegi. Proviso kehta hai, kharab order dene se pehle show cause dena padega.", ORANGE, "EXAM"),
            ("9(8) - BREACH", "Taking commercial employment within a year without permission, or breaching a condition, lets the Government declare by reasoned order that pension is not payable in whole or part for stated periods, after a show cause.", "Sub rule eight penalty ka hai. Bina permission ek saal ke andar job lena, ya condition todna. Government likhit order se keh sakti hai ki pension ka poora ya hissa, ek period ke liye, band. Par show cause ke bina nahi. Aur teen cheezein dekhni padengi: pensioner ki financial condition, job ki nature aur emoluments, aur koi doosra factor.", RED, "EXAM"),
            ("9(9) - COMMUNICATION", "Every order passed by the Government under Rule 9 must be communicated to the pensioner concerned. An uncommunicated order cannot be enforced against him.", "Sub rule nine chhota par important hai. Rule nine ke under har order pensioner ko communicate karna zaroori hai. Jo order communicate hi nahi hua, usko pensioner ke khilaaf enforce nahi kar sakte. Yeh pehle version mein nahi tha.", PINK, "EXAM"),
        ],
        "trap": "TRAP: Rule 9(8) allows a cut in pension for a period. It is not a recovery order, and it is not a Rule 8 withholding order.",
        "trap_say": "Trap yeh hai ki Rule nine ka penalty pension ka period cut hai. Woh recovery order nahi hai, aur Rule eight ka withholding order bhi nahi. Teen cheezein alag hain, inhe mix na karo.",
    },
    {
        "id": "c27_rule10",
        "chapter": "CHAPTER 27 - RULE 10: EMPLOYMENT AFTER RETIREMENT UNDER A GOVERNMENT OUTSIDE INDIA",
        "title": "Rule 10 - No One-Year Limit, No Form, and Pension Stops for the Period Employed",
        "badge": "RULE 10",
        "chips": [("No time limit", "unlike Rule 9", ORANGE),
                  ("Central Govt", "previous permission", SKY),
                  ("No pension", "for the period", RED),
                  ("Or longer", "as Govt directs", PINK)],
        "q": "A Group A pensioner wants a job under a foreign Government two years after retirement. Does Rule 9 apply?",
        "q_say": "Sir, Group A pensioner ko retirement ke do saal baad videshi government ke under job chahiye. Rule nine lagega?",
        "rows": [
            ("10(1) - THE RULE", "A pensioner who immediately before retirement was a member of Central Service Group A and wishes to accept employment under any Government outside India needs the previous permission of the Central Government.", "Rule ten sub rule one. Agar pensioner retirement se pehle Central Service Group A ka member tha, aur kisi videshi government ke under employment lena chahta hai, to Central Government ki previous permission chahiye. Yahan koi form number nahi diya gaya.", ORANGE, "EXAM"),
            ("10(1) - THE CONSEQUENCE", "No pension is payable to a pensioner who accepts such employment without proper permission, for the period for which he is so employed, or for such longer period as the Government may direct.", "Consequence clear hai. Bina permission aisi employment li, to us period ki pension nahi milegi. Aur government chahe to usse zyada lamba period bhi direct kar sakti hai. Yeh such longer period pehle version mein nahi tha.", RED, "EXAM"),
            ("THE PROVISO - LPR", "A servant permitted by the Central Government to take up a particular form of employment under a Government outside India during leave preparatory to retirement need not obtain subsequent permission to continue after retirement.", "Proviso wahi LPR relief deta hai. Agar leave preparatory to retirement ke dauran kisi particular employment ki permission mil gayi thi, to retirement ke baad usi ko continue karne ke liye nayi permission nahi chahiye.", GREEN, ""),
            ("10(2) - HOW CONSIDERED", "The request is considered in accordance with the Government of India (Transaction of Business) Rules, 1961 and the instructions issued from time to time. The DoPPW O.M. of 30.10.2025 restates this.", "Sub rule two. Request Government of India Transaction of Business Rules nineteen sixty one aur time to time instructions ke hisaab se dekhi jaayegi. Thirty October two thousand twenty five ka O.M. yahi baat dohrata hai, naya rule nahi deta.", SKY, "FLAG"),
            ("9 VERSUS 10 - THE SHORT CUT", "Rule 9: one-year window, Form 1, negotiation limb, commercial employer. Rule 10: no time limit, no form, no negotiation limb, a foreign Government as employer.", "Short cut yaad rakho. Rule nine: ek saal ki window, Form one, negotiation clause, commercial employer. Rule ten: koi time limit nahi, koi form nahi, negotiation clause nahi, aur employer videshi government. Do minute mein decide ho jaata hai.", PURPLE, "EXAM"),
        ],
        "trap": "TRAP: the Rule 9 one-year limit does not save a Rule 10 case. A foreign Government job needs permission five years later as well.",
        "trap_say": "Trap yeh hai ki Rule nine ka ek saal Rule ten ko bachata nahi. Videshi government ki job ke liye paanch saal baad bhi permission chahiye.",
    },
]


SCENES += [
    {
        "id": "c28_time_limits",
        "chapter": "CHAPTER 28 - CHART: EVERY TIME LIMIT AND THRESHOLD INSIDE RULES 1 TO 10",
        "title": "Time Limits on One Scale - From 15 Days to Four Years",
        "badge": "TIME LIMITS",
        "chips": [("15 + 15", "Rule 7(3)", ORANGE),
                  ("30 days", "Rule 9(7)", SKY),
                  ("6 months", "Rule 4 option", GREEN),
                  ("1 / 3 / 4 yrs", "Rules 9, 9(3), 8(2)", RED)],
        "q": "Can you place every time limit in Rules 1 to 10 on a single scale?",
        "q_say": "Sir, Rules one se ten tak ke saare time limits ek scale par dikha do?",
        "kind": "bars",
        "bars": {
            "items": [
                ("Rule 7(3) - notice reply, extendable by 15 more", 15, "15 days", "DAYS"),
                ("Rule 9(7) - representation against a refusal", 30, "30 days", "DAYS"),
                ("Rule 4 - option against a transfer, or return from leave", 183, "6 months", "MONTHS"),
                ("Rule 9(1) - commercial employment window", 365, "1 year", "YEARS"),
                ("Rule 9(3)(b) - sensitive information look-back", 1095, "3 years", "YEARS"),
                ("Rule 8(2)(c)(ii) - no event older than", 1460, "4 years", "YEARS"),
            ],
        },
        "says": [
            "Ab poore batch ke time limits ek scale par. Sabse chhota pandrah din. Rule seven sub rule three ka notice reply period, jo pandrah din aur badh sakta hai.",
            "Uske baad tees din. Rule nine sub rule seven ki representation, jab permission refuse ho ya conditions ke saath mili ho.",
            "Phir chhah mahine. Rule four ka option, transfer order se ya leave se wapsi se, jo baad mein aaye.",
            "Ek saal. Rule nine ki commercial employment window. Teen saal, Rule nine ke sensitive information look back. Aur chaar saal, Rule eight mein event ki outer limit.",
            "Yeh scale exam mein answer sheet ke margin mein likh lo, revision ek nazar mein ho jaayega.",
        ],
        "trap": "TRAP: six months is not one year. Rule 4's option and Rule 9's window are different clocks for different purposes.",
        "trap_say": "Trap yeh hai ki chhah mahine aur ek saal alag hain. Rule four ka option aur Rule nine ki window alag clock hain, alag maqsad ke liye.",
    },
    {
        "id": "c29_amendments",
        "chapter": "CHAPTER 29 - CHART: THE BASE NOTIFICATION AND FOUR AMENDMENTS THAT TOUCH RULES 1 TO 10",
        "title": "Which Notification Changed Which Rule - and Which Ones to Quote Carefully",
        "badge": "AMENDMENTS",
        "chips": [("868(E)", "20.12.2021 base", BLUE),
                  ("770(E)", "07.10.2022", ORANGE),
                  ("410(E)", "16.07.2024 Form 6-A", GREEN),
                  ("340(E) / 775(E)", "2025 / 2026", PINK)],
        "q": "Which amendments matter for Rules 1 to 10, and which figures in this batch are unverified?",
        "q_say": "Sir, Rules one se ten ke liye kaunse amendments important hain, aur kaunse figures unverified hain?",
        "kind": "table",
        "table": {
            "cols": ["Notification", "Date", "What it does", "Confidence"],
            "widths": [0.17, 0.13, 0.50, 0.20],
            "rows": [
                ["G.S.R. 868(E)", "20.12.2021", "Base rules, 87 rules and 14 chapters; Rules 1 to 10 sit here.", "Gazette read"],
                ["G.S.R. 770(E)", "07.10.2022", "Rule 8(1) replaced (three authorities), proviso to 8(2)(a) replaced, new 8(6A) appeal bar, plus at least ten textual changes across the rules.", "Summary read"],
                ["G.S.R. 410(E)", "16.07.2024", "Form 6-A replaces Form 6 and the retiree's nomination Form A; Rules 57, 58, 63(4) and 80(5) aligned. Applies to retirees from 16.11.2024.", "Partly read"],
                ["G.S.R. 340(E)", "22.05.2025", "Rule 37(29)(c): PSU dismissal or removal after absorption can forfeit Government-service benefits. Outside Rules 1-10 but quoted with Rule 8.", "One source"],
                ["G.S.R. 775(E)", "Sept 2026", "Adds a proviso under Rule 37(7) for certain ex-Ordnance Factory Board employees. Date garbled in the copy read.", "Flagged"],
                ["O.M. 22.06.2026", "22.06.2026", "Compassionate appointments: crucial date is the date of application. Explains the Rule 2 cut-off, does not amend it.", "Press text"],
            ],
        },
        "says": [
            "Base notification G.S.R. eight six eight E, twenty December two thousand twenty one. Isi mein eighty seven rules aur fourteen chapters hain, aur Rules one se ten yahin baithe hain.",
            "Twenty twenty two ka G.S.R. seven seven zero E Rule eight ko chhoota hai. Sub rule one replace hua, teen authorities aayi, clause two a ki proviso badli, aur clause six A joda gaya jisme President ke order ki appeal band ho gayi.",
            "Twenty twenty four ka G.S.R. four one zero E Form six A laata hai. Form six aur nomination Form A ek ho gaye, aur sixteen November two thousand twenty four se retire hone waalon par lagu.",
            "Twenty twenty five ka G.S.R. three four zero E Rule thirty seven ko chhoota hai, jo is batch se bahar hai, par Rule eight ke saath quote hota hai. Aur twenty twenty six ka G.S.R. seven seven five E Rule thirty seven sub rule seven mein proviso jodta hai. Iski exact date copy mein clear nahi thi, isliye flagged hai.",
        ],
        "trap": "TRAP: a new form is not a new rule. Form 6-A changed paperwork; it did not change the pension formula in Rule 44.",
        "trap_say": "Trap yeh hai ki naya form naya rule nahi hota. Form six A ne paperwork badla, Rule forty four ka pension formula nahi.",
    },
    {
        "id": "c30_currency",
        "chapter": "CHAPTER 30 - CURRENCY NOTE: FIGURES, DATES AND WHAT COULD NOT BE VERIFIED",
        "title": "How Current Is This Batch? Dearness Relief, Minimum Pension and Open Flags",
        "badge": "CURRENCY",
        "chips": [("DR 60%", "from 01.01.2026", GREEN),
                  ("Rs 9,000", "reported floor", ORANGE),
                  ("Check date", "24.10.2026", SKY),
                  ("Flags", "what is unread", RED)],
        "q": "Which numbers in this batch are settled, and which ones must be re-checked before an exam or an office note?",
        "q_say": "Sir, is batch mein kaunse numbers pakke hain, aur kaunse dobara check karne chahiye?",
        "rows": [
            ("DEARNESS RELIEF", "DR is 60 per cent with effect from 01.01.2026, per the Department of Expenditure O.M. of 22.04.2026. A July 2026 revision had not been announced as of the last check.", "Dearness relief sixty percent, pehla January two thousand twenty six se, Department of Expenditure ke twenty two April two thousand twenty six ke O.M. se. July two thousand twenty six ki revision last check tak announce nahi hui thi. Exam se pehle latest O.M. dekh lo.", GREEN, "NEW"),
            ("MINIMUM PENSION", "The floor under Rule 44 is reported at Rs 9,000 a month. Rule 44 itself was not read in this batch, and the 8th Pay Commission had not reported.", "Minimum pension Rule forty four ke under nau hazaar rupaye mahina reported hai. Lekin is batch mein Rule forty four padha nahi gaya, aur eighth Pay Commission ki report bhi nahi aayi. Isliye ise reported figure likho, guaranteed na likho.", ORANGE, "FLAG"),
            ("WHAT THIS BATCH DID READ", "Gazette text of Rules 1 to 10, Forms 1 to 3, the 2022 and 2024 amendments and the two 2025 O.M.s. Everything on the cards is a close restatement of that text.", "Is batch mein kya padha gaya? Rules one se ten ka Gazette text, Form one se teen, twenty twenty two aur twenty twenty four ke amendments, aur twenty twenty five ke do O.M. Cards par jo likha hai, woh usi text ka close restatement hai.", SKY, "EXAM"),
            ("WHAT IT DID NOT READ", "Rule 87 verbatim, the NPS Rules beyond Rule 10, the CCS (Extraordinary Pension) Rules 2023, the Unified Pension Scheme Rules 2025, and the exact date of G.S.R. 775(E).", "Kya nahi padha gaya? Rule eighty seven poora, NPS Rules sirf Rule ten tak, Extraordinary Pension Rules two thousand twenty three, Unified Pension Scheme Rules two thousand twenty five, aur G.S.R. seven seven five E ki exact date. Yeh flags honest rakho.", RED, "FLAG"),
            ("HOW TO QUOTE", "Quote a rule number only for what the rule says. Use a separate sentence for an O.M., a form or a case law, so that a change in the O.M. never falsifies the rule statement.", "Quoting ka tarika. Rule number sirf usi baat ke liye do jo rule mein likhi hai. O.M., form ya case law ke liye alag sentence banao. Isse O.M. badalne par tumhara rule statement galat nahi hoga.", PURPLE, "EXAM"),
        ],
        "trap": "TRAP: 'reported Rs 9,000' and 'Rs 9,000 under Rule 44' are not the same sentence. Keep the hedge where the source is secondary.",
        "trap_say": "Trap yeh hai ki reported nau hazaar aur Rule forty four ke under nau hazaar, dono ek sentence nahi hain. Jahan source secondary hai, wahan hedge rakho.",
    },
    {
        "id": "c31_recap",
        "chapter": "CHAPTER 31 - RECAP: RULES 1 TO 10 IN ONE SCREEN",
        "title": "Batch 1 Recap - Numbers, Authorities and the Ten Traps That Decide Marks",
        "badge": "RECAP",
        "chips": [("26 chapters", "this batch", ORANGE),
                  ("Rules 1-10", "Chapters I and II", SKY),
                  ("10 traps", "revision list", RED),
                  ("Next", "Batch 2: Rules 11-30", GREEN)],
        "q": "If you have only two minutes before the paper, what should you revise from Rules 1 to 10?",
        "q_say": "Sir, paper se pehle do minute hain, Rules one se ten se kya revise karein?",
        "rows": [
            ("THE SKELETON", "Rule 1 name and date. Rule 2 application and one Explanation with six limbs. Rule 3 twenty-six definitions plus the FR 1922 fallback. Rules 4 to 10 complete Chapters I and II.", "Skeleton yaad rakho. Rule one naam aur date. Rule two application aur ek Explanation ke chhah limb. Rule three chhabbis definitions, a se z, aur sub rule two mein FR nineteen twenty two ka fallback. Rule four se ten Chapter one aur two mein hain.", ORANGE, "EXAM"),
            ("THE NUMBERS", "Cut-off 31.12.2003; 8 exclusions; 6 limbs; 26 definitions; 6 months (Rule 4); 15+15 days (7(3)); 30 days (9(7)); 1 year (9(1)); 3 years (9(3)(b)); 4 years (8(2)(c)(ii)); one-third recovery cap (8(6)).", "Numbers ek saath. Cut off thirty one December two thousand three. Aath exclusions. Chhah limb. Chhabbis definitions. Rule four mein chhah mahine. Rule seven mein pandrah aur pandrah din. Rule nine mein tees din aur ek saal. Teen saal, chaar saal, aur Rule eight mein ek tihai recovery cap.", SKY, "EXAM"),
            ("THE AUTHORITIES", "Rule 7: Appointing Authority. Rule 8: President, Secretary or C&AG by post, and no appeal from the President. Rules 9 and 10: the Central Government.", "Authority chart. Rule seven Appointing Authority. Rule eight President, Secretary ya CAG, post ke hisaab se. Rule eight ka clause six A, President ke order par appeal nahi. Rule nine aur ten mein Government, matlab Central Government.", GREEN, "EXAM"),
            ("THE TRAPS", "Explanations extend, never backdate. Form is not Format. DR is not pension. CCA Rule 16 never touches pension. One-third is a recovery rate, not a withholding cap. Provisional pension needs instituted proceedings.", "Traps. Explanation coverage badhata hai, date peeche nahi khinchta. Form aur Format alag. DR pension nahi. CCA Rule sixteen pension ko chhoota nahi. Ek tihai recovery rate hai, withholding cap nahi. Provisional pension ke liye proceedings instituted chahiye, sirf contemplated nahi.", RED, "TRAP"),
            ("FLAGS AND WHAT COMES NEXT", "Open items: Rule 8(4)(d) cites a sub-rule (9) that is not printed, and Rule 87, Rule 44 and the date of G.S.R. 775(E) are unread. Batch 2 takes Rules 11 to 30, with the Rule 15 fifty per cent cut.", "Flags aur aage ka plan. Open items: Rule eight ka sub rule nine reference chhapa nahi, Rule eighty seven, Rule forty four aur G.S.R. seven seven five E ki date abhi padhi nahi. Batch two mein Rules eleven se thirty, jisme Rule fifteen ka fifty percent cut hai.", PURPLE, "FLAG"),
        ],
        "trap": "REMEMBER: one rule book, one pension, one floor. Every trap in Rules 1 to 10 is a version of those three ideas.",
        "trap_say": "Aakhir mein. Ek rule book, ek pension, ek floor. Rules one se ten ke saare traps inhi teen ideas ke aas paas ghoomte hain.",
    },
]

# ---------------------------------------------------------------------------
# Normalise: accept 4-tuples (no flag) and 5-tuples, and index everything once.
# ---------------------------------------------------------------------------
for _sc in SCENES:
    if "rows" in _sc:
        _n = []
        for _row in _sc["rows"]:
            if len(_row) == 4:
                _n.append(tuple(_row) + ("",))
            else:
                _n.append(tuple(_row))
        _sc["rows"] = _n

SCENES_BY_ID = {s["id"]: s for s in SCENES}
PART_STARTS = [SCENES[0]["id"], SCENES[10]["id"], SCENES[20]["id"]]


# ============================================================================
# DRAWING HELPERS
# ============================================================================
_FONT_CACHE = {}
_FONT_CANDIDATES = {
    False: ["DejaVuSans.ttf", "LiberationSans-Regular.ttf", "arial.ttf", "NotoSans-Regular.ttf"],
    True: ["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "arialbd.ttf", "NotoSans-Bold.ttf"],
}


def font(size: int, bold: bool = False):
    key = (size, bold)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    f = None
    for name in _FONT_CANDIDATES[bold]:
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


def text_w(draw, s, f):
    b = draw.textbbox((0, 0), s, font=f)
    return b[2] - b[0]


def wrap_text(draw, text, f, max_w):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split(" "):
            trial = f"{cur} {word}".strip()
            if text_w(draw, trial, f) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def fit_block(draw, text, bold, max_w, max_h, start, min_size, spacing=1.26):
    """Shrink until every line fits. Raises instead of truncating."""
    for size in range(start, min_size - 1, -1):
        f = font(size, bold)
        lines = wrap_text(draw, text, f, max_w)
        lh = int(size * spacing)
        if len(lines) * lh <= max_h:
            return f, lines, lh, size
    raise ValueError(f"DOES NOT FIT at {min_size}px: {text[:70]!r}")


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def tint(c, t):
    """Mix colour c into the card background - used for quiet fills."""
    return lerp(CARD_BG, c, t)


FLAG_COLOURS = {"EXAM": SKY, "TRAP": RED, "FLAG": ORANGE, "NEW": GREEN}


def background():
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(H):
        d.line([(0, y), (W, y)], fill=lerp(BG_TOP, BG_BOT, y / H))
    for x in range(40, W, 64):
        for y in range(140, 1040, 64):
            d.point((x, y), fill=(28, 38, 64))
    return img, d


def draw_top_bar(d, qno, total, ticker):
    d.rectangle([0, 0, W, TOP_BAR_H], fill=(5, 8, 20))
    d.line([(0, TOP_BAR_H), (W, TOP_BAR_H)], fill=(28, 38, 60), width=2)
    f = font(19, True)
    chip = f"MODULE {qno:02d}/{total:02d}"
    cw = text_w(d, chip, f) + 30
    d.rounded_rectangle([20, 12, 20 + cw, 44], radius=6, outline=(58, 72, 100), width=2)
    d.text((34, 19), chip, font=f, fill=TEXT_WHITE)
    ff = font(16, True)
    t = ticker.upper()
    x = 20 + cw + 24
    maxw = W - x - 560
    if text_w(d, t, ff) > maxw:
        while t and text_w(d, t + "...", ff) > maxw:
            t = t[:-1]
        t = t.rstrip(" ,-") + "..."
    d.text((x, 21), t, font=ff, fill=(128, 146, 176))
    # right hand chips
    fr = font(15, True)
    vw = text_w(d, VOICE_LABEL, fr) + 26
    d.rounded_rectangle([W - 20 - vw, 12, W - 20, 44], radius=6, outline=GREEN, width=2)
    d.text((W - 20 - vw + 13, 20), VOICE_LABEL, font=fr, fill=GREEN)
    dw = text_w(d, DRAFT_LABEL, fr) + 26
    d.rounded_rectangle([W - 40 - vw - dw, 12, W - 40 - vw, 44], radius=6, outline=(58, 72, 100), width=2)
    d.text((W - 40 - vw - dw + 13, 20), DRAFT_LABEL, font=fr, fill=(150, 166, 194))


BANNER = (138, 158, 232)


def draw_banner(d, text, accent):
    d.rounded_rectangle([48, BANNER_Y, W - 48, BANNER_Y + 34], radius=6, fill=(11, 17, 33), outline=(40, 52, 78), width=1)
    f, lines, _, _ = fit_block(d, text.upper(), True, W - 140, 26, 18, 14, 1.1)
    d.text((62, BANNER_Y + 8), lines[0], font=f, fill=BANNER)


def draw_title(d, text, accent, badge):
    f, lines, lh, _ = fit_block(d, text, True, W - 420, 56, 44, 30, 1.08)
    d.text((48, TITLE_Y), lines[0], font=f, fill=TEXT_WHITE)
    fb = font(18, True)
    bw = text_w(d, badge, fb) + 30
    d.rounded_rectangle([W - 48 - bw, TITLE_Y + 2, W - 48, TITLE_Y + 40], radius=7, fill=tint(accent, 0.28), outline=accent, width=2)
    d.text((W - 48 - bw + 15, TITLE_Y + 11), badge, font=fb, fill=accent)


def draw_chips(d, chips):
    chips = chips[:4]
    gap = 16
    cw = (W - 96 - gap * (len(chips) - 1)) // len(chips)
    for i, (label, sub, colour) in enumerate(chips):
        x = 48 + i * (cw + gap)
        d.rounded_rectangle([x, CHIP_Y, x + cw, CHIP_Y + CHIP_H], radius=10,
                            fill=tint(colour, 0.16), outline=colour, width=2)
        d.rectangle([x, CHIP_Y + 10, x + 5, CHIP_Y + CHIP_H - 10], fill=colour)
        ft, lt, lht, _ = fit_block(d, label, True, cw - 40, 46, CHIP_T_START, CHIP_T_MIN, 1.14)
        if len(lt) > 2:
            raise ValueError(f"chip label too long: {label!r}")
        for k, ln in enumerate(lt):
            d.text((x + 20, CHIP_Y + 14 + k * lht), ln, font=ft, fill=colour)
        fs, ls, _, _ = fit_block(d, sub, False, cw - 40, CHIP_H - (24 + len(lt) * lht), CHIP_S_START, CHIP_S_MIN, 1.12)
        for k, ln in enumerate(ls):
            d.text((x + 20, CHIP_Y + 18 + len(lt) * lht + k * 19), ln, font=fs, fill=(198, 210, 230))


def rows_region(has_trap):
    return ROWS_Y, (ROWS_BOTTOM if has_trap else PROG_Y - 26)


def row_geometry(n, has_trap):
    """Constant per chapter: rows are drawn at their final size from the first reveal,
    so showing the next row never shifts or reflows the ones already on screen."""
    top, bottom = rows_region(has_trap)
    gap = 12
    h = min(150, (bottom - top - gap * (n - 1)) // n)
    used = h * n + gap * (n - 1)
    return top + max(0, (bottom - top - used) // 2), h, gap


def draw_row(d, scene, i, n, x_kind, accent):
    top, h, gap = row_geometry(n, bool(scene.get("trap")))
    y = top + i * (h + gap)
    label, body, _hi, colour, flag = scene["rows"][i]
    newest = (x_kind == "step") and (i == n - 1)
    if newest:
        d.rounded_rectangle([ROW_X0 - 4, y - 4, ROW_X1 + 4, y + h + 4], radius=14, outline=YELLOW, width=3)
    d.rounded_rectangle([ROW_X0, y, ROW_X1, y + h], radius=11,
                        fill=CARD_BG if not newest else lerp(CARD_BG, colour, 0.10),
                        outline=colour if newest else tint(colour, 0.42), width=2)
    d.rectangle([ROW_X0 + 1, y + 12, ROW_X0 + 5, y + h - 12], fill=colour)
    ft, lt, lht, _ = fit_block(d, label, True, LABEL_W, h - 26, TITLE_START, TITLE_MIN, 1.16)
    for k, ln in enumerate(lt):
        d.text((LABEL_X, y + 13 + k * lht), ln, font=ft, fill=colour)
    body_w = BODY_W - (118 if flag else 0)
    fb, lb, lhb, _ = fit_block(d, body, False, body_w, h - 24, BODY_START, BODY_MIN, 1.26)
    ty = y + (h - len(lb) * lhb) // 2
    for k, ln in enumerate(lb):
        d.text((BODY_X, ty + k * lhb), ln, font=fb, fill=TEXT_WHITE)
    if flag:
        fc = FLAG_COLOURS.get(flag, MUTED)
        ff = font(15, True)
        pw = text_w(d, flag, ff) + 22
        d.rounded_rectangle([ROW_X1 - 22 - pw, y + 12, ROW_X1 - 22, y + 38], radius=5, fill=tint(fc, 0.3), outline=fc, width=1)
        d.text((ROW_X1 - 22 - pw + 11, y + 17), flag, font=ff, fill=fc)


def draw_pending_row(d, scene, i, n):
    """Empty slot for a row that is not revealed yet: keeps the page geometry stable
    and makes the reveal read as progress instead of as a gap."""
    top, h, gap = row_geometry(n, bool(scene.get("trap")))
    y = top + i * (h + gap)
    d.rounded_rectangle([ROW_X0, y, ROW_X1, y + h], radius=11, fill=(15, 22, 41), outline=(34, 46, 72), width=1)


def draw_table(d, scene, shown, accent):
    tb = scene["table"]
    top, bottom = rows_region(bool(scene.get("trap")))
    cols, widths, rows = tb["cols"], tb["widths"], tb["rows"]
    total_w = W - 96
    xs, cur = [], 0.0
    for wfrac in widths:
        xs.append(48 + int(cur * total_w))
        cur += wfrac
    xs.append(48 + total_w)
    head_h = 46
    d.rounded_rectangle([48, top, W - 48, top + head_h], radius=8, fill=tint(accent, 0.22), outline=accent, width=2)
    fh = font(20, True)
    for j, cname in enumerate(cols):
        fh2, lh2, _, _ = fit_block(d, cname, True, xs[j + 1] - xs[j] - 26, head_h - 12, 20, 15, 1.1)
        d.text((xs[j] + 14, top + 13), lh2[0], font=fh2, fill=accent if j == 0 else MUTED)
    vis = max(1, min(len(rows), shown))
    body_top = top + head_h + 8
    body_h = bottom - body_top
    rh = min(96, (body_h - 8 * (vis - 1)) // vis)
    for i in range(vis):
        y = body_top + i * (rh + 8)
        newest = (i == vis - 1)
        d.rounded_rectangle([48, y, W - 48, y + rh], radius=8,
                            fill=CARD_BG if i % 2 == 0 else CARD_BG_ALT,
                            outline=YELLOW if newest and shown < len(rows) else tint(accent, 0.30),
                            width=2 if newest and shown < len(rows) else 1)
        for j, cell in enumerate(rows[i]):
            bold = (j == 0)
            col = accent if bold else TEXT_WHITE
            fcell, lcell, lhcell, _ = fit_block(d, cell, bold, xs[j + 1] - xs[j] - 26, rh - 14, TABLE_START, TABLE_MIN, 1.2)
            ty = y + (rh - len(lcell) * lhcell) // 2
            for k, ln in enumerate(lcell):
                d.text((xs[j] + 14, ty + k * lhcell), ln, font=fcell, fill=col)
        for j in range(1, len(cols)):
            d.line([(xs[j], y + 8), (xs[j], y + rh - 8)], fill=(44, 58, 86), width=1)
    if vis < len(rows):
        d.text((W - 300, bottom + 2), f"rows {vis}/{len(rows)} revealed", font=font(15, False), fill=DIM)


def draw_bars(d, scene, shown, accent):
    """Three groups (days / months / years). Each group is scaled to its own largest
    value, so a 15-day rule is still visible next to a four-year bar - and every bar
    carries its own printed value, so the scale can never mislead."""
    top, bottom = rows_region(bool(scene.get("trap")))
    items = scene["bars"]["items"]
    vis = max(1, min(len(items), shown))
    groups, order = {}, []
    for it in items:
        g = it[3]
        if g not in groups:
            groups[g] = []
            order.append(g)
        groups[g].append(it)
    shown_items = items[:vis]
    palette = [SKY, GREEN, ORANGE, YELLOW, PINK, RED, PURPLE]
    bar_x0, bar_x1 = 470, W - 250
    y = top + 4
    header_h, bar_h, gap = 30, 76, 6
    idx = 0
    for g in order:
        if idx >= vis:
            break
        d.text((48, y), g, font=font(18, True), fill=MUTED)
        d.line([(48 + text_w(d, g, font(18, True)) + 14, y + 12), (W - 48, y + 12)], fill=(38, 50, 76), width=1)
        y += header_h
        gmax = max(v for (_l, v, _d, _g) in groups[g])
        for (label, value, display, _g) in groups[g]:
            if idx >= vis:
                break
            col = palette[idx % len(palette)]
            newest = (idx == vis - 1)
            fl, ll, llh, _ = fit_block(d, label, newest, 400, 52, 20, 14, 1.14)
            for k, ln in enumerate(ll[:2]):
                d.text((48, y + 6 + k * llh), ln, font=fl,
                       fill=TEXT_WHITE if newest else (208, 218, 236))
            frac = value / gmax
            bx1 = bar_x0 + max(14, int((bar_x1 - bar_x0) * frac))
            d.rounded_rectangle([bar_x0, y + 8, bar_x1, y + 44], radius=8, fill=(24, 33, 56))
            d.rounded_rectangle([bar_x0, y + 8, bx1, y + 44], radius=8,
                                fill=col if newest else tint(col, 0.55), outline=col, width=1)
            fd = font(22, True)
            d.text((bar_x1 + 22, y + 12), display, font=fd, fill=col)
            y += bar_h + gap
            idx += 1


def draw_trap(d, text, accent):
    if not text:
        return
    for lead in ("CLASSIC UPSC TRAP:", "TRAP:"):
        if text.upper().startswith(lead):
            text = text[len(lead):].strip()
    d.rounded_rectangle([48, TRAP_Y0, W - 48, TRAP_Y1], radius=9, fill=YELLOW)
    prefix = "CLASSIC UPSC TRAP:  "
    fp = font(21, True)
    body_w = W - 96 - 60 - text_w(d, prefix, fp)
    fb, lb, lhb, _ = fit_block(d, text, True, body_w, (TRAP_Y1 - TRAP_Y0) - 14, 21, 15, 1.16)
    if len(lb) > 2:
        raise ValueError("trap text needs more than two lines")
    total_h = len(lb) * lhb
    ty = TRAP_Y0 + (TRAP_Y1 - TRAP_Y0 - total_h) // 2
    d.text((78, ty), prefix, font=fp, fill=(28, 22, 6))
    for k, ln in enumerate(lb):
        d.text((78 + text_w(d, prefix, fp), ty + k * lhb), ln, font=fb, fill=(28, 22, 6))


def draw_question_panel(d, scene, text, is_intro, accent):
    """Question slide: the question in big type plus the chapter's row map, sized to
    its content so the frame never carries dead space."""
    top, bottom = rows_region(bool(scene.get("trap")))
    labels = [r[0] for r in scene.get("rows", [])] or [c[0] for c in scene.get("chips", [])]
    nrows = math.ceil(len(labels) / 2)
    f, lines, lh, _ = fit_block(d, text, True, W - 300, 200, 50, 28, 1.26)
    content_h = 74 + len(lines) * lh + 26 + 48 + nrows * 40 + 26
    trap_txt = scene.get("trap", "")
    for lead in ("CLASSIC UPSC TRAP:", "TRAP:"):
        if trap_txt.upper().startswith(lead):
            trap_txt = trap_txt[len(lead):].strip()
    trap_lines, trap_lh = [], 0
    if trap_txt:
        _, trap_lines, trap_lh, _ = fit_block(d, trap_txt, False, W - 220, 200, 24, 17, 1.2)
    trap_h = (46 + len(trap_lines) * trap_lh + 18) if trap_txt else 0
    reserve = (trap_h + 26) if trap_txt else 0
    panel_h = min(bottom - top - reserve, content_h)
    y0 = top + 6
    y1 = y0 + panel_h
    d.rounded_rectangle([48, y0, W - 48, y1], radius=14, fill=tint(accent, 0.10),
                        outline=tint(accent, 0.55), width=3)
    chip = "SERIES INTRO" if is_intro else "RIYA ASKS"
    fc = font(17, True)
    cw = text_w(d, chip, fc) + 26
    d.rounded_rectangle([112, y0 + 22, 112 + cw, y0 + 52], radius=6, fill=YELLOW if not is_intro else GREEN)
    d.text((125, y0 + 29), chip, font=fc, fill=(20, 16, 6))
    qtop = y0 + 74
    for k, ln in enumerate(lines):
        d.text((112, qtop + k * lh), ln, font=f, fill=TEXT_WHITE)
    rule_y = qtop + len(lines) * lh + 26
    d.line([(112, rule_y), (W - 112, rule_y)], fill=tint(accent, 0.45), width=2)
    d.text((112, rule_y + 16), "IN THIS CHAPTER", font=font(18, True), fill=accent)
    col_w = (W - 300) // 2
    fl = font(20, False)
    for i, label in enumerate(labels):
        cx = 112 + (i % 2) * col_w
        cy = rule_y + 52 + (i // 2) * 40
        d.text((cx, cy), f"{i + 1:02d}", font=font(17, True), fill=DIM)
        one = fit_block(d, label, False, col_w - 70, 26, 20, 15, 1.1)[1][0]
        d.text((cx + 40, cy - 2), one, font=fl, fill=(206, 216, 234))
    if trap_txt:
        ty0 = y1 + 26
        ty1 = ty0 + trap_h
        d.rounded_rectangle([48, ty0, W - 48, ty1], radius=12, fill=tint(YELLOW, 0.12),
                            outline=YELLOW, width=2)
        d.text((78, ty0 + 16), "TRAP AHEAD IN THIS CHAPTER", font=font(17, True), fill=YELLOW)
        ft = font(24, False)
        for k, ln in enumerate(trap_lines):
            d.text((78, ty0 + 44 + k * trap_lh), ln, font=ft, fill=(238, 232, 196))


def draw_progress(d, qno, total, step, nsteps, accent):
    d.rectangle([0, PROG_Y, W, H], fill=(6, 10, 22))
    seg = W / total
    base_y1, base_y2 = PROG_Y + 10, PROG_Y + 18
    for k in range(total):
        x0 = int(k * seg)
        x1 = int((k + 1) * seg) - 3
        d.rounded_rectangle([x0, base_y1, x1, base_y2], radius=3, fill=(30, 40, 64))
    frac = min(1.0, step / max(1, nsteps))
    done = (qno - 1) + frac
    x_end = int(done * seg)
    d.rounded_rectangle([0, base_y1, max(6, x_end), base_y2], radius=3, fill=accent)
    f = font(16, True)
    d.text((48, PROG_Y + 26), f"{BATCH_LABEL}   |   chapter {qno:02d} of {total:02d}", font=f, fill=(120, 138, 168))
    d.text((W - 420, PROG_Y + 26), "ENGLISH ON SCREEN - HINGLISH NARRATION", font=font(14, True), fill=(96, 112, 142))


def render_frame(scene, qno, total, step, kind, out_path: Path):
    img, d = background()
    accent = scene["chips"][0][2]
    n = len(scene.get("rows", [])) if "rows" in scene else len(scene.get("says", []))
    d.rectangle([0, 0, W, 4], fill=accent)
    draw_top_bar(d, qno, total, "CCS (PENSION) RULES 2021 - BATCH 1 - RULES 1 TO 10 - CITY HINGLISH EXPLAINER")
    draw_banner(d, scene["chapter"], accent)
    draw_title(d, scene["title"], accent, scene["badge"])
    draw_chips(d, scene["chips"])
    if kind in ("intro", "question"):
        draw_question_panel(d, scene, scene["intro"] if kind == "intro" else scene["q"], kind == "intro", accent)
    else:
        if scene.get("kind") == "table":
            draw_table(d, scene, step, accent)
        elif scene.get("kind") == "bars":
            draw_bars(d, scene, step, accent)
        else:
            for i in range(n):
                if i < step:
                    draw_row(d, scene, i, n, kind, accent)
                else:
                    draw_pending_row(d, scene, i, n)
        if scene.get("trap") and step >= n:
            draw_trap(d, scene.get("trap", ""), accent)
    draw_progress(d, qno, total, step, n + 1, accent)
    img.save(out_path)


# ============================================================================
# SEGMENTS / REFERENCE SHEET / AUDIT
# ============================================================================
def build_segments(scene):
    """Returns (speaker, text, step, kind, nsteps). step drives both reveal and progress."""
    segs = []
    if scene.get("intro"):
        segs.append(("teacher", scene["intro"], 0, "intro", 1))
    segs.append(("student", scene["q_say"], 0, "question", 1))
    n = len(scene["rows"]) if "rows" in scene else 1
    if "rows" in scene:
        for i, row in enumerate(scene["rows"]):
            segs.append(("teacher", row[2], i + 1, "step", n))
    else:
        says = scene["says"]
        nrows = len(scene["table"]["rows"]) if scene.get("kind") == "table" else len(scene["bars"]["items"])
        for i, say in enumerate(says):
            step = max(1, round(nrows * (i + 1) / len(says)))
            segs.append(("teacher", say, step, "step", nrows))
    segs.append(("teacher", scene.get("trap_say", ""), n + 1, "trap", n + 1))
    return segs


def write_reference_sheet(path=Path("pension_b1_reference_sheet.md")):
    out = ["# CCS (Pension) Rules 2021 - Batch 1 (Rules 1 to 10) - full reference sheet",
           "",
           "English on screen, Hinglish narration. Every row below is one card of the video;",
           "the narration column is the exact spoken line (Roman script, no Devanagari).", ""]
    for i, sc in enumerate(SCENES, 1):
        out += [f"## {i:02d}. {sc['title']}", f"*{sc['chapter']}*  |  badge: {sc['badge']}", "",
                f"**Q:** {sc['q']}", ""]
        if "rows" in sc:
            for label, body, hi, _c, flag in sc["rows"]:
                tag = f" `{flag}`" if flag else ""
                out += [f"### {label}{tag}", body, "", f"> {hi}", ""]
        elif sc.get("kind") == "table":
            tb = sc["table"]
            out += ["| " + " | ".join(tb["cols"]) + " |", "|" + "---|" * len(tb["cols"])]
            for r in tb["rows"]:
                out.append("| " + " | ".join(r) + " |")
            out.append("")
            for j, say in enumerate(sc["says"], 1):
                out += [f"> Part {j}: {say}", ""]
        else:
            cur = None
            for label, value, display, grp in sc["bars"]["items"]:
                if grp != cur:
                    out.append(f"\n**{grp}**\n")
                    cur = grp
                out.append(f"- **{display}** - {label}")
            out.append("")
            for j, say in enumerate(sc["says"], 1):
                out += [f"> Part {j}: {say}", ""]
        out += [f"**Trap:** {sc['trap']}", "", "---", ""]
    path.write_text("\n".join(out), encoding="utf-8")
    return path


def audit_density():
    img, d = background()
    bad = 0
    print(f"{'scene':26s} {'kind':6s} {'rows':>4s} {'label':>6s} {'body':>5s}  note")
    for sc in SCENES:
        has_trap = bool(sc.get("trap"))
        try:
            ft, lt, lht, ts = fit_block(d, sc["title"], True, W - 420, 56, 44, 30, 1.08)
            if len(lt) > 1:
                bad += 1
                print(f"{sc['id'][:26]:26s} TITLE WRAPS to {len(lt)} lines")
        except ValueError as e:
            bad += 1
            print(f"{sc['id'][:26]:26s} TITLE FAIL {e}")
        for chip in sc["chips"]:
            try:
                _, lc, _, _ = fit_block(d, chip[0], True, (W - 96 - 48) // 4 - 40, 46, CHIP_T_START, CHIP_T_MIN, 1.14)
                if len(lc) > 2:
                    raise ValueError(f"chip label wraps to {len(lc)} lines")
                fit_block(d, chip[1], False, (W - 96 - 48) // 4 - 40, CHIP_H - 24 - len(lc) * 31, CHIP_S_START, CHIP_S_MIN, 1.12)
            except ValueError as e:
                bad += 1
                print(f"{sc['id'][:26]:26s} CHIP FAIL {chip[0]!r}: {e}")
        if "rows" in sc:
            n = len(sc["rows"])
            _, h, _gap = row_geometry(n, has_trap)
            body_sizes = []
            for label, body, hi, _c, _f in sc["rows"]:
                try:
                    _, l1, _, s1 = fit_block(d, label, True, LABEL_W, h - 26, TITLE_START, TITLE_MIN, 1.16)
                    fbw = BODY_W - (118 if _f else 0)
                    _, l2, _, s2 = fit_block(d, body, False, fbw, h - 24, BODY_START, BODY_MIN, 1.26)
                    body_sizes.append(s2)
                    if len(l1) > 3:
                        raise ValueError(f"label wraps to {len(l1)} lines")
                    if not hi.strip():
                        raise ValueError(f"empty narration: {label!r}")
                except ValueError as e:
                    bad += 1
                    body_sizes.append(0)
                    print(f"{sc['id'][:26]:26s} ROW FAIL {label[:30]!r}: {e}")
            print(f"{sc['id'][:26]:26s} {'rows':6s} {n:>4d} {min(body_sizes) if body_sizes else 0:>6d}  h={h}")
        elif sc.get("kind") == "table":
            tb = sc["table"]
            if len(tb["cols"]) != len(tb["widths"]):
                bad += 1
                print(f"{sc['id']}: table widths/cols mismatch")
            top, bottom = rows_region(has_trap)
            vis = len(tb["rows"])
            rh = min(96, (bottom - top - 46 - 8 - 8 * (vis - 1)) // vis)
            for r in tb["rows"]:
                for j, cell in enumerate(r):
                    try:
                        fit_block(d, cell, j == 0, (W - 96) * tb["widths"][j] - 26, rh - 14, TABLE_START, TABLE_MIN, 1.2)
                    except ValueError as e:
                        bad += 1
                        print(f"{sc['id']}: TABLE CELL FAIL {cell[:40]!r}: {e}")
            print(f"{sc['id'][:26]:26s} {'table':6s} {vis:>4d}     -     -  rh={rh}")
        else:
            top, bottom = rows_region(has_trap)
            items = sc["bars"]["items"]
            groups = len({it[3] for it in items})
            need = groups * 30 + len(items) * 82
            if need > bottom - top:
                bad += 1
                print(f"{sc['id']}: bars need {need}px, only {bottom - top}px free")
            print(f"{sc['id'][:26]:26s} {'bars':6s} {len(items):>4d}     -     -  groups={groups}")
        if has_trap:
            try:
                fp = font(21, True)
                body_w = W - 96 - 60 - text_w(d, "CLASSIC UPSC TRAP:  ", fp)
                _, lb, _, _ = fit_block(d, sc["trap"], True, body_w, TRAP_Y1 - TRAP_Y0 - 14, 21, 15, 1.16)
                if len(lb) > 2:
                    raise ValueError(f"trap needs {len(lb)} lines")
            except ValueError as e:
                bad += 1
                print(f"{sc['id'][:26]:26s} TRAP FAIL {e}")
        # narration sanity: Roman script only
        all_say = [s[1] for s in build_segments(sc)]
        for t in all_say:
            if any("\u0900" <= ch <= "\u097f" for ch in t):
                bad += 1
                print(f"{sc['id']}: DEVANAGARI found in narration")
    total_rows = sum(len(s.get("rows", [])) for s in SCENES)
    print(f"\nchapters={len(SCENES)}  row cards={total_rows}  tables={sum(1 for s in SCENES if s.get('kind') == 'table')}  charts={sum(1 for s in SCENES if s.get('kind') == 'bars')}")
    print("AUDIT PASSED - every card is inside the density budget" if not bad else f"{bad} PROBLEM(S) FOUND")
    return bad


# ============================================================================
# AUDIO / SUBTITLES / RENDER
# ============================================================================
def probe_duration(path: Path) -> float:
    """ffprobe if present, otherwise read the Duration line ffmpeg prints on stderr."""
    if FFPROBE:
        out = subprocess.check_output(
            [FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
            text=True).strip()
        return float(out)
    err = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True).stderr
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.?\d*)", err)
    if not m:
        raise RuntimeError(f"cannot read duration of {path}")
    h, mi, sec = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(sec)


def silent_audio(text: str, out: Path) -> float:
    dur = max(1.6, len(text.split()) / 2.5)
    subprocess.run([FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", f"{dur:.2f}",
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
                with open(out, "wb") as fh:
                    async for ch in com.stream():
                        if ch["type"] == "audio":
                            fh.write(ch["data"])
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


def write_ass(cues, path: Path):
    head = (
        "[Script Info]\nScriptType: v4.00+\nPlayResX: 1920\nPlayResY: 1080\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, "
        "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
        "MarginR, MarginV, Encoding\n"
        # BorderStyle 3 = opaque box behind each caption line, so the Hinglish line stays
        # readable over the yellow trap strip as well as over the dark rows.
        # BorderStyle 3 = opaque box per caption line. MarginV 14 keeps the Hinglish
        # caption in the bottom band so it never covers a row card or the trap strip.
        "Style: Default,DejaVu Sans,30,&H00FFFFFF,&H0000E6FF,&H00000000,&HD00A0F1E,-1,0,0,0,100,100,0,0,3,12,0,2,240,240,16,1\n"
        "Style: Student,DejaVu Sans,30,&H0042E4F0,&H0000E6FF,&H00000000,&HD00A0F1E,-1,0,0,0,100,100,0,0,3,12,0,2,240,240,16,1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"
    )
    lines = [head]
    for s, e, style, txt in cues:
        lines.append(f"Dialogue: 0,{fmt_ass(s)},{fmt_ass(e)},{style},,0,0,0,,{txt}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _two_lines(text, max_chars=112):
    """Pre-wrap a caption into at most two lines so it can never run off the frame.
    libass does not wrap reliably inside an opaque-box style, so we do it ourselves."""
    text = text.strip()
    if len(text) <= max_chars // 2:
        return text
    words = text.split()
    total = len(text)
    best, best_d = None, 10 ** 9
    for i in range(1, len(words)):
        first = " ".join(words[:i])
        second = " ".join(words[i:])
        if len(first) > max_chars // 2 + 12:
            break
        d = abs(len(first) - len(second))
        if d < best_d:
            best, best_d = (first, second), d
    if not best:
        return text
    return best[0] + chr(92) + "N" + best[1]


def make_cues(words, offset, style, chunk=9, max_chars=112):
    cues, buf = [], []
    for w in words:
        buf.append(w)
        joined = sum(len(x[0]) + 1 for x in buf)
        if len(buf) >= chunk or joined > max_chars or w[0].endswith((".", "?", "!", ":")):
            cues.append((offset + buf[0][1], offset + buf[-1][2] + 0.12, style, _two_lines(" ".join(x[0] for x in buf), max_chars)))
            buf = []
    if buf:
        cues.append((offset + buf[0][1], offset + buf[-1][2] + 0.15, style, _two_lines(" ".join(x[0] for x in buf), max_chars)))
    return cues


def even_words(text, dur):
    toks = text.split()
    step = dur / max(len(toks), 1)
    return [(t, i * step, (i + 1) * step) for i, t in enumerate(toks)]


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true", help="density + narration check, no ffmpeg needed")
    ap.add_argument("--preview", action="store_true", help="render slides only")
    ap.add_argument("--no-tts", action="store_true", help="silent audio, offline timing test")
    ap.add_argument("--only", default="", help="render one chapter id, e.g. c01_rule1")
    ap.add_argument("--teacher", default=DEFAULT_TEACHER)
    ap.add_argument("--student", default=DEFAULT_STUDENT)
    ap.add_argument("--rate", default="-4%")
    ap.add_argument("--part", type=int, choices=[1, 2, 3], help="1..3 = first, middle, last third")
    args = ap.parse_args()

    ref = write_reference_sheet()
    if args.audit:
        print(f"reference sheet written: {ref.resolve()}")
        sys.exit(1 if audit_density() else 0)

    for folder in (BUILD_DIR, SLIDES_DIR, AUDIO_DIR):
        folder.mkdir(parents=True, exist_ok=True)

    global SCENES, OUTPUT_MP4
    if args.only:
        SCENES = [s for s in SCENES if s["id"] == args.only] or sys.exit(f"no scene id {args.only}")
    elif args.part:
        idx = [SCENES.index(SCENES_BY_ID[pid]) for pid in PART_STARTS] + [len(SCENES)]
        SCENES = SCENES[idx[args.part - 1]:idx[args.part]]
        OUTPUT_MP4 = Path(f"{OUT_STEM}_part{args.part}.mp4")
    total = len(SCENES)
    if audit_density() and not args.preview:
        sys.exit("Build stopped: fix the cards listed above.")

    print(f"\n=== Step 1: {total} chapter slides ===")
    jobs = []
    for si, sc in enumerate(SCENES):
        for gi, (who, text, step, kind, nsteps) in enumerate(build_segments(sc)):
            sp = SLIDES_DIR / f"{sc['id']}_{gi:02d}_{kind}.png"
            render_frame(sc, si + 1, total, step, kind, sp)
            jobs.append((si, who, text, kind, sp, AUDIO_DIR / f"{sc['id']}_{gi:02d}.mp3"))
        print(f"  {si + 1:02d}/{total}  {sc['id']}")
    if args.preview:
        print(f"Preview written to {SLIDES_DIR.resolve()}")
        return

    if not FFMPEG:
        sys.exit("ERROR: no ffmpeg found. pip install imageio-ffmpeg, or set FFMPEG_BIN")

    print(f"\n=== Step 2: narration ({'SILENT TEST' if args.no_tts else args.student + ' / ' + args.teacher}) ===")
    words_by_job = {}
    if not args.no_tts:
        try:
            import edge_tts  # noqa: F401
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "edge-tts"])
        sem = asyncio.Semaphore(4)
        tasks = [tts_segment(t, args.student if who == "student" else args.teacher, mp3, args.rate, sem)
                 for (_s, who, t, _k, _p, mp3) in jobs]
        for i, w in enumerate(await asyncio.gather(*tasks)):
            words_by_job[i] = w

    print("\n=== Step 3: clips ===")
    clips, cues, cursor = [], [], 0.0
    for i, (si, who, text, kind, sp, mp3) in enumerate(jobs):
        if args.no_tts:
            dur_speech = silent_audio(text, mp3)
            words = even_words(normalize_for_tts(text), dur_speech)
        else:
            dur_speech = probe_duration(mp3)
            words = words_by_job[i] or even_words(text, dur_speech)
        dur = dur_speech + (1.1 if kind in ("question", "trap") else 0.55)
        clip = BUILD_DIR / f"clip_{i:03d}.mp4"
        subprocess.run([
            FFMPEG, "-y", "-loop", "1", "-framerate", "5", "-i", str(sp), "-i", str(mp3),
            "-af", "apad", "-t", f"{dur:.3f}",
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-g", "60", "-r", "30", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", str(clip)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cues += make_cues(words, cursor, "Student" if who == "student" else "Default")
        clips.append(clip)
        cursor += dur
    print(f"  {len(clips)} clips | {cursor / 60:.2f} min")

    print("\n=== Step 4: concat + burn subtitles ===")
    concat = BUILD_DIR / "concat.txt"
    concat.write_text("\n".join(f"file '{c.name}'" for c in clips) + "\n", encoding="utf-8")
    raw = BUILD_DIR / "raw_concat.mp4"
    subprocess.run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(raw)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ass = BUILD_DIR / "subtitles.ass"
    write_ass(cues, ass)
    ass_esc = str(ass).replace("\\", "/").replace(":", "\\:")
    subprocess.run([
        FFMPEG, "-y", "-i", str(raw), "-vf", f"subtitles='{ass_esc}'",
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(OUTPUT_MP4)], check=True,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("\n=== Step 5: verify ===")
    dur = probe_duration(OUTPUT_MP4)
    if FFPROBE:
        streams = subprocess.check_output([FFPROBE, "-v", "error", "-show_entries", "stream=codec_type,width,height",
                                           "-of", "csv=p=0", str(OUTPUT_MP4)], text=True).split()
    else:
        streams = ["video (ffprobe not installed)", "audio"]
    print("streams:", streams)
    print(f"DONE: {OUTPUT_MP4.resolve()}  |  {dur / 60:.2f} min  |  {OUTPUT_MP4.stat().st_size / 1048576:.1f} MB")
    if not any(s.startswith("audio") for s in streams):
        print("WARNING: no audio stream found")


if __name__ == "__main__":
    asyncio.run(main())
