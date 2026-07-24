# Agentic vs Deterministic Automation

The core trade-off behind [[agentic-workflows]].

- **Deterministic** (Python/TypeScript scripts, [[n8n]] nodes): fixed step 1→2→3. Predictable and cheap, but **brittle** — an unexpected error just fails.
- **Agentic** ([[claude-code]] agents): reads the whole project, uses all tools, tries alternatives, **self-heals**, and can **improve itself** over time. Less strictly predictable, far more robust.

You can dial in determinism when you need it by having an agent simply execute a script. This tension recurs in [[claude-code-scheduled-tasks]], [[self-healing-workflows]], and [[n8n-vs-claude-code]].
