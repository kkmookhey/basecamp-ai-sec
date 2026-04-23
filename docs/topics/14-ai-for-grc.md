---
title: AI for GRC
summary: "AI applied to GRC work — policy authoring, control mapping, audit evidence, compliance gap analysis."
last-reviewed: 2026-04-22
status: ready
---

# AI for GRC

SOC 2 prep used to be a spreadsheet project. ISO 42001 arrives on top of that, plus the EU AI Act, plus NIST AI RMF — and the spreadsheet breaks. AI-native compliance tooling reframes this work: control evidence becomes an LLM-queryable substrate; audit prep becomes a workflow; framework mapping becomes a one-shot translation. This topic catalogs the tools and technical writing behind that shift, not the vendor promises.

## Start here

- [Build and manage assessments in Microsoft Purview Compliance Manager](https://learn.microsoft.com/en-us/purview/compliance-manager-assessments) `[docs]` — Microsoft's canonical technical reference for Compliance Manager, covering the AI-specific regulatory templates (EU AI Act, ISO/IEC 42001:2023, NIST AI RMF 1.0, ISO/IEC 23894) and the Azure AI Foundry integration that automatically syncs 75 compliance actions — 15 of them fully automated evaluation metrics (reliability, coherence, BLEU score, fluency) — into assessment dashboards in real time. The control-mapping engine tracks pass/fail by service and regulation simultaneously; the evidence export produces an auditor-ready Excel snapshot. The clearest primary account of what it means for an AI system to automate its own compliance evidence collection against multiple frameworks at once. (Microsoft; updated Dec 2025)

- [Building a smarter retrieval system: Lessons from Vanta AI](https://www.vanta.com/resources/building-a-smarter-retrieval-system-lessons-from-vanta-ai) `[blog]` — Walton Seymour (Vanta engineering) describes the RAG architecture that powers Vanta's compliance AI features: five chunking strategies benchmarked against a compliance-specific evaluation dataset (precision@k, recall@k, MRR, F1), context-aware chunking winning with a 16% recall improvement, hybrid BM25-plus-semantic search adding 9%, and Cohere v3.5 reranking adding a further 21% MRR gain — for a combined 40% recall and 22% MRR lift over the baseline. The engineering reality of what "AI-assisted evidence collection" requires at the retrieval layer, told by the team that built it. (Walton Seymour, Vanta; Feb 2025)

## Go deeper

- [Executable Governance for AI: Translating Policies into Rules Using LLMs](https://arxiv.org/abs/2512.04408) `[paper]` — Datla, Vurity, Dash, Ahmad, Adnan, and Rafi introduce Policy-to-Tests (P2T): a pipeline that extracts policy documents and compiles them into a domain-specific language capturing hazards, scope, conditions, exceptions, and required evidence — producing executable test artifacts rather than prose summaries. Validated across sector guidance and enterprise standards including HIPAA, with AI-generated rules matching strong human baselines at span and rule level. Accepted at the AAAI-26 AI Governance Workshop. The most direct technical treatment of the question GRC teams actually need answered: can LLMs turn a policy document into checks that run in an engineering workflow? (Datla et al.; arXiv 2512.04408; Dec 2025)

- [The Unified Control Framework: Establishing a Common Foundation for Enterprise AI Governance, Risk Management and Regulatory Compliance](https://arxiv.org/abs/2503.05937) `[paper]` — Eisenberg, Gamboa, and Sherman (Credo AI) propose a 42-control library that simultaneously satisfies multiple regulatory requirements through many-to-many mapping: each control addresses multiple risk scenarios; each regulation is satisfied by multiple overlapping controls. Validated against the Colorado AI Act with full policy-requirement-to-control-to-evidence traceability. The framework reduces governance duplication by letting an organization implement one coherent control set instead of separate parallel programs for each regulation — the scaling problem that becomes acute when ISO 42001, NIST AI RMF, and the EU AI Act all apply simultaneously. (Eisenberg, Gamboa, Sherman; arXiv 2503.05937; Mar 2025)

- [Computational Compliance for AI Regulation: Blueprint for a New Research Domain](https://arxiv.org/abs/2601.04474) `[paper]` — Marino and Lane (University of Cambridge) argue that AI regulation compliance at scale is computationally intractable by manual means and propose a two-component algorithmic architecture: an Inspector that continuously diagnoses compliance status across models, datasets, logs, and code, and a Mechanic that deploys repairs without human intervention. Includes design goals, performance criteria (accuracy, latency, precision, recall), and a benchmark dataset for measuring algorithm quality — the first such benchmark in this space. The foundational paper for anyone building or evaluating automated compliance tooling: it defines what "done" means for the Inspector and Mechanic functions that every compliance automation vendor is implicitly building. (Marino, Lane; arXiv 2601.04474; Jan 2026)

## Tools

- [shasta](https://github.com/transilienceai/shasta) — AI-native compliance automation for SOC 2, ISO 27001, and HIPAA on AWS and Azure — treats control evidence collection and audit prep as an AI workflow rather than a spreadsheet workflow. 174+ automated checks via deterministic Semgrep AST patterns and cloud SDK calls (no LLM in detection), 112 Terraform remediation templates, 8 auto-generated SOC 2 policy documents, and real-time monitoring via AWS Config Rules and Azure Defender. Interface is 15 Claude Code skills. Active (pushed Apr 2026) · 115 stars.

## Related topics

- [→ 09 Governance & Compliance](./09-governance-and-compliance.md)
- [→ 10 AI Incident Response](./10-incident-response.md)
