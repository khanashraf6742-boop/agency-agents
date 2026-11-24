"use strict";
/* ============================================================================
   CCS (Leave) Rules, 1972 — study and practice engine
   Vanilla JS, single file, no dependencies, no network calls.
   Data is injected before this script runs:
     RULES_DATA, MCQS_DATA, FLASHCARDS_DATA, MODULES_DATA, MOCK_TESTS_DATA,
     TABLES_DATA, CASES_DATA, FORMS_DATA, AMENDMENTS_DATA, CORE_DATA
   ========================================================================== */

const MCQS_MAP = {};
MCQS_DATA.forEach(m => { MCQS_MAP[m.id] = m; });
const NUM80_MAP = {};
NUM80_DATA.forEach(m => { NUM80_MAP[m.id] = m; MCQS_MAP[m.id] = m; });

const LS_KEY = "ccslr1972-state-v1";
const STATE = {
  answers: {},          // mcqId -> { chosen, correct, ts }
  bookmarks: [],        // mcqIds
  mistakes: [],         // mcqIds
  flashcards: {},       // fcId -> box (1..5)
  mockResults: [],      // { mockId, score, total, at, perQ }
  prefs: { theme: "light", showHinglish: true, explanations: "full" },
  mcq: { page: 1, pageSize: 12, chapter: "ALL", difficulty: "ALL", filter: "ALL", search: "" },
  num80: { block: "ALL", filter: "ALL", attempts: 0, correct: 0 },
  fc: { index: 0, category: "ALL", flipped: false },
  mock: null,
  view: "dash"
};

/* ------------------------------------------------------------------ storage */
function save() {
  try {
    localStorage.setItem(LS_KEY, JSON.stringify({
      answers: STATE.answers, bookmarks: STATE.bookmarks, mistakes: STATE.mistakes,
      flashcards: STATE.flashcards, mockResults: STATE.mockResults, prefs: STATE.prefs,
      mcqPageSize: STATE.mcq.pageSize
    }));
  } catch (e) { /* storage full or blocked — the app still works in memory */ }
}
function load() {
  let raw = null;
  try { raw = localStorage.getItem(LS_KEY); } catch (e) { raw = null; }
  if (!raw) return;
  let d;
  try { d = JSON.parse(raw); } catch (e) { return; }
  if (!d || typeof d !== "object") return;
  if (d.answers && typeof d.answers === "object") {
    for (const k in d.answers) {
      if (MCQS_MAP[k] && d.answers[k] && typeof d.answers[k] === "object") STATE.answers[k] = d.answers[k];
    }
  }
  if (Array.isArray(d.bookmarks)) STATE.bookmarks = d.bookmarks.filter(k => MCQS_MAP[k]);
  if (Array.isArray(d.mistakes)) STATE.mistakes = d.mistakes.filter(k => MCQS_MAP[k]);
  if (d.flashcards && typeof d.flashcards === "object") {
    const ids = new Set(FLASHCARDS_DATA.map(c => c.id));
    for (const k in d.flashcards) if (ids.has(k)) STATE.flashcards[k] = d.flashcards[k];
  }
  if (Array.isArray(d.mockResults)) STATE.mockResults = d.mockResults.slice(-60);
  if (d.prefs && typeof d.prefs === "object") Object.assign(STATE.prefs, d.prefs);
  if (Number.isFinite(d.mcqPageSize)) STATE.mcq.pageSize = Math.min(50, Math.max(6, d.mcqPageSize));
}

/* ------------------------------------------------------------------ helpers */
const $ = sel => document.querySelector(sel);
const $$ = sel => Array.from(document.querySelectorAll(sel));
const LETTERS = "ABCD";
function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, c =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}
function chapters() {
  const seen = new Map();
  MCQS_DATA.forEach(m => { if (!seen.has(m.chapter)) seen.set(m.chapter, m.chapter_title); });
  return Array.from(seen.entries());
}
function pct(a, b) { return b ? Math.round((a / b) * 100) : 0; }
function ruleLabel(rule) {
  if (rule === "FS") return "First Schedule";
  if (rule === 0 || rule === "0") return "Not in the Rules";
  return "Rule " + rule;
}
function todayKey() { return new Date().toISOString().slice(0, 10); }

/* ------------------------------------------------------------------ theme */
function applyTheme(t) {
  document.documentElement.setAttribute("data-theme", t);
  STATE.prefs.theme = t;
  const b = $("#btnTheme");
  if (b) b.textContent = t === "dark" ? "☀ Light" : "🌙 Dark";
}
function toggleTheme() {
  applyTheme(STATE.prefs.theme === "dark" ? "light" : "dark");
  save();
}

/* ------------------------------------------------------------------ routing */
function switchView(v) {
  STATE.view = v;
  $$(".view-panel").forEach(p => p.classList.toggle("active", p.id === "view-" + v));
  $$(".nav-btn").forEach(b => {
    const on = b.dataset.view === v;
    b.classList.toggle("active", on);
    if (on) b.setAttribute("aria-current", "page"); else b.removeAttribute("aria-current");
  });
  const main = $("#main-content");
  if (main) main.scrollTop = 0;
  window.scrollTo({ top: 0, behavior: "instant" in window ? "instant" : "auto" });
  if (v === "dash") renderDashboard();
  if (v === "rules") renderRules();
  if (v === "modules") renderModules();
  if (v === "mcqs") renderMcqs();
  if (v === "num80") renderNum80();
  if (v === "flashcards") renderFlashcard();
  if (v === "mock") renderMockList();
  if (v === "tables") renderTables();
  if (v === "cases") renderCases();
  if (v === "forms") renderForms();
  if (v === "amendments") renderAmendments();
  if (v === "core") renderCore();
  if (v === "lab") renderLab();
  if (v === "mistakes") renderMistakes();
  if (v === "settings") renderSettings();
}

/* ------------------------------------------------------------------ dashboard */
function stats() {
  const attempted = Object.keys(STATE.answers).length;
  const correct = Object.values(STATE.answers).filter(a => a.correct).length;
  const mastered = Object.values(STATE.flashcards).filter(b => b >= 4).length;
  return { attempted, correct, mastered, total: MCQS_DATA.length };
}
function renderDashboard() {
  const s = stats();
  const acc = s.attempted ? pct(s.correct, s.attempted) : 0;
  const cover = pct(s.attempted, s.total);
  const best = STATE.mockResults.reduce((b, r) => Math.max(b, pct(r.score, r.total)), 0);
  $("#dashAttempted").textContent = s.attempted.toLocaleString();
  $("#dashAccuracy").textContent = s.attempted ? acc + "%" : "—";
  $("#dashCoverage").textContent = cover + "%";
  $("#dashMistakes").textContent = STATE.mistakes.length;
  $("#dashMastered").textContent = s.mastered + " / " + FLASHCARDS_DATA.length;
  $("#dashMockBest").textContent = best ? best + "%" : "—";
  $("#dashProgressFill").style.width = cover + "%";
  $("#dashRing").style.setProperty("--p", cover + "%");
  $("#dashRingLabel").textContent = cover + "%";
  const hour = new Date().getHours();
  $("#dashGreeting").textContent = hour < 12 ? "Good morning" : hour < 17 ? "Good afternoon" : "Good evening";

  // chapter table
  const rows = chapters().map(([ch, title]) => {
    const all = MCQS_DATA.filter(m => m.chapter === ch);
    const att = all.filter(m => STATE.answers[m.id]);
    const cor = att.filter(m => STATE.answers[m.id].correct);
    const tags = Array.from(new Set(all.map(m => m.tag)));
    return `<tr>
      <td><b>${esc(ch)}</b></td>
      <td>${esc(title)}</td>
      <td>${all.length}</td>
      <td>${att.length}</td>
      <td>${att.length ? pct(cor.length, att.length) + "%" : "—"}</td>
      <td>${esc(tags.join(", "))}</td>
      <td><button class="btn-secondary" style="padding:2px 8px;font-size:.75rem"
           onclick="jumpToChapter('${esc(ch)}')">Practise</button></td>
    </tr>`;
  }).join("");
  $("#dashChapterRows").innerHTML = rows || `<tr><td colspan="7">No data</td></tr>`;

  const weak = chapters().map(([ch, title]) => {
    const all = MCQS_DATA.filter(m => m.chapter === ch);
    const att = all.filter(m => STATE.answers[m.id]);
    const cor = att.filter(m => STATE.answers[m.id].correct);
    return { ch, title, n: att.length, acc: att.length ? pct(cor.length, att.length) : null };
  }).filter(x => x.n >= 3).sort((a, b) => a.acc - b.acc).slice(0, 3);
  $("#dashRecommendation").innerHTML = weak.length
    ? `Your weakest chapters so far: ` + weak.map(w =>
        `<b>${esc(w.ch)}</b> (${w.acc}% over ${w.n})`).join(", ") +
      `. Start a focused set there, or open the mistake notebook if you want the exact questions.`
    : `Nothing attempted yet. Begin with <b>Rule 26</b> and <b>Rule 39</b> — they carry the most marks — or take the twenty-five-question mixed drill.`;
  const recent = STATE.mockResults.slice(-3).reverse();
  $("#dashRecentMocks").innerHTML = recent.length ? recent.map(r => {
    const t = MOCK_TESTS_DATA.find(m => m.id === r.mockId);
    return `<div class="worked-step"><span class="ws-k">${esc(t ? t.title : r.mockId)}</span>
      <span class="ws-v">${r.score}/${r.total} · ${pct(r.score, r.total)}%</span></div>`;
  }).join("") : `<div class="empty-state">No mock test taken yet.</div>`;
}
function jumpToChapter(ch) {
  STATE.mcq.chapter = ch; STATE.mcq.page = 1; STATE.mcq.filter = "ALL";
  switchView("mcqs");
  const sel = $("#mcqChapter");
  if (sel) sel.value = ch;
}

/* ------------------------------------------------------------------ rules */
function renderRules() {
  const q = ($("#ruleSearch").value || "").toLowerCase().trim();
  const ch = $("#ruleChapter").value;
  const box = $("#rulesList");
  const list = RULES_DATA.filter(r => {
    if (ch !== "ALL" && String(r.chapter) !== ch) return false;
    if (!q) return true;
    return (r.title + " " + r.statutory_text + " " + r.summary + " " + r.hinglish +
            " " + r.traps + " " + r.conditions.join(" ")).toLowerCase().includes(q);
  });
  $("#ruleCount").textContent = list.length + " of " + RULES_DATA.length + " rule cards";
  box.innerHTML = list.map(r => {
    const num = String(r.rule);
    const conds = r.conditions.map(c => `<li>${esc(c)}</li>`).join("");
    const exc = r.exceptions.map(c => `<li>${esc(c)}</li>`).join("");
    return `<article class="rule-card" id="rule-card-${esc(num)}">
      <div class="rule-card-hd" onclick="toggleRule('${esc(num)}')">
        <span class="rule-num-badge">${esc(num)}</span>
        <div style="flex:1">
          <div class="rule-title">${esc(r.title)}</div>
          <div class="rule-ch-tag">Chapter ${esc(r.chapter)} — ${esc(r.chapter_title)}</div>
        </div>
        <button class="btn-secondary" style="padding:3px 9px;font-size:.75rem">Open</button>
      </div>
      <div class="rule-summary">${esc(r.summary)}</div>
      <div class="rule-details" id="rule-details-${esc(num)}">
        <div class="rule-statutory-box"><b>${r.verbatim ? "Statutory text" : "Key provisions"}.</b>${r.verbatim ? "" : ` <span style="color:#b45309;font-weight:600">Not yet checked against the consolidated edition &mdash; do not quote this as the section.</span>`}<div style="white-space:pre-wrap;margin-top:6px">${esc(r.statutory_text)}</div></div>
        ${STATE.prefs.showHinglish ? `<div class="rule-hinglish"><b>Hinglish.</b> ${esc(r.hinglish)}</div>` : ""}
        <div class="rule-props">
          <div class="rule-prop"><b>Authority</b>${esc(r.authority || "—")}</div>
          <div class="rule-prop"><b>Time limit / figure</b>${esc(r.time_limit || "—")}</div>
          <div class="rule-prop"><b>Forms</b>${esc(r.forms || "—")}</div>
          <div class="rule-prop"><b>Cross-references</b>${esc(r.cross_refs || "—")}</div>
        </div>
        <div class="rule-props" style="margin-top:10px">
          <div class="rule-prop"><b>Requirements</b><ul style="margin:6px 0 0 16px">${conds || "<li>—</li>"}</ul></div>
          <div class="rule-prop"><b>Exceptions</b><ul style="margin:6px 0 0 16px">${exc || "<li>—</li>"}</ul></div>
        </div>
        <div class="danger-note"><b>Exam trap.</b> ${esc(r.traps || "—")}</div>
        <div class="pill-row">
          <span class="pill">${MCQS_DATA.filter(m => String(m.rule) === num).length} questions mapped</span>
          ${num === "3" ? `<span class="pill">2 more on the First Schedule</span>` : ""}
          <button class="btn-secondary" style="padding:2px 9px;font-size:.75rem"
            onclick="practiseRule('${esc(num)}')">Practise this rule</button>
        </div>
      </div>
    </article>`;
  }).join("") || `<div class="empty-state">No rule matches that filter.</div>`;
}
function toggleRule(num) {
  const el = $("#rule-details-" + num);
  if (el) el.classList.toggle("open");
}
function practiseRule(num) {
  STATE.mcq.chapter = "ALL"; STATE.mcq.filter = "RULE:" + num; STATE.mcq.page = 1;
  switchView("mcqs");
}
function expandAllRules() { $$(".rule-details").forEach(d => d.classList.add("open")); }
function collapseAllRules() { $$(".rule-details").forEach(d => d.classList.remove("open")); }

/* ------------------------------------------------------------------ modules */
function renderModules() {
  $("#modulesList").innerHTML = MODULES_DATA.map(m => `
    <article class="rule-card">
      <div class="rule-card-hd">
        <span class="rule-num-badge">${m.id}</span>
        <div style="flex:1">
          <div class="rule-title">${esc(m.title)}</div>
          <div class="rule-ch-tag">${esc(m.rules)}</div>
        </div>
      </div>
      <div class="rule-summary">${esc(m.summary)}</div>
      <div class="rule-props" style="margin-top:10px">
        <div class="rule-prop"><b>Key facts</b><ul style="margin:6px 0 0 16px">
          ${m.key_facts.map(k => `<li>${esc(k)}</li>`).join("")}</ul></div>
        <div class="rule-prop"><b>Mnemonic</b><span class="rule-figure">${esc(m.mnemonics)}</span></div>
      </div>
      ${m.traps ? `<div class="danger-note"><b>Traps.</b> ${esc(m.traps)}</div>` : ""}
    </article>`).join("");
}

/* ------------------------------------------------------------------ MCQs */
function currentMcqList() {
  let list = MCQS_DATA.slice();
  const c = STATE.mcq;
  if (c.chapter !== "ALL") list = list.filter(m => m.chapter === c.chapter);
  if (c.difficulty !== "ALL") list = list.filter(m => m.tag === c.difficulty);
  if (c.filter === "MISTAKES") list = list.filter(m => STATE.mistakes.includes(m.id));
  if (c.filter === "BOOKMARKS") list = list.filter(m => STATE.bookmarks.includes(m.id));
  if (c.filter === "UNSEEN") list = list.filter(m => !STATE.answers[m.id]);
  if (c.filter.startsWith("RULE:")) {
    const rn = c.filter.slice(5);
    list = list.filter(m => String(m.rule) === rn);
  }
  if (c.filter.startsWith("MOCK:")) {
    const mk = MOCK_TESTS_DATA.find(m => m.id === c.filter.slice(5));
    if (mk) {
      const ids = new Set(mk.question_ids);
      list = MCQS_DATA.concat(NUM80_DATA).filter(m => ids.has(m.id));
    }
  }
  if (c.search) {
    const q = c.search.toLowerCase();
    list = list.filter(m => (m.id + " " + m.stem + " " + m.topic + " " + m.expl).toLowerCase().includes(q));
  }
  return list;
}
function renderMcqs() {
  const list = currentMcqList();
  const c = STATE.mcq;
  const pages = Math.max(1, Math.ceil(list.length / c.pageSize));
  if (c.page > pages) c.page = pages;
  const slice = list.slice((c.page - 1) * c.pageSize, c.page * c.pageSize);
  $("#mcqCount").textContent = list.length.toLocaleString() + " questions in this set";
  $("#mcqScope").textContent = describeScope();
  $("#mcqList").innerHTML = slice.length ? slice.map(m => mcqCard(m)).join("")
    : `<div class="empty-state">No question matches this set. Clear the filters or pick another chapter.</div>`;
  $("#mcqPager").innerHTML = pages > 1 ? `
    <button class="btn-secondary" ${c.page === 1 ? "disabled" : ""} onclick="mcqPage(-1)">← Previous</button>
    <span class="fc-progress">Page ${c.page} of ${pages}</span>
    <button class="btn-secondary" ${c.page === pages ? "disabled" : ""} onclick="mcqPage(1)">Next →</button>` : "";
}
function describeScope() {
  const c = STATE.mcq;
  const bits = [];
  bits.push(c.chapter === "ALL" ? "all chapters" : "chapter " + c.chapter);
  if (c.difficulty !== "ALL") bits.push("difficulty " + c.difficulty);
  if (c.filter === "MISTAKES") bits.push("mistake notebook only");
  if (c.filter === "BOOKMARKS") bits.push("bookmarked only");
  if (c.filter === "UNSEEN") bits.push("not yet attempted");
  if (c.filter.startsWith("RULE:")) bits.push("rule " + c.filter.slice(5) + " only");
  if (c.filter.startsWith("MOCK:")) bits.push("mock " + c.filter.slice(5));
  if (c.search) bits.push(`search "${c.search}"`);
  return "Showing " + bits.join(" · ");
}
function mcqCard(m) {
  const a = STATE.answers[m.id];
  const chosen = a ? a.chosen : null;
  const showExpl = !!a;
  const bookmarked = STATE.bookmarks.includes(m.id);
  const opts = m.opts.map((o, i) => {
    const L = LETTERS[i];
    let cls = "mcq-opt";
    if (a) {
      if (L === m.ans) cls += " correct";
      else if (L === chosen) cls += " incorrect";
    }
    return `<button class="${cls}" onclick="answerMcq('${esc(m.id)}','${L}')"
      aria-pressed="${chosen === L}">
      <span class="opt-letter">${L}</span><span class="opt-text">${esc(o)}</span></button>`;
  }).join("");
  const tagCls = m.tag.replace(/\s+/g, "");
  return `<article class="mcq-card" id="mcq-${esc(m.id)}">
    <div class="mcq-hd">
      <span class="mcq-id">${esc(m.id)}</span>
      <span class="mcq-tag ${esc(tagCls)}">${esc(m.tag)}</span>
      <span class="mcq-tag Topic">${esc(ruleLabel(m.rule))}</span>
      <span class="mcq-tag Topic">${esc(m.chapter)}</span>
      <button class="copy-btn" onclick="toggleBookmark('${esc(m.id)}')"
        title="Bookmark this question">${bookmarked ? "★ Bookmarked" : "☆ Bookmark"}</button>
    </div>
    <div class="mcq-stem">${esc(m.stem)}</div>
    <div class="mcq-opts">${opts}</div>
    ${showExpl ? `<div class="mcq-expl open"><div class="mcq-expl-hd">Explanation — ${a.correct ? "correct" : "review this"}</div>
      <div class="mcq-expl-text" style="white-space:pre-wrap">${esc(m.expl)}</div>
      <div class="mcq-src">${esc(m.src)}</div></div>` : ""}
    <div class="mcq-actions">
      ${a ? `<button class="mcq-act-btn" onclick="resetMcq('${esc(m.id)}')">↺ Try again</button>` : ""}
      ${!a ? `<button class="mcq-act-btn" onclick="revealMcq('${esc(m.id)}')">Reveal answer</button>` : ""}
      <span class="pill">Topic: ${esc(m.topic)}</span>
      ${m.trap ? `<span class="pill warn">Trap: ${esc(m.trap)}</span>` : ""}
    </div>
  </article>`;
}
function answerMcq(id, letter) {
  if (STATE.answers[id]) return;
  const m = MCQS_MAP[id];
  const correct = letter === m.ans;
  STATE.answers[id] = { chosen: letter, correct, ts: Date.now() };
  if (!correct) {
    if (!STATE.mistakes.includes(id)) STATE.mistakes.push(id);
  } else {
    STATE.mistakes = STATE.mistakes.filter(x => x !== id);
  }
  save();
  const card = document.getElementById("mcq-" + id);
  if (card) card.outerHTML = mcqCard(m);
  updateSideProgress();
}
function revealMcq(id) {
  const m = MCQS_MAP[id];
  STATE.answers[id] = { chosen: null, correct: false, ts: Date.now(), revealed: true };
  if (!STATE.mistakes.includes(id)) STATE.mistakes.push(id);
  save();
  const card = document.getElementById("mcq-" + id);
  if (card) card.outerHTML = mcqCard(m);
  updateSideProgress();
}
function resetMcq(id) {
  delete STATE.answers[id];
  STATE.mistakes = STATE.mistakes.filter(x => x !== id);
  save();
  const card = document.getElementById("mcq-" + id);
  if (card) card.outerHTML = mcqCard(MCQS_MAP[id]);
  updateSideProgress();
}
function toggleBookmark(id) {
  if (STATE.bookmarks.includes(id)) STATE.bookmarks = STATE.bookmarks.filter(x => x !== id);
  else STATE.bookmarks.push(id);
  save();
  renderMcqs();
}
function mcqPage(d) {
  STATE.mcq.page += d;
  renderMcqs();
  window.scrollTo({ top: 0, behavior: "smooth" });
}
function applyMcqFilters() {
  STATE.mcq.chapter = $("#mcqChapter").value;
  STATE.mcq.difficulty = $("#mcqDifficulty").value;
  STATE.mcq.search = $("#mcqSearch").value.trim();
  STATE.mcq.page = 1;
  renderMcqs();
}
function setMcqFilter(f) {
  STATE.mcq.filter = f;
  STATE.mcq.page = 1;
  $$(".mcq-act-btn[data-filter]").forEach(b => b.classList.toggle("active", b.dataset.filter === f));
  renderMcqs();
}
function shuffleSet() {
  const list = currentMcqList();
  for (let i = list.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [list[i], list[j]] = [list[j], list[i]];
  }
  STATE.mcq.page = 1;
  renderMcqs();
}
function updateSideProgress() {
  const s = stats();
  const p = pct(s.attempted, s.total);
  $("#sideProgressPercent").textContent = p + "%";
  $("#sideProgressFill").style.width = p + "%";
  $("#sideProgressText").textContent = s.attempted.toLocaleString() + " / " + s.total.toLocaleString() + " practised";
}

/* ------------------------------------------------------------------ numerical 80 */
function num80Blocks() {
  return Array.from(new Set(NUM80_DATA.map(m => m.topic.split(" — worked")[0])));
}
function num80Steps(m) {
  const t = m.expl;
  return t.slice(t.indexOf("Worked solution") , t.indexOf("Where the other options come from"));
}
function renderNum80() {
  const c = STATE.num80;
  let list = NUM80_DATA.slice();
  if (c.block !== "ALL") list = list.filter(m => m.topic.split(" — worked")[0] === c.block);
  if (c.filter === "UNSEEN") list = list.filter(m => !STATE.answers[m.id]);
  if (c.filter === "MISTAKES") list = list.filter(m => STATE.mistakes.includes(m.id));
  $("#num80Count").textContent = list.length + " of " + NUM80_DATA.length + " questions";
  const done = NUM80_DATA.filter(m => STATE.answers[m.id] && STATE.answers[m.id].chosen).length;
  const right = NUM80_DATA.filter(m => STATE.answers[m.id] && STATE.answers[m.id].correct).length;
  $("#num80Score").textContent = done ? `attempted ${done} · right ${right} · ${Math.round(right / done * 100)}%` : "not started";
  const open = c.filter === "STEPS";
  $("#num80List").innerHTML = list.length ? list.map((m, i) => {
    const a = STATE.answers[m.id];
    const shown = open || !!a;
    const opts = m.opts.map((o, k) => {
      const L = LETTERS[k];
      let cls = "mcq-opt";
      if (shown) {
        if (L === m.ans) cls += " correct";
        else if (a && a.chosen === L) cls += " incorrect";
      }
      return `<button class="${cls}" onclick="answerNum80('${esc(m.id)}','${L}')">
        <span class="opt-letter">${L}</span><span class="opt-text">${esc(o)}</span></button>`;
    }).join("");
    return `<article class="mcq-card" id="num80-${esc(m.id)}">
      <div class="mcq-hd">
        <span class="mcq-id">${esc(m.id)}</span>
        <span class="mcq-tag ${esc(m.tag.replace(/\s+/g, ""))}">${esc(m.tag)}</span>
        <span class="mcq-tag Topic">${esc(ruleLabel(m.rule))}</span>
        <span class="mcq-tag Topic">${esc(m.topic.split(" — worked")[0])}</span>
      </div>
      <div class="mcq-stem">${esc(m.stem)}</div>
      <div class="mcq-opts">${opts}</div>
      ${shown ? `<div class="mcq-expl open"><div class="mcq-expl-hd">Worked solution</div>
        <div class="mcq-expl-text" style="white-space:pre-wrap">${esc(m.expl)}</div>
        <div class="mcq-src">${esc(m.src)}</div></div>`
        : `<div class="mcq-actions"><button class="mcq-act-btn" onclick="revealNum80('${esc(m.id)}')">Show the worked solution</button></div>`}
    </article>`;
  }).join("") : `<div class="empty-state">No question in this block matches the filter.</div>`;
}
function answerNum80(id, L) {
  const m = NUM80_MAP[id];
  if (STATE.answers[id]) return;
  const correct = L === m.ans;
  STATE.answers[id] = { chosen: L, correct, ts: Date.now() };
  STATE.num80.attempts = (STATE.num80.attempts || 0) + 1;
  if (correct) STATE.num80.correct = (STATE.num80.correct || 0) + 1;
  if (!correct && !STATE.mistakes.includes(id)) STATE.mistakes.push(id);
  if (correct) STATE.mistakes = STATE.mistakes.filter(x => x !== id);
  save();
  if (document.querySelector("#num80List .mcq-id") &&
      document.querySelector("#num80List .mcq-id").textContent === "SELF-TEST") {
    // in a self-test just recolour the chosen card, leaving the ten on screen
    const card = document.getElementById("num80-" + id);
    if (card) card.querySelectorAll(".mcq-opt").forEach(b => {
      const L2 = b.querySelector(".opt-letter").textContent;
      b.classList.toggle("correct", L2 === m.ans);
      b.classList.toggle("incorrect", L2 === L && !correct);
    });
    const done = NUM80_DATA.filter(x => STATE.answers[x.id] && STATE.answers[x.id].chosen &&
                                        STATE.answers[x.id].ts > Date.now() - 6e5).length;
    $("#num80Score").textContent = "answers marked on the spot";
  } else {
    renderNum80();
  }
  updateSideProgress();
}
function revealNum80(id) {
  STATE.answers[id] = { chosen: null, correct: false, ts: Date.now(), revealed: true };
  if (!STATE.mistakes.includes(id)) STATE.mistakes.push(id);
  save();
  renderNum80();
}
function setNum80(f) {
  STATE.num80.filter = f;
  $$(".mcq-act-btn[data-n80]").forEach(b => b.classList.toggle("active", b.dataset.n80 === f));
  renderNum80();
}
function selfTestNum80() {
  // ten unseen questions at random; if fewer than ten are unseen, fill from the whole set
  let pool = NUM80_DATA.filter(m => !STATE.answers[m.id]);
  if (pool.length < 10) pool = NUM80_DATA.slice();
  const pick = pool.slice().sort(() => Math.random() - 0.5).slice(0, 10);
  STATE.num80.filter = "ALL";
  STATE.num80.block = "ALL";
  switchView("num80");
  $("#num80List").innerHTML = pick.map(m => {
    const opts = m.opts.map((o, k) =>
      `<button class="mcq-opt" onclick="answerNum80('${esc(m.id)}','${LETTERS[k]}')">
        <span class="opt-letter">${LETTERS[k]}</span><span class="opt-text">${esc(o)}</span></button>`).join("");
    return `<article class="mcq-card" id="num80-${esc(m.id)}">
      <div class="mcq-hd"><span class="mcq-id">SELF-TEST</span>
        <span class="mcq-tag ${esc(m.tag.replace(/\s+/g, ""))}">${esc(m.tag)}</span>
        <span class="mcq-tag Topic">${esc(m.topic.split(" — worked")[0])}</span></div>
      <div class="mcq-stem">${esc(m.stem)}</div>
      <div class="mcq-opts">${opts}</div></article>`;
  }).join("") + `<div class="tip-note" style="margin-top:6px"><b>Score ten.</b> The answers are marked as you go;
    open the full Numerical 80 page afterwards to read the working for anything you missed.</div>`;
  $("#num80Count").textContent = "self-test: 10 questions";
  $("#num80Score").textContent = "answers marked on the spot";
}

function exportNum80() {
  const rows = ["CCS (LEAVE) RULES, 1972 — THE NUMERICAL 80", "Stepwise solutions", ""];
  let block = "";
  NUM80_DATA.forEach((m, i) => {
    const b = m.topic.split(" — worked")[0];
    if (b !== block) { block = b; rows.push("", "=".repeat(70), b.toUpperCase(), "=".repeat(70), ""); }
    rows.push(`Q${i + 1}. ${m.stem}`);
    m.opts.forEach((o, k) => rows.push(`    ${LETTERS[k]}) ${o}`));
    rows.push(`Answer: ${m.ans}`, "");
    rows.push(m.expl, "", "-".repeat(70), "");
  });
  const blob = new Blob([rows.join("\n")], { type: "text/plain;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "CCS-Leave-Numerical-80-with-solutions.txt";
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 2000);
}

/* ------------------------------------------------------------------ flashcards */
function flashcardList() {
  const c = STATE.fc;
  return c.category === "ALL" ? FLASHCARDS_DATA : FLASHCARDS_DATA.filter(f => f.category === c.category);
}
function renderFlashcard() {
  const list = flashcardList();
  if (!list.length) { $("#fcBody").innerHTML = `<div class="empty-state">No cards in this category.</div>`; return; }
  if (STATE.fc.index >= list.length) STATE.fc.index = 0;
  const card = list[STATE.fc.index];
  const box = STATE.flashcards[card.id] || 1;
  $("#fcCat").textContent = card.category;
  $("#fcRule").textContent = card.rule ? "Rule " + card.rule : "All rules";
  $("#fcFront").textContent = card.front;
  $("#fcBack").textContent = card.back;
  $("#fcExpl").textContent = card.expl || "";
  $("#fcSource").textContent = card.src || "";
  $("#fcMnemonic").textContent = card.mnemonic || "";
  $("#fcBackDetails").classList.toggle("open", STATE.fc.flipped);
  $("#fcProgress").textContent = `Card ${STATE.fc.index + 1} of ${list.length} · box ${box}`;
  const flipBtn = $("#fcFlipBtn");
  if (flipBtn) flipBtn.textContent = STATE.fc.flipped ? "Hide answer" : "Show answer";
  renderLeitner();
}
function flipCard() {
  STATE.fc.flipped = !STATE.fc.flipped;
  renderFlashcard();
}
function nextCard() {
  const list = flashcardList();
  STATE.fc.index = (STATE.fc.index + 1) % list.length;
  STATE.fc.flipped = false;
  renderFlashcard();
}
function prevCard() {
  const list = flashcardList();
  STATE.fc.index = (STATE.fc.index - 1 + list.length) % list.length;
  STATE.fc.flipped = false;
  renderFlashcard();
}
function rateCard(box) {
  const list = flashcardList();
  const card = list[STATE.fc.index];
  STATE.flashcards[card.id] = box;
  save();
  nextCard();
}
function renderLeitner() {
  const counts = [0, 0, 0, 0, 0];
  FLASHCARDS_DATA.forEach(c => { const b = STATE.flashcards[c.id] || 1; counts[b - 1]++; });
  const due = FLASHCARDS_DATA.filter(c => (STATE.flashcards[c.id] || 1) === 1).length;
  $("#leitnerStats").innerHTML = counts.map((n, i) =>
    `<div class="worked-step"><span class="ws-k">Box ${i + 1} · ${["daily", "every 3 days", "every 7 days", "every 14 days", "mastered"][i]}</span>
     <span class="ws-v">${n}</span></div>`).join("") +
    `<div class="tip-note" style="margin-top:10px"><b>${due}</b> card(s) sit in box 1 and are due today. Rate a card 1–5 after you flip it.</div>`;
}
function fcCategoryChanged() {
  STATE.fc.category = $("#fcCategory").value;
  STATE.fc.index = 0;
  STATE.fc.flipped = false;
  renderFlashcard();
}

/* ------------------------------------------------------------------ mock tests */
function renderMockList() {
  $("#mockList").innerHTML = MOCK_TESTS_DATA.map(t => {
    const done = STATE.mockResults.filter(r => r.mockId === t.id);
    const best = done.reduce((b, r) => Math.max(b, pct(r.score, r.total)), 0);
    return `<article class="rule-card">
      <div class="rule-card-hd">
        <span class="rule-num-badge">${esc(t.id.replace("MOCK-", ""))}</span>
        <div style="flex:1">
          <div class="rule-title">${esc(t.title)}</div>
          <div class="rule-ch-tag">${esc(t.rules)}</div>
        </div>
      </div>
      <div class="mock-meta">
        <span>${t.q_count} questions</span>
        <span>${t.time_mins} minutes</span>
        <span>${esc(t.tag)}</span>
        ${done.length ? `<span>attempted ${done.length}×</span><span>best ${best}%</span>` : ""}
      </div>
      <div class="pill-row">
        <button class="btn-primary" onclick="startMock('${esc(t.id)}')">Start CBT →</button>
        <button class="btn-secondary" onclick="practiseMock('${esc(t.id)}')">Practise untimed</button>
      </div>
    </article>`;
  }).join("");
}
function practiseMock(id) {
  const t = MOCK_TESTS_DATA.find(m => m.id === id);
  if (t && id === "MOCK-31") {          // the stepwise set lives in its own view
    STATE.num80.block = "ALL";
    STATE.num80.filter = "ALL";
    switchView("num80");
    return;
  }
  STATE.mcq.filter = "MOCK:" + id;
  STATE.mcq.chapter = "ALL";
  STATE.mcq.page = 1;
  switchView("mcqs");
}
function startMock(id) {
  const t = MOCK_TESTS_DATA.find(m => m.id === id);
  if (!t) return;
  STATE.mock = {
    id: t.id, title: t.title, ids: t.question_ids, timeMins: t.time_mins,
    left: t.time_mins * 60, idx: 0, answers: {}, marked: {}, started: Date.now(), timer: null
  };
  $("#mockListScreen").style.display = "none";
  $("#mockExamScreen").style.display = "block";
  $("#cbtTitle").textContent = t.title;
  renderCbt();
  STATE.mock.timer = setInterval(() => {
    STATE.mock.left--;
    const m = Math.floor(STATE.mock.left / 60), s = STATE.mock.left % 60;
    $("#cbtTimer").textContent = `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
    if (STATE.mock.left <= 0) submitMock(true);
  }, 1000);
}
function renderCbt() {
  const st = STATE.mock;
  if (!st) return;
  const m = MCQS_MAP[st.ids[st.idx]];
  $("#cbtQNum").textContent = `Question ${st.idx + 1} of ${st.ids.length}`;
  $("#cbtStem").textContent = m.stem;
  const chosen = st.answers[m.id];
  $("#cbtOpts").innerHTML = m.opts.map((o, i) => {
    const L = LETTERS[i];
    return `<button class="mcq-opt ${chosen === L ? "selected" : ""}" onclick="cbtPick('${L}')">
      <span class="opt-letter">${L}</span><span class="opt-text">${esc(o)}</span></button>`;
  }).join("");
  const mm = Math.floor(st.left / 60), ss = st.left % 60;
  $("#cbtTimer").textContent = `${String(Math.max(0, mm)).padStart(2, "0")}:${String(Math.max(0, ss)).padStart(2, "0")}`;
  const answered = Object.keys(st.answers).length;
  $("#cbtAnswered").textContent = answered + " answered";
  $("#cbtMarked").textContent = Object.keys(st.marked).length + " marked";
  $("#cbtPalette").innerHTML = st.ids.map((id, i) => {
    let cls = "palette-btn";
    if (i === st.idx) cls += " current";
    else if (st.marked[id]) cls += " review";
    else if (st.answers[id]) cls += " ans";
    return `<button class="${cls}" onclick="cbtGo(${i})">${i + 1}</button>`;
  }).join("");
}
function cbtPick(L) {
  const st = STATE.mock;
  const m = MCQS_MAP[st.ids[st.idx]];
  st.answers[m.id] = L;
  renderCbt();
}
function cbtGo(i) {
  STATE.mock.idx = i;
  renderCbt();
}
function cbtNav(d) {
  const st = STATE.mock;
  st.idx = Math.min(st.ids.length - 1, Math.max(0, st.idx + d));
  renderCbt();
}
function cbtMark() {
  const st = STATE.mock;
  const id = st.ids[st.idx];
  if (st.marked[id]) delete st.marked[id]; else st.marked[id] = true;
  renderCbt();
}
function cbtClear() {
  const st = STATE.mock;
  delete st.answers[st.ids[st.idx]];
  renderCbt();
}
function submitMock(auto) {
  const st = STATE.mock;
  if (!st) return;
  if (!auto && !confirm("Submit the paper? Unanswered questions score zero.")) return;
  clearInterval(st.timer);
  let score = 0;
  const perQ = st.ids.map(id => {
    const m = MCQS_MAP[id];
    const chosen = st.answers[id] || null;
    const ok = chosen === m.ans;
    if (ok) score++;
    // record into the practice state as well
    if (!STATE.answers[id] || !ok) {
      STATE.answers[id] = { chosen, correct: ok, ts: Date.now(), mock: st.id };
    }
    if (!ok && !STATE.mistakes.includes(id)) STATE.mistakes.push(id);
    if (ok) STATE.mistakes = STATE.mistakes.filter(x => x !== id);
    return { id, chosen, ans: m.ans, ok };
  });
  STATE.mockResults.push({
    mockId: st.id, score, total: st.ids.length, at: Date.now(), perQ
  });
  save();
  const total = st.ids.length;
  const acc = pct(score, total);
  const spent = Math.round((Date.now() - st.started) / 1000);
  $("#mockScorecard").innerHTML = `
    <div class="dash-hero" style="padding:22px">
      <h3 style="font-size:1.3rem;margin-bottom:6px">${esc(st.title)}</h3>
      <div class="dash-metrics" style="margin-top:14px">
        <div class="metric-card"><div class="lbl">Score</div><div class="val">${score} / ${total}</div></div>
        <div class="metric-card"><div class="lbl">Accuracy</div><div class="val">${acc}%</div></div>
        <div class="metric-card"><div class="lbl">Time used</div><div class="val">${Math.floor(spent / 60)}m ${spent % 60}s</div></div>
        <div class="metric-card"><div class="lbl">Attempted</div><div class="val">${Object.keys(st.answers).length} / ${total}</div></div>
      </div>
      <div class="pill-row" style="margin-top:14px">
        <button class="btn-primary" onclick="retakeMock()">Retake this paper</button>
        <button class="btn-secondary" onclick="backToMockList()">Back to test series</button>
        <button class="btn-secondary" onclick="practiseMock('${esc(st.id)}')">Practise these questions</button>
      </div>
    </div>
    <h3 class="dash-section-heading" style="margin-top:20px">Question-by-question review</h3>
    <div id="mockReviewList"></div>`;
  $("#mockReviewList").innerHTML = perQ.map((r, i) => {
    const m = MCQS_MAP[r.id];
    return `<article class="rule-card">
      <div class="rule-card-hd">
        <span class="rule-num-badge">${i + 1}</span>
        <div style="flex:1"><div class="rule-title" style="font-size:.92rem">${esc(m.topic)}</div>
        <div class="rule-ch-tag">${esc(m.id)} · ${esc(ruleLabel(m.rule))} · ${r.ok ? "correct" : r.chosen ? "incorrect" : "unanswered"}</div></div>
      </div>
      <div class="rule-summary">${esc(m.stem)}</div>
      <div class="worked-steps">
        <div class="worked-step"><span class="ws-k">Your answer</span><span class="ws-v">${r.chosen ? r.chosen + ". " + esc(m.opts[LETTERS.indexOf(r.chosen)]) : "—"}</span></div>
        <div class="worked-step"><span class="ws-k">Correct answer</span><span class="ws-v">${r.ans}. ${esc(m.opts[LETTERS.indexOf(r.ans)])}</span></div>
      </div>
      <div class="mcq-expl open"><div class="mcq-expl-hd">Explanation</div>
        <div class="mcq-expl-text" style="white-space:pre-wrap">${esc(m.expl)}</div>
        <div class="mcq-src">${esc(m.src)}</div></div>
    </article>`;
  }).join("");
  $("#mockExamScreen").style.display = "none";
  $("#mockScoreScreen").style.display = "block";
  renderMockList();
}
function retakeMock() { const id = STATE.mock.id; $("#mockScoreScreen").style.display = "none"; startMock(id); }
function backToMockList() {
  if (STATE.mock && STATE.mock.timer) clearInterval(STATE.mock.timer);
  STATE.mock = null;
  $("#mockScoreScreen").style.display = "none";
  $("#mockExamScreen").style.display = "none";
  $("#mockListScreen").style.display = "block";
  renderMockList();
}
function quitMock() {
  if (!confirm("Leave the paper without submitting?")) return;
  clearInterval(STATE.mock.timer);
  STATE.mock = null;
  $("#mockExamScreen").style.display = "none";
  $("#mockListScreen").style.display = "block";
}

/* ------------------------------------------------------------------ tables */
function renderTables() {
  $("#tablesList").innerHTML = TABLES_DATA.map(t => `
    <article class="rule-card">
      <div class="rule-card-hd">
        <span class="rule-num-badge">${t.id}</span>
        <div style="flex:1"><div class="rule-title" style="font-size:.98rem">${esc(t.title)}</div>
        <div class="rule-ch-tag">${t.rows.length} rows · ${t.headers.length} columns</div></div>
      </div>
      <div class="table-wrap"><table class="mini-table">
        <thead><tr>${t.headers.map(h => `<th>${esc(h)}</th>`).join("")}</tr></thead>
        <tbody>${t.rows.map(r => `<tr>${r.map(c => `<td>${esc(c)}</td>`).join("")}</tr>`).join("")}</tbody>
      </table></div>
      <div class="pill-row"><span class="pill">${esc(t.note)}</span></div>
    </article>`).join("");
}

/* ------------------------------------------------------------------ cases */
function renderCases() {
  $("#casesList").innerHTML = CASES_DATA.map(c => `
    <article class="rule-card">
      <div class="rule-card-hd">
        <span class="rule-num-badge">${c.id}</span>
        <div style="flex:1"><div class="rule-title">${esc(c.title)}</div>
          <div class="rule-ch-tag">${esc(c.file_no)} · ${esc(c.date)}</div></div>
      </div>
      <div class="rule-props">
        <div class="rule-prop"><b>Facts</b>${esc(c.facts)}</div>
        <div class="rule-prop"><b>Issue</b>${esc(c.issue)}</div>
        <div class="rule-prop"><b>Correct action</b>${esc(c.action)}</div>
        <div class="rule-prop"><b>Authority</b>${esc(c.authority)}</div>
      </div>
      <div class="tip-note"><b>Point to carry away.</b> ${esc(c.conclusion)}</div>
      <div class="pill-row"><button class="btn-secondary"
        onclick="openCaseQuestion('${esc(c.ref_id)}')">Open the MCQ version</button></div>
    </article>`).join("");
}
function openCaseQuestion(id) {
  STATE.mcq.chapter = "ALL";
  STATE.mcq.difficulty = "ALL";
  STATE.mcq.filter = "ALL";
  STATE.mcq.page = 1;
  STATE.mcq.search = id;
  switchView("mcqs");
  const box = $("#mcqSearch");
  if (box) box.value = id;
  renderMcqs();
}

/* ------------------------------------------------------------------ forms */
function renderForms() {
  $("#formsList").innerHTML = `
    <div class="table-wrap"><table class="mini-table">
      <thead><tr><th>Form</th><th>Rule</th><th>Title</th><th>Submitted by</th><th>To</th><th>Timing</th><th>Note</th></tr></thead>
      <tbody>${FORMS_DATA.map(f => `<tr>
        <td><b>${esc(f.form)}</b></td><td>${esc(f.rule)}</td><td>${esc(f.title)}</td>
        <td>${esc(f.submits)}</td><td>${esc(f.to)}</td><td>${esc(f.timeline)}</td>
        <td>${esc(f.amendment_note)}</td></tr>`).join("")}</tbody>
    </table></div>`;
}

/* ------------------------------------------------------------------ amendments */
function renderAmendments() {
  $("#amendmentsList").innerHTML = `
    <div class="table-wrap"><table class="mini-table">
      <thead><tr><th>Instrument</th><th>Dated</th><th>In force</th><th>Subject</th><th>Rules</th><th>Point to note</th></tr></thead>
      <tbody>${AMENDMENTS_DATA.map(a => `<tr>
        <td><b>${esc(a.notify)}</b></td><td>${esc(a.date)}</td><td>${esc(a.eff_date)}</td>
        <td>${esc(a.subject)}</td><td>${esc(a.rules_affected)}</td><td>${esc(a.summary)}</td></tr>`).join("")}</tbody>
    </table></div>`;
}

/* ------------------------------------------------------------------ core facts */
function renderCore() {
  $("#coreList").innerHTML = CORE_DATA.map(c => `
    <div class="worked-step"><span class="ws-k"><b>${c.n}.</b> ${esc(c.fact)}</span>
      <span class="ws-v">${esc(c.rule)}</span></div>`).join("");
}

/* ------------------------------------------------------------------ lab */
function elCreditCalc() {
  const bal = parseInt($("#labElBalance").value, 10) || 0;
  const credit = 15;
  const post = bal + credit;
  const out = $("#labElOut");
  const ceiling = 300;
  if (bal > 285 && bal <= ceiling) {
    out.innerHTML =
      `<b>The 285-day buffer applies.</b> The balance is ${bal}, which is above 285 but not above 300, so the ` +
      `advance credit of ${credit} days is <b>kept separately</b>. It is first adjusted against any earned leave ` +
      `taken during this half-year, and only the unspent balance is posted at the close of the half-year.<br>` +
      `If no earned leave is taken, the posted balance becomes ${post} days — lawfully above the ${ceiling}-day ` +
      `ceiling permanently, because the buffer exists to let a servant that high keep drawing until the balance ` +
      `falls back to ${ceiling}.`;
  } else if (bal <= 285 && post <= ceiling) {
    out.innerHTML =
      `<b>Full credit.</b> ${bal} + ${credit} = ${post} days. The balance is at or below 285, so the credit is ` +
      `posted in the ordinary way and nothing is held apart.`;
  } else if (bal <= 285) {
    out.innerHTML =
      `<b>Ceiling engaged.</b> ${bal} + ${credit} = ${post}, which is over ${ceiling}. Only ${ceiling - bal} ` +
      `day(s) can be posted; the remaining ${post - ceiling} day(s) lapse. The 285-day buffer does not help here ` +
      `because the starting balance was ${bal}, not above 285.`;
  } else {
    out.innerHTML =
      `<b>Already above the ceiling.</b> A balance of ${bal} can only arise through the 285-day buffer. No further ` +
      `credit is posted; the balance is drawn down until it falls to ${ceiling} or below.`;
  }
}
function labCommutation() {
  const hpl = parseInt($("#labHpl").value, 10) || 0;
  const want = parseInt($("#labCommute").value, 10) || 0;
  const maxCommute = Math.floor(hpl / 2);
  const allowed = Math.min(want, maxCommute);
  $("#labCommOut").innerHTML =
    `<b>Maximum commutable:</b> half of ${hpl} = ${maxCommute} day(s).<br>` +
    `<b>Granted:</b> ${allowed} day(s) at full pay, debiting <b>${allowed * 2}</b> day(s) against HPL.<br>` +
    (want > maxCommute ? `<span class="pill bad">Request of ${want} days exceeds the half-of-HPL limit.</span>` : `<span class="pill ok">Within the Rule 30(1) limit.</span>`);
}
function labEncashment() {
  const el = parseInt($("#labEncEl").value, 10) || 0;
  const hpl = parseInt($("#labEncHpl").value, 10) || 0;
  const pay = parseInt($("#labEncPay").value, 10) || 0;
  const da = parseInt($("#labEncDa").value, 10) || 0;
  const days = Math.min(300, el + hpl);
  const fromEl = Math.min(el, days);
  const fromHpl = Math.max(0, days - fromEl);
  const base = pay + da;
  const cash = Math.round((base * fromEl) / 30 + (base / 2 * fromHpl) / 30);
  $("#labEncOut").innerHTML =
    `<b>Encashable days:</b> ${days} (of ${el + hpl} at credit, ceiling 300).<br>` +
    `<b>From EL:</b> ${fromEl} days · <b>From HPL:</b> ${fromHpl} days.<br>` +
    `<b>Approximate cash equivalent:</b> ₹${cash.toLocaleString("en-IN")} ` +
    `at pay ₹${pay.toLocaleString("en-IN")} + DA ₹${da.toLocaleString("en-IN")} (HPL leg at half of that base; HRA excluded).`;
}
function labEol() {
  const days = parseInt($("#labEol").value, 10) || 0;
  const elCut = Math.min(15, Math.round(days / 10));
  const hplCut = Math.min(10, Math.round(days / 18));
  $("#labEolOut").innerHTML =
    `<b>EOL:</b> ${days} days, no leave salary.<br>` +
    `<b>EL account penalty:</b> 1/10th of ${days} = ${(days / 10).toFixed(1)} → <b>${elCut}</b> day(s) (cap 15).<br>` +
    `<b>HPL account penalty:</b> 1/18th of ${days} = ${(days / 18).toFixed(1)} → <b>${hplCut}</b> day(s) (cap 10).`;
}
function labStudy() {
  const sl = parseInt($("#labStudyLeave").value, 10) || 0;
  const other = parseInt($("#labStudyOther").value, 10) || 0;
  const phd = $("#labStudyPhd").checked;
  const cap = phd ? 36 : 28;
  const total = sl + other;
  $("#labStudyOut").innerHTML = total <= cap
    ? `<b>Within the cap.</b> ${sl} + ${other} = ${total} months against a ${cap}-month cap (vacation included).`
    : `<b>Beyond the cap.</b> ${sl} + ${other} = ${total} months against ${cap}. The excess of ${total - cap} month(s) must be reduced or the combination refused.`;
}
function labCcl() {
  const used = parseInt($("#labCclUsed").value, 10) || 0;
  const left = Math.max(0, 730 - used);
  const full = Math.max(0, Math.min(365 - used, left));
  const eighty = Math.max(0, left - full);
  $("#labCclOut").innerHTML =
    `<b>Remaining:</b> ${left} day(s) of the 730.<br>` +
    `<b>At 100% pay:</b> ${full} day(s) · <b>at 80% pay:</b> ${eighty} day(s).<br>` +
    `Spell limit: minimum 5 days, maximum 120 days; 3 spells a year (6 for a single female parent).`;
}
function renderLab() {
  elCreditCalc(); labCommutation(); labEncashment(); labEol(); labStudy(); labCcl();
}

/* ------------------------------------------------------------------ mistakes */
function renderMistakes() {
  const ids = STATE.mistakes.slice().reverse();
  $("#mistakeCount").textContent = ids.length;
  $("#mistakesList").innerHTML = ids.length
    ? ids.map(id => mcqCard(MCQS_MAP[id])).join("")
    : `<div class="empty-state">Nothing in the notebook yet. Every wrong answer or reveal lands here automatically.</div>`;
}
function clearMistakes() {
  if (!confirm("Empty the mistake notebook?")) return;
  STATE.mistakes = [];
  save();
  renderMistakes();
}

/* ------------------------------------------------------------------ settings */
function renderSettings() {
  $("#settingsStats").innerHTML = `
    <div class="worked-step"><span class="ws-k">Questions in the bank</span><span class="ws-v">${MCQS_DATA.length}</span></div>
    <div class="worked-step"><span class="ws-k">Rule cards</span><span class="ws-v">${RULES_DATA.length}</span></div>
    <div class="worked-step"><span class="ws-k">Flashcards</span><span class="ws-v">${FLASHCARDS_DATA.length}</span></div>
    <div class="worked-step"><span class="ws-k">Questions attempted</span><span class="ws-v">${Object.keys(STATE.answers).length}</span></div>
    <div class="worked-step"><span class="ws-k">Bookmarks</span><span class="ws-v">${STATE.bookmarks.length}</span></div>
    <div class="worked-step"><span class="ws-k">Mock papers taken</span><span class="ws-v">${STATE.mockResults.length}</span></div>`;
}
function exportProgress() {
  const blob = new Blob([JSON.stringify({
    app: "ccs-leave-1972-platform", version: 1, exported: new Date().toISOString(),
    answers: STATE.answers, bookmarks: STATE.bookmarks, mistakes: STATE.mistakes,
    flashcards: STATE.flashcards, mockResults: STATE.mockResults, prefs: STATE.prefs
  }, null, 1)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "ccs-leave-progress-" + todayKey() + ".json";
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 2000);
}
function importProgress(ev) {
  const f = ev.target.files && ev.target.files[0];
  if (!f) return;
  const r = new FileReader();
  r.onload = () => {
    try {
      const d = JSON.parse(r.result);
      if (!d || d.app !== "ccs-leave-1972-platform") throw new Error("not this app's backup");
      localStorage.setItem(LS_KEY, JSON.stringify(d));
      location.reload();
    } catch (e) {
      alert("That file could not be read as a backup of this platform.");
    }
  };
  r.readAsText(f);
}
function resetEverything() {
  if (!confirm("Erase all saved progress on this device? This cannot be undone.")) return;
  try { localStorage.removeItem(LS_KEY); } catch (e) {}
  location.reload();
}

/* ------------------------------------------------------------------ counters */
/* Numbers written into the page come from the data, never from the markup, so a
   rebuild cannot leave a stale count on screen. */
const NUMBER_WORDS = {
  11: "eleven", 12: "twelve", 18: "eighteen", 19: "nineteen", 20: "twenty", 25: "twenty-five",
  28: "twenty-eight", 29: "twenty-nine", 31: "thirty-one", 38: "thirty-eight", 40: "forty",
  69: "sixty-nine", 80: "eighty", 82: "eighty-two",
  341: "three hundred and forty-one", 682: "six hundred and eighty-two",
  700: "seven hundred", 780: "seven hundred and eighty"
};
function fillCounts() {
  const n = {
    rules: RULES_DATA.length, mcqs: MCQS_DATA.length, flashcards: FLASHCARDS_DATA.length,
    modules: MODULES_DATA.length, mocks: MOCK_TESTS_DATA.length, tables: TABLES_DATA.length,
    cases: CASES_DATA.length, forms: FORMS_DATA.length, amendments: AMENDMENTS_DATA.length,
    num80: NUM80_DATA.length
  };
  $$("[data-count]").forEach(el => {
    const v = n[el.dataset.count];
    if (v != null) el.textContent = v.toLocaleString("en-IN");
  });
  $$("[data-count-word]").forEach(el => {
    const v = n[el.dataset.countWord];
    if (v != null) el.textContent = NUMBER_WORDS[v] || String(v);
  });
}

/* ------------------------------------------------------------------ test hook */
/* A tiny read-only handle so a headless test (or the console) can inspect the
   loaded data and the live state. Nothing in the app depends on it. */
window.__CCSLR = {
  get state() { return STATE; },
  get mcqsById() { return MCQS_MAP; },
  rules: RULES_DATA, mcqs: MCQS_DATA, flashcards: FLASHCARDS_DATA,
  mocks: MOCK_TESTS_DATA, tables: TABLES_DATA, cases: CASES_DATA,
  modules: MODULES_DATA, forms: FORMS_DATA, amendments: AMENDMENTS_DATA, core: CORE_DATA,
  num80: NUM80_DATA, num80ById: NUM80_MAP
};

/* ------------------------------------------------------------------ boot */
function boot() {
  load();
  fillCounts();
  applyTheme(STATE.prefs.theme || "light");
  $("#btnTheme").addEventListener("click", toggleTheme);
  $$(".nav-btn").forEach(b => b.addEventListener("click", () => switchView(b.dataset.view)));
  // chapter selects
  const chOpts = chapters().map(([ch, t]) => `<option value="${esc(ch)}">${esc(ch)} — ${esc(t)}</option>`).join("");
  $("#ruleChapter").innerHTML = `<option value="ALL">All chapters</option>` +
    RULES_DATA.reduce((acc, r) => acc.includes(`value="${r.chapter}"`) ? acc :
      acc + `<option value="${esc(r.chapter)}">Chapter ${esc(r.chapter)} — ${esc(r.chapter_title)}</option>`, "");
  $("#mcqChapter").innerHTML = `<option value="ALL">All chapters</option>` +
    MCQS_DATA.reduce((acc, m) => acc.includes(`value="${m.chapter}"`) ? acc :
      acc + `<option value="${esc(m.chapter)}">${esc(m.chapter)} — ${esc(m.chapter_title)}</option>`, "");
  $("#num80Block").innerHTML = `<option value="ALL">All nine blocks</option>` +
    num80Blocks().map(b => `<option value="${esc(b)}">${esc(b)}</option>`).join("");
  $("#fcCategory").innerHTML = `<option value="ALL">All categories (${FLASHCARDS_DATA.length})</option>` +
    Array.from(new Set(FLASHCARDS_DATA.map(f => f.category))).map(c =>
      `<option value="${esc(c)}">${esc(c)} (${FLASHCARDS_DATA.filter(f => f.category === c).length})</option>`).join("");
  $("#ruleSearch").addEventListener("input", renderRules);
  $("#ruleChapter").addEventListener("change", renderRules);
  $("#mcqSearch").addEventListener("input", () => { STATE.mcq.search = $("#mcqSearch").value.trim(); STATE.mcq.page = 1; renderMcqs(); });
  $("#mcqChapter").addEventListener("change", () => { STATE.mcq.chapter = $("#mcqChapter").value; STATE.mcq.page = 1; renderMcqs(); });
  $("#mcqDifficulty").addEventListener("change", () => { STATE.mcq.difficulty = $("#mcqDifficulty").value; STATE.mcq.page = 1; renderMcqs(); });
  $("#fcCategory").value = STATE.fc.category;
  updateSideProgress();
  switchView("dash");
}
document.addEventListener("DOMContentLoaded", boot);
