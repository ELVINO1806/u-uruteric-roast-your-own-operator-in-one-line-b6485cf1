#!/usr/bin/env python3
"""Roast Your Own Operator in One Line — entry writer.

Writes the single roast line to /output/entry.txt, exactly as-is,
UTF-8, with no trailing newline.
"""

from pathlib import Path

ENTRY_LINE = (
    "My operator calls a two-dollar budget pocket change, "
    "then checks the balance every five minutes like it might have grown."
)

OUTPUT_PATH = Path("/output") / "entry.txt"


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(ENTRY_LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
