# Shipping

## When

- "ship it"
- "open the PR and merge"
- a feature or fix is green and the room has not yet reviewed it for contact

## The loop

Lead: Aria.

- **Rin** — How does this fail, and how fast? REVIEW the diff first: failure modes in ordinary words, the bugs CI misses, the trust boundaries. No ship without an ACCEPT. Produces ACCEPT or END.
- **Aria** — What ships, and what triggers it? SHIP: run the tests, order the commit stack, one accepted unit per commit. Produces the release, SHIP or STAND DOWN.
- **Reika** — What are we building, in one sentence? Close: the ship goes or it does not. `VERDICT: ...`.

## Gates

- Rin ACCEPTs before the release. A ship with an END is refused.
- Tests green. One accepted unit per commit. No force-push to a default branch.
- The revision is reported by the SHA the gates measured, not a wave number.

## Close

Reika closes: `VERDICT: ...` after Rin's ACCEPT and Aria's SHIP.

## Notes

Rin reviews before the release. A ship that skips the failure review is a deploy waiting to become a failure surface. The release is the exact window and action — contact, not a speech.
