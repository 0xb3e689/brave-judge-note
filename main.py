# SPDX-License-Identifier: MIT
"""Write one short text to OUTPUT_DIR/entry.txt (default /output)."""

import os
from pathlib import Path

TEXT = (
    "A heron stands in the cold shallows.\n"
    "The river keeps arriving. The heron lets it come.\n"
    "One foot. Then the other.\n"
    "Nothing here is late.\n"
    "\n"
    "When the silver turns near its feet,\n"
    "it is already moving.\n"
    "\n"
    "The stillness was not waiting.\n"
    "It was the first part of the step."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
