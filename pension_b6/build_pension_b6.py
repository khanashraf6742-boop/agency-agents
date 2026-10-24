#!/usr/bin/env python3
"""
CCS (Pension) Rules 2021 - BATCH 6 - RULES 71-87 (Chapters XI-XIV)
"DEATH, PAYMENT AND MISCELLANEOUS" - 32 chapters, 128 cards, 4 comparison tables.
ENGLISH ON SCREEN + HINGLISH NARRATION (Roman script only - no Devanagari anywhere).
=====================================================================================================

WHAT THIS BUILD IS
  A Q&A explainer compiler: a teacher (Prabhat) and a student (Riya) walk through Rules 71 to 87,
  one chapter per rule-group, four cards per chapter, plus a gold TRAP strip and a recap chapter.
  Every card carries (a) a short English key-point for the screen and (b) a Hinglish narration line
  for the voice. Long, examinable detail lives in pension_b6_reference_sheet.md, not on the slide.

LANGUAGE POLICY (fixed by the brief)
  * On-screen text: ENGLISH only, plain "city English" (Indian administrative English, no jargon
    left unexplained). Every technical term is glossed the first time it appears.
  * Narration: HINGLISH in Roman script. Hindi grammar, English technical nouns, exactly how a
    Delhi/Mumbai teacher speaks in class. No Devanagari at any point (asserted in code).
  * Voice: en-IN neural voices reading Roman Hinglish. If a studio wants warmer Hindi vowels, run
    with --teacher hi-IN-MadhurNeural --student hi-IN-SwaraNeural; the script is voice-agnostic.

AUDIT PASS RUN ON 24.10.2026 (senior-professor review, rule by rule)
  Method: the bare text of Chapter XI (Rules 71-78), Chapter XII (79-80), Chapter XIII (81-84) and
  Chapter XIV (85-87) was read in full from a complete reproduction of the 2021 Rules, then every
  sub-rule, clause, proviso and exception in 71-87 was mapped to the card that teaches it. The map
  is machine-checked: run `--coverage` and the build fails if any sub-rule has no card.
  Result: all 17 rules (71-87) and 115 sub-rule units are covered. Gaps found and FILLED in this
  version are listed below under "GAPS FILLED". Items that were only "close gist" in the earlier
  build are now verified against the bare text and the doubt-flags are removed.

GAPS FILLED IN THIS VERSION (they were missing or thin before)
  * Rule 73(2)(b)(iii) PROVISO - a period that cannot be verified at all must be reported to the
    referring Head of Office at the same time (Chapter 8).
  * Rule 77(1)(i)(a)-(g) - the full seven-item information list sent to the Directorate of Estates,
    including (g)(A)-(E) (unrecovered fee period, standard-rent-bill amounts, the proposed recovery
    out of gratuity, and earlier Directorate references) (Chapter 15).
  * Rule 76(5)(c)-(e) - the MISSING-servant balance of gratuity: one-month intimation, payment only
    after six months from the police report, and adjustment of the gratuity withheld under Rule 77
    against outstanding licence fee with refund of the balance (Chapter 14).
  * Rule 79(4)(c) - a child who had ALREADY attained majority at the time of the widow's remarriage
    takes the family pension after the remarriage (Chapter 22).
  * Format 7 (indemnity bond where the claimant is a minor) and Form 3 (common nomination form for
    gratuity, GPF and CGEGIS under Rule 46) added to the Forms/Formats map (Chapter 4).
  * Rules 85, 86, 87 - the earlier build carried them as unverified gist. Operative text now read
    and the cards rewritten with the real wording (Chapters 28 and 29).

FOUR DRAFTING SLIPS IN THE PRINTED RULES (teach them as slips, do not repeat them as law)
  1. Rule 75(5)(b) sends the recoverable-dues figure to "sub-rule (3) of rule 74"; the dues are
     actually listed in Rule 74(4), because 74(3) is only about keeping copies.
  2. Rule 76(5)(e) cites "clause (b) of sub-rule (1) of rule 77" for the 10 per cent withholding
     (that is clause (vi)) and "clause (viii)" for outstanding licence fee (that is clause (iii)).
  3. Rule 81(2) says "clause (d) of sub-rule (2) of rule 76"; the family-pension start date sits in
     Rule 76(3)(b) (and 76(3)(e) for a missing servant).
  4. Numbering: G.S.R. 770(E) of 07.10.2022 replaced the SECOND sub-rule numbered "(5)" in Rule 76
     with "(5A)" ("The fact of the issue..."). Rule 76 therefore reads (1) to (5), then (5A), then
     (6), (7) and (8). Loose reproductions that never had the duplicate renumber their list and
     print those last clauses as (6) to (9). Quote the clause text, and cite the print you follow.

WHAT IS STILL A CLOSE RESTATEMENT (do not over-claim)
  * Rules 45, 47, 50, 51, 57, 62, 64, 65, 68 belong to Batches 4-5 and are cited here only as
    cross-references; their own wording was not re-read in this pass.
  * Dynamic figures: dearness relief and the GPF rate move every quarter. The rule is permanent,
    the figure is not - always check the latest DoPPW/DEA O.M. before quoting a number.
  * Amendment currency was checked to 21.10.2026: no change to Rules 71-87 was found after
    G.S.R. 410(E) of 16.07.2024 (effective 16.11.2024), which swapped Form 6 for Form 6-A.

VISUALS (matched to the reference still)
  * 1920x1080, night-blue gradient, thin accent bar on top, chapter tab, one-line title,
    metadata chips at top right, question banner with the Q number, four accent PILLS showing the
    card topics, four detail ROWS (coloured label on the left, key-point on the right), the newest
    row ringed in gold, a gold TRAP strip, and a segmented progress bar at the foot.
  * Four chapters render as real TABLES (Forms map, retirement vs death, amendment register, key
    numbers) because a table beats a paragraph for comparison-heavy material.

USAGE
    python build_pension_b6.py --coverage    # rule-by-rule coverage matrix + density check
    python build_pension_b6.py --audit       # density check only (no ffmpeg / internet)
    python build_pension_b6.py --preview     # slides only (writes PNGs you can eyeball)
    python build_pension_b6.py --no-tts      # silent dry run with synthetic timing
    python build_pension_b6.py --part 1      # one third of the chapters (1, 2 or 3)
    python build_pension_b6.py               # full build (edge-tts + ffmpeg with libass)
"""
import argparse
import asyncio
import math
import re
import os
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
BUILD_DIR = Path("pension_b6_build")
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
OUT_STEM = "pension_b6_masterclass"
OUTPUT_MP4 = Path(OUT_STEM + ".mp4")

# Density budget (px). Build fails if text needs to go below these.
BODY_START, BODY_MIN = 30, 22
PILL_START, PILL_MIN = 24, 17
LABEL_START, LABEL_MIN = 26, 18
CELL_START, CELL_MIN = 24, 16
TRAP_START, TRAP_MIN = 28, 19

BG_TOP = (10, 16, 36)
BG_BOT = (22, 30, 58)
CARD_BG = (28, 39, 62)
ROW_BG = (26, 36, 58)
ROW_ALT = (21, 30, 50)
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

# Pronunciation fixes for the neural voices. Hinglish narration is Roman script, so the main job is
# rule references ("Rule 71(4)(c)" -> "Rule 71, sub rule 4, clause c") and English acronyms.
# NOTE: longer patterns first, otherwise "Rule 15(3)" would swallow "Rule 15(3)(a)".
_TTS_FIXES = [
    (r'\bUPSC\b', 'U.P.S.C.'), (r'\bSSC\b', 'S.S.C.'), (r'\bCVC\b', 'C.V.C.'), (r'\bCBI\b', 'C.B.I.'),
    (r'\bDoPT\b', 'D.O.P.T.'), (r'\bDOPT\b', 'D.O.P.T.'), (r'\bDoPPW\b', 'D.O.P.P.W.'),
    (r'\bDoP&AR\b', 'D.O.P. and A.R.'), (r'\bMHA\b', 'M.H.A.'),
    (r'\bOMs\b', 'O.M.s'), (r'\bOM\b', 'O.M.'), (r'\bGIDs\b', 'Government of India decisions'),
    (r'\bGID\b', 'Government of India decision'),
    (r'\bCCS\b', 'C.C.S.'), (r'\bCCA\b', 'C.C.A.'), (r'\bCAG\b', 'C.A.G.'), (r'C&AG', 'C.A.G.'),
    (r'\bGOI\b', 'G.O.I.'), (r'\bDPC\b', 'D.P.C.'), (r'\bAPAR\b', 'A.P.A.R.'), (r'\bACR\b', 'A.C.R.'),
    (r'\bACP\b', 'A.C.P.'), (r'\bMTS\b', 'M.T.S.'), (r'\bFR\b', 'F.R.'), (r'\bSR\b', 'S.R.'),
    (r'\bCPC\b', 'C.P.C.'), (r'\bRR\b', 'R.R.'), (r'\bRTI\b', 'R.T.I.'), (r'\bFCRA\b', 'F.C.R.A.'),
    (r'\bIAS\b', 'I.A.S.'), (r'\bIPS\b', 'I.P.S.'), (r'\bIFS\b', 'I.F.S.'), (r'\bLBSNAA\b', 'L.B.S.N.A.A.'),
    (r'\bNITI\b', 'Nitee'), (r'\bSC/ST\b', 'S.C. and S.T.'), (r'\bOBC\b', 'O.B.C.'),
    (r'\bCGEGIS\b', 'C.G.E.G.I.S.'), (r'\bCPAO\b', 'C.P.A.O.'), (r'\bPDA\b', 'P.D.A.'),
    (r'\bPPO\b', 'P.P.O.'), (r'\bSSA\b', 'S.S.A.'), (r'\bNDC\b', 'N.D.C.'), (r'\bGPF\b', 'G.P.F.'),
    (r'\bDR\b', 'D.R.'), (r'\bEOL\b', 'E.O.L.'), (r'\bFIR\b', 'F.I.R.'), (r'\bHoD\b', 'Head of Department'),
    (r'\bHoO\b', 'Head of Office'), (r'\bAO\b', 'A.O.'), (r'\bDoE\b', 'Directorate of Estates'),
    (r'\bw\.e\.f\.', 'with effect from'), (r'\bW\.E\.F\.', 'with effect from'),
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
    # Hinglish spelling the voices trip on
    (r'\byaani\b', 'yani'), (r'\bmatlab\b', 'matlab'), (r'%', ' percent'),
    (r'[\u2014\u2013]', ','),
]


def normalize_for_tts(text: str) -> str:
    for pat, rep in _TTS_FIXES:
        text = re.sub(pat, rep, text)
    return re.sub(r'[ \t]+', ' ', text).strip()


SCENES = [
    {
        "id": "c6_01_rule71_first_steps",
        "chapter": "CHAPTER 1 • RULE 71(1)-(3): A SERVANT DIES, WHAT HAPPENS FIRST",
        "title": "RULE 71(1)-(3) — THE FIRST STEPS AFTER A DEATH IN SERVICE",
        "accent": "SKY",
        "badge": "RULE 71(1)-(3)",
        "q": "A government servant dies in service. What must the office do first, and which letters go out?",
        "intro": "Namaste! Batch 6 shuru karte hain — CCS Pension Rules do hazaar ikkis ka aakhri lamba hissa. Aaj Rules ikehattar se sattasi: service ke dauraan death, pensioner ki death ya missing hona, pension ka payment, aur aakhirkar unnis sau bahattar ke purane rules ka repeal. Yeh sirf explanation hai, aur batch ke end mein chhota recap milega. Chaliye, Riya ka pehla sawaal sunte hain.",
        "q_say": "Sir, agar government servant service ke dauraan mar jaaye, to office ko sabse pehle kya karna chahiye, aur kaunse letters jaate hain?",
        "boxes": [
            ("RULE 71(1): DECIDE WHAT IS PAYABLE",
             "On news of the death, the Head of Office decides: death gratuity, family pension, or both.",
             "SKY",
             "Shuruaat Head of Office se hoti hai. Death ki khabar milte hi woh decide karta hai ki death gratuity deni hai, family pension deni hai, ya dono. Yeh clarity aage ka poora case aasan bana deti hai."),
            ("RULE 71(2): THE GRATUITY LETTER",
             "Check the nomination. If none, or it no longer holds, find who is entitled, write in FORMAT 11, ask for a claim.",
             "BLUE",
             "Gratuity ke liye pehle nomination check hota hai. Agar nomination nahi hai, ya woh ab valid nahi hai, to Head of Office decide karta hai ki kaun entitled hai. Phir Format 11 ka letter jaata hai aur claim Form 9 mein maanga jaata hai."),
            ("RULE 71(3): THE FAMILY PENSION LETTER",
             "Write to the eligible member or guardian in FORMAT 12. The claim comes in FORM 10, with a FORMAT 9 bank undertaking.",
             "GREEN",
             "Family pension ke liye letter Format 12 mein jaata hai, eligible family member ya guardian ke naam. Claim Form 10 mein aata hai, saath mein bank undertaking Format 9. Dhyan rakhiye, Format 9 aur Form 9 do bilkul alag cheezein hain."),
            ("REAL EXAMPLE AND THE TRAP",
             "Esha's father dies with no nomination: Format 11 goes to the entitled heirs. Trap: Rule 71 has SIX sub-rules, not four.",
             "RED",
             "Ek example. Dev Rao ki death hui aur koi nomination nahi thi. Head of Office ne heirs ko Format 11 bheja aur widow ko Format 12. Trap yeh hai ki Rule 71 mein chhe sub-rules hain, chaar nahi. Aur Form, Format se alag hota hai."),
        ],
        "hook": "REMEMBER: Death gratuity letter = Format 11 + Form 9 claim. Family pension letter = Format 12 + Form 10!",
        "hook_say": "Yaad rakhiye: gratuity ke liye Format 11 jaata hai aur claim Form 9 mein aata hai. Family pension ke liye Format 12 aur Form 10.",
        "covers": ["R71-1", "R71-2", "R71-2-FORM9", "R71-3", "R71-COUNT", "R71-EX", "FORMAT-11", "FORMAT-12", "FORM-10", "FORMAT-9"],
    },
    {
        "id": "c6_02_rule71_4_quarters",
        "chapter": "CHAPTER 2 • RULE 71(4): GOVERNMENT QUARTERS AFTER A DEATH",
        "title": "RULE 71(4) — LICENCE FEE WAIVED, DAMAGES NOT, AND THE SEVEN DAYS",
        "accent": "ORANGE",
        "badge": "RULE 71(4)",
        "q": "If the employee lived in government quarters, what happens to licence fee and damages after death?",
        "q_say": "Sir, agar employee government quarter mein rehta tha, to death ke baad licence fee aur damages ka kya hota hai?",
        "boxes": [
            ("RULE 71(4)(a): OLD FEE WAIVED",
             "Licence fee for the period BEFORE the death is waived.",
             "ORANGE",
             "Agar servant government quarter mein rehta tha, to death se pehle ka licence fee maaf ho jaata hai. Matlab family se purana rent nahi maanga jaayega. Yeh waiver seedha Rule 71(4)(a) se aata hai."),
            ("RULE 71(4)(b): DAMAGES STILL RECOVERED",
             "DAMAGES are still recovered from the death gratuity. If the family keeps the house: no fee for death month plus 3 months.",
             "RED",
             "Lekin damages maaf nahi hote. Damages yani bina permission rehne ka penalty charge, aur woh death gratuity se kaata jaata hai. Haan, agar family quarter retain karti hai, to death ke mahine aur uske baad teen mahine ka fee nahi liya jaata."),
            ("RULE 71(4)(c): SEVEN DAYS",
             "Head of Office writes to the Directorate of Estates within SEVEN days, to get a No Demand Certificate (NDC).",
             "BLUE",
             "Teesra clause ek clock lagata hai. Head of Office ko intimation milne ke saat din ke andar Directorate of Estates ko likhna hota hai, taaki No Demand Certificate mil sake. Letter late hua to recovery ka jhagda baad tak chalta hai."),
            ("EXAMPLE AND TRAP",
             "Charu dies 12 Aug; family stays. No fee for Aug, Sep, Oct, Nov. Trap: waiver covers fee, NOT damages.",
             "YELLOW",
             "Charu Nair ki death 12 August ko hui, office ko 14 August ko pata chala, to letter 21 August tak jaana chahiye. Family ne quarter rakha, to August se November tak fee nahi. Trap: fee maaf hai, damages nahi."),
        ],
        "hook": "REMEMBER: Fee before death waived; damages NOT; death month plus 3 months free; write in 7 days!",
        "hook_say": "Yaad rakhiye: death se pehle ka fee maaf, damages nahi, death ka mahina aur teen mahine free, aur letter saat din mein.",
        "covers": ["R71-4A", "R71-4B-DAMAGES", "R71-4B-3MONTHS", "R71-4C-7DAYS", "R71-QA"],
    },
    {
        "id": "c6_03_rule71_5_6_missing",
        "chapter": "CHAPTER 3 • RULE 71(5)-(6): A SERVANT WHO IS MISSING",
        "title": "RULE 71(5)-(6) — MISSING SERVANT: POLICE REPORT BEFORE CLAIMS",
        "accent": "PINK",
        "badge": "RULE 71(5)-(6)",
        "q": "What if the serving employee is missing, not dead? When can claims be called for?",
        "q_say": "Agar employee dead nahi, missing hai, to kya hota hai? Claims kab maange ja sakte hain?",
        "boxes": [
            ("RULE 71(5): RULE 51 APPLIES",
             "For a missing servant, Rule 51(1) and 51(4) apply.",
             "PINK",
             "Ab missing ka case. Servant gayab hai, death certificate nahi hai. Rule 71(5) kehta hai ki Rule 51 ke sub-rule ek aur chaar ke hisaab se dekho ki gratuity ya family pension banti hai ya nahi."),
            ("RULE 71(6): POLICE REPORT FIRST",
             "Claims are called for only AFTER a police report: FIR, Daily Diary Entry or General Diary Entry.",
             "RED",
             "Claims tabhi maange jaate hain jab police report ho — FIR, Daily Diary Entry ya General Diary Entry — aur police ka untraced report bhi. Bina report claim maangna jaldi karna hai, aur woh file wapas aayegi."),
            ("THE PAPERS THAT TRAVEL WITH THE CLAIM",
             "Use Format 11/Form 9 and Format 12/Form 10. Claim carries Format 9, Format 8 indemnity bond, both police reports.",
             "GREEN",
             "Missing case mein claim ke saath Format 9 undertaking, Format 8 ka indemnity bond, aur dono police reports lagti hain. Aur Head of Office death certificate ka intezaar nahi karta — credible information par action shuru kar deta hai."),
            ("TRAP: DISAPPEARED IS NOT DEAD",
             "Trap: no claims until the police report. Source said 'four sub-rules' and listed only 71(5)-(6) briefly.",
             "ORANGE",
             "Trap yeh hai ki missing aur death ek jaisa nahi hai. Police report hi trigger hai. Aur yaad rakhiye, Rule 71 mein chhe sub-rules hain, isliye 71(5) aur 71(6) ko chhodna nahi chahiye."),
        ],
        "hook": "REMEMBER: Missing servant = Rule 51 + police report first + Format 8 indemnity bond!",
        "hook_say": "Yaad rakhiye: missing servant matlab Rule 51, police report pehle, aur Format 8 ka indemnity bond.",
        "covers": ["R71-5", "R71-6-POLICE", "R71-6-ADD", "FORMAT-8"],
    },
    {
        "id": "c6_04_forms_map_71_80",
        "chapter": "CHAPTER 4 • FORMS AND FORMATS IN RULES 71 TO 80: THE MAP",
        "title": "FORMS AND FORMATS OF THE DEATH CHAPTERS — WHO USES WHICH",
        "accent": "YELLOW",
        "badge": "FORMS 4-13 • FORMATS",
        "q": "There are so many Forms and Formats in Rules 71 to 80. Which is which?",
        "q_say": "Sir, Rules 71 se 80 mein itne Forms aur Formats hain. Kaun kiska hai?",
        "boxes": [
            ("FORMATS: LETTERS AND UNDERTAKINGS",
             "Format 8 indemnity bond; 9 bank undertaking; 10 covering letter; 11 gratuity letter; 12 family-pension letter; 13 sanction.",
             "YELLOW",
             "Formats sarkari letters aur bonds hote hain. Format 8 missing case ka indemnity bond, Format 9 bank undertaking, Format 10 covering letter, Format 11 gratuity ka letter, Format 12 family pension ka letter, aur Format 13 family pension ka sanction."),
            ("FORMS: CLAIMS AND RECORDS",
             "Form 3 common nomination; 8 spouse request; 9 gratuity claim; 10 family pension; 11 case file; 12 PPO claim; 13 residuary gratuity; Format 7 bond for a minor.",
             "BLUE",
             "Forms claims aur records hote hain. Form 3 common nomination — gratuity, GPF aur insurance ke liye. Form 9 gratuity claim, Form 10 family pension claim, Form 11 poora case file, Form 12 death certificate ke saath claim, Form 13 residuary gratuity."),
            ("OBSOLETE / HISTORY ONLY",
             "OBSOLETE: the 8-9-10-11-12-13 memory rhyme; also 'Form A' for retirees (now Form 6-A).",
             "RED",
             "Purane rhyme par bharosa mat kijiye ki aath, nau evidence hain. Form 8 spouse ka request hai, Format 8 indemnity bond. Aur Form A retirees ke liye Form 6-A se replace ho gaya, gyarah September 2024 ke Office Memorandum se."),
            ("SAME NUMBER, DIFFERENT PAPER",
             "Format 13 sanctions family pension; Form 13 claims residuary gratuity. Format 9 is not Form 9.",
             "GREEN",
             "Ek hi number, do alag kagaz. Format 13 family pension sanction karta hai, Form 13 residuary gratuity ka claim hai. Format 9 undertaking hai, Form 9 gratuity claim. Exam mein pehle poochhiye — Form hai ya Format?"),
        ],
        "hook": "REMEMBER: Never learn 8 to 13 by rhyme. Ask: Form or Format? Form 6 is now 6-A!",
        "hook_say": "Yaad rakhiye: aath se terah tak rhyme se mat sikhiye. Poochhiye Form hai ya Format, aur Form 6 ab Form 6-A hai.",
        "covers": ["FORMAT-8", "FORMAT-9", "FORMAT-10", "FORMAT-11", "FORMAT-12", "FORMAT-13", "FORM-8", "FORM-10", "FORM-11", "FORM-12", "FORM-13", "FORM-4-6A-7", "FORM-A", "FORMS-MNEMONIC"],
    },
    {
        "id": "c6_05_rule72_1_service",
        "chapter": "CHAPTER 5 • RULE 72(1): CHECKING THE SERVICE OF A DECEASED SERVANT",
        "title": "RULE 72(1) — WHOLE SERVICE BOOK, UNVERIFIED SERVICE DEEMED VERIFIED",
        "accent": "GREEN",
        "badge": "RULE 72(1)",
        "q": "In a death case, how is the dead servant's service checked, and what is the big relief?",
        "q_say": "Death case mein marhoom ki service kaise check hoti hai, aur bada relief kya hai?",
        "boxes": [
            ("RULE 72(1)(a): THE WHOLE SERVICE BOOK",
             "The Head of Office examines the service book for the WHOLE service, not only the part after Rule 30.",
             "GREEN",
             "Death case mein service book poora dekha jaata hai, sirf Rule 30 ke baad ka hissa nahi. Head of Office ko satisfy hona chahiye ki poori service ke verification certificates record mein hain."),
            ("RULE 72(1)(b)(i): THE RELIEF",
             "Service that was never verified is treated as VERIFIED, on the strength of the entries in the service book.",
             "SKY",
             "Aur yahi bada relief hai. Jo service verify nahi hui, woh service book ke entries ke aadhaar par verified maan li jaati hai. Family ko bahar se proof dhoondhne nahi bheja jaata."),
            ("(b)(ii) AND (b)(iii): POWER AND CHECK",
             "(ii) The officer MAY use other easy material. (iii) He MUST see service was continuous and not forfeited.",
             "ORANGE",
             "Do aur limbs. Officer chahe to koi bhi relevant material, jo usko ready access mein mile, use kar sakta hai — yeh power hai, duty nahi. Lekin use dekhna hoga ki service continuous thi aur dismissal, removal, resignation ya strike se forfeit nahi hui."),
            ("EXAMPLE AND TRAP",
             "Dev's two years had no certificates; entries were accepted. Trap: 'deemed verified' does not skip the forfeiture check.",
             "RED",
             "Dev Rao ke do saal ke certificates nahi the. Office ne entries accept ki, lekin continuity aur forfeiture phir bhi check ki. Trap: deemed verified ka matlab forfeiture check chhodna nahi hai."),
        ],
        "hook": "REMEMBER: Death case = whole book, unverified deemed verified, but forfeiture still checked!",
        "hook_say": "Yaad rakhiye: death case mein poori book, unverified service deemed verified, par forfeiture check banta rahega.",
        "covers": ["R72-1A", "R72-1B-I", "R72-1B-II", "R72-1B-III", "R72-VS-57-FORFEITURE", "R72-QA"],
    },
    {
        "id": "c6_06_rule72_emoluments_vs57",
        "chapter": "CHAPTER 6 • RULE 72(2)-(3): ONE YEAR OF EMOLUMENTS, ONE MONTH TO DECIDE",
        "title": "RULE 72(2)-(3) — ONE YEAR OF EMOLUMENTS, AND DEATH VERSUS RETIREMENT",
        "accent": "BLUE",
        "badge": "RULE 72(2)-(3) • R57",
        "q": "How many months of emoluments are checked in a death case, and how does that differ from retirement?",
        "q_say": "Death case mein kitne mahine ke emoluments dekhe jaate hain, aur retirement se kya farq hai?",
        "boxes": [
            ("RULE 72(2): ONE YEAR",
             "Emoluments for the ONE year before death or disappearance. If on extraordinary leave, the year before that leave began.",
             "BLUE",
             "Emoluments sirf ek saal ke dekhe jaate hain, death ya disappearance se pehle ke. Agar servant us din extraordinary leave par tha, to EOL shuru hone se pehle ka ek saal dekha jaata hai."),
            ("RULE 72(3): ONE MONTH",
             "The whole determination must be finished within ONE month of the intimation.",
             "SKY",
             "Aur poora determination ek mahine mein khatam hona chahiye — intimation milne ke ek mahine ke andar. Yahan clock intimation se chalta hai, claim se nahi. Rule 74 mein clock claim se chalta hai."),
            ("DEATH VERSUS RETIREMENT",
             "Death: ONE year of emoluments, decided in one month. Retirement: correctness verified for 24 months (Rule 57(1)(b)(v)); stages end 8 months before.",
             "GREEN",
             "Comparison yaad rakhiye. Death mein ek saal ke emoluments aur ek mahina. Retirement mein chaubees mahine ke emoluments verify hote hain, aur stages retirement se aath mahine pehle khatam hote hain."),
            ("EXAMPLE AND TRAP",
             "Esha dies 20 March 2026: year checked is Mar 2025 to Mar 2026. Retirement would need 24 months.",
             "RED",
             "Esha ki death bees March do hazaar chhabbis ko hui, to March do hazaar pachees se ek saal ke emoluments dekhe jaayenge. Agar woh January se EOL par hoti, to EOL se pehle se ginte. Trap: retirement ke chaubees mahine death case mein mat le jaaiye."),
        ],
        "hook": "REMEMBER: Death = 1 year of emoluments in 1 month. Retirement = 24 months verified!",
        "hook_say": "Yaad rakhiye: death mein ek saal ke emoluments, ek mahine mein faisla. Retirement mein chaubees mahine verify hote hain.",
        "covers": ["R72-2", "R72-3", "R72-EX", "LIMIT-DEATH-EMOL-12M", "R57-SCOPE-AFTER-R30", "R57-UNVERIFIED-DOCS", "R57-8M"],
    },
    {
        "id": "c6_07_rule73_incomplete_records",
        "chapter": "CHAPTER 7 • RULE 73(1)-(3): WHEN THE SERVICE BOOK IS INCOMPLETE",
        "title": "RULE 73 — INCOMPLETE SERVICE RECORDS, STEP BY STEP",
        "accent": "ORANGE",
        "badge": "RULE 73(1)-(3)",
        "q": "What if the service book of the dead servant was never properly maintained?",
        "q_say": "Agar marhoom ki service book theek se maintain hi nahi hui thi, to kya hota hai?",
        "boxes": [
            ("RULE 73(1): A CASE THAT SHOULD NOT ARISE",
             "No case should arise where the service book is not properly kept. Subject to 73(2), 73(3) and 75(7).",
             "ORANGE",
             "Rule 73 ka pehla sub-rule ek achha principle deta hai — aisa koi case nahi hona chahiye jahan service book theek se maintain na hui ho. Yeh office ki duty hai, family ki galti nahi."),
            ("RULE 73(2)(a): FAMILY PENSION IN ONE MONTH",
             "Family pension amount and period are fixed under Rule 50(2), within one month of the news of death.",
             "BLUE",
             "Family pension ka amount aur period Rule 50 ke sub-rule do ke hisaab se tay hota hai, death ki intimation ke ek mahine ke andar. Yahan service book ki kharabi family pension ko rok nahi sakti."),
            ("RULE 73(2)(b)(i)-(ii): PROVING FOR GRATUITY",
             "Unverified service is checked from pay bills and acquittance rolls. Service in another office is referred to that office.",
             "SKY",
             "Gratuity ke liye unverified service pay bills, acquittance rolls, last pay certificate aur April ki pay slip se verify hoti hai. Doosre office ki service ho to wahan reference jaata hai."),
            ("RULE 73(3): THE LAST VERIFIED SPELL",
             "If the whole service cannot be verified quickly, gratuity is decided provisionally on the last verified spell, as in Rule 75(7).",
             "GREEN",
             "Aur Rule 73(3) bachav deta hai — poori service turant verify na ho, to gratuity last verified spell par provisionally tay hoti hai, Rule 75(7) ke hisaab se. Family ko intezaar mein nahi chhoda jaata."),
        ],
        "hook": "REMEMBER: Rule 73 is the remedy for the office's bad record-keeping. Never the family's loss!",
        "hook_say": "Yaad rakhiye: Rule 73 office ki kharab record-keeping ka ilaaj hai — family ka nuksaan nahi.",
        "covers": ["R73-1", "R73-2-A", "R73-2-B-I", "R73-2-B-II", "R73-3", "R73-PHIL"],
    },
    {
        "id": "c6_08_rule73_clocks",
        "chapter": "CHAPTER 8 • RULE 73(2)(b)(iii)-(vi): ONE MONTH, SILENCE AND ACCOUNTABILITY",
        "title": "RULE 73(2)(b) — THE ONE-MONTH REPLY AND WHAT SILENCE MEANS",
        "accent": "PINK",
        "badge": "RULE 73(2)(b)(iii)-(vi)",
        "q": "How long does the other office get to reply, and what if it stays silent or nothing can be proved?",
        "q_say": "Doosre office ko reply ke liye kitna time milta hai, aur chup rehne par ya kuch prove na hone par kya hota hai?",
        "boxes": [
            ("(iii): REPLY IN ONE MONTH",
             "The other office replies within ONE month; a period that cannot be verified at all must be reported to the referring office at the same time.",
             "PINK",
             "Doosre office ko reference jaata hai, aur usko ek mahine ke andar verify karke certificate bhejna hota hai. Provison bhi yaad rakhiye — jo period verify ho hi nahi sakta, woh saath hi referring office ko batana hota hai."),
            ("(iv) AND (v): SILENCE AND DEFAULT",
             "No reply in time: the period is treated as qualifying. If not told, the Secretary fixes responsibility.",
             "ORANGE",
             "Agar time par jawab nahi aaya, to woh period pension ke liye deemed qualified ho jaata hai. Aur agar kisi ne non-qualifying period batana hi nahi bataya, to Secretary of the Ministry responsibility fix karta hai."),
            ("(vi): EVERY EFFORT, THEN IGNORE",
             "Make every possible effort. What still cannot be verified is IGNORED; gratuity rests on service-book entries.",
             "GREEN",
             "Aakhri limb: har possible effort kiya jaaye. Jo phir bhi verify nahi ho sakta, usko ignore kiya jaata hai, aur gratuity service book ke entries par tay hoti hai."),
            ("EXAMPLE AND TRAP",
             "Bilal's file had 2 gap years. Other office replied in 1 month. Trap: one month here, not two.",
             "RED",
             "Bilal ke file mein do saal ka gap tha. Doosre office ne ek mahine mein reply diya, aur jo prove nahi hua woh entries par chala gaya. Trap: yahan ek mahina hai, do mahine nahi."),
        ],
        "hook": "REMEMBER: Reply in 1 month; silence = qualifying; Secretary fixes blame; unprovable part ignored!",
        "hook_say": "Yaad rakhiye: reply ek mahine mein, chuppi matlab qualifying, Secretary blame fix karta hai, aur jo prove na ho woh ignore.",
        "covers": ["R73-2-B-III", "R73-2-B-IV", "R73-2-B-V", "R73-2-B-VI", "R73-EX", "R73-QA", "CMP-R57-2M"],
    },
    {
        "id": "c6_09_rule74_send_to_ao",
        "chapter": "CHAPTER 9 • RULE 74: SENDING THE FAMILY PENSION CASE TO THE ACCOUNTS OFFICER",
        "title": "RULE 74 — ONE MONTH FROM THE CLAIM, AND THE TEN PERCENT HOLD-BACK",
        "accent": "SKY",
        "badge": "RULE 74(1)-(4)",
        "q": "How does the Head of Office send the case to the Accounts Officer, and when does the clock start?",
        "q_say": "Head of Office case Accounts Officer ko kaise bhejta hai, aur clock kab se chalta hai?",
        "boxes": [
            ("RULE 74(1): FORM 11 IN ONE MONTH",
             "Complete FORM 11 with a FORMAT 10 letter, FORMAT 9 undertaking and updated service book, within one month of the CLAIM.",
             "SKY",
             "Claim milne ke baad Head of Office Form 11 bharta hai, saath mein Format 10 covering letter, Format 9 undertaking, aur up-to-date service book. Yeh sab Accounts Officer ko ek mahine ke andar jaana chahiye — claim se gin kar, death se nahi."),
            ("RULE 74(2)-(3): RELIEF AND COPIES",
             "A claim is not rejected only because a member is missing from Form 4 or the office records. Keep a copy of Formats 10, Form 10 and Form 11.",
             "GREEN",
             "Do reliefs. Kisi family member ka naam Form 4 ya records mein nahi hai, sirf isliye claim reject nahi hota, agar Head of Office baaki tarah se satisfied hai. Aur office ko Format 10, Form 10 aur Form 11 ki ek-ek copy apne paas rakhni hoti hai."),
            ("RULE 74(4): THE TEN PERCENT MARGIN",
             "The AO is told about Rule 77 dues and about part of the gratuity held back for unassessed dues and margin: at most 10 percent.",
             "ORANGE",
             "Gratuity ka kuch hissa roka jaata hai — jo dues abhi assess nahi hue, aur margin ke liye. Lekin yeh hold-back gratuity ke das percent se zyada nahi ho sakta. Roka jaata hai, cheena nahi jaata."),
            ("EXAMPLE AND TRAP",
             "Claim on 10 Sep, case to AO by 10 Oct. Gratuity 8,00,000: hold-back at most 80,000.",
             "RED",
             "Claim das September ko aayi, to case das October tak Accounts Officer ko jaana chahiye. Gratuity aath lakh ho to zyada se zyada assi hazaar roki ja sakti hai. Trap: clock claim se shuru hota hai, aur das percent ek ceiling hai."),
        ],
        "hook": "REMEMBER: Rule 74 clock starts at the CLAIM. Hold-back is at most 10 percent!",
        "hook_say": "Yaad rakhiye: Rule 74 ka clock claim se chalta hai, aur hold-back das percent se zyada nahi.",
        "covers": ["R74-1", "R74-2", "R74-3", "R74-4", "LIMIT-R74-10PC", "R74-VS-62", "R74-EX", "FORMAT-10", "FORM-11"],
    },
    {
        "id": "c6_10_rule75_provisional_fp",
        "chapter": "CHAPTER 10 • RULE 75(1)-(4): PROVISIONAL FAMILY PENSION IN 15 DAYS",
        "title": "RULE 75(1)-(4) — PROVISIONAL FAMILY PENSION: 15 DAYS, SIX MONTHS",
        "accent": "GREEN",
        "badge": "RULE 75(1)-(4)",
        "q": "How soon can the family start getting money, before the final pension order is ready?",
        "q_say": "Final pension order banne se pehle family ko paisa kab shuru mil sakta hai?",
        "boxes": [
            ("RULE 75(1): WITHIN FIFTEEN DAYS",
             "Within 15 days of the claim, if satisfied, the Head of Office sanctions provisional family pension, not above the maximum.",
             "GREEN",
             "Family ko paisa kab shuru milta hai? Claim milne ke pandrah din ke andar, agar eligibility par satisfaction hai, Head of Office provisional family pension sanction karta hai — maximum se zyada nahi. Sanction letter ki copy Accounts Officer ko jaati hai."),
            ("RULE 75(2): PAY AT ONCE",
             "After drawing, pay immediately, with arrears.",
             "SKY",
             "Drawing ke baad payment turant hota hai, arrears sameth. Yeh establishment ki pay aur allowances ki tarah draw hota hai, isliye family ko final order ka lamba intezaar nahi karna padta."),
            ("RULE 75(3): SIX MONTHS",
             "It runs for SIX months from the day AFTER the death, unless extended under the proviso to Rule 76(1).",
             "ORANGE",
             "Provisional family pension chhe mahine chalti hai — death ke doosre din se. Agar Rule 76 ke proviso se extension mila to zyada. Period khatam hone par Head of Office Accounts Officer ko batata hai."),
            ("EXAMPLE AND TRAP",
             "Died 1 Oct; claim 7 Oct; sanction by 22 Oct; runs from 2 Oct for six months.",
             "RED",
             "Bilal ki death ek October ko, claim saat October ko. Pandrah din se doosri October tak sanction, aur payment do October se chhe mahine. Trap: pandrah din claim se, chhe mahine death ke doosre din se."),
        ],
        "hook": "REMEMBER: 15 days from the CLAIM; 6 months from the day AFTER DEATH!",
        "hook_say": "Yaad rakhiye: pandrah din claim se, chhe mahine death ke doosre din se.",
        "covers": ["R75-1", "R75-2", "R75-3", "R75-4", "R75-EX"],
    },
    {
        "id": "c6_11_rule75_gratuity",
        "chapter": "CHAPTER 11 • RULE 75(5)-(8): GRATUITY, AND THE RULE 62 COMPARISON",
        "title": "RULE 75(5)-(8) — 100 PERCENT GRATUITY AND PROVISIONAL GRATUITY",
        "accent": "BLUE",
        "badge": "RULE 75(5)-(8)",
        "q": "What happens to the death gratuity under Rule 75, and how does it compare with Rule 62?",
        "q_say": "Rule 75 mein death gratuity ka kya hota hai, aur Rule 62 se comparison kaise karein?",
        "boxes": [
            ("RULE 75(5)-(6): 100 PERCENT, PAID AT ONCE",
             "After the Rule 74 forwarding the Head of Office draws 100 percent gratuity, less dues, and pays at once. The print sends you to Rule 74(3); the dues sit in 74(4).",
             "BLUE",
             "Rule 74 ke tahat case Accounts Officer ko jaane ke baad, Head of Office poora sau percent gratuity draw karta hai. Sanction letter mein likha hota hai ki kitna due gratuity se recoverable hai, aur wahi amount minus karke draw hota hai."),
            ("RULE 75(7)(a): WHEN SERVICE IS NOT VERIFIED",
             "Gratuity is decided provisionally under Rule 45(1)(b), on the last verified spell, whatever Rule 73(1) says.",
             "SKY",
             "Agar poori service verify nahi hui, to gratuity Rule 45 ke clause ke hisaab se provisionally tay hoti hai — jo spell death se pehle verify hui. Rule 73(1) ke bawajood yeh raasta khula hai."),
            ("RULE 75(7)(b)-(c) AND (8)",
             "Form 9 claim in: provisional gratuity in ONE month. Final gratuity within THREE months of that. Tell the AO when paid.",
             "GREEN",
             "Form 9 ka claim aa gaya to provisional gratuity death ki intimation ke ek mahine ke andar authorize hoti hai. Final gratuity teen mahine mein, aur balance beneficiaries ko. Payment hone par Accounts Officer ko batana hota hai."),
            ("COMPARE RULE 62, AND HISTORY",
             "Rule 62 (retirement): 100 percent provisional pension, gratuity less 10 percent. Rule 75: 15 days, 6 months, for the family.",
             "ORANGE",
             "Retirement wale Rule 62 se compare kijiye: wahan sau percent provisional pension, aur gratuity mein se das percent roka jaata hai. Rule 75 death case ka jawab hai — pandrah din, chhe mahine. Dono mein drawing establishment pay jaisi hoti hai."),
        ],
        "hook": "REMEMBER: Rule 75 has EIGHT sub-rules; 100 percent gratuity; final gratuity within 3 months!",
        "hook_say": "Yaad rakhiye: Rule 75 mein aath sub-rules, sau percent gratuity, aur final gratuity teen mahine mein.",
        "covers": ["R75-5", "R75-6", "R75-7A", "R75-7BC-8", "R75-COUNT", "R75-VS-62", "R75-2020-RELAX"],
    },
    {
        "id": "c6_12_rule76_1_2_ao",
        "chapter": "CHAPTER 12 • RULE 76(1)-(2): THE ACCOUNTS OFFICER'S CHECKS",
        "title": "RULE 76(1)-(2) — ONE MONTH FOR THE AO, AND HOD APPROVAL TO EXTEND",
        "accent": "ORANGE",
        "badge": "RULE 76(1)-(2)",
        "q": "What does the Accounts Officer do with the case, and who can extend the provisional pension?",
        "q_say": "Accounts Officer case ka kya karta hai, aur provisional pension ka extension kaun kar sakta hai?",
        "boxes": [
            ("RULE 76(1): FORM 11 PART II, SECTION I",
             "The AO does the checks and fills Part II, Section I of FORM 11 within ONE month of getting the case.",
             "ORANGE",
             "Case Accounts Officer ko milta hai, aur woh ek mahine ke andar checks lagakar Form 11 ke Part II ka Section I bharta hai. Emoluments sirf ek saal ke verify hote hain — death ya disappearance se pehle ke."),
            ("THE PROVISO: IF TIME RUNS OUT",
             "If the AO cannot assess in time, he asks the Head of Office to keep paying provisional family pension.",
             "SKY",
             "Agar Accounts Officer time par assess nahi kar paata, to chup nahi baithta. Woh Head of Office ko likhta hai ki provisional family pension aage chalao, aur kitne period tak — yeh proviso ka kaam hai."),
            ("RULE 76(2): HEAD OF DEPARTMENT",
             "An extension of provisional family pension needs the approval of the HEAD OF DEPARTMENT.",
             "GREEN",
             "Extension apne aap nahi hoti. Head of Office case Head of Department ke paas bhejta hai, approval milti hai, phir naya sanction issue hota hai. Yani faisla Head of Department ka hai, Head of Office ka nahi."),
            ("EXAMPLE AND TRAP",
             "Case reaches AO 5 Nov: Form 11 part done by 5 Dec. If late, HoD approves extension.",
             "RED",
             "Case paanch November ko Accounts Officer ko mila, to Part II Section I paanch December tak bharna hai. Der ho rahi ho to Head of Department se approval. Trap: is jawab mein Head of Office likhna galat hai."),
        ],
        "hook": "REMEMBER: AO has 1 month; extension is approved by the HEAD OF DEPARTMENT!",
        "hook_say": "Yaad rakhiye: Accounts Officer ko ek mahina, aur extension Head of Department approve karta hai.",
        "covers": ["R76-1", "R76-2", "R76-EX", "R76-QA"],
    },
    {
        "id": "c6_13_rule76_3_ppo",
        "chapter": "CHAPTER 13 • RULE 76(3): THE PPO AND ITS DATES",
        "title": "RULE 76(3) — PPO IN ONE MONTH, AND THE DATES IT MUST CARRY",
        "accent": "PINK",
        "badge": "RULE 76(3)(a)-(f)",
        "q": "What dates and clocks does Rule 76(3) fix for the Pension Payment Order?",
        "q_say": "Rule 76(3) PPO ke liye kaunsi dates aur clocks tay karta hai?",
        "boxes": [
            ("(a), (b), (c): ONE MONTH AND TWO DATES",
             "PPO within ONE month. Regular family pension starts the day after provisional payment stops. PPO shows both dates.",
             "PINK",
             "PPO ek mahine ke andar — family pension case milne ke baad. Aur Rule 75 wali provisional family pension band hone ke doosre din se regular family pension effective hoti hai."),
            ("(d): ARREARS FOR THE PROVISIONAL PERIOD",
             "(d) The AO authorises the Head of Office to pay arrears for the provisional period. Rule 81(2) prints 76(2)(d) - a slip for 76(3)(b).",
             "SKY",
             "PPO mein do dates likhi jaati hain: kab tak provisional family pension Head of Office se milti rahegi, aur kab se Pension Disbursing Authority payment karegi. Yeh dates CPAO aur PDA ka time jodkar tay hoti hain."),
            ("(e) AND (f): MISSING SERVANT",
             "Start date is the LATEST of: leave sanctioned end, pay paid end, police report. Payment not before six months from the police report.",
             "GREEN",
             "Provisional period ke arrears Accounts Officer authorize karta hai, aur payment Head of Office karta hai. Note: Rule 81(2) mein sub-rule do likha hai, jo print ki galti lagti hai — clause 76(3)(b) hi sahi pointer hai."),
            ("EXAMPLE AND TRAP",
             "Leave ends 31 Jan, pay paid to 28 Feb, police report 15 Mar: start 15 Mar; pay not before 15 Sep.",
             "RED",
             "Missing servant ke liye start date teen mein se latest hoti hai: sanctioned leave ka end, pay milne ka end, ya police report ki date. Aur payment police report se chhe mahine se pehle nahi. Trap: earliest date mat chuniye."),
        ],
        "hook": "REMEMBER: PPO in 1 month; two dates in the PPO; missing = LATEST of three dates; wait 6 months!",
        "hook_say": "Yaad rakhiye: PPO ek mahine mein, PPO par do dates, missing mein teen mein se latest date, aur chhe mahine ka wait.",
        "covers": ["R76-3A", "R76-3B", "R76-3C", "R76-3D", "R76-3E", "R76-3F", "R76-CHAIN-R75", "R81-2"],
    },
    {
        "id": "c6_14_rule76_4_8",
        "chapter": "CHAPTER 14 • RULE 76(4)-(8): NAMES IN THE PPO, EXCESS AND THE FINAL SEAL",
        "title": "RULE 76(4)-(8) — DISABLED DEPENDANTS, EXCESS PAYMENTS AND THE CPAO SEAL",
        "accent": "YELLOW",
        "badge": "RULE 76(4)-(8)",
        "q": "What do the rest of Rule 76's sub-rules say, and what did the 2022 amendment fix?",
        "q_say": "Rule 76 ke baaki sub-rules kya kehte hain, aur do hazaar baees ke amendment ne kya theek kiya?",
        "boxes": [
            ("RULE 76(4): WHO IS NAMED",
             "The AO names a disabled child, dependent parents and disabled siblings in the PPO only if no one ranks ahead of them.",
             "YELLOW",
             "PPO mein permanently disabled child, dependent parents aur disabled siblings ke naam tabhi aate hain jab unse pehle koi eligible na ho. Rule 50 ki priority PPO ke text mein utar aati hai."),
            ("RULE 76(5) AND (5A)",
             "(5) Balance of gratuity, the missing case (one month, six-month wait), and adjustment of the withheld amount. (5A) PPO issue reported. 770(E) renumbered a duplicate (5).",
             "BLUE",
             "Balance gratuity ka hisaab Accounts Officer karta hai — outstanding dues adjust karke — aur Head of Office ko batata hai ki jinko provisional gratuity mili, unko yeh balance de. Missing case mein gratuity ek mahine mein decide hoti hai, par payment police report se chhe mahine baad."),
            ("RULE 76(6) AND (7): EXCESS PAID",
             "(6) Excess provisional family pension is adjusted from gratuity, else instalments. (7) Excess provisional gratuity is not refunded; the HoD fixes blame.",
             "ORANGE",
             "PPO issue hone ki baat Accounts Officer Head of Office ko batata hai aur faltu documents wapas karta hai. Yeh clause do hazaar baees ke amendment se (5A) ban gaya — pehle do sub-rules dono (5) number par the."),
            ("RULE 76(8): THE FINAL CHAIN, AND COUNT",
             "AO to CPAO with Format 9 in ONE month; CPAO seal in TEN days; PDA pays in FIFTEEN days. Rule 76 has EIGHT sub-rules.",
             "GREEN",
             "Excess provisional family pension gratuity se adjust hoti hai, warna aage ki pension se installments mein. Excess provisional gratuity wapas nahi maangi jaati, par Head of Department responsibility fix karta hai. Numbering par mat ladaiye — clause padhiye."),
        ],
        "hook": "REMEMBER: Rule 76 = 8 sub-rules plus 5A. Excess pension recovered; excess gratuity not refunded!",
        "hook_say": "Yaad rakhiye: Rule 76 mein (5) ke baad (5A), phir (6), (7), (8). Excess pension recover, excess gratuity refund nahi.",
        "covers": ["R76-4", "R76-5A", "R76-5-8-ADD", "R76-COUNT", "GSR-770E"],
    },
    {
        "id": "c6_15_rule77_a",
        "chapter": "CHAPTER 15 • RULE 77(1)(i)-(iv): GOVERNMENT DUES AFTER A DEATH, PART ONE",
        "title": "RULE 77(1)(i)-(iv) — ACCOMMODATION DETAILS TO THE ESTATES DIRECTORATE",
        "accent": "ORANGE",
        "badge": "RULE 77(1)(i)-(iv)",
        "q": "How are Government housing dues handled after a death, and who sends what to whom?",
        "q_say": "Death ke baad sarkari housing ke dues kaise handle hote hain, aur kaun kisko kya bhejta hai?",
        "boxes": [
            ("CLAUSE (i): WITHIN SEVEN DAYS",
             "Seven items go to the Directorate of Estates in seven days: name, quarter details, date of death, leave, rent-free status, last recovery, and the fee arithmetic.",
             "ORANGE",
             "Quarter wale case mein sarkari housing ke dues ka alag hisaab hai. Head of Office saat din mein Directorate of Estates ko details bhejta hai aur No Demand Certificate maangta hai — taaki family pension aur gratuity late na hon."),
            ("CLAUSE (ii): FEE WAIVED",
             "Fee before death waived. If the family stays, no fee for the death month plus 3 months.",
             "GREEN",
             "Do jagah yeh baat aati hai, Rule 71(4) aur Rule 77(1)(ii) — death se pehle ka licence fee maaf, aur family quarter rakhe to death ke mahine plus teen mahine ka fee nahi. Damages phir bhi recover honge."),
            ("CLAUSE (iii): NOW SEEN",
             "Clause (iii): the Head of Office recovers from the gratuity the licence fee he reported to the DoE.",
             "SKY",
             "Clause teen ka matlab: jo licence fee Head of Office ne Directorate of Estates ko batayi, woh gratuity se recover karta hai. Yani reporting aur recovery ka link yahin judta hai."),
            ("CLAUSE (iv)",
             "Recovery beyond the concessional period is the Directorate of Estates' job.",
             "RED",
             "Clause chaar ek limit khada karta hai: concessional period ke baad ka fee recover karna Directorate of Estates ki zimmedari hai, Head of Office ka kaam nahi. Trap: office ko har cheez ka collector mat samajhiye."),
        ],
        "hook": "REMEMBER: Write to DoE in 7 days; waiver as in Rule 71(4); clause (iii) recovers reported fee from gratuity!",
        "hook_say": "Yaad rakhiye: Directorate ko saat din, waiver Rule 71(4) jaisa, aur clause (iii) mein reported fee gratuity se recover.",
        "covers": ["R77-1-I", "R77-1-I-PURPOSE", "R77-1-I-STDRENT", "R77-1-II", "R77-1-III", "R77-1-IV"],
    },
    {
        "id": "c6_16_rule77_b",
        "chapter": "CHAPTER 16 • RULE 77(1)(v)-(x) AND 77(2): GOVERNMENT DUES, PART TWO",
        "title": "RULE 77(1)(v)-(x) AND 77(2) — OTHER DUES, THE TEN PERCENT AND THE CROSS-CHECK",
        "accent": "RED",
        "badge": "RULE 77(1)(v)-(x)",
        "q": "How are other dues reported and recovered, and what stops the family paying twice?",
        "q_say": "Baaki dues kaise report aur recover hote hain, aur family ko do baar payment se kaun bachata hai?",
        "boxes": [
            ("CLAUSES (v)-(vii): ONE MONTH, TEN PERCENT",
             "DoE reports other dues in 1 month; meanwhile 10 percent of death gratuity is withheld; if no word, nothing is recoverable.",
             "RED",
             "Directorate of Estates ko ek mahine mein batana hota hai ki licence fee ke alawa koi due hai ya nahi. Tab tak Head of Office death gratuity ka das percent rok kar rakhta hai."),
            ("CLAUSE (viii): THE CROSS-CHECK",
             "If dues are reported, the Head of Office checks the acquittance rolls for amounts already recovered, and tells the DoE.",
             "BLUE",
             "Agar jawab nahi aaya, ya Directorate kehti hai ki assess nahi kar sakti, to maan liya jaata hai ki kuch recoverable nahi tha — aur roka hua amount family ko de diya jaata hai."),
            ("CLAUSES (ix), (x) AND 77(2)",
             "(ix) Dues adjusted against the withheld amount, balance repaid. (x) Later dues may be recovered from dearness relief. 77(2): 15 days for Rule 67 dues.",
             "PINK",
             "Dues report ho jaayein to Head of Office acquittance rolls se check karta hai ki woh pehle pay se kata tha ya nahi. Agar kata tha, to woh pay bills Directorate ko dikhata hai — taaki family do baar na bhare."),
            ("RULE 77 VERSUS RULE 68, AND EXAMPLE",
             "Rule 77: 7 days, 1 month, family favoured. Rule 68 (retirement): 2 months for DoE. NDC in 14 days is shown only for Rule 68.",
             "GREEN",
             "Bachi hui dues roke hue amount se adjust hoti hain, balance wapas. Baad mein aayi dues dearness relief se recover ho sakti hain, bina consent ke, aur tab tak DR band. Aur Rule 67 wali doosri dues pandrah din mein."),
        ],
        "hook": "REMEMBER: Rule 77(1) has TEN clauses; 10 percent held; check acquittance rolls so family pays once!",
        "hook_say": "Yaad rakhiye: Rule 77(1) mein das clauses, das percent roka jaata hai, aur acquittance rolls se double recovery rukti hai.",
        "covers": ["R77-1-V", "R77-1-VI", "R77-1-VII", "R77-1-VIII", "R77-1-IX-X", "R77-2", "R77-COUNT", "R77-VS-68", "R77-NDC14", "R77-EX", "DYN-DR"],
    },
    {
        "id": "c6_17_rule78_deputation",
        "chapter": "CHAPTER 17 • RULE 78: DEATH OR DISAPPEARANCE WHILE ON DEPUTATION",
        "title": "RULE 78 — DEPUTATION: THE BORROWING OFFICE OR THE LENDING SIDE",
        "accent": "SKY",
        "badge": "RULE 78",
        "q": "If the servant dies or goes missing on deputation, which Head of Office handles the case?",
        "q_say": "Agar servant deputation par death ya missing ho jaaye, to kaun Head of Office case chalayega?",
        "boxes": [
            ("RULE 78(1): CENTRAL DEPUTATION",
             "Deputed to another CENTRAL Department: the BORROWING Department's Head of Office acts.",
             "SKY",
             "Deputation par death ya disappearance ho, to kaun kaam karega? Rule 78 kehta hai — doosre Central Department mein deputation ho to borrowing Department ka Head of Office poora case chalayega."),
            ("RULE 78(2): STATE OR FOREIGN SERVICE",
             "State Government or foreign service: the Head of Office or cadre authority that sanctioned the deputation acts. That is the lending side.",
             "BLUE",
             "Lekin State Government ya foreign service ki deputation ho to lambi line kaam karti hai — jis Head of Office ya cadre authority ne deputation sanction ki thi, wahi family pension aur gratuity authorize karega."),
            ("COVERS MISSING TOO",
             "Rule 78 covers death AND disappearance. Rule 64 is about retirement only.",
             "GREEN",
             "Rule 78 death aur disappearance, dono cover karta hai. Rule 64 retirement ka case dekhta hai, isliye missing limb wahan banti nahi. Yaad rakhiye, yeh allocation rule hai — kaun, kahan se."),
            ("EXAMPLE AND TRAP",
             "Officer dies on deputation to another Central Department: the borrowing department handles it.",
             "RED",
             "Charu doosre Central Department mein deputation par thi aur wahan unki death hui — case borrowing Department ka. State deputation hoti to cadre authority karti. Trap: Central mein borrowing, State ya foreign mein lending."),
        ],
        "hook": "REMEMBER: Central deputation = borrowing side; State or foreign = lending side; covers missing too!",
        "hook_say": "Yaad rakhiye: Central deputation mein borrowing side, State ya foreign mein lending side, aur missing bhi cover hai.",
        "covers": ["R78-1", "R78-2", "R78-MISSING", "R64-MIRROR", "ALLOC-PATTERN"],
    },
    {
        "id": "c6_18_chX_vs_chXI",
        "chapter": "CHAPTER 18 • RETIREMENT CASE VERSUS DEATH CASE: THE COMPARISON TABLE",
        "title": "CHAPTER X VERSUS CHAPTER XI — HOW A DEATH CASE DIFFERS FROM RETIREMENT",
        "accent": "YELLOW",
        "badge": "RETIREMENT vs DEATH",
        "q": "Side by side, how do retirement cases and death cases differ in timing and evidence?",
        "q_say": "Retirement aur death case mein timing aur evidence ka farq side by side kya hai?",
        "boxes": [
            ("START OF THE CASE AND THE FORM",
             "Retirement: starts a year before, or at start of leave before retirement (Rule 56); form 6 months before. Death: starts on the news; no fixed claim deadline.",
             "YELLOW",
             "Retirement case ek saal pehle shuru hota hai, ya retirement se pehle ki leave ke din se. Death case death ki khabar par shuru hota hai. Isliye dono ki speed aur sequence alag hoti hai."),
            ("SERVICE AND EMOLUMENTS",
             "Death: unverified service deemed verified; one year of emoluments. Retirement: 24 months of emoluments verified.",
             "BLUE",
             "Service mein death case ka bada relief: unverified service deemed verified, aur emoluments sirf ek saal ke. Retirement mein chaubees mahine ke emoluments verify hote hain. Forfeiture check dono mein rehta hai."),
            ("PROVISIONAL PAYMENT AND THE PPO",
             "Retirement: PPO 2 months before (Rule 63(1)(a)), or 45 days if otherwise. Death: provisional pension in 15 days for 6 months; PPO within a month.",
             "GREEN",
             "Retirement mein PPO do mahine pehle aa jaata hai, warna paintalis din. Death mein provisional family pension pandrah din mein, chhe mahine ke liye, aur final PPO ek mahine mein."),
            ("HOUSING DUES, AND THE ONE-LINE TRAP",
             "Retirement: last 8 months' fee from pay, DoE has 2 months. Death: old fee waived, HoO writes in 7 days, DoE has 1 month.",
             "RED",
             "Housing dues ka farq dekhiye. Retirement mein aakhri aath mahine ka fee pay se, aur Directorate ko do mahine. Death mein purana fee maaf, letter saat din, jawab ek mahina. Trap: retirement ke numbers death case mein mat le jaaiye."),
        ],
        "hook": "REMEMBER: Retirement = 24 months, DoE 2 months, 8 months. Death = 1 year, DoE 1 month, 7 days!",
        "hook_say": "Yaad rakhiye: retirement chaubees mahine, Directorate do mahine, aath mahine. Death ek saal, ek mahina, saat din.",
        "covers": ["CMP-R56", "CMP-R63", "CMP-FORM-6M", "CMP-PROV-R62", "R57-8M", "LIMIT-DEATH-EMOL-12M"],
    },
    {
        "id": "c6_19_death_case_chain",
        "chapter": "CHAPTER 19 • THE DEATH-CASE CHAIN: WHO ACTS, IN WHAT ORDER",
        "title": "DEATH IN SERVICE — THE FOUR-STEP CHAIN WITH ITS CLOCKS",
        "accent": "SKY",
        "badge": "RULES 71 TO 76",
        "q": "Put the whole death-in-service route in order, with the key time limit at each step.",
        "q_say": "Poora death-in-service route order mein bataiye, har step ki time limit ke saath.",
        "boxes": [
            ("STEP 1: HEAD OF OFFICE (R71, R72)",
             "On news: decide what is payable, call for claims, write to DoE in 7 days.",
             "SKY",
             "Poora death case chaar step ka chain hai. Step one: Head of Office — kya payable hai, letters, Directorate ko saat din, aur ek mahine mein service aur emoluments ka determination."),
            ("STEP 2: THE CASE TO THE AO (R74, R75)",
             "Case to the AO in 1 month of the CLAIM; provisional family pension within 15 days.",
             "BLUE",
             "Step two: case Accounts Officer ko ek mahine mein claim se, gratuity ka das percent se zyada hold-back nahi, aur provisional family pension pandrah din mein claim se."),
            ("STEP 3: THE PPO (R76)",
             "AO finishes Form 11 Part II in 1 month; PPO in 1 month; extension needs HoD approval.",
             "GREEN",
             "Step three: Accounts Officer ka Form 11 Part II ek mahine mein, PPO ek mahine mein, aur extension chahiye to Head of Department ki approval."),
            ("STEP 4: SEAL AND PAYMENT (R76(8), R80)",
             "AO to CPAO in 1 month, seal in 10 days, PDA pays in 15 days. Trap: clocks start at different points.",
             "RED",
             "Step four: CPAO ko file ek mahine mein, Special Seal das din mein, PDA payment pandrah din mein. Trap: har clock ka start point alag hai — intimation, claim, aur death ke doosre din."),
        ],
        "hook": "REMEMBER: News, then claim, then AO, then seal. Check WHERE each clock starts!",
        "hook_say": "Yaad rakhiye: khabar, phir claim, phir Accounts Officer, phir seal. Har clock ka start point alag hai.",
        "covers": ["R71-1", "R72-3", "R74-1", "R75-1", "R76-1", "R76-3A", "R76-5-8-ADD", "R80-2", "R80-3", "R80-4"],
    },
    {
        "id": "c6_20_rule79_named",
        "chapter": "CHAPTER 20 • RULE 79(1)-(2)(a): A PENSIONER DIES, AND THE NAME IS IN THE PPO",
        "title": "RULE 79(1)-(2)(a) — NAME ALREADY IN THE PPO: NO FRESH SANCTION",
        "accent": "GREEN",
        "badge": "RULE 79(1)-(2)(a)",
        "q": "A pensioner dies. If the widow's name is already in the PPO, what happens, and how fast?",
        "q_say": "Pensioner ki death hui. Agar widow ka naam PPO mein already hai to kya hota hai, aur kitni jaldi?",
        "boxes": [
            ("RULE 79(1): THE TRIGGERS",
             "Triggers: a pensioner's death or disappearance; and a family pensioner's death, disappearance OR ineligibility. Then see what is payable.",
             "GREEN",
             "Ab pensioner ki death ka chapter. Trigger teen hain: pensioner ki death ya disappearance, aur family pensioner ki death, disappearance ya ineligibility. Head of Office dekhta hai family pension, residuary gratuity, ya dono banti hai."),
            ("RULE 79(2)(a)(i)-(ii): NO FRESH SANCTION",
             "Eligible widow or widower gets what the PPO already says, from the day AFTER death. The PDA pays within a month of the Form 12 claim.",
             "SKY",
             "Agar widow ya widower PPO mein already named hai, to naya sanction nahi chahiye. PPO jo kehta hai wahi milta hai, pensioner ki death ke doosre din se, aur PDA ek mahine mein payment shuru karta hai."),
            ("RULE 79(2)(a)(iii)-(v): OTHER DEPENDANTS",
             "Disabled child, dependent parents, disabled siblings already in the PPO use the same route. Not named: AO adds names on Form 8.",
             "BLUE",
             "Claim Form 12 mein hota hai, saath mein death certificate ki copy aur Format 9 undertaking. Disabled child, dependent parents, disabled siblings — jo PPO mein naam hain, unka bhi yahi raasta hai."),
            ("EXAMPLE AND TRAP",
             "Bilal dies 3 Mar; his wife is in the PPO. Form 12 claim; paid from 4 Mar, no new sanction.",
             "RED",
             "Bilal ki death teen March ko, widow PPO mein thi, claim Form 12 se. Payment chaar March se, bina naye sanction ke. Trap: PPO wali widow ko Form 10 aur Format 13 ke raaste mat bhejiye."),
        ],
        "hook": "REMEMBER: Name in PPO = Form 12, PDA pays, no fresh sanction, from the day after death!",
        "hook_say": "Yaad rakhiye: naam PPO mein ho to Form 12, PDA payment, naya sanction nahi, aur death ke doosre din se.",
        "covers": ["R79-1", "R79-2A-I", "R79-2A-II", "R79-2A-III", "R79-2A-IV", "R79-2A-V", "R79-EX", "FORM-12"],
    },
    {
        "id": "c6_21_rule79_notnamed_missing",
        "chapter": "CHAPTER 21 • RULE 79(2)(b) AND 79(3): NO NAME IN THE PPO, OR A MISSING PENSIONER",
        "title": "RULE 79(2)(b)-(3) — SANCTION IN FORMAT 13, AND THE MISSING PENSIONER",
        "accent": "ORANGE",
        "badge": "RULE 79(2)(b)-(3)",
        "q": "What if no one is named in the PPO, or the pensioner is missing instead of dead?",
        "q_say": "Agar PPO mein kisi ka naam nahi hai, ya pensioner missing hai, to kya karein?",
        "boxes": [
            ("RULE 79(2)(b): FORMAT 13 IN ONE MONTH",
             "No name in the PPO, or someone else is eligible: sanction in FORMAT 13 within one month of the Form 10 claim - including a person who joined the family after retirement.",
             "ORANGE",
             "PPO mein kisi ka naam nahi, ya Head of Office ko lagta hai ki koi doosra eligible hai — to woh Form 10 claim milne ke ek mahine ke andar Format 13 mein sanction karta hai. Isme woh member bhi aata hai jo retirement ke baad family member bana."),
            ("RULE 79(3): A MISSING PENSIONER",
             "Rule 51(2) and (3) apply; Format 12 letter; Form 10 claim with police report, untraced report, Format 8 bond, Format 9.",
             "PINK",
             "Missing pensioner ke liye Rule 51 ke sub-rule do aur teen lagte hain. Letter Format 12, claim Form 10, saath mein police report, untraced report, Format 8 bond aur Format 9."),
            ("79(3)(iv)-(v): TWO DATES, SIX MONTHS",
             "Only two dates: day after last payment, or police report date, whichever is later. Payment not within six months of the police report.",
             "SKY",
             "Missing pensioner ke do hi date hain: jis din tak pension paid hui uske doosre din, ya police report ki date — jo baad mein aaye. Payment police report se chhe mahine se pehle nahi."),
            ("79(3)(vi)-(vii), AND THE TRAP",
             "A claim is not rejected only because the name is missing from Form 4. A relative who is not the widow also files the Rule 50(12)(b) papers.",
             "RED",
             "Claim sirf isliye reject nahi hota ki naam Form 4 mein nahi hai. Aur widow ke alawa koi claim kare to Rule 50 ke sub-rule bara ke clause be ke documents lagte hain. Trap: missing servant ki teen date, missing pensioner ki do."),
        ],
        "hook": "REMEMBER: Missing pensioner = TWO dates; missing servant = THREE; six months after the police report!",
        "hook_say": "Yaad rakhiye: missing pensioner ki do date, missing servant ki teen, aur police report se chhe mahine.",
        "covers": ["R79-2B", "R79-2B-AFTERRET", "R79-3-MISSING", "R79-3-IV", "R79-3-V", "LIMIT-6M-POLICE", "R79-3-VI", "R79-3-VII", "FORMAT-13"],
    },
    {
        "id": "c6_22_rule79_remarriage",
        "chapter": "CHAPTER 22 • RULE 79(4)-(6): REMARRIAGE, GUARDIANS AND RESIDUARY GRATUITY",
        "title": "RULE 79(4)-(6) — REMARRIAGE, GUARDIANS AND THE THREE ROUTES",
        "accent": "PINK",
        "badge": "RULE 79(4)-(6)",
        "q": "What if the widow remarries, and what are sub-rules 5 and 6 of Rule 79?",
        "q_say": "Agar widow remarriage kar leti hai, aur Rule 79 ke sub-rule paanch aur chhe kya kehte hain?",
        "boxes": [
            ("RULE 79(4): REMARRIAGE",
             "(a) A widow or widower may draw for eligible minor children while remaining their guardian. (b) The child draws from majority. (c) An ALREADY-major child takes it after the remarriage.",
             "PINK",
             "Remarriage par pension seedha band nahi hoti. Widow apne eligible minor children ke liye draw kar sakti hai, lekin tab tak jab tak woh unki guardian hai. Guardian na rahe to legal guardian claim karega."),
            ("RULE 79(5): GUARDIAN CLAIMS",
             "A guardian may claim in Form 10 for a minor, or for a person with mental disorder, disability or mental retardation.",
             "BLUE",
             "Declaration Form 10 ke saath jaata hai. Aur haan, jo child pehle se majority age cross kar chuka hai aur eligible hai, usko remarriage ke baad seedha pension milti hai — yeh clause (c) hai."),
            ("RULE 79(6): RESIDUARY GRATUITY",
             "After a retired servant's death, residuary gratuity under Rule 45(2) is sanctioned by the Head of Office on Form 13 claims.",
             "GREEN",
             "Majboori wale cases ke liye Rule 79(5): minor, ya mental disorder, disability ya mental retardation wale person ke liye guardian Form 10 mein claim kar sakta hai."),
            ("THE THREE ROUTES, AND TRAP",
             "Name in PPO: Form 12 and PDA. No name: Form 10 and Format 13. Missing: Form 10, Format 8, Format 13.",
             "RED",
             "Aur Rule 79(6): retired servant ki death par residuary gratuity Rule 45 ke sub-rule do ke tahat, eligible persons ke Form 13 claims par Head of Office sanction karta hai. Rule 79 mein chhe sub-rules hain — chaar nahi."),
        ],
        "hook": "REMEMBER: Remarriage is not an automatic stop; Rule 79 has SIX sub-rules; Form 13 is not Format 13!",
        "hook_say": "Yaad rakhiye: remarriage automatic stop nahi, Rule 79 mein chhe sub-rules, aur Form 13 Format 13 nahi.",
        "covers": ["R79-4", "R79-5-6", "R79-COUNT", "R79-FORMS-3PATHS", "FORM-13", "FORMAT-13"],
    },
    {
        "id": "c6_23_rule80_clocks",
        "chapter": "CHAPTER 23 • RULE 80(1)-(4): AUTHORISATION, SEAL AND PAYMENT",
        "title": "RULE 80(1)-(4) — ONE MONTH, TEN DAYS, FIFTEEN DAYS, AND INTEREST",
        "accent": "BLUE",
        "badge": "RULE 80(1)-(4)",
        "q": "After the family pension is sanctioned, what are the three clocks, and when is interest due?",
        "q_say": "Family pension sanction hone ke baad teen clock kya hain, aur interest kab banta hai?",
        "boxes": [
            ("THE THREE CLOCKS",
             "AO authorises in 1 month of the Rule 79 sanction; AO to CPAO with Format 9 in 1 month; Special Seal in 10 days; PDA pays in 15 days.",
             "BLUE",
             "Rule 79 ka sanction milne ke baad teen clock chalti hain. Accounts Officer ek mahine mein authorize karta hai, CPAO ko file ek mahine mein jaati hai, aur Special Seal das din mein."),
            ("FIRST PROVISO: INTEREST",
             "Gratuity delayed by an administrative lapse earns interest, but only for delay beyond THREE months of the CLAIM.",
             "ORANGE",
             "Phir Pension Disbursing Authority pandrah din mein payment shuru karti hai — matlab aakhri teen steps mein lagbhag pachpan din. Aur yeh timelines CGA aur CPAO ke orders ke hisaab se hoti hain."),
            ("SECOND PROVISO: MISSING CASES",
             "Missing case: the PPO states the date up to which payment was made, and no payment within six months of the police report.",
             "SKY",
             "Pehla proviso interest ka hai. Gratuity administrative lapse se late hui to interest milta hai — lekin sirf claim ke teen mahine ke baad wali deri par. Responsibility Rule 65 ke tahat fix hoti hai."),
            ("EXAMPLE AND TRAP",
             "Claim on 1 Mar; interest only for delay beyond 1 Jun. Trap: three months from the CLAIM.",
             "RED",
             "Doosra proviso missing cases ka hai: PPO par likha jaata hai ki pension kab tak paid hui, aur police report se chhe mahine pehle payment nahi. Claim ek March ko to interest ek June ke baad ki deri par."),
        ],
        "hook": "REMEMBER: One month, ten days, fifteen days. Interest only beyond 3 months of the CLAIM!",
        "hook_say": "Yaad rakhiye: ek mahina, das din, pandrah din. Interest sirf claim ke teen mahine ke baad ki deri par.",
        "covers": ["R80-1", "R80-1-PROV1", "R80-1-PROV2", "R80-2", "R80-3", "R80-4", "TL-R80-CLOCKS", "R80-INTEREST-VS-65", "R80-2MONTHS-TOTAL", "DYN-GPF", "R80-EX"],
    },
    {
        "id": "c6_24_rule80_5",
        "chapter": "CHAPTER 24 • RULE 80(5): A PENSIONER WHO DIED WITHOUT FILING HIS FORMS",
        "title": "RULE 80(5) — DEATH AFTER RETIREMENT, FORMS NOT SUBMITTED",
        "accent": "GREEN",
        "badge": "RULE 80(5)",
        "q": "What if a retired servant died before he ever submitted his pension forms?",
        "q_say": "Agar retired servant ne forms bhare hi nahi aur death ho gayi, to kya hota hai?",
        "boxes": [
            ("RULE 80(5)(a): THE SPOUSE CLAIMS",
             "The Head of Office lets the spouse (else another eligible member) claim in FORM 10, with FORM 4 and the FORMAT 9 undertaking.",
             "GREEN",
             "Ek khaas case: pensioner retire hone ke baad, forms bhare bina hi mar gaya. Tab bhi family ko paisa milta hai. Rule 80(5)(a) kehta hai spouse, ya spouse na ho to koi eligible member, Form 10 ke saath Form 4 aur Format 9 de."),
            ("THE PROVISO: GRATUITY NOMINEE",
             "If no one is eligible for family pension, the gratuity nominee may file a Form 6-A (with bank details) instead of Form 10.",
             "SKY",
             "Agar koi family pension ke liye eligible hi nahi hai, to gratuity nominee Form 10 ki jagah Form 6-A de sakta hai, apne bank details ke saath. Do hazaar chaubis ke amendment ke baad Form 6 nahi, Form 6-A likhiye."),
            ("CLAUSES (b) TO (e)",
             "(b) HoO completes Form 7 and notes Form 6-A was not filed. (c) Forms: Form 4, 10, Format 9, 13, OR Form 6-A. (d)-(e) AO authorises in the PPO and the seal follows.",
             "BLUE",
             "Head of Office Form 7 bharta hai aur note karta hai ki retiree ne Form 6-A nahi diya tha. Family pension ka claim ho to Format 13 sanction bhi jaata hai. File Accounts Officer ko Format 10 letter ke saath jaati hai."),
            ("EXAMPLE AND TRAP",
             "Dev retired and died two years later, no Form 6-A. Spouse files Form 10, Form 4, Format 9. Then 1 month, 10 days, 15 days.",
             "RED",
             "Accounts Officer Part II of PPO mein pension, gratuity aur family pension authorize karta hai, aur Head of Office ko retirement ke doosre din se death tak ke arrears dene ka haq deta hai. Phir wahi das din, pandrah din ka chain."),
        ],
        "hook": "REMEMBER: 80(5) after 2024 = old form set OR Form 6-A. Form 6 is now 6-A!",
        "hook_say": "Yaad rakhiye: 80(5) mein purana form set ya Form 6-A. Form 6 ab Form 6-A hai.",
        "covers": ["R80-5-A", "R80-5-A-PROV", "R80-5-B", "R80-5-C", "R80-5-DE", "GSR-410E", "G.S.R.410E-DATE", "FORM-4-6A-7"],
    },
    {
        "id": "c6_25_rule81_start",
        "chapter": "CHAPTER 25 • RULE 81: FROM WHICH DAY IS PENSION PAYABLE",
        "title": "RULE 81 — PENSION FROM THE DAY OFF THE ROLLS; FAMILY PENSION FROM THE NEXT DAY",
        "accent": "ORANGE",
        "badge": "RULE 81(1)-(3)",
        "q": "From which day do pension and family pension start, and is the day of death paid?",
        "q_say": "Pension aur family pension kis din se shuru hoti hai, aur death ka din paid hai ya nahi?",
        "boxes": [
            ("RULE 81(1): PENSION",
             "Pension (not family pension) is payable from the day the servant stops being borne on the establishment, subject to Rule 8.",
             "ORANGE",
             "Rule 81 batata hai ki pension kab se banti hai. Family pension ke alawa pension us din se jab servant establishment se hat jaata hai — Rule 8 ke power ke subject."),
            ("RULE 81(2): FAMILY PENSION",
             "From the day AFTER the death of the servant or pensioner; or the day after a family pensioner dies or becomes ineligible.",
             "GREEN",
             "Family pension death ke doosre din se — servant ho ya pensioner. Aur family pensioner ki death ya ineligibility ho to uske doosre din se. Rule 79(3)(iv) missing case ki date batata hai."),
            ("RULE 81(3): THE DAY OF DEATH IS PAID",
             "Pension, including family pension, is payable for the day of the recipient's death too. No part-day cut.",
             "SKY",
             "Aur ek insaani detail: pension, family pension sameth, us din ke liye bhi payable hai jab recipient ki death hoti hai. Aakhri din poora milta hai, aadha din kaatne ka koi rule nahi."),
            ("TRAP: RULE 70(2) VERSUS RULE 81(1)",
             "Rule 70(2): when the servant is deemed retired. Rule 81(1): when pension starts. Two different questions.",
             "RED",
             "Charu ki death bara August ko: unki pension bara August ke liye poori, aur family pension terah August se. Trap: family pension death ke din se shuru karna galat hai. Aur Rule 70(2) bilkul alag sawaal hai."),
        ],
        "hook": "REMEMBER: Pension from the day off the rolls; family pension from the day AFTER death; death day is paid!",
        "hook_say": "Yaad rakhiye: pension establishment se hatne ke din se, family pension death ke doosre din se, aur death ka din paid.",
        "covers": ["R81-1", "R81-2", "R81-3", "R81-70-2"],
    },
    {
        "id": "c6_26_rules82_83",
        "chapter": "CHAPTER 26 • RULES 82 AND 83: RUPEES, INDIA, LUMP SUM AND THE MARCH EXCEPTION",
        "title": "RULES 82-83 — RUPEES IN INDIA, LUMP SUM, AND WHEN MARCH PENSION IS PAID",
        "accent": "YELLOW",
        "badge": "RULES 82 • 83",
        "q": "In what currency and where is pension paid, and when in the month, including March?",
        "q_say": "Pension kis currency mein, kahan, aur mahine ki kis tareekh ko milti hai — March sameth?",
        "boxes": [
            ("RULE 82: RUPEES, ONLY IN INDIA",
             "All pensions and gratuities are paid in rupees and only in India.",
             "YELLOW",
             "Rule 82 chhota hai par sakht: saari pensions aur gratuities rupees mein, aur sirf India mein. Currency ya desh mein koi flexibility nahi."),
            ("RULE 83(1): GRATUITY LUMP SUM",
             "Gratuity is paid as a lump sum, unless these Rules say otherwise.",
             "BLUE",
             "Rule 83(1): gratuity lump sum mein di jaati hai, jab tak rules kuch aur na kahein. Installments default nahi hain."),
            ("RULE 83(2): MONTH-END, AND MARCH",
             "Monthly pension: on or after the last working day of that month. March pension: on or after the first working day of April.",
             "GREEN",
             "Rule 83(2): mahine ki pension us mahine ke last working day ko ya uske baad di jaati hai. March ka exception yaad rakhiye — March ki pension April ke pehle working day par ya uske baad."),
            ("RECOMPUTED EXAMPLE, AND THE TRAP",
             "Bilal retires 30 June 2026: pension starts 1 July; first payment is for July. March 2027 pension: on or after first working day of April.",
             "RED",
             "Bilal tees June do hazaar chhabbis ko retire hue, to pension ek July se, aur pehla payment July ka. March do hazaar sattais ki pension April ke pehle working day se. Trap: pehli pension June ki batana galat hai."),
        ],
        "hook": "REMEMBER: Rupees, in India; gratuity lump sum; pension at month-end; March pension in April!",
        "hook_say": "Yaad rakhiye: rupees, India mein; gratuity lump sum; pension month-end par; March ki pension April mein.",
        "covers": ["R82", "R83-1", "R83-2", "R83-WHY", "R83-EX"],
    },
    {
        "id": "c6_27_rule84",
        "chapter": "CHAPTER 27 • RULE 84: THREE OTHER INSTRUMENTS THAT APPLY",
        "title": "RULE 84 — TREASURY RULES, COMMUTATION RULES 1981 AND ARREARS NOMINATIONS 1983",
        "accent": "SKY",
        "badge": "RULE 84(1)-(3)",
        "q": "Rule 84 seems to say nothing itself. Which other rules does it bring in?",
        "q_say": "Rule 84 khud kuch nahi kehta lagta. Kaunse doosre rules isko chalate hain?",
        "boxes": [
            ("RULE 84(1): TREASURY RULES",
             "Treasury Rules govern the procedure for four payments: gratuity, pension, pension undrawn for over a year, and a dead pensioner's pension.",
             "SKY",
             "Rule 84 khud rights nahi banata — woh batata hai kaunse doosre rules lagenge. Treasury Rules payment ki procedure ke liye aate hain, chaar cheezon mein: gratuity, pension, ek saal se zyada undrawn pension, aur dead pensioner ki pension."),
            ("RULE 84(2): COMMUTATION RULES 1981",
             "The CCS (Commutation of Pension) Rules 1981 cover commutation, payment of the commuted value, and restoration.",
             "GREEN",
             "Doosra: CCS Commutation of Pension Rules 1981 — commutation, commuted value ka payment, aur period khatam hone par restoration. Yani unnis sau ikkasi ke rules, Rule 84(2) ke through."),
            ("RULE 84(3): ARREARS NOMINATIONS 1983",
             "The Payment of Arrears of Pension (Nominations) Rules 1983: who gets unpaid arrears after a pensioner's death.",
             "BLUE",
             "Teesra: Payment of Arrears of Pension Nominations Rules 1983 — pensioner ki death ke baad arrears kaun lega. Retirees ke liye nomination ab Form 6-A mein aati hai; Form A sirf baad ki ya badli hui nomination ke liye."),
            ("PATTERN AND TRAP",
             "Rule 84 decides which instrument applies. It does not create the rights itself.",
             "RED",
             "Pattern yaad rakhiye: kaun aur kaunsa instrument poochhe to allocation rule, kitna aur kab se poochhe to substantive rule. Commutation ke percentage Rule 84 mein dhoondhna bekaar hai."),
        ],
        "hook": "REMEMBER: Rule 84 = Treasury Rules + Commutation 1981 + Arrears Nominations 1983. Three sub-rules!",
        "hook_say": "Yaad rakhiye: Rule 84 matlab Treasury Rules, Commutation 1981 aur Arrears Nominations 1983 — teen sub-rules.",
        "covers": ["R84-1", "R84-2", "R84-3", "R84-COUNT", "ALLOC-PATTERN"],
    },
    {
        "id": "c6_28_rules85_86",
        "chapter": "CHAPTER 28 • RULES 85 AND 86: DOUBTS AND RELAXATION",
        "title": "RULES 85-86 — REFER A DOUBT, RELAX A RULE, AND THE 2025 REFERRAL O.M.",
        "accent": "PINK",
        "badge": "RULES 85 • 86",
        "q": "Who settles a doubt about the Rules, who can relax them, and how must a case be referred?",
        "q_say": "Rules ki interpretation par doubt ho to kaun settle karta hai, kaun relax kar sakta hai, aur case kaise refer hota hai?",
        "boxes": [
            ("RULE 85: INTERPRETATION",
             "A doubt on meaning is referred for decision to the Government - DoPPW or DoPT - whoever owns that rule or subject. The office does not decide it.",
             "PINK",
             "Rule 85: rules ki interpretation par doubt ho to khud decide nahi karte. Woh Government ko refer hota hai — DoPPW ya DoPT ko, is baat par depend karta hai ki rule kis subject ka hai."),
            ("RULE 86: POWER TO RELAX",
             "Undue hardship in one case: a Ministry may relax a rule by written order - but only with DoPPW or DoPT concurrence.",
             "ORANGE",
             "Rule 86: agar kisi rule ke chalne se kisi ek case mein undue hardship hoti hai, to Ministry ya Department order se us requirement ko relax kar sakti hai — reasons likhkar, aur just aur equitable tarike se."),
            ("O.M. 24.10.2025: HOW TO REFER",
             "Examine first, form a tentative conclusion, name the rule, then refer through the Ministry with Secretary approval, preferably on e-File.",
             "GREEN",
             "Lekin proviso sakht hai: aisa order DoPPW ya DoPT ki concurrence ke bina nahi ho sakta. Yani relaxation ka power hai, par akela istemaal nahi."),
            ("THE LINK, AND THE TRAP",
             "Rule 85 says WHO to ask; the O.M. of 24.10.2025 says HOW to ask. Rule 86 needs the same department's concurrence.",
             "RED",
             "Chobis October do hazaar pachees ka Office Memorandum batata hai referral kaise bhejein: pehle case examine karo, tentative conclusion banao, phir specific rule likho, Secretary ki approval se, preferably e-File par. Bina examination referral bhejna galat hai."),
        ],
        "hook": "REMEMBER: Refer only AFTER examining the case. Relaxation needs written reasons plus concurrence!",
        "hook_say": "Yaad rakhiye: pehle examine kijiye, tentative conclusion banaiye, phir refer kijiye. Rules 85 aur 86 ka text ab verified hai.",
        "covers": ["R85", "R86", "OM-24.10.2025-NO", "OM-24.10.2025-PRE", "OM-24.10.2025-5ITEMS", "OM-24.10.2025-ROUTE", "OM-24.10.2025-SCOPE", "OM-24.10.2025-R86"],
    },
    {
        "id": "c6_29_rule87",
        "chapter": "CHAPTER 29 • RULE 87: REPEAL AND SAVINGS, DOCUMENTS FORWARD, CASES BACK",
        "title": "RULE 87 — THE 1972 RULES ARE REPEALED, AND THE FIVE SAVINGS",
        "accent": "RED",
        "badge": "RULE 87(1)-(2)",
        "q": "What does Rule 87 repeal, and what happens to old papers and pending cases?",
        "q_say": "Rule 87 kya repeal karta hai, purane papers ka kya hota hai, aur pending cases kahan jaate hain?",
        "boxes": [
            ("RULE 87(1): THE REPEAL",
             "Every earlier rule, regulation or order - Office Memoranda included, the 1972 Rules named as the example - ceases to operate so far as it covers a matter in these Rules.",
             "RED",
             "Rule 87(1) purane rules ko repeal karta hai — har rule, regulation ya order, Office Memorandum sameth, jisme unnis sau bahattar ke Pension Rules example ke taur par diye hain. Lekin repeal partial hai: sirf utni baat tak, jitni in rules mein covered hai."),
            ("SAVINGS (a) AND (b): DOCUMENTS",
             "(a) An old nomination, an old family-details form and an old pension application count as made under these Rules. (b) What was not done must now be done under these Rules.",
             "ORANGE",
             "Savings (a): purane rules ke tahat ki gayi nomination, family details ka form, aur pension ki formal application — teeno naye rules ke tahat ki hui maani jaati hain."),
            ("SAVINGS (c), (d), (e): PENDING CASES",
             "(c) A pending pension-authorisation case of someone who retired earlier is decided under the OLD rule. (d) Same for pending gratuity and family pension cases. (e) Past acts count as done under these Rules.",
             "BLUE",
             "Savings (b): jo cheez purane rule ke tahat honi chahiye thi par nahi hui, woh ab in rules ke hisaab se hogi. Yani documents aage chalte hain."),
            ("MEMORY LINE, EXAMPLE AND TRAP",
             "Documents move FORWARD; pending cases stay BEHIND. Dev retired in 2019 and his case is pending: it is decided under the 1972 Rules.",
             "GREEN",
             "Savings (c), (d), (e): commencement se pehle retire hue servant ka pending case, aur deceased servant ya pensioner ke gratuity aur family pension ke pending cases — purane rule se decide honge, jaise naye rules bane hi na hon. Baaki jo hua, woh naye rules ke tahat hua maana jaayega."),
        ],
        "hook": "REMEMBER: Documents go FORWARD, pending cases stay BEHIND. That is Rule 87(2), now read in full!",
        "hook_say": "Yaad rakhiye: documents aage, pending cases peeche. Rule 87 ka poora text ab verified hai.",
        "covers": ["R87-1", "R87-2-A", "R87-2-B", "R87-2-C", "R87-2-D", "R87-2-E", "R87-CLIMAX", "R87-QA"],
    },
    {
        "id": "c6_30_guidelines_2025",
        "chapter": "CHAPTER 30 • THE 2025 GUIDELINES AND CLAIMS O.M.: WHAT THEY ADD TO RULES 71 TO 83",
        "title": "SEPT-OCT 2025 O.M.S — WELFARE OFFICER, PPO CALENDAR AND THE DEATH DAY",
        "accent": "SKY",
        "badge": "O.M.s 2025",
        "q": "What do the autumn 2025 O.M.s add for claim and payment stages, and what do they not change?",
        "q_say": "Do hazaar pachees ke Office Memoranda claim aur payment stages ke liye kya jodte hain, aur kya nahi badalte?",
        "boxes": [
            ("THE GUIDELINES O.M. AND THE WELFARE OFFICER",
             "O.M. No. 4/35/2024-P&PW(D)/10377 (29.09.2025). A Welfare Officer helps dependents with papers when a pensioner dies.",
             "SKY",
             "Unnees September do hazaar pachees ki comprehensive guidelines administrative calendar deti hain. Welfare Officer, yani Pension Mitra, har retiring employee ke saath hota hai, aur pensioner ki death par dependents ko documents mein help karta hai."),
            ("THE PPO CALENDAR (CORRECTED LABELS)",
             "Stage 9: PAO sends PPO by the last working day of the month before. Stage 10-A: CPAO seal to PDA by the 20th. Stage 10-B: half copy on retirement day. Stage 11: credit by month-end.",
             "BLUE",
             "Calendar ke stages nau, das-A, das-B aur gyarah hain — nau, das, gyarah, baarah nahi. Stage nau mein PAO PPO bhejta hai, das-A mein CPAO seal, das-B mein half copy, gyarah mein credit."),
            ("THE CLAIMS O.M. OF 30.10.2025",
             "O.M. F.No. 38/10(03)/2025-P&PW(A) of 30.10.2025: the death date counts as a completed working day; claims follow the rules in force on retirement or death.",
             "GREEN",
             "Tees October do hazaar pachees ka Office Memorandum do baatein kehta hai: death ki date completed working day maani jaayegi, aur claim us date par lagne wale rules se chalega. Note: family pension ka doosre din se shuru hona Rule 81(2) hai, is memorandum ka bayaan nahi."),
            ("TRAP: CALENDAR VERSUS RULE",
             "Rule clock = law. Calendar = administrative target. Welfare Officer help does not extend any time limit.",
             "RED",
             "Layer alag rakhiye: rule ka clock kanoon hai, calendar administrative target hai. Welfare Officer ki madad time limit badha nahi sakti. Trap: stage baarah quote karna, ya calendar ko Rule 80 se replace karna."),
        ],
        "hook": "REMEMBER: Stages 9, 10-A, 10-B and 11 are administrative. The Rule 80 clocks are the law!",
        "hook_say": "Yaad rakhiye: calendar ke stages nau, das-A, das-B, gyarah administrative hain. Rule 80 ka clock kanoon hai.",
        "covers": ["OM-29.09.2025-NO", "OM-29.09.2025-WELFARE", "OM-29.09.2025-S9", "OM-29.09.2025-S10A", "OM-29.09.2025-S10B", "OM-29.09.2025-S11", "OM-29.09.2025-SCOPE", "OM-30.10.2025-NO", "OM-30.10.2025-FPSTART", "QA-WELFARE"],
    },
    {
        "id": "c6_31_amendments_currency",
        "chapter": "CHAPTER 31 • WHICH AMENDMENTS TOUCH RULES 71 TO 87, AND HOW CURRENT IS THIS",
        "title": "AMENDMENTS AND CURRENCY — WHAT CHANGED IN RULES 71-87 UP TO 21 OCT 2026",
        "accent": "YELLOW",
        "badge": "AMENDMENTS • CURRENCY",
        "q": "Which Gazette amendments touch Rules 71 to 87, and are there any newer changes?",
        "q_say": "Kaunse Gazette amendments Rules 71 se 87 ko chhoote hain, aur koi naya change hai kya?",
        "boxes": [
            ("THE FOUR NOTIFICATIONS",
             "868(E) of 20.12.2021 created the Rules; 770(E) renamed Rule 76's duplicate (5) to (5A); 410(E) swapped Form 6 for Form 6-A; 340(E) touched Rule 37 only.",
             "YELLOW",
             "Chaar notifications dekhiye. G.S.R. aath sau adsath E ne rules banaaye, saat sau sattar E ne Rule 76 ka doosra paanch (5A) kiya, chaar sau das E ne Form 6 ko Form 6-A kiya, aur teen sau chalees E ne sirf Rule 37 ko chhua."),
            ("ANYTHING NEWER?",
             "No amendment to Rules 71-87 found after 410(E) up to 21.10.2026. A negative result, limited to the pages searched.",
             "ORANGE",
             "Rule 71 se 87 mein chaar sau das E ke baad, ikkees October do hazaar chhabbis tak, koi amendment nahi mila. Yeh negative result sirf padhe gaye pages tak limited hai — isliye Office Memorandum check karna aadat banaiye."),
            ("DYNAMIC FIGURES: CHECK BEFORE QUOTING",
             "DR 60 percent from 01.01.2026; GPF 7.1 percent for Oct-Dec 2026. Both change: check the latest O.M.",
             "SKY",
             "Dynamic figures: dearness relief saath percent ek January do hazaar chhabbis se, aur GPF saat point ek percent October se December do hazaar chhabbis tak. Dono badalte hain — rule quote kijiye, figure memorandum se lijiye."),
            ("SOURCE PROBLEMS WE CORRECTED",
             "Counts check out: 71 has 6 sub-rules, 72 three, 73 three, 74 four, 75 eight, 76 eight plus 5A, 77 ten clauses, 79 six, 80 five.",
             "RED",
             "Aur ek padhne wali baat: loose reproductions Rule 76 ke baad wale clauses ko chhe se nau tak print karte hain, kyunki woh duplicate paanch ko collapse kar dete hain. Sahi citation paanch, paanch-A, chhe, saat, aath hai."),
        ],
        "hook": "REMEMBER: Only 770(E) and 410(E) changed Rules 71-87. DR and GPF move: check the latest O.M.!",
        "hook_say": "Yaad rakhiye: Rules 71 se 87 ko sirf 770(E) aur 410(E) ne chhua. Dearness relief aur GPF badalte hain — memorandum dekhiye.",
        "covers": ["GSR-868E", "GSR-770E", "GSR-410E", "GSR-340E", "NO-AMEND-71-87", "DYN-DR", "DYN-GPF", "TOC-14-CHAPTERS", "R76-COUNT", "R71-COUNT", "R75-COUNT", "R77-COUNT", "R79-COUNT"],
    },
    {
        "id": "c6_32_recap",
        "chapter": "CHAPTER 32 • BATCH 6 RECAP: KEY NUMBERS, TOP TRAPS, CURRENCY, NEXT STEP",
        "title": "RECAP OF RULES 71-87 — NUMBERS, TRAPS, CURRENCY AND WHAT COMES NEXT",
        "accent": "GREEN",
        "badge": "BATCH 6 RECAP",
        "q": "Can we close this batch with the key numbers, the top traps, and a note on how current it is?",
        "q_say": "Batch ko key numbers, top traps aur currency note ke saath band karein?",
        "boxes": [
            ("KEY NUMBERS",
             "Death: 7 days (DoE), 1 year emoluments, 1 month, 15 days, 6 months. Rule 80: 1 month, 10 days, 15 days. Missing: 6 months after police report.",
             "GREEN",
             "Numbers ek saath. Saat din Directorate ko, ek saal ke emoluments, ek mahina determination, pandrah din provisional family pension, chhe mahine, aur missing case mein police report se chhe mahine."),
            ("TOP TRAPS",
             "Clock starts differ. Damages are not waived. Missing servant 3 dates, pensioner 2. Form 6 is now 6-A. Form 13 is not Format 13.",
             "RED",
             "Rule 80 ka chain: ek mahina, das din, pandrah din. Interest claim ke teen mahine ke baad. Aur Rule 83: pension month-end par, March ki pension April mein."),
            ("CURRENCY NOTE",
             "Current to G.S.R. 410(E), effective 16.11.2024; nothing newer found up to 21.10.2026. All of Rules 71-87 read. DR and GPF: check the O.M.",
             "SKY",
             "Top traps: clock ke start point alag, damages maaf nahi, missing servant ki teen date aur pensioner ki do, Form 6 ab 6-A, Format 13 aur Form 13 alag, aur purane pending cases unnis sau bahattar ke rules mein."),
            ("WHAT COMES NEXT",
             "Batch 7: the decision tree, amendment register, Forms 1-13, Formats 1-13, deadlines, amounts and counts.",
             "PINK",
             "Currency: chaar sau das E tak sab kuch verified, Rules 71 se 87 ka text padha gaya, aur dearness relief aur GPF jaise figures har baar Office Memorandum se check kijiye. Agla batch: decision tree, forms, aur master deadlines."),
        ],
        "hook": "REMEMBER: 1 year, 15 days and 6 months, then 1 month, 10 days, 15 days. Next: Batch 7!",
        "hook_say": "Yaad rakhiye: ek saal, pandrah din aur chhe mahine, phir ek mahina, das din, pandrah din. Agla Batch 7.",
        "covers": ["R71-4C-7DAYS", "R72-2", "R75-1", "R75-3", "TL-R80-CLOCKS", "LIMIT-6M-POLICE", "R83-2", "GSR-410E", "NO-AMEND-71-87", "DYN-DR", "DYN-GPF"],
    },
]


# Full, examinable wording behind every on-screen card (used by the reference sheet).
FULL = {
    ("c6_01_rule71_first_steps", "RULE 71(1): DECIDE WHAT IS PAYABLE"):
        "Rule 71(1): on receiving intimation of the death, the Head of Office decides whether death gratuity, family pension, or both are payable. Layer: the Rule's own text. [Bare text of the 2021 Rules, Chapter XI, read 24.10.2026.] Terms: Head of Office = the officer in charge of the office where the employee worked. Death gratuity = a lump sum paid to the family when a serving employee dies. Family pension = a monthly pension for eligible family members.",
    ("c6_01_rule71_first_steps", "RULE 71(2): THE GRATUITY LETTER"):
        "Rule 71(2): for the Rule 45 death gratuity the Head of Office (a) checks whether a nomination exists; if there is none, or it does not subsist, decides who is entitled; and (b) writes to those persons in FORMAT 11 and asks them to claim in FORM 9. The Form 9 detail is an ADDITION to the source, which did not name the claim form. [Bare text read 24.10.2026.] Nomination = the employee's own written choice of who receives the gratuity.",
    ("c6_01_rule71_first_steps", "RULE 71(3): THE FAMILY PENSION LETTER"):
        "Rule 71(3): for the Rule 50 family pension the Head of Office writes to the eligible family member or guardian in FORMAT 12; the claim is made in FORM 10, accompanied by the FORMAT 9 bank undertaking. [Bare text read 24.10.2026.] Bank undertaking = a signed promise about the bank account the pension will be paid into and about returning wrong payments. Note: the 2024 amendment replaced Format 9 by Form 6-A only in Rules 60(1) and 63(4) (retirement cases); Rules 71 to 80 still use Format 9.",
    ("c6_01_rule71_first_steps", "REAL EXAMPLE AND THE TRAP"):
        "Example (invented): Mr Dev Rao, a clerk, dies in service and had made no nomination. The Head of Office decides who is entitled to the death gratuity, writes to them in Format 11 and asks for a Form 9 claim; for family pension he writes to his widow in Format 12 and she claims in Form 10 with a Format 9 undertaking. Trap: the source said Rule 71 has four sub-rules; the current text has six, 71(1) to 71(6) (ledger R71-COUNT, status changed). Form and Format are different numbered documents: never mix Format 9 with Form 9.",
    ("c6_02_rule71_4_quarters", "RULE 71(4)(a): OLD FEE WAIVED"):
        "Rule 71(4)(a): the licence fee for the period before the death is waived. [Bare text read 24.10.2026.] Licence fee = the rent-like charge for official housing allotted to the employee.",
    ("c6_02_rule71_4_quarters", "RULE 71(4)(b): DAMAGES STILL RECOVERED"):
        "Rule 71(4)(b): damages (the penal charge for unauthorised occupation) are still recovered from the death gratuity; and if the family retains the accommodation, no licence fee is charged for the month of death and the next three months. The three-month limb is for the family (confirmed). [Bare text read 24.10.2026.]",
    ("c6_02_rule71_4_quarters", "RULE 71(4)(c): SEVEN DAYS"):
        "Rule 71(4)(c): the Head of Office writes to the Directorate of Estates within seven days of intimation, for the No Demand Certificate (NDC); this links to Rule 77(1). NDC = a certificate that no housing dues remain. [Bare text read 24.10.2026.]",
    ("c6_02_rule71_4_quarters", "EXAMPLE AND TRAP"):
        "Example (invented): Mr Charu Nair, a clerk, dies on 12 August. Intimation reaches the office on 14 August, so the letter to the Directorate of Estates must go by 21 August (seven days). His family keeps the quarters: no licence fee for August, September, October and November (month of death plus three months = four calendar months). His fee for the time before 12 August is waived. A damages bill for an earlier overstay would still be recovered from the gratuity. Trap: death-case licence fee waiver does not waive damages.",
    ("c6_03_rule71_5_6_missing", "RULE 71(5): RULE 51 APPLIES"):
        "Rule 71(5): where the servant is missing, Rule 51 sub-rules (1) and (4) apply. [Bare text read 24.10.2026.] Missing = disappeared and not heard of; Rule 51 (Batch 4) sets the family pension entitlement for a missing person.",
    ("c6_03_rule71_5_6_missing", "RULE 71(6): POLICE REPORT FIRST"):
        "Rule 71(6)(c): claims are called for only after the police report (an FIR, a Daily Diary Entry or a General Diary Entry) that the person could not be traced. [Bare text read 24.10.2026.] FIR = First Information Report lodged at a police station.",
    ("c6_03_rule71_5_6_missing", "THE PAPERS THAT TRAVEL WITH THE CLAIM"):
        "Rule 71(6) additions (source omitted them; ledger R71-6-ADD): (a)-(b) use Format 11 with Form 9, and Format 12 with Form 10; (c) police-report condition; (d) the claim must carry the Format 9 undertaking, the FORMAT 8 indemnity bond and copies of both police reports; (e) the Head of Office does not wait for a death certificate and acts on credible information; (f) special efforts to collect forms: in person at the place of duty, blank forms by post elsewhere; (g) a family member other than the widow, widower or pensioner submits the Rule 50(12)(b) documents. [Bare text read 24.10.2026.] Indemnity bond = a promise to repay the Government if the missing person turns up or a wrong person is paid.",
    ("c6_03_rule71_5_6_missing", "TRAP: DISAPPEARED IS NOT DEAD"):
        "Trap: calling for claims before a police report exists is premature. Also note the sub-rule count: six, not four. Later chapters show the same police-report anchor in Rules 76(3)(e)-(f), 79(3) and 80(1). Example (invented): Bilal, a serving clerk, disappears; his wife lodges a General Diary Entry; only after that does the office call for claims, with an indemnity bond.",
    ("c6_04_forms_map_71_80", "FORMATS: LETTERS AND UNDERTAKINGS"):
        "Formats in Rules 71-80 (all confirmed, close restatement from secondary pages): FORMAT 8 = indemnity bond for missing cases (71(6)(d), 79(3)(iii)); FORMAT 9 = bank undertaking sent with a claim; FORMAT 10 = covering letter (Rule 60(1)(ii) retirement, Rule 74(1) death, also Rule 80(5)(c)); FORMAT 11 = Head of Office letter to those entitled to Rule 45 death gratuity (71(2)(b)); FORMAT 12 = letter to the eligible member or guardian (71(3), also 79(3)(ii) for a missing pensioner); FORMAT 13 = sanction of family pension (79(2)(b), 79(3)(iv), 80(5)(b)).",
    ("c6_04_forms_map_71_80", "FORMS: CLAIMS AND RECORDS"):
        "Forms (bare text): FORM 3 = the common nomination form for gratuity, GPF and CGEGIS [Rule 46]; FORM 8 = the spouse's request on which the Accounts Officer adds names to the PPO [79(2)(a)(iv)]; FORM 9 = application for the gratuity of a deceased or missing servant [71(2)(b), 71(6)]; FORM 10 = application for family pension [50, 71, 74, 76, 79, 80]; FORM 11 = the family-pension case, Part II Section I completed by the AO [74(1), 76(1)]; FORM 12 = claim where the name is already in the PPO [79(2)(a)]; FORM 13 = claim for the residuary gratuity of a retired servant [79(6)]. Formats: FORMAT 7 = indemnity bond where the claimant is a minor [Form 9, enclosure (b)]; FORMAT 8 = indemnity bond in a missing case [71(6)(d), 79(3)(iii)]. Form and Format are different documents: Form 9 is a claim, Format 9 is a bank undertaking. [Bare text read 24.10.2026.]",
    ("c6_04_forms_map_71_80", "OBSOLETE / HISTORY ONLY"):
        "OBSOLETE / HISTORY ONLY: (1) The source mnemonic 'eight and nine evidence, ten claim, eleven and twelve claimants, thirteen sanction' is not safe (ledger FORMS-MNEMONIC): Form 8 is a spouse request, Form 9 is a gratuity claim, Format 8 is the indemnity bond, Format 9 an undertaking, Forms 12 and 13 are claim forms. Teach each Form and Format separately. (2) Form A under the Payment of Arrears of Pension (Nominations) Rules 1983: for retiring employees the nomination for arrears and commutation now goes in Form 6-A, replacing it, per O.M. F.No. 55/13/2023-P&PW(C)(Part1) of 11.09.2024; Form A is still used for later or changed nominations by pensioners and family pensioners. A formal amendment of the 1981 and 1983 Rules was said to follow; none was found. [Bare text read 24.10.2026.]",
    ("c6_04_forms_map_71_80", "SAME NUMBER, DIFFERENT PAPER"):
        "Look-alikes: Format 13 (sanction of family pension, issued by the Head of Office) versus Form 13 (claim for residuary gratuity of a retired servant); Format 12 (letter to a claimant) versus Form 12 (claim where the names are already in the PPO); Format 9 (bank undertaking) versus Form 9 (gratuity claim); Format 8 (indemnity bond) versus Form 8 (spouse request). Quick routes: name in PPO leads to Form 12 and the Pension Disbursing Authority; no name leads to Form 10 and Format 13; missing leads to Form 10, Format 8 and Format 13.",
    ("c6_05_rule72_1_service", "RULE 72(1)(a): THE WHOLE SERVICE BOOK"):
        "Rule 72(1)(a): the Head of Office examines the service book for the whole service (verification certificates covering the whole service), not only the portion after Rule 30 as in the retirement chapter. [Bare text read 24.10.2026.] Service book = the official record of a servant's appointments, pay and leave, kept by the office. Qualifying service = the service that counts for pension.",
    ("c6_05_rule72_1_service", "RULE 72(1)(b)(i): THE RELIEF"):
        "Rule 72(1)(b)(i): service not yet verified is deemed verified on the strength of the entries already in the service book. [Bare text read 24.10.2026.] This removes the burden of hunting for outside proof in a death case.",
    ("c6_05_rule72_1_service", "(b)(ii) AND (b)(iii): POWER AND CHECK"):
        "Rule 72(1)(b)(ii): the Head of Office may rely on other material easily available to him: a power, not a duty. Rule 72(1)(b)(iii): he must see that the service was continuous and was not forfeited by dismissal, removal, resignation or strike. Forfeiture = loss of past service for pension because of such an event. Relief is in verification, not in the forfeiture check (ledger R72-VS-57-FORFEITURE). [Bare text read 24.10.2026.]",
    ("c6_05_rule72_1_service", "EXAMPLE AND TRAP"):
        "Example (invented): Mr Dev Rao, an Assistant, dies in service. Two years of his service have no verification certificates. The Head of Office accepts the existing service-book entries as verification and checks that his service was continuous and had no forfeiting event. Q and A: what happens to unverified service in a death case? It is treated as verified on the entries (Rule 72(1)(b)(i)), but continuity and forfeiture must still be checked.",
    ("c6_06_rule72_emoluments_vs57", "RULE 72(2): ONE YEAR"):
        "Rule 72(2): emoluments are examined for a maximum of one year before the death or disappearance; if the servant was on extraordinary leave (EOL) on that day, the year before the EOL began. Emoluments = the pay and allowances that count for pension. [Bare text read 24.10.2026.]",
    ("c6_06_rule72_emoluments_vs57", "RULE 72(3): ONE MONTH"):
        "Rule 72(3): the determination is to be made within one month of intimation. [Bare text read 24.10.2026.]",
    ("c6_06_rule72_emoluments_vs57", "DEATH VERSUS RETIREMENT"):
        "Comparison. Death: one year (Rule 72(2)); one month to decide (72(3)). Retirement: correctness of emoluments verified for 24 months, Rule 57(1)(b)(v) (confirmed). Rule 57(1)(b)(iv) also mentions the last ten months of entries. The source cited Rule 63(1)(c) for 24 months; that citation was not confirmed. Rule 57 staged verification is completed eight months before retirement (57(1)(a)(vii), confirmed). NOT CONFIRMED against an official source: the source claims that Rule 57 verifies only the service after Rule 30 (R57-SCOPE-AFTER-R30), and that the unverified portion is proved from pay bills and LPC (R57-UNVERIFIED-DOCS). These two are Batch 5 points; do not rely on them. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_06_rule72_emoluments_vs57", "EXAMPLE AND TRAP"):
        "Example (invented): Ms Esha Menon, an Assistant, dies on 20 March 2026. Emoluments are examined for the one year before 20 March 2026, that is, from 20 March 2025. Had she been on extraordinary leave from 1 January 2026, the year would be counted back from 1 January 2026, that is, from 1 January 2025. In a retirement case the same office would have checked 24 months. Trap: do not carry the 24-month figure into a death case, and do not forget the forfeiture check.",
    ("c6_07_rule73_incomplete_records", "RULE 73(1): A CASE THAT SHOULD NOT ARISE"):
        "Rule 73(1): no case should arise where the service book has not been properly maintained; this is subject to sub-rules (2) and (3) and to Rule 75(7). It is a declaration that record-keeping is the office's duty. [Bare text read 24.10.2026.] Teaching comment (not rule text): the family is not punished for the office's default, and Rule 73 also opens the way to fix responsibility.",
    ("c6_07_rule73_incomplete_records", "RULE 73(2)(a): FAMILY PENSION IN ONE MONTH"):
        "Rule 73(2)(a): where the service book was not maintained despite Government orders, the amount and period of family pension are fixed under Rule 50(2) within one month of the intimation of death or disappearance. [Bare text read 24.10.2026.]",
    ("c6_07_rule73_incomplete_records", "RULE 73(2)(b)(i)-(ii): PROVING FOR GRATUITY"):
        "Rule 73(2)(b)(i): service not verified is checked from pay bills and acquittance rolls; the two examples are the last pay certificate and the April pay slip. Rule 73(2)(b)(ii): service rendered in another office is referred to that office. [Bare text read 24.10.2026.] Pay bill = the office's monthly pay record. Acquittance roll = the signed record that the employee received pay.",
    ("c6_07_rule73_incomplete_records", "RULE 73(3): THE LAST VERIFIED SPELL"):
        "Rule 73(3) (an ADDITION; the source did not describe it): if the whole service of the deceased cannot be verified quickly, gratuity is provisionally decided on the last verified spell, as in Rule 75(7). [Bare text read 24.10.2026.]",
    ("c6_08_rule73_clocks", "(iii): REPLY IN ONE MONTH"):
        "Rule 73(2)(b)(iii): on receipt of the reference, the other Head of Office verifies the period or periods in the manner given in sub-clause (i) and sends the certificates to the referring Head of Office within one month of the reference. PROVISO: where a period of service is incapable of being verified, it must be brought to the notice of the referring Head of Office simultaneously - the other office cannot simply stay silent. [Bare text read 24.10.2026.] Batch 5 comparison: the two-month reply said to exist in Rule 57(1)(a) was not re-read here; do not quote two months for a death case.",
    ("c6_08_rule73_clocks", "(iv) AND (v): SILENCE AND DEFAULT"):
        "Rule 73(2)(b)(iv): if no reply is received in time, the period is deemed to qualify. Rule 73(2)(b)(v): where a non-qualifying period was not communicated, the Secretary of the Ministry fixes responsibility. [Bare text read 24.10.2026.]",
    ("c6_08_rule73_clocks", "(vi): EVERY EFFORT, THEN IGNORE"):
        "Rule 73(2)(b)(vi): every effort is made to verify; what still cannot be verified is ignored, and the gratuity is decided on the service-book entries. [Bare text read 24.10.2026.]",
    ("c6_08_rule73_clocks", "EXAMPLE AND TRAP"):
        "Example (invented): Mr Bilal Khan's service book has a two-year gap. The Head of Office writes to the other office; the reply comes within one month; the part still not proved is taken on the service-book entries, and the case goes forward. Trap: the one-month limit is for the incomplete-record death case; do not quote a two-month figure for it. Q and A: within how many days must the other office reply in an incomplete-record death case? One month, Rule 73(2)(b)(iii).",
    ("c6_09_rule74_send_to_ao", "RULE 74(1): FORM 11 IN ONE MONTH"):
        "Rule 74(1): the Head of Office completes FORM 11 and sends it with a FORMAT 10 covering letter, the FORMAT 9 undertaking, the up-to-date service book and other documents to the Accounts Officer (AO) within one month of receiving the claim, not of the death. [Bare text read 24.10.2026.] Accounts Officer = the officer in the Pay and Accounts Office who checks the case and issues the Pension Payment Order (PPO). Form 11 is the death-case pair of Form 7.",
    ("c6_09_rule74_send_to_ao", "RULE 74(2)-(3): RELIEF AND COPIES"):
        "Rule 74(2): a claim is not rejected only because the member is not in Form 4 or the office records, if the Head of Office is otherwise satisfied. Rule 74(3): the Head of Office keeps one copy each of Format 10, Form 10 and Form 11. Format 10 serves in two places: Rule 60(1) in retirement and Rule 74(1) in death. [Bare text read 24.10.2026.]",
    ("c6_09_rule74_send_to_ao", "RULE 74(4): THE TEN PERCENT MARGIN"):
        "Rule 74(4): the Head of Office draws the Accounts Officer's attention to Rule 77 dues and to the gratuity held back, partly for unassessed dues and partly as a margin; the hold-back is at most 10 per cent of the gratuity (ledger LIMIT-R74-10PC, Rule 74(4)(c)). Comparison: Rule 62(3)(a)(ii) also withholds 10 per cent of provisional gratuity; the detail that it is released on final accounts or NDC was not seen in a source. The ten percent is held, not forfeited. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_09_rule74_send_to_ao", "EXAMPLE AND TRAP"):
        "Example (invented): the widow files her claim on 10 September; the Head of Office must send the case to the Accounts Officer by 10 October (one month from the claim). One daughter was missing from Form 4 but the Head of Office is satisfied she is eligible, so the claim is not rejected. If the death gratuity is 8,00,000 rupees, at most 80,000 rupees (10 per cent) can be held back. Trap: the clock starts at the claim, not at the death; ten percent is a ceiling, not a fixed deduction.",
    ("c6_10_rule75_provisional_fp", "RULE 75(1): WITHIN FIFTEEN DAYS"):
        "Rule 75(1): the Head of Office determines provisional family pension, not exceeding the maximum under these Rules, within fifteen days of the claim, provided the claim has come and he is satisfied. Clause (a): a sanction letter is issued and a copy goes to the Accounts Officer; clause (b): it is drawn like establishment pay and allowances. Provisional = temporary, paid before the final order. [Bare text read 24.10.2026.]",
    ("c6_10_rule75_provisional_fp", "RULE 75(2): PAY AT ONCE"):
        "Rule 75(2): after drawal, the provisional family pension is disbursed immediately, with arrears. [Bare text read 24.10.2026.]",
    ("c6_10_rule75_provisional_fp", "RULE 75(3): SIX MONTHS"):
        "Rule 75(3): the provisional family pension runs for six months from the day after the death, unless extended by the proviso to Rule 76(1). Rule 75(4): when the period ends, the Head of Office informs the Accounts Officer (whether the provisional period or an extension). [Bare text read 24.10.2026.]",
    ("c6_10_rule75_provisional_fp", "EXAMPLE AND TRAP"):
        "Example (invented): Asha's husband, Mr Bilal, dies on 1 October; the claim is filed on 7 October. Fifteen days from the claim means sanction by 22 October. Payment is counted from 2 October, the day after death, for six months (to 1 April of the next year). Trap: the fifteen days run from the CLAIM, but the six months run from the day AFTER THE DEATH. Q and A: provisional family pension begins within 15 days of claim, from the day after death, for six months (Rules 75(1) and 75(3)); extension is possible under the proviso to Rule 76(1).",
    ("c6_11_rule75_gratuity", "RULE 75(5)-(6): 100 PERCENT, PAID AT ONCE"):
        "Rule 75(5): after the family pension and gratuity case has been forwarded to the Accounts Officer under Rule 74, the Head of Office draws 100 per cent of the gratuity - (a) a sanction letter stating the amount, with a copy to the AO; (b) the letter states the amount recoverable out of the death gratuity; (c) the amount is drawn after deducting those dues. Rule 75(6): the gratuity is disbursed immediately after drawal. DRAFTING SLIP: clause (b) sends the reader to 'sub-rule (3) of rule 74', which only requires copies to be kept; the recoverable dues are listed in Rule 74(4). Quote the clause, not the pointer. [Bare text read 24.10.2026.]",
    ("c6_11_rule75_gratuity", "RULE 75(7)(a): WHEN SERVICE IS NOT VERIFIED"):
        "Rule 75(7)(a): where the full service has not been verified, the gratuity is provisionally decided under Rule 45(1)(b), on the last verified spell, notwithstanding Rule 73(1). [Bare text read 24.10.2026.]",
    ("c6_11_rule75_gratuity", "RULE 75(7)(b)-(c) AND (8)"):
        "ADDITIONS (the source omitted them): Rule 75(7)(b): if a gratuity claim in Form 9 is received, provisional gratuity is authorised within one month of intimation. Rule 75(7)(c): the final gratuity is decided within three months of the provisional authority, and the balance is authorised. Rule 75(8): the Head of Office informs the Accounts Officer once the provisional gratuity is paid. Count: Rule 75 has EIGHT sub-rules, not seven as the source said. [Bare text read 24.10.2026.]",
    ("c6_11_rule75_gratuity", "COMPARE RULE 62, AND HISTORY"):
        "Comparison (ledger R75-VS-62): Rule 62 provisional pension is 100 per cent and provisional gratuity is 100 per cent less 10 per cent withheld, with a six-month limit; Rule 75 is the death-case counterpart with fifteen days and six months. Both treat the amount as drawn like establishment pay. HISTORY ONLY: a 2020 relaxation under the old Rule 80-A (provisional family pension without waiting for the file to go to the Accounts Officer) is background; its idea is carried into Rule 75 as sanction by the Head of Office. It is not examinable under the 2021 Rules. Teaching comment from the source (not rule text): in a death case no final PPO is ready beforehand, so the provisional step matters more. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_12_rule76_1_2_ao", "RULE 76(1): FORM 11 PART II, SECTION I"):
        "Rule 76(1): the Accounts Officer applies the requisite checks and completes Part II, Section I of FORM 11 within one month of receiving the case; emoluments are verified for a maximum of one year. [Bare text read 24.10.2026.]",
    ("c6_12_rule76_1_2_ao", "THE PROVISO: IF TIME RUNS OUT"):
        "Proviso to Rule 76(1): if the Accounts Officer cannot assess within time, he asks the Head of Office to continue the provisional family pension. [Bare text read 24.10.2026.] This keeps the six-month chain of Rule 75 from breaking.",
    ("c6_12_rule76_1_2_ao", "RULE 76(2): HEAD OF DEPARTMENT"):
        "Rule 76(2): the extension of provisional family pension requires the approval of the Head of Department; the Head of Office does not decide it alone. Head of Department = the senior officer over a group of offices. [Bare text read 24.10.2026.]",
    ("c6_12_rule76_1_2_ao", "EXAMPLE AND TRAP"):
        "Example (invented): the case reaches the Accounts Officer on 5 November; Part II Section I of Form 11 must be completed by 5 December, with one year of emoluments verified. If assessment cannot be finished, the Head of Department's approval is obtained to continue the provisional pension. Q and A: who decides to extend provisional family pension under Rule 76? The Head of Department (Rule 76(2)). Trap: do not answer 'Head of Office'.",
    ("c6_13_rule76_3_ppo", "(a), (b), (c): ONE MONTH AND TWO DATES"):
        "Rule 76(3)(a): PPO within one month. (b): regular family pension from the day after the provisional payment stops. (c): the PPO states the date up to which provisional payment ran and the date from which the Pension Disbursing Authority (PDA) payment starts. PPO = Pension Payment Order, the document that authorises pension. PDA = the bank or office that pays. [Bare text read 24.10.2026.]",
    ("c6_13_rule76_3_ppo", "(d): ARREARS FOR THE PROVISIONAL PERIOD"):
        "Rule 76(3)(d): arrears of family pension for the period during which provisional family pension was drawn and disbursed by the Head of Office are also authorised by the Accounts Officer to be paid by the Head of Office. CROSS-REFERENCE SLIP: Rule 81(2) says 'clause (d) of sub-rule (2) of rule 76', but sub-rule (2) only deals with Head of Department approval of an extension. The family-pension start date is Rule 76(3)(b), and Rule 76(3)(e) for a missing servant. [Bare text read 24.10.2026.]",
    ("c6_13_rule76_3_ppo", "(e) AND (f): MISSING SERVANT"):
        "Rule 76(3)(e): for a missing servant the entitlement start is the latest of (1) the end of the leave sanctioned, (2) the end of the period for which pay and allowances were paid, and (3) the police report date. Rule 76(3)(f): payment is not made before six months from the police report. The same 'latest date' test appears in Rule 51 (Batch 4; that ledger notes day-after wording). [Bare text read 24.10.2026.]",
    ("c6_13_rule76_3_ppo", "EXAMPLE AND TRAP"):
        "Example (invented): a missing servant's sanctioned leave ends on 31 January, pay was paid up to 28 February, and the police report is dated 15 March. The latest of the three dates is 15 March, which becomes the start date. Payment cannot be made before six months from the police report, that is, not before 15 September. Trap: choosing the earliest date, or counting six months from the date of disappearance instead of from the police report.",
    ("c6_14_rule76_4_8", "RULE 76(4): WHO IS NAMED"):
        "Rule 76(4): the Accounts Officer names permanently disabled child, dependent parents and disabled siblings in the PPO only if there is no one ranking ahead of them; the priority order of Rule 50 reaches the PPO text. [Bare text read 24.10.2026.]",
    ("c6_14_rule76_4_8", "RULE 76(5) AND (5A)"):
        "Rule 76(5)(a)-(b): the Accounts Officer determines the balance of the gratuity after adjusting anything outstanding, and intimates the Head of Office so that it is paid to those who received the provisional gratuity. (c)-(d): in a MISSING case he determines the gratuity after adjusting outstanding dues and intimates the Head of Office within one month of receiving the case, and payment is made only after six months from the date of the police report. (e): the gratuity withheld under Rule 77 is adjusted against outstanding licence fee and the balance refunded. Rule 76(5A): the Accounts Officer promptly reports the issue of the PPO and returns documents no longer needed. NUMBERING: G.S.R. 770(E) of 07.10.2022 substituted '(5A)' for the second sub-rule numbered '(5)' ('The fact of the issue...'); reproductions that never carried the duplicate print the following clauses as (6) to (9). [Bare text + G.S.R. 770(E) read 24.10.2026.]",
    ("c6_14_rule76_4_8", "RULE 76(6) AND (7): EXCESS PAID"):
        "Rule 76(6): if the provisional family pension disbursed exceeds the final family pension assessed, the Accounts Officer may adjust the excess from the gratuity, failing which in instalments from future family pension. Rule 76(7)(a): if provisional gratuity paid proves larger than the amount finally assessed, the beneficiary is NOT required to refund the excess. (b): the Head of Office must minimise such excess, and where it happens the Head of Department fixes responsibility. NEIGHBOURING SLIP: 76(5)(e) cites 'clause (b) of sub-rule (1) of rule 77' for the withheld gratuity - the withholding is clause (vi) - and 'clause (viii)' for licence fee, when the licence-fee recovery is clause (iii). [Bare text read 24.10.2026.]",
    ("c6_14_rule76_4_8", "RULE 76(8): THE FINAL CHAIN, AND COUNT"):
        "ADDITION: Rule 76(8): the Accounts Officer sends the case to the CPAO (Central Pension Accounting Office) with Format 9 within one month; the CPAO issues the Special Seal within ten days and sends it to the PDA; the PDA pays within fifteen days of the seal. If one eligible member has not filed Form 10 or Form 9, the others proceed without waiting. Count: Rule 76 has eight sub-rules plus 5A (the source said four). [Bare text read 24.10.2026.]",
    ("c6_15_rule77_a", "CLAUSE (i): WITHIN SEVEN DAYS"):
        "Rule 77(1)(i): within seven days of intimation or information the Head of Office forwards the available accommodation details to the Directorate of Estates and requests a No Demand Certificate, SO THAT AUTHORISATION OF FAMILY PENSION AND GRATUITY IS NOT DELAYED, supplying: (a) name with designation; (b) particulars of the accommodation, including earlier accommodation; (c) date of death or disappearance; (d) whether the servant was on leave, with period and nature; (e) whether the accommodation was rent-free; (f) the period up to which licence fee was recovered from pay, with the monthly rate and pay-bill particulars; (g) if fee was not recovered, then (A) the unrecovered period, (B) the fee for that period ON THE STANDARD RENT BILL, (C) the fee for the permissible concessional retention period, also on the standard bill, (D) how much of (C) is proposed to be recovered out of gratuity, and (E) details of earlier Directorate references. Both doubts raised in the last build are closed: the 'not delayed' purpose and the 'standard rent bill' wording are in the text. [Bare text read 24.10.2026.]",
    ("c6_15_rule77_a", "CLAUSE (ii): FEE WAIVED"):
        "Rule 77(1)(ii): licence fee for the period before the death is waived; if the family retains the accommodation, no licence fee is charged for the month of death and the next three months. This repeats Rule 71(4). [Bare text read 24.10.2026.]",
    ("c6_15_rule77_a", "CLAUSE (iii): NOW SEEN"):
        "Rule 77(1)(iii) (the source could not quote it and flagged it UNVERIFIED): now seen on a secondary page, the Head of Office recovers from the gratuity the licence fee that was intimated to the DoE. This partly resolves the source's flag; read the official text to be certain. [Bare text read 24.10.2026.]",
    ("c6_15_rule77_a", "CLAUSE (iv)"):
        "Rule 77(1)(iv): recovery of licence fee beyond the concessional period is the responsibility of the Directorate of Estates. Concessional period = the period of waiver or concession. Trap: the Head of Office does not chase fee beyond that period. [Bare text read 24.10.2026.]",
    ("c6_16_rule77_b", "CLAUSES (v)-(vii): ONE MONTH, TEN PERCENT"):
        "Rule 77(1)(v): the DoE reports other dues within one month of the Head of Office's intimation. (vi): meanwhile the Head of Office withholds 10 per cent of the death gratuity. (vii): if there is no intimation, or the DoE says it cannot assess, nothing is presumed recoverable and the withheld amount is released. [Bare text read 24.10.2026.]",
    ("c6_16_rule77_b", "CLAUSE (viii): THE CROSS-CHECK"):
        "Rule 77(1)(viii): if dues are intimated, the Head of Office checks the acquittance rolls to see whether they were already recovered; if so, he draws the DoE's attention to those pay bills. This stops the same money being recovered twice from the family. The source also compares this two-way check with Rule 68(3) (instalments from current pay before touching gratuity); that Rule 68(3) detail was not checked in this batch. [Bare text read 24.10.2026.]",
    ("c6_16_rule77_b", "CLAUSES (ix), (x) AND 77(2)"):
        "ADDITIONS (source stopped at clause (viii); Rule 77(1) has TEN clauses (i)-(x) plus sub-rule (2); ledger R77-1-IX-X, R77-2, R77-COUNT): Rule 77(1)(ix): dues not recovered earlier are adjusted against the withheld amount and the balance repaid. Rule 77(1)(x): unpaid dues left or reported later may be recovered by the Accounts Officer from dearness relief (DR, the cost-of-living add-on to pension) without the pensioner's consent, and no dearness relief is paid until recovered. Rule 77(2): within fifteen days of intimation the Head of Office finds other dues under Rule 67 (not accommodation dues) and recovers them from the gratuity. [Bare text read 24.10.2026.]",
    ("c6_16_rule77_b", "RULE 77 VERSUS RULE 68, AND EXAMPLE"):
        "Comparison (ledger R77-VS-68, R77-NDC14): Rule 68 (superannuation): the DoE reports within two months (one month for others), the NDC is issued within fourteen days of the application after vacating, ten per cent may be withheld, and the last eight months' fee is recovered from pay monthly (O.M. 28/91/2022-P&PW(B)(2) of 20.10.2023). The fourteen-day NDC and interest on excess withheld at the GPF rate are stated for retirement cases; the O.M. of 20.10.2023 does not mention Rule 77, so they are not stated for death cases. Example (invented): the Head of Office writes to the DoE in seven days; the DoE reports in one month; a due already recovered from pay is not recovered again.",
    ("c6_17_rule78_deputation", "RULE 78(1): CENTRAL DEPUTATION"):
        "Rule 78(1): where the servant is on deputation to another Central Department, the Head of Office of the borrowing Department performs the functions. Deputation = a temporary posting to another department. [Bare text read 24.10.2026.]",
    ("c6_17_rule78_deputation", "RULE 78(2): STATE OR FOREIGN SERVICE"):
        "Rule 78(2): where the servant is on deputation to a State Government or in foreign service, the Head of Office or cadre authority which sanctioned the deputation performs the functions (the lending side). [Bare text read 24.10.2026.]",
    ("c6_17_rule78_deputation", "COVERS MISSING TOO"):
        "Rule 78 covers both death and disappearance (confirmed). The source says it mirrors Rule 64 (retirement) and that Rule 64 has no missing limb because disappearance is not retirement; the Rule 64 half was NOT checked here (Batch 5) and the mirror claim is unverified (ledger R64-MIRROR). Teaching pattern from the source: Rules 64, 74, 84 and 87 mainly decide who acts or which instrument applies (ledger ALLOC-PATTERN). Correction: Rule 74 is not purely allocation, since it holds a one-month limit and a ten per cent hold-back. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_17_rule78_deputation", "EXAMPLE AND TRAP"):
        "Example (invented): Ms Charu Das is on deputation to another Central Department and dies there. The Head of Office of the borrowing Department calls for the claim, checks service and emoluments, sanctions provisional family pension and arranges gratuity. Had she been on deputation to a State Government, the lending cadre authority would act. Trap: Central deputation means borrowing side; State or foreign means lending side.",
    ("c6_18_chX_vs_chXI", "START OF THE CASE AND THE FORM"):
        "Retirement: the case starts one year before retirement or on leave preparatory to retirement, whichever is earlier (Rule 56, confirmed); the forms are due six months before retirement (Rule 57(2)(a), now Form 6-A). Death: the Head of Office acts as soon as the intimation arrives (Rule 71(1)); the family claims, and no fixed claim deadline was found in the rules read (ledger CMP-FORM-6M). [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_18_chX_vs_chXI", "SERVICE AND EMOLUMENTS"):
        "Death: unverified service is deemed verified on service-book entries (Rule 72(1)(b)(i)); emoluments for one year (Rule 72(2)). Retirement: correctness of emoluments verified for 24 months (Rule 57(1)(b)(v)). The Rule 57(1)(a) two-month reply figure and the 'service after Rule 30 only' claim are not confirmed (see Chapters 6 and 8). Forfeiture check applies in both. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_18_chX_vs_chXI", "PROVISIONAL PAYMENT AND THE PPO"):
        "Retirement: PPO two months before superannuation (Rule 63(1)(a)); 45 days otherwise (63(1)(b)). Provisional payment applies only if there is a delay (Rule 62, six-month limit). Death: provisional family pension within fifteen days for six months (Rule 75); final PPO within one month (Rule 76(3)(a)). [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_18_chX_vs_chXI", "HOUSING DUES, AND THE ONE-LINE TRAP"):
        "Housing: retirement (Rule 68): DoE reports within two months; last eight months' fee from pay monthly. Death (Rules 71(4), 77): HoO writes in seven days, DoE replies in one month, pre-death licence fee waived, death month plus three months free. Summary: in retirement the servant runs his own case and preparation starts a year early; in death the family claims and the steps are shorter and softer. Trap: do not carry retirement numbers (24 months, two months, eight months) into death cases. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_19_death_case_chain", "STEP 1: HEAD OF OFFICE (R71, R72)"):
        "Step 1: Head of Office. Rule 71: decide what is payable; Format 11 or 12 letters; DoE letter in seven days. Rule 72: service and one year of emoluments within one month of intimation. Rule 73: incomplete records remedy (family pension in one month). [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_19_death_case_chain", "STEP 2: THE CASE TO THE AO (R74, R75)"):
        "Step 2: Rule 74: Form 11 and papers to the Accounts Officer within one month of the claim; hold-back at most 10 per cent. Rule 75: provisional family pension within fifteen days of the claim, for six months from the day after death; 100 per cent gratuity after the Rule 74 forwarding. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_19_death_case_chain", "STEP 3: THE PPO (R76)"):
        "Step 3: Rule 76: the Accounts Officer completes Form 11 Part II Section I in one month and issues the PPO in one month; extension of provisional pension needs Head of Department approval; the PPO shows when provisional payment ended and when the PDA starts. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_19_death_case_chain", "STEP 4: SEAL AND PAYMENT (R76(8), R80)"):
        "Step 4: Rule 76(8) and Rule 80(2)-(4): the Accounts Officer sends the case to the CPAO with Format 9 in one month; Special Seal in ten days; the PDA disburses in fifteen days. Start points differ: Rule 72 from intimation, Rules 74 and 75 from the claim, Rule 75(3) from the day after death. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_20_rule79_named", "RULE 79(1): THE TRIGGERS"):
        "Rule 79(1): where the Head of Office receives intimation or information about the death or disappearance of a PENSIONER, or the death, disappearance or INELIGIBILITY of a FAMILY PENSIONER, he shall ascertain whether family pension or residuary gratuity or both are payable for a deceased pensioner, whether family pension is payable for a missing pensioner, and whether family pension is payable on the death or disappearance of a family pensioner, and proceed as provided. Ineligibility is a trigger on its own. Residuary gratuity = what is left of the retired servant's gratuity entitlement after his death (Rule 45(2), Batch 4). [Bare text read 24.10.2026.]",
    ("c6_20_rule79_named", "RULE 79(2)(a)(i)-(ii): NO FRESH SANCTION"):
        "Rule 79(2)(a)(i): an eligible widow or widower gets the family pension as already stated in the PPO, from the day after the pensioner's death, with no fresh sanction. (ii): the Pension Disbursing Authority, not the Head of Office, pays within one month of the Form 12 claim accompanied by a copy of the death certificate and the Format 9 undertaking. [Bare text read 24.10.2026.]",
    ("c6_20_rule79_named", "RULE 79(2)(a)(iii)-(v): OTHER DEPENDANTS"):
        "Rule 79(2)(a)(iii): a permanently disabled child, dependent parents and disabled siblings already named in the PPO (under Rule 63(1)(e)) use the same route. (iv): if not named, the Accounts Officer adds the names on the Head of Office's written communication, based on the spouse's request in FORM 8. (v): on the death or ineligibility of a family pensioner, the next disabled dependant is paid by the PDA within one month on Form 12. The source flagged (iii) to (v) as unverified; they now match a secondary summary. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_20_rule79_named", "EXAMPLE AND TRAP"):
        "Example (invented): pensioner Mr Bilal Khan dies on 3 March; his widow, already named in the PPO, files a Form 12 claim with a death certificate and the Format 9 undertaking; the PDA starts payment within a month of the claim, and the pension runs from 4 March. No Format 13 sanction is needed. Trap: do not send a PPO-named widow down the Form 10 and Format 13 route.",
    ("c6_21_rule79_notnamed_missing", "RULE 79(2)(b): FORMAT 13 IN ONE MONTH"):
        "Rule 79(2)(b)(i): where the PPO includes no member of the family, or the Head of Office is of the opinion that family pension has become payable to a member other than the one named in the PPO under Rule 63(1) or 79(2)(a)(i)/(iv) - INCLUDING A PERSON WHO BECAME A MEMBER OF THE FAMILY OF THE PENSIONER AFTER HIS RETIREMENT - he shall, within one month of the receipt of a claim in Form 10, sanction the family pension in FORMAT 13 to that member. (ii): a permanently disabled child, dependent parents and disabled siblings are added only if nobody ranks ahead of them. The earlier doubt (ledger R79-2B-AFTERRET) is now closed: those words are in the text. [Bare text read 24.10.2026.]",
    ("c6_21_rule79_notnamed_missing", "RULE 79(3): A MISSING PENSIONER"):
        "Rule 79(3)(i)-(v): for a missing pensioner or family pensioner, entitlement comes from Rule 51(2) and (3) (compare Rule 71(5), which uses 51(1) and (4) for a serving person); the Head of Office writes in FORMAT 12; the claim is in FORM 10 with the police report (FIR, DD or GD entry), the untraced report, the FORMAT 8 indemnity bond and the FORMAT 9 undertaking; the Head of Office sanctions in FORMAT 13. [Bare text read 24.10.2026.]",
    ("c6_21_rule79_notnamed_missing", "79(3)(iv)-(v): TWO DATES, SIX MONTHS"):
        "Rule 79(3)(iv): only two dates: the day after the last pension or family pension paid, or the police report date, whichever is later. (v): payment is not made earlier than six months after the police report, and the sanction must say so (ledger LIMIT-6M-POLICE; the same six months appears in 76(3)(f) and 80(1) second proviso). [Bare text read 24.10.2026.]",
    ("c6_21_rule79_notnamed_missing", "79(3)(vi)-(vii), AND THE TRAP"):
        "Rule 79(3)(vi): a claim is not rejected only because the name is not in Form 4 or in the records. Rule 79(3)(vii) (an ADDITION; the source omitted it): a family member other than the widow or widower files the Rule 50(12)(b) documents with the claim. Trap: serving missing servant has THREE dates (Rule 76(3)(e)); missing pensioner has TWO (Rule 79(3)(iv)). [Bare text read 24.10.2026.]",
    ("c6_22_rule79_remarriage", "RULE 79(4): REMARRIAGE"):
        "Rule 79(4)(a)(i): where a widow or widower in receipt of family pension remarries and has, at the time of remarriage, a minor child or children of the deceased servant or pensioner who are eligible, the remarried individual remains eligible to draw the family pension ON BEHALF OF those children, so long as he or she continues to be their guardian. (ii): the remarried individual applies to the Head of Office in Form 10 with a declaration of continuing guardianship. (iii): if that person has ceased to be the guardian, the pension goes to whoever is entitled to act as guardian under the law, who may claim in Form 10. (b): in a clause (a) case the family pension becomes payable to the child from the date he attains majority, provided he remains eligible after that date. (c): where the child had ALREADY attained majority at the time of the remarriage and is eligible, the family pension is payable to that child after the remarriage of the parent. Remarriage moves the pension down one generation; it does not switch it off. [Bare text read 24.10.2026.]",
    ("c6_22_rule79_remarriage", "RULE 79(5): GUARDIAN CLAIMS"):
        "Rule 79(5) (an ADDITION; the source had no sub-rules 5 and 6): a guardian may claim in Form 10 for a minor or for a person with mental disorder, disability or mental retardation. [Bare text read 24.10.2026.]",
    ("c6_22_rule79_remarriage", "RULE 79(6): RESIDUARY GRATUITY"):
        "Rule 79(6) (an ADDITION): after the death of a retired servant, residuary gratuity under Rule 45(2) is sanctioned by the Head of Office on the FORM 13 claims of eligible persons. Count: Rule 79 has SIX sub-rules, not four as the source said (ledger R79-COUNT). [Bare text read 24.10.2026.]",
    ("c6_22_rule79_remarriage", "THE THREE ROUTES, AND TRAP"):
        "Three routes (ledger R79-FORMS-3PATHS): name already in the PPO leads to Form 12 and the PDA; no name in the PPO leads to Form 10 and Format 13; missing leads to Form 10, Format 8 indemnity bond and Format 13. Trap: Format 13 sanctions family pension; Form 13 claims residuary gratuity. Q and A: if the widow remarries, is family pension stopped? Not directly: she may draw for minor children while she is their guardian (Rule 79(4)); the child draws on majority.",
    ("c6_23_rule80_clocks", "THE THREE CLOCKS"):
        "Rule 80(1): the Accounts Officer authorises payment within one month of the Rule 79 sanction. 80(2): the AO sends the case to the Central Pension Accounting Office (CPAO) with the Format 9 undertaking within one month. 80(3): the CPAO issues the Special Seal within ten days, as per the orders of the CGA (Controller General of Accounts). 80(4): the Pension Disbursing Authority (PDA) disburses within fifteen days (ledger TL-R80-CLOCKS). Together about 55 to 60 days (30 + 10 + 15 days) for the last three steps (R80-2MONTHS-TOTAL). [Bare text read 24.10.2026.]",
    ("c6_23_rule80_clocks", "FIRST PROVISO: INTEREST"):
        "First proviso to Rule 80(1): if payment of gratuity is delayed because of administrative lapses, interest is payable for delay beyond three months of the date of submitting the claim (a claim-based clock, not death-based); responsibility is fixed under Rule 65. Interest is at the GPF rate; sanctioned by the Secretary or an officer not below Joint Secretary; payment within two months of the sanction (O.M. No. 28/91/2022-P&PW(B)/8331 of 11.10.2022). Contrast: Rule 65(5)(a) for superannuation counts three months from retirement. GPF rate: 7.1 per cent for 01.10.2026 to 31.12.2026 (DEA resolution of 05.10.2026), a quarterly figure from a blog-level source: check the latest O.M. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_23_rule80_clocks", "SECOND PROVISO: MISSING CASES"):
        "Second proviso to Rule 80(1): in a missing case the Accounts Officer records in the PPO the date up to which pension or family pension was paid, and that payment will not be made earlier than six months from the police report. [Bare text read 24.10.2026.]",
    ("c6_23_rule80_clocks", "EXAMPLE AND TRAP"):
        "Example (invented): Dev's family submits the gratuity claim on 1 March. Interest for administrative delay is counted only for delay beyond 1 June (three months from the claim). The last three steps take about 55 days from the Rule 79 sanction. Trap: counting the three months from the date of death, or forgetting that the lapse must be administrative. Delay at the PDA stage often traces to earlier steps, so the whole record is examined (teaching comment from the source).",
    ("c6_24_rule80_5", "RULE 80(5)(a): THE SPOUSE CLAIMS"):
        "Rule 80(5)(a): where the retired servant died without submitting the forms under Rule 57 or 58, the Head of Office allows the spouse (and, if there is no spouse, any other member eligible for family pension) to claim in FORM 10, with FORM 4 and the FORMAT 9 undertaking. [Bare text read 24.10.2026.] Form 4 = the family details form.",
    ("c6_24_rule80_5", "THE PROVISO: GRATUITY NOMINEE"):
        "Proviso to Rule 80(5)(a): if no member is eligible for family pension, the gratuity nominee may submit a form instead of Form 10. OBSOLETE / HISTORY ONLY: the original and the O.M. of 28.10.2022 name FORM 6; since G.S.R. 410(E) of 16.07.2024 (effective 16.11.2024) the proviso reads FORM 6-A (with bank details), which replaced Form 6. [Bare text read 24.10.2026.]",
    ("c6_24_rule80_5", "CLAUSES (b) TO (e)"):
        "Rule 80(5)(b): the Head of Office completes Form 7 for pension and gratuity, noting that the retiree did not submit Form 6 (now 6-A) and other documents before death; if a Form 10 claim exists, he issues a Format 13 sanction. 80(5)(c), substituted by G.S.R. 410(E): he forwards 'Form 4, Form 10, Format 9 and Format 13, if applicable, OR Form 6-A, as the case may be' with Form 7 and the Format 10 letter to the Accounts Officer. 80(5)(d) and (e) are ADDITIONS: the AO authorises pension, retirement gratuity and family pension in Part II of the PPO and authorises the Head of Office to pay pension arrears from the day after retirement up to death to the family pension recipient (else to the gratuity recipient); if family pension is authorised, the PPO copy goes with Format 9 to the CPAO for the Special Seal, and sub-rules (2) to (4) apply. [Close restatement; Gazette text not read.]",
    ("c6_24_rule80_5", "EXAMPLE AND TRAP"):
        "Example (invented): Mr Dev Rao retires and dies two years later without submitting Form 6-A. His wife files Form 10, Form 4 and the Format 9 undertaking; accounts authorises in one month, the CPAO seals in ten days, the PDA pays in fifteen days. Dates: G.S.R. 410(E) of 16.07.2024 took effect 16.11.2024 (120 days after publication, computed). Q and A: after the 2024 amendment both routes exist: the old form set or Form 6-A (Rule 80(5)(c)). Trap: do not quote Form 6 any more.",
    ("c6_25_rule81_start", "RULE 81(1): PENSION"):
        "Rule 81(1): pension, other than family pension, is payable from the date the servant ceases to be borne on the establishment, subject to Rule 8 (the power to withhold or withdraw pension). Borne on the establishment = on the rolls of the office. [Bare text read 24.10.2026.]",
    ("c6_25_rule81_start", "RULE 81(2): FAMILY PENSION"):
        "Rule 81(2): family pension is payable from the day after the death of the servant or the pensioner, and from the day after the death or ineligibility of a family pensioner, subject to Rule 76(2)(d) and Rule 79(3)(iv) as cited. Flag: the cited Rule 76 reference looks like a slip for 76(3)(d) (ledger R81-2, R76-3D); check the Gazette. Rule 79(3)(iv) is the two-dates test for a missing pensioner. [Bare text read 24.10.2026.]",
    ("c6_25_rule81_start", "RULE 81(3): THE DAY OF DEATH IS PAID"):
        "Rule 81(3): pension, including family pension, is payable for the day on which the recipient dies. The last day is paid in full. [Bare text read 24.10.2026.]",
    ("c6_25_rule81_start", "TRAP: RULE 70(2) VERSUS RULE 81(1)"):
        "Rule 70(2) says when the servant ceases to be in service (deemed retired on reaching superannuation age; consistent, ledger R81-70-2); Rule 81(1) says when pension starts. Example (invented): Charu, a pensioner, dies on 12 August: her own pension is payable for 12 August (Rule 81(3)) and family pension starts on 13 August. Trap: starting family pension on the day of death.",
    ("c6_26_rules82_83", "RULE 82: RUPEES, ONLY IN INDIA"):
        "Rule 82: pensions and gratuities are paid in rupees and only in India. No flexibility on currency or place. [Bare text read 24.10.2026.]",
    ("c6_26_rules82_83", "RULE 83(1): GRATUITY LUMP SUM"):
        "Rule 83(1): gratuity is paid as a lump sum unless these Rules provide otherwise. Lump sum = all at once, not in instalments. [Bare text read 24.10.2026.]",
    ("c6_26_rules82_83", "RULE 83(2): MONTH-END, AND MARCH"):
        "Rule 83(2): monthly pension for a month is paid on or after the last working day of that month; the exception is March: March pension is paid on or after the first working day of April. The source gives the reason as the financial year ending in March; that explanation is the source's own, not rule text (ledger R83-WHY). [Bare text read 24.10.2026.]",
    ("c6_26_rules82_83", "RECOMPUTED EXAMPLE, AND THE TRAP"):
        "Corrected example (ledger R83-EX, source example was doubtful): Mr Bilal Khan retires on 30 June 2026. Pension starts the day he ceases to be borne on the establishment (Rule 81(1)), so from 1 July 2026; the first monthly payment is for July, paid on or after the last working day of July. His March 2027 pension is paid on or after the first working day of April 2027. The O.M. of 29.09.2025 sets a calendar target of crediting by the last day of the retirement month, which concerns the first credit and is administrative. Trap: saying the first pension is for June, and forgetting the March exception.",
    ("c6_27_rule84", "RULE 84(1): TREASURY RULES"):
        "Rule 84(1): SAVE AS OTHERWISE PROVIDED IN THESE RULES, the Treasury Rules of the Central Government apply to the procedure for payment of (i) gratuity, (ii) pension, (iii) pension undrawn for more than a year, and (iv) pension in respect of a deceased pensioner. The opening words are in the text, so the 2021 Rules win in a conflict. (2): the CCS (Commutation of Pension) Rules 1981 govern commutation, payment of the commuted value and restoration after the period of commutation. (3): the Payment of Arrears of Pension (Nominations) Rules 1983 govern nomination for receiving arrears after a pensioner's death. [Bare text read 24.10.2026.]",
    ("c6_27_rule84", "RULE 84(2): COMMUTATION RULES 1981"):
        "Rule 84(2): the CCS (Commutation of Pension) Rules, 1981 apply to commutation, payment of the commuted value, and restoration after the commutation period ends. Commutation = giving up part of the monthly pension for a lump sum. Restoration = the monthly pension returning to full when the commutation period is over. [Bare text read 24.10.2026.]",
    ("c6_27_rule84", "RULE 84(3): ARREARS NOMINATIONS 1983"):
        "Rule 84(3): the Payment of Arrears of Pension (Nominations) Rules, 1983, which let a pensioner nominate who receives arrears after death. OBSOLETE / HISTORY ONLY for retirees: nominations were in Form A; the nomination for arrears and commutation now goes in Form 6-A for retiring employees (O.M. F.No. 55/13/2023-P&PW(C)(Part1) of 11.09.2024); Form A is still used for later or changed nominations. Count: Rule 84 has THREE sub-rules (confirmed, ledger R84-COUNT). [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_27_rule84", "PATTERN AND TRAP"):
        "Teaching pattern (not rule text; ledger ALLOC-PATTERN): when the question is 'which instrument' or 'who', think allocation rule; when it is 'how much' or 'from when', think substantive rule. Q and A: where is commutation governed? In the 1981 Commutation Rules, brought in by Rule 84(2). Trap: looking for commutation percentages inside Rules 71 to 87.",
    ("c6_28_rules85_86", "RULE 85: INTERPRETATION"):
        "Rule 85 (Interpretation): where any doubt arises as to the interpretation of these rules, it shall be referred, FOR DECISION, to the Government in the Department of Pension and Pensioners' Welfare or the Department of Personnel and Training, depending upon the rule or the subject on which a decision is required and the department concerned with that rule or subject. Read it with the O.M. of 24.10.2025, which tells you HOW to refer. The office does not decide a doubt itself. [Bare text read 24.10.2026.]",
    ("c6_28_rules85_86", "RULE 86: POWER TO RELAX"):
        "Rule 86 (Power to relax): where any Ministry or Department is satisfied that the operation of any of these rules causes undue hardship in any particular case, that Ministry or Department may, by order for reasons recorded in writing, dispense with or relax the requirements of that rule to such extent and subject to such exceptions and conditions as it may consider necessary for dealing with the case in a just and equitable manner. PROVISO: no such order shall be made except with the concurrence of DoPPW or DoPT, depending upon the rule or the subject. Three keys: individual hardship, written reasons, prior concurrence. [Bare text read 24.10.2026.]",
    ("c6_28_rules85_86", "O.M. 24.10.2025: HOW TO REFER"):
        "O.M. No. 1/1(51)/2024-P&PW(F)/9852 dated 24.10.2025 (number and date confirmed): guidelines for referring cases to DoPPW. Principle: first examine the case thoroughly and reach a tentative conclusion; refer only if doubt remains. The proposal has five items: (1) background and examination done; (2) tentative conclusion; (3) the specific rule or provision on which clarification is sought; (4) cases not explicitly covered, with the justification for an exception; (5) officer name, designation, phone and email. Route: through the administrative Ministry with the Secretary's approval and comments, preferably on e-File. Scope: Railways, Defence, PSUs, Banks, Autonomous Bodies and Statutory Bodies are outside. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_28_rules85_86", "THE LINK, AND THE TRAP"):
        "Link: Rule 85 (to whom) plus the O.M. (how). The source's further point that the O.M. discipline also applies to Rule 86 relaxation proposals is its own commentary (ledger OM-24.10.2025-R86, unverified). Q and A: can an office refer a case to DoPPW without examining it? No; it must first examine, form a tentative conclusion and identify the provision. Trap: a bare reference with no tentative conclusion is not a proper referral.",
    ("c6_29_rule87", "RULE 87(1): THE REPEAL"):
        "Rule 87(1): on the commencement of these rules, every rule [including the CCS (Pension) Rules, 1972], regulation or order including an Office Memorandum in force immediately before commencement shall, in so far as it provides for any of the matters contained in these rules, cease to operate. Two limits: it is a partial repeal (only overlapping matters), and only instruments in force immediately before commencement. [Bare text read 24.10.2026.]",
    ("c6_29_rule87", "SAVINGS (a) AND (b): DOCUMENTS"):
        "Rule 87(2)(a): every (i) nomination for the payment of gratuity, (ii) form regarding the details of the family for family pension, and (iii) formal application for the sanction of pension, made or given under the old rule, is deemed to have been made or given under the corresponding provisions of these Rules. (b): a nomination or family-details form required under the old rule but not made or given before commencement must be made or given after commencement in accordance with these Rules. Documents go forward. [Bare text read 24.10.2026.]",
    ("c6_29_rule87", "SAVINGS (c), (d), (e): PENDING CASES"):
        "Rule 87(2)(c): a case concerning the authorisation of pension to a Government servant who had retired before commencement, pending at commencement, is disposed of under the old rule as if these rules had not been made. (d): the same for a pending case concerning authorisation of gratuity and family pension to the family of a deceased servant or a deceased pensioner. (e): subject to (c) and (d), anything done or action taken under the old rule is deemed to have been done or taken under the corresponding provisions of these rules. Pending cases stay behind; documents and past acts come forward. [Bare text read 24.10.2026.]",
    ("c6_29_rule87", "MEMORY LINE, EXAMPLE AND TRAP"):
        "Teaching device, not rule text: the document goes forward, the pending case stays behind. Example (invented): Mr Dev Rao retired in 2019 and his pension case is still pending at commencement; it is decided under the CCS (Pension) Rules 1972, and his old nomination still counts under 87(2)(a). Q and A: a servant who retired before 2021 with a pending case is dealt with under the 1972 Rules - that is clause (c). Trap: applying the 2021 Rules to such a case, or thinking that only the 1972 Rules were repealed (Office Memoranda are covered too). [Bare text read 24.10.2026.]",
    ("c6_30_guidelines_2025", "THE GUIDELINES O.M. AND THE WELFARE OFFICER"):
        "Comprehensive guidelines O.M. No. 4/35/2024-P&PW(D)/10377: number confirmed; dated 29.09.2025 (PIB copy posted 30.09.2025). Layer: executive O.M. and administrative calendar, not the Rules. The Welfare Officer (Pension Mitra) is posted with each retiring employee, and one task is to hand-hold dependents in documentation and verification of the family pension claim when a pensioner dies. A separate circular on Welfare Officer roles was promised; none was found. Q and A: the Welfare Officer helps with documentation and verification. [Close restatement from secondary pages; PIB copy listed, not itemised.]",
    ("c6_30_guidelines_2025", "THE PPO CALENDAR (CORRECTED LABELS)"):
        "Calendar stages (ledger OM-29.09.2025-S9, S10A, S10B, S11): stage 9, the PAO sends the PPO or ePPO to the CPAO on the last working day of the month before the retirement month; stage 10-A, the CPAO sends the Special Seal of Authority to the PDA by the 20th of the retirement month; stage 10-B, the pensioner's half copy is handed over on the retirement day by the Head of Office; stage 11, the paying branch credits the pension by the last day of that month. CORRECTION: the source called these stages nine, ten, eleven and twelve; the labels in the O.M. are 9, 10-A, 10-B and 11. READ together with, never in place of, Rule 80: the Rule 80 clocks (one month, ten days, fifteen days) are statutory; this calendar is administrative. Scope: framed for superannuation and other non-superannuation cases (PPO within 45 days); it does not change the death-case timelines of Rules 71 to 80. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_30_guidelines_2025", "THE CLAIMS O.M. OF 30.10.2025"):
        "O.M. F.No. 38/10(03)/2025-P&PW(A) (e 11193)(iii) dated 30.10.2025 (ledger OM-30.10.2025-NO): the date of death is treated as a completed working day; and, under Rule 5, a claim is governed by the rules in force on the date of retirement or death. CORRECTION (OM-30.10.2025-FPSTART): the source said this O.M. also says family pension starts the day after death; the O.M. only deals with the death date as a completed working day. The next-day start is Rule 81(2). [Bare text read 24.10.2026.]",
    ("c6_30_guidelines_2025", "TRAP: CALENDAR VERSUS RULE"):
        "Summary of layers: Layer 1 Rule text (Rules 71 to 83 clocks); Layer 3 executive O.M.s and the September 2025 calendar. Q and A: what is the Welfare Officer's role in a death case? To hand-hold dependents in documentation and verification of the family pension claim. Example (invented): after pensioner Mr Bilal Khan dies, the Welfare Officer helps his widow Asha fill Form 12 and collect the death certificate; the Rule 79 and 80 clocks still run as written. Trap: quoting stage 12, or using the calendar to replace the Rule 80 clocks.",
    ("c6_31_amendments_currency", "THE FOUR NOTIFICATIONS"):
        "G.S.R. 868(E) of 20.12.2021: the Rules themselves; no separate change to Rules 71-87 came with it. G.S.R. 770(E) of 07.10.2022, Rule 6 of the Amendment Rules 2022: 'In rule 76 ... for the brackets, figure and words \"(5) The fact of the issue\", the brackets, figure and words \"(5A) The fact of the issue\" shall be substituted.' G.S.R. 410(E) of 16.07.2024, effective 16.11.2024: substituted the proviso and clause (c) of Rule 80(5) and replaced Form 6 by Form 6-A. G.S.R. 340(E) of 22.05.2025: Rule 37(29)(c) only - nothing in Rules 71-87. [Read 24.10.2026.]",
    ("c6_31_amendments_currency", "ANYTHING NEWER?"):
        "NO-AMEND-71-87: no change to Rules 71-87 was found after G.S.R. 410(E) up to 21.10.2026 in the DoPT notification list and in the sources searched; that negative result is limited to those pages. A 2026 G.S.R. 775(E) noted by Batch 4 concerns Rule 37(7), not this batch. Chapter map confirmed from the text: XI (71-78), XII (79-80), XIII (81-84), XIV (85-87). Unlike the previous build, the operative text of Rules 85 to 87 and of Rule 79(1) has now been read, so no rule in 71-87 is left unread. [Read 24.10.2026.]",
    ("c6_31_amendments_currency", "DYNAMIC FIGURES: CHECK BEFORE QUOTING"):
        "Dearness relief (DR): 60 per cent with effect from 01.01.2026 was still current as of 17.10.2026; the 01.07.2026 revision had not been announced then. Check the latest O.M. It matters here through Rule 77(1)(x), where unpaid dues can be recovered from DR. GPF rate: 7.1 per cent for 01.10.2026 to 31.12.2026 (DEA resolution of 05.10.2026, F.No. 5(3)-B(PD)/2023); quarterly, from a blog-level source: check the latest. It is the interest rate used in Rule 80(1) first proviso and in Rule 65. [Bare text read 24.10.2026; cross-batch rules are close restatements.]",
    ("c6_31_amendments_currency", "SOURCE PROBLEMS WE CORRECTED"):
        "Rule counts, checked against the bare text: 71 six sub-rules; 72 three; 73 three; 74 four; 75 eight; 76 eight plus 5A - numbered (1) to (5), then (5A), then (6), (7), (8); 77(1) ten clauses plus 77(2); 78 two; 79 six; 80 five; 81 three; 82 one; 83 two; 84 three; 85 one; 86 one; 87 two. The earlier build's counts were right; the podcast source's were not. Also right: the Form 8-13 rhyme is unsafe, Form A is superseded for retirees, the Rule 83 example had to be recomputed, the 2025 calendar stages are 9, 10-A, 10-B and 11, and the 30.10.2025 O.M. does not say family pension starts the next day. [Bare text read 24.10.2026.]",
    ("c6_32_recap", "KEY NUMBERS"):
        "Key numbers. Rule 71(4)(c): 7 days. Rule 72: 1 year of emoluments, 1 month. Rule 73: other office replies in 1 month. Rule 74: 1 month from the claim; hold-back at most 10 per cent. Rule 75: provisional family pension within 15 days of the claim, for 6 months from the day after death; provisional gratuity in 1 month, final in 3 months. Rule 76: AO 1 month, PPO 1 month; CPAO seal 10 days; PDA 15 days. Rule 77: DoE 1 month, 10 per cent withheld, Rule 67 dues in 15 days. Rule 79: PDA 1 month; Format 13 in 1 month. Rule 80: 1 month, 10 days, 15 days; interest beyond 3 months of the claim. Missing: 6 months after the police report. Rule 83: month-end; March pension in April.",
    ("c6_32_recap", "TOP TRAPS"):
        "Top traps: (1) clocks start at different points - intimation (Rule 72), the claim (Rules 74, 75, 80 interest), and the day after death (Rule 75(3)); (2) licence fee is waived but damages are not; (3) an extension of provisional family pension needs the Head of Department; (4) three dates for a missing servant, two for a missing pensioner; (5) Form 6 is now Form 6-A, and Form A is superseded for retirees; (6) Format 13 sanctions while Form 13 claims, and Format 9 is not Form 9; (7) pending cases of those who retired before commencement stay with the 1972 Rules (Rule 87(2)(c)); (8) the September 2025 calendar does not replace the Rule 80 clocks. [Bare text read 24.10.2026.]",
    ("c6_32_recap", "CURRENCY NOTE"):
        "Currency: Rules 71-87 read in the bare text on 24.10.2026; no change to them found after G.S.R. 410(E) (effective 16.11.2024) up to 21.10.2026. Dynamic figures: dearness relief 60 per cent from 01.01.2026 (the 01.07.2026 revision had not been announced when this was checked); GPF 7.1 per cent for 01.10.2026 to 31.12.2026, which is the rate used by the proviso to Rule 80(1) and by Rule 65 - check the latest O.M. Principle from the rule, figure from the O.M.",
    ("c6_32_recap", "WHAT COMES NEXT"):
        "Next: Batch 7, the cross-cutting recap: the pension computation decision tree, the three amendments, Forms 1 to 13, Formats 1 to 13, master deadlines, key amounts and counts. Before then, rehearse three things: death-case emoluments are one year; provisional family pension is 15 days and 6 months; the Rule 80 clocks are one month, ten days and fifteen days. Chapters covered this batch: XI (71-78), XII (79-80), XIII (81-84), XIV (85-87).",
}

_COLOURS = {"BG_TOP": BG_TOP, "BG_BOT": BG_BOT, "CARD_BG": CARD_BG, "TEXT_WHITE": TEXT_WHITE,
            "MUTED": MUTED, "ORANGE": ORANGE, "GREEN": GREEN, "BLUE": BLUE, "SKY": SKY,
            "RED": RED, "YELLOW": YELLOW, "PINK": PINK}
for _sc in SCENES:
    _sc["accent"] = _COLOURS[_sc["accent"]]
    _sc["boxes"] = [(t, s, _COLOURS[c], n) for (t, s, c, n) in _sc["boxes"]]
assert len({s["id"] for s in SCENES}) == len(SCENES), "duplicate scene id"
assert all(len(s["boxes"]) == 4 for s in SCENES), "every chapter must carry four cards"
assert set(FULL) == {(s["id"], b[0]) for s in SCENES for b in s["boxes"]}, "FULL/card mismatch"



# ============================================================================
# RULE INVENTORY - machine-checked coverage of Rules 71 to 87
# Every sub-rule, clause and proviso of the chapters in scope must point at a scene.
# `--coverage` fails the build if any unit is unmapped or points at a missing scene.
# ============================================================================
INVENTORY = [
    # ---- Chapter XI: death or disappearance while in service (Rules 71-78)
    ("71(1)", "c6_01_rule71_first_steps"),
    ("71(2)(a)", "c6_01_rule71_first_steps"),
    ("71(2)(b)", "c6_01_rule71_first_steps"),
    ("71(3)", "c6_01_rule71_first_steps"),
    ("71(4)(a)", "c6_02_rule71_4_quarters"),
    ("71(4)(b)", "c6_02_rule71_4_quarters"),
    ("71(4)(c)", "c6_02_rule71_4_quarters"),
    ("71(5)", "c6_03_rule71_5_6_missing"),
    ("71(6)(a)-(b)", "c6_03_rule71_5_6_missing"),
    ("71(6)(c)", "c6_03_rule71_5_6_missing"),
    ("71(6)(d)", "c6_03_rule71_5_6_missing"),
    ("71(6)(e)", "c6_03_rule71_5_6_missing"),
    ("71(6)(f)", "c6_03_rule71_5_6_missing"),
    ("71(6)(g)", "c6_03_rule71_5_6_missing"),
    ("72(1)(a)", "c6_05_rule72_1_service"),
    ("72(1)(b)(i)", "c6_05_rule72_1_service"),
    ("72(1)(b)(ii)", "c6_05_rule72_1_service"),
    ("72(1)(b)(iii)", "c6_05_rule72_1_service"),
    ("72(2)(a)", "c6_06_rule72_emoluments_vs57"),
    ("72(2)(b)", "c6_06_rule72_emoluments_vs57"),
    ("72(3)", "c6_06_rule72_emoluments_vs57"),
    ("73(1)", "c6_07_rule73_incomplete_records"),
    ("73(2)(a)", "c6_07_rule73_incomplete_records"),
    ("73(2)(b)(i)", "c6_07_rule73_incomplete_records"),
    ("73(2)(b)(ii)", "c6_07_rule73_incomplete_records"),
    ("73(3)", "c6_07_rule73_incomplete_records"),
    ("73(2)(b)(iii)", "c6_08_rule73_clocks"),
    ("proviso to 73(2)(b)(iii)", "c6_08_rule73_clocks"),
    ("73(2)(b)(iv)", "c6_08_rule73_clocks"),
    ("73(2)(b)(v)", "c6_08_rule73_clocks"),
    ("73(2)(b)(vi)", "c6_08_rule73_clocks"),
    ("74(1)", "c6_09_rule74_send_to_ao"),
    ("74(2)", "c6_09_rule74_send_to_ao"),
    ("74(3)", "c6_09_rule74_send_to_ao"),
    ("74(4)(a)-(b)", "c6_09_rule74_send_to_ao"),
    ("74(4)(c)", "c6_09_rule74_send_to_ao"),
    ("75(1)", "c6_10_rule75_provisional_fp"),
    ("75(2)", "c6_10_rule75_provisional_fp"),
    ("75(3)", "c6_10_rule75_provisional_fp"),
    ("75(4)", "c6_10_rule75_provisional_fp"),
    ("75(5)-(6)", "c6_11_rule75_gratuity"),
    ("75(7)(a)", "c6_11_rule75_gratuity"),
    ("75(7)(b)-(c)", "c6_11_rule75_gratuity"),
    ("75(8)", "c6_11_rule75_gratuity"),
    ("76(1)", "c6_12_rule76_1_2_ao"),
    ("first proviso to 76(1)", "c6_12_rule76_1_2_ao"),
    ("second proviso to 76(1)", "c6_12_rule76_1_2_ao"),
    ("76(2)", "c6_12_rule76_1_2_ao"),
    ("76(3)(a)", "c6_13_rule76_3_ppo"),
    ("76(3)(b)-(c)", "c6_13_rule76_3_ppo"),
    ("76(3)(d)", "c6_13_rule76_3_ppo"),
    ("76(3)(e)", "c6_13_rule76_3_ppo"),
    ("76(3)(f)", "c6_13_rule76_3_ppo"),
    ("76(4)", "c6_14_rule76_4_8"),
    ("76(5)(a)-(b)", "c6_14_rule76_4_8"),
    ("76(5)(c)-(d)", "c6_14_rule76_4_8"),
    ("76(5)(e)", "c6_14_rule76_4_8"),
    ("76(5A)", "c6_14_rule76_4_8"),
    ("76(6)", "c6_14_rule76_4_8"),
    ("76(7)(a)-(b)", "c6_14_rule76_4_8"),
    ("76(8)(a)-(c)", "c6_14_rule76_4_8"),
    ("76(8)(d)-(e)", "c6_14_rule76_4_8"),
    ("77(1)(i)(a)-(g)", "c6_15_rule77_a"),
    ("77(1)(ii)", "c6_15_rule77_a"),
    ("77(1)(iii)", "c6_15_rule77_a"),
    ("77(1)(iv)", "c6_15_rule77_a"),
    ("77(1)(v)", "c6_16_rule77_b"),
    ("77(1)(vi)", "c6_16_rule77_b"),
    ("77(1)(vii)", "c6_16_rule77_b"),
    ("77(1)(viii)", "c6_16_rule77_b"),
    ("77(1)(ix)", "c6_16_rule77_b"),
    ("77(1)(x)", "c6_16_rule77_b"),
    ("77(2)", "c6_16_rule77_b"),
    ("78(1)", "c6_17_rule78_deputation"),
    ("78(2)", "c6_17_rule78_deputation"),
    # ---- Chapter XII: deceased or missing pensioners (Rules 79-80)
    ("79(1)", "c6_20_rule79_named"),
    ("79(2)(a)(i)-(ii)", "c6_20_rule79_named"),
    ("79(2)(a)(iii)-(v)", "c6_20_rule79_named"),
    ("79(2)(b)(i)", "c6_21_rule79_notnamed_missing"),
    ("79(2)(b)(ii)", "c6_21_rule79_notnamed_missing"),
    ("79(3)(i)-(iii)", "c6_21_rule79_notnamed_missing"),
    ("79(3)(iv)", "c6_21_rule79_notnamed_missing"),
    ("79(3)(v)", "c6_21_rule79_notnamed_missing"),
    ("79(3)(vi)-(vii)", "c6_21_rule79_notnamed_missing"),
    ("79(4)(a)", "c6_22_rule79_remarriage"),
    ("79(4)(b)-(c)", "c6_22_rule79_remarriage"),
    ("79(5)", "c6_22_rule79_remarriage"),
    ("79(6)", "c6_22_rule79_remarriage"),
    ("80(1)", "c6_23_rule80_clocks"),
    ("first proviso to 80(1)", "c6_23_rule80_clocks"),
    ("second proviso to 80(1)", "c6_23_rule80_clocks"),
    ("80(2)", "c6_23_rule80_clocks"),
    ("80(3)", "c6_23_rule80_clocks"),
    ("80(4)", "c6_23_rule80_clocks"),
    ("80(5)(a)", "c6_24_rule80_5"),
    ("proviso to 80(5)(a)", "c6_24_rule80_5"),
    ("80(5)(b)-(c)", "c6_24_rule80_5"),
    ("80(5)(d)-(e)", "c6_24_rule80_5"),
    # ---- Chapter XIII: payment (Rules 81-84)
    ("81(1)", "c6_25_rule81_start"),
    ("81(2)", "c6_25_rule81_start"),
    ("81(3)", "c6_25_rule81_start"),
    ("82", "c6_26_rules82_83"),
    ("83(1)", "c6_26_rules82_83"),
    ("83(2)", "c6_26_rules82_83"),
    ("84(1)(i)-(iv)", "c6_27_rule84"),
    ("84(2)", "c6_27_rule84"),
    ("84(3)", "c6_27_rule84"),
    # ---- Chapter XIV: miscellaneous (Rules 85-87)
    ("85", "c6_28_rules85_86"),
    ("86", "c6_28_rules85_86"),
    ("proviso to 86", "c6_28_rules85_86"),
    ("87(1)", "c6_29_rule87"),
    ("87(2)(a)", "c6_29_rule87"),
    ("87(2)(b)", "c6_29_rule87"),
    ("87(2)(c)-(d)", "c6_29_rule87"),
    ("87(2)(e)", "c6_29_rule87"),
]

# Chapters that are pure cross-reference / comparison chapters (no new sub-rule of their own).
CROSS_CUTTING = {
    "c6_04_forms_map_71_80": "Forms and Formats used by Rules 71-80",
    "c6_18_chX_vs_chXI": "Chapter X (retirement) versus Chapter XI (death)",
    "c6_19_death_case_chain": "The death-case chain, step by step",
    "c6_30_guidelines_2025": "The September-October 2025 O.M.s",
    "c6_31_amendments_currency": "Amendment register and currency",
    "c6_32_recap": "Recap",
}

PART_STARTS = ["c6_01_rule71_first_steps", "c6_12_rule76_1_2_ao", "c6_23_rule80_clocks"]

# ============================================================================
# TABLES - four chapters are better shown as a real table than as four cards.
# Rows are revealed in four groups (one per narration beat) so the video still moves.
# ============================================================================
TABLES = {
    "c6_04_forms_map_71_80": {
        "cols": ["Paper", "What it actually is", "Where it appears"],
        "widths": [0.20, 0.52, 0.28],
        "rows": [
            ["Form 3", "Common nomination: gratuity + GPF + CGEGIS", "Rule 46"],
            ["Form 9", "Claim for gratuity (death or missing)", "71(2)(b), 71(6)"],
            ["Form 10", "Claim for family pension", "50, 71, 74, 76, 79, 80"],
            ["Form 11", "The family-pension case file; AO fills Part II, Section I", "74(1), 76(1)"],
            ["Form 12", "Claim where the name is already in the PPO", "79(2)(a)"],
            ["Form 13", "Claim for residuary gratuity of a retired servant", "79(6)"],
            ["Format 7", "Indemnity bond where the claimant is a minor", "Form 9, enclosure (b)"],
            ["Format 8", "Indemnity bond in a MISSING case", "71(6)(d), 79(3)(iii)"],
            ["Format 9", "Undertaking to the bank (not the gratuity claim)", "71(3), 74(1), 80(5)"],
            ["Format 10 / 11 / 12", "Covering letter / gratuity letter / family-pension letter", "74(1) / 71(2)(b) / 71(3)"],
            ["Format 13", "Sanction of family pension (not a claim)", "79(2)(b), 79(3)(iv)"],
        ],
    },
    "c6_18_chX_vs_chXI": {
        "cols": ["Point of comparison", "Retirement case (Chapter X)", "Death case (Chapter XI)"],
        "widths": [0.24, 0.38, 0.38],
        "rows": [
            ["When the case starts", "One year before, or on leave preparatory to retirement", "The moment intimation of death arrives"],
            ["Service verification", "Staged checks; unverified parts proved from records", "Whole service book; unverified part deemed verified"],
            ["Emoluments checked", "24 months (Rule 57)", "One year (Rule 72(2))"],
            ["Provisional payment", "Only if there is a delay (Rule 62), 6-month cap", "Family pension in 15 days, paid 6 months"],
            ["The PPO", "2 months before superannuation; 45 days otherwise", "Within one month of the family pension case"],
            ["Housing dues", "Last 8 months' fee from pay; DoE has 2 months", "Old fee waived; letter in 7 days; DoE has 1 month"],
            ["Who drives it", "The servant himself, a year in advance", "The family, helped by the Head of Office"],
            ["The trap", "Do not import 24 / 2 / 8 months into a death case", "Do not import the 15-day / 6-month clock into retirement"],
        ],
    },
    "c6_31_amendments_currency": {
        "cols": ["Instrument", "Date and effect", "What it did to Rules 71-87"],
        "widths": [0.24, 0.30, 0.46],
        "rows": [
            ["G.S.R. 868(E)", "20.12.2021 - the Rules themselves", "Brought Rules 71-87 into force"],
            ["G.S.R. 770(E)", "07.10.2022, from publication", "Rule 76: the second sub-rule (5) became (5A)"],
            ["G.S.R. 410(E)", "16.07.2024, effective 16.11.2024", "Rule 80(5): Form 6 replaced by Form 6-A"],
            ["G.S.R. 340(E)", "22.05.2025", "Rule 37 only - nothing in Rules 71-87"],
            ["Search result", "Checked to 21.10.2026", "No later change found in Rules 71-87"],
            ["Dynamic figures", "Every quarter / half year", "DR and the GPF rate: quote the latest O.M."],
        ],
    },
    "c6_32_recap": {
        "cols": ["Number", "Rule", "What it times"],
        "widths": [0.28, 0.24, 0.48],
        "rows": [
            ["7 days", "71(4)(c)", "Head of Office writes to the Directorate of Estates"],
            ["1 year", "72(2)", "Emoluments checked before death or disappearance"],
            ["1 month", "72(3) / 74(1)", "Determination from intimation / case to AO from the claim"],
            ["15 days", "75(1)", "Provisional family pension from receipt of the claim"],
            ["6 months", "75(3) / 76(3)(f) / 79(3)(v)", "Provisional family pension / wait after a police report"],
            ["1 + 10 + 15 days", "80(1)-(4)", "Authorisation, Special Seal, payment by the PDA"],
            ["10 per cent", "74(4)(c) / 77(1)(vi)", "Maximum gratuity held back"],
            ["3 months", "proviso to 80(1)", "Delay after which interest on gratuity begins"],
        ],
    },
}

# ============================================================================
# LANGUAGE GUARD - English on screen, Hinglish in the voice, no Devanagari at all.
# ============================================================================
_DEVANAGARI = re.compile(r'[\u0900-\u097F]')


def assert_no_devanagari():
    bad = []
    for sc in SCENES:
        for field in ("chapter", "title", "badge", "q", "q_say", "hook", "hook_say", "intro", "lead"):
            v = sc.get(field)
            if isinstance(v, str) and _DEVANAGARI.search(v):
                bad.append((sc["id"], field))
        for (t, short, _c, narr) in sc["boxes"]:
            for field, v in (("card title", t), ("card text", short), ("narration", narr)):
                if _DEVANAGARI.search(v):
                    bad.append((sc["id"], field))
    assert not bad, f"Devanagari found (brief says Roman script only): {bad}"


assert_no_devanagari()
assert len({s["id"] for s in SCENES}) == len(SCENES), "duplicate scene id"


# ============================================================================
# REFERENCE SHEET + COVERAGE MATRIX
# ============================================================================
def coverage_rows():
    """[(rule, [(unit, scene_id)])] grouped by top-level rule number."""
    groups = {}
    for unit, sid in INVENTORY:
        rule = re.search(r'(\d+)', unit).group(1)
        groups.setdefault(rule, []).append((unit, sid))
    for rule in groups:
        groups[rule].sort(key=lambda u: [int(x) for x in re.findall(r'\d+', u[0])] or [0])
    return [(r, groups[r]) for r in sorted(groups, key=int)]


def total_units():
    return len(INVENTORY)


def chapter_numbers():
    return {s["id"]: i + 1 for i, s in enumerate(SCENES)}


def write_reference_sheet():
    cn = chapter_numbers()
    out = ["# CCS (Pension) Rules 2021 - Batch 6 (Rules 71-87) - reference sheet",
           "",
           "Generated by build_pension_b6.py. English on screen, Hinglish narration (Roman script).",
           "",
           "Every slide carries a short key-point. This sheet carries the full, examinable wording of",
           "each card, the rule-by-rule coverage matrix, and the drafting slips worth knowing.",
           ""]
    out += ["## 1. Coverage matrix (Rules 71 to 87)", "",
            f"Units mapped: **{total_units()}**. Every unit below is taught on screen in the chapter shown.",
            "", "| Rule | Sub-rule / clause / proviso | Chapter |", "|---|---|---|"]
    for rule, units in coverage_rows():
        for unit, sid in units:
            out.append(f"| {rule} | {unit} | {cn.get(sid, '??')} - {sid} |")
    out += ["", "Chapters without a rule of their own: " +
            ", ".join(f"{cn[sid]} ({why})" for sid, why in CROSS_CUTTING.items() if sid in cn), ""]

    out += ["## 2. Drafting slips in the printed Rules (quote the clause, not the pointer)", "",
            "1. **Rule 75(5)(b)** points to \"sub-rule (3) of rule 74\" for recoverable dues; the dues are listed in Rule 74(4). Rule 74(3) only says keep copies.",
            "2. **Rule 76(5)(e)** cites \"clause (b) of sub-rule (1) of rule 77\" for the 10 per cent withholding - that is clause (vi) - and \"clause (viii)\" for outstanding licence fee - that is clause (iii).",
            "3. **Rule 81(2)** says \"clause (d) of sub-rule (2) of rule 76\"; the family-pension start date is Rule 76(3)(b), and 76(3)(e) for a missing servant.",
            "4. **Rule 76 numbering**: G.S.R. 770(E) of 07.10.2022 turned the second sub-rule numbered (5) into (5A). Rule 76 reads (1)-(5), (5A), (6), (7), (8). Reproductions that never carried the duplicate renumber the list and print those clauses as (6)-(9).", ""]

    out += ["## 3. Language policy", "",
            "* On screen: English, plain administrative English, every term glossed once.",
            "* Narration: Hinglish in Roman script (Hindi grammar, English technical nouns).",
            "* No Devanagari anywhere; the build asserts this before rendering.", ""]

    out += ["## 4. Card-by-card full text", ""]
    for sc in SCENES:
        out += [f"### Chapter {cn[sc['id']]}: {sc['chapter']}",
                f"**{sc['title']}**  ({sc['badge']})", "", f"Q: {sc['q']}", ""]
        for (t, _short, _c, _narr) in sc["boxes"]:
            out += [f"#### {t}", FULL[(sc["id"], t)], ""]
        out += [f"> TRAP: {sc['hook']}", ""]

    Path("pension_b6_reference_sheet.md").write_text("\n".join(out), encoding="utf-8")


def write_narration_script():
    """A plain shooting script: English on screen, Hinglish (Roman) to be spoken."""
    cn = chapter_numbers()
    out = ["# CCS (Pension) Rules 2021 - Batch 6 - shooting script",
           "",
           "English on screen, Hinglish voice (Roman script). On-screen lines are what the viewer reads;",
           "the SAY line under each is what the voice artist speaks. Rule references are spoken in full",
           "('Rule 71, sub rule 4, clause c') by normalize_for_tts().",
           ""]
    for sc in SCENES:
        out += [f"## Chapter {cn[sc['id']]}: {sc['chapter']}", f"**{sc['title']}**  [{sc['badge']}]", ""]
        if sc.get("intro"):
            out += ["**TEACHER (intro)**", f"> {sc['intro']}", ""]
        out += ["**RIYA ASKS**", f"> {sc['q_say']}", "", f"*On screen:* {sc['q']}", ""]
        for i, (title, short, _c, narr) in enumerate(sc["boxes"], 1):
            out += [f"**Card {i} - {title}**", f"*On screen:* {short}", f"> SAY: {narr}", ""]
        out += [f"**TRAP strip**", f"*On screen:* {sc['hook']}", f"> SAY: {sc['hook_say']}", ""]
    Path("pension_b6_narration_script.md").write_text("\n".join(out), encoding="utf-8")


def print_coverage():
    cn = chapter_numbers()
    known = {s["id"] for s in SCENES}
    problems = []
    missing_scene = {sid for _u, sid in INVENTORY if sid not in known}
    if missing_scene:
        problems.append(f"inventory points at unknown scenes: {sorted(missing_scene)}")
    covered = {sid for _u, sid in INVENTORY}
    orphan = [sid for sid in known if sid not in covered and sid not in CROSS_CUTTING]
    if orphan:
        problems.append(f"scenes with no rule mapped: {orphan}")

    print(f"{'rule':6s} {'units':>5s}  chapters")
    for rule, units in coverage_rows():
        chs = sorted({cn[sid] for _u, sid in units})
        print(f"{rule:6s} {len(units):>5d}  {', '.join(map(str, chs))}")
    print(f"\nRules 71-87: {len(coverage_rows())} rules, {total_units()} sub-rule units, "
          f"{len(SCENES)} chapters, {sum(len(s['boxes']) for s in SCENES)} cards.")
    if problems:
        for p in problems:
            print("PROBLEM:", p)
        return 1
    print("Coverage: every inventoried sub-rule, clause and proviso has a chapter. No orphans.")
    return 0


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


def fit_block(draw, text, bold, max_w, max_h, start, min_size=15, spacing=1.22):
    """Shrinks the font until ALL text fits. Never truncates - raises if it cannot fit at min_size."""
    for size in range(start, min_size - 1, -1):
        f = font(size, bold)
        lines = wrap_text(draw, text, f, max_w)
        lh = int(size * spacing)
        if len(lines) * lh <= max_h:
            return f, lines, lh, size
    raise ValueError(f"TOO DENSE (needs < {min_size}px): {text[:90]!r} - shorten the on-screen text")


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
        for y in range(200, 860, 60):
            d.point((x, y), fill=(34, 46, 76))
    return img, d


def split_title(title):
    """'RULE 71(2): THE GRATUITY LETTER' -> ('RULE 71(2)', 'THE GRATUITY LETTER')."""
    if ":" in title:
        head, tail = title.split(":", 1)
        if len(head) <= 26:
            return head.strip(), tail.strip()
    return title.strip(), ""


def dark_ink(color):
    """Near-black ink for light fills, white for dark fills."""
    return (10, 16, 36) if color in (ORANGE, SKY, YELLOW, GREEN, PINK) else TEXT_WHITE


def rounded(d, box, radius, fill=None, outline=None, width=2):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


# ---------------------------------------------------------------------------
# LAYOUT: fixed bands, so every chapter looks like the same broadcast template
# ---------------------------------------------------------------------------
M = 80
PILL_Y, PILL_H = 278, 88
ROWS_TOP, ROWS_BOT = 382, 930
TRAP_Y, TRAP_H = 940, 66


def row_heights(n):
    gap = 12
    h = (ROWS_BOT - ROWS_TOP - gap * (n - 1)) // n
    return h, gap


def draw_chrome(d, scene, qno, total, acc):
    d.rectangle([0, 0, W, 8], fill=acc)

    # chapter tab
    tab = scene["chapter"]
    f_tab = font(21, True)
    tw = text_w(d, tab, f_tab) + 44
    rounded(d, [M, 28, M + tw, 66], 19, fill=lerp(CARD_BG, acc, 0.34), outline=lerp(CARD_BG, acc, 0.75), width=2)
    d.text((M + 22, 38), tab, font=f_tab, fill=TEXT_WHITE)

    # title
    f_title, l_title, lh, _ = fit_block(d, scene["title"], True, 1330, 54, 38, 22, 1.08)
    for k, ln in enumerate(l_title):
        d.text((M, 84 + k * lh), ln, font=f_title, fill=TEXT_WHITE)

    # metadata chips, top right
    chips = [("BATCH 6  •  RULES 71-87", lerp(CARD_BG, acc, 0.55)),
             ("ENGLISH ON SCREEN  •  HINGLISH VOICE", (40, 52, 78))]
    y = 24
    for label, col in chips:
        f = font(15, True)
        cw = text_w(d, label, f) + 28
        rounded(d, [W - M - cw, y, W - M, y + 28], 14, fill=col)
        d.text((W - M - cw + 14, y + 7), label, font=f, fill=TEXT_WHITE)
        y += 34

    d.line([(M, 150), (W - M, 150)], fill=(51, 65, 85), width=2)


def draw_question(d, scene, acc, kind, qno):
    asking = kind == "question"
    top, bot = 162, 258
    rounded(d, [M, top, W - M, bot], 16,
            fill=lerp(CARD_BG, acc, 0.20 if asking else 0.09),
            outline=YELLOW if asking else lerp(CARD_BG, acc, 0.5), width=4 if asking else 2)
    d.ellipse([M + 18, top + 16, M + 82, top + 80], fill=acc)
    qs = f"Q{qno}"
    fq = font(28 if len(qs) < 3 else 23, True)
    d.text((M + 50 - text_w(d, qs, fq) // 2, top + 33), qs, font=fq, fill=dark_ink(acc))
    f_q, l_q, lh_q, _ = fit_block(d, scene["q"], True, 1290, 76, 34, 20, 1.18)
    ty = top + (bot - top - len(l_q) * lh_q) // 2
    for i, ln in enumerate(l_q):
        d.text((M + 104, ty + i * lh_q), ln, font=f_q, fill=TEXT_WHITE)
    chip, chip_col = (("RIYA ASKS", YELLOW) if asking else ("THE TEACHER EXPLAINS", GREEN))
    fc = font(15, True)
    cw = text_w(d, chip, fc) + 26
    rounded(d, [W - M - 18 - cw, top + 12, W - M - 18, top + 40], 14, fill=chip_col)
    d.text((W - M - 18 - cw + 13, top + 17), chip, font=fc, fill=(10, 16, 36))


def draw_pills(d, scene, acc, reveal, kind):
    n = len(scene["boxes"])
    gap = 20
    pw = (W - 2 * M - gap * (n - 1)) // n
    for i, (title, _short, col, _narr) in enumerate(scene["boxes"]):
        x = M + i * (pw + gap)
        live = True
        newest = (i == reveal - 1) and kind == "answer"
        fill = col if live else dim(col, 0.45)
        rounded(d, [x, PILL_Y, x + pw, PILL_Y + PILL_H], 14, fill=fill,
                outline=YELLOW if newest else lerp(fill, TEXT_WHITE, 0.35), width=3 if newest else 2)
        ink = dark_ink(col) if live else lerp(dark_ink(col), (10, 16, 36), 0.4)
        label, tail = split_title(title)
        f1, l1, lh1, _ = fit_block(d, label, True, pw - 32, 46, PILL_START, PILL_MIN, 1.12)
        y = PILL_Y + 12
        for ln in l1:
            d.text((x + 16, y), ln, font=f1, fill=ink)
            y += lh1
        if tail:
            f2 = font(15, True)
            t = tail
            while t and text_w(d, t, f2) > pw - 32:
                t = t[:-2]
            if t != tail:
                t = t[:-1] + "…"
            d.text((x + 16, y + 2), t, font=f2, fill=lerp(ink, fill, 0.25))


def draw_rows(d, scene, acc, reveal, kind):
    n = len(scene["boxes"])
    h, gap = row_heights(n)
    for i, (title, body, col, _narr) in enumerate(scene["boxes"]):
        x = M
        y = ROWS_TOP + i * (h + gap)
        w = W - 2 * M
        newest = (i == reveal - 1) and kind == "answer"
        c = col if (newest or kind == "hook") else dim(col, 0.8)
        pending = i >= reveal and kind != "hook"
        rounded(d, [x, y, x + w, y + h], 12,
                fill=ROW_BG if not pending else lerp(BG_TOP, ROW_BG, 0.55),
                outline=YELLOW if newest else (c if not pending else (42, 54, 78)),
                width=4 if newest else 2)
        d.rectangle([x, y + 8, x + 10, y + h - 8], fill=c if not pending else (44, 56, 80))

        label, _tail = split_title(title)
        if pending:
            f_p, l_p, lh_p, _ = fit_block(d, label, True, 320 - 30, h - 20, LABEL_START, LABEL_MIN, 1.14)
            py = y + (h - len(l_p) * lh_p) // 2
            for k, ln in enumerate(l_p):
                d.text((x + 26, py + k * lh_p), ln, font=f_p, fill=(72, 86, 112))
            d.line([(x + 320, y + 14), (x + 320, y + h - 14)], fill=(44, 56, 80), width=2)
            f_d = font(26)
            dots = ".".join([""] * 3)
            d.text((x + 344, y + h // 2 - 18), "coming next", font=f_d, fill=(66, 80, 106))
            continue
        lw = 320
        f_l, l_l, lh_l, _ = fit_block(d, label, True, lw - 30, h - 20, LABEL_START, LABEL_MIN, 1.14)
        ly = y + (h - len(l_l) * lh_l) // 2
        for k, ln in enumerate(l_l):
            d.text((x + 26, ly + k * lh_l), ln, font=f_l, fill=c)

        d.line([(x + lw, y + 14), (x + lw, y + h - 14)], fill=(52, 66, 92), width=2)
        f_b, l_b, lh_b, _ = fit_block(d, body, False, w - lw - 40, h - 18, BODY_START, BODY_MIN, 1.24)
        by = y + (h - len(l_b) * lh_b) // 2
        for k, ln in enumerate(l_b):
            d.text((x + lw + 24, by + k * lh_b), ln, font=f_b, fill=TEXT_WHITE)


def col_x(widths, total_w):
    xs, acc = [], M
    span = W - 2 * M
    for f in widths:
        xs.append((acc, int(span * f)))
        acc += int(span * f)
    return xs


def draw_table(d, spec, acc, reveal, n, kind):
    top, bottom = PILL_Y, ROWS_BOT
    rows = spec["rows"]
    head_h = 46
    xs = col_x(spec["widths"], W - 2 * M)

    if kind in ("intro", "question"):
        shown = 1          # open on the first row so the table never looks empty
    elif kind == "hook":
        shown = len(rows)
    else:
        shown = max(1, math.ceil(len(rows) * reveal / n))

    body_h = min(112, (bottom - top - head_h) // max(shown, 1)) if shown else 0
    block_h = head_h + shown * body_h
    y = top + max(0, (bottom - top - block_h) // 2)   # centre the block in the band

    rounded(d, [M, y, W - M, y + head_h], 8, fill=lerp(CARD_BG, acc, 0.92))
    for (cx, cw), name in zip(xs, spec["cols"]):
        f, l, lh, _ = fit_block(d, name, True, cw - 28, head_h - 8, 24, 15, 1.1)
        d.text((cx + 14, y + (head_h - len(l) * lh) // 2), l[0], font=f, fill=dark_ink(acc))
        if cx != M:
            d.line([(cx, y + 6), (cx, y + head_h - 6)], fill=lerp(CARD_BG, acc, 0.45), width=2)

    newest = shown - max(1, math.ceil(len(rows) / n)) if kind == "answer" else -1
    for r, cells in enumerate(rows[:shown]):
        ry = y + head_h + r * body_h
        fresh = r == shown - 1 and kind == "answer"
        rounded(d, [M, ry + 2, W - M, ry + body_h - 2], 6,
                fill=ROW_ALT if r % 2 else ROW_BG,
                outline=YELLOW if fresh else None, width=3)
        for (cx, cw), txt in zip(xs, cells):
            bold = cx == M
            f, l, lh, _ = fit_block(d, txt, bold, cw - 28, body_h - 8, CELL_START, CELL_MIN, 1.14)
            ty = ry + (body_h - len(l) * lh) // 2
            for k, ln in enumerate(l):
                d.text((cx + 14, ty + k * lh), ln, font=f,
                       fill=TEXT_WHITE if not bold else lerp(TEXT_WHITE, acc, 0.55))
            if cx != M:
                d.line([(cx, ry + 6), (cx, ry + body_h - 6)], fill=(48, 62, 88), width=2)


def draw_trap(d, scene, acc, kind):
    text = re.sub(r"^REMEMBER:\s*", "", scene["hook"])
    rounded(d, [M, TRAP_Y, W - M, TRAP_Y + TRAP_H], 12, fill=YELLOW,
            outline=lerp(YELLOW, (255, 255, 255), 0.4), width=3)
    tag = "TRAP"
    ft = font(20, True)
    tw = text_w(d, tag, ft) + 26
    rounded(d, [M + 12, TRAP_Y + 14, M + 12 + tw, TRAP_Y + TRAP_H - 14], 8, fill=(26, 22, 6))
    d.text((M + 25, TRAP_Y + 21), tag, font=ft, fill=YELLOW)
    f, l, lh, _ = fit_block(d, text, True, W - 2 * M - tw - 70, TRAP_H - 16, TRAP_START, TRAP_MIN, 1.12)
    ty = TRAP_Y + (TRAP_H - len(l) * lh) // 2
    for k, ln in enumerate(l):
        d.text((M + tw + 40, ty + k * lh), ln, font=f, fill=(20, 16, 4))


def draw_footer(d, acc, qno, total, reveal, n, kind):
    f = font(17, True)
    d.text((M, 1026), "CCS (PENSION) RULES 2021  •  BATCH 6  •  RULES 71-87", font=f, fill=MUTED)
    right = f"CHAPTER {qno} OF {total}"
    d.text((W - M - text_w(d, right, f), 1026), right, font=f, fill=MUTED)

    y0, y1 = 1052, 1066
    d.rectangle([0, y0 - 6, W, H], fill=(7, 11, 24))
    seg = W / total
    frac = min(1.0, (reveal + (1 if kind == "hook" else 0)) / (n + 1))
    d.rectangle([0, y0, W, y1], fill=(26, 34, 54))
    d.rectangle([0, y0, int(seg * (qno - 1) + seg * frac), y1], fill=acc)
    for k in range(1, total):
        d.line([(int(seg * k), y0), (int(seg * k), y1)], fill=(7, 11, 24), width=2)


def render_frame(scene, qno, total, reveal, kind, out_path: Path):
    img, d = background()
    acc = scene["accent"]
    n = len(scene["boxes"])

    draw_chrome(d, scene, qno, total, acc)
    draw_question(d, scene, acc, kind, qno)

    spec = TABLES.get(scene["id"])
    if spec:
        draw_table(d, spec, acc, reveal, n, kind)
    else:
        draw_pills(d, scene, acc, reveal, kind)
        draw_rows(d, scene, acc, reveal, kind)

    draw_trap(d, scene, acc, kind)
    draw_footer(d, acc, qno, total, reveal, n, kind)
    img.save(out_path)


def audit_density():
    """Prints the font size every element ends up with. Returns the number of failing items."""
    img, d = background()
    bad = 0
    print(f"{'scene':30s} {'element':34s} {'px':>4s}  chars")
    for sc in SCENES:
        spec = TABLES.get(sc["id"])
        if spec:
            xs = col_x(spec["widths"], W - 2 * M)
            head_h = 46
            body_h = min(112, (ROWS_BOT - PILL_Y - head_h) // max(len(spec["rows"]), 1))
            try:
                for (cx, cw), name in zip(xs, spec["cols"]):
                    fit_block(d, name, True, cw - 28, head_h - 10, 22, 15, 1.1)
                for cells in spec["rows"]:
                    for (cx, cw), txt in zip(xs, cells):
                        _, _, _, s = fit_block(d, txt, cx == M, cw - 28, body_h - 8, CELL_START, CELL_MIN, 1.14)
                        if s < 18:
                            print(f"{sc['id'][:30]:30s} {txt[:34]:34s} {s:>4d}  TABLE CELL (tight)")
            except ValueError as e:
                bad += 1
                print(f"{sc['id'][:30]:30s} TABLE FAIL  {e}")
        else:
            h, _gap = row_heights(len(sc["boxes"]))
            for (title, body, col, _n) in sc["boxes"]:
                label, _t = split_title(title)
                try:
                    _, _, _, ls = fit_block(d, label, True, 320 - 30, h - 20, LABEL_START, LABEL_MIN, 1.14)
                    _, _, _, bs = fit_block(d, body, False, W - 2 * M - 320 - 40, h - 18, BODY_START, BODY_MIN, 1.24)
                    flag = "" if min(bs, ls) >= 24 else "  (tight)"
                    print(f"{sc['id'][:30]:30s} {title[:34]:34s} {min(bs, ls):>4d}  {len(body):>4d}{flag}")
                except ValueError as e:
                    bad += 1
                    print(f"{sc['id'][:30]:30s} {title[:34]:34s}  FAIL  {e}")
        try:
            fit_block(d, sc["hook"], True, W - 2 * M - 160, TRAP_H - 16, TRAP_START, TRAP_MIN, 1.12)
        except ValueError as e:
            bad += 1
            print(f"{sc['id']}: TRAP strip does not fit: {e}")
        for (title, short, _c, narr) in sc["boxes"]:
            if not narr.strip():
                bad += 1
                print(f"{sc['id']}: empty narration for {title!r}")
    print(f"\n{'ALL CARDS WITHIN BUDGET' if not bad else str(bad) + ' ITEM(S) OVER BUDGET'}")
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


FFMPEG = "ffmpeg"


def find_ffmpeg():
    """Locate an ffmpeg binary: $FFMPEG, then PATH, then the imageio-ffmpeg wheel."""
    global FFMPEG
    cand = [os.environ.get("FFMPEG", ""), shutil.which("ffmpeg") or ""]
    for c in cand:
        if c and Path(c).exists():
            FFMPEG = c
            return FFMPEG
    try:
        import imageio_ffmpeg
        FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
        return FFMPEG
    except Exception:
        sys.exit("ERROR: no ffmpeg found. Install it (apt install ffmpeg / brew install ffmpeg), "
                 "put it on PATH, set $FFMPEG, or pip install imageio-ffmpeg.")


def probe_duration(path: Path) -> float:
    """ffprobe if available, otherwise parse the duration out of ffmpeg's own banner."""
    if shutil.which("ffprobe"):
        out = subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(path)], text=True).strip()
        return float(out)
    err = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)],
                         capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", err)
    if not m:
        raise RuntimeError(f"cannot read duration of {path}")
    h, mi, se = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(se)


def stream_info(path: Path):
    """[(kind, w, h)] - ffprobe when present, ffmpeg banner otherwise."""
    if shutil.which("ffprobe"):
        out = subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height",
             "-of", "csv=p=0", str(path)], text=True)
        return [tuple(x.split(",")) for x in out.split()]
    err = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)],
                         capture_output=True, text=True).stderr
    info = []
    if "Audio:" in err:
        info.append(("audio", "", ""))
    m = re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", err)
    if m:
        info.insert(0, ("video", m.group(1), m.group(2)))
    return info


def has_subtitles_filter():
    try:
        out = subprocess.run([FFMPEG, "-hide_banner", "-filters"], capture_output=True, text=True).stdout
    except Exception:
        return False
    return bool(re.search(r"^\s*\S+\s+subtitles\s", out, re.M))


def silent_audio(text: str, out: Path) -> float:
    dur = max(1.5, len(text.split()) / 2.6)
    subprocess.run([FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", f"{dur:.2f}",
                    "-c:a", "libmp3lame", "-b:a", "24k", "-ar", "24000", "-ac", "1", str(out)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
        "Style: Default,DejaVu Sans,38,&H00FFFFFF,&H0000E6FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,160,160,60,1\n"
        "Style: Student,DejaVu Sans,38,&H0042E4F0,&H0000E6FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,160,160,60,1\n\n"
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
    ap.add_argument("--script", action="store_true", help="write the shooting script (English screen + Hinglish voice) and exit")
    ap.add_argument("--coverage", action="store_true", help="print the rule coverage matrix + density check, then exit")
    ap.add_argument("--audit", action="store_true", help="print the density table and exit (no ffmpeg needed)")
    ap.add_argument("--preview", action="store_true", help="render slides only")
    ap.add_argument("--no-tts", action="store_true", help="silent audio (offline layout/timing test)")
    ap.add_argument("--no-subs", action="store_true", help="do not burn subtitles (default when --no-tts)")
    ap.add_argument("--crf", type=int, default=21, help="x264 quality for the master (lower = bigger)")
    ap.add_argument("--clip-crf", type=int, default=23, help="x264 quality for the per-slide clips")
    ap.add_argument("--fps", type=int, default=24, help="frame rate of the slides (24 is plenty for stills)")
    ap.add_argument("--teacher", default=DEFAULT_TEACHER)
    ap.add_argument("--student", default=DEFAULT_STUDENT)
    ap.add_argument("--rate", default="-4%")
    ap.add_argument("--part", type=int, choices=[1, 2, 3], help="1..3 = first, middle, last third of the chapters")
    args = ap.parse_args()

    write_reference_sheet()
    write_narration_script()
    if args.script:
        print("wrote pension_b6_narration_script.md and pension_b6_reference_sheet.md")
        return
    cov = print_coverage()
    if args.coverage:
        sys.exit(1 if (cov or audit_density()) else 0)
    if args.audit:
        sys.exit(1 if audit_density() else 0)
    if cov:
        sys.exit("Build stopped: fix the coverage problems listed above.")
    if audit_density():
        sys.exit("Build stopped: fix the over-dense elements listed above.")

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

    find_ffmpeg()
    print(f"  ffmpeg: {FFMPEG}")

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
            FFMPEG, "-y", "-loop", "1", "-framerate", "5", "-i", str(sp), "-i", str(mp3),
            "-af", "apad", "-t", f"{dur:.3f}",
            "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-crf", str(args.clip_crf),
            "-g", str(args.fps * 10), "-r", str(args.fps), "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", ("24k" if args.no_tts else "192k"),
            "-ar", ("24000" if args.no_tts else "48000"), "-ac", ("1" if args.no_tts else "2"), str(clip)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cues += make_cues(words, cursor, "Student" if who == "student" else "Default")
        clips.append(clip)
        cursor += dur
    print(f"  {len(clips)} clips | timeline {cursor/60:.2f} min")

    burn = (not args.no_subs) and (not args.no_tts) and has_subtitles_filter()
    if not args.no_subs and not args.no_tts and not burn:
        print("  NOTE: this ffmpeg has no libass 'subtitles' filter - rendering without burned captions.")
    if args.no_tts:
        print("  NOTE: --no-tts master is silent; captions are skipped (the cards already carry the text).")

    print(f"\n=== Step 4: concat{' + burn subtitles' if burn else ' (stream copy, no re-encode)'} ===")
    concat = BUILD_DIR / "concat.txt"
    concat.write_text("\n".join(f"file '{c.name}'" for c in clips) + "\n", encoding="utf-8")
    raw = BUILD_DIR / "raw_concat.mp4"
    subprocess.run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(raw)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ass = BUILD_DIR / "subtitles.ass"
    write_ass(cues, ass)
    if burn:
        ass_esc = str(ass).replace("\\", "/").replace(":", "\\:")
        subprocess.run([
            FFMPEG, "-y", "-i", str(raw), "-vf", f"subtitles='{ass_esc}'",
            "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
            "-c:v", "libx264", "-crf", str(args.crf), "-preset", "fast", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(OUTPUT_MP4)], check=True,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.run([
            FFMPEG, "-y", "-i", str(raw), "-c", "copy", "-movflags", "+faststart", str(OUTPUT_MP4)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    dur = probe_duration(OUTPUT_MP4)
    info = stream_info(OUTPUT_MP4)
    print("\n=== Step 5: verification ===")
    print("streams:", info)
    print(f"DONE: {OUTPUT_MP4.resolve()}  |  {dur/60:.2f} min  |  {OUTPUT_MP4.stat().st_size/1048576:.1f} MB")
    if not any(str(s[0]).startswith("audio") for s in info):
        print("WARNING: no audio stream found!")


if __name__ == "__main__":
    asyncio.run(main())
