# AutoResearch nightly queue — 2026-08-30 (Sunday weekly run)

Regenerated each run from `tasks/index.md` Open items (this file is an output, never an input).
Baseline this run: `HEALTH_DEBT = 16` (orphans 2×3=6, missing_from_index 5×2=10, stale_claims 0).

## Selected for tonight (cloud-doable, bounded)

1. **Phase 1 BUILD — "Improve + general skills" ([[Claude Mastery]]) → audit + fix `networking-prep`.**
   The one open `@cloud` build item whose next step is genuinely cloud-doable. Run the
   [[skill-authoring-playbook]] checklist against the `networking-prep` skill (the vault's
   2nd-largest at 118 lines), extending the [[skill-audit-worked-example]] pattern. Audit finds
   5 sections clean/minor + **one real fix**: Step 1 hardcodes a stale-prone lane snapshot,
   violating the skill's own Freshness principle. Apply the safe fix; record the run as a compact
   second worked example. Synced vault only, no web needed → but review-lane (edits a SKILL.md).

2. **Phase 3 SELF-HEAL (MODE A) — drive HEALTH_DEBT 16 → 0.** All pre-existing objective debt is
   recent pages (Aug 8–20) that landed without wiring: fix 2 orphans (`startup-radar`,
   `skill-audit-worked-example`) with reciprocal links, and 5 missing-from-index entries
   (`startup-radar`, `skill-audit-worked-example`, `activate`, `claude-api`, `ply`).

3. **Phase 4 MODE B — one generative enrichment proposal** (chosen during the run per the
   new-page test + simplicity criterion; no thin filler).

Build night → the whole run lives on `autoresearch/night-2026-08-30` → one morning PR (no
direct-to-main push this run).

## Considered but skipped this run (with reason)

- **Train skills — Skill Creator A/B eval run** (@cloud): the remaining work is an *interactive*
  eval run (needs Cole + live baseline measurement); not fully unattended. The manual playbook
  audit tonight is the cloud-doable analog.
- **Prompt max — eval-test the 3 prompt-architect skills** (@cloud): evals need interactive
  baseline measurement against real tasks. No bounded unattended deliverable.
- **Skill max — Skill Creator A/B eval run** (@cloud): same interactive-eval blocker; the
  trigger-tuning pass it needed is already complete (progress 2026-08-10).
- **Build the source-seeking (MODE B) rung** (@cloud): a structural change to `program.md`;
  architecturally significant → warrants human sign-off, too large for one night's build.
- **Tune HEALTH_DEBT weights / add metrics** (@cloud): would touch the **frozen** `score.py` —
  never edited by the loop. Ineligible.
- **Try an autoresearch loop hands-on** (@cloud): requires provisioning an external/rented GPU →
  outward action + spending. Ineligible for the cloud lane.

## Not eligible here (for reference — @local or @human)

All `@local` and `@human` items — Fulbright deadlines, Neuro pipeline, CRM enrichment, finance
decisions, Uship, Claude Corps application steps, password holder, IG/YouTube exports — are
ineligible for the cloud lane (local data, outward actions, or human decisions).
