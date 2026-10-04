# AutoResearch nightly queue — 2026-10-04 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items (this file is an output, never an input).
Baseline this run: `HEALTH_DEBT = 0` (orphans 0, missing_from_index 0, stale_claims 0).

## Phase 0 baseline

- **HEALTH_DEBT = 0** — no pre-existing structural defects.
- Defect list: **empty** — no orphans, no missing_from_index, no stale_claims.
- Fast-track lane (Phase 1): **no-op** — nothing to heal.

## Phase 1 fast-track heals (→ main, auto-merged)

**Skipped** — HEALTH_DEBT already 0; no structural fixes required.

## Phase 2 build — Selected (@cloud, 1 item)

1. **Improve + general skills → audit `wiki-query` SKILL.md against [[skill-authoring-playbook]]**:
   `wiki-query` is the most used vault skill (fires on every query session) and has never been
   formally audited. Deliverable: `wiki/concepts/skill-audit-wiki-query.md` (findings log) +
   any safe structural fixes applied to `.claude/skills/wiki-query/SKILL.md`. Review lane.

## Phase 4 MODE B

- **New entity page: `wiki/entities/dorm-room-fund.md`**:
  Dorm Room Fund (DRF) is referenced in `wiki/concepts/atp-competitive-analysis.md` (the ATP
  competitive analysis Cole built Sept 2026) as the investor backing Athletic Training Portal —
  but no page exists. DRF is a student-VC fund relevant to Cole's JHTV + job-search context
  (student entrepreneurship, VC career track). Web-grounded page. Review lane.

## Considered but skipped this night (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): interactive eval run needs Cole +
  live baseline measurement; not fully unattended.
- **Prompt max — eval-test the 3 prompt-architect skills** (@cloud): same interactive-eval blocker.
- **Skill max — Skill Creator A/B eval run** (@cloud): same interactive-eval blocker; trigger
  tuning pass already complete (2026-08-10).
- **Build the source-seeking (MODE B) rung** (@cloud): structural change to `program.md`;
  warrants human sign-off.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch frozen `score.py` — never
  edited by the loop. HEALTH_DEBT = 0 tonight anyway.
- **Try an autoresearch loop hands-on** (@cloud): requires rented GPU → outward action + spending.
  Ineligible for the cloud lane.

## Not eligible here (for reference — @local or @human)

All `@local` and `@human` items — Fulbright, Neuro pipeline, CRM enrichment, finance decisions,
Uship, Claude Corps application steps, password holder, IG/YouTube exports — are ineligible for
the cloud lane.
