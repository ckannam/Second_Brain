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

Related: [[json-prompting]], [[html-over-markdown-specs]], [[bitter-lesson]] (don't
over-constrain capable models), [[evals-for-taste]].
