"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes one short, funny rant about an everyday annoyance to
``<OUTPUT_DIR>/entry.txt``. The rant is fixed text, so the output is
byte-identical on every run. Standard library only, no network.
"""

import os
from pathlib import Path

RANT = (
    "Every app update moves the buttons I finally learned. "
    "I open an app I have used for two years and the send button "
    "is hiding in a menu, the settings live in a drawer, and the "
    "one thing I tap daily is just gone. "
    "I never asked for a new layout. I asked for the app to work. "
    "Give me my buttons back, you cowards."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(RANT, encoding="utf-8")


if __name__ == "__main__":
    main()
