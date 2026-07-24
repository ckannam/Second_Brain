---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=IA5LWIGqnyM"
event: "Code with Claude"
speaker: "Fiona Fung (Eng + Product lead, Claude Code & Cowork)"
created: 2026-07-24
---

# Running an AI-native engineering org

[[fiona-fung|Fiona Fung]] (leads eng + product for [[claude-code]] and [[claude-cowork]];
formerly Meta, Microsoft) on what breaks when agentic coding goes from individual tool to
org-wide default: "the tool isn't the hard part — your processes are." The core idea:
[[ai-native-engineering-org|the bottlenecks moved]].

## The shift
For years engineering bandwidth was the scarce resource, so planning/review/ownership all
existed to protect it. Historical parallel: early-2000s Visual Studio shipped from one
server room, a build queue merging **6 PRs at a time**; cloud + continuous build moved that
bottleneck. Now **coding is rarely the slow part** — writing code, tests, and refactoring
stopped being bottlenecks. The new ones: **verification, review, ownership, maintenance.**
Mantra: "what served you prior may no longer" — audit processes that *quietly stopped
working.*

## Rewritten norms
- **TDD became fun** — Claude takes the tax out of writing the failing test first (the
  "broccoli"). See [[test-driven-development]].
- **Planning:** "code wins; building is cheap, arguing is expensive." Generate three PR
  versions instead of whiteboarding; discuss in PRs/prototypes; **fewer design docs**.
  Prototype → production is now fast, defusing the old "throwaway prototype" fear.
- **Verification = shift left** — automate to catch bugs near the source, not in customers'
  hands.
- **Ownership:** nearly every Claude Code commit is co-authored by Claude. "Who made this
  change?" → get to the *root* question; Claude can answer it.
- **Code review:** [[adversarial-code-review|Claude Code review]] keeps pace — great at
  style/lint, obvious bugs, and **spec drift** (check the spec into the repo). Keep humans
  for legal, risk tolerance, trust boundaries, and **product sense / taste** (the "snowman
  that was actually Mr. Peanut" story).
- **Team makeup:** double down on two profiles — **creative builders with product sense**
  and **deep system expertise**. Build product sense by **dogfooding**.
- **Org shape:** flatter and agile; every Claude Code manager started as an IC.
- **Routines:** a morning [[claude-code-scheduled-tasks|routine]] amalgamates feedback
  channels into themes over coffee.

Companion workshop: [[how-we-claude-code]]. Enterprise view: [[ai-native-enterprise-scale]].
