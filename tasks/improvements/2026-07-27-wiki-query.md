# Improve — wiki-query skill (2026-07-27)

**Target type:** skill / workflow (primary). **Metric-shaped?** No — `score.py` not consulted.

## Diagnosis (gap vs. vision)

`wiki-query` is a clean thin-router with a sound index-first → traverse → cite → file-back
loop. Measured against Cole's vision ("skills that take better advantage of Claude Code"
and faithfulness to `AGENTS.md`), the gaps are:

1. **No parallel-agent escalation.** The vault's own `wiki/concepts/extending-the-llm-wiki.md`
   explicitly flags this: big traversals should fan out to `Explore`/parallel agents, but
   "the escalation path [is] not yet built into `wiki-query`." The skill under-uses Claude
   Code's subagents — the single biggest tooling-leverage miss.
2. **No concrete dedup guard.** The file-back step says "apply the new-page test" but,
   unlike `AGENTS.md`, gives no concrete "check for a same-basename page before creating"
   step — the exact collision `AGENTS.md` warns breaks links.
3. **`buckets/index.md` not named as an entry.** Step 2 lists specific bucket files but not
   the bucket index, so a life-area question with an unknown bucket has no first hop.
4. **No cross-link to `vault-improve`.** Now that this sibling exists, the "for X use Y"
   disambiguation footer in the description is one-sided.

## Plan

- [ ] `[local]` Add a **parallel-agent escalation clause** to the Traverse step: when the
      candidate neighborhood is large (say >~8 pages or multiple life-areas), dispatch
      `Explore`/parallel subagents to read in parallel and return excerpts, then synthesize.
      Cross-link `[[parallel-agents]]` / `[[multi-agent-orchestration]]`.
- [ ] `[local]` Add a **dedup guard** to the file-back step: before creating a page, grep
      for a same-basename page across folders (per `AGENTS.md`) and prefer enrichment.
- [ ] `[local]` Add **`buckets/index.md`** as an entry-point option in the index-first step.
- [ ] `[local]` Add `vault-improve` to the description's disambiguation footer.
- [ ] `[human]` **Policy call:** should `wiki-query` auto-parallelize when the neighborhood
      is large, or ask first? (Affects how aggressive the escalation clause is worded.)
- [ ] `[cloud]` *(none this run — no recurring/background work warranted.)*

## Gate

Plan written. **Stopping here.** No edit was made to `.claude/skills/wiki-query/SKILL.md`.
Say go to run the `[local]` steps; the `[human]` policy call is filed for Cole.
