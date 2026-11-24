#!/usr/bin/env python3
"""assemble.py — one self-contained HTML file, built from source, never hand-edited.

Pipeline:  paymatrix.py -> data_numeric.py / data_bank.py -> engine.py -> audit.py -> assemble.py
The audit must pass before the HTML is written; a wrong rupee fails the build.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "CCS-Revised-Pay-Rules-2016-Exam-Platform.html"
NUM_MD = HERE.parent / "Numerical-Set-Worked-Solutions.md"


def js_json(obj) -> str:
    """JSON that is safe inside a <script> block."""
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return (s.replace("</", "<\\/").replace("<!--", "<\\!--")
             .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))


def main() -> int:
    print("— audit —")
    r = subprocess.run([sys.executable, "audit.py"], cwd=HERE, capture_output=True, text=True)
    print(r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr[-400:])
    if r.returncode != 0:
        print(r.stdout[-4000:])
        print("BUILD STOPPED: the audit failed, so no HTML was written.")
        return r.returncode

    pay = json.loads((HERE / "pay.json").read_text())
    matrix = json.loads((HERE / "matrix.json").read_text())
    rj = json.loads((HERE / "rules_out.json").read_text())

    css = (HERE / "app.css").read_text()
    app = (HERE / "app.js").read_text()
    shell = (HERE / "shell.html").read_text()

    data = (
        "const MATRIX_DATA=" + js_json(matrix) + ";\n"
        "const RULES_DATA=" + js_json(rj["rules"]) + ";\n"
        "const CHAPTERS_DATA=" + js_json(rj["chapters"]) + ";\n"
        "const AMENDMENTS_DATA=" + js_json(rj["amendments"]) + ";\n"
        "const PAY_DATA=" + js_json(pay) + ";\n"
    )
    html = (shell.replace("/*__CSS__*/", css)
                 .replace("/*__DATA__*/", data)
                 .replace("/*__APP__*/", app))
    OUT.write_text(html)

    # the printable edition of the numerical set, from the same records
    LET = "ABCD"
    md = ["# The Numerical Set — worked solutions", "",
          "*Every question in this file that turns on a rupee, with its matrix column, its step-by-step solution, and a "
          "note on where each wrong option comes from. Generated from the same records that build the platform, so the "
          "two cannot drift apart.*", ""]
    for i, q in enumerate([x for x in pay if x["section"] == "NUM"], 1):
        md += [f"## Q{i}. [{q['id']}] {q['q']}", ""]
        if q["table"]:
            t = q["table"]
            if t["kind"] == "cells":
                head = " | ".join(str(c["cell"]) for c in t["cells"])
                vals = " | ".join(f"₹{c['pay']:,}" for c in t["cells"])
                md += [f"*Level {t['level']} — cell:* {head}", f"*Pay:* {vals}", ""]
            elif t["kind"] == "compare":
                md += ["*As notified:* " + " | ".join(f"₹{c['pay']:,}" for c in t["before"]),
                       "*After 16.05.2017:* " + " | ".join(f"₹{c['pay']:,}" for c in t["after"]), ""]
        for k, o in enumerate(q["opts"]):
            md.append(f"- ({LET[k]}) {o}" + (" **← answer**" if LET[k] == q["ans"] else ""))
        md += ["", f"**Answer: ({q['ans']})**", ""]
        body = q["expl"]
        steps = body[body.index("Worked solution, step by step"):body.index("Where the other options come from")]
        md += ["**Stepwise solution**", ""]
        md += [f"{n}. {ln.strip()}" for n, ln in enumerate(steps.split("\n")[1:], 1) if ln.strip()]
        md += ["", "**Why the other options are wrong**", ""]
        tail = body[body.index("Where the other options come from"):]
        for ln in tail.split("\n")[1:]:
            ln = ln.strip()
            if not ln:
                continue
            if ln.startswith("Exam-safe point:"):
                md += ["", f"**{ln}**"]
            elif ln.startswith("Statutory Authority:"):
                continue
            else:
                md.append("- " + ln)
        md += ["", f"> *Authority:* {q['src']}", "", "---", ""]
    NUM_MD.write_text("\n".join(md))

    size = OUT.stat().st_size
    print(f"wrote {OUT.name}  {size / 1024:.0f} KB")
    print(f"wrote {NUM_MD.name}  {NUM_MD.stat().st_size / 1024:.0f} KB")
    print(f"  {len(pay)} questions · {sum(1 for q in pay if q['table'])} with a matrix · "
          f"{sum(1 for q in pay if q['section'] == 'NUM')} numericals · {len(rj['rules'])} rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
