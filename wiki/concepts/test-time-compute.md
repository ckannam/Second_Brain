# Test-time compute (the thinking lever)

Spending more tokens **at inference** so the model reasons more before/while answering —
the runtime analogue of train-time compute scaling. From [[the-thinking-lever]]: performance
rises along **two axes**, model size (Haiku → Sonnet → Opus) and tokens-spent-thinking
(log scale), and both can reach the same score. Holds across reasoning (Deep Search QA),
computer use (OSWorld), and PhD-level (Humanity's Last Exam) tasks.

Exposed to developers as **effort / thinking levels** (low / high / max): higher effort =
more tokens *and* more wall-clock time, but better results (the traffic-sim demo went from
simple at low to physically-plausible at 10× tokens on max). The **METR** benchmark tracks
the resulting growth in hours of autonomous human work a model can complete.

Three ways to spend it: **thinking** (reasoning scratchpad), **tool calling** (interface to
the world), and sampling/multiple attempts. Pairs with [[eval-driven-model-selection]] and
[[cost-per-successful-outcome]] (effort is a knob on the cost/accuracy frontier). Related:
[[the-capability-curve]], [[opus-4-7]].
