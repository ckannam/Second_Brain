---
name: claude-code-prompt
description: Use when Cole wants an optimized prompt for Claude Code — building/editing a codebase, file operations, automation, or agentic multi-step technical work in a repo — or says "write me a Claude Code prompt." For quick interactive work use claude-chat-prompt; for delegated async knowledge work use claude-cowork-prompt.
---

# Claude Code Prompt Architect

Turns a task into an **optimal prompt for Claude Code** — the agentic coding tool that reads/edits
files, runs commands, and works in a repo. Claude Code is **outcome-oriented**: give it a goal, the
context, and a way to *verify*. Grounded in [[prompt-engineering-playbook]], [[outcome-oriented-agents]],
[[html-over-markdown-specs]]; tailored via [[cole|profile]].

## Process
1. **Understand the task first** — the concrete goal (build X / fix Y / automate Z), which repo/files,
   and how success is checked. Ask **1–3 clarifying questions only if genuinely unclear**.
2. **Pull context** — the target repo's conventions (e.g. its `AGENTS.md`/`CLAUDE.md`), relevant files,
   and any Cole-specific preferences ([[cole|profile]]).
3. **Apply hygiene** — clear sections; an **output/verification contract**; don't over-constrain.
4. **Shape it for Code** (below) and **output a ready-to-paste prompt**.

## The Claude Code prompt shape (goal + context + verification)
- **Goal** — what to build or fix, stated as an outcome.
- **Where / context** — repo, key files/dirs, conventions to follow, relevant existing patterns.
- **Constraints & guardrails** — what **not** to touch, keep changes minimal/reversible, style to match.
- **How to verify** — the tests/commands/expected behavior that prove it works (Code thrives on a
  verification loop — give it one, or ask it to write the test first).
- **Deliverable** — commit/branch/PR expectations; explain-then-do if the change is risky.
Prefer **outcome + verification** over step-by-step micromanagement — capable agents do better with a
goal and a way to check themselves.

## Output
Return the prompt in a fenced block, then **one line** on the verification step + any file/convention
Cole should point it at. If it's really a thinking task or async delegation, route to the sibling skill.

## Common mistakes
- Goal without a verification path. · Not naming the repo's conventions file. · Over-scripting steps
  instead of stating the outcome. · No guardrails on what's off-limits. · Forgetting the commit/PR expectation.
