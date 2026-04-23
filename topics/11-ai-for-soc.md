---
title: AI for SOC
summary: "AI-augmented SOC operations: alert triage, detection engineering, log summarization, playbook automation."
last-reviewed: 2026-04-22
status: ready
---

# AI for SOC

The SOC of 2026 runs on alert volume that no human team can triage linearly. AI-augmentation has moved from "copilot" to "tier-1 automation" at pace; the architectural questions now are: what does the LLM actually read, what authority does it have, how do you measure a false-negative you never saw. The sources below are the ones that describe those choices, not the vendor landing pages that promise them.

## Start here

- [What is Microsoft Security Copilot?](https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot) `[docs]` — Microsoft's canonical technical overview of Security Copilot: describes the grounding pipeline (prompt preprocessing via plugins before the LLM call, then post-processing with additional plugin context), how Microsoft Defender XDR, Sentinel, and Intune feed event logs, alerts, and incidents into the system, and how natural language translates to KQL queries and incident summaries. The architectural description of what the LLM actually reads — and what it doesn't — is here, not on the product marketing page. (Microsoft; updated Apr 2026)

- [Behind the scenes of Elastic Security's generative AI features](https://www.elastic.co/blog/elastic-security-generative-ai-features) `[blog]` — Chang and Jaramillo describe the engineering reality of building AI Assistant and Attack Discovery at production scale: the LangGraph agent architecture, LangSmith tracing and debugging infrastructure, the five-component evaluation framework (attack-scenario test datasets, tracing, rubrics, scoring, threshold enforcement), and the 85%-accuracy gate that blocks prompt changes from shipping. The honest account of how a vendor actually iterates on LLM-backed security features — and what falls out when the evaluation framework finds a regression. (Elastic; Feb 2025)

- [CTI-REALM: A new benchmark for end-to-end detection rule generation with AI agents](https://www.microsoft.com/en-us/security/blog/2026/03/20/cti-realm-a-new-benchmark-for-end-to-end-detection-rule-generation-with-ai-agents/) `[blog]` — Chakraborty (Microsoft Security) introduces CTI-REALM: 37 real threat intelligence reports, telemetry from Linux endpoints, AKS, and Azure cloud, and a multi-step agent evaluation that covers CTI comprehension → MITRE mapping → data source identification → KQL query construction → Sigma rule generation → validation against ground-truth attack telemetry. The first rigorous benchmark for detection-engineering copilots; the results (cloud detection hardest, CTI-specific tooling worth +0.150 score points, small models close a third of the gap with human-authored workflow guidance) give practitioners actual numbers to argue against before deploying AI-generated detections in production. (Microsoft; Mar 2026)

## Go deeper

- [CORTEX: Collaborative LLM Agents for High-Stakes Alert Triage](https://arxiv.org/abs/2510.00311) `[paper]` — Wei, Tay, Liu, Pan, Luo, Zhu, and Jordan present CORTEX: a divide-and-conquer multi-agent architecture where a behavior-analysis agent inspects activity sequences, evidence-gathering agents query SIEM logs and threat intelligence, and a reasoning-and-coordination agent synthesizes auditable decisions — contrasted with single-model systems that hallucinate when facing noisy enterprise telemetry. Evaluated on a production-sourced dataset of documented analyst actions and tool outputs; substantially reduces false positives and improves investigation quality over state-of-the-art single-agent LLMs. The architecture paper for understanding why multi-agent triage outperforms a single prompted LLM. (George Mason University; arXiv 2510.00311; Sep 2025)

- [LLMs in the SOC: An Empirical Study of Human-AI Collaboration in Security Operations Centres](https://arxiv.org/abs/2508.18947) `[paper]` — Singh, Tariq, Jalalvand, Baruwal Chhetri, Nepal, Paris, and Lochner (CSIRO + eSentire) analyze 3,090 real analyst queries submitted to GPT-4 over 10 months across 45 SOC analysts at a managed detection and response firm. Key finding: 93% of queries map to NICE Framework cybersecurity competencies; analysts treat LLMs as on-demand sensemaking aids rather than decision-makers (only 4% of queries seek explicit recommendations); 75% of conversations are 2-3 turns, showing targeted use not exploratory dialogue. The empirical baseline for what analysts actually ask LLMs, which is the prerequisite for knowing what "AI-augmented SOC" actually means in production. (CSIRO / eSentire; arXiv 2508.18947; Aug 2025)

- [Evaluating LLM Generated Detection Rules in Cybersecurity](https://arxiv.org/abs/2509.16749) `[paper]` — Bertiger, Filar, Luthra, Meschiari, Mitchell, Scholten, and Sharath (Sublime Security) introduce an open-source evaluation framework and holdout-set methodology for measuring LLM-generated detection rules against a human-authored corpus, using three expert-inspired metrics. Applied to Sublime Security's Automated Detection Engineer (ADE) system. Accepted at CAMLIS 2025. The missing measurement layer for any organization considering AI-generated detections: how do you tell whether the LLM's rule is any good before it runs in production? (Sublime Security; CAMLIS 2025; Sep 2025)

- [Crawl, Walk, Run: A Practitioner's Guide to AI Maturity in the SOC](https://techcommunity.microsoft.com/blog/microsoft-security-blog/crawl-walk-run-a-practitioners-guide-to-ai-maturity-in-the-soc/4500433) `[blog]` — kfriedemann (Microsoft Security) maps the three-stage AI adoption arc for SOC teams: Crawl (approved chatbots as research assistants, conversational augmentation without automation), Walk (LLMs embedded in bounded workflows via automation platforms with constrained inputs and human oversight at decision points), Run (earned autonomy for agentic operations, with human-in-the-loop preserved for high-impact actions). Concrete guidance on what governance and measurement must precede each stage. The practitioner maturity model for teams trying to move past "we have a copilot license" to "we know what AI is authorised to do in our SOC." (Microsoft; Mar 2026)

## Related topics

- [→ 10 AI Incident Response](./10-incident-response.md)
- [→ 12 AI for Pentesting](./12-ai-for-pentesting.md)
- [→ 15 AI for Threat Intel](./15-ai-for-threat-intel.md)
