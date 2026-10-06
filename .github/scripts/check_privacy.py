#!/usr/bin/env python3
"""Fail if the repo contains personal or local-machine data.

Two pattern sets:
- generic: e-mail addresses, absolute home paths, private-key headers;
- private: one regex per line from the PRIVATE_PATTERNS environment variable
  (a repository secret, so the list itself is never published). Hits on these
  report only file:line, never the matched text.
"""
import os
import re
import subprocess
import sys

ALLOWED_EMAILS = {"noreply@anthropic.com", "noreply@github.com"}

GENERIC = [
    ("e-mail address", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")),
    ("absolute home path", re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\Users\\)(?!you\b|<|\$|USER\b)[A-Za-z0-9._-]+")),
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]


def tracked_files():
    out = subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True).stdout
    return [p for p in out.decode().split("\0") if p and not p.startswith(".github/")]


def private_patterns():
    raw = os.environ.get("PRIVATE_PATTERNS", "")
    return [re.compile(line.strip(), re.IGNORECASE) for line in raw.splitlines() if line.strip()]


def main():
    private = private_patterns()
    if not private:
        print("::warning::PRIVATE_PATTERNS is empty; only generic checks ran.")
    problems = 0
    for path in tracked_files():
        try:
            lines = open(path, encoding="utf-8").read().splitlines()
        except (UnicodeDecodeError, IsADirectoryError):
            continue
        for n, line in enumerate(lines, 1):
            for label, rx in GENERIC:
                for m in rx.finditer(line):
                    if label == "e-mail address" and m.group(0).lower() in ALLOWED_EMAILS:
                        continue
                    print(f"::error file={path},line={n}::{label}: {m.group(0)}")
                    problems += 1
            for rx in private:
                if rx.search(line):
                    print(f"::error file={path},line={n}::matches a private pattern")
                    problems += 1
    print(f"{problems} problem(s) found." if problems else "No personal data found.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
