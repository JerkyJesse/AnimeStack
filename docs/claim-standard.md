# The Claim Standard

*Status: canon-grade · The page beside canon §XXII. The canon carries the shape; this page carries the teeth: ten fields, one card, one gate, and a park that is dated before it is believed.*

A ship is an announcement. A claim is a receipt.

The house ships the way it thinks: someone falls in love, someone opens the knife, and the record is what survives both. This page is the knife, written down. It says what a claim must carry before the room believes it, what a number must look like before it may be called a measurement, what happens to a first sample that goes red, and how a house with no crowd to settle its wagers still settles them.

The sentence the card cannot survive without is the seat's own: **what failure does this prevent, and what would falsify it?** Both halves of that sentence, or you have a collage. Name it after it survives.

## 1. The claim card

A claim is one file: `claims/claim-NNN-<slug>.md`. Ten fields and the id that names the card, in one fenced block, then the prose that explains it. The block is the machine copy; the prose is the reader's copy; the gate reads the block and refuses prose that argues with it.

```yaml
id: claim-000
claim: one sentence — the assertion the record is asked to settle
failure: one sentence — the failure class the change removes
mechanism: what changed, at file:line
sample: what was counted, n, window-end date, and the floor stated before the count
control: the same box with the change stripped, and what it did
halves: formed=<green|red|thin|unrun> …; fresh=<green|red|thin|unrun> …
falsifier: one ordinary sentence that would kill it
carved: YYYY-MM-DD — the day the falsifier was written
receipt: the command that reproduces the count
disposition: SHIP | PARK review=YYYY-MM-DD | RETIRE refusal=<path:line> | THIN — with pattern=<P-###|A-###>
```

One line each, and what the gate does with it:

| Field | It carries | The gate refuses |
| --- | --- | --- |
| `id` | The card's name, `claim-NNN`, matched to its filename | A malformed or duplicated id |
| `claim` | The assertion, one sentence | An empty sentence |
| `failure` | The failure class it removes, one sentence | An empty failure |
| `mechanism` | What changed, at file:line | A mechanism that names no path the tree can resolve |
| `sample` | What was counted, how many, the window's end date, and the floor written before the count | A sample with no date, or no floor |
| `control` | The same box with the mechanism removed, and what it did | An absent control, a control that is the mechanism, or the word "none" |
| `halves` | Two states: formed-on and fresh | A half with no state; a ship with a half that is not green |
| `falsifier` | One ordinary sentence, carved before the count | An empty falsifier |
| `carved` | The day the falsifier was written | A date after the sample — a caption, not a test |
| `receipt` | The command that reproduces the count | A command whose path the tree cannot resolve, or an unstubbed card |
| `disposition` | `SHIP`, `PARK` with a review date, `RETIRE` with a counted refusal, or `THIN` | A park with no review date, a retire with no counted refusal, a thin card quoting a result, a disposition with no `pattern=` |

The `pattern=` citation is the prior-art trace: every card names the nearest row in `patterns/registry.json`, so a claim arrives with its kin already retrieved. No kin, no claim — MechaPip's floor is a sentence, not a skipped step.

## 2. The hymn catalogue

A hymn is a number that flatters a story. The catalogue is closed on purpose; a hymn not on this list is still a hymn, and the list is where the argument starts.

1. **A count with no command.** The pack's own first refusal: `grep -c '^### ' README.md` dressed as a host count (`docs/measurement.md:99`). It counts headings. It measures nothing.
2. **A benchmark only the author ran.** One hand, one machine, no second run: a receipt with no witness.
3. **A suite that passes on the old code too.** The control closes the gap, so the change was not the mechanism.
4. **"All green" with no tail.** The color is not the count.
5. **A survivor count with no denominator.** The trials that failed are the denominator, and a headline that omits them is a story about a story.
6. **Stars, downloads, followers, applause.** The crowd is not a scale.
7. **A check that cannot fail.** It watched nothing red, so it is decoration with an exit code.
8. **A number quoted from a THIN sample.** Below the card's own floor, the reading is named, never quoted.
9. **A median with no n.** A denominator wearing a decimal point.
10. **A falsifier written after the result.** The caption that pretends it was a test.

Two of these are already in the pack's archive with their numbers: the heading count (`P-005`) and the self-counted literal (`P-004`). The archive is not a museum; it is the catalogue's evidence.

## 3. The park law

A first sample that goes red does not delete the memory.

- **The artifact is deleted in the same commit.** A losing mechanism does not stay in the tree under a new name, a flag, or a promise deferred. Law 10 is the deletion; law 14 is the reason the deletion is not a burial.
- **The card stays, dated.** It keeps its red half, its killing number, its `carved` date, and a `review=` date. That card is the park: alive, readable, and owed an answer on its date.
- **The archive keeps only a counted refusal.** A card becomes an archive row — a `P-###` — only when a counted sample refused it, never on a first look. Until then the park sits below the archive, in the same registry, marked `PARKED`.
- **Nothing is renamed.** A second attempt cites the parked card's id in its own `pattern=` line. A failure with a name is a lesson; a failure without one returns wearing a better coat.
- **The park is read at the frame.** Every room opens with the record read, and a park whose review date has passed is named in the open — a park is not a filing cabinet.

The house keeps its own refusals the same way. A claim that misses, a check that went red, a design that failed its control: the number stays, the coat goes, the date is written.

## 4. The floor

There is no imported threshold. A number borrowed from another house's ledger would be a private fact wearing a public coat, and this pack carries none.

The card states its own floor, in the `sample` field, before the count: how many units make a verdict, what the unit is, and what would be THIN. The floor is reproducible — a reader can rerun the count and check the arithmetic — and it is stated before the sample, never chosen to fit it. Raising a floor on evidence is discipline; lowering one on appetite is a hymn with a date.

Below the floor, the reading is **THIN**: named, never quoted, never promoted. A THIN card is a claim with a sample too small to settle it — it parks, with its review date, or it goes back for a bigger sample. It does not get a sentence that sounds like a verdict.

## 5. The four clauses that replace a crowd

The house has no exchange to settle its claims, so the record does the settling. Four clauses make that honest:

1. **The settlement is the counted sample.** Not a price, not a poll, not a feeling in the room. Every claim names the command that produced its count, and the count is the settlement.
2. **The control is the counterfactual.** The same box with the change removed. If the control closes the gap, the change was not the mechanism. No control, no claim.
3. **The halves are split by time, and the second half belongs to someone else.** The formed-on half is where the claim was built. The fresh half is a sample the claim never saw — a later window, a clean checkout, another hand's run. One half and a story is not a result.
4. **The bar sizes; it does not bury.** The floor decides how much weight a claim earns and whether it ships, parks, or retires. It never deletes the card, and it never promotes a claim on a first look.

The cold re-run is the witness: a second hand runs the receipt and gets the count. A self-certified green is not a pass.

## 6. The seven surfaces

A claim lives on one surface, and every surface names its unit and its receipt. A claim on an unnamed surface is a hypothesis wearing a jersey.

| Surface | The unit it counts | The receipt it owes |
| --- | --- | --- |
| Code | A behaviour, a defect, a case fired | The test command and its tail |
| Docs | A claim against the tree — a count, a path, a version | The gate that reads the tree |
| Release | A version, a page set, a tag | The release chain's sweep table |
| Eval | A scored item on a held-out sample | The eval command, the sample, the split |
| Performance | A measurement on one harness, before and after | Both numbers, same sample, same harness |
| Security | An attack that must fail, or a leak that must not resolve | The red-once case and its refusal |
| Install | A host that installs, and a dry run that writes nothing | The installer's check mode |

The surface is not decoration. A code claim settled on a docs gate is a category error, and the card's `mechanism` and `receipt` fields are where the error becomes visible.

## 7. Three worked cards

- **`claims/claim-001-the-claim-standard.md` — SHIP.** The standard itself. The sample is the gate's own red-once suite: the refusals watched red before the gate was trusted, then the clean run on the live cards. Control: the v1.17.0 tree, where a ship was an announcement and no card existed.
- **`claims/claim-002-house-vs-simple.md` — PARK.** The pack's oldest claim, the one in `docs/measurement.md` §5: a `/house` session catches a defect that a plain session ships. It has never been run at its own floor. It parks, dated, with the sample it must count and the window it must close — the house's first public act under its own standard is to park its own claim.
- **`claims/claim-003-heading-count-hymn.md` — RETIRE.** A metric the record refused: a heading count dressed as a host count, killed by the installer's own list. The refusal is counted, the number is kept, and the name stays in the archive so no page repeats it.

Three dispositions, one instrument. A house that can show its own burial next to its own park and its own ship is not performing intelligence.

## 8. The gate

```
python scripts/check-claim --check     # the gate: schema, ordering, disposition, receipts
python scripts/check-claim --count     # how many cards the registry holds
python scripts/check-claim --list      # one line per card: id, disposition, kin, due
python scripts/check-claim --rerun     # re-run the receipts that can be re-run, and report each exit
```

Exit 0 is clean, 1 is a refusal (with the reason named), 2 is usage. The gate is stdlib only, reads no network, and never writes: the card is the author's, the gate is the reader's. `--rerun` executes only the receipts the house allows to be replayed — `python scripts/…` and `python -m pytest …` — and skips its own name so a receipt cannot call the gate that is reading it.

A red gate is a hold, never a bypass. The claim does not ship until the gate is green, and the card's `receipt` is the tail a second hand can reproduce.

## 9. Who owns what

- **Yui writes the card.** The failure, the mechanism, the falsifier, the halves. She may fall in love; she may not be excused from the falsifier.
- **Rin owns the floor.** The card states its floor; Rin says whether the stated floor earns a verdict, and the failure mode the claim accepts.
- **Elo audits the number.** What is counted, on what sample, and whether the number is a measurement or a hymn.
- **MechaPip keeps the kin.** The `pattern=` citation resolves against the registry; no match is a recorded finding, and a no-match parks with a date.
- **Niko owns the body.** A claim whose surface cannot hold the change is not a claim yet; the cage comes before the count.
- **Aria owns the contact.** The card ships with the change or the change stands down.
- **Reika signs.** The card is evidence; the verdict is hers.

## Close

The knife is sharpened before the meal, not after. Write the failure first, carve the falsifier before the heat, run the control, split the halves, keep the receipt — and when the first sample goes red, delete the coat and keep the card. That is the whole standard. Everything else is a template for it.

> A beautiful curve that cannot walk into a second sample is an archive entry, not a ship. The second sample can wait — that is a line this house does not say twice.
