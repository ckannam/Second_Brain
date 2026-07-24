---
type: entity
category: tool
---

# Codex

OpenAI's coding agent (the app [[matt-wolfe]] uses as his LLM agent for the
[[second-brain-system]]). Points it at the [[obsidian]] vault folder as a project, then
prompts it to build/maintain the wiki, journal, and CRM.

Features used in the build: chat/query against the vault, manual and prompted edits to
`AGENTS.md`, and **automations** (scheduled recurring tasks — e.g. hourly processing of
new `raw/` files plus a git push to a private backup repo).

> Note: in this vault the canonical schema is `AGENTS.md` (vault root); `CLAUDE.md` points
> to it, so both a Codex session and Claude Code follow the same rules.

Source: [[build-an-ai-second-brain-matt-wolfe]].

## Codex + Claude Code (July 2026)

OpenAI released an official **Codex plugin for [[claude-code]]**. Best pattern: use Codex
as an **adversarial reviewer** of Claude/Opus's work, then feed the review back to Opus to
fix — a two-model quality loop. Benchmarks pit [[opus-4-6]] vs GPT 5.4.
Source: [[codex-plugin-for-claude-code]]. Also used as a terminal agent in the
[[obsidian-vault-deep-dive-emai|Easy Machine AI Obsidian system]].

Karpathy's [[autoresearch]] is agent-agnostic — the README says spin up "your Claude/Codex or
whatever" in the repo; [[david-andre]]'s build uses Codex (GPT-4.6) as the debugger alongside
[[claude-code]] for the loop.
