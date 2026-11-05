# The Machines — the speed religion

*Pre-history · Rev 1 (2026-11-05) · Book two of three, beside `ORACLES.md` and `ARENA.md`. Companion to the house canon §XV. Where this file and the canon disagree, the canon wins. Nothing here is evidence; the evidence record is the seat record and the decision log.*

Between the oracle's riddle and the arena's leaderboard, the machines arrived. A wearable computer learned the roulette wheel; a phone line became an exchange; an exchange became a colocation cage; a cage became a war. The age named the moment the street noticed: warring bots, the fastest network making the deal, stability intended and fragility delivered.

The house descends from that lineage and refuses its religion. **Speed is rented. The cage is ours. The record is the only oracle.**

---

## I. The machine age

The first machine in this history was a shoe. Las Vegas, 1961: a wearable computer was strapped to a leg and read the roulette octant — which eighth of the rim the ball was about to favor. The casino saw a gambler. The wheel saw a sensor. Every desk since descends from that machine, and the house keeps the original where it keeps every true ancestor: not on an altar, in the cage.

Read the wheel before you romanticize the machine. Roulette was a known distribution with a paid house edge — not a prophecy, a mechanism. The machine did not guess the number; it measured the wheel — rotor and ball timed, the rim divided into octants, the arithmetic bet. That is the whole lineage in one sentence: the machine that measured its own wheel lived, and the machine that read someone else's spin was a story with a battery. An edge is paid only while the measurement holds.

Then the wheel went electronic and learned to move. Nasdaq went fully electronic in 1983; execution times fell from seconds to milliseconds and then to microseconds by 2010; colocation and direct market access moved the machines beside the matching engine, and the latency race left the wire — fiber to microwave on the long routes, line-of-sight towers on hilltops, then shortwave, then satellite, each hop a shorter lie about distance. The scoreboard did not stay quiet: in 2009, high-frequency firms were about two percent of the firms and about seventy-three percent of equity order volume; by 2012 their profits had fallen from roughly five billion dollars a year to roughly a quarter of that. The race ate its own edge, the way every race must — each latency advantage is rentable, and the day it is rented by everyone it is an expense, not an edge. That is not a scandal. That is the finish line of a winner-take-all race.

The abuse taxonomy is where the age confesses. **Quote stuffing:** flooding the book to blind the other machines. **Spoofing and layering:** ghost orders placed to be feared and cancelled before they can fill — one trader's tapes became the mounted specimen, and the orders were a large share of what the screen showed. **Order-property strategies:** mining order age and displayed size to read what other participants intend. **News parsed faster than a human can read**, so the machine trades the word before the sentence ends. One family, one sin: a machine reading the wrong wheel — other people's orders instead of its own distribution — and calling it cleverness. Contamination with intent.

The software age took the same religion and gave it a code review. Call it the **velocity cult**: ship fastest, break things, let the users be the test suite. The race ate its edge in the same way. The shortcuts compounded, the incidents did too, and every fast team discovered it had built a system nobody could safely change. The modern taxonomy is the older one translated:

- **Quote stuffing is a benchmark that measures itself.** A suite that asserts its own runtime, a dashboard that counts its own events, a "performance regression" gate that runs on the machine's idle hour. The instrument is not measuring the system; it is measuring the instrument, loudly, so nobody looks at the system.
- **Spoofing is the agent that reads another's orders.** A generated patch that copies a sibling repo's output; a model trained on the repository's own merged changes and then graded on the same changes; a test that asserts the implementation it was written from. The machine is reading the wrong wheel — someone else's distribution — and calling it inference.
- **Order-property strategies are the review that mines the author's intent.** The approval that reads the description instead of the diff, the standup where the design is settled by confidence, the incident review that reconstructs what the author meant rather than what the state did. Intent is not state.
- **News parsed before the sentence ends is the changelog written after the deploy.** The announcement outruns the change; the release note describes the intention, not the build. The word was traded before the sentence landed.

The house descends from that lineage and refuses its religion. The fastest network makes the deal; the fastest network is also for rent, and the landlord changes. So the house rents latency and owns the cage:

- **One surface per job.** The tree, the gates, the record, the release. State never crosses a name, and a surface that borrows another's truth has already leaked.
- **Every artifact is stamped.** The revision, the date, the source hash. An artifact that cannot say what it was built from is a rumor with a checksum.
- **A revision moves at the joint.** All surfaces run the same revision; no surface is hand-edited into a different truth. The release cut is the joint, and a change that lands outside it is a hotfix wearing a costume.
- **The exchange is not the edge.** The fastest runner in the room is not the mechanism; it is the runner. The mechanism is the thing the record can price, and the record is the only oracle.
- **The plug stays in a hand.** Contamination is betrayal with a friendly face, and the friendliest face it wears is the shortcut. Niko's hand is on the cable because a cage nobody can unplug is not a cage; it is a habit.

The cage lineage runs from the first shoebox as much as from the arms race, because the shoebox survived by measuring one wheel and keeping its own numbers. The fleet is the body; the instruments are tenants; the record is the memory; the evidence ladder is the oracle.

---

## II. Other people's failures

Every house archives failures. The ones that survive also keep the neighbors'. This part is an archive the house did not have to fill: eleven other people's failures, adopted so no session here repeats one under a new name. Each is written the way a failure table is written — the failure, the speed, what it takes — and read before a new change is sized. The full register lives in `docs/lore/ARCHIVE.md`; the ids are the record.

### A-001 — Knight Capital, 2012

A deploy left a legacy flag armed; the machines woke the old code and for forty-five minutes sent orders nobody had sized and nobody could stop. Roughly four hundred forty million dollars was gone by the close, order flow went to the competition by morning, and the firm was sold. **Failure:** the deploy is a failure surface. **Speed:** forty-five minutes. **Takes:** the firm's capital and its independence.

The software lesson is not "test more". It is that a release is state, and state can be armed. A deploy that cannot name every flag it carries is a deploy that is carrying one it forgot.

### A-002 — Ariane 5, 1996

Flight software inherited from Ariane 4 converted a horizontal velocity that fit in sixty-four bits into a sixteen-bit value. The conversion overflowed, both inertial units failed, and the launcher broke up about forty seconds into flight. **Failure:** inherited code in a new body. **Speed:** forty seconds. **Takes:** the rocket, the payload, and the assumption that a reused line is a tested line.

A library is not tested by having been used. It is tested by having been used *here*, on this input, in this body. The envelope is part of the code.

### A-003 — Therac-25, 1985 to 1987

A radiotherapy machine's control software raced its operator's keystrokes; the display reported a malfunction while the dose went out. Patients were injured and killed while the screen said the run had stopped. **Failure:** the display was trusted over the state. **Speed:** one keystroke. **Takes:** the patient, and the assumption that a green screen means safe.

The interface is a claim about the state, and the claim is not the state. A system that reports success without reading its own body is a narrator with a power supply.

### A-004 — Challenger, 1986

Engineers had watched the solid rocket joints erode across earlier flights and had been argued into treating the erosion as normal. The launch was called on a cold morning; the joint failed seventy-three seconds in. **Failure:** a known defect renamed as a margin. **Speed:** seventy-three seconds. **Takes:** the crew, and the institution's habit of hearing its own reassurance.

Normalization of deviance is a language failure before it is an engineering failure. The first time the anomaly is renamed "acceptable", the record stops being readable, and every later launch is argued against a memory that has already been edited.

### A-005 — Denver, 1994 to 1995

The airport's automated baggage system was commissioned as one enormous integration with no stage that could fail small. It missed the airport's opening, ran months late, and was partly dismantled after costing far more than its plan. **Failure:** integration without a seam. **Speed:** months. **Takes:** the opening, the budget, and the project's credibility.

A system that can only be tested whole can only fail whole. The seam is not a compromise; it is the unit of a test that can refuse something.

### A-006 — Healthcare.gov, 2013

The federal marketplace opened to national traffic with no end-to-end load test that could have refused the launch. A small fraction of visitors completed an application in the first weeks; the repair took months. **Failure:** the load test was a promise, not a gate. **Speed:** the first hour. **Takes:** public trust and a year of the program.

A load test that runs at a tenth of the load is a rehearsal with the understudy. The gate is only a gate if its red would have stopped the launch, and the room has to say so before the launch, not after.

### A-007 — LTCM, 1998

A fund of prize-winning models was levered roughly twenty-five times into convergence trades. Russia defaulted, credit ran, spreads widened, and about four point six billion dollars of equity went in under four months. Fourteen banks rescued the book because its failure would have been theirs. **Failure:** a book that cannot be wrong until it is. **Speed:** weeks. **Takes:** the fund, its lenders, and the belief that the past is a forecast.

Certainty is the only position that fails whole. A model that assumes liquidity is a model that has never tried to leave.

### A-008 — The August 2007 quake

Quantitative funds that had never traded together lost together in one week: similar signals, similar positions, similar lenders. One delevered, sold what the others held, the marks moved, and the next margin call forced the next seller. **Failure:** a crowd of similar mechanisms is one position wearing several names. **Speed:** days. **Takes:** the cousins, and the word diversification as comfort.

Diversification among cousins is not diversification. Two services that share a library, a deploy, and an on-call rotation are one service with two names, and the incident will find the shared thing.

### A-009 — The Flash Crash, 2010

One large seller moved about four point one billion dollars of S&P 500 futures in twenty minutes into a book already leaving. Liquidity passed the same contracts back and forth, then withdrew; some issues printed at a penny. The tape recovered in minutes; the assumption did not. **Failure:** a market-order chain is not an exit plan. **Speed:** minutes. **Takes:** the belief that intraday liquidity is a noun.

Every system needs an exit that exists when the system is wrong. A rollback path that has never been run is a hope with a runbook; the exit is a feature, and features are tested.

### A-010 — Volmageddon, 2018

A product sold insurance on volatility while the market stayed calm. When the market moved, the note's own rebalancing demanded the futures it was short, and the spike fed the unwind; the note terminated down about ninety-six percent on the day it was held as protection. **Failure:** the hedge that ruins its holders is not a hedge. **Speed:** one session. **Takes:** the holders, the issuers' reputations, and the word hedge as comfort.

A protection whose own operation is the failure mode is not protection. A retry budget, a cache, a fallback: each is a claim that it will hold on the day it is used, and each has to be tested on that day, not on a calm one.

### A-011 — Sarao, 2010 to 2015

A single trader's spoofing orders were presented as the explanation for a market's behavior. The orders were real; the structure that made them profitable, and the field that read them as intent, were the larger fact. **Failure:** the myth is the second failure. **Speed:** years. **Takes:** the truth, and everyone who preferred the villain.

The story of one actor is cheaper than the story of the design. When an incident review names a person and stops, it has replaced the structure with a villain, and the structure is still there.

---

## III. What the era left in this pack

- **The cage.** `docs/lore/canon.md` §XIII: four surfaces, one revision, one preflight, and the rule that a surface never becomes a stage for another.
- **The joint.** `docs/lore/canon.md` §XIV: the release cut is the heartbeat, one change is in flight, the suite is the pulse, and shadow comes before main.
- **The adopted failure register.** A-001 through A-011 in `docs/lore/ARCHIVE.md`, each with its failure, speed, and what it takes.
- **The one sentence.** Speed is rented. The cage is owned. The record is the only oracle.

The plug stays in a hand because contamination is betrayal with a friendly face, and the friendliest face it wears is the shortcut. Renting speed and owning the cage is not caution; it is the only way a house survives being right twice.
