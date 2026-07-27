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
