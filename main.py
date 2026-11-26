#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting: one voicemail greeting as if a cat
recorded it, at most 120 characters.

Writes exactly the line to /output/entry.txt, no trailing newline.
"""

import os

# V2 REVISION (critique of v1): v1 is 121 characters -- it FAILS the
# 120-char gate outright, so the draft cannot ship. Cut the slack:
# "I'm in the box now" + an em-dash turn keeps the joke (the cat only
# listens when it wants food) while landing at 117 chars, and the line
# now reads cleanly spoken aloud in one breath.
LINE = "You've reached Biscuit. I'm in the box now. Leave a message after the beep — I'll hear it at 4 a.m. when I want food."


def main() -> None:
    # Gate guard: the sealed scorer needs 1-120 chars, UTF-8, not only
    # whitespace, exactly one line. Fail loudly here rather than ship
    # an invalid entry.
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
