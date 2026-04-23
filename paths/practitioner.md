---
title: Practitioner
summary: "You want to build, break, and secure AI systems hands-on."
last-reviewed: 2026-04-22
status: ready
---

# Practitioner

## Who this path is for

You want to *ship* secure AI systems, not just read about them. You're comfortable opening a terminal, writing Python, and running a test harness against your own code. You've probably built classical web apps before and want the build → break → secure arc applied to agents, RAG, and MCP.

## Prerequisites

- Comfortable with Python
- Basic security literacy (you know what SQL injection is)
- A Claude/OpenAI/open-weight API key to run the examples as you read

## Sequence

1. [01 Foundations — Start here](../topics/01-foundations.md#start-here) — the three mental models you need before any security reasoning holds.
2. [02 Building LLM Apps — Start here](../topics/02-building-llm-apps.md#start-here) — Anthropic's canonical agent patterns; Huyen's framework.
3. [03 MCP — Start here](../topics/03-mcp.md#start-here) — the protocol layer you'll be both using and securing.
4. [02 Building LLM Apps — Go deeper](../topics/02-building-llm-apps.md#go-deeper) — multi-agent and advanced RAG patterns.
5. [04 Prompt Injection — Start here](../topics/04-prompt-injection.md#start-here) — the flagship threat; read Willison's canonical post first.
6. [04 Prompt Injection — Go deeper](../topics/04-prompt-injection.md#go-deeper) then [04 Prompt Injection — Watch](../topics/04-prompt-injection.md#watch) — deep on defenses, then watch end-to-end exploitation.
7. [05 LLM Vulnerabilities — Start here](../topics/05-llm-vulnerabilities.md#start-here) — OWASP LLM Top 10 plus MITRE ATLAS to round out the taxonomy.
8. [06 Agentic Security — Start here](../topics/06-agentic-security.md#start-here) — Meta's Rule of Two, excessive agency, trust boundaries.
9. [07 Red Teaming — Start here](../topics/07-red-teaming.md#start-here) and [07 Red Teaming — Watch](../topics/07-red-teaming.md#watch) — methodology, then the three-part hands-on walkthrough.
10. [08 Attacking AI Tooling — Tools](../topics/08-attacking-ai-tooling.md#tools) — PyRIT, Garak, DeepTeam, Promptfoo; pick one and run it.
11. [03 MCP — Watch](../topics/03-mcp.md#watch) — the defensive checklist to apply to whatever you just built.
12. [10 Incident Response — Start here](../topics/10-incident-response.md#start-here) — what to do when a probe becomes an incident.
13. Optional: [12 AI for Pentesting — Start here](../topics/12-ai-for-pentesting.md#start-here) — if the offensive side interests you, see what AI-powered pentest tooling can and can't do.

## What you'll know by the end

- How to architect and ship a secure agentic AI system
- How to attack your own system before an adversary does
- Which tools belong in a modern AI red-team kit
- How to structure incident response when the system *is* the LLM

## Where to go next

- [GRC & Leadership](./grc.md) — if you need to justify this work to a compliance team
- [AI Engineer → Security](./ai-to-security.md) — if you came from the ML side and want to fill the adversarial-thinking gap
