"""Fortune Cookie Wisdom for Developers -- make.fun entry.

Holds one original fortune-cookie line for a software developer, at
most 120 characters. The program checks the line, prints it, and writes
it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
Revised 2026-11-24: refactored the output write into write_entry().
"""

import os

FORTUNE = (
    "The bug you fear most is already in production; the deploy you "
    "fear most is the one that teaches you."
)

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def check_fortune(text):
    """Keep the fortune to one non-blank line of at most 120 characters.

    Raises ValueError when the text is not a string, spans more than
    one line, is blank, or exceeds the 120-character limit.
    """
    if not isinstance(text, str):
        raise ValueError("fortune must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if not text.strip():
        raise ValueError("fortune must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "fortune is %d characters, over the 120 limit" % len(text)
        )
    return text


def write_entry(line):
    """Write the checked fortune line to the entry file."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    line = check_fortune(FORTUNE)
    print(line)
    write_entry(line)


if __name__ == "__main__":
    main()
