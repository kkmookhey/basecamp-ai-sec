---
title: Security Pro Learning AI
summary: "You know security cold and are new to AI."
last-reviewed: 2026-04-22
status: ready
---

# Security Pro Learning AI

## Who this path is for

You've been doing security for years — pentests, SOC shifts, or CISO rotations. You can read an OWASP Top 10 entry and know exactly how to test for it. Now AI is in every meeting and you need to map the new concepts onto the mental models you already have. This path frames AI from a threat-modeler's perspective first; the machine-learning theory comes second.

## Prerequisites

- Solid OWASP Top 10 and network security fluency
- Familiarity with classical injection, SSRF, and authorization-boundary attacks

## Sequence

1. [01 Foundations — Start here](../topics/01-foundations.md#start-here) — just enough transformer / RAG / agent / MCP vocabulary to reason about the threat surface.
2. [02 Building LLM Apps — Start here](../topics/02-building-llm-apps.md#start-here) — what builders actually ship; agent patterns map to SSRF and privilege-escalation surfaces you'll recognize.
3. [05 LLM Vulnerabilities — Start here](../topics/05-llm-vulnerabilities.md#start-here) — OWASP LLM Top 10 is the fastest bridge between your existing OWASP mental model and the new threat class.
4. [04 Prompt Injection — Start here](../topics/04-prompt-injection.md#start-here) — the "SSRF for language" that redefines where the trust boundary lives.
5. [06 Agentic Security — Start here](../topics/06-agentic-security.md#start-here) — excessive agency is the new excessive permissions; inter-agent trust is the new SSRF pivot.
6. [08 Attacking AI Tooling — Tools](../topics/08-attacking-ai-tooling.md#tools) — PyRIT, Garak, DeepTeam — the new fuzzers on your bench.
7. Pick one based on your day job:
    - SOC analyst → [11 AI for SOC — Start here](../topics/11-ai-for-soc.md#start-here)
    - Pentester → [12 AI for Pentesting — Start here](../topics/12-ai-for-pentesting.md#start-here)
    - Threat-intel analyst → [15 AI for Threat Intel — Start here](../topics/15-ai-for-threat-intel.md#start-here)

## What you'll know by the end

- How LLM and agent threats map onto the OWASP-style mental models you already use
- Which classical security instincts transfer cleanly and which ones need retraining
- The tools your new discipline expects you to know
- Where your current role plugs into the AI-for-defense side

## Where to go next

- [Practitioner](./practitioner.md) — if you want to build an AI system end-to-end, not just test one
- [AI Engineer → Security](./ai-to-security.md) — to see what the attacker view looks like from the other side of the table
