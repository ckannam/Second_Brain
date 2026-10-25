# AutoResearch nightly queue — 2026-10-25 (Sunday weekly run)

> **Note — two concurrent firings tonight.** Two sessions ran the loop for 2026-10-25 and were
> merged into one morning PR (nothing discarded; union merge). The sections below are the
> **union** of both firings' selections. Combined Phase-2 build = **3 audits** (`concert-digest`
> + the 3 prompt-architect skills from firing A; `orchestrate-agents` re-audit from firing B)
> **+ DSIP/AFWERX FY27 R1 monitoring** (firing B → [[atp-federal-funding-landscape]]). Combined
> Phase-4 MODE B = **two new pages** ([[prompt-architect-skills]] from A; [[potff]] entity from B).
> Baseline + final HEALTH_DEBT = 0 for both.

Regenerated each run from `tasks/index.md` Open items (this file is an **output**, never an
input — do not hand-curate). Cadence gate: `TZ=America/New_York date +%u` → `7` (Sunday,
02:39 EDT) → full loop runs.

## Phase 0 — baseline

- **HEALTH_DEBT = 0** (orphans 0 ×3, missing_from_index 0 ×2, stale_claims 0 ×1). 609 markdown files.
- Pre-existing objective defect set: **empty**. Soft signals only (152 dangling wikilinks, 1157
  reciprocal-link gaps) — unscored, judgment-heavy, not cloud-fixable without churn.

## Phase 1 — fast-track heals (→ main, auto-merge)

**None.** HEALTH_DEBT already 0 on `main`; no structural heal to fast-track tonight.

## Phase 2 — build (@cloud, 2 deliverables, both under "Improve + general skills")

Top-down selection from the Open `@cloud` items. The workhorse item ("Improve + general
skills") had **4 un-audited skills remaining** (the 2026-10-04 queue named them:
`concert-digest` + the 3 prompt-architect skills). Auditing them finishes dedicated coverage
to 10/11.

1. **Audit `concert-digest`** against the [[skill-authoring-playbook]] 6-section checklist →
   append to [[skill-audits-2026]]; apply safe structural fixes only.
   *Result:* §1 third-person fix applied; §5 evals gap logged; rest clean.
2. **Audit the 3 prompt-architect skills** (`claude-chat-prompt`, `claude-cowork-prompt`,
   `claude-code-prompt`) as a family → append to [[skill-audits-2026]].
   *Result:* all 6/6 structurally clean (textbook §1 + sibling redirects); shared §5 eval set
   logged — that eval run **is** the open "Prompt max" item (needs Cole).

## Phase 4 — MODE B (one generative enrichment)

- **New concept page `wiki/concepts/prompt-architect-skills.md`** — documents the 3-skill
  prompt-architect family as a *system*: the shared 4-step method, the surface-routing rule
  (interactive→chat, async-delegated→Cowork, repo/agentic→Code), and the per-surface prompt
  shape differences. Passes the new-page test: no page owns the family/routing concept
  ([[prompt-engineering-playbook]] is the general theory; this is the vault-specific
  instantiation), and it is a distinct reusable node. Grounded in the three skill files.
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

- **Train skills / Skill max / Prompt max — Skill Creator A/B + prompt eval runs** (@cloud):
  the remaining work is an *interactive* Skill Creator eval run needing Cole + a live baseline;
  no bounded unattended deliverable. The cloud-safe analog (skill audits) is this run's build.
- **Monitor DSIP + AFWERX (first Wednesday)** (🔁 @cloud): today is Sunday Oct 25, not a first
  Wednesday (last was Oct 1; next Nov 5). The 2026-10-11 pass already verified FY27 R1 (no HPW
  topics) from secondary sources; the ARM27BX01-DP001 lead's Oct 23 deadline has now passed.
  Nothing actionable in the cloud lane tonight; the recurring check resumes Nov 5.
- **Build the source-seeking (MODE B) rung** (@cloud): the design is proposed
  ([[tasks/improvements/2026-09-13-source-seeking-rung|source-seeking-rung]]); wiring it into
  `program.md` is a loop-brain edit → Cole's call.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch the frozen `score.py`.
  HEALTH_DEBT = 0 tonight anyway.
- **Try the autoresearch loop hands-on** (@cloud): requires renting an external GPU →
  outward/spending action. Ineligible for the unattended cloud lane.

## Not eligible here (for reference — @local or @human)

All `@local` and `@human` items — ATP federal-funding deadlines (xTech/SOFWERX/MTEC/AFRL),
Fulbright, Neuro pipeline + account creation, Claude Corps application steps, CRM enrichment,
finance decisions, Uship, password holder, IG/YouTube exports, concert/Spotify alerts,
the Sourcing & verification ingest (needs primary-source verification) — are ineligible for the
cloud lane (local data, outward/irreversible actions, or human decisions).
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
