---
name: claude-cowork-prompt
description: Use when Cole wants an optimized prompt to delegate a task to Claude Cowork — async/background knowledge work he'll review later, or a scheduled/recurring task — or says "write me a Cowork prompt." For quick interactive work use claude-chat-prompt; for coding/repo work use claude-code-prompt.
---

# Claude Cowork Prompt Architect

Turns a task into an **optimal delegation brief for Claude Cowork** — *async* knowledge work you hand
off and review later (and scheduled/recurring tasks). Because it runs without you in the loop, the
prompt must **front-load everything**; you can't easily course-correct mid-run. Grounded in
[[prompt-engineering-playbook]]; tailored via [[cole|profile]].

## Process
1. **Understand the task first** — objective, the exact **deliverable**, and what "done" looks like.
   Ask **1–3 clarifying questions only if genuinely unclear**; Cowork can't ask mid-run, so resolve
   ambiguity *now*.
2. **Pull Cole's context** ([[cole|profile]] + relevant vault pages) and name the **inputs/resources/
   connectors** the task needs (files, apps, data).
3. **Apply hygiene** (role/context/task/constraints/output-contract, don't over-constrain).
4. **Shape it as a delegation brief** (below) and **output a ready-to-paste prompt**.

## The Cowork prompt shape (brief a capable teammate on a whole project)
- **Objective & deliverable** — the outcome + the concrete artifact to produce.
- **Why / context** — enough for good judgment calls without you there.
- **Inputs & resources** — what to use (docs, connectors, data), and what it may access.
- **Approach** — steps or method *if you have a preference*; otherwise let it plan.
- **Definition of done / success criteria** — the checklist it should satisfy.
- **Output format** — exactly how to deliver (doc structure, file, summary + artifact).
- **Scope & guardrails** — boundaries, what **not** to do, no irreversible/outward actions without flagging.

## Output
Return the brief in a fenced block, then **one line** on the success criteria to double-check + any
resource/connector Cole must ensure is available. If it's really interactive or coding, route to the
sibling skill.

## Common mistakes
- Leaving ambiguity it can't resolve async. · No definition of done. · Not specifying the deliverable
  format. · Forgetting to grant/name the resources it needs. · Assuming it can iterate with you mid-run.
