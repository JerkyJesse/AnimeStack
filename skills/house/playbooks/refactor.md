# Refactor

## When

- "refactor this module"
- "split this god object"
- "migrate these callers off the legacy API"

## The loop

Lead: Niko then Yui.

- **Niko** — Where does it live, and what must it never touch? SHAPE the target: data flow, boundaries, one concern per module. Freeze the edit surface if needed. Produces the target architecture.
- **Yui** — What wound does this exploit? The wound is the legacy API's leak. BUILD the new shape; migrate every caller; delete the legacy API in the same wave. No compatibility layers. Produces the migration.
- **Rin** — How is this allowed to die? The death is a half-migration — callers on both shapes, a compatibility layer that outlives the change. Produces ACCEPT or END.
- **Aria** — What is the click? Run the tests across migrated callers. CLICK or STAND DOWN.
- **Reika** — What are we allowed to want? Close. `VERDICT: ...`.

## Gates

- Every caller migrated. The legacy API is deleted, not deprecated.
- No compatibility layer survives the wave.
- Full test suite green on the new shape.

## Close

Reika closes: `VERDICT: ...`.

## Notes

A refactor that leaves the old API behind a shim is not a refactor; it is two bodies in one box. One box, one mechanism. Migrate and delete in the same wave or do not start.
