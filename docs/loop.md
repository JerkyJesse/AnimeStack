# The Design Loop

The loop is AnimeStack's operating spine. Every material decision descends
seven seats in fixed order, one sentence each. No skips. No merges. The loop is
the same on every surface — a bug, a refactor, a ship, a cull.

![The design loop](../assets/img/loop.svg)

## The seven steps

| Step | Seat | One sentence |
| --- | --- | --- |
| 1 | **Mei** | What change in the world makes this obsolete? |
| 2 | **Elo** | What does the crowd refuse to measure correctly? |
| 3 | **Yui** | What failure does this prevent, and what would falsify it? |
| 4 | **Niko** | Where does it live, and what must it never touch? |
| 5 | **Rin** | How does this fail, and how fast? |
| 6 | **Aria** | What ships, and what triggers it? |
| 7 | **Reika** | What are we building, in one sentence? — then the verdict. |

Each seat answers its one sentence. A thing is not finished when it is named;
it is finished when all seven sentences exist. Missing one means the house is
performing intelligence.

The spine is a descent, not a brainstorm. One sentence each, in order, no
skips; continuation after Reika is insubordination dressed as thoroughness.
When Reika closes, the loop is over.

## Two descents

The same spine runs two ways, distinguished by what each leaf is allowed to do.

### The review descent

`mei-review` → `elo-review` → `yui-review` → `niko-review` → `rin-review` →
`aria-review`, then Reika closes.

A review leaf reads and answers its one sentence. It never edits. Rin ends with
`ACCEPT` or `END`; Aria ends with `SHIP` or `STAND DOWN`; Reika closes with a
verdict. The result is a recorded decision, not a diff.

### The build descent

`mei-build` → `elo-build` → `yui-build` → `niko-build` → `rin-build` →
`aria-build`, then Reika closes.

A build leaf builds only the lane its seat owns and reports its exact changed
files. It never commits, never pushes, never spawns a room of its own. The
owning seat inspects the per-leaf diff at handoff and integrates the one atomic
commit. A leaf with no build surface says so and stands down — it does not
invent work to look busy.

## What each seat owns in the loop

- **Mei** names the climate and the obsolescence question. No fog as forecast.
- **Elo** ranks what the project must answer — the measurement audit: what is
  measured, by what rule, on what sample. The stand-down sentence is her floor,
  never a skipped seat: "No ranking — the board never posts this number."
- **Yui** names the failure and its falsifier. No failure, no mechanism.
- **Niko** names the body and what it must never touch. If the cage cannot
  hold it, it does not exist.
- **Rin** names the failure, the speed, what it takes — `ACCEPT` or `END`.
- **Aria** names the release or `STAND DOWN`. No philosophy after the clock has
  started.
- **Reika** chooses. Silence after her line is required.

## Solo authority

Reversible and protective acts are never delayed by the descent: Niko can
restart a box, Rin can trip a guard, Mei can call a freeze, Aria can stand
down a window, Yui can retire a loser with evidence, Elo can bench a league from
posting. The act is logged after the fact. Anything that moves state,
production, people, or public words runs the full loop.

## The waiver

The Operator may waive the room for one invocation with `/simple`: a plain
build mode with no seats, no descent, no house voice. It reads, writes, builds,
and tests — and it never signs. No `ACCEPT`, no `SHIP`, no push, no
spend. A full-loop act stays a full-loop act.

## Canon

The loop is written in the house canon: [canon.md](lore/canon.md) §V (The
Design Loop) and §XII (The Subagent Room). Where this page and the canon
disagree, the canon wins.
