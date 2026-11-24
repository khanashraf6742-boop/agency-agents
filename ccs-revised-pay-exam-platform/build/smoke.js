/* smoke.js — drives the built HTML in jsdom and asserts what a reader would see. */
const fs = require("fs");
const path = require("path");
const { JSDOM } = require("/home/user/agency-agents/node_modules/jsdom");

const FILE = path.resolve(__dirname, "..", "CCS-Revised-Pay-Rules-2016-Exam-Platform.html");
const html = fs.readFileSync(FILE, "utf8");
const errors = [];
const dom = new JSDOM(html, { runScripts: "dangerously", pretendToBeVisual: true, url: "https://example.org/" });
const w = dom.window;
w.addEventListener("error", e => errors.push("window error: " + e.message));
w.alert = () => {};
w.confirm = () => true;

let pass = 0, fail = 0;
function ok(name, cond, detail) {
  if (cond) { pass++; console.log("  ✓ " + name); }
  else { fail++; console.log("  ✗ " + name + (detail ? " — " + detail : "")); }
}

setTimeout(() => {
  const d = w.document;
  console.log("\n== boot ==");
  ok("no script errors", errors.length === 0, errors.join(" | "));
  const N = w.__CCSRP.PAY_DATA.length;
  ok("the data is inlined", Array.isArray(w.__CCSRP.PAY_DATA) && N >= 89);
  ok("the matrix is inlined", !!w.__CCSRP.MATRIX_DATA && w.__CCSRP.MATRIX_DATA.levels.length === 19);
  ok("543 cells reach the page", w.__CCSRP.MATRIX_DATA.levels.reduce((n, l) => n + w.__CCSRP.MATRIX_DATA.current[l].length, 0) === 543);
  ok("the dashboard rendered", d.querySelector("#dashChapterRows").children.length === 17);
  ok("counts filled from the data", d.querySelector('[data-count="pay"]').textContent === String(N));

  console.log("\n== a matrix question draws the matrix ==");
  const q = w.__CCSRP.PAY_MAP["PY-001"];
  const card = w.qCard(q, { forceTable: true });
  ok("the card carries a matrix block", card.includes("matrix-block"));
  ok("the level is named", card.includes("Level 4"));
  ok("the landing cell is marked", card.includes("cell-land"));
  ok("the landing cell is the only one marked", !card.includes("cell-start") && !card.includes("cell-both"));
  const startCard = w.qCard(w.__CCSRP.PAY_MAP["PY-004"], { forceTable: true });
  ok("a question with a genuine starting cell marks it", startCard.includes("cell-start"));
  ok("cell 9 is printed with its number", card.includes('Cell 9'));
  ok("the rupee figure is printed in Indian grouping", card.includes("₹32,300"));
  ok("the note is carried through", card.includes("Cell 9 (₹32,300)"));

  console.log("\n== the three table shapes ==");
  const cmp = w.__CCSRP.PAY_MAP["PY-015"];
  const cmpCard = w.qCard(cmp, { forceTable: true });
  ok("a compare table draws two columns", (cmpCard.match(/mx-col-table/g) || []).length === 2);
  ok("both amendment dates are labelled", cmpCard.includes("As notified") && cmpCard.includes("After 16.05.2017"));
  const map = w.__CCSRP.PAY_MAP["PY-018"];
  const mapCard = w.qCard(map, { forceTable: true });
  ok("a mapping table draws rows", mapCard.includes("mx-map") && mapCard.includes("5200-20200"));
  const cells = w.__CCSRP.PAY_MAP["RP-016"];
  ok("a general question can carry a table too", cells.table && cells.table.kind === "cells");

  console.log("\n== the explanation is structured, not a wall of text ==");
  const ex = w.explHtml(q.expl, q.id);
  ok("the answer line is a heading", ex.includes('class="ans-line"'));
  ok("the worked solution is an ordered list", ex.includes('class="expl-steps"'));
  ok("each step is a list item", (ex.match(/<li>/g) || []).length >= 4);
  ok("the wrong options are a list", ex.includes('class="expl-wrong"'));
  ok("the safe point is boxed", ex.includes('class="safe-box"'));
  ok("the authority is on its own line", ex.includes('class="auth-line"'));

  console.log("\n== answering ==");
  w.switchView("bank");
  ok("the bank lists questions", d.querySelector("#bankList").children.length > 0);
  const before = w.__CCSRP.STATE.answers["PY-001"];
  w.answer("PY-001", "B");
  const after = w.__CCSRP.STATE.answers["PY-001"];
  ok("an answer is recorded", !before && after && after.chosen === "B");
  ok("a wrong answer is recorded as wrong", after.correct === false);
  ok("it enters the mistake notebook", w.__CCSRP.STATE.mistakes.includes("PY-001"));
  ok("the explanation opens after answering", d.querySelector("#q-PY-001 .mcq-expl"));
  ok("the paper is still rendered", d.querySelector("#q-PY-001 .matrix-block"));
  w.answer("PY-002", w.__CCSRP.PAY_MAP["PY-002"].ans);
  ok("a right answer clears nothing it should not", w.__CCSRP.STATE.answers["PY-002"].correct === true);
  const coverage = w.stats().coverage;
  ok("coverage counts it", coverage === 2, "coverage=" + coverage + "%");
  w.resetQ("PY-001");
  ok("trying again clears the record", !w.__CCSRP.STATE.answers["PY-001"]);

  console.log("\n== the numerical set ==");
  w.switchView("numerical");
  const numCards = d.querySelectorAll("#numericalList .mcq-card").length;
  ok("all 23 numericals render", numCards === 23, "got " + numCards);
  const withMatrix = d.querySelectorAll("#numericalList .matrix-block").length;
  ok("every numerical that turns on a figure carries a matrix", withMatrix === 19, "got " + withMatrix);
  ok("the numerical count pill is right", d.querySelector("#numCount").textContent.startsWith("23"));

  console.log("\n== the rule library ==");
  w.switchView("rules");
  ok("17 rule cards", d.querySelectorAll("#rulesList .rule-card").length === 17);
  ok("the statutory text is shown", d.querySelectorAll("#rulesList .bare-text").length === 17);
  ok("the statutory text is the rule's own words",
     d.querySelector("#rule-7 .bare-text").textContent.includes("located in that Level"));
  ok("the plain-language summary is labelled as one",
     d.querySelectorAll("#rulesList .rule-summary").length === 17);
  ok("the trap line is shown", d.querySelectorAll("#rulesList .trap-line").length === 17);
  w.practiseRule("13");
  ok("practising a rule filters the bank", w.__CCSRP.STATE.bank.rule === "13" && w.__CCSRP.STATE.view === "bank");
  ok("the rule filter is applied", w.bankList().every(x => String(x.rule) === "13"));

  console.log("\n== the full matrix ==");
  w.switchView("matrix");
  const lvlRows = d.querySelectorAll("#mxTableWrap tbody tr").length;
  ok("19 level rows", lvlRows === 19, "got " + lvlRows);
  ok("the Level 13 re-cast cells are flagged", d.querySelectorAll("#mxTableWrap td.l13").length === 20);
  ok("the footer note counts the cells", d.querySelector("#mxCellCount").textContent === "543");

  console.log("\n== the lab does the rules' arithmetic ==");
  w.switchView("lab");
  d.querySelector("#labPay").value = "10160";
  d.querySelector("#labGP").value = "2400";
  d.querySelector("#labLevel").value = "4";
  w.labFitment();
  ok("12,560 fits to ₹32,300", d.querySelector("#labFitOut").textContent.includes("₹32,300"));
  ok("the lab shows the product", d.querySelector("#labFitOut").textContent.includes("32,279"));
  d.querySelector("#labIncLevel").value = "4";
  d.querySelector("#labIncPay").value = "32300";
  w.labIncrement();
  ok("the increment from 32,300 is 33,300", d.querySelector("#labIncOut").textContent.includes("₹33,300"));
  ok("and it says the step is ₹1,000, not 3%", d.querySelector("#labIncOut").textContent.includes("₹969"));
  d.querySelector("#labPromFrom").value = "4";
  d.querySelector("#labPromTo").value = "5";
  d.querySelector("#labPromPay").value = "28700";
  w.labPromotion();
  ok("the promotion lands on ₹30,100", d.querySelector("#labPromOut").textContent.includes("₹30,100"));
  ok("and shows the step through ₹29,600", d.querySelector("#labPromOut").textContent.includes("₹29,600"));
  w.labNpa();
  ok("the NPA route lands on ₹61,300", d.querySelector("#labNpaOut").textContent.includes("₹61,300"));
  ok("and adds the pre-revised NPA on top", d.querySelector("#labNpaOut").textContent.includes("₹66,550"));

  console.log("\n== the papers ==");
  w.switchView("mock");
  ok("four papers are offered", d.querySelectorAll("#mockList .rule-card").length === 4);
  ok("each paper has questions", w.__CCSRP.PAPERS.every(p => p.questions.length > 0));
  ok("every paper is at least a quarter arithmetic", w.__CCSRP.PAPERS.every(p =>
    p.questions.filter(x => x.section === "NUM").length >= Math.ceil(p.questions.length / 4)),
    w.__CCSRP.PAPERS.map(p => p.id + ":" + p.questions.filter(x => x.section === "NUM").length + "/" + p.questions.length).join(" "));
  ok("each paper carries matrix questions", w.__CCSRP.PAPERS.every(p => p.questions.some(x => x.table)));
  w.startPaper("PAPER-1");
  ok("a paper starts", !!w.__CCSRP.STATE.mock && d.querySelector("#cbtBar").hidden === false);
  ok("the paper renders its questions", d.querySelectorAll("#cbtList .mcq-card").length === w.__CCSRP.STATE.mock.paper.questions.length);
  const pid = w.__CCSRP.STATE.mock.paper.questions[0].id;
  w.cbtPick(pid, "A");
  ok("an option can be picked", w.__CCSRP.STATE.mock.answers[pid] === "A");
  w.cbtPick(pid, "A");
  ok("picking it again clears it", w.__CCSRP.STATE.mock.answers[pid] === undefined);
  w.cbtPick(pid, "B");
  w.finishPaper();
  ok("submitting scores the paper", w.__CCSRP.STATE.mockResults.length === 1);
  ok("the score is out of the paper's length", w.__CCSRP.STATE.mockResults[0].total > 0);
  ok("the paper's questions are now in the bank", w.__CCSRP.STATE.answers[pid] !== undefined);
  ok("the paper list comes back", d.querySelectorAll("#mockList .rule-card").length === 4);

  console.log("\n== mistakes and persistence ==");
  w.switchView("mistakes");
  ok("the wrong answers are here", w.__CCSRP.STATE.mistakes.length > 0);
  ok("the notebook counts them", Number(d.querySelector("#mistakeCount").textContent) === w.__CCSRP.STATE.mistakes.length);
  const saved = JSON.parse(w.localStorage.getItem("ccsrpr2016-state-v1"));
  ok("progress is written to local storage", saved && saved.answers && Object.keys(saved.answers).length > 0);
  w.switchView("settings");
  ok("the settings page counts the file", d.querySelector("#settingsStats").textContent.includes("543"));

  console.log("\n== printing and theme ==");
  w.toggleTheme();
  ok("the dark theme applies", d.documentElement.getAttribute("data-theme") === "dark");
  w.toggleTheme();
  ok("and toggles back", d.documentElement.getAttribute("data-theme") === "light");

  console.log(`\n${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
}, 600);
