# Self-Healing Workflows

Automations that **detect and fix their own failures** using an agent, instead of just alerting a human.

## Canonical example ([[i-will-never-fix-n8n-self-healing]])
An [[n8n]] error triggers an error workflow → calls [[claude-code]] → Claude uses the **n8n MCP server** to audit the broken workflow, diagnose it, and patch it → you just get a "fixed" notification → the next run works.

Rooted in the [[agentic-vs-deterministic|agentic]] property that agents try alternatives and update themselves. Also appears as the "self-improving loop" in [[claude-code-scheduled-tasks]] (fix the script → refine the prompt → keep a run log).

**At platform scale**, self-healing becomes a memory/learning problem: [[agent-dreaming]] curates cross-session memory so a swarm stops repeating the same mistakes, and [[instructions-as-code]] closes the loop by merging fixes into reviewed skills. [[elicit|Elicit]]'s [[agentic-dsl|AshPL]] engine self-heals within a run (write → interpret → redraft on type/exec errors), and [[lovable]]'s fleet-learning layer catches coding mistakes across all users. Related: [[agentic-workflows]], [[mcp]], [[governed-skills-framework]].

**Self-improving (not just self-healing).** [[autoresearch]] pushes this one step further: git becomes a ratchet — every experiment either **advances the branch** (improved the metric) or is **`git reset` away** (equal/worse), and crashes are caught by grepping the run log and retried or discarded. Self-healing keeps a pipeline *working*; the autoresearch loop makes it *better* over time against an objective metric.
