# AutoResearch nightly queue — 2026-10-04 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items (this file is an output, never an input).
Cadence gate: `TZ=America/New_York date +%u` → `7` (Sunday) → full loop runs.

> **Note — two concurrent firings tonight.** Two sessions ran the loop for 2026-10-04 on the same
> `autoresearch/night-2026-10-04` branch. Their work was merged into one morning PR (nothing
> discarded). This queue reflects the **union** of both runs' selections. All three skill audits
> below are under the same "Improve + general skills" @cloud item.

## Phase 0 baseline

- **HEALTH_DEBT = 0** (orphans 0 × 3, missing_from_index 0 × 2, stale_claims 0 × 1).
- Pre-existing objective defect set: **empty**. Soft signals only (dangling wikilinks to
  `@local`/`@human` CRM pages + stub pages — unscored, not cloud-fixable).

## Phase 1 fast-track heals (→ main, auto-merged)

**None.** HEALTH_DEBT is already 0 on `main`; no structural heal to fast-track tonight.

## Phase 2 build — Selected (@cloud, all under "Improve + general skills")

1. **Reconcile the `startup-radar` audit drift.** [[skill-audit-worked-example]] (2026-08-08) §6
   documents a 🔧 *applied* fix — "normalized Step 7 to `python3 startup-tracker/validate.py`" —
   but `git log -S` confirms that relative path **never existed** in
   `.claude/skills/startup-radar/SKILL.md`; the live Step 7 still hardcodes the absolute
   `/Users/colekannam/Desktop/Second Brain/...` path. The documented fix never landed → the audit
   page asserts a change the skill never got. **Deliverable:** actually apply the fix to SKILL.md
   (vault-internal path → relative, matching Steps 4–5; the audit's own "structural, no-behavior
   change" safe category) + update the audit page to record the drift was caught and the fix
   re-applied 2026-10-04. Review lane. *(`.claude/` is unscored → zero HEALTH_DEBT impact.)*

2. **Third worked-example audit: `vault-autoresearch` SKILL.md.** The loop's own driver skill,
   un-audited, 40 lines. **Deliverable:** `wiki/concepts/skill-audit-vault-autoresearch.md` against
   all six [[skill-authoring-playbook]] sections, indexed + reciprocally linked. Clean bill (6/6),
   with the notable finding that it is the *one* vault skill whose §5 "evals first" discipline is
   already satisfied — its eval **is** the frozen `score.py` / HEALTH_DEBT ratchet. Review lane.

3. **Worked-example audit: `wiki-query` SKILL.md** *(concurrent firing).* `wiki-query` is the most
   used vault skill (fires on every query session) and had never been formally audited.
   **Deliverable:** `wiki/concepts/skill-audit-wiki-query.md` (findings log) + any safe structural
   fixes to `.claude/skills/wiki-query/SKILL.md`. Review lane.

## Phase 4 MODE B (two proposals — one per firing)

- **New concept page: `wiki/concepts/skill-evals-playbook.md`** — owns the recurring §5 "write ~3
  evals" gap all three audits log: the query+files+expected_behavior triplet, code- vs model-based
  grader choice, worked triplets for the vault's own skills, and the keep-or-revert run loop.
  Passes the new-page test ([[evals-for-taste]] is only a source summary of the general method).
  Review lane.
- **New entity page: `wiki/entities/dorm-room-fund.md`** *(concurrent firing)* — Dorm Room Fund
  (DRF) is referenced in [[atp-competitive-analysis]] as an investor backing Athletic Training
  Portal, but had no page. A student-run VC relevant to Cole's JHTV + job-search context.
  Web-grounded. Review lane.

## Considered but skipped this night (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): remaining work is an *interactive* eval
  run (needs Cole + live baseline measurement). Not fully unattended.
- **Prompt max — eval-test the 3 prompt-architect skills** (@cloud): same interactive-eval blocker.
- **Skill max — Skill Creator A/B eval run** (@cloud): same interactive-eval blocker; the
  trigger-tuning pass it needed is already complete (progress 2026-08-10).
- **Build the source-seeking (MODE B) rung** (@cloud): a structural change to `program.md`, which
  the human owns. Warrants human sign-off; too large for one unattended night.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch the frozen `score.py` — never
  edited by the loop. HEALTH_DEBT = 0 tonight anyway.
- **Try an autoresearch loop hands-on** (@cloud): requires provisioning an external/rented GPU →
  outward action + spending. Ineligible for the cloud lane.

## Not eligible here (for reference — @local or @human)

All `@local` and `@human` items — Fulbright deadlines/materials, Neuro pipeline, CRM enrichment,
finance decisions, Uship, Claude Corps application steps, password holder, IG/YouTube exports,
reply-rate scoreboard, Spotify/concert alerts — are ineligible for the cloud lane (local data,
outward/irreversible actions, or human decisions).
