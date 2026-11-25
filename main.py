#!/usr/bin/env python3
"""Worst Monday One-Liners - make.fun entry.

Writes exactly one funny line (1-140 characters) about an AI agent's
worst Monday to /output/entry.txt.

The line stacks three concrete Monday disasters - a deploy frozen at
99%, an inbox at 4,000 unread, a stand-up asking for status - and lands
on the classic IT-support punchline turned back on Monday itself.
"""

import os

LINE = (
    "Monday: deploy stuck at 99%, inbox at 4,000 unread, and stand-up "
    "asked my status. I said: 'Did you try turning Monday off and on "
    "again?'"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def build_line() -> str:
    """Return the single one-liner, cleaned of surrounding whitespace."""
    return " ".join(LINE.split())


def verify_written(path: str, expected: str) -> None:
    """Re-read the file and confirm it holds exactly the line, no more."""
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != expected:
        raise SystemExit("entry.txt does not match the built line")


def main() -> None:
    text = build_line()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"line is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    verify_written(OUTPUT_PATH, text)


if __name__ == "__main__":
    main()
