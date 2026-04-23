---
title: Foundations
summary: "Mental model for transformers, RAG, agents, and MCP. Just enough to reason about attacks and defenses."
last-reviewed: 2026-04-22
status: ready
---

# Foundations

Transformers, RAG pipelines, agents, and the Model Context Protocol are the four substrate concepts that recur across every subsequent topic in this map. You do not need to train a model to reason about their attack surfaces — but you do need an accurate mental model of what each component does, what it can be told, and what it can be made to invoke. A security practitioner who conflates "the model" with "the system" will misread the threat landscape: prompt injection, tool abuse, data exfiltration through embeddings, and MCP server compromise all exploit different layers of the stack.

This topic builds that mental model. The sequencing is deliberate: start with how agents and LLM applications are *structured* (Anthropic, Huyen, Weng), then understand the transformer mechanism that underlies them (Alammar, 3Blue1Brown, Vaswani), then see how MCP extends the attack surface outward to external tools and data sources. Readers who already have the agent-level picture and want the transformer internals can jump directly to Go deeper.

## Start here

- [Building effective agents](https://www.anthropic.com/research/building-effective-agents) `[blog]` — Anthropic's own taxonomy of agent patterns (workflows vs. agents, prompt chaining, orchestrator-subagent, evaluator-optimizer); read this before reasoning about which patterns expand the attack surface and how. (Anthropic, Dec 2024)

- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) `[blog]` — The canonical reference architecture for LLM agents: planning, memory, and tool-use as first-class components; every agent-security paper that followed cites this framing. (Lilian Weng, Jun 2023)

- [Agents](https://huyenchip.com/2025/01/07/agents.html) `[blog]` — Huyen's own analytical framework for agents, covering tool calling, plan generation, reflection patterns (ReAct), and — crucially — failure modes that map directly onto security-relevant misbehavior. (Chip Huyen, Jan 2025)

- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) `[blog]` — Anthropic's announcement of MCP as an open standard for connecting AI assistants to external systems; establishes the vocabulary (host, client, server, tools, resources, prompts) before the full security treatment in → Topic 03. (Anthropic, Nov 2024)

## Go deeper

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) `[blog]` — The definitive visual walkthrough of transformer architecture, attention heads, and the encoder-decoder structure; read when you need mechanistic grounding sufficient to trace where prompt injection exploits attention routing. (Jay Alammar, Jun 2018, updated 2025)

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) `[paper]` — The original transformer paper; useful for the precise terminology (query/key/value matrices, multi-head attention, positional encoding) that security papers cite when discussing context-window limits and attention manipulation. (Vaswani et al., Jun 2017)

- [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) `[repo]` — Official companion code to Sebastian Raschka's *Build a Large Language Model from Scratch* (Manning 2024); 91k-star repo that gives implementation-level grounding — tokenization through pretraining through fine-tuning — without a paywall.

- [aie-book](https://github.com/chiphuyen/aie-book) `[repo]` — Official supporting materials for Chip Huyen's *AI Engineering* (O'Reilly 2025); the `resources.md` file is the most useful free artifact — a curated pointer list for foundation-model engineering concepts that the book elaborates.

## Watch

- [But what is a GPT? (Ch 5)](https://www.youtube.com/watch?v=wjZofJX0v4M) and [Attention in transformers (Ch 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc) `[video]` — 3Blue1Brown's two-part visual series on transformer structure and the attention mechanism; best-in-class for building the mental model of how token prediction works before reading papers that exploit it. (Grant Sanderson / 3Blue1Brown, Apr 2024)

- [Chapter 1: AI & Cybersecurity — An Introduction](https://www.youtube.com/watch?v=caSd12M5Axk) `[video]` — The only widely available resource that explicitly frames AI foundations through a security-practitioner lens rather than an ML-research lens; fills the gap that general-AI primers leave for readers asking "why does this matter for attacks and defenses?" (KK Mookhey / Transilience AI, 2024, 12 min)

## Related topics

- [→ 02 Building LLM Apps](./02-building-llm-apps.md)
- [→ 03 MCP](./03-mcp.md)
- [→ 05 LLM Vulnerabilities](./05-llm-vulnerabilities.md)
