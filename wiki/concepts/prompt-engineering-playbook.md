# Prompt engineering playbook

Best practices for prompting agentic systems, from [[the-prompting-playbook]]:

- **Evals before edits.** You can't know a prompt change helped without an eval suite (see
  [[eval-driven-model-selection]]). Cover control cases, edge cases (past failures), and
  **capability boundaries** (hand off / refuse).
- **Diagnose migrations.** When a prompt breaks on a new model, decide: capable-but-behaves-
  differently (fix by prompting) vs. less-capable (prompting won't fix it).
- **Hygiene first.** Strip junk (website copy, cookie/"hero image" cruft), don't lie to the
  model ("you are human"), and **structure with XML tags** separating role / policy /
  guidelines / tone / data. *"If you can't tell guidelines from policy from data, the model
  can't either."*
- **Output contracts** for format consistency; enforce in the **harness** where the prompt
  isn't enough.
- **Target failure modes one at a time** against the eval.
- **Clarifying-question prompting.** For an under-specified request, have the model **ask
  before it answers** — e.g. *"Before you start, ask me the 3–5 questions that would most
  change your output; be concise."* Resolving ambiguity up front collapses several correction
  round-trips into one and measurably lifts accuracy on ambiguous queries (modeling the
  follow-up turn gives ~5% F1 / ~3% better ask-vs-answer judgment in the research). It's the
  interactive dual of *output contracts*: contracts pin the **output** shape, clarifying
  questions pin the **input** intent. This is the core move behind the vault's shipped
  **prompt-architect skills** (`claude-chat-prompt` / `claude-cowork-prompt` /
  `claude-code-prompt`) — understand the task (asking when unsure) *then* emit the optimal
  prompt. Related move: **Rephrase-and-Respond** — ask the model to restate the question in
  its own words before answering, surfacing a misread cheaply.

Related: [[json-prompting]], [[html-over-markdown-specs]], [[bitter-lesson]] (don't
over-constrain capable models), [[evals-for-taste]], [[skill-authoring-playbook]] (the same
evals-before-edits discipline, applied to skills).
