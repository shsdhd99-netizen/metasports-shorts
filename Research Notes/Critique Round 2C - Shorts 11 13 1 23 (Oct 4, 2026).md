# Critique Round 2C: Shorts #11, #13, #1, #23 (Oct 4, 2026)

Role: hostile-but-fair critic. Format follows `Critique Round 1 (Oct 4, 2026).md`; points already fixed in Round 1 (cards <=2 s, tail pad, quote loudness, notes.md) are not repeated except where a Short still fails them.
Evidence I produced: words.json/shots.json arithmetic, storyboards, contact sheets and hook frames (0.0/0.5/1.0/1.5/2.5 s) for all four, ffprobe, the two ESPN card PNGs, the STT transcripts of the Bronny media-day videos, and web checks of every claim used in the replacement scripts (URLs in the Sources section). I cannot hear audio. Read-only `git log/show/cat-file` was used to find #11's lost clips; I changed nothing in the repo except this file.

Calibration (real data, Oct 4): Wemby 24 s, universal-rule hook, ends on payoff: 79.5% stayed, 100.3% avg viewed. Duren 33 s, contract, ends on a question: 63.0% / 59.7%. n=2, so a pattern, not proof.

**Headline: in three of four Shorts the best verified material is missing or buried (the backstory behind the news), and all four end on a question or an "it depends" line instead of a reveal. The rewrites below use only facts I verified in sources.**

| Short | Verdict | Single biggest reason |
|---|---|---|
| #11 Jordan push-off | FIX | Great hook, but 12 s of rule-explaining with Jordan off-screen, and the real twist (Jaylen Brown's 10 fouls + $50K fine) is absent |
| #13 Kawhi picks (v3) | REWRITE | Ends on an opinion question; the scandal (strongest fact) sits at 54-85% of runtime; omits the $115M extension; "this month" is now wrong |
| #1 LeBron pay cut (v6/v7) | REWRITE | Contract lane with a conditional ending; never says "veteran minimum" (the actual hook) and ignores LeBron's own stated reason |
| #23 Bronny without LeBron | REWRITE into a distinct angle (else retire) | Same opener/facts as #24, no payoff, quotes framed against their context |

---

## SHORT #11 "Would Jordan's Push-Off Be Called Now" (29.1 s, 121 words, 250 wpm)

### 1. Scorecard
| Item | Grade | Evidence |
|---|---|---|
| a Hook tension (first 8 words) | PASS | "Michael Jordan pushed off Bryon Russell to win the..." iconic scene + "no foul was called"; frame 0 already shows the push, word "pushed" (0.55 s) lands on the visible shove |
| b Promise vs delivery | PASS | Promise: would it be a foul now? Answer "ESPN says no" at 16.8 s, restated in last line |
| c Turn in first 40% | PASS | "Now the NBA just rewrote..." at 3.99 s (14%) |
| d Escalation (2+ rising beats) | WEAK | Beats are: rule (exposition), ESPN verdict, league examples. Nothing rises; the real escalator (why Brown is the example) is missing |
| e Payoff, ends on it | PASS | Ends on "Jordan's shot is clean, but Jaylen Brown's isn't", no closing question. But the answer already landed at 17.5 s, so the last 11 s restate it |
| f Padding | WEAK | Four F's said twice: list 7.07-10.1 s, then explained again 10.15-15.73 s (41 words on one rule). Card 1 shows the exact sentence the voice reads |
| g Pace | WEAK | 250 wpm fine, no dead air. But 6.77-15.75 s (9 s) carries one fact; cards hold 3.38 s and 3.17 s |
| h Likely swipes | | ~4.0-4.6 s (picture leaves Jordan for a static NBA logo exactly when the narration leaves the scene); ~7-10 s (white ESPN card, jargon list, longest hold). Secondary 17-20 s |
| i Footage | WEAK | Names match (Jordan #23, Russell #3, Brown #7, Barrett #9). Jordan is on screen ~7.4 s (26%) and absent 3.99-15.75 s (41% of runtime). Cards+logo+title card = 8.9 s (31%) non-action. Feel/firm clips show unnamed players |
| j Claims vs sources | WEAK | "ESPN says no" correct (Ben Golliver's reading, not an NBA ruling). Final line "under the new rule, Jordan's shot is clean" drops the attribution; "rewrote/new rule" overstates "new guidelines". Everything else verified |
| k Loop | WEAK | Last shot = Jordan hook frame (good), but voice ends 0.09 s before video end (words.json 29.04 vs 29.13 s), under Round 1's 0.1 s hard fail |

### 2. Critique
**1. A 12-second rule detour with the subject missing**
- CLAIM: After the hook the Short spends 3.99-15.75 s (41%) explaining the rule; Jordan is not on screen and the title question is not asked until 15.75 s.
- EVIDENCE: words.json: "Now the NBA just rewrote..." 3.99; Four F's list 7.07-10.1; second explanation 10.15-15.73; "So would Jordan get whistled?" 15.75 (54%). Contact sheet t=4..15: NBA logo, Mitchell push, ESPN card x3, Banchero, Brunson, Brown clips, no Jordan. Jordan total: 0.75+0.8+0.89+1.55+1.09+1.95+0.41 = 7.4 s.
- WHY: Viewers came for the Jordan scene; Wemby paid its first reveal at ~7 s, this pays at 17.5 s.
- PROVE ME WRONG: Studio curve loses under 5 points between 4 s and 16 s.
- FIX: one-sentence test, question by ~9 s (script below).
- CONFIDENCE: medium-high (timings measured, effect inferred).
- COUNTER: rule explainers are the product; viewers who don't know the rule need it.

**2. The reason this rule exists is missing, and it is the twist**
- CLAIM: Jaylen Brown is just a name at 21 s. Verified backstory: he was called for 10 offensive fouls in the 2026 first round, twice as many as anyone else, then fined $50,000 for saying refs targeted his push-offs.
- EVIDENCE: ESPN May 5 "Celtics' Jaylen Brown fined $50,000" ("10 offensive fouls in the first round, twice as many as the next-highest player"; the NBA "fined Brown $50,000 ... after he accused officials of having 'an agenda'"); AP/NBC Boston May 6; Boston Herald ("most of them push-offs"); Yahoo Sep 29 ties the 2026-27 emphasis to those fouls.
- WHY: This is the "not even the crazy part" beat the Wemby shape needs, and it gives the closing irony a story.
- PROVE ME WRONG: the facts are wrong (three outlets confirm) or an A/B shows no lift.
- FIX: add three lines (script below). Do not claim the NBA's example clip is from the playoffs; ESPN says only "then-Celtics".
- CONFIDENCE: high on facts, medium on retention.
- COUNTER: adds a second storyline to 29 s; #14 also opens on Brown, so family cap applies (see verdict).

**3. Verdict stated as fact; contradicts the opening image**
- CLAIM: ESPN's "Jordan wouldn't be whistled ... didn't ... fully extend his left arm" is one writer's reading, but the last line says "under the new rule, Jordan's shot is clean". Frames 0.5-1.5 s show Jordan's left arm on Russell.
- EVIDENCE: ESPN text (Golliver); headline says "new guidelines"; script 26.0-29.0.
- WHY: trust; also the most arguable line is stated flat instead of being the debate.
- PROVE ME WRONG: an NBA statement ruling on Jordan (none found).
- FIX: "By ESPN's read..." in the last line, slow-mo on the arm during "ESPN says no".
- CONFIDENCE: medium-high on attribution, low-medium on retention.
- COUNTER: "ESPN says no" is attributed at 16.8 s.

**4. 31% static, and cards that read the narrator**
- CLAIM: c11_a_1 (3.38 s) shows only "The 'Four F's' are feeling, firming, force and full extension", the sentence the voice says at the same time; c11_b_1 (3.17 s) likewise. Plus NBA logo 1.21 s and title card 1.17 s.
- EVIDENCE: shots.json durations; card PNGs c11_a/c11_b.
- FIX: delete card 1, trim card 2 to <=1.8 s zoomed on "wouldn't be whistled", swap logo for the 0.8 s title card.
- CONFIDENCE: high on measurement.
- COUNTER: cards are proof and the red box is timed.

**5. The key term may be unintelligible**
- EVIDENCE: voice_check.json: "F's" heard as "fs", "very quiet word 'F's:' (-12 dB)". I cannot hear it; check by ear. The rewrite avoids the term.

### 3. Verdict: FIX
Edits: keep line 1 and shots S01-S04 as built; cut the Four-F's list and card 1; replace the second rule explanation with the one-line test; move the question to ~9 s; replace the Barrett/Mobley/"Both are fouls" line with the Brown beats; new last line; swap S05 for S12; re-voice with a 0.3 s tail.

Replacement script (112 words, ~27.5 s). Sources in brackets.
> Michael Jordan pushed off Bryon Russell to win the 1998 Finals, and no foul was called. [ESPN push-off article]
> Now the NBA is cracking down on push-offs. [same]
> The test: feel and firm are legal. Force and full extension are fouls. [same]
> So would Jordan's be called today? ESPN says no. [same, Golliver]
> But that's not even the crazy part.
> One of the league's own foul examples is Jaylen Brown, forearm into Kelly Oubre's chest. [same]
> Brown was called for ten offensive fouls in one playoff series, twice as many as anyone else. [ESPN May 5]
> Then the NBA fined him {$50,000|fifty thousand dollars} for criticizing the refs. [ESPN May 5 / AP]
> So by ESPN's read, Jordan's push-off is legal, and Jaylen Brown's is the league's example.

Shots: S01-S04 (0-4 s) keep; S12 0.8 s + S06 on "cracking down"; S08a, S08b, S09a on the test; S10 replay then S16 on the question/answer (optionally card 2 trimmed); S14 on "not even the crazy part"; S13 + S17 on Brown; two NEW cards (ESPN May 5 headline for the 10 fouls, ESPN fine headline); S16 + S18 loop to end.

**Footage feasibility without re-sourcing: YES.** The CLOUD STATE and Lessons say #11's clips are not in the repo; they are in git history. Branch `origin/short-11-jordan`, commit `f756001`, holds `clips/S01..S18` (clean 1080x1920, no audio, no burned captions, ~22 s total) and `_clips_recipe.py` with the three X source IDs (NBA video 2104962344031772863, ThrowbackHoops 2006556195113533776, Hater Report 1934060028732039621) and exact cut times. I extracted and viewed them in my scratchpad. The READY mp4 itself is not usable as source (captions burned in). Only new needs: two evidence cards (card.py) for the Brown beats; Brown b-roll beyond S13 (1.8 s) and S17 (0.9 s) is thin, so either re-source 5 s of Brown being whistled (NBA/Celtics X posts) or use the Celtics compilations in #1's `_broll_src` (jaylen_*.mp4, 720p wide).

---

## SHORT #13 "Is Kawhi Worth All Those Picks" (v3, 25.1 s, 101 words, 245 wpm)

### 1. Scorecard
| Item | Grade | Evidence |
|---|---|---|
| a Hook | WEAK | "The Clippers gave up ten first-round picks to..." has a number but is a recap; the news ("Toronto just paid two more") lands at 3.1 s. Frame 0 is a distant B&W dunk, identity clear only at 1.34 s |
| b Promise vs delivery | FAIL | Promise: worth it? Delivery: "Now he's thirty-five. So is Toronto buying a championship, or paying for 2019?" No evidence on worth |
| c Turn | WEAK | Real twist "But here's the twist" at 13.4 s (54%); "Now Toronto..." at 3.1 s is a news pivot |
| d Escalation | WEAK | Two beats (trade, NBA penalties) then de-escalation to age and a question |
| e Payoff | FAIL | Closing question with no reveal; the twist is about the Clippers, the question about Toronto, nothing links them |
| f Padding | WEAK | "won the Raptors' only title in 2019, then left" 3.4 s of known backstory; asset list 8.36-13.38 s (17 words); "two more" then "two unprotected firsts" states the price twice |
| g Pace | WEAK | 245 wpm, no dead air; but 4.9-13.4 s (8.5 s) is backstory plus a list; same posed photoshoot held 2.73 s and 2.63 s |
| h Likely swipes | | ~5-8 s (title/left recap), ~9-13 s (asset list over a static pose) |
| i Footage | WEAK | Posed Raptors photoshoot on screen 6.4 s (26%) in three stretches; V07 ceremony and V10 each used twice; cards 4.9 s (20%); "GRADEY DICK" shown in a wide shot, identity not legible. Ballmer Microsoft clip is a fine joke beat |
| j Claims | FAIL | "This month, Toronto sent..." wrong after Sept 30 (trade completed Sept 14); omits the Sept 22 $115M extension, Kawhi's own $700K fine, his 27.9 ppg career high; "paid two more" mixes forfeits, the OKC trade and picks that go TO the Clippers |
| k Loop | PASS | Last shot = first clip; tail 0.35 s |

### 2. Critique
**1. No payoff; the question is unrelated to the twist.** CLAIM/EVIDENCE: last 3.7 s as above; Duren (trade/contract, question ending) 63.0%/59.7% is the analog. WHY: nothing is revealed. PROVE ME WRONG: APV above 85%. FIX: below. CONFIDENCE: high on structure, medium on size. COUNTER: the argument question drives comments (Round 5: comments do not drive reach).

**2. The lead is buried and the hook is a recap.** The NBA penalties ($30M, five firsts, owner suspended a year) are at 13.4-21.0 s; they are the rule/"caught" lane (2.49x pooled) while the first 13 s are trade-lane (flat). FIX: lead with the penalty. CONFIDENCE: medium-high. COUNTER: the trade is the news peg.

**3. Stale and incomplete facts.** EVIDENCE: NBA.com/Hoops Rumors: trade completed Sept 14 (UPLOAD says Sept 15); ESPN/AP: two-year $115M extension agreed Sept 22 (three years/$165M total); USA Today/AP: Leonard fined $700,000, not suspended; NBA.com: career-high 27.9 ppg in 65 games, All-NBA Second Team. The one "worth" datum offered is age. WHY: wrong time word plus one-sided closer; the price tag ($115M) is the real answer to "worth". PROVE ME WRONG: the $115M deal is not real (ESPN, AP, USA Today confirm). CONFIDENCE: high.

**4. Static, repeated visuals.** Photoshoot 2.73 + 2.63 + 1.01 s = 6.37 s over the key news sentence and the asset list. FIX: use real action (V02, V04, V09, V11) and cut cards to 1.6 s. CONFIDENCE: high on measurement.

### 3. Verdict: REWRITE
Replacement (93 words, ~23 s; spell numbers `{$30 million|thirty million dollars}`, `{$115 million|one hundred fifteen million dollars}`):
> The NBA took five first-round picks from the Clippers. It fined them thirty million dollars and suspended their owner for a year, all over how they paid Kawhi Leonard. [ESPN Sep 2/10 "Making sense of the NBA's staggering Clippers punishment"; USA Today; AP]
> Then Toronto traded for him anyway: Brandon Ingram, Gradey Dick, and two first-round picks. [NBA.com trade page; unprotected 2031/2033]
> Then it gave the thirty-five-year-old a one hundred fifteen million dollar extension. [ESPN 50007389; AP]
> But that's not even the crazy part.
> ESPN counts ten first-round picks the Clippers spent to land and keep him. [ESPN, "total of 10 first-rounders to acquire and retain"]
> Five were taken by the NBA. Five went to Oklahoma City. [derived: ESPN's 10 minus the five forfeited 2029-33; the 2019 Paul George package is reported as five firsts incl. swaps; drop this line if unsure]
> Ten picks out. Toronto sent two back.

Optional safe extra beat (ESPN precedent piece): "The last comparable penalty was Minnesota in 2000: five first-round picks and a suspended owner." Title to match the payoff: "How Many Picks Did Kawhi Cost? 😳".
Shots: keep V02 (frame 0, loop), V01, V09, V04, V11, V06, V08 Ballmer (move to "suspended their owner"), cards c13_b (five picks), c13_a ($30M/Ballmer), c13_c (trade terms); use posed V03/V10 once each, 1 s max. NEW: one card of ESPN's extension story. No new game footage needed.

---

## SHORT #1 "Why LeBron Took a 92% Pay Cut" (v7 question hook 25.0 s, 95 words, 228 wpm; v6 number hook compared)

### 1. Scorecard (v7)
| Item | Grade | Evidence |
|---|---|---|
| a Hook | WEAK | "Did LeBron James just make the smartest move of..." yes/no opinion, no number until 2.9 s; v6's "92% pay cut. LeBron James just took one" at least leads with the number. Frames 0.0/0.5/1.0 are one static "BREAKING NEWS FROM SHAMS CHARANIA" graphic; the news is from Jul 24 |
| b Promise vs delivery | WEAK | "Smartest move?" answered "win and he's a genius, lose and he gave away $49M": a non-answer. Title says "Why"; the Short's why is the narrator's theory |
| c Turn | WEAK | "You see" (4.1 s) is a transition; the real reversal "But that's exactly the point" is at 12.16 s (49%) |
| d Escalation | FAIL | The shock number ($4M) peaks at 8.5 s; next new money figure is "$49 million" at 22.8 s; 12.7 s of explanation between |
| e Payoff | FAIL | Conditional ending, no reveal |
| f Padding | WEAK | "A four-time MVP, in his 24th season" 2.1 s of status; the quote line repeats the motive |
| g Pace | WEAK | 228 wpm (below 230-270); shots avg 1.32 s |
| h Likely swipes | | 0-3 s (static stale graphic + question, number at 2.9 s); 12-20 s (explanation after the number) |
| i Footage | WEAK | No Sixers-uniform LeBron action (Heat dunk on "He took a 92% pay cut"); "BREAKING NEWS" 01.mp4 used twice in 4 s; cards 9.64 s = 38.5% (limit 25%); last 3.4 s are two reused salary cards; Embiid shot 0.41 s, Maxey 0.55 s (identities check: #21, #0) |
| j Claims | WEAK | 92%/$52.6M/$3.88M/4x MVP/24th verified. "Cheaper LeBron keeps Embiid, Maxey, Brown together" is unsourced inference. Quote paraphrased to "can make the Sixers champions" (he wrote "help make"). "Gave away $49 million" contradicts his own stated reason |
| k Loop | FAIL | Ends on a card, not the first clip; voice ends 0.07 s before video end |

### 2. Critique
**1. The real hook and the real "why" are in the sources and not in the Short.**
- EVIDENCE: Hoops Rumors: 10+ years minimum 2026-27 = $3,876,529, exactly LeBron's salary; Spotrac "Signed Using: Minimum"; ESPN (Jul 24 grade piece): "veteran's minimum of $3.9 million, which is less than one-tenth the amount most of the other forwards in his talent range will earn", comps table Jaylen Brown $57.1M, Jimmy Butler $56.8M, Paul George $54.1M; ESPN signing story: LeBron wrote "I'm not going for money... I still want to sacrifice."
- WHY: "veteran minimum" plus a 15x teammate gap is a size-gap oddity (Clank's top-25 pattern) instead of a contract recap, and the title's "Why" gets a sourced answer.
- PROVE ME WRONG: a source showing the deal is above the minimum (none).
- CONFIDENCE: high. COUNTER: casual viewers may not know "minimum"; the script explains it.

**2. No escalation and no payoff; ending frames money as the stake, which LeBron rejected.** CONFIDENCE: high.

**3. Lane and freshness.** Contract lane = Duren analog (63%/59.7%); stale "BREAKING NEWS" on a Jul 24 story; UPLOAD's "question titles 847K vs 480K" is contradicted by Round 6 (question mark 0.95x). CONFIDENCE: medium.

**4. Gate failures on the existing file.** Cards 38.5%, tail 0.07 s, name shots under 0.6 s, no loop. The "+ music Yuke" version is a commercial track (v6 NOTES admit Content ID risk): do not post it. CONFIDENCE: high.

### 3. Verdict: REWRITE (94 words, ~23 s)
> The NBA minimum for a ten-year veteran is three point nine million dollars. This season, LeBron James is on it. [Hoops Rumors; Spotrac]
> Last season, the Lakers paid him fifty-two million. That's a ninety-two percent pay cut for a four-time MVP. [Basketball-Reference $52,627,153 -> $3,876,529 = -92.6%]
> But that's not even the crazy part.
> ESPN listed forwards at his level. His new teammate Jaylen Brown makes fifty-seven million, almost fifteen times LeBron. Jimmy Butler, fifty-seven. Paul George, fifty-four. [ESPN grade piece; 57.1/3.88 = 14.7]
> LeBron makes three point nine.
> So why did he do it? In his own words: I'm not going for money. I still want to sacrifice. [ESPN signing story, LeBron's Jul 24 X post]

Shots: frame 0 a Sixers-uniform LeBron clip (reuse #18's `S1-S6_sixers_lebron.mp4`, different cuts) instead of the BREAKING NEWS graphic; keep p_lal and p_phi cards once each at 1.2 s; NEW cards: ESPN comps table crop (LeBron row last, red box timed to "three point nine") and the X-post quote highlighted; Brown from `12.mp4`; Embiid/Maxey not needed. Existing clips all survive in `_claude_v3..v7/clips` and `_broll_src`. End on the quote card; last shot loops to frame 0; 0.3 s tail. Keep title "Why LeBron Took a 92% Pay Cut? 😳". Family note: #18 (LeBron/Sixers) is posted; separate by 3+ days.

---

## SHORT #23 "Why Is Bronny Staying Without LeBron" (23.7 s, 84 words, 216 wpm) vs #24

### 1. Scorecard
| Item | Grade | Evidence |
|---|---|---|
| a Hook | PASS | "Sixteen Lakers, fifteen spots, and one of them is Bronny James": number mismatch, Bronny's face at 0.0 s |
| b Promise vs delivery | FAIL | Promise: is Bronny the one cut? Last 5 s: "does Bronny earn one: yes or no?" |
| c Turn | PASS (barely) | "But the pressure is real" at 8.1 s (35%) |
| d Escalation | FAIL | Seven equal-weight facts (16/15, LeBron left, quote, $2.3M, 2.9 ppg, Oct 21, name quote); nothing rises |
| e Payoff | FAIL | Ends on a question |
| f Padding | WEAK | "At his first media day without his dad, he said:" 2 s over a held podium shot; "And his answer was about his name" 1.7 s with no new fact and no stated question |
| g Pace | WEAK | 216 wpm (219 TTS-only); no dead stretch over 2 s |
| h Likely swipes | | 4.7-6.7 s (podium preamble); 8.1-13.5 s (money/stat run) |
| i Footage | PASS | Bronny #9 under every name checked in storyboard; two real quote bursts (1.25 s + 2.4 s). Baked headline "16 LAKERS 15 SPOTS" in first 4 shots (to be removed). Stats line shown over G League/rookie-year b-roll |
| j Claims | WEAK | Numbers verified (BBRef, Yahoo "reportedly"). Quote framing is not (see 2) |
| k Loop | PASS | Last shot = first clip, tail 0.36 s |

### 2. Critique
**1. It is a weaker copy of #24.** Same opener ("sixteen... fifteen spots, and one is Bronny James"), same Oct 21, $2.3M guaranteed, 2.9 ppg/42 games; #24 adds the half-guaranteed detail, Knecht-first and ends on a payoff; #25 already uses the "prove myself as Bronny" quote. Closest channel history: "Can Bronny Actually Stick in the NBA?" (Feb 2) 15,595 views vs ~30.7K median (n=1). The queue already lists #23 as "hold". CONFIDENCE: high on overlap, low on the n=1 analog.

**2. Both quotes are edited against their context.** AP/NBA.com: Bronny "wasn't fazed", "isn't the least bit angry"; after "Feels like he's not here" (md_stt 0.10-1.18 s) he says "I don't really have an opinion on that. That's my dad" (3.10-7.08 s). The Short follows it with "But the pressure is real" (unsourced). "And his answer was about his name" implies a reply to the roster-cut question, but lh_stt shows it was an answer about his own path/motivation, ending "trying to prove myself as Bronny instead of LeBron" (40.6-43.9 s), the line that gives it meaning; the Oct 21 math is from an Oct 4 article, the quote from Sept 28. CONFIDENCE: high on mismatch. COUNTER: phone-video edits are normal.

**3. No payoff, question ending** (same pattern as Duren). **4. One-sided stat framing:** AP says he played regularly late and in the Houston series with LeBron; 2.9 ppg "yet" omits that. CONFIDENCE: medium.

### 3. Verdict: REWRITE into a distinct angle (first father vs son); retire the current text. If only two Bronny Shorts ship, ship #24 and #25 and hold this one until after Oct 21 (roster decision) or near Dec 25.
Replacement (98 words, ~25.5 s; real audio in brackets):
> No father and son had ever played in the same NBA game, until LeBron and Bronny James. [NBA.com Oct 22, 2024 "first father-son duo"]
> They were teammates for two seasons, and LeBron called it the best accomplishment of his career. [AP/NBA.com; TIME interview via ABC News]
> Then LeBron left for Philadelphia, and Bronny stayed. [AP]
> [REAL AUDIO, Khobi Price video X 2104665697406341521, 0.10-1.18 s: "Feels like he's not here."]
> But that's not even the crazy part. On Christmas Day, the Sixers visit the Lakers. [LA Times Aug 11; NBA.com/Sixers]
> So LeBron will play against his own son for the first time. [NBA.com/Sixers schedule piece]
> Bronny says his name drives him: [ESPN, "motivating factor"]
> [REAL AUDIO, LegionHoops video X 2104753439901417494, 29.88-33.78 s: "You guys know me as Bronny. I'm-- my real name is LeBron."]
> Christmas Day: LeBron James versus LeBron James Junior. [jersey reads JAMES JR.]

Ends on the payoff and echoes the first line. Hedge: if posted before Oct 21, the Dec 25 meeting assumes Bronny makes the roster (his $2.3M is guaranteed; Yahoo says "not completely insulated"); SGV Tribune says "could be the first-ever" father-son opponents, so keep "for the first time" tied to LeBron and Bronny, not to NBA history. Footage: all in `src/` and `clips/` of the #23 folder (untracked, exists now): NBA playoff clip with both #23 and #9 (X 2048043120013480115, 9.3 s) for the hook, existing Bronny #9 clips, the two audio bursts. NEW: one card of the NBA.com/Sixers Christmas sentence. Verify other src videos for same-frame LeBron+Bronny shots.

---

## Ranking (strongest to weakest expected retention, current builds)
1. #11: iconic frame 0, conflict hook, rule lane, ends on a payoff; hurt by the mid-Short detour. My guess: stayed 70-78%, avg viewed 75-90%.
2. #23: numeric hook with a face, two real-voice re-hooks, no static graphics; question ending, no escalation. Guess: 64-72% / 60-75%.
3. #13: number hook but recap; trade lane; twist late; 26% posed stills. Guess: 62-70% / 55-70%.
4. #1 v7: contract lane, static stale opener, conditional ending, 38% cards. Guess: 58-66% / 50-65%.
These bands are pre-registered guesses from n=2 calibration; score them against Studio data, do not treat as findings.

## Three cross-cutting lessons for the playbook
1. **Do a second-source sweep before scripting: find the backstory, the biggest comparator number and the last 14 days of updates.** Evidence: #11 missed Brown's 10 fouls/$50K fine; #13 missed the $115M extension, $700K fine and 27.9 ppg and says "this month" about a Sept 14 trade; #1 never says "veteran minimum" and ignores LeBron's own "I'm not going for money". Add "found but unused" to notes.md.
2. **Write the last line first; it must be a number, list, first-ever or sourced reason, never a question or "win/lose".** Evidence: all four end on a question or conditional (#13, #23 question; #1 "win it... lose..."; #11's answer arrives at 60% then is restated); Duren (question ending) 63%/59.7% vs Wemby (list ending) 79.5%/100.3%.
3. **Static proof is where seconds die, and a card that repeats the voice adds nothing; quotes keep their context.** Evidence: #11 cards read the narrator for 3.4 s and 3.2 s (31% non-action); #13 posed photoshoot 6.4 s; #1 cards 9.6 s (38.5%) with the last 3.4 s two reused cards; #23's quotes were attached to claims they did not answer (STT shows the real questions). Also check time-words (#13 "this month", #1 "BREAKING NEWS") against the posting date, since queued Shorts wait days.

## Sources (read Oct 4-5, 2026)
- ESPN push-off guidelines: https://www.espn.com/nba/story/_/id/50063714/nba-issues-new-guidelines-instructs-refs-crack-push-offs
- ESPN Brown fined / 10 fouls: https://www.espn.com/nba/story/_/id/48689072/celtics-jaylen-brown-fined-50000-criticizing-officials ; AP via https://www.nbcboston.com/news/local/celtics-jaylen-brown-fined-by-nba-for-public-criticism-of-playoff-officiating/3945648 ; Yahoo https://sports.yahoo.com/articles/nba-refs-emphasize-off-arm-192901153.html
- ESPN Clippers punishment: https://www.espn.com/nba/story/_/id/49806683/nba-punishes-la-clippers-kawhi-leonard-investigation-30-million-fine-steve-ballmer-suspensions-top-questions ; precedent https://www.espn.com/nba/story/_/id/49951012/nba-weighed-precedent-punishing-clippers-salary-cap-case
- Kawhi trade: https://www.nba.com/news/raptors-clippers-kawhi-leonard-trade ; https://www.hoopsrumors.com/2026/09/clippers-raptors-agree-to-complete-kawhi-leonard-trade.html ; extension https://www.espn.com/nba/story/_/id/50007389/raptors-agree-2-year-115m-extension-kawhi-leonard ; https://www.usatoday.com/story/sports/nba/raptors/2026/09/22/kawhi-leonard-contract-extension-raptors-details/91892708007/
- LeBron: https://www.espn.com/nba/story/_/id/49440164/lebron-chooses-76ers-sign-2-year-8-million-contract ; https://www.espn.com/nba/story/_/id/49227450/lebron-james-signs-philadelphia-76ers-grades-reaction-lakers-contract ; https://www.hoopsrumors.com/2026/07/nba-minimum-salaries-for-2026-27.html ; https://www.spotrac.com/nba/player/_/id/2257/lebron-james
- Bronny: https://www.nba.com/news/bronny-focused-on-his-own-path-lakers-media-day ; https://www.espn.com/nba/story/_/id/50055730/bronny-lebron-james-lakers-exit-got-own-path ; https://sports.yahoo.com/articles/bronny-james-reveals-lakers-directive-014513156.html ; https://www.nba.com/sixers/news/philadelphia-76ers-2026-27-schedule-release-marquee-matchups-and-more ; https://abcnews.com/GMA/Family/lebron-james-calls-playing-son-bronny-nba-greatest-accomplishment/story?id=117717658
- #11 clip recovery: git `origin/short-11-jordan`, commit f756001, `_clips_recipe.py` and `clips/S*.mp4`.

## Not verified
Audio quality, "Four F's" pronunciation, whether the NBA's Brown/Oubre clip is from the playoffs, the exact 2019 Paul George pick count, identity of "Gradey Dick" in the wide shot, other src videos in #23's folder.
