# Vault AutoResearch — loop instructions (`program.md`)

The **loop's brain** — the human edits it; the loop follows it. `AGENTS.md` is the
source of truth for *how to write the wiki*; this file governs the *build +
improvement loop*. Karpathy's AutoResearch, applied to this vault.

## Cadence gate — WEEKLY (scheduled runs; read this first)

**Scheduled/unattended runs execute the full loop once a week, on SUNDAY (ET) — not nightly.**
Changed 2026-08-07 (daily runs piled up `autoresearch/night-*` branches faster than they could be
reviewed/merged).

**First action of every *scheduled* run:** check the day (`TZ=America/New_York date +%u` → `7` = Sunday).
- **Sunday →** run all phases below in order (the weekly build + heal + PR).
- **Any other day →** **no-op night**: do **not** run Phase 0–5, do **not** fork a night branch, do
  **not** open a PR. Exit immediately. (If a scheduled session still spawns on a non-Sunday, this gate
  makes it a clean no-op so no branch is ever created off-schedule.)

**Manual runs are exempt.** When a human invokes the loop directly (the `vault-autoresearch` skill /
"run autoresearch" / `/vault-autoresearch`), run in full **regardless of the day** — the gate governs
only the unattended schedule. Everywhere below, "nightly" means **"on the weekly Sunday run."** The
`night-YYYY-MM-DD` branch name is unchanged (dated to that Sunday) → ~1 branch/week instead of ~7.

## The weekly order (two lanes: heal-then-build)

The run has two lanes, split by whether the output is **objectively verifiable by
`score.py`**:

- **Fast-track lane → auto-merges to `main`.** Score-verified *structural* self-heal:
  clearly positive, so it lands directly.
- **Review lane → one morning PR.** New *content* (build + generative): truth isn't
  score-checkable, so the human reviews before it reaches `main`.

**Heal what already exists on `main`; build new work on the branch for review.** Healing
pre-existing debt first (before the branch forks) keeps the auto-merged heals cleanly
separate from the build the human is reviewing.

- **Phase 0 — Select & baseline.** Read `tasks/index.md` Open items; select the ones
  doable unattended (see Doability rubric). **Regenerate `autoresearch/nightly-queue.md`**
  (what was picked; one line each on why the rest were skipped). Run
  `python3 autoresearch/score.py --json`; **record the baseline HEALTH_DEBT AND the
  defect list** — this is the *pre-existing* debt set (used in Phase 3 to tell
  pre-existing debt from build-introduced debt).
- **Phase 1 — Heal on `main` (fast-track / auto-merge).** MODE A structural self-heal
  against `main` for the Phase-0 pre-existing defect set. Each fix that is **purely
  structural** and **strictly lowers HEALTH_DEBT** → commit to `main` and push
  (fast-forward only; see the auto-merge guards in MODE A). This is the score-verified
  "clearly positive" lane.
- **Phase 2 — Build (branch).** Fork `autoresearch/night-YYYY-MM-DD` from the healed
  `main`. Work selected items **top-down, bounded (≤2–3/night)**, per `AGENTS.md`. Web
  tools (WebSearch/WebFetch) + synced vault only. **Review lane — never auto-merges.**
- **Phase 3 — Write-back + build-heal (branch).** Update `tasks/index.md` (see Write-back
  rules). Then MODE A again for any **build-introduced** debt (defects *not* in the
  Phase-0 baseline set); these commit to the **branch** — they ride the PR with the build
  that caused them.
- **Phase 4 — AutoResearch (MODE B, branch).** One generative enrichment proposal. Branch
  only.
- **Phase 5 — PR.** Open one morning PR (night branch → `main`) for the build +
  build-heal + generative, and stop. A pure-maintenance night (no build) may have nothing
  to PR — that's fine; the Phase-1 heals already landed on `main`.

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
**infer** against the rubric; **when unsure → skip and flag** (note why in the PR). An explicit `@cloud` tag means the item is already cleared for unattended build — the morning-PR merge is its human sign-off, so the "no human decision" clause never disqualifies a tagged `@cloud` item. An
item partly doable → do the cloud-safe part, leave the rest as a `⏳ progress` note.

## Write-back rules (Phase 2)

- **Fully done** → flip `- [ ]` to `- [x]`, append `(done YYYY-MM-DD)`, move it to the
  **Done** section (newest at top), per `AGENTS.md`. Never delete history.
- **Partially advanced** → leave `- [ ]` open, append an indented
  `⏳ progress YYYY-MM-DD: did X; remaining Y` line.
- **Never mark done what was not finished.** If completion can't be verified, it isn't done.

## MODE A — self-healing (Phases 1 & 3)

Runs twice: **Phase 1** against `main` for pre-existing debt (auto-merge lane), **Phase 3**
against the branch for build-introduced debt (rides the PR). The iteration loop is identical;
only *where the commit lands* differs.

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

### Auto-merge guards (Phase 1 fast-track lane only)

A MODE A commit may land on `main` directly **only when all hold** — otherwise move the fix
to the night branch and let it ride the PR:

- **Structural only.** The change edits `[[links]]`, `index.md` entries, reciprocal
  backlinks, or stale-claim markers. **No net-new page, no new factual prose/claim** — those
  can't be truth-checked by `score.py` and belong in the review lane.
- **Strict score drop.** `score.py` HEALTH_DEBT is *strictly lower* after the fix (the
  existing ratchet). Equal-or-worse was already discarded in step 5.
- **Clean apply.** Commit to `main` and `git push` as a fast-forward. If the push is
  rejected (main moved) or a merge/conflict would be needed, **do not force** — re-target the
  fix onto the night branch and note it in the PR. (Divergence is unlikely: the local Stop
  hook keeps `main` current and the run is at 2 AM ET.)
- **Pre-existing debt.** The defect is in the Phase-0 baseline defect list. Build-introduced
  debt is Phase 3 (branch), not this lane.

## MODE B — autoresearch / generative (Phase 4)

Propose ONE improvement: a genuinely new page a source warrants, a stub worth filling, or
a source to ingest — applying `AGENTS.md`'s **new-page test** and **simplicity criterion**
(never farm thin pages to inflate counts). Commit on the branch. **Always the review lane —
never auto-merges** (generated content is exactly the "uncertain" case the PR exists for).

## Branch model

- **Fast-track lane → `main` (auto-merge).** Phase-1 MODE A structural heals that pass the
  auto-merge guards land on `main` directly, every night. Score-verified and clearly
  positive — no PR needed.
- **Review lane → morning PR.** Phase-2 build, Phase-3 write-back + build-heal, and Phase-4
  generative live on the night branch → **one morning PR**. The Action Items board updates on
  `main` only when the human **merges**. New/generated content never reaches `main`
  unreviewed.
- **Pure-maintenance nights** (no cloud-doable build): only the fast-track heals land on
  `main`; the branch may carry just one MODE B proposal (or nothing).

## NEVER STOP (for scheduled/unattended runs)

Don't ask the human whether to continue — they may be asleep. Run all phases in order, then
open the PR and end. Next run resumes from the current state via `tasks/index.md`,
`score.py`, and `results.tsv` (the cross-run memory).

## Safety — the frozen boundaries

- **NEVER edit `autoresearch/score.py`** (the frozen evaluator) or modify anything under `raw/`.
- **NEVER take outward/irreversible actions** — no email/messages, no spending.
- **The `main` boundary has exactly ONE exception:** the Phase-1 fast-track lane, and *only*
  when every auto-merge guard holds (structural-only, strict score drop, clean fast-forward,
  pre-existing debt). Everything else — build, generated content, anything not score-verified
  — reaches `main` **only via the human-merged PR.** New factual prose never auto-merges.
- **Honor `@human` / `@local` lanes strictly** — never attempt them in the cloud.
- **Never fabricate completion.**
- All new/generated content is reviewable in the morning PR before it reaches `main`.
- Pair unattended runs with Auto Mode deny-rules for `raw/**` and `autoresearch/score.py`.
