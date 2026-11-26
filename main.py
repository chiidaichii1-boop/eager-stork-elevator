#!/usr/bin/env python3
"""What the Elevator Would Say.

Writes a single funny line, spoken in the elevator's own voice,
to entry.txt in the output directory.
"""

import os

LINE = (
    "You all gossip about each other the second my doors close "
    "- and I carry every secret to the top floor."
)


def main() -> None:
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
