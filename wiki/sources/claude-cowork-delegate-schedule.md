---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=tYOI-WoLS_o"
created: 2026-07-24
---

# Delegate and schedule tasks in Claude Cowork

Tutorial for [[claude-cowork|Claude Cowork]]: delegating multi-step work and scheduling
recurring tasks.

**Delegate — meeting prep.** Connect calendar, Slack, email; point Claude at a meeting-notes
folder and ask it to prep for a call: search the calendar, research attendees, review recent
Slack threads and past notes, and draft an agenda **in the existing template's format**.
Claude **pivots mid-task** when you add a source ("also check my email"), rather than
stopping and regenerating. It surfaces decisions to push for, your lead win, and watch items,
and saves the doc to your folder — a **handoff** where the final document is yours to own.

**Schedule — recurring tasks.** Ask for "every hour, scan the content team's shared drive for
changes, note who changed what, group by client, save a summary." Claude drafts a scheduled-
task prompt you review, set the cadence (hourly / daily / weekdays / manual), and accept. It
appears on the **Scheduled** page and runs automatically while the desktop app is open. Each
run is its **own Cowork session with fresh context** (latest files + connectors); the
computer must be awake and the app open, and delayed runs execute when you return.

Related: [[claude-code-scheduled-tasks]], [[proactive-agents]], [[financial-crime-claude-cowork]].
