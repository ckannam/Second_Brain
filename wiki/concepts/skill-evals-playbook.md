---
type: concept
created: 2026-10-04
---

# Skill-evals playbook

The concrete, vault-specific answer to the question every skill audit ends on: **"§5 — no evals
exist; write ~3."** [[skill-authoring-playbook]] §5 says *build evals first, then iterate*;
[[evals-for-taste]] explains *why* evals beat vibes and *what* a grader is. Neither says **how to
write an eval for one of this vault's own skills.** This page owns that — the format, the grader
choice, a worked triplet per skill type, and the run loop. It's the missing rung between the
checklist and the three audits ([[skill-audit-worked-example|startup-radar]],
[[skill-audit-networking-prep|networking-prep]], [[skill-audit-vault-autoresearch]]), all of which
logged §5 as the recurring gap.

> **This is synthesis** — a method assembled from the vault's eval sources applied to its skills,
> not a transcript of one source. Grounded in [[evals-for-taste]] (graders, rubrics, replayability)
> and [[eval-driven-model-selection]] (build your own, don't trust public benchmarks), and modeled
> on the vault's own working eval, the frozen `score.py` / HEALTH_DEBT ratchet ([[vault-autoresearch]]).

## The eval triplet (the unit)

Write each eval as three fields — the same shape the audits already use:

- **`query`** — the trigger input a real run would receive ("run the startup radar", a person's name).
- **`files`** — the vault state the eval assumes (which `crm/`, `startup-tracker/`, or `wiki/` files
  exist, and with what frontmatter). Evals are only meaningful against a fixed input state.
- **`expected_behavior`** — the *observable, checkable* outcome, phrased so pass/fail is unambiguous
  ("a `startup-tracker/companies/<name>.md` is written with `lane: health-bio-ai`", not "a good note").

Three to five triplets per skill is the right starting budget — enough to cover the fragile parts
(the "narrow bridge" from [[skill-authoring-playbook]] §4), not so many that upkeep rots.

## Pick the grader to match the output

Straight from [[evals-for-taste]]'s two grader families, mapped to what vault skills actually emit:

- **Code-based grader (deterministic)** — when the expected behavior is *structural*: a file exists at
  a path, frontmatter has a required field, an enum value is legal, a dedup skip fired, a path is
  relative. Cheap, fast, brittle-but-sufficient. **Most skill evals are this** because most skill
  outputs are files with schemas (this is also why the vault's own eval, `score.py`, is code-based).
- **Model-based grader ([[llm-as-judge]])** — when the expected behavior is *taste*: "the Section-3
  questions are specific to the person's actual role," "the angle is honest, not hype." Encode the
  taste as a short rubric the judge applies. Use sparingly — reserve it for the genuinely subjective
  claims a regex can't catch.

Rule of thumb: **try to write a code-based grader first.** If you can't phrase the check
deterministically, that's the signal you need a rubric — or that the `expected_behavior` is still too
vague to be an eval at all.

## Worked triplets (drawn from the real audits)

**`startup-radar`** (file-emitting, mostly code-graded):
1. `query`: a sweep surfaces a robotics-only company · `files`: clean tracker · `expected`: it is
   **dropped** (no note written) — lane filter rejects `other`. *(code: assert no new file.)*
2. `query`: a company with an existing `status: passed` note re-appears · `files`: that note exists ·
   `expected`: **skipped**, not re-surfaced. *(code: assert file count unchanged.)*
3. `query`: a Baltimore health-AI seed co · `files`: clean tracker · `expected`: note written with
   `geo_fit: strong` **and** `lane: health-bio-ai`. *(code: assert frontmatter values.)*

**`networking-prep`** (file + taste, mixed grader):
1. `query`: a person whose `crm/<Name>.md` exists · `expected`: a `crm/prep/<Name>.md` is written and
   cross-links back to the CRM record. *(code: assert file + backlink.)*
2. `query`: same · `expected`: the pitch section names ≥1 proof-point drawn from the proof-point bank.
   *(code: assert overlap with the bank.)*
3. `query`: same · `expected`: Section-3 questions name the person's **actual** employer/role, not a
   generic "your industry." *(model-judge: rubric on specificity.)*

**`vault-autoresearch`** (already has its eval): its `expected_behavior` is "HEALTH_DEBT is strictly
lower, else the change is reverted" — checked by `score.py`. This is the template: a skill whose core
loop is metric-gated **is** eval-covered (see [[skill-audit-vault-autoresearch]] §5).

## The run loop (keep-or-revert, like the vault itself)

1. Fix the input `files` to a known state (a tmp vault or a committed fixture) so runs are replayable
   — the [[evals-for-taste]] "replayable over real projects" idea, scaled down.
2. Run the skill against each `query`.
3. Grade: code-based assertions first, the model-judge rubric for the taste triplets.
4. A change to the skill is kept only if the eval score holds or rises — the exact **keep-or-revert
   ratchet** [[vault-autoresearch]] runs on HEALTH_DEBT. Evals are a skill's private HEALTH_DEBT.

## When *not* to write evals

Honoring [[skill-authoring-playbook]] §3 (assume Claude is smart) and [[token-context-management]]
(context is a public good): a tiny, stable, low-freedom skill with no file output and an obvious
single behavior (e.g. the prompt-architect skills, which emit prose for a human to read) earns little
from a formal harness — a single golden-output spot-check is enough. Spend the eval budget where a
**silent** regression is possible: skills that write files, dedup, filter, or route, where a wrong
output looks plausible and ships unnoticed.

Related: [[skill-authoring-playbook]] · [[evals-for-taste]] · [[eval-driven-model-selection]] ·
[[llm-as-judge]] · [[vault-autoresearch]] · [[skill-audit-worked-example]] ·
[[skill-audit-networking-prep]] · [[skill-audit-vault-autoresearch]] · [[token-context-management]] ·
[[claude-code-skills]] · [[Claude Mastery]].
