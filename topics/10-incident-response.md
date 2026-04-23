---
title: AI Incident Response
summary: "AI-specific IR playbooks, forensics, and notification practice."
last-reviewed: 2026-04-22
status: ready
---

# AI Incident Response

AI incident response is a young discipline. Classical IR playbooks assume deterministic systems, stable signatures, and clear forensics. AI systems are probabilistic, versioned by weights and prompts and tools, and often fail non-reproducibly. The sources below are the first serious attempts to define what IR looks like when the system under investigation is an LLM or an agent.

The challenge is compounded by fragmented regulatory notification requirements — CIRCIA, HIPAA, GDPR, NIS2, and DORA each impose different timelines and scope — and by the fact that the forensic artifacts themselves are novel: system prompts, embedding snapshots, RAG query logs, and external tool execution traces rather than the packet captures and filesystem images that classical DFIR tooling was built around.

## Start here

- [AI Incident Response, V 1.0](https://github.com/cosai-oasis/ws2-defenders/blob/main/incident-response/AI-Incident-Response.md) `[guide]` — CoSAI Workstream 2's first full AI-specific IR framework: playbooks for training-data poisoning, multi-channel prompt injection, MINJA memory injection, RAG poisoning, and infrastructure credential abuse — each written to the OASIS CACAO specification with detection, triage, containment, eradication, and communication steps. Includes a forensics chapter on what telemetry to preserve (system prompts, raw outputs, embedding snapshots, tool execution traces) and a disclosure section navigating CIRCIA, GDPR, NIS2, and DORA simultaneously. The most operationally complete AI IR document available as of 2026. (CoSAI Workstream 2; approved Oct 2026)

- [AI Incident Database (AIID)](https://incidentdatabase.ai) `[database]` — The canonical repository of real-world AI system failures, maintained by the Responsible AI Collaborative and modeled on aviation incident databases. Freely searchable without login across thousands of cataloged incidents — autonomous vehicle failures, deepfake fraud, biased predictive-policing outputs, AI-generated misinformation in healthcare and finance — with spatial, table, and list discovery views. The empirical grounding for what "AI incidents" actually look like in deployment, and the primary source for case-study analysis before drafting any IR playbook. (Responsible AI Collaborative, est. 2021, continuously updated)

## Go deeper

- [Preventing Repeated Real World AI Failures by Cataloging Incidents: The AI Incident Database](https://arxiv.org/abs/2011.08512) `[paper]` — McGregor's founding paper proposing the AIID: argues that AI systems currently harm society without "a collective memory of their failings," and establishes the aviation-style incident-database model as the structural fix. Accepted at IAAI-21; the methodological rationale behind the database, explaining why incident cataloging — not just incident reporting — is necessary to break the cycle of repeated AI failures across organizations. (Sean McGregor; IAAI-21; Nov 2020)

- [Is the Digital Forensics and Incident Response Pipeline Ready for Text-Based Threats in LLM Era?](https://arxiv.org/abs/2407.17870) `[paper]` — Bhandarkar et al. evaluate whether classical DFIR methodologies can handle threats posed by neural text generators: using 14 datasets and 43 language models including GPT-4, they expose critical weaknesses in forensic profiling for AI-generated content, introduce the CS-ACT co-authorship text attack, and show that traditional authorship attribution fails against sophisticated generative models. The first systematic audit of DFIR pipeline readiness for the LLM threat class. (Bhandarkar, Wilson, Swarup, Zhu, Woodard; Jul 2024)

- [DFIR-Metric: A Benchmark Dataset for Evaluating Large Language Models in Digital Forensics and Incident Response](https://arxiv.org/abs/2505.19973) `[paper]` — Introduces the first structured benchmark for measuring LLM capability in DFIR contexts: 700 expert-reviewed multiple-choice questions from industry certifications, 150 CTF-style forensic challenges requiring multi-step reasoning, and 500 real-world cases from the NIST Computer Forensics Tool Testing Program. Evaluates 14 LLMs and introduces the Task Understanding Score (TUS) metric to surface performance differences that standard accuracy metrics obscure. Quantifies both the opportunity and the error-rate risk of deploying LLMs for log analysis, memory forensics, and incident reconstruction. (Cherif, Bisztray, Dubniczky, Aldahmani, Alshehhi, Tihanyi; May 2025)

- [Automating Cloud Security and Forensics Through a Secure-by-Design Generative AI Framework](https://arxiv.org/abs/2604.03912) `[paper]` — Proposes CIAF (Cloud Investigation Automation Framework), which applies ontology-based reasoning across all six forensic investigation phases using LLMs, and PromptShield, an ontology-driven defense against prompt injection attacks on those same LLMs. Validated on real AWS and Azure log datasets with demonstrated improvements in ransomware detection accuracy. The practical template for organizations building LLM-assisted forensics pipelines while defending the investigative AI from adversarial manipulation. (Alharthi, Garcia; Apr 2026)

## Related topics

- [→ 05 LLM Vulnerabilities](./05-llm-vulnerabilities.md)
- [→ 06 Agentic Security](./06-agentic-security.md)
- [→ 09 Governance & Compliance](./09-governance-and-compliance.md)
