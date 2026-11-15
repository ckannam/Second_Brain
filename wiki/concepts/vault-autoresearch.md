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

## The two-lane model

The loop runs two lanes on each nightly firing, each with a different merge policy:

| Lane | Work | Branch | Merge |
|---|---|---|---|
| **Fast-track** | Phase 1 score-verified structural heals (orphan fixes, index gaps) | `main` directly | Auto, only after HEALTH_DEBT strictly decreases |
| **Review** | Phases 2–4: build items, write-back, one MODE B page | `autoresearch/night-YYYY-MM-DD` | Morning PR → Cole approves |

The fast-track / review split is the vault's key safety property: *nothing that changes facts or
adds knowledge* lands on `main` without human review. Only objective-metric improvements
(HEALTH_DEBT lower after the change, same as Karpathy's `val_bpb` gate) get the express lane.

## Six-phase run structure

Each nightly or weekly run (`autoresearch/program.md` is the authority):

1. **Phase 0** — regenerate `autoresearch/nightly-queue.md`; run scorer for baseline HEALTH_DEBT.
2. **Phase 1** — MODE A fast-track heals on `main` (keep-or-revert ratchet).
3. **Phase 2** — build: fork branch, work selected `@cloud` task items (≤2–3/night).
4. **Phase 3** — write-back + build-heal: update `tasks/index.md` progress notes; re-run MODE A for any build-introduced debt.
5. **Phase 4** — one MODE B generative page or enrichment proposal.
6. **Phase 5** — open morning PR (branch → main); stop.

## Two work modes

- **MODE A — self-healing** (autonomous, fast-track lane): drive HEALTH_DEBT to 0 one defect at a
  time; keep-or-`git checkout --` ratchet on every iteration.
- **MODE B — generative** (review lane only, never auto-merges): grow coverage and connectivity;
  Cole approves each morning. Guarded by `AGENTS.md`'s new-page test + the two-lane boundary.

## First run

Baseline HEALTH_DEBT was **2** ([[agentic-note-taking]] existed but was absent from
[[index|the index]]); one MODE A iteration fixed it → **0**, kept. Logged in
`autoresearch/results.tsv` (the cross-run memory).

## Relationship to the rest of the vault

Complements [[wiki-query]] (which files *answers* back) by continuously improving the graph
those answers draw from. The furthest rung — a scheduled [[proactive-agents|proactive]] run
that also *seeks new sources* — remains open (see [[tasks/index]]). Related: [[ingest-query-lint]]
(the manual Lint this automates), [[ai-second-brain-levels]], [[agentic-workflows]].
