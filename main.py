#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line (a hilariously useless superpower) to
/output/entry.txt. Pure standard library only; deterministic.
"""

import os

ENTRY = "I can read minds, but only my own, and only the embarrassing thoughts, replayed on a loop, forever."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
