# Transilience AI Repo Inventory (Plan 2)

Assessment of Transilience's public repos against the quality bar defined
in CONTRIBUTING.md. Per design spec section 7: these repos appear in the
topic that matches their actual function, evaluated under the
same quality bar as any other tool. No homepage links, no promotional
framing. If a repo fails the bar, it doesn't go in.

This file is deleted at Plan 2 DoD (Task 24).

## Quality bar for tools (from CONTRIBUTING.md Tools section and spec section 7)
- Actively maintained (commit in last ~60 days)
- Reasonable README / docs
- Adoption signal or a published threat model
- Public and accessible

---

## shasta

- Description: Shasta — AWS and Azure compliance automation platform for SOC 2, ISO 27001 and HIPAA. AI-native toolkit for founders.
- Visibility: PUBLIC
- Last push: 2026-04-21 (yesterday — actively maintained)
- Stars: 115
- Identified function: AI-powered automation for cloud compliance (SOC 2, ISO 27001, HIPAA) on AWS and Azure. Targeted at founders / early-stage teams.
- Meets bar: **YES** — public, active (pushed yesterday), 115 stars is strong adoption signal, description clearly identifies function.
- Proposed topic placement: **14-ai-for-grc** — AI applied to GRC work (compliance automation is the textbook example of "AI for GRC").
- Proposed section: `## Tools`
- Proposed annotation draft: *AI-native compliance automation for SOC 2, ISO 27001, and HIPAA on AWS and Azure — treats control evidence collection and audit prep as an AI workflow rather than a spreadsheet workflow.*

## whitney

- Description: Open-source static AI security scanner — prompt injection across 15 source types, broken LLM-as-judge detection, AI dependency SBOM. Beats Semgrep AI ruleset 2x on a labelled corpus.
- Visibility: PUBLIC
- Last push: 2026-04-21 (yesterday — actively maintained)
- Stars: 18
- Identified function: Defensive static analyzer for AI codebases. Detects prompt-injection patterns in 15 input source types, identifies broken LLM-as-judge patterns, and emits an AI dependency SBOM. Positions itself against Semgrep's AI ruleset with a measured 2× benchmark win on a labelled corpus.
- Meets bar: **YES** — public, active, 18 stars is modest but a published benchmark claim against Semgrep is a legitimate adoption signal and shows serious engineering.
- Proposed topic placement: **05-llm-vulnerabilities** — Whitney scans for the vulnerability *patterns* catalogued in OWASP LLM Top 10 (prompt injection sources, LLM-as-judge failures, supply chain via SBOM). Fits naturally next to the vulnerability references as the detection tool for them. Not 08-attacking-ai-tooling (which is for tools that attack AI); Whitney is defensive pre-deployment scanning.
- Proposed section: `## Tools`
- Proposed annotation draft: *Static scanner for AI codebases — detects prompt-injection patterns across 15 source types, catches broken LLM-as-judge implementations, and emits an AI-dependency SBOM. Published 2× benchmark win against Semgrep's AI ruleset.*

## communitytools

- Description: Open-source Claude Code skills, agents, and slash commands for AI-powered penetration testing, bug bounty hunting, and security research
- Visibility: PUBLIC
- Last push: 2026-04-22 (today — actively maintained)
- Stars: 195
- Identified function: Claude Code skills + agents + slash commands specifically for offensive security work — pentest, bug bounty, research. Turns Claude Code into a pentest assistant.
- Meets bar: **YES** — public, actively maintained (pushed today), 195 stars is strong adoption, description is clear and functional.
- Proposed topic placement: **12-ai-for-pentesting** — the canonical home for tools that use AI to attack non-AI systems. Claude Code as a pentest agent is exactly this topic.
- Proposed section: `## Tools`
- Proposed annotation draft: *A curated set of Claude Code skills, agents, and slash commands for offensive security — pentest workflows, bug bounty recon, and research assistants. Turns a general-purpose coding agent into a specialized red-team tool.*

---

## Summary

Tools that will ship in Plan 2, listed by topic:

- **topic 05 (llm-vulnerabilities)** — whitney (static scanner for AI code vulns)
- **topic 12 (ai-for-pentesting)** — communitytools (Claude Code skills/agents for offensive work)
- **topic 14 (ai-for-grc)** — shasta (AI-native compliance automation for cloud)

All three meet the tool bar. None require waivers.

Tools that did NOT meet the bar:

*(none)*
