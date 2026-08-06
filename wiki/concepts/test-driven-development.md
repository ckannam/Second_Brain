---
type: concept
created: 2026-07-31
---

# Test-Driven Development (TDD)

Write the failing test **first**, then the code that makes it pass, then refactor —
the classic **red → green → refactor** loop. The test is written before the
implementation, so it encodes the *intended behavior* as an executable check rather
than describing code that already exists. Filed 2026-07-31 as the concept the
[[ai-native-engineering-org|AI-native engineering]] cluster keeps pointing at.

## The AI-native reframe (why this matters now)

Classic TDD's selling point was regression safety; its tax was discipline — writing
the "broccoli" failing test first, before the fun part. Two things invert in the
[[ai-native-engineering-org|AI-native]] era:

- **The tax is gone.** [[claude-code|Claude]] takes the drudgery out of writing the
  failing test, so "**TDD became fun**" — teams that skipped it now do it by default
  ([[running-ai-native-engineering-org]]).
- **The test becomes the part the human still owns.** When an agent writes the
  implementation, the test is the **executable spec the agent optimizes against** —
  and, crucially, the part it *can't fake its way past*. Vague prose instructions get
  gamed; a green test suite is a hard, checkable contract. So TDD shifts from
  "regression insurance" to **the steering wheel for autonomous code generation**:
  the human specifies behavior as tests, the agent drives the code to green.

This is why [[running-ai-native-engineering-org|the new bottleneck is verification,
not coding]]: once writing code is cheap, the scarce, human-owned work is deciding
*what "correct" means* and encoding it so a machine can check it — **shift-left
verification**, catching bugs at the source rather than in production.

## The pattern this vault already runs

TDD-as-a-metric-gate is the same shape as this vault's own loop: [[vault-autoresearch]]
edits pages freely but keeps a change **only if `score.py`'s HEALTH_DEBT drops** — a
frozen, un-gameable evaluator playing exactly the role the test suite plays for agentic
code. "Tests are the reward function" and "HEALTH_DEBT is the ratchet" are the same
idea: give the autonomous editor a cheap, objective pass/fail it cannot talk its way
around. (Karpathy's [[autoresearch]] uses a frozen `prepare.py`/`val_bpb` for the same
reason.)

## Where it sits among the vault's verification concepts

- **Complements [[adversarial-code-review]]** — TDD checks *behavior against a spec you
  wrote up front*; adversarial review hunts *defects you didn't anticipate* (style,
  spec-drift, security). Both are "shift-left" verification; neither replaces the other.
- **Distinct from [[eval-driven-model-selection]]** — evals score a *model's* aggregate
  quality on a task suite; TDD gates a *single change* against a behavioral spec. Same
  philosophy (measure, don't vibe), different granularity.
- Humans still own the boundaries a test can't encode — legal, risk, trust boundaries,
  product **taste** ([[ai-native-engineering-org]]).

## Caveats (kept honest)

- A green suite proves *the encoded behavior*, not *correct behavior* — tests can be
  wrong, shallow, or miss the real spec; TDD raises the floor, it doesn't guarantee the
  ceiling.
- Over-fitting to tests is real: an agent optimizing to green can satisfy the letter and
  miss the intent — which is exactly why adversarial review and human taste stay in the
  loop.

Sources: [[running-ai-native-engineering-org]], [[ai-native-engineering-org]]. Related:
[[adversarial-code-review]], [[eval-driven-model-selection]], [[vault-autoresearch]],
[[the-capability-curve]].
