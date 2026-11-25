#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

The program's whole job: write the entry line to /output/entry.txt
(the file the sealed gate checks and the judge reads) and print it.
"""

import os

# The line is built from its two beats: the setup names the machine premise
# (autocomplete finishing what you type) and the punch turns "ending" into
# both the end of a sentence and the end of a life story.
SETUP = "Are you my autocomplete? Because I started typing my future,"
PUNCH = "and you were the only ending I want."
ENTRY = f"{SETUP} {PUNCH}"


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-200 characters of
    # single-line, non-whitespace UTF-8 text.
    assert 1 <= len(ENTRY) <= 200, "entry must fit the 200 character gate"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
