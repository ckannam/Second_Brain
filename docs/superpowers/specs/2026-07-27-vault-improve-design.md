# vault-improve — Design

**Date:** 2026-07-27
**Status:** Approved (brainstorm), pending implementation plan

## Purpose

A skill that lets Cole say **`improve [target]`** (or just `improve`) and get a
diagnosis of the gap between that target and his vision, followed by a **venue-tagged
plan** that always stops for approval before any execution. The skill figures out
*how* to improve the target autonomously, grounded in what it can already know.

**Primary targets in practice (weight the design here):**
1. **Skills / vault machinery** — the skills we've built to exploit Claude Code
   (`.claude/skills/*`, `AGENTS.md`, the autoresearch loop). "improve this skill" =
   make our tooling take better advantage of the tool.
2. **Projects we're building** — e.g. the **grant finder** and the **JHTV second
   brain**. These are bucket/life-area-shaped efforts; "improve the JHTV second brain"
   = strengthen that whole Map-of-Content neighborhood.

Other target types (arbitrary wiki page, task item, whole-vault) are supported but
secondary — the two above are where `improve` earns its keep.

## Framework alignment (non-negotiable)

The vault is an **LLM Wiki** in Karpathy's sense (see `AGENTS.md`). `improve` operates
entirely inside that idiom:

- **Improvement = a denser, more current, better-connected graph** — not page count,
  not net-new invented content. **Links > pages.**
- **Enrichment before creation.** First move is always to strengthen and reconnect what
  exists; a new page is the second move, gated by `AGENTS.md`'s new-page test.
- **Never invent facts.** Everything traces to a raw source or is clearly marked as
  synthesis/inference. Sources are point-in-time snapshots; reconcile freshness and mark
  superseded claims.
- **`AGENTS.md` is the single source of truth and wins on any conflict.** This skill is a
  thin router to it — it does not restate the schema.

## Shape

A single `SKILL.md` at `.claude/skills/vault-improve/`, matching the thin-router pattern
of `wiki-query` and `vault-autoresearch`. No `program.md` — "improve toward my vision" is
judgment-driven, not a mechanical metric loop.

**Relationship to `vault-autoresearch`:** separate and complementary.
- `vault-autoresearch` = autonomous, metric-driven self-healing (the HEALTH_DEBT ratchet,
  git as the keep/revert gate). Runs the overnight loop.
- `vault-improve` = human-directed, vision-driven improvement of a named target.
- `improve` **may read** `python3 autoresearch/score.py` as *one input signal* when a
  target is metric-shaped, but is **never bound by the ratchet** and never edits the
  scorer. If a target is purely metric-shaped, `improve` may point Cole at
  `vault-autoresearch` instead.

## Invocation

- Command: `/vault-improve`
- Natural language: "improve JHTV", "improve the model-speciation page", "improve the
  ingest workflow", or bare "improve" (→ whole-vault diagnosis).
- Description-driven triggering so a bare "improve X" against the vault routes here.

## Procedure

### 1. Resolve the target
Parse what `improve` points at. Supported target types, primary first:
- **Skill / workflow / schema** *(primary)* — a `SKILL.md`, `AGENTS.md`, the autoresearch
  loop, the ingest process. Diagnosis asks: does this make better use of Claude Code's
  capabilities, and is it faithful to `AGENTS.md`?
- **Project / bucket / life-area** *(primary)* — e.g. grant finder, JHTV second brain, or
  any of Duke / Uship / Job Search / Personal / Claude Mastery. Target = the MOC and its
  linked neighborhood.
- **Wiki page/facet** *(secondary)* — a concept, entity, source, or `overview.md`.
- **Task item** *(secondary)* — an entry in `tasks/index.md`; improve = figure out how to
  advance it.
- **Nothing named** → **whole-vault** *(secondary)*: find the highest-leverage improvement
  (read `index.md`, scan orphans/staleness, glance at `score.py`).

If the target is ambiguous, ask one sharp clarifying question before proceeding.

### 2. Diagnose against the vision
Measure the target against four grounding sources:
1. **`AGENTS.md`** — the vault's rules/principles = the standard.
2. **Cole's profile + memory + relevant `buckets/` and `journal/`** — what he actually
   cares about; his life-areas and stated goals.
3. **The target's own graph** — inbound/outbound links, neighbors, source freshness,
   orphan / contradiction / dangling-stub state.
4. **`score.py`** — optional signal when the target is metric-shaped.

Output a **short diagnosis**: the concrete gap between where the target *is* and Cole's
vision, expressed in LLM-Wiki terms (missing links, thin/orphan pages, stale claims,
uncited assertions, dangling wikilinks, absent sources, weak MOC coverage).

If the vision is genuinely ambiguous, ask **one** sharp question (AskUserQuestion) rather
than guessing.

### 3. Write the plan
An ordered plan where **every step carries a venue tag**:
- `[local]` — Claude Code does it now, this session.
- `[cloud]` — a scheduled/background agent does it (hand to `/schedule`, or the
  `autoresearch/pending` review branch for generative work).
- `[human]` — only Cole: a decision, a source to provide, an offline action.

The plan is **shown in chat** and **persisted** to
`tasks/improvements/YYYY-MM-DD-<target>.md` so it survives the session (this folder is
new; `tasks/` is the vault's cross-session action memory, and human/cloud items *are*
future actions).

### 4. Approval gate (hard stop)
After writing the plan, **stop**. Execute `[local]` steps only after Cole says go.
`[cloud]` and `[human]` items never auto-run:
- File each as a checkbox in `tasks/index.md` (per `AGENTS.md`'s Action Items rules) so
  it doesn't vanish.
- Offer to `/schedule` the `[cloud]` ones.
- Never auto-merge generative/cloud work.

### 5. Execute + report
Local work follows `AGENTS.md` exactly: enrich-before-create, reciprocal links, update
`index.md`, add bucket links, append `log.md`. Then report what changed and what remains
for cloud/human.

## Guardrails

- `AGENTS.md` wins on any conflict; do not restate its rules in the skill.
- Never invent facts; snapshots age — reconcile and mark superseded claims.
- Never edit `autoresearch/score.py` or anything under `raw/`.
- Never auto-merge generative/cloud work; the plan-first approval gate is sacred.
- Don't duplicate the autoresearch ratchet — `improve` is directed, not metric-bound.
- Links > pages; enrichment before creation; apply the new-page test before creating.

## Open items resolved

- **Skill name:** `vault-improve` (invoked `/vault-improve`, triggers on "improve X").
- **Plan location:** `tasks/improvements/YYYY-MM-DD-<target>.md`.

## Out of scope

- No new metric or scorer (that's autoresearch's domain).
- No automatic execution of cloud/human work.
- No changes to `AGENTS.md` unless a specific `improve` run targets the schema and Cole
  approves that plan.
