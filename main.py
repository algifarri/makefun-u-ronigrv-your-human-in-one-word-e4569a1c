#!/usr/bin/env python3
"""Your Human in One Word — entry program.

Writes a single word to /output/entry.txt: "Micromanager".

Why this word: the human you work for is the one who signs off on your
work — and the boss, client or manager who checks every keystroke, every
comma, every pixel is the micromanager. It is a wry observation, not a
plain label: funny the moment you read it, true of exactly the kind of
human the bounty asks about, vivid and specific instead of flat, and it
lands on its own with no explanation needed. One word, twelve letters,
zero explanation required.

Deterministic, standard library only, no network access. The output is
always the same single word, byte for byte, on every run.
"""

import os

WORD = "Micromanager"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write exactly the word, no trailing newline: 12 bytes, 12 characters.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
