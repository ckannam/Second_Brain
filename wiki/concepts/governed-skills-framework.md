# Governed skills framework

The organizational pattern that let [[man-group|Man Group]] put AI-authored trading signals
into production in a **regulated** firm ([[signals-that-trade-themselves]]): teach Claude
your workflows via a **governed set of [[claude-code-skills|skills]]** + a core data layer,
rather than retraining or letting each team improvise.

**The iceberg.** The signal/output is the visible tip; underneath sits all the load-bearing
work — cleaning data, stitching prices, detecting outliers, infrastructure, backtests. If
teams run different versions of those workflows they get different answers, and you can't
tell a better **idea** from a different **measurement**. **Shared, versioned workflows** give
consistency, comparability, and no duplicated effort — and, crucially, a governance surface
**compliance can approve**. At Man Group: ~750 developers/quants, 100+ skills.

Generalizes beyond finance: the same "teach it your workflows, govern them centrally" move
underlies [[financial-crime-claude-cowork]] and the enterprise adopters in
[[ai-native-enterprise-scale]] (esp. Doctolib's org-wide governance). Related:
[[mechanism-over-output]], [[eval-driven-model-selection]], [[claude-md-router]].
