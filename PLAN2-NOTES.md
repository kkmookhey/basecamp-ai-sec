# Plan 2 Curation Notes

Running notes of judgment calls, deferrals, and KK-attention items
during Plan 2 content curation. Reviewed and emptied at Plan 2 DoD
(Task 24). Not committed to any tag.

## Deferred judgment calls

*(entries added as they arise)*

## Scope questions raised during research

*(entries added as they arise)*

## Tools / links investigated but rejected

*(entries added as they arise)*

---

## Per-topic seed hints (authored at Task 4; guides Tasks 5-20)

### 01-foundations
- Authoritative anchors: Lilian Weng's LLM Powered Autonomous Agents post; 3Blue1Brown transformer series; Chip Huyen's Agents post; Anthropic's Building Effective Agents; MCP's own spec intro.
- Likely `[book-ch]`: Sebastian Raschka *Build a Large Language Model from Scratch* ch.1; Chip Huyen *AI Engineering* ch.1.
- KK video candidate: Video 1 (see PLAN2-VIDEO-MAP).

### 02-building-llm-apps
- Authoritative anchors: Anthropic's Building Effective Agents; Chip Huyen's Agents post; LangChain docs; LlamaIndex RAG tutorial; OpenAI's Agents SDK; Meta practical-AI-agent-security.
- Look for: multi-agent patterns from Microsoft's AutoGen, CrewAI, Anthropic's research.

### 03-mcp
- Authoritative anchors: modelcontextprotocol.io spec; Anthropic's MCP intro post; arxiv 2503.23278 (comprehensive MCP survey); CSA MCP Resource Center; Johann Rehberger's MCP security series on embracethered.com.
- Tools: MCP Scanner, anthropic/mcp reference impls.
- KK video candidate: Video 13 (MCP security checklist).

### 04-prompt-injection
- Authoritative anchors: Simon Willison's prompt-injection tag on simonwillison.net; Google Security Blog 2025 post on mitigating prompt injection; arxiv 2511.03247 (multi-turn attacks); OWASP LLM01:2025 Prompt Injection section.
- Tools: none here (tools go in 08-attacking-ai-tooling).
- KK video candidate: Video 4.

### 05-llm-vulnerabilities
- Authoritative anchors: OWASP LLM Top 10 2025 (genai.owasp.org); MITRE ATLAS; Meta rule-of-two; HuggingFace security blog; NIST AI 100-2 Adversarial ML taxonomy.
- Topics inside: data poisoning, model poisoning, supply chain, training-time, sensitive data exposure.

### 06-agentic-security
- Authoritative anchors: Meta's Agents Rule of Two; OWASP Agentic AI Top 10 (if available - check genai.owasp.org); Anthropic's research on agent misbehavior; CSA Agentic Red Teaming Guide; Ken Huang's CSA agentic patterns post.
- KK video candidate: Video 6 and/or 14-16.

### 07-red-teaming
- Authoritative anchors: CSA Agentic Red Teaming Guide; Microsoft AI Red Team (learn.microsoft.com/security/ai-red-team); MAESTRO framework (if published primary source exists); MITRE ATLAS tactics.
- KK video candidate: Videos 8-10 (Red Teaming 3-part series, bundled).

### 08-attacking-ai-tooling
- Authoritative anchors: PyRIT GitHub (github.com/Azure/PyRIT); DeepTeam GitHub; MCP Scanner; NOVA.
- Distinct from 12-ai-for-pentesting: these tools ATTACK AI; topic 12's tools USE AI to attack non-AI targets.

### 09-governance-and-compliance
- Authoritative anchors: NIST AI RMF 1.0 + GenAI profile; ISO/IEC 42001 summary; EU AI Act official text at artificialintelligenceact.eu; CSA AI Controls Matrix (AICM); Google Cloud recommended AI controls framework; CSA ISO 42001 mapping.
- Standards only - no vendor takes on governance here.

### 10-incident-response
- Authoritative anchors: COSAI's AI Incident Response document (github.com/cosai-oasis/ws2-defenders); MITRE ATLAS incident case studies; Anthropic's threat-intel reports.

### 11-ai-for-soc
- Authoritative anchors: Microsoft Security Copilot docs; Google SecOps AI docs; Splunk's AI agents for SOC posts (if primary); Elastic's AI for Search/Observability.
- Transilience fit: unlikely - more of a detection/response angle, assess in Task 15.

### 12-ai-for-pentesting
- Authoritative anchors: XBOW (xbow.com); Strix pentesting tool GitHub; Hexastrike; Kali-MCP; Burp-MCP; Claude Code as pentest agent (Anthropic post or a trustworthy practitioner's writeup).
- KK video candidate: Video 20 (Bake-Off results).
- Transilience fit: communitytools is likely here.

### 13-ai-for-vulnerability-management
- Authoritative anchors: Microsoft's ExCyTIn-Bench benchmark; Tenable AI posts (if primary); Qualys AI TruRisk.
- Transilience fit: Shasta or Whitney may fit here - confirm from Task 3.
- KK video candidate: Video 25 if Transilience repo lands here.

### 14-ai-for-grc
- Authoritative anchors: Microsoft Copilot for Compliance; Google Cloud's AI controls framework; Ken Huang/CSA GRC posts; IBM's ISO 42001 implementation guide.

### 15-ai-for-threat-intel
- Authoritative anchors: Anthropic's threat-intel reports; Microsoft's threat-intel AI tooling; Google Mandiant AI-augmented TI posts; Meisam Eslahi's threat-hunting posts (primary site, not LinkedIn).

### 16-research-frontier
- Authoritative anchors: Microsoft ExCyTIn-Bench (github.com/microsoft/SecRL); MITRE ATLAS; NeurIPS Safety workshop 2025 papers; USENIX Security 2025 AI papers; notable labs to follow.
- Not a dumping ground - this topic is specifically for *evaluation benchmarks* and *active research directions* worth following. Papers that belong in 04/05/06 stay there.
