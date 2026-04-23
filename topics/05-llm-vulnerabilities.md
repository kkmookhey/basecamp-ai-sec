---
title: LLM Vulnerabilities
summary: "OWASP LLM Top 10 2025, data and model poisoning, supply chain risks, training-time exposures."
last-reviewed: 2026-04-22
status: ready
---

# LLM Vulnerabilities

The taxonomy matters here more than in most topics. OWASP's LLM Top 10 2025 is the spine — the checklist practitioners actually use when auditing an AI system. MITRE ATLAS is the attacker's playbook — structured the same way as ATT&CK, covering the full kill chain from reconnaissance through impact. NIST's Adversarial Machine Learning taxonomy (AI 100-2) is the academic and regulatory frame — the vocabulary that compliance teams and researchers share. Know all three before arguing about individual attack classes.

Prompt injection as a vulnerability class has its own topic (see Related topics). This topic covers everything else in the catalog: data and model poisoning, supply chain, sensitive data exposure, training-data extraction, model inversion, vector and embedding weaknesses, and the structural scaffolding that connects them.

## Start here

- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) `[guide]` — The definitive practitioner taxonomy for LLM security risk: ten vulnerability classes from prompt injection through unbounded consumption, each with real-world attack scenarios, root cause analysis, and mitigation checklists. The 2025 edition added supply chain, vector/embedding weaknesses, and misinformation as distinct entries, reflecting how the threat surface has matured since 2023. Start here before any other source in this topic. (OWASP GenAI Security Project, Nov 2024)

- [MITRE ATLAS™](https://atlas.mitre.org) `[framework]` — A living knowledge base of adversary tactics and techniques targeting AI and ML systems, structured identically to MITRE ATT&CK so security teams can map AI-specific threats into existing detection and response workflows. Covers the full adversarial kill chain — reconnaissance, resource development, initial access through training-data or supply-chain compromise, model evasion, and exfiltration — grounded in real-world attack observations and AI red-team demonstrations. (MITRE Corporation, continuously updated)

- [NIST AI 100-2 E2025: Adversarial Machine Learning — A Taxonomy and Terminology of Attacks and Mitigations](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) `[guide]` — The US government's authoritative taxonomy for adversarial ML: classifies evasion, poisoning, privacy, and misuse attacks across both predictive and generative AI systems, defines standardized terminology shared across the ML and cybersecurity communities, and surveys mitigations with honest acknowledgment of their limitations. Developed jointly by NIST, the US and UK AI Safety Institutes, and industry partners; will be updated annually. The vocabulary baseline for regulatory and compliance conversations. (Vassilev, Oprea, Fordyce, Anderson, Davies, Hamin; NIST, Mar 2025)

## Go deeper

- [LLM04:2025 Data and Model Poisoning](https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/) `[guide]` — OWASP's primary entry on training-time attacks: defines how manipulation of pre-training, fine-tuning, or embedding datasets can introduce backdoors, biases, and capability regressions that survive into production, and maps nine attack scenarios including supply-chain poisoning via external datasets and LoRA adapter tampering. The reference framing for anyone scoping a data-integrity control. (OWASP GenAI Security Project, 2025)

- [LLM02:2025 Sensitive Information Disclosure](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/) `[guide]` — OWASP's entry on the three distinct pathways through which LLMs leak confidential data: inadvertent training-data regurgitation, targeted prompt injection to extract credentials or PII, and inadequate output sanitization that exposes one user's data to another. Operationalizes the threat model that the extraction and inversion papers below demonstrate empirically. (OWASP GenAI Security Project, 2025)

- [LLM03:2025 Supply Chain](https://genai.owasp.org/llmrisk/llm032025-supply-chain/) `[guide]` — OWASP's supply-chain entry: covers nine risk categories unique to the ML supply chain — compromised pre-trained models, weak model provenance, vulnerable LoRA adapters, and outdated third-party components — alongside ten mitigations including AI-specific SBOM requirements and red-teaming evaluations of third-party models before deployment. (OWASP GenAI Security Project, 2025)

- [Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149) `[paper]` — Carlini et al. demonstrate two immediately exploitable dataset poisoning attacks: split-view poisoning exploits the mutable nature of web content so that dataset annotators see different content than downstream training clients — demonstrated against LAION-400M for $60 — and frontrunning poisoning targets crowd-sourced snapshots like Wikipedia. Published at IEEE S&P 2024, it is the canonical empirical proof that training-data poisoning at scale is not a theoretical concern. (Carlini, Jagielski, Choquette-Choo, Paleka, Pearce, Anderson, Terzis, Thomas, Tramèr; Feb 2023)

- [Scalable Extraction of Training Data from (Production) Language Models](https://arxiv.org/abs/2311.17035) `[paper]` — Nasr, Carlini et al. show that extractable memorization is a production-grade threat: their "divergence attack" forces aligned models like ChatGPT away from chatbot behavior and into training-data emission at a rate 150× higher than normal operation, recovering gigabytes of data from open-source through closed models. Directly refutes the assumption that RLHF alignment eliminates memorization risk. (Nasr, Carlini, Hayase, Jagielski, Cooper, Ippolito, Choquette-Choo, Wallace, Tramèr, Lee; Nov 2023)

- [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733) `[paper]` — The foundational backdoor-attack paper: Gu, Dolan-Gavitt, and Garg demonstrate that outsourcing neural network training enables adversaries to inject hidden backdoors that activate on attacker-specified inputs while maintaining normal performance on all other data — and that the backdoor persists through subsequent retraining. Coined "BadNets" as the template for the supply-chain poisoning threat class that OWASP LLM03 and LLM04 now formalize. (Gu, Dolan-Gavitt, Garg; Aug 2017, revised 2019)

- [4M Models Scanned: Protect AI + Hugging Face 6 Months In](https://huggingface.co/blog/pai-6-month) `[blog]` — Protect AI and Hugging Face's six-month progress report on scanning the Hub at scale: 4.47 million model versions scanned, 352,000 unsafe issues identified across 51,700 models, and four new threat-detection modules covering archive slip vulnerabilities, malicious Joblib execution, TensorFlow architectural backdoors, and Llamafile code injection. The strongest empirical signal available on the real prevalence and variety of malicious models in the wild. (Sean Morgan / Protect AI and Hugging Face, Apr 2025)

## Tools

- [Whitney](https://github.com/transilienceai/whitney) `[tool]` — Static scanner for AI codebases — detects prompt-injection patterns across 15 source types (direct, indirect-fetched, indirect-agent, indirect-stored, and cross-modal), catches broken LLM-as-judge implementations, and emits an AI-dependency SBOM in CycloneDX format. Achieves 100% recall and 94.5% F1 on its labeled test corpus versus 50% recall for Semgrep's AI ruleset — a published 2× benchmark win. Zero LLM API calls required by default. (Transilience AI, actively maintained)

## Related topics

- [→ 04 Prompt Injection & Jailbreaks](./04-prompt-injection.md)
- [→ 06 Agentic Security](./06-agentic-security.md)
- [→ 16 Research Frontier](./16-research-frontier.md)
