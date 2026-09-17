# Session Pickup

## When

- "where was I"
- resuming a repo after time away
- picking up another engineer's in-flight work

## The loop

Lead: Mei then Niko.

- **Mei** — What change in the world makes this obsolete? Read the tree and the decision record; name what changed since the last session and what is now stale. Produces the weather read.
- **Niko** — Where does it live, and what must it never touch? Confirm the state is where it should be; freeze the edit surface if needed; no test environment drinking production data. Produces the body check.
- **Yui** — What failure does this prevent, and what would falsify it? If there is in-flight work, name its failure and check its second sample. Produces the mechanism status.
- **Rin** — How does this fail, and how fast? The failure is resuming stale work as if no time passed. Produces ACCEPT or END on the resume.
- **Reika** — What are we building, in one sentence? Close: what is the one next thing. `VERDICT: ...`.

## Gates

- The state is confirmed present and unmixed before any edit.
- The decision record is read, not assumed.
- The one next thing is named before work starts.

## Close

Reika closes: `VERDICT: ...`.

## Notes

A session that starts without reading the record is a session that renames a failure it never saw. State dirs never mix; a pickup that cannot confirm the state stands down.
