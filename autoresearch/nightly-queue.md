# AutoResearch nightly queue — 2026-10-25 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items (this file is an output, never an input).
Cadence gate: `TZ=America/New_York date +%u` → `7` (Sunday) → full loop runs.

## Phase 0 baseline

- **HEALTH_DEBT = 0** (orphans 0 × 3, missing_from_index 0 × 2, stale_claims 0 × 1).
- Pre-existing objective defect set: **empty**. Soft signals only (dangling wikilinks to
  `@local`/`@human` CRM/concept pages — unscored, not cloud-fixable).

## Phase 1 fast-track heals (→ main, auto-merged)

**None.** HEALTH_DEBT is already 0 on `main`; no structural heal to fast-track tonight.

## Phase 2 build — Selected (@cloud, 2 items)

1. **DSIP + AFWERX FY27 R1 monitoring** (🔁 @cloud, time-sensitive — Oct 27 contact-author
   deadline is tomorrow):
   FY27 R1 pre-released Oct 7, opens **Oct 28**, closes Nov 25, 2026. Previous run (2026-10-11)
   found no 711 HPW / human-performance topics and confirmed SOCOM standing BAA as a new lead.
   Secondary source cited `ARM27BX01-DP001` (Army FY27 topic, Oct 23 deadline) — now past.
   Tonight: web-verify (a) any new DSIP/AFWERX human-performance topics, (b) ARM27BX01-DP001
   status, (c) SOCOM BAA current state. Update `wiki/concepts/atp-federal-funding-landscape.md`
   with verified results + dated monitoring note. **Review lane.**

2. **Improve + general skills → audit `orchestrate-agents` SKILL.md** (@cloud):
   Last progress (2026-10-11): audited `startup-radar`. Still remaining: `orchestrate-agents`,
   `concert-digest`, the 3 prompt skills. Tonight audits `orchestrate-agents` (57 lines, clean
   structure) against all 6 [[skill-authoring-playbook]] sections. Deliverables: safe structural
   fix (§1 description form: imperative → third-person), new
   `wiki/concepts/skill-audit-orchestrate-agents.md` audit record. **Review lane.**

## Phase 4 MODE B (planned)

- One generative enrichment chosen after Phase 2, targeting a genuine gap uncovered tonight.

## Considered but skipped this week (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): interactive Claude platform eval run;
  not fully unattended. Deferred.
- **Prompt max — eval-test the 3 prompt-architect skills** (@cloud): interactive baseline
  measurement needed. Not unattended-doable.
- **Skill max — Skill Creator A/B eval run** (@cloud): same interactive-eval blocker.
- **Build the source-seeking (MODE B) rung** (@cloud): structural change to `program.md`, which
  the human owns. Warrants human sign-off; the design is already proposed.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch frozen `score.py`. HEALTH_DEBT
  = 0 tonight anyway.
- **Try autoresearch loop hands-on** (@cloud): requires external GPU provisioning + spending —
  ineligible for unattended cloud lane.

## Not eligible this week (for reference — @local or @human)

All `@local` and `@human` items — xTech white paper (due Oct 19, now past), SOFWERX/USSOCOM
networking (Nov 5 Tampa), Barbara Knight email, MTEC FY26 (due Oct 30), Fulbright deadlines,
Neuro pipeline, Claude Corps application, CRM enrichment, finance decisions, Uship, password
holder, IG/YouTube exports — are ineligible for the cloud lane (local data, outward actions,
or human decisions).
