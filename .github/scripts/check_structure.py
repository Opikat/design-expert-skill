#!/usr/bin/env python3
"""Check that the skill is loadable and internally consistent.

- design-expert/SKILL.md has frontmatter with name and description;
- every relative Markdown link points to an existing file;
- every Python script compiles;
- every CSV row has the same number of columns as its header.
"""
import csv
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKILL = ROOT / "design-expert" / "SKILL.md"
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
errors = []


def check_frontmatter():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{SKILL.relative_to(ROOT)}: no frontmatter")
        return
    for key in ("name", "description"):
        if not re.search(rf"^{key}:\s*\S", m.group(1), re.M):
            errors.append(f"{SKILL.relative_to(ROOT)}: frontmatter lacks '{key}'")


def check_links():
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
        for target in LINK.findall(text):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            path = (md.parent / target.split("#")[0]).resolve()
            if not path.exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link -> {target}")


def check_python():
    for py in ROOT.rglob("*.py"):
        if ".git" in py.parts:
            continue
        try:
            compile(py.read_text(encoding="utf-8"), str(py), "exec")
        except SyntaxError as e:
            errors.append(f"{py.relative_to(ROOT)}:{e.lineno}: {e.msg}")


def check_csv():
    for f in ROOT.rglob("*.csv"):
        with f.open(encoding="utf-8", newline="") as fh:
            rows = list(csv.reader(fh))
        if not rows:
            continue
        width = len(rows[0])
        for n, row in enumerate(rows[1:], 2):
            if row and len(row) != width:
                errors.append(f"{f.relative_to(ROOT)}:{n}: {len(row)} columns, header has {width}")


check_frontmatter()
check_links()
check_python()
check_csv()
for e in errors:
    print(f"::error::{e}")
print(f"{len(errors)} problem(s) found." if errors else "Structure OK.")
sys.exit(1 if errors else 0)
