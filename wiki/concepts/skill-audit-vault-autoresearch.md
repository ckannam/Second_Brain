---
type: concept
created: 2026-10-04
---

# Skill audit — `vault-autoresearch` (2026-10-04)

The third skill run through the [[skill-authoring-playbook]] checklist, after
[[skill-audit-worked-example|startup-radar]] and [[skill-audit-networking-prep|networking-prep]].
Format mirrors the reusable template in [[skill-audit-worked-example]]. It's the worked example the
*Improve + general skills* task ([[Claude Mastery]]) asked for — "more skill iterations."

**Subject chosen:** `vault-autoresearch` — the loop's **own driver skill**, at 40 lines the leanest
non-prompt skill in the vault, and un-audited until now. Auditing the skill that runs *this very
audit* is the right meta-check: if the loop's entry point has drifted, every nightly run inherits the
drift. Only its `SKILL.md` is git-tracked and it touches nothing personal.

## The audit

For each playbook section: **Verdict** (✅ clean · 🟡 recommend · 🔧 fixed) → finding → action.

### §1 — Description is the trigger surface — ✅
Third-person, packs *what it does* ("run the vault's self-healing or AutoResearch loop") **and** a
rich trigger set ("heal the wiki", "run autoresearch", "improve the vault", "lower the health debt",
the overnight/scheduled run, the `/vault-autoresearch` command). Crucially it carries an explicit
**disambiguation clause** — "For answering a question from the wiki use `wiki-query` instead; for
writing wiki content follow `AGENTS.md`" — which steers Claude away from the two sibling skills it is
most likely to be confused with. That's the playbook's "be pushy, but route correctly" done well. No
action.

### §2 — Progressive disclosure keeps it cheap — ✅ (exemplary)
The single best progressive-disclosure example in the vault. The 40-line body states only invariants
and a 3-step quick start, then **delegates the entire loop to `autoresearch/program.md`** ("read it
and follow it exactly"). `program.md` is read on demand via bash — **zero context cost until the loop
actually runs**. This is the metadata → body → reference tiering the playbook prescribes, applied
perfectly: the heavy, frequently-edited loop logic lives in the file the human tunes, not baked into
the skill. No action.

### §3 — Be concise (assume Claude is smart) — ✅
The body explicitly refuses to restate its sources: "Do not restate either here." It's the shortest
path from trigger to the authoritative instructions. No padding. No action.

### §4 — Match degrees of freedom to task fragility — ✅
Correctly **low-freedom / narrow bridge**: a metric-ratcheted loop that must not be improvised. The
skill hard-codes the non-negotiables (never edit `score.py`, keep-or-revert on the metric, the
two-lane auto-merge/review split, heal-on-`main`-then-build-on-branch) and otherwise says "follow
`program.md` exactly." For a loop where a wrong move can push unreviewed content to `main`, scripting
the invariants and delegating the rest is the right fragility match. No action.

### §5 — Build evals first, then iterate — ✅ (the one skill that already passes)
The genuinely notable finding. Every prior audit logged §5 as the 🟡 gap — no evals exist
([[skill-audit-worked-example|startup-radar]], [[skill-audit-networking-prep|networking-prep]]).
`vault-autoresearch` is the **exception**: its eval is built in. The frozen `autoresearch/score.py`
emitting **HEALTH_DEBT** *is* the objective signal the playbook's §5 demands — every change is
kept only if the number drops (git as the ratchet). The skill doesn't need a bolted-on eval harness
because measuring-before-keeping is its whole operating model. This is [[evals-for-taste]] and the
[[vault-autoresearch]] ratchet realized as a skill. No action — and a template data point: a skill
whose core loop is already metric-gated satisfies §5 by construction.

### §6 — Anti-patterns — ✅
No time-sensitive facts baked in (the weekly-Sunday cadence gate correctly lives in `program.md`, not
restated here — delegation, not omission). No deep/absolute paths: both script references use the
vault-relative `autoresearch/score.py`. Terminology is consistent with `program.md` and `AGENTS.md`
(HEALTH_DEBT, MODE A/B, fast-track/review lanes). No voodoo constants, no vague helper names. Clean.

## Verdict

`vault-autoresearch` is a **clean, exemplary skill** — 6 / 6 sections pass, 0 recommendations, 0
fixes. That is the honest result for a mature, tightly-scoped skill, and the point the
[[skill-audit-worked-example]] template makes: a good audit confirms health and resists manufacturing
churn. Two things make it a worthwhile data point rather than a rubber stamp: it is the **best
progressive-disclosure example** in the vault (§2) and the **only skill that already satisfies §5**,
because its eval is the HEALTH_DEBT ratchet it runs.

## Audit scoreboard (running)

Three skills now carry a worked audit against the playbook:

| Skill | Lines | Clean | Recommend | Fixed | Headline |
|---|---|---|---|---|---|
| [[skill-audit-worked-example\|startup-radar]] | 198 | 3 | 2 | 1 | Step-7 path (drift re-applied 2026-10-04) |
| [[skill-audit-networking-prep\|networking-prep]] | 119 | 4 | 2 | 1 | step-numbering fix |
| vault-autoresearch | 40 | 6 | 0 | 0 | exemplary; §5 satisfied by HEALTH_DEBT |

Pattern across three audits: mature skills mostly pass; the real issues are **structural drift**
(a path, a step number, a fix that never landed), never the description or logic. §5 (evals) is the
recurring gap — satisfied only where a skill is metric-gated by construction.

Related: [[skill-authoring-playbook]] · [[skill-audit-worked-example]] · [[skill-audit-networking-prep]] ·
[[vault-autoresearch]] · [[evals-for-taste]] · [[token-context-management]] · [[claude-code-skills]] ·
[[Claude Mastery]].
