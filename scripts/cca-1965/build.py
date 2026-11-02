#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the CCS (CCA) Rules, 1965 case-study book as one self-contained HTML file.

Usage
    python3 scripts/cca-1965/build.py --out CCS_CCA_Rules_1965_Case_Studies_2026-11-02.html
    python3 scripts/cca-1965/build.py --audit

The build refuses to write the file if the audit finds a duplicate id, an
unresolved internal anchor, a case without marks, an empty required block, or
dangerous markup. Content modules are trusted (they are part of this repo);
the audit nevertheless rejects script injection patterns.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import meta
from l1 import L1_SETS
from l2a import L2A
from l2b import L2B
from l2c import L2C
from l2d import L2D
from l3a import L3A
from l3b import L3B
from l3c import L3C

L2 = L2A + L2B + L2C + L2D
L3 = L3A + L3B + L3C
CASES = L2 + L3

# Which rule(s) each L1 item turns on (explicit, so the rule index cannot drift).
L1_RULES = {
    1: ["3"], 2: ["3"], 3: ["2"], 4: ["12"], 5: ["8"], 6: ["4"], 7: ["2"], 8: ["12"],
    9: ["13"], 10: ["12"], 11: ["12"], 12: ["12"],
    13: ["10"], 14: ["10"], 15: ["10"], 16: ["10"], 17: ["10"], 18: ["10"], 19: ["10"],
    20: ["10"], 21: ["10"], 22: ["10"], 23: ["FR 53"], 24: ["FR 53"],
    25: ["11"], 26: ["11"], 27: ["11"], 28: ["16"], 29: ["11"], 30: ["11"], 31: ["11"],
    32: ["11"], 33: ["11"], 34: ["11"], 35: ["11"], 36: ["11"],
    37: ["14"], 38: ["14"], 39: ["14"], 40: ["14"], 41: ["14"], 42: ["14"], 43: ["14"],
    44: ["14"], 45: ["14"], 46: ["14"], 47: ["15"], 48: ["15"],
    49: ["15"], 50: ["16"], 51: ["22"], 52: ["23"], 53: ["23"], 54: ["25"], 55: ["25"],
    56: ["26"], 57: ["27"], 58: ["27"], 59: ["29"], 60: ["29-A"],
}

CSS = r"""
:root{--navy:#14284b;--blue:#2b5797;--ink:#1d2b40;--mut:#6b7a8f;--line:#d6deea;--amber:#fff4d6;--amberb:#e0b23a;--green:#e9f6ee;--greenb:#2e8b57;--red:#fdecea;--redb:#c0392b;--bg:#f6f8fc;--teal:#0e7490}
*{box-sizing:border-box} body{font-family:Inter,'DejaVu Sans',Arial,sans-serif;color:var(--ink);font-size:9.4pt;line-height:1.45;margin:0;background:#fff}
.wrap{max-width:920px;margin:0 auto;padding:18px}
h1{font-size:16pt;color:var(--navy);margin:0 0 6px} h2{font-size:12.5pt;color:#fff;background:var(--navy);padding:6px 10px;border-radius:4px;margin:16px 0 8px}
h3{margin:0;font-size:inherit} h4{margin:8px 0 3px;font-size:10pt;color:var(--navy)}
.sub{color:var(--mut);font-size:8.4pt;margin:4px 0 8px}
.lv{display:inline-block;font-size:7.5pt;font-weight:700;padding:1px 6px;border-radius:10px;margin-right:6px;color:#fff}
.lv.L1{background:#6b8e23}.lv.L2{background:#2b5797}.lv.L3{background:#8e3b8e}
table{border-collapse:collapse;width:100%;margin:5px 0} th,td{border:1px solid var(--line);padding:3.5px 6px;vertical-align:top;text-align:left}
th{background:#e8eef8;font-size:8.2pt} td{font-size:8.5pt}
.case{border:1px solid var(--line);border-radius:6px;margin:10px 0;padding:0 0 7px;background:#fff;break-inside:avoid}.ch{break-after:avoid}tr{break-inside:avoid}.wrong,.ans,.model{break-inside:avoid}
.ch{background:#eef3fa;padding:6px 10px;border-bottom:1px solid var(--line);border-radius:6px 6px 0 0;font-weight:700;color:var(--navy);display:flex;justify-content:space-between;gap:8px}
.ch .mk{font-weight:600;color:var(--mut);font-size:8pt;white-space:nowrap}
.bd{padding:5px 10px}
.facts{background:var(--bg);border-left:3px solid var(--blue);padding:5px 8px;margin:5px 0}
.lab{font-size:7.3pt;font-weight:800;letter-spacing:.6pt;text-transform:uppercase;color:var(--blue);margin:7px 0 2px}
ol.ask{margin:2px 0 4px 18px;padding:0}
.path{display:flex;flex-wrap:wrap;gap:4px;align-items:center;margin:4px 0}
.path span{background:#eef3fa;border:1px solid #c5d3ea;border-radius:12px;padding:1px 8px;font-size:7.8pt}
.path b{color:var(--blue)}
td.r{font-family:'DejaVu Sans Mono',monospace;font-size:7.3pt;color:var(--blue);width:15%} td.m{text-align:center;font-weight:700;width:30px}
td.s{font-weight:600;white-space:nowrap;color:#1f3b63;width:15%}
.wrong{background:var(--red);border-left:3px solid var(--redb);padding:4px 8px;margin:6px 0}
.wrong ul{margin:2px 0 0 16px;padding:0}
.ans{background:var(--green);border-left:3px solid var(--greenb);padding:5px 8px;margin:6px 0;font-weight:600}
.model{background:var(--amber);border-left:3px solid var(--amberb);padding:5px 8px;margin:6px 0;font-size:8.6pt}
.write{border:1px dashed #b9c6da;border-radius:4px;margin:6px 0;color:#7b8aa0;font-size:7.6pt;padding:5px 8px}
.chips{margin:5px 0 0;font-size:7.6pt;color:var(--mut)} .chips span{display:inline-block;background:#eef3fa;border:1px solid #c5d3ea;border-radius:9px;padding:0 6px;margin:1px 2px 1px 0;color:#1f3b63;font-family:'DejaVu Sans Mono',monospace}
details{margin:6px 10px} summary{cursor:pointer;font-weight:700;color:var(--blue);padding:5px 8px;background:#eef3fa;border-radius:4px;list-style:revert}
.legend{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:8px 0}.legend div{border:1px solid var(--line);border-radius:6px;padding:6px 8px;font-size:8.3pt}
.cover{background:var(--navy);color:#fff;padding:60px 36px 36px;border-radius:8px;display:flex;flex-direction:column;justify-content:space-between}
.cover h1{color:#fff;font-size:25pt;line-height:1.15;margin:8px 0 12px}.cover .k{color:#f6b385;font-size:8.5pt;letter-spacing:1.6pt;font-weight:700}
.cover .law{font-size:11pt;color:#cfd9ea}.stats{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:20px 0}.stats div{background:rgba(255,255,255,.09);border-radius:6px;padding:10px 8px;text-align:center}
.stats b{display:block;font-size:17pt;color:#fff}.stats span{font-size:7.6pt;color:#cfd9ea}
.cover table td{border-color:rgba(255,255,255,.18);color:#e7edf7;font-size:8.4pt}.cover table td:first-child{width:118px;color:#f6b385;font-weight:700}
.disc{font-size:7.8pt;color:#cfd9ea;border-top:1px solid rgba(255,255,255,.18);padding-top:10px;margin-top:18px}
.howgrid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:8px 0}.howbox{border:1px solid var(--line);border-radius:6px;padding:8px 10px;font-size:8.4pt}
.howbox .t{font-weight:800;color:var(--navy);font-size:8.6pt;margin-bottom:4px;text-transform:uppercase;letter-spacing:.5pt}
.howbox ol,.howbox ul{margin:2px 0 2px 16px;padding:0}
nav.toc{border:1px solid var(--line);border-radius:6px;padding:8px 12px;font-size:8.6pt}
nav.toc a{color:var(--blue);text-decoration:none} nav.toc ul{margin:2px 0 6px 16px;padding:0} nav.toc li{margin:1px 0}
nav.toc .grp{font-weight:800;color:var(--navy);text-transform:uppercase;font-size:7.8pt;letter-spacing:.5pt;margin-top:6px}
.flt{position:sticky;top:0;background:#fff;border-bottom:1px solid var(--line);padding:7px 0;z-index:5;display:flex;gap:6px;align-items:center;flex-wrap:wrap;font-size:8.4pt}
.flt button,.flt input{font:inherit;padding:3px 9px;border:1px solid var(--line);background:#fff;border-radius:14px;cursor:pointer}
.flt button.on{background:var(--navy);color:#fff;border-color:var(--navy)}
.flt input{cursor:text;min-width:200px;border-radius:6px}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.qf td.a{width:34%}
.reveal{font:inherit;font-size:7.3pt;padding:1px 7px;border:1px solid #c5d3ea;background:#eef3fa;color:var(--blue);border-radius:9px;cursor:pointer;margin-right:6px}
.reveal[aria-expanded="true"]{background:var(--blue);color:#fff;border-color:var(--blue)}
.vf{color:#b8860b;font-weight:800}
.st{display:inline-block;font-size:7.1pt;font-weight:800;padding:0 6px;border-radius:9px;border:1px solid;white-space:nowrap}
.st.in{color:#1e6b46;border-color:#9fd3b8;background:#eaf7f0}
.st.concept{color:#1f4f8a;border-color:#b9cdea;background:#eef3fa}
.st.spent{color:#6b5a2a;border-color:#e2d3a0;background:#fdf8e6}
.st.superseded{color:#8d2f24;border-color:#eab8b0;background:#fdeeeb}
table.idx td{font-size:8pt} table.idx td:first-child{width:16%;font-weight:700;color:#1f3b63}
table.idx a{color:var(--blue);text-decoration:none}
.pb{page-break-before:always}
.top-index{position:fixed;right:14px;bottom:14px;background:var(--navy);color:#fff;text-decoration:none;padding:7px 11px;border-radius:18px;font-size:8pt;z-index:9}
a.back{font-size:7.4pt;color:var(--mut);text-decoration:none;display:inline-block;margin:2px 0}
h2#sources + div + ul{font-size:8.8pt}
@media print{
  .noprint{display:none!important} .wrap{max-width:none;padding:0}
  body{font-size:9pt} .case{border-color:#bbb} details{margin:4px 0} summary{display:none}
  details>div{display:block!important} .pb{page-break-before:always} a{color:inherit;text-decoration:none}
  .cover{background:#14284b!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
@media (max-width:720px){
  .legend,.howgrid{grid-template-columns:1fr} .stats{grid-template-columns:repeat(2,1fr)}
  .cover{padding:28px 18px} .cover h1{font-size:19pt} .ch{flex-direction:column}
  .flt input{min-width:0;width:100%}
}
"""

JS = r"""
let filter='all';
function apply(){
  const q=(document.getElementById('q').value||'').trim().toLowerCase();
  document.querySelectorAll('.case').forEach(c=>{
    const okLv=(filter==='all'||c.dataset.lv===filter);
    const okQ=(!q||(c.dataset.s||'').includes(q));
    c.hidden=!(okLv&&okQ);
  });
  let total=0;
  document.querySelectorAll('.qf').forEach(t=>{
    let count=0;
    t.querySelectorAll('tr[id]').forEach(r=>{
      const yes=(filter==='all'||filter==='L1')&&(!q||r.textContent.toLowerCase().includes(q));
      r.hidden=!yes; if(yes)count++;
    });
    t.hidden=!count;
    const h=t.previousElementSibling;
    if(h&&h.tagName==='H4')h.hidden=!count;
    total+=count;
  });
  const p1=document.getElementById('part-1'); if(p1)p1.hidden=!total;
  ['L2','L3'].forEach((lv,i)=>{
    const p=document.getElementById('part-'+(i+2));
    if(!p)return;
    p.hidden=!Array.from(document.querySelectorAll('.case[data-lv="'+lv+'"]')).some(c=>!c.hidden);
  });
}
document.querySelectorAll('.flt button[data-f]').forEach(b=>b.addEventListener('click',()=>{
  filter=b.dataset.f;
  document.querySelectorAll('.flt button[data-f]').forEach(x=>{
    const on=x===b; x.classList.toggle('on',on); x.setAttribute('aria-pressed',String(on));
  });
  apply();
}));
const qBox=document.getElementById('q');
if(qBox)qBox.addEventListener('input',apply);
const ex=document.getElementById('ex');
if(ex)ex.addEventListener('click',()=>document.querySelectorAll('.case:not([hidden]) details').forEach(d=>d.open=true));
const co=document.getElementById('co');
if(co)co.addEventListener('click',()=>document.querySelectorAll('.case details').forEach(d=>d.open=false));
document.querySelectorAll('.reveal').forEach(b=>b.addEventListener('click',()=>{
  const row=b.closest('tr');
  const show=b.getAttribute('aria-expanded')!=='true';
  b.setAttribute('aria-expanded',String(show));
  b.textContent=show?'Hide':'Show';
  row.querySelectorAll('.answer-text').forEach(s=>s.hidden=!show);
}));
document.addEventListener('click',e=>{
  const a=e.target.closest('a[href^="#"]'); if(!a)return;
  const el=document.getElementById(a.getAttribute('href').slice(1));
  if(el&&(el.hidden||el.closest('[hidden]'))){
    const box=document.getElementById('q'); if(box)box.value='';
    const all=document.querySelector('.flt button[data-f="all"]'); if(all)all.click();
  }
});
let printState=[];
window.addEventListener('beforeprint',()=>{
  printState=Array.from(document.querySelectorAll('.case details'),d=>[d,d.open]);
  printState.forEach(([d])=>d.open=true);
});
window.addEventListener('afterprint',()=>{
  printState.forEach(([d,open])=>d.open=open); printState=[];
});
"""

FORBIDDEN = ("javascript:", "onerror=", "onload=", "<iframe", "src=")


def esc(s: str) -> str:
    return html.escape(str(s), quote=False)


def marks_of(case) -> int:
    return sum(int(r[3]) for r in case["steps"] if isinstance(r[3], int))


def rule_keys(case):
    out = set()
    for tag in case.get("tags", []):
        label = tag[0]
        base = label.split("(")[0].strip()
        out.add(base)
    return out


def search_blob(case) -> str:
    parts = [case["id"], case["title"], case["facts"], " ".join(t[0] for t in case.get("tags", []))]
    parts += case.get("questions", [])
    return re.sub(r"\s+", " ", " ".join(parts)).lower()


def render_l1():
    out = []
    for i, st in enumerate(L1_SETS, start=1):
        out.append(f'<h4 id="l1-set-{i}"><span class="lv L1">L1</span> Set {i} — {esc(st["title"])} ({esc(st["range"])})</h4>')
        out.append('<table class="qf"><tr><th>#</th><th>Question</th><th>Answer</th><th>Rule · Trap</th></tr>')
        for it in st["items"]:
            n = it["n"]
            out.append(
                f'<tr id="l1-{n}"><td>{n}</td><td>{esc(it["q"])}</td>'
                f'<td class="a"><button aria-expanded="false" aria-label="Reveal answer and rule for L1-{n:02d}" class="reveal" type="button">Show</button>'
                f'<span class="answer-text" hidden=""><b>{esc(it["a"])}</b></span></td>'
                f'<td class="a"><span class="answer-text" hidden=""><span style="font-family:monospace">{esc(it["r"])}</span> · {esc(it["t"])}</span></td></tr>'
            )
        out.append('</table>')
    return "\n".join(out)


def render_case(case):
    cid = case["id"]
    marks = marks_of(case)
    lv = "L3" if cid.startswith("L3") else "L2"
    out = [f'<div class="case" data-lv="{lv}" data-s="{esc(search_blob(case))}" id="q-{cid}">']
    out.append(f'<h3 class="ch"><span><span class="lv {lv}">{lv}</span>{cid} · {esc(case["title"])}</span><span class="mk">{marks} marks</span></h3>')
    out.append('<div class="bd">')
    out.append(f'<div class="facts"><b>Facts.</b> {case["facts"]}</div>')
    if case.get("record"):
        out.append('<div class="lab">Record / key dates</div><table><tr><th>Item</th><th>Date / period</th><th>Note</th></tr>')
        for row in case["record"]:
            cells = "".join(f"<td>{c}</td>" for c in row)
            out.append(f"<tr>{cells}</tr>")
        out.append("</table>")
    out.append('<div class="lab">Questions</div><ol class="ask">')
    for q in case["questions"]:
        out.append(f"<li>{q}</li>")
    out.append("</ol></div>")
    out.append("<details><summary>Show solution</summary><div class=\"bd\">")
    out.append(f'<a class="back" href="#q-{cid}">↑ Back to question</a>')
    if case.get("path"):
        out.append('<div class="lab">Decision path</div><div class="path">')
        chips = []
        for i, p in enumerate(case["path"]):
            if i:
                chips.append("<b>→</b>")
            chips.append(f"<span>{p}</span>")
        out.append(" ".join(chips))
        out.append("</div>")
    out.append('<div class="lab">Solution — step by step (marks as an examiner would award)</div>')
    out.append("<table><tr><th>Step</th><th>Working</th><th>Rule</th><th>Marks</th></tr>")
    for step, working, rule, mk in case["steps"]:
        m = str(mk) if isinstance(mk, int) else "—"
        out.append(f'<tr><td class="s">{step}</td><td>{working}</td><td class="r">{rule}</td><td class="m">{m}</td></tr>')
    out.append(f'<tr><td></td><td style="text-align:right;font-weight:700">Total</td><td></td><td class="m">{marks}</td></tr></table>')
    if case.get("wrong"):
        out.append('<div class="wrong"><b>Common wrong answers</b><ul>')
        for w in case["wrong"]:
            out.append(f"<li>{w}</li>")
        out.append("</ul></div>")
    out.append(f'<div class="ans">Answer: {case["answer"]}</div>')
    if case.get("model"):
        out.append(f'<div class="model"><b>Model answer (exam style).</b> {case["model"]}</div>')
    if case.get("tags"):
        out.append('<div class="chips">Rule tags: ')
        for label, title in case["tags"]:
            out.append(f'<span title="{esc(title)}">{esc(label)}</span>')
        out.append("</div>")
    out.append(f'<a class="back" href="#q-{cid}">↑ Back to question</a>')
    out.append("</div></details></div>")
    return "\n".join(out)


def render_toc():
    out = ['<nav class="toc" aria-label="Table of contents" id="contents">']
    out.append('<div class="grp">Front matter</div><ul>'
               '<li><a href="#how-to">How to use this book</a></li>'
               '<li><a href="#scope-register">Scope register — what is in, what is out, and why</a></li>'
               '<li><a href="#obsolete">Obsolete register — what is no longer the law</a></li>'
               '<li><a href="#authority">Competence matrix</a></li></ul>')
    out.append('<div class="grp">Part 1 — L1 concept checks</div><ul>')
    for i, st in enumerate(L1_SETS, start=1):
        out.append(f'<li><a href="#l1-set-{i}">Set {i} — {esc(st["title"])} ({esc(st["range"])})</a></li>')
    out.append("</ul>")
    out.append('<div class="grp">Part 2 — L2 standard cases</div><ul>')
    for c in L2:
        out.append(f'<li><a href="#q-{c["id"]}">{c["id"]} — {esc(c["title"])}</a> <span class="sub">{marks_of(c)} marks</span></li>')
    out.append("</ul>")
    out.append('<div class="grp">Part 3 — L3 integrated cases</div><ul>')
    for c in L3:
        out.append(f'<li><a href="#q-{c["id"]}">{c["id"]} — {esc(c["title"])}</a> <span class="sub">{marks_of(c)} marks</span></li>')
    out.append("</ul>")
    out.append('<div class="grp">Indices</div><ul>'
               '<li><a href="#rule-index">Rule-to-case index</a></li>'
               '<li><a href="#clock-index">Clock-to-case index</a></li>'
               '<li><a href="#caselaw-index">Case-law index</a></li>'
               '<li><a href="#sources">Sources and notes</a></li></ul>')
    out.append("</nav>")
    return "\n".join(out)


def render_scope():
    out = ['<h2 id="scope-register">Scope register — what is in, what is out, and why</h2>']
    out.append('<p class="sub">Fixed before drafting. <b>IN</b> — full treatment. <b>IN (concept only)</b> — cited, not expanded. '
               '<b>OUT (omitted)</b> — struck out of the rule book. <b>OUT (transitional)</b> — spent on its own terms. '
               '<b>OUT (no case value)</b> — live but never examinable. Exclusion from this book is not a finding of obsolescence; only the first two OUT classes are law that has gone. '
               'Nothing in the book relies on a provision marked OUT.</p>')
    out.append('<table class="idx"><tr><th>Rule / instrument</th><th>Subject</th><th>Status</th><th>Why</th></tr>')
    for rule, subject, status, why in meta.SCOPE:
        cls = "in" if status == "IN" else ("concept" if status.startswith("IN") else ("spent" if ("omitted" in status or "transitional" in status) else "superseded"))
        out.append(f'<tr><td>{esc(rule)}</td><td>{esc(subject)}</td><td><span class="st {cls}">{esc(status)}</span></td><td>{esc(why)}</td></tr>')
    out.append("</table>")
    return "\n".join(out)


def render_obsolete():
    out = ['<h2 id="obsolete">Obsolete register — what is no longer the law</h2>']
    out.append('<p class="sub">Every entry below is still taught somewhere. None of it is taught here as current. Where a case meets one, it does so as a '
               'wrong answer marked <span class="vf">⊘</span>, with the amending instrument named.</p>')
    out.append('<table class="idx"><tr><th>Taught as current</th><th>Current position</th><th>Authority for the change</th></tr>')
    for taught, current, auth in meta.OBSOLETE:
        out.append(f'<tr><td>{taught}</td><td>{current}</td><td>{auth}</td></tr>')
    out.append("</table>")
    return "\n".join(out)


def render_authority():
    out = ['<h2 id="authority">Competence matrix</h2>']
    out.append('<p class="sub">Read the rule first, then the Schedule, then any general or special order. The last column is the error that most often reaches '
               'the Tribunal.</p>')
    out.append('<table class="idx"><tr><th>Order to be made</th><th>Competent authority</th><th>Test</th><th>Common error</th></tr>')
    for a, b, c, d in meta.AUTHORITY:
        out.append(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>")
    out.append("</table>")
    return "\n".join(out)


def render_rule_index():
    out = ['<h2 class="pb" id="rule-index">Rule-to-case index</h2>']
    out.append('<p class="sub">Every rule in the scope register, with the L1 checks and the cases that turn on it. Links jump to the item.</p>')
    out.append('<table class="idx"><tr><th>Rule</th><th>Where it is tested (L1 check · L2/L3 case)</th></tr>')
    # which cases cite each rule
    for rule, subject, status, _why in meta.SCOPE:
        if status.startswith("OUT"):
            continue
        hits = []
        for n, rules in sorted(L1_RULES.items()):
            if rule in rules:
                hits.append(f'<a href="#l1-{n}">L1-{n:02d}</a>')
        for c in CASES:
            if rule in rule_keys(c):
                hits.append(f'<a href="#q-{c["id"]}">{c["id"]}</a>')
        if not hits:
            continue
        out.append(f'<tr><td>{esc(rule)}</td><td>{", ".join(hits)}</td></tr>')
    out.append("</table>")
    covered = {r for r, *_ in meta.SCOPE if not r}
    unused = [r for r, _s, st, _w in meta.SCOPE if not st.startswith("OUT")
              and not any(r in rules for rules in L1_RULES.values())
              and not any(r in rule_keys(c) for c in CASES)]
    if unused:
        out.append('<p class="sub">Rules in scope with no dedicated item (covered by the authority matrix and the L1 trap column): '
                   + ", ".join(esc(u) for u in unused) + ".</p>")
    return "\n".join(out)


def render_clock_index():
    out = ['<h2 id="clock-index">Clock-to-case index</h2>']
    out.append('<p class="sub">The clocks an officer is expected to know to the day, with the provision and the cases that compute them.</p>')
    out.append('<table class="idx"><tr><th>Clock</th><th>Limit</th><th>Provision</th><th>Cases</th></tr>')
    for clock, limit, prov, ids in meta.CLOCKS:
        links = ", ".join(f'<a href="#q-{i}">{i}</a>' for i in ids)
        out.append(f"<tr><td>{clock}</td><td>{limit}</td><td>{prov}</td><td>{links}</td></tr>")
    out.append("</table>")
    return "\n".join(out)


def render_caselaw():
    out = ['<h2 id="caselaw-index">Case-law index</h2>']
    out.append('<p class="sub">The proposition at the width it is decided, with the limit stated. Nothing in this book quotes a judgment for atmosphere.</p>')
    out.append('<table class="idx"><tr><th>Proposition</th><th>Authority</th><th>Width and limit</th></tr>')
    for prop, auth, width in meta.CASELAW:
        out.append(f"<tr><td>{prop}</td><td>{auth}</td><td>{width}</td></tr>")
    out.append("</table>")
    return "\n".join(out)


def render_sources():
    out = ['<h2 id="sources">Sources and notes</h2>', '<div style="height:1px"></div>', '<ul class="sub" style="font-size:8.8pt;color:#1d2b40">']
    for text, url in meta.SOURCES:
        out.append(f'<li>{text} — <a href="{url}">{url}</a></li>')
    for note in meta.NOTES:
        out.append(f"<li>{note}</li>")
    out.append("</ul>")
    return "\n".join(out)


def render():
    l1_count = sum(len(s["items"]) for s in L1_SETS)
    model_count = sum(1 for c in CASES if c.get("model"))
    rules_anchored = len([r for r, _s, st, _w in meta.SCOPE if not st.startswith("OUT")])
    stats = [(l1_count, "L1 concept checks"), (len(L2), "L2 standard cases"), (len(L3), "L3 integrated cases"),
             (model_count, "model answers"), (rules_anchored, "rules and provisions anchored")]

    parts = ['<!DOCTYPE html>', '<html lang="en"><head><meta charset="utf-8"/>',
             '<meta content="width=device-width,initial-scale=1" name="viewport"/>',
             f'<title>{meta.TITLE} — Case Studies L1 · L2 · L3 (AAO)</title>',
             f'<style>{CSS}</style></head><body><div class="wrap">']

    # cover
    parts.append('<section class="cover"><div>')
    parts.append(f'<div class="k">GOVERNMENT RULES · CASE-STUDY BOOK · {meta.VERSION} · NON-OBSOLETE CONTENT</div>')
    parts.append(f'<h1>{meta.TITLE}<br/>Case Studies at Three Levels</h1>')
    parts.append(f'<div class="law">{meta.PITCH}</div>')
    parts.append('<div class="stats">')
    for n, label in stats:
        parts.append(f"<div><b>{n}</b><span>{label}</span></div>")
    parts.append("</div>")
    parts.append("<table>")
    for label, text in meta.COVERAGE:
        parts.append(f"<tr><td>{label}</td><td>{text}</td></tr>")
    parts.append("</table></div>")
    parts.append('<div class="disc"><b>Disclaimer.</b> Exam-study aid, not legal advice. Rely on the Gazette text and the current DoPT/CVC/CAG instructions '
                 'for official work. Facts, names, offices and figures are constructed for teaching; pay computations use 7th CPC matrix values and '
                 'illustrative DA/DR flagged ⚑ where the formal order was awaited on the law date.</div></section>')

    # how to use
    parts.append('<h2 class="pb" id="how-to">How to use this book</h2>')
    parts.append('<div class="legend">')
    for lv_, title, text in meta.LEGEND:
        parts.append(f'<div><span class="lv {lv_}">{lv_}</span><b>{title}</b><br/>{text}</div>')
    parts.append("</div>")
    parts.append('<div class="howgrid">')
    parts.append('<div class="howbox"><div class="t">The six-step method</div><ol>')
    for step, text in meta.METHOD:
        parts.append(f"<li><b>{step}</b> — {text}</li>")
    parts.append("</ol></div>")
    parts.append('<div class="howbox"><div class="t">Numbers to keep ready</div><ul>')
    for label, text in meta.NUMBERS:
        parts.append(f"<li><b>{label}.</b> {text}</li>")
    parts.append("</ul></div>")
    parts.append('<div class="howbox"><div class="t">Flags</div><ul>')
    parts.append("<li><b>⚑</b> a rate or order still awaited — state the date of the last order you have.</li>")
    parts.append("<li><b>⚠</b> a genuinely unsettled point — state both readings.</li>")
    parts.append("<li><b>⊘</b> a superseded provision — shown only to be distinguished, never taught as current.</li>")
    parts.append("<li><b>Marks.</b> The marks in a case header are the sum of the marks in its step table. A step without a rule reference is not a marking point.</li>")
    parts.append("</ul></div>")
    parts.append('<div class="howbox"><div class="t">Reading the layout</div><ul>'
                 "<li><b>Part 1</b> L1 checks: use the row button to reveal the answer and the rule together.</li>"
                 "<li><b>Part 2</b> L2 cases: attempt on paper, then open the solution.</li>"
                 "<li><b>Part 3</b> L3 cases: full file, every computation, model answer in exam register.</li>"
                 "<li><b>Indices</b> rule, clock and case law — each links back to the item that tests it.</li>"
                 "<li><b>Printing</b> opens every solution automatically and breaks before each part.</li></ul></div>")
    parts.append("</div>")

    parts.append(render_toc())
    parts.append(render_scope())
    parts.append(render_obsolete())
    parts.append(render_authority())

    parts.append(f'<h2 class="pb" id="part-1">Part 1 — L1 concept checks ({l1_count})</h2>')
    parts.append('<p class="sub">Use Show to reveal the answer and rule together. Aim for two minutes a set.</p>')
    parts.append(render_l1())

    parts.append(f'<h2 class="pb" id="part-2">Part 2 — L2 standard cases ({len(L2)})</h2>')
    for c in L2:
        parts.append(render_case(c))

    parts.append(f'<h2 class="pb" id="part-3">Part 3 — L3 integrated cases ({len(L3)})</h2>')
    for c in L3:
        parts.append(render_case(c))

    parts.append(render_rule_index())
    parts.append(render_clock_index())
    parts.append(render_caselaw())
    parts.append(render_sources())

    parts.append('<a aria-label="Go to table of contents" class="top-index noprint" href="#contents">Top / Index</a>')
    parts.append(f'<script>{JS}</script></div></body></html>')
    return "\n".join(parts)


def audit(doc: str) -> list[str]:
    errors = []
    ids = re.findall(r'\bid="([^"]+)"', doc)
    dupes = {i for i in ids if ids.count(i) > 1}
    for d in sorted(dupes):
        errors.append(f"duplicate id: {d}")
    for href in set(re.findall(r'href="#([^"]+)"', doc)):
        if href not in ids and href != "":
            errors.append(f"unresolved anchor: #{href}")
    for pat in FORBIDDEN:
        if pat in doc:
            errors.append(f"forbidden markup: {pat}")
    if doc.count("<script") != 1:
        errors.append(f"expected exactly one inline script, found {doc.count('<script')}")
    for c in CASES:
        if marks_of(c) <= 0:
            errors.append(f"{c['id']}: no marks in step table")
        if not c.get("facts"):
            errors.append(f"{c['id']}: empty facts")
        if len(c.get("questions", [])) < 3:
            errors.append(f"{c['id']}: fewer than three questions")
        for row in c["steps"]:
            if len(row) != 4 or not str(row[2]).strip():
                errors.append(f"{c['id']}: step row without a rule reference")
        if not c.get("answer"):
            errors.append(f"{c['id']}: empty answer")
    for clock, _l, _p, ids_ in meta.CLOCKS:
        for i in ids_:
            if i not in {c["id"] for c in CASES}:
                errors.append(f"clock index points to missing case: {i}")
    ids_case = [c["id"] for c in CASES]
    if len(ids_case) != len(set(ids_case)):
        errors.append("duplicate case id")
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=f"CCS_CCA_Rules_1965_Case_Studies_{meta.BUILD_STAMP}.html")
    ap.add_argument("--audit", action="store_true", help="validate only, do not write")
    args = ap.parse_args()

    doc = render().replace("↯", "⚠").replace("⅀", "⊘")
    errors = audit(doc)
    if errors:
        print("AUDIT FAILED", file=sys.stderr)
        for e in errors:
            print("  -", e, file=sys.stderr)
        return 1
    l1_count = sum(len(s["items"]) for s in L1_SETS)
    print(f"audit ok: {l1_count} L1 · {len(L2)} L2 · {len(L3)} L3 · "
          f"{sum(1 for c in CASES if c.get('model'))} model answers · {len(doc):,} bytes")
    if args.audit:
        return 0
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out = args.out if os.path.isabs(args.out) else os.path.join(root, args.out)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"written: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
