# Outcome-oriented agents (outcomes)

A shift from conversational, tool-by-tool prompting to giving an agent a **desired result**
and letting it figure out the path. In [[claude-managed-agents|Claude Managed Agents]],
**outcomes** let you define a **rubric / set of goals**; after a first pass the agent
triggers its own outcome grading and loops — re-planning tool calls — until it judges the
rubric satisfied.

This is the natural interface once agents run for hours: you hand off a whole task (the
example given is an end-to-end M&A pipeline) and the agent returns only when confident it's
done, rather than checking in after every step. Pairs with [[agent-memory]] and
[[multi-agent-orchestration]].

Sources: [[production-faster-managed-agents]], [[ship-your-first-managed-agent]]. Related:
[[the-capability-curve]], [[agentic-workflows]].
