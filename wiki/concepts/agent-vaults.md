# Agent vaults

A [[claude-managed-agents|Claude Managed Agents]] primitive for storing agent credentials
securely. Secrets live encrypted on a **separate endpoint** from the sandbox; the agent
gets scoped access **per user, per session** without ever holding the raw credential. This
is made possible by [[brain-hands-decoupling|brain–hands decoupling]] — because tool
execution is separated from the loop, you don't have to run your own secret store.

Solves the "agents need access to internal systems + identity/auth" problem raised in
[[production-faster-managed-agents]]. Source: [[ship-your-first-managed-agent]].
