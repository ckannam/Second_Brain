# Vault AutoResearch — loop instructions (`program.md`)

The `program.md` of Karpathy's AutoResearch, applied to this vault. This is the
**loop's brain** — the human edits it; the loop follows it. It is a
"super-lightweight skill" in Karpathy's phrasing. The `wiki-query` skill and
`AGENTS.md` remain the source of truth for *how to write the wiki*; this file only
governs the *improvement loop*.

## The metric

`autoresearch/score.py` emits **HEALTH_DEBT** — one scalar, **lower is better**
(0 = clean). It is the vault's `val_bpb`. Run it with `--json` to drive the loop.

## The ratchet (git)

Every iteration either **lowers HEALTH_DEBT (keep the commit)** or **does not
(revert)**. Git is the ratchet and the rollback — a bad unattended night is one
`git reset` away. This is why the vault is a repo.

## Two modes, one machinery

- **MODE A — self-healing (autonomous, commits to `main`).** Drive HEALTH_DEBT
  down by fixing *objective* defects. Safe to run unattended.
- **MODE B — autoresearch / generative (proposes, never self-merges).** Grow the
  wiki's coverage and connectivity — new pages, sources to ingest, deeper
  synthesis. Because "is this good knowledge?" is subjective (Karpathy's failure
  mode), MODE B works on the `autoresearch/pending` branch for **human review**,
  never on `main`.

## MODE A loop (self-healing)

1. `python3 autoresearch/score.py --json` → record `health_debt` as **baseline**.
2. Pick the single **highest-weight** defect (orphans → missing_from_index →
   stale_claims). One change per iteration, like AutoResearch edits one file.
3. Fix it in the wiki, following `AGENTS.md`:
   - orphan → add the missing reciprocal link(s) from pages that should reference it.
   - missing_from_index → add the page to `index.md` (or `crm/index.md`) with a
     one-line summary in the right category.
   - stale_claim → mark the superseded claim (e.g. note the current flagship) per
     the freshness rule; never silently rewrite a source.
4. Re-run `score.py`.
5. **Improved?** `git add -A && git commit`. **Equal or worse?** `git checkout -- .`
   (throw the change away — do not keep it "for reference").
6. Append a row to `autoresearch/results.tsv`
   (`ts / mode / target / debt_before / debt_after / status / note`).
7. Repeat until HEALTH_DEBT is 0 or no *safe, objective* fix remains.

## MODE B loop (generative — review-gated)

1. `git switch -c autoresearch/pending` (or reuse it).
2. Propose ONE improvement: a genuinely new page a source warrants, a stub worth
   filling, or a source to ingest — applying `AGENTS.md`'s **new-page test** and
   **simplicity criterion** (never farm thin pages to inflate counts; a change
   that adds clutter for a tiny gain is a revert).
3. Commit on the branch. Do **not** merge. Leave it for the human's morning review
   — the "log of experiments you wake up to."

## NEVER STOP (for scheduled/unattended runs)

Don't ask the human whether to continue — they may be asleep. When MODE A reaches
HEALTH_DEBT 0, make **one** MODE B proposal on the review branch, log it, and end
the run. Next run resumes from the current state via `score.py` + `results.tsv`
(the cross-run memory).

## Safety — the frozen boundaries

- **NEVER edit `autoresearch/score.py`** — the frozen evaluator. Changing the
  metric to lower the number is cheating, not healing. Only a human retunes it.
- **NEVER modify anything under `raw/`** — immutable sources.
- MODE A → `main`; MODE B → `autoresearch/pending` (review). Never auto-merge B.
- Pair unattended runs with Auto Mode deny-rules for `raw/**` and
  `autoresearch/score.py`.
