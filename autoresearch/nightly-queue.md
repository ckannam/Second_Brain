# AutoResearch nightly queue — 2026-10-04 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items (this file is an output, never an input).
Cadence gate: `TZ=America/New_York date +%u` → `7` (Sunday) → full loop runs.

## Phase 0 baseline

- **HEALTH_DEBT = 0** (orphans 0 × 3, missing_from_index 0 × 2, stale_claims 0 × 1).
- Pre-existing objective defect set: **empty**. Soft signals only (dangling wikilinks to
  `@local`/`@human` CRM pages + stub pages — unscored, not cloud-fixable).

## Phase 1 fast-track heals (→ main, auto-merged)

**None.** HEALTH_DEBT is already 0 on `main`; no structural heal to fast-track tonight.

## Phase 2 build — Selected (@cloud, 2 items — both under "Improve + general skills")

1. **Reconcile the `startup-radar` audit drift.** [[skill-audit-worked-example]] (2026-08-08) §6
   documents a 🔧 *applied* fix — "normalized Step 7 to `python3 startup-tracker/validate.py`" —
   but `git log -S` confirms that relative path **never existed** in
   `.claude/skills/startup-radar/SKILL.md`; the live Step 7 still hardcodes the absolute
   `/Users/colekannam/Desktop/Second Brain/...` path. The documented fix never landed → the audit
   page asserts a change the skill never got. **Deliverable:** actually apply the fix to SKILL.md
   (vault-internal path → relative, matching Steps 4–5; the audit's own "structural, no-behavior
   change" safe category) + update the audit page to record the drift was caught and the fix
   re-applied 2026-10-04. Review lane. *(`.claude/` is unscored → zero HEALTH_DEBT impact; this is
   a correctness fix, not a heal.)*

2. **Third worked-example audit: `vault-autoresearch` SKILL.md.** The loop's own driver skill,
   un-audited, 40 lines. Advances the tracked "more skill iterations" remaining-work note.
   **Deliverable:** `wiki/concepts/skill-audit-vault-autoresearch.md` against all six
   [[skill-authoring-playbook]] sections, indexed + reciprocally linked. Expect a clean bill (the
   honest result for a mature skill) with one genuinely notable finding — it is the *one* vault
   skill whose §5 "evals first" discipline is already satisfied, because its eval **is** the frozen
   `score.py` / HEALTH_DEBT ratchet. Review lane.

## Phase 4 MODE B

- One generative enrichment proposal (see the morning PR body). Review lane — never auto-merges.

## Considered but skipped this night (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): remaining work is an *interactive* eval
  run (needs Cole + live baseline measurement). Not fully unattended.
- **Prompt max — eval-test the 3 prompt-architect skills** (@cloud): evals need interactive
  baseline measurement against real tasks. No bounded unattended deliverable.
- **Skill max — Skill Creator A/B eval run** (@cloud): same interactive-eval blocker; the
  trigger-tuning pass it needed is already complete (progress 2026-08-10).
- **Build the source-seeking (MODE B) rung** (@cloud): a structural change to `program.md`, which
  the human owns ("the human edits it; the loop follows it"). Warrants human sign-off; too large
  for one unattended night's build.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch the frozen `score.py` — never
  edited by the loop. HEALTH_DEBT = 0 tonight anyway.
- **Try an autoresearch loop hands-on** (@cloud): requires provisioning an external/rented GPU →
  outward action + spending. Ineligible for the cloud lane.

## Not eligible here (for reference — @local or @human)

All `@local` and `@human` items — Fulbright deadlines/materials, Neuro pipeline, CRM enrichment,
finance decisions, Uship, Claude Corps application steps, password holder, IG/YouTube exports,
reply-rate scoreboard, Spotify/concert alerts — are ineligible for the cloud lane (local data,
outward/irreversible actions, or human decisions).
