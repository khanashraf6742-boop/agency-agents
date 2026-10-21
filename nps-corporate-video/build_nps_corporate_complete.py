# FIXED BUILD (Arena): Ch.6 title shortened (was 85 chars, crashed --preview/full build);
# _TTS_FIXES extended: Tier-I/II spoken as Tier 1/2, helpline read digit-by-digit,
# websites spelled out, 0.0075 spoken in full. All rule content unchanged from source.
#!/usr/bin/env python3
"""
PFRDA National Pension System (NPS) — Corporate Sector Model Complete Masterclass Compiler
SIMPLE ENGLISH Q&A EXPLANATION MASTERCLASS COMPILER - 16 chapters.
Scope: Full Official PFRDA Brochure (Sections 1 to 7: Paras 1 to 5.16, References, Annexure A)
=====================================================================================================
SOURCES READ & VERIFIED IN THIS BUILD:
  * PFRDA National Pension System for Corporate Sector Brochure (Official Publication)
  * Pension Fund Regulatory and Development Authority Act, 2013 & PFRDA Regulations
  * Indian Trusts Act, 1882 (NPS Trust & Board of Trustees Constitution)
  * Prevention of Money Laundering Act (PMLA), 2002 & AML/CFT FIU-IND Guidelines
  * Income Tax Act, 1961 (Sections 80CCD(1), 80CCD(2), 36(1)(iva) Business Expense)
KEY FACTS COMPILED (100% GRANULAR):
  * Launched in Dec 2011 to extend NPS to corporate entities, PSUs, partnerships, and proprietorships.
  * Unbundled Architecture: PFRDA (Regulator), NPS Trust (Fiduciary ownership), Trustee Bank (BOI),
    CRA (NSDL), Custodian (SHCIL), PFMs (6 institutional managers), ASPs (7 life insurers), POPs (>50 registered, >14,000 POP-SPs).
  * Eligible Corporates: Entities under Companies Act, Co-operative Acts, CPSEs, SPSEs, Partnerships,
    LLPs, Statutory Bodies, Proprietorships, and registered Trusts/Societies.
  * Corporate Tax: Employer contribution up to 10% of (Basic + DA) deductible as business expense under Sec. 36(1)(iva).
  * Subscriber Tax: Sec. 80CCD(1) employee deduction up to 10% of (Basic + DA) within Rs. 1L limit;
    Sec. 80CCD(2) employer contribution up to 10% is fully tax-exempt and EXCLUDED from the Rs. 1L cap.
  * Investment Patterns: Active Choice (Asset Class E capped at 50%, Asset Class C, Asset Class G) or
    Auto Choice (Lifecycle Fund decaying 2% E and 1% C annually from age 36 to 55).
  * Account Rules: Tier-I (non-withdrawable, tax-exempt) and Tier-II (voluntary savings, anytime liquidity, no tax breaks).
    Tier-II funds can switch to Tier-I, but Tier-I funds can NEVER switch to Tier-II.
  * Minimum Contributions: Tier-I = Rs. 500 per deposit, Rs. 6,000 per year, 1 deposit per year (Rs. 100 default penalty).
    Tier-II = Rs. 250 per deposit, Rs. 2,000 year-end minimum balance, 1 deposit per year.
  * POP Charges: Initial registration Rs. 100 + 0.25% (min Rs. 20, max Rs. 25,000); subsequent deposits 0.25% (min Rs. 20, max Rs. 25,000);
    non-financial transactions Rs. 20 upfront.
  * CRA & Custodian Charges: PRA opening Rs. 50; Annual maintenance Rs. 225 (includes annual printed statement);
    Per-transaction Rs. 5 (via unit cancellation). Custodian electronic asset fee = 0.0075% p.a., physical = 0.05% p.a.
  * PFM & Trustee Bank Rules: PFM fee calculated on average monthly assets (excludes custodian charges and taxes).
    Trustee Bank charges zero for RBI locations, Rs. 15 for non-RBI locations.
  * Exit & Vesting: Before age 60 = minimum 80% annuity, maximum 20% lump sum.
    Age 60 to 70 = minimum 40% annuity, maximum 60% lump sum (or phased annual withdrawal min 10% up to age 70).
    Death = nominee gets 100% lump sum.
  * Six Annuity Variants: (1) Uniform life; (2) Guaranteed 5, 10, 15, 20 yrs certain; (3) Return of purchase price;
    (4) 3% simple increasing; (5) 50% spouse annuity; (6) 100% spouse annuity.
  * Forms: CHO-1 (Corporate Head Office), CBO (Branch), CS-S1 (Subscriber Registration), CS-S2 (Master Changes / Reissue),
    CS-S3 (Change Employer/Scheme), CHO-2 (Corporate Scheme Change), CHO-3 (Corporate POP Change), UOS-S10 (Tier-II later).
  * Grievances (CGMS): Toll-Free IVR 1-800-222080, cra-nsdl.com with I-PIN, or physical forms via POP with token generation.
Usage:
    python build_nps_corporate_complete.py --audit      # density & layout budget check (no ffmpeg needed)
    python build_nps_corporate_complete.py --preview    # render slides only (visual inspection)
    python build_nps_corporate_complete.py --no-tts     # silent dry run (verify ASS subtitles and video concat)
    python build_nps_corporate_complete.py --part 1     # render first third of chapters (1, 2 or 3)
    python build_nps_corporate_complete.py              # full master build with edge-tts and burned ASS subtitles
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
BUILD_DIR = Path("nps_corporate_complete_build")
SLIDES_DIR = BUILD_DIR / "slides"
AUDIO_DIR = BUILD_DIR / "audio"
OUT_STEM = "nps_corporate_complete_masterclass"
OUTPUT_MP4 = Path(OUT_STEM + ".mp4")

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

_TTS_FIXES = [
    (r'\bPFRDA\b', 'P.F.R.D.A.'), (r'\bNPS\b', 'N.P.S.'), (r'\bPRAN\b', 'P.R.A.N.'), (r'\bPRA\b', 'P.R.A.'),
    (r'\bCRA\b', 'C.R.A.'), (r'\bNSDL\b', 'N.S.D.L.'), (r'\bPOP-SPs\b', 'P.O.P. Service Providers'),
    (r'\bPOP-SP\b', 'P.O.P. Service Provider'), (r'\bPOPs\b', 'P.O.P.s'), (r'\bPOP\b', 'P.O.P.'),
    (r'\bPFMs\b', 'P.F.M.s'), (r'\bPFM\b', 'P.F.M.'), (r'\bASPs\b', 'A.S.P.s'), (r'\bASP\b', 'A.S.P.'),
    (r'\bSHCIL\b', 'S.H.C.I.L.'), (r'\bBOI\b', 'Bank of India'), (r'\bTB\b', 'Trustee Bank'),
    (r'\bPSUs\b', 'P.S.U.s'), (r'\bPSU\b', 'P.S.U.'), (r'\bCPSEs\b', 'C.P.S.E.s'), (r'\bCPSE\b', 'C.P.S.E.'),
    (r'\bSPSEs\b', 'S.P.S.E.s'), (r'\bSPSE\b', 'S.P.S.E.'), (r'\bLLPs\b', 'L.L.P.s'), (r'\bLLP\b', 'L.L.P.'),
    (r'\bKYC\b', 'K.Y.C.'), (r'\bAML\b', 'A.M.L.'), (r'\bCFT\b', 'C.F.T.'), (r'\bPMLA\b', 'P.M.L.A.'),
    (r'\bFIU-IND\b', 'F.I.U. India'), (r'\bNAV\b', 'N.A.V.'), (r'\bDA\b', 'D.A.'),
    (r'\bIRDA\b', 'I.R.D.A.'), (r'\bSEBI\b', 'S.E.B.I.'), (r'\bIVR\b', 'I.V.R.'),
    (r'\bCGMS\b', 'C.G.M.S.'), (r'\bSLR/TAT\b', 'Service Level Requirements and Turnaround Time'),
    (r'\bTAT\b', 'Turnaround Time'), (r'\bMOU\b', 'M.O.U.'), (r'\bMOUs\b', 'M.O.U.s'),
    (r'\bCBO\b', 'Corporate Branch Office'), (r'\bCHO\b', 'Corporate Head Office'),
    (r'\bSec\.\s*80CCD\(1\)', 'Section 80 C.C.D. 1'), (r'\bSec\.\s*80CCD\(2\)', 'Section 80 C.C.D. 2'),
    (r'\b80CCD\(1\)', '80 C.C.D. 1'), (r'\b80CCD\(2\)', '80 C.C.D. 2'),
    (r'\bSec\.\s*36\(1\)\(iva\)', 'Section 36 1 4 a'),
    (r'\bTier-II\b', 'Tier 2'), (r'\bTier-I\b', 'Tier 1'),
    (r'1-800-222080|1800222080', 'one eight zero zero, two two two, zero eight zero'),
    (r'pfrda\.org\.in', 'P.F.R.D.A. dot org dot in'), (r'cra-nsdl\.com', 'C.R.A. dash N.S.D.L. dot com'),
    (r'0\.0075', 'zero point zero zero seven five'), (r'0\.05', 'zero point zero five'),
    (r'\bPRANs\b', 'P.R.A.N.s'), (r'\bPRAN\b', 'P.R.A.N.'),
    (r'\bRs\.', 'Rupees'), (r'[\u2014\u2013]', ','),
]

def normalize_for_tts(text: str) -> str:
    for pat, rep in _TTS_FIXES:
        text = re.sub(pat, rep, text)
    return re.sub(r'[ \t]+', ' ', text).strip()

# ===== SCENES_BEGIN =====
SCENES = [
    {
        "id": "c01_01_evolution_and_concept",
        "chapter": "CHAPTER 1 • SECTION 1 & 2: NPS EVOLUTION & CORPORATE SECTOR MODEL",
        "title": "SECTION 1 & 2 — EVOLUTION OF NPS & THE CORPORATE SECTOR MODEL",
        "accent": SKY, "badge": "SECTIONS 1 & 2",
        "q": "How did the National Pension System evolve, and why was the Corporate Sector Model introduced?",
        "intro": ("Welcome to the Complete PFRDA National Pension System Corporate Model Masterclass! In this session, "
                  "we examine the unbundled architecture, investment choices, tax rules, fee schedules, and exit options. Let us begin."),
        "q_say": "Sir, when was NPS introduced for government employees, and what led to the launch of the Corporate Sector Model?",
        "flow": "nps_core_architecture",
        "boxes": [
            ("HISTORICAL TIMELINE (SECTION 1)",
             "Adopted for Central Govt 01.01.2004 (except Armed Forces); All Citizens 01.05.2009; Corporates Dec 2011.",
             "Section 1: The Government of India adopted the National Pension System (NPS) based on defined contributions for all new entrants to Central Government services, excepting the Armed Forces, with effect from 1st January 2004. State Governments subsequently notified similar systems. PFRDA extended NPS to All Citizens on 1st May 2009, and launched the 'NPS - Corporate Sector Model' in December 2011.",
             SKY,
             "Let us review the historical milestones first. National Pension System started on 1 January 2004 for Central Government employees, opened to all citizens on 1 May 2009, and expanded to corporate entities in December 2011."),
            ("DEFINED CONTRIBUTION PHILOSOPHY",
             "Replaces defined-benefit pension with individual defined contributions, market-linked growth, and individual PRANs.",
             "Section 1 & 2: NPS operates on a defined-contribution mechanism where retirement benefits depend on regular contributions and prudential market returns, tracked under a unique Permanent Retirement Account Number (PRAN).",
             GREEN,
             "Unlike traditional defined-benefit pensions, National Pension System is an individual defined-contribution plan. Your retirement wealth grows through market-linked investments tracked under your unique Permanent Retirement Account Number."),
            ("CORPORATE MODEL OBJECTIVE",
             "Provides organised retirement savings for private and public sector employees within employer-employee relationship.",
             "Section 1 & 2: The Corporate Model enables organized corporate entities, including PSUs, to extend institutional pension benefits to their employees within the purview of their employer-employee relationship.",
             ORANGE,
             "The Corporate Model enables employers and Public Sector Undertakings to co-contribute toward retirement savings for their staff, using standard institutional frameworks."),
            ("THE TRAP: ARMED FORCES EXCLUSION",
             "Trap: Armed Forces are statutorily excluded from mandatory NPS; Central civil employees joined w.e.f. 01.01.2004.",
             "Exam Trap (Section 1): Candidates often forget that the Armed Forces were specifically excluded from the mandatory 01.01.2004 NPS rollout.",
             RED,
             "Keep this exam trap in mind: the Armed Forces were completely excluded from the mandatory National Pension System rollout on 1 January 2004."),
        ],
        "hook": "REMEMBER: Central Govt: 01.01.2004 • All Citizens: 01.05.2009 • Corporate Model: December 2011!",
        "hook_say": "Remember the key dates: Central Government on 1 January 2004, All Citizens on 1 May 2009, and the Corporate Model in December 2011.",
        "covers": ["NPS-EVOLUTION"],
    },
    {
        "id": "c01_02_unbundled_architecture",
        "chapter": "CHAPTER 2 • SECTION 2 & 3: UNBUNDLED ARCHITECTURE & THE REGULATOR (PFRDA)",
        "title": "SECTION 2 & 3 — PFRDA REGULATION & THE UNBUNDLED ARCHITECTURE",
        "accent": GREEN, "badge": "ARCHITECTURE",
        "q": "What is meant by an unbundled architecture in NPS, and what is the role of PFRDA?",
        "q_say": "Sir, why is NPS called an unbundled system, and how does PFRDA oversee its different institutional pillars?",
        "flow": "nps_core_architecture",
        "boxes": [
            ("PFRDA AS STATUTORY REGULATOR",
             "PFRDA regulates NPS, appoints intermediaries (CRA, PFMs, TB, Custodian), issues guidelines, and monitors performance.",
             "Section 3: PFRDA is the statutory regulator for NPS. It appoints various intermediaries such as Central Recordkeeping Agency (CRA), Pension Fund Managers, Custodian, and Trustee Bank, monitors performance, issues investment guidelines, and enforces compliance.",
             SKY,
             "Under Section 3, the Pension Fund Regulatory and Development Authority is the statutory regulator. It appoints all operational agencies, sets investment mandates, and monitors performance."),
            ("THE UNBUNDLED PRINCIPLE",
             "Each function is segregated: recordkeeping, fund management, banking, asset custody, and annuities are handled by separate bodies.",
             "Section 4: NPS has an unbundled architecture where each function is performed by a specialized entity to minimize administrative overheads, prevent conflicts of interest, and keep system costs lowest in the world.",
             GREEN,
             "NPS features an unbundled architecture. Recordkeeping, fund management, asset custody, and banking are handled by independent, specialized institutions to eliminate conflicts of interest and reduce costs."),
            ("SEPARATION OF POWERS",
             "CRA maintains data; Trustee Bank channels money; PFMs invest assets; Custodian secures physical/electronic holdings.",
             "Architecture Mechanics: Separation ensures safety: NSDL maintains the transaction register, Bank of India clears funds, PFMs decide security allocation, and SHCIL holds underlying securities.",
             ORANGE,
             "This separation ensures safety: recordkeeping agency N.S.D.L. maintains your account data, Bank of India clears funds, fund managers manage portfolios, and Stock Holding Corporation holds the assets."),
            ("THE TRAP: PFRDA DOES NOT HOLD FUNDS",
             "Trap: PFRDA is a regulatory authority; funds and assets are held by the NPS Trust and the Custodian, NOT by PFRDA!",
             "Exam Trap (Section 3 & 4): Neither PFRDA nor the Ministry holds subscriber funds. Funds vest in the NPS Trust under the Indian Trusts Act, 1882.",
             RED,
             "Never make this mistake: the regulator does not hold your money. Funds vest legally in the independent N.P.S. Trust, while assets remain with the Custodian."),
        ],
        "hook": "REMEMBER: PFRDA Regulates • Intermediaries Are Unbundled • World's Lowest Cost Architecture!",
        "hook_say": "Remember: The regulator oversees the framework, while unbundled institutions manage records, banking, and investments at low cost.",
        "covers": ["UNBUNDLED-ARCH"],
    },
    {
        "id": "c01_03_cra_and_trustee_bank",
        "chapter": "CHAPTER 3 • SECTION 4: CENTRAL RECORDKEEPING AGENCY & TRUSTEE BANK",
        "title": "SECTION 4 — ROLES OF NSDL (CRA) AND BANK OF INDIA (TRUSTEE BANK)",
        "accent": ORANGE, "badge": "CRA & TRUSTEE BANK",
        "q": "What specific functions do the Central Recordkeeping Agency (NSDL) and Trustee Bank (BOI) execute?",
        "q_say": "Sir, what are the exact responsibilities of NSDL as the CRA, and why is Bank of India designated as the Trustee Bank?",
        "boxes": [
            ("CRA: NSDL RESPONSIBILITIES",
             "NSDL issues unique PRANs, maintains subscriber database, records transactions, and interfaces with all intermediaries.",
             "Section 4: Central Recordkeeping Agency is National Securities Depository Limited (NSDL). Key functions: (1) Recordkeeping, administration, and customer service; (2) Issuing unique Permanent Retirement Account Numbers (PRAN) to each subscriber; (3) Maintaining transaction database; (4) Operating as operational interface between PFRDA, PFMs, ASPs, and Trustee Bank.",
             SKY,
             "National Securities Depository Limited serves as the Central Recordkeeping Agency. It issues unique Permanent Retirement Account Numbers, tracks ledger units, and connects all operating entities."),
            ("NPS TRUST & TRUSTEE BANK (BOI)",
             "NPS Trust established under Indian Trusts Act, 1882. Bank of India (BOI) appointed as designated Trustee Bank.",
             "Section 4: PFRDA established the NPS Trust under the Indian Trusts Act, 1882, vesting administration in the Board of Trustees. The Trust holds an account with Bank of India (BOI), designated as Trustee Bank. BOI manages banking of pension funds in accordance with PFRDA guidelines.",
             GREEN,
             "The N.P.S. Trust is established under the Indian Trusts Act of 1882. It maintains an account with Bank of India, which is designated as the Trustee Bank to handle fund transfers."),
            ("TRUSTEE BANK TRANSACTION SCOPE",
             "Footnote 4: TB handles whole chain: electronic/physical receipt, transfer to PFMs, and outflow credit to beneficiary account.",
             "Section 4 & Footnote 4: Trustee Bank charges are not levied on subscribers directly. Transaction refers to the entire chain of activities: receipt of instructions, transfer to PFMs, and on the outflow side, all activities leading to credit of the beneficiary's bank account.",
             ORANGE,
             "Footnote 4 defines the Trustee Bank transaction: it spans the entire chain from receiving remittance instructions, transferring funds to fund managers, and clearing exit payouts directly into subscriber bank accounts."),
            ("THE TRAP: POP VS CRA ROLES",
             "Trap: POP collects documents and funds, but PRAN generation and ledger maintenance belong EXCLUSIVELY to CRA (NSDL)!",
             "Exam Trap (Section 4): POPs are distribution interfaces; they do not generate PRANs or maintain primary ledger units.",
             RED,
             "Do not confuse distributor and recordkeeper: Points of Presence collect registration forms, but unique account generation and ledger accounting are performed exclusively by N.S.D.L."),
        ],
        "hook": "REMEMBER: CRA = NSDL (PRAN & Records) • Trustee Bank = Bank of India • Fiduciary = NPS Trust!",
        "hook_say": "Remember: N.S.D.L. is the recordkeeper issuing your account number, Bank of India is the Trustee Bank, and the N.P.S. Trust holds fiduciary ownership.",
        "covers": ["CRA-TRUSTEE-BANK"],
    },
    {
        "id": "c01_04_pfms_custodian_asps",
        "chapter": "CHAPTER 4 • SECTION 4: PFMs, CUSTODIAN (SHCIL) & ANNUITY SERVICE PROVIDERS",
        "title": "SECTION 4 — FUND MANAGERS, ASSET CUSTODIAN & ANNUITY SERVICE PROVIDERS",
        "accent": RED, "badge": "PFMs • CUSTODIAN • ASPs",
        "q": "Who manages the pension corpus, who holds the securities, and who delivers the monthly pension?",
        "q_say": "Sir, which fund managers are registered under NPS, who holds physical custody of the shares and bonds, and who pays annuities?",
        "boxes": [
            ("PENSION FUND MANAGERS (PFMs)",
             "6 appointed PFMs: SBI Pension Funds, LIC Pension Fund, UTI Retirement, ICICI Prudential, Kotak Mahindra, Reliance Capital.",
             "Section 4: Appointed Pension Fund Managers (PFMs) manage retirement savings strictly per PFRDA and Govt guidelines: (1) SBI Pension Funds Pvt. Ltd., (2) LIC Pension Fund Ltd., (3) UTI Retirement Solutions Ltd., (4) ICICI Prudential Pension Funds Management Co. Ltd., (5) Kotak Mahindra Pension Fund Ltd., (6) Reliance Capital Pension Fund Ltd. Corporate or subscriber selects any one.",
             SKY,
             "Under Section 4, the six registered institutional fund managers include S.B.I., L.I.C., U.T.I., I.C.I.C.I. Prudential, Kotak Mahindra, and Reliance Capital. Either the employer or the employee selects one."),
            ("CUSTODIAN: SHCIL & EXTRA CHARGES",
             "SHCIL holds custody of underlying assets. Footnote 5: Demat/Remat, receipt of shares, and SEBI charges are EXTRA.",
             "Section 4 & Footnote 5: Stock Holding Corporation of India Ltd. (SHCIL) is the SEBI-registered Custodian. Footnote 5 clarifies that asset servicing fees cover custody, but charges for Demat/Remat, receipt of shares, and statutory SEBI charges are extra.",
             GREEN,
             "Stock Holding Corporation of India serves as the registered Custodian. Footnote 5 clarifies that while custody is covered, Demat and statutory market charges are billed extra."),
            ("ANNUITY SERVICE PROVIDERS (ASPs)",
             "7 life insurers empanelled as ASPs to deliver regular monthly pensions as per chosen annuity scheme upon exit.",
             "Section 4: At present, 7 IRDA-regulated Life Insurance Companies have been empanelled as Annuity Service Providers (ASPs) responsible for delivering monthly pensions based on the subscriber's selected annuity plan.",
             ORANGE,
             "Seven life insurance companies are empanelled as Annuity Service Providers. They receive the exit corpus and deliver guaranteed monthly pension payments."),
            ("THE TRAP: PFM INVESTMENT MANAGEMENT FEE",
             "Trap: Footnote 3: PFM fee is calculated on AVERAGE MONTHLY ASSETS; includes brokerage, but excludes custodian charges and taxes!",
             "Exam Trap (Section 4 & Footnote 3): The Investment Management Fee (IMF) is calculated on average monthly assets managed by the PFM. It is inclusive of brokerage and transaction costs, but strictly excludes custodian fees and applicable taxes.",
             RED,
             "Watch out for Footnote 3: the fund management fee is calculated on average monthly assets. It includes trade brokerage, but excludes custodian fees and government taxes."),
        ],
        "hook": "REMEMBER: 6 PFMs Manage Portfolios • SHCIL Holds Assets • 7 ASPs Deliver Monthly Pensions!",
        "hook_say": "Remember: Six fund managers handle portfolio investments, S.H.C.I.L. holds asset custody, and seven insurance companies pay monthly annuities.",
        "covers": ["PFMS-CUSTODIAN-ASPS"],
    },
    {
        "id": "c01_05_corporate_entities_and_pops",
        "chapter": "CHAPTER 5 • SECTION 4 & 5.5: ELIGIBLE CORPORATES, POPs & ONBOARDING FORMS",
        "title": "SECTION 4 & 5.5 — ELIGIBLE CORPORATE BODIES & THE CHO-I ONBOARDING PROTOCOL",
        "accent": BLUE, "badge": "POPs & CORPORATES",
        "q": "Which corporate bodies can adopt the Corporate Model, and what is the exact onboarding procedure using Form CHO-I?",
        "q_say": "Sir, can a partnership firm, trust, or proprietary business join the Corporate Model, and what forms are submitted to the POP?",
        "boxes": [
            ("ELIGIBLE CORPORATE BODIES",
             "Available to: Companies Act entities, Co-operatives, CPSEs, SPSEs, Partnerships, LLPs, Statutory Bodies, Proprietorships, Trusts/Societies.",
             "Section 4: The Corporate Model is open to: (1) Entities registered under Companies Act, (2) Co-operative societies, (3) Central and State PSEs, (4) Registered Partnership firms, (5) Registered LLPs, (6) Bodies incorporated under Parliament or State Acts, (7) Proprietorship Concerns, (8) Registered Trusts and Societies.",
             SKY,
             "Under Section 4, almost all organized employers qualify: registered companies, cooperatives, Central and State Public Sector Undertakings, partnerships, Limited Liability Partnerships, proprietorships, trusts, and societies."),
            ("POP / POP-SP INTERFACE & SLA RELAXATION",
             ">50 registered POPs with >14,000 branch POP-SPs. POP SLAs relaxed to receive consolidated corporate data and funds.",
             "Section 4 & 5.5: Over 50 registered Points of Presence (POPs) with more than 14,000 POP Service Providers (POP-SPs) act as branches. Section 5.5 specifies that SLAs prescribed by PFRDA for POPs stand relaxed to allow acceptance of consolidated data, aggregated funds, and nominal rolls from corporate clients.",
             GREEN,
             "Over 50 Points of Presence operating more than 14,000 branch service points act as the operational interface. Their standard service timelines are relaxed to allow consolidated corporate data and fund uploads."),
            ("ONBOARDING: FORM CHO-I & CBOs",
             "Corporate signs MOU with POP. Completes Form CHO-I with branch (CBO) details. CRA issues Entity Registration Number.",
             "Section 5.5: Corporate executes an MOU with a chosen POP. Corporate completes Form CHO-I along with details of Corporate Branch Offices (CBOs). POP carries out AML/CFT due diligence and submits certified forms to CRA. CRA registers the corporate and issues an Entity Registration Number, which appears on subscriber forms CS-S1.",
             ORANGE,
             "The employer signs an agreement with an authorized Point of Presence, fills Form C.H.O. 1 with branch details, completes identity checks, and receives an Entity Registration Number from N.S.D.L."),
            ("THE TRAP: PMLA & AML/CFT COMPLIANCE",
             "Trap: Corporate and POP MUST comply with Prevention of Money Laundering Act (PMLA) 2002 guidelines per FIU-IND!",
             "Compliance Trap (Section 4 & 5.5): Onboarding is subject to strict KYC standards prescribed under the PML Act, 2002 as notified by Financial Intelligence Unit, India (FIU-IND).",
             RED,
             "Do not overlook regulatory compliance: both the employer and Point of Presence must follow customer due diligence rules under the Prevention of Money Laundering Act."),
        ],
        "hook": "REMEMBER: Open to Companies, LLPs, PSUs, Partnerships & Trusts • Form CHO-I • PMLA Compliant!",
        "hook_say": "Remember: The model covers companies, partnerships, trusts, and public undertakings through Form C.H.O. 1 under anti-money laundering regulations.",
        "covers": ["CORP-ELIGIBILITY-POPS"],
    },
    {
        "id": "c01_06_corporate_benefits_and_tax",
        "chapter": "CHAPTER 6 • SECTION 5.1 & 5.2: SALIENT FEATURES & CORPORATE TAX ADVANTAGES",
        "title": "SECTION 5.1 & 5.2 — WHY CORPORATES ADOPT NPS: 10% TAX DEDUCTION",
        "accent": YELLOW, "badge": "CORPORATE TAX",
        "q": "What operational and tax benefits does a company gain by adopting the NPS Corporate Model?",
        "q_say": "Sir, how does a corporate entity save taxes and administrative costs by offering NPS to its workforce?",
        "boxes": [
            ("OUTSOURCING PENSION OVERHEADS",
             "Saves expenses incurred on internal pension administration (recordkeeping, fund management, and annuity contracting).",
             "Section 5.1 & 5.2: Adopting NPS eliminates internal superannuation trust administrative expenses. The company does not need to handle standalone recordkeeping, actuarial valuations, portfolio management, or annuity procurement.",
             SKY,
             "Section 5.2 explains that adopting National Pension System saves administrative costs. Companies avoid the expense of managing private retirement trusts, bookkeeping, and annuity negotiations."),
            ("10% BUSINESS EXPENSE TAX DEDUCTION",
             "Employer contribution up to 10% of salary (Basic + DA) deductible as Business Expense under Profit & Loss Account.",
             "Section 5.2: From 1st April 2012, employer contribution towards employee NPS up to 10% of salary (Basic plus Dearness Allowance) is allowable as a deductible business expense from the Profit & Loss Account under Section 36(1)(iva) of the Income Tax Act.",
             GREEN,
             "Under Section 5.2, employer contributions up to 10 percent of salary, covering basic pay and dearness allowance, are deductible as a business expense from the company's profit and loss statement."),
            ("FLEXIBLE PFM CHOICES",
             "Corporate can centrally select PFM and asset allocation for all staff, or give choice to individual employees.",
             "Section 5.2 & 5.6: The corporate can exercise central scheme preference (PFM and investment allocation) for all its underlying employees, or pass full discretion to each subscriber.",
             ORANGE,
             "The platform offers operational flexibility: an employer can select the fund manager and asset mix centrally for all employees, or allow employees to choose individually."),
            ("WORKED EXAMPLE: CORPORATE TAX SAVINGS",
             "Example: Salary bill = Rs. 10 Crores. Employer contributes 10% = Rs. 1 Crore. Full Rs. 1 Crore deducted from taxable profit!",
             "Corporate Math Example: A corporate has an eligible Basic + DA payroll of Rs. 10,00,00,000. It contributes 10% (Rs. 1,00,00,000) to employee NPS. The entire Rs. 1,00,00,000 is deducted as business expense, reducing corporate taxable income.",
             RED,
             "Consider this calculation: on an eligible payroll of 10 crore rupees, a 10 percent employer contribution equals 1 crore rupees. The entire 1 crore is deducted as a business expense."),
        ],
        "hook": "REMEMBER: Employer Contribution Up to 10% of (Basic + DA) = Deductible Business Expense!",
        "hook_say": "Remember: Employer pension contributions up to 10 percent of basic plus D.A. qualify as a deductible corporate business expense.",
        "covers": ["CORP-BENEFITS-TAX"],
        "calc_asserts": ["int(100000000 * 0.10) == 10000000"],
    },
    {
        "id": "c01_07_subscriber_benefits_and_tax",
        "chapter": "CHAPTER 7 • SECTION 5.3 & 5.4: SUBSCRIBER ADVANTAGES & INCOME TAX EXEMPTIONS",
        "title": "SECTION 5.3 & 5.4 — SUBSCRIBER TAX BENEFITS UNDER SECTION 80CCD(1) & 80CCD(2)",
        "accent": PINK, "badge": "SUBSCRIBER TAX",
        "q": "What tax exemptions do employees receive under Sections 80CCD(1) and 80CCD(2), and what are the eligibility criteria?",
        "q_say": "Sir, how does NPS help salaried employees reduce income tax, and what are the age and eligibility conditions?",
        "boxes": [
            ("ELIGIBILITY: CITIZENS AGED 18–60",
             "Any Indian citizen (resident or non-resident) aged 18 to 60 years on application date. KYC compliance via Form CS-S1.",
             "Section 5.4: Eligibility criteria: (1) Citizen of India, whether resident or non-resident; (2) Between 18–60 years of age on application submission date; (3) Full KYC compliance via registration form CS-S1. Pre-existing NPS account holders cannot open a duplicate account due to complete portability.",
             SKY,
             "Under Section 5.4, any Indian citizen, whether resident or non-resident, aged between 18 and 60 years can join through registration Form C.S. S. 1. Duplicate accounts are prohibited because your account is portable."),
            ("SECTION 80CCD(1) EMPLOYEE DEDUCTION",
             "Employee contribution up to 10% of (Basic + DA) is deductible under Section 80CCD(1) within the overall Rs. 1 Lakh cap.",
             "Section 5.3: Employee contribution to NPS up to 10% of basic plus DA is an allowable deduction under Section 80CCD(1) within the overall limit of Rs. 1 lakh (as detailed in Finance Bill 2011-12 provisions).",
             GREEN,
             "Under Section 80 C.C.D. 1, an employee's personal contribution up to 10 percent of basic pay plus dearness allowance is tax-deductible within the overall 1 lakh rupee limit."),
            ("SECTION 80CCD(2) EXCLUDED FROM 1 LAKH CAP",
             "Employer contribution up to 10% of (Basic + DA) under Section 80CCD(2) is DEDUCTIBLE AND EXCLUDED from the Rs. 1 Lakh ceiling!",
             "Section 5.3: 'The employer's contribution to NPS upto 10% of basic plus DA is allowed deduction under section 80CCD (2) and excluded from the limit of Rs. 1 lakh.' This offers additional tax savings over and above individual limits.",
             ORANGE,
             "The biggest tax advantage lies in Section 80 C.C.D. 2: employer contributions up to 10 percent of basic plus D.A. are deductible without being counted inside the 1 lakh rupee ceiling."),
            ("THE TRAP: NO DUPLICATE PRAN",
             "Trap: An individual already holding a PRAN cannot open a second PRAN; previous PRAN must be shifted via Form CS-S3!",
             "Exam Trap (Section 5.4): PRAN is fully portable across employers and geographies. Opening a second PRAN is illegal; the existing PRAN must be mapped to the corporate.",
             RED,
             "Remember: you can hold only one account number in your lifetime. If you already have an account, you must map it to your new corporate using Form C.S. S. 3 rather than opening a second one."),
        ],
        "hook": "REMEMBER: Sec. 80CCD(1) Within Rs. 1L Cap • Sec. 80CCD(2) Employer 10% EXCLUDED From Cap!",
        "hook_say": "Remember: Employee contributions fall under Section 80 C.C.D. 1 within the limit, while employer contributions under 80 C.C.D. 2 stand outside the cap.",
        "covers": ["SUB-BENEFITS-TAX"],
    },
    {
        "id": "c01_08_active_vs_auto_choice",
        "chapter": "CHAPTER 8 • SECTION 5.6: INVESTMENT CHOICES (ACTIVE CHOICE VS AUTO CHOICE)",
        "title": "SECTION 5.6 — ACTIVE CHOICE (ASSET CLASSES E, C & G) VS AUTO CHOICE (LIFECYCLE FUND)",
        "accent": SKY, "badge": "INVESTMENT CHOICE",
        "q": "What is the difference between Active Choice and Auto Choice, and what are Asset Classes E, C, and G?",
        "q_say": "Sir, how can a subscriber decide where his pension money is invested across equity, bonds, and government securities?",
        "flow": "asset_allocation_flow",
        "boxes": [
            ("THREE ASSET CLASSES DEFINED",
             "Class E = Predominantly Equity. Class C = Fixed Income (Corporate Bonds). Class G = Government Securities.",
             "Section 5.6: Portfolio allocation spans 3 classes: (1) Asset Class E: Investment in predominantly equity market instruments; (2) Asset Class C: Investment in fixed income instruments other than Government Securities; (3) Asset Class G: Investment in Government Securities.",
             SKY,
             "Section 5.6 outlines three asset classes: Asset Class E invests in equity shares, Asset Class C invests in corporate debt and fixed income, and Asset Class G invests in Government Securities."),
            ("ACTIVE CHOICE (50% EQUITY CAP)",
             "Subscriber actively sets percentage across E, C, and G. Asset Class E (Equity) is capped at a MAXIMUM of 50%.",
             "Section 5.6(B): Active Choice allows the corporate or subscriber to actively decide the asset allocation across classes, provided that the allocation to Asset Class E (Equity) does NOT exceed 50%.",
             GREEN,
             "Under Active Choice, you set your own investment percentages across E, C, and G. However, equity investment in Class E is capped at a strict maximum of 50 percent."),
            ("AUTO CHOICE (LIFECYCLE FUND)",
             "Lifecycle fund automatically manages allocation based on age. Stays 50% E up to age 35, then rebalances yearly.",
             "Section 5.6(B): In Auto Choice, funds are invested in a Lifecycle Fund where asset mix is determined by a pre-defined matrix according to subscriber age. It maintains 50% Equity, 30% Corporate Debt, and 20% G-Sec up to age 35, rebalancing annually thereafter.",
             ORANGE,
             "Under Auto Choice, an automated Lifecycle Fund rebalances your portfolio based on age. It maintains 50 percent equity up to age 35, gradually reducing risk as you get older."),
            ("THE TRAP: 50% EQUITY CEILING",
             "Trap: You CANNOT allocate 100% or 75% to Equity under the Corporate Brochure rules; Class E ceiling is 50%!",
             "Exam Trap (Section 5.6): Candidates often assume equity can be 100%. Under the Corporate Model brochure rules, Class E is strictly limited to 50% maximum.",
             RED,
             "Do not forget this limit: under the brochure rules, you cannot choose 100 percent equity. Asset Class E is capped at a maximum of 50 percent."),
        ],
        "hook": "REMEMBER: Asset Class E = Max 50% • Auto Choice Rebalances With Age • E=Equity, C=Corporate, G=G-Sec!",
        "hook_say": "Remember: Active choice caps equity at 50 percent, while Auto Choice automatically lowers risk as your age increases.",
        "covers": ["INVESTMENT-CHOICE"],
    },
    {
        "id": "c01_09_lifecycle_fund_matrix",
        "chapter": "CHAPTER 9 • SECTION 5.6: LIFECYCLE FUND AGE-WISE ASSET MATRIX",
        "title": "SECTION 5.6 — HOW DOES AUTO CHOICE REBALANCE FROM AGE 35 TO 55?",
        "accent": ORANGE, "badge": "LIFECYCLE MATRIX",
        "q": "What exact percentages are allocated to Asset Classes E, C, and G each year between ages 35 and 55?",
        "q_say": "Sir, how does the Lifecycle matrix adjust equity, corporate debt, and government securities as an employee ages?",
        "boxes": [
            ("ANCHOR BASELINE: UP TO AGE 35",
             "Up to 35 years: Asset Class E = 50%, Asset Class C = 30%, Asset Class G = 20%. Maximum growth phase.",
             "Section 5.6 Table: Up to age 35, portfolio is locked at: 50% Equity (E), 30% Corporate Debt (C), and 20% Government Securities (G). Total = 100%.",
             SKY,
             "Review the baseline: up to age 35, your portfolio holds 50 percent equity, 30 percent corporate bonds, and 20 percent government securities for capital growth."),
            ("ANNUAL DECAY PATTERN (AGES 36–55)",
             "From age 36: Equity (E) drops 2% per year (50% to 10%). Corporate Debt (C) drops 1% per year (30% to 10%). G-Sec rises.",
             "Section 5.6 Matrix Dynamics: Each year from age 36 to 55, Asset Class E decreases by 2% annually, Asset Class C decreases by 1% annually, and Asset Class G absorbs the remaining 3% annually, increasing from 20% up to 80%.",
             GREEN,
             "Starting at age 36, equity reduces by 2 percent every year, corporate debt reduces by 1 percent, and safe government securities increase by 3 percent each year."),
            ("TERMINAL ALLOCATION AT AGE 55",
             "At age 55: Asset Class E = 10%, Asset Class C = 10%, Asset Class G = 80%. Capital preservation phase.",
             "Section 5.6 Table: By age 55, allocation reaches conservative terminal values: Equity E drops to 10%, Corporate Debt C drops to 10%, and Government Securities G reaches 80% to protect accumulated wealth from market volatility before retirement.",
             ORANGE,
             "By age 55, your portfolio reaches conservative safety: equity and corporate debt drop to 10 percent each, while government securities increase to 80 percent."),
            ("WORKED EXAMPLE: AGE 45 ALLOCATION",
             "Example at age 45: E = 30%, C = 20%, G = 50%. (50 - 2*10 = 30% E; 30 - 1*10 = 20% C; 20 + 3*10 = 50% G).",
             "Arithmetic Verification: For a 45-year-old subscriber: Elapsed years over 35 = 10 years. Equity reduction = 10 * 2% = 20% -> E = 50% - 20% = 30%. Corporate Debt reduction = 10 * 1% = 10% -> C = 30% - 10% = 20%. G-Sec increase = 10 * 3% = 30% -> G = 20% + 30% = 50%. Sum = 30 + 20 + 50 = 100%.",
             RED,
             "Let us verify age 45: 10 years past age 35 reduces equity by 20 percent to 30 percent, drops debt to 20 percent, and raises government bonds to 50 percent, balancing at 100 percent."),
        ],
        "hook": "REMEMBER: Up to Age 35: 50% E, 30% C, 20% G • Age 55: 10% E, 10% C, 80% G!",
        "hook_say": "Remember: The matrix starts at 50 percent equity up to age 35, and shifts to 80 percent government securities by age 55.",
        "covers": ["LIFECYCLE-MATRIX"],
        "calc_asserts": [
            "50 - (45 - 35) * 2 == 30",
            "30 - (45 - 35) * 1 == 20",
            "20 + (45 - 35) * 3 == 50",
            "30 + 20 + 50 == 100",
            "10 + 10 + 80 == 100"
        ],
    },
    {
        "id": "c01_10_tier1_vs_tier2_accounts",
        "chapter": "CHAPTER 10 • SECTION 5.7 & 5.8: TIER-I VS TIER-II ACCOUNTS & CONTRIBUTION PATTERNS",
        "title": "SECTION 5.7 & 5.8 — TIER-I (RETIREMENT) VS TIER-II (SAVINGS) & CONTRIBUTION MODELS",
        "accent": GREEN, "badge": "TIER-I VS TIER-II",
        "q": "What are the structural differences between Tier-I and Tier-II accounts, and who pays contributions?",
        "q_say": "Sir, can a subscriber withdraw money anytime from Tier-I, and how does voluntary Tier-II operate?",
        "boxes": [
            ("TIER-I: PENSION ACCOUNT (NON-WITHDRAWABLE)",
             "Non-withdrawable retirement account. Tax benefits available. Employer & employee contribute. Charges borne by either.",
             "Section 5.7: Tier-I is a non-withdrawable retirement account where employer and employee contribute. Income Tax benefits under the Income Tax Act, 1961 are available. Tier-I charges can be borne either by the Corporate or Subscriber at corporate discretion.",
             SKY,
             "Under Section 5.7, Tier-I is your core, non-withdrawable retirement pension account. It provides full tax exemptions, and administrative charges can be covered by your employer."),
            ("TIER-II: VOLUNTARY SAVINGS FACILITY",
             "Voluntary savings account. Anytime liquidity and withdrawal. NO tax benefits. Charges borne strictly by subscriber.",
             "Section 5.7: Tier-II is an open-access voluntary savings facility with low fund management fees. Subscribers can withdraw funds whenever they wish. Tax benefits do NOT apply to Tier-II. Charges are borne strictly by the subscriber.",
             GREEN,
             "Tier-II is an optional investment account with complete withdrawal flexibility. However, it offers no tax deductions, and operating charges are paid entirely by the subscriber."),
            ("SWITCHING RULES & ACTIVATION FORMS",
             "Activate via CS-S1 (composite) or UOS-S10 later. Tier-II funds can switch to Tier-I, but Tier-I CANNOT switch to Tier-II!",
             "Section 5.7: Tier-II is activated via form CS-S1 or later via UOS-S10 at the same POP. Crucial Rule: Tier-II accumulations can be switched to Tier-I, but Tier-I funds can NEVER be shifted to Tier-II.",
             ORANGE,
             "For account operations: you can transfer money from Tier-II into your Tier-I retirement account, but retirement funds in Tier-I can never be transferred back into Tier-II."),
            ("FLEXIBLE CONTRIBUTION PATTERNS (5.8)",
             "Three variations: (1) Equal employer/employee, (2) Unequal contribution, (3) Contribution by employer or employee only.",
             "Section 5.8: The NPS Corporate platform permits all 3 contribution variations: (1) Equal contributions by employer and employee, (2) Unequal contributions by both, (3) Contribution from either the employer alone or the employee alone.",
             RED,
             "Section 5.8 gives maximum flexibility: employers and employees can contribute equal amounts, unequal percentages, or let either party contribute independently."),
        ],
        "hook": "REMEMBER: Tier-I = Non-Withdrawable & Tax Perks • Tier-II = Anytime Liquidity • Tier-II Switches to Tier-I Only!",
        "hook_say": "Remember: Tier-I is your tax-exempt retirement account, Tier-II offers anytime withdrawals, and funds can switch only from Tier-II into Tier-I.",
        "covers": ["TIER1-VS-TIER2"],
    },
    {
        "id": "c01_11_minimum_contributions_and_dormancy",
        "chapter": "CHAPTER 11 • SECTION 5.9 & 5.10: MINIMUM CONTRIBUTIONS & DORMANCY PENALTIES",
        "title": "SECTION 5.9 & 5.10 — MINIMUM CONTRIBUTION THRESHOLDS & DORMANCY RULES",
        "accent": BLUE, "badge": "MIN CONTRIBUTIONS",
        "q": "What are the minimum contribution amounts for Tier-I and Tier-II, and what penalty applies on default?",
        "q_say": "Sir, what is the least amount a subscriber must deposit each year, and what happens if he misses a payment?",
        "boxes": [
            ("TIER-I CONTRIBUTION THRESHOLDS (5.9)",
             "Minimum per contribution: Rs. 500. Minimum per year: Rs. 6,000. Minimum frequency: 1 contribution per year.",
             "Section 5.9: Minimum contribution requirements for Tier-I account: (1) Minimum amount per contribution = Rs. 500; (2) Minimum total contribution per financial year = Rs. 6,000; (3) Minimum number of contributions per financial year = 1.",
             SKY,
             "Under Section 5.9, Tier-I accounts require at least 500 rupees per deposit, an annual minimum total of 6,000 rupees, and at least one deposit every financial year."),
            ("TIER-II CONTRIBUTION THRESHOLDS (5.10)",
             "Minimum per contribution: Rs. 250. Minimum year-end balance: Rs. 2,000. Minimum frequency: 1 contribution per year.",
             "Section 5.10: Minimum contribution requirements for Tier-II account: (1) Minimum amount per contribution = Rs. 250; (2) Minimum account balance at the end of each financial year = Rs. 2,000; (3) Minimum frequency = 1 contribution per year.",
             GREEN,
             "For Tier-II accounts under Section 5.10, the minimum deposit is 250 rupees, with an annual requirement of at least one deposit and a year-end closing balance of 2,000 rupees."),
            ("DEFAULT PENALTY: RS. 100 PER YEAR",
             "Failure to meet minimum: Account becomes DORMANT and bears a default penalty of Rs. 100 per year of default.",
             "Section 5.10 Penalty: If the subscriber contributes less than the minimum in a year, then he would have to bear a default penalty of Rs. 100 per year of default and the account would become dormant.",
             ORANGE,
             "If you deposit less than the mandatory minimum in a financial year, your account turns dormant and a default penalty of 100 rupees per year is charged."),
            ("REACTIVATION & CLOSURE RULES",
             "Reactivate by paying minimum dues plus Rs. 100 penalty. Account is permanently closed when account value falls to zero.",
             "Section 5.10 Reactivation: To reactivate, subscriber pays missed minimum contributions plus Rs. 100 penalty for the dormancy period. A dormant account is permanently closed when its value drops to zero through fee deductions.",
             RED,
             "To unfreeze a dormant account, pay the missed contributions along with the 100-rupee penalty. If fees erode the balance to zero, the account closes permanently."),
        ],
        "hook": "REMEMBER: Tier-I Min: Rs. 500/dep & Rs. 6,000/yr • Tier-II Min: Rs. 250/dep & Rs. 2,000 bal • Penalty: Rs. 100!",
        "hook_say": "Remember: Tier-I requires 6,000 rupees a year, Tier-II requires a 2,000-rupee year-end balance, and missing payments costs a 100-rupee penalty.",
        "covers": ["MIN-CONTRIBUTIONS"],
        "calc_asserts": ["500 * 12 == 6000"],
    },
    {
        "id": "c01_12_pop_and_intermediary_charges",
        "chapter": "CHAPTER 12 • SECTION 5.11 & 5.12: POP, CRA, CUSTODIAN & TRUSTEE BANK CHARGES",
        "title": "SECTION 5.11 & 5.12 — INTERMEDIARY FEE STRUCTURE & ALL FIVE CRITICAL FOOTNOTES",
        "accent": RED, "badge": "CHARGES TABLE",
        "q": "What fees are charged across intermediaries, and what do Footnotes 1 through 5 specify about services and taxes?",
        "q_say": "Sir, how much commission does a Point of Presence charge, and what do the five footnotes say about CRA and Custodian fees?",
        "boxes": [
            ("POP CHARGES (SECTION 5.11)",
             "Initial: Rs. 100 + 0.25% (min Rs. 20, max Rs. 25,000). Subsequent: 0.25% (min Rs. 20, max Rs. 25,000). Non-fin: Rs. 20.",
             "Section 5.11: Existing POP charges under All Citizens Model: (1) Initial registration & contribution upload = Rs. 100 plus 0.25% of contribution (min Rs. 20, max Rs. 25,000) collected upfront; (2) Subsequent transaction = 0.25% of contribution (min Rs. 20, max Rs. 25,000); (3) Any non-contribution transaction = Rs. 20.",
             SKY,
             "Under Section 5.11, Points of Presence charge 100 rupees plus 0.25 percent on initial registration, and 0.25 percent on future deposits, capped between 20 and 25,000 rupees."),
            ("CRA CHARGES & FOOTNOTE 1",
             "Open: Rs. 50. Annual: Rs. 225. Per txn: Rs. 5. Footnote 1: Annual fee includes printed account statement sent once a year.",
             "Section 5.12 & Footnote 1: Central Recordkeeping Agency (NSDL) charges: PRA opening Rs. 50; Annual maintenance Rs. 225; Per transaction Rs. 5 (recovered via unit cancellation). Footnote 1 clarifies that annual maintenance includes electronic balance records, processing electronic changes, and sending a printed account statement once a year.",
             GREEN,
             "Recordkeeping agency N.S.D.L. charges 50 rupees for opening, 225 rupees annually, and 5 rupees per transaction. Footnote 1 confirms that your annual fee covers a printed account statement sent once every year."),
            ("TRANSACTIONS & PFM IMF (FOOTNOTES 2 & 3)",
             "Footnote 2: Txn includes scheme change, withdrawal, and statement printing. Footnote 3: PFM fee based on average monthly assets.",
             "Section 5.12 Footnotes 2 & 3: Footnote 2 lists chargeable transactions: regular contributions, detail updates, scheme/PFM shifts, withdrawal processing, and duplicate statement printing. Footnote 3: PFM Investment Management Fee is calculated on average monthly assets; includes brokerage and transaction costs, but excludes custodian charges and taxes.",
             ORANGE,
             "Footnote 2 details transactions like scheme changes and statement reprints. Footnote 3 notes that the fund manager's fee is calculated on average monthly assets and includes brokerage, but excludes custodian fees and taxes."),
            ("CUSTODIAN, TB & FOOTNOTE 5",
             "Custodian: 0.0075% pa (elec) / 0.05% pa (phys). TB: Rs. 0 (RBI) / Rs. 15 (non-RBI). Footnote 5: Demat/SEBI charges are EXTRA.",
             "Section 5.12 & Footnote 5: Custodian charges on asset value in custody = 0.0075% p.a. for electronic segment and 0.05% p.a. for physical segment. Trustee Bank = Rs. 0 for RBI locations, Rs. 15 for non-RBI locations (NAV deduction). Footnote 5 specifies that Demat/Remat, receipt of shares, and SEBI charges are extra.",
             RED,
             "Asset Custodian S.H.C.I.L. charges 0.0075 percent annually on electronic holdings, and Bank of India charges zero for R.B.I. centers. Footnote 5 adds that Demat and S.E.B.I. charges are billed extra."),
        ],
        "hook": "REMEMBER: POP Fee = 0.25% (Min Rs. 20, Max Rs. 25k) • CRA = Rs. 225/yr (Incl. Annual Printed Statement)!",
        "hook_say": "Remember: Points of Presence charge 0.25 percent capped between 20 and 25,000 rupees, while N.S.D.L. charges 225 rupees a year, including a printed statement.",
        "covers": ["FEE-STRUCTURE"],
        "calc_asserts": [
            "int(10000 * 0.0025) == 25",
            "20 <= 25 <= 25000"
        ],
    },
    {
        "id": "c01_13_exit_and_vesting_criteria",
        "chapter": "CHAPTER 13 • SECTION 5.13: EXIT, VESTING CRITERIA & THE 10% PHASED RULE",
        "title": "SECTION 5.13 — WITHDRAWAL RULES: PRE-60, AGE 60 TO 70, AND DEATH CLAIMS",
        "accent": YELLOW, "badge": "WITHDRAWAL RULES",
        "q": "What percentage of pension wealth can be withdrawn as a lump sum before age 60, at retirement, and upon death?",
        "q_say": "Sir, when can a subscriber withdraw his NPS corpus, and how does phased withdrawal between age 60 and 70 work?",
        "flow": "exit_criteria_flow",
        "boxes": [
            ("PREMATURE EXIT (BEFORE AGE 60)",
             "Before 60 years: Must invest MINIMUM 80% in life annuity; maximum 20% can be withdrawn as lump sum.",
             "Section 5.13: At any point in time before 60 years of age, subscriber must invest at least 80% of pension wealth to purchase an immediate life annuity from an IRDA-regulated life insurer. The remaining 20% may be withdrawn as a lump sum.",
             SKY,
             "Under Section 5.13, if you exit early before turning 60, you must lock in at least 80 percent of your wealth to buy a monthly annuity. Only 20 percent is paid out as lump sum."),
            ("RETIREMENT EXIT & 10% PHASED RULE",
             "At age 60: Min 40% annuity; 60% lump sum. Phased exit: Must withdraw MINIMUM 10% lump sum every year up to age 70.",
             "Section 5.13: On attaining age 60 (up to 70): (1) Minimum 40% invested in life annuity; (2) Remaining 60% withdrawn as lump sum or in a phased manner between 60 and 70. In phased withdrawal, subscriber MUST withdraw minimum 10% of pension wealth every year. Compulsory lump-sum closure at age 70.",
             GREEN,
             "At age 60, retirement rules apply: you invest at least 40 percent in an annuity, and withdraw the remaining 60 percent as a lump sum or phased up to age 70. In phased withdrawal, you must take out at least 10 percent each year."),
            ("DEATH BENEFIT (100% LUMP SUM)",
             "Death due to any cause: 100% of the NPS pension wealth can be received by the nominee as a lump sum.",
             "Section 5.13: In the unfortunate event of death due to any cause, option is available to the nominee to receive 100% of the accumulated NPS pension wealth in lump sum.",
             ORANGE,
             "In the event of death, the nominee has the option to receive 100 percent of the accumulated pension corpus as an immediate lump sum payment."),
            ("THE TRAP: MANDATORY CLOSURE AT 70",
             "Trap: You cannot stay invested past age 70; any amount remaining at age 70 MUST be compulsorily withdrawn!",
             "Exam Trap (Section 5.13): Phased withdrawal is allowed only between age 60 and 70. Any credit remaining at age 70 must be compulsorily liquidated.",
             RED,
             "Do not forget this deadline: you cannot keep funds invested past age 70. Any remaining balance at age 70 must be compulsorily withdrawn."),
        ],
        "hook": "REMEMBER: Pre-60: Min 80% Annuity • Age 60: Min 40% Annuity (Min 10%/yr Phased) • Death: 100% Cash!",
        "hook_say": "Remember: Before age 60, 80 percent goes to an annuity. At age 60, 40 percent goes to an annuity with at least 10 percent taken yearly if phased. On death, 100 percent goes to the nominee.",
        "covers": ["EXIT-CRITERIA"],
        "calc_asserts": [
            "80 + 20 == 100",
            "40 + 60 == 100"
        ],
    },
    {
        "id": "c01_14_types_of_annuity",
        "chapter": "CHAPTER 14 • SECTION 5.14: TYPES OF ANNUITY PLANS OFFERED BY ASPs",
        "title": "SECTION 5.14 — THE SIX STANDARD ANNUITY SCHEMES OFFERED BY LIFE INSURERS",
        "accent": PINK, "badge": "ANNUITY TYPES",
        "q": "What are the six standard types of annuity schemes subscribers can select from upon retirement?",
        "q_say": "Sir, when buying a monthly pension with the retirement corpus, what annuity options do life insurance companies offer?",
        "boxes": [
            ("LIFE ANNUITY & GUARANTEED CERTAIN",
             "Scheme 1: Uniform life pension to annuitant. Scheme 2: Pension guaranteed for 5, 10, 15, or 20 years certain, and thereafter for life.",
             "Section 5.14: (1) Pension payable for life at a uniform rate to the annuitant only; (2) Pension payable for 5, 10, 15, or 20 years certain and thereafter as long as the annuitant is alive.",
             SKY,
             "Under Section 5.14, Scheme 1 pays a uniform monthly pension for life. Scheme 2 guarantees pension payments for 5, 10, 15, or 20 years certain, and continues as long as you live thereafter."),
            ("RETURN OF PURCHASE PRICE & 3% INCREASING",
             "Scheme 3: Life pension with Return of Purchase Price on death. Scheme 4: Life pension increasing at simple 3% pa.",
             "Section 5.14: (3) Pension for life with return of purchase price on death of the annuitant to nominees; (4) Pension payable for life increasing at a simple rate of 3% per annum to offset inflation.",
             GREEN,
             "Scheme 3 returns the full purchase price to your family upon death. Scheme 4 provides an increasing pension that rises at a simple rate of 3 percent per year."),
            ("SPOUSE SURVIVOR PLANS (50% & 100%)",
             "Scheme 5: Life pension with 50% annuity to spouse on death. Scheme 6: Life pension with 100% annuity to spouse on death.",
             "Section 5.14: (5) Pension for life with provision of 50% annuity payable to spouse during lifetime upon death; (6) Pension for life with provision of 100% annuity payable to spouse during lifetime upon death.",
             ORANGE,
             "Schemes 5 and 6 protect your family: Scheme 5 pays a 50 percent pension to the surviving spouse, while Scheme 6 continues the full 100 percent pension for the spouse's lifetime."),
            ("THE TRAP: ANNUITY CHOICE IS FINAL",
             "Trap: Once an annuity is purchased from an ASP, the chosen annuity option CANNOT be altered or surrendered!",
             "Exam Trap (Section 5.14): Annuity selection is irrevocable under insurance contract laws; choose your scheme with care.",
             RED,
             "Keep this in mind: once an annuity contract is executed with a life insurer, the option is permanent and cannot be changed or surrendered."),
        ],
        "hook": "REMEMBER: 6 Annuity Types: Uniform Life • Certain Period • Return of Purchase Price • 3% Rise • Spouse 50%/100%!",
        "hook_say": "Remember the six annuity options: flat life pension, guaranteed term, return of capital, 3 percent yearly growth, and spouse survivor coverage.",
        "covers": ["ANNUITY-TYPES"],
    },
    {
        "id": "c01_15_grievances_and_modifications",
        "chapter": "CHAPTER 15 • SECTION 5.15 & 5.16: GRIEVANCE REDRESSAL (CGMS) & MASTER CHANGES",
        "title": "SECTION 5.15 & 5.16 — MULTI-LAYERED GRIEVANCES & MASTER RECORD CORRECTION FORMS",
        "accent": SKY, "badge": "CGMS & FORMS",
        "q": "How can an employee lodge a complaint via CGMS, and which forms are used to update details or reissue PRAN cards?",
        "q_say": "Sir, if an employee faces an issue, how does the grievance system work, and which forms update subscriber records?",
        "boxes": [
            ("THREE GRIEVANCE CHANNELS (5.15)",
             "Multi-layered system: (1) Toll-Free IVR (1-800-222080); (2) Web Interface (cra-nsdl.com with I-PIN); (3) Physical form via POP to CGMS.",
             "Section 5.15: Grievances can be registered through: (1) Call Centre/IVR at toll-free 1-800-222080 (allots token number); (2) Web interface at cra-nsdl.com using I-PIN (generates online tracking token); (3) Physical complaint form submitted to Corporate/POP for upload to Central Grievance Management System (CGMS).",
             SKY,
             "Section 5.15 outlines three grievance channels: call the toll-free helpline, log into the web portal with your I-P.I.N. for an instant token, or submit a physical form to your Point of Presence."),
            ("SUBSCRIBER CHANGE FORMS (CS-S2 & CS-S3)",
             "Form CS-S2: Personal details, re-issue of I-PIN/T-PIN/PRAN card. Form CS-S3: Change of employer or scheme preference.",
             "Section 5.16: Subscriber submits Form CS-S2 for correction in personal master details and reissue of I-PIN, T-PIN, or PRAN card. Form CS-S3 is submitted for shifting employer or updating investment scheme preferences.",
             GREEN,
             "For updating records: submit Form C.S. S. 2 to correct personal details or reissue cards and passwords, and Form C.S. S. 3 to change employers or investment options."),
            ("CORPORATE MODIFICATION FORMS (CHO-2 & CHO-3)",
             "Form CHO-2: Corporate change in investment choice. Form CHO-3: Corporate request to change Point of Presence (POP).",
             "Section 5.16: Corporates update institutional settings by submitting: (1) Form CHO-2 for changes in central investment choices, and (2) Form CHO-3 for transferring the corporate account to a different Point of Presence (POP).",
             ORANGE,
             "Employers use two institutional forms: Form C.H.O. 2 updates central investment allocations, and Form C.H.O. 3 transfers the company's account to a new Point of Presence."),
            ("THE TRAP: TOKEN TRACKING",
             "Trap: Filing a complaint without securing an official CGMS token number leaves the grievance untraceable in the CRA audit trail!",
             "Exam Trap (Section 5.15): An acknowledgement token generated by CGMS is the sole statutory tracking identifier for PFRDA escalations.",
             RED,
             "Always secure your token number: whether registering complaints online or by phone, an official tracking token is required for all escalation follow-ups."),
        ],
        "hook": "REMEMBER: CGMS Helpline: 1-800-222080 • Form CS-S2: Master Changes • Form CS-S3: Change Employer/Scheme!",
        "hook_say": "Remember: Grievances use toll-free 1-800-222080, Form C.S. S. 2 updates personal details, and Form C.S. S. 3 changes your employer or scheme.",
        "covers": ["CGMS-FORMS"],
    },
    {
        "id": "c01_16_master_recap_and_annexure",
        "chapter": "CHAPTER 16 • SECTIONS 6 & 7: MASTER RECAP, OFFICIAL REFERENCES & REGISTERED POPs",
        "title": "SECTIONS 6 & 7 — COMPLETE MASTER RECAP, OFFICIAL WEBSITES & ANNEXURE A",
        "accent": GREEN, "badge": "RECAP & POP LIST",
        "q": "Can we summarize all key figures, statutory rules, websites, and registered POPs on one master slide?",
        "q_say": "Sir, before we conclude, can we review a rapid-fire summary of all fees, percentages, thresholds, and websites?",
        "boxes": [
            ("ARCHITECTURE & TAX RECAP",
             "Unbundled model: PFRDA, NPS Trust, BOI, NSDL, SHCIL, 6 PFMs, 7 ASPs. Sec 36(1)(iva) & 80CCD(2) 10% tax deductions.",
             "Master Recap: NPS Corporate launched Dec 2011. 10% employer contribution deductible as business expense for corporate, and tax-exempt for employee under Sec. 80CCD(2) over and above 80CCD(1). 6 PFMs, 7 ASPs, Custodian SHCIL, Trustee Bank BOI, CRA NSDL.",
             SKY,
             "Final review, card 1: The Corporate Model features an unbundled architecture with six fund managers and seven insurers. Ten percent employer contributions offer dual corporate tax deductions and personal tax exemptions."),
            ("INVESTMENT & ACCOUNT MATRIX",
             "Active Choice: Class E <= 50%. Auto Choice: 50% E up to 35, 10% E at 55. Tier-I min Rs. 500/dep & Rs. 6,000/yr (Rs. 100 penalty).",
             "Master Recap: Active choice limits equity to 50%. Lifecycle matrix shifts from 50% Equity at age 35 to 80% G-Sec at age 55. Tier-I annual minimum is Rs. 6,000; Tier-II minimum balance is Rs. 2,000.",
             GREEN,
             "Card 2: Equity is capped at 50 percent, the Lifecycle matrix rebalances automatically from age 35 to 55, and Tier-I requires 6,000 rupees annually to avoid a 100-rupee dormancy penalty."),
            ("CHARGES, EXIT & ANNUITIES",
             "POP fee 0.25% (Rs. 20-25k). CRA Rs. 225/yr. Pre-60: 80% Annuity. Age 60: 40% Annuity. Death: 100% Cash. 6 Annuity types.",
             "Master Recap: POP charge is 0.25% (Rs. 20-25,000). CRA annual charge is Rs. 225. Early exit before 60 demands 80% annuity; normal retirement at 60 requires 40% annuity with 60% cash (lump sum or phased to age 70 with min 10%/yr). Death grants 100% cash to nominee.",
             ORANGE,
             "Card 3: Points of Presence charge 0.25 percent, while N.S.D.L. charges 225 rupees annually. Premature exits require an 80 percent annuity, normal retirement requires 40 percent, and death pays 100 percent cash."),
            ("STATUTORY REFERENCES & ANNEXURE A",
             "PFRDA: pfrda.org.in. CRA: cra-nsdl.com. Helpline: 1800222080. Annexure A lists 52 registered POPs (SBI, PNB, HDFC, ICICI, etc.).",
             "Section 6 & 7: Official websites: pfrda.org.in and cra-nsdl.com. Toll-free numbers: CRA 1800222080, NPS Info Desk 1800110708. Annexure A registers 52 certified institutional POPs including all major public, private, and postal banks across India.",
             RED,
             "Card 4: Track accounts on pfrda.org.in and cra-nsdl.com, or dial 1800222080. Annexure A lists 52 registered Points of Presence delivering access nationwide."),
        ],
        "hook": "REMEMBER: NPS Corporate Model = Lowest Cost Pension • Dual Tax Breaks • Flexible 50% Equity & Auto Life-Cycle!",
        "hook_say": "Remember: The NPS Corporate Model combines low institutional costs, tax savings, flexible equity options, and secure life annuities.",
        "covers": ["MASTER-RECAP"],
    },
]

FLOWS = {
    "nps_core_architecture": {
        "nodes": [
            (80, 300, 420, 80, "CORPORATE / SUBSCRIBER", "KYC & Form CS-S1 Upload", SKY, 1),
            (570, 300, 430, 80, "POP / POP-SP INTERFACE", "Data & Funds Aggregator", GREEN, 2),
            (1070, 300, 360, 80, "CRA (NSDL) & TRUSTEE (BOI)", "PRAN Database & Clearing", ORANGE, 3),
            (1500, 300, 340, 80, "PFMs & CUSTODIAN (SHCIL)", "Portfolio Assets & Security", RED, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, GREEN, 3), (2, 3, ORANGE, 4)],
    },
    "asset_allocation_flow": {
        "nodes": [
            (80, 300, 420, 80, "INVESTMENT SELECTION", "Corporate or Subscriber", SKY, 1),
            (570, 300, 430, 80, "ACTIVE CHOICE", "Class E <= 50%, C & G", GREEN, 2),
            (1070, 300, 360, 80, "AUTO CHOICE (LIFECYCLE)", "Age Matrix: 50% E to 10% E", ORANGE, 3),
            (1500, 300, 340, 80, "PORTFOLIO EXECUTION", "Allocated to Chosen PFM", RED, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, GREEN, 3), (2, 3, ORANGE, 4)],
    },
    "exit_criteria_flow": {
        "nodes": [
            (80, 300, 420, 80, "VESTING / EXIT EVENT", "Pre-60, Age 60, or Death", SKY, 1),
            (570, 300, 430, 80, "PRE-60 EARLY EXIT", "Min 80% Annuity / 20% Cash", GREEN, 2),
            (1070, 300, 360, 80, "NORMAL EXIT AT AGE 60", "Min 40% Annuity / 60% Cash", ORANGE, 3),
            (1500, 300, 340, 80, "ANNUITY DISBURSAL", "Monthly Pension via ASPs", RED, 4),
        ],
        "edges": [(0, 1, SKY, 2), (1, 2, GREEN, 3), (2, 3, ORANGE, 4)],
    },
}

PART_STARTS = ["c01_01_evolution_and_concept", "c01_06_corporate_benefits_and_tax", "c01_11_minimum_contributions_and_dormancy"]
# ===== SCENES_END =====

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
    out = ["# PFRDA National Pension System (Corporate Sector Model) - Full-Wording Reference Sheet", "",
           "Every card on screen is a short key-point; the full verbatim text / official terms are compiled here.", ""]
    for sc in SCENES:
        out += [f"## {sc['chapter']}", f"**{sc['title']}**  ({sc['badge']})", "", f"Q: {sc['q']}", ""]
        for (t, _b, _c, _n) in sc["boxes"]:
            out += [f"### {t}", FULL[(sc["id"], t)], ""]
        out += [f"> {sc['hook']}", ""]
    Path("nps_corporate_complete_reference_sheet.md").write_text("\n".join(out), encoding="utf-8")

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
    for size in range(start, min_size - 1, -1):
        f = font(size, bold)
        lines = wrap_text(draw, text, f, max_w)
        lh = int(size * spacing)
        if len(lines) * lh <= max_h:
            return f, lines, lh, size
    raise ValueError(f"CARD TOO DENSE (needs < {min_size}px): {text[:80]!r} - shorten on-screen text")

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
        raise ValueError(f"Flow node text wraps: {title!r} / {sub!r}")
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
            raise ValueError(f"Hook strip wraps: {scene['hook']!r}")
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
            print(f"{sc['id']}: HOOK wraps on line at >=20px ({len(sc['hook'])} chars)")
    print(f"\n{'ALL CARDS WITHIN BUDGET' if not bad else str(bad) + ' CARD(S) OVER BUDGET'}")
    return bad

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

    if args.audit:
        sys.exit(1 if audit_density() else 0)
    write_reference_sheet()
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
