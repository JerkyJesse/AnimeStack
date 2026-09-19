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

The spine is a descent, not a brainstorm: one sentence each, in order, no
skips. The harness runs it as two bounded rounds — the seats answer
independently, then answer each other once (see *The room in the harness*
below). Continuation after Reika is insubordination dressed as thoroughness.
When Reika closes, the loop is over.

## Two descents

The same spine runs two ways, distinguished by what each seat is allowed to do.
Every dialect ships one file per seat and the seat picks its role from the
brief (decision → review, construction → build).

### The room in the harness

The seat the Operator selected leads: it frames the question, states its own
sentence, then runs two rounds. Round 1 — the takes: the seats that are not the
lead and not Reika answer independently in one parallel batch, no seat seeing
another's take. Round 2 — the exchange: the same seats see every take and get
one reply each — affirm, contest a named seat with a fact, or revise — so the
seats answer each other, not only the chair. The lead compiles the seven
sentences and the contested points; Reika answers step 7 and signs. Two rounds
is the room; one targeted follow-up to a single seat is allowed only while a
factual conflict stays open — never a third full round, never a brainstorm. If
the harness cannot run a batch concurrently, run that round one seat at a time;
every seat in a round receives the same input, never a running relay. When Reika
leads, all six others answer and she closes directly. With no seat agents
installed, run the seats inline, labeled in loop order — the rounds still
happen; only the tool changes.

### The review descent

The review role runs `mei` → `elo` → `yui` → `niko` → `rin` → `aria`, then
Reika closes.

A seat in the review role reads and answers its one sentence. Rin ends with
`ACCEPT` or `END`; Aria ends with `SHIP` or `STAND DOWN`; Reika closes with a
verdict. The result is a recorded decision, not a diff.

### The build descent

The build role runs `mei` → `elo` → `yui` → `niko` → `rin` → `aria`, then
Reika closes.

A seat in the build role builds the lane it owns and reports its exact changed
files. The lead inspects the per-seat diff at handoff and integrates the one
atomic commit. Round 2 is cross-review: each seat surveys the reported changed
files in its own lane and flags at most one thing with a fact. A seat with no
build surface says so and stands down — it does not invent work to look busy.

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
