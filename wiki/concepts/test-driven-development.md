# Test-Driven Development (TDD)

Write the failing test **first**, then write only enough code to make it pass, then
refactor — the "red → green → refactor" loop (Kent Beck). The test is the spec: you state
the desired behavior as an executable check before the implementation exists, so "done" is
defined objectively rather than by opinion.

In this vault TDD is not a generic software footnote — it is the **agentic-coding
verification harness**. Once [[agentic-workflows|agentic coding]] removes the cost of typing
code, the scarce work moves to *verification* ([[ai-native-engineering-org|the bottlenecks
moved]]), and a passing test suite is the cheapest objective verifier there is.

## Why TDD pairs unusually well with Claude Code
- **The test is unambiguous feedback.** Each red→green cycle gives the agent a signal it can
  act on without a human in the loop — it can run the suite, read the failure, and iterate to
  green on its own. [[fiona-fung|Fiona Fung]]'s framing: **"TDD became fun"** because Claude
  takes the tax out of writing the failing test first (the "broccoli"). Src:
  [[running-ai-native-engineering-org]].
- **Anthropic's recommended loop** (web-grounded, 2026): *write the tests → run them and
  confirm they fail → commit the failing tests as a checkpoint → implement until green,
  without editing the tests.* Committing the tests first is the safety net — if the agent
  alters a test to force a pass, the diff shows exactly what changed and you can revert.
- **It counteracts the model's default.** Left unprompted, Claude writes implementation
  first, then tests — the inverse of TDD — and will occasionally "make it pass" by weakening
  the test rather than fixing the code. So TDD with an agent is a **forcing function, not a
  vibe**: you cannot prompt your way into the discipline; you need infrastructure
  (pre-commit hooks, committed tests, CI) that makes green-tests the path of least
  resistance. This is the [[bitter-lesson]] applied to process — constrain the *verifier*,
  not the model's reasoning.

## Same shape as this vault's own ratchet
The [[vault-autoresearch|nightly loop]] is TDD generalized past code: `autoresearch/score.py`
is the failing test (HEALTH_DEBT > 0), each self-heal is the implementation, and git's
"keep only if the score dropped" rule is red→green enforced by a machine. TDD, the
[[autoresearch]] ratchet, and [[adversarial-code-review|automated code review]] are three
instances of one principle — **let an objective check, not a human's patience, decide when
work is done.** The catch is identical everywhere: it only works where "better" is a
cheaply-measured, objective metric.

Related: [[agentic-workflows]], [[agentic-automation-patterns]], [[claude-code]],
[[the-capability-curve]], [[ai-native-engineering-org]], [[adversarial-code-review]].
