# AutoResearch nightly queue — 2026-08-30 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items (this file is an output, never an input).
Baseline this run: `HEALTH_DEBT = 16` (orphans 2×3=6, missing_from_index 5×2=10, stale_claims 0).

## Phase 0 baseline

- **HEALTH_DEBT = 16** (orphans: 2 × 3 = 6, missing_from_index: 5 × 2 = 10)
- Defects:
  - Orphans: `skill-authoring-playbook` (no inbound from `startup-radar` / `skill-audit-worked-example`), `skill-audit-worked-example` itself had no inbound
  - Missing from index: `startup-radar`, `skill-audit-worked-example`, `activate`, `claude-api`, `ply`
- All 7 defects are pre-existing; all structural → Phase-1 fast-track eligible.

## Phase 1 fast-track heals (→ main, auto-merged)

HEALTH_DEBT driven 16 → 0 across 6 iterations:
1. Fixed 2 orphans: added `[[startup-radar]]` + `[[skill-audit-worked-example]]` to `skill-authoring-playbook.md` Related section. Debt 16→10.
2. Added `startup-radar` to index.md. Debt 10→8.
3. Added `skill-audit-worked-example` to index.md. Debt 8→6.
4. Added `activate` to index.md. Debt 6→4.
5. Added `claude-api` to index.md. Debt 4→2.
6. Added `ply` to index.md. Debt 2→0. **HEALTH_DEBT = 0** after Phase 1.

## Phase 2 build — Selected (@cloud, 1 item)

1. **Improve + general skills → audit `networking-prep` SKILL.md against [[skill-authoring-playbook]]**:
   The playbook checklist was built last session; applying it to a live skill is the outstanding
   "run one skill through the checklist" deliverable. `networking-prep` chosen because it's
   cloud-visible (~119 lines) and was recently extended. Deliverable:
   `wiki/concepts/skill-audit-networking-prep.md` + structural step-numbering fix on the skill
   (`Step 5-output`→`Step 4`, `Step 6`→`Step 5`). Review lane.

## Phase 4 MODE B

- **Gap-fill: `wiki/concepts/fmri-experimental-design.md`**:
  The fMRI concept cluster covers preprocessing, GLM/stats, and lab pages but had no page on
  experimental design — the upstream step that determines what the GLM can detect.
  `fmri-glm-analysis` already referenced it with no target. New page written from course
  knowledge (Huettel Ch. 7 + NEUROSCI 382 context); synthesis note included; reciprocal links
  from `fmri-glm-analysis` and entry in index.md. Review lane.

- **MCP hub enrichment: `wiki/entities/mcp.md`** (prior session, 2026-08-30T02):
  Built the 19x-referenced mcp stub into a hub page — architecture, primitives, transports,
  web-grounded 2026-07-28 spec snapshot; promoted index entry.

## Considered but skipped this night (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): the remaining work is an *interactive*
  eval run (needs Cole + live baseline measurement); not fully unattended.
- **Prompt max — eval-test the 3 prompt-architect skills** (@cloud): evals need interactive
  baseline measurement against real tasks. No bounded unattended deliverable.
- **Skill max — Skill Creator A/B eval run** (@cloud): same interactive-eval blocker; the
  trigger-tuning pass it needed is already complete (progress 2026-08-10).
- **Build the source-seeking (MODE B) rung** (@cloud): structural change to `program.md`;
  warrants human sign-off, too large for one night's build.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch the frozen `score.py` —
  never edited by the loop. HEALTH_DEBT = 0 tonight anyway.
- **Try an autoresearch loop hands-on** (@cloud): requires provisioning an external/rented GPU →
  outward action + spending. Ineligible for the cloud lane.

## Not eligible here (for reference — @local or @human)

All `@local` and `@human` items — Fulbright deadlines, Neuro pipeline, CRM enrichment, finance
decisions, Uship, Claude Corps application steps, password holder, IG/YouTube exports — are
ineligible for the cloud lane (local data, outward actions, or human decisions).
