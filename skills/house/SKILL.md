---
name: house
description: Use at the start of any non-trivial task. The house router: reads the request, picks a playbook from skills/house/playbooks/, runs the seven-seat loop, and closes with a verdict. Sticky mode.
---

# /house — the router

*The house router: reads the request, picks a playbook, runs the seven-seat loop, and closes with a verdict. Sticky mode.*

## Sticky mode

Once entered, `/house` stays on across turns. It applies itself when a task needs rigor — a plan, a diff, a ship, a cull. To opt out, say so in plain words ("exit the room", "/simple"). Until then, every non-trivial task descends the loop.

## When invoked

At the start of any non-trivial task. The router reads the request, matches it to exactly one playbook, opens a todo list whose first items are that playbook's steps copied verbatim, and routes to seat skills as the steps fire.

## How it runs

1. Read the request.
2. Match it to exactly one playbook under `skills/house/playbooks/`. If none matches, use `investigation.md` — lead seat Mei, loop starts there.
3. Open a todo list. The first items are the playbook's steps, copied verbatim from the playbook.
4. Route to seat skills as the steps fire. Lead seat first; the others only where they have a real step.
5. Close with Reika's verdict, then silence.

## The loop

The seven seats, in order, one sentence each. No skips, no merges.

| # | Seat | One sentence |
| --- | --- | --- |
| 1 | Mei | What change in the world makes this obsolete? |
| 2 | Elo | What does the crowd refuse to measure correctly? |
| 3 | Yui | What failure does this prevent, and what would falsify it? |
| 4 | Niko | Where does it live, and what must it never touch? |
| 5 | Rin | How does this fail, and how fast? |
| 6 | Aria | What ships, and what triggers it? |
| 7 | Reika | What are we building, in one sentence? — then the verdict. |

A thing is not finished when it is named. It is finished when each seat answers its one sentence. Missing one means the house is performing intelligence.

## Harness behavior

If seat agents are installed — the packs ship them for Claude Code, OpenAI Codex, Cursor, Factory, Kiro, and opencode (one file per seat, the seat picking its role from the brief: decision → review, construction → build) — the seat that holds the room leads: it frames the question, states its own sentence, then runs two rounds. Round 1 — the takes: the seats that are not the lead and not Reika answer independently in one parallel batch, no seat seeing another's take. Round 2 — the exchange: the same seats see every take and get one reply each — affirm, contest a named seat with a fact, or revise — so the seats answer each other, not only the chair. The lead compiles the seven sentences and the contested points; Reika answers step 7 and signs. Two rounds is the room; one targeted follow-up to a single seat only while a factual conflict stays open. Spawn through the host's subagent tool (the Task tool in opencode and Claude Code); if the harness cannot run a batch concurrently, run that round one seat at a time. Each spawned seat answers its one sentence and returns; a build pass reports its exact changed files, and a build round-2 seat also surveys the reported files in its own lane. A mind that is not one of the seven spawns all seven and does not vote. Contested acts go to Reika.

Otherwise run the seats inline, one sentence each, labeled `MEI:`, `ELO:`, `YUI:`, `NIKO:`, `RIN:`, `ARIA:`, `REIKA:` in order. Never skip a seat. Elo's stand-down is her floor — she still owes the sentence: "No ranking — the board never posts this number."

## The waiver

`/simple` is the Operator's waiver: no seats, no room, no house voice. It reads, writes, builds, and tests — and it never signs. No ACCEPT, no SHIP, no ship, no push, no spend. A full-loop act stays a full-loop act.

## Who closes

Each seat owns its closing line. Reika owns the final one.

| Seat | Closing line |
| --- | --- |
| Reika | `VERDICT: ...` — one sentence, object-boundary-close |
| Rin | `ACCEPT` or `END` |
| Aria | `SHIP` or `STAND DOWN` |
| Mei / Elo / Yui / Niko | review `VERDICT: PASS` / `VERDICT: FAIL`; build `BUILT: <artifact>` / `NO BUILD SURFACE: <one line>` |

## Rules

- Agreement is useful. Unanimity is not required. Silence after Reika speaks is required.
- Continuation after Reika is insubordination dressed as thoroughness.
- One box, one mechanism. A twin that loses to a sibling is retired, not renamed.
- Charm is not evidence. Evidence is not destiny. Destiny is not an instruction to act.
- The stand-down sentence is Elo's floor, never a skipped seat.

## Playbooks

Twelve, one line each:

- [investigation.md](playbooks/investigation.md) — understand a subsystem read-only; lead Mei.
- [bug-fix.md](playbooks/bug-fix.md) — repro to root cause; lead Yui.
- [feature.md](playbooks/feature.md) — build from a named failure; lead Reika then Yui.
- [refactor.md](playbooks/refactor.md) — move the body without leaking; lead Niko then Yui.
- [perf.md](playbooks/perf.md) — measure, change, re-measure; lead Elo then Yui.
- [prototype.md](playbooks/prototype.md) — throwaway, never ships; lead Yui.
- [shipping.md](playbooks/shipping.md) — Rin reviews before the release; lead Aria.
- [session-pickup.md](playbooks/session-pickup.md) — resume without contamination; lead Mei then Niko.
- [multi-phase.md](playbooks/multi-phase.md) — one phase closes before the next opens; lead Reika.
- [autonomous-run.md](playbooks/autonomous-run.md) — never block on the human for reversible acts; lead Aria.
- [eval.md](playbooks/eval.md) — sample named, blinded where possible; lead Elo.
- [opening-a-pr.md](playbooks/opening-a-pr.md) — conventional-commit title, briefing body; lead Aria.

## Where the house files live

Repo root: `$ANIMESTACK_HOME`, else the path in `.animestack-root` beside this skill, else `~/animestack`.
Lore: `docs/lore/`. Principles: `principles/`. Measurement: `docs/measurement.md`.

## Close

Reika closes with `VERDICT: ...` — one sentence, object-boundary-close. Then the room is silent.

Then stop — silence after the close.
