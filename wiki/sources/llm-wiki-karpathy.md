---
type: source
source: web
format: gist
url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
author: "Andrej Karpathy"
ingested: 2026-07-23
---

# Source: LLM Wiki (Karpathy gist)

By [[andrej-karpathy]]. The foundational idea file this whole vault is built on.

## Summary

Proposes the [[llm-wiki-pattern]]: instead of RAG (re-retrieving from raw docs on every
query), the LLM **incrementally builds and maintains a persistent, interlinked wiki** of
markdown files that compounds over time. Knowledge is compiled once and kept current, not
re-derived per query.

Key points:
- **Three layers**: immutable raw sources → the LLM-owned wiki → the schema
  (`CLAUDE.md`/`AGENTS.md`) that makes the LLM a disciplined maintainer.
- **Three operations**: [[ingest-query-lint|ingest, query, lint]].
- Two navigation files: `index.md` (content catalog) and `log.md` (chronological).
- The human curates sources and asks questions; the LLM does all bookkeeping.
- Workflow in practice: LLM agent on one side, [[obsidian]] on the other. "Obsidian is
  the IDE; the LLM is the programmer; the wiki is the codebase."
- Related in spirit to Vannevar Bush's **Memex** (1945) — the unsolved part was who does
  the maintenance; the LLM solves that.
- Optional tooling: [[qmd]] search, Marp slides, Dataview, git backing.

## Why it matters here

This is the source of truth for how this vault operates. The schema in `CLAUDE.md` is a
concrete instantiation of this pattern.
