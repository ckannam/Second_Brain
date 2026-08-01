---
name: token-context-management
description: Use when Cole asks how to manage context, avoid hitting the context limit, keep a Claude Code session efficient, or asks about /compact, CLAUDE.md sizing, sub-agents for context isolation, or compaction hooks. Also triggers on "context is getting long", "session is slow", or "I'm running out of context".
---

# Token & Context Management

Quick-reference skill for keeping Claude Code sessions signal-dense and avoiding context
bloat. Full concept: [[token-context-management]].

## Four levers (in order of effectiveness)

1. **CLAUDE.md (most durable)** — instructions loaded at session start, not consumed by
   conversation. Keep each file **under ~200 lines**; beyond that, adherence degrades.
   Put rules and conventions here. Do NOT put large docs or raw data here.

2. **`/compact`** — triggers a context compaction: the conversation is summarised into a
   shorter form. Use it **proactively** before switching to a very different task; don't
   wait for the window to fill. What's lost: fine-grained tool history. What survives:
   the model's synthesis of what happened.
   - Automate with `PreCompact`/`PostCompact` hooks (see [[claude-code-hooks]]) to
     inject critical reminders into the fresh context after compaction.

3. **Sub-agents for heavy reads** — each [[claude-code-subagents|sub-agent]] gets its
   own context window. If a task requires reading 10+ files or a long tool run, delegate
   it to a sub-agent; the parent thread stays clean.

4. **Read small** — request specific sections rather than whole files; prefer targeted
   reads over broad context dumps. Ask the model to summarise rather than reproduce.

## Auto-memory (across sessions)
Claude writes `~/.claude/projects/<repo>/memory/MEMORY.md` between sessions. First 200
lines / 25KB load automatically; topic files load on demand. Manage with `/memory`.
Keep it trimmed — stale memory adds noise, not signal.

## When to reach for [[claude-managed-agents]]
If context management across many parallel sessions is becoming a bottleneck, consider
CMA — it absorbs compaction, caching, and context-anxiety handling automatically at the
platform level, so individual apps don't have to.

## Quick heuristics
| Symptom | Fix |
|---|---|
| Model ignoring CLAUDE.md rules | File is too long (>200 lines) — trim it |
| Session slow / repeating work | `/compact` now; then put key rules in CLAUDE.md |
| Task needs to read many files | Delegate to a sub-agent |
| Losing state across sessions | Use `/memory` to persist key facts |

Related: [[token-context-management]], [[claude-code-memory]], [[claude-code-hooks]],
[[claude-code-subagents]], [[claude-managed-agents]], [[context-anxiety]].
