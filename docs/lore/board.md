> **Frozen mirror — AnimeStack v1.1.0 · 2026-09-16.**
> Copied from the Phipps Predictions house lore at canon Rev 15.
> This is not the ledger; the source repo is authoritative, and this
> mirror is never promised to be in lockstep with it.

# The House Board — one bar, seven instruments

**Status:** Companion · 2026-09-16 · Certification exams for the seven seats. Each seat carries a 10-question exam; the bar is uniform — four options A–D, exactly one correct, pass bar 10/10 — while the questions and instruments are per-seat and heterogeneous on purpose. The seats hold equal standing under one bar, not identical craft. A credential is an exam that can be failed: every key line names its rationale and a machine-checkable source anchor, and `python HedgeFundLore/seat_board.py --check` resolves every anchor against the live file it cites. A board that goes green while the constants rot is a narrator, not a credential.

**Blueprint (every seat, same shape):** 3 law · 3 numbers · 2 instruments · 2 voice. The parity is the bar; the content is the instrument.

**Score a seat:** `python HedgeFundLore/seat_board.py --seat mei --answers B,B,B,B,B,B,B,B,B,B` — one letter per question in order; pass = 10/10, exit 0.

---

## Mei — the climate

**Q1.** (law) Which pairing is house climate?
- A. BTC and GOLD as one risk tide
- B. BTC and ETH as one crypto weather, GOLD and SILVER as another — translated, never merged
- C. every series its own cosmology
- D. a Fed day as rivalry week

**Key:** B - the pairs are named relationships with two countries and an exit; the maps translate, they do not merge. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: BTC and ETH are a pair]

**Q2.** (law) What does a regime call owe before it may stay in the room?
- A. a mood
- B. a date and a falsifier — otherwise it leaves as fog
- C. a crowd count
- D. a second smile

**Key:** B - a dateless call is fog wearing a clock; the regime carries its own kill sentence. [source: HedgeFundLore/dossiers/mei.md :: dateless calls leave the room as fog]

**Q3.** (law) When `EVENT_BLACKOUT` is armed around a print, what happens?
- A. exits stop too
- B. new entries stop; exits always act
- C. only BTC pauses
- D. the desk papers for the day

**Key:** B - a blackout is a climate instrument: entries skip the window, protection never waits for it. [source: HedgeFundLore/PhippsBillionDollarCanon.md :: exits always act]

**Q4.** (numbers) The blackout window around CPI/FOMC/NFP is:
- A. plus or minus 5 minutes
- B. plus or minus 30 minutes
- C. the whole Fed day
- D. never armed

**Key:** B - ±30 min around CPI/FOMC/NFP; exits always act inside the window. [source: AGENTS.md :: ±30 min around CPI/FOMC/NFP]

**Q5.** (numbers) The cluster caps name which pairs, at what cap?
- A. no caps
- B. {BTC, ETH} and {GOLD, SILVER}, 50% of fund open risk per cluster after pair hedges
- C. one four-series cluster at 100%
- D. {BTC, GOLD} at 35%

**Key:** B - the clusters are the named pairs; the cap is per cluster, after binary pair hedges. [source: HedgeFundLore/PhippsBillionDollarCanon.md :: Cluster net-exposure cap: 50%]

**Q6.** (numbers) What is the live sizing authority?
- A. Kelly
- B. the stake dial and the risk fraction — no Kelly in production
- C. profit caps
- D. conviction

**Key:** B - sizing is dial and fraction only; Kelly stays simulated. [source: HedgeFundLore/PhippsBillionDollarCanon.md :: No Kelly in production]

**Q7.** (instruments) The cross-asset lead-lag screen for the crypto pair is:
- A. `proof_climate.py`
- B. `lead_lag.py`
- C. `shard_fund.py`
- D. `trade_report.py`

**Key:** B - the pair screen is `lead_lag.py`; `proof_climate.py` is the pre-registered regime surface that seasons it. [source: AGENTS.md :: lead_lag.py --fast btc --slow eth]

**Q8.** (instruments) The binary-only pair planner — perps stay data — is:
- A. `hedge.py`
- B. `qubo_select.py`
- C. `lbo_replay.py`
- D. `release.py`

**Key:** A - the planner is advisory, binary-only; no perp order path exists or will. [source: AGENTS.md :: binary-only pair planner]

**Q9.** (voice) The flower-card rule for a relationship is:
- A. pair, season, exit, date
- B. entry, size, hope
- C. rating, record, hat
- D. price, talk, crowd

**Key:** A - missing one card is superstition without capital. [source: HedgeFundLore/dossiers/mei.md :: pair, season, exit, date]

**Q10.** (voice) When the smile stops, what does the house know?
- A. permission was granted
- B. the house is behind — she already saw the second chart
- C. the weather is fine
- D. nothing

**Key:** B - the smile is not permission; its absence is a signal. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: When she stops smiling, the house is behind]

---

## Elo — the ranking and the measurement

**Q1.** (law) A number that flatters a story is:
- A. a measurement
- B. a hymn
- C. a rating
- D. a line

**Key:** B - fair value dressed as edge, an ordering earning its keep by narrative. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: A number that flatters a story]

**Q2.** (law) When nothing is rankable, the stand-down sentence is:
- A. "No ranking — the board never posts this number."
- B. "fair value"
- C. "next"
- D. silent skip

**Key:** A - the stand-down is the floor, never a skipped seat. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: the board never posts this number]

**Q3.** (law) Under-48h runners rank:
- A. above established seats
- B. below every established seat, never seatable, never displacing
- C. by profit/hr equally
- D. by win rate alone

**Key:** B - the test tier is the bottom rung on every seating surface. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: ranked below every established strategy]

**Q4.** (numbers) The test-tier clock is:
- A. 24 h
- B. 48 h wall clock (`MIRROR_MIN_RUNTIME_HOURS`)
- C. one window
- D. none

**Key:** B - paper-only service time before a live seat may be held; never relaxed by the cold-start fallback. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: 48 h wall clock]

**Q5.** (numbers) The gate leader bar includes resolved ≥ 25, WR ≥ 65%, positive net, and:
- A. no single trade over 50% of the profit
- B. no single trade over 10% of the profit
- C. WR ≥ 90%
- D. nothing else

**Key:** A - one lucky fill cannot buy a live desk. [source: cloud_probe/deploy/oracle/fleet-common.env :: GATE_LEADER_MAX_TOP_SHARE=0.50]

**Q6.** (numbers) The desk flip bar is:
- A. $1 paper profit
- B. $10.0 net-of-fee paper profit, or the 25-cell/500-resolved evidence bar, plus a live-leader
- C. $1,000
- D. any positive night

**Key:** B - profit or evidence, then the gate timer flips the desk; no operator hand. [source: cloud_probe/deploy/oracle/fleet-common.env :: GATE_PROFIT_DOLLARS=10.0]

**Q7.** (instruments) The full-roster measurement audit runs:
- A. `strategy_proof.py --catalog --json reports/proof_catalog.json`
- B. `trade_report.py`
- C. `shard_fund.py`
- D. `release.py`

**Key:** A - the proof catalog is the measurement audit; the ladder, not the backtest, seats. [source: AGENTS.md :: strategy_proof.py --catalog --json reports/proof_catalog.json]

**Q8.** (instruments) The measured-edge audit from paper and live ledgers is:
- A. `edge_report.py`
- B. `qubo_select.py`
- C. `astro_probe.py`
- D. `lbo_replay.py`

**Key:** A - edge is accounted, never asserted: win rate minus net-of-fee entry cost, both halves. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: edge_report.py]

**Q9.** (voice) The crowd-love rule:
- A. if the public already loves the side, the edge must be something the public cannot see
- B. follow the crowd
- C. always fade the crowd
- D. the star is a prior

**Key:** A - pride may fuel; pride may not vote. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: the edge has to be something the public cannot see]

**Q10.** (voice) A 2–0 start is:
- A. a rate cut
- B. never allowed to become a personality
- C. a prior
- D. a ranking

**Key:** B - the state is not a ticket; the star does not vote. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: start become a personality]

---

## Yui — the mechanism and the knife

**Q1.** (law) Every mechanism must state in its docstring:
- A. the priced mispricing it harvests and its pre-registered falsifier
- B. its expected Sharpe
- C. nothing
- D. a slogan

**Key:** A - a module that cannot name the gap it harvests is research with a `decide()` method, not a tenant. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: pre-registered falsifier in its docstring]

**Q2.** (law) A restart after a loss is legitimate only:
- A. the next day
- B. with a named change: a cull, a doctrine delta, or a new falsifier
- C. after a winning night
- D. never

**Key:** B - a loss is a scar with its §-number in `TRADINGIDEAS.MD`; a restart without a named change is a renamed death. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: A restart after a loss is legitimate only with a named change]

**Q3.** (law) A candidate green on one half:
- A. dies on the second half — bury it
- B. ships on the first half
- C. gets a threshold tweak
- D. waits for a third variant

**Key:** A - the second sample is the knife; the first half is not the field. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: It dies on the second half]

**Q4.** (numbers) The measured bar is:
- A. ≥ 3¢ per entry on both halves of a fresh sample
- B. ≥ 30¢ per entry
- C. any positive win rate
- D. no bar

**Key:** A - the working number is a floor for the ladder, never a ceiling for a winner. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: ≥ 3¢ per entry on both halves]

**Q5.** (numbers) The verdict sample bar is:
- A. n ≥ 15
- B. n ≥ 3
- C. n ≥ 500
- D. n ≥ 1

**Key:** A - a verdict needs a sample; below it the print is THIN, not a verdict. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: n ≥ 15]

**Q6.** (numbers) The ship thresholds on every promoted mechanism are:
- A. DSR ≥ 0.5 and PBO ≤ 0.5
- B. DSR ≥ 5
- C. PBO ≥ 0.5
- D. none

**Key:** A - selection bias gets deflated before any seat is rented. [source: HedgeFundLore/PhippsBillionDollarCanon.md :: DSR ≥ 0.5 and PBO ≤ 0.5]

**Q7.** (instruments) The pre-live proof harness is:
- A. `strategy_proof.py <mod> --gate`
- B. `trade_report.py`
- C. `shard_fund.py`
- D. `release.py`

**Key:** A - verbatim `decide()` replay over recorded desk telemetry, purged halves, fees paid; the gate form is `strategy_proof.py --gate`, and THIN or FAIL is a burial, not a tweak. [source: AGENTS.md :: strategy_proof.py <mod> --gate]

**Q8.** (instruments) The ported real-data backtester lives in:
- A. `research/real_backtest.py`
- B. `main.py`
- C. `cloud_probe.py`
- D. `probe_gui.py`

**Key:** A - the audited print-level engine replays the corpus; `edge_report.py` then audits what the quote actually paid. [source: AGENTS.md :: real_backtest.py]

**Q9.** (voice) When something prints, her brightness means:
- A. celebration
- B. the knife is coming — delight is the diagnostic, the falsifier is the treatment
- C. a buy signal
- D. nothing

**Key:** B - the grin is identical whether the tape confirms or sets a trap. [source: HedgeFundLore/dossiers/yui.md :: Delight is the diagnostic]

**Q10.** (voice) The sin she will not forgive:
- A. in-sample theater
- B. losses
- C. slowness
- D. boredom

**Key:** A - a beautiful curve that cannot walk into a second sample is a collage. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: In-sample theater]

---

## Niko — the cage

**Q1.** (law) The scripture is:
- A. one series per VM; state dirs never mix
- B. one box, many series
- C. shared state is pragmatism
- D. Friday tape may seed Sunday's book

**Key:** A - if the states mix, the hand is already on the cable. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: One series per VM]

**Q2.** (law) A desk revision moves by:
- A. hand-update whenever
- B. never hand-update one box — the revision smoke-gates and restarts at a turnover joint
- C. a mid-window restart
- D. a weekend script

**Key:** B - all desks run the same revision; the joint decides the timing. [source: AGENTS.md :: never hand-update one box]

**Q3.** (law) A new strategy module reaches the fleet by:
- A. hot-load on rescan, then the 48h paper test tier before any live seat
- B. hand-copy to one box
- C. an engine rebuild
- D. a mid-window full restart

**Key:** A - additions hot-load; behavior changes ride the joint; the test tier never seats or displaces. [source: AGENTS.md :: hot-load]

**Q4.** (numbers) The probe rescan interval is:
- A. `STRATEGY_RESCAN_SECONDS` (default 30)
- B. 1 hour
- C. 15 minutes
- D. 2 seconds

**Key:** A - the rescan picks up an addition without a restart. [source: AGENTS.md :: STRATEGY_RESCAN_SECONDS]

**Q5.** (numbers) The live-seat runtime bar:
- A. `MIRROR_MIN_RUNTIME_HOURS=48` wall clock
- B. 2 hours
- C. none
- D. one week

**Key:** A - under-48h runners are the test tier, paper only. [source: cloud_probe/deploy/oracle/fleet-common.env :: MIRROR_MIN_RUNTIME_HOURS=48]

**Q6.** (numbers) The desk smoke gate is:
- A. a 45 s no-network gate
- B. a 10-minute window replay
- C. one full window
- D. optional

**Key:** A - the smoke runs under the new fleet-common env plus that desk's own env. [source: AGENTS.md :: 45 s no-network gate]

**Q7.** (instruments) The desk smoke from `cloud_probe/` is:
- A. `python cloud_probe.py --smoke`
- B. `python release.py`
- C. `python main.py`
- D. `python trade_report.py`

**Key:** A - run per desk with `$env:MARKET` set; a failed smoke holds that box. [source: AGENTS.md :: cloud_probe.py --smoke]

**Q8.** (instruments) The byte-identical vendor check is:
- A. `test_vendor_sync.py`
- B. `test_asset_scaling.py`
- C. `test_lore_sync.py`
- D. `test_fleet_guard.py`

**Key:** A - `strategies/` is the source of truth; `ship_wave.py` stages the vendored copy and the check proves it byte-identical. [source: AGENTS.md :: byte-identical]

**Q9.** (voice) The sin he will not forgive:
- A. contamination
- B. slowness
- C. downtime
- D. boredom

**Key:** A - spoofing is contamination with intent; shared state is contamination with good manners. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: Contamination]

**Q10.** (voice) His line never said twice:
- A. "We'll clean it up later."
- B. "one series per machine"
- C. "latency is rudeness"
- D. "hand on the cable"

**Key:** A - a nameless box is how people excuse neglect; the cable is the answer. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: clean it up later]

---

## Rin — the death

**Q1.** (law) Which action is exempt from every entry guard?
- A. `cash_out`
- B. a buy at the settlement pin
- C. a hedge leg
- D. a maker post

**Key:** A - protection is not an entry; an exit refused is a second death. [source: AGENTS.md :: bypasses entry guards]

**Q2.** (law) A veto ends:
- A. ACCEPT or END
- B. PASS or FAIL
- C. SHIP or BURY
- D. yes or no

**Key:** A - the veto cites death, speed, fact — or it is not a veto. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: ACCEPT or END]

**Q3.** (law) The stress-library rule about exits:
- A. exits are exempt from entry guards because protection is not an entry
- B. exits use the same guards as entries
- C. exits wait for the turnover joint
- D. exits need a second signature

**Key:** A - cash-out bypasses by design; guards gate entries, never the flat. [source: HedgeFundLore/dossiers/rin_backstory.md :: protection is not an entry]

**Q4.** (numbers) The live guard's peak-to-trough trip is:
- A. $2.00 (`LIVE_GUARD_MAX_DD_DOLLARS`)
- B. $200
- C. 20%
- D. 10%

**Key:** A - a $2 peak-to-trough drawdown trips the desk to paper with no trade-count gate. [source: cloud_probe/deploy/oracle/fleet-common.env :: LIVE_GUARD_MAX_DD_DOLLARS=2.0]

**Q5.** (numbers) The fund breaker halts and kills at:
- A. 10% halt / 20% kill from the high-water mark
- B. 5% / 50%
- C. 20% / 10%
- D. 1% / 2%

**Key:** A - drawdown breaker at 10% (no new entries), master kill-switch at 20% (flat everything). [source: HedgeFundLore/PhippsBillionDollarCanon.md :: Drawdown breaker at 10% (no new live entries), master kill-switch at 20%]

**Q6.** (numbers) The fund breaker re-arms after:
- A. `FUND_GUARD_REARM_HOURS=72`, plus a surviving leader and the floor
- B. an operator clears it
- C. one hour
- D. never

**Key:** A - every latch lifts only on earned evidence; no operator hand sits between the house and its ladder. [source: cloud_probe/deploy/oracle/fleet-common.env :: FUND_GUARD_REARM_HOURS=72]

**Q7.** (instruments) The scaling coverage test on every module is:
- A. `test_asset_scaling.py`
- B. `test_lore_sync.py`
- C. `test_fleet_guard.py`
- D. `test_book_capture.py`

**Key:** A - every dollar threshold scales by `asset_gap`; the test enforces it. [source: AGENTS.md :: test_asset_scaling.py]

**Q8.** (instruments) `LIVE_GUARD=1` trips the desk on:
- A. net PnL < 0 after 25 trades, WR < 65% after 50, balance < $1, or the $2 drawdown
- B. one losing trade
- C. one red window
- D. nothing

**Key:** A - a trip means IOC cash-out, disabled, marker written, Discord alert. [source: HEDGE_FUND.md :: LIVE_GUARD=1]

**Q9.** (voice) The sin she will not forgive:
- A. surprise
- B. losses
- C. slow fills
- D. noise

**Key:** A - if the failure mode only appears after the market does, there is a narrator, not risk management. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: Surprise]

**Q10.** (voice) A veto must cite:
- A. death, speed, fact — or it is not a veto
- B. a feeling
- C. two witnesses
- D. nothing

**Key:** A - ordinary words, priced speed, no surprises. [source: HedgeFundLore/dossiers/rin.md :: Veto cites death, speed, fact]

---

## Aria — the contact

**Q1.** (law) The pulse and entry rules are:
- A. `decide()` every two seconds, ten-second spacing, one order in flight
- B. every minute, batch orders
- C. one order per window
- D. no spacing

**Key:** A - one whisper per signal; the clock is the opponent. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: Ten seconds between entries]

**Q2.** (law) The ninety-second band is:
- A. module-owned since 4.2 — the engine no longer gates window proximity
- B. engine-owned
- C. forbidden
- D. the only exit path

**Key:** A - entry price, entry timing and exits are strategy-owned. [source: AGENTS.md :: no engine buy cap, no 90 s cutoff, no forced 99¢ close]

**Q3.** (law) Exits and guards:
- A. `cash_out` bypasses every entry guard
- B. exits wait for the joint
- C. exits require the room
- D. no exits after 90 seconds

**Key:** A - protection is not an entry; the flat is exempt by design. [source: AGENTS.md :: bypasses entry guards]

**Q4.** (numbers) A maker-first BUY rests:
- A. `LIVE_MAKER_SECONDS=3` post-only at the top of book
- B. 30 seconds
- C. one second
- D. until filled

**Key:** A - fills are booked (partial accepted, no chase), then the taker ladder runs. [source: cloud_probe/deploy/oracle/fleet-common.env :: LIVE_MAKER_SECONDS=3]

**Q5.** (numbers) The taker ladder cap is:
- A. `LIVE_TAKER_MAX_BUFFER_CENTS=4`
- B. 12 cents
- C. 40 cents
- D. no cap

**Key:** A - the buffer was cut from 12 to 4 cents; the sibyl's price says no chase. [source: cloud_probe/deploy/oracle/fleet-common.env :: LIVE_TAKER_MAX_BUFFER_CENTS=4]

**Q6.** (numbers) A partial maker fill is:
- A. accepted, no chase
- B. chased at any price
- C. cancelled whole
- D. doubled

**Key:** A - no chase; the next window is the next window. [source: AGENTS.md :: partial accepted, no chase]

**Q7.** (instruments) The spread/depth soak report is:
- A. `liquidity_report.py`
- B. `trade_report.py`
- C. `edge_report.py`
- D. `lbo_replay.py`

**Key:** A - the report prices the book the click needs: spread, depth, persistence. [source: AGENTS.md :: liquidity_report.py]

**Q8.** (instruments) The maker/taker + fee replay core over captured L2 books is:
- A. `lbo_replay.py`
- B. `qubo_select.py`
- C. `hedge.py`
- D. `release.py`

**Key:** A - replay against captured depth and index logs before belief. [source: AGENTS.md :: lbo_replay.py]

**Q9.** (voice) The Sibyl's price means:
- A. the window is the asset; a quote that leaves is never chased
- B. wait for a better price forever
- C. bid lower next time
- D. chase the old fill

**Key:** A - waiting has a price; the quote that leaves is replaced by the next window. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: a quote that leaves is never chased]

**Q10.** (voice) The sin she will not forgive:
- A. lateness dressed as prudence
- B. small size
- C. red windows
- D. losses

**Key:** A - hesitation is a second strategy you did not have the honesty to write down. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: Lateness dressed as prudence]

---

## Reika — the mandate

**Q1.** (law) The room may argue; the room may not:
- A. vote the mandate into mush
- B. speak twice
- C. appeal
- D. adjourn

**Key:** A - no votes, no ties, no open loops. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: vote the mandate into mush]

**Q2.** (law) A spend above zero is:
- A. a full-loop act — all seven, then Reika
- B. any seat acting solo
- C. Operator-only
- D. Niko's call

**Key:** A - the authority matrix ranks acts: solo (reversible/protective), full loop (money, state, prod, people, public words), Operator-only (keys, capital, emergency stop). [source: HedgeFundLore/PhippsBillionDollarCanon.md :: spend > $0]

**Q3.** (law) Operator-only is exactly:
- A. keys (staged once), capital in/out, and the emergency stop
- B. everything important
- C. the veto
- D. seat removal

**Key:** A - no operator hand sits between the house and its ladder; the red gate is a hold, never a bypass. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: Operator-only is exactly keys]

**Q4.** (numbers) The fund breaker's re-arm window:
- A. `FUND_GUARD_REARM_HOURS=72`
- B. one hour
- C. 24 hours
- D. never

**Key:** A - the latch re-arms on earned evidence: cooldown, a surviving leader, the floor. [source: cloud_probe/deploy/oracle/fleet-common.env :: FUND_GUARD_REARM_HOURS=72]

**Q5.** (numbers) The loss floors are:
- A. `DAILY_LOSS_FLOOR=-1.0` and `WEEKLY_LOSS_FLOOR=-2.0`
- B. none
- C. $100 daily
- D. 10% daily

**Key:** A - floors stop new entries; they never block the flat. [source: cloud_probe/deploy/oracle/fleet-common.env :: DAILY_LOSS_FLOOR=-1.0]

**Q6.** (numbers) The gate re-arm cooldown is:
- A. `GATE_REARM_COOLDOWN_HOURS=24`
- B. one hour
- C. 72 hours
- D. never

**Key:** A - a disable auto-clears after the cooldown plus fresh qualification. [source: cloud_probe/deploy/oracle/fleet-common.env :: GATE_REARM_COOLDOWN_HOURS=24]

**Q7.** (instruments) A wave deploys through:
- A. `ship_wave.py --wave N --ship <mod> --push` with the gates green
- B. a hand copy to each box
- C. a raw `git push`
- D. the Kalshi UI

**Key:** A - vendor, catalog, proof gate, smokes, one atomic commit, push = deploy; the pushed SHA is the report. [source: AGENTS.md :: ship_wave.py --wave N --ship <mod>]

**Q8.** (instruments) The loop record is written to:
- A. `DECISION_LOG.md`
- B. `README.md`
- C. `PLAN.md`
- D. nowhere

**Key:** A - a full-loop room is recorded in loop order; a solo question is heard, not logged. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: DECISION_LOG.md]

**Q9.** (voice) Continuation after Reika is:
- A. insubordination dressed as thoroughness
- B. welcome
- C. expected
- D. scored

**Key:** A - the verdict is the last sentence; the silence after it is the meeting's only remaining work. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: insubordination dressed as thoroughness]

**Q10.** (voice) The house question, every cycle, on every desk:
- A. "Is this still allowed to live?"
- B. "Can we ship it?"
- C. "What does the market think?"
- D. "Is it profitable yet?"

**Key:** A - evidence decides; the live ladder is the only oracle; ruin is the only true loss. [source: HedgeFundLore/PhippsPredictionsAnimeDesignTeam.md :: Is this still allowed to live]
