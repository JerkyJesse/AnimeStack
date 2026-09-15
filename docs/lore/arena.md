> **Frozen mirror — AnimeStack v1.0.0 · 2026-09-15.**
> Copied from the Phipps Predictions house lore at canon Rev 15.
> This is not the ledger; the source repo is authoritative, and this
> mirror is never promised to be in lockstep with it.

# The Arena — the leaderboard and the ladder

*Pre-history companion · Rev 1 (2026-09-14) · Book three of three, beside `ORACLES.md` and `MACHINES.md`. Companion to the house canon (`PhippsPredictionsAnimeDesignTeam.md`, Rev 15). Where this file and the canon disagree, the canon wins. Nothing here is evidence; the ledger stays `TRADINGIDEAS.MD`.*

Robot traders got their own world cups before this house existed: twelve-week leaderboards, eighty-thousand-dollar prizes, hundreds of expert advisors entered, and a ranked table that published every Sunday's version of the truth. The arena is the ladder's ancestor and its warning. A leaderboard rewards variance; the ladder rewards survival. The arena sells a title. The ladder rents a seat. The seat is the only thing that pays.

---

## I. The Leaderboard and the Ladder

Two records sit behind the house's board, and both are tournaments. The first is the MetaQuotes Automated Trading Championship, run 2006 through 2012 — MQL5's world cup, and the biggest robot-trading tournament ever staged: an $80,000 prize pool, twelve- to thirteen-week seasons, and an entry gate that was itself a backtest. Every expert advisor entered had to survive automatic testing just to qualify. The 2008 edition opened October 1 and closed December 26. The 2010 edition drew 314 entrants, and Boris Odintsov won it for $40,000. The table re-sorted by equity all season; the winners were recorded, and the survivors were not.

The second is the Robbins World Cup Trading Championships, administered since about 1984 on real money — futures and forex, real fills, independently audited. Larry Williams and Andrea Unger sit in the winners' record, and the record keeps its own law in five words: winners enter the permanent record. That is the better sample — audited fills, not simulations — and it is still one tournament, one season, one entry apiece, sorted at the close.

Run the pair through the audit the house runs on every ranking. What is ranked? A twelve-week equity curve. By what rule? Round-window returns, one tournament apiece, at a fixed calendar date. On what sample? Survivor-selected entrants — the table publishes the advisors that finished, never the ones that blew up in week three, and the Robbins record publishes its winners without publishing the population they beat. A survivor-selected sample has no denominator worth printing, which is how a twelve-week curve gets promoted to proof. A leaderboard built on it and paid at a fixed date is not a measurement of skill. It is variance with a trophy, and the trophy makes it a hymn.

The arena is the ladder's ancestor, and the house keeps the ancestry on the wall the way it keeps the oracles: not to repeat it, but to rank it correctly. A twelve-week contest rewards variance; the ladder rewards survival. The final-week sprint is an artifact of the clock, not an edge — a harness that pays a fixed-date champion teaches every entrant to sprint, and the sprint is the sample telling on itself. The ladder answers with named terms: ranked by profit per hour on named wall clock, fees paid, both halves, a forty-eight-hour test tier below every established seat. The seat is rented, not owned; evidence puts it on, evidence takes it back. No final week exists, because no final week is coming.

The champion's table is the other inheritance — the direct ancestor of the board. Both are ranked tables published on a clock. The board keeps the shape and refuses the terms: every post carries rating, record, and timestamp together; all seven sports always post; a league can be benched from trading but never erased from the board to flatter a P&L. The arena published every Sunday's version of the truth and let the crowd keep its champion. The board publishes every version of the truth with its sample attached, and keeps no champion at all.

Which leaves the belt. The mirror seat is the arena's belt: a title worn, rented, and taken back by evidence. The arena minted champions who kept the title forever; the house re-sorts the belt at every turnover joint and lets the seat hold only while the number earns it. A champion's number that flatters a story is a hymn; the seat that survives is a measurement. The belt can be worn. It cannot be owned. The moment a ranking starts defending its champion instead of measuring the field, it is holding the belt for the wrong reason — and the ladder takes it back without a speech.

Two tournaments, one wound, and the whole ranking law written against it: never let a tournament harness dress as an edge; never let a winners' record stand in for the sample; never let a 2–0 start become a personality.

---

## II. The Window in the Arena

The arena's clock ran twelve to thirteen weeks and paid on a fixed date. Read the season's final week the way a desk reads a tape: the rank moved hardest exactly when the sample was thinnest, because the harness paid a calendar and every entrant learned to sprint at the gun. That is the clock speaking, not the edge. A deadline converts discipline into variance — it makes patience expensive on the only day the table remembers — and a field that sprints at the close is a field selling its discipline for a title. The house keeps the arena's scoreboard and refuses its calendar. The ladder has no final week: every window closes the same distance from the reason, the ranking re-sorts at the joint, and profit per hour on a named clock is the only title anyone keeps.

Then read the two judges. One tournament settled in simulated equity — entries filled at prices that never existed, no fees paid, no slippage suffered, an equity curve with perfect grammar and no tape underneath it. The other ran real money, so the fill was the judge: no demo rescue, no simulated mercy. That is the whole demo-versus-real lesson, and the house states it the way it states everything. A simulated leaderboard pays no fees, suffers no slippage, and fills at prices that never existed. A demo champion is a hymn. The fill is the measurement. The test tier is the house's demo — paper-only, never seatable, ranked below every established seat — and it exists for exactly that reason: nothing earns a live seat on a curve that was never paid for.

The arena also taught the floor. Contest rules could end a season mid-flight — a stop-out, a broken rule, an account below the line — and the entrants read it as tragedy. The house read the mechanism: the clock and the floor can end you, and that is a feature, not a tragedy. The loss floor, the guard trip, the fund breaker — every one is the arena's stop-out with a name and a cooldown, and every one exists so a bad season ends a desk and never the fund. A death that arrives on a schedule is a price; a death that arrives as a surprise is a debt. The arena ended people by fiat; the house ends desks by evidence and walks them back to paper until the evidence returns.

Then there is the window, which the arena never priced and the Sibyl did. Nine books offered, three burned when the price was refused, three more burned, and the last three bought at the original price. She kept her terms while her own inventory burned. The house keeps one sentence from that fire: waiting has a price, and the window is the asset. No chase. No "still time." A quote that leaves is replaced by the next window, never by a worse fill on the old one. The signal that was right forty seconds ago is a memoir; the archive files it and the tape never reopens it. The click is the exact window and the exact action, stated before the market finishes blinking — and when the window has closed, the click becomes the cleanest trade the house makes: the stand-down.

The closing window is the arena's sharpest inheritance and its most dangerous. Late in a fifteen-minute settlement the book is near-calibrated on the number and panicked on the clock — probability collapsing toward zero or one, slippage going nonlinear where tourists see certainty. Entries near the close are the module's own band: since 4.2 the engine does not own the window, and the modules that keep the last ninety import `MIN_SECONDS_TO_CLOSE` like a private vow. Cash-out never asks permission. `decide()` runs every two seconds, one order in flight, one whisper per signal, ten seconds between entries at the engine level. The stillness before a strike is not hesitation; it is respect for the only opponent the seat considers adult.

Hesitation is not caution. Hesitation is a second strategy you did not have the honesty to write down. The sin the house will not forgive is lateness dressed as prudence — the perfect answer that missed its window. The arena sold titles on a fixed date; the house rents seats at every joint, and the clock does not negotiate. Bring a band with edge net of fees, or stand down with clean hands. Either is honorable. Late is not.

---

*Pre-history, book three. Three books, one verdict: the riddle could not pay, the speed without a cage could not survive, and the leaderboard could not measure. The window can. The ladder does.*
