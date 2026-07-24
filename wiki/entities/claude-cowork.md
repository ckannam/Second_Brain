# Claude Cowork

[[anthropic|Anthropic]]'s surface for **delegated, asynchronous knowledge work** (Claude
desktop app) — the non-coding sibling of [[claude-code]]. You hand Claude a whole task, it
plans and executes against your connected tools, and the finished artifact is **yours to
own** (a handoff, not a black box). Eng + product led by [[fiona-fung]].

## What it does (from [[claude-cowork-delegate-schedule]])
- **Delegate** multi-step work — e.g. meeting prep: connect calendar/Slack/email, point at a
  notes folder, and Claude searches the calendar, researches attendees, reviews threads and
  past notes, and drafts an agenda **matching your existing template**. It can **pivot
  mid-task** when you add context (unlike chat, where you'd stop and regenerate).
- **Schedule** recurring tasks (hourly / daily / weekdays / manual). Each run is a **fresh
  Cowork session** with the latest state of files + [[mcp|connectors]]; needs the desktop app
  open and the computer awake, and runs delayed tasks when you return. Mirrors
  [[claude-code-scheduled-tasks|Claude Code routines]] for non-coders.

## In production
[[financial-crime-claude-cowork]] — high-stakes analyst workflows with in-house MCPs, MCP
gateways, and [[eval-driven-model-selection|evals]]. Related: [[claude-tag]] (proactive
multiplayer), [[ai-executive-assistant]], [[proactive-agents]].
