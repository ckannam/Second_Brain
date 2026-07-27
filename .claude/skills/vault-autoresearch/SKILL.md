---
name: vault-autoresearch
description: Use when asked to run the vault's self-healing or AutoResearch loop — "heal the wiki", "run autoresearch", "improve the vault", "lower the health debt", the overnight/scheduled vault-maintenance run, or the /vault-autoresearch command. For answering a question from the wiki use wiki-query instead; for writing wiki content follow AGENTS.md.
---

# Vault AutoResearch

Runs Karpathy's AutoResearch loop against this vault: measure **HEALTH_DEBT**, make
one improvement, keep it only if the number drops (git as the ratchet), log it,
repeat. Self-healing keeps the wiki *working*; AutoResearch makes it *better*.

**The loop instructions live in `autoresearch/program.md` — read it and follow it
exactly.** This skill only routes you there and states the invariants. `program.md`
is the source of truth for the loop; `AGENTS.md` is the source of truth for how to
write the wiki. Do not restate either here.

## Invariants (do not violate)

- The metric is `python3 autoresearch/score.py` (`--json` to drive the loop).
  **Lower HEALTH_DEBT is better.**
- **Never edit `autoresearch/score.py`** (the frozen evaluator) or anything under
  `raw/`. Lowering the number by changing the scorer is cheating, not healing.
- **Keep or revert on the metric:** improved → `git commit`; equal/worse →
  `git checkout -- .`. Never keep a non-improving change.
- **Build first, heal second.** Action-item build work (Phases 0–2) runs before self-heal
  (Phase 3) and generative work (Phase 4). On a build night, the entire run lives on the
  night branch → one PR; nothing reaches `main` unreviewed. Pure-maintenance nights may
  still commit objective self-heal fixes to `main`.
- Log every iteration to `autoresearch/results.tsv`.

## Quick start

1. `python3 autoresearch/score.py` — see current debt + the defect list.
2. Follow `autoresearch/program.md`'s six phases in order: **Select → Build →
   Write-back → Self-heal → AutoResearch → PR**.
3. On a build night the whole run stays on the night branch → one morning PR. Stop after
   the PR is opened.
