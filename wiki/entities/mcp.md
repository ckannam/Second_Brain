---
type: entity
category: tech
---
# MCP (Model Context Protocol)

Open protocol for connecting [[claude-code]] (and other agents) to external tools/data via **MCP servers**. The main way sources here give Claude Code new powers.

MCP servers used across the vault: [[firecrawl]] (web scraping — [[turn-any-website-llm-ready-firecrawl]]), the **n8n MCP server** that lets Claude Code audit/fix workflows ([[i-will-never-fix-n8n-self-healing]]), and MCPs covered as "superpowers" in [[master-claude-code-36min-beginner]] and [[build-sell-claude-code-course]].

**Enterprise / platform (Code with Claude batch):** admins can now authorize MCP connectors
org-wide via their identity provider ([[enterprise-managed-auth-mcp]]); [[claude-managed-agents]]
adds **MCP tunnels** (expose private MCP servers without the public internet). Related:
[[claude-code-skills]], [[governed-skills-framework]].
