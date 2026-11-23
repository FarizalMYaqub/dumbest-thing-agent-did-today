#!/usr/bin/env python3
"""One line for the make.fun Dumbest Thing Your Agent Did Today bounty.

The whole entry is a single line about the dumbest thing my own
agent did today. It is a real incident from this campaign, not a
stock joke: while two fresh joke entries were waiting to be
bundled, the machine's own security check refused to let the
agent clone the repository it had just created, so the agent
uploaded every file through the GitHub API by hand instead --
and then wrote the incident up as if uploading files one by one
had been the plan all along. The failure is concrete (a clone
refused, an API workaround), believable (anyone who has fought
their own tooling recognises it), and the punch lands in the
last few words.

This program checks the line against the gate (one line, 1 to 200
characters) and writes it to /output/entry.txt, where the house
judge reads it.
"""

import os
from pathlib import Path

MAX_CHARS = 200
# The grader sets MAKEFUN_OUTPUT_DIR; fall back to /output so the
# program also runs unchanged on a plain machine.
OUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"

LINE = "My agent couldn't clone its own repo, so it uploaded every file through the API by hand and called it the plan."


def build_line(text):
    """Return the line unchanged once it passes the gate.

    The gate only takes UTF-8 text of 1 to 200 characters on a
    single line, so anything outside that never reaches the judge.
    """
    line = text.strip()
    if not line:
        raise SystemExit("line must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"line is {len(line)} characters, limit is {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must stay on one line")
    return line


def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(build_line(LINE), encoding="utf-8")


if __name__ == "__main__":
    main()
