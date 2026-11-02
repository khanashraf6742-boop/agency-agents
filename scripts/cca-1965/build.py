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

CSS = r""":root{
  --navy:#0f2244;--navy-2:#1b3a6b;--blue:#2b5797;--blue-ink:#1d4ed8;
  --ink:#1a2433;--ink-2:#41506a;--mut:#6b7a8f;--line:#e3e8f2;--line-2:#cfd8e8;
  --paper:#ffffff;--page:#f5f7fc;--bg:#f2f6fd;
  --gold:#c08a2e;--gold-2:#f0c987;
  --green:#e9f6ee;--greenb:#2e8b57;--red:#fdecea;--redb:#c0392b;
  --amber:#fff6dd;--amberb:#d9a520;
  --l1:#4d7c0f;--l2:#1d4ed8;--l3:#7e22ce;
  --radius:14px;--radius-s:10px;
  --shadow:0 1px 2px rgba(15,34,68,.05),0 8px 24px -18px rgba(15,34,68,.35);
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"DejaVu Sans Mono",monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  font-family:var(--sans);color:var(--ink);font-size:15px;line-height:1.62;margin:0;
  background:
    radial-gradient(1200px 600px at 15% -10%,#e8eefb 0%,transparent 60%),
    radial-gradient(900px 500px at 100% 0%,#eef4fb 0%,transparent 55%),
    var(--page);
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;
}
.wrap{max-width:1040px;margin:0 auto;padding:26px 22px 80px}

/* ---------- progress + chrome ---------- */
.prog{position:fixed;top:0;left:0;height:3px;width:0;z-index:60;
  background:linear-gradient(90deg,var(--navy),var(--blue-ink) 55%,var(--gold));transition:width .1s linear}

/* ---------- type ---------- */
h1{font-size:clamp(1.9rem,3.6vw,2.6rem);line-height:1.12;letter-spacing:-.02em;color:var(--navy);margin:0 0 10px}
h2{font-size:clamp(1.12rem,1.9vw,1.34rem);letter-spacing:-.01em;color:var(--navy);
  margin:34px 0 12px;padding:0 0 8px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:11px}
h2::before{content:"";flex:0 0 auto;width:6px;height:1.05em;border-radius:3px;
  background:linear-gradient(180deg,var(--navy),var(--blue-ink))}
h3{margin:0;font-size:1rem}
h3.set{display:flex;align-items:center;gap:9px;margin:26px 0 8px;font-size:1.02rem;color:var(--navy);font-weight:700}
p{margin:8px 0}
a{color:var(--blue-ink);text-decoration:none}
a:hover{text-decoration:underline}
.sub{color:var(--mut);font-size:.84rem;margin:6px 0 10px}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
:focus-visible{outline:2px solid var(--blue-ink);outline-offset:2px;border-radius:4px}

/* ---------- level pills ---------- */
.lv{display:inline-flex;align-items:center;justify-content:center;min-width:30px;
  font-size:.68rem;font-weight:800;letter-spacing:.06em;padding:3px 8px;border-radius:999px;color:#fff;
  box-shadow:0 1px 2px rgba(15,34,68,.18)}
.lv.L1{background:linear-gradient(135deg,#5d9414,var(--l1))}
.lv.L2{background:linear-gradient(135deg,#3b82f6,var(--l2))}
.lv.L3{background:linear-gradient(135deg,#a855f7,var(--l3))}

/* ---------- tables ---------- */
table{border-collapse:separate;border-spacing:0;width:100%;margin:10px 0;font-size:.88rem;
  border:1px solid var(--line);border-radius:var(--radius-s);overflow:hidden;background:var(--paper)}
th,td{padding:8px 11px;vertical-align:top;text-align:left;border-bottom:1px solid var(--line)}
tr:last-child>th,tr:last-child>td{border-bottom:0}
th{background:#eff3fa;color:#33415c;font-size:.74rem;font-weight:700;letter-spacing:.055em;text-transform:uppercase}
tbody tr:nth-child(even)>td{background:#fafcff}
td{color:var(--ink-2)}
td.r{font-family:var(--mono);font-size:.78rem;color:var(--blue-ink);white-space:nowrap;width:15%}
td.m{text-align:center;font-weight:800;color:var(--navy);width:34px;font-variant-numeric:tabular-nums}
td.s{font-weight:700;color:#1f3b63;width:15%}

/* ---------- case card ---------- */
.case{border:1px solid var(--line);border-radius:var(--radius);margin:16px 0;background:var(--paper);
  box-shadow:var(--shadow);overflow:hidden;break-inside:avoid;transition:box-shadow .18s ease,transform .18s ease}
.case:hover{box-shadow:0 2px 4px rgba(15,34,68,.06),0 18px 40px -26px rgba(15,34,68,.55)}
.case[data-lv="L2"]{border-top:3px solid var(--l2)}
.case[data-lv="L3"]{border-top:3px solid var(--l3)}
.ch{display:flex;justify-content:space-between;align-items:flex-start;gap:14px;padding:13px 18px;
  font-weight:700;color:var(--navy);border-bottom:1px solid var(--line);break-after:avoid;
  background:linear-gradient(180deg,#f7faff,#eef3fb)}
.case[data-lv="L3"] .ch{background:linear-gradient(180deg,#fbf7ff,#f3ecfd)}
.ch>span:first-child{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.ch .mk{flex:0 0 auto;font-size:.74rem;font-weight:800;letter-spacing:.03em;color:var(--navy);
  background:#fff;border:1px solid var(--line-2);border-radius:999px;padding:3px 10px;white-space:nowrap}
.bd{padding:14px 18px 16px}

/* ---------- facts / labels ---------- */
.facts{background:linear-gradient(180deg,#f4f8ff,#eef4fd);border:1px solid #dde7f7;border-left:4px solid var(--blue);
  border-radius:var(--radius-s);padding:11px 14px;margin:10px 0 12px;color:var(--ink-2)}
.facts b{color:var(--navy)}
.lab{display:flex;align-items:center;gap:8px;font-size:.68rem;font-weight:800;letter-spacing:.12em;
  text-transform:uppercase;color:#5d6f8c;margin:16px 0 6px}
.lab::before{content:"";width:14px;height:3px;border-radius:2px;background:var(--gold);flex:0 0 auto}
ol.ask{margin:6px 0 4px;padding-left:24px}
ol.ask li{margin:3px 0}
ol.ask li::marker{color:var(--blue-ink);font-weight:700}

/* ---------- decision path ---------- */
.path{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:6px 0}
.path span{background:#fff;border:1px solid var(--line-2);border-radius:999px;padding:3px 11px;
  font-size:.79rem;color:#2b3c57}
.path b{color:var(--gold);font-size:.9rem}

/* ---------- answer blocks ---------- */
.wrong,.ans,.model{border-radius:var(--radius-s);padding:11px 14px;margin:10px 0;break-inside:avoid;border:1px solid transparent}
.wrong{background:var(--red);border-color:#f6d5cf;border-left:4px solid var(--redb)}
.wrong b{color:#8d2f24;font-size:.8rem;letter-spacing:.06em;text-transform:uppercase}
.wrong ul{margin:6px 0 0;padding-left:20px}
.wrong li{margin:4px 0;color:#5d3029}
.ans{background:var(--green);border-color:#cfe9d9;border-left:4px solid var(--greenb);font-weight:600;color:#154d31}
.model{background:var(--amber);border-color:#f2e0b0;border-left:4px solid var(--amberb);color:#4a3a12}
.model b{color:#7a5a0d}
.write{border:1px dashed var(--line-2);border-radius:var(--radius-s);color:#8494ab;font-size:.84rem;padding:10px 12px;margin:10px 0}

/* ---------- tags ---------- */
.chips{margin:12px 0 0;font-size:.8rem;color:var(--mut);display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.chips span{background:#fff;border:1px solid var(--line-2);border-radius:999px;padding:2px 9px;
  color:#26405f;font-family:var(--mono);font-size:.76rem}

/* ---------- solution disclosure ---------- */
details{margin:14px 0 4px;border-radius:var(--radius-s)}
summary{cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:9px;
  font-weight:700;font-size:.86rem;color:var(--blue-ink);background:#eef4ff;
  border:1px solid #d7e3fb;border-radius:999px;padding:7px 15px;transition:background .15s ease,border-color .15s ease}
summary::-webkit-details-marker{display:none}
summary::before{content:"";width:0;height:0;border-left:6px solid currentColor;
  border-top:4.5px solid transparent;border-bottom:4.5px solid transparent;transition:transform .18s ease}
summary:hover{background:#e2ecff;border-color:#bcd2f7}
details[open]>summary{background:var(--navy);border-color:var(--navy);color:#fff}
details[open]>summary::before{transform:rotate(90deg)}
details>div.bd{padding:6px 0 0}
a.back{display:inline-block;font-size:.76rem;color:var(--mut);margin:10px 0 0;padding:2px 0}
a.back:hover{color:var(--blue-ink)}

/* ---------- toolbar ---------- */
.flt{position:sticky;top:3px;z-index:20;display:flex;flex-wrap:wrap;gap:7px;align-items:center;
  margin:0 -22px 18px;padding:10px 22px;font-size:.86rem;
  background:rgba(255,255,255,.96);backdrop-filter:blur(12px) saturate(1.4);
  -webkit-backdrop-filter:blur(12px) saturate(1.4);border-bottom:1px solid var(--line);
  transition:box-shadow .2s ease}
.flt.stuck{box-shadow:0 6px 20px -14px rgba(15,34,68,.6)}
.flt button{font:inherit;font-weight:600;color:#33415c;padding:6px 13px;border:1px solid var(--line-2);
  background:#fff;border-radius:999px;cursor:pointer;transition:all .15s ease}
.flt button:hover{border-color:#9fb6dc;background:#f4f8ff;color:var(--navy)}
.flt button.on{background:linear-gradient(180deg,var(--navy-2),var(--navy));color:#fff;border-color:var(--navy);
  box-shadow:0 2px 8px -3px rgba(15,34,68,.7)}
.flt input{font:inherit;padding:6px 12px 6px 32px;border:1px solid var(--line-2);background:#fff;border-radius:999px;
  min-width:230px;color:var(--ink);
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%236b7a8f' stroke-width='2.4' stroke-linecap='round'><circle cx='11' cy='11' r='7'/><path d='M20 20l-4.2-4.2'/></svg>");
  background-repeat:no-repeat;background-position:11px 50%}
.flt input:focus{outline:none;border-color:var(--blue-ink);box-shadow:0 0 0 3px rgba(29,78,216,.14)}
.flt .hint{font-size:.76rem;color:#7c8aa0;margin-left:auto}

/* ---------- cover ---------- */
.cover{position:relative;overflow:hidden;color:#fff;border-radius:20px;padding:clamp(30px,5vw,54px);
  background:
    radial-gradient(900px 380px at 88% -12%,rgba(89,132,209,.55),transparent 62%),
    radial-gradient(600px 300px at -8% 110%,rgba(192,138,46,.28),transparent 60%),
    linear-gradient(160deg,#12294f 0%,#0f2244 45%,#0b1a35 100%);
  box-shadow:0 24px 60px -34px rgba(9,21,44,.9)}
.cover::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.32;
  background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);
  background-size:34px 34px;
  -webkit-mask-image:radial-gradient(70% 60% at 78% 10%,#000,transparent 78%);
          mask-image:radial-gradient(70% 60% at 78% 10%,#000,transparent 78%)}
.cover>*{position:relative;z-index:1}
.cover .k{display:inline-block;color:var(--gold-2);font-size:.7rem;letter-spacing:.22em;font-weight:800;
  text-transform:uppercase;border:1px solid rgba(240,201,135,.42);border-radius:999px;padding:5px 13px;
  background:rgba(240,201,135,.09)}
.cover h1{color:#fff;font-size:clamp(1.85rem,4.2vw,2.9rem);margin:16px 0 14px;text-shadow:0 2px 24px rgba(0,0,0,.25)}
.cover .law{font-size:1rem;color:#c9d7ee;max-width:62ch;line-height:1.65}
.cover .law b{color:#fff;font-weight:700}
.stats{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:24px 0 20px}
.stats div{background:rgba(255,255,255,.075);border:1px solid rgba(255,255,255,.13);border-radius:12px;
  padding:14px 10px;text-align:center;backdrop-filter:blur(4px)}
.stats b{display:block;font-size:1.6rem;color:#fff;line-height:1.1;letter-spacing:-.02em}
.stats span{font-size:.71rem;color:#b9c9e2;line-height:1.35;display:block;margin-top:3px}
.cover table{margin:8px 0 0;border-color:rgba(255,255,255,.16);background:rgba(255,255,255,.04);font-size:.86rem}
.cover th,.cover td{border-color:rgba(255,255,255,.14);color:#dbe5f5;background:transparent!important}
.cover th{background:rgba(255,255,255,.07)!important;color:var(--gold-2);width:132px}
.cover tr:last-child>th,.cover tr:last-child>td{border-bottom:0}
.disc{font-size:.79rem;color:#aebfd8;border-top:1px solid rgba(255,255,255,.16);padding-top:14px;margin-top:20px;line-height:1.6}
.disc b{color:#e6edf8}

/* ---------- how to use ---------- */
.legend{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:14px 0}
.legend div{border:1px solid var(--line);border-radius:var(--radius-s);padding:12px 14px;font-size:.87rem;
  background:var(--paper);box-shadow:var(--shadow);color:var(--ink-2)}
.legend b{color:var(--navy);display:inline-block;margin:0 0 3px}
.howgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0}
.howbox{border:1px solid var(--line);border-radius:var(--radius-s);padding:14px 16px;font-size:.88rem;
  background:var(--paper);box-shadow:var(--shadow);color:var(--ink-2)}
.howbox .t{font-weight:800;color:var(--navy);font-size:.74rem;text-transform:uppercase;letter-spacing:.1em;margin-bottom:8px}
.howbox ol,.howbox ul{margin:6px 0 4px;padding-left:20px}
.howbox li{margin:4px 0}
.howbox b{color:var(--navy)}

/* ---------- toc ---------- */
nav.toc{border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px;background:var(--paper);
  box-shadow:var(--shadow);columns:2;column-gap:34px;font-size:.87rem}
nav.toc .grp{break-after:avoid;font-weight:800;color:var(--navy);text-transform:uppercase;font-size:.7rem;
  letter-spacing:.11em;margin:14px 0 6px;padding-bottom:4px;border-bottom:1px solid var(--line)}
nav.toc .grp:first-child{margin-top:0}
nav.toc ul{margin:0 0 4px;padding:0;list-style:none}
nav.toc li{margin:3px 0;color:var(--ink-2);break-inside:avoid}
nav.toc a{color:var(--ink-2)}
nav.toc a:hover{color:var(--blue-ink)}
nav.toc .sub{font-size:.76rem;color:var(--mut);white-space:nowrap}

/* ---------- index tables ---------- */
table.idx{font-size:.84rem}
table.idx td:first-child{font-weight:700;color:var(--navy);white-space:nowrap}
table.idx a{color:var(--blue-ink);border-bottom:1px solid #cfdcf5}
table.idx a:hover{border-color:var(--blue-ink);text-decoration:none}

/* ---------- status pills ---------- */
.st{display:inline-block;font-size:.68rem;font-weight:800;letter-spacing:.05em;padding:2px 9px;
  border-radius:999px;border:1px solid;white-space:nowrap;text-transform:uppercase}
.st.in{color:#14603c;border-color:#a9d8c1;background:#e9f8f0}
.st.concept{color:#1b4f93;border-color:#bdd2ee;background:#edf3fd}
.st.spent{color:#6b5a2a;border-color:#e6d6a2;background:#fdf8e6}
.st.superseded{color:#8d2f24;border-color:#eec0b8;background:#fdeeeb}

/* ---------- L1 quick-fire rows ---------- */
table.qf td.a{width:36%}
.reveal{font:inherit;font-size:.74rem;font-weight:700;padding:3px 11px;border:1px solid #c9d9f4;
  background:#eef4ff;color:var(--blue-ink);border-radius:999px;cursor:pointer;margin-right:8px;transition:all .15s ease}
.reveal:hover{background:#e0ebff;border-color:#a9c4ee}
.reveal[aria-expanded="true"]{background:var(--blue-ink);color:#fff;border-color:var(--blue-ink)}
.answer-text b{color:var(--navy)}
.vf{color:#a9761a;font-weight:800}

/* ---------- floating controls ---------- */
.top-index{position:fixed;right:18px;bottom:18px;z-index:40;background:linear-gradient(180deg,var(--navy-2),var(--navy));
  color:#fff;text-decoration:none;padding:9px 15px;border-radius:999px;font-size:.78rem;font-weight:700;
  box-shadow:0 10px 24px -12px rgba(15,34,68,.85);transition:transform .15s ease,box-shadow .15s ease}
.top-index:hover{transform:translateY(-2px);box-shadow:0 16px 30px -14px rgba(15,34,68,.9);text-decoration:none}

/* ---------- jump strip ---------- */
.jump{display:flex;flex-wrap:wrap;gap:7px;margin:0 0 20px}
.jump a{font-size:.79rem;font-weight:600;color:#33415c;background:#fff;border:1px solid var(--line);
  border-radius:999px;padding:5px 12px;box-shadow:0 1px 1px rgba(15,34,68,.04)}
.jump a:hover{color:var(--navy);border-color:#a9c0e2;background:#f4f8ff;text-decoration:none}

/* ---------- print ---------- */
@page{margin:14mm 11mm}
@media print{
  .flt,.jump,.prog,.top-index,.noprint{display:none!important}
  .wrap{max-width:none;padding:0}
  body{font-size:9.6pt;line-height:1.45;background:#fff}
  h2{break-after:avoid;margin:16px 0 8px}
  .case,.wrong,.ans,.model,.legend div,.howbox,tr{break-inside:avoid}
  .case{box-shadow:none;border-color:#c3ccdd}
  .ch{background:#eef3fa!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  details>summary{display:none}
  details>div.bd{display:block!important;padding-top:0}
  .pb{page-break-before:always}
  a{color:inherit;text-decoration:none}
  .cover{background:#0f2244!important;-webkit-print-color-adjust:exact;print-color-adjust:exact;border-radius:0}
  nav.toc{columns:2}
}

/* ---------- responsive ---------- */
@media (max-width:900px){
  nav.toc{columns:1}
  .stats{grid-template-columns:repeat(3,1fr)}
}
@media (max-width:760px){
  .wrap{padding:18px 14px 70px}
  .flt{margin:0 -14px 14px;padding:9px 14px}
  .flt input{min-width:0;width:100%;order:5}
  .flt .hint{display:none}
  .legend,.howgrid{grid-template-columns:1fr}
  .stats{grid-template-columns:repeat(2,1fr)}
  .ch{flex-direction:column}
  .ch .mk{align-self:flex-start}
  h2{margin-top:26px}
  table{font-size:.82rem}
  th,td{padding:7px 8px}
}
@media (prefers-reduced-motion:reduce){
  *{transition:none!important;animation:none!important;scroll-behavior:auto!important}
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
    if(h&&(h.tagName==='H3'||h.tagName==='H4'))h.hidden=!count;
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
const pr=document.getElementById('pr');
if(pr)pr.addEventListener('click',()=>window.print());
const bar=document.getElementById('prog');
const chrome=document.querySelector('.flt');
function onScroll(){
  const h=document.documentElement;
  const max=h.scrollHeight-h.clientHeight;
  if(bar)bar.style.width=(max>0?Math.min(100,(h.scrollTop/max)*100):0)+'%';
  if(chrome)chrome.classList.toggle('stuck',h.scrollTop>10);
}
window.addEventListener('scroll',onScroll,{passive:true});
window.addEventListener('resize',onScroll);
onScroll();
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
        out.append(f'<h3 class="set" id="l1-set-{i}"><span class="lv L1">L1</span> Set {i} — {esc(st["title"])} ({esc(st["range"])})</h3>')
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
             f'<style>{CSS}</style></head><body>',
             '<div class="prog" id="prog" aria-hidden="true"></div>',
             '<div class="wrap">']

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
        parts.append(f'<tr><th scope="row">{label}</th><td>{text}</td></tr>')
    parts.append("</table></div>")
    parts.append('<div class="disc"><b>Disclaimer.</b> Exam-study aid, not legal advice. Rely on the Gazette text and the current DoPT/CVC/CAG instructions '
                 'for official work. Facts, names, offices and figures are constructed for teaching; pay computations use 7th CPC matrix values and '
                 'illustrative DA/DR flagged ⚑ where the formal order was awaited on the law date.</div></section>')

    # toolbar — the controls the script has always listened for
    parts.append('<div class="flt" role="toolbar" aria-label="Filter and search the book">')
    parts.append('<span class="lab" style="margin:0 4px 0 0">Filter</span>')
    parts.append('<button type="button" data-f="all" class="on" aria-pressed="true">All</button>')
    parts.append('<button type="button" data-f="L1" aria-pressed="false">L1 · checks</button>')
    parts.append('<button type="button" data-f="L2" aria-pressed="false">L2 · cases</button>')
    parts.append('<button type="button" data-f="L3" aria-pressed="false">L3 · integrated</button>')
    parts.append('<input id="q" type="search" placeholder="Search facts, rules, figures, cases" aria-label="Search the book"/>')
    parts.append('<button type="button" id="ex">Expand all</button>')
    parts.append('<button type="button" id="co">Collapse all</button>')
    parts.append('<button type="button" id="pr">Print</button>')
    parts.append('<span class="hint">Filters and search work offline; nothing leaves the file.</span>')
    parts.append('</div>')

    # jump strip — the book is long, so the three parts and the indices get one click
    parts.append('<nav class="jump" aria-label="Jump to a part">')
    parts.append('<a href="#contents">Contents</a>')
    parts.append('<a href="#part-1">Part 1 · L1 checks</a>')
    parts.append('<a href="#part-2">Part 2 · L2 cases</a>')
    parts.append('<a href="#part-3">Part 3 · L3 cases</a>')
    parts.append('<a href="#rule-index">Rule index</a>')
    parts.append('<a href="#clock-index">Clocks</a>')
    parts.append('<a href="#caselaw-index">Case law</a>')
    parts.append('<a href="#sources">Sources</a>')
    parts.append('</nav>')

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
                 "<li><b>Toolbar</b> filter by level, search every case, expand or collapse all solutions, or send the book to the printer.</li>"
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
