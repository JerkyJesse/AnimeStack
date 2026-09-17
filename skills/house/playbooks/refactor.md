# Refactor

## When

- "refactor this module"
- "split this god object"
- "migrate these callers off the legacy API"

## The loop

Lead: Niko then Yui.

- **Niko** — Where does it live, and what must it never touch? SHAPE the target: data flow, boundaries, one concern per module. Freeze the edit surface if needed. Produces the target architecture.
- **Yui** — What failure does this prevent, and what would falsify it? The failure is the legacy API's leak. BUILD the new shape; migrate every caller; delete the legacy API in the same wave. No compatibility layers. Produces the migration.
- **Rin** — How does this fail, and how fast? The failure is a half-migration — callers on both shapes, a compatibility layer that outlives the change. Produces ACCEPT or END.
- **Aria** — What ships, and what triggers it? Run the tests across migrated callers. SHIP or STAND DOWN.
- **Reika** — What are we building, in one sentence? Close. `VERDICT: ...`.

## Gates

- Every caller migrated. The legacy API is deleted, not deprecated.
- No compatibility layer survives the wave.
- Full test suite green on the new shape.

## Close

Reika closes: `VERDICT: ...`.

## Notes

A refactor that leaves the old API behind a shim is not a refactor; it is two bodies in one box. One box, one mechanism. Migrate and delete in the same wave or do not start.
