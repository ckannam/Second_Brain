# Mechanism over output (trust the how, not just the what)

If two systems produce **identical output**, you don't necessarily trust them equally — it
depends on the **mechanism** that produced it. James Brady's example
([[trustworthy-agentic-workflows-dsl]]): "this code is free of vulnerabilities, safe to
ship" means something different from an old weak model than from a SOTA model that did tool
use, critique, and redrafting — even if the sentence is word-for-word the same.

Consequences:
- There is **no single correct mechanism** — it's a design choice driven by domain, user,
  task, and a **speed-vs-rigor** tradeoff (and by the provider's brand/taste).
- To be trustworthy, an agent's process should be **legible** (spot-checkable by humans and
  other agents), **retain fidelity** under iteration, and be **followed faithfully** — which
  is what pushed [[elicit|Elicit]] toward an [[agentic-dsl]].

Rhymes with [[html-over-markdown-specs]] (make the process legible) and
[[eval-driven-model-selection]] (verify the working, not just the answer). Related:
[[adversarial-code-review]], [[agentic-workflows]].
