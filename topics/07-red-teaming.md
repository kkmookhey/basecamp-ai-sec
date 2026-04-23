---
title: AI Red Teaming
summary: "Methodology and frameworks for adversarial evaluation of AI systems. How to think, not which tools to click."
last-reviewed: 2026-04-22
status: ready
---

# AI Red Teaming

Red-teaming an AI system is different from red-teaming a web app. The attack surface is probabilistic; failure modes are non-deterministic; the "system" includes weights, prompts, tools, and humans. A single pass finds nothing — adversarial behaviors surface through repeated, varied attempts and sometimes only when the system is under specific contextual pressure. This topic catalogs the frameworks that exist for doing it as a discipline rather than ad-hoc: how to scope, staff, structure, and repeat an adversarial evaluation of an AI system.

Tools (PyRIT, DeepTeam) are in topic 08. Specific attack techniques live in topics 04 and 06. This topic is the methodology layer: what mental models and structured processes govern the exercise.

## Start here

- [Agentic AI Red Teaming Guide](https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide) `[guide]` — CSA's canonical methodology document for adversarially testing autonomous AI systems: distinguishes agentic red teaming from generative-AI red teaming (the threat surface expands from model outputs to agent workflows, inter-agent dependencies, and real-world state changes), then walks through structured test procedures across permission escalation, hallucination exploitation, orchestration flaws, memory manipulation, and supply chain risks. The reference playbook for any team running a red team exercise against an agent-based system. (Cloud Security Alliance, May 2025)

- [AI Security Training](https://learn.microsoft.com/en-us/security/ai-red-team/training) `[guide]` — Microsoft AI Red Team's free 10-episode training series covering the full methodology arc: what AI red teaming is and how it differs from traditional red teaming (Episode 1), how model architecture creates unique security risks (Episode 2), core attack techniques from direct and indirect prompt injection through multi-turn Crescendo and Skeleton Key attacks (Episodes 3–6), defense and mitigation strategies (Episode 7), and automation at scale (Episodes 8–10). Hands-on labs included. The most structured publicly available curriculum on AI red teaming methodology from the team that has run it across 100+ products. (Microsoft AI Red Team, Jul 2025)

- [OWASP AI Testing Guide v1](https://owasp.org/www-project-ai-testing-guide/) `[guide]` — OWASP's structured testing methodology for AI systems, released November 2025 after two phases of development. Frames the objective as AI trustworthiness (not just security), and organizes testing across four layers — Application, Model, Infrastructure, and Data — covering adversarial manipulation, bias, data poisoning, hallucinations, and model drift. The practitioner's structured testing framework that sits alongside the OWASP LLM Top 10: that taxonomy names the risks, this guide tells you how to test for them. (OWASP AI Testing Guide Project, Nov 2025)

## Go deeper

- [Agentic AI Threat Modeling Framework: MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) `[blog]` — Ken Huang (CSA Fellow, DistributedApps.ai) introduces MAESTRO (Multi-Agent Environment, Security, Threat, Risk, and Outcome): a seven-layer reference architecture for systematically enumerating threats in agentic AI systems, extending traditional frameworks (STRIDE, PASTA) with AI-specific threat categories. The layers span Foundation Models through Agent Ecosystem, enabling red teams to scope adversarial exercises at the right level of abstraction. The structured counterpart to MITRE ATLAS for the agentic deployment context. (Ken Huang / CSA, Feb 2025)

- [Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned](https://arxiv.org/abs/2209.07858) `[paper]` — Ganguli, Lovitt, Kernion, Askell, Bai, and 31 co-authors at Anthropic present the foundational empirical study of AI red teaming as a repeatable discipline: how to structure manual red team exercises, how harm rates scale with model size and training type (RLHF models become harder to red team as they scale), and what the distribution of 38,961 released attack attempts reveals about the practical difficulty of the exercise. The methods and uncertainty analysis here are the implicit reference model for every serious AI red team program that came after. (Ganguli et al., Anthropic; arXiv 2209.07858, Aug 2022)

- [3 Takeaways from Red Teaming 100 Generative AI Products](https://www.microsoft.com/en-us/security/blog/2025/01/13/3-takeaways-from-red-teaming-100-generative-ai-products/) `[blog]` — Bullwinkel and Ram Shankar Siva Kumar distill what Microsoft's AI Red Team learned after running structured adversarial evaluations across more than 100 products: generative AI systems amplify both novel AI vulnerabilities and classical security weaknesses simultaneously; human expertise (cultural context, domain knowledge, emotional intelligence) is irreplaceable for the portions automation tools cannot reach; and effective AI red teaming requires layered defense-in-depth rather than point fixes. Includes the team's red team ontology mapping adversary, tactic, technique, weakness, and downstream impact. (Microsoft Security Blog, Jan 2025)

- [Google's AI Red Team: The Ethical Hackers Making AI Safer](https://blog.google/technology/safety-security/googles-ai-red-team-the-ethical-hackers-making-ai-safer/) `[blog]` — Daniel Fabian (Head of Google Red Teams) publicly describes Google's dedicated AI Red Team for the first time: how it was structured to combine AI subject-matter expertise with traditional offensive security tradecraft, what attack categories the team exercises (prompt attacks, training data extraction, model backdooring, adversarial examples, data poisoning, exfiltration), and four operational lessons — AI expertise is essential, findings must feed product development cycles, standard security controls still matter, and many AI attacks surface through conventional detection methods. The primary organizational description of a mature in-house AI red team program from a lab with a decade of red team history. (Daniel Fabian / Google, Jul 2023)

- [Threat Modeling AI/ML Systems and Dependencies](https://learn.microsoft.com/en-us/security/engineering/threat-modeling-aiml) `[guide]` — Marshall, Parikh, Kiciman, and Ram Shankar Siva Kumar present Microsoft's structured threat modeling guidance for AI/ML systems, authored for the AETHER Engineering Practices for AI Working Group. Extends SDL threat modeling with AI-specific threat enumeration: adversarial perturbation (four variants), targeted and indiscriminate data poisoning, model inversion, membership inference, model stealing, neural net reprogramming, physical-domain adversarial examples, malicious ML providers, and supply chain attacks — each with mitigations and severity ratings. The structured pre-engagement threat enumeration companion to an AI red team exercise. (Marshall, Parikh, Kiciman, Ram Shankar Siva Kumar / Microsoft, Nov 2019; updated Mar 2025)

## Watch

- **KK's "Red Teaming Agentic AI" three-part series (~66 min total)** `[video]` — Practitioner-level walkthrough of adversarial evaluation of agentic AI systems across three sessions: scoping the agentic attack surface, running structured red team exercises against agent workflows, and documenting findings in a repeatable framework. The most thorough publicly available hands-on red-teaming walkthrough for agentic systems. *URL pending — add via batch fix.*

## Related topics

- [→ 05 LLM Vulnerabilities](./05-llm-vulnerabilities.md)
- [→ 06 Agentic Security](./06-agentic-security.md)
- [→ 08 Attacking AI Tooling](./08-attacking-ai-tooling.md)
