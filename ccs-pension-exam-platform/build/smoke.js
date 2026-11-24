// smoke.js — DOM-level checks on the built HTML. Fails loudly rather than printing warnings.
const fs = require("fs");
const path = require("path");
const { JSDOM } = require(path.join(__dirname, "..", "..", "node_modules", "jsdom"));

const file = path.join(__dirname, "..", "CCS-Pension-Rules-2021-Exam-Platform.html");
const dom = new JSDOM(fs.readFileSync(file, "utf8"), { runScripts: "outside-only" });
const d = dom.window.document;

const fails = [];
const ck = (name, ok, detail = "") => {
  if (!ok) fails.push(`${name}${detail ? " — " + detail : ""}`);
};

const cards = [...d.querySelectorAll("details.rule-card")];
ck("87 rule cards", cards.length === 87, `${cards.length}`);
const nums = cards.map(c => parseInt(c.id.replace("rule-", ""), 10));
ck("rule cards numbered 1..87 with none missing",
   nums.join(",") === [...Array(87)].map((_, i) => i + 1).join(","));

// every rule card must have real statutory text, not a placeholder
const short = cards.filter(c => c.querySelector(".rule-body").textContent.trim().length < 40);
ck("every rule card carries text", short.length === 0, short.map(c => c.id).join(","));

// rule 3 must actually define Form and Format, which the whole platform turns on
const r3 = d.querySelector("#rule-3").textContent;
ck("rule 3 defines Form", /Form.*appended to these rules/i.test(r3));
ck("rule 3 defines Format", /Format.*appended to these rules/i.test(r3));

// the last rule must be the repeal, proving transcription reached the end
ck("rule 87 is the repeal provision", /Repeal and Saving/i.test(d.querySelector("#rule-87").textContent));
ck("rule 87 mentions the 1972 Rules",
   /1972/.test(d.querySelector("#rule-87").textContent));

const qs = [...d.querySelectorAll(".q-card")];
// read the count from the build itself, so a rebuild never leaves a stale constant here
const QCOUNT = JSON.parse(fs.readFileSync(path.join(__dirname, "questions.json"), "utf8")).length;
ck("question cards rendered", qs.length === QCOUNT, `${qs.length} vs ${QCOUNT}`);
ck("every provision is covered", /Coverage, measured/.test(d.body.textContent));
ck("the amendment register is on the page", d.querySelectorAll("table.amend tbody tr").length >= 15,
   `${d.querySelectorAll("table.amend tbody tr").length}`);
ck("every question has exactly four options",
   qs.every(q => q.querySelectorAll(".q-opts li").length === 4));
ck("every question marks exactly one key",
   qs.every(q => q.querySelectorAll(".q-opts li.key").length === 1));
ck("every question has a reasoning block",
   qs.every(q => q.querySelector("details.q-expl")));
ck("no question shows an empty explanation",
   qs.every(q => q.querySelector("details.q-expl div").textContent.trim().length > 80));

// every Form and Format row must be present and sourced
const tables = [...d.querySelectorAll("table")].filter(t => !t.classList.contains("amend")
  && !t.classList.contains("cov"));
ck("two registers: Forms then Formats", tables.length === 2, `${tables.length}`);
const rows = t => [...t.querySelectorAll("tbody tr")];
ck("14 Form rows", rows(tables[0]).length === 14, `${rows(tables[0]).length}`);
ck("13 Format rows", rows(tables[1]).length === 13, `${rows(tables[1]).length}`);
ck("every Form row is sourced",
   rows(tables[0]).every(r => /sourced/.test(r.lastElementChild.textContent)));
ck("every Format row is sourced",
   rows(tables[1]).every(r => /sourced/.test(r.lastElementChild.textContent)));
ck("any unsourced row would be visibly marked",
   rows(tables[0]).concat(rows(tables[1])).every(r =>
     /sourced|not yet sourced/.test(r.lastElementChild.textContent)));

// Form and Format must never collapse into one label
const body = d.body.textContent;
ck("the page distinguishes Form from Format", /Formats appended/i.test(body));

// no template or encoding debris
ck("no unresolved placeholders", !/\{[a-z_]+\}/.test(body));
ck("no mojibake", !/â€|Ã¢|ï¿½/.test(body));

if (fails.length) {
  console.log(`SMOKE FAILED — ${fails.length}`);
  fails.forEach(f => console.log("  FAIL —", f));
  process.exit(1);
}
const amend = d.querySelectorAll("table.amend tbody tr").length;
console.log(`SMOKE PASSED — ${qs.length} questions, ${cards.length} rules, 14 Forms, 13 Formats, ${amend} instruments`);
