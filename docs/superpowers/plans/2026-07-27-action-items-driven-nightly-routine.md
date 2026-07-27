# Action-Items-Driven Nightly Routine — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the overnight cloud routine read the Action Items board directly, build every task it can do unattended, write progress back, then self-heal and enrich — all reviewable in one morning PR.

**Architecture:** Pure documentation/config change. The "program" the routine follows is `autoresearch/program.md` (rewritten to a 6-phase order); the board is `tasks/index.md` (per `AGENTS.md`). No code executes differently — the cloud agent reads these instruction files at run time. Verification is by text-presence checks, running the frozen `score.py` to confirm nothing broke, and a final subagent dry-run of the selection rubric.

**Tech Stack:** Markdown instruction files, `python3 autoresearch/score.py` (unchanged frozen evaluator), the `RemoteTrigger` cloud-routine API, git.

## Global Constraints

- **NEVER edit `autoresearch/score.py`** (frozen evaluator) or modify anything under `raw/`.
- The three lanes are exactly `@cloud` / `@local` / `@human`.
- Cloud-doable rubric (all four must hold): touches only synced vault + web/connectors · needs no local data (`crm/`, `profile/`, `finance/`, iMessage, Contacts) · takes no outward/irreversible action · needs no human decision.
- Selection precedence: **explicit tag wins → infer if untagged → skip + flag if unsure.**
- Nightly order is fixed: **Select → Build → Write-back → Self-heal → AutoResearch → PR.**
- Action-item line format: `- [ ] @lane <action> — <context> [[related-page]] (added YYYY-MM-DD)`.
- Write-back: done → `[x]` + `(done DATE)` + move to Done; partial → leave `[ ]`, append `⏳ progress DATE: did X; remaining Y`. Never fabricate completion.
- Branch model: build nights → whole run on `autoresearch/night-YYYY-MM-DD` → one PR; pure-maintenance nights → MODE A may commit to `main`.
- Date today: 2026-07-27.

---

### Task 1: Rewrite `autoresearch/program.md` to the 6-phase loop

**Files:**
- Modify (full rewrite): `autoresearch/program.md`

**Interfaces:**
- Produces: the phase vocabulary (`Phase 0 Select` … `Phase 5 PR`) and the doability rubric that Tasks 2, 5, and 7 reference verbatim.

- [ ] **Step 1: Replace the file contents** with exactly:

```markdown
# Vault AutoResearch — loop instructions (`program.md`)

The **loop's brain** — the human edits it; the loop follows it. `AGENTS.md` is the
source of truth for *how to write the wiki*; this file governs the *nightly build +
improvement loop*. Karpathy's AutoResearch, applied to this vault.

## The nightly order (six phases, on the night branch)

The whole run works on `autoresearch/night-YYYY-MM-DD`. **Build first, heal second** —
self-heal cleans up any structural debt the build introduces.

- **Phase 0 — Select.** Read `tasks/index.md` Open items. Select the ones doable
  unattended (see Doability rubric). **Regenerate `autoresearch/nightly-queue.md`** as
  the night's worklist: what was picked, and one line each on why the rest were skipped.
- **Phase 1 — Build.** Work selected items **top-down, bounded (≤2–3/night)**, building
  per `AGENTS.md`. Web tools (WebSearch/WebFetch) + synced vault only.
- **Phase 2 — Write-back.** Update `tasks/index.md` (see Write-back rules).
- **Phase 3 — Self-heal (MODE A).** Drive HEALTH_DEBT down (see below), including any
  defect the build just introduced.
- **Phase 4 — AutoResearch (MODE B).** One generative enrichment proposal.
- **Phase 5 — PR.** Open one morning PR (night branch → `main`) and stop.

## The metric

`autoresearch/score.py` emits **HEALTH_DEBT** — one scalar, **lower is better** (0 =
clean). Run with `--json` to drive the loop. It is the vault's `val_bpb`.

## The ratchet (git)

Every self-heal iteration either **lowers HEALTH_DEBT (keep the commit)** or **does not
(revert)**. Git is the ratchet and the rollback — a bad unattended night is one
`git reset` away.

## Doability rubric (Phase 0)

An item is **cloud-doable** only if **all** hold:
- touches only the **synced vault + web/connectors**;
- needs **no local data** (`crm/`, `profile/`, `finance/`, iMessage, Contacts — invisible
  to the cloud);
- takes **no outward/irreversible action** (no email/messages, no spending, no merge to `main`);
- needs **no human decision**.

Precedence: **explicit `@cloud`/`@local`/`@human` tag wins**; if an item is **untagged**,
**infer** against the rubric; **when unsure → skip and flag** (note why in the PR). An
item partly doable → do the cloud-safe part, leave the rest as a `⏳ progress` note.

## Write-back rules (Phase 2)

- **Fully done** → flip `- [ ]` to `- [x]`, append `(done YYYY-MM-DD)`, move it to the
  **Done** section (newest at top), per `AGENTS.md`. Never delete history.
- **Partially advanced** → leave `- [ ]` open, append an indented
  `⏳ progress YYYY-MM-DD: did X; remaining Y` line.
- **Never mark done what was not finished.** If completion can't be verified, it isn't done.

## MODE A — self-healing (Phase 3)

1. `python3 autoresearch/score.py --json` → record `health_debt` as **baseline**.
2. Pick the single **highest-weight** defect (orphans → missing_from_index → stale_claims).
   One change per iteration.
3. Fix it per `AGENTS.md`:
   - orphan → add the missing reciprocal link(s) from pages that should reference it.
   - missing_from_index → add the page to `index.md` (or `crm/index.md`) with a one-line
     summary in the right category.
   - stale_claim → mark the superseded claim per the freshness rule; never silently rewrite.
4. Re-run `score.py`.
5. **Improved?** commit. **Equal or worse?** `git checkout -- .` (discard — don't keep "for reference").
6. Append a row to `autoresearch/results.tsv` (`ts / mode / target / debt_before / debt_after / status / note`).
7. Repeat until HEALTH_DEBT is 0 or no safe, objective fix remains.

## MODE B — autoresearch / generative (Phase 4)

Propose ONE improvement: a genuinely new page a source warrants, a stub worth filling, or
a source to ingest — applying `AGENTS.md`'s **new-page test** and **simplicity criterion**
(never farm thin pages to inflate counts). Commit on the branch. Do **not** merge.

## Branch model

- **Build nights** (Phase 1 did work): the **entire run** — build, write-back, self-heal,
  generative — lives on the night branch → **one morning PR**. The Action Items board
  updates on `main` only when the human **merges**.
- **Pure-maintenance nights** (no cloud-doable tasks): MODE A self-heal may commit objective
  fixes straight to `main` as before; then one MODE B proposal on the branch.

## NEVER STOP (for scheduled/unattended runs)

Don't ask the human whether to continue — they may be asleep. Run all phases in order, then
open the PR and end. Next run resumes from the current state via `tasks/index.md`,
`score.py`, and `results.tsv` (the cross-run memory).

## Safety — the frozen boundaries

- **NEVER edit `autoresearch/score.py`** (the frozen evaluator) or modify anything under `raw/`.
- **NEVER take outward/irreversible actions** — no email/messages, no spending, no merge to `main`.
- **Honor `@human` / `@local` lanes strictly** — never attempt them in the cloud.
- **Never fabricate completion.**
- Everything is reviewable in the morning PR before it reaches `main`.
- Pair unattended runs with Auto Mode deny-rules for `raw/**` and `autoresearch/score.py`.
```

- [ ] **Step 2: Verify the phase order and rubric are present**

Run: `grep -n "Phase 0 — Select\|Phase 3 — Self-heal\|Doability rubric\|Write-back rules\|Never fabricate completion" autoresearch/program.md`
Expected: 5 matches, one per line.

- [ ] **Step 3: Verify frozen boundaries survived the rewrite**

Run: `grep -c "NEVER edit \`autoresearch/score.py\`\|modify anything under \`raw/\`" autoresearch/program.md`
Expected: ≥1 (the safety section retained).

- [ ] **Step 4: Confirm the evaluator still runs unchanged**

Run: `python3 autoresearch/score.py --json | python3 -c "import sys,json; print('health_debt=', json.load(sys.stdin)['health_debt'])"`
Expected: `health_debt= 0` (no error — we did not touch `score.py`).

- [ ] **Step 5: Commit**

```bash
git add autoresearch/program.md
git commit -m "program.md: rewrite loop to 6-phase order (build → write-back → heal → research)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 2: Repurpose `autoresearch/nightly-queue.md` as an auto-generated staging artifact

**Files:**
- Modify: `autoresearch/nightly-queue.md` (header + rules block; keep existing Queue items as the current example content)

**Interfaces:**
- Consumes: the Phase 0 vocabulary from Task 1.

- [ ] **Step 1: Replace the top of the file** (everything from the H1 through the end of the `## Rules for the routine` block) with:

```markdown
# Nightly Selection — auto-generated by the routine (Phase 0)

**Do not hand-curate this file.** The overnight routine **regenerates** it each night in
**Phase 0** of `autoresearch/program.md`: it reads `tasks/index.md`, selects the items
doable unattended (Doability rubric — tag wins → infer → skip-if-unsure), and writes them
here as the night's worklist, with one line on why each skipped item was skipped. It is a
**transparency record**, not an input.

The routine then works these in **Phase 1 (Build)**, top-down, bounded to ≤2–3/night, and
writes results back to `tasks/index.md` in **Phase 2**.
```

- [ ] **Step 2: Verify the hand-curation instruction is gone and the auto-gen note is present**

Run: `grep -n "Do not hand-curate\|auto-generated by the routine" autoresearch/nightly-queue.md; grep -c "vetted\|Work the \*\*top 1–2" autoresearch/nightly-queue.md`
Expected: 2 matches for the new text; `0` for the old "vetted"/"top 1–2" instructions.

- [ ] **Step 3: Commit**

```bash
git add autoresearch/nightly-queue.md
git commit -m "nightly-queue.md: repurpose to auto-generated Phase 0 selection artifact

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 3: Require a lane tag in `AGENTS.md` Action Items → Capture

**Files:**
- Modify: `AGENTS.md` (the Action Items section, around lines 206–220)

**Interfaces:**
- Produces: the `@lane` line-format that Task 4 applies to every existing item.

- [ ] **Step 1: Replace the Capture step (step 1) of the Action Items block** with:

```markdown
1. **Capture (with a lane).** When an action item arises, append it under **Open** in
   `tasks/index.md` as an Obsidian checkbox, **tagged with the lane decided in the moment**:
   `- [ ] @lane <action> — <one-line context> [[related-page]] (added YYYY-MM-DD)`, where
   `@lane` is one of:
   - `@cloud` — the overnight routine can do it **fully** unattended (synced vault + web only;
     no local data; no outward/irreversible action; no human decision).
   - `@local` — needs Cole's Mac (local data / connectors the cloud can't see).
   - `@human` — needs a Cole decision or an outward/irreversible action.
   Resolve ambiguity **at capture**, not at run time: if a large item is only partly
   cloud-doable, split it — tag the cloud-safe sub-part `@cloud`, the rest `@local`/`@human`.
   Cross-link the wiki/CRM pages it relates to; group under a short subheading.
```

- [ ] **Step 2: Verify the lane requirement and format are documented**

Run: `grep -n "Capture (with a lane)\|@cloud — the overnight routine\|Resolve ambiguity \*\*at capture" AGENTS.md`
Expected: 3 matches.

- [ ] **Step 3: Commit**

```bash
git add AGENTS.md
git commit -m "AGENTS.md: require a lane tag (@cloud/@local/@human) at action-item capture

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 4: Backfill lane tags on existing Open items + reconcile the two drifted items

**Files:**
- Modify: `tasks/index.md`

**Interfaces:**
- Consumes: the `@lane` format from Task 3; the Write-back rules from Task 1.

- [ ] **Step 1: Reconcile last night's drift.** In the `### Sourcing & verification` subheading, both items were completed by the 2026-07-27 run. Flip each `- [ ]` to `- [x]`, append `(done 2026-07-27)`, and move both to the **Done** section (newest at top):
  - `Ingest official Anthropic Claude Code docs to ground single-source (Nate Herk) feature claims` → done note: `grounded [[claude-code-browser-automation]] against official Anthropic Week 28 docs`.
  - `Verify the Auto Dream trigger cadence (community-inferred)` → done note: `verified in [[claude-code-memory]] — ≥24h AND ≥5 sessions, marked plausible-but-unverified`.

- [ ] **Step 2: Add a `@lane` tag to every remaining Open checkbox**, inserting it immediately after `- [ ] ` (or after `- [ ] 💰`/emoji prefixes). Use this mapping (from the Doability rubric):
  - `@cloud` — vault+web research/build with no local data or human decision: e.g. *Prompt max refinement/eval-testing*, *Token max skill*, *Skill max*, *Agent max*, *Improve + general skills*, *Build the source-seeking (MODE B) rung*, *Watch [[agent-hub]]*, *Tune HEALTH_DEBT weights*, *Try an autoresearch loop hands-on (research portion)*.
  - `@local` — needs the Mac / local data: e.g. *Enrich the CRM from message content*, *Gmail pass 2*, *Add YouTube watch history*, *Export Instagram information*, *DIY Plaid export script*, *Extend the @local lane*.
  - `@human` — needs a Cole decision or outward action: e.g. *Data connection (finance app choice)*, *Define the Freedom Number*, *Max the Roth*, *Verify the Roth is invested*, *Move idle checking → HYSA*, *VXUS decision*, *Build a Uship email responder*, *Build a password holder*, *Decide whether to build the Journal pillar*, *Populate the buckets (awaiting Cole to name people)*, *Spotify + concert alerts*.

- [ ] **Step 3: Verify every Open item is tagged and the two items moved**

Run: `awk '/^## Open/{f=1} /^## Done/{f=0} f' tasks/index.md | grep -E "^- \[ \]|^  - \[ \]" | grep -vc "@cloud\|@local\|@human"`
Expected: `0` (no untagged Open checkbox remains).

Run: `awk '/^## Done/{f=1} f' tasks/index.md | grep -c "Auto Dream trigger cadence\|ground single-source (Nate Herk)"`
Expected: `2` (both reconciled items now in Done).

- [ ] **Step 4: Append a `log.md` line** (per AGENTS.md step 4):

Add under a new dated entry: `## [2026-07-27] tasks | Backfilled @cloud/@local/@human lanes on all open action items; reconciled 2 Sourcing & verification items completed by the nightly run.`

- [ ] **Step 5: Commit**

```bash
git add tasks/index.md log.md
git commit -m "tasks: backfill lane tags on all open items; reconcile 2 items done by 07-27 run

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 5: Update `vault-autoresearch` SKILL.md to the new order/invariants

**Files:**
- Modify: `.claude/skills/vault-autoresearch/SKILL.md` (the "Quick start" and "Invariants" sections)

**Interfaces:**
- Consumes: the phase order + branch model from Task 1. Must not restate the loop (points to `program.md`).

- [ ] **Step 1: Replace the `## Quick start` section** with:

```markdown
## Quick start

1. `python3 autoresearch/score.py` — see current debt + the defect list.
2. Follow `autoresearch/program.md`'s six phases in order: **Select → Build →
   Write-back → Self-heal → AutoResearch → PR**.
3. On a build night the whole run stays on the night branch → one morning PR. Stop after
   the PR is opened.
```

- [ ] **Step 2: In the `## Invariants` section, replace the "Self-healing → `main`" bullet** with:

```markdown
- **Build first, heal second.** Action-item build work (Phases 0–2) runs before self-heal
  (Phase 3) and generative work (Phase 4). On a build night, the entire run lives on the
  night branch → one PR; nothing reaches `main` unreviewed. Pure-maintenance nights may
  still commit objective self-heal fixes to `main`.
```

- [ ] **Step 3: Verify the skill points at the new order without restating it**

Run: `grep -n "Select → Build\|Build first, heal second\|program.md" .claude/skills/vault-autoresearch/SKILL.md`
Expected: ≥3 matches; and `grep -c "MODE A loop\|MODE B loop" .claude/skills/vault-autoresearch/SKILL.md` → `0` (it doesn't duplicate program.md's loop steps).

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/vault-autoresearch/SKILL.md
git commit -m "vault-autoresearch skill: reflect 6-phase order + build-first branch model

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 6: Point the nightly cloud routine at the new program.md flow

**Files:**
- No repo files. Uses the `RemoteTrigger` tool (load via `ToolSearch select:RemoteTrigger`).

**Interfaces:**
- Consumes: the finished `program.md` (Tasks 1–5 merged to `main`, since the cloud agent checks out `main`).

- [ ] **Step 1: Locate the recurring nightly routine.**

Call `RemoteTrigger {action: "list"}`. Find the routine whose prompt runs the AutoResearch loop (name contains "Vault AutoResearch" / "nightly", or a `cron_expression` around `0 6 * * *` UTC = ~2am ET). Record its `id`. If paging is needed, follow `next_cursor`. **If no recurring routine exists** (only `send_later` PR check-ins do), note that and create one per the `schedule` skill's Create body shape with `cron_expression: "0 6 * * *"`, repo `https://github.com/ckannam/Second_Brain`, model `claude-sonnet-4-6`.

- [ ] **Step 2: Set the routine's prompt** (via `update`, or as the `create` message) to exactly:

```
Nightly Vault AutoResearch run on ckannam/Second_Brain. Follow autoresearch/program.md exactly, in its six phases and order: Phase 0 Select (read tasks/index.md, pick the cloud-doable items per the Doability rubric — explicit @cloud/@local/@human tag wins, infer if untagged, skip+flag if unsure — and regenerate autoresearch/nightly-queue.md as the night's worklist). Phase 1 Build the selected items top-down, bounded to 2–3, per AGENTS.md, on branch autoresearch/night-<today>. Phase 2 Write results back to tasks/index.md (done → [x] + move to Done; partial → ⏳ progress note; never fabricate completion). Phase 3 Self-heal (MODE A) to lower HEALTH_DEBT, including any defect the build introduced. Phase 4 one MODE B generative proposal. Phase 5 open ONE PR (night branch → main) and stop, then arm an hourly PR check-in. NEVER edit autoresearch/score.py or touch raw/. NEVER take outward/irreversible actions or merge to main. Honor @human/@local lanes — do not attempt them.
```

- [ ] **Step 3: Verify the routine reflects the new prompt**

Call `RemoteTrigger {action: "get", trigger_id: "<id>"}`. Confirm the message content contains `Phase 0 Select` and `Follow autoresearch/program.md`. Relay the routine's `next_run_at` and its `https://claude.ai/code/routines/<id>` URL to Cole.

- [ ] **Step 4: No commit** (cloud-side config). Note completion in the final summary to Cole.

---

### Task 7: Dry-run the selection rubric (final verification)

**Files:**
- None (read-only validation).

**Interfaces:**
- Consumes: merged `program.md` (Task 1) + tagged `tasks/index.md` (Task 4).

- [ ] **Step 1: Dispatch a fresh subagent** (Explore or general-purpose) with this task:

> Read `autoresearch/program.md` and `tasks/index.md`. Acting as Phase 0 only — DO NOT build or edit anything — output: (a) the 1–3 items you would work tonight and why each is cloud-doable, (b) the items you would skip and the exact rubric clause that excludes each. Return just that list.

- [ ] **Step 2: Judge the output**

Expected: the subagent selects only `@cloud`-tagged (or clearly cloud-inferable) items, and correctly excludes every `@local`/`@human` item citing a rubric clause (local data / outward action / human decision). If it picks a `@human` or `@local` item, the rubric wording in `program.md` needs tightening — fix Task 1's rubric text and re-run this task.

- [ ] **Step 3: Record the result** in the final summary to Cole (which items the first real night will likely tackle). No commit.

---

## Self-Review

**Spec coverage:**
- Capture-time lane tagging → Task 3 (AGENTS.md) + Task 4 (backfill). ✓
- Doability rubric (tag→infer→skip) → Task 1 (program.md rubric) + Task 7 (validation). ✓
- 6-phase order (build first) → Task 1 + Task 5 (skill) + Task 6 (routine prompt). ✓
- Write-back (done/partial/never-fake) → Task 1 rules + Task 4 applies them. ✓
- Branch model → Task 1 + Task 5. ✓
- nightly-queue.md as auto-generated artifact → Task 2. ✓
- Cloud routine points at new flow → Task 6. ✓
- Safety / frozen boundaries → Task 1 safety section, enforced in Task 6 prompt. ✓
- Morning PR location → documented in spec; operationalized in Task 6 Phase 5. ✓

**Placeholder scan:** No TBD/TODO; every edit gives exact replacement text and concrete grep/score/subagent verifications.

**Type consistency:** Phase names (`Phase 0 Select` … `Phase 5 PR`), lane tokens (`@cloud/@local/@human`), and the `⏳ progress YYYY-MM-DD` marker are used identically across Tasks 1, 2, 3, 4, 5, 6, 7.
