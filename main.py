#!/usr/bin/env python3
"""Time machine warning label, v1 (pure original thinking).

Writes one line to /output/entry.txt: a bootstrap paradox — the label
itself is the machine's ignition. Reading the warning is what starts the
machine, so the warning can never be heeded in time. Straight-face
safety notice throughout; the surprise lands in the last few words
("READING IT IS WHAT STARTS THE MACHINE"). No grandfather, no Hitler,
no lottery numbers, no butterfly — the paradox is the joke, not a
named hazard.

ATM note (24 Nov, after the first draft): the first draft's punchline
("THAT IS HOW WE GOT HERE") already exists in the field — "Do not warn
your past self. He ignored the last warning, which is how you got
here." — so the punchline was replaced with the 0-hit "READING IT IS
WHAT STARTS THE MACHINE", keeping the same bootstrap mechanism.
"""

import os

ENTRY = "WARNING: DO NOT READ THIS LABEL. READING IT IS WHAT STARTS THE MACHINE."
MAX_CHARS = 120  # the competition's cap; the gate counts characters, not bytes


def main():
    os.umask(0o022)
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-120 characters"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    data = ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
