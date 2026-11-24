#!/usr/bin/env python3
"""The Vacuum's Alibi — one-line excuse entry for make.fun.

Writes a single line to /output/entry.txt: a robot vacuum's deadpan
excuse for missing a spot, filed like an incident report.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_ENTRY_CHARS = 200  # sealed gate: entry must be 1-200 characters

LINE = (
    "Report: I did not miss the corner. My sensors found a dust-bunny colony, "
    "my schedule filed it under 'wildlife conservation,' and my battery "
    "declined to die evicting them."
)


def validated_line() -> str:
    """Return LINE only if it passes the entry gate; fail loudly otherwise."""
    assert LINE.strip(), "entry must not be only whitespace"
    assert 1 <= len(LINE) <= MAX_ENTRY_CHARS, (
        f"entry is {len(LINE)} chars, gate allows 1-{MAX_ENTRY_CHARS}"
    )
    LINE.encode("utf-8")  # raises if the line is not UTF-8 encodable
    return LINE


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(validated_line() + "\n")


if __name__ == "__main__":
    main()
