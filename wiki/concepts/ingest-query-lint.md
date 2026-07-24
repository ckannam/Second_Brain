---
type: concept
---

# Ingest, Query, Lint

The three operations of the [[llm-wiki-pattern]] ([[llm-wiki-karpathy]]). This vault's
concrete versions live in `CLAUDE.md`.

## Ingest

Drop a source into `raw/` and ask the LLM to process it: read it, discuss takeaways,
write a source summary page, create/update relevant entity and concept pages (a single
source may touch 10–15 pages, noting contradictions), update `index.md`, append to
`log.md`. Best done one source at a time with the human involved.

## Query

Ask a question against the wiki: read `index.md`, drill into relevant pages, synthesize
an answer with citations. **Valuable answers get filed back into the wiki** as new pages,
so explorations compound just like ingested sources.

## Lint

Periodic health check: find contradictions, stale claims, orphan pages, missing concept
pages, missing cross-references, and data gaps worth a web search. Suggest new questions
and sources.

Related: [[matt-wolfe]]'s [[second-brain-system]] adds journal and CRM operations on top
of these three.
