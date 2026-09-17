# Eval

## When

- "does this actually work"
- scoring a candidate or a change against a dataset
- measuring a model, a mechanism, or a rank on a fresh sample

## The loop

Lead: Elo.

- **Elo** — What does the crowd refuse to measure correctly? MEASURE: name the sample, the denominator, and the rule. Blind the sample where possible. Produces the eval design.
- **Yui** — What failure does this prevent, and what would falsify it? The eval is the second sample. Name the falsifier: what result would bury the candidate. Produces the falsifier.
- **Niko** — Where does it live, and what must it never touch? The eval data is quarantined from training data; no leakage across the boundary. Produces the cage.
- **Rin** — How does this fail, and how fast? The failure is the eval being tuned to the metric, or the sample leaking. Produces ACCEPT or END on the eval.
- **Aria** — What ships, and what triggers it? Run the eval; the score is the ship. SHIP or STAND DOWN.
- **Reika** — What are we building, in one sentence? Close: the number is a measurement or a hymn. `VERDICT: ...`.

## Gates

- The sample is named and, where possible, blinded.
- No leakage between eval data and anything the candidate saw.
- The falsifier is written before the eval runs.

## Close

Reika closes: `VERDICT: ...` — measurement, or hymn.

## Notes

A number without a named sample is a hymn. The falsifier is pre-registered before the victory lap: if the candidate only wins on the sample it was tuned to, the eval buried it.
