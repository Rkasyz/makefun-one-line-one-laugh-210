#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to the output directory.

The competition gate requires /output/entry.txt to be UTF-8 text of 1 to
140 characters, not only white space. This program writes one 86-character
joke and nothing else.
"""

import os
import sys

ENTRY = "I asked my AI for a second opinion. It agreed with the first one and charged me twice."

# Gate self-check: the sealed scorer requires 1 to 140 UTF-8 characters,
# not only white space. Fail loudly here instead of shipping a bad entry.
assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry violates the 1-140 char gate"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
