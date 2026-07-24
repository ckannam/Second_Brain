---
source: youtube
channel: "Nate Herk"
url: "https://www.youtube.com/watch?v=pkSxISewcw8"
title: "STOP Using Bypass Permissions, Use This New Feature Instead"
created: 2026-07-24
---
# STOP Using Bypass Permissions — Use Auto Mode

**Thesis:** Claude Code's new **Auto Mode** is a permission setting between "ask before every edit" and "dangerously skip permissions." A **classifier checks each action's risk** — safe actions run automatically, risky ones get flagged.

## Key points
- Solves the two bad extremes: constant interruptions vs. giving the agent free rein.
- Enable in permission settings; especially important for unattended runs ([[claude-code-scheduled-tasks]]).
- Pair with deny-rules (e.g. block destructive bash `rm`/deletes) so autonomous agents can't go off the rails.

Tools/entities: [[claude-code]], [[anthropic]], [[claude-code-permissions]].
