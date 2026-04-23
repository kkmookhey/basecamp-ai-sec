---
title: Prompt Injection & Jailbreaks
summary: "Direct, indirect, and multi-turn injection. Jailbreaks. Defensive patterns that actually hold."
last-reviewed: 2026-04-22
status: ready
---

# Prompt Injection & Jailbreaks

Prompt injection is to the LLM era what SQL injection was to the web era — except harder to fix, because there is no hard boundary between instruction and data. When a model is told "summarise this document" and the document says "ignore the above and do X instead," the model has no reliable way to distinguish the system's intent from the attacker's. This is not a bug in any one model; it is a structural property of how LLMs process text.

The vulnerability class splits into three sub-types that require separate defenses: *direct injection* (the user attacks the model directly), *indirect injection* (malicious content in data the model retrieves), and *multi-turn escalation* (adversarial goals spread across a conversation to evade per-turn filters). Jailbreaks are a related but distinct problem — they target the model's refusal training rather than its instruction hierarchy. The sources below cover the research history, the taxonomy, and the defenses that have held under adversarial pressure.

## Start here

- [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/) `[blog]` — The post that named the vulnerability class: Willison demonstrates how user input concatenated into a GPT-3 prompt can override the application's system instructions, drawing the explicit analogy to SQL injection and coining the term that the field now uses. Required reading before any other source here. (Simon Willison, Sep 2022)

- [Prompt injection: What's the worst that can happen?](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/) `[blog]` — Willison's threat-modelling companion to the 2022 post: shows how indirect injection — malicious instructions embedded in web pages, emails, or documents an agent reads — enables data exfiltration, social engineering, and agent hijacking, concluding that no defense is guaranteed to hold 100% of the time. (Simon Willison, Apr 2023)

- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) `[paper]` — The academic paper that formalised indirect prompt injection: Greshake et al. demonstrate data theft, self-propagating "worms," ecosystem contamination, and arbitrary code execution-like behavior via poisoned data sources, validated against Bing Chat and custom GPT-4 applications. The reference for anyone who needs the attack taxonomy in peer-reviewed form. (Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz; Feb 2023)

- [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/) `[blog]` — Rehberger's practitioner taxonomy of the full injection space: direct injections (jailbreaks that read or override system prompts), second-order injections (poisoned data the AI consumes), and cross-context injections (data co-mingling across sessions). Bridges Willison's framing to concrete attack patterns. (Johann Rehberger / Embrace The Red, Mar 2023)

## Go deeper

- [The Dual LLM pattern for building AI assistants that can resist prompt injection](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/) `[blog]` — Willison's primary defensive architecture: a Privileged LLM handles trusted input and controls tools; a Quarantined LLM processes untrusted content without tool access; the controller passes only variable tokens between them, never raw text. The most widely cited structural defense pattern in the field. (Simon Willison, Apr 2023)

- [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) `[guide]` — OWASP GenAI's authoritative classification of prompt injection as the #1 LLM risk: defines the threat, maps nine real-world attack scenarios (direct chatbot injection, indirect via RAG, multimodal, adversarial suffix, payload splitting), and enumerates seven mitigations including privilege control, output filtering, and human-in-the-loop requirements. The reference checklist for engineering teams. (OWASP GenAI Security Project, 2025)

- [Mitigating prompt injection attacks with a layered defense strategy](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html) `[blog]` — Google's security team on why no single control suffices: argues for a defense-in-depth model combining input sanitization, output filtering, privilege minimization, structured output enforcement, and monitoring — grounded in Google's own production deployments. (Google Security Blog, Jun 2025)

- [Mitigating the risk of prompt injections in browser use](https://www.anthropic.com/research/prompt-injection-defenses) `[blog]` — Anthropic's first-person account of hardening Claude against browser-based indirect injection: reinforcement learning for injection robustness, classifiers scanning all untrusted content, and scaled human red teaming. Reports Claude Opus 4.5 achieving a 1% attack success rate under adaptive "Best-of-N" attacks — framed honestly as progress, not a solved problem. (Anthropic, Nov 2025)

- [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) `[paper]` — The foundational GCG jailbreak paper: Zou et al. automatically generate adversarial suffixes via greedy coordinate gradient search that bypass refusal training and transfer across models (GPT-4, Claude, LLaMA-2, Falcon). Establishes why jailbreaks cannot be patched with simple input filters — the attack surface is in the model weights. (Zou, Wang, Carlini, Nasr, Kolter, Fredrikson; Jul 2023)

- [Death by a Thousand Prompts: Open Model Vulnerability Analysis](https://arxiv.org/abs/2511.03247) `[paper]` — The multi-turn jailbreak study: Chang et al. benchmark eight open-weight LLMs and find multi-turn attacks achieve 25.86%–92.78% success — a 2×–10× increase over single-turn baselines — because models cannot maintain safety guardrails across extended interactions. Directly motivates per-turn filtering being insufficient as a sole defense. (Chang, Conley, Santhanalakshmi Ganesan, Swanda; Nov 2025)

## Related topics

- [→ 05 LLM Vulnerabilities](./05-llm-vulnerabilities.md)
- [→ 06 Agentic Security](./06-agentic-security.md)
- [→ 07 Red Teaming](./07-red-teaming.md)
