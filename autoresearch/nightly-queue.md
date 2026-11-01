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
