---
type: entity
created: 2026-08-08
---

# Claude API

The **Claude API** (Anthropic's developer platform, `platform.claude.com`) is how you call
Claude **programmatically** — one HTTP endpoint, `POST /v1/messages`, wrapped by official SDKs
(`anthropic` for Python, `@anthropic-ai/sdk` for TypeScript, plus Go/Java/Ruby/C#/PHP). It is the
third way to use Claude alongside the two Cole already leans on, and the distinction matters:

- **[[claude-code]]** — the agentic CLI/coding harness (what runs this vault's autoresearch loop).
- **claude.ai chat app** — the interactive thinking-partner UI.
- **Claude API** — raw model access from your own code, for pipelines and apps. No chat UI, no
  agent loop unless you build one.

> **Snapshot — 2026 (models/prices age fast; reconcile before quoting).** Current model lineup:
> **Claude Fable 5** (most capable, $10/$50 per 1M in/out tokens), **Opus 5** ($5/$25),
> **Sonnet 5** ($3/$15, the speed/quality balance), **Haiku 4.5** ($1/$5, fastest/cheapest). All
> have a 1M-token context window except Haiku (200K). Opus is the default for hard work; Sonnet for
> high-volume production; Haiku for simple/fast tasks. Verify live via the Models API
> (`GET /v1/models`) or [[anthropic]]'s pricing page before relying on these.

## Why it's in this vault — the Neuro pipeline's script-gen step

Cole's [[neuro-production-pipeline|Neuro production pipeline]] calls the Claude API as its
**scripting brain**: given a topic, a `claude.messages.create(...)` call returns the voice-ready
script **plus** the scene-by-scene storyboard `spec.json` that drives the rest of the render
([[neuro-scripts-batch-1|batch-1 scripts]] were drafted this way). This is a clean division of
labor in the pipeline — **Claude API writes the words and the plan; the Gemini "Nano Banana" API
draws the ~12 doodle scenes** (the `$0.045–0.067`/image cost line lives on the pipeline page). Both
are pay-per-call developer APIs, not subscriptions, which fits the [[neuro-free-tool-stack|$0 /
no-new-subscription]] constraint (a full ~12-scene Short's Claude-side scripting cost is a few
cents). **Structured outputs** (`output_config.format` with a JSON schema) is the right primitive
for the storyboard step — it guarantees the returned `spec.json` validates against the scene schema
instead of hoping the model returns clean JSON.

## Capabilities worth knowing (for building on it)

The API is one endpoint whose *features* are request parameters, not separate products:

- **Tool use** — give Claude functions to call; the SDK "tool runner" drives the agentic loop.
- **Structured outputs** — constrain the response to a JSON schema (the storyboard use case above).
- **Adaptive thinking + effort** — `thinking: {type: "adaptive"}` plus an `effort` level
  (`low`→`max`) trades depth for cost; the modern replacement for a fixed "thinking budget."
- **Prompt caching** — cache a large stable prefix (~90% cheaper on re-reads); a prefix match, so
  volatile content must go *after* the cached block.
- **Streaming** — token-by-token output; required for large `max_tokens` to avoid HTTP timeouts.
- **Batches** — asynchronous processing at **50% cost** for non-latency-sensitive jobs.
- **Server-side tools** — web search / web fetch / code execution run on Anthropic's side.
- **MCP connector** — call remote [[mcp|MCP]] servers directly from a message request.
- **Vision + PDF + Files API** — image and document input, uploaded once and referenced by ID.

For *building against it*, the platform ships a bundled **`claude-api` skill** (model IDs, params,
SDK patterns, migration notes) — the authoritative reference to consult rather than guessing model
strings, which age out.

## Relation to the rest of the toolbox

The API is the **lowest-level, most flexible** rung: [[claude-code]] and the chat app are both
*built on* the same models, but hand you a harness; the API hands you the raw call and asks you to
build the harness (or not). Reach for it when a pipeline needs Claude as one programmatic step
(Neuro script-gen), a custom app needs model access without a chat UI, or you want batch/caching
economics the interactive surfaces don't expose. When the job is agentic coding, use
[[claude-code]]; when it's interactive thinking/writing, use the chat app.

Related: [[claude-code]] · [[anthropic]] · [[neuro-production-pipeline]] · [[neuro-channel]] ·
[[neuro-free-tool-stack]] · [[claude-code-scheduled-tasks]] · [[Claude Mastery]].
