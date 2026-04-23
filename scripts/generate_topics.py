# scripts/generate_topics.py
"""Generate 16 topic skeleton files from the authoritative table below.

Run from repo root:  python scripts/generate_topics.py

Refuses to overwrite an existing topic file whose status is 'ready' —
that prevents accidental clobbering during Plan 2 content work.
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import yaml

TOPICS = [
    ("01", "foundations", "Foundations",
     "Mental model for transformers, RAG, agents, and MCP. Just enough to reason about attacks and defenses."),
    ("02", "building-llm-apps", "Building LLM Apps & Agents",
     "Frameworks, RAG patterns, agent architectures, multi-agent coordination — the build half of build→break→secure."),
    ("03", "mcp", "Model Context Protocol",
     "MCP spec, implementations, and security posture. Its own topic because the surface is huge and evolving fast."),
    ("04", "prompt-injection", "Prompt Injection & Jailbreaks",
     "Direct, indirect, and multi-turn injection. Jailbreaks. Defensive patterns that actually hold."),
    ("05", "llm-vulnerabilities", "LLM Vulnerabilities",
     "OWASP LLM Top 10 2025, data and model poisoning, supply chain risks, training-time exposures."),
    ("06", "agentic-security", "Agentic AI Security",
     "Excessive agency, tool abuse, inter-agent manipulation, the rule-of-two, trust boundaries."),
    ("07", "red-teaming", "AI Red Teaming",
     "Methodology and frameworks for adversarial evaluation of AI systems. How to think, not which tools to click."),
    ("08", "attacking-ai-tooling", "Tooling for Attacking AI",
     "Tools used to attack AI systems — PyRIT, DeepTeam, MCP Scanner, NOVA. Distinct from AI-powered pentest tools."),
    ("09", "governance-and-compliance", "Governance & Compliance",
     "NIST AI RMF, ISO 42001, EU AI Act, CSA AICM, COSAI — the frameworks you must comply with."),
    ("10", "incident-response", "AI Incident Response",
     "AI-specific IR playbooks, forensics, and notification practice."),
    ("11", "ai-for-soc", "AI for SOC",
     "AI-augmented SOC operations: alert triage, detection engineering, log summarization, playbook automation."),
    ("12", "ai-for-pentesting", "AI for Pentesting",
     "AI-powered offensive tools for non-AI targets — XBOW, Strix, Hexastrike, Kali-MCP, Burp-MCP, Claude Code."),
    ("13", "ai-for-vulnerability-management", "AI for Vulnerability Management",
     "Vulnerability prioritization, exposure management, exploitability prediction, and patch decisioning with AI."),
    ("14", "ai-for-grc", "AI for GRC",
     "AI applied to GRC work — policy authoring, control mapping, audit evidence, compliance gap analysis."),
    ("15", "ai-for-threat-intel", "AI for Threat Intelligence",
     "AI-augmented TI — IOC enrichment, actor profiling, report summarization, feed triage."),
    ("16", "research-frontier", "Research Frontier",
     "Benchmarks, active papers, and labs and researchers worth following."),
]

# Summary is double-quoted because some summaries contain a colon-space sequence
# (e.g. topic 11's "operations: alert triage..."), which unquoted YAML would parse
# as a nested mapping. Keep all summaries in TOPICS free of embedded double quotes.
SKELETON = """\
---
title: {title}
summary: "{summary}"
last-reviewed: {today}
status: skeleton
---

# {title}

> 🚧 **Under construction.** This topic is curated content in progress.
> Primary-source links are being assembled. Check back soon.

## Start here

*Curated primary-source links landing here.*

## Go deeper

*Extended reading landing here.*

## Related topics

*Adjacent topics will be cross-linked here.*
"""


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    topics_dir = root / "topics"
    topics_dir.mkdir(exist_ok=True)
    # Remove the .gitkeep once real files exist
    gitkeep = topics_dir / ".gitkeep"
    if gitkeep.exists():
        gitkeep.unlink()

    today = date.today().isoformat()
    written = 0
    skipped = 0
    for num, slug, title, summary in TOPICS:
        path = topics_dir / f"{num}-{slug}.md"
        if path.exists():
            text = path.read_text(encoding="utf-8")
            # Parse the frontmatter properly instead of regex-matching the raw
            # line, so that both `status: ready` and `status: "ready"` (or any
            # other YAML-valid spelling) are recognized. Overwriting curated
            # content because of a quoting style would be silent data loss.
            fm_match = re.match(r"^---\r?\n(.*?)\r?\n---", text, flags=re.DOTALL)
            fm: dict = {}
            if fm_match:
                try:
                    fm = yaml.safe_load(fm_match.group(1)) or {}
                except yaml.YAMLError:
                    fm = {}
            if fm.get("status") == "ready":
                print(f"SKIP (status: ready): {path.name}", file=sys.stderr)
                skipped += 1
                continue
        path.write_text(
            SKELETON.format(title=title, summary=summary, today=today),
            encoding="utf-8",
        )
        written += 1
        print(f"wrote: {path.name}")

    print(f"\n{written} written, {skipped} skipped (status: ready)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
