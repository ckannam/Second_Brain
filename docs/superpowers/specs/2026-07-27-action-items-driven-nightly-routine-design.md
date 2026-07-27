# Action-Items-Driven Nightly Routine — Design

**Date:** 2026-07-27
**Status:** Approved, pre-implementation
**Owner:** Cole (human owns direction; agent owns bookkeeping)

## Problem

Today the overnight cloud routine works `autoresearch/nightly-queue.md` — a **hand-curated**
extract of cloud-safe tasks. Two gaps:

1. **Manual curation.** Cole must lift action items from `tasks/index.md` into the queue by hand.
2. **One-way, no write-back.** When the routine finishes a queue item it does *not* update the
   matching action item in `tasks/index.md`. The board drifts (observed 2026-07-27: two
   "Sourcing & verification" items completed by the run but still shown open).

Desired workflow: **daytime = brainstorm + capture (with lane decided in the moment); nighttime =
the routine reads the board, builds everything it can do unattended, and writes progress back** —
so Cole wakes up to completed work and an updated board.

## Goals

- Routine reads `tasks/index.md` (the Action Items board) as its source of work.
- Routine self-selects the items doable **without Cole**, builds them overnight, and reflects the
  outcome back into the board.
- Build work runs **first**; self-heal and autoresearch run **after** (so self-heal cleans up any
  structural debt the build introduced).
- Nothing outward/irreversible; everything reviewable in one morning PR before it touches `main`.

## Non-goals

- No change to the `score.py` metric or the frozen boundaries (`raw/`, `score.py` stay untouched).
- No automated sync to `main` — the human still merges the morning PR.
- No new task-tracking system; `tasks/index.md` stays the single board per `AGENTS.md`.
- Not solving `@local`-lane (Mac-dependent) work — that remains the separate local ingest lane.

## Design

### 1. Capture-time lane tagging (workflow + `AGENTS.md` change)

Every action item carries a lane tag, **decided when the item is created**:

- `@cloud` — the routine can do this **fully** unattended.
- `@local` — needs Cole's Mac (local data / connectors not in the cloud).
- `@human` — needs a Cole decision or outward/irreversible action.

When it is ambiguous whether an item is fully cloud-doable, resolve it **at capture** (during the
daytime brainstorm), not at 2am. If a large item is partly cloud-doable, split it: tag the
cloud-doable sub-part `@cloud` and the rest `@human`/`@local`.

**`AGENTS.md` change** — the Action Items → **Capture** step (currently step 1) gains a required
lane tag in the line format:

```
- [ ] @cloud <action> — <one-line context> [[related-page]] (added YYYY-MM-DD)
```

### 2. The doability rubric (frozen text in `program.md`)

An item is **cloud-doable** only if **all** hold:

- touches only the **synced vault + web/connectors**;
- needs **no local data** (`crm/`, `profile/`, `finance/`, iMessage, Contacts — invisible to the cloud);
- takes **no outward/irreversible action** (no email/messages, no spending, no merges to `main`);
- needs **no human decision**.

Selection precedence: **explicit tag wins**; if an item is **untagged**, the routine **infers**
against this rubric; **when unsure → skip and flag** (note why in the PR). Conservative by default.

### 3. New nightly order (rewrite of `program.md`)

The whole run works on the night branch `autoresearch/night-YYYY-MM-DD`.

| Phase | Action | Writes to |
|-------|--------|-----------|
| **0 · Select** | Read `tasks/index.md` Open items. Select cloud-doable ones (tag-wins → infer → skip-if-unsure). **Regenerate `nightly-queue.md`** as the auto-selected worklist for the night — a transparency artifact listing what was picked and why the rest were skipped. Cole stops hand-curating it. | `nightly-queue.md` |
| **1 · Build** | Work selected items **top-down, bounded** (cap ≈2–3 items/night to avoid a runaway), building per `AGENTS.md`. | night branch |
| **2 · Write-back** | **Done** → flip `[ ]`→`[x]`, append `(done YYYY-MM-DD)`, move to **Done** (per `AGENTS.md`). **Partial** → leave `[ ]` open, append an indented `⏳ progress YYYY-MM-DD: did X; remaining Y`. **Never** mark done what was not finished. | `tasks/index.md` |
| **3 · Self-heal (MODE A)** | Run `score.py`; fix the highest-weight objective defects **including any the build introduced**; keep-or-revert on the metric; log to `results.tsv`. | night branch |
| **4 · AutoResearch (MODE B)** | One generative enrichment proposal per `AGENTS.md`'s new-page test + simplicity criterion. | night branch |
| **5 · PR** | Open one morning PR (night branch → `main`) and stop. Arm the hourly check-in follow-up. | GitHub |

### 4. Branch model

**On nights that did build work, the entire run lives on the night branch → one morning PR.** The
build and the self-heal that cleans up after it are entangled, so they are reviewed together and
nothing hits `main` unreviewed. Consequence: **the Action Items board only updates when Cole merges
the PR** — merging is what advances `main`.

On a **pure-maintenance night** (no cloud-doable tasks selected), MODE A self-heal may commit
objective fixes straight to `main` as it does today (nothing to review), then still make one MODE B
proposal on the branch.

### 5. Role of `nightly-queue.md`

Changes from **hand-curated input** to **auto-generated staging artifact**, regenerated every night
in Phase 0. It records the night's selection + skip reasons for transparency. Cole no longer edits it.

## Where the morning PR lives

GitHub: `https://github.com/ckannam/Second_Brain/pulls`. The cloud routine (which has GitHub access)
opens it; the hourly check-in routines babysit it until merged. Cole reviews in the GitHub web UI or
through the assistant (fetch branch → show diff → merge on say-so). `gh` is **not** installed locally,
so terminal PR ops aren't available unless installed later (optional, out of scope).

## Safety (unchanged frozen boundaries + new guardrails)

- **NEVER** edit `autoresearch/score.py` or modify anything under `raw/`.
- **NEVER** take outward/irreversible actions (email, messages, spending, merges to `main`).
- Honor `@human` / `@local` lanes strictly; never attempt them in the cloud.
- **Never fabricate completion.** If an item can't be verified done, it isn't marked done.
- Everything is reviewable in the morning PR before it reaches `main`.

## Files changed at implementation

1. `autoresearch/program.md` — rewrite loop to the 6-phase order; add the doability rubric; add
   the write-back rules; state the branch model.
2. `autoresearch/nightly-queue.md` — repurpose header to "auto-generated nightly selection"; remove
   the hand-curation instruction.
3. `AGENTS.md` — Action Items → Capture: require a lane tag; document the three lanes and the
   capture-time resolution rule.
4. Cloud routine prompt (via the `schedule`/RemoteTrigger routine) — update the nightly agent's
   instruction to point at the new `program.md` order (read board → build → write-back → heal →
   research → PR).
5. `.claude/skills/vault-autoresearch/SKILL.md` — reflect the new order/invariants if it restates any.

## Success criteria

- Adding an item to `tasks/index.md` with `@cloud` (or a clearly cloud-doable untagged item) causes
  the next night's routine to attempt it without further curation.
- After a run, completed items appear `[x]` in **Done** and partially-advanced items carry an
  `⏳ progress` note — visible once the PR is merged.
- Self-heal and autoresearch run **after** build work; `score.py` still reports the vault's debt and
  the loop still keeps-or-reverts on the metric.
- No outward/irreversible action ever taken; `raw/` and `score.py` never modified.
