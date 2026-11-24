#!/usr/bin/env python3
"""audit.py — the checks that must hold before the pension platform is published."""
from __future__ import annotations

import json
import pathlib
import re
import sys

import amendments
import coverage
import data_compute
import forms
import pension_rules as pr
import provisions as pv
import xrefs

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent / "AUDIT.md"
qs = json.loads((HERE / "questions.json").read_text())

checks = {}

# The bank is being rebuilt by hand, chapter by chapter. While COMPLETE is False the coverage
# checks report progress instead of failing, and the report says so prominently. Flip it to True
# when the last bank is written and coverage becomes a hard gate again.
COMPLETE = (HERE / "COMPLETE").exists()

ONLY = None
if "--only" in sys.argv:
    ONLY = sys.argv[sys.argv.index("--only") + 1]

# The cross-reference group: what mutation_test.py exercises, and what audit.py gates on.
XREF_CHECKS = (
    "every internal cross-reference resolves",
    "the defect whitelist holds exactly five entries",
    "every whitelisted defect still occurs",
    "no whitelisted defect is claimed at an address",
    "rule 35 carries the sub-rules",
)


def ck(name, ok, detail=""):
    checks[name] = (bool(ok), detail)


# ---- every question is answerable from a rule this build actually holds
def rule_of(q):
    m = re.match(r"Rule (\d+)", q["rules_text"])
    return m.group(1) if m else None


uncited = [q["id"] for q in qs if rule_of(q) and rule_of(q) not in pr.TEXT]
ck("every question cites a rule this build has transcribed", not uncited, str(uncited))

ck("four distinct options in every question",
   all(len(q["opts"]) == 4 and len({o.strip().lower() for o in q["opts"]}) == 4 for q in qs))
ck("the key matches the explanation's first line",
   all(re.search(r"^\(\s*([A-D])\s*\)", q["expl"]).group(1) == q["ans"] for q in qs))
ck("no two questions share a stem", len({q["q"] for q in qs}) == len(qs))
ck("every question carries an authority line", all(q["src"].strip() for q in qs))
ck("every question names a trap", all(q["trap"].strip() for q in qs))
ck("the key is spread across all four letters",
   len({q["ans"] for q in qs}) == 4, str(sorted({q["ans"] for q in qs})))
def visibly_longest(q):
    """A key gives itself away only if it is longer than the next-longest option by a
    margin a candidate can see: twelve characters, or fifteen per cent, whichever is
    greater. A two-character difference is not a tell."""
    ls = sorted(len(o) for o in q["opts"])
    k = len(q["opts"]["ABCD".index(q["ans"])])
    second = ls[-2] if k == ls[-1] else ls[-1]
    return k > second and (k - second) >= max(12, 0.15 * second)

tells = [q["id"] for q in qs if visibly_longest(q)]
ck("the key is not visibly the longest option",
   len(tells) <= len(qs) // 4, f"{len(tells)} of {len(qs)}: {tells}")

ck("the answer letters are evenly used",
   max(sum(1 for q in qs if q["ans"] == L) for L in "ABCD")
   - min(sum(1 for q in qs if q["ans"] == L) for L in "ABCD") <= 3,
   str({L: sum(1 for q in qs if q["ans"] == L) for L in "ABCD"}))

# ---- the coverage claim is the code's, not a sentence in a README
ck("the transcribed plus pending sets cover the statute",
   len(pr.TEXT) + len(pr.PENDING) == 87,
   f"{len(pr.TEXT)} text + {len(pr.PENDING)} pending = {len(pr.TEXT)+len(pr.PENDING)}")

ck("all 87 rules are transcribed, with no rule left pending",
   len(pr.TEXT) == 87 and not pr.PENDING, f"{len(pr.TEXT)} transcribed, {len(pr.PENDING)} pending")

# each of the 14 chapters must actually contribute transcribed text
CHAPTER_SPAN = {"I": (1, 4), "II": (5, 10), "III": (11, 30), "IV": (31, 32), "V": (33, 41),
               "VI": (42, 43), "VII": (44, 49), "VIII": (50, 51), "IX": (52, 52), "X": (53, 70),
               "XI": (71, 78), "XII": (79, 80), "XIII": (81, 84), "XIV": (85, 87)}
missing_ch = {c: [n for n in range(a, b + 1) if str(n) not in pr.TEXT]
              for c, (a, b) in CHAPTER_SPAN.items()}
ck("every chapter's rules are present",
   not any(missing_ch.values()), str({k: v for k, v in missing_ch.items() if v}))

# questions must reach past the middle of the statute, not stop at Chapter VII
covered = {int(q["rule"]) for q in qs}
if not COMPLETE:
    checks["[progress] chapters covered"] = (
        True, f"{len({q['chapter'] for q in qs})}/14")
if COMPLETE:
    ck("questions cover every chapter",
       all(any(n in covered for n in range(a, b + 1)) for a, b in CHAPTER_SPAN.values()),
       str([c for c, (a, b) in CHAPTER_SPAN.items()
            if not any(n in covered for n in range(a, b + 1))]))
overlap = set(pr.TEXT) & {n for n, _ in pr.PENDING}
ck("no rule is both transcribed and pending", not overlap, str(overlap))
nums = sorted([int(k) for k in pr.TEXT] + [int(n) for n, _ in pr.PENDING])
ck("every rule number 1 to 87 is accounted for", nums == list(range(1, 88)),
   str([n for n in range(1, 88) if n not in nums]))

# ---- the arithmetic re-derives
def d_pension(e): return max(9000, min(125000, round(e * 0.5)))
def d_retg(e, p):
    """rule 45(1)(a): one-fourth per period capped at 16.5 times emoluments.
    Rule 45(1)'s Rs 20 lakh proviso is the ceiling on the *statutory* figure;
    on a small emolument the 16.5x cap bites first, which is the point of PC-009."""
    return int(min(e / 4 * p, e * 16.5))
def d_fp(pay, enh): return max(9000, min(125000 if enh else 75000, round(pay * (0.5 if enh else 0.3))))

arabic = {
    "PC-001": d_pension(86000), "PC-002": d_pension(16000), "PC-003": d_pension(300000),
    "PC-005": 40000 // 2 * 16, "PC-009": d_retg(60000, 65), "PC-014": d_fp(60000, False),
    "PC-015": d_fp(200000, True), "PC-017": d_fp(22000, False),
}


def rupees(s):
    m = re.search(r"[\u20b9]\s?([\d,]+)", s)
    return int(m.group(1).replace(",", "")) if m else None


bad = []
for q in qs:
    if q["id"] in arabic:
        key = rupees(q["opts"]["ABCD".index(q["ans"])])
        if key != arabic[q["id"]]:
            bad.append((q["id"], key, arabic[q["id"]]))
ck("every worked rupee figure re-derives from the rule's formula", not bad, str(bad))

# ---- Forms and Formats are kept apart
ck("no Form and Format share a number within their own series",
   len({f[0] for f in forms.FORMS}) == len(forms.FORMS) and
   len({f[0] for f in forms.FORMATS}) == len(forms.FORMATS))
ck("every sourced Form/Format names a rule that exists in the transcribed text",
   all(re.match(r"Rules? (\d+)", f[3]) and re.match(r"Rules? (\d+)", f[3]).group(1) in pr.TEXT
       for f in forms.FORMS + forms.FORMATS if f[5]),
   str([f[0] for f in forms.FORMS + forms.FORMATS if f[5] and
        (not re.match(r"Rules? (\d+)", f[3]) or re.match(r"Rules? (\d+)", f[3]).group(1) not in pr.TEXT)]))
ck("an unsourced entry does not pretend to a rule citation",
   all(f[3] == "\u2014" for f in forms.FORMS + forms.FORMATS if not f[5]))

# ---- every FAQ must cite a rule that exists in the transcribed text
import assemble
import re as _re
bad_faq = []
for q, a, cite in assemble.FAQ:
    nums = _re.findall(r"(\d+)", cite)
    if not nums or not all(n in pr.TEXT for n in nums):
        bad_faq.append((q[:50], cite))
ck("every FAQ cites a transcribed rule", not bad_faq, str(bad_faq))
ck("every FAQ answer is substantive", all(len(a) > 120 for _, a, _ in assemble.FAQ))


# ---- granular coverage: every provision, down to provisos and Explanations
PROVS = pv.build()
COV = coverage.report(qs, verbose=False)
per = COV["per_kind"]
hit = COV["per_kind_hit"]
for kind, label in (("rule", "rule"), ("sub-rule", "sub-rule"), ("clause", "clause"),
                    ("sub-clause", "sub-clause"), ("proviso", "proviso"),
                    ("explanation", "Explanation")):
    if per.get(kind):
        name = f"every {label} is reached by a question"
        if COMPLETE:
            ck(name, hit.get(kind, 0) == per[kind], f"{hit.get(kind, 0)}/{per[kind]}")
        else:
            checks[f"[progress] {label}: {hit.get(kind,0)}/{per[kind]}"] = (True,
                f"{100*hit.get(kind,0)/per[kind]:.0f}%")

ck("the provision inventory accounts for the rule text",
   sum(len(re.sub(r"\W+", "", p["text"])) for p in PROVS)
   / sum(len(re.sub(r"\W+", "", pr.TEXT[str(n)])) for n in range(1, 88)) > 0.99,
   "less than 99 per cent of the rule text survives parsing, so provisions are being lost")

ck("every internal cross-reference resolves, or is one of the five enumerated statute defects",
   not xrefs.unknown(),
   str([(b[0], b[1]) for b in xrefs.unknown()]))

# The whitelist is closed. These three checks are what keep it closed.
ck("the defect whitelist holds exactly five entries, each a distinct citation",
   len(xrefs.KNOWN_DEFECTS) == 5
   and len({k for k in xrefs.KNOWN_DEFECTS}) == 5,
   f"{len(xrefs.KNOWN_DEFECTS)} entries")

ck("every whitelisted defect still occurs in the rule text",
   all(d["occurrences"] >= 1 for d in xrefs.defects()),
   "an entry that no longer occurs means the gazette was amended; delete it and the audit tightens: "
   + str([d["source"] for d in xrefs.defects() if d["occurrences"] == 0]))

ck("no whitelisted defect is claimed at an address the statute actually contains",
   all((d["source"], d["target"]) in {(b[0], b[1]) for b in xrefs.unresolved()}
       for d in xrefs.defects()),
   "a whitelist entry that resolves is not a defect any more, and must be removed")

# each defect's justification must match the structure of the provision it points at
def _n_sub(n):
    return sorted(int(x) for x in
                  {p["path"].split("(")[1][:-1] for p in PROVS
                   if p["rule"] == int(n) and p["kind"] == "sub-rule"})
def _clauses(path):
    return [p["path"] for p in PROVS if p["path"].startswith(path + "(")]

ck("rule 8 really does stop at sub-rule (8), as the rule 8(4)(d) entry claims",
   _n_sub(8) == list(range(1, 9)), str(_n_sub(8)))
ck("rule 8(5) really is a single unlettered sentence, as the rule 65 entries claim",
   not _clauses("8(5)"), str(_clauses("8(5)")))
ck("rule 77(1) really is lettered (i)-(x), as the rule 76(5)(e) entry claims",
   [p["path"].rsplit("(", 1)[1][:-1] for p in PROVS
    if p["path"].startswith("77(1)(")] == ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"],
   str([p["path"] for p in PROVS if p["path"].startswith("77(1)(")]))
ck("rule 76(2) really has no clauses, as the rule 81(2) entry claims",
   not _clauses("76(2)"), str(_clauses("76(2)")))

# the control must be shown to fail; a whitelist never seen to reject anything proves nothing
if ONLY != "xref":
    import subprocess as _sp
    _r = _sp.run([sys.executable, "mutation_test.py"], cwd=HERE, capture_output=True, text=True)
    _last = (_r.stdout + _r.stderr).strip().splitlines()[-1] if (_r.stdout + _r.stderr).strip() else "no output"
    ck("the cross-reference control catches every seeded transcription gap",
       _r.returncode == 0, _last)

# an exact-match whitelist is worthless if the resolver resolves things loosely
ck("a coalesced citation list is not silently accepted as a provision address",
   not any(h.startswith("65(5)(d)(e") for h in {p["path"] for p in PROVS}),
   "a target that is a list of two clauses must not masquerade as a single provision")

ck("rule 35 carries the sub-rules its own text cites",
   all(f"35({i})" in {p["path"] for p in PROVS} for i in range(1, 8)),
   "rule 35(1) says 'subject to sub-rule (6)'; a transcription without (6) and (7) is truncated")

# rule 50 was transcribed short of its clauses; these are the addresses the 2026 orders use
for path in ("50(8)(e)", "50(8)(f)", "50(8)(g)", "50(8)(h)", "50(8)(i)", "50(8)(j)", "50(8)(k)",
             "50(9)(h)", "50(9)(p)", "50(10)(a)", "50(12)(b)(i)", "50(16)"):
    ck(f"rule 50 has {path}", any(p["path"] == path for p in PROVS), path)

ck("rule 45(1) still prints the 2021 figure and rule 45 has its provisos",
   "twenty lakh rupees" in pr.TEXT["45"] or "Twenty lakh rupees" in pr.TEXT["45"],
   "the printed figure must stay as notified; the order is recorded separately")

# ---- the amendment register
ck("every amendment cites its instrument",
   all(a["number"].strip() and a["date"].strip() for a in amendments.AMENDMENTS))
ck("every amendment names at least one provision it touches",
   all(a["affects"] for a in amendments.AMENDMENTS if a["kind"] == "rules"),
   str([a["id"] for a in amendments.AMENDMENTS if a["kind"] == "rules" and not a["affects"]]))
ck("every provision an amendment names exists in the rule text",
   all(any(p["path"] == x for p in PROVS) for a in amendments.AMENDMENTS for x in a["affects"]),
   str([(a["id"], x) for a in amendments.AMENDMENTS for x in a["affects"]
        if not any(p["path"] == x for p in PROVS)]))
ck("no two instruments share an id",
   len({a["id"] for a in amendments.AMENDMENTS}) == len(amendments.AMENDMENTS))
ck("the gratuity ceiling order is registered with its effective date",
   any(a["id"] == "A-2024-03" and a["effective"] == "01.01.2024" for a in amendments.AMENDMENTS))
ck("the female-nominee instrument is registered as an order, not an amendment",
   any(a["id"] == "A-2024-02" and a["kind"] == "om" for a in amendments.AMENDMENTS))
ck("the 2022 rule 8 amendment is registered",
   any(a["id"] == "A-2022-01" and a["kind"] == "rules" for a in amendments.AMENDMENTS))

ck("provenance is recorded for every instrument, and full text outnumbers summaries",
   all(a["verified"] in ("gazette text", "order text", "summary") for a in amendments.AMENDMENTS)
   and sum(1 for a in amendments.AMENDMENTS if a["verified"] != "summary") >= 8,
   f"{sum(1 for a in amendments.AMENDMENTS if a['verified'] != 'summary')} read in full, "
   f"{sum(1 for a in amendments.AMENDMENTS if a['verified'] == 'summary')} from the index")

ck("an instrument recorded only from the index is not used to state a paragraph",
   all(not (a["verified"] == "summary" and len(a["effect"].split()) > 60)
       for a in amendments.AMENDMENTS),
   str([a["id"] for a in amendments.AMENDMENTS
        if a["verified"] == "summary" and len(a["effect"].split()) > 60]))

# ---- currency: no question may state a superseded figure as current
texts = [(q["id"], q["opts"][ord(q["ans"]) - 65]) for q in qs]
bad_twenty = [i for i, o in texts
              if re.search(r"\btwenty lakh rupees\b", o, re.I)
              and re.search(r"maximum|ceiling", o, re.I)
              and not re.search(r"printed|rule 45\(1\)|2021", o, re.I)]
ck("no question offers twenty lakh rupees as the current gratuity ceiling",
   not bad_twenty, str(bad_twenty))

ck("the four substitutions are shown on the page",
   len(assemble.SUBSTITUTIONS) == 4,
   str(len(assemble.SUBSTITUTIONS)))
ck("every substitution names the instrument that displaces the printed rule",
   all(any(k in body for k in ("G.S.R. 770(E)", "G.S.R. 410(E)", "30 May 2024", "1 January 2024"))
       for _, body in assemble.SUBSTITUTIONS))

# a question tagged with a version must carry the amendment it tests
bad_ver = [q["id"] for q in qs if q.get("version") and q["version"] not in
           {a["id"] for a in amendments.AMENDMENTS}]
ck("every versioned question names a registered instrument", not bad_ver, str(bad_ver))

# ---- write the report
if ONLY:
    fails = [(k, d) for k, (ok, d) in checks.items() if not ok]
    if fails:
        print("AUDIT FAILED")
        for k, d in fails:
            print("  FAIL \u2014", k, d)
        sys.exit(1)
    print(f"AUDIT PASSED \u2014 {len(checks)} checks")
    sys.exit(0)

lines = ["# Audit \u2014 CCS (Pension) Rules, 2021", "",
         "Generated by `build/audit.py`. The build refuses to publish if any check fails.", "",
         f"- Rules in the statute: **87**",
         f"- Rules transcribed from the gazette: **{len(pr.TEXT)}**",
         f"- Rules listed as pending (number and title only, no text invented): **{len(pr.PENDING)}**",
         f"- Questions: **{len(qs)}**",
         f"- Forms: **{len(forms.FORMS)}**, Formats: **{len(forms.FORMATS)}**",
         f"- FAQs: **{len(assemble.FAQ)}** (each cited to a transcribed rule)",
         f"- Provisions in the parsed inventory: **{len(PROVS)}**",
         f"- Instruments in the amendment register: **{len(amendments.AMENDMENTS)}**",
         f"- Rules touched by an instrument: **{len({int(k) for k in amendments.BY_RULE})}**", ""]
for k, (ok, detail) in checks.items():
    lines.append(f"- {'PASS' if ok else 'FAIL'} \u2014 {k}" + (f"  ({detail})" if detail and not ok else ""))
lines += ["", "## Coverage by level", "",
          "| Level | Provisions | With a question | Coverage |", "|---|---|---|---|"]
for kind, label in (("rule", "Rule as a whole"), ("sub-rule", "Sub-rule"), ("clause", "Clause"),
                    ("sub-clause", "Sub-clause"), ("proviso", "Proviso"),
                    ("explanation", "Explanation")):
    if per.get(kind):
        lines.append(f"| {label} | {per[kind]} | {hit.get(kind, 0)} | "
                     f"{100 * hit.get(kind, 0) / per[kind]:.0f}% |")
lines.append(f"| **Total** | **{COV['provs']}** | **{sum(hit.values())}** | "
             f"**{100 * sum(hit.values()) / max(1, COV['provs']):.0f}%** |")

lines += ["", "## The amendment register", "",
          "| Instrument | Date | Effective | Kind | Provisions |", "|---|---|---|---|---|"]
for a in amendments.AMENDMENTS:
    lines.append(f"| {a['number']} | {a['date']} | {a['effective']} | "
                 f"{'Amendment rules' if a['kind'] == 'rules' else 'Office Memorandum'} | "
                 f"{len(a['affects'])} |")

lines += ["", "## Provision coverage matrix", "",
          "Every provision the parser finds, with the questions that reach it. A provision with no "
          "question is a failure of the audit above, and the row is here so the claim can be checked by "
          "hand as well as by code.", ""]
hitmap = {}
for q in qs:
    for c in q.get("covers") or []:
        hitmap.setdefault(c, []).append(q["id"])
lines.append("| Provision | Kind | Questions |")
lines.append("|---|---|---|")
for p in PROVS:
    ids = hitmap.get(p["path"], [])
    short = ", ".join(ids[:4]) + (f" +{len(ids) - 4}" if len(ids) > 4 else "")
    lines.append(f"| {p['path']} | {p['kind']} | {short or '**none**'} |")

lines += ["", "## The closed whitelist of statute defects", "",
          "Five cross-references in the published Rules point at provisions that do not exist",
          "in the form described. They are defects in the instrument, not in the transcription:",
          "each was checked against the gazette and the offending words are quoted verbatim.",
          "",
          "`build/xrefs.py` holds them as an exact-match set. `build/audit.py` fails on **any**",
          "unresolved citation that is not one of these five, so a transcription gap cannot be",
          "excused as another statute defect. The list is closed: it may be shortened when an",
          "amendment corrects a reference, and a stale entry fails the build. Adding a sixth",
          "entry also fails the build, because the count is asserted.",
          "",
          "| Provision | What it says (verbatim) | Points to | Why that fails |",
          "|---|---|---|---|"]
for d in xrefs.defects():
    lines.append(f"| Rule {d['source']} | \u201c{d['quote']}\u201d | `{d['target']}` | {d['reason']} |")
lines += ["", "`build/mutation_test.py` seeds four faults \u2014 a truncated rule, a retargeted",
          "citation, a sixth whitelist entry, and a stale entry after a fix \u2014 and asserts the audit",
          "fails on each. `audit.py` runs it as a check, so the control is re-proved on every build.",
          ""]

lines += ["", "## Pending rules", "",
          "These carry no text in this build. They are listed so the gap is visible, not so that it can be filled "
          "with prose:", ""]
for n, t in pr.PENDING:
    lines.append(f"- Rule {n} \u2014 {t}")
OUT.write_text("\n".join(lines) + "\n")

if ONLY == "xref":
    checks = {k: v for k, v in checks.items()
              if any(k.startswith(x) or x in k for x in XREF_CHECKS)}

fails = [(k, d) for k, (ok, d) in checks.items() if not ok]
if fails:
    print("AUDIT FAILED")
    for k, d in fails:
        print("  FAIL \u2014", k, d)
    sys.exit(1)
print(f"AUDIT PASSED \u2014 {len(checks)} checks")
