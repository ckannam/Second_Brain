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
| **Parallelize; you're the bottleneck** | Escalate big ingests/lints to [[parallel-agents]] / [[multi-agent-orchestration]] — the escalation path not yet built into `wiki-query`. Karpathy's [[agent-hub]] is the reference *substrate* for this rung (a swarm on a branch-less DAG); adopting it would need a collapse step back onto the reviewed `main` — see the relevance evaluation on [[agent-hub]]. |
| **AutoResearch** — close the loop ([[autoresearch]]) | [[claude-code-scheduled-tasks]] + [[proactive-agents]]: a cron lint that finds graph gaps *and seeks new sources* — the vault researching itself. |
| [[qmd]] optional search tooling | A local markdown-search fallback for when index-summary retrieval isn't enough (the grep-sweep option shelved from the skill design). |
| **Self-healing** ([[agentic-workflows]], [[self-healing-workflows]]) | Point self-healing at the vault's own upkeep: broken wikilinks, orphan pages, stale model claims fixed autonomously. |

**Shipped 2026-07-24:** the self-healing + AutoResearch rungs are now built — see
[[vault-autoresearch]] (git ratchet + a HEALTH_DEBT metric). The scheduled *source-seeking*
rung remains open.

## Source-seeking design (MODE C sketch — 2026-09-27)

The self-healing + generative rungs are operational, but the vault still depends entirely on
Cole to *supply* sources. The source-seeking rung closes that loop: the routine scans public
surfaces, scores candidate sources against the vault's topic frontier, and proposes the
highest-value ones in the morning PR for Cole to approve before anything is ingested.

### What it seeks

| Surface | Rationale |
|---|---|
| arXiv `cs.AI` + `q-bio` daily digest | Covers the hard-science side of Cole's topic clusters (spaced learning, neurotech, LLM architecture) |
| HN front page + "Ask HN Who is Hiring" | Startup radar + AI tooling news; overlaps `startup-radar` skill but different signal (discourse, not just jobs) |
| YouTube channel RSS for existing vault channels | New uploads by [[nate-herk]], [[andrej-karpathy]], [[sarah-guo]], [[the-economist]] etc. that the vault already references |
| Newsletter issues (Substack RSS) | Next Play, a16z, Lenny's — already in the job-search orbit |

### Scoring a candidate

A source earns a score based on overlap with the vault's open frontier:
1. **Topic match**: does it touch a concept already in the wiki with thin coverage (e.g. a 3-line stub) or a dangling `[[link]]` target? More overlap = higher score.
2. **Freshness**: does it report something dated after the vault's most recent entry on that topic? Avoids re-ingesting ground already covered.
3. **Novelty bonus**: does it introduce a concept, person, or organization *not yet in the vault* that passes the new-page test (`AGENTS.md` §Ingest)?
4. **Cole-relevance filter**: hard filter — drop sources unrelated to Cole's active areas (Neuro, AI/LLM, Fulbright/entrepreneurship, Job Search, neuroscience).

### Output

The routine does **not** ingest autonomously. It proposes in the morning PR:
```
## Source-seeking proposals (MODE C)

1. [arXiv 2509.XXXXX] "Title" — new claims on [[spacing-effect]] (thin page); adds the 2026 protocol update.
2. [YouTube] New Nate Herk upload: "Claude Code X" — covers [[claude-code-hooks]] and a new pattern not yet in wiki.
```
Cole approves by merging the PR; the next run ingests approved proposals via the normal ingest
workflow. This keeps the human in the sourcing loop while offloading the *scanning* step.

### Implementation path (deferred to Cole)

The design fits as a new **Phase 2.5** in `program.md` between Phase 2 (Build) and Phase 3
(Write-back), running on the branch. Concretely: one `WebSearch`/`WebFetch` sweep per surface,
scored against `score.py --json`'s dangling-links list + index topic set, top 2–3 proposals
appended to the PR description. The scoring is heuristic (not `score.py`–verifiable), so it
belongs in the review lane — exactly the right posture for content that needs a human eye.

**Shipped 2026-09-27:** this design section. Implementation in `program.md` is deferred pending
Cole's review (in the morning PR).

## The throughline

Each rung is a step up the [[ai-second-brain-levels]] ladder — from a well-maintained manual
wiki toward Karpathy's end state where the wiki **maintains, extends, and researches itself**
and the human mostly curates sources and asks questions.

The furthest rung is a shift in *kind*, not degree: [[agent-native-infrastructure]] — rebuilding
the tooling itself around agent swarms rather than human readers (Karpathy's [[agent-hub]] is the
version-control instance). This vault is already partway there (`AGENTS.md` as a machine-read
schema, `index.md`/`log.md` as catalog+log) while keeping version control human-native, which is
the right posture for a single-agent loop — see [[agent-native-infrastructure]] for when the swarm
rung actually pays off.
