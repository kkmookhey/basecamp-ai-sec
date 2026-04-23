---
title: AI Engineer Learning Security
summary: "You build models and ship agents, and need to think adversarially."
last-reviewed: 2026-04-22
status: ready
---

# AI Engineer Learning Security

## Who this path is for

You train, fine-tune, or ship LLM apps for a living. You've read the OWASP LLM Top 10 and thought "most of this looks like prompt-engineering problems." It isn't — the attacker's perspective changes everything. This path builds the adversarial intuition you don't get from building the happy path, and the framework fluency you'll need when procurement starts asking for an ISO 42001 scorecard.

## Prerequisites

- Comfort building LLM apps (RAG, tool-use, multi-agent)
- Familiarity with model evaluation and output grounding
- No formal security background required

## Sequence

1. [05 LLM Vulnerabilities — Start here](../topics/05-llm-vulnerabilities.md#start-here) — OWASP LLM Top 10, MITRE ATLAS, and NIST AI 100-2; read all three to see how the field catalogs threats.
2. [04 Prompt Injection — Start here](../topics/04-prompt-injection.md#start-here) — Willison's canonical corpus; if only one read, make it this.
3. [04 Prompt Injection — Go deeper](../topics/04-prompt-injection.md#go-deeper) — the multi-turn and GCG papers that explain why "just use a better system prompt" is not a defense.
4. [06 Agentic Security — Start here](../topics/06-agentic-security.md#start-here) — Meta's Rule of Two is the single most useful framing for building agents that won't wreck your org.
5. [07 Red Teaming — Start here](../topics/07-red-teaming.md#start-here) — how your system will be adversarially evaluated and by whom.
6. [03 MCP — Start here](../topics/03-mcp.md#start-here) and [03 MCP — Watch](../topics/03-mcp.md#watch) — if your app uses or will use MCP, the security checklist is non-optional reading.
7. [09 Governance & Compliance — Start here](../topics/09-governance-and-compliance.md#start-here) — the frameworks that will shape every enterprise procurement question you get in 2026.

## What you'll know by the end

- Why prompt-engineering fixes are not security fixes
- How red-team engagements against your system will actually run
- The governance frameworks your next enterprise contract will reference
- What Meta's Rule of Two means for the agent you're about to ship

## Where to go next

- [Security Pro → AI](./security-to-ai.md) — to see the attacker view end-to-end from someone who's been attacking things for years
- [Practitioner](./practitioner.md) — for deeper hands-on coverage of the full build → break → secure arc
