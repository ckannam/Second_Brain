---
type: entity
category: tech
updated: 2026-08-30
---
# MCP (Model Context Protocol)

Open protocol (originated by [[anthropic|Anthropic]], now a broad cross-vendor standard) for
connecting [[claude-code]] and other AI agents to external tools and data via **MCP servers**. It
is the main way the sources in this vault give Claude Code new powers — and the plumbing this
vault's own automation runs on: the nightly loop reaches GitHub, Gmail, Calendar, Drive, and more
through MCP servers, not bespoke integrations. Think of it as *"a USB-C port for AI apps"* — one
standard socket so any compliant tool plugs into any compliant agent, instead of an N×M mesh of
custom connectors.

## Architecture — host / client / server

MCP is a **client–server** protocol speaking **JSON-RPC 2.0**. Three roles:
- **Host** — the user-facing AI app that orchestrates the model and manages connections (Claude
  Code, the claude.ai app, [[claude-cowork]], an IDE).
- **Client** — an intermediary inside the host, one per server, that carries the bidirectional
  traffic and dispatches tool calls.
- **Server** — an independent process exposing capabilities. Servers are cheap and composable — a
  host can hold many at once (this session alone runs GitHub, Gmail, Calendar, Drive, Notion,
  Spotify servers side by side).

## The three primitives

Every server exposes external capability through three primitives — the whole surface area:
- **Tools** — functions the model can *invoke* (search a repo, query a DB, send a request).
- **Resources** — data the model can *read* (file contents, records, docs).
- **Prompts** — reusable templates/workflows the server offers the user.

## Transport

- **stdio** — local servers over standard in/out; the default for CLI and local integrations.
- **Streamable HTTP** — remote servers; what makes hosted/enterprise MCP servers possible.

## Snapshot — the 2026-07-28 specification (protocols age; reconcile before quoting)

The **2026-07-28 revision** is the largest since MCP launched, retooling it as *multi-agent
infrastructure* rather than single tool hookups. Web-grounded against the official spec/blog
(`modelcontextprotocol.io`):
- **Stateless core** — dropped the stateful `initialize`/`initialized` handshake and session IDs
  for a plain request/response model, so a remote server can sit behind an ordinary round-robin
  load balancer instead of needing sticky sessions + a shared session store.
- **Header-based routing** — Streamable HTTP now carries `Mcp-Method` / `Mcp-Name` headers so
  gateways and rate-limiters route without parsing the JSON body.
- **Extensions framework** — formalizes add-ons split out of the core: **Tasks** (long-running
  agent work via polling), **MCP Apps** (server-rendered UI), and **Enterprise Managed
  Authorization / EMA** (the standardized form of admin-authorized connectors —
  see [[enterprise-managed-auth-mcp]]).
- **Multi Round-Trip Requests (MRTR)** — mid-call user interaction (confirmations, missing
  params) even over a stateless connection.
- **OAuth / OIDC alignment** — requires RFC 9207 issuer validation and deprecates Dynamic Client
  Registration in favor of **Client ID Metadata Documents (CIMD)**; credentials bind to the issuer
  that minted them (no cross-server reuse). Auth + provenance are the frontier here, and the
  security-research literature (real-world remote-server auth audits) flags it as the soft spot.
- **SDKs**: TypeScript, Python, Go, C# stable; Rust in beta.

## How this vault uses MCP

- **Servers as superpowers:** [[firecrawl]] (web scraping → [[turn-any-website-llm-ready-firecrawl]]),
  the **n8n MCP server** that lets Claude Code audit/fix workflows
  ([[i-will-never-fix-n8n-self-healing]]), and MCP "superpowers" covered in
  [[master-claude-code-36min-beginner]] and [[build-sell-claude-code-course]].
- **From the message API:** the [[claude-api|Claude API]]'s **MCP connector** calls remote MCP
  servers directly inside a single message request — MCP without a full agent harness.
- **Enterprise / platform (Code with Claude batch):** admins authorize MCP connectors org-wide
  through their identity provider ([[enterprise-managed-auth-mcp]]); [[claude-managed-agents]] adds
  **MCP tunnels** to expose private servers without the public internet. Governance of what a skill
  or agent may reach ties into [[governed-skills-framework]].

Related: [[claude-code]] · [[anthropic]] · [[claude-api]] · [[claude-managed-agents]] ·
[[claude-cowork]] · [[firecrawl]] · [[n8n]] · [[enterprise-managed-auth-mcp]] ·
[[claude-code-skills]] · [[governed-skills-framework]].
