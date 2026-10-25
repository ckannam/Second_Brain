---
type: concept
category: Claude Mastery
created: 2026-10-25
---

# Prompt-architect skills (the surface-routing family)

The three vault skills that turn a task into an **optimal prompt for one arm of Claude** —
shipped 2026-07-26 as the "prompt max" track ([[Claude Mastery]]) and living in
`.claude/skills/`:

| Skill | Surface | When it fires |
|---|---|---|
| `claude-chat-prompt` | **Claude.ai chat** — interactive thinking partner | quick, iterative work: thinking, writing, analysis, research, Q&A, artifacts |
| `claude-cowork-prompt` | **Claude Cowork** — async delegation | hand-off / background knowledge work reviewed later; scheduled or recurring tasks |
| `claude-code-prompt` | **Claude Code** — agentic repo work | building/editing a codebase, file ops, automation, multi-step technical work |

This page is the **concept** the three skills instantiate — [[prompt-engineering-playbook]] is
the general *theory* of prompting; this is the vault-specific *system* for choosing and shaping
a prompt per surface. The dedicated audit of the family lives in [[skill-audits-2026]]
(2026-10-25: all three judged 6/6 structurally clean — the cleanest-authored family in the vault).

## The surface-routing rule

The three skills share one intent — "write me an optimal prompt" — so they're disambiguated by
**where the prompt will run**, not what it's about. Each skill's description carries explicit
**sibling cross-redirects** ("for delegated async work use `claude-cowork-prompt`; for coding/repo
work use `claude-code-prompt`") — the [[skill-trigger-tuning]] pattern for a cluster of near-twins:

- **Interactive, you're in the loop** → `claude-chat-prompt`.
- **Delegated, you'll review the result later** → `claude-cowork-prompt`.
- **In a repo, outcome is verifiable by tests/commands** → `claude-code-prompt`.

## The shared four-step method

Every one of the three runs the same spine before specializing:

1. **Understand the task first** — objective, real audience/use, constraints, desired output
   shape. Ask 1–3 clarifying questions *only if genuinely unclear*.
2. **Pull Cole's context** — read `[[cole|profile]]` (local-only — see below) + relevant vault
   pages, and fold in only what the task needs.
3. **Apply hygiene** — separate role / context / task / constraints / **output contract**; don't
   over-constrain a capable model ([[bitter-lesson]]).
4. **Shape for the surface** (below) and emit a **ready-to-paste** block + one line on why it's
   shaped that way and what to tweak.

## Where the surfaces diverge

The specialization — the reason three skills beat one — is the *prompt shape*:

- **Chat** leaves room to iterate: role/framing, one task, minimum context, output contract, and
  an explicit *invite to iterate*. Don't front-load like a spec.
- **Cowork** **front-loads everything** — it can't ask mid-run: objective + concrete deliverable,
  why/context for judgment calls, inputs/resources/connectors to grant, a **definition of done**,
  exact output format, and scope guardrails ("no irreversible/outward action without flagging").
- **Code** is **outcome + verification**: goal as an outcome, where/conventions (point it at the
  repo's `AGENTS.md`/`CLAUDE.md`), guardrails on what not to touch, and a **way to verify** (tests/
  commands — or ask it to write the test first). Grounded in [[outcome-oriented-agents]] and
  [[html-over-markdown-specs]]. Prefer outcome over step-by-step micromanagement.

## Notes & open edge

- **Local-only grounding.** All three ground in `[[cole|profile]]`, which is `profile/` —
  **gitignored / local-only** (personal identity data, invisible to the cloud lane). Correct home
  for it, but it means the cloud lane can audit these skills' *structure* yet can't fully exercise
  their Cole-tailoring; the full behavior only runs on Cole's Mac.
- **Evals (§5 gap).** The family has no eval harness — the open "Prompt max — eval-test the 3
  prompt-architect skills" task ([[tasks/index]]). A shared eval set (one task, three surfaces →
  the right skill fires with the right shape) is sketched in [[skill-audits-2026]]; running it
  needs Cole + a live baseline. The how-to is [[skill-evals-playbook]].

Related: [[prompt-engineering-playbook]] · [[the-prompting-playbook]] · [[skill-authoring-playbook]] ·
[[skill-audits-2026]] · [[skill-trigger-tuning]] · [[outcome-oriented-agents]] ·
[[html-over-markdown-specs]] · [[claude-code-skills]] · [[Claude Mastery]].
