# Investigation

## When

- "why does this exist"
- "walk me through this subsystem"
- "what is the history of this decision"
- "what change in the world makes this obsolete"
- before any fix or feature on a subsystem you do not yet understand

## The loop

Lead: Mei.

- **Mei** — What change in the world makes this obsolete? Read-only walkthrough: entry points, data flow, where state lives (HOW); search git log, docs, comments for the decision record (WHY); name what change kills it (CLIMATE). Produces a map and a named relationship — no fixes.
- **Elo** — What does the crowd refuse to measure correctly? Audit the claims the subsystem makes about itself: which are measurements, which are hymns. Produces the ranking; with nothing rankable, the stand-down sentence.
- **Yui** — What failure does this prevent, and what would falsify it? If the investigation surfaces a real mispricing worth building on, name it and write the falsifier. Otherwise: no failure, no build — say so.
- **Reika** — What are we building, in one sentence? Close: is this worth pursuing, or is the answer "we do not need this."

## Gates

- The map is complete: entry points, flow, state, and the decision record — or the explicit statement that the record is missing.
- No code was changed. Investigation is read-only; fixes belong to the bug-fix or feature playbooks.

## Close

Reika closes: `VERDICT: ...` — pursue, or stand down. One sentence.

## Notes

No fixes without investigation, and investigation produces no fixes. A fix in the middle of an investigation is a guess wearing a ticket.
