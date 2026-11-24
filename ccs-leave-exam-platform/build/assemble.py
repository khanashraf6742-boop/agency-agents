#!/usr/bin/env python3
"""Assemble the single-file platform: shell.html + app.css + app.js + JSON data."""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "CCS-Leave-Rules-1972-Exam-Platform.html"

def js_json(obj):
    """JSON that is safe to drop inside a <script> block."""
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("</", "<\\/").replace("<!--", "<\\!--").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")

def main():
    rules = json.loads((HERE / "rules.json").read_text())
    mcqs = json.loads((HERE / "mcqs.json").read_text())
    extras = json.loads((HERE / "extras.json").read_text())
    num80 = json.loads((HERE / "num80.json").read_text())
    css = (HERE / "app.css").read_text()
    app = (HERE / "app.js").read_text()
    shell = (HERE / "shell.html").read_text()

    data = (
        "const RULES_DATA=" + js_json(rules) + ";\n"
        "const MCQS_DATA=" + js_json(mcqs) + ";\n"
        "const FLASHCARDS_DATA=" + js_json(extras["flashcards"]) + ";\n"
        "const MODULES_DATA=" + js_json(extras["modules"]) + ";\n"
        "const MOCK_TESTS_DATA=" + js_json(extras["mocks"]) + ";\n"
        "const TABLES_DATA=" + js_json(extras["tables"]) + ";\n"
        "const CASES_DATA=" + js_json(extras["cases"]) + ";\n"
        "const FORMS_DATA=" + js_json(extras["forms"]) + ";\n"
        "const AMENDMENTS_DATA=" + js_json(extras["amendments"]) + ";\n"
        "const CORE_DATA=" + js_json(extras["core"]) + ";\n"
        "const NUM80_DATA=" + js_json(num80) + ";\n"
    )

    html = shell.replace("/*__CSS__*/", css).replace("/*__DATA__*/", data).replace("/*__APP__*/", app)
    # sidebar counts are hard-coded in the shell; keep them honest
    counts = {
        "rules": len(rules), "mcqs": len(mcqs), "fc": len(extras["flashcards"]),
        "mods": len(extras["modules"]), "mocks": len(extras["mocks"]),
        "tables": len(extras["tables"]), "cases": len(extras["cases"]),
        "forms": len(extras["forms"]), "amends": len(extras["amendments"]),
        "num80": len(num80),
    }
    OUT.write_text(html)

    # the readable study edition of the numerical set, generated from the same data
    LET = "ABCD"
    md = ["# The Numerical 80 — CCS (Leave) Rules, 1972", "",
          "*Eighty questions that turn on arithmetic, each with a step-by-step solution and a note on where every wrong "
          "option comes from. Built into the platform as the **Numerical 80** view and as CBT paper MOCK-31.*", "",
          "**How to use it.** Try each question with the solution covered. The three steps are written the way an "
          "establishment clerk works a file: test the limit, do the arithmetic, then apply the ceiling. The last block of "
          "each answer says which mistake produces each wrong option — that is what the examiner is really testing.", ""]
    blocks = []
    for m in num80:
        b = m["topic"].split(" — worked")[0]
        if b not in blocks:
            blocks.append(b)
    md.append("## Contents")
    for b in blocks:
        k = [i for i, m in enumerate(num80, 1) if m["topic"].split(" — worked")[0] == b]
        md.append(f"- **{b}** — questions {k[0]}–{k[-1]}")
    md.append("")
    cur = None
    for i, m in enumerate(num80, 1):
        b = m["topic"].split(" — worked")[0]
        if b != cur:
            cur = b
            md += ["", f"## {b}", ""]
        md.append(f"### Q{i}. {m['stem']}")
        md.append("")
        for k, o in enumerate(m["opts"]):
            md.append(f"- ({LET[k]}) {o}" + (" **← answer**" if LET[k] == m["ans"] else ""))
        md.append("")
        body = m["expl"]
        steps = body[body.index("Worked solution, step by step"):body.index("Where the other options come from")]
        whys = body[body.index("Where the other options come from"):]
        md += ["**Stepwise solution**", ""]
        md += [ln.strip() for ln in steps.split("\n")[1:] if ln.strip()]
        md += ["", "**Why the other options are wrong**", ""]
        tail = []
        for ln in whys.split("\n")[1:]:
            ln = ln.strip()
            if not ln:
                continue
            if ln.startswith("Exam-safe point:"):
                tail.append(ln)
            elif ln.startswith("Statutory Authority:"):
                continue
            else:
                md.append("- " + ln)
        if tail:
            md += ["", "**" + tail[0] + "**"]
        md += ["", f"> *Authority:* {m['src']}", ""]
    (HERE.parent / "Numerical-80-CCS-Leave-Rules-1972.md").write_text("\n".join(md))
    print("wrote the numerical-80 markdown edition")
    print("wrote", OUT, f"{OUT.stat().st_size/1024/1024:.2f} MB")
    print("counts", counts)
    return 0

if __name__ == "__main__":
    sys.exit(main())
