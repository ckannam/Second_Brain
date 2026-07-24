---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=qOjleN2-50c"
event: "Code with Claude"
speaker: "James Brady (Elicit)"
created: 2026-07-24
---

# Making agentic workflows trustworthy and verifiable with a custom DSL

James Brady ([[elicit|Elicit]]) on an unconventional research-assistant architecture: one
component writes a plan in a **custom domain-specific language**, another interprets it, and
a "quiver of models" executes concrete tasks. Architecture as an instantiation of company
values.

## Trust is about mechanism, not just output
If two systems produce identical output, do you trust them equally? It depends on the
**[[mechanism-over-output|how]]**. "This code is free of vulnerabilities" from an old weak
model vs. a SOTA model that did tool use + critique + redrafting are different objects, even
if the message is identical. There's no single correct mechanism — it's a design choice
(speed vs. rigor; provider brand/taste; [[elicit|Elicit]] prizes reliability + data
provenance).

## Three desiderata → a DSL
1. **Legible** process — spot-checkable by humans *and* other (critique) agents.
2. **Iteration retains fidelity** — add layers/directions without drifting from the user's
   original intent.
3. **Followed faithfully** — the system actually executes the vetted steps.

These led to **AshPL** (Æsh PL): **Turing-incomplete**, no loops/recursion/mutation, purely
functional, reactive — an **opinionated typed subset of Python** with domain primitives
(retrieve academic papers, clinical trials). Core engine: **write AshPL → interpret (plain
Python) → redraft** on results (e.g. type error → fix → reinterpret), looping. System: web
UI ↔ append-only **event log** (distributed state) ↔ Python service ↔ sandbox. See
[[agentic-dsl]].

Related: [[html-over-markdown-specs]] (legible artifacts), [[multi-agent-orchestration]]
(critique agents), [[agentic-workflows]].
