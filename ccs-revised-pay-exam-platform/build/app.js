"use strict";
/* ============================================================================
   CCS (Revised Pay) Rules, 2016 — study and practice engine
   Vanilla JS, single file, no dependencies, no network calls.
   Data is injected before this script runs:
     MATRIX_DATA, RULES_DATA, PAY_DATA, CHAPTERS_DATA
   The distinctive part of this build is mxHtml(), below: every question that
   turns on a figure carries the slice of the Pay Matrix it turns on, and the
   platform draws that slice as a table with its cells numbered as in the
   printed Schedule.
   ========================================================================== */

const PAY_MAP = {};
PAY_DATA.forEach(q => { PAY_MAP[q.id] = q; });
const RULES_MAP = {};
RULES_DATA.forEach(r => { RULES_MAP[r.no] = r; });
const RULE_NOS = RULES_DATA.map(r => r.no);

const LS_KEY = "ccsrpr2016-state-v1";
const STATE = {
  answers: {},          // questionId -> { chosen, correct, ts, revealed }
  bookmarks: [],
  mistakes: [],
  mockResults: [],      // { id, score, total, at, minutes }
  prefs: { theme: "light", showTableInBank: true },
  bank: { page: 1, pageSize: 5, rule: "ALL", filter: "ALL", search: "" },
  num: { filter: "ALL", search: "" },
  rules: { search: "", chapter: "ALL" },
  mock: null,
  view: "dash"
};

/* ------------------------------------------------------------------ storage */
function save() {
  try {
    localStorage.setItem(LS_KEY, JSON.stringify({
      answers: STATE.answers, bookmarks: STATE.bookmarks, mistakes: STATE.mistakes,
      mockResults: STATE.mockResults, prefs: STATE.prefs, pageSize: STATE.bank.pageSize
    }));
  } catch (e) { /* storage blocked: the app still works in memory */ }
}
function load() {
  let raw = null;
  try { raw = localStorage.getItem(LS_KEY); } catch (e) { return; }
  if (!raw) return;
  let d; try { d = JSON.parse(raw); } catch (e) { return; }
  if (!d || typeof d !== "object") return;
  if (d.answers && typeof d.answers === "object")
    for (const k in d.answers) if (PAY_MAP[k] && d.answers[k] && typeof d.answers[k] === "object") STATE.answers[k] = d.answers[k];
  if (Array.isArray(d.bookmarks)) STATE.bookmarks = d.bookmarks.filter(k => PAY_MAP[k]);
  if (Array.isArray(d.mistakes)) STATE.mistakes = d.mistakes.filter(k => PAY_MAP[k]);
  if (Array.isArray(d.mockResults)) STATE.mockResults = d.mockResults.slice(-40);
  if (d.prefs && typeof d.prefs === "object") Object.assign(STATE.prefs, d.prefs);
  if (Number.isFinite(d.pageSize)) STATE.bank.pageSize = Math.min(20, Math.max(1, d.pageSize));
}

/* ------------------------------------------------------------------ helpers */
const $ = s => document.querySelector(s);
const $$ = s => Array.from(document.querySelectorAll(s));
const LETTERS = "ABCD";
function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, c =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}
/* Indian digit grouping, the way the Schedule prints money: 1,23,100 not 123,100 */
function inr(n) {
  if (n == null) return "—";
  const s = String(Math.trunc(n));
  if (s.length <= 3) return s;
  const last3 = s.slice(-3), rest = s.slice(0, -3);
  return rest.replace(/\B(?=(\d{2})+(?!\d))/g, ",") + "," + last3;
}
const rupee = n => "₹" + inr(n);
function pct(a, b) { return b ? Math.round((a / b) * 100) : 0; }
function ordinal(n) {
  const s = ["th", "st", "nd", "rd"], v = n % 100;
  return n + (s[(v - 20) % 10] || s[v] || s[0]);
}

/* ------------------------------------------------------------------ theme + nav */
function applyTheme(t) {
  document.documentElement.setAttribute("data-theme", t);
  const b = $("#btnTheme");
  if (b) b.textContent = t === "dark" ? "☀️ Light" : "🌙 Dark";
  STATE.prefs.theme = t; save();
}
function toggleTheme() { applyTheme(STATE.prefs.theme === "dark" ? "light" : "dark"); }

function switchView(v, opts) {
  STATE.view = v;
  $$(".view-panel").forEach(p => p.classList.toggle("active", p.id === "view-" + v));
  $$(".nav-btn[data-view]").forEach(b => b.classList.toggle("active", b.dataset.view === v));
  const main = $("#main-content");
  if (main) main.focus({ preventScroll: true });
  window.scrollTo(0, 0);
  if (v === "dash") renderDashboard();
  if (v === "rules") renderRules();
  if (v === "bank") renderBank();
  if (v === "numerical") renderNumerical();
  if (v === "matrix") renderMatrixView();
  if (v === "lab") { labPromotion(); labIncrement(); labFitment(); }
  if (v === "mock") { if (STATE.mock) renderCbt(); else renderMockList(); }
  if (v === "mistakes") renderMistakes();
  if (v === "settings") { renderSettings(); renderAmendments(); }
  if (opts && opts.rule) {
    STATE.bank.rule = String(opts.rule); STATE.bank.page = 1;
    const sel = $("#bankRule"); if (sel) sel.value = String(opts.rule);
    renderBank();
  }
}

/* ==========================================================================
   THE MATRIX RENDERER
   A question's `table` is one of three shapes, and each is drawn the way the
   printed Schedule reads: cell numbers across the top, pay beneath.
   ========================================================================== */
function mxRoleClass(role) {
  return role === "start" ? "cell-start" : role === "land" ? "cell-land" : role === "both" ? "cell-both" : "";
}
function mxRoleLabel(role) {
  return role === "start" ? "Pay before" : role === "land" ? "Lands here" : role === "both" ? "Start &amp; end" : "";
}
function mxColumnTable(rows, opts) {
  opts = opts || {};
  const missing = [];
  const cells = rows.map((r, i) => {
    // a run of unshown cells between two printed ones is marked, not silently closed up
    if (i > 0 && rows[i - 1].cell != null && r.cell != null && r.cell - rows[i - 1].cell > 1) {
      missing.push({ after: i - 1, from: rows[i - 1].cell + 1, to: r.cell - 1 });
    }
    return r;
  });
  let head = `<tr class="lvl"><td colspan="${cells.length}">${esc(opts.levelLabel || "")}</td></tr>`;
  const top = cells.map(r =>
    `<th scope="col"><span class="cn">Cell ${r.cell == null ? "—" : r.cell}</span>
      <span class="pay">${rupee(r.pay)}</span></th>`).join("");
  const body = cells.map(r =>
    `<td class="${mxRoleClass(r.role)}">${opts.showRole && r.role !== "plain"
      ? `<span class="role">${mxRoleLabel(r.role)}</span>` : ""}</td>`).join("");
  let html = `<table class="mx-col-table"><thead>${head}<tr>${top}</tr></thead>
    <tbody><tr>${body}</tr></tbody></table>`;
  if (missing.length) {
    // tell the reader the column is an excerpt, so a missing cell is not a lie
    const note = missing.map(m =>
      `cells ${m.from}${m.from !== m.to ? "–" + m.to : ""} not shown`).join("; ");
    html += `<div class="matrix-note" style="border-top:none;padding:2px 0 0">
      <span class="mx-key"><span class="sw gap" style="background:repeating-linear-gradient(45deg,#e2e8f0,#e2e8f0 3px,#fff 3px,#fff 6px)"></span>
      Excerpt: ${esc(note)}.</span></div>`;
  }
  return html;
}
function mxHtml(t) {
  if (!t) return "";
  const badge = t.kind === "cells" ? "Pay Matrix" : t.kind === "compare" ? "Amendment" : "Grade Pay map";
  let body = "", meta = "", note = t.note ? esc(t.note) : "";

  if (t.kind === "cells") {
    meta = `Level ${esc(t.level)}${t.pay_band ? " · Pay Band " + esc(t.pay_band) : ""}${t.grade_pay ? " · Grade Pay " + esc(t.grade_pay) : ""}`;
    body = mxColumnTable(t.cells, { levelLabel: `Level ${t.level}`, showRole: true });
    note = `<span class="mx-key"><span class="sw" style="background:var(--primary-light)"></span>pay before</span>` +
           `<span class="mx-key"><span class="sw" style="background:var(--gold-light)"></span>lands here</span>` +
           (note ? esc(note) : "");
  } else if (t.kind === "compare") {
    meta = `Level ${esc(t.level)} · the same cells before and after the notification`;
    body = `<div class="mx-compare">
      <figure class="before"><figcaption>${esc(t.before_label)}</figcaption>
        ${mxColumnTable(t.before, { levelLabel: `Level ${t.level}` })}</figure>
      <figure class="after"><figcaption>${esc(t.after_label)}</figcaption>
        ${mxColumnTable(t.after, { levelLabel: `Level ${t.level}` })}</figure></div>`;
  } else {
    meta = "One Grade Pay, more than one Pay Band — read the Level off the caption";
    body = `<table class="mx-map"><thead><tr><th>Grade Pay</th><th>Pay Band</th><th></th><th>Level</th><th>First cell</th></tr></thead><tbody>
      ${t.rows.map(r => `<tr class="${r.highlight ? "on" : ""}">
        <td>${r.grade_pay === "—" ? "—" : "₹" + esc(r.grade_pay)}</td>
        <td>${esc(r.pay_band)}</td><td class="mx-arrow">→</td>
        <td><b>${esc(r.level)}</b></td><td>${rupee(r.first_cell)}</td></tr>`).join("")}
      </tbody></table>`;
  }
  return `<div class="matrix-block">
    <div class="matrix-hd"><b>Pay Matrix</b><span class="mx-meta">${meta}</span>
      <span class="mx-badge">${badge}</span></div>
    <div class="matrix-scroll">${body}</div>
    ${note ? `<div class="matrix-note">${note}</div>` : ""}
  </div>`;
}

/* ==========================================================================
   THE EXPLANATION RENDERER
   The explanation is written in labelled blocks by the assembler; this turns
   each block into the right element rather than one wall of pre-formatted text.
   ========================================================================== */
const EXPL_HEADINGS = [
  "Worked solution, step by step",
  "Steps & statutory rationale",
  "Where the other options come from"
];
function explHtml(text, id) {
  const lines = String(text || "").split("\n");
  let cur = "", buf = [], out = [];
  function flush() {
    const body = buf.join("\n").trim();
    if (cur === "Answer") {
      const first = body.split("\n")[0] || "";
      out.push(`<div class="ans-line">${esc(first)}</div>`);
      const rest = body.split("\n").slice(1).join("\n").trim();
      if (rest) out.push(`<p class="ans-note">${esc(rest)}</p>`);
    } else if (cur === "Worked solution, step by step") {
      out.push(`<h4 class="expl-h">Worked solution</h4><ol class="expl-steps">${
        body.split("\n").map(l => l.trim()).filter(Boolean).map(l => `<li>${esc(l)}</li>`).join("")}</ol>`);
    } else if (cur === "Steps & statutory rationale") {
      out.push(`<h4 class="expl-h">The rule, step by step</h4><p class="expl-para">${esc(body)}</p>`);
    } else if (cur === "Where the other options come from") {
      out.push(`<h4 class="expl-h">Where the other options come from</h4><ul class="expl-wrong">${
        body.split("\n").map(l => l.trim()).filter(Boolean)
          .map(l => `<li>${esc(l)}</li>`).join("")}</ul>`);
    } else if (cur === "Exam-safe point") {
      out.push(`<div class="safe-box"><b>Exam-safe point</b>${esc(body)}</div>`);
    } else if (cur === "Statutory Authority") {
      out.push(`<div class="auth-line"><b>Authority</b> ${esc(body)}</div>`);
    } else if (body) {
      out.push(`<p class="expl-para">${esc(body)}</p>`);
    }
    buf = [];
  }
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed === "Answer" || EXPL_HEADINGS.includes(trimmed) || trimmed.startsWith("Exam-safe point")
        || trimmed.startsWith("Statutory Authority")) {
      flush();
      cur = trimmed.startsWith("Statutory Authority") ? "Statutory Authority"
          : trimmed.startsWith("Exam-safe point") ? "Exam-safe point" : trimmed;
      const after = trimmed.startsWith("Statutory Authority") ? trimmed.replace("Statutory Authority:", "").trim()
                  : trimmed.startsWith("Exam-safe point") ? trimmed.replace("Exam-safe point:", "").trim() : "";
      if (after) buf.push(after);
      continue;
    }
    buf.push(line);
  }
  flush();
  return out.join("");
}

/* ------------------------------------------------------------------ scoring */
function recordAnswer(id, letter, revealed) {
  const q = PAY_MAP[id];
  if (!q) return null;
  const correct = !revealed && letter === q.ans;
  STATE.answers[id] = { chosen: revealed ? null : letter, correct, revealed: !!revealed, ts: Date.now() };
  if (revealed || !correct) { if (!STATE.mistakes.includes(id)) STATE.mistakes.push(id); }
  else STATE.mistakes = STATE.mistakes.filter(x => x !== id);
  save();
  return { q, correct };
}
function stats() {
  const ids = Object.keys(STATE.answers);
  const attempted = ids.filter(k => !STATE.answers[k].revealed);
  const correct = attempted.filter(k => STATE.answers[k].correct).length;
  return {
    seen: ids.length, attempted: attempted.length, correct,
    accuracy: attempted.length ? Math.round((correct / attempted.length) * 100) : null,
    coverage: pct(ids.length, PAY_DATA.length),
    mistakes: STATE.mistakes.length,
    numeric: PAY_DATA.filter(q => q.section === "NUM").length,
    tables: PAY_DATA.filter(q => q.table).length
  };
}

/* ==========================================================================
   QUESTION CARD — shared by the practise bank, the numerical set and the mocks
   ========================================================================== */
function qCard(q, opts) {
  opts = opts || {};
  const a = STATE.answers[q.id];
  const chosen = a ? a.chosen : null;
  const showExpl = !!a;
  const booked = STATE.bookmarks.includes(q.id);
  const pad = opts.comped ? "mock-" : "";
  const optHtml = q.opts.map((o, i) => {
    const L = LETTERS[i];
    let cls = "mcq-opt";
    if (a) {
      if (L === q.ans) cls += " correct";
      else if (L === chosen) cls += " incorrect";
      else cls += " dim";
    }
    return `<button class="${cls}" onclick="answer('${esc(q.id)}','${L}')"
      ${a ? "disabled" : ""} aria-pressed="${chosen === L}">
      <span class="opt-letter">${L}</span><span class="opt-text">${esc(o)}</span></button>`;
  }).join("");

  const hasTable = q.table && (opts.forceTable || STATE.prefs.showTableInBank || opts.section === "numerical");
  const tableHtml = hasTable ? mxHtml(q.table) : (q.table && opts.offerTable
    ? `<div class="matrix-collapsed"><button class="mcq-act-btn" onclick="toggleTable('${esc(q.id)}')">
        ▦ ${STATE.openTables && STATE.openTables[q.id] ? "Hide" : "Show"} the pay-matrix excerpt</button></div>` : "");
  return `<article class="mcq-card" id="${pad}q-${esc(q.id)}">
    <div class="mcq-hd">
      <span class="mcq-id">${esc(q.id)}</span>
      <span class="mcq-tag Tag">${esc(q.tag)}</span>
      <span class="mcq-tag Topic">${esc(q.rules_text)}</span>
      ${q.section === "NUM" ? `<span class="mcq-tag Topic" style="border-color:var(--gold)">Numerical</span>` : ""}
      ${q.faq ? `<span class="mcq-tag Topic" style="border-color:var(--teal)">FAQ</span>` : ""}
      ${q.table ? `<span class="mcq-tag Topic">▦ matrix</span>` : ""}
      ${opts.comped ? "" : `<button class="copy-btn" onclick="toggleBookmark('${esc(q.id)}')">${booked ? "★ Bookmarked" : "☆ Bookmark"}</button>`}
    </div>
    <div class="mcq-stem">${esc(q.q)}</div>
    ${tableHtml}
    <div class="mcq-opts">${optHtml}</div>
    ${showExpl ? `<div class="mcq-expl open">
        <div class="mcq-expl-hd">Explanation — ${a.correct ? "correct ✓" : a.revealed ? "answer revealed" : "review this"}</div>
        <div class="mcq-expl-body">${explHtml(q.expl, q.id)}</div>
        ${q.table && !hasTable ? mxHtml(q.table) : ""}
        <div class="mcq-src">${esc(q.src)}</div></div>` : ""}
    <div class="mcq-actions">
      ${a ? `<button class="mcq-act-btn" onclick="resetQ('${esc(q.id)}')">↺ Try again</button>`
           : `<button class="mcq-act-btn" onclick="revealQ('${esc(q.id)}')">Reveal answer</button>`}
      ${q.table && !hasTable && opts.offerTable ? "" : ""}
      <span class="pill">${esc(q.topic)}</span>
      ${q.trap ? `<span class="pill warn">Trap: ${esc(q.trap)}</span>` : ""}
    </div>
  </article>`;
}

const OPEN_TABLES = {};
function toggleTable(id) { OPEN_TABLES[id] = !OPEN_TABLES[id]; renderBank(); }

function answer(id, L) {
  if (STATE.answers[id]) return;
  const res = recordAnswer(id, L, false);
  const card = document.getElementById("q-" + id);
  if (card) { card.outerHTML = qCard(res.q, card.dataset.opts ? {} : {}); }
  updateSideProgress();
  afterAnswer();
}
function revealQ(id) {
  if (STATE.answers[id]) return;
  const res = recordAnswer(id, null, true);
  const card = document.getElementById("q-" + id);
  if (card) card.outerHTML = qCard(res.q, {});
  updateSideProgress();
  afterAnswer();
}
function resetQ(id) {
  delete STATE.answers[id];
  STATE.mistakes = STATE.mistakes.filter(x => x !== id);
  save();
  if (STATE.view === "bank") renderBank();
  if (STATE.view === "numerical") renderNumerical();
  if (STATE.view === "mistakes") renderMistakes();
  updateSideProgress();
}
function toggleBookmark(id) {
  if (STATE.bookmarks.includes(id)) STATE.bookmarks = STATE.bookmarks.filter(x => x !== id);
  else STATE.bookmarks.push(id);
  save();
  if (STATE.view === "bank") renderBank();
}
function afterAnswer() {
  if (STATE.view === "mock" && STATE.mock) renderCbt();
}

/* ==========================================================================
   DASHBOARD
   ========================================================================== */
function renderDashboard() {
  const s = stats();
  $("#dashAttempted").textContent = s.attempted;
  $("#dashAccuracy").textContent = s.accuracy == null ? "—" : s.accuracy + "%";
  $("#dashCoverage").textContent = s.coverage + "%";
  $("#dashMistakes").textContent = s.mistakes;
  const budget = Math.max(0, Math.round((100 - s.coverage) / 100 * PAY_DATA.length * 1.4));
  $("#dashRing").style.setProperty("--pct", s.coverage);
  $("#dashRingLabel").textContent = s.coverage + "%";
  $("#dashProgressFill").style.width = s.coverage + "%";
  $("#sideProgressPercent").textContent = s.coverage + "%";
  $("#sideProgressFill").style.width = s.coverage + "%";
  $("#sideProgressText").textContent = `${s.seen} / ${PAY_DATA.length} questions seen`;

  let rec;
  if (!s.seen) rec = "Start with <b>The craft of the file</b> or with <b>PY-001</b>: the whole of rule 7 is in that one sum. Ten minutes on the matrix, then come back to the questions.";
  else if (s.mistakes) rec = `You have <b>${s.mistakes}</b> question(s) in the mistake notebook. Work those first — the same two or three traps account for most of the errors in this subject.`;
  else if (s.coverage < 40) rec = `You have covered <b>${s.coverage}%</b> of the bank at <b>${s.accuracy}%</b> accuracy. The fastest gain now is the numerical set: every one of the ${PAY_DATA.filter(q => q.section === "NUM").length} figures is worked in full.`;
  else if (s.coverage < 80) rec = `Past the halfway mark, at <b>${s.accuracy}%</b>. Sit one of the timed papers next — the matrix questions are where the clock disappears.`;
  else rec = `Nearly through the bank at <b>${s.accuracy}%</b>. Go back to the trap list on each card: the marks left are in the rounding and in the old-Level increment.`;
  $("#dashRecommendation").innerHTML = rec;

  const rows = RULE_NOS.map(no => {
    const qs = PAY_DATA.filter(q => String(q.rule) === no);
    const seen = qs.filter(q => STATE.answers[q.id]);
    const att = seen.filter(q => !STATE.answers[q.id].revealed);
    const cor = att.filter(q => STATE.answers[q.id].correct);
    const r = RULES_MAP[no];
    return `<tr><td><b>${no}</b></td><td>${esc((r.title || "").slice(0, 74))}</td>
      <td>${qs.length}</td><td>${seen.length}</td>
      <td>${att.length ? Math.round(cor.length / att.length * 100) + "%" : "—"}</td>
      <td><button class="copy-btn" onclick="switchView('bank',{rule:'${no}'})">practise</button></td></tr>`;
  }).join("");
  $("#dashChapterRows").innerHTML = rows;
  $("#dashTableCount").textContent = s.tables;
  $("#dashNumericCount").textContent = s.numeric;
}

/* ==========================================================================
   PRACTISE — the general bank and the numericals
   ========================================================================== */
function bankList() {
  let list = PAY_DATA.slice();
  const c = STATE.bank;
  if (c.rule !== "ALL") list = list.filter(q => String(q.rule) === c.rule);
  if (c.filter === "MISTAKES") list = list.filter(q => STATE.mistakes.includes(q.id));
  if (c.filter === "BOOKMARKS") list = list.filter(q => STATE.bookmarks.includes(q.id));
  if (c.filter === "UNSEEN") list = list.filter(q => !STATE.answers[q.id]);
  if (c.filter === "NUMERICAL") list = list.filter(q => q.section === "NUM");
  if (c.filter === "MATRIX") list = list.filter(q => q.table);
  if (c.filter === "FAQ") list = list.filter(q => q.faq);
  if (c.search) {
    const q = c.search.toLowerCase();
    list = list.filter(m => (m.id + " " + m.q + " " + m.topic + " " + m.expl + " " + m.rules_text).toLowerCase().includes(q));
  }
  return list;
}
function renderBank() {
  const list = bankList(), c = STATE.bank;
  const pages = Math.max(1, Math.ceil(list.length / c.pageSize));
  if (c.page > pages) c.page = pages;
  const slice = list.slice((c.page - 1) * c.pageSize, c.page * c.pageSize);
  $("#bankCount").textContent = inr(list.length) + " question" + (list.length === 1 ? "" : "s") + " in this set";
  $("#bankScope").textContent = "Showing " + describeScope();
  $("#bankList").innerHTML = slice.length
    ? slice.map(q => qCard(q, { offerTable: true })).join("")
    : `<div class="empty-state">No question matches this set. Clear the filters or pick another rule.</div>`;
  $("#bankPager").innerHTML = pages > 1 ? `
    <button class="btn-secondary" ${c.page === 1 ? "disabled" : ""} onclick="bankPage(-1)">← Previous</button>
    <span class="fc-progress">Page ${c.page} of ${pages}</span>
    <button class="btn-secondary" ${c.page === pages ? "disabled" : ""} onclick="bankPage(1)">Next →</button>` : "";
}
function describeScope() {
  const c = STATE.bank, bits = [];
  bits.push(c.rule === "ALL" ? "all seventeen rules" : "rule " + c.rule + (RULES_MAP[c.rule] ? " — " + RULES_MAP[c.rule].title : ""));
  if (c.filter === "MISTAKES") bits.push("mistake notebook only");
  if (c.filter === "BOOKMARKS") bits.push("bookmarked only");
  if (c.filter === "UNSEEN") bits.push("not yet attempted");
  if (c.filter === "NUMERICAL") bits.push("the numerical set only");
  if (c.filter === "MATRIX") bits.push("questions that carry a matrix");
  if (c.filter === "FAQ") bits.push(`the FAQ library — ${PAY_DATA.filter(q => q.faq).length} points settled by the Department`);
  if (c.search) bits.push(`search "${c.search}"`);
  return bits.join(" · ");
}
function bankPage(d) { STATE.bank.page += d; renderBank(); window.scrollTo({ top: 0, behavior: "smooth" }); }
function setBankFilter(f) { STATE.bank.filter = f; STATE.bank.page = 1; renderBank(); }
function bankFilters() {
  STATE.bank.rule = $("#bankRule").value;
  STATE.bank.search = $("#bankSearch").value.trim();
  STATE.bank.page = 1;
  renderBank();
}

function numericalList() {
  let list = PAY_DATA.filter(q => q.section === "NUM");
  const f = STATE.num.filter;
  if (f === "UNSEEN") list = list.filter(q => !STATE.answers[q.id]);
  if (f === "MISTAKES") list = list.filter(q => STATE.mistakes.includes(q.id));
  if (f === "STEPS") { /* all shown, handled below */ }
  if (STATE.num.search) {
    const s = STATE.num.search.toLowerCase();
    list = list.filter(q => (q.id + q.q + q.topic).toLowerCase().includes(s));
  }
  return list;
}
function renderNumerical() {
  const list = numericalList();
  const f = STATE.num.filter;
  $("#numCount").textContent = list.length + " question" + (list.length === 1 ? "" : "s");
  $("#numericalList").innerHTML = list.length
    ? list.map(q => {
        const open = f === "STEPS" && !STATE.answers[q.id];
        if (open) STATE.answers[q.id] = { chosen: null, correct: false, revealed: true, ts: Date.now() };
        return qCard(q, { section: "numerical", forceTable: true });
      }).join("")
    : `<div class="empty-state">Nothing in this set. Switch the filter back to All.</div>`;
  const att = list.filter(q => STATE.answers[q.id] && !STATE.answers[q.id].revealed);
  const cor = att.filter(q => STATE.answers[q.id].correct);
  $("#numScore").textContent = att.length ? `${cor.length} / ${att.length} correct` : "";
}
function setNumFilter(f) { STATE.num.filter = f; renderNumerical(); }
function numSearch() { STATE.num.search = $("#numSearch").value.trim(); renderNumerical(); }
function exportNumerical() {
  const LET = LETTERS;
  const lines = ["THE NUMERICAL SET — CCS (Revised Pay) Rules, 2016", ""];
  let i = 0;
  for (const q of PAY_DATA.filter(q => q.section === "NUM")) {
    i++;
    lines.push(`Q${i}. [${q.id}] ${q.q}`, "");
    q.opts.forEach((o, k) => lines.push(`  (${LET[k]}) ${o}`));
    lines.push("", `Answer: (${q.ans})`, "");
    lines.push(q.expl, "", "-".repeat(72), "");
  }
  const blob = new Blob([lines.join("\n")], { type: "text/plain;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "CCS-Revised-Pay-Numerical-Set.txt";
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
}

/* ==========================================================================
   RULE LIBRARY
   ========================================================================== */
function renderRules() {
  const c = STATE.rules;
  const q = (c.search || "").toLowerCase();
  const list = RULES_DATA.filter(r => {
    if (c.chapter !== "ALL" && String(r.chapter) !== String(c.chapter)) return false;
    if (!q) return true;
    return (r.no + " " + r.title + " " + r.bare + " " + r.why + " " + (r.figures || []).join(" ") + " " + r.trap).toLowerCase().includes(q);
  });
  $("#ruleCount").textContent = list.length + " of " + RULES_DATA.length + " rules";
  $("#rulesList").innerHTML = list.map(r => {
    const figs = (r.figures || []).map(f => {
      const i = f.indexOf(":");
      return i > 0 ? `<div><b>${esc(f.slice(0, i))}</b>${esc(f.slice(i + 1).trim())}</div>`
                   : `<div class="fig-plain">${esc(f)}</div>`;
    }).join("");
    const hooks = (r.hooks || []).length
      ? `<div class="pill-row">${r.hooks.map(h => `<span class="pill">${esc(h)}</span>`).join("")}</div>` : "";
    return `<article class="rule-card" id="rule-${esc(r.no)}">
      <div class="mcq-hd">
        <span class="mcq-id">Rule ${esc(r.no)}</span>
        <span class="mcq-tag Topic">${esc(chapterTitle(r.chapter))}</span>
        <button class="copy-btn" onclick="practiseRule('${esc(r.no)}')">practise this rule</button>
      </div>
      <h3 style="font-size:1.02rem;margin:6px 0 8px">${esc(r.title)}</h3>
      <div class="bare-text">${esc(r.text)}</div>
      <p class="rule-summary"><b>In short.</b> ${esc(r.bare)}</p>
      <div class="rule-fig">${figs}</div>
      <details class="rule-details open"><summary>Why the rule says what it says</summary>
        <p class="expl-para">${esc(r.why)}</p>
        ${hooks}
      </details>
      <div class="trap-line"><b>Trap</b> ${esc(r.trap)}</div>
    </article>`;
  }).join("") || `<div class="empty-state">No rule matches that search.</div>`;
}
function chapterTitle(c) {
  const ch = CHAPTERS_DATA.find(x => String(x.no) === String(c) || String(x.id) === String(c));
  return ch ? (ch.title || ch.name || ("Chapter " + c)) : ("Chapter " + c);
}
function practiseRule(no) { switchView("bank", { rule: no }); }
function ruleFilters() {
  STATE.rules.search = $("#ruleSearch").value.trim();
  STATE.rules.chapter = $("#ruleChapter").value;
  renderRules();
}
function expandAllRules() { $$(".rule-details").forEach(d => d.open = true); }
function collapseAllRules() { $$(".rule-details").forEach(d => d.open = false); }

/* ==========================================================================
   THE FULL MATRIX
   ========================================================================== */
function renderMatrixView() {
  const lvls = MATRIX_DATA.levels;
  const maxCols = Math.max(...lvls.map(l => MATRIX_DATA.current[l].length));
  const head = `<tr><th>Level</th><th>Pay Band</th><th>Grade Pay</th>` +
    Array.from({ length: maxCols }, (_, i) => `<th>${i + 1}</th>`).join("") + "</tr>";
  const body = lvls.map(l => {
    const cur = MATRIX_DATA.current[l];
    const cell = (i) => {
      if (i < cur.length) {
        const flagged = l === "13" && i < MATRIX_DATA.level13_original.length &&
          cur[i] !== MATRIX_DATA.level13_original[i];
        return `<td class="${flagged ? "l13" : ""}" title="${flagged ? "Re-cast by the resolution of 16.05.2017; as notified " + rupee(MATRIX_DATA.level13_original[i]) : ""}">${inr(cur[i])}</td>`;
      }
      return `<td class="pv">·</td>`;
    };
    return `<tr><td>Level ${l}</td><td>${esc(MATRIX_DATA.pay_band[l] || "")}</td>
      <td>${esc(MATRIX_DATA.grade_pay[l] || "")}</td>
      ${Array.from({ length: maxCols }, (_, i) => cell(i)).join("")}</tr>`;
  }).join("");
  $("#mxTableWrap").innerHTML = `<table class="mx-full"><thead>${head}</thead><tbody>${body}</tbody></table>`;
  $("#mxCellCount").textContent = inr(lvls.reduce((n, l) => n + MATRIX_DATA.current[l].length, 0));
  $("#mxLevelCount").textContent = lvls.length;
}

/* ==========================================================================
   THE LAB — four calculators, each on the same engine
   ========================================================================== */
function labFitment() {
  const pay = +$("#labPay").value || 0, gp = +$("#labGP").value || 0;
  const basic = pay + gp;
  const prod = Math.round(basic * 2.57);
  const lv = $("#labLevel").value;
  const col = MATRIX_DATA.current[lv];
  const hit = col.find(c => c >= prod);
  const cell = hit ? col.indexOf(hit) + 1 : null;
  const note = !hit ? "Above the top of this Level — check the Level." :
    hit === prod ? `₹${inr(prod)} is itself a cell, so the pay is fixed there.` :
    `₹${inr(prod)} is not a cell; the next higher cell is ₹${inr(hit)}.`;
  $("#labFitOut").innerHTML = `
    <div class="line">Existing basic pay (pay + grade pay) <b>${rupee(basic)}</b></div>
    <div class="line">× 2.57 <b>${basic.toLocaleString("en-IN")} × 2.57 = ${prod.toLocaleString("en-IN")}</b></div>
    <div class="line">Rounded to the nearest rupee <b>${rupee(prod)}</b></div>
    <div class="line">Level ${esc(lv)}${cell ? ` · cell ${cell}` : ""} <b>${hit ? rupee(hit) : "—"}</b></div>
    <div class="big">${hit ? rupee(hit) : "—"}</div>
    <div class="calc-hint">${esc(note)} Rule 7(1)(A)(i) rounds to the rupee and then takes the equal or next higher cell; clause (ii) puts the pay at the first cell if the product falls below it.</div>`;
  const bar = col.slice(Math.max(0, (cell || 1) - 3), Math.min(col.length, (cell || 1) + 2));
  $("#labFitBar").innerHTML = bar.map(c => `<span class="rung ${c === hit ? "here" : ""}">${rupee(c)}</span>`).join('<span class="arw">→</span>');
}
function labIncrement() {
  const lv = $("#labIncLevel").value, pay = +$("#labIncPay").value || 0;
  const col = MATRIX_DATA.current[lv];
  const i = col.indexOf(pay);
  const next = i >= 0 && i < col.length - 1 ? col[i + 1] : null;
  $("#labIncOut").innerHTML = i < 0
    ? `<div class="line" style="color:var(--bad)">${rupee(pay)} is not a cell of Level ${esc(lv)}. Pick a printed figure.</div>`
    : next == null
      ? `<div class="line">${rupee(pay)} is the last cell of Level ${esc(lv)}</div>
         <div class="big">${rupee(pay)}</div>
         <div class="calc-hint">There is no next cell, so the pay stands still. Rule 9 moves pay only within the printed cells.</div>`
      : `<div class="line">Cell ${i + 1} <b>${rupee(pay)}</b></div>
         <div class="line">Next cell, +1 <b>${rupee(next)}</b></div>
         <div class="line">The step is <b>${rupee(next - pay)}</b> (3% would be ${rupee(Math.round(pay * 0.03))})</div>
         <div class="big">${rupee(next)}</div>
         <div class="calc-hint">One increment is one vertical cell. The matrix has already rounded each cell to the nearest ₹100, which is why the step is not exactly 3%.</div>`;
  const from = Math.max(0, (i < 0 ? 0 : i) - 2), to = Math.min(col.length, (i < 0 ? 0 : i) + 3);
  $("#labIncBar").innerHTML = col.slice(from, to).map(c =>
    `<span class="rung ${c === pay ? "here" : c === next ? "next" : ""}">${rupee(c)}</span>`).join('<span class="arw">→</span>');
}
function labPromotion() {
  const from = $("#labPromFrom").value, to = $("#labPromTo").value;
  const pay = +$("#labPromPay").value || 0;
  const src = MATRIX_DATA.current[from], dst = MATRIX_DATA.current[to];
  const i = src.indexOf(pay);
  const stepped = i >= 0 && i < src.length - 1 ? src[i + 1] : pay;
  const landIdx = dst.findIndex(c => c >= stepped);
  const land = landIdx >= 0 ? dst[landIdx] : null;
  $("#labPromOut").innerHTML = i < 0
    ? `<div class="line" style="color:var(--bad)">${rupee(pay)} is not a cell of Level ${esc(from)}.</div>`
    : `<div class="line">Step 1 — one increment in Level ${esc(from)} <b>${rupee(stepped)}</b></div>
       <div class="line">Step 2 — the equal or next higher cell in Level ${esc(to)} <b>${land ? rupee(land) : "—"}</b></div>
       <div class="line">Rise on promotion <b>${land ? rupee(land - pay) : "—"}</b></div>
       <div class="big">${land ? rupee(land) : "—"}</div>
       <div class="calc-hint">Rule 13(i): the increment is always taken in the OLD Level. If the stepped figure is not a cell of the new Level, the next higher cell is used — which is why 28,700 → 29,600 lands on ₹30,100 and not on ₹29,600.</div>`;
  $("#labPromBar").innerHTML = [[from, pay, "here"], [from, stepped, "next"], [to, land, "here"]]
    .filter(x => x[1] != null)
    .map(x => `<span class="rung ${x[2]}" title="Level ${x[0]}">L${x[0]} ${rupee(x[1])}</span>`)
    .join('<span class="arw">→</span>');
}
function labNpa() {
  const basic = +$("#labNpaPay").value || 0, pctNpa = +$("#labNpaPct").value || 0;
  const npa = Math.round(basic * pctNpa / 100);
  const da = Math.round(npa * 1.25);
  const prod = Math.round(basic * 2.57) + da;
  const col = MATRIX_DATA.current["10"];
  const hit = col.find(c => c >= prod);
  $("#labNpaOut").innerHTML = `
    <div class="line">Pre-revised NPA (${pctNpa}% of basic) <b>${rupee(npa)}</b></div>
    <div class="line">DA at 125% on the NPA (rounded up) <b>${rupee(da)}</b></div>
    <div class="line">Basic × 2.57 + DA on NPA <b>${rupee(Math.round(basic * 2.57))} + ${rupee(da)}</b></div>
    <div class="line">Figure to locate in Level 10 <b>${rupee(prod)}</b></div>
    <div class="big">${hit ? rupee(hit) : "—"}</div>
    <div class="calc-hint">Rule 7(1)(B): the revised pay is ${hit ? rupee(hit) : "—"}, and the pre-revised NPA of ${rupee(npa)} is then added on top until revised NPA rates are settled — ${hit ? rupee(hit + npa) : "—"} in all. The NPA never enters the matrix.</div>`;
}

/* ==========================================================================
   MOCK PAPERS — generated, then frozen into the paper
   ========================================================================== */
function buildPapers() {
  const papers = [];
  const all = PAY_DATA.slice();
  // a deterministic shuffle, so the same paper is the same every time it is opened
  function seeded(seed) {
    let s = seed;
    return () => { s = (s * 1103515245 + 12345) & 0x7fffffff; return s / 0x7fffffff; };
  }
  function take(pool, n, rnd) {
    const cp = pool.slice();
    for (let i = cp.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [cp[i], cp[j]] = [cp[j], cp[i]]; }
    return cp.slice(0, n);
  }
  const num = all.filter(q => q.section === "NUM");
  const bank = all.filter(q => q.section !== "NUM");
  const specs = [
    { id: "PAPER-1", name: "Paper I — Fixation and the fitment factor", n: 15, min: 18, pick: q => ["7", "9", "8", "11"].includes(String(q.rule)) },
    { id: "PAPER-2", name: "Paper II — The option, increments and dates", n: 15, min: 18, pick: q => ["5", "6", "10"].includes(String(q.rule)) },
    { id: "PAPER-3", name: "Paper III — Promotion, MACP and Level 13", n: 15, min: 18, pick: q => ["13", "12", "Schedule"].includes(String(q.rule)) },
    { id: "PAPER-4", name: "Paper IV — The whole rule-book", n: 25, min: 30, pick: () => true }
  ];
  specs.forEach((sp, k) => {
    const rnd = seeded(9173 + k * 331);
    const chosen = take(all.filter(sp.pick), sp.n, rnd);
    // keep the balance: a third of every paper is arithmetic where the pool allows it
    const needNum = Math.max(0, Math.ceil(sp.n / 3) - chosen.filter(q => q.section === "NUM").length);
    const extra = take(num.filter(q => !chosen.includes(q)), needNum, rnd);
    const final = chosen.concat(extra);
    const byRule = {};
    final.forEach(q => { byRule[q.rule] = (byRule[q.rule] || 0) + 1; });
    papers.push({ id: sp.id, name: sp.name, minutes: sp.min, questions: final, byRule,
                  matrixQs: final.filter(q => q.table).length });
  });
  return papers;
}
const PAPERS = buildPapers();

function renderMockList() {
  $("#mockHeading").textContent = "Timed papers";
  $("#mockSubheading").textContent = "Four papers generated from the bank itself, each weighted so that at least a third of the questions are arithmetic. The matrix comes with the question, as it does in the practice bank.";
  $("#cbtBar").hidden = true;
  $("#cbtList").innerHTML = "";
  $("#mockList").innerHTML = PAPERS.map(p => {
    const done = STATE.mockResults.filter(r => r.id === p.id);
    const best = done.length ? Math.max(...done.map(r => r.score)) : null;
    return `<article class="rule-card">
      <div class="mcq-hd"><span class="mcq-id">${esc(p.id)}</span>
        <span class="mcq-tag Topic">${p.questions.length} questions · ${p.minutes} minutes</span>
        <span class="mcq-tag Topic">▦ ${p.matrixQs} matrix questions</span></div>
      <h3 style="font-size:1.02rem;margin:6px 0 6px">${esc(p.name)}</h3>
      <p style="font-size:.86rem;color:var(--ink-muted)">Rules drawn: ${Object.keys(p.byRule).sort((a, b) => a - b).map(r => "R" + r).join(", ")}.
        ${done.length ? `Best so far: <b>${best}/${p.questions.length}</b> over ${done.length} attempt(s).` : "Not attempted yet."}</p>
      <div class="pill-row"><button class="btn-primary" onclick="startPaper('${esc(p.id)}')">Start the paper →</button></div>
    </article>`;
  }).join("");
}
function startPaper(id) {
  const p = PAPERS.find(x => x.id === id);
  STATE.mock = { paper: p, answers: {}, started: Date.now(), seconds: p.minutes * 60 };
  switchView("mock");
  renderCbt();
  if (typeof mockTimer !== "undefined" && mockTimer) clearInterval(mockTimer);
  mockTimer = setInterval(() => {
    if (!STATE.mock) { clearInterval(mockTimer); return; }
    STATE.mock.seconds--;
    const el = $("#cbtTimer");
    if (el) el.textContent = fmtClock(Math.max(0, STATE.mock.seconds));
    if (STATE.mock.seconds === 60) { const t = $("#cbtTimer"); if (t) t.style.color = "var(--bad)"; }
    if (STATE.mock.seconds <= 0) { clearInterval(mockTimer); finishPaper(); }
  }, 1000);
}
let mockTimer = null;
function fmtClock(s) {
  const m = Math.floor(s / 60), r = s % 60;
  return String(m).padStart(2, "0") + ":" + String(r).padStart(2, "0");
}
function renderCbt() {
  const st = STATE.mock;
  if (!st) { renderMockList(); return; }
  const p = st.paper;
  $("#mockHeading").textContent = p.name;
  $("#mockSubheading").textContent = `${p.questions.length} questions in ${p.minutes} minutes. At least a third of them are arithmetic.`;
  $("#mockList").innerHTML = "";
  $("#cbtBar").hidden = false;
  $("#cbtName").textContent = p.id;
  $("#cbtTimer").textContent = fmtClock(Math.max(0, st.seconds));
  const answered = Object.keys(st.answers).length;
  $("#cbtProgress").textContent = `${answered} / ${p.questions.length} answered`;
  $("#cbtList").innerHTML = p.questions.map((q, i) => {
    const mine = st.answers[q.id];
    const opt = q.opts.map((o, k) => {
      const L = LETTERS[k];
      const cls = "mcq-opt" + (mine === L ? " picked" : "");
      return `<button class="${cls}" onclick="cbtPick('${esc(q.id)}','${L}')"><span class="opt-letter">${L}</span>
        <span class="opt-text">${esc(o)}</span></button>`;
    }).join("");
    return `<article class="mcq-card" id="cbt-${esc(q.id)}">
      <div class="mcq-hd"><span class="mcq-id">Q${i + 1}</span>
        <span class="mcq-tag Topic">${esc(q.rules_text)}</span></div>
      <div class="mcq-stem">${esc(q.q)}</div>
      ${q.table ? mxHtml(q.table) : ""}
      <div class="mcq-opts">${opt}</div></article>`;
  }).join("");
}
function abandonPaper() {
  if (mockTimer) { clearInterval(mockTimer); mockTimer = null; }
  const st = STATE.mock;
  STATE.mock = null;
  $("#cbtResult").innerHTML = "";
  $("#cbtList").innerHTML = "";
  renderMockList();
  if (st) $("#mockSubheading").textContent = "Paper left unfinished. Nothing was recorded.";
}
function cbtPick(id, L) {
  if (!STATE.mock) return;
  if (STATE.mock.answers[id] === L) delete STATE.mock.answers[id];
  else STATE.mock.answers[id] = L;
  renderCbt();
}
function finishPaper() {
  const st = STATE.mock;
  if (!st) return;
  if (mockTimer) { clearInterval(mockTimer); mockTimer = null; }
  let score = 0;
  const per = [];
  st.paper.questions.forEach(q => {
    const mine = st.answers[q.id];
    const ok = mine === q.ans;
    if (ok) score++;
    per.push({ id: q.id, mine: mine || "—", key: q.ans, ok });
    STATE.answers[q.id] = { chosen: mine || null, correct: ok, revealed: !mine, ts: Date.now() };
    if (!ok) { if (!STATE.mistakes.includes(q.id)) STATE.mistakes.push(q.id); }
  });
  const used = st.paper.minutes * 60 - Math.max(0, st.seconds);
  STATE.mockResults.push({ id: st.paper.id, score, total: st.paper.questions.length, at: Date.now(), seconds: used });
  save();
  $("#cbtResult").innerHTML = `<div class="stat-card" style="border-left:4px solid var(--ok)">
    <h3 style="font-size:1.05rem">${esc(st.paper.name)} — ${score} / ${st.paper.questions.length}</h3>
    <p style="font-size:.86rem;color:var(--ink-muted)">Time used: ${fmtClock(used)}. Accuracy ${Math.round(score / st.paper.questions.length * 100)}%.
      Every question is now in the bank with its solution open below.</p>
    <div class="pill-row">${per.map(x => `<span class="pill ${x.ok ? "ok" : "bad"}">${esc(x.id)} ${x.ok ? "✓" : "✗"}</span>`).join("")}</div></div>`;
  STATE.mock = null;
  renderMockList();
  updateSideProgress();
  $("#cbtList").innerHTML = st.paper.questions.map(q => qCard(q, { forceTable: true })).join("");
}

/* ==========================================================================
   MISTAKES, SETTINGS, PROGRESS
   ========================================================================== */
function renderMistakes() {
  const list = PAY_DATA.filter(q => STATE.mistakes.includes(q.id));
  $("#mistakeCount").textContent = list.length;
  $("#mistakesList").innerHTML = list.length
    ? list.map(q => qCard(q, { forceTable: true })).join("")
    : `<div class="empty-state">Nothing here. Answer a question wrongly, or reveal one, and it will wait for you here until you get it right.</div>`;
}
function clearMistakes() {
  STATE.mistakes = [];
  STATE.answers = {};
  save(); renderMistakes(); updateSideProgress();
}
function renderSettings() {
  const s = stats();
  $("#settingsStats").innerHTML = `
    <div class="schema-row"><b>questions</b><span>${PAY_DATA.length} — ${PAY_DATA.filter(q => q.section === "NUM").length} worked numericals, ${PAY_DATA.filter(q => q.section !== "NUM").length} general</span></div>
    <div class="schema-row"><b>matrix excerpts</b><span>${PAY_DATA.filter(q => q.table).length} questions carry the slice of the Pay Matrix they turn on</span></div>
    <div class="schema-row"><b>matrix cells</b><span>${inr(MATRIX_DATA.levels.reduce((n, l) => n + MATRIX_DATA.current[l].length, 0))} across ${MATRIX_DATA.levels.length} Levels, each regenerated from its first cell at 3% to the nearest ₹100</span></div>
    <div class="schema-row"><b>rules</b><span>${RULES_DATA.length}, with the bare text, the working, the figures and the trap</span></div>
    <div class="schema-row"><b>you</b><span>${s.seen} questions seen · ${s.attempted} attempted · ${s.accuracy == null ? "—" : s.accuracy + "%"} accuracy · ${s.mistakes} in the notebook</span></div>`;
}
function renderAmendments() {
  const el = $("#amendList");
  if (!el) return;
  el.innerHTML = AMENDMENTS_DATA.map(a => `
    <div class="schema-row" style="align-items:flex-start">
      <b>${esc(a.date)}</b>
      <span><b>${esc(a.instrument)}</b><br>${esc(a.effect)}
        <div class="pill-row">${(a.figures || []).map(f => `<span class="pill warn">${esc(f)}</span>`).join("")}</div>
        <br><span style="color:var(--ink-muted);font-size:.8rem">${esc(a.why)}</span></span>
    </div>`).join("");
}
function updateSideProgress() {
  const s = stats();
  const el = $("#sideProgressPercent");
  if (el) {
    el.textContent = s.coverage + "%";
    $("#sideProgressFill").style.width = s.coverage + "%";
    $("#sideProgressText").textContent = `${s.seen} / ${PAY_DATA.length} questions seen`;
  }
  $$("[data-count]").forEach(n => {
    const k = n.dataset.count;
    if (k === "pay") n.textContent = PAY_DATA.length;
    if (k === "num") n.textContent = PAY_DATA.filter(q => q.section === "NUM").length;
    if (k === "rules") n.textContent = RULES_DATA.length;
    if (k === "papers") n.textContent = PAPERS.length;
  });
}
function exportProgress() {
  const blob = new Blob([JSON.stringify({
    platform: "CCS (Revised Pay) Rules, 2016", exported: new Date().toISOString(),
    answers: STATE.answers, bookmarks: STATE.bookmarks, mistakes: STATE.mistakes,
    mockResults: STATE.mockResults
  }, null, 1)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "ccs-revised-pay-progress.json";
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000);
}
function importProgress(ev) {
  const f = ev.target.files && ev.target.files[0];
  if (!f) return;
  const r = new FileReader();
  r.onload = () => {
    try {
      const d = JSON.parse(r.result);
      if (d.answers) for (const k in d.answers) if (PAY_MAP[k]) STATE.answers[k] = d.answers[k];
      if (Array.isArray(d.bookmarks)) STATE.bookmarks = d.bookmarks.filter(k => PAY_MAP[k]);
      if (Array.isArray(d.mistakes)) STATE.mistakes = d.mistakes.filter(k => PAY_MAP[k]);
      if (Array.isArray(d.mockResults)) STATE.mockResults = d.mockResults.slice(-40);
      save(); renderDashboard(); updateSideProgress();
      alert("Progress imported.");
    } catch (e) { alert("That file could not be read as a progress backup."); }
  };
  r.readAsText(f);
}
function resetEverything() {
  if (!confirm("Clear every answer, bookmark and mock result kept in this browser?")) return;
  STATE.answers = {}; STATE.bookmarks = []; STATE.mistakes = []; STATE.mockResults = [];
  save(); renderDashboard(); updateSideProgress();
  alert("Cleared.");
}

/* ==========================================================================
   BOOT
   ========================================================================== */
function boot() {
  load();
  applyTheme(STATE.prefs.theme || "light");
  const ruleSel = $("#bankRule");
  if (ruleSel) {
    ruleSel.innerHTML = `<option value="ALL">All seventeen rules</option>` +
      RULE_NOS.map(no => `<option value="${no}">Rule ${no} — ${esc((RULES_MAP[no].title || "").slice(0, 60))}</option>`).join("");
  }
  const chSel = $("#ruleChapter");
  if (chSel) {
    chSel.innerHTML = `<option value="ALL">All chapters</option>` +
      CHAPTERS_DATA.map(c => `<option value="${esc(c.no != null ? c.no : c.id)}">${esc(c.title || c.name || c.no)}</option>`).join("");
  }
  const fromSel = $("#labPromFrom"), toSel = $("#labPromTo");
  const lvOpts = MATRIX_DATA.levels.map(l => `<option value="${l}">Level ${l}</option>`).join("");
  if (fromSel) { fromSel.innerHTML = lvOpts; fromSel.value = "4"; }
  if (toSel) { toSel.innerHTML = lvOpts; toSel.value = "5"; }
  const incSel = $("#labIncLevel"), fitSel = $("#labLevel");
  if (incSel) { incSel.innerHTML = lvOpts; incSel.value = "4"; }
  if (fitSel) { fitSel.innerHTML = lvOpts; fitSel.value = "4"; }
  const gpSel = $("#labGP");
  if (gpSel) {
    const gps = [...new Set(MATRIX_DATA.levels.map(l => MATRIX_DATA.grade_pay[l]).filter(g => g && /^\d+$/.test(g)))];
    gpSel.innerHTML = gps.map(g => `<option value="${g}">₹${g}</option>`).join("");
    gpSel.value = "2400";
  }
  updateSideProgress();
  renderDashboard();
  $$(".nav-btn[data-view]").forEach(b => b.addEventListener("click", () => switchView(b.dataset.view)));
  $$("input[type=search]").forEach(i => i.addEventListener("input", () => {
    if (i.id === "bankSearch") bankFilters();
    if (i.id === "ruleSearch") ruleFilters();
    if (i.id === "numSearch") numSearch();
  }));
}
document.addEventListener("DOMContentLoaded", boot);

/* a handle for the test harness (and for anyone who opens the console) */
window.__CCSRP = {
  get PAY_DATA() { return PAY_DATA; }, get MATRIX_DATA() { return MATRIX_DATA; },
  get RULES_DATA() { return RULES_DATA; }, get CHAPTERS_DATA() { return CHAPTERS_DATA; },
  get PAY_MAP() { return PAY_MAP; }, get PAPERS() { return PAPERS; },
  get STATE() { return STATE; }
};
