---
type: concept
created: 2026-07-24
---

# Vault AutoResearch

This vault's instantiation of [[andrej-karpathy]]'s [[autoresearch]] loop, applied to
knowledge upkeep instead of ML training. Built 2026-07-24 as the concrete next rungs of
[[extending-the-llm-wiki]]. It unifies **[[self-healing-workflows|self-healing]]** (keep the
wiki *working*) and **AutoResearch** (make it *better*) under one machinery.

## The Karpathy mapping

| AutoResearch primitive | Here |
|---|---|
| `prepare.py` (frozen evaluator) | `autoresearch/score.py` — emits **HEALTH_DEBT**, one scalar, lower is better. The loop may never edit it (anti-cheating). |
| `train.py` (the one editable surface) | the wiki pages themselves |
| `val_bpb` (the metric) | **HEALTH_DEBT** = 3·orphans + 2·missing-from-index + 1·stale-claims |
| `program.md` (loop brain) | `autoresearch/program.md` + the `vault-autoresearch` skill |
| git reset (the ratchet) | this vault is now a git repo; keep on improvement, revert otherwise. Note the contrast with Karpathy's [[agent-hub]], which *drops* main/merge for a branch-less DAG — this loop instead depends on a linear `main` + a metric-gated collapse as its ratchet |
| overnight cron | [[claude-code-scheduled-tasks]] or GitHub Actions |

## Why the metric is deliberately narrow

Karpathy's failure mode is that **a bad metric gets confidently optimized in the wrong
direction**, and wiki quality is partly subjective. So HEALTH_DEBT scores only *unambiguous*
defects (a file nothing links to; a page missing from its catalog; a superseded claim shown
as current). Judgment-heavy signals (stub debt, reciprocal-link gaps) are *reported but not
scored*, and all net-new knowledge (MODE B) is routed to a human review branch rather than
committed autonomously.

## The two-lane model (how the nightly run splits work)

Split by whether `score.py` can objectively verify the output:

| Lane | What | Where it lands |
|---|---|---|
| **Fast-track** | Score-verified *structural* self-heal (Phase 1 MODE A) | Directly on `main` — no PR |
| **Review** | New content (Phase 2 build + Phase 3 build-heal + Phase 4 generative) | Night branch → morning PR |

The boundary is strict: if a fix is purely structural (editing `[[links]]`, `index.md` entries, stale-claim markers) AND strictly lowers HEALTH_DEBT AND applies as a clean fast-forward to `main` AND repairs pre-existing debt → it auto-merges. Anything not meeting all four guards rides the PR.

## Phase order (nightly)

0. **Select & baseline** — read `tasks/index.md`, pick `@cloud` items, regenerate `autoresearch/nightly-queue.md`, run `score.py --json` to record baseline HEALTH_DEBT + the pre-existing defect set.
1. **Heal on `main` (fast-track)** — MODE A against `main` for the Phase-0 defect set; each fix that passes the auto-merge guards commits + pushes directly to `main`.
2. **Build (branch)** — fork `autoresearch/night-YYYY-MM-DD` from healed `main`; work ≤2–3 selected items per `AGENTS.md`. Web tools allowed.
3. **Write-back + build-heal (branch)** — update `tasks/index.md`; MODE A again for build-introduced debt; those fixes commit to the branch.
4. **AutoResearch (MODE B, branch)** — one generative enrichment proposal.
5. **PR** — open one morning PR (night branch → `main`) for review-lane work; stop.

## Two modes (detail)

- **MODE A — self-healing**: drive HEALTH_DEBT to 0 by fixing objective defects, one change per iteration, keep-or-`git reset` on the metric. Runs twice per night: Phase 1 (auto-merge, pre-existing debt) and Phase 3 (branch, build-introduced debt).
- **MODE B — generative**: propose ONE enrichment — a new page a source warrants, a stub worth filling, or a source to ingest — guarded by `AGENTS.md`'s new-page test + simplicity criterion. Always the review lane; never auto-merges.

## First run

Baseline HEALTH_DEBT was **2** ([[agentic-note-taking]] existed but was absent from
[[index|the index]]); one MODE A iteration fixed it → **0**, kept. Logged in
`autoresearch/results.tsv` (the cross-run memory).

## Relationship to the rest of the vault

Complements [[wiki-query]] (which files *answers* back) by continuously improving the graph
those answers draw from. The furthest rung — a scheduled [[proactive-agents|proactive]] run
that also *seeks new sources* — remains open (see [[tasks/index]]). Related: [[ingest-query-lint]]
(the manual Lint this automates), [[ai-second-brain-levels]], [[agentic-workflows]],
[[vault-autoresearch|the skill]] (the router and invariants), [[claude-code-scheduled-tasks]].
