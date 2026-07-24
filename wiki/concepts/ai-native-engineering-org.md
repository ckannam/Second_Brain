# AI-native engineering org (the bottlenecks moved)

Once agentic coding becomes the org-wide default, the tool isn't the hard part — the
**processes** are. [[fiona-fung|Fiona Fung]]'s thesis: coding is no longer the bottleneck,
so the norms built to protect scarce engineering bandwidth "quietly stopped working" and
have to be rewritten.

**Old bottlenecks → gone:** writing code, writing tests (TDD is now enjoyable — Claude
removes the tax), refactoring, architecture cleanup.

**New bottlenecks:** verification, code review, ownership, maintenance — because throughput
and the number of people committing both exploded.

**Rewritten norms:**
- Planning: "building is cheap, arguing is expensive" — generate 3 PRs instead of
  whiteboarding; fewer design docs; discuss in PRs/prototypes.
- Verification: **shift left**, automate to catch bugs at the source.
- Ownership: commits co-authored by Claude; "who changed this?" → get to the root question.
- Review: [[adversarial-code-review|Claude Code review]] for style/lint/spec-drift; humans
  for legal, risk, trust boundaries, **product sense/taste**.
- Team: hire **creative builders with product sense** + **deep system expertise**; flatter
  orgs; managers start as ICs.

Enterprise instances: [[ai-native-enterprise-scale]] (Delivery Hero 100+ PRs/day merged,
Doctolib governance, monday.com in-product). Non-engineer instance: [[gtm-engineering-anthropic]].
Sources: [[running-ai-native-engineering-org]], [[how-we-claude-code]]. Related:
[[test-driven-development]], [[the-capability-curve]].
