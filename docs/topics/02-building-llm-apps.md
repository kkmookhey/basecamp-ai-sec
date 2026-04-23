---
title: Building LLM Apps & Agents
summary: "Frameworks, RAG patterns, agent architectures, multi-agent coordination — the build half of build→break→secure."
last-reviewed: 2026-04-22
status: ready
---

# Building LLM Apps & Agents

The builder's problem shifted between 2023 and 2025: from *How do I call an LLM?* to *How do I compose LLM calls into a reliable workflow?* The patterns — prompt chaining, RAG, tool use, orchestrator-worker, evaluator-optimizer — are now well-enough understood that first-principles writing on them is abundant. What's scarce is the judgment to pick the right pattern for a given task: when a simple chain beats a full agent loop, when RAG is cheaper than fine-tuning, when a multi-agent graph earns its complexity. These sources supply both the patterns and that judgment.

This topic is the build half of build→break→secure. Security-specific agent concerns (prompt injection in agentic loops, least-privilege for tool-calling agents, agentic red-teaming) live in → Topic 06. MCP specifically — the protocol that connects agents to external tools and data — lives in → Topic 03.

## Start here

- [Building effective agents](https://www.anthropic.com/research/building-effective-agents) `[blog]` — Anthropic's own taxonomy of agentic patterns: augmented LLM, prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, and autonomous agents. The clearest first-principles treatment of when to reach for each pattern and when simpler is better. Read before choosing a framework. (Erik Schluntz & Barry Zhang / Anthropic, Dec 2024)

- [Agents](https://huyenchip.com/2025/01/07/agents.html) `[blog]` — Huyen's analytical framework for what makes an agent: tools (knowledge-augmenting, capability-extending, state-writing), planning patterns (sequential, parallel, conditional, ReAct, Reflexion), and failure modes. The failure-modes section is the most practically useful for building reliable systems. (Chip Huyen, Jan 2025)

- [A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) `[guide]` — OpenAI's distillation of lessons from production agent deployments: when to use single vs. multi-agent topologies, how to define tools and guardrails, and an orchestration decision framework grounded in real deployment patterns rather than toy examples. (OpenAI, 2025)

## Go deeper

- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) `[blog]` — Anthropic's engineering team on the orchestrator-worker architecture behind Claude's Research feature: how lead agents decompose queries and spawn parallel subagents, how they handle context-window limits via memory persistence, and what they learned from evaluating single-agent vs. multi-agent tradeoffs ("90.2% improvement," "15× more tokens than chats"). First-person production account. (Jeremy Hadfield et al. / Anthropic, Jun 2025)

- [Building RAG from scratch](https://developers.llamaindex.ai/python/framework/optimizing/building_rag_from_scratch/) `[docs]` — LlamaIndex's component-level walkthrough of RAG pipelines: data ingestion, indexing, retrieval, and response synthesis — built piece by piece rather than via high-level abstractions, so readers understand what the abstractions hide. Authored and maintained by the LlamaIndex team. (LlamaIndex, updated 2025)

- [Advanced RAG: a cheat sheet and recipes](https://www.llamaindex.ai/blog/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b) `[blog]` — LlamaIndex team's practical map of advanced retrieval strategies: chunk optimization, structured knowledge, re-ranking, query rewriting, and hybrid search — with runnable LlamaIndex recipes for each. Useful after you understand basic RAG and need to improve retrieval quality. (LlamaIndex team, Jan 2024)

- [anthropic-cookbook / patterns/agents](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents) `[repo]` — Anthropic's official collection of executable agent notebooks: orchestrator-subagent patterns, tool-use recipes, multi-agent research workflows, and Claude Agent SDK examples. The reference implementation that accompanies "Building effective agents." (Anthropic, maintained 2024–2025)

- [aie-book resources](https://github.com/chiphuyen/aie-book) `[repo]` — Chip Huyen's official companion repo for *AI Engineering* (O'Reilly 2025); the `resources.md` file is a curated pointer list covering evaluation, RAG, agents, and deployment. Focus here on the agents and RAG chapters (chapters 6–9) for the builder's perspective; topic 01 uses this repo for foundations.

## Tools

- [LangGraph](https://github.com/langchain-ai/langgraph) `[framework]` — LangChain's stateful, graph-based agent orchestration framework. Primary strengths: durable execution (agents resume after failure), human-in-the-loop state inspection, persistent memory across sessions, and a deployment runtime. Version CLI 0.4.24 as of April 2026. Actively maintained by LangChain Inc.

- [CrewAI](https://github.com/crewAIInc/crewAI) `[framework]` — Role-based multi-agent framework built independently of LangChain. Supports both "Crews" (collaborative autonomous agents) and "Flows" (event-driven, deterministic workflows). Version 1.14.2, 179 releases, actively maintained. Well-suited for tasks that benefit from explicit agent roles and delegation.

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) `[framework]` — OpenAI's lightweight multi-agent SDK (successor to Swarm). Core primitives: agents (LLM + instructions + tools), handoffs (agent-to-agent delegation), guardrails (input/output validation), and sessions (conversation history). Provider-agnostic; supports 100+ LLMs beyond OpenAI. Version 0.14.4, actively maintained.

## Related topics

- [→ 01 Foundations](./01-foundations.md)
- [→ 03 MCP](./03-mcp.md)
- [→ 06 Agentic Security](./06-agentic-security.md)
