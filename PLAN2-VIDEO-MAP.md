# KK YouTube Video -> Topic Mapping (Plan 2)

Source course: "AI and Cybersecurity - Foundations to Red Teaming", ~7.5 hours across 25 videos.
Assessment rule (per design spec section 7): a video lands in a topic's `## Watch` section ONLY
if it is the best-or-tied-best resource for that topic. Each inclusion below lists the
merit reason. Exclusions are not listed - they were evaluated and did not meet the bar.

This file is deleted at Plan 2 DoD (Task 24) - it's a working record, not a permanent artifact.

---

## Video-by-video assessment

### Chapter 1 foundations
- **Video 1 - AI & Cybersecurity: An Introduction (12:12).** Candidate for `01-foundations`. Assess against: Lilian Weng's LLM post, Chip Huyen's Agents post, 3Blue1Brown's transformer series. Likely **merit-bound**: KK's video covers the *intersection* specifically, which the general-AI primers don't. Include if primary-source-competitive in `01-foundations.md ## Start here`. (DEFER final decision to Task 5 research.)

### Chapter 2 RAG
- **Video 2 - Building your first RAG app (17:23).** Candidate for `02-building-llm-apps`. Competes with Anthropic's RAG guide, LangChain docs, Chroma's docs. Likely **not best-in-class** for pure RAG mechanics (those are written by the tool authors); DEFER to Task 6 research.
- **Video 3 - Countering LLM Hallucinations with RAG (20:57).** Has Transilience AI product demo - per spec, Transilience content goes in AI-for-* topics, not here. Likely **EXCLUDE** from `02-building-llm-apps`. May reappear in `13-ai-for-vulnerability-management` depending on what Transilience's RAG-grounding tool actually does.

### Chapter 3 prompt injection
- **Video 4 - Hacking Chatbots: Prompt Injection & Security Testing (25:04).** Candidate for `04-prompt-injection`. Competes with Simon Willison's prompt-injection series. KK shows hands-on exploitation + defense architecture, which is the *applied* counterpart to Willison's *theoretical* treatment. Likely **INCLUDE** in `04-prompt-injection.md ## Watch` with annotation noting hands-on complement.
- **Video 5 - How To Hack AI (Lakera Gandalf) (16:44).** Competes with Lakera's own Gandalf write-ups. Lakera's primary; KK's is a walkthrough. Likely **EXCLUDE**; DEFER to Task 8 confirmation.

### Chapter 4 building & attacking agentic AI
- **Video 6 - Building Your First Agentic AI App (18:44).** Candidate for `02-building-llm-apps` or `06-agentic-security`. Competes with Anthropic's *Building Effective Agents* and Chip Huyen's agent post. Those are better at concepts; KK is better at hands-on with security flavor. Likely **INCLUDE** in `06-agentic-security.md ## Watch` (under-tested vulns is the hook). DEFER to Task 10.
- **Video 7 - LLM Vulnerabilities Explained (5:39).** 5 minutes is too terse to beat OWASP's own LLM Top 10 overview. Likely **EXCLUDE**.

### Chapter 5 red teaming agentic AI (3 parts, 66 min total)
- **Videos 8, 9, 10 - Red Teaming Agentic AI parts 1-3.** Candidate for `07-red-teaming`. Competes with CSA's Agentic Red Teaming Guide, PyRIT docs, MAESTRO framework. KK's 66-minute deep-dive may be the most thorough practitioner-level red-teaming walkthrough publicly available. Likely **INCLUDE the 3-part series** in `07-red-teaming.md ## Watch` as a single bundled entry. DEFER to Task 11.

### Chapter 6 MCP (3 parts, 77 min total)
- **Videos 11, 12, 13 - MCP: Intro/Demo/Security, Hacking MCP, Securing MCP Checklist.** Candidates for `03-mcp`. Competes with the MCP official spec, Anthropic's MCP intro post, Johann Rehberger's MCP security series. Likely **INCLUDE** Video 13 (the developer checklist) in `03-mcp.md ## Watch` - defensive checklists are under-served in primary sources. Videos 11 and 12 compete with Rehberger's blog which is more surgical; likely **EXCLUDE**. DEFER to Task 7.

### Chapter 7 multi-agent (3 parts, 48 min total)
- **Videos 14, 15, 16 - Multi-Agent AI: Build, Hack, Secure.** Candidates for `06-agentic-security`. Competes with the Anthropic rule-of-two blog and the CrewAI docs. Likely one of the build/hack/secure trilogy wins on hands-on multi-agent security; DEFER to Task 10.

### Chapter 8 AI-powered pentest tools (4 parts)
- **Videos 17, 18, 19, 20 - Strix, Kali-MCP+Burp-MCP, Claude Code, Bake-Off.** Candidates for `12-ai-for-pentesting`. Each competes with the respective tool's own GitHub repo. The **Bake-Off video (Video 20)** is likely unique - no one else has published a comparative evaluation. Likely **INCLUDE** Video 20 in `12-ai-for-pentesting.md ## Watch`. Videos 17-19 likely **EXCLUDE** (tool READMEs are primary). DEFER to Task 16.

### Chapter 9 OWASP LLM Top 10 (4 parts)
- **Videos 21, 22, 23, 24.** Candidates for `05-llm-vulnerabilities` and `04-prompt-injection` (Video 24 is the prompt-injection installment). Competes with OWASP's own LLM Top 10 2025 document. OWASP primary always wins on these; likely **EXCLUDE all four** unless one video has hands-on that OWASP's PDF doesn't. DEFER to Tasks 8 and 9.

### Chapter 10 AI-powered vuln management (bonus)
- **Video 25 - Vulnerability Prioritization Walkthrough with Transilience AI (13:34).** Transilience demo - per spec, if the Transilience tool fits `13-ai-for-vulnerability-management` and meets the bar, the video could accompany it in `## Watch`. DEFER to Task 17 after Transilience inventory.
