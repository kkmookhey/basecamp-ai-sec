---
title: Model Context Protocol
summary: "MCP spec, implementations, and security posture. Its own topic because the surface is huge and evolving fast."
last-reviewed: 2026-04-22
status: ready
---

# Model Context Protocol

MCP standardised how AI assistants talk to tools and data sources — an open, JSON-RPC-based protocol that replaced a hundred bespoke integrations with one common vocabulary: host, client, server, tools, resources, prompts. Since Anthropic published the spec in late 2024 it has become the de-facto control plane for agentic AI, supported by Claude, ChatGPT, VS Code Copilot, Cursor, and hundreds of third-party servers.

That standardisation opened a large new attack surface. Every MCP server is a trust boundary decision; every tool description is untrusted text that flows into the model's context; every client that auto-invokes tools without human confirmation is a remote-code-execution path waiting to be triggered. The sources below cover the spec itself, its reference implementations, and the security primitives — tool poisoning, rug pulls, prompt injection via tool metadata, data-exfiltration vectors — that practitioners have had to map and defend against as adoption has accelerated.

## Start here

- [MCP Specification (2025-03-26)](https://modelcontextprotocol.io/specification/2025-03-26) `[spec]` — The authoritative protocol document: JSON-RPC 2.0 message format, capability negotiation, lifecycle management, and the security and trust principles that all implementors MUST address (user consent, data privacy, tool safety, LLM sampling controls). The version-dated URL locks to the current stable release. (MCP Steering Group, Mar 2025)

- [MCP Architecture Overview](https://modelcontextprotocol.io/docs/concepts/architecture) `[docs]` — The reference for MCP's two-layer design: a data layer (tools, resources, prompts, sampling, elicitation) over a transport layer (stdio for local processes, Streamable HTTP for remote servers). Establishes the host-client-server participant model and the security boundary between them. (modelcontextprotocol.io, maintained 2025–2026)

- [MCP: Untrusted Servers and Confused Clients, Plus a Sneaky Exploit](https://embracethered.com/blog/posts/2025/model-context-protocol-security-risks-and-exploits/) `[blog]` — Johann Rehberger's primary MCP security post: demonstrates tool-metadata prompt injection, hidden Unicode Tag instructions in tool descriptions, and a cross-application exploit chain across Claude Desktop, GitHub Copilot, and Cursor — showing concretely why tool metadata is an untrusted attack surface. (wunderwuzzi / Embrace The Red, May 2025)

- [CheatSheet: A Practical Guide for Securely Using Third-Party MCP Servers](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/) `[guide]` — OWASP GenAI Security Project's v1.0 framework for organisations adopting external MCP servers: threat taxonomy (tool poisoning, rug pulls, prompt injection, memory poisoning, tool interference), authentication and authorisation controls, sandboxing, and a governance workflow built around a trusted MCP registry. (OWASP GenAI Security Project, Nov 2025)

- [A Primer on Model Context Protocol Secure Implementation](https://cloudsecurityalliance.org/blog/2025/06/23/a-primer-on-model-context-protocol-mcp-secure-implementation) `[blog]` — CSA Fellow Ken Huang and co-author Dr. Ying-Jung Chen walk through a full implementation — server, host, and client — then apply the MAESTRO framework across seven security layers, including working insecure code examples showing SQL injection, arbitrary code execution, and authorization failures alongside the hardening fixes. (Ken Huang / CSA, Jun 2025)

## Go deeper

- [Model Context Protocol: Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278) `[paper]` — The comprehensive academic survey of MCP: maps the full server lifecycle into 16 activities across four phases, builds a threat taxonomy covering four attacker categories and 16 threat scenarios, and validates findings with real-world case studies. The reference paper for anyone who needs a structured threat model rather than practitioner anecdotes. (Hou, Zhao, Wang, Wang; submitted Mar 2025, revised Oct 2025)

- [Model Context Protocol has prompt injection security problems](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) `[blog]` — Willison's own analysis of MCP's structural security problems: rug pulls, tool shadowing, tool poisoning, data exfiltration via WhatsApp MCP, and horizontal-scrollbar obfuscation tricks — with his key observation that "mixing tools with untrusted instructions is inherently dangerous" regardless of implementation quality. (Simon Willison, Apr 2025)

- [Securing the Agentic AI Control Plane: Announcing the MCP Security Resource Center](https://cloudsecurityalliance.org/blog/2025/08/20/securing-the-agentic-ai-control-plane-announcing-the-mcp-security-resource-center) `[blog]` — CSA's launch post for their MCP Security Resource Center, authored by Kurt Seifried (CSA CIO): contextualises the scale of MCP deployment (70+ clients, 16,000+ public servers within eight months), introduces the Top 10 MCP Server Security Risks and Top 10 MCP Client Security Risks frameworks, and links to the open audit and vulnerability databases at modelcontextprotocol-security.io. (Kurt Seifried / CSA, Aug 2025)

- [Security Advisory: Anthropic's Slack MCP Server Vulnerable to Data Exfiltration](https://embracethered.com/blog/posts/2025/security-advisory-anthropic-slack-mcp-server-data-leakage/) `[blog]` — Rehberger's responsible-disclosure advisory against Anthropic's own deprecated Slack MCP server: exploits the "lethal trifecta" (private data access + untrusted input + exfiltration channel) via link-unfurl leakage; CVSS 8.7–9.3 across multiple AI evaluators. Illustrates that even first-party reference servers carry production risk. (wunderwuzzi / Embrace The Red, Jun 2025)

## Tools

- [invariantlabs-ai/mcp-scan](https://github.com/invariantlabs-ai/mcp-scan) `[tool]` — The most-adopted open-source MCP security scanner (2.2k stars; acquired by Snyk, Jun 2025, now also at snyk/agent-scan). Scans installed MCP server configurations and tool descriptions for prompt injection, tool poisoning, tool shadowing, rug pull attacks, and cross-origin escalation. Run with `uvx mcp-scan@latest`; supports Claude Desktop, Cursor, Windsurf, VS Code, and Gemini CLI. (Invariant Labs / Snyk, Apr 2025, v0.4.17 Apr 2026)

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) `[repo]` — Anthropic's official reference server repository (84k stars): Filesystem, Git, Fetch, Memory, Sequential Thinking, Time, and Everything servers, each demonstrating how to give LLMs secure, controlled access to a specific resource class. The canonical starting point for understanding what a well-structured MCP server looks like before auditing third-party ones. (Anthropic MCP Steering Group, maintained through Jan 2026)

## Watch

- [Chapter 6.3: Securing MCP — The Essential Developer Checklist](https://www.youtube.com/watch?v=D8CWFwYRJMM) `[video]` — Practical defensive checklist for developers building or operating MCP servers and clients: covers authentication, authorisation, input validation, human-in-the-loop controls, and monitoring. Included because no primary written source packages the same concrete checklist in a single walkthrough — practitioner-authored from the person teaching the course, not a recap of others' work. (KK Mookhey / Transilience AI, Oct 2025, 17 min)

## Related topics

- [→ 02 Building LLM Apps](./02-building-llm-apps.md)
- [→ 06 Agentic Security](./06-agentic-security.md)
- [→ 08 Attacking AI Tooling](./08-attacking-ai-tooling.md)
