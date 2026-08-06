# Test-driven development (TDD)

Write the failing test **first**, then the code that makes it pass, then refactor —
the **red → green → refactor** loop. The test encodes the spec *before* the implementation
exists, so "done" is defined objectively and up front rather than argued after the fact.

## Why it resurfaces in the agentic era

TDD is decades old, but [[claude-code|agentic coding]] changed its economics and its role,
which is why two vault sources reach for it:

- **The tax is gone.** Writing the failing test first was always the disciplined-but-annoying
  part — the "broccoli." When Claude writes the test, TDD "became *fun*": you keep the
  guardrail without paying the tax ([[running-ai-native-engineering-org]], [[fiona-fung|Fiona
  Fung]]). In the [[ai-native-engineering-org]] framing, *writing tests* dropped off the
  bottleneck list entirely.
- **The test becomes the agent's spec and its leash.** When an agent writes the
  implementation, a red test is an objective, machine-checkable definition of the target and
  a **guardrail against spec-drift** — it lets the agent iterate autonomously (run test → fix →
  repeat) without a human adjudicating every step. This is the coding-side twin of two patterns
  the vault already owns:
  - **Eval-first skill authoring** — build the evals *before* the instructions so the skill
    solves a real, measured gap ([[skill-authoring-playbook]], [[evals-for-taste]],
    [[llm-as-judge]]). A test is to code what an eval is to a skill/prompt.
  - **The self-heal ratchet** — HEALTH_DEBT is this vault's own "test suite": every change
    either lowers the objective metric (keep) or doesn't (revert) ([[vault-autoresearch]],
    [[self-healing-workflows]]).

## Where it sits among the guardrails

TDD catches *spec* failures (does the code do what was asked?). It pairs with, but doesn't
replace, the other verification layers the [[ai-native-engineering-org]] calls out as the
*new* bottleneck: [[adversarial-code-review|Claude code review]] for style/lint/drift, and
humans for legal, risk, trust boundaries, and product taste. The general move — judge the
work by an objective artifact you wrote first, not by eyeballing the output afterward — is the
[[mechanism-over-output]] principle applied to code.

**Failure modes to respect:** tests that assert the implementation rather than the behavior
(brittle, block refactors); chasing coverage as a vanity metric instead of testing the risky
paths; and letting an agent "make the test pass" by weakening the test — the reason human
review of the *test itself* still matters.

Related: [[ai-native-engineering-org]] · [[running-ai-native-engineering-org]] ·
[[adversarial-code-review]] · [[skill-authoring-playbook]] · [[evals-for-taste]] ·
[[mechanism-over-output]] · [[the-capability-curve]].
