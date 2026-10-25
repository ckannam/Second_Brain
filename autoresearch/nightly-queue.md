# AutoResearch nightly queue — 2026-10-25 (Sunday weekly run)

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

## Considered but skipped this run (with reason)

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
