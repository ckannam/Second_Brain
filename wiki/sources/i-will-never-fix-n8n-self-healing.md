---
source: youtube
channel: "Nate Herk"
url: "https://www.youtube.com/watch?v=uUEa6K-FLB8"
title: "I Will Never Fix Another n8n Workflow (Claude Code)"
created: 2026-07-24
---
# Self-Healing n8n Workflows with Claude Code

**Thesis:** A **self-healing** automation system: when an [[n8n]] workflow errors, an error workflow calls Claude Code, which uses the **n8n MCP server** to audit, diagnose, and **fix the broken workflow automatically** — no manual intervention.

## Key points
- Flow: n8n error → error workflow → Claude Code → n8n MCP → patch → notify. Next run just works.
- "AI engineer on call 24/7" for your automations.
- Covers why workflows fail, more examples, and what happens if Claude Code **can't** fix it.

Tools/entities: [[claude-code]], [[n8n]], [[mcp]]. Concept: [[self-healing-workflows]]. Related: [[is-n8n-dead]], [[n8n-vs-claude-code]].

**Raw clip:** [[I Will Never Fix Another n8n Workflow (Claude Code)]]
