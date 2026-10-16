# AutoResearch nightly queue — 2026-09-13 (Sunday weekly run)
# AutoResearch nightly queue — 2026-09-27 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items (this file is an output, never an input).
Baseline this run: `HEALTH_DEBT = 0` (orphans 0, missing_from_index 0, stale_claims 0).

## Phase 0 baseline

## Night of 2026-09-13 (Sunday — weekly run)

### Baseline (Phase 0)
- **HEALTH_DEBT = 0** (orphans: 0, missing_from_index: 0, stale_claims: 0)
- Pre-existing defect set: **empty** — no fast-track self-heal work in Phase 1.

## Phase 1 fast-track heals (→ main, auto-merged)

HEALTH_DEBT = 0 at baseline; Phase 1 is a clean skip. No fast-track work needed.

## Phase 2 build — Selected (@cloud, 2 items)

1. **Improve + general skills → skill audit pass on `orchestrate-agents` + `wiki-query`**:
   Task "Improve + general skills" remaining work = "more skill iterations." The
   `startup-radar` audit (skill-audit-worked-example, 2026-08-08) is the only completed
   audit. Auditing two more vault skills tonight advances the task: apply the
   [[skill-authoring-playbook]] 6-section checklist to `orchestrate-agents` and `wiki-query`,
   apply any structural/no-behavior-change fixes unattended, document findings in a combined
   audit wiki page, and log recommendations for Cole.
- **HEALTH_DEBT = 0** — no structural defects in the pre-existing set.
- Phase 1 (fast-track heal on `main`): **no-op** — nothing to heal.

## Phase 1 fast-track heals (→ main, auto-merged)

None. HEALTH_DEBT = 0 at baseline; no eligible fast-track work.

## Phase 2 build — Selected (@cloud, 2 items)

1. **Improve + general skills → audit `startup-radar` SKILL.md against [[skill-authoring-playbook]]**:
   Previous audits covered `vault-improve` (2026-08-10) and `networking-prep` (2026-08-30).
   `startup-radar` is the next-highest-leverage unaudited skill: 199 lines, complex multi-step
   procedure, and the prior audit noted it had no evals (§5 gap). The key findings to investigate:
   hardcoded absolute Mac paths, an interactive "ask Cole" step that breaks unattended runs,
   and no evals.
   Deliverable: `wiki/concepts/skill-audit-startup-radar.md` + any safe structural fixes to
   the skill file. Review lane.

2. **Build source-seeking MODE B rung (cloud-safe part) — design page**:
   Previous nights skipped this as "too large for one night." Tonight's cloud-safe deliverable:
   research what systematic source-seeking would look like and update [[extending-the-llm-wiki]]
   with a concrete design for a MODE C rung. The human-reviewed PR is the sign-off; implementation
   in `program.md` is deferred to Cole. Advances the item meaningfully without unreviewed
   changes to the loop's control file.
   Deliverable: update to `wiki/concepts/extending-the-llm-wiki.md` + progress note on task.
   Review lane.

2. **MODE B (Phase 4) — enrich `wiki/sources/evals-for-taste.md`**:
   `evals-for-taste` is referenced by six wiki pages (skill-authoring-playbook,
   writing-reliable-skills, skill-audit-worked-example, the-prompting-playbook,
   skill-authoring-playbook, agent-skills) but the page itself has no inbound backlinks
   from those referencing pages (all appear as reciprocal_gaps in the score output) and
   may be a stub. Tonight: web-ground the "evals for taste" concept, enrich the page, and
   add reciprocal backlinks. Review-lane only (generated content → PR).

### Considered but skipped this night (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): The Skill Creator tool runs inside
  the Claude platform and requires interactive evaluation runs; cannot be run fully unattended.
  Deferred again.
- **Prompt max — eval-test the 3 prompt-architect skills** (@cloud): Evals require interactive
  baseline measurement against real tasks; no bounded unattended deliverable.
- **Skill max — Skill Creator A/B eval run** (@cloud): Same as above; the interactive portion
  needs Cole. The manual skill-audit portion (tonight's item) is the cloud-safe analog.
- **Build the source-seeking (MODE B) rung** (@cloud): Structural change to `program.md`;
  architectural design warrants human sign-off. Too large for a single night.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): Touches the scorer; needs human sign-off.
  HEALTH_DEBT = 0 tonight anyway.
- **Try autoresearch loop hands-on** (@cloud): Requires external GPU provisioning → outward
  action. Ineligible.

## Not eligible here (for reference — @local or @human)

All `@local` and `@human` items — Fulbright deadlines, Neuro pipeline, CRM enrichment, finance
decisions, Uship, Claude Corps application steps, password holder, IG/YouTube exports — are
ineligible for the cloud lane (local data, outward actions, or human decisions).
## Week of 2026-09-06 (Sunday — full run)

### Baseline (Phase 0)
- **HEALTH_DEBT = 0** (orphans: 0, missing_from_index: 0, stale_claims: 0)
- Pre-existing defect set: **empty** — no scored defects to fast-track heal tonight.
- Cadence gate: Sunday ET ✅ — running full loop.
- **Note:** Two concurrent runs contributed this week's build. Items 1–2 were completed by an earlier firing; items 3–4 by a later firing. All four are recorded here for transparency.

### Selected (@cloud, bounded to ≤3 per run) — top-down

**Earlier firing:**

1. **Improve + general skills / Skill max → land the real fix + vault-wide audit sweep**:
   The `skill-audit-worked-example` page (2026-08-08) audited `startup-radar` against the
   playbook and recorded a §6 path fix (Step 7 validator) as **applied** — but the change
   never reached the `SKILL.md` (still hardcoded the absolute
   `/Users/colekannam/Desktop/Second Brain/startup-tracker/validate.py`; file last edited
   2026-07-31). Tonight: (a) **land the fix** — normalize Step 7 to `startup-tracker/validate.py`
   (structural, no behavior change, matches Steps 4–5), reconciling the claim with the file;
   (b) **rerun the reusable audit template across all 11 vault skills** and record the honest
   per-skill verdicts in the worked-example page — proving the template scales and catching any
   other real defect. Result: 10 clean, 1 fix. Directly advances "Improve + general skills"
   (remaining: more skill iterations) and "Skill max".

2. **MODE B (Phase 4) — create `wiki/concepts/skill-evals.md`**:
   Concrete skill-eval how-to (official query/files/expected_behavior format, baseline-first
   5-step process, Claude A/B loop, "no built-in runner" reality, runnable worked eval set for
   startup-radar); grounded in Anthropic's Skill authoring best practices. Wired into
   [[skill-authoring-playbook]] §5, [[skill-audit-worked-example]], index, and [[Claude Mastery]]
   bucket. Review-lane only (generated content → PR).

**Later firing:**

3. **Improve + general skills → cross-redirect pass on `vault-autoresearch` and `wiki-query` skill descriptions**:
   The skill-authoring-playbook checklist requires sibling-skill cross-redirects so Claude
   routes correctly among related skills. Currently:
   - `vault-improve` already redirects to both `vault-autoresearch` and `wiki-query` ✅
   - `vault-autoresearch` redirects to `wiki-query` but NOT to `vault-improve` ❌
   - `wiki-query` redirects to neither sibling ❌
   Fix: add the missing redirect clauses to both descriptions. Small structural change to
   skill files (not scored, rides the PR).

4. **MODE B (Phase 4) — create `wiki/concepts/outreach-kit.md`**:
   Fills the long-standing dangling `[[outreach-kit]]` link referenced from
   `outreach-pipeline.md` and `tasks/index.md`. No existing page owns the template library
   (separate from `outreach-pipeline` which describes the process). Passes the new-page test:
   distinct reusable thing (Cole would link to it on every outreach session), genuinely
   cloud-doable (grounded in vault's `cold-email-job-search.md` + pipeline templates).
   Review-lane only (generated content → PR).

### Considered but skipped this week (with reason)
- **Train skills — Skill Creator A/B eval run** (@cloud): requires interactive Claude platform
  evaluation runs; not fully unattended. Deferred.
- **Prompt max — eval-test the 3 prompt-architect skills** (@cloud): interactive baseline
  measurement needed. Not doable unattended.
- **Skill max — Skill Creator A/B eval run** (@cloud): same constraint. Deferred.
- **Build the source-seeking (MODE B) rung** (@cloud): structural change to `program.md`;
  architectural design warrants human sign-off.
- **Tune HEALTH_DEBT weights** (@cloud): touches the scorer; needs human sign-off. Also
  HEALTH_DEBT = 0 tonight — no urgency.
- **Try autoresearch loop hands-on** (@cloud): requires external GPU provisioning (outward
  irreversible action). Ineligible.

### Not eligible this week (for reference — @local or @human)
All `@local` and `@human` items (Fulbright deadlines, Neuro pipeline, CRM enrichment, finance
decisions, Uship, Claude Corps application steps, etc.) are ineligible for the cloud lane.
- **Enrich `wiki/concepts/proactive-agents.md`**: The page is a 9-line stub that references four
  pages without developing the concept. Filling it from already-ingested vault sources is a
  bounded, factual enrichment with no net-new web-search claims.

## Considered but skipped this night (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): remaining work is an interactive eval
  run (needs Cole + live baseline); no bounded unattended deliverable.
- **Prompt max — eval-test the 3 prompt-architect skills** (@cloud): evals need interactive
  baseline measurement. Not unattended-doable.
- **Skill max — Skill Creator A/B eval run** (@cloud): trigger-tuning pass complete (2026-08-10);
  remaining eval run needs Cole.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch the frozen `score.py`. Also
  HEALTH_DEBT = 0 tonight.
- **Try an autoresearch loop hands-on** (@cloud): requires provisioning a rented GPU →
  outward action + spending. Ineligible for unattended cloud lane.

## Not eligible here (for reference — @local or @human)

All `@local` and `@human` items — Fulbright steps, Neuro pipeline, CRM enrichment, finance
decisions, Uship, Claude Corps application, password holder, IG/YouTube exports,
concert alerts — are ineligible (local data, outward actions, or human decisions).
