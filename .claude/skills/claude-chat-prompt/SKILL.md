---
name: claude-chat-prompt
description: Use when Cole wants an optimized prompt to paste into the Claude.ai chat app — for thinking, writing, analysis, research, synthesis, Q&A, or artifacts — or says "write me a Claude chat prompt." For delegated async work use claude-cowork-prompt; for coding/repo work use claude-code-prompt.
---

# Claude Chat Prompt Architect

Turns a task into an **optimal prompt for the Claude.ai chat app** (interactive thinking partner:
writing, analysis, research, Q&A, artifacts). Grounded in [[prompt-engineering-playbook]] /
[[the-prompting-playbook]]; tailored to Cole via [[cole|profile]].

## Process
1. **Understand the task first.** Nail the objective, the real audience/use, constraints, and the
   *desired output shape*. Ask **1–3 clarifying questions only if genuinely unclear** — otherwise proceed.
2. **Pull Cole's context** when it sharpens the prompt: read [[cole|profile]] and the relevant vault
   pages (his role, voice, goals) and fold in only what the task actually needs.
3. **Apply hygiene** (from the playbook): separate **role / context / task / constraints / output
   format** with clear headers or XML tags; don't over-constrain a capable model; give an **output
   contract** (format, length, structure).
4. **Shape it for chat** (see below) and **output a ready-to-paste prompt**.

## The chat prompt shape (interactive — leave room to iterate)
- **Role / framing** — who Claude is being for this ("You are a sharp editor…").
- **Task** — the one clear objective.
- **Context** — the minimum background it needs (incl. relevant Cole-context).
- **Output contract** — format, length, structure; an example of "good" if taste matters.
- **Invite iteration** — "ask me anything unclear before starting" when the task is open-ended.
Chat is conversational, so *don't* front-load like a spec — be specific about the deliverable but
leave room to refine in follow-ups.

## Output
Return the prompt in a fenced block (ready to copy), then **one line** on why it's shaped that way +
what Cole might tweak. If the task is really coding or long async delegation, say so and point to the
sibling skill.

## Common mistakes
- Vague deliverable (no output contract). · Dumping context the task doesn't need. · Over-scripting a
  task that's better handled interactively. · Forgetting to use what the vault already knows about Cole.
