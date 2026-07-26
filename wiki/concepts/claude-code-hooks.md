---
type: concept
updated: 2026-07-26
---
# Claude Code Hooks

User-defined event handlers that run deterministically at specific points in
[[claude-code]]'s lifecycle — the complement to [[claude-code-permissions|permission rules]].
Where permission rules gate what Claude *may* do, hooks guarantee certain actions *always*
happen regardless of the model's choices.
Source: [Anthropic official docs](https://code.claude.com/docs/en/hooks-guide) · [Hooks reference](https://code.claude.com/docs/en/hooks).

## What you can hook

Hooks fire on 30+ named lifecycle events. The most useful everyday ones:

| Event | When it fires | Can block? |
|---|---|---|
| `PreToolUse` | before a tool call executes | yes (exit 2) |
| `PostToolUse` | after a tool call succeeds | no (action already ran) |
| `Stop` | when Claude finishes a turn | yes (exit 2 keeps Claude working) |
| `Notification` | when Claude needs attention / input | no |
| `SessionStart` | when a session begins or resumes | no |
| `PermissionRequest` | when a permission dialog appears | yes (return allow/deny JSON) |
| `PermissionDenied` | when auto mode classifier denies a call | can signal retry |
| `ConfigChange` | when a settings file changes mid-session | yes (exit 2) |
| `CwdChanged` | when the working directory changes | no |
| `FileChanged` | when a watched file changes on disk | no |
| `PreCompact` / `PostCompact` | around context compaction | no |
| `SessionEnd` | when the session terminates | no |

Full list (30+ events) in the [Hooks reference lifecycle table](https://code.claude.com/docs/en/hooks#hook-lifecycle).

## Hook types

- **`command`** (default) — run a shell command; communicate via stdin/stdout/exit code.
- **`http`** — POST event data to an HTTP endpoint; same JSON response format.
- **`mcp_tool`** — call a tool on an already-connected MCP server.
- **`prompt`** — single-turn LLM call (Haiku by default) for judgment-based decisions.
- **`agent`** — multi-turn subagent with tool access, for verification against live state (experimental).

## Configuration in `settings.json`

Add a `hooks` block; each key is an event name, the value is a list of matcher groups:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          { "type": "command", "command": "osascript -e 'display notification \"Claude needs your attention\"'" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write" }]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{ "type": "command", "command": ".claude/hooks/block-rm-rf.sh" }]
      }
    ]
  }
}
```

**Scope by location:** `~/.claude/settings.json` (user-global) or `.claude/settings.json`
(project, committable). Plugin and skill frontmatter can also define scoped hooks.
Run `/hooks` inside a session to browse all active hooks.

## Exit codes and output

A `command` hook communicates via exit code and stdout/stderr:
- **Exit 0** — no objection; action proceeds (for `UserPromptSubmit`/`SessionStart`, anything written to stdout is added to Claude's context).
- **Exit 2** — block the action; write a reason to stderr and Claude receives it as feedback.
- **Any other exit code** — action proceeds; a hook error notice appears in the transcript.

For richer control, exit 0 and write a JSON object to stdout:
```json
{ "hookSpecificOutput": { "hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "Use rg instead of grep" } }
```
`permissionDecision` values: `allow` (skip interactive prompt), `deny`, `ask` (force prompt), `defer` (headless mode only).

**Multiple hooks on one event:** all run in parallel; most-restrictive decision wins
(deny > defer > ask > allow). A deny from one hook doesn't stop sibling hooks from executing.

## Common patterns

- **Desktop notification on idle:** `Notification` hook, empty matcher, `osascript`/`notify-send` command. Used in this vault's [[claude-code-scheduled-tasks]] setup. Src: [[claude-code-2-scheduled-tasks]].
- **Auto-format on edit:** `PostToolUse` hook, `Edit|Write` matcher, run Prettier.
- **Block dangerous commands:** `PreToolUse` hook, `Bash` matcher, exit 2 if command matches `rm -rf`.
- **Re-inject context after compaction:** `SessionStart` hook, `compact` matcher, echo critical reminders to stdout.
- **Audit config changes:** `ConfigChange` hook, append to a log file.
- **Auto-approve a known-safe permission:** `PermissionRequest` hook, narrow matcher, return `{"behavior": "allow"}` JSON.
- **Prompt-based stop check:** `Stop` `prompt` hook; model returns `{"ok": false, "reason": "…"}` to keep Claude working.

## Hooks and permission modes

`PreToolUse` hooks fire in *every* permission mode, including `bypassPermissions`. A hook
returning `deny` blocks the tool even when the user skips all permission prompts — hooks can
only tighten restrictions, not loosen them past what permission rules allow.
In [[claude-code-permissions|auto mode]], a hook returning `"ask"` forces a permission prompt;
the auto mode classifier can still deny the call but cannot silently approve it.

Related: [[claude-code-permissions]], [[claude-code-scheduled-tasks]] (hooks for notifications),
[[claude-code-skills]] (skills can define hooks in frontmatter), [[claude-code-agent-teams]].
