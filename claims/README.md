# The claim registry

One card per claim. One gate over all of them. The standard is `docs/claim-standard.md`; this file is how the registry is read and how a card is added.

## What a card is

A claim card is a markdown file named `claim-NNN-<slug>.md`. It opens with one fenced block carrying the ten fields and the id that names the card, then prose that explains the claim to a stranger. The block is the machine copy; the prose is the reader's copy. The gate reads the block and refuses prose that argues with it.

The ten fields, in order:

```
id          claim-001
claim       one sentence — what the record is asked to settle
failure     one sentence — the failure class the change removes
mechanism   what changed, at file:line
sample      what was counted, n, window-end date, floor stated before the count
control     the same box with the change stripped, and what it did
halves      formed=<green|red|thin|unrun> …; fresh=<green|red|thin|unrun> …
falsifier   one ordinary sentence that would kill it
carved      YYYY-MM-DD — the day the falsifier was written
receipt     the command that reproduces the count
disposition SHIP | PARK review=YYYY-MM-DD | RETIRE refusal=<path:line> | THIN, with pattern=<P-###|A-###>
```

## What the dispositions mean

- **SHIP** — both halves are green, the control held, the receipt resolves, and the kin is named. The change goes into contact with its card.
- **PARK** — a first sample went red, or the sample does not exist yet. The card carries a review date; the artifact is deleted in the same commit; the card stays, dated, and the park is read at the frame.
- **RETIRE** — a counted sample refused the claim. The card carries the refusal's path:line; the archive keeps the number; the name does not come back under a new coat.
- **THIN** — the sample is below the card's own floor. The reading is named and never quoted. A THIN card does not carry a verdict.

Every card cites a `pattern=` row from `patterns/registry.json`: the nearest kin, already retrieved. No kin, no claim. A no-match is a recorded finding, and a no-match parks with a date.

## How to add one

1. Copy the block above into `claims/claim-NNN-<slug>.md`, with the next free number.
2. Write the falsifier first, and date it. A falsifier written after the count is a caption.
3. State the floor in `sample` before the count. There is no imported threshold: the floor is the card's, stated and reproducible.
4. Run the control. Write both halves down, whatever they are.
5. Run `python scripts/check-claim --check` and paste the tail into the build report.

## How the gate reads

```
python scripts/check-claim --check     # schema, ordering, disposition, receipts, hymns, stubs
python scripts/check-claim --count     # how many cards the registry holds
python scripts/check-claim --list      # one line per card: id, disposition, kin, due
python scripts/check-claim --rerun     # replay the receipts that can be replayed
```

Exit 0 is clean, 1 is a refusal with the reason named, 2 is usage. The gate is stdlib only, reads no network, and never writes. A red gate is a hold, never a bypass.

## What this registry is not

It is not the seat record. `record/seat_record.jsonl` counts conduct — credits and debts with receipts — and it stays the only append-only ledger in the house. A card carries evidence; the record carries conduct. A ship writes one credit through `python scripts/seat_record --event`, and the card is the receipt beside it.

This README is not a card. The gate counts cards, not prose.
