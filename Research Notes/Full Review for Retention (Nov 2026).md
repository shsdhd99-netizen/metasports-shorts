# Full Review for Retention (Nov 1, 2026)

Question (owner): we sit at 15-30K views a Short; what keeps us from 100K+? Question every default; keep a rule only if our data or strong outside evidence supports it.
Tiers: **[V]** measured on our data · **[S]** seen in a few examples or on other channels (Gemini-watched, model-observed, not measured) · **[H]** a guess.
Data and code: `Tools/review_measure.py` (re-runnable), `Research Notes/Full Review data (Nov 1, 2026)/` (`features.csv`, `correlations.csv`, public view lists, `gemini ask/`). Builds on today's Editing Study, Soccer Topic Study, Soccer Script Craft, Idea Gauging, Daily Brief and the API retention CSVs; nothing here repeats them.

## 0. The answer in six lines
1. **The edit is not what separates 3K from 30K.** Our post-Oct-26 builds already sit next to the winners on pacing (NBA: 12 shots, 2 in the first 3 s, shot 1 = 2.95 s, median shot 2.0 s, 224 wpm; FC: 31 shots, 226 wpm, median shot 2.0 s) [V]. Inside each competitor channel the better half and worse half edit almost identically: music 100% vs 97%, caption colour 39% vs 48%, real audio 39% vs 52%, loops 17% vs 27%, zooms 20% vs 25% (n=64 vs 64 Shorts, six channels, Gemini [S]). What differs is the premise, and how fast the viewer decides in the first 1-3 s.
2. **The viewer decides in the first 4 seconds.** On the 16 of our Shorts we can join to API retention curves, the single steepest 2%-step drop is in the first 4 s for 15, and 40 of the 48 steepest drops are in the first 4 s [V]. Only 17 of the 48 sit within 0.5 s of a cut, so it is the swipe decision, not a bad cut. Frame 1 and line 1 are the job.
3. **Topic is the biggest lever we can measure.** FC goalkeeper-in-a-shootout: 4 of 4 posted Shorts at 15-30K (S01 30K, S05 29K, S03 15K, S17 17K at 2 days; S17 was the test of "trick vs goalkeeper": a plain goalkeeper subbed on, no trick, still 17K) against 0 of 8 others above 3.2K [V, n=12]. NBA: the same pattern in the Idea Gauging page.
4. **Shorter NBA wins.** Voice of 22 s or less: median 10.0K public views vs 3.1K above (n=8 vs 16) [V, small n]. Line 1 of 11 words or fewer: 8.0K vs 3.4K (n=18 vs 6) [V small]. A number spoken before 3 s: 3.4K vs 8.0K (n=10 vs 14) [S].
5. **We copy the winners' look less than we think.** CoachClank's three biggest Shorts we asked Gemini about (34M, 26M, 1.2M) all show: small sentence-case white captions, no colour, no pop, **no SFX**, a quiet music bed, 1-6 cuts per 10 s [S, n=3, plus the frame study in the Editing Study]. Ours: large all-caps, coloured words, pop-in, a whoosh or whistle. Whether that costs views is **untestable on our data** (all our Shorts used one caption look), so it is an A/B, below.
6. **Most of what is left is cheap:** a handful of QA checks (added), two opt-in tool switches (added), and a list of things to stop.

## 1. What was measured and how far to trust it
- 90 production folders read (`words.json`, `cuts.json`, `captions.ass`, `sfx.json`, `music.json`, final mp4: frame-1 brightness, length). **Joined to results: 29** by title match (folder names are truncated and some posted titles were reworded). Public views (yt-dlp, Nov 1; YouTube rounds large counts to 2 digits) for 24 NBA and 9 FC; API stayed-proxy (`engaged_ratio`, average % viewed) and retention curves for the 18 NBA + 10 FC Shorts at 3+ days.
- **n is small everywhere.** FC's 9 are confounded by topic (4 goalkeeper hits), so no FC edit feature can be read on its own: with n=9 the top correlations (|rho| 0.5-0.8) are what topic would produce. NBA n=19-24 gives a direction, not a proof. I report group medians with n and call them [V small] / [S].
- Nothing in our data varies caption look, SFX, zoom or punch-ins, so those cannot be tested here. They are judged on competitors and on frames.
- Gemini's word-timing/wpm and music fields are unreliable (it hears crowd noise as music and returned 175 wpm for almost everything). I used its **transcript word count over length** for wpm, which matches the numbers we know, and its caption/SFX/cut descriptions only as [S].
- Competitor watching was economical: 12 targeted `--ask` questions (3 per channel: CoachClank, swishyhoopz, Ahmed's Goal, Ahmed's Basketball; 2 top + 1 median each) on top of the 171 reports already in `Watch Reports/`. Our own last 10 per channel were NOT sent to Gemini: our own files give exact values, and it misreports our music and shot counts (Oct 27/28 calibration).

## 2. The retention curves: what happens at each drop (API, 18 NBA + 10 FC Shorts)
| What we see | Detail | Cause (read from words, cuts, footage) | Tier |
|---|---|---|---|
| NBA drop at 0.7-1.5 s | "Who Has Missed The Most Threes" (-17 pts at 1.0 s, spoken: "has missed more threes"), "Who Has Lost The Most Games", Wemby "Worst Night", Caitlin Clark: all on line 1 **before** the first cut | The claim is a record/superlative the viewer judges in one second (older builds: no shot list to read the frame) | [V] observation, [H] cause |
| NBA action openers (Haliburton, This Kid, Rookie) | Drop of -8 to -13 pts at 0.9-1.3 s, 0.9-1.3 s from the nearest cut, while the first sentence is still being said ("just threw an alley-oop", "every second of") | Same swipe decision even with action on screen; the fix is a faster, bigger first sentence, not a different cut | [S] |
| SGA "Ended His Own Record" | -16.5 pts at 1.0 s with a face shot, name spoken is a mouthful ("Gilgeous-Alexander just ended the") | A long surname before any picture of action | [S] |
| FC hits (sock, bottle, danced): -28 to -34 pts at 1.8-2.4 s, again at 3.0 s | Exactly at the end of the title line and the start of "Back in 2006 / 2005 / 2018" (cut 0.1-0.9 s away) | The swipe happens as the spoken title ends; the viewers who stay hold 83-97% average viewed | [V] observation |
| FC end of curve | Only the two over-length Shorts ("Players who got in TROUBLE...", Loch Ness) drop at 56-64 s | Ending past 59 s / viewers leaving as it runs out | [S] |

Does speaking the title first cost us? No evidence it does: Ahmed's Goal opens with the title line in 26 of 36 Shorts (top half 14/18, bottom half 12/18) [S]. Keep it. The goalkeeper dip is the price of a plural title the winners also pay; the only open test is an action-first opener (change 6).

## 3. Every hard-coded default we have, what the evidence says, and the verdict
| Part | Default now | What winners do | Our data | Verdict |
|---|---|---|---|---|
| Caption font/size/y | Montserrat Black 86, y 1100, outline 6, 1-3 words (max 19 chars), pop-in 86%→100% in 90 ms, width capped 700 px; FC: TikTok Sans SemiBold 80 at y 960 | CoachClank: small, sentence case, y≈50%, no pop. Swishy: bold caps, 3-4 words. Ahmed: small centred | Never varied → untestable | Keep default; A/B `--caption-style clank` (change 8) |
| Caption colour | Whole card red if it holds a SHOCK word (incl. "no", "not", "until", "cut", "first"), green for numbers/"big" words, ≤35% of cards | CoachClank 3/3: none. Gemini 128 Shorts: better halves use colour a little LESS (39% vs 48%) | Our colour was on 25% of cards or fewer | New opt-in `--color-rule word` (1 word per card, 1 card in 4) and `none`; default unchanged |
| Words per card | 2.4 NBA, 2.5 FC | 2-4 | no variation | keep |
| Voice speed | 224 wpm NBA, 226 FC (Alex @1.2) | Transcript wpm: Ahmed's Goal 230, Ahmed's Basketball 226, CoachClank 257, swishyhoopz 259, Rebound Rewind 182; top vs bottom half identical in every channel | our wpm not correlated with views (|rho|<0.4) | **233 wpm is right for soccer.** NBA could go to ~245 but there is no evidence; keep |
| Pauses | `tighten_voice` keeps 0.12 s (manual), default 0.06; median gap 0.04 s, 0 pauses over 0.3 s | similar, minimal | n/a | keep |
| First line | ≤11 words, name/number/stakes, done by ~3 s (median 2.66 NBA, 2.94 FC) | title line first (Ahmed 26/36) | ≤11 words: 8.0K vs 3.4K (n=18/6) | keep, enforce |
| Shot 1 / shots in first 3 s | ≥2.0 s, ≤2 shots in 3 s | CoachClank 7-8 cuts in 21 s; swishy 1 per 2.6 s | ours: shot 1 median 2.9 s | keep |
| Shot length | median 2.0 s | 1.3-3 s | NBA ≥15 shots lost in Oct data | keep |
| Zoom / punch-in | none by default; `zoom` per shot, `--auto-zoom` 0 | Gemini: zoom in 20% of top vs 25% of bottom; CoachClank "natural camera only" | NBA zoom≥1: 12.9K vs 5.8K (n=2/22, noise) | **Do not add punch-ins.** Tool already has `zoom`; use it for a small hook subject (edit_lint) |
| Blur-fit | 3:4 window (0.75) on wide plays, fill dimmed −0.12 brightness | footage fills 60-70% of the frame, fill reads as picture | #82/#48 frames | Keep 3:4; new `--fill-brightness` (opt-in, default old) |
| Music | opt-in bed −20 LU under voice, +2 dB gap lift, 1 s fade, drop under real audio | 96% of top Shorts have a bed, quiet (hip-hop/lo-fi), no drops | NBA music n=4 9.9K vs n=20 4.75K (confounded: music was used on later, more spectacle-heavy builds); FC: all with music, no control | Keep the A/B; no change [H] |
| SFX | catalog of 22 (whoosh, whistle, rim...), sparingly at turns | CoachClank 3/3 none; competitors' median SFX per 10 s = 0.0 | NBA SFX≥2: 5.6K vs 10K (n=17/7, confounded) | **Stop decorative SFX**; keep one only when it is the sound of a visible event (whistle on the whistle) |
| Real audio | opt-in, bed −15 (NBA) / −26 (FC), bursts at full level | CoachClank keeps arena sound under the voice | n=2 | keep testing (rule 11) [H] |
| Loudness | −14 LUFS, true peak ≤ −1 dBTP | same | passes | keep |
| Frame 1 | luma 70-115, lit, subject moving | subject big from frame 1 | median 89 / 96 | keep |
| Ending | stop on payoff; last shot ≤ 2.8 s (lint) | no filler | NBA last shot 2.2 s, FC 2.7 s | keep, lint added to QA |

## 4. Competitors (Gemini `--ask`, 12 Shorts) in one table [S]
| Channel | Captions | Colour | SFX | Music | Cuts/10 s | First 2 s |
|---|---|---|---|---|---|---|
| CoachClank (34M, 26M, 1.2M) | small sentence case, 2-5 words, centre, no pop | none (3/3); one used light blue for quoted dialogue | none | quiet hip-hop/lo-fi | 1-6 | the first sentence's action already moving |
| swishyhoopz (30M, 22M, 261K) | bold caps 1-4 words, black outline, pop | scores/counters change yellow→green; captions white | whoosh/swish and a counting tick on action | upbeat trap, below voice | 4 | the stunt in frame 1, "This shot is worth 27 points" |
| Ahmed's Goal (1.9M x2, 121K) | small, 2-6 words, pop | key names/stakes in yellow (Gemini; frame study says plain white: it is inconsistent) | whoosh on transitions | cinematic/electronic | fast | story line first, title as on-screen text |
| Ahmed's Basketball (530K, 461K, 241K) | sentence case 2-5 words | none; stat callouts as separate graphics | whistle/whoosh/pop on overlays | beat | 4-6 | title spoken and shown at the top |
The only consistent signal: **the footage is big and moving from frame 1, and the caption is quiet.** Nothing here supports more colour, more SFX or more zooms.

## 5. The 15 changes, ranked by likely effect on stayed % and views
"Done" = already in the tools/skills after this review. "Test" = an A/B we run. Measure at 72 h.

| # | Change | Evidence (tier) | Status | How we will know |
|---|---|---|---|---|
| 1 | **Pick the premise by the gauge, goalkeeper/spectacle first.** FC: goalkeeper + odd device/shootout; NBA: moment you can watch. Skip rules, record numbers, hypotheticals | FC 4/4 GK ≥15K vs 0/8 others >3.2K [V n=12]; NBA flop shapes in Idea Gauging [V]; S17 plain goalkeeper 17K [V] | Done (Soccer Playbook v2, `idea_gauge.py`, daily-run) | share of posts ≥10K: target 2 of the next 5 per channel |
| 2 | **Shorter NBA moment: ≤22 s of voice; cut colour sentences first** | ≤22 s median 10.0K vs 3.1K (n=8/16) [V small]; stayed-proxy: avg viewed 99% vs 87% [V small] | Done (QA warn >24 s; nba-short/rules) | next 10 NBA: median views and avg % viewed vs the last 10 |
| 3 | **Line 1 ≤11 words, a name/action before any number; the number comes after the viewer has a picture** | line1 ≤11: 8.0K vs 3.4K (n=18/6) [V small]; first number <3 s: 3.4K vs 8.0K (n=10/14) [S]; Oct data 72.6% vs 62.2% stayed [V] | Already a rule; QA hook check kept; wording tightened | stayed % of next 10 |
| 4 | **Treat the first 1-3 s as the whole retention job:** frame 1 = the thing happening, large, moving; no setup words; a surname of 4+ syllables not first (SGA: "Gilgeous-Alexander just ended" = -16.5 pts at 1.0 s) | 15/16 steepest drops in first 4 s [V]; only 17/48 near a cut [V] | Done in rules; edit_lint "small hook subject" now in QA | retention at 3% elapsed (API `ret_at_3pct`, median NBA 1.54, FC 1.30 today) up by 0.1 |
| 5 | **FC: test an action-first opener on the next two goalkeeper Shorts** (open on the first story sentence over the action, title as on-screen text only) | FC hits dip 28-34 pts exactly as the spoken title ends [V]; Ahmed's Goal does both (26/36 title first, rest story-first) [S] | **Test**, not default | stayed % and retention at 3%, the next two goalkeeper Shorts vs the previous three; n=2 vs n=3 is a signal at best |
| 6 | **Footage big, no black, no clipped bug** (zoom 1.5 on a small hook subject; full frame when the scorebug is the proof; lighter fill) | 6-Short frame study [S]; #82 v1 flaws | Done: `edit_lint` runs inside `qa_short` as warnings; `--fill-brightness`; demos use it | edit_lint clean on every new Short; stayed % vs the last 10 |
| 7 | **No same angle three times in the hook; a new picture per idea** | Editing Study [S] | Done (lint) | same as 6 |
| 8 | **Quiet captions A/B:** `--caption-style clank` (NBA) and `--color-rule word` on 2 Shorts per channel | CoachClank 3/3 plain [S]; colour no help within channels (39% vs 48%, n=64/64) [S]; ours never varied [V] | **Test** (tools ready) | stayed %, 4 vs the channel's last 10; decide after 8 Shorts |
| 9 | **Stop decorative SFX** (one SFX only when it is the sound of an on-screen event) | CoachClank none; competitor median SFX/10 s = 0.0 [S]; ours SFX≥2 5.6K vs 10K (confounded) [S] | Done in rules (stop list) | n/a; no loss expected |
| 10 | **Time-free wording** ("just", "yesterday", "tonight" in line 1 for a Short that may post days later) | #73 built Oct 27, posts a week later [S] | Done (QA warn) | none (hygiene) |
| 11 | **One number on screen at a time** (no counter plus a caption of the same number) | #48 [S] | Done (QA warn) | none |
| 12 | **Escalating counter** (same slot counts up, swishy style) | swishy 30M/22M both use it [S, n=2] | Not built yet: needs a "from/to" in `overlay.py` | build for the next list-style Short; compare retention |
| 13 | **Judge at 72 h and compare with the channel's last 10, never one number** | Posting Study; S03 1.4K at 10 h → 14.5K [V] | Done | habit |
| 14 | **Real-audio moments** (keep testing; keep narrated spare) | n=2 [H] | Test running | after 5 posts each |
| 15 | **Pin the comment on every Short the day it goes live** (the API cannot) | Daily Brief | Owner step | comments per 1K views |

Not changed because the evidence did not support it (kept, with the reason): voice speed (competitor wpm 226-259, ours 224-226, no top-half/bottom-half difference), words per caption, shot length, music default, punch-ins/zoom ramps (Gemini 20% vs 25%), freeze frames and arrows (0-4% of winners), emoji (5% vs 3%, and flops), title wording (no effect), loops (17% vs 27%, wrong way round).

## 6. Small-mistakes checklist (each now has a check, or says why not)
| Mistake that slipped | Check |
|---|---|
| Wrong or stale fact ("still the record", Mourinho knee slide) | `notes.md` claims table with the exact source wording (rule). New: QA lists claim words (still/record/first/never/only/most) to verify on the day [Done in `qa_short`] |
| Dark frame 1 | `qa_short` frame-1 luma (exists) |
| Voice glitches / mis-heard names | `voice_take` check + `pronunciation.json` + `export_check` captions vs script (exist) |
| Captions too fast / off-screen | `export_check` timing and safe area (exist); `comfort_audit` for reading speed (context only) |
| Sound cut off at the end | `qa_short` end-peak check (exists) |
| Dead air | `tighten_voice` + `qa_short` 0.6 s gap FAIL (exist) |
| Edit made outside the pipeline skipped the limiter (S18) | after any direct DRAFT edit run `comfort_audit.py` true peak (rule exists) |
| Re-render of a folder brings back removed lines (#74, S18) | use `word_edit.py` before re-rendering (rule exists) |
| Same picture three times in the hook; clipped scorebug; long closing hold; tiny hook subject | **new:** `edit_lint` inside `qa_short` |
| Double number on screen | **new** QA warn |
| Time-bound wording | **new** QA warn |
| NBA Short running past ~24 s | **new** QA warn |
| Wrong music version posted / A/B unlogged | log version in Outcome Log (rule); not automatable |
| Gemini says "music" for a no-music cut | do not use its music field (documented) |

## 7. Stop doing
- Decorative SFX; more than one SFX in a 20 s Short.
- Colouring function words ("no", "not", "until", "cut") or whole cards without a rule (use `--color-rule word` for the A/B).
- Building a Short whose gauge shape is a flop (rules, record counts, hypotheticals, "most/worst" lists of lesser names).
- NBA moment Shorts over ~24 s of voice, and any FC Short that runs to 59.5+ s.
- Citing a scorebug the 3:4 window cuts in half; showing one play from one camera three times in the first 8 s.
- Judging a Short before 72 h; posting from a build older than 2-3 days with "just"/"yesterday" in line 1.
- Adding punch-in zooms, freeze frames, arrows or emoji because a top Short has one (no evidence they matter).

## 8. What was implemented (all opt-in or warnings; no default render changes)
- `Tools/review_measure.py` (new): re-runs this whole measurement.
- `Tools/captions.py`: `--color-rule card|word|none` (default `card` = old behaviour); `assemble.py --color-rule` passes it through.
- `Tools/broll.py` / `cut_list.py`: `--fill-brightness` / `"fill_brightness"` per shot (default −0.12 = old).
- `Tools/qa_short.py`: new warnings (voice length NBA, time-bound wording, same number twice, edit_lint, claim words to verify). No new FAILs.
- Skills and THE RULES updated: `cloud-short`, `story-short`, `nba-short`, `daily-run`, `MetaSports - Playbook.md` THE RULES, `Soccer Channel/Playbook.md`.

## 9. What we cannot know yet
- Whether quiet captions or no colour lift stayed %: needs the A/B in change 8 (8 Shorts).
- Whether an action-first FC opener beats the title-first opener: needs 3+ vs 3+ goalkeeper Shorts (change 5).
- Whether music helps: NBA 4 vs 20 and FC 9 vs 0 are not tests.
- The 100K+ question itself: none of our 130 Shorts has passed 30K, and the competitors with 100K+ medians are 5-30x our subscriber base. The data say the next gain is the premise (change 1) and the opener (changes 4-5), not the edit.

## 10. Before/after demos
See the section appended below after the demo renders (`Research Notes/Full Review demos/`).
