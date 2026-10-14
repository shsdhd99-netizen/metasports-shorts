# Rules Audit (Oct 14, 2026): KEEP / REVISE / RETIRE / TEST

**What this file is:** every creative, editing, voice and workflow rule we use, treated as a hypothesis that has to earn its place.
- **Evidence:** `Posted Video Audit (Oct 14, 2026).md` (102 Shorts, analytics, 10 retention curves), `Voice Audition (Oct 14, 2026)/`, `Winning Formula v2`, and the critic reviews.
- **The outcome** is written into `MetaSports - Playbook.md` → "CREATIVE SYSTEM v3" and into `Tools/qa_short.py`.

**Tiers:**
- **[V]** verified in our data
- **[R]** reported
- **[E]** external (other channels or outside research)
- **[H]** hypothesis

**Confidence:** H / M / L.

**Cautions:**
- Our sample is small. The new era has 18 posts with analytics, and most are under 3 days old at their final read.
- The era effect (section 2 of the audit) overshadows everything.
- No decision below is "proven". KEEP means the evidence leans that way and the rule costs little.

## A. Story and script
| # | Current rule | Source / why it exists | Supports | Contradicts | Decision | Better alternative | Conf. | How to test |
|---|---|---|---|---|---|---|---|---|
| A1 | Every Short = Hook / Context / Payoff | CoachClank study [E]; Strict Formula | All 3 new-era winners fit [V] | Chris Paul (28.4K) is an emotional arc, not a paradox → payoff. Curry (30.8K) is "moment + hidden reason" [V] | **REVISE** | H/C/P is the default for **3 formats**: (1) paradox, (2) moment + hidden reason, (3) emotional arc. Each has its own shape (Playbook v3) | M | Tag every post's format in the Outcome Log; compare medians at n≥4 per format |
| A2 | One visible object + one paradox in second 1 | Winning Formula v2 | #22/#03/#19 [V]. Old Flagg (hype, no fact) 4.9K vs new Flagg (visible number) 20.6K [V] | LeBron 23rd had a visible fact and good retention, and still got 5.3K (the fact was everywhere) [V] | **KEEP** for format 1, plus **novelty**: the fact must be one most fans haven't seen | Add "not the night's most-covered fact" to the gate | M | Premise-first scoring (D1), validated at 10 posts |
| A3 | First line ≤10 words | Strict Formula [H] | #22 (11 words, clear by 2.1 s) [V] | #03's hook is 16 words, clear by 4.1 s, and got 27K. #20's 4-word hook ("Ninety-two point nine.") flopped [V] | **REVISE** | **One idea, clear by about 3 s.** Measure time-to-question, not words. No compound sentences (#13: 6.1 s) and no naked numbers (#20) | M | QA warns if the first sentence ends after 3.5 s or opens on a bare number |
| A4 | Context: every sentence adds a fact on the same measure | Winning Formula v2 | #29 (6 numbers, 5 measures, 1.5K). Duren cliff at 4-6 s on contract terms [V] | #41 v2 shifts to skills for its answer; the critic called it weak but passing | **KEEP** as default | The payoff may switch measure **only** if it answers the opening "why" | M | Critic v2 Gate A3 |
| A5 | Ending answers the opening; no question, CTA or hedge | Strict Formula | Question endings #12 and #18 both about 2.8K. #19 ends in its subject's own voice (20.6K) [V] | Curry's CTA ending still got 30.8K [V]; n is small | **KEEP** | Prefer the subject's own words or one number | M | Count answer vs question endings across the next 10 posts |
| A6 | No CTA | CoachClank [E] | The CTA line drops end-viewers 12-27% (Curry, old Flagg curves) [V] | No data that it costs reach; Curry had one | **KEEP** (zero cost) | The debate goes in the pinned comment | M | Optional pair: same-format Shorts with and without "follow for..." |
| A7 | Absolute, confident wording | CoachClank style [E] | Confident hooks are clearer [H] | #17's over-promising title ("BAN") went with 81% viewed. #40 kept "probably" and passed the critic [V] | **REVISE** | Keep the qualifier when it is part of the truth ("listed", "probably", "regular season"); confidence comes from specifics, not from overclaiming | M | Critic Gate A6 |
| A8 | Runtime 21-45 s, target 21-26 (QA FAIL under 21) | CoachClank: 21 s+ stories beat ≤20 s, 848K vs 291K [E] | — | Old era: **under 18 s median 32.8K (n=9)**, 18-20 s 30.4K, 21-25 s 30.6K, 26-33 s 26.2K [V]. No length effect (rho −0.13) [V]. The floor forced padding and re-records on #40 | **REVISE** | Length follows the story: moments 12-20 s, paradox stories 18-26 s, arcs up to 30 s. QA only **warns** under 15 s or over 35 s | M | Track length vs avg % viewed; build one 15-17 s visual moment |
| A9 | Same pacing for every story | Strict Formula | Fast narration goes with views (rho +0.50, n=16) [V] | Emotional arcs (Chris Paul) may need air [H] | **REVISE** | ~~Fast (250-290 wpm)~~ 200-265 wpm (see C2 revision); arcs may slow to about 200 with one pause on the turn | L | One arc Short at a slower pace, compared with the format median |
| A10 | Reject a story a bigger channel already told | Round 5 [E]; #29 vs CoachClank | #29 1.5K [V] | Curry, Giannis and Chris Paul were widely covered and still got about 30K [V] | **REVISE** | Reject only when **our angle** is the same as the big telling. A fresh angle on a known event is fine | M | copy_check plus an angle note in notes.md |
| A11 | Don't re-post an identical file; don't retell an old winner by name | Outcome Log | #25 re-post 193; #29 1.5K vs 73K [V] | — | **KEEP** | — | H | — |
| A12 | Don't frame a story as "tonight" news on the most-covered fact | NEW (LeBron 23rd: 5.3K with good retention) | [V] n=1 | — | **TEST** (as a gate warning) | Lead with the angle nobody else has | L | Track "news-frame" Shorts |

## B. Editing
| # | Current rule | Source | Supports | Contradicts | Decision | Better alternative | Conf. | Test |
|---|---|---|---|---|---|---|---|---|
| B1 | Frame 1 is the object, readable at phone size | Strict Formula | Winners' frame 1 = the object. Old Flagg's tiny wide shot started at 1.56 [V] | — | **KEEP** | Frame 1 can be the **moment** (a ref holding the ball) or the **person** with a scale reference | M | Critic Gate A2 |
| B2 | ≥3 shots in the first 3 s (QA FAIL) | Fast-cut lore [E] | — | Shot length didn't separate winners from flops (Flagg 1.15 s avg, same as the flops) [V]. The rule forced #40's weak far-wide shot (the critic called it optional to fix) | **REVISE → warn** | Cut when the picture's information is spent | M | Optional A/B: a 1.9 vs 2.8 s average-shot pair (pending since Oct 5) |
| B3 | Average shot ≤2.6 s (QA FAIL) | Same | — | Same | **REVISE → warn** | Same | M | Same |
| B4 | B-roll ≥35%, talking head ≤45% (QA FAIL) | House | Proof footage beats talk [H] | Forced #41's reach clip under "led the G League in blocks"; a card is better proof there [V] | **REVISE → warn** | The real rule is B6 (every claim has proof on screen) | M | Critic Gate B |
| B5 | Cards ≤25%, none before 4 s (FAIL / warn) | Strict Formula | An early card goes with 1.9K vs 3.9K median (n=5 vs 13) [V, confounded] | Cards are the proof for numbers. The cap forced #41's 350 card later than ideal | **REVISE** | Keep the warn for cards before 4 s (TEST); demote the 25% cap to a warn; never two cards in a row | L | Every new build follows "no card before 4 s"; compare at n≥6 |
| B6 | Every claim with a name or number has proof on screen | Critic | Critic v2 caught wrong-picture beats in #40, #41 and #32 [V] | — | **KEEP** | — | H | Critic Gate B |
| B7 | Last shot reuses the first clip (QA FAIL) | Loop lore [E] | Winners start at 1.74-1.83 (loops/replays) [V] | Forcing it created a 0.28 s noise shot in #41 [V] | **REVISE → warn** | End on an image that flows into frame 1 **when it serves the payoff**; never add a sub-0.6 s shot just to loop | M | Compare start ratios across ending types |
| B8 | Gentle push-in (≤6%) on frame 1 and stills only; no random zooms | Oct 5 test | Flash cuts washed out faces [R] | — | **KEEP** | Motion only with purpose (reveal a detail, follow the ball) | M | — |
| B9 | House captions (white ALL CAPS, 45-62% band) | House | Caption style didn't separate winners [V] | Captions sat on Wemby's chin and mic in #41 v1 [V] | **KEEP** the style; **REVISE** placement | Re-crop the shot or move the band per shot when a face sits in the band. Avoid single-word orphan cards ("CAREER.") | M | Critic Gate B |
| B10 | No music | Owner rule Oct 5 [D] | — | No data either way | ~~TEST~~ **RETIRED Oct 14 (later) by the owner: music on by default** (see the addendum) | A bed 20 dB under the voice, chosen by story type | L | M1 cohort (Outcome Log) |
| B11 | 2-3 sound effects, only where the picture makes the sound | House | — | — | **KEEP** (no evidence, low cost) | — | L | — |
| B12 | No hook headline text (owner rule Oct 4) | Owner [D] | — | **#19 is the only post with an on-screen premise pill, and it reached 20.6K**; it was posted alongside losers [V, n=1] | **TEST** (owner decides) | A small premise pill on frame 1 only (e.g. "6-8 to 6-11?") | L | Alternate 3 pairs of similar Shorts, with and without a pill. Adopt if the pill wins 2 of 3 |
| B13 | Red circle on the object in frame 1 | Winning Formula v2 (old era 7/27 vs 2/44 at 40K+) [V, one coder] | — | — | **TEST** (running: #40 ring vs #41 plain) | — | L | Running |
| B14 | Crop burned-in tickers, scorebugs and source captions | Critic | #41 v1 had cropped bugs [V] | Old hits KEPT the scorebug as proof (Luka, Kobe) [S] | **REVISED Oct 14 (later)** | Crop tickers and others' captions always; keep the scorebug when the clip is the exact game (circle the number); crop it on stand-ins | H | S1 (Outcome Log) |

## C. Voice
| # | Current rule | Source | Supports | Contradicts | Decision | Better alternative | Conf. | Test |
|---|---|---|---|---|---|---|---|---|
| C1 | Clone "pham v2", multilingual_v2, speed about 1.1-1.15, stability .65 | Oct 5 lab | Audition: the only voice at the house pace natively (245-268 wpm); equal intelligibility; good consistency [V] | Naturalness unheard by me; v3 voices have more pitch variety [V] | **KEEP** (fallback: clone "Pham", take D) | — | M | Owner listening task (Voice Audition README) |
| C2 | Narration 247-289 wpm | CoachClank [E] | Pace goes with views in the new era (rho +0.50) [V] | **Our own old hits measured 182-212 wpm** from timed transcripts [V, n=3] | **REVISED Oct 14 (later)** | Warn outside 200-265 wpm: don't drag, don't rush | M | — |
| C3 | Respell hard names ({Wembanyama\|wem-bun-YAH-muh}) | Oct 5 | — | The recogniser heard "Wembun Yama" in 9/9 respelled takes, and "Wembanyama" with the plain spelling [V, n=1 each] | **REVISE** | Plain "Wembanyama"; keep "Yoki-ch" for Jokic. Verify each name with the recogniser on a test line before the full take | M | Owner's ear (A vs A3) |
| C4 | Time-stretch ≤1.08x | Oct 5 lab | HNR drops with stretch [R] | — | **KEEP** | — | H | — |
| C5 | Flash model to save credits | Never adopted | — | Flattest pitch (3.69) and worst phone intelligibility [V] | **RETIRE** the idea | — | M | — |

## D. Workflow, scoring, titles
| # | Current rule | Source | Supports | Contradicts | Decision | Better alternative | Conf. | Test |
|---|---|---|---|---|---|---|---|---|
| D1 | Queue score N C Q S E V A U F (/45) | Oct 13 | — | Never validated. The previous craft score ran backwards (rho −0.63) [V] | **REVISE** | A premise-first score: Clarity in second 1 ×3, Novelty of the angle ×3, Visual proof secured ×2, Stakes/emotion ×2, Audience name ×2, Accuracy gate (pass/fail), Feasibility ×1. Written down **before** posting | M | Prediction check: at 10 posts, Spearman of score vs 48 h views |
| D2 | Script first, then find footage | The old pipeline | — | #40's "No look" mismatch and #41's frame-1 problem came from footage found too late [V] | **REVISE** | **Footage-first gate:** secure frame 1 and a proof clip for each beat **before** voicing | H | Count critic Gate B defects per build before vs after |
| D3 | Critic v2 (independent agent) before "ready" | Oct 13 | It found real defects in 3 of 3 builds [V] | — | **KEEP** | — | H | — |
| D4 | Craft-score critic ranks the posting order | Round 3 | — | rho −0.63 [V] | **RETIRED** (Oct 13) | Order by premise score and deadline | H | — |
| D5 | Titles: 4-7 words, Why/How/What/Did/Is + emoji | Clank title study [E] | — | Old era: no title split moves the median more than 3K [V]. The feed is 94.5% of views; search is 3.9% [V] | **REVISE** (lighter) | Title = the premise in plain words, **exactly as packaged**, true to the facts. No more title scoring | M | — |
| D6 | QA warn: title starts with a name | Clank n=20 [E] | — | Old era: name-first median 29.9K vs 30.4K [V] | **RETIRE** | — | M | — |
| D7 | QA warn: no turn word in the first 40% | Clank [E] | — | No support in our data | **RETIRE** | — | M | — |
| D8 | 20-30 tags per Short | Habit | — | Search is 3.9% of views; tags barely matter [V] | **REVISE** | Up to about 12 tags and up to 3 hashtags; 2 minutes max | M | — |
| D9 | Pinned comment = the debate question | House | — | No data | **KEEP** (zero cost) | — | L | — |
| D10 | Post 2 a day | Oct 5 plan (YouTube says no penalty [E]) | — | Channel views fell after the 2-3/day stretch (Oct 4: 37K → Oct 10-11: about 4.6K/day) [V, confounded] | **TEST** | 1 a day for 7 days, then compare the per-post 48 h median with the 2-a-day weeks | L | Owner's choice of schedule |
| D11 | Change a rule only at n≥3 or a large effect | Oct 5 | — | — | **KEEP** | — | H | — |
| D12 | Test a premise before full production | NEW | We can't A/B posts; full builds take hours | — | **TEST** | "Second-1 test": write frame 1 + line 1 and score clarity/novelty **before** scripting. Build only if it scores ≥ the queue median | L | Prediction check (D1) |

## What changed in the tools today (reversible, in git)
`Tools/qa_short.py` and `Tools/captions.py`; details in `Tools Guide.md` → "Oct 14 changes".
- **B2, B3, B4, B5 (25% cap), B7, A8 (21 s floor): demoted from FAIL to warn.**
- **D6, D7: removed.**
- **New checks:**
  - **dead air** (a gap over 0.6 s inside the speech = FAIL)
  - **slow hook** (first sentence ends after 3.5 s = warn)
  - **naked-number opening** (warn)
- **Captions:** a one-word final card such as "CAREER." now merges into the card before it when the two fit together. Later Oct 14: a per-shot `cap_y` in shots.json moves captions off a face (#21 v3.1).


## Addendum, Oct 14, 2026 (later): old-video study, B-roll sourcing, music and voice emphasis
**Sources:**
- `Posted Video Audit (Oct 14, 2026).md` section 10 (5 old Shorts watched via vidIQ: 4 hits and 1 control)
- `Library/B-roll Sourcing Guide.md`
- `Library/Music Guide.md`
- `Voice Audition (Oct 14, 2026)/README.md` part 2

| # | Rule | Source | Support | Contradiction | Decision | Confidence | Test |
|---|---|---|---|---|---|---|---|
| B10 → **B15** | A music bed by story type, 20 dB under the voice, the payoff marked by the music (silence, stop, swell or hit), dropped under real quotes | **Owner decision Oct 14** [D]; old Shorts 5/5 had a bed [S] | Our beds cost no words in the phone test, even at -2 LU [V] | The weak old control had music too: it did not separate hits from misses [S] | **ADOPT** (house style; no reach claim) | M for clarity, L for views | M1 |
| B16 | Every clip has a `sources.csv` row with link, seconds and what it shows, verified by eye | Owner request Oct 14; #39's wrong-opponent shots; #41's agency photo [V] | Frame matching recovered the exact post and second for 28 of the 40 footage clips in the 4 ready Shorts, plus 4 probable and 1 logged at the cut; 7 have no recoverable download [V] | — | **ADOPT** (QA FAIL once a log exists) | H | — |
| B17 | No agency photos (Getty/Imagn/AP) taken from news posts; official league/team posts first | Licensing practice [E] | #41's Dallas still was an Imagn photo; replaced with broadcast footage [V] | — | **ADOPT** | H | — |
| B18 | Exact-moment footage under nearly every line; generic only under "what if" lines | Old hits (8/11, 11/13 exact shots) [S] | Critic findings in 3/3 builds [V] | Weak control used a generic montage [S] | **KEEP** (strengthens B6) | M | — |
| B19 | Hold the payoff shot longest; escalate to it where the story allows | Old hits [S] | — | — | **TEST** (craft) | L | — |
| C6 | Emphasis comes from the edit (caption colour, circle, music drop, cut-in pause), not the voice | Voice part 2 [V] | Our voice reads numbers flat (-0.4 to +0.2 dB); "..." adds about 0.05 s; expressive settings didn't help | — | **ADOPT** | M | P1 |
| A13 | Question hooks ("Why would X do Y?") | Old hits 3/4 [S] | — | Our best new Shorts (#22, #03) used statements; 0/20 new posts used questions | **TEST** | L | Q1 |
| B20 | A real-quote shot plays at 1.0x (never slowed or held) | Critic v2 on #38 [V] | Lips trailed the audio by up to 0.29 s at 1.094x | — | **ADOPT** (QA FAIL) | H | — |
| D13 | Sound effects need a logged licence | Licensing practice [E] | `Tools/sfx` came from "Downloads/music", source unknown [V] | — | **REVISE**: replace them over time with logged effects (Mixkit free licence or ElevenLabs sound effects) | M | — |

**What changed in the tools:**
- `assemble.py`: `music.json` with a measured bed level, gap lifts, drops, hits and `--no-music`; one render log per output file.
- `qa_short.py`:
  - music licence and level checks, plus the speech-band margin
  - source-log and verification checks
  - pace 200-265
- `footage_lib.py` (new): source logs, frame matching to posts, contact sheets, verify, index, search.
- `x_clip.py` and `broll.py cut` now write the logs themselves.
- `music_gen.py` (new): licensed generated beds.
- `captions.py`: per-shot `cap_y`.
