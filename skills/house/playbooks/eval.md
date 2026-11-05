# Eval

## When

- "does this actually work"
- scoring a candidate or a change against a dataset
- measuring a model, a mechanism, or a rank on a fresh sample

## The loop

Lead: Elo.

- **Elo** — What does the crowd refuse to measure correctly? MEASURE: name the sample, the denominator, and the rule. Blind the sample where possible. Produces the eval design.
- **MechaPip** — What has this pattern done before? RETRIEVE the kin before the eval is designed: `python scripts/check-patterns`, the row in `patterns/registry.json`. A prior sample on the same shape is a measurement already paid for; a no-match parks the candidate with a dated review.
- **Yui** — What failure does this prevent, and what would falsify it? The eval is the second sample. Name the falsifier: what result would retire the candidate. Produces the falsifier and the claim card at `claims/claim-NNN-<slug>.md` (`docs/claim-standard.md`), on the eval surface: the split, the sample, the score.
- **Niko** — Where does it live, and what must it never touch? The eval data is quarantined from training data; no leakage across the boundary. Produces the cage.
- **Rin** — How does this fail, and how fast? The failure is the eval being tuned to the metric, or the sample leaking. Produces ACCEPT or END on the eval.
- **Aria** — What ships, and what triggers it? Run the eval; the score is the ship. SHIP or STAND DOWN.
- **Reika** — What are we building, in one sentence? Close: the number is a measurement or a hymn. `VERDICT: ...`.

## Gates

- The sample is named and, where possible, blinded.
- No leakage between eval data and anything the candidate saw.
- The falsifier is written before the eval runs.
- The claim card validates: `python scripts/check-claim --check` — the floor is stated before the score, and a THIN reading is named, never quoted.

## Close

Reika closes: `VERDICT: ...` — measurement, or hymn.

## Notes

A number without a named sample is a hymn. The falsifier is pre-registered before the victory lap: if the candidate only wins on the sample it was tuned to, the eval retired it. A below-floor sample parks the claim with its date; the card carries the floor and the review date, and the archive waits for a counted refusal.
