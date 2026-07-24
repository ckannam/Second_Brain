# Agentic DSL (custom domain-specific language for agent plans)

An architectural pattern for trustworthy agents: have the agent express its plan in a
**constrained domain-specific language** rather than free-form code or prose, then interpret
and redraft it in a loop. Exemplar: **AshPL** (Æsh PL) at [[elicit|Elicit]]
([[trustworthy-agentic-workflows-dsl]]).

**AshPL properties:** Turing-**incomplete** (no loops, recursion, or mutation), purely
functional, reactive, an **opinionated typed subset of Python** with domain primitives baked
in (retrieve academic papers, clinical trials). Types enable fast redrafts on type errors.

**Core engine:** one component writes AshPL → interpret it in plain Python → redraft based on
what happened (type error → fix → reinterpret; ran → rewrite) — a constant write/interpret/
rewrite loop, with a "quiver of models" executing concrete tasks.

**Why:** a constrained language makes the plan **legible** (spot-checkable by humans and
critique agents), keeps **fidelity** during iteration, and can be **executed faithfully** —
the three desiderata of [[mechanism-over-output]]. Not universal advice: "you probably
shouldn't" reach for a DSL unless those needs dominate. Related:
[[html-over-markdown-specs]], [[json-prompting]], [[self-healing-workflows]].
