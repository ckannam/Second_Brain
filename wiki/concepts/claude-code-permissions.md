---
type: concept
updated: 2026-07-26
---
# Claude Code Permissions

Controls what [[claude-code]] may do without asking. The community framing is "three
postures" (ask / auto / bypass) — [[claude-code-auto-mode-permissions]] (Nate Herk) —
but official docs show **six modes** (see below).
Official source: [Configure permissions](https://code.claude.com/docs/en/permissions) ·
[Permission modes](https://code.claude.com/docs/en/permission-modes).

## The six permission modes

| Mode | What runs without asking |
|---|---|
| `default` / Manual | Read-only operations only |
| `acceptEdits` | Reads + file edits + common filesystem commands |
| `plan` | Reads + classifier-approved commands (no source edits) |
| `auto` | **Auto Mode** — classifier reviews all actions before they run |
| `dontAsk` | Auto-denies tools unless pre-approved via `/permissions` or allow rules |
| `bypassPermissions` | Skips all permission prompts (use only in isolated containers) |

## Auto Mode — how the classifier works

Auto Mode runs a **separate classifier model** that reviews each action before execution.
It blocks anything that: escalates beyond your request, targets unrecognized infrastructure,
or appears driven by hostile content Claude read. Explicit `ask` rules still force a prompt
even in auto mode.

- **Classifier model:** Claude Sonnet 5 by default (as of Claude Code v2.1.210). Falls back
  to the session model when Sonnet 5 is unavailable, or to an Opus model for Fable 5
  sessions. (Source: [official permission-modes docs](https://code.claude.com/docs/en/permission-modes))
- **What it blocks:** unrecognized external infra, destructive git operations, secrets
  exfiltration, writing to Claude's own session transcripts, unresolvable glob deletions.
- **Fallback:** if the classifier blocks an action 3× in a row or 20× total, auto mode
  pauses and Claude Code resumes prompting.
- **The classifier sees:** user messages, tool calls, and CLAUDE.md content. Tool results
  are stripped so file/web content can't manipulate it directly.
- **Requirements:** Opus 4.6+, Sonnet 4.6+, or Fable 5 on Anthropic API. Owner must enable
  it in admin settings for Team/Enterprise accounts.

> **Original (community) framing** [[claude-code-auto-mode-permissions]]: "a risk classifier
> checks each action; safe ones run automatically, risky ones get flagged." This is accurate
> at a high level. The three-posture simplification (ask / auto / bypass) omits `acceptEdits`,
> `plan`, and `dontAsk` modes documented in official sources.

## Deny rules and hooks

Pair auto mode with `permissions.deny` rules (e.g. `Bash(rm -rf *)`) so unattended runs
([[claude-code-scheduled-tasks]]) can't go off the rails. [[claude-code-hooks|Hooks]] extend
this further: `PreToolUse` hooks fire in *every* mode including `bypassPermissions` and
can block actions the classifier would otherwise allow. This is the concrete control for the broader [[agent-security-risks]] threat model — least privilege on a tool-wielding agent.

Manage rules via `/permissions` in any session.
