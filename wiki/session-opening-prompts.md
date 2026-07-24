---
type: reference
created: 2026-07-24
---
# Session-Opening Prompts

The commands/prompts used to start Claude Code sessions for this vault — stored so they
aren't re-derived each time. (Will file under the **Claude Mastery** bucket once the
[[tasks/index|life buckets]] exist.)

## 1. Skip permission prompts

Launch flag that runs the session without per-action permission prompts — full autonomy,
appropriate in a trusted directory like this vault:

```
claude --dangerously-skip-permissions
```

Note: this is a **launch flag**, so it must be set when starting the session; it can't be
toggled from inside a running session.

## 2. iMessage plugin channel

Launches the session in iMessage **channel mode** so the vault is reachable by text from
your phone.

```
claude --channels plugin:imessage@claude-plugins-official
```

Related: [[claude-code-imessage]] (the feature walkthrough), [[claude-code-channels]].

---
_Both prompts can be combined on one launch, e.g._
`claude --dangerously-skip-permissions --channels plugin:imessage@claude-plugins-official`
