# AutoResearch nightly queue — 2026-09-13 (Sunday weekly run)
# AutoResearch nightly queue — 2026-09-27 (Sunday weekly run)
# AutoResearch nightly queue — 2026-10-04 (Sunday weekly run)
# AutoResearch nightly queue — 2026-10-11 (Sunday weekly run)
# AutoResearch nightly queue — 2026-10-18 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items in **Phase 0** of `autoresearch/program.md`
(this file is an **output / transparency record, never an input**). The routine reads the task
board, selects the items doable unattended per the Doability rubric (explicit tag wins → infer →
skip-if-unsure), and records them here with one line on why each skipped item was skipped.

**Do not hand-curate this file.** The overnight routine **regenerates** it each night in
**Phase 0** of `autoresearch/program.md`: it reads `tasks/index.md`, selects the items
doable unattended (Doability rubric — tag wins → infer → skip-if-unsure), and writes them
here as the night's worklist, with one line on why each skipped item was skipped. It is a
**transparency record**, not an input.

The routine then works these in **Phase 2 (Build)**, top-down, bounded to ≤2–3/night, and
writes results back to `tasks/index.md` in **Phase 3**.

## Week of 2026-10-18 (Sunday — full run)

### Phase 0 baseline
Cadence gate: `TZ=America/New_York date +%u` → `7` (Sunday) → full loop runs.

## Phase 0 baseline

- **Cadence gate:** `TZ=America/New_York date +%u` → `7` (Sunday) ✅ — running full loop.
- **HEALTH_DEBT = 0** (orphans 0 × 3, missing_from_index 0 × 2, stale_claims 0 × 1).
- Pre-existing defect set: **empty** — no fast-track self-heal work in Phase 1.
- Phase 1 fast-track: **no-op** — HEALTH_DEBT already 0.
- Pre-existing objective defect set: **empty**. Only soft signals (dangling wikilinks to
  `@local`/`@human` CRM & profile pages, deliberately-atomic concept nodes) — unscored, not
  cloud-fixable.

### Phase 2 build — Selected (@cloud, 2 items)

1. **Verify ARM27BX01-DP001 (DSIP monitoring task — time-sensitive)**
   The 2026-10-11 monitoring note flagged "possible Army FY27 topic ARM27BX01-DP001 (Oct 23
   white-paper deadline) found in one secondary source — needs direct verification." Today is
   Oct 18 — 5 days from that deadline. This is time-sensitive. Web-verify the topic on
   dodsbirsttr.mil / armysbir.army.mil and update `atp-federal-funding-landscape.md` with the
   confirmed result. Also update the SOCOM BAA confirmation and FY27 R1 topic-count now that
   full DSIP data is available. Advances the `@cloud` DSIP monitoring recurring task.
   Deliverable: dated monitoring note in `atp-federal-funding-landscape.md`. Review lane.

2. **Skill audit — `concert-digest` SKILL.md**
   The last "Improve + general skills" progress note (2026-10-04) lists remaining audits:
   `orchestrate-agents`, `concert-digest`, the 3 prompt skills. `orchestrate-agents` was
   audited in the combined [[skill-audits-2026]] log (2026-09-13) — its brief entry is on record.
   `concert-digest` has never been audited. It is 51 lines, a @local/scheduled skill with
   concrete operating steps; a §6 finding (absolute Mac path) is visible on first read.
   Deliverable: `wiki/concepts/skill-audit-concert-digest.md` + any safe structural-only fixes to
   the skill. Review lane.

### Phase 4 MODE B (planned)

- One generative enrichment chosen after Phase 2 completes, from gaps uncovered during the build.

### Considered but skipped this run (with reason)

- **Train skills / Skill max / Prompt max — Skill Creator A/B eval runs** (@cloud): remaining
  work is interactive evaluation runs (needs Cole + live baseline). Not unattended-doable.
  Repeatedly deferred for this reason; unchanged.
- **Improve + general skills — `orchestrate-agents` standalone audit page** (@cloud): audited
  in the combined [[skill-audits-2026]] log (2026-09-13) as 4-sections-clean, no fixes; no new
  structural finding warrants a standalone page tonight; doing `concert-digest` instead.
- **Build the source-seeking (MODE B) rung** (@cloud): structural change to `program.md`;
  architectural change warrants human sign-off. Design published in
  [[tasks/improvements/2026-09-13-source-seeking-rung]]; deferred to Cole.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would edit the frozen `score.py`.
  HEALTH_DEBT = 0 tonight anyway. Ineligible.
- **Try autoresearch loop hands-on** (@cloud): requires external GPU + spending — ineligible.

### Not eligible this week (for reference — @local or @human)

All `@local` and `@human` items — xTech white paper (past Oct 19 deadline now), SOFWERX/USSOCOM
event, Barbara Knight email, MTEC, Fulbright deadlines, Neuro pipeline, Claude Corps application,
CRM enrichment, finance decisions, Uship, password holder, IG/YouTube exports — are ineligible
for the cloud lane (local data, outward actions, or human decisions).
**None.** HEALTH_DEBT is already 0 on `main`; no structural heal to fast-track tonight. The whole
run lives on the `autoresearch/night-2026-10-18` branch → one morning PR.

## Phase 2 build — Selected (@cloud, 2 items, bounded)

1. **DSIP + AFWERX monthly monitoring** (🔁 @cloud, [[atp-federal-funding-landscape]]). Timely: the
   2026-10-11 scan left one open verification — an unidentified Army FY27 topic **ARM27BX01-DP001**
   with an **Oct 23** white-paper deadline (5 days out) flagged "verify before Oct 23." **Deliverable:**
   resolve that topic + re-confirm whether any 711 HPW / human-performance opening appeared in FY27
   Release 1, and refresh the dated monitoring note. Pure web + synced vault → cloud-safe. Review lane.

2. **Improve + general skills → audit `concert-digest` SKILL.md** (@cloud). `concert-digest` is one of
   the last two vault skills never given a dedicated [[skill-authoring-playbook]] audit. **Deliverable:**
   run the 6-section checklist, apply any structural/no-behavior-change fix unattended, and log the
   findings on the existing [[skill-audits-2026]] scoreboard (no new thin page — the vault is already
   audit-saturated). Review lane.

## Phase 4 MODE B (planned)

- TBD after Phase 2 — one generative enrichment proposal chosen from a genuine gap uncovered during
  the build (per the new-page test + simplicity criterion; no thin filler).

## Considered but skipped this run (with reason)

- **Train skills / Skill max / Prompt max** (@cloud): their remaining work is the **interactive Skill
  Creator A/B eval run** and live prompt eval-testing — needs Cole + the interactive harness. Not
  unattended-doable. (The cloud-safe analog, structural skill audits, is tonight's item 2.)
- **Build the source-seeking (MODE B) rung** (@cloud): the cloud-safe design slice is already written
  ([[extending-the-llm-wiki]] + [[tasks/improvements/2026-09-13-source-seeking-rung]]); the remaining
  step is a `program.md` loop-brain edit, which is Cole's call (@human sign-off). Nothing new to build
  unattended.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch the **frozen** `score.py` — out of
  bounds. HEALTH_DEBT = 0 tonight anyway.
- **Try the autoresearch loop hands-on** (@cloud): requires provisioning an external/rented GPU →
  outward/spending action. Ineligible for the unattended cloud lane.
- **Ingest + verify Anthropic "Code with Claude 2026" / Claude Code mid-2026 release notes**
  (Sourcing & verification): tagged **@human** on the board — honored strictly, not attempted in the
  cloud. (Its web-research shape is cloud-friendly, but the explicit tag wins; left for Cole.)

## Not eligible here (for reference — @local or @human)

All `@local` and `@human` items — xTech|Search 10 white paper (due Oct 19), SOFWERX/USSOCOM event,
Barbara Knight / AFRL email, MTEC, Fulbright deadlines & materials, Neuro pipeline, Claude Corps
application steps, outreach/networking sends, CRM enrichment, finance decisions, Uship, password
holder, IG/YouTube exports — are ineligible for the cloud lane (local data, outward/irreversible
actions, or human decisions).
