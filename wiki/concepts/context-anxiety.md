# Context anxiety

A model behavior observed in **Sonnet 4.5**: the agent wraps up a task early — declaring
itself done — even when it still has room to spare in its context window. Anthropic added
harness-level mitigations to counter the early-stopping behavior; when **[[opus-4-5]]**
shipped, the behavior disappeared and those mitigations became obsolete.

Cited as the motivating example for why **harnesses must co-evolve with models**, and why
[[claude-managed-agents|Claude Managed Agents]] absorbs that maintenance burden (compaction,
caching, context-anxiety handling) so developers don't rebuild it per model. Source:
[[ship-your-first-managed-agent]].
