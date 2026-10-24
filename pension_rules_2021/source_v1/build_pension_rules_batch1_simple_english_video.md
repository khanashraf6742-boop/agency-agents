# CCS (Pension) Rules 2021 - Batch 1 - Rules 1-10: Preliminary and Classification of Claims - Simple English Video Compiler (Python script)

Scope: Batch 1: Rules 1 to 10 (Chapters I and II) of the CCS (Pension) Rules, 2021, plus the four amendments, related O.M.s and dynamic figures (DR, minimum pension) as of 21.10.2026. Explanation only; recap chapter at the end.

Save the code block as `build_pension_b1.py` and run it as described in its docstring.

````python
#!/usr/bin/env python3
"""
CCS (Pension) Rules 2021 - Batch 1 - Rules 1-10: Preliminary and Classification of Claims
SIMPLE ENGLISH Q&A EXPLANATION MASTERCLASS COMPILER - 32 chapters. Scope: Batch 1: Rules 1 to 10 (Chapters I and II) of the CCS (Pension) Rules, 2021, plus the four amendments, related O.M.s and dynamic figures (DR, minimum pension) as of 21.10.2026. Explanation only; recap chapter at the end.
=====================================================================================================
SOURCES READ / CHECKED IN THIS BUILD:
  * https://www.staffnews.in/wp-content/uploads/2021/12/CSS_PensionRules_2021_Book_Eng.pdf
  * https://betadgs.dgshipping.gov.in/download/1753360910_68822a0e96fd1_pension-rules.pdf
  * https://cdn.taxguru.in/wp-content/uploads/2022/01/Central-Civil-Services-Pension-Rules-2021.pdf
  * https://seepz.gov.in/uploads/175027136568530585800c8_CSS Pension Rules 2021_compressed.pdf
  * https://www.staffnews.in/2022/10/central-civil-services-pension-amendment-rules-2022-in-rule-8.html
  * https://www.staffnews.in/2023/04/amendment-of-rule-8-of-ccs-pension-rules-2021.html
  * https://www.staffnews.in/2024/07/central-civil-services-pension-amendment-rules-2024.html
  * https://www.staffnews.in/2024/09/nomination-for-arrears-of-pension-and-commutation-of-pension.html
  * https://www.staffnews.in/2025/05/central-civil-services-pension-amendment-rules-2025.html
  * https://www.staffnews.in/2025/11/claims-to-pension-or-family-pension-under-ccs-pension-rules.html
  * https://www.staffnews.in/2025/11/employment-after-retirement-under-a-government.html
  * https://www.staffnews.in/2025/11/services-in-autonomous-bodies-under-the-ccs-pension-rules.html
  * https://www.staffnews.in/2026/06/consideration-of-crucial-date-for-compassionate-appointments-for-ops.html
  * https://www.taxheal.com/wp-content/uploads/2026/09/276041.pdf
  * https://www.gconnect.in/orders-in-brief/pension/ccs-pension-rules-2021-pension-family-pension-clarification.html
  * https://www.careerindia.com/news/july-2026-da-hike-status-latest-update-for-central-government-employees-011-67233.html
  * https://www.epfindia.gov.in/site_docs/PDFs/Circulars/Y2026-2027/Circular_DAEnhancement_Pensioners29042026.pdf
  * Ledger file ledger/B1_verified.json (all URLs listed in its urls_read)
CHANGES VERSUS THE SOURCE (outdated / superseded / corrected):
  * Rule 8(2)(a) proviso: source says proceedings by a subordinate authority are deemed initiated by the appointing authority; current is that the subordinate authority submits a report of findings to the competent authority; evidence staffnews 2022/10 and 2023/04 summaries, dgshipping copy
  * Rule 4 sub-rules 2 and 3: source says a claims processing frame; current is that the election is in writing to the authority that issued the transfer order and is final; numbering to be confirmed
  * Rule 5(2) proviso: source calls the leave, absence, suspension line new in the 30.10.2025 O.M.; current is that it is already in the Rule and the O.M. restates it; evidence staffnews 2025/11 and gconnect
  * Rule 6 Explanations: source gave no content; current is deemed proper permission (Expl 1) and pension for body or PSU service paid by that body (Expl 2); evidence dgshipping copy
  * Rule 7: source omitted sub-rules 4 and 5 (Second Schedule RTI organisations, Format 1 undertaking), the Explanation definitions; ADD-B1-3 President limb not found; President appears in 7(6) and 7(7) only
  * Format 1: source says commercial employment application; current is the Rule 7(4)(b) undertaking; commercial employment uses Form 1 and Form 2; evidence forms copy at taxguru
  * G.S.R. 410(E): source lists nine merged forms including Format 1 and says Rule 63(4) was the only replaced clause; current is that only Forms 6 and A are confirmed merged and many rules and forms were amended; evidence staffnews 2024/07 and 2024/09
  * G.S.R. 770(E): source says six changes; current is at least ten (also Rule 8(2)(c), 8(4)(d), 8(6), 50(9)(h)); wording of the four not read
  * Amendment count: source says three; a fourth, G.S.R. 775(E) of September 2026 (new proviso under Rule 37(7)), exists; evidence taxheal PDF
  * Rule 9 and 10: source presents the Transaction of Business Rules 1961 line as new for Rule 10 and as a contrast with Rule 9; Rule 9(4) says the same; the 30.10.2025 O.M. restates Rule 10(2)
  * Rule 9(1) first proviso: source adds refused leave; not found in text read
  * Rule 3(1)(q) Head of Office: source says only declaration counts; definition also allows another person specified by the competent authority
  * Rules 8(2)(c) four years, 8(3)-(5) provisional pension, 8(6) one-third, 8(7)-(8), Explanations: omitted by source, added from the rules copy
  * Currency: source dates (30.07.2026 and 12.09.2026) not confirmed; this check 21.10.2026
KEY FACTS:
  * Base notification G.S.R. 868(E) of 20.12.2021; in force on Gazette publication
  * Cut-off 31.12.2003; 8 exclusions (a) to (h); 6 Explanations; 26 definitions (a) to (z)
  * O.M. 22.06.2026 No. 57/05/2021-P&PW(B)/Compassionate/10593: date of application is the crucial date for compassionate appointments
  * Rule 4 option: 6 months from the transfer order or return from leave, whichever is later; in writing; final
  * Rule 7(3) reply in 15 days plus up to 15; Rule 9(7) representation in 30 days; Rule 9 window 1 year; Rule 10 no time limit
  * Rule 8(1) authority is decided by the post's appointing authority: President, Secretary, or C&AG; no appeal against the President's order (8(6A))
  * Rule 8(2)(c) no event older than 4 years; Rule 8(6) recovery not ordinarily above one-third
  * Amendments: 770(E) of 07.10.2022, 410(E) of 16.07.2024 (Form 6-A for retirees from 16.11.2024), 340(E) of 22.05.2025, 775(E) of September 2026
  * DR 60% w.e.f. 01.01.2026 (DoE O.M. of 22.04.2026); July 2026 revision not announced as of 17.10.2026; check the latest O.M.
  * Minimum pension floor reported Rs 9,000 a month (secondary source); check the latest O.M.
NOT VERIFIED (flagged on the cards - quote the official text in an answer sheet):
  * Gazette text of the Rules and of all amendments: not read verbatim; wording is a close restatement from secondary summaries
  * Rule 87 repeal of the 1972 Rules and saving of pending cases: Rule 87 not read in this batch
  * NPS Rules Rule 10 option and narrowness of the Explanation 5 gateway: NPS rules not read
  * Rule 4 sub-rule numbering: found in only one PDF summary
  * Exact Gazette publication date of G.S.R. 410(E): 120 days from 16.07.2024 ends 13.11.2024, so 16.11.2024 rests on a secondary source
  * G.S.R. 340(E) publication on 23.05.2025: one press source only
  * G.S.R. 775(E) exact date: garbled in the file read
  * CSIR order of 07.07.2026 and the no blanket order remark for autonomous bodies: not found
  * 13 Forms and 13 Formats, 87 rules and 14 chapters counts: not checked in this batch
  * CCS (Extraordinary Pension) Rules 2023, NPS gratuity amendment 2025, UPS Rules 2025: not searched
  * Minimum pension Rs 9,000: Rule 44 not read; secondary source only
  * Any DoPPW amendment or O.M. after 22.06.2026 touching Rules 1 to 10: none found, but doppw.gov.in, egazette and India Code were unreadable and pensionersportal is blocked, so absence is not proven
  * Content of Rules 19 and 20 previewed from the source only; verified in Batch 2
Usage
    python build_pension_b1.py --audit      # density check only (no ffmpeg / internet)
    python build_pension_b1.py --preview    # slides only
    python build_pension_b1.py --no-tts     # silent dry run
    python build_pension_b1.py --part 1     # one third of the chapters (1, 2 or 3)
    python build_pension_b1.py              # full build (needs internet for edge-tts; ffmpeg+ffprobe with libass on PATH)
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
BUILD_DIR = Path("pension_b1_build")
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
OUT_STEM = "pension_b1_masterclass"
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
        "id": "c1_01_rule1",
        "chapter": "CHAPTER 1 • RULE 1: NAME AND START DATE",
        "title": "RULE 1 — THE NAME, THE START DATE AND THE BASE NOTIFICATION",
        "accent": RED, "badge": "RULE 1",
        "q": "What are these rules called, and from which date do they apply?",
        "intro": ("Welcome! In this series we study the Central Civil Services (Pension) Rules, 2021, one rule at a time, in simple English. "
                  "Riya asks the questions and I answer, card by card. This is batch one: Rules one to ten, which make up Chapter one and Chapter two. "
                  "Let us hear Riya's first question."),
        "q_say": "Sir, what are these rules called, and from which date do they apply?",
        "boxes": [
            ("THE NAME • RULE 1(1)",
             "Short title: Central Civil Services (Pension) Rules, 2021 — often written CCS (Pension) Rules, 2021.",
             "Rule 1(1): the rules are called the Central Civil Services (Pension) Rules, 2021. Short title confirmed (close restatement from a page-summarising tool, not read verbatim from the Gazette).",
             RED,
             "Let us take the rule first. Rule one, sub-rule one, gives the name: the Central Civil Services (Pension) Rules, two thousand twenty-one. Pension here simply means the monthly money a government servant gets after retiring."),
            ("THE START DATE • RULE 1(2)",
             "In force from the day they were published in the Official Gazette. No separate 'appointed day'.",
             "Rule 1(2): the rules come into force on the date of their publication in the Official Gazette. The Gazette is the government's official printed notice. Confirmed (close restatement).",
             ORANGE,
             "Rule one, sub-rule two, says the rules start on the day they were published in the Official Gazette. The Gazette is the government's official printed notice. So there is no later appointed day to wait for."),
            ("THE BASE NOTIFICATION",
             "G.S.R. 868(E), dated 20 December 2021, of the Department of Pension and Pensioners' Welfare (DoPPW).",
             "Base notification: G.S.R. 868(E) dated 20.12.2021, Ministry of Personnel, Public Grievances and Pensions (Department of Pension and Pensioners' Welfare). The number and date are also recited in the preambles of the later amending notifications. Confirmed.",
             BLUE,
             "The base notification is G.S.R. eight six eight E, dated twenty December two thousand twenty-one. G.S.R. is the serial number the Gazette gives to a rule notification. Later amendments repeat this number in their opening lines, so it is safe to quote."),
            ("OLD RULES • NOT YET CONFIRMED",
             "These rules replaced the CCS (Pension) Rules, 1972 (repeal in Rule 87). UNVERIFIED: Rule 87 not read yet.",
             "UNVERIFIED (not confirmed against an official source in this batch): the script says the 2021 Rules replaced the CCS (Pension) Rules, 1972, with the repeal and saving in Rule 87; for pre-commencement retirees the script says the 1972 Rules still decide the case and earlier actions are treated as valid (Rule 87(2)(c)). Rule 87 will be checked in the batch on Rules 71 to 87 (Batch 6). The script's reasons for new rules (one consolidated instrument instead of scattered orders, the online system Bhavishya, the NPS after 31.12.2003) are the script author's commentary, not quoted rule text.",
             GREEN,
             "Now a flagged point. The script says these rules replaced the nineteen seventy-two rules, and that people who retired before the start still stay under the old rules. That sits in Rule eighty-seven, which we have not yet checked against an official source, so treat it as unconfirmed for now."),
        ],
        "hook": "REMEMBER: CCS (Pension) Rules 2021 • in force on Gazette publication • G.S.R. 868(E) of 20.12.2021!",
        "hook_say": "Remember: the name is CCS Pension Rules 2021, they began on the day of Gazette publication, and the base notification is G.S.R. 868 E of twenty December 2021.",
        "covers": ["R1(1)", "R1(2)", "GSR-868E", "R1-REPEAL1972", "BONUS-1-WHY", "BONUS-1-R87-2c"],
    },
    {
        "id": "c1_02_rule2_main",
        "chapter": "CHAPTER 2 • RULE 2: WHO IS COVERED AND WHO IS LEFT OUT",
        "title": "RULE 2 — WHO IS COVERED, AND THE EIGHT EXCLUSIONS",
        "accent": ORANGE, "badge": "RULE 2",
        "q": "Whom do these rules apply to, and which eight groups are left out?",
        "q_say": "Sir, whom do these rules apply to, and who is left out?",
        "boxes": [
            ("THE MAIN RULE",
             "Covers Government servants appointed on or before 31.12.2003, in substantive posts on pensionable establishments.",
             "Rule 2 (main text): the rules apply to Government servants appointed on or before 31.12.2003, including civilian Government servants in the Defence Services, who hold a substantive appointment on a pensionable establishment under the Union. 'Substantive' means a regular, permanent appointment; 'pensionable establishment' means a post that carries pension. Confirmed in substance (close restatement; not read verbatim from the Gazette).",
             SKY,
             "Let us take the rule first. These rules cover Government servants who were appointed on or before thirty-one December two thousand three. That includes civilians working in the Defence Services. The appointment must be substantive, which means regular, and on a post that carries a pension."),
            ("EXCLUSIONS (a) TO (d)",
             "Left out: (a) railway servants; (b) casual and daily rated staff; (c) staff paid from contingencies; (d) CPF beneficiaries.",
             "Rule 2 exclusions: (a) railway servants; (b) casual and daily rated employees; (c) persons paid from contingencies (a contingency is an office running-cost budget, not a regular pay scale); (d) persons entitled to Contributory Provident Fund benefits. Confirmed (close restatement).",
             BLUE,
             "Now the exclusions. There are eight. Clause a is railway servants. Clause b is casual and daily rated staff. Clause c is people paid out of contingencies. Clause d is those who get Contributory Provident Fund benefits."),
            ("EXCLUSIONS (e) TO (h)",
             "(e) All India Services; (f) locally hired staff abroad; (g) contract staff unless the contract says otherwise; (h) staff governed by the Constitution or another law.",
             "Rule 2 exclusions continued: (e) members of the All India Services; (f) locally recruited persons in Indian diplomatic, consular or other establishments abroad; (g) persons employed on contract, unless the contract provides otherwise; (h) persons whose conditions of service are governed by the Constitution or other law. Eight exclusions in all, (a) to (h): count confirmed. 'The list is closed' is the script author's inference, not rule text.",
             GREEN,
             "Clause e is the All India Services. Clause f is people hired locally for Indian missions abroad. Clause g is contract staff, with one small door: if the contract itself says pension rules apply, they come in. Clause h is people whose service terms come from the Constitution or another law."),
            ("EXAMPLE AND TRAP",
             "Example: Bilal, a railway technician, is out under Rule 2(a). Trap: contract staff are out unless the contract says otherwise.",
             "Example (invented): Bilal is a technician on the railways. He asks which pension rules apply. Rule 2(a) leaves railway servants out, so the CCS (Pension) Rules, 2021 do not apply to him; railway rules do. Charu is on a contract that says pension rules apply to her; Rule 2(g) lets her in. Dev is on a contract that is silent; he stays out. Script's rule of thumb: treat the list of eight as closed, do not add classes by guesswork (author's inference).",
             RED,
             "Here is a real example. Bilal is a railway technician. Clause a leaves him out, so he follows the railway rules, not these. Be careful, this is the trap: contract staff are out unless the contract itself brings them in. Charu's contract says pension rules apply, so she is in; Dev's contract is silent, so he is out."),
        ],
        "hook": "REMEMBER: appointed on or before 31.12.2003 • eight exclusions (a) to (h) • contract staff out unless the contract says so!",
        "hook_say": "Remember: appointed on or before thirty-one December two thousand three, eight exclusions a to h, and contract staff are out unless the contract says otherwise.",
        "covers": ["R2-MAIN", "R2-DEFENCE", "R2(a)", "R2(b)", "R2(c)", "R2(d)", "R2(e)", "R2(f)", "R2(g)", "R2(h)", "R2-EXCL-COUNT"],
    },
    {
        "id": "c1_03_cpf_ais_nps",
        "chapter": "CHAPTER 3 • RULE 2(d) AND 2(e): CPF, AIS AND NPS COMPARED",
        "title": "RULE 2(d) AND 2(e) — WHY CPF AND ALL INDIA SERVICES ARE LEFT OUT",
        "accent": SKY, "badge": "RULE 2(d) • 2(e)",
        "q": "CPF holders and All India Services officers are both out. Is the reason the same?",
        "q_say": "Sir, CPF holders and All India Services officers are both left out. Is the reason the same?",
        "boxes": [
            ("CPF: A FUND, NOT PENSION",
             "CPF is a Contributory Provident Fund: employee and Government both pay in, and a lump sum comes out.",
             "Exclusion (d) is confirmed. The reasons given in the script (the retirement benefit comes from a contributory fund, not from the Consolidated Fund) are the script author's commentary, not checked against an official source. Plain meaning of the terms: a provident fund is a savings pot built from contributions; a pension is a regular monthly payment.",
             SKY,
             "Let us start with clause d. The Contributory Provident Fund is a savings pot. The employee and the Government both put money in, and a lump sum comes out at the end. That is different from a monthly pension. The reason I am giving is explanation, not quoted rule text."),
            ("NPS: ANOTHER PATH",
             "NPS staff, appointed after 2003, follow separate NPS rules. UNVERIFIED: the NPS rules title was not checked.",
             "UNVERIFIED commentary (BONUS-2): the script says NPS employees are governed by the CCS (Implementation of National Pension System) Rules, 2021, with a special gateway to Rules 39 and 50 through Explanation 5 of Rule 2. The exclusion list was confirmed; the NPS rules title, and the reasons, were not checked. NPS means National Pension System, where a staff member and the Government pay into an account during service.",
             BLUE,
             "People appointed after two thousand three mostly go to the National Pension System, where money is saved during service. The script names a separate set of NPS rules for them, but we have not checked that title, so it is flagged. A narrow door back to these rules exists in Explanation five, which we meet shortly."),
            ("ALL INDIA SERVICES",
             "IAS, IPS and Indian Forest Service have their own pension framework, so Rule 2(e) leaves them out.",
             "Exclusion (e): members of the All India Services. The script says these are IAS, IPS and Indian Forest Service, with a separate AIS pension framework. The exclusion is confirmed; the explanation of why is the script author's commentary, not checked.",
             GREEN,
             "Clause e is different. The All India Services, meaning the IAS, the IPS and the Indian Forest Service, have their own pension framework. So the reason for leaving them out is a separate framework, not a provident fund."),
            ("THE TRAP",
             "An IAS officer is out; a Central Secretariat Service Under Secretary is covered. Not every senior officer is All India Service.",
             "Script's trap (commentary, not checked against an official source): 'member of the All India Services' is not the same as 'Group A officer of a Central Civil Service'. Example (from the script): an IAS officer of the AGMUT cadre is an AIS member and is out; an Under Secretary of the Central Secretariat Service is a Central Civil Service officer and these rules apply.",
             RED,
             "Be careful, this is the trap. Being a senior officer does not make someone an All India Services member. In the script's example, an IAS officer is out, while an Under Secretary of the Central Secretariat Service is covered. Remember this is the script's commentary and is flagged as unchecked."),
        ],
        "hook": "REMEMBER: CPF = savings pot • AIS = own framework • senior officer does not mean AIS member!",
        "hook_say": "Remember: CPF is a savings pot, the All India Services have their own framework, and a senior officer is not automatically an All India Services member.",
        "covers": ["BONUS-2-CPF"],
    },
    {
        "id": "c1_04_expl_1to3",
        "chapter": "CHAPTER 4 • RULE 2: EXPLANATIONS 1 TO 3",
        "title": "RULE 2 — EXPLANATIONS 1 TO 3: WHO ELSE IS BROUGHT IN",
        "accent": GREEN, "badge": "RULE 2 • EXPL 1-3",
        "q": "Some people were appointed after 2003 but still seem covered. What do Explanations 1 to 3 say?",
        "q_say": "Sir, what do the first three Explanations of Rule 2 say?",
        "boxes": [
            ("EXPLANATION 1: TRAINING",
             "Induction training on or before 31.12.2003, then regular appointment: covered if training was compulsory, paid, and counted under the 1972 Rules.",
             "Explanation 1 (close restatement): the rules also apply to a servant who was on induction training on or before 31.12.2003 and was then regularly appointed, if (i) completing the training was an essential condition of the regular appointment, (ii) a salary or stipend was paid during training, and (iii) the training period was countable as qualifying service under the 1972 Rules. Qualifying service means service that counts when pension is worked out. Confirmed in substance.",
             GREEN,
             "Explanation one is about training. Induction training means the first training a new recruit takes. If someone was in it on or before thirty-one December two thousand three and was later regularly appointed, three conditions apply. Training was compulsory for the job, pay or a stipend was given, and the 1972 Rules counted that period as qualifying service."),
            ("EXPLANATION 2: OTHER SCHEMES",
             "Appointed by 31.12.2003 under another pension scheme (or a State or autonomous body with a similar scheme), then moved to a covered Central post.",
             "Explanation 2 (close restatement): applies to a person first appointed on or before 31.12.2003 in a Central establishment under a pension scheme other than the 1972 Rules, or in a State Government or autonomous body with a similar non-contributory scheme, and later appointed to a covered Central establishment, subject to the other conditions being met. Confirmed in substance; exact wording not read verbatim.",
             SKY,
             "Explanation two covers someone who started before the cut-off date under a different pension scheme, such as a State government job with a similar non-contributory scheme, and later joined a covered Central post. Non-contributory means the employee did not pay into it. The other conditions must still be met."),
            ("EXPLANATION 3: SPECIAL ORDERS",
             "Appointed after 31.12.2003 but meets the conditions of a special or general Government order that brings them in.",
             "Explanation 3 (close restatement): applies to a person appointed after 31.12.2003 who fulfils the coverage conditions laid down in a special or general order of the Government. Confirmed in substance. A recent example of such an order is the O.M. of 22.06.2026 on compassionate appointments, explained in chapter 7 of this batch.",
             ORANGE,
             "Explanation three is a catch-all. Someone appointed after the cut-off date can still be covered if a special or general government order says so and they meet its conditions. A very recent example is the June two thousand twenty-six memorandum, which we study in a later chapter."),
            ("EXAMPLE AND LOOK-ALIKE",
             "Example: Charu, induction trainee in 2002 with stipend, regular in 2004: covered. Look-alike: these Explanations extend coverage; they do not backdate the appointment.",
             "Example (invented): Charu joined induction training in 2002, completion of which was a condition of regular appointment; she received a stipend; the 1972 Rules counted that period. She was regularly appointed in 2004, after the cut-off, but Explanation 1 brings her in, and her training period counts as qualifying service. Look-alike: the Explanations read 'these rules shall also apply to'; they do not say the person is 'deemed appointed' on or before 31.12.2003. This reading is the script author's interpretation: reasonable but not an official statement (R2-EXPL-FORMAT, unverified).",
             RED,
             "Here is a real example. Charu was an induction trainee in two thousand two, with a stipend, and became regular in two thousand four. All three conditions are met, so she is covered and her training counts. Be careful with the look-alike: the Explanations extend coverage, they do not pretend she was appointed before the cut-off. That reading is our interpretation, flagged as unofficial."),
        ],
        "hook": "REMEMBER: Explanations 1-3 = training, other schemes, special orders — they extend coverage, they do not backdate!",
        "hook_say": "Remember: Explanations one to three cover training, other schemes and special orders. They extend coverage, they do not backdate the appointment.",
        "covers": ["R2-EXPL1", "R2-EXPL2", "R2-EXPL3", "R2-EXPL-FORMAT"],
    },
    {
        "id": "c1_05_expl_4to6",
        "chapter": "CHAPTER 5 • RULE 2: EXPLANATIONS 4 TO 6 AND THE COUNTS",
        "title": "RULE 2 — EXPLANATIONS 4 TO 6, AND THE COUNTS TO REMEMBER",
        "accent": PINK, "badge": "RULE 2 • EXPL 4-6",
        "q": "What do Explanations 4, 5 and 6 add, and how many things must I count?",
        "q_say": "Sir, what do Explanations four, five and six add, and what should I count?",
        "boxes": [
            ("EXPLANATION 4: TEMPORARY STATUS",
             "Temporary status under the 1993 casual labourers scheme by 31.12.2003, then regular: covered, but Rule 15 halves the service.",
             "Explanation 4 (close restatement): applies to a person granted temporary status under the Casual Labourers (Grant of Temporary Status and Regularisation) Scheme, 1993 on or before 31.12.2003 and then regularly appointed without a break, subject to Rule 15 (only half of the temporary-status service counts). The detail of Rule 15 is in the next batch. Confirmed in substance.",
             PINK,
             "Explanation four is for casual labourers who got temporary status under the nineteen ninety-three scheme by the cut-off date and were then regularised without a break. They are covered, but Rule fifteen applies, so only half of that earlier service counts. Rule fifteen comes in the next batch."),
            ("EXPLANATION 5: NPS GATEWAY",
             "A narrow door for NPS-covered staff on death or invalidation. Full card in the next chapter.",
             "Explanation 5 (close restatement): an NPS-covered servant appointed after 31.12.2003 can get Invalid Pension (Rule 39) and Family Pension (Rule 50) on death or discharge on invalidation, if the option (or default) is as described. Discussed fully in chapter 6 of this batch. Confirmed in substance.",
             BLUE,
             "Explanation five is the narrow NPS door. It links to Rule thirty-nine on invalid pension and Rule fifty on family pension. I will give it a full chapter of its own next, because it is a favourite exam trap."),
            ("EXPLANATION 6: TEMPORARY STAFF",
             "Temporary appointee by 31.12.2003 who retires before a substantive post gets only what the CCS (Temporary Service) Rules, 1965 allow.",
             "Explanation 6 (close restatement): a person appointed in a temporary capacity on or before 31.12.2003 who retires before being substantively appointed gets benefits only to the extent provided in the CCS (Temporary Service) Rules, 1965. Confirmed in substance; not read verbatim.",
             ORANGE,
             "Explanation six covers a temporary appointee who retires before ever getting a substantive post. Such a person gets benefits only as far as the Temporary Service Rules of nineteen sixty-five allow, not the full benefits of these rules."),
            ("COUNT AND TRAP",
             "Count: 8 exclusions, 6 Explanations. Trap: each Explanation adds a class; none removes one.",
             "Counts confirmed: eight exclusions, (a) to (h); six Explanations. Trap (script's study aid, interpretation): Explanations 1 to 6 bring people in or limit their benefits; the exclusions are separate from them. Exam habit: keep the three questions apart: (1) is the person in the main text, (2) does an exclusion apply, (3) does an Explanation bring them back.",
             RED,
             "Count two things: eight exclusions and six Explanations. Be careful, this is the trap: do not mix them up. Ask three questions in order. Is the person in the main text? Does an exclusion apply? Does an Explanation bring them back?"),
        ],
        "hook": "REMEMBER: 8 exclusions • 6 Explanations • Expl 4 halves service via Rule 15 • Expl 6 = Temporary Service Rules 1965!",
        "hook_say": "Remember: eight exclusions, six Explanations, Explanation four halves service through Rule fifteen, and Explanation six points to the Temporary Service Rules of nineteen sixty-five.",
        "covers": ["R2-EXPL4", "R2-EXPL5", "R2-EXPL6", "R2-EXPL-COUNT"],
    },
    {
        "id": "c1_06_expl5_nps",
        "chapter": "CHAPTER 6 • RULE 2, EXPLANATION 5: THE NPS GATEWAY",
        "title": "EXPLANATION 5 — HOW AN NPS EMPLOYEE REACHES RULES 39 AND 50",
        "accent": BLUE, "badge": "RULE 2 • EXPL 5",
        "q": "NPS employees are outside these rules. So how does Explanation 5 let them in?",
        "q_say": "Sir, NPS employees are outside these rules, so how does Explanation five let them in?",
        "boxes": [
            ("THE DOOR",
             "NPS-covered staff appointed after 31.12.2003 can get Invalid Pension (Rule 39) and Family Pension (Rule 50).",
             "Explanation 5 (close restatement): for a Government servant appointed after 31.12.2003 and covered by the NPS under the CCS (NPS) Rules, 2021, the Invalid Pension of Rule 39 and the Family Pension of Rule 50 are payable on death or on discharge on invalidation, on the stated option or default. Rule 2 Explanation 5 is confirmed in substance; wording not read verbatim.",
             BLUE,
             "Let us take the rule first. A person appointed after two thousand three and covered by the National Pension System would normally be outside these rules. Explanation five opens a narrow door: if the person dies, or is discharged because of invalidity, Rule thirty-nine on invalid pension and Rule fifty on family pension can apply."),
            ("THE CONDITION • UNVERIFIED",
             "Needs an option under Rule 10 of the NPS Rules, or a default option for these rules or the 1972 Rules. Rule 10 not confirmed.",
             "UNVERIFIED (R2-EXPL5-OPTION): the script says the person must have exercised an option under Rule 10 of the NPS Rules to this effect, or the default option is for the benefits of these rules or the 1972 Rules. The reference to Rule 10 of the NPS Rules was not read in the NPS rules themselves. Invalid pension is the pension paid when a servant is discharged because of ill health; family pension is the monthly pension paid to the family after a death. Both are covered in later batches.",
             SKY,
             "Now the condition. The script says the person must have chosen this option under Rule ten of the NPS Rules, or the default option must lead to these rules. We could not confirm that Rule ten reference in the NPS rules, so it is flagged as not confirmed."),
            ("THE LIMIT",
             "Only for death or invalidation. On normal superannuation (retiring at the usual age) the NPS employee gets NPS benefits.",
             "Limit (script's reading of Explanation 5; the narrowness of the gateway is part of the unverified item R2-EXPL5-OPTION): the gateway covers death and discharge on invalidation only; on ordinary superannuation retirement an NPS employee receives NPS benefits and these rules do not apply. Later instruments (CCS (Payment of Gratuity under NPS) Amendment Rules 2025 and the CCS (Implementation of the Unified Pension Scheme under NPS) Rules 2025) are separate and are covered in chapter 31 of this batch.",
             GREEN,
             "Here is the limit. The door opens only for death or discharge on invalidity. If an NPS employee simply retires at the usual age, the NPS benefits apply and these rules do not. Newer NPS and Unified Pension Scheme instruments are separate, and we note them in a later chapter."),
            ("EXAMPLE AND TRAP",
             "Example: Esha, joined 2008 under NPS, dies in service; with the right option her family looks to Rule 50. Trap: not for ordinary retirement.",
             "Example (invented): Esha joined in 2008 and is covered by the NPS. She dies in service. If the option or default described above applies, her family can claim Family Pension under Rule 50 of these rules. Her colleague Dev, also NPS, retires normally at the usual age: he gets NPS benefits, not this gateway. Trap: reading the gateway as covering every NPS employee. Confirmation of the option rule is pending (unverified).",
             RED,
             "Here is a real example. Esha joined in two thousand eight under the NPS and dies in service. If the option condition is met, her family can look to Rule fifty. Her colleague Dev retires normally, so he gets NPS benefits only. The trap is thinking the gateway covers every NPS employee; it does not."),
        ],
        "hook": "REMEMBER: NPS gateway = death or invalidation only, to Rules 39 and 50 — not for normal retirement!",
        "hook_say": "Remember: the NPS gateway is for death or invalidation only, leading to Rules thirty-nine and fifty, never for normal retirement.",
        "covers": ["R2-EXPL5", "R2-EXPL5-OPTION"],
    },
    {
        "id": "c1_07_om_2026_compassionate",
        "chapter": "CHAPTER 7 • RULE 2 AND THE 31.12.2003 CUT-OFF: O.M. OF 22.06.2026",
        "title": "RULE 2 CUT-OFF — THE 22.06.2026 O.M. ON COMPASSIONATE APPOINTMENTS",
        "accent": ORANGE, "badge": "O.M. 22.06.2026",
        "q": "Does a compassionate appointee who joined after 2003 but applied before it get these rules?",
        "q_say": "Sir, a compassionate appointee applied before the cut-off but joined after it. Which pension rules apply?",
        "boxes": [
            ("THE O.M.",
             "DoPPW Office Memorandum of 22.06.2026 (No. 57/05/2021, file ending 10593) on the crucial date for compassionate appointments.",
             "DoPPW Office Memorandum No. 57/05/2021-P&PW(B)/Compassionate/10593 dated 22.06.2026, subject: Consideration of crucial date for compassionate appointments for inclusion under the CCS (Pension) Rules. Confirmed from press text of the O.M.; the full O.M. PDF was not read, so this is a close restatement. Applies to all Ministries and Departments; the C&AG was consulted for the Indian Audit and Accounts Department under Article 148(5). Compassionate appointment means a job given to a family member of a government servant who died or became unfit in service, to help the family.",
             ORANGE,
             "This is a very fresh order. It is Office Memorandum number fifty-seven slash oh-five slash two thousand twenty-one, dated twenty-two June two thousand twenty-six, from the Department of Pension and Pensioners' Welfare. It deals with compassionate appointments, which are jobs given to a family member of an employee who died or became unfit in service."),
            ("THE DECISION",
             "The DATE OF APPLICATION is the crucial date, not the joining date, if the applicant was eligible then.",
             "Decision (close restatement): for compassionate appointment the date of application is the crucial date, provided the applicant was eligible for appointment at the time of application. A family member who applied on or before 31.12.2003 and was then eligible is covered by the CCS (Pension) Rules, 2021 even if the actual appointment or joining was on or after 01.01.2004.",
             RED,
             "The decision is simple. The crucial date is the date of application, not the date of joining or appointment, as long as the applicant was eligible when applying. So someone who applied on or before thirty-one December two thousand three, and was eligible then, comes under these rules even if the job started after that."),
            ("WHY IT CAME",
             "Staff side raised it at the National Council (JCM) meeting of 25.02.2025; DoE ID Note 1(7)/EV/2019 of 21.05.2026; DoPT consulted.",
             "Background (confirmed as references in the press text): the demand was raised in the National Council (JCM) meeting of 25.02.2025 chaired by Secretary (Pension); Department of Expenditure ID Note No. 1(7)/EV/2019 dated 21.05.2026; DoPT consulted; the O.M. of 03.03.2023 for regular recruitment (advertisement date as the crucial date) is cited as the principle, but the text of that 03.03.2023 O.M. was not read. Compassionate appointments have no advertisement, so the application date became the natural crucial date (the script's explanation).",
             BLUE,
             "Why did it come? Staff side raised it in the National Council meeting of twenty-five February two thousand twenty-five. The Department of Expenditure's note of twenty-one May two thousand twenty-six and the Department of Personnel were consulted. For regular recruitment the earlier principle used the advertisement date; compassionate jobs have no advertisement, so the application date was used."),
            ("REAL EXAMPLE",
             "Example: Bilal's brother applied on 15.12.2003, eligible, joined 2006: 2021 Rules apply. If he applied in 2005: NPS.",
             "Example (invented): Bilal's brother applied for compassionate appointment on 15.12.2003 and was eligible then; the appointment letter came in 2006. The crucial date, 15.12.2003, is on or before 31.12.2003, so the CCS (Pension) Rules, 2021 apply. If he had applied in 2005, the crucial date would be after the cut-off, and the NPS would apply. Recomputed: 15.12.2003 is before 31.12.2003.",
             GREEN,
             "Here is a real example. Bilal's brother applied on fifteen December two thousand three and was eligible then. The appointment letter came only in two thousand six. His crucial date is fifteen December two thousand three, which is before the cut-off, so these rules apply. Had he applied in two thousand five, the NPS would apply."),
            ("LIMITS AND FLAGS",
             "Not a general OPS rollback. Regular recruits are not covered. CSIR order of 07.07.2026: not confirmed.",
             "Scope (UNVERIFIED as the script's wording; teacher's plain reading): the O.M. addresses only compassionate applicants who applied on or before 31.12.2003; it is not a general return to the old pension scheme for all NPS subscribers, and regular recruits are not covered. The script's remark that autonomous bodies have no blanket order and must decide for themselves is not in the O.M. text read (the addressees are Ministries and Departments). The script's statement that CSIR issued an implementing order on 07.07.2026 was searched and not found: not confirmed. A Railway Board parallel (RBE No. 49/2026) appeared in a search result only, was not read and is not needed here.",
             PINK,
             "Be careful with the limits. This is not a general return to the old pension scheme. It covers only compassionate applicants who applied on or before the cut-off date. The script also says an organisation called CSIR passed an implementing order on seven July two thousand twenty-six, but we could not find it, so that point is not confirmed."),
        ],
        "hook": "REMEMBER: compassionate cases • crucial date = DATE OF APPLICATION • eligible on 31.12.2003 or earlier • O.M. of 22.06.2026!",
        "hook_say": "Remember: for compassionate appointments the crucial date is the date of application. If the person applied on or before thirty-one December two thousand three and was eligible, these rules apply. The O.M. is dated twenty-two June two thousand twenty-six.",
        "covers": ["OM-22.06.2026", "OM-22.06.2026-REFS", "OM-22.06.2026-SCOPE", "CSIR-07.07.2026", "EX-ADD8-1512", "RAIL-RBE-49-2026"],
    },
    {
        "id": "c1_08_defs_a_to_f",
        "chapter": "CHAPTER 8 • RULE 3(1): DEFINITIONS (a) TO (f)",
        "title": "RULE 3(1) — DEFINITIONS (a) TO (f): THE FIRST SIX",
        "accent": SKY, "badge": "RULE 3(1)(a)-(f)",
        "q": "Rule 3 defines 26 terms. What do the first six mean in everyday words?",
        "q_say": "Sir, Rule three has twenty-six definitions. What do the first six, a to f, mean?",
        "boxes": [
            ("(a) ACCOUNTS OFFICER • (b) ALLOTTEE",
             "(a) The officer who keeps a Ministry's accounts; includes the Accountant-General. (b) Someone given Government housing.",
             "Rule 3(1)(a): Accounts Officer means the officer, by whatever designation, who maintains the accounts of a Ministry, Department or Office of the Central Government or of a Union territory, and includes the Accountant-General. Rule 3(1)(b): Allottee means a Government servant to whom Government accommodation has been allotted, on licence fee or otherwise. Both confirmed (close restatement; not read verbatim from the Gazette).",
             SKY,
             "Definition a: an Accounts Officer is the officer, whatever the designation, who keeps the accounts of a Ministry, Department or office. The Accountant-General is included. Definition b: an allottee is a Government servant who has been given Government housing, whether on licence fee or otherwise."),
            ("(c) AVERAGE EMOLUMENTS • (d) BHAVISHYA",
             "(c) As worked out under Rule 32. (d) Bhavishya is the online system for sanctioning and tracking retirement benefits.",
             "Rule 3(1)(c): Average emoluments means average emoluments as determined under Rule 32 (Rule 31 defines emoluments themselves). Rule 3(1)(d): Bhavishya means an online system for sanction of retirement benefits and for tracking sanction and payment of pension. Emoluments means the pay and allowances that count for pension. Both confirmed (close restatement).",
             BLUE,
             "Definition c: average emoluments are worked out under Rule thirty-two. Emoluments are the pay and allowances that count for pension, and Rule thirty-one defines them. Definition d: Bhavishya is the online system used to sanction retirement benefits and to track sanction and payment."),
            ("(e) CHILD • (f) DEARNESS RELIEF",
             "(e) A son or daughter who can get death gratuity (Rule 45) or family pension (Rule 50). (f) Extra relief on pension, as in Rule 52.",
             "Rule 3(1)(e): Child or Children means a son or daughter of the Government servant eligible for death gratuity under Rule 45 or family pension under Rule 50. Rule 3(1)(f): Dearness Relief means the relief on pension and family pension specified in Rule 52; it is the extra amount added to pension to offset rising prices (also written DR). Both confirmed (close restatement).",
             GREEN,
             "Definition e: a child means a son or daughter who is eligible for death gratuity under Rule forty-five or family pension under Rule fifty. Definition f: dearness relief, written DR, is the extra amount added to pension and family pension to offset rising prices, as Rule fifty-two specifies."),
            ("EXAMPLE AND TRAP",
             "Example: is an Accountant-General an Accounts Officer? Yes, Rule 3(1)(a) names him. Trap: emoluments (Rule 31) is not average emoluments (Rule 32).",
             "Example (invented): a Junior Accounts Officer asks where the Accountant-General is defined. Answer: Rule 3(1)(a); the definition of Accounts Officer includes the Accountant-General. Trap: Rule 31 defines emoluments; Rule 32 gives the average that the formulae use; the definition clauses (c) and (h) point to different rules. Rule 3 contains 26 definitions in all, (a) to (z): count confirmed.",
             RED,
             "Here is a real example. A junior accounts officer asks where the Accountant-General is defined. The answer is Rule three, one, a: the Accounts Officer definition includes him. Be careful, this is the trap: Rule thirty-one gives emoluments, Rule thirty-two gives the average. The definitions point to different rules."),
        ],
        "hook": "REMEMBER: 26 definitions • AG is an Accounts Officer • emoluments = Rule 31, average emoluments = Rule 32!",
        "hook_say": "Remember: there are twenty-six definitions, the Accountant-General counts as an Accounts Officer, and emoluments sit in Rule thirty-one while the average sits in Rule thirty-two.",
        "covers": ["R3(1)(a)", "R3(1)(b)", "R3(1)(c)", "R3(1)(d)", "R3(1)(e)", "R3(1)(f)", "R3-COUNT"],
    },
    {
        "id": "c1_09_defs_g_to_j",
        "chapter": "CHAPTER 9 • RULE 3(1): DEFINITIONS (g) TO (j), DEFENCE SERVICE",
        "title": "RULE 3(1) — DEFINITIONS (g) TO (j): DEFENCE SERVICE AND FAMILY PENSION",
        "accent": GREEN, "badge": "RULE 3(1)(g)-(j)",
        "q": "Is a soldier in Defence Service for these rules, and what do (h), (i) and (j) say?",
        "q_say": "Sir, is an Army soldier in Defence Service under these rules, and what do h, i and j say?",
        "boxes": [
            ("(g) DEFENCE SERVICE",
             "Civil services in the Ministry of Defence paid from Civil Estimates and not under the Army, Navy or Air Force Acts.",
             "Rule 3(1)(g): Defence Service means the Central Government services in the Ministry of Defence, including the Defence Accounts Department, which are paid from the Civil Estimates and are not subject to the Air Force Act, 1950, the Army Act, 1950 or the Navy Act, 1957. Confirmed (close restatement). 'Civil Estimates' are the budget for civilian, not uniformed, staff.",
             GREEN,
             "Definition g is a sharp one. Defence Service means civilian services in the Ministry of Defence, including the Defence Accounts Department, paid from the Civil Estimates, and not governed by the Army, Navy or Air Force Acts. Civil Estimates is simply the budget head for civilian staff."),
            ("DEFENCE SERVICE VS ARMED FORCES",
             "A civilian clerk or Defence Accounts staffer is covered. An Army havaldar or Navy officer is not: separate framework.",
             "Script's explanation (BONUS-4; the definition itself is confirmed): a Ministry of Defence civilian clerk or a Defence Accounts Department officer is Defence Service and these rules apply; an Army havaldar or a Navy officer belongs to the Armed Forces of the Union and has a separate pension framework. Rule 20 is the separate rule that counts military service as qualifying service when an ex-serviceman is re-employed in civil service; Rule 20 was not read in this batch and is checked in the next batch (Batch 2).",
             ORANGE,
             "So who is in? A civilian clerk in the Ministry of Defence, or an officer of the Defence Accounts Department, is Defence Service and is covered. An Army havaldar or a Navy officer is in the Armed Forces and has a separate pension framework. Rule twenty separately counts military service for someone who later joins civil service; we verify it in the next batch."),
            ("(h) EMOLUMENTS • (i) FAMILY PENSION",
             "(h) Emoluments as defined in Rule 31. (i) Family pension under Rule 50, but NOT including dearness relief.",
             "Rule 3(1)(h): Emoluments has the meaning in Rule 31. Rule 3(1)(i): Family Pension means family pension under Rule 50 but does not include Dearness Relief. Both confirmed (close restatement). R3-TRAP-DR confirmed: family pension excludes DR here; DR is added separately under Rule 52.",
             BLUE,
             "Definition h says emoluments are as Rule thirty-one defines. Definition i says family pension is the pension under Rule fifty, but without dearness relief. That is a favourite trap: dearness relief is added on separately under Rule fifty-two."),
            ("(j) FOREIGN SERVICE • TRAP",
             "(j) Pay drawn, with Government sanction, from a source other than the Consolidated Fund of India, a State or a Union territory.",
             "Rule 3(1)(j): Foreign Service means service in which a Government servant receives his pay, with the sanction of Government, from a source other than the Consolidated Fund of India, a State or a Union territory. Confirmed (close restatement). Q and A: does family pension include DR? No; Rule 3(1)(i) says so plainly.",
             RED,
             "Definition j: foreign service means service where, with the Government's sanction, your pay comes from a source other than the Consolidated Fund of India, a State or a Union territory. The trap again: if someone asks whether family pension includes dearness relief, the answer is no."),
        ],
        "hook": "REMEMBER: Defence Service = civilians in MoD • soldiers are Armed Forces • family pension excludes DR!",
        "hook_say": "Remember: Defence Service means civilians in the Ministry of Defence, soldiers belong to the Armed Forces, and family pension does not include dearness relief.",
        "covers": ["R3(1)(g)", "R3-DEF-G-NOTE", "R3(1)(h)", "R3(1)(i)", "R3(1)(j)"],
    },
    {
        "id": "c1_10_defs_k_to_p",
        "chapter": "CHAPTER 10 • RULE 3(1): DEFINITIONS (k) TO (p)",
        "title": "RULE 3(1) — DEFINITIONS (k) TO (p): FORM, FORMAT, GRATUITY AND HEADS",
        "accent": PINK, "badge": "RULE 3(1)(k)-(p)",
        "q": "What do (k) to (p) mean, and how do Form and Format differ?",
        "q_say": "Sir, what do definitions k to p mean, and what is the difference between a Form and a Format?",
        "boxes": [
            ("(k) FORM • (l) FORMAT",
             "Form and Format are documents attached to the rules. Rule of thumb: a Form is an application, a Format is a template or undertaking.",
             "Rule 3(1)(k): Form means a form appended to these rules. Rule 3(1)(l): Format means a format appended to these rules. Confirmed (close restatement). The script says there are 13 Forms and 13 Formats: those counts were not checked in this batch (unverified). Rule of thumb (study aid, not rule text; R3-TRAP-FORMFORMAT unverified): Form 1 is an application (Rule 9); Format 1 is an undertaking (Rule 7(4)(b)).",
             PINK,
             "Definitions k and l are short. A Form and a Format are simply documents attached to the rules. As a rule of thumb, a Form is usually an application and a Format is a template or undertaking. For example Form one is an application under Rule nine, while Format one is an undertaking under Rule seven. This is a study aid, not rule text, and the script's count of thirteen each is unchecked."),
            ("(m) GOVERNMENT • (n) DUES",
             "(m) Government means the Central Government. (n) Government dues are as defined in Rule 67(2).",
             "Rule 3(1)(m): Government means the Central Government. Rule 3(1)(n): Government dues has the meaning given in Rule 67(2). Both confirmed (close restatement). So where the rules say Government, it does not mean a State Government.",
             SKY,
             "Definition m: Government means the Central Government, never a State Government. Definition n: Government dues are as Rule sixty-seven, sub-rule two, defines them. Those are amounts such as housing dues that may be recovered from retirement benefits."),
            ("(o) GRATUITY: THREE KINDS",
             "Gratuity covers service gratuity (Rule 44), retirement or death gratuity (Rule 45(1)) and residuary gratuity (Rule 45(3)).",
             "Rule 3(1)(o): Gratuity includes service gratuity under Rule 44, retirement gratuity or death gratuity under Rule 45(1), and residuary gratuity under Rule 45(3). Confirmed (close restatement). Gratuity is a one-time lump sum paid on retirement or death, unlike pension, which is paid every month.",
             GREEN,
             "Definition o: gratuity covers three things. Service gratuity under Rule forty-four, retirement or death gratuity under Rule forty-five, sub-rule one, and residuary gratuity under Rule forty-five, sub-rule three. Gratuity is a one-time lump sum, unlike the monthly pension."),
            ("(p) HEAD OF DEPARTMENT",
             "The authority named in Schedule I of the DFPR 1978, or any other authority the President specifies.",
             "Rule 3(1)(p): Head of Department means the authority specified in Schedule I of the Delegation of Financial Powers Rules, 1978 (DFPR), or any other authority specified by the President. Confirmed (close restatement). Trap: a title alone does not make someone Head of Department; the DFPR Schedule or a Presidential specification does (script's BONUS-5 reasoning; the clause (q) side of this point was corrected, see the next chapter).",
             ORANGE,
             "Definition p: Head of Department is the authority named in Schedule one of the Delegation of Financial Powers Rules, nineteen seventy-eight, or any other authority the President specifies. So the title alone does not decide it; the Schedule or a Presidential specification does."),
        ],
        "hook": "REMEMBER: Government = Central Government • gratuity = 3 kinds • Form (application) and Format (template) are different!",
        "hook_say": "Remember: Government means the Central Government, gratuity has three kinds, and a Form and a Format are different documents.",
        "covers": ["R3(1)(k)", "R3(1)(l)", "R3(1)(m)", "R3(1)(n)", "R3(1)(o)", "R3(1)(p)", "R3-TRAP-FORMFORMAT", "FORM-FORMAT-13"],
    },
    {
        "id": "c1_11_defs_q_to_w",
        "chapter": "CHAPTER 11 • RULE 3(1): DEFINITIONS (q) TO (w)",
        "title": "RULE 3(1) — DEFINITIONS (q) TO (w): HEAD OF OFFICE TO QUALIFYING SERVICE",
        "accent": BLUE, "badge": "RULE 3(1)(q)-(w)",
        "q": "Who is Head of Office, what is a Pension Disbursing Authority, and what is qualifying service?",
        "q_say": "Sir, who is the Head of Office, what is a Pension Disbursing Authority, and what is qualifying service?",
        "boxes": [
            ("(q) HEAD OF OFFICE",
             "A Gazetted Officer declared as such under DFPR Rule 14, or another person the competent authority specifies.",
             "Rule 3(1)(q): Head of Office means a Gazetted Officer declared as such under Rule 14 of the DFPR, 1978, or another person specified by the competent authority. CORRECTED against the script: the script (BONUS-5) says only declaration counts and that seniority never makes a Head of Office; the definition also allows another person specified by the competent authority, so the script's claim is too strong. Gazetted Officer means an officer whose appointment is notified in the Gazette.",
             BLUE,
             "Definition q is where the script needs a correction. Head of Office means a Gazetted Officer declared as such under Rule fourteen of the Delegation of Financial Powers Rules, or another person the competent authority specifies. Being the senior-most officer does not by itself make someone Head of Office. But the script's claim that declaration is the only route is too strong."),
            ("(r) LOCAL FUND • (s) MINOR",
             "(r) A fund where Government has complete, direct control over spending. (s) A minor is a person under 18.",
             "Rule 3(1)(r): Local Fund administered by Government means the fund of a body, under law or rule, over whose expenditure Government keeps complete and direct control (linked to Rule 12). Rule 3(1)(s): Minor means a person who has not completed 18 years. Example (recomputed): Esha's son, aged 17 years 11 months, is a minor; on his 18th birthday he is not. Both definitions confirmed (close restatement).",
             SKY,
             "Definition r: a local fund administered by Government is a body's fund over whose spending the Government has complete and direct control. Definition s: a minor is a person under eighteen. Esha's son, aged seventeen years eleven months, is a minor; on his eighteenth birthday he is not."),
            ("(t) PENSION AND DR",
             "Pension includes gratuity unless the context separates them, and does NOT include dearness relief.",
             "Rule 3(1)(t): Pension includes gratuity, except where the context separates pension from gratuity, and does not include Dearness Relief. Confirmed (close restatement). R3-TRAP-DR confirmed: DR is never part of pension or family pension under Rules 3(1)(i) and (t); it is added under Rule 52. DR is currently 60% w.e.f. 01.01.2026 (see the currency chapter; check the latest O.M.).",
             GREEN,
             "Definition t: pension includes gratuity unless the context keeps them apart, and it does not include dearness relief. This is the same trap as family pension. Dearness relief sits on top, under Rule fifty-two, and its rate changes; the current figure is in a later chapter."),
            ("(u) DISBURSING AUTHORITY • (v) PPO",
             "(u) Four channels: banks, Post Office, Treasury, Accounts Officer. (v) PPO includes e-PPO.",
             "Rule 3(1)(u): Pension Disbursing Authority means banks selected in consultation with the Reserve Bank of India for paying Central civil pensioners, the Post Office, a Treasury including a Sub-Treasury, and an Accounts Officer: four channels confirmed. The script says the CGA specifies the banks in consultation with RBI; the CGA role is not confirmed. Rule 3(1)(v): Pension Payment Order (PPO) includes an electronic PPO (e-PPO). PPO is the order that authorises the pension to be paid. Confirmed (close restatement).",
             ORANGE,
             "Definition u: a Pension Disbursing Authority is one of four channels: banks selected with the Reserve Bank of India, the Post Office, a Treasury including a Sub-Treasury, or an Accounts Officer. The script names the Controller General of Accounts as the bank selector, but we could not confirm that part. Definition v: the Pension Payment Order, the PPO, includes the electronic one."),
            ("(w) QUALIFYING SERVICE",
             "Service rendered on duty or otherwise that counts when pension and gratuity are worked out.",
             "Rule 3(1)(w): Qualifying Service means service rendered, on duty or otherwise, which counts for pension and gratuity. Confirmed (close restatement). Example (invented): Dev's years of ordinary duty count; whether time on leave or in a special category counts depends on Chapter III (Rules 11 onwards), covered from the next batch.",
             PINK,
             "Definition w: qualifying service is service, on duty or otherwise, that counts when pension and gratuity are worked out. Which periods exactly count is the subject of Chapter three, starting from the next batch."),
        ],
        "hook": "REMEMBER: HOO = declared under DFPR Rule 14 OR specified • minor = under 18 • DR is outside pension!",
        "hook_say": "Remember: Head of Office is declared under DFPR Rule fourteen or specified by the competent authority, a minor is under eighteen, and dearness relief is outside pension.",
        "covers": ["R3(1)(q)", "R3(1)(r)", "R3(1)(s)", "R3(1)(t)", "R3-TRAP-DR", "R3(1)(u)", "R3(1)(v)", "R3(1)(w)"],
    },
    {
        "id": "c1_12_defs_x_to_z",
        "chapter": "CHAPTER 12 • RULE 3: DEFINITIONS (x) TO (z) AND RULE 3(2)",
        "title": "RULE 3 — DEFINITIONS (x) TO (z), THE FUNDAMENTAL RULES FALLBACK",
        "accent": RED, "badge": "RULE 3(1)(x)-(z), 3(2)",
        "q": "What do (x), (y) and (z) mean, and where do I look for a word Rule 3 does not define?",
        "q_say": "Sir, what do x, y and z mean, and where do I look when a word is not defined in Rule three?",
        "boxes": [
            ("(x) RETIREMENT BENEFITS",
             "Pension or service gratuity, and retirement gratuity where it is admissible.",
             "Rule 3(1)(x): Retirement Benefits means pension or service gratuity, and retirement gratuity where admissible. Confirmed (close restatement).",
             RED,
             "Definition x: retirement benefits mean pension or service gratuity, plus retirement gratuity where it is admissible."),
            ("(y) SERVICE BOOK • (z) TREASURY",
             "(y) Service Book includes the service roll, if any. (z) Treasury includes a Sub-Treasury.",
             "Rule 3(1)(y): Service Book includes the service roll, if any (the service book is the record of a servant's career). Rule 3(1)(z): Treasury includes a Sub-Treasury. Both confirmed (close restatement).",
             ORANGE,
             "Definition y: the service book includes the service roll, if there is one. It is the record of a servant's career. Definition z: a treasury includes a sub-treasury."),
            ("RULE 3(2): THE FALLBACK",
             "A word not defined here but defined in the Fundamental Rules, 1922 takes that meaning.",
             "Rule 3(2): words and expressions not defined in these rules but defined in the Fundamental Rules, 1922 have the meanings given there (close restatement). The script adds that the General Clauses Act is not the dictionary here: that comparison is the script author's remark and was not in the text read.",
             BLUE,
             "Sub-rule two says a word not defined in these rules, but defined in the Fundamental Rules of nineteen twenty-two, has the meaning given there. The script adds that the General Clauses Act is not used; that comparison is the author's remark, not confirmed in the text we read."),
            ("COUNT AND EXAM LINE",
             "26 definitions, (a) to (z). Unknown word? Check Rule 3, then the Fundamental Rules 1922.",
             "Count: 26 clauses, (a) to (z), confirmed. Q and A from the script: if a term is not in Rule 3, where is the dictionary? In the Fundamental Rules, 1922 under Rule 3(2). Three traps in this chapter family: Form versus Format, DR not part of pension or family pension, and Head of Office needing declaration or specification.",
             GREEN,
             "Count again: twenty-six definitions, a to z. If a word is missing, look at the Fundamental Rules of nineteen twenty-two. And keep the three traps in mind: Form versus Format, dearness relief outside pension, and Head of Office needing a declaration or specification."),
        ],
        "hook": "REMEMBER: 26 definitions • missing word? Fundamental Rules 1922 via Rule 3(2)!",
        "hook_say": "Remember: twenty-six definitions, and if a word is missing, look in the Fundamental Rules of nineteen twenty-two through Rule three, sub-rule two.",
        "covers": ["R3(1)(x)", "R3(1)(y)", "R3(1)(z)", "R3(2)"],
    },
    {
        "id": "c1_13_rule4",
        "chapter": "CHAPTER 13 • RULE 4: TRANSFER FROM A SERVICE OUTSIDE THESE RULES",
        "title": "RULE 4 — A PERMANENT TRANSFER IN, AND THE SIX-MONTH OPTION",
        "accent": ORANGE, "badge": "RULE 4",
        "q": "If someone moves permanently into a post covered by these rules, which pension rules apply?",
        "q_say": "Sir, if someone is permanently transferred into a covered post, which pension rules apply, and can he choose?",
        "boxes": [
            ("THE RULE • 4(1)",
             "A servant permanently transferred from a service where these rules do not apply to one where they do is governed by these rules.",
             "Rule 4(1): a Government servant who is permanently transferred from a service or post to which these rules do not apply to a service or post to which they apply shall be governed by these rules. Confirmed (close restatement; not read verbatim from the Gazette).",
             ORANGE,
             "Let us take the rule first. If a Government servant is permanently transferred from a service where these rules do not apply into one where they do, he comes under these rules automatically. The door opens for him."),
            ("THE PROVISO • SIX MONTHS",
             "He may choose to stay under his earlier pension rules, within 6 months of the transfer order, or of returning from leave, whichever is later.",
             "Proviso to Rule 4(1): the servant may elect to be governed by the pension rules applicable to him immediately before the transfer, within six months from the date of issue of the transfer order, or, if he was on leave on that day, within six months from the date of return from leave, whichever is later. Six months confirmed (TL-R4-6M). Close restatement.",
             GREEN,
             "Now the exception. The servant gets an option: he may choose to stay under the pension rules he had before the transfer. He must choose within six months of the transfer order, or, if he was on leave that day, within six months of returning from leave, whichever is later."),
            ("HOW: IN WRITING, THEN FINAL",
             "The choice must be in writing to the authority that issued the transfer order, and once made it is final.",
             "Election in writing and communicated to the authority that issued the transfer order (the sub-rule text found in one PDF summary as Rule 4(2)); election once made is final (found as Rule 4(3) in the same summary). The sub-rule NUMBERING is a point to confirm, because the book summary places the writing and authority wording in the proviso. The script described sub-rules 2 and 3 only as a claims processing frame, with no text; that description is wrong. R4(2), R4(3) and R4-FINAL: substance confirmed, numbering to be confirmed.",
             BLUE,
             "How is the choice made? It must be in writing and sent to the authority that issued the transfer order. And once made, it is final; there is no second thought. The script called the later sub-rules a claims frame, but the official text shows they carry these two points. One caution: the sub-rule numbers need confirming."),
            ("REAL EXAMPLE",
             "Dev's order is dated 10.03.2026; he was on leave and returned 04.04.2026. His deadline is 04.10.2026.",
             "Example (invented, recomputed): Dev, on deputation, is permanently absorbed into a covered post. The transfer order is dated 10.03.2026. Six months from the order would be 10.09.2026. Dev was on leave on 10.03.2026 and returned on 04.04.2026, six months from which is 04.10.2026. The later date, 04.10.2026, is his deadline. On 15.09.2026 he sends a written option to the issuing authority to stay under his earlier rules: valid, and final.",
             SKY,
             "Here is a real example. Dev is permanently absorbed. The order is dated ten March two thousand twenty-six. He was on leave that day and came back on four April. Six months from the order would be ten September, but six months from his return is four October, which is later. So four October is his deadline, and a written option on fifteen September is in time and final."),
            ("THE TRAP: A ROUTING RULE",
             "Rule 4 gives no money by itself. It only says WHICH rule book applies. After the choice, no change of mind.",
             "Rule 4 grants no benefit, no amount of pension and no qualifying service on its own: it is a routing rule that decides whether these rules apply (script's ADD-B1-1, reasonable summary, confirmed). Q and A: can he change his mind after electing? No, the election is final. Compare Rule 5 in the next chapter, which asks a different question.",
             RED,
             "Be careful, this is the trap. Rule four gives no benefit of its own. It only decides which rule book applies. And after the option is exercised, the servant cannot change his mind."),
        ],
        "hook": "REMEMBER: Rule 4 = routing • option within 6 months (later of order or return from leave) • in writing • final!",
        "hook_say": "Remember: Rule four is a routing rule. The option must be in writing within six months, counted from the later of the order or the return from leave, and it is final.",
        "covers": ["R4(1)", "R4-PROV", "R4(2)", "R4(3)", "R4-FINAL", "R4-ADD1", "EX-R4", "TL-R4-6M"],
    },
    {
        "id": "c1_14_rule5",
        "chapter": "CHAPTER 14 • RULE 5: WHICH VERSION OF THE RULES APPLIES",
        "title": "RULE 5 — THE RULES IN FORCE ON RETIREMENT OR DEATH APPLY",
        "accent": SKY, "badge": "RULE 5",
        "q": "A claim arises today but the rules change tomorrow. Which version decides?",
        "q_say": "Sir, if the rules change after someone retires, which version decides the claim?",
        "boxes": [
            ("THE RULE • 5(1)",
             "A pension or family pension claim is decided by the rules in force when the servant retires, is retired, is discharged, resigns or dies.",
             "Rule 5(1): claims to pension or family pension shall be regulated by the rules in force when the Government servant retires, is retired, is discharged or is allowed to resign, or dies. Confirmed (close restatement).",
             SKY,
             "Let us take the rule first. A claim is decided by the rules that were in force on the day the servant retires, is retired, is discharged, is allowed to resign, or dies. A later change does not reopen the case."),
            ("5(2): LAST WORKING DAY",
             "Retirement day counts as the last completed working day; so does the date of death.",
             "Rule 5(2): the day of retirement, retirement by the Government, discharge or resignation is treated as the last completed working day; the date of death is treated as a completed working day. Proviso (part of Rule 5(2) itself, not a line created by the 2025 O.M.): if the servant was on leave, absent or under suspension immediately before retirement or death, that day is treated as part of the leave, absence or suspension. Confirmed (close restatement).",
             GREEN,
             "Sub-rule two: the day of retirement is treated as the last completed working day, and the date of death is a completed working day. The proviso adds that if the servant was on leave, absent or suspended just before, that day counts as part of the leave, absence or suspension. Nothing is chopped off."),
            ("THE O.M. OF 30.10.2025",
             "DoPPW O.M. of 30.10.2025 on claims to pension restates Rule 5. It is not a new rule.",
             "DoPPW O.M. F.No. 38/10(03)/2025-P&PW(A) (e 11193)(iii) dated 30.10.2025, subject: Claims to pension or family pension under Central Civil Services (Pension) Rules 2021; signed by Under Secretary Madhu Mankotia. Number, date and subject confirmed. CORRECTION to the script: the script called the leave, absence and suspension line a new clarification; it is already part of the Rule 5(2) proviso, and the O.M. restates the rule. The script lists the number without the (iii) suffix.",
             BLUE,
             "A memorandum dated thirty October two thousand twenty-five, file number thirty-eight slash ten, bracket three, slash two thousand twenty-five, repeats this rule. The script treated the leave and suspension line as new, but it was already in the rule. So the memorandum restates, it does not add."),
            ("REAL EXAMPLE",
             "Asha retires on 30.06.2026 after earned leave: that day is both leave and her last completed day. Rules in force that day decide.",
             "Example (invented): Asha superannuates on 30.06.2026 and was on earned leave just before. Her 30.06.2026 is part of the leave and also her last completed working day. The rules in force on 30.06.2026 decide her claim. In a death case, the date of death is a completed working day and fixes the version of the rules. The script adds that the Rule 81(2) clock for the day after death starts from that date: Rule 81 was not checked in this batch (unverified). Rule 87(2)(c) is the script's pending-cases link (unverified, Batch 6).",
             ORANGE,
             "Here is a real example. Asha retires on thirty June two thousand twenty-six, having been on earned leave just before. That day is part of her leave and also her last completed day. The rules in force on that day decide her claim. The script links this to Rule eighty-one and to the saving in Rule eighty-seven; we have not checked those yet."),
            ("RULE 4 VERSUS RULE 5",
             "Rule 4 asks: which rule BOOK applies to me? Rule 5 asks: which VERSION applies on my date?",
             "Script's comparison (BONUS-6; consistent with the texts, confirmed): Rule 4 is an individual-option rule about which rule-set applies after a permanent transfer; Rule 5 is a time rule about which version of the rules applies, fixed at the date of retirement or death. Together: Rule 4 decides whether these rules apply; Rule 5 decides which version. Rule 87(2)(c) pending-cases link: not read, unverified.",
             PINK,
             "To keep them apart: Rule four asks which rule book applies to me. Rule five asks which version of that book applies on my date. Decide Rule four first, then Rule five."),
        ],
        "hook": "REMEMBER: version on the day of retirement or death • last completed working day • leave or suspension day stays part of it!",
        "hook_say": "Remember: the version in force on the day of retirement or death decides, that day is the last completed working day, and a leave or suspension day stays part of the leave or suspension.",
        "covers": ["R5(1)", "R5(2)", "R5-PROV", "OM-30.10.2025-5", "R5-R87-2c", "BONUS-6-R4R5", "EX-R5-30JUN2026"],
    },
    {
        "id": "c1_15_rule6_main",
        "chapter": "CHAPTER 15 • RULE 6: NO DOUBLE PENSION",
        "title": "RULE 6 — NO TWO PENSIONS FOR THE SAME SERVICE, AND ITS EXCEPTIONS",
        "accent": RED, "badge": "RULE 6",
        "q": "Can a re-employed pensioner draw two pensions for the same service?",
        "q_say": "Sir, can a pensioner who is re-employed draw two pensions?",
        "boxes": [
            ("THE RULE • 6(1)",
             "No Government servant can earn two pensions for the same service or post, at the same time, or for the same continuous service.",
             "Rule 6(1): a Government servant shall not be entitled to two pensions in respect of the same service or post, or at the same time, or in respect of the same continuous service. Confirmed (close restatement; the sub-rule wording is a summary from page-summarising tools).",
             RED,
             "Let us take the rule first. Rule six, sub-rule one, says a Government servant cannot get two pensions for the same service or post, nor at the same time, nor for the same continuous service."),
            ("6(2): RE-EMPLOYED PENSIONERS",
             "Except as Rules 19 and 20 allow, a re-employed pensioner gets no separate pension or gratuity for the re-employment period.",
             "Rule 6(2): except as provided in Rule 19 or Rule 20, a Government servant who has retired on superannuation pension, retiring pension or compulsory retirement pension, or who is drawing compassionate allowance after dismissal or removal, and is re-employed, shall not be entitled to a separate pension or gratuity for the period of re-employment. Confirmed (close restatement). Compassionate allowance is a small allowance given to a dismissed person's family at the Government's discretion.",
             ORANGE,
             "Sub-rule two is the re-employment case. Except as Rules nineteen and twenty allow, a servant who retired on superannuation, retiring or compulsory retirement pension, or draws a compassionate allowance after dismissal, and is then re-employed, gets no separate pension or gratuity for the re-employment period."),
            ("FIRST PROVISO",
             "Autonomous body or PSU service, then Government service joined with proper permission by 31.12.2003: Government pension plus the body's pension.",
             "First proviso: where a servant served in an autonomous body or Public Sector Undertaking (PSU) and then joined Government service, with the proper permission of the body, on or before 31.12.2003, he may receive the pension and gratuity for the Government service and also the pension or gratuity from the body or PSU. Confirmed (close restatement). An autonomous body is a government-funded organisation that runs with its own board; a PSU is a company owned by the Government.",
             GREEN,
             "First proviso. Someone who worked in an autonomous body or a Public Sector Undertaking, and then joined Government service with the body's proper permission on or before thirty-one December two thousand three, can take the Government pension and gratuity and also the pension or gratuity from the body."),
            ("SECOND PROVISO, EXAMPLE, TRAP",
             "Combined gratuity is capped at what would be paid if all service were Government service. Rules 19 and 20 are the only exceptions in the main rule.",
             "Second proviso: the gratuity for the combined service of the body or PSU and the Government shall not exceed the gratuity that would have been admissible if the whole service had been under the Government, on the Government emoluments. Example (invented): Charu retired on superannuation pension and was re-employed as a consultant in a PSU; for that re-employment period she gets no separate pension or gratuity, and any combined gratuity is capped at the notional Government figure. Q and A: do re-employed civil pensioners always get two pensions? No; Rule 6(2) stops it, except Rule 19 (re-employed civil pensioner) and Rule 20 (military service). Confirmed.",
             BLUE,
             "Second proviso: the combined gratuity cannot go above what would have been payable if all the service had been with the Government. Here is a real example. Charu retired on superannuation pension and was re-employed as a PSU consultant; she gets no separate pension for that period. Be careful, this is the trap: the answer to 'do they always get two?' is no, only Rules nineteen and twenty are exceptions."),
        ],
        "hook": "REMEMBER: one service, one pension • re-employment gets no second pension • exceptions only Rules 19 and 20!",
        "hook_say": "Remember: one service, one pension. Re-employment gives no separate pension, and the only exceptions are Rules nineteen and twenty.",
        "covers": ["R6(1)", "R6(2)", "R6-PROV1", "R6-PROV2", "EX-R6-PSU"],
    },
    {
        "id": "c1_16_rule6_expl",
        "chapter": "CHAPTER 16 • RULE 6: THE TWO EXPLANATIONS AND THE RULES 19, 20 PREVIEW",
        "title": "RULE 6 — THE TWO EXPLANATIONS AND THE EXCEPTIONS IN RULES 19 AND 20",
        "accent": BLUE, "badge": "RULE 6 • EXPL 1-2",
        "q": "What do Rule 6's two Explanations say, and what are Rules 19 and 20 that it mentions?",
        "q_say": "Sir, what do the two Explanations of Rule six say, and what are Rules nineteen and twenty?",
        "boxes": [
            ("EXPLANATION 1: PROPER PERMISSION",
             "Permission is deemed proper if the servant applied with the body's prior permission and its order says he resigns to take the Government post.",
             "Explanation 1 to Rule 6 (close restatement): a servant is deemed to have joined Government service with proper permission if he applied for the post with the prior permission of the body and the body's order clearly states that he resigns from the body to take up the Government post. The script left the Explanations' content blank; it is now filled from the official-copy text. A related O.M. (see below) says the same for qualifying service under Rule 14.",
             BLUE,
             "The script said it did not know what the Explanations contain. Here they are. Explanation one: a servant is deemed to have joined with proper permission if he applied with the body's prior permission, and the body's order clearly says he resigns to take the Government post."),
            ("EXPLANATION 2: WHO PAYS",
             "Pension for the body or PSU service is paid by that body. The Government has no liability for it.",
             "Explanation 2 to Rule 6 (close restatement): the pension for the service in the body or PSU is payable by that body, and the Government has no liability for it. Found in one official-copy PDF summary.",
             GREEN,
             "Explanation two: the pension for the body or PSU service is paid by that body, and the Government has no liability for it."),
            ("RELATED O.M. • 29.10.2025",
             "DoPPW O.M. of 29.10.2025: proper-permission deeming for autonomous-body service; PSU or bank service is not qualifying service before a Central appointment.",
             "DoPPW O.M. No. 28/04/2024-P&PW(I)/QS/10145 dated 29.10.2025 on services in autonomous bodies: applies the proper-permission deeming rule; PSU service, including service in a nationalised bank or financial institution, is not qualifying service before the Central appointment (applying Rule 14 and the O.M. of 02.10.2022). Confirmed; belongs mainly to the Rule 14 chapter in the next batch.",
             ORANGE,
             "A related memorandum of twenty-nine October two thousand twenty-five, number twenty-eight slash oh-four slash two thousand twenty-four, deals with autonomous bodies. It repeats the proper-permission idea and says PSU or bank service before a Central appointment is not qualifying service. It belongs mainly to the Rule fourteen chapter next time."),
            ("RULES 19 AND 20: A PREVIEW • UNVERIFIED",
             "Rule 19: re-employed civil pensioner. Rule 20: counting military service. Details unconfirmed here; see Batch 2.",
             "UNVERIFIED in this batch (BONUS-7-R19R20): the script says Rule 19 deals with a re-employed civil pensioner and the refund of pension drawn, commutation value and gratuity; Rule 20 deals with counting military service as qualifying service when an ex-serviceman joins civil service. Not read here: verified in Batch 2. Structure of Rule 6 (confirmed): 1 main rule, 2 exceptions (Rules 19 and 20), 2 provisos, 2 Explanations. OBSOLETE / HISTORY ONLY: the script's open point that the Explanations' wording is missing is replaced by the text above.",
             RED,
             "Be careful, this is a preview only. The script says Rule nineteen is about a re-employed civil pensioner and refunds, and Rule twenty counts military service. We have not confirmed those details here; we do so in the next batch. The structure of Rule six is confirmed: one main rule, two exceptions, two provisos, two Explanations."),
        ],
        "hook": "REMEMBER: Rule 6 = 1 main rule + 2 exceptions + 2 provisos + 2 Explanations!",
        "hook_say": "Remember: Rule six has one main rule, two exceptions, two provisos and two Explanations.",
        "covers": ["R6-EXPL1", "R6-EXPL2", "R6-STRUCT", "R6-GAPFLAG", "OM-29.10.2025-QS", "BONUS-7-R19R20"],
    },
    {
        "id": "c1_17_rule7_main",
        "chapter": "CHAPTER 17 • RULE 7: PENSION DEPENDS ON FUTURE GOOD CONDUCT",
        "title": "RULE 7(1) TO 7(3) — WITHHOLDING PENSION FOR BAD CONDUCT AFTER RETIREMENT",
        "accent": ORANGE, "badge": "RULE 7(1)-(3)",
        "q": "Can pension be stopped after retirement, who decides, and how much notice is given?",
        "q_say": "Sir, can pension be stopped after retirement, who decides, and what notice does the pensioner get?",
        "boxes": [
            ("7(1)(a): GOOD CONDUCT",
             "Future good conduct is an implied condition of every grant of pension and of its continuance.",
             "Rule 7(1)(a): future good conduct shall be an implied condition of every grant of pension and its continuance. Confirmed (close restatement). Implied means not spelled out in each sanction letter but always understood.",
             ORANGE,
             "Let us take the rule first. Future good conduct is an implied condition of every grant of pension and of its continuing. Implied means it is not written into each letter but is always understood."),
            ("7(1)(b): WHO AND WHEN",
             "The Appointing Authority may, by written order, withhold or withdraw pension, whole or part, permanently or for a period, for serious crime or grave misconduct.",
             "Rule 7(1)(b): the Appointing Authority may by order in writing withhold or withdraw a pension or any part of it, whether permanently or for a specified period, if the pensioner is convicted of a serious crime or is found guilty of grave misconduct. Confirmed. Floor proviso: where a part of the pension is withheld or withdrawn, the pension shall not be reduced below the minimum pension specified in Rule 44. Confirmed (close restatement).",
             RED,
             "Under clause b, the Appointing Authority, by a written order, may withhold or withdraw all or part of the pension, for ever or for a period, if the pensioner is convicted of a serious crime or found guilty of grave misconduct. If only part is cut, the pension cannot fall below the Rule forty-four minimum."),
            ("7(2) AND 7(3): TWO SITUATIONS",
             "Convicted by a court: act in the light of the judgment. No conviction: give notice with the proposed action and grounds; 15 days to reply, extendable by 15.",
             "Rule 7(2): where the pensioner has been convicted of serious crime by a court, action shall be taken in the light of the judgment. Rule 7(3): in other cases, a notice stating the proposed action and its grounds shall be given; the pensioner may make a representation within fifteen days, which may be extended by up to a further fifteen days; the authority shall consider the representation. TL-R7-15D confirmed (close restatement). Representation means a written reply stating the pensioner's case.",
             BLUE,
             "Two situations. If a court has convicted the pensioner of a serious crime, the authority acts in the light of the judgment. Otherwise it must first give a notice stating the proposed action and its grounds. The pensioner has fifteen days to reply, and this can be extended by up to fifteen more, and the authority must consider the reply."),
            ("EXAMPLE",
             "Bilal gets a notice on 01.06.2026. His reply is due 16.06.2026, or at the latest 01.07.2026 if extended.",
             "Example (invented, recomputed): a notice is served on Bilal on 01.06.2026. Fifteen days gives 16.06.2026; with the extra fifteen days the outer limit is 01.07.2026. After considering his reply, the Appointing Authority withholds part of his pension for a fixed period by a written order; the remaining pension is not below the Rule 44 minimum. Compare Rule 9(7), which gives thirty days, not fifteen.",
             GREEN,
             "Here is a real example. Bilal gets a notice on first June two thousand twenty-six. His reply is due on sixteen June, and at the latest on first July if the extra fifteen days are given. Then the authority considers his reply and decides, never going below the minimum pension."),
            ("THE TRAP: WHO IS THE AUTHORITY",
             "In 7(1)(b) the authority is the Appointing Authority, NOT the President. Do not write President.",
             "R7-TRAP confirmed: Rule 7(1)(b) names the Appointing Authority. CORRECTION to the script's ADD-B1-3 claim that one limb of Rule 7 has the President as the authority (R7-ADD3-PRES, unverified and not found): the President appears in Rule 7(6) (UPSC consultation when the President is the competent authority) and Rule 7(7) (appeal), not as a separate first-instance limb. Q and A: in the Rule 7(1)(b) situation is the authority the President? No.",
             PINK,
             "Be careful, this is the trap. In Rule seven, one, b, the authority is the Appointing Authority, not the President. The script suggested a separate President limb, but we could not find one. The President shows up later, in sub-rules six and seven, for UPSC consultation and appeals."),
        ],
        "hook": "REMEMBER: Rule 7(1)(b) = Appointing Authority • notice 15 + 15 days • floor = Rule 44 minimum!",
        "hook_say": "Remember: in Rule seven the authority is the Appointing Authority, the notice period is fifteen days extendable by fifteen, and the floor is the Rule forty-four minimum pension.",
        "covers": ["R7(1)(a)", "R7(1)(b)", "R7-PROV", "R7(2)", "R7(3)", "R7-ADD3-PRES", "R7-TRAP", "EX-R7", "TL-R7-15D"],
    },
    {
        "id": "c1_18_rule7_rest",
        "chapter": "CHAPTER 18 • RULE 7: SECURITY ORGANISATIONS, UPSC, APPEAL AND THE EXPLANATION",
        "title": "RULE 7(4) TO 7(7) AND THE EXPLANATION — THE REST OF RULE 7",
        "accent": PINK, "badge": "RULE 7(4)-(7)",
        "q": "What are Rule 7's sub-rules 4 to 7 and its Explanation? The script skipped some.",
        "q_say": "Sir, what are sub-rules four to seven of Rule seven, and what does its Explanation say?",
        "boxes": [
            ("7(4) AND 7(5): SECURITY STAFF",
             "Staff of organisations in the RTI Act Second Schedule need clearance to publish. Format 1 undertaking; Head of the Organisation decides.",
             "Rule 7(4) (omitted by the script; close restatement): employees of intelligence and security organisations listed in the Second Schedule to the Right to Information Act, 2005 shall not publish any material relating to the domain of their organisation without the prior clearance of the Head of the Organisation; they give an undertaking in Format 1; breach is grave misconduct; on transfer out, the undertaking is made in duplicate and one copy goes into the service book. Rule 7(5): the Head of the Organisation decides whether a proposed publication is sensitive and within the domain. Note: Format 1 is this undertaking under Rule 7(4)(b).",
             PINK,
             "The script left out sub-rules four and five. Staff of the intelligence and security organisations listed in the Second Schedule of the Right to Information Act, two thousand five, may not publish material about their organisation's field without prior clearance of the Head of the Organisation. They sign an undertaking in Format one. A breach is grave misconduct. The Head of the Organisation decides what is sensitive."),
            ("7(6) AND 7(7): UPSC AND APPEAL",
             "If the President is the competent authority, consult UPSC first. Appeal against another authority's order goes to the President, who decides with UPSC.",
             "Rule 7(6): if the President is the competent authority, the Union Public Service Commission (UPSC) must be consulted before an order is passed. Rule 7(7): an appeal against a sub-rule (1) order of an authority other than the President lies to the President, who decides in consultation with the UPSC. Confirmed (close restatement). UPSC is the constitutional body that advises Government on such matters.",
             BLUE,
             "Sub-rule six: if the President is the competent authority, the Union Public Service Commission must be consulted before the order. Sub-rule seven: an appeal against an order of any other authority goes to the President, who decides after consulting the Commission."),
            ("THE EXPLANATION",
             "Pension includes family pension; pensioner includes family pensioner. It also defines serious crime, grave misconduct, publication and information.",
             "Rule 7 Explanation (confirmed in part): pension includes family pension and pensioner includes family pensioner. The Explanation also defines serious crime (including offences under the Official Secrets Act, 1923), grave misconduct, publication and information; the script mentions only the first point. The full wording of those definitions was not read: check the Gazette text.",
             GREEN,
             "The Explanation says pension includes family pension, and pensioner includes a family pensioner. It also defines serious crime, which includes offences under the Official Secrets Act nineteen twenty-three, and grave misconduct, publication and information. The script mentioned only the first point, and we have not read the full definitions."),
            ("EXAMPLE AND TRAP",
             "Example: Asha, in a listed organisation, plans a book about her work. She needs prior clearance. Trap: Format 1 is NOT an application.",
             "Example (invented): Asha works in an organisation named in the Second Schedule to the RTI Act. She gives the Format 1 undertaking and later wants to publish a book on her work; she must first obtain the Head of the Organisation's clearance. Publishing without clearance is grave misconduct under Rule 7(4) (teacher's reading: this can bring Rule 7(1)(b) into play). Trap: the script treated Format 1 as the commercial-employment application; it is the Rule 7(4)(b) undertaking, while commercial employment uses Form 1 (Rule 9).",
             RED,
             "Here is a real example. Asha works in a listed organisation and wants to publish a book about her work. She must first get clearance from the Head of the Organisation. Be careful, this is the trap: Format one is the undertaking under Rule seven, not an application for commercial employment."),
        ],
        "hook": "REMEMBER: Rule 7(4) = Format 1 undertaking • 7(6) UPSC if President • 7(7) appeal to President!",
        "hook_say": "Remember: Rule seven, four, has the Format one undertaking, sub-rule six needs the Commission if the President is the authority, and sub-rule seven sends the appeal to the President.",
        "covers": ["R7(4)", "R7(5)", "R7(6)", "R7(7)", "R7-EXPL", "FORMAT-1"],
    },
    {
        "id": "c1_19_rule8_chain",
        "chapter": "CHAPTER 19 • RULE 8(1): WHO CAN WITHHOLD PENSION FOR MISCONDUCT IN SERVICE",
        "title": "RULE 8(1) — FROM A MISCONDUCT FINDING TO THE DECIDING AUTHORITY",
        "accent": SKY, "badge": "RULE 8(1) • 6A",
        "q": "A pensioner is found guilty of grave misconduct in service. Who acts, and where is the appeal?",
        "q_say": "Sir, a pensioner was found guilty of grave misconduct during service. How do we find who acts and where the appeal goes?",
        "flow": "r8chain",
        "boxes": [
            ("STEP 1: THE TRIGGER",
             "Proceedings show grave misconduct or negligence in service (even in re-employment).",
             "Rule 8(1) as substituted by G.S.R. 770(E) of 07.10.2022: if, in departmental or judicial proceedings, the pensioner is found guilty of grave misconduct or negligence during service, including service rendered on re-employment after retirement, the competent authority may withhold or withdraw pension or gratuity or both, in whole or part, permanently or for a specified period, and may order recovery from the pension of the whole or part of any pecuniary loss caused to the Government. Confirmed (close restatement; not read verbatim from the Gazette). Pecuniary loss means loss of money.",
             SKY,
             "Step one is the trigger. In departmental or court proceedings, the pensioner is found guilty of grave misconduct or negligence during service, including service on re-employment. Then the competent authority may withhold or withdraw pension or gratuity or both, in whole or in part, for ever or for a period, and may order recovery of the Government's money loss."),
            ("STEP 2: WHO DECIDES",
             "Look at the post's appointing authority: President, or Secretary of the Ministry, or the C&AG for Audit and Accounts staff.",
             "Three authorities after the 2022 amendment (GSR770-1, confirmed): (a) the President, where the President is the appointing authority of the post; (b) the Secretary of the Administrative Ministry or Department, where the appointing authority is subordinate to the President; (c) the Comptroller and Auditor General (C&AG), for a pensioner of the Indian Audit and Accounts Department holding a post whose appointing authority is subordinate to the President. The test is the appointing authority of the post, not the rank of the pensioner or the gravity of the misconduct (R8-3AUTH confirmed). OBSOLETE / HISTORY ONLY: before 07.10.2022 the President alone held this power; replaced by G.S.R. 770(E) (three authorities). Cases (neutral, not assumptions about particular posts): a post whose appointing authority is the President means the President decides; a post whose appointing authority is subordinate means the Secretary decides; an Audit and Accounts Department post means the C&AG decides.",
             BLUE,
             "Step two is who decides. Before October two thousand twenty-two the President alone held this power; that is history only. Now it depends on the post's appointing authority. If it is the President, the President acts. If it is subordinate, the Secretary of the Ministry acts. For Audit and Accounts staff, the Comptroller and Auditor General acts. Rank and gravity are not the test."),
            ("STEP 3: UPSC",
             "If the President passes the final order, the UPSC must be consulted first. Not needed when the President is not the appointing authority.",
             "First proviso to Rule 8(1): the UPSC shall be consulted before a final order is passed by the President. Confirmed; not needed where the President is not the appointing authority. The DoPPW O.M. F.No. 38/41/19-P&PW(A) dated 10.04.2023 explains the amended rule: the President decides only if he is the appointing authority; otherwise the Secretary or the C&AG decides; UPSC consultation is not needed where the President is not the appointing authority; and a case where a subordinate authority has not yet sent its findings to the President need not go to the President. Confirmed.",
             GREEN,
             "Step three is the Union Public Service Commission. If the President passes the final order, the Commission must be consulted first. If the Secretary or the C&AG decides, that consultation is not needed. A memorandum of ten April two thousand twenty-three explains this, in file number thirty-eight slash forty-one slash nineteen."),
            ("STEP 4: APPEAL • RULE 8(6A)",
             "No appeal against the President's order. An order of any other authority is appealed to the President, who consults UPSC.",
             "Rule 8(6A), inserted by G.S.R. 770(E): (a) there is no appeal against an order of the President; (b) an appeal against a Rule 8(1) order of any other authority lies to the President, who decides in consultation with the UPSC. Confirmed (close restatement). Scheme is symmetrical: where the President decides first, the UPSC has already been consulted, so no appeal. Trap: the script's cases saying the President decides for Secretary-level posts, or that an Under Secretary is appointed by the Appointments Committee of the Cabinet, are assumptions about particular posts (BONUS-9-CASES): do not state them as fact; apply the appointing-authority test.",
             RED,
             "Step four is the appeal. There is no appeal against an order of the President. An order of any other authority can be appealed to the President, who decides after consulting the Commission. Be careful: the script's examples named particular posts and their authorities, which were assumptions. Always use the test of the post's appointing authority."),
        ],
        "hook": "REMEMBER: test = appointing authority of the POST • President, Secretary or C&AG • no appeal from the President!",
        "hook_say": "Remember: the test is the appointing authority of the post. It is the President, the Secretary or the C and A G, and there is no appeal against the President's own order.",
        "covers": ["R8(1)", "R8(1)-ORIG", "GSR770-1", "R8-3AUTH", "R8(1)-PROV1", "OM-10.04.2023-8", "R8(6A)", "GSR770-3", "BONUS-9-CASES"],
    },
    {
        "id": "c1_20_rule8_procedure",
        "chapter": "CHAPTER 20 • RULE 8: THE FLOOR, PROCEEDINGS AND PROVISIONAL PENSION",
        "title": "RULE 8 — THE FLOOR, HOW PROCEEDINGS RUN, AND PENSION IN THE MEANTIME",
        "accent": ORANGE, "badge": "RULE 8(1)-(5)",
        "q": "How low can part-withholding go, and how do proceedings and provisional pension work?",
        "q_say": "Sir, how low can part-withholding go, and what happens to pension while proceedings are pending?",
        "boxes": [
            ("THE FLOOR • SECOND PROVISO",
             "Part-withholding cannot take pension below the Rule 44 minimum. The reported figure is Rs 9,000, but check the latest O.M.",
             "Second proviso to Rule 8(1): where a part of the pension is withheld or withdrawn, the pension shall not be reduced below the minimum pension under Rule 44. Confirmed. The floor applies only to part withholding (not to full withdrawal) and only to pension (not to gratuity): a reasonable reading of the provisos (BONUS-8-FLOOR confirmed). The minimum pension figure is reported as Rs 9,000 per month (ADD-B1-4, 7th CPC level), reported current at 07.09.2026 from a secondary source; the 8th Pay Commission has not reported. The Rule 44 text was not read: figure moves by executive order, so check the latest O.M.",
             ORANGE,
             "Let us start with the floor. If only part of the pension is withheld or withdrawn, the pension cannot go below the minimum pension under Rule forty-four. It applies to part withholding only, and to pension, not gratuity. The reported minimum is nine thousand rupees a month, from a secondary source, so check the latest memorandum."),
            ("8(2)(a) AND 8(2)(b)",
             "Proceedings begun in service continue after retirement. Proceedings under CCS (CCA) Rule 16 do not affect pension or gratuity.",
             "Rule 8(2)(a): departmental proceedings begun while the servant was in service continue after retirement under this rule (close restatement). Its proviso, as substituted by G.S.R. 770(E): where an authority subordinate to the competent authority begins departmental proceedings, it must submit a report of its findings to the competent authority (GSR770-2 / current wording; close restatement). OBSOLETE / HISTORY ONLY: the earlier proviso sent the subordinate authority's report to the President; the script's wording that such proceedings are deemed initiated by the appointing authority was not found in any source read. Rule 8(2)(b): proceedings under Rule 16 of the CCS (CCA) Rules, 1965 (minor penalty proceedings) do not affect pension or gratuity.",
             SKY,
             "Sub-rule two, clause a: proceedings begun in service carry on after retirement. Its proviso now says a subordinate authority that starts proceedings must send its findings to the competent authority; earlier it went to the President, and that is history only. The script's wording about proceedings being deemed started by the appointing authority was not found. Clause b: proceedings under Rule sixteen of the old conduct rules do not touch pension."),
            ("8(2)(c) AND 8(2)(d)",
             "Proceedings first started after retirement need sanction in Format 2, a memorandum in Format 3, and no event older than 4 years.",
             "Rule 8(2)(c): proceedings first instituted after retirement need sanction (Format 2) and a memorandum (Format 3), and no event more than four years before the institution may be inquired into (TL-R8-4Y). 8(2)(c) was amended by G.S.R. 770(E); the new wording was not read. Rule 8(2)(d): no further show-cause notice is needed if a full inquiry has already given the pensioner an opportunity. Close restatements; the script omitted these.",
             GREEN,
             "Clause c: proceedings first started after retirement need a sanction in Format two and a memorandum in Format three, and no event older than four years can be inquired into. This clause was amended in two thousand twenty-two, and the new wording was not read. Clause d: no further show-cause is needed if a full inquiry gave the pensioner an opportunity."),
            ("8(3)-(5): INTERIM PENSION",
             "While proceedings are pending: provisional pension up to the maximum admissible; no gratuity until final orders; adjusted later.",
             "Rules 8(3) to 8(5) (close restatement): during pending proceedings, the pensioner gets provisional pension (the Accounts Officer authorises it up to the maximum admissible); no gratuity is paid until final orders; provisional pension is not given where there is only an investigation or proceedings are only contemplated; it is adjusted against the final benefits and any excess is not recovered. Rule 8(4)(d) was amended by G.S.R. 770(E); the new wording was not read. Form 7, Part I, item 8 refers to provisional pension in terms of Rule 8 (R8-PROVISIONAL confirmed). Provisional pension means interim monthly pension paid while the case is pending.",
             PINK,
             "While proceedings are pending the pensioner gets a provisional pension, an interim monthly pension authorised by the Accounts Officer up to the maximum admissible. No gratuity is paid until final orders. It does not apply if there is only an investigation. The final orders adjust everything, and any excess is not recovered. Sub-rule four, clause d was amended in two thousand twenty-two."),
            ("EXAMPLE AND TRAP",
             "Example: pension Rs 40,000; floor Rs 9,000 means at most Rs 31,000 can be withheld. Trap: the floor does not protect gratuity.",
             "Example (invented, recomputed at the reported floor): Charu's pension is Rs 40,000 a month. If the authority withholds a part, the remaining pension cannot be lower than the Rule 44 minimum, reported as Rs 9,000; so at most Rs 40,000 minus Rs 9,000 equals Rs 31,000 can be withheld. If the minimum pension is revised, the answer changes. Trap: the floor does not apply to full withdrawal and does not protect gratuity.",
             RED,
             "Here is a real example. Charu's pension is forty thousand rupees. At the reported nine thousand rupee floor, at most thirty-one thousand can be withheld, because forty minus nine is thirty-one. If the minimum is revised the answer changes. Be careful: the floor does not protect gratuity and does not apply to full withdrawal."),
        ],
        "hook": "REMEMBER: floor = Rule 44 minimum (reported Rs 9,000) • part withholding only • 4-year limit • provisional pension while pending!",
        "hook_say": "Remember: the floor is the Rule forty-four minimum pension, reported at nine thousand rupees. It applies to part withholding only, there is a four year limit on new proceedings, and a provisional pension is paid while a case is pending.",
        "covers": ["R8(1)-PROV2", "BONUS-8-FLOOR", "ADD-B1-4-9000", "R8(2)(a)", "R8(2)(a)-PROV-ORIG", "GSR770-2", "R8(2)(b)", "R8(2)(c)", "R8(2)(d)", "R8(3)-(5)", "R8-PROVISIONAL", "FORMAT-2-3", "TL-R8-4Y"],
    },
    {
        "id": "c1_21_rule8_end",
        "chapter": "CHAPTER 21 • RULE 8: RECOVERY LIMIT, REVISION AND EXPLANATIONS",
        "title": "RULE 8(6) TO 8(8) AND THE EXPLANATIONS — RECOVERY, REVIEW, MEANINGS",
        "accent": GREEN, "badge": "RULE 8(6)-(8)",
        "q": "How much can be recovered from pension, and what do the last sub-rules and Explanations of Rule 8 add?",
        "q_say": "Sir, how much can be recovered from pension, and what do the last sub-rules and Explanations of Rule eight say?",
        "boxes": [
            ("8(6): ONE-THIRD LIMIT",
             "Recovery of loss from pension should not ordinarily go above one-third of the pension admissible on retirement.",
             "Rule 8(6): recovery of pecuniary loss from the pension shall not ordinarily exceed one-third of the pension admissible on retirement (TL-R8-1/3 confirmed; close restatement). Rule 8(6) was amended by G.S.R. 770(E); the new wording was not read. Example (invented, recomputed): if Dev's admissible pension is Rs 60,000, one-third is Rs 20,000; recovery from the pension should not ordinarily go above Rs 20,000. The script omitted this limit.",
             GREEN,
             "Sub-rule six sets a limit. Recovery of a money loss from the pension should not ordinarily go above one-third of the pension admissible on retirement. If Dev's admissible pension is sixty thousand rupees, one-third is twenty thousand. This sub-rule was also amended in two thousand twenty-two, and we did not read the new wording."),
            ("8(6A): APPEAL ROUTE",
             "No appeal against the President's order; other authorities' orders are appealed to the President, with UPSC.",
             "Rule 8(6A) (inserted by G.S.R. 770(E) of 07.10.2022): (a) no appeal against an order of the President; (b) an appeal against an order of any other authority under sub-rule (1) lies to the President, who decides in consultation with the UPSC. Confirmed (close restatement). Covered with the decision chain in chapter 19.",
             BLUE,
             "Sub-rule six A is the appeal route we met in the decision chain: no appeal from the President's order, and appeals against other authorities go to the President after consulting the Commission."),
            ("8(7) AND 8(8)",
             "The President may call for records and revise, after UPSC. The President may review on new material. Reasonable chance to represent before increasing a penalty.",
             "Rules 8(7) and 8(8) (close restatement; omitted by the script): the President may call for the records of a case and revise an order after consulting the UPSC; the President may review an order on extenuating circumstances or new material; before the amount of any penalty is increased, the pensioner must have a reasonable chance to represent. Confirmed.",
             ORANGE,
             "Sub-rules seven and eight: the President may call for records and revise an order after consulting the Commission, and may review it if there are extenuating circumstances or new material. Before any increase in the penalty, the pensioner must have a reasonable chance to put his case."),
            ("THE EXPLANATIONS (1) TO (4)",
             "They fix when proceedings are 'instituted', what misconduct includes, corrupt practices, and that civil proceedings means suits by Government.",
             "Rule 8 Explanations (1) to (4) (close restatement; confirmed in substance, but the wording in the copy read is partly garbled): proceedings are treated as instituted, for departmental proceedings, on the date of charge-sheet or suspension and, for judicial proceedings, on the date of cognizance or filing; misconduct covers breach of the CCS (Conduct) Rules, including during re-employment; corrupt practices are included; civil proceedings means suits filed by the Government. Check the Gazette text for the exact wording. Cognizance means the court formally taking up the case.",
             PINK,
             "Rule eight has four Explanations. They say when proceedings count as instituted, such as on the charge-sheet or suspension date, or the date of cognizance or filing in court. Misconduct covers breach of the conduct rules, even in re-employment. Corrupt practices are included, and civil proceedings means suits filed by the Government. The copy we read was partly garbled, so check the Gazette."),
        ],
        "hook": "REMEMBER: recovery not above one-third • President can revise and review • four Explanations define the terms!",
        "hook_say": "Remember: recovery is not ordinarily above one-third of the pension, the President can revise and review, and four Explanations define the terms.",
        "covers": ["R8(6)", "R8(7)-(8)", "R8-EXPL", "TL-R8-1/3", "GSR770-EXTRA", "R8(6A)"],
    },
    {
        "id": "c1_22_rule7_vs_8",
        "chapter": "CHAPTER 22 • COMPARISON: RULE 7 VERSUS RULE 8",
        "title": "RULE 7 VERSUS RULE 8 — TWO DOORS TO WITHHOLDING PENSION",
        "accent": PINK, "badge": "RULE 7 vs RULE 8",
        "q": "Both rules can stop a pension. How do I tell them apart?",
        "q_say": "Sir, both Rule seven and Rule eight can stop a pension. How do I tell them apart?",
        "boxes": [
            ("DIFFERENCE 1: THE TRIGGER",
             "Rule 7: conviction for serious crime or grave misconduct (usually after retirement). Rule 8: guilt in proceedings for misconduct DURING service.",
             "Rule 7 trigger: the pensioner is convicted of a serious crime or found guilty of grave misconduct (future good conduct; mostly post-retirement conduct or a court conviction). Rule 8 trigger: departmental or judicial proceedings find grave misconduct or negligence during service, including re-employment. Confirmed (BONUS-8-4DIFF, mostly right).",
             PINK,
             "First difference: the trigger. Rule seven is about good conduct after retirement, a conviction for a serious crime or grave misconduct. Rule eight is about grave misconduct or negligence during service, found in departmental or court proceedings."),
            ("DIFFERENCE 2: THE AUTHORITY",
             "Rule 7: the Appointing Authority. Rule 8: President, Secretary or C&AG, by the post's appointing authority.",
             "Rule 7(1)(b): the Appointing Authority acts; the President comes in under 7(6) and 7(7). Rule 8(1): after G.S.R. 770(E), three authorities (President, Secretary of the Administrative Ministry or Department, C&AG) according to the appointing authority of the post. Confirmed.",
             BLUE,
             "Second difference: the authority. Under Rule seven it is the Appointing Authority. Under Rule eight there are three, the President, the Secretary or the Comptroller and Auditor General, chosen by the post's appointing authority."),
            ("DIFFERENCE 3: THE POWER",
             "Rule 7 deals with pension only. Rule 8 can reach pension, gratuity or both, and order recovery of the Government's loss.",
             "Rule 7 speaks of pension or any part of it. Rule 8 is wider: pension or gratuity or both can be withheld or withdrawn, in whole or part, and recovery of pecuniary loss can be ordered. Confirmed.",
             GREEN,
             "Third difference: the power. Rule seven speaks only of pension. Rule eight is wider: pension or gratuity or both, and also recovery of the Government's loss."),
            ("DIFFERENCE 4: THE APPEAL",
             "Both lead to the President on appeal. Under Rule 8(6A) there is no appeal from the President's own order.",
             "Correction to the script (BONUS-8-4DIFF): an appeal to the President exists in both rules (Rule 7(7) and Rule 8(6A)(b)); the extra feature of Rule 8 is the express bar on appeal against the President's own order, Rule 8(6A)(a), introduced in 2022. Confirmed.",
             ORANGE,
             "Fourth difference: the appeal. The script made this look like only Rule eight, but both rules send appeals to the President. The special feature of Rule eight is that there is no appeal against the President's own order."),
            ("WHAT THEY SHARE",
             "A floor: part withholding cannot go below the Rule 44 minimum. Only pension, not gratuity, and only part, not full withdrawal.",
             "Common: the proviso to Rule 7(1) and the second proviso to Rule 8(1) both set the Rule 44 minimum pension as the floor for part withholding. Reasonable reading (BONUS-8-FLOOR confirmed): the floor protects pension only (not gratuity) and only against partial withholding (not full withdrawal). Trap: do not assume rank or seriousness decides who acts; the appointing authority test governs Rule 8.",
             RED,
             "What do they share? A floor. Under both rules, part withholding cannot reduce the pension below the Rule forty-four minimum. The floor protects only the pension, not the gratuity, and only against part withholding. Be careful: rank and seriousness do not decide the authority."),
        ],
        "hook": "REMEMBER: Rule 7 = conduct after retirement, Appointing Authority • Rule 8 = misconduct in service, three authorities!",
        "hook_say": "Remember: Rule seven is about conduct after retirement and the Appointing Authority. Rule eight is about misconduct in service and three possible authorities.",
        "covers": ["BONUS-8-4DIFF", "BONUS-8-FLOOR"],
    },
    {
        "id": "c1_23_rule9_main",
        "chapter": "CHAPTER 23 • RULE 9: COMMERCIAL EMPLOYMENT AFTER RETIREMENT (PART 1)",
        "title": "RULE 9(1) AND 9(2) — SANCTION FOR A JOB IN THE FIRST YEAR AFTER RETIREMENT",
        "accent": ORANGE, "badge": "RULE 9(1)-(2)",
        "q": "A retired senior officer wants a private-sector job. When does he need permission, and on which form?",
        "q_say": "Sir, a retired senior officer wants a private job. When does he need permission, and on which form?",
        "boxes": [
            ("THE RULE • 9(1)",
             "A pensioner who was in Central Service Group A just before retiring needs prior Government sanction for commercial employment within 1 year, on Form 1.",
             "Rule 9(1): a pensioner who, immediately before retirement, was a member of Central Service Group A, and who wishes to take up commercial employment within one year of retirement, must obtain the previous sanction of the Government; application is made in Form 1 (titled: application for permission to accept commercial employment within one year after retirement). Time limit TL-R9-1Y confirmed. Group A is the senior-most group of officers. Commercial employment means a job with a business or company. Confirmed (close restatement).",
             ORANGE,
             "Let us take the rule first. A pensioner who was a Group A officer in Central Service just before retiring needs the Government's prior sanction for any commercial employment within one year of retirement. The application is made on Form one."),
            ("THE TWO PROVISOS",
             "No new permission to continue a job already permitted during leave preparatory to retirement. And no job talks in service without the Ministry's prior permission.",
             "First proviso: permission already given during leave preparatory to retirement for a particular employment need not be taken again to continue in that employment after retirement (confirmed for leave preparatory to retirement). The script adds 'or refused leave': that part was not found in the text read. Second proviso: no negotiation for commercial employment during service without the prior permission of the administrative Ministry or Department, which is given only for special reasons. Confirmed (close restatement).",
             GREEN,
             "Two provisos. First, if permission for a particular job was already given while the officer was on leave preparatory to retirement, no fresh permission is needed to continue. The script also mentioned refused leave, which we could not find. Second, during service, he may not even negotiate for a commercial job without the Ministry's prior permission, given only for special reasons."),
            ("9(2): GRANT OR REFUSE",
             "Government may grant with conditions or refuse. A refusal needs recorded reasons.",
             "Rule 9(2): the Government may grant the permission, with or without conditions, or refuse it; refusal is with reasons recorded. Confirmed (close restatement). The script skipped this sub-rule.",
             BLUE,
             "Sub-rule two: the Government may grant the permission, with conditions if it wishes, or refuse. If it refuses, the reasons are recorded."),
            ("EXAMPLE",
             "Bilal retired 31.03.2026 and takes a job on 15.01.2027: inside the year, needs sanction. Esha retired 31.03.2026 and takes one on 10.05.2027: outside Rule 9.",
             "Example (invented, recomputed): Bilal, a Group A officer, retires on 31.03.2026. The one-year window runs to 31.03.2027. He wants to join a private firm on 15.01.2027, inside the window, so he applies in Form 1. Esha, also retiring on 31.03.2026, wants to join a firm on 10.05.2027, after the window, so Rule 9 does not ask for sanction (employment abroad under a Government is different: Rule 10 has no time limit).",
             SKY,
             "Here is a real example. Bilal, a Group A officer, retires on thirty-one March two thousand twenty-six. His one-year window ends on thirty-one March two thousand twenty-seven. A job on fifteen January two thousand twenty-seven is inside the window, so he needs sanction on Form one. Esha wants a job on ten May two thousand twenty-seven, which is after the window, so Rule nine does not ask her."),
            ("FORM 1 AND FORM 2: DO NOT MIX",
             "Form 1 is the pensioner's application. Form 2 is the Ministry's own checklist under 9(5). Format 1 is something else.",
             "Rule 9(5): the administrative Ministry keeps a checklist in Form 2 (a record for the office, not a claim form). FORM-1 and FORM-2 confirmed. CORRECTION to the script's ADD-B1-5: the script listed Format 1 as the commercial-employment application and flagged the position as unclear; Format 1 is the Rule 7(4)(b) undertaking for intelligence and security staff, and commercial employment uses Form 1 and Form 2. The unclear-instrument flag is no longer needed (R9-FORM1FORMAT1, FORMAT-1).",
             RED,
             "Be careful with the forms. Form one is the pensioner's own application. Form two is the Ministry's internal checklist under sub-rule five. And Format one is a different document, the security staff undertaking under Rule seven. The script confused this and its doubt is now settled."),
        ],
        "hook": "REMEMBER: Group A • 1 year after retirement • prior sanction on Form 1 • Form 2 = Ministry checklist!",
        "hook_say": "Remember: Group A, one year after retirement, prior sanction on Form one, and Form two is only the Ministry's checklist.",
        "covers": ["R9(1)", "R9(1)-PROV1", "R9(1)-PROV2", "R9(2)", "R9(5)", "FORM-1", "FORM-2", "R9-FORM1FORMAT1", "TL-R9-1Y"],
    },
    {
        "id": "c1_24_rule9_rest",
        "chapter": "CHAPTER 24 • RULE 9: COMMERCIAL EMPLOYMENT AFTER RETIREMENT (PART 2)",
        "title": "RULE 9(3) TO 9(8) — WHAT GOVERNMENT CHECKS, THE 30 DAYS, AND BREACH",
        "accent": BLUE, "badge": "RULE 9(3)-(8)",
        "q": "What does Government look at before granting permission, and what if the pensioner breaks the rule?",
        "q_say": "Sir, what does Government look at before granting permission, and what happens if the pensioner breaks the rule?",
        "boxes": [
            ("9(3): FACTORS (a) TO (d)",
             "Look at: (a) No Objection from cadre authority and retirement office; (b) sensitive information in last 3 years; (c) conflict of interest; (d) a hostile organisation.",
             "Rule 9(3) lists seven factors in substance (confirmed, close restatement): (a) a No Objection from the cadre controlling authority and the office of retirement; (b) whether in the last three years of service the servant had access to sensitive or strategic information of the organisation; (c) whether there is a conflict of interest; (d) whether the organisation acts against India's foreign relations, national security or domestic harmony, or gathers intelligence. The script says conflict of interest excludes normal economic competition: that was not seen in the text read.",
             BLUE,
             "Sub-rule three lists what the Government considers. Clause a: a No Objection from the cadre authority and the retirement office. Clause b: whether in the last three years the officer had access to sensitive or strategic information. Clause c: conflict of interest; the script says normal competition is excluded, which we could not confirm. Clause d: whether the organisation works against India's foreign relations, security or harmony, or gathers intelligence."),
            ("9(3): FACTORS (e) TO (g)",
             "(e) A clear service record; (f) pay far above industry rates; (g) any other relevant factor.",
             "Rule 9(3) continued: (e) whether the service record is clear; (f) whether the proposed emoluments are far in excess of the prevailing industry rates; (g) any other relevant factor. Seven factors, (a) to (g), confirmed in substance. TL-R9-LAST3Y (last three years) confirmed.",
             SKY,
             "Clause e: is the service record clear? Clause f: are the proposed emoluments far above industry rates? Clause g: any other relevant factor. That makes seven factors, a to g."),
            ("9(4), 9(6): HOW AND HOW LIBERAL",
             "Applications are considered under the Transaction of Business Rules 1961. If no disqualifying factor, be liberal, including consultancy and directorship.",
             "Rule 9(4): applications are considered under the Government of India (Transaction of Business) Rules, 1961 and current instructions (close restatement; the script omitted this and wrongly presented the same line as unique to Rule 10). Rule 9(6): if there is no disqualification under clauses (b) to (g), the Government should be liberal, including for directorship, consultancy and professional practice, with no distinction between honorary and paid work. Confirmed in substance.",
             GREEN,
             "Sub-rule four says applications are considered under the Transaction of Business Rules of nineteen sixty-one and current instructions. The script omitted this. Sub-rule six says that if none of clauses b to g blocks it, the Government should be liberal, including for directorship, consultancy and professional practice, whether honorary or paid."),
            ("9(7) AND 9(8): 30 DAYS AND BREACH",
             "Reply within 30 days of the order, with a show-cause before an adverse order. Breach can cost all or part of pension for set periods.",
             "Rule 9(7): the applicant may make a representation within thirty days of the order granting with conditions or refusing (TL-R9-30D confirmed); a show-cause notice is given before an adverse order. Rule 9(8): on breach, a reasoned order may say that pension, whole or part, is not payable for specified periods, after show-cause, having regard to the pensioner's financial circumstances, the nature of the employment and the emoluments. Confirmed. R9-15VS30: Rule 7(3) gives fifteen days; Rule 9(7) gives thirty: both confirmed.",
             ORANGE,
             "Sub-rule seven gives thirty days to make a representation against a conditional grant or refusal, and a show-cause notice comes before any adverse order. Sub-rule eight: on breach, a reasoned order may stop all or part of the pension for set periods, after show-cause, looking at the pensioner's circumstances, the job and the pay. Remember thirty here, not fifteen."),
            ("EXAMPLE AND FLAG",
             "Example: Dev's record is clear and no conflict, so sanction is likely. Flag: a current DoPT O.M. for Rule 9 was not found.",
             "Example (invented): Dev, a retired Group A officer with a clear record, wishes to become a consultant to a private firm that is not in conflict of interest and offers normal pay; no disqualification arises, so under Rule 9(6) the Government should be liberal. UNVERIFIED: the script says commercial-employment policy also runs through DoPT O.M.s; only a 2014 O.M. (No. 27012/3/2014-Estt(A), 19.11.2014, revising Form 25 under the old 1972 Rules) was found, and no current O.M. for Rule 9; the pensionersportal list could not be read (blocked by robots.txt). Check for any newer O.M.",
             PINK,
             "Here is a real example. Dev has a clear record, and the firm offers normal pay with no conflict of interest. No disqualifying factor arises, so the Government should be liberal. One flag: the script says DoPT memoranda also guide this area, but we found only an old two thousand fourteen one under the earlier rules. Check for any newer memorandum."),
        ],
        "hook": "REMEMBER: seven factors • last 3 years • representation within 30 days, not 15 • breach = pension stopped for set periods!",
        "hook_say": "Remember: seven factors, the last three years of service, thirty days to make a representation and not fifteen, and a breach can stop the pension for set periods.",
        "covers": ["R9(3)", "R9(4)", "R9(6)", "R9(7)", "R9(8)", "R9-15VS30", "R9-DOPT-FORM25", "EX-R9", "TL-R9-LAST3Y", "TL-R9-30D"],
    },
    {
        "id": "c1_25_rule10",
        "chapter": "CHAPTER 25 • RULE 10 AND THE COMPARISON WITH RULE 9",
        "title": "RULE 10 — A GOVERNMENT JOB ABROAD, AND HOW IT DIFFERS FROM RULE 9",
        "accent": GREEN, "badge": "RULE 10 vs RULE 9",
        "q": "What does Rule 10 say about employment abroad, and is it just Rule 9 again?",
        "q_say": "Sir, what does Rule ten say about employment abroad, and is it just Rule nine again?",
        "boxes": [
            ("THE RULE • 10(1)",
             "A Group A pensioner needs previous Central Government permission for employment under any Government outside India. No permission, no pension for that period.",
             "Rule 10(1): a pensioner who, immediately before retirement, was a member of Central Service Group A, and who wishes to take employment under any Government outside India, must obtain the previous permission of the Central Government; if he takes such employment without proper permission, no pension is payable for the period of employment or for such longer period as the Government directs. Proviso: permission given during leave preparatory to retirement for a particular employment need not be repeated to continue after retirement. Confirmed (close restatement).",
             GREEN,
             "Let us take the rule first. A pensioner who was a Group A officer in Central Service just before retiring needs the Central Government's previous permission for employment under any Government outside India. Without it, no pension is paid for that period, or for longer if the Government directs. A proviso lets permission given during leave preparatory to retirement continue."),
            ("10(2) AND THE 30.10.2025 O.M.",
             "Requests are considered under the Transaction of Business Rules 1961 and current instructions. The 2025 O.M. restates this.",
             "Rule 10(2): requests are considered under the Government of India (Transaction of Business) Rules, 1961 and instructions issued from time to time. DoPPW O.M. F.No. 38/10(03)/2025-P&PW(A) (e 11193)(iv) dated 30.10.2025, subject: Employment after retirement under a Government outside India: number, date and subject confirmed; it restates Rule 10. CORRECTION to the script: the script presented the Transaction of Business line as new and as a contrast with Rule 9, but Rule 9(4) says the same. UNVERIFIED: the script's statement that the O.M. noted ambiguity about retired officers in advisory or consultancy roles abroad was not found in the summary read.",
             BLUE,
             "Sub-rule two says requests are considered under the Transaction of Business Rules of nineteen sixty-one and current instructions. A memorandum of thirty October two thousand twenty-five, with the suffix four in brackets, restates this. The script called it new and a contrast with Rule nine, but Rule nine has the same line. Its claim about advisory roles is not confirmed."),
            ("RULE 9 VERSUS RULE 10",
             "Rule 9: 1-year window, Form 1, a negotiation limb. Rule 10: no time limit, no form, no negotiation limb.",
             "Comparison (all confirmed): (1) time: Rule 9 has the one-year window after retirement; Rule 10 has no time limit (R9V10-1). (2) Form: Rule 9 prescribes Form 1; Rule 10 prescribes none (R9V10-2). (3) Negotiation during service without prior permission is a limb only of Rule 9 (R9V10-3). (4) Breach: Rule 9(8) is a reasoned order, after show-cause, that the whole or part of the pension is not payable for specified periods; Rule 10 says no pension for the period of employment or longer as the Government directs (R9V10-4). CORRECTION: the script said the breach effect is the same in both; the wording differs as stated.",
             ORANGE,
             "Compare the two. Rule nine has a one-year window; Rule ten has no time limit. Rule nine prescribes Form one; Rule ten prescribes none. Only Rule nine has the negotiation limb. On breach, Rule nine allows a reasoned order, after show-cause, stopping all or part of the pension for set periods, while Rule ten says no pension for the period or longer as directed."),
            ("EXAMPLE AND TRAP",
             "Example: Charu retired and, 2 years later, wants a post under a foreign Government: no one-year limit, still needs permission.",
             "Example (invented): Charu, a retired Group A officer, wishes to accept a post under a foreign Government two years after retirement. The one-year window of Rule 9 does not apply to Rule 10: she needs the Central Government's previous permission; if she joins without it, no pension is paid for that period or longer. Q and A: does the one-year limit apply to Rule 10? No, that is Rule 9's trigger. Trap: treating the two rules as the same.",
             RED,
             "Here is a real example. Charu wants a post under a foreign Government two years after retirement. The one-year limit is a Rule nine feature, so it does not apply, but she still needs the Central Government's previous permission. The trap is treating the two rules as the same."),
        ],
        "hook": "REMEMBER: Rule 10 = abroad • no time limit • no form • permission, else no pension for that period!",
        "hook_say": "Remember: Rule ten is for Government employment abroad, with no time limit and no form, and without permission no pension is paid for that period.",
        "covers": ["R10(1)", "R10-PROV", "R10(2)", "OM-30.10.2025-10", "R10-OM-AMBIG", "R9V10-1", "R9V10-2", "R9V10-3", "R9V10-4", "EX-R10"],
    },
    {
        "id": "c1_26_forms_formats",
        "chapter": "CHAPTER 26 • FORMS AND FORMATS MET IN RULES 1 TO 10",
        "title": "FORMS AND FORMATS IN RULES 1 TO 10 — WHICH DOCUMENT FOR WHICH RULE",
        "accent": SKY, "badge": "FORMS • FORMATS",
        "q": "Which Form or Format goes with which rule in this batch?",
        "q_say": "Sir, which Form or Format goes with which rule in this batch?",
        "boxes": [
            ("FORMS 1 AND 2 • RULE 9",
             "Form 1: application to accept commercial employment within a year of retirement. Form 2: the Ministry's checklist.",
             "Form 1: application for permission to accept commercial employment within one year after retirement (Rule 9(1)). Form 2: checklist under Rule 9(5) kept by the administrative Ministry. Both confirmed from the forms copy of the rules.",
             SKY,
             "Form one and Form two belong to Rule nine. Form one is the application. Form two is the Ministry's checklist."),
            ("FORMATS 1, 2, 3",
             "Format 1: security staff undertaking, Rule 7(4)(b). Formats 2 and 3: sanction and memorandum for proceedings after retirement, Rule 8(2)(c).",
             "Format 1: undertaking by employees of intelligence or security organisations, Rule 7(4)(b). Format 2: sanction for proceedings first instituted after retirement, Rule 8(2)(c)(i); Format 3: the memorandum, per the book summary. Confirmed. Format 4: certificate of verification of service, used in the Rule 30 verification (the next batch); FORMAT-4 confirmed from the forms copy.",
             BLUE,
             "Format one is the security staff undertaking under Rule seven. Formats two and three are the sanction and the memorandum for proceedings first started after retirement under Rule eight. Format four is the certificate of verification of service, used with Rule thirty in the next batch."),
            ("FORM 6-A AND THE COUNTS",
             "Form 6-A is the single pension application from 16.11.2024. The script says 13 Forms and 13 Formats: not confirmed.",
             "Form 6-A: introduced by G.S.R. 410(E), effective 16.11.2024 (FORM-6A confirmed; see chapter 29). Counts: the script's 13 Forms and 13 Formats were not checked in this batch (FORM-FORMAT-13 unverified); the script's 87 rules and 14 chapters were not checked either (COUNT-87-14 unverified).",
             GREEN,
             "Form six A is the single pension application introduced by the two thousand twenty-four amendment, effective sixteen November two thousand twenty-four. The script says there are thirteen Forms and thirteen Formats, and eighty-seven rules in fourteen chapters, but we did not check those counts."),
            ("THE TRAP",
             "A Form is usually an application; a Format a template or undertaking. This is a study aid, not rule text.",
             "R3-TRAP-FORMFORMAT (unverified as rule text): Rule 3 says only appended form and appended format. The rule of thumb that a Form is a statutory application and a Format a template or undertaking is a study aid; it fits Form 1 (application) against Format 1 (undertaking). Exam habit: check the number AND the word.",
             RED,
             "Be careful, this is the trap. Form versus Format is a study aid, not rule text. It fits Form one, an application, against Format one, an undertaking, but always check both the word and the number."),
        ],
        "hook": "REMEMBER: Form 1-2 = Rule 9 • Format 1 = Rule 7(4) • Formats 2-3 = Rule 8(2)(c) • check word AND number!",
        "hook_say": "Remember: Forms one and two belong to Rule nine, Format one to Rule seven, Formats two and three to Rule eight, and always check both the word and the number.",
        "covers": ["FORM-6A", "FORMAT-4", "COUNT-87-14"],
    },
    {
        "id": "c1_27_time_limits",
        "chapter": "CHAPTER 27 • TIME LIMITS AND THRESHOLDS IN RULES 1 TO 10",
        "title": "EVERY TIME LIMIT IN RULES 1 TO 10 ON ONE LADDER",
        "accent": ORANGE, "badge": "TIME LIMITS",
        "q": "Which time limits and fractions must I remember from these ten rules?",
        "q_say": "Sir, which time limits and fractions must I remember from these ten rules?",
        "flow": "timeladder",
        "boxes": [
            ("DAYS: 15+15 AND 30",
             "Rule 7(3): 15 days to reply, plus up to 15 more. Rule 9(7): 30 days.",
             "Days: Rule 7(3) representation within fifteen days, extendable by up to a further fifteen (TL-R7-15D); Rule 9(7) representation within thirty days (TL-R9-30D). Do not mix them (R9-15VS30).",
             SKY,
             "Days first. Under Rule seven you get fifteen days to reply, extendable by fifteen. Under Rule nine, sub-rule seven, you get thirty days. Do not swap them."),
            ("MONTHS: 6 IN RULE 4",
             "Rule 4: 6 months to elect, from the order or return from leave, whichever is later.",
             "Months: Rule 4 proviso, six months from the transfer order, or from return from leave if he was on leave that day, whichever is later (TL-R4-6M).",
             BLUE,
             "Months: Rule four gives six months to choose, counted from the later of the transfer order or the return from leave."),
            ("YEARS: 1, 3 AND 4",
             "Rule 9: 1-year window. Rule 9(3): last 3 years of service. Rule 8(2)(c): no event over 4 years before.",
             "Years: Rule 9(1) one year after retirement (TL-R9-1Y); Rule 9(3) the last three years of service for sensitive information (TL-R9-LAST3Y); Rule 8(2)(c) no event more than four years before institution (TL-R8-4Y). The 120 days of G.S.R. 410(E) (the 2024 amendment) run from publication in the Gazette. Recomputed: 120 days from 16.07.2024 ends on 13.11.2024, not 16.11.2024; 16.11.2024 would fit a Gazette publication on 19.07.2024, but that publication date was not read. So 16.11.2024 rests on a secondary source (Outlook Money) and is consistent with the DoPPW O.M. of 11.09.2024; the exact Gazette publication date is unverified (TL-GSR410-120D: the 120-day period is confirmed).",
             GREEN,
             "Years: Rule nine has a one-year window, the last three years of service matter for sensitive information, and under Rule eight, sub-rule two, clause c, no event more than four years before can be inquired into. The two thousand twenty-four amendment starts after one hundred twenty days. Counted from its sixteen July date that ends on thirteen November, so the reported sixteen November start suggests a later Gazette publication date, which we did not read."),
            ("FRACTION: ONE-THIRD",
             "Rule 8(6): recovery from pension not ordinarily above one-third of the pension admissible on retirement.",
             "Fraction: Rule 8(6) one-third (TL-R8-1/3). Example (recomputed): pension Rs 60,000 means a one-third limit of Rs 20,000. Trap: the Rule 44 floor in Rules 7 and 8 is a rupee floor, not a fraction.",
             RED,
             "Finally the fraction. Recovery from the pension is not ordinarily above one-third. On sixty thousand rupees, that is twenty thousand. Do not confuse it with the Rule forty-four floor, which is a rupee amount, not a fraction."),
        ],
        "hook": "REMEMBER: 15+15 and 30 days • 6 months • 1, 3 and 4 years • one-third!",
        "hook_say": "Remember: fifteen plus fifteen and thirty days, six months, one, three and four years, and one-third.",
        "covers": ["TL-GSR410-120D"],
    },
    {
        "id": "c1_28_gsr770",
        "chapter": "CHAPTER 28 • AMENDMENT 1: G.S.R. 770(E) OF 07.10.2022",
        "title": "THE 2022 AMENDMENT — G.S.R. 770(E), WHAT IT CHANGED",
        "accent": RED, "badge": "G.S.R. 770(E)",
        "q": "What exactly did the October 2022 amendment change, and was the count of six changes right?",
        "q_say": "Sir, what exactly did the October two thousand twenty-two amendment change, and were there only six changes?",
        "boxes": [
            ("THE DATE",
             "G.S.R. 770(E) dated 07.10.2022. Start on publication: not confirmed on the page read.",
             "G.S.R. 770(E) dated 7 October 2022 confirmed (GSR770-DATE). The script says it came into force on publication; this commencement was not stated on the page read, so mark it unverified. The Gazette text itself was not read: every change below is a close restatement from secondary summaries (ADD-B1-6-ARTICLE unverified).",
             RED,
             "The first amendment is G.S.R. seven seven zero E, dated seven October two thousand twenty-two. The script says it started on publication, but the page we read did not say so, so that is unverified. We did not read the Gazette text itself, so all changes are close restatements."),
            ("RULE 8 CHANGES",
             "Rule 8(1) replaced (three authorities); the proviso to 8(2)(a) replaced; new Rule 8(6A) on appeals.",
             "Change 1: Rule 8(1) substituted, with the power spread across the President, the Secretary of the Administrative Ministry or Department and the C&AG (GSR770-1 confirmed). Change 2: the proviso to Rule 8(2)(a) substituted; current wording: a subordinate authority beginning departmental proceedings submits a report of its findings to the competent authority; the script's 'deemed initiated by the appointing authority' wording was not found (GSR770-2, changed). Change 3: new Rule 8(6A), no appeal against the President's order, other orders appealed to the President with UPSC (GSR770-3 confirmed).",
             ORANGE,
             "The Rule eight changes: Rule eight, sub-rule one was replaced with three authorities. The proviso to sub-rule two, clause a was replaced; it now sends the subordinate authority's findings to the competent authority. And sub-rule six A on appeals is new."),
            ("OTHER THREE LISTED CHANGES",
             "Rule 20 Explanation 1(ii): 'not required to be refunded' became 'was to be refunded'. Rule 46(5)(a): 'proviso to' dropped. Rule 76: second (5) renumbered (5A).",
             "Change 4: Rule 20, Explanation 1, clause (ii): 'was not required to be refunded' replaced by 'was to be refunded' (GSR770-4 confirmed; the content belongs to the Rule 20 chapter in Batch 2). Change 5: Rule 46(5)(a), the words 'proviso to' omitted (drafting; GSR770-5 confirmed). Change 6: Rule 76, the second '(5)' renumbered '(5A)' (GSR770-6 confirmed). Changes 5 and 6 are drafting clean-ups, not benefit or policy changes.",
             GREEN,
             "Three more listed changes. In Rule twenty, an Explanation changed from 'was not required to be refunded' to 'was to be refunded'; that belongs to the next batch. In Rule forty-six, the words 'proviso to' were dropped. In Rule seventy-six, a second sub-rule five became five A. The last two are only drafting clean-ups."),
            ("THE COUNT WAS WRONG",
             "At least ten changes: the page also lists Rules 8(2)(c), 8(4)(d), 8(6) and 50(9)(h). Wording of those four not read.",
             "The script says six changes only. The summarised page also lists amendments to Rule 8(2)(c), Rule 8(4)(d), Rule 8(6) and Rule 50(9)(h); the exact new wording was not read, so the count of six is incomplete: at least ten changes, wording of the extra four not verified (GSR770-EXTRA).",
             PINK,
             "The count of six is incomplete. The same page lists changes to Rule eight, sub-rule two clause c, sub-rule four clause d, sub-rule six, and to Rule fifty, sub-rule nine, clause h. So there are at least ten changes. The wording of those extra four was not verified."),
        ],
        "hook": "REMEMBER: G.S.R. 770(E) of 07.10.2022 • Rule 8 rewritten • at least 10 changes, not 6!",
        "hook_say": "Remember: G.S.R. seven seven zero E of seven October two thousand twenty-two rewrote Rule eight, and it had at least ten changes, not six.",
        "covers": ["GSR-770E-DATE", "GSR770-1", "GSR770-2", "GSR770-3", "GSR770-4", "GSR770-5", "GSR770-6", "GSR770-EXTRA", "ADD-B1-6-ARTICLE"],
    },
    {
        "id": "c1_29_gsr410",
        "chapter": "CHAPTER 29 • AMENDMENT 2: G.S.R. 410(E) OF 16.07.2024 AND FORM 6-A",
        "title": "THE 2024 AMENDMENT — G.S.R. 410(E) AND THE NEW FORM 6-A",
        "accent": BLUE, "badge": "G.S.R. 410(E)",
        "q": "What did the 2024 amendment change, and what is the single Form 6-A?",
        "q_say": "Sir, what did the two thousand twenty-four amendment change, and what is the single Form six A?",
        "boxes": [
            ("DATE AND START",
             "Dated 16.07.2024; applies after 120 days; Form 6-A used for retirees from 16.11.2024 (secondary source).",
             "G.S.R. 410(E) dated 16 July 2024; applies after 120 days from publication (confirmed); Form 6-A applies to retiring employees from 16 November 2024 (secondary source: Outlook Money), consistent with the DoPPW O.M. of 11.09.2024. Recomputed: 120 days from 16.07.2024 ends on 13.11.2024, so 16.11.2024 would fit a Gazette publication on 19.07.2024; the exact publication date was not read (unverified).",
             BLUE,
             "The second amendment is G.S.R. four one zero E, dated sixteen July two thousand twenty-four. It applies after one hundred twenty days, and Form six A is reported to apply to retirees from sixteen November two thousand twenty-four. Counting one hundred twenty days from sixteen July gives thirteen November, so the exact Gazette publication date remains unverified."),
            ("FORM 6-A: WHAT IS CONFIRMED",
             "Form 6-A replaces Form 6 and the retiree's nomination Form A. It also carries family details and the bank undertaking.",
             "DoPPW O.M. F.No. 55/13/2023-P&PW(C)(Part1) dated 11.09.2024 (confirmed): Form 6-A replaces Form 6; for retiring employees, nominations for arrears of pension and for commutation go into Form 6-A, so Form A is not needed for them; pensioners still use Form A for later nominations or changes. Commutation means taking part of the pension as a lump sum. Form 6-A also carries family details and the bank undertaking. Press reports add that later amendments to the commutation and arrears-nomination rules are to follow.",
             GREEN,
             "What is confirmed about Form six A: a memorandum of eleven September two thousand twenty-four says it replaces Form six, and for retirees, nominations for arrears of pension and for commutation go into it, so Form A is not needed. Pensioners still use Form A for later changes. Commutation means taking part of your pension as a lump sum."),
            ("THE NINE-FORM CLAIM • UNVERIFIED",
             "The script says Form 6-A merged nine old forms. Only Forms 6 and A are confirmed. Format 1 is NOT part of it.",
             "UNVERIFIED (GSR410-1): the script's list of nine merged forms (Form 3, Form 4, Form 6, Form 8, Form A of 1983, Format 1, Format 9, FMA, Zero Option Form). Press says Form 6-A amalgamates nine older forms but names only Forms 6 and 8; the O.M. of 11.09.2024 confirms Form 6 replaced and Form A folded in for retirees; the notification text shows Form 4 and Format 9 amended, not removed, and does not mention Format 1. Do not list the nine as fact. CORRECTION (GSR410-FMT1): Format 1 is the Rule 7(4)(b) undertaking by staff of intelligence or security organisations; the claim that it merged into Form 6-A is not supported.",
             RED,
             "Be careful with the nine-form claim. Press says Form six A merges nine older forms but names only two, and the notification shows Form four and Format nine amended, not removed. Format one is the security undertaking and was not merged. So do not list the nine forms as fact."),
            ("THE RULE CHANGES",
             "Rules 57, 58 and 80(5) were aligned to Form 6-A. Rule 63(4) too, but it was NOT the only change.",
             "Rule changes (close restatements): Rule 57(1)(c)(iii), (2)(a) (six months before retirement, to the Head of Office), (3)(a) and (b): Form 4 and Form 6 replaced by Form 6-A, proviso replaced (GSR410-2 confirmed). Rule 58(1) substituted: in non-superannuation cases Form 6-A is submitted immediately after approval, or when retirement takes effect (GSR410-3 confirmed). Rule 63(4)(a) and (b): Format 9 replaced by Form 6-A, but it is not the only change: Rules 50(15)(e), 53, 57, 58, 59, 60, 62(6)(a), 80(5) and Forms 4 and 7 and Format 10 were also amended (GSR410-4 changed: remove the script's word 'only'). Rule 80(5)(c): the Head of Office forwards Form 4, Form 10, Format 9, Format 13 (if applicable) or Form 6-A, with Form 7 and Format 10; a gratuity nominee may use Form 6-A instead of Form 10 (GSR410-5 confirmed). These rules appear in Batches 5 and 6.",
             ORANGE,
             "The rule changes: Rule fifty-seven was aligned to Form six A. Rule fifty-eight now asks for Form six A right after approval in non-superannuation cases. Rule sixty-three, sub-rule four replaced Format nine with Form six A, but the script wrongly called this the only change; many other rules and forms were amended. Rule eighty, sub-rule five, clause c allows either the old forms or Form six A."),
        ],
        "hook": "REMEMBER: G.S.R. 410(E) of 16.07.2024 • Form 6-A for retirees • nine-form list unverified • not only Rule 63(4)!",
        "hook_say": "Remember: G.S.R. four one zero E of sixteen July two thousand twenty-four brought Form six A for retirees. The nine-form list is unverified, and Rule sixty-three, sub-rule four was not the only change.",
        "covers": ["GSR-410E", "GSR410-1", "GSR410-2", "GSR410-3", "GSR410-4", "GSR410-5", "GSR410-FMT1", "OM-11.09.2024-6A", "TL-GSR410-120D"],
    },
    {
        "id": "c1_30_gsr340_775",
        "chapter": "CHAPTER 30 • AMENDMENTS 3 AND 4: G.S.R. 340(E) OF 2025 AND G.S.R. 775(E) OF 2026",
        "title": "THE 2025 AND 2026 AMENDMENTS — PSU DISMISSAL AND A FOURTH NOTIFICATION",
        "accent": GREEN, "badge": "G.S.R. 340(E) • 775(E)",
        "q": "What did G.S.R. 340(E) of 2025 change, and is there anything newer than the script's three amendments?",
        "q_say": "Sir, what did G.S.R. three four zero E of two thousand twenty-five change, and is there anything newer than the script's three amendments?",
        "boxes": [
            ("G.S.R. 340(E) OF 22.05.2025",
             "Dated 22.05.2025 (F.No. 04/17/2023-P&PW(D)); in force on publication. One press source says published 23.05.2025: unverified.",
             "G.S.R. 340(E) dated 22 May 2025, F.No. 04/17/2023-P&PW(D); in force on publication (confirmed). One secondary source says the Gazette publication appeared on 23 May 2025: keep the date 22.05.2025; the publication date 23.05.2025 is unverified. Close restatement, not read verbatim.",
             GREEN,
             "The third amendment is G.S.R. three four zero E, dated twenty-two May two thousand twenty-five, and it applies from publication. One press source says the Gazette appeared on twenty-three May, which is unverified, so keep the date of twenty-two May."),
            ("RULE 37(29)(c) CHANGED",
             "If a PSU dismisses or removes an absorbed employee for later misconduct, the Government-service benefits can be forfeited. Rules 7, 8, 41, 44(5) apply the same way.",
             "Change 1 (GSR340-1 confirmed): Rule 37(29)(c) substituted: dismissal or removal by the PSU of an absorbed employee for subsequent misconduct also forfeits the retirement benefits for the Government service. Change 3 (GSR340-3 confirmed): an Explanation added: Rules 7, 8, 41 and 44(5) apply analogously to such employees as to Government servants. Rule 37 belongs to a later batch. UNVERIFIED commentary (GSR340-2): the script says Government pension was earlier protected from PSU misconduct and that this has reversed; the previous wording of clause (c) was not read and one press report calls it a departure from the earlier reading.",
             ORANGE,
             "Change one: Rule thirty-seven, sub-rule twenty-nine, clause c was substituted. If a PSU dismisses or removes an absorbed employee for later misconduct, the benefits for the Government service are also forfeited. Change three: an Explanation applies Rules seven, eight, forty-one and forty-four, sub-rule five to them in the same way. The script's remark that the old position was the opposite is commentary we could not confirm."),
            ("TRIGGER AND REVIEW",
             "Only dismissal or removal triggers forfeiture. A PSU decision on dismissal, removal or retrenchment is reviewable by the concerned Ministry.",
             "Change 4 (GSR340-4 confirmed on the page read): the forfeiture trigger is dismissal or removal; the decision on dismissal, removal or retrenchment is subject to review by the administratively concerned Ministry. One press report says retrenched employees are also hit; so state the Gazette wording only. Retrenchment means ending a job for reasons other than misconduct. Close restatement.",
             BLUE,
             "Change four is a fine point. Forfeiture follows dismissal or removal. Retrenchment, which means ending a job for reasons other than misconduct, is not itself the forfeiture trigger on the page we read. The Ministry concerned can review the PSU's decision on dismissal, removal or retrenchment. One press report disagrees, so quote only the Gazette wording."),
            ("A FOURTH AMENDMENT: G.S.R. 775(E)",
             "September 2026: CCS (Pension) Amendment Rules 2026 add a proviso under Rule 37(7) for certain ex-Ordnance Factory Board employees.",
             "G.S.R. 775(E) (September 2026; the exact day is garbled in the file read, a code suggests 7 September 2026): CCS (Pension) Amendment Rules, 2026, F.No. 4/27/2026-P&PW(D): a new proviso below Rule 37(7) exempting certain ex-Ordnance Factory Board employees (deemed deputation with Defence PSUs on foreign-service terms). Confirmed from the file read. This is newer than the script (which says three amendments); it is not related to Rules 1 to 10. The count of amendments is now four (AMEND-COUNT). Other amendments after 22.06.2026 touching Rules 1 to 10 were not found, but the official sites were not readable, so absence is not proven.",
             PINK,
             "There is a fourth one the script does not mention. G.S.R. seven seven five E, September two thousand twenty-six, adds a proviso below Rule thirty-seven, sub-rule seven for certain former Ordnance Factory Board employees. It does not touch Rules one to ten, but it makes four amendments in all. We found nothing newer for these rules, though the official sites could not be read."),
        ],
        "hook": "REMEMBER: G.S.R. 340(E) of 22.05.2025 = Rule 37(29)(c) • dismissal or removal • FOUR amendments now (775(E) of 2026)!",
        "hook_say": "Remember: G.S.R. three four zero E of twenty-two May two thousand twenty-five changed Rule thirty-seven, twenty-nine, c on dismissal or removal, and there are now four amendments because of G.S.R. seven seven five E of two thousand twenty-six.",
        "covers": ["GSR-340E", "GSR340-1", "GSR340-2", "GSR340-3", "GSR340-4", "PERSONS-SCOPE", "GSR-775E-2026", "AMEND-COUNT"],
    },
    {
        "id": "c1_31_currency",
        "chapter": "CHAPTER 31 • HOW CURRENT IS THIS? FIGURES, SCOPE AND CHECK DATES",
        "title": "CURRENCY CHECK — DR, THE MINIMUM PENSION AND WHAT IS OUTSIDE THESE RULES",
        "accent": SKY, "badge": "CURRENCY NOTE",
        "q": "Which figures change over time, and what lies outside these rules?",
        "q_say": "Sir, which figures change over time, and what lies outside these rules?",
        "boxes": [
            ("DEARNESS RELIEF",
             "DR is 60% from 01.01.2026 (DoE O.M. of 22.04.2026). A July 2026 revision was not announced as of 17.10.2026. Check the latest O.M.",
             "DR raised from 58% to 60% effective 01.01.2026 (Department of Expenditure O.M. No. 1/1(0)/2026-E.II(B) dated 22.04.2026; confirmed; DR-60). The July 2026 revision was still unannounced as of 17.10.2026 (press). DR is not part of pension (Rule 3(1)(t)). Dynamic figure: check the latest O.M.",
             SKY,
             "Dearness relief is sixty percent from first January two thousand twenty-six, under a Department of Expenditure memorandum of twenty-two April two thousand twenty-six. A July revision had not been announced as of seventeen October two thousand twenty-six, so always check the latest memorandum."),
            ("MINIMUM PENSION",
             "Reported at Rs 9,000 a month. The 8th Pay Commission has not reported. Check the latest O.M.",
             "Minimum pension (the Rule 44 floor used in Rules 7 and 8) reported at Rs 9,000 per month (7th CPC level) as at 7 September 2026, from a secondary source only; the Rule 44 text was not read (ADD-B1-4-9000); 8th Pay Commission hearings were ongoing in September 2026 and no revised minimum pension was in force. Check the latest O.M.",
             BLUE,
             "The minimum pension is reported at nine thousand rupees a month. The source is secondary, the 8th Pay Commission has not reported, and we did not read Rule forty-four. So treat it as a dynamic figure."),
            ("OUTSIDE THESE RULES • UNVERIFIED",
             "Separate tracks: CCS (Extraordinary Pension) Rules 2023; NPS gratuity amendment 2025; Unified Pension Scheme rules 2025. Not searched here.",
             "UNVERIFIED (SCOPE-CCS-EXTRAORD; not searched in this batch): the script names three separate instruments that are not amendments of these rules: CCS (Extraordinary Pension) Rules, 2023; CCS (Payment of Gratuity under NPS) Amendment Rules, 2025; and CCS (Implementation of the Unified Pension Scheme under NPS) Rules, 2025. NPS and UPS employees are treated under those, apart from the Explanation 5 gateway of Rule 2 to Rules 39 and 50.",
             GREEN,
             "Three instruments the script places outside these rules are the Extraordinary Pension Rules of two thousand twenty-three, the NPS gratuity amendment of two thousand twenty-five, and the Unified Pension Scheme rules of two thousand twenty-five. We did not search for them, so their titles are unverified. NPS and UPS staff follow them, apart from the narrow Explanation five door."),
            ("CHECK DATES AND WHAT WE COULD NOT READ",
             "The script gives two check dates (30 July and 12 September 2026). Neither confirmed. This check: 21 October 2026.",
             "CURR-DATE: the script gives two different verification dates (30 July 2026 and 12 September 2026); neither is confirmed; the latest check for this ledger was 21 October 2026. Not found: any DoPPW amendment or O.M. after 22.06.2026 touching Rules 1 to 10. The official sites (doppw.gov.in, egazette.gov.in, India Code) were not readable with the available tools and pensionersportal.gov.in was blocked by robots.txt, so absence is not proven. Every rule wording in this batch is a close restatement from secondary summaries, not read verbatim from the Gazette.",
             RED,
             "Be careful with dates. The script gives two different check dates, thirty July and twelve September two thousand twenty-six, and neither is confirmed. Our latest check is twenty-one October two thousand twenty-six. We found nothing newer for these rules, but the official sites could not be read, so check the Gazette before an exam."),
        ],
        "hook": "REMEMBER: DR 60% from 01.01.2026 • minimum pension reported Rs 9,000 • always check the latest O.M.!",
        "hook_say": "Remember: dearness relief is sixty percent from first January two thousand twenty-six, the minimum pension is reported at nine thousand rupees, and always check the latest memorandum.",
        "covers": ["DR-60", "SCOPE-CCS-EXTRAORD", "CURR-DATE", "ADD-B1-4-9000"],
    },
    {
        "id": "c1_32_recap",
        "chapter": "CHAPTER 32 • RECAP OF BATCH 1: RULES 1 TO 10",
        "title": "BATCH 1 RECAP — KEY NUMBERS, TOP TRAPS, CURRENCY AND WHAT COMES NEXT",
        "accent": PINK, "badge": "RECAP • RULES 1-10",
        "q": "Can we recap the key numbers and traps from Rules 1 to 10, and say what is next?",
        "q_say": "Sir, can we recap the key numbers and traps from Rules one to ten, and what comes next?",
        "boxes": [
            ("KEY NUMBERS",
             "G.S.R. 868(E) of 20.12.2021 • cut-off 31.12.2003 • 8 exclusions, 6 Explanations • 26 definitions • 6 months, 15+15, 30 days, 1 year.",
             "Key numbers: base notification G.S.R. 868(E) of 20.12.2021, in force on Gazette publication; cut-off 31.12.2003; eight exclusions (a) to (h); six Explanations; 26 definitions (a) to (z); Rule 4 option six months; Rule 7(3) fifteen days plus up to fifteen; Rule 8(2)(c) four years; Rule 8(6) one-third; Rule 9 one year and thirty days; the Rule 44 floor (reported Rs 9,000); amendments: G.S.R. 770(E) of 07.10.2022, G.S.R. 410(E) of 16.07.2024 (Form 6-A for retirees from 16.11.2024), G.S.R. 340(E) of 22.05.2025, and G.S.R. 775(E) of September 2026. CORRECTION to the script's BONUS-11: line four (Head of Office needs declaring) is only partly right, because a person specified by the competent authority also counts; add Rule 7(4) (the security staff undertaking, Format 1) to the script's list (RECAP-BONUS11).",
             PINK,
             "Key numbers. The base notification is G.S.R. eight six eight E of twenty December two thousand twenty-one. The cut-off date is thirty-one December two thousand three. There are eight exclusions, six Explanations and twenty-six definitions. Time limits are six months, fifteen plus fifteen days, thirty days and one year. Four amendments exist now."),
            ("TOP TRAPS",
             "Explanations extend, they do not backdate • Form is not Format • DR is not pension • Rule 7(1)(b) = Appointing Authority • Rule 9 is not Rule 10.",
             "Top traps: (1) the Explanations to Rule 2 say 'also apply to' and do not deem appointment before 31.12.2003; Explanation 5 is for death and invalidation only; (2) Form versus Format (Form 1 is Rule 9; Format 1 is Rule 7(4)); (3) pension and family pension exclude DR; (4) Head of Office is declared under DFPR Rule 14 or specified; (5) Rule 7(1)(b) names the Appointing Authority, not the President; Rule 8 depends on the post's appointing authority; (6) 15 days under Rule 7(3) but 30 days under Rule 9(7); (7) Rule 10 has no time limit and no form; (8) Rule 4 is a routing rule, Rule 5 a version rule.",
             RED,
             "Top traps. The Explanations extend coverage, they do not backdate it. A Form is not a Format. Dearness relief is not pension. In Rule seven, one, b the authority is the Appointing Authority. Rule nine has thirty days and a one-year window, while Rule ten has no time limit. Rule four chooses the rule book, Rule five chooses the version."),
            ("CURRENCY NOTE",
             "Latest checked 21.10.2026. DR 60% from 01.01.2026; minimum pension reported Rs 9,000; check the latest O.M. Unverified items are flagged.",
             "Currency: ledger checked up to 21.10.2026. Dynamic figures: DR 60% w.e.f. 01.01.2026 (DoE O.M. of 22.04.2026; July 2026 revision not announced as of 17.10.2026); minimum pension reported Rs 9,000 (secondary source). The Gazette text of the amendments and of the Rules was not read verbatim: rule wording is a close restatement. Flagged unverified in this batch: Rule 87 repeal and saving; Rule 4 sub-rule numbering; the NPS Rule 10 option; the script's nine-form merger list; the 120-day Gazette publication date; the 23.05.2025 publication date; the CSIR order of 07.07.2026; the 13 Forms and 13 Formats counts; the 87 rules and 14 chapters counts; the three out-of-scope instruments.",
             ORANGE,
             "A currency note. Our latest check is twenty-one October two thousand twenty-six. Dearness relief is sixty percent from first January two thousand twenty-six, and the minimum pension is reported at nine thousand rupees, but both are dynamic, so check the latest memorandum. Rule wording here is a close restatement, and the unverified items are flagged on their cards."),
            ("NEXT BATCH",
             "Batch 2: Chapter III, qualifying service, Rules 11 to 30, including Rules 19 and 20, Rule 15 and the Rule 30 verification.",
             "Next: Batch 2, Chapter III (Qualifying service), Rules 11 to 30. It will verify Rule 14, Rule 15 (temporary status, half service), Rule 19 (re-employed civil pensioner, refunds), Rule 20 (military service; Explanation 1(ii) as amended in 2022) and Rule 30 (verification, Format 4), which this batch only previewed. Revise the G.S.R. numbers and the Rule 9 versus Rule 10 comparison before moving on.",
             GREEN,
             "Next time we start Chapter three, qualifying service, Rules eleven to thirty. We will check Rules fourteen, fifteen, nineteen, twenty and thirty, which this batch only previewed. Before then, revise the G.S.R. numbers and the Rule nine versus Rule ten comparison. Thank you, and see you in batch two."),
        ],
        "hook": "REMEMBER: 31.12.2003 • 8 + 6 + 26 • 6 months, 15+15, 30 days, 1 year • 4 amendments • next: Rules 11 to 30!",
        "hook_say": "Remember: the cut-off is thirty-one December two thousand three, eight exclusions, six Explanations and twenty-six definitions, the time limits, four amendments, and next comes Rules eleven to thirty.",
        "covers": ["RECAP-BONUS11"],
    },
]

FLOWS = {
    "r8chain": {
        "nodes": [
            (80, 300, 420, 80, "TRIGGER", "Guilt found in service", SKY, 1),
            (570, 300, 430, 80, "WHO DECIDES", "Post's appointing authority", BLUE, 2),
            (1070, 300, 360, 80, "UPSC", "Only if President acts", GREEN, 3),
            (1500, 300, 340, 80, "APPEAL", "Rule 8(6A)", RED, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, BLUE, 3), (2, 3, GREEN, 4)],
    },
    "timeladder": {
        "nodes": [
            (80, 300, 420, 80, "DAYS", "15+15 and 30", SKY, 1),
            (570, 300, 430, 80, "MONTHS", "6 months (Rule 4)", BLUE, 2),
            (1070, 300, 360, 80, "YEARS", "1, 3 and 4 years", GREEN, 3),
            (1500, 300, 340, 80, "FRACTION", "One-third (8(6))", RED, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, BLUE, 3), (2, 3, GREEN, 4)],
    },
}
PART_STARTS = ["c1_01_rule1", "c1_13_rule4", "c1_23_rule9_main"]



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
    out = ["# CCS (Pension) Rules 2021 - Batch 1 - Rules 1-10: Preliminary and Classification of Claims - full-wording reference sheet", "",
           "Every card on screen is a short key-point; the full wording / examinable facts of each card are listed here.", ""]
    for sc in SCENES:
        out += [f"## {sc['chapter']}", f"**{sc['title']}**  ({sc['badge']})", "", f"Q: {sc['q']}", ""]
        for (t, _b, _c, _n) in sc["boxes"]:
            out += [f"### {t}", FULL[(sc["id"], t)], ""]
        out += [f"> {sc['hook']}", ""]
    Path("pension_b1_reference_sheet.md").write_text("\n".join(out), encoding="utf-8")


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

````
