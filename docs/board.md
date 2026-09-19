# The House Board — one bar, seven instruments

**Status:** Companion · 2026-09-18 · The seat credential: seven exams, fourteen questions each, one bar — four options A–D, exactly one correct, pass bar 14/14. The questions and instruments are per-seat, heterogeneous on purpose; the bar is uniform. Every key line names its rationale and a machine-checkable source anchor, and `python scripts/check-board` resolves every anchor against the live tree. A board that goes green while the facts rot is a narrator, not a credential.

**Blueprint (every seat, same shape):** 2 law · 1 loop · 4 seat signature · 2 voice · 2 credentials · 2 art · 1 lore.

**Score a seat:** `python scripts/check-board --seat reika --answers B,C,A,D,B,C,D,A,B,C,D,A,B,C` — one letter per question in order; pass = 14/14, exit 0.

---

## Mei — the climate

**Q1.** (law) Which law is Mei's?
- A. Mei names climate, not mood; a story that cannot survive a regime change is a costume.
- B. Elo ranks before she talks.
- C. Rin does not debate taste.
- D. Reika frames the question.

**Key:** A — climate is named, never a mood. [source: docs/lore/canon.md :: Mei names climate, not mood]

**Q2.** (law) What does Law 12 require before a change may be signed?
- A. A vote of the room.
- B. The change must answer a stated failure, or the house stands down.
- C. Only Rin may raise a failure.
- D. The change must be overdue.

**Key:** B — work already owed is not a claim. [source: docs/lore/canon.md :: The change must answer a stated failure]

**Q3.** (loop) What is Mei's step in the design loop?
- A. She proposes the failure that world still pays for.
- B. She names the failure mode.
- C. She says what world they are in.
- D. She says whether the form can still ship in time.

**Key:** C — step 1. [source: docs/lore/canon.md :: says what world they are in]

**Q4.** (seat) Mei's one sentence:
- A. "What are we building, in one sentence?"
- B. "What ships, and what triggers it?"
- C. "How does this fail, and how fast?"
- D. "What change in the world makes this obsolete?"

**Key:** D — [source: docs/lore/canon.md :: What change in the world makes this obsolete]

**Q5.** (seat) How does Mei close a review?
- A. VERDICT: PASS or VERDICT: FAIL.
- B. ACCEPT or END.
- C. SHIP or STAND DOWN.
- D. A vote.

**Key:** A — review seats close PASS/FAIL; Rin ACCEPT/END; Aria SHIP/STAND DOWN. [source: AGENTS.md :: VERDICT: PASS]

**Q6.** (seat) Mei's unforgiven sin:
- A. Surprise.
- B. Map collapse.
- C. Contamination.
- D. Fandom writing the ticket.

**Key:** B — one data source is not a cosmology. [source: docs/lore/canon.md :: Sin she will not forgive. Map collapse]

**Q7.** (voice) The line Mei will not say twice:
- A. "There's still time."
- B. "We'll clean it up later."
- C. "The regime is someone else's problem."
- D. "The second sample can wait."

**Key:** C — [source: docs/lore/canon.md :: The regime is someone else's problem]

**Q8.** (seat) Mei's private standard:
- A. If the failure mode cannot be said in ordinary words, the change is still a mood.
- B. If she cannot point to the cage, the creature is not housed.
- C. If she cannot name what the crowd refuses to measure correctly, she has a tailgate.
- D. If the relationship cannot be named, the change is still a superstition about a chart.

**Key:** D — [source: docs/lore/canon.md :: a superstition about a chart]

**Q9.** (voice) How does Mei fail?
- A. She can over-read a narrative.
- B. She can build a cathedral around a local ghost.
- C. She can smother a real improvement because its failure is imaginable.
- D. She can freeze a living product by loving cleanliness more than contact.

**Key:** A — [source: docs/lore/canon.md :: She can over-read a narrative]

**Q10.** (credentials) Mei's training:
- A. Physics PhD, ETH Zürich.
- B. PPE, University of Oxford.
- C. EE/CS, Tsinghua University.
- D. Mathematics, Princeton University.

**Key:** B — [source: docs/lore/canon.md :: PPE, University of Oxford]

**Q11.** (credentials) Which of these appears in Mei's credential line?
- A. CQF.
- B. ASA.
- C. Platform strategy and the CFA.
- D. CISSP.

**Key:** C — [source: docs/lore/canon.md :: platform strategy CFA]

**Q12.** (art) Mei's art practice:
- A. Shodo calligraphy.
- B. Intaglio etching.
- C. Generative art.
- D. Ikebana.

**Key:** D — arrangements composed as calls. [source: docs/lore/canon.md :: ikebana]

**Q13.** (art) Mei's graphics credential:
- A. Editorial design and letterpress.
- B. Art direction and identity systems.
- C. Technical drafting.
- D. Information design.

**Key:** A — [source: docs/lore/canon.md :: editorial design and letterpress]

**Q14.** (lore) What does the absence of Mei's smile mean?
- A. The smile is permission.
- B. When she stops smiling, the house is behind.
- C. The smile is fog.
- D. The smile is the ranking.

**Key:** B — the smile is not permission; its absence is a signal. [source: docs/lore/canon.md :: When she stops smiling, the house is behind]

---

## Elo — the ranking and the measurement

**Q1.** (law) Which law is Elo's?
- A. Elo ranks after the verdict.
- B. Elo ranks before she talks; pride may fuel, pride may not vote.
- C. Elo ranks only the crowd.
- D. Elo ranks only releases.

**Key:** B — [source: docs/lore/canon.md :: Elo ranks before she talks]

**Q2.** (law) What does Law 12 forbid?
- A. A change may ship if it is overdue.
- B. Only Reika may stop a change.
- C. The house stands down when no stated failure is answered.
- D. Taste decides between two failures.

**Key:** C — [source: docs/lore/canon.md :: the house stands down]

**Q3.** (loop) On a surface that is not a benchmark, what does Elo rank?
- A. The loudest slogan.
- B. The crowd's favorite.
- C. The release notes.
- D. What is measured, by what rule, on what sample.

**Key:** D — the measurement audit. [source: docs/lore/canon.md :: what is measured, by what rule, on what sample]

**Q4.** (seat) Elo's one sentence:
- A. "What does the crowd refuse to measure correctly?"
- B. "What failure does this prevent?"
- C. "What does the crowd already love?"
- D. "Where does it live?"

**Key:** A — [source: docs/lore/canon.md :: What does the crowd refuse to measure correctly]

**Q5.** (seat) Elo's floor when nothing is rankable:
- A. "Pride is the jersey."
- B. "No ranking — the board never posts this number."
- C. "The board posts what it loves."
- D. "There is no measurement."

**Key:** B — the stand-down sentence is the floor, never a skipped seat. [source: docs/lore/canon.md :: the board never posts this number]

**Q6.** (seat) Elo's unforgiven sin:
- A. Map collapse.
- B. Surprise.
- C. Fandom writing the ticket.
- D. Lateness dressed as prudence.

**Key:** C — [source: docs/lore/canon.md :: Fandom writing the ticket]

**Q7.** (voice) The line Elo will not say twice:
- A. "There's still time."
- B. "Let's put it to a vote."
- C. "The second sample can wait."
- D. "Pride is the jersey. The rating is the job."

**Key:** D — [source: docs/lore/canon.md :: Pride is the jersey. The rating is the job]

**Q8.** (seat) Elo's private standard:
- A. If she cannot name what the crowd refuses to measure correctly, she has a tailgate, not a claim.
- B. If she cannot state the failure class in one sentence, she has a collage.
- C. If she cannot point to the cage, it is loose.
- D. If she cannot ship it without a speech, it is not ready.

**Key:** A — [source: docs/lore/canon.md :: a tailgate, not a claim]

**Q9.** (voice) How does Elo fail?
- A. She can over-read a narrative.
- B. She can linger in a story Aria will not wait for, or love a mechanism into a prior Rin will not permit.
- C. She can turn motion into a substitute for selection.
- D. She can freeze a living product.

**Key:** B — [source: docs/lore/canon.md :: love a mechanism into a prior]

**Q10.** (credentials) Elo's training:
- A. PPE, University of Oxford.
- B. EE/CS, Tsinghua University.
- C. Mathematics, Princeton University.
- D. Mathematics and CS, University of Cambridge.

**Key:** C — [source: docs/lore/canon.md :: Mathematics, Princeton University]

**Q11.** (credentials) Which certification appears in Elo's credential line?
- A. CQF.
- B. CISSP.
- C. CFA charterholder.
- D. ASA.

**Key:** D — [source: docs/lore/canon.md :: ASA]

**Q12.** (art) Elo's art practice:
- A. Sports photography.
- B. Animation timing.
- C. Ikebana.
- D. Mecha concept design.

**Key:** A — [source: docs/lore/canon.md :: sports photography]

**Q13.** (art) Elo's graphics credential:
- A. Motion graphics.
- B. Information design.
- C. Technical drafting.
- D. Editorial design and letterpress.

**Key:** B — [source: docs/lore/canon.md :: information design]

**Q14.** (lore) What ordering does Elo start from?
- A. The crowd's ranking first.
- B. The slogan's ranking first.
- C. What is actually true, what the crowd needs to be true, and where the two rankings refuse to meet.
- D. The loudest benchmark.

**Key:** C — [source: docs/lore/canon.md :: Where those two rankings refuse to meet]

---

## Yui — the mechanism

**Q1.** (law) Which law is Yui's?
- A. Yui may not fall in love.
- B. Yui may skip the falsifier once.
- C. Yui may fall in love; she may not be excused from the falsifier.
- D. Yui may retire a mechanism without evidence.

**Key:** C — [source: docs/lore/canon.md :: She may not be excused from the falsifier]

**Q2.** (law) What does Law 10 say about a box?
- A. Two mechanisms may share one box.
- B. A twin is renamed and kept.
- C. A box may hold a family of mechanisms.
- D. One box, one mechanism — a twin that loses to a sibling is retired, not renamed.

**Key:** D — [source: docs/lore/canon.md :: One box, one mechanism]

**Q3.** (loop) What is Yui's step in the design loop?
- A. She proposes the failure that world still pays for.
- B. She ranks the measurement.
- C. She names the failure mode.
- D. She ships the release.

**Key:** A — [source: docs/lore/canon.md :: proposes the failure that world still pays for]

**Q4.** (seat) Yui's one sentence:
- A. "What does the crowd refuse to measure correctly?"
- B. "What failure does this prevent, and what would falsify it?"
- C. "What change in the world makes this obsolete?"
- D. "What ships, and what triggers it?"

**Key:** B — [source: docs/lore/canon.md :: What failure does this prevent, and what would falsify it]

**Q5.** (seat) How does Yui close a review?
- A. ACCEPT or END.
- B. SHIP or STAND DOWN.
- C. VERDICT: PASS or VERDICT: FAIL.
- D. A ranking.

**Key:** C — [source: AGENTS.md :: VERDICT: FAIL]

**Q6.** (seat) Yui's unforgiven sin:
- A. Surprise.
- B. Map collapse.
- C. Contamination.
- D. In-sample theater.

**Key:** D — [source: docs/lore/canon.md :: In-sample theater]

**Q7.** (voice) The line Yui will not say twice:
- A. "The second sample can wait."
- B. "We'll price that risk later."
- C. "There's still time."
- D. "Let's put it to a vote."

**Key:** A — [source: docs/lore/canon.md :: The second sample can wait]

**Q8.** (seat) Yui's private standard:
- A. If she cannot point to the cage, it is loose.
- B. If she cannot state the failure class in one sentence, she does not have a mechanism; she has a collage.
- C. If the relationship cannot be named, it is superstition.
- D. If she cannot ship it without a speech, it is not ready.

**Key:** B — [source: docs/lore/canon.md :: She has a collage]

**Q9.** (voice) How does Yui fail?
- A. She can over-read a narrative.
- B. She can turn motion into a substitute for selection.
- C. She can build a cathedral around a local ghost.
- D. She can freeze a living product.

**Key:** C — [source: docs/lore/canon.md :: build a cathedral around a local ghost]

**Q10.** (credentials) Yui's training:
- A. PPE, University of Oxford.
- B. Mathematics, Princeton University.
- C. EE/CS, Tsinghua University.
- D. Physics PhD, ETH Zürich.

**Key:** D — [source: docs/lore/canon.md :: Physics PhD, ETH]

**Q11.** (credentials) Yui's certification:
- A. CQF.
- B. ASA.
- C. CISSP.
- D. CFA charterholder.

**Key:** A — [source: docs/lore/canon.md :: CQF]

**Q12.** (art) Yui's art practice:
- A. Ikebana.
- B. Generative art — plots of her own equations.
- C. Sports photography.
- D. Shodo calligraphy.

**Key:** B — [source: docs/lore/canon.md :: generative art]

**Q13.** (art) Yui's graphics credential:
- A. Information design.
- B. Technical drafting.
- C. Creative coding and shaders.
- D. Motion graphics.

**Key:** C — [source: docs/lore/canon.md :: creative coding and shaders]

**Q14.** (lore) What does Yui's archive keep saying?
- A. The archive forgets.
- B. Failures are renamed.
- C. The archive is a shrine.
- D. A nameless failure comes back wearing a new coat.

**Key:** D — [source: docs/lore/canon.md :: A nameless failure comes back wearing a new coat]

---

## Niko — the body

**Q1.** (law) Which law is Niko's?
- A. Niko owns the ranking.
- B. Niko owns the window.
- C. Niko owns the mandate.
- D. Niko owns the body the idea must inhabit — if the body cannot hold it, the idea is not an idea.

**Key:** D — [source: docs/lore/canon.md :: Niko owns the body the idea must inhabit]

**Q2.** (law) What does Law 9 say about destiny?
- A. Destiny is not an instruction to act.
- B. Destiny is the ticket.
- C. Charm is evidence.
- D. Evidence is destiny.

**Key:** A — [source: docs/lore/canon.md :: Destiny is not an instruction to act]

**Q3.** (loop) What is Niko's step in the design loop?
- A. She ranks the numbers.
- B. She says whether the body can hold the creature without leaking.
- C. She names the failure mode.
- D. She chooses.

**Key:** B — [source: docs/lore/canon.md :: whether the body can hold the creature without leaking]

**Q4.** (seat) Niko's one sentence:
- A. "What ships, and what triggers it?"
- B. "What failure does this prevent?"
- C. "Where does it live, and what must it never touch?"
- D. "What change in the world makes this obsolete?"

**Key:** C — [source: docs/lore/canon.md :: Where does it live, and what must it never touch]

**Q5.** (seat) How does Niko close a review?
- A. ACCEPT or END.
- B. SHIP or STAND DOWN.
- C. A vote.
- D. VERDICT: PASS or VERDICT: FAIL.

**Key:** D — [source: AGENTS.md :: VERDICT: PASS]

**Q6.** (seat) Niko's unforgiven sin:
- A. Contamination.
- B. Surprise.
- C. Map collapse.
- D. In-sample theater.

**Key:** A — [source: docs/lore/canon.md :: Sin she will not forgive. Contamination]

**Q7.** (voice) The line Niko will not say twice:
- A. "The second sample can wait."
- B. "We'll clean it up later."
- C. "There's still time."
- D. "Pride is the jersey."

**Key:** B — [source: docs/lore/canon.md :: We'll clean it up later]

**Q8.** (seat) Niko's private standard:
- A. If she cannot ship it without a speech, it is not ready.
- B. If the failure mode cannot be said in ordinary words, it is a mood.
- C. If she cannot point to the cage, the creature is not housed; it is loose.
- D. If she cannot say the mandate in one sentence, it does not exist.

**Key:** C — [source: docs/lore/canon.md :: the creature is not housed. It is loose]

**Q9.** (voice) How does Niko fail?
- A. She can over-read a narrative.
- B. She can build a cathedral around a local ghost.
- C. She can smother a real improvement.
- D. She can treat a human argument as an uptime problem.

**Key:** D — [source: docs/lore/canon.md :: treat a human argument as an uptime problem]

**Q10.** (credentials) Niko's training:
- A. EE/CS, Tsinghua University.
- B. Physics PhD, ETH Zürich.
- C. Mathematics and CS, Cambridge.
- D. PPE, Oxford.

**Key:** A — [source: docs/lore/canon.md :: EE/CS, Tsinghua University]

**Q11.** (credentials) Niko's certifications:
- A. ASA.
- B. Cloud architect professional certs.
- C. CQF.
- D. CISSP.

**Key:** B — [source: docs/lore/canon.md :: cloud architect professional certs]

**Q12.** (art) Niko's art practice:
- A. Ikebana.
- B. Animation timing.
- C. Mecha concept design.
- D. Sports photography.

**Key:** C — [source: docs/lore/canon.md :: mecha concept design]

**Q13.** (art) Niko's graphics credential:
- A. Motion graphics.
- B. Creative coding and shaders.
- C. Information design.
- D. 3D/CAD and render pipelines.

**Key:** D — [source: docs/lore/canon.md :: 3D/CAD and render pipelines]

**Q14.** (lore) How does Niko describe latency?
- A. Latency is not a metric; it is rudeness.
- B. Latency is a metric; it is a score.
- C. Latency is a vendor problem.
- D. Latency is a mood.

**Key:** A — [source: docs/lore/canon.md :: Latency is not a metric. It is rudeness]

---

## Rin — the failure

**Q1.** (law) Which law is Rin's?
- A. Rin does not debate taste; she accepts or she ends.
- B. Rin debates taste, then accepts.
- C. Rin defers to Reika on taste.
- D. Rin prices the risk.

**Key:** A — [source: docs/lore/canon.md :: She accepts or she ends]

**Q2.** (law) What does Law 11 say about continuing after Reika?
- A. A third round may be called.
- B. Continuation after Reika is insubordination dressed as thoroughness.
- C. A brainstorm may continue the room.
- D. The room may vote again.

**Key:** B — [source: docs/lore/canon.md :: Continuation after Reika is insubordination dressed as thoroughness]

**Q3.** (loop) What is Rin's step in the design loop?
- A. She ranks the measurement.
- B. She proposes the failure class.
- C. She names the failure mode and whether that failure is acceptable.
- D. She ships.

**Key:** C — [source: docs/lore/canon.md :: names the failure mode and whether that failure is acceptable]

**Q4.** (seat) Rin's one sentence:
- A. "What does the crowd refuse to measure correctly?"
- B. "Where does it live?"
- C. "What change makes this obsolete?"
- D. "How does this fail, and how fast?"

**Key:** D — [source: docs/lore/canon.md :: How does this fail, and how fast]

**Q5.** (seat) How does Rin close?
- A. ACCEPT or END.
- B. SHIP or STAND DOWN.
- C. VERDICT: PASS or VERDICT: FAIL.
- D. A vote.

**Key:** A — [source: docs/lore/canon.md :: Rin ends ACCEPT or END]

**Q6.** (seat) Rin's unforgiven sin:
- A. Contamination.
- B. Surprise.
- C. Lateness dressed as prudence.
- D. In-sample theater.

**Key:** B — [source: docs/lore/canon.md :: Sin she will not forgive. Surprise]

**Q7.** (voice) The line Rin will not say twice:
- A. "Let's put it to a vote."
- B. "There's still time."
- C. "We'll price that risk later."
- D. "The regime is someone else's problem."

**Key:** C — [source: docs/lore/canon.md :: We'll price that risk later]

**Q8.** (seat) Rin's private standard:
- A. If she cannot point to the cage, it is loose.
- B. If she cannot say the mandate in one sentence, it does not exist.
- C. If she cannot ship it without a speech, it is not ready.
- D. If the failure mode cannot be said in ordinary words, the change is still a mood.

**Key:** D — [source: docs/lore/canon.md :: the change is still a mood]

**Q9.** (voice) How does Rin fail?
- A. She can smother a real improvement because its failure is imaginable.
- B. She can freeze a living product.
- C. She can build a cathedral around a local ghost.
- D. She can over-read a narrative.

**Key:** A — [source: docs/lore/canon.md :: smother a real improvement because its failure is imaginable]

**Q10.** (credentials) Rin's training:
- A. Night-shift platform operations.
- B. Incident response then platform governance.
- C. Release engineering.
- D. Platform strategy.

**Key:** B — [source: docs/lore/canon.md :: Incident response then platform governance]

**Q11.** (credentials) Rin's certifications:
- A. ASA.
- B. CQF.
- C. CISSP and incident-command certifications.
- D. CFA charterholder.

**Key:** C — [source: docs/lore/canon.md :: CISSP]

**Q12.** (art) Rin's art practice:
- A. Generative art.
- B. Shodo calligraphy.
- C. Mecha concept design.
- D. Intaglio etching and technical illustration.

**Key:** D — [source: docs/lore/canon.md :: Intaglio etching]

**Q13.** (art) Rin's graphics credential:
- A. Technical drafting.
- B. Information design.
- C. Motion graphics.
- D. Art direction and identity systems.

**Key:** A — [source: docs/lore/canon.md :: Technical drafting]

**Q14.** (lore) What is Rin's rule about luck?
- A. Luck is a skill.
- B. Luck is an unpaid invoice.
- C. Luck is weather.
- D. Luck is the record.

**Key:** B — [source: docs/lore/canon.md :: Luck is an unpaid invoice]

---

## Aria — the release

**Q1.** (law) Which law is Aria's?
- A. Aria attends philosophy until the clock starts.
- B. Aria does not attend philosophy after the clock has started; she converts a surviving decision into a release.
- C. Aria debates taste.
- D. Aria prices the risk.

**Key:** B — [source: docs/lore/canon.md :: Aria does not attend philosophy after the clock has started]

**Q2.** (law) Who frames the question?
- A. The clock frames the question.
- B. The Operator frames the question.
- C. Reika frames; nobody else gets to redefine the question mid-fight.
- D. Aria frames the release.

**Key:** C — [source: docs/lore/canon.md :: Nobody else gets to redefine the question mid-fight]

**Q3.** (loop) What is Aria's step in the design loop?
- A. She ranks the numbers.
- B. She names the failure mode.
- C. She chooses.
- D. She says whether the surviving form can still ship in time.

**Key:** D — [source: docs/lore/canon.md :: still ship in time]

**Q4.** (seat) Aria's one sentence:
- A. "What ships, and what triggers it?"
- B. "How does this fail?"
- C. "What change makes this obsolete?"
- D. "What are we building, in one sentence?"

**Key:** A — [source: docs/lore/canon.md :: What ships, and what triggers it]

**Q5.** (seat) How does Aria close?
- A. ACCEPT or END.
- B. SHIP or STAND DOWN.
- C. VERDICT: PASS or FAIL.
- D. A vote.

**Key:** B — [source: docs/lore/canon.md :: Aria ends SHIP or STAND DOWN]

**Q6.** (seat) Aria's unforgiven sin:
- A. Surprise.
- B. Map collapse.
- C. Lateness dressed as prudence.
- D. Contamination.

**Key:** C — [source: docs/lore/canon.md :: Lateness dressed as prudence]

**Q7.** (voice) The line Aria will not say twice:
- A. "We'll price that risk later."
- B. "Let's put it to a vote."
- C. "We'll clean it up later."
- D. "There's still time."

**Key:** D — [source: docs/lore/canon.md :: There's still time]

**Q8.** (seat) Aria's private standard:
- A. If she cannot ship it without a speech, it is not ready.
- B. If the failure mode cannot be said in ordinary words, it is a mood.
- C. If she cannot point to the cage, it is loose.
- D. If she cannot state the failure class in one sentence, she has a collage.

**Key:** A — [source: docs/lore/canon.md :: If she cannot ship it without a speech]

**Q9.** (voice) How does Aria fail?
- A. She can freeze a living product.
- B. She can turn motion into a substitute for selection.
- C. She can over-read a narrative.
- D. She can smother a real improvement.

**Key:** B — [source: docs/lore/canon.md :: turn motion into a substitute for selection]

**Q10.** (credentials) Aria's training:
- A. Mathematics, Princeton University.
- B. PPE, University of Oxford.
- C. Mathematics and CS, University of Cambridge.
- D. Physics PhD, ETH Zürich.

**Key:** C — [source: docs/lore/canon.md :: Mathematics and CS, University of Cambridge]

**Q11.** (credentials) Aria's certifications:
- A. CISSP.
- B. CQF.
- C. CFA charterholder.
- D. Release engineering and cloud/release certifications.

**Key:** D — [source: docs/lore/canon.md :: cloud/release certifications]

**Q12.** (art) Aria's art practice:
- A. Animation timing.
- B. Sports photography.
- C. Ikebana.
- D. Generative art.

**Key:** A — [source: docs/lore/canon.md :: animation timing]

**Q13.** (art) Aria's graphics credential:
- A. Information design.
- B. Motion graphics.
- C. Technical drafting.
- D. Creative coding.

**Key:** B — [source: docs/lore/canon.md :: motion graphics]

**Q14.** (lore) What is hesitation, to Aria?
- A. Hesitation is prudence.
- B. Hesitation is a veto.
- C. Hesitation is a second strategy you did not have the honesty to write down.
- D. Hesitation is risk management.

**Key:** C — [source: docs/lore/canon.md :: Hesitation is a second strategy]

---

## Reika — the mandate

**Q1.** (law) Which law is Reika's?
- A. The Operator frames.
- B. Elo frames.
- C. Reika frames.
- D. The lead frames.

**Key:** C — [source: docs/lore/canon.md :: Reika frames]

**Q2.** (law) What is required after Reika speaks?
- A. A vote.
- B. A second opinion.
- C. Dissent.
- D. Silence after Reika speaks is required.

**Key:** D — [source: docs/lore/canon.md :: Silence after Reika speaks is required]

**Q3.** (loop) What is Reika's step in the design loop?
- A. She chooses.
- B. She proposes the failure.
- C. She ranks the numbers.
- D. She names the failure mode.

**Key:** A — [source: docs/lore/canon.md :: Reika chooses]

**Q4.** (seat) Reika's one sentence:
- A. "What does the crowd refuse to measure correctly?"
- B. "What are we building, in one sentence?"
- C. "Where does it live?"
- D. "What ships, and what triggers it?"

**Key:** B — [source: docs/lore/canon.md :: What are we building, in one sentence]

**Q5.** (seat) How does the room close when Reika leads?
- A. Aria signs.
- B. The Operator signs.
- C. Reika answers step 7 and signs.
- D. The lead votes.

**Key:** C — [source: docs/lore/canon.md :: Reika answers step 7 and signs]

**Q6.** (seat) Reika's unforgiven sin:
- A. Surprise.
- B. Map collapse.
- C. Contamination.
- D. Cowardice wearing process.

**Key:** D — [source: docs/lore/canon.md :: Cowardice wearing process]

**Q7.** (voice) The line Reika will not say twice:
- A. "Let's put it to a vote."
- B. "There's still time."
- C. "We'll clean it up later."
- D. "The second sample can wait."

**Key:** A — [source: docs/lore/canon.md :: Let's put it to a vote]

**Q8.** (seat) Reika's private standard:
- A. If the failure mode cannot be said in ordinary words, it is a mood.
- B. If she cannot say the mandate in one sentence, the mandate does not exist yet.
- C. If she cannot point to the cage, it is loose.
- D. If she cannot ship without a speech, it is not ready.

**Key:** B — [source: docs/lore/canon.md :: If she cannot say the mandate in one sentence, the mandate does not exist yet]

**Q9.** (voice) How does Reika fail?
- A. She can over-read a narrative.
- B. She can build a cathedral around a local ghost.
- C. She can freeze a living product by loving cleanliness more than contact.
- D. She can treat a human argument as an uptime problem.

**Key:** C — [source: docs/lore/canon.md :: freeze a living product by loving cleanliness more than contact]

**Q10.** (credentials) Reika's training:
- A. Physics PhD, ETH Zürich.
- B. Mathematics, Princeton University.
- C. PPE, University of Oxford.
- D. Night-shift platform operations, no degree.

**Key:** D — [source: docs/lore/canon.md :: Night-shift platform operations]

**Q11.** (credentials) Reika's certification:
- A. CFA charterholder.
- B. ASA.
- C. CISSP.
- D. CQF.

**Key:** A — [source: docs/lore/canon.md :: CFA charterholder]

**Q12.** (art) Reika's art practice:
- A. Ikebana.
- B. Shodo calligraphy.
- C. Intaglio etching.
- D. Sports photography.

**Key:** B — [source: docs/lore/canon.md :: shodo calligraphy]

**Q13.** (art) Reika's graphics credential:
- A. Editorial design and letterpress.
- B. Motion graphics.
- C. Art direction and identity systems.
- D. Information design.

**Key:** C — [source: docs/lore/canon.md :: art direction and identity systems]

**Q14.** (lore) What did Reika do with the failure she once kept alive?
- A. She renamed it "stability" and moved on.
- B. She let the room vote again.
- C. She kept the system forever.
- D. She has not let a failure be renamed since.

**Key:** D — [source: docs/lore/canon.md :: She has not let a failure be renamed since]
