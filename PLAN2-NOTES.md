# Plan 2 Curation Notes

Running notes of judgment calls, deferrals, and KK-attention items
during Plan 2 content curation. Reviewed and emptied at Plan 2 DoD
(Task 24). Not committed to any tag.

## Deferred judgment calls

- Topic 01: Lilian Weng's *LLM Powered Autonomous Agents* is a survey of others' agent papers, not original research — yet it's the canonical reference architecture in the field. Decided: include as primary. Reason: CONTRIBUTING.md's table says "The researcher's own blog post on their own work → primary"; Weng wrote this as her own synthesis and framework from her position as an AI researcher — it's her intellectual contribution, not a recap of a single paper's work. Comparable to a professor's own textbook chapter.
- Topic 01: KK Video 1 — "AI & Cybersecurity: An Introduction" (12 min). Decided: include in Watch. Reason: general-AI primers (3Blue1Brown, Alammar) cover transformer mechanics better; KK's video uniquely frames the same foundations through an explicit security-practitioner lens, answering "why do these components matter for attacks and defenses?" No comparable primary source exists for this specific angle at introductory level.
- Topic 01: Chip Huyen *AI Engineering* Ch1 and Sebastian Raschka *Build a Large Language Model* Ch1 are both behind paywalls (O'Reilly and Manning respectively). Decided: include the official GitHub companion repos instead (chiphuyen/aie-book and rasbt/LLMs-from-scratch), which are free, open, and maintained by the same authors. This preserves the primary-source bar while satisfying the accessibility criterion.

## Scope questions raised during research

- Topic 02: Where does the Anthropic "Building Effective Agents" post belong — topic 01 (foundations) already includes it. Decided: include in topic 02 as well. Reason: the post is the canonical first-principles source for the builder's topic; topic 01 uses it to build a mental model of agent layers, topic 02 uses it as the builder's design reference. Same source, different lens. Not a duplication problem when the topic purpose differs.
- Topic 02: KK videos — per PLAN2-VIDEO-MAP.md, Videos 2, 3, and 6 were all candidates. Video 2 (first RAG app) competes directly with LlamaIndex/LangChain primary docs which are stronger. Video 3 (RAG hallucination) features Transilience demo — excluded per policy. Video 6 (building agentic app) tilts security — excluded, belongs in topic 06. Decision: no Watch section in topic 02; primary sources are sufficient and better.

- Topic 03: KK Video 13 — "Securing MCP: The Essential Developer Checklist" (17:22). Decided: include in Watch. Reason: No primary written source packages a concrete defensive checklist for MCP server/client developers in a single walkthrough — OWASP's cheatsheet is the closest written equivalent but covers third-party adoption governance rather than a developer build-checklist. Video 13 is authored by the practitioner teaching the course (primary under CONTRIBUTING.md's "YouTube video by the person doing the work" criterion) and fills a gap the written primary sources leave open.
- Topic 03: invariantlabs-ai/mcp-scan was acquired by Snyk (Jun 2025) and is also published as snyk/agent-scan. Decided: link to the original invariantlabs-ai/mcp-scan repo because it has more stars (2.2k vs lower for the Snyk fork), the blog post introducing it is still at invariantlabs.ai, and the Snyk acquisition has not broken or archived the original. Cross-noted that snyk/agent-scan is the production successor for enterprise users.
- Topic 03: Windsurf MCP advisory (embracethered.com/blog/posts/2025/windsurf-dangers-lack-of-security-controls-for-mcp-server-tool-invocation/) investigated but excluded. Coverage of the same vulnerability pattern (missing human-in-the-loop, automatic tool invocation) is already supplied by the primary Rehberger post and the Slack MCP advisory. A third Rehberger post would be redundant; the Slack advisory was chosen because it names a first-party (Anthropic) server and includes a responsible-disclosure timeline.
- Topic 03: OWASP MCP Top 10 (owasp.org/www-project-mcp-top-10/) investigated. Status: Incubator Project, Phase 3 Beta, community-led. Excluded: still a draft/beta without a stable version number; the OWASP GenAI cheatsheet (v1.0, Nov 2025) is a more mature and citable primary source for the same security concern space.

- Topic 04: KK Video 4 — "Hacking Chatbots: Prompt Injection & Security Testing" (25:04). Merit: passes — the hands-on applied counterpart to Willison's theoretical posts; no primary written source covers live injection exploitation + defense architecture end-to-end in a single walkthrough. Decided: include in Watch. **Concern: YouTube URL could not be verified during research (WebFetch cannot read YouTube page content; repo has no record of the watch?v= ID for Video 4). URL used is a best-guess placeholder (watch?v=lYg_8Dm0BFo) — KK must confirm or replace this URL before shipping. If URL is wrong, the Watch entry should be updated or the section removed until confirmed.**

- Topic 04: NIST AI 100-2 E2025 ("Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations", Mar 2025, doi.org/10.6028/NIST.AI.100-2e2025) — investigated. The NIST page abstract does not explicitly name "prompt injection" in its keywords (lists: data poisoning, evasion, abuse, privacy breach). The PDF may cover it internally, but the accessibility bar (accessible without login, verifiable) is met via nvlpubs.nist.gov. Decision: excluded from topic 04 — the OWASP LLM01, Google Security Blog, and Anthropic research posts provide more direct, LLM-specific prompt injection taxonomy and defense coverage. NIST 100-2 fits better as a reference in topic 05 (LLM Vulnerabilities) for the broad adversarial ML taxonomy.

- Topic 04: Willison 2025-Nov-2 "New prompt injection papers: Agents Rule of Two and The Attacker Moves Second" (simonwillison.net/2025/Nov/2/new-prompt-injection-papers/) — investigated. This post is a roundup/commentary on two other papers (Meta's Rule of Two and OpenAI+Anthropic+Google's "Attacker Moves Second" study). Excluded: borders on secondary synthesis; the original papers are the primary source. "Attacker Moves Second" paper (arxiv, Oct 2025, 14 authors from OpenAI/Anthropic/Google DeepMind) is a strong candidate for topic 04 Go deeper but could not be confirmed at a stable arxiv ID during research — flag for future curation.

- Topic 04: arxiv 2403.02691 (InjecAgent, Mar 2024) — "Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents." Investigated. Strong paper: 1,054 test cases, 30 LLMs tested, ReAct-prompted GPT-4 vulnerable in ~24% of cases. Excluded: the Go deeper section is already at 5 entries (OWASP, Google, Anthropic, GCG, multi-turn); adding a 6th benchmark paper tips the section toward academic rather than practitioner. Retain as a candidate if the multi-turn paper (2511.03247) is later displaced.

- Topic 05: OWASP LLM08:2025 Vector and Embedding Weaknesses (genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) — investigated as a Go deeper candidate. Excluded: the three OWASP individual entries already included (LLM02, LLM03, LLM04) cover the training-time and data-integrity threat surface; LLM08 addresses RAG-specific retrieval attacks that belong more naturally adjacent to topic 06 (agentic/RAG security). A fourth OWASP sub-entry would tip the section toward OWASP recaps rather than diverse source types.

- Topic 05: Carlini 2021 "Extracting Training Data from Large Language Models" (arxiv.org/abs/2012.07805, USENIX Security 2021) — investigated as a Go deeper candidate. Excluded in favor of the 2023 follow-up (arxiv.org/abs/2311.17035, "Scalable Extraction from Production Language Models") which demonstrates the same attack class at production scale against ChatGPT with a 150× amplification effect. The 2023 paper is strictly more impactful and more relevant to current deployment context. The 2021 paper remains the canonical founding reference but the 2023 paper is the stronger "go deeper" pick.

- Topic 05: HuggingFace "2024 Security Feature Highlights" (huggingface.co/blog/2024-security-features, Aug 2024) — investigated as a supply-chain source. Excluded: the post covers Hub access controls, 2FA, commit signing, and pickle scanning at a feature-announcement level — useful operational reference but not a primary vulnerability research source. The "4M Models Scanned" post (selected) is a better primary-source fit because it reports empirical threat data rather than feature announcements.

- Topic 05: HuggingFace + JFrog partnership post (huggingface.co/blog/jfrog, Mar 2025) — investigated as a supply-chain source. Excluded: coverage of the same supply-chain-scanning concern is more empirically grounded in the Protect AI "4M Models Scanned" post (selected). The JFrog post is a product-launch announcement describing scanner integration rather than threat research; secondary to the Protect AI 6-month findings report.

- Topic 05: "Are aligned neural networks adversarially aligned?" Carlini et al. (arxiv.org/abs/2306.15447, NeurIPS 2023) — investigated as a Go deeper candidate for the model-alignment safety angle. Excluded: scope is primarily about whether RLHF alignment holds under adversarial image perturbations in multimodal models — closer to topic 07 (red teaming) or topic 16 (research frontier) than the training-time and supply-chain remit of topic 05.

- Topic 05: MITRE ATLAS matrix page (atlas.mitre.org/matrices/ATLAS) — URL returns 404; the framework is accessed via the root URL (atlas.mitre.org), which is what was used.

## Tools / links investigated but rejected

- Topic 02: Microsoft AutoGen (github.com/microsoft/autogen) — as of September 2025 the repo entered maintenance mode (v0.7.5 final). Microsoft explicitly recommends new users adopt their successor "Microsoft Agent Framework." Excluded: a deprecated framework is not the right tool reference for a builder who wants to ship in 2025–2026.
- Topic 02: Meta "Agents Rule of Two: A Practical Approach to AI Agent Security" (ai.meta.com/blog/practical-ai-agent-security/, Oct 2025) — confirmed primarily security-focused (the Rule of Two is about mitigating prompt injection risk, not about building patterns). Excluded from topic 02. Goes to topic 06 (agentic security).
- Topic 02: LangChain conceptual docs (docs.langchain.com) — LangChain itself is now mostly a thin wrapper that routes to LangGraph; the docs site redirected and focuses on the LangGraph runtime for agent work. Excluded: LangGraph (already included) is the more specific, primary reference for the stateful-agent use case. Including both would be redundant.
- Topic 02: LlamaIndex "Introduction to RAG" page (developers.llamaindex.ai/python/framework/understanding/rag/) — covers the same conceptual territory as "Building RAG from scratch" but at a higher level of abstraction. Excluded in favor of the more mechanistic "from scratch" page which better serves the builder who wants to understand internals.

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
