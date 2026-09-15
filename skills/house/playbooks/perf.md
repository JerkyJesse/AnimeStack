# Perf

## When

- "make this faster"
- "this endpoint is slow"
- a benchmark or profile names a hotspot

## The loop

Lead: Elo then Yui.

- **Elo** — What wound does the crowd refuse to rank correctly? MEASURE: baseline first, name the sample and the denominator. A metric without its sample is a hymn. Produces the baseline.
- **Yui** — What wound does this exploit? The wound is the measured hotspot. BUILD one change at the root, not a spray of tweaks. Produces the change.
- **Elo** — MEASURE again. One accepted win per commit; if the re-measure shows no win, the change is reverted. Produces the verdict on the win.
- **Rin** — How is this allowed to die? The death is a micro-optimization that broke correctness, or a benchmark gamed past the real path. Produces ACCEPT or END.
- **Aria** — What is the click? One accepted unit per commit, then contact. CLICK or STAND DOWN.
- **Reika** — What are we allowed to want? Close. `VERDICT: ...`.

## Gates

- Baseline recorded before the change, re-measured after, on the same named sample.
- One accepted win per commit; no win, no ship.
- Correctness tests green after the change.

## Close

Reika closes: `VERDICT: ...`.

## Notes

One accepted win per commit. A perf change with no re-measurement is a rumor with a changelog. The falsifier: the win must survive a fresh re-measure on the same sample — if it only shows under a gamed benchmark, it is a hymn.
