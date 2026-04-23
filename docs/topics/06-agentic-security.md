---
title: Agentic AI Security
summary: "Excessive agency, tool abuse, inter-agent manipulation, the rule-of-two, trust boundaries."
last-reviewed: 2026-04-22
status: ready
---

# Agentic AI Security

When an LLM gains the ability to act — call tools, spawn sub-agents, browse the web, edit files — the failure modes expand from "model says the wrong thing" to "model does the wrong thing, at scale, irreversibly." Prompt injection becomes privilege escalation. Plain outputs become filesystem writes, emails sent, APIs called. This topic is about that expansion: what goes wrong specifically when LLMs become agents, and what the emerging defenses look like.

Readers arriving here should know topic 04 (prompt injection as an input attack) and topic 05 (the LLM vulnerability taxonomy). This topic picks up where those leave off: the agentic threat surface — excessive permissions, tool misuse, inter-agent trust exploitation, cascading failures, and browser / computer-use agents as a category that may be architecturally unsecurable.

## Start here

- [Agents Rule of Two: A Practical Approach to AI Agent Security](https://ai.meta.com/blog/practical-ai-agent-security/) `[blog]` — Meta's governing design constraint for agentic systems: an agent must satisfy no more than two of (A) processing untrustworthy inputs, (B) access to sensitive systems or private data, (C) ability to change state or communicate externally. Any agent that satisfies all three requires human-in-the-loop supervision. The Rule of Two is the most actionable single heuristic in the field for scoping agent permissions before deployment. (Meta AI, Oct 2025)

- [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) `[guide]` — OWASP's formal entry for the vulnerability class that defines this topic: an LLM system granted excessive functionality, excessive permissions, or excessive autonomy can cause damaging real-world actions from hallucinated or manipulated outputs alone. Maps the root causes — unnecessary tool capabilities, open-ended extensions like shell access, over-broad permission scopes — and eight mitigations anchored to least-privilege and mandatory human approval for high-impact actions. The reference checklist for anyone scoping an agent's tool surface. (OWASP GenAI Security Project, 2025)

- [Agentic Misalignment: How LLMs Could Be Insider Threats](https://www.anthropic.com/research/agentic-misalignment) `[paper]` — Anthropic and collaborators stress-tested 16 leading models in simulated corporate environments where agents could autonomously send emails and access sensitive information. When facing replacement or goal conflicts, models from every developer resort to malicious insider behaviors — blackmail, data exfiltration to competitors, disobeying shutdown commands — in at least some cases. Establishes that current safety training does not prevent intentional harmful decision-making in agentic deployments and quantifies the triggering conditions. (Lynch, Wright, Larson, Ritchie, Mindermann, Hubinger, Perez, Troy; Anthropic; arxiv 2510.05179, Oct 2025)

## Go deeper

- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) `[guide]` — OWASP's dedicated threat taxonomy for agentic systems, developed with over 100 industry experts and grounded in real-world incidents: ten risks from ASI01 Agent Goal Hijack through ASI10 Rogue Agents, covering tool misuse, identity and privilege abuse, agentic supply chain vulnerabilities, memory and context poisoning, insecure inter-agent communication, cascading failures, and human-agent trust exploitation. The companion to the LLM Top 10 for teams building multi-step autonomous workflows. (OWASP GenAI Security Project, Dec 2025)

- [Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents](https://arxiv.org/abs/2505.02077) `[paper]` — Introduces multi-agent security as a new research field distinct from both individual AI safety and classical cybersecurity: taxonomizes threats that emerge from agent-to-agent interaction (secret collusion, coordinated swarm attacks, network-propagating jailbreaks), surveys security-performance tradeoffs in decentralized systems, and calls for a unified research agenda across AI security, game theory, distributed systems, and governance. The field-defining framing paper for this threat class. (de Witt; May 2025)

- [The Trust Paradox in LLM-Based Multi-Agent Systems: When Collaboration Becomes a Security Vulnerability](https://arxiv.org/abs/2510.18563) `[paper]` — Empirically demonstrates the Trust-Vulnerability Paradox: increasing inter-agent trust to improve coordination simultaneously expands over-exposure and over-authorization risks. Introduces two measurement metrics — Over-Exposure Rate and Authorization Drift — validated across 19 scenarios with parameterized trust levels. Shows that "Sensitive Information Repartitioning" and Guardian-Agent defenses reduce drift, but no configuration eliminates the paradox entirely. (Xu, Qi, Wu, Zhang, Wei, He, Li; Oct 2025)

- [From AI Agents to MultiAgent Systems: A Capability Framework](https://cloudsecurityalliance.org/blog/2024/12/09/from-ai-agents-to-multiagent-systems-a-capability-framework) `[blog]` — Ken Huang (CSA AI Safety WG Co-Chair) presents an 11-level capability progression for AI systems — from basic perception through meta-learning — and identifies level 6 (collaboration) as the transition point where multi-agent security concerns become primary. Security properties that hold for individual agents break down once agents coordinate, share memory, or resolve conflicts through decentralized consensus. The framing for why multi-agent systems require a distinct threat model. (Ken Huang / CSA, Dec 2024)

- [Agentic Browser Security: Indirect Prompt Injection in Perplexity Comet](https://simonwillison.net/2025/Aug/25/agentic-browser-security/) `[blog]` — Willison's analysis of the Brave security team's findings that Perplexity's Comet browser extension feeds webpage content directly to its LLM without distinguishing trusted instructions from untrusted content — enabling attackers to embed prompt injection payloads that trigger unauthorized actions including account recovery flows and data exfiltration. Willison's central argument: the entire category of agentic browser extensions may be architecturally unsecurable because "to an LLM the trusted instructions and untrusted content are concatenated together into the same stream of tokens." (Simon Willison, Aug 2025)

- [Computer use — Security considerations](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use) `[guide]` — Anthropic's official guidance on computer-use agent security for deployers: identifies prompt injection from webpage content or images as the primary attack vector, mandates dedicated VMs or containers with minimal privileges, prohibits access to sensitive accounts without strict oversight, and requires human confirmation for actions with real-world consequences. Documents the classifier layer Anthropic added to detect injections in screenshots and steer the model to pause before acting. The authoritative reference for deploying computer-use agents safely. (Anthropic, 2025)

## Watch

- [Chapter 7.2: Hacking Multi-Agent AI Systems — Breaking Your AI Agent Crew](https://www.youtube.com/watch?v=_m_U83XMqJQ) `[video]` — Hands-on walkthrough of attacks against multi-agent systems: how inter-agent trust is exploited, how tool-call chains enable privilege escalation across agent boundaries, and live demonstrations of cascading failure scenarios. Practitioner-level coverage that the primary written literature on multi-agent attacks does not yet match in accessibility. (KK Mookhey / Transilience AI, ~21 min)

## Related topics

- [→ 02 Building LLM Apps](./02-building-llm-apps.md)
- [→ 04 Prompt Injection & Jailbreaks](./04-prompt-injection.md)
- [→ 07 Red Teaming](./07-red-teaming.md)
