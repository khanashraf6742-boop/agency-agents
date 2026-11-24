#!/usr/bin/env python3
"""assemble.py — build the single self-contained pension HTML file."""
from __future__ import annotations

import json
import pathlib

import amendments
import coverage
import forms
import xrefs
import provisions as pv
import pension_rules as pr
from titles import TITLES

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent / "CCS-Pension-Rules-2021-Exam-Platform.html"

# The places where quoting the 2021 text would state a superseded position. Kept as data so
# the audit can check that each one is shown on the page and that its figures are consistent
# with the instrument it cites.
SUBSTITUTIONS = [
    ("Gratuity ceiling: \u20b920 lakh in the rule, \u20b925 lakh in force",
     "Rule 45(1) caps retirement and death gratuity at twenty lakh rupees. The Office Memorandum of 30 May 2024 "
     "raised the maximum to twenty-five lakh rupees with effect from 1 January 2024, on the Seventh Pay "
     "Commission's trigger of dearness allowance reaching fifty per cent. Paragraph 7 of the order says the "
     "formal amendment to the Rules will be notified separately, so the printed rule has not caught up. A case "
     "decided today is settled at twenty-five lakh rupees."),
    ("Family pension to a child before the husband: an order, not an amendment",
     "Rule 50(8)(a) pays family pension to the widow or widower first. The Office Memorandum of 1 January 2024 "
     "allows a female Government servant or pensioner to ask that her eligible child be paid in precedence where "
     "divorce proceedings are pending or she has filed a case under the Domestic Violence Act, the Dowry "
     "Prohibition Act or the Indian Penal Code. Paragraph 6 of that order records that a formal amendment to "
     "rule 50 will be notified separately; none has been. The rule text still reads spouse-first and the order "
     "governs the case."),
    ("The authority that may withhold a pension: the President, in the 2021 text",
     "Rule 8(1) in the 2021 gazette reserves the power to the President. G.S.R. 770(E) dated 7 October 2022 "
     "substituted the sub-rule so that the power is exercised by the President only where the President is the "
     "appointing authority, otherwise by the Secretary of the administrative Ministry or Department, and by the "
     "Comptroller and Auditor-General for the Indian Audit and Accounts Department. The same instrument added "
     "sub-rule (6A), which allows an appeal to the President against an order of any other authority."),
    ("Form 4 and Form 6 at retirement: Form 6-A since 2024",
     "Rule 50(15)(e) and rule 57 required the family details in Form 4 and Form 6. G.S.R. 410(E) dated 16 July "
     "2024 substituted Form 6-A for both across rules 50, 53, 57, 58, 59, 60, 62, 63 and 80, and rewrote the "
     "proviso to rule 80(5) so that a gratuity nominee may submit Form 6-A in place of Form 10 where no family "
     "member is eligible. The notification gives the date of effect as one hundred twenty days after "
     "publication, which is 13 November 2024."),
]

CHAPTERS = [
    ("I", "Preliminary", 1, 4),
    ("II", "General Conditions", 5, 10),
    ("III", "Qualifying Service", 11, 30),
    ("IV", "Emoluments and Average Emoluments", 31, 32),
    ("V", "Classes of Pension and Conditions Governing their Grant", 33, 41),
    ("VI", "Premature Retirement and Voluntary Retirement", 42, 43),
    ("VII", "Regulation of Pension and Gratuity", 44, 49),
    ("VIII", "Family Pension", 50, 51),
    ("IX", "Dearness Relief", 52, 52),
    ("X", "Determination and Authorisation of Pension and Gratuity", 53, 70),
    ("XI", "Family Pension and Gratuity on Death or Disappearance in Service", 71, 78),
    ("XII", "Family Pension and Residuary Gratuity on Death or Disappearance of a Pensioner", 79, 80),
    ("XIII", "Payment of Pensions", 81, 84),
    ("XIV", "Miscellaneous", 85, 87),
]



FAQ = [
 ("What is the difference between a Form and a Format under these rules?",
  "Rule 3(1)(k) defines a Form as a form appended to these rules. Rule 3(1)(l) defines a Format as a format "
  "appended to them. They are two appended series, separately numbered, so Form 3 is the gratuity nomination "
  "(rule 46) while Format 3 is the memorandum of charges (rule 8(2)(c)). The prescribing clause, not the "
  "familiarity of the number, decides which one an answer needs.",
  "Rules 3(1)(k) and 3(1)(l)"),
 ("Does qualifying service begin on confirmation?",
  "No. Rule 11 begins it on the date the servant takes charge of the post to which he is first appointed, whether "
  "substantively, in an officiating capacity or on a temporary basis. Confirmation matters at rule 16, which says "
  "probation followed by confirmation qualifies, but it is not the commencement date.",
  "Rules 11 and 16"),
 ("How is a broken month handled in the average emoluments?",
  "A month is reckoned as thirty days, so fractional periods in the last ten months are multiplied by 14/30, 16/30 "
  "and so on, whatever the calendar length of the month, February included. Rule 32(3) works this through on a "
  "retirement dated 16 July 2019.",
  "Rule 32(3) and its Illustration"),
 ("What is the pension ceiling, and does it apply to family pension?",
  "Ordinary pension is subject to a minimum of \u20b99,000 and a maximum of \u20b91,25,000 a month under rule 44(1). "
  "Family pension is subject to the same minimum, but its ordinary maximum is \u20b975,000 under rule 50(2)(a)(i), "
  "rising to \u20b91,25,000 for the enhanced rate under rule 50(2)(a)(iv).",
  "Rules 44(1) and 50(2)"),
 ("Is the \u20b920 lakh gratuity ceiling still the operative figure?",
  "The text of rule 45(1), as notified in 2021, caps retirement gratuity and death gratuity at twenty lakh rupees. "
  "The ceiling was raised to twenty-five lakh rupees with effect from 1 January 2024 by a subsequent Office "
  "Memorandum, so a question that quotes the rule and a question that quotes current practice have different "
  "answers. This platform states the rule text and flags the change.",
  "Rule 45(1) proviso"),
 ("Which Forms does a retiring servant actually file?",
  "Form 4 for family particulars and Form 6 for the pension claim, each with a Format 9 undertaking to the bank, "
  "not later than six months before retirement under rule 57(2)(a). Form 7 is then completed by the Head of Office "
  "and the Accounts Officer under rules 59 and 63, and forwarded under a Format 10 covering letter.",
  "Rules 57(2), 59, 60 and 63"),
 ("What happens if the pension papers are not ready by the retirement date?",
  "Rule 62 authorises 100 per cent of pension as provisional pension and 100 per cent of gratuity as provisional "
  "gratuity while withholding ten per cent of the gratuity, and rule 62(4) requires that sanction within ten days "
  "after retirement on superannuation. If the final amounts are still not determined six months later, rule 62(7) "
  "makes the provisional amounts final.",
  "Rule 62"),
 ("How long must a family wait after reporting a missing servant?",
  "Six months from lodging the police report before family pension, including arrears, and gratuity may be paid, "
  "under rule 51(8)(a). Death gratuity becomes payable once death is conclusively established or on expiry of "
  "seven years from the report, whichever is earlier, under rule 51(8)(b).",
  "Rule 51(8)"),
 ("Can pension be reduced after it has been authorised?",
  "Only for a clerical error, under rule 66(2). If the error is detected more than two years after authorisation, "
  "the revision needs the concurrence of the Department of Pension and Pensioners' Welfare. Rule 66(4) then "
  "requires the Ministry to examine waiver of any resulting overpayment with the Ministry of Finance.",
  "Rule 66"),
 ("Which rules still govern a case pending when the 2021 Rules commenced?",
  "The old rules. Rule 87(1) repeals the 1972 Rules so far as the new rules cover the same matters, but rule "
  "87(2)(c) and (d) require pending pension, gratuity and family pension cases to be disposed of under the old "
  "rules as if the new rules had not been made.",
  "Rule 87(2)"),
]


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    qs = json.loads((HERE / "questions.json").read_text())
    css = (HERE / "app.css").read_text()

    total_chars = sum(len(pr.TEXT[str(n)]) for n in range(1, 88))
    total_words = sum(len(pr.TEXT[str(n)].split()) for n in range(1, 88))

    # ---- rule library, grouped by chapter
    chapters_html = []
    for num, title, lo, hi in CHAPTERS:
        rows = []
        for n in range(lo, hi + 1):
            text = pr.TEXT[str(n)]
            rows.append(f'''
<details class="rule-card" id="rule-{n}">
  <summary><b>Rule {n}. {esc(TITLES[n])}</b> <span class="muted">{len(text.split()):,} words</span></summary>
  <div class="rule-body"><div style="white-space:pre-wrap">{esc(text)}</div></div>
</details>''')
        chapters_html.append(
            f'<details class="chapter" id="ch-{num}" open><summary><b>Chapter {num}</b> \u2014 {title} '
            f'<span class="muted">rules {lo}\u2013{hi}</span></summary>{"".join(rows)}</details>')

    # ---- Forms / Formats registers
    def rows(entries):
        out = []
        for num, kind, title, rule, use, sourced in entries:
            status = ('<span class="ok">sourced</span>' if sourced
                      else '<span class="warn">not yet sourced</span>')
            out.append(f'<tr><td><b>{esc(num)}</b></td><td>{esc(title)}</td><td>{esc(rule)}</td>'
                       f'<td>{esc(use)}</td><td>{status}</td></tr>')
        return "".join(out)

    # ---- questions grouped by chapter
    by_ch = {}
    for q in qs:
        by_ch.setdefault(q["chapter"], []).append(q)

    def q_html(q):
        opts = "".join(
            f'<li class="{"key" if L == q["ans"] else ""}"><b>{L}</b>&nbsp;{esc(o)}</li>'
            for L, o in zip("ABCD", q["opts"]))
        return f'''
<div class="q-card" id="q-{q['id']}">
  <div class="q-head"><b>{q['id']}</b> \u00b7 Chapter {esc(q['chapter'])} \u00b7 {esc(q['rules_text'])}</div>
  <div class="q-stem">{esc(q['q'])}</div>
  <ol class="q-opts">{opts}</ol>
  <details class="q-expl"><summary>Answer and reasoning</summary><div style="white-space:pre-wrap">{esc(q['expl'])}</div></details>
</div>'''

    qs_html = []
    for num, title, lo, hi in CHAPTERS:
        grp = [q for q in qs if lo <= int(q["rule"]) <= hi]
        if not grp:
            continue
        qs_html.append(f'<h3>Chapter {num} \u2014 {title} <span class="muted">({len(grp)} questions)</span></h3>'
                       + "".join(q_html(q) for q in grp))
    leftovers = [q for q in qs if not any(lo <= int(q["rule"]) <= hi for _, _, lo, hi in CHAPTERS)]
    if leftovers:
        qs_html.append('<h3>Other</h3>' + "".join(q_html(q) for q in leftovers))

    # ---- defects in the instrument itself, with the offending words quoted
    defect_rows = "".join(
        f'<tr><td><b>Rule {esc(d["source"])}</b></td>'
        f'<td>\u201c{esc(d["quote"])}\u201d</td>'
        f'<td><code>{esc(d["target"])}</code></td>'
        f'<td>{esc(d["reason"])}</td></tr>'
        for d in xrefs.defects())

    # ---- amendment register
    amend_rows = []
    for a in sorted(amendments.AMENDMENTS, key=lambda x: (x["date"][-4:], x["date"][3:5], x["date"][:2])):
        badge = "rules" if a["kind"] == "rules" else "order"
        ver = ('<span class="pill full">full text</span>'
               if a["verified"] in ("gazette text", "order text")
               else '<span class="pill part">from the index</span>')
        provs = ", ".join(a["affects"][:6]) + (" ..." if len(a["affects"]) > 6 else "")
        provs = provs or "\u2014"
        amend_rows.append(
            f'<tr><td><b>{esc(a["number"])}</b><br><span class="muted">{esc(a["title"])}</span>'
            f'<br><span class="pill">{badge}</span>{ver}</td>'
            f'<td>{esc(a["date"])}<br><span class="muted">from {esc(a["effective"])}</span></td>'
            f'<td>{esc(a["effect"])}</td>'
            f'<td><span class="muted">{esc(provs)}</span></td></tr>')
    amend_rows = "".join(amend_rows)

    # ---- the four places where the order and the rule part company
    currency_html = "".join(
        f'<div class="delta"><b>{esc(t)}</b><div class="delta-body">{body}</div></div>'
        for t, body in SUBSTITUTIONS)

    # ---- coverage table
    cov = coverage.report(qs, verbose=False)
    order = [("rule", "Rule as a whole"), ("sub-rule", "Sub-rule"), ("clause", "Clause"),
             ("sub-clause", "Sub-clause"), ("proviso", "Proviso"), ("explanation", "Explanation")]
    cov_rows = "".join(
        f'<tr><td>{label}</td><td>{cov["per_kind"].get(k, 0):,}</td>'
        f'<td>{cov["per_kind_hit"].get(k, 0):,}</td>'
        f'<td>{100 * cov["per_kind_hit"].get(k, 0) / max(1, cov["per_kind"].get(k, 0)):.0f}%</td></tr>'
        for k, label in order if cov["per_kind"].get(k))
    cov_rows += (f'<tr class="total"><td><b>Total</b></td><td><b>{cov["provs"]:,}</b></td>'
                 f'<td><b>{sum(cov["per_kind_hit"].values()):,}</b></td>'
                 f'<td><b>{100 * sum(cov["per_kind_hit"].values()) / max(1, cov["provs"]):.0f}%</b></td></tr>')

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CCS (Pension) Rules, 2021 \u2014 Study Platform</title>
<style>
{css}
body{{font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;line-height:1.65;color:#1c1917;background:#fafaf9;margin:0}}
.wrap{{max-width:1040px;margin:0 auto;padding:24px 20px 90px}}
h1{{font-size:1.7rem;margin:0 0 4px;letter-spacing:-.01em}}
h2{{font-size:1.2rem;margin:36px 0 12px;padding-bottom:8px;border-bottom:2px solid #e7e5e4}}
h3{{font-size:1rem;margin:26px 0 8px;color:#44403c}}
.muted{{color:#78716c;font-weight:400;font-size:.85em}}
.ok{{color:#166534;font-weight:600}}
.warn{{color:#b45309;font-weight:600}}
.banner{{background:#f0f9ff;border:1px solid #bae6fd;border-radius:8px;padding:14px 16px;margin:18px 0;font-size:.92rem}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin:16px 0}}
.stat{{background:#fff;border:1px solid #e7e5e4;border-radius:8px;padding:10px 14px;font-size:.8rem;color:#57534e}}
.stat b{{display:block;font-size:1.5rem;color:#1e3a8a;font-weight:700;line-height:1.2}}
details.chapter{{margin:14px 0;border:1px solid #d6d3d1;border-radius:10px;padding:6px 14px;background:#fff}}
details.chapter>summary{{cursor:pointer;padding:8px 0;font-size:.98rem}}
details.rule-card{{border-top:1px solid #f5f5f4;padding:8px 0}}
details.rule-card summary{{cursor:pointer;font-size:.9rem}}
.rule-body{{margin-top:8px;font-size:.88rem;color:#292524;max-height:480px;overflow:auto;
  border-left:3px solid #c7d2fe;background:#f8fafc;padding:10px 14px;border-radius:4px}}
table{{border-collapse:collapse;width:100%;font-size:.84rem;background:#fff;margin:10px 0}}
th,td{{border:1px solid #e7e5e4;padding:7px 9px;text-align:left;vertical-align:top}}
th{{background:#f5f5f4;font-weight:600}}
.q-card{{background:#fff;border:1px solid #e7e5e4;border-radius:8px;margin:10px 0;padding:12px 15px}}
.q-head{{font-size:.78rem;color:#a8a29e;margin-bottom:6px;letter-spacing:.02em;text-transform:uppercase}}
.q-stem{{font-weight:600;margin-bottom:9px}}
.q-opts{{margin:0;padding-left:0;list-style:none;font-size:.92rem}}
.q-opts li{{margin:4px 0;padding-left:4px}}
.q-opts li.key{{font-weight:600;color:#166534;background:#f0fdf4;border-radius:4px;padding:4px 6px}}
details.q-expl{{margin-top:9px;font-size:.87rem}}
details.q-expl summary{{cursor:pointer;color:#1d4ed8;font-weight:500}}
details.q-expl div{{margin-top:8px;background:#f8fafc;border-left:3px solid #93c5fd;padding:10px 12px;border-radius:4px}}
nav.toc{{background:#fff;border:1px solid #e7e5e4;border-radius:8px;padding:12px 16px;font-size:.88rem}}
nav.toc a{{color:#1d4ed8;text-decoration:none;margin-right:12px;white-space:nowrap}}
nav.toc a:hover{{text-decoration:underline}}
.faq-item{{background:#fff;border:1px solid #e7e5e4;border-radius:8px;margin:8px 0;padding:10px 15px}}
.faq-item summary{{cursor:pointer;font-weight:600;font-size:.93rem}}
.faq-item div{{margin-top:8px;font-size:.9rem;color:#292524}}
.faq-item .cite{{color:#1d4ed8;font-size:.84rem;font-weight:600;margin:6px 0 0}}
</style>
</head>
<body>
<div class="wrap">
<h1>CCS (Pension) Rules, 2021</h1>
<p class="muted">G.S.R. 868(E), notified 20 December 2021 \u00b7 Department of Pension and Pensioners\u2019 Welfare \u00b7
87 rules in 14 chapters \u00b7 14 Forms and 13 Formats \u00b7 {len(qs)} questions</p>

<div class="banner">
<b>The whole statute.</b> All 87 rules are transcribed from the gazette text and reproduced here in full \u2014
{total_words:,} words, {total_chars:,} characters \u2014 grouped by chapter, with no rule summarised in place of its
text. The Forms and Formats are listed separately, because rule 3 treats them as two different things: a
<b>Form</b> is a form appended to the rules, a <b>Format</b> is a format appended to them.
</div>

<div class="stats">
  <div class="stat"><b>87/87</b>rules, full text</div>
  <div class="stat"><b>{total_words:,}</b>words of statute</div>
  <div class="stat"><b>{len(qs)}</b>questions</div>
  <div class="stat"><b>{len(forms.FORMS)}</b>Forms</div>
  <div class="stat"><b>{len(forms.FORMATS)}</b>Formats</div>
</div>

<nav class="toc">
<b>Chapters:</b>
{" ".join(f'<a href="#ch-{n}">{n}</a>' for n, _, _, _ in CHAPTERS)}
&nbsp;\u00b7&nbsp; <a href="#forms">Forms</a> <a href="#formats">Formats</a> <a href="#questions">Questions</a>
</nav>

<h2>The rule library</h2>
{"".join(chapters_html)}

<h2 id="amendments">The amendments and orders in force ({len(amendments.AMENDMENTS)})</h2>
<p class="muted">The 2021 gazette is the starting point, not the current position. Three sets of amendment rules
and fifteen office memoranda have changed or explained it since. Each entry says what it does, the date it takes
effect, and the provisions it touches. Where an order operates on a rule without amending its text, both are
shown: the rule as printed and the order as applied.</p>
<p class="muted"><b>full text</b> means the instrument was read in full and its paragraphs are
reflected in the questions. <b>from the index</b> means the instrument is listed in the
Department&rsquo;s own circular index and its effect is recorded from that listing; the paragraphs have
not been read in full, so the entry is a description of the instrument and not a substitute for it.
Eight of the eighteen were read in full.</p>
<table class="amend"><thead><tr><th>Instrument</th><th>Date</th><th>Effect</th><th>Provisions</th></tr></thead>
<tbody>{amend_rows}</tbody></table>

<h2 id="currency">Where the current order differs from the printed rule</h2>
<p class="muted">Four places where a figure or a rule quoted straight from the 2021 text would now be wrong.</p>
{currency_html}

<h2 id="coverage">Coverage, measured ({cov["provs"]:,} provisions)</h2>
<p class="muted">The platform claims to cover every rule, sub-rule, clause, sub-clause, proviso and Explanation.
That claim is measured at build time, not asserted: each provision the parser finds is matched against the
questions that cite it, and the build fails if any provision is left without one.</p>
<table class="cov"><thead><tr><th>Level</th><th>Provisions</th><th>With a question</th><th>Coverage</th></tr></thead>
<tbody>{cov_rows}</tbody></table>
<p class="muted">Every provision is listed in the coverage matrix in <code>AUDIT.md</code>, with the questions
that reach it.</p>

<h2 id="defects">Defects in the instrument itself ({len(xrefs.KNOWN_DEFECTS)})</h2>
<p class="muted">Five cross-references in the published Rules point at provisions that do not exist in the form
described. They are not transcription errors: each was checked against the gazette, and the offending words are
quoted below exactly as printed. The platform cannot correct them and does not silently repair them \u2014 it
records them, and the build fails if any <em>other</em> citation fails to resolve, so a transcription gap cannot
hide behind the statute&rsquo;s own drafting slips.</p>
<table class="defect"><thead><tr><th>Provision</th><th>What it says</th><th>Points to</th><th>Why that fails</th></tr></thead>
<tbody>{defect_rows}</tbody></table>
<p class="muted">Two of the five are the same sentence repeated: rule 65(5)(d) and (e) both send the reader to a
clause of rule 8(5) that was never lettered. The list is closed. If an amendment corrects one of these references,
the entry is deleted and the build tightens \u2014 a stale entry fails it.</p>

<h2 id="forms">Forms appended to the rules ({len(forms.FORMS)})</h2>
<p class="muted">Rule 3(1)(k): a Form is a form appended to these rules. Each entry gives the sub-rule that prescribes it.</p>
<table><thead><tr><th>Form</th><th>Title</th><th>Prescribed by</th><th>What it is for</th><th>Status</th></tr></thead>
<tbody>{rows(forms.FORMS)}</tbody></table>

<h2 id="formats">Formats appended to the rules ({len(forms.FORMATS)})</h2>
<p class="muted">Rule 3(1)(l): a Format is a format appended to these rules \u2014 a separate series, numbered from 1 again.</p>
<table><thead><tr><th>Format</th><th>Title</th><th>Prescribed by</th><th>What it is for</th><th>Status</th></tr></thead>
<tbody>{rows(forms.FORMATS)}</tbody></table>

<h2 id="questions">The questions ({len(qs)})</h2>
<p class="muted">Each answer is derived from the rule text above. Worked figures are re-checked against the
formulas in rules 44, 45 and 50 at build time.</p>
{"".join(qs_html)}

<h2 id="faq">Questions people actually ask ({len(FAQ)})</h2>
<p class="muted">Each answer is tied to the rule that decides it. Nothing here is stated without a rule citation.</p>
<div class="faq">
{"".join(f'<details class="faq-item"><summary>{esc(q)}</summary><div><p>{esc(a)}</p><p class="cite">Authority: {esc(r)}</p></div></details>' for q, a, r in FAQ)}
</div>

<h2>How this was built</h2>
<p class="muted" style="font-size:.88rem">
The rule text is transcribed from the gazette and every one of the 87 rules is present; the build fails if a rule
number is missing, if a question cites a rule the build does not hold, if a Form or Format cites a sub-rule that
cannot be resolved, or if a worked rupee figure does not re-derive from the formula it claims to apply. The
Formats are separated from the Forms throughout, because the statute separates them in rule 3 and a question that
asks for one has a different answer from a question that asks for the other.
</p>
</div>
</body>
</html>
'''
    OUT.write_text(html)
    print(f"wrote {OUT.name}: {len(html):,} bytes")
    print(f"  87 rules, {total_words:,} words, {len(qs)} questions, "
          f"{len(forms.FORMS)} Forms, {len(forms.FORMATS)} Formats")


if __name__ == "__main__":
    main()
