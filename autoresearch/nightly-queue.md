# AutoResearch nightly queue — 2026-09-27 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items (this file is an output, never an input).
Baseline this run: `HEALTH_DEBT = 0` (orphans 0, missing_from_index 0, stale_claims 0).

## Phase 0 baseline

- **HEALTH_DEBT = 0** — no structural defects in the pre-existing set.
- Phase 1 (fast-track heal on `main`): **no-op** — nothing to heal.

## Phase 1 fast-track heals (→ main, auto-merged)

None. HEALTH_DEBT = 0 at baseline; no eligible fast-track work.

## Phase 2 build — Selected (@cloud, 2 items)

1. **Improve + general skills → audit `startup-radar` SKILL.md against [[skill-authoring-playbook]]**:
   Previous audits covered `vault-improve` (2026-08-10) and `networking-prep` (2026-08-30).
   `startup-radar` is the next-highest-leverage unaudited skill: 199 lines, complex multi-step
   procedure, and the prior audit noted it had no evals (§5 gap). The key findings to investigate:
   hardcoded absolute Mac paths, an interactive "ask Cole" step that breaks unattended runs,
   and no evals.
   Deliverable: `wiki/concepts/skill-audit-startup-radar.md` + any safe structural fixes to
   the skill file. Review lane.

2. **Build source-seeking MODE B rung (cloud-safe part) — design page**:
   Previous nights skipped this as "too large for one night." Tonight's cloud-safe deliverable:
   research what systematic source-seeking would look like and update [[extending-the-llm-wiki]]
   with a concrete design for a MODE C rung. The human-reviewed PR is the sign-off; implementation
   in `program.md` is deferred to Cole. Advances the item meaningfully without unreviewed
   changes to the loop's control file.
   Deliverable: update to `wiki/concepts/extending-the-llm-wiki.md` + progress note on task.
   Review lane.

## Phase 4 MODE B

- **Enrich `wiki/concepts/proactive-agents.md`**: The page is a 9-line stub that references four
  pages without developing the concept. Filling it from already-ingested vault sources is a
  bounded, factual enrichment with no net-new web-search claims.

## Considered but skipped this night (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): remaining work is an interactive eval
  run (needs Cole + live baseline); no bounded unattended deliverable.
- **Prompt max — eval-test the 3 prompt-architect skills** (@cloud): evals need interactive
  baseline measurement. Not unattended-doable.
- **Skill max — Skill Creator A/B eval run** (@cloud): trigger-tuning pass complete (2026-08-10);
  remaining eval run needs Cole.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch the frozen `score.py`. Also
  HEALTH_DEBT = 0 tonight.
- **Try an autoresearch loop hands-on** (@cloud): requires provisioning a rented GPU →
  outward action + spending. Ineligible for unattended cloud lane.

## Not eligible here (for reference — @local or @human)

All `@local` and `@human` items — Fulbright steps, Neuro pipeline, CRM enrichment, finance
decisions, Uship, Claude Corps application, password holder, IG/YouTube exports,
concert alerts — are ineligible (local data, outward actions, or human decisions).
