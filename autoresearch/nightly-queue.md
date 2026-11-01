# Nightly queue — 2026-11-01 (Sunday weekly run)

Regenerated each run (an **output**, not an input). Tonight's worklist per `program.md` Phase 0
SELECT + the Doability rubric. Baseline `score.py` HEALTH_DEBT = **0** (orphans 0,
missing_from_index 0, stale_claims 0) — empty pre-existing defect set, so Phase 1 fast-track
heal-on-`main` is a **no-op** this run.

## Cadence gate
Sunday ET confirmed (`TZ=America/New_York date +%u` → 7). Full loop runs.

## Selected (cloud-doable, bounded ≤2–3) — built this run

1. **🔁 @cloud — DSIP + AFWERX first-Wednesday monitoring** ([[atp-federal-funding-landscape]]).
   *Why:* explicit `@cloud`, web-only, and time-sensitive — FY27 R1 closes **Nov 25** and the
   Nov first-Wednesday pre-release is **Nov 4** (3 days out). → Added a dated monitoring note:
   FY27 R1 open with no 711 HPW topic; **reauthorization resolved through Sept 30, 2031**; AFWERX
   "Focused Open Topic" model shift flagged; all secondary-sourced (DSIP + afrl.af.mil unreachable
   via proxy — verify primary).

2. **@cloud — Improve + general skills: audit `concert-digest`** ([[Claude Mastery]]).
   *Why:* the steady `@cloud` audit thread; `concert-digest` was next on the 2026-10-04
   remaining-audits list and had no dedicated audit page. → Fixed the §1 second-person description
   ("Use to compose" → "Composes"); wrote [[skill-audit-concert-digest]] (§2–§4/§6 clean, §5 eval
   gap logged); appended to [[skill-audits-2026]].

## MODE B (Phase 4, one proposal, branch)
Enriched [[skill-authoring-playbook]] §1 with an empirical **imperative-opening lint check** —
grounded in the 2/2 audit hit-rate found tonight (data-backed, reusable, no web fabrication).

## Skipped (with reason)

- **@cloud "Train skills" / "Prompt max" / "Skill max"** — cloud-doable parts exhausted over prior
  nights; the only remaining work is the **interactive Skill Creator A/B eval run that needs Cole**
  (@human). Not unattended-doable.
- **@cloud "Build the source-seeking (MODE B) rung"** — design already proposed
  ([[tasks/improvements/2026-09-13-source-seeking-rung|source-seeking-rung]]); remaining step is a
  **@human decision** to wire it into `program.md` (a loop-brain edit = Cole's call).
- **@cloud "Tune HEALTH_DEBT weights / add metrics"** — would require editing the **frozen
  `score.py`** (hard boundary — never edit). Not cloud-executable; needs a human design decision.
- **@cloud "Try an autoresearch loop hands-on (rented GPU)"** — needs **spending money + outward
  actions** (clone/run on paid compute). Fails the Doability rubric (outward/irreversible).
- **All `@human` / `@local` / ⏸️ items** — ATP federal human moves (xTech, SOFWERX, AFRL emails,
  MTEC, SOCOM), Job Search outreach (Solace/Atlanta Ventures/Left Lane/Damien/Christy), Fulbright,
  Neuro channel + learning app, finance, CRM/message enrichment, Uship, Instagram/YouTube exports,
  vault password holder — honor the lanes; **never attempted in the cloud.**

## Outcome
2 Phase-2 builds + 1 Phase-3 write-back + 1 Phase-4 MODE B, all on
`autoresearch/night-2026-11-01` → one morning PR. HEALTH_DEBT held at 0 throughout; no Phase-1
`main` heals (empty baseline defect set).
# AutoResearch nightly queue — 2026-11-01 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items (this file is an output, never an input).
Cadence gate: `TZ=America/New_York date +%u` → `7` (Sunday) → full loop runs.

## Phase 0 baseline

- **HEALTH_DEBT = 0** (orphans 0 × 3, missing_from_index 0 × 2, stale_claims 0 × 1).
- Pre-existing objective defect set: **empty**.
- Soft signals only: 154 dangling wikilinks to `@local`/`@human` CRM + profile pages — unscored,
  not cloud-fixable (most reference local-only files: people names, finance pages, personal profile).

## Phase 1 fast-track heals (→ main, auto-merged)

**None.** HEALTH_DEBT is already 0 on `main`; no structural heal to fast-track tonight.

## Phase 2 build — Selected (@cloud, ≤3 items)

1. **Improve + general skills → standalone skill audit: `concert-digest`**  
   Task "Improve + general skills" remaining: "audits of `orchestrate-agents`, `concert-digest`,
   the 3 prompt skills." `concert-digest` has never been audited (not in skill-audits-2026.md, no
   standalone page). **Deliverable:** `wiki/concepts/skill-audit-concert-digest.md` + apply any
   safe structural fixes to `.claude/skills/concert-digest/SKILL.md`. Review lane.

2. **Improve + general skills → standalone skill audit: `orchestrate-agents`**  
   `orchestrate-agents` has an entry in `skill-audits-2026.md` (2026-09-13) but no standalone audit
   page (unlike networking-prep, startup-radar, vault-autoresearch, wiki-query which all have one).
   The 2026-10-04 progress note explicitly lists it as remaining. **Deliverable:**
   `wiki/concepts/skill-audit-orchestrate-agents.md` — supersedes the 2026-09-13 combined-log
   entry with a full standalone audit record. Review lane.

3. **Monitor DSIP + AFWERX** (🔁 @cloud task, first-Wed cadence)  
   DSIP FY27 R1 opened Oct 28; closes Nov 25, 2026. Today (Nov 1) is 4 days into the window —
   close enough to the Nov 4 first-Wednesday trigger to do a meaningful check. Previous run
   (2026-10-11) could not access the DSIP site directly via proxy; using web search. **Deliverable:**
   update `wiki/concepts/atp-federal-funding-landscape.md` with a dated monitoring note (findings
   or "no new human-performance topics"). Review lane.

## Phase 4 (MODE B) — planned

- ONE generative enrichment chosen after Phase 2 completes. Candidate: enrich a dangling-link
  stub that the Phase 2 work surfaces, or propose a source to ingest from the Sourcing &
  verification task.

## Considered but skipped this night (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): interactive eval, needs Cole.
- **Prompt max — eval-test 3 prompt-architect skills** (@cloud): interactive evals, needs Cole.
- **Skill max — Skill Creator A/B eval run** (@cloud): same interactive-eval blocker.
- **Build the source-seeking (MODE B) rung** (@cloud): structural change to `program.md`; warrants
  human sign-off. The design proposal already landed (2026-09-13); remaining = Cole's wiring decision.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would edit the frozen `score.py` — never
  edited by the loop.
- **Try autoresearch loop hands-on** (@cloud): requires external GPU + spending — ineligible.
- **Audit remaining 3 prompt skills** (`claude-chat-prompt`, `claude-cowork-prompt`,
  `claude-code-prompt`): deferred to a future night to keep this run bounded.

## Not eligible (for reference — @local or @human)

All `@local` and `@human` items — xTech white paper, SOFWERX networking, Barbara Knight email,
MTEC, Fulbright deadlines, Neuro pipeline + channel, Claude Corps application, CRM enrichment,
finance decisions, Uship, password holder, IG/YouTube exports, Spotify alerts — are ineligible for
the cloud lane (local data, outward/irreversible actions, or human decisions).
