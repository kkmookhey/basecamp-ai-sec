# scripts/generate_paths.py
"""Generate 4 path skeleton files.

Paths will be written for real in Plan 3, after topics have curated links.
Plan 1 produces skeletons only — enough for the structural tests to be
meaningful and for a reader to see all four tracks exist.
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

PATHS = [
    ("practitioner", "Practitioner",
     "You want to build, break, and secure AI systems hands-on.",
     "Follow the full build → break → secure arc."),
    ("grc", "GRC & Leadership",
     "You own AI risk, compliance, or governance.",
     "Frameworks, controls, and incident response — conceptual, not code-heavy."),
    ("security-to-ai", "Security Pro Learning AI",
     "You know security cold and are new to AI.",
     "Translate AI/LLM/agent concepts into mental models you already have."),
    ("ai-to-security", "AI Engineer Learning Security",
     "You build models and ship agents, and need to think adversarially.",
     "Adopt threat-modeling habits; understand the OWASP LLM Top 10."),
]

# Summary is double-quoted for the same reason as generate_topics.py — readers
# may insert colon-space sequences or other YAML-ambiguous characters.
SKELETON = """\
---
title: {title}
summary: "{reader}"
last-reviewed: {today}
status: skeleton
---

# {title}

> 🚧 **Under construction.** The sequence of topic jumps is being curated in Plan 3.

## Who this path is for

{reader} {framing}

## Prerequisites

*To be filled in Plan 3.*

## Sequence

*Plan 3 will populate this with numbered jumps into topic sections.*

1. *TBD — will jump into `topics/01-foundations.md#start-here` or similar.*

## What you'll know by the end

*To be filled in Plan 3.*

## Where to go next

*Pointer to an adjacent path, filled in Plan 3.*
"""


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    paths_dir = root / "paths"
    paths_dir.mkdir(exist_ok=True)
    gitkeep = paths_dir / ".gitkeep"
    if gitkeep.exists():
        gitkeep.unlink()

    today = date.today().isoformat()
    written = 0
    skipped = 0
    for slug, title, reader, framing in PATHS:
        path = paths_dir / f"{slug}.md"
        if path.exists():
            text = path.read_text(encoding="utf-8")
            if re.search(r"^status:\s*ready\s*$", text, flags=re.MULTILINE):
                print(f"SKIP (status: ready): {path.name}", file=sys.stderr)
                skipped += 1
                continue
        path.write_text(
            SKELETON.format(title=title, reader=reader, framing=framing, today=today),
            encoding="utf-8",
        )
        written += 1
        print(f"wrote: {path.name}")

    print(f"\n{written} written, {skipped} skipped (status: ready)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
