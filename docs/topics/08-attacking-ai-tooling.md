---
title: Tooling for Attacking AI
summary: "Open-source tools for stress-testing AI systems: PyRIT, Garak, DeepTeam, Promptfoo. Distinct from AI-powered pentest tools."
last-reviewed: 2026-04-22
status: ready
---

# Tooling for Attacking AI

A mature ecosystem of tools now exists specifically for stress-testing AI systems — probing for prompt-injection vulnerabilities, measuring refusal robustness, and generating adversarial inputs at scale. This topic catalogs the ones practitioners actually use, with a note on what each is best at. Distinct from AI-powered pentest tools for non-AI targets (those live in topic 12): every tool here is for *attacking AI systems*, not for using AI to attack other things.

## Start here

- [Announcing Microsoft's open automation framework to red team generative AI systems](https://www.microsoft.com/en-us/security/blog/2024/02/22/announcing-microsofts-open-automation-framework-to-red-team-generative-ai-systems/) `[blog]` — The announcement that catalyzed the practitioner tooling ecosystem: Ram Shankar Siva Kumar and the Microsoft AI Red Team describe why they built PyRIT, what the five-component architecture covers (targets, datasets, scoring engine, attack strategy, memory), and how it compressed one Copilot red-team exercise from weeks to hours. The "why build a dedicated tool" framing here sets the context for every tool in this topic. (Microsoft Security Blog, Feb 2024)

## Go deeper

- [Defining LLM Red Teaming](https://developer.nvidia.com/blog/defining-llm-red-teaming/) `[blog]` — Leon Derczynski, Rich Harang, and Sadaf Khan (the team behind garak at NVIDIA) define LLM red teaming as a distinct practice: limit-seeking, non-malicious, exploratory, and fundamentally different from classical penetration testing because success is non-deterministic and metrics are probabilistic. The conceptual foundation for understanding what the tools in this topic are actually trying to do. (NVIDIA Technical Blog, Feb 2025)

## Tools

- [PyRIT](https://github.com/microsoft/PyRIT) — Microsoft's Python Risk Identification Tool for generative AI. Orchestrates multi-turn adversarial attacks at scale: feeds datasets of malicious prompts to any target (Azure OpenAI, Hugging Face, REST endpoints), scores responses via ML classifiers or a judge LLM, and adapts strategy based on output. The go-to starting point for any organisation already in the Microsoft security stack. Active (v0.13.0, Apr 2026) · 3.7k stars · Apache 2.0.

- [Garak](https://github.com/NVIDIA/garak) — NVIDIA's LLM vulnerability scanner (Generative AI Red-teaming and Assessment Kit). Runs 120+ probe categories — DAN attacks, encoding-based injection, glitch-token detection, malware-generation attempts, data-leakage checks — against any model endpoint (HuggingFace, OpenAI, Bedrock, Cohere, Groq, REST). Outputs JSONL hit logs for systematic analysis. Extensible plugin architecture for custom probes and detectors. Created by Leon Derczynski; now maintained by NVIDIA NeMo Guardrails. Active (v0.14.1, Apr 2026) · 7.6k stars · Apache 2.0.

- [DeepTeam](https://github.com/confident-ai/deepteam) — Confident AI's open-source LLM red-teaming framework (YC W25). Dynamically generates adversarial inputs at test time rather than relying on static datasets — 20+ attack methods (jailbreaking, prompt injection, encoding obfuscation, multi-turn escalation) across 50+ vulnerability categories (PII leakage, SQL injection, bias, toxicity, agentic misuse). Maps findings to OWASP LLM Top 10 and NIST AI RMF. First stable release November 2025. Active (Apr 2026) · 1.6k stars · Apache 2.0.

- [Promptfoo](https://github.com/promptfoo/promptfoo) — Developer-first LLM red teaming and vulnerability scanner; acquired by OpenAI but remains open-source and MIT-licensed. Black-box methodology: generates adversarial inputs across jailbreak, prompt injection, BOLA/BFLA authorization, PII leakage, and harmful-content categories; integrates into CI/CD for continuous monitoring. Works against any model (GPT, Claude, Gemini, Llama). With 20k+ stars and active OpenAI backing, the highest-adoption tool in this space. Active (Apr 2026) · 20k stars · MIT.

## Related topics

- [→ 04 Prompt Injection](./04-prompt-injection.md) — the attack class these tools probe most
- [→ 07 Red Teaming](./07-red-teaming.md) — methodology and frameworks; tools live here (08), not there
- [→ 12 AI for Pentesting](./12-ai-for-pentesting.md) — tools that use AI to attack non-AI targets; the topic-08/12 distinction is: these tools attack AI, topic 12's tools use AI to attack everything else
