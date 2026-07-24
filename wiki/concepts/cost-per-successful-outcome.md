# Cost per successful outcome

The right metric for model economics: not the cheapest or fastest model **per token**, but
the one that is cheapest **per successful outcome**. A cheaper/faster model that fails more
often, needs retries, or requires human cleanup can cost more in total than a pricier model
that succeeds first try.

Reframes model choice as an economics problem over the **cost/accuracy Pareto frontier** —
and there are knobs ([[test-time-compute|effort levels]], prompt quality, harness) that move
you along *or shift* that frontier. Source: [[picking-the-right-model]]. Related:
[[eval-driven-model-selection]], [[outcome-oriented-agents]].
