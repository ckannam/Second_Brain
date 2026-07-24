# Brain–hands decoupling

The core architectural decision behind [[claude-managed-agents|Claude Managed Agents]]:
separate the **agent loop** ("brain," Claude thinking about what to do) from **tool
execution** ("hands," where actions actually run). Earlier harnesses (including
[[claude-code]]) tightly couple the two — sensible when you *want* the agent to have direct
file-system access, but limiting at production scale.

Decoupling buys:
- **Security** — the sandbox never holds raw credentials; secrets stay encrypted in
  [[agent-vaults|vaults]] on a separate endpoint.
- **Latency** — no per-session container spin-up in the hot path → **>90% reduction in P95
  time-to-first-token** (reported).
- **Reliability** — if a tool container dies, respawn it without restarting the agent loop.
- **Durability** — the loop lives server-side, so sessions persist across laptop close /
  hard refresh, with managed state (idle → running → rescheduling → terminated).

Contrast with the coupled model in [[claude-code]] (agent + tools in one box, direct
computer access). Sources: [[ship-your-first-managed-agent]], [[production-faster-managed-agents]].
