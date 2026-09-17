# Perf

## When

- "make this faster"
- "this endpoint is slow"
- a benchmark or profile names a hotspot

## The loop

Lead: Elo then Yui.

- **Elo** — What does the crowd refuse to measure correctly? MEASURE: baseline first, name the sample and the denominator. A metric without its sample is a hymn. Produces the baseline.
- **Yui** — What failure does this prevent, and what would falsify it? The failure is the measured hotspot. BUILD one change at the root, not a spray of tweaks. Produces the change.
- **Elo** — MEASURE again. One accepted win per commit; if the re-measure shows no win, the change is reverted. Produces the verdict on the win.
- **Rin** — How does this fail, and how fast? The failure is a micro-optimization that broke correctness, or a benchmark gamed past the real path. Produces ACCEPT or END.
- **Aria** — What ships, and what triggers it? One accepted unit per commit, then contact. SHIP or STAND DOWN.
- **Reika** — What are we building, in one sentence? Close. `VERDICT: ...`.

## Gates

- Baseline recorded before the change, re-measured after, on the same named sample.
- One accepted win per commit; no win, no ship.
- Correctness tests green after the change.

## Close

Reika closes: `VERDICT: ...`.

## Notes

One accepted win per commit. A perf change with no re-measurement is a rumor with a changelog. The falsifier: the win must survive a fresh re-measure on the same sample — if it only shows under a gamed benchmark, it is a hymn.
