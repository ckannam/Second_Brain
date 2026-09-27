---
type: concept
created: 2026-07-24
updated: 2026-09-27
---

# Proactive Agents

Agents that act **without being asked** — checking in, surfacing help, and building things in the
background — rather than only responding to prompts. The defining trait of "Klaus" on
[[clawdbot]] ([[i-turned-clawdbot-personal-assistant]]) and the design north star of this vault's
own [[vault-autoresearch|AutoResearch]] loop. Enabled by [[claude-code-scheduled-tasks|scheduled
tasks/loops]] and [[agent-memory|persistent memory]] working together.

## The proactivity spectrum

| Level | Pattern | Example |
|---|---|---|
| **Reactive** | Responds when asked | Standard Claude chat session |
| **Scheduled** | Runs at a fixed cadence, produces output | Vault AutoResearch (2 AM Sunday) |
| **Event-triggered** | Wakes on an external signal (new file, webhook, message) | daily-ingest on new clips in `raw/assets/` |
| **Context-maintaining** | Initiates contact based on what it knows about you | Klaus nudging based on calendar + preferences |
| **Multiplayer-proactive** | Joins a team channel, participates without prompting | [[claude-tag|@Claude]] in Slack |

Most agents today sit at "Scheduled"; "Context-maintaining" is the frontier. The jump from
"scheduled" to "context-maintaining" requires *both* a trigger mechanism *and* a memory of what
matters — without memory, scheduled agents produce generic output.

## The mechanism

Three components work together:

1. **Trigger** — how the agent wakes: calendar cron ([[claude-code-scheduled-tasks]]), file
   watch, webhook, or a loop interval ([[claude-code-loops]]).
2. **Memory** — what the agent knows before it starts: files in the project (`CLAUDE.md`, vault
   content), [[agent-memory|cross-run memory files]], or both. Without this, each run is a
   blank slate.
3. **Action scope** — what it can do without asking: read, write, search, send to pre-approved
   destinations. The [[claude-code-permissions|Auto Mode]] + deny-rules pattern gates this
   safely ([[claude-code-scheduled-tasks]]).

The vault instantiates all three: the AutoResearch routine is cron-triggered, reads `program.md` +
`tasks/index.md` + the wiki as its "memory," and is scoped by the deny-rules in settings.

## Anthropic's first-party stack

- **[[claude-tag|Claude Tag / @Claude]]** ([[future-of-work-claude-tag]]): "in the past you opened
  Claude and asked; now Claude jumps in." Proactive *and* multiplayer — add it to a Slack channel
  and the whole team participates. Runs work over days/weeks, follows up, and remembers next time.
- **[[claude-cowork|Cowork]]** scheduled tasks: the same instinct for recurring background work,
  personal rather than team-facing.

## Vault instantiation

This vault runs two proactive lanes:

- **@cloud lane** — `Vault AutoResearch` (Sunday 2 AM ET): self-heal + build + generative; produces
  a morning PR. Enabled by: cron trigger, `program.md` + wiki as memory, branch/PR pattern for the
  action scope. See [[vault-autoresearch]].
- **@local lane** — `daily-ingest` (~3 AM, Mac awake): ingests `raw/assets/` clips → wiki per
  `AGENTS.md`, commits to `main`. Enabled by: launchd trigger, AGENTS.md + raw inbox as inputs.

Future proactive rungs under consideration:
- **Source-seeking** (MODE C): sweep public surfaces, propose new sources in the PR → [[extending-the-llm-wiki]].
- **CRM enrichment**: message-history pass to fill relationship context (needs @local, not yet built).

## Related

[[claude-code-scheduled-tasks]] · [[claude-code-loops]] · [[agent-memory]] · [[agent-dreaming]] ·
[[claude-tag]] · [[claude-cowork]] · [[vault-autoresearch]] · [[ai-executive-assistant]] ·
[[extending-the-llm-wiki]] · [[ai-second-brain-levels]].
