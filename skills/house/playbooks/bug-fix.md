# Bug Fix

## When

- "fix this bug"
- "this fails intermittently in production"
- a failing repro exists, or one can be written
- a CI failure with a stack trace

## The loop

Lead: Yui.

- **Yui** — What wound does this exploit? The wound is the failing repro. Reproduce as a failing test first. Ask why until the root cause is named. Fix at the root; no nil-check silencers. Produces the failing test, the root-cause sentence, and the fix.
- **Niko** — Where does it live, and what must it never touch? Confirm the fix lands in the right module and touches nothing it must not. Produces the boundary check.
- **Rin** — How is this allowed to die? Name the failure mode in ordinary words, and confirm the fix does not reopen a worse one. Produces ACCEPT or END.
- **Aria** — What is the click? Run the tests, one accepted unit per commit. Produces the verified fix, CLICK or STAND DOWN.
- **Reika** — What are we allowed to want? Close: ship the fix or send it back. `VERDICT: ...`.

## Gates

- The failing test passes on the fix and fails on the old code.
- No regression in the touched module's existing tests.
- The root cause is named in one sentence; the fix is at the root, not at the symptom.

## Close

Reika closes: `VERDICT: ...` after Rin ACCEPTs and Aria CLICKs.

## Notes

A fix without a repro is a story. A fix with a nil-check is a silencer, not a cure. The falsifier: the repro must fail before the fix and pass after — if it never failed, it was not the bug.
