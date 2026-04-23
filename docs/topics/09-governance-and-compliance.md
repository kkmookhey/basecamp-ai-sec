---
title: Governance & Compliance
summary: "NIST AI RMF, ISO 42001, EU AI Act, CSA AICM, COSAI — the frameworks you must comply with."
last-reviewed: 2026-04-22
status: ready
---

# Governance & Compliance

Three frameworks dominate the AI compliance landscape: NIST AI RMF (US, voluntary, risk-based), ISO/IEC 42001 (international, certifiable), and the EU AI Act (EU law, binding by 2026). CSA's AICM provides technical controls; COSAI assembles defender-side reference architectures. Every AI GRC conversation starts by picking which of these applies to you — and most large organizations will need to satisfy more than one simultaneously.

Note: NIST AI 100-2 (Adversarial ML taxonomy) is a separate document that lives in topic 05. This topic covers the risk management and compliance frameworks: AI 100-1, AI 600-1, and the international standards landscape.

## Start here

- [Artificial Intelligence Risk Management Framework (AI RMF 1.0)](https://doi.org/10.6028/NIST.AI.100-1) `[standard]` — NIST AI 100-1: the US government's voluntary, sector-agnostic framework for managing AI risk across the full system lifecycle. Organizes guidance into four functions — Govern, Map, Measure, Manage — and is the reference vocabulary for virtually every US federal AI policy, procurement requirement, and third-party audit. The starting point for any organization building an AI risk program in a US regulatory context. (Tabassi, NIST; Jan 2023)

- [Artificial Intelligence Risk Management Framework: Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) `[standard]` — NIST AI 600-1: the companion profile that extends AI RMF 1.0 to generative AI systems, mandated by Executive Order 14110. Focuses on four GAI-specific concern areas — governance, content provenance, pre-deployment testing, and incident disclosure — and maps suggested actions to each AI RMF subcategory. The normative overlay any organization deploying LLMs or diffusion models needs alongside the base framework. (Autio, Schwartz, Dunietz et al.; NIST; Jul 2024)

- [Regulation (EU) 2024/1689 — Artificial Intelligence Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) `[standard]` — The EU AI Act: binding law establishing risk-tiered rules for AI systems placed on the EU market. Prohibits certain AI practices outright, imposes conformity and documentation obligations on high-risk systems, and sets transparency requirements for general-purpose AI models. Entered into force 1 August 2024; prohibition rules applied 2 February 2025; full application by 2 August 2026. This is the primary source — the official text in the EU's Official Journal. (European Parliament and Council; OJ L 2024/1689; Jul 2024)

- [ISO/IEC 42001:2023 — Artificial Intelligence Management Systems](https://www.iso.org/standard/81230.html) `[standard]` — The international standard specifying requirements for establishing, implementing, maintaining, and continually improving an AI Management System (AIMS). Certifiable by accredited third parties; widely adopted by organizations that need auditable evidence of responsible AI governance for customers, regulators, or procurement requirements. The ISO page is the primary landing; the full text requires purchase. (ISO/IEC JTC 1/SC 42; Dec 2023)

## Go deeper

- [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) `[guide]` — NIST's suggested-actions companion to AI RMF 1.0, organized by Govern / Map / Measure / Manage subcategory. Not a checklist to execute in full — designed for selective adoption based on organizational context. Available in PDF, CSV, Excel, and JSON; updated approximately twice yearly. The operational translation of the framework into concrete implementation steps. (NIST AI Resource Center; Mar 2023, updated 2024)

- [CSA AI Controls Matrix (AICM)](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix) `[standard]` — CSA's vendor-agnostic control framework for cloud-based AI systems: 243 control objectives across 18 security domains, with built-in mappings to ISO 42001, NIST AI RMF 1.0, NIST AI 600-1, and the EU AI Act. Includes role-specific implementation and auditing guides for five organizational roles (model provider, orchestrator, application provider, AI customer, cloud provider) and an AI Consensus Assessment Initiative Questionnaire (AI-CAIQ) for self- and third-party assessment. Download requires a free CSA account. (Cloud Security Alliance; v1.0.3, released Jul 2025, updated Oct 2025)

- [Announcing the AI Controls Matrix and ISO/IEC 42001 Mapping — and the Roadmap to STAR for AI 42001](https://cloudsecurityalliance.org/blog/2025/08/20/announcing-the-ai-controls-matrix-and-iso-iec-42001-mapping-and-the-roadmap-to-star-for-ai-42001) `[blog]` — Jim Reavis (CSA CEO) explains the control-by-control mapping between AICM v1.0 and ISO/IEC 42001:2023, the rationale for the STAR for AI certification program, and the gap-identification value of reading AICM and ISO 42001 side by side. The authoritative narrative on how CSA's technical controls framework connects to the certifiable ISO standard — practical orientation for organizations pursuing both. (Jim Reavis, CSA; Aug 2025)

- [Preparing Defenders of AI Systems, V 1.0](https://github.com/cosai-oasis/ws2-defenders/blob/main/preparing-defenders-of-ai-systems.md) `[guide]` — COSAI's (Coalition for Secure AI, an OASIS Open Project) foundational defender-side guidance: maps six security priorities — threat analysis across the AI lifecycle, MLSecOps and incident response capabilities, supply chain integrity, AI governance structures, identity and access management for autonomous systems, and leveraging AI as a security tool — to concrete actions for cross-functional teams. Evaluates NIST, MITRE ATLAS, and OWASP against real implementation gaps. The practitioner complement to the compliance frameworks: what your security team actually needs to build. (CoSAI Workstream 2; Jul 2025)

- [Risks and Controls for the AI Supply Chain, V 1.0](https://github.com/cosai-oasis/ws1-supply-chain/blob/main/risks-and-controls-for-the-ai-supply-chain-v1.md) `[guide]` — COSAI's technical analysis of AI supply chain risk across four dimensions — data, models, applications, and infrastructure — at two phases: model generation and model integration/consumption. Provides stakeholder-specific guidance for executives, security practitioners, and researchers, and benchmarks existing frameworks against supply chain security coverage gaps. The normative companion to governance frameworks for organizations that procure or integrate third-party models and datasets. (CoSAI Workstream 1; Jun 2025)

## Related topics

- [→ 10 Incident Response](./10-incident-response.md)
- [→ 14 AI for GRC](./14-ai-for-grc.md)
