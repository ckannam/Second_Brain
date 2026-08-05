---
type: concept
created: 2026-08-05
---
# Test-driven development (TDD in the agentic era)

**TDD** is the discipline of writing a **failing test first**, then the minimum code to make
it pass, then refactoring — the *red → green → refactor* loop. The test is written before the
implementation, so it doubles as an **executable specification**: "done" is defined as
"the test goes green," not as a human eyeballing the output.

## Why agentic coding changes the calculus

Classic TDD's friction was always the **first step**: writing the failing test is upfront work
with no immediate reward — the "broccoli" you eat before the code. [[fiona-fung|Fiona Fung]]'s
observation is that agentic coding **removes that tax**: Claude drafts the failing test, so
"TDD became fun" (source: [[running-ai-native-engineering-org]]). Writing tests was one of the
**old bottlenecks that disappeared** once coding stopped being the scarce step — see
[[ai-native-engineering-org]] for the full "the bottlenecks moved" thesis.

That inverts what TDD is *for*. When a human writes both test and code, TDD mostly guards
against the human's own mistakes. When an **agent** writes the code, the test-first habit
becomes the **control surface**: a pre-committed, machine-checkable spec the agent must
satisfy, written before the agent can "reason backward" from a solution to a lenient test.

## Tests as the spec (why this matters for verification)

The new bottleneck is **verification, not authorship** ([[ai-native-engineering-org]]). TDD is
the cheapest form of shift-left verification: it moves the spec to the front and makes drift
detectable. A failing test checked into the repo *before* the agent runs is the same idea as
**checking the spec into the repo** so [[adversarial-code-review|Claude Code review]] can catch
**spec drift**. It also embodies [[mechanism-over-output]]: an output that passes a rigorous
test written *first* is more trustworthy than the identical output with a test retrofitted to
match it.

Caveat — the failing test must be **written before, and independently of, the implementation**.
An agent that writes code and *then* a test tailored to that code gets green with no assurance
(a form of teaching-to-the-test). The value is entirely in the ordering.

## In this vault

- The [[Neuro]] learning-app project's "Learning-Triage" wedge is itself a candidate for this
  loop: define the routing behavior as tests first, then build against them.
- The [[vault-autoresearch]] loop is a cousin pattern — a **frozen evaluator**
  (`score.py` / HEALTH_DEBT) plays the role the failing test plays in TDD: a pre-committed,
  un-gameable metric that a change must strictly improve. Same principle (define success before
  you build), different substrate.

Related: [[ai-native-engineering-org]], [[running-ai-native-engineering-org]],
[[adversarial-code-review]], [[mechanism-over-output]], [[agentic-workflows]],
[[the-capability-curve]].
