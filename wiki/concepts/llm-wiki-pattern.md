---
type: concept
---

# LLM Wiki pattern

A pattern for personal knowledge bases, from [[andrej-karpathy]]
([[llm-wiki-karpathy]]). The core move: instead of RAG — where the LLM re-retrieves and
re-synthesizes from raw documents on every query, accumulating nothing — the LLM
**incrementally builds and maintains a persistent, interlinked wiki** of markdown files
that sits between you and the sources. Knowledge is compiled once and kept current.

## Why it beats RAG

RAG rediscovers knowledge from scratch each query; nothing compounds. The wiki is a
**persistent, compounding artifact**: cross-references already exist, contradictions are
already flagged, the synthesis already reflects everything read. It gets richer with
every source added and every question asked.

## Three layers

1. **Raw sources** — immutable source of truth (`raw/`). Read, never modified.
2. **The wiki** — LLM-owned markdown pages (`wiki/`): summaries, entities, concepts,
   comparisons, overview, synthesis.
3. **The schema** — `CLAUDE.md`/`AGENTS.md`: conventions + workflows that make the LLM a
   disciplined maintainer rather than a generic chatbot.

## Operations & navigation

Runs on [[ingest-query-lint]], with `index.md` (content catalog) and `log.md`
(chronological) for navigation.

## Why it works

The hard part of a knowledge base isn't reading or thinking — it's the **bookkeeping**.
Humans abandon wikis because maintenance outpaces value. LLMs don't get bored and can
touch 15 files in one pass, so maintenance cost approaches zero. Lineage: Vannevar Bush's
**Memex** (1945), whose unsolved problem was who maintains the trails.

## Instantiations

[[matt-wolfe]] extended it into a full [[second-brain-system]] (wiki + journal + CRM).
See [[extending-the-llm-wiki]] for how this vault instantiates the pattern and the roadmap
for pushing it further along Karpathy's own trajectory.
