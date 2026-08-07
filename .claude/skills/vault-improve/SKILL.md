---
name: vault-improve
description: >
  Use when Cole wants to improve, strengthen, enhance, update, refine, fix, or polish
  something in this Second Brain vault — a skill (SKILL.md), the ingest workflow (AGENTS.md),
  a project (grant finder, JHTV second brain), a life-area bucket, a wiki page, a task item,
  or bare "improve the vault". Trigger on: "improve X", "make X better", "strengthen X",
  "refine X", "update X", "polish X", "fix the X skill/page/workflow". Diagnoses the gap to
  Cole's vision and writes a venue-tagged plan (local/cloud/human), then waits for approval
  before executing local steps only. For the autonomous metric-driven heal loop use
  vault-autoresearch; for answering questions from the vault use wiki-query.
---

# Vault Improve

## Overview

Point `improve` at anything in the vault and this skill diagnoses the gap between where
that target *is* and Cole's vision, then writes a **venue-tagged plan** that always stops
for approval before executing. It figures out *how* to improve the target on its own,
grounded in what it can already know.

`AGENTS.md` (vault root) is the **single source of truth** for how the vault works and
**wins on any conflict** — this skill only routes to it and states the trigger, procedure,
and invariants. **Do not restate `AGENTS.md`'s rules here; read it if unsure.**

This is the human-directed complement to `vault-autoresearch`: autoresearch is the
autonomous, metric-driven heal loop (the HEALTH_DEBT ratchet); `improve` is judgment-driven
improvement of a *named* target toward Cole's vision.

## Invariants (do not violate)

- **Improvement = a denser, more current, better-connected graph** — not page count, not
  net-new invented content. **Links > pages. Enrich before you create. Never invent facts.**
- **`AGENTS.md` wins on any conflict**; this skill is a thin router, not a second schema.
- **Separate from autoresearch.** You *may read* `python3 autoresearch/score.py` as one
  signal when a target is metric-shaped, but you are **never bound by the ratchet**, you
  **never edit `score.py`**, and you **never edit anything under `raw/`**. If a target is
  purely metric-shaped, point Cole at `vault-autoresearch` instead.
- **Every plan step carries exactly one venue tag:** `[local]`, `[cloud]`, or `[human]`.
- **The approval gate is sacred.** After writing the plan you STOP. Only `[local]` steps run
  after Cole says go. `[cloud]` and `[human]` steps never auto-run and are never auto-merged.

## Procedure

### 1. Resolve the target
Parse what `improve` points at. Target types, primary first:
- **Skill / workflow / schema** *(primary)* — a `SKILL.md`, `AGENTS.md`, the autoresearch
  loop, the ingest process. Ask: does this make better use of Claude Code's capabilities,
  and is it faithful to `AGENTS.md`?
- **Project / bucket / life-area** *(primary)* — e.g. the grant finder, the JHTV second
  brain, or any of Duke / Uship / Job Search / Personal / Claude Mastery. Target = the MOC
  and its linked neighborhood.
- **Wiki page / facet** *(secondary)* — a concept, entity, source, or `wiki/overview.md`.
- **Task item** *(secondary)* — an entry in `tasks/index.md`; improve = figure out how to
  advance it.
- **Nothing named** → **whole-vault** *(secondary)* — find the highest-leverage improvement
  (read `index.md`, scan orphans/staleness, glance at `score.py`).

If the target itself is ambiguous, ask one sharp question before going further.

### 2. Diagnose against the vision
Measure the target against four grounding sources:
1. **`AGENTS.md`** — the vault's rules/principles = the standard.
2. **Cole's profile + memory + relevant `buckets/` and `journal/`** — what he actually
   cares about; his life-areas and stated goals.
3. **The target's own graph** — inbound/outbound links, neighbors, source freshness,
   orphan / contradiction / dangling-stub state.
4. **`score.py`** — optional signal, only when the target is metric-shaped.

Output a **short diagnosis**: the concrete gap between where the target *is* and Cole's
vision, in LLM-Wiki terms — missing links, thin/orphan pages, stale or uncited claims,
dangling wikilinks, absent sources, weak MOC coverage, a skill that under-uses the tooling.

If the *vision* is genuinely ambiguous (not just the target), ask **one** sharp question
rather than guessing.

### 3. Write the plan
Write an ordered plan where **every step carries one venue tag**:
- `[local]` — Claude Code does it now, this session.
- `[cloud]` — a scheduled/background agent does it (hand to `/schedule`, or the
  `autoresearch/pending` review branch for generative work).
- `[human]` — only Cole: a decision, a source to provide, an offline action.

**Show the plan in chat AND persist it** to `tasks/improvements/YYYY-MM-DD-<target>.md`
so it survives the session.

### 4. Approval gate (hard stop)
After writing the plan, **STOP**. Execute `[local]` steps only after Cole says go.
`[cloud]` and `[human]` items never auto-run:
- File each as a checkbox in `tasks/index.md` per `AGENTS.md`'s Action Items rules so it
  doesn't vanish.
- Offer to `/schedule` the `[cloud]` ones.
- Never auto-merge generative/cloud work.

### 5. Execute + report
After Cole says go, do the `[local]` steps following `AGENTS.md` exactly — enrich before
create, make links reciprocal, update `index.md`, add the relevant `buckets/` link, append
`log.md`. Then report what changed and what remains for cloud/human.

## Guardrails

- `AGENTS.md` wins on any conflict; don't restate its rules here.
- Never invent facts; snapshots age — reconcile freshness and mark superseded claims.
- Never edit `autoresearch/score.py` or anything under `raw/`.
- Never auto-merge generative/cloud work; the plan-first approval gate is sacred.
- Don't duplicate the autoresearch ratchet — `improve` is directed, not metric-bound.
- Links > pages; enrichment before creation; apply `AGENTS.md`'s new-page test before
  creating anything.
