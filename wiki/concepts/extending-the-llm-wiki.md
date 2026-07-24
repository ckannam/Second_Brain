---
type: concept
created: 2026-07-24
---

# Extending the LLM Wiki

A forward roadmap for this vault: how [[andrej-karpathy]]'s [[llm-wiki-pattern]] is already
instantiated here, and how to keep building along his own trajectory. Where
[[llm-wiki-pattern]] is *the idea* and [[second-brain-system]] is *an instantiation*, this
page is *the direction of travel*. Filed from a query on 2026-07-24.

## The insight being extended

Karpathy's core claim: the hard part of a knowledge base is the **bookkeeping**, not the
reading or thinking. LLMs don't get bored and can touch ~15 files per pass, so maintenance
cost approaches zero — knowledge is **compiled once and kept current** rather than re-derived
per query ([[llm-wiki-vs-rag]]). Everything below pushes maintenance cost further toward zero
and hands more of the loop to the agent.

## Already built in

- **Three layers** — `raw/` (immutable) · `wiki/` (LLM-owned) · schema (`AGENTS.md`) — are
  Karpathy's structure verbatim ([[llm-wiki-pattern]]).
- **`index.md` + `log.md`** navigation and the [[ingest-query-lint]] loop.
- **"Enrich before you accumulate / links > pages"** — his compounding-artifact principle as
  a house rule.
- **The `wiki-query` skill** (`.claude/skills/wiki-query/`) — its mandatory file-back step is
  the anti-RAG move at query time: every answer becomes a persistent, cross-linked artifact.
  Pointing it at `AGENTS.md` instead of copying the rules is "schema as single disciplined
  maintainer" applied to the tooling.

## Roadmap (Karpathy's own signals → next rungs)

| Karpathy signal (source) | Next rung for this vault |
|---|---|
| Praises [[openclaw]] **memory systems** ([[skill-issue-karpathy-sarah-guo]]) | Wire in [[claude-code-memory]] (Memory 2.0 / Auto Dream): out-of-band consolidation — a "dreaming" [[ingest-query-lint\|lint]] that curates the graph while away. |
| **Parallelize; you're the bottleneck** | Escalate big ingests/lints to [[parallel-agents]] / [[multi-agent-orchestration]] — the escalation path not yet built into `wiki-query`. |
| **AutoResearch** — close the loop ([[autoresearch]]) | [[claude-code-scheduled-tasks]] + [[proactive-agents]]: a cron lint that finds graph gaps *and seeks new sources* — the vault researching itself. |
| [[qmd]] optional search tooling | A local markdown-search fallback for when index-summary retrieval isn't enough (the grep-sweep option shelved from the skill design). |
| **Self-healing** ([[agentic-workflows]], [[self-healing-workflows]]) | Point self-healing at the vault's own upkeep: broken wikilinks, orphan pages, stale model claims fixed autonomously. |

## The throughline

Each rung is a step up the [[ai-second-brain-levels]] ladder — from a well-maintained manual
wiki toward Karpathy's end state where the wiki **maintains, extends, and researches itself**
and the human mostly curates sources and asks questions.
