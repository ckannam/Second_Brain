---
type: concept
---
# Skills vs Sub-agents

The decision page for the whole skill/agent cluster: when to package work as a
[[claude-code-skills|skill]] versus delegate it to a [[claude-code-subagents|sub-agent]]. The
one-line frame that resolves most cases: **a skill *teaches* the current session; a sub-agent
*staffs* it with a fresh worker.** It's a **context-architecture choice, not a capability
choice** — both can carry the same instructions; what differs is *where the work runs and whose
context pays for it*.

## The core distinction

| | **Skill** | **Sub-agent** |
|---|---|---|
| **What it is** | a packaged, reusable *procedure* (`SKILL.md` + optional refs) the main agent loads **in-context** when a description matches | a *separate delegated agent* (`.claude/agents/*.md`) with its **own fresh context window**; the parent conversation does **not** come along |
| **Context** | runs in the **main** window — its body is added to the current context ([[token-context-management]]) | runs in an **isolated** window — returns only a summary to the parent, keeping heavy work out of the main context |
| **Best for** | a **repeatable procedure** you keep re-explaining (a house style, a build sequence, a checklist) | an **isolatable or parallel** task (a long code review, a deep research sweep) whose intermediate tokens shouldn't pollute the parent |
| **Reuse** | portable knowledge, invoked on demand across sessions | a role you hand a scoped job and get one answer back |
| **Parallelism** | one procedure in the main thread | many can run **concurrently**, each in its own context |

## Reach for a skill when…
- You find yourself **pasting the same instructions** across sessions — that repetition *is* the
  signal (see the [[skill-authoring-playbook]] build discipline).
- The work is a **procedure with a right way to do it** — Claude should follow it, not re-derive it.
- You want the capability **available in-context** to inform the main task as it runs.

## Reach for a sub-agent when…
- The sub-task would **flood the main context** with tokens you don't want to keep (a long review,
  a big log grep, a multi-file research read) — isolation is the whole point.
- You need **several independent tracks at once** — fan-out that a single linear context can't hold.
- You want a **clean-slate perspective** (an adversarial reviewer that hasn't seen your reasoning).

## They compose — it's a ladder, not an either/or
The two aren't rivals; they stack. A sub-agent can **invoke skills** inside its own context, and a
skill's body can tell the main agent **when to spin up a sub-agent**. The reusability ladder runs:
inline instruction → `CLAUDE.md` standing convention → **skill** (reusable procedure) →
**sub-agent** (isolated context) → **[[claude-code-agent-teams|agent team]]** (many coordinated
sub-agents) → Claude Managed Agents (server-hosted). Climb only as far as the job needs — the
[[orchestrate-agents]] decision ladder is the full walkthrough, and [[claude-code-worktrees]]
covers the file-isolation layer when parallel agents would otherwise collide.

## The trap to avoid
Don't reach for a sub-agent just because a task *feels* big. If it's a **repeatable procedure**,
a skill is cheaper and more reliable (no context hand-off, no summary round-trip). Sub-agents earn
their overhead only when you genuinely need **context isolation or parallelism** — otherwise the
delegation is pure cost. Symmetrically, don't cram a genuinely heavy, one-off, context-polluting
job into a skill that runs in the main window.

Related: [[claude-code-skills]] (the concept/hub) · [[skill-authoring-playbook]] (authoring craft) ·
[[claude-code-subagents]] · [[claude-code-agent-teams]] · [[orchestrate-agents]] ·
[[token-context-management]] · [[master-claude-code-skills-28min]] · [[build-sell-claude-code-course]].
