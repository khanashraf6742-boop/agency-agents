#!/usr/bin/env python3
"""mutation_test.py — prove the cross-reference control actually catches gaps.

The whitelist is only worth having if a citation that is NOT one of the five enumerated
statute defects fails the build. This script seeds a scratch copy of the build with faults
that a transcription error would realistically produce, and asserts the audit fails on each.
A control that has never been seen to fail is not a control.

Run from anywhere:  python3 build/mutation_test.py
"""
from __future__ import annotations

import pathlib
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent


# The checks that constitute the control. audit.py imports this list so the two cannot drift
# apart; running the whole audit here would recurse (audit.py runs this script).
CONTROL_CHECKS = [
    "every internal cross-reference resolves",
    "the defect whitelist holds exactly five entries",
    "every whitelisted defect still occurs",
    "no whitelisted defect is claimed at an address",
    "rule 35 carries the sub-rules",
]


def audit_fails(root):
    """Run the cross-reference checks in a copy of the build; return (failed, output).

    Deliberately not the whole audit: audit.py invokes this script, so running it here would
    recurse forever. Selection is by check name, so a check that is renamed or removed shows up
    as a baseline failure rather than silently narrowing the control.
    """
    r = subprocess.run([sys.executable, "audit.py", "--only", "xref"], cwd=root,
                       capture_output=True, text=True)
    return r.returncode != 0, (r.stdout + r.stderr)


# Each mutation is (description, file, transform). The transform must change the file.
MUTATIONS = [
    ("truncate rule 35 at sub-rule (5) — the historical bug",
     "pension_rules.py",
     lambda s: (s[:s.index('TEXT["35"] = TEXT["35"].rstrip')]
                + s[s.index('TEXT["36"] = (', s.index('TEXT["35"] = TEXT["35"].rstrip')):])),

    ("retarget a live citation to a rule that does not exist",
     "pension_rules.py",
     lambda s: s.replace("in accordance with rule 44 and rule 45",
                         "in accordance with rule 44 and rule 99", 1)),

    ("add a sixth entry to the whitelist to excuse a gap",
     "xrefs.py",
     lambda s: s.replace('    ("81(2)", "76(2)(d)"): {',
                         '    ("35(1)", "35(9)"): {\n'
                         '        "quote": "invented", "reason": "invented to excuse a gap",\n'
                         '    },\n    ("81(2)", "76(2)(d)"): {', 1)),

    ("leave a stale entry after the statute is amended to fix a defect",
     "xrefs.py",
     lambda s: (s[:s.index('    ("8(4)(d)", "8(9)"): {')]
                + s[s.index('    ("65(5)(d)", "8(5)(c)"): {'):])),
]


def main():
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp) / "base"
        shutil.copytree(HERE, base, ignore=shutil.ignore_patterns("__pycache__"))
        failed, out = audit_fails(base)
        if failed:
            print("BASELINE ALREADY FAILS — fix the build before testing the control")
            print(out[-1500:])
            return 1
        print("baseline: audit passes\n")

        for desc, fname, transform in MUTATIONS:
            root = pathlib.Path(tmp) / f"m{MUTATIONS.index((desc, fname, transform))}"
            shutil.copytree(base, root)
            path = root / fname
            before = path.read_text()
            after = transform(before)
            if after == before:
                print(f"  INVALID  {desc}\n           the mutation did not change {fname}")
                ok = False
                continue
            path.write_text(after)
            failed, out = audit_fails(root)
            caught = failed and "AUDIT FAILED" in out
            print(f"  {'CAUGHT' if caught else 'MISSED':8} {desc}")
            if caught:
                for line in out.splitlines():
                    if line.strip().startswith("FAIL"):
                        print(f"           {line.strip()[:150]}")
                        break
            else:
                ok = False
                print(out[-800:])

    print("\n" + ("MUTATION TEST PASSED — every seeded fault was caught"
                  if ok else "MUTATION TEST FAILED — the control has a blind spot"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
