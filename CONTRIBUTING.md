# Contributing to Basecamp

Basecamp is a curated learning map. Every link earns its place. This document explains the bar and the flow.

## The quality bar

A link ships only if it meets **all** of these:

1. **It's a primary source** (see below).
2. **It's dated or versioned** so staleness is visible.
3. **It's accessible without login** where possible.
4. **It isn't duplicative** of a better link already in the topic.

## Definition: "primary source"

**A primary source is authored by the person or organization doing the work, not a recap or explainer of someone else's work.**

| Link type | Verdict |
|-----------|---------|
| A paper on multi-turn LLM attacks | ✅ Primary |
| A LinkedIn post summarizing that paper | ❌ Secondary — excluded |
| A tool's official GitHub README | ✅ Primary |
| A blog post reviewing that tool | ⚠️ Secondary — included only if it adds analysis the primary doesn't |
| A transcribed interview with the researcher | ❌ Secondary |
| The researcher's own blog post on their own work | ✅ Primary |
| A YouTube video by the person doing the work | ✅ Primary |
| A summary video about someone else's work | ❌ Secondary |

This bar is deliberate. High-quality explainers fail it and that's okay — Basecamp routes readers to the source, not to intermediaries.

## Not in scope

Basecamp covers the intersection of AI and cybersecurity. It does not cover:

- **General cybersecurity learning** — OSCP prep, CTF walkthroughs, classical penetration testing — other resources cover these well.
- **General ML / data-science tutorials** — how to train a classifier, EDA, feature engineering.
- **Academic ML theory** beyond what's needed to reason about threat models.
- **Training-time AI development** beyond the security implications surfaced in topics 05 and 16.
- **Opinion takes or rants** — find those on social media.
- **Non-English-only resources** where a comparable English source exists.

If your contribution lands in one of these categories, we thank you for the thought but cannot accept it. This isn't a judgment of quality — it's a scope boundary.

## How to contribute

### Adding a link

Open a PR using the "Add link" template. Your PR must answer:

1. What's the link?
2. Which topic file does it belong in, and in which section (`## Start here`, `## Go deeper`, `## Tools`, `## Watch`)?
3. Why does it meet the primary-source bar?
4. What's the one-line annotation? (Why read this — not what it is.)
5. Does it replace an existing link? If so, which one, and why is yours better?

Replacement-oriented PRs are strongly preferred over additive ones. Quality floor beats quantity.

### Adding a new topic

Open an issue first. New topics require a spec change and wide discussion.

### Fixing a dead link

Open a PR using the "Replace link" template with the replacement already identified. A dead link with no proposed replacement can go into an issue instead.

## How contributions get reviewed

Reviewer runs through this mental checklist:

- Does the link meet the primary-source bar?
- Does the annotation answer "why read this"?
- Is it in the right topic and the right section?
- Does it duplicate or displace an existing link cleanly?
- Would removing an existing link make room without loss? If yes, make the swap.

## Repo discipline

Topic files use *only* these five H2s, verbatim:

- `## Start here` (required)
- `## Go deeper` (required)
- `## Tools` (optional)
- `## Watch` (optional)
- `## Related topics` (required)

Reason: paths route to topic files via GitHub-auto-generated anchors (e.g., `topics/04-prompt-injection.md#start-here`). A fixed H2 vocabulary keeps anchors stable. The CI (`integrity.yml`) enforces this; your PR will fail if you introduce a new H2.

## Tests

Run tests locally before pushing:

```bash
pip install -e ".[dev]"
pytest tests/
```

All tests must pass. Link-check runs on PR automatically.
