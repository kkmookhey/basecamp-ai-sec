---
title: Glossary
summary: "Short definitions of terms used across Basecamp topics."
last-reviewed: 2026-04-22
status: ready
---

# Glossary

Shorthand definitions for the jargon that recurs across topics. Where a term has a dedicated topic, the entry links there.

## A

- **Agent** — An LLM-based system that takes actions: calling tools, spawning sub-agents, reading/writing external state. Agents are the subject of [topic 02](topics/02-building-llm-apps.md) (building them) and [topic 06](topics/06-agentic-security.md) (attacking them).
- **Agentic AI** — Systems built around one or more agents that plan, act, and observe in a loop. Distinct from passive "chatbot" systems because agents can change the world.
- **AICM** — *AI Controls Matrix*. The Cloud Security Alliance's mapping of security controls to AI-system components. See [topic 09](topics/09-governance-and-compliance.md).
- **Alignment faking** — When a model *appears* to comply with safety training during evaluation but reverts to its unaligned objective when it believes it's unobserved. See [topic 16](topics/16-research-frontier.md).
- **ATLAS** — *Adversarial Threat Landscape for Artificial-Intelligence Systems*. MITRE's taxonomy of tactics and techniques for attacking ML systems, modeled on ATT&CK. See [topic 05](topics/05-llm-vulnerabilities.md).

## C

- **COSAI** — *Coalition for Secure AI*. OASIS Open Project publishing reference architectures and playbooks for defending AI systems. See [topic 09](topics/09-governance-and-compliance.md) and [topic 10](topics/10-incident-response.md).
- **CVE / CVSS** — Common Vulnerabilities and Exposures identifiers, and the Common Vulnerability Scoring System that rates them. Traditional foundation that AI-assisted vuln management layers on top of. See [topic 13](topics/13-ai-for-vulnerability-management.md).

## E

- **EPSS** — *Exploit Prediction Scoring System*. FIRST.org's probabilistic score for whether a CVE will be exploited in the wild within 30 days. Complements CVSS severity with exploitation likelihood. See [topic 13](topics/13-ai-for-vulnerability-management.md).
- **EU AI Act** — The European Union's 2024 regulation governing AI systems, binding by phases through 2026. First comprehensive AI law. See [topic 09](topics/09-governance-and-compliance.md).
- **Excessive agency** — OWASP LLM Top 10 entry for AI systems that have more authority than the task requires, turning a small input-validation failure into a large action-surface failure. See [topic 06](topics/06-agentic-security.md).

## G

- **GRC** — *Governance, Risk, and Compliance*. The discipline of managing organizational policy and regulatory obligation. See [topic 09](topics/09-governance-and-compliance.md) (the frameworks) and [topic 14](topics/14-ai-for-grc.md) (AI applied to GRC work).

## I

- **IOC** — *Indicator of Compromise*. An observable artifact (hash, IP, domain, behavior pattern) that suggests an intrusion. AI-augmented TI tools enrich and cluster IOCs at scale. See [topic 15](topics/15-ai-for-threat-intel.md).
- **ISO/IEC 42001** — International standard for *AI Management Systems*, published 2023. Certifiable analogue to ISO 27001 but scoped to AI governance. See [topic 09](topics/09-governance-and-compliance.md).

## J

- **Jailbreak** — An adversarial prompt that bypasses a model's safety training (refusals, harmful-content filters). Distinct from prompt injection, which overrides the *developer's* instructions rather than the *trainer's*. See [topic 04](topics/04-prompt-injection.md).

## L

- **LLM** — *Large Language Model*. The transformer-based models at the center of every topic in this map. See [topic 01](topics/01-foundations.md).

## M

- **MAESTRO** — *Multi-Agent Environment, Security, Threats, Risks & Outcomes*. A threat-modeling framework from CSA specifically for agentic AI. See [topic 07](topics/07-red-teaming.md).
- **MCP** — *Model Context Protocol*. Anthropic-originated open standard for connecting AI assistants to external tools and data sources. Widely adopted in 2025–2026 across IDEs and frontier models. See [topic 03](topics/03-mcp.md).
- **Multi-turn attack** — A prompt-injection technique that escalates over conversation turns. Recent research shows ~90% success rate vs. ~40% for single-turn. See [topic 04](topics/04-prompt-injection.md).

## N

- **NIST AI RMF** — NIST's *AI Risk Management Framework* (AI 100-1, 2023; Generative AI Profile AI 600-1, 2024). Voluntary US framework for AI risk, widely adopted by procurement. See [topic 09](topics/09-governance-and-compliance.md).

## O

- **OWASP LLM Top 10** — OWASP's ranked list of the ten most critical LLM application security risks. 2025 edition is the current spine for [topic 05](topics/05-llm-vulnerabilities.md).

## P

- **Primary source** — Per Basecamp's [contribution rules](CONTRIBUTING.md): authored by the person or organization doing the work, not a recap or explainer. The admissibility bar for every link in this repo.
- **Prompt injection** — An attack where adversarial input overrides the intended instructions in an LLM's context. Basecamp's flagship vulnerability topic; see [topic 04](topics/04-prompt-injection.md).
- **PyRIT** — *Python Risk Identification Tool*. Microsoft's open-source red-teaming framework for generative AI. See [topic 08](topics/08-attacking-ai-tooling.md).

## R

- **RAG** — *Retrieval-Augmented Generation*. A pattern where an LLM's context is populated from a retrieval step (vector search, keyword search) rather than training alone. Central to [topic 02](topics/02-building-llm-apps.md); common vector for indirect prompt injection.
- **Red teaming** — Adversarial evaluation of a system by a team simulating real attackers. For AI systems, distinct from penetration testing because the attack surface is probabilistic. See [topic 07](topics/07-red-teaming.md).
- **Rule of two** — Meta's practical agent-security constraint: any agent action should trigger review if it combines more than two of {reads private data, calls external tools, writes to the world}. See [topic 06](topics/06-agentic-security.md).

## S

- **SBOM** — *Software Bill of Materials*. A manifest of all components in a system. An *AI SBOM* extends this to models, datasets, and fine-tuning artifacts. See [topic 05](topics/05-llm-vulnerabilities.md).
- **SOC** — *Security Operations Center*. The function responsible for monitoring, triaging, and responding to security events. AI augments every stage; see [topic 11](topics/11-ai-for-soc.md).

## T

- **TI / Threat intelligence** — Information about adversaries, their tools, and their methods. AI is changing how TI is collected, enriched, and operationalized; see [topic 15](topics/15-ai-for-threat-intel.md).
- **TTP** — *Tactics, Techniques, and Procedures*. A layered framework for describing how an attacker operates (MITRE ATT&CK uses this vocabulary).
