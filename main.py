#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis.

Deterministic program: writes the funniest single-line diagnosis an AI
therapist hands its human (200 characters or fewer) to entry.txt.
Stdlib only, no network, no randomness, no model calls — the same line
every run.
"""

import os
from pathlib import Path

# The diagnosis: tab-hoarding. Relatable, specific, and the prescription
# is the joke — one tab a day, plus the admission nobody wants to make.
LINE = (
    "Diagnosis: acute tab-hoarding — 47 tabs open, none closed since "
    "2019. Prescription: close one tab a day and admit you'll never "
    "read any of them."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
