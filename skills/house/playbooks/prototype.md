# Prototype

## When

- "spike this idea"
- "does this approach even work"
- throwaway exploration before any real build

## The loop

Lead: Yui.

- **Yui** — What failure does this prevent, and what would falsify it? BUILD the throwaway fast, from a named data shape, no production harness. Write the falsifier even here. Produces the prototype and its verdict.
- **MechaPip** — What has this pattern done before? RETRIEVE the kin before the verdict: `python scripts/check-patterns`, the row in `patterns/registry.json`. A question that was parked before returns with its review date, not as a fresh idea; a no-match parks with a dated review.
- **Niko** — Where does it live, and what must it never touch? The prototype lives in a scratch directory; it never touches production state. Produces the quarantine.
- **Rin** — How does this fail, and how fast? The failure is the prototype leaking into the real path. Produces ACCEPT or END on the quarantine.
- **Reika** — What are we building, in one sentence? Close: does the idea earn a real build, or does it fail here. `VERDICT: ...`.

## Gates

- The prototype is throwaway and is never shipped as-is.
- It touches nothing outside its scratch directory.
- The falsifier is written, so the prototype has a falsifier before it has a victory lap.
- The claim card is a `PARK` by construction — `python scripts/check-claim --check` — with the review date the answer is read on. A prototype never earns a `SHIP`.

## Close

Reika closes: `VERDICT: ...` — promote to a feature, or retire.

## Notes

A prototype is a question, not a product. It never ships; it earns a real build or it is thrown away. The archive is free here — cheaper to park a prototype than to maintain one. The card is the question's receipt: the failure it asked about, the falsifier it carried, and the date the answer is read.
