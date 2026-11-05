# claim-003 — the heading count as a host count

```yaml
id: claim-003
claim: A heading count is not a host count — the number flatters the page and measures nothing.
failure: The failure is a release page that counts its own headings and calls them hosts; the count reproduces on the page and nowhere in the installer.
mechanism: docs/measurement.md §2, the install-targets note; the installer's own host list replaces the heading count.
sample: the host count at the v1.17.0 release — the installer's list and the README heading count, both read on 2026-10-15; floor one reproduced count; the heading count did not reproduce the list.
control: the installer's own host list, read from `setup`, which reproduces; the heading count did not.
halves: formed=red (the heading count and the installer's list disagreed on the first reading); fresh=red (the counts table replaced the heading count with the installer's list, and the mismatch stayed red in the prose)
falsifier: If the heading count reproduces the installer's host list, it is a measurement; it did not.
carved: 2026-10-15
receipt: python scripts/check-measurement --check-doc
disposition: RETIRE refusal=docs/measurement.md:99 pattern=P-005
```

## The failure

A README grows a heading per host, the headings drift, and a page that counts them starts reporting a number that looks like coverage. The number is real — it counts something — and the something is not the host list. A reader sees fourteen and believes the installer ships fourteen; the installer ships ten.

This is the hymn the pack caught first: a count with no command behind it, written by the same hand that wanted the number to be bigger.

## The refusal

The counts audit refused it in the open: the install-targets row reads the installer's own host list, not a README heading, because a heading count is a hymn. The rule and the refusal are the same table's first pass, which is why the card is dated to that day.

The refusal is counted in the only way the house accepts: the replacement command reproduces the number, and the heading count does not.

## Why it retires and does not park

A park is for a claim the record cannot yet seat. This claim was seated, counted, and refused: the heading count failed to reproduce the host list on the first and the second reading. There is no sample left to collect. It becomes an archive row — `P-005`, the unbacked number — and the name stays so no page repeats it under a new coat.

The retirement is not a punishment of the page. It is the page's receipt: the number it carries now has a command beside it, and the command is the one the installer's own list answers to.

## What the archive keeps

The killing fact: the heading count and the installer's list disagreed, and the row was rewritten to read the installer instead of the page. The number is kept, the coat is gone, and the next release page that wants a host count reads the installer.
