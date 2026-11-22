# AutoResearch nightly queue — 2026-11-22 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items (this file is an output, never an input).
Cadence gate: `TZ=America/New_York date +%u` → `7` (Sunday) → full loop runs.

## Phase 0 baseline

- **HEALTH_DEBT = 0** (orphans 0 × 3, missing_from_index 0 × 2, stale_claims 0 × 1).
- Pre-existing objective defect set: **empty**. Soft signals only (dangling wikilinks to
  `@local`/`@human` CRM pages + stub pages — unscored, not cloud-fixable).

## Phase 1 fast-track heals (→ main, auto-merged)

**None.** HEALTH_DEBT is already 0 on `main`; no structural heal to fast-track tonight.

## Phase 2 build — Selected (@cloud, 2 items)

1. **🔁 @cloud DSIP + AFWERX Nov 2026 monitoring check** — URGENT: FY27 R1 closes Nov 25
   (3 days). Last check was Oct 11; a full November scan is overdue. Verify: any 711 HPW /
   human-performance topic added to FY27 R1; AFWERX Nov 4 FOT pre-release results for
   human-performance; SOCOM standing BAA status; xTech|Search 10 outcome (deadline was Oct 19).
   **Deliverable:** append a dated `### 🔁 DSIP + AFWERX monitoring note — 2026-11-22`
   section to `wiki/concepts/atp-federal-funding-landscape.md`. Progress note on task.

2. **@cloud Skill audit — `concert-digest` SKILL.md** (Improve + general skills).
   `concert-digest` is one of the remaining unaudited vault skills (no dedicated audit page
   exists; others unaudited: `token-context-management`, the 3 prompt skills).
   Apply the [[skill-authoring-playbook]] 6-section checklist; apply any structural
   no-behavior-change fixes; create `wiki/concepts/skill-audit-concert-digest.md` audit
   record + update `skill-audits-2026.md` running scoreboard.
   **Deliverable:** dedicated audit wiki page, any safe structural fixes to SKILL.md, indexed,
   reciprocally linked. Progress note on task. Review lane.

## Phase 4 MODE B (planned)

- One generative enrichment proposal: a new concept page filling a genuine gap surfaced by
  tonight's build — candidate: **`wiki/concepts/dod-sbir-human-performance-landscape.md`**
  consolidating DoD SBIR / AFWERX / xTech topology as a reusable reference (distinct from the
  ATP-scoped funding page; passes new-page test).

## Considered but skipped this run (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): interactive eval run needs Cole.
  Not cloud-doable unattended.
- **Prompt max — eval-test 3 prompt-architect skills** (@cloud): interactive baseline
  measurement needed. Not unattended-doable.
- **Skill max — Skill Creator A/B eval run** (@cloud): same interactive-eval blocker.
- **Build the source-seeking (MODE B) rung** (@cloud): design proposed 2026-09-13; wiring
  into `program.md` is Cole's call. No new cloud-doable deliverable tonight.
- **🔁 @cloud Read One NC Matching FY2027 solicitation** (@cloud): releases Dec 14, 2026 —
  not yet available.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch frozen `score.py`. Also
  HEALTH_DEBT = 0 tonight — no urgency.
- **Try autoresearch loop hands-on** (@cloud): requires external GPU + spending. Ineligible.

## Not eligible this run (for reference — @local or @human)

All `@local` and `@human` items (xTech white paper outcome, One NC claim, Fulbright deadlines &
materials, Neuro pipeline & accounts, CRM enrichment, finance decisions, Uship, Claude Corps
application steps, password holder, IG/YouTube exports, Solace/Atlanta Ventures follow-ups,
SOFWERX join, Barbara Knight email, etc.) are ineligible for the cloud lane.
