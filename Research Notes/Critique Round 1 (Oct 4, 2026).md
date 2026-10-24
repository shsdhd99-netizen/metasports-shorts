# Critique Round 1 (Oct 4, 2026)

Role: hostile-but-fair critic. Scope: Shorts #11-#18 (+ #12 v2, #13), the cloud-short skill, `Tools/qa_short.py`, `Tools/assemble.py`, Research Notes Rounds 4-6 and the Lessons log. Evidence I produced: ffprobe/ffmpeg loudness and duration, per-shot arithmetic from shots.json, storyboard.jpg frame reading (#13, #14, #15, #16, #17, #18), hook-frame strips for #11 and #12, re-running qa_short.py with `--infer-kinds`, a regex test of the hook check, and the repo's own 80-Short CSV. I could not watch/hear any Short with human ears, and I could not verify 2026 news beyond what UPLOAD.md cites. Where a point rests on reading small storyboard frames I say so.

Headline: **the pipeline has produced 8 Shorts in two days and has zero outcome data on any of them under the new recipe. Every "rule" is either a hypothesis (the docs say so) or a gate threshold the Shorts pass by construction. The most likely real failure modes are not in the gate at all: story/footage mismatch, same-story-family repetition, a templated sameness across the batch, and hooks that are statements, not promises.**

---

## (a) The 15 strongest criticisms, ranked by expected impact on retention/virality

### 1. Our hooks are news statements, not payoff promises; the gate cannot tell the difference
- **CLAIM:** All eight first sentences are declarative recaps. None opens a gap the viewer needs closed. The skill itself says "the line after the hook must be a payoff promise or a turn"; none of the eight does that.
- **EVIDENCE (script.txt first lines):** #11 "Michael Jordan pushed off Bryon Russell to win the 1998 Finals, and no foul was called." #13 "The Clippers gave up ten first-round picks for Kawhi Leonard." #14 "The NBA just named four stars in one video about one illegal move." #15 "The Miami Heat are about to become Vice City." #16 "Giannis is about to face the Bucks for the first time." #17 "Flop, and the NBA wants a technical foul." #18 "LeBron James just walked into Sixers media day, and asked this." Only #18 ("asked this" -> the quote) and #12 ("one number nobody's talking about") even gesture at a gap. #14 promises four names and delivers the first name at 3.10 s (storyboard: "JAYLEN BROWN" at 3.10 s); a viewer who swipes at 1-3 s has not yet learned who. The `qa_short.py` hook check is `\d|[A-Z][a-z]+ [A-Z]|million|...|first|never|only|rule` on the first 3 s of words: "The Miami" (#15), "The NBA" (#14), "The Clippers" all pass on capitalisation alone. I tested the regex: "This is a Very Boring story about nothing" -> True.
- **WHY IT MATTERS:** Viewed-vs-swiped at 3 s is the only retention number YouTube gives us (Round 6). A hook that states a fact the viewer does not yet care about loses to hooks that create a question.
- **WHAT WOULD PROVE ME WRONG:** 24 h Viewed-vs-swiped >= 70% on #14/#15/#16/#17. Or an A/B in which the "statement" hook beats a rewritten question/stakes hook of the same Short.
- **PROPOSED FIX:** Add a human-judgement line to notes: "What is the one question the viewer needs answered, and is it on screen/spoken by 1.5 s?" Rewrite #14 as "Four NBA stars just got called for the same illegal move. One is still legal." (name no one first; tease which). Replace the regex with a check that the first 8 words contain a conflict word (but/never/banned/caught/first/only/wrong) or a number, else WARN.
- **CONFIDENCE:** medium-high on the pattern; medium on impact size.
- **COUNTER-ARGUMENT:** News Shorts from Clank/House of Highlights do open on plain statements and still hit; the strong first frame + boom + hook-text carry the first second, not the words.

### 2. #18 tells a Sixers story with the wrong uniforms for most of its b-roll, and the best joke lands without setup
- **CLAIM:** Footage does not show what the words say; the final line has no context for the viewer.
- **EVIDENCE (storyboard.jpg, #18; UPLOAD.md admits "Hype-video b-roll shows LeBron in Lakers uniforms"):** at 0.56 s "JUST WALKED" shows LeBron in a **Lakers** #23; 4.07-6.13 s "THEN HE SIGNED / FOR $8 MILLION / AND MADE / ONE PROMISE" is Lakers/other-team game clips; 10.19-11.25 s "PHILLY HASN'T WON A TITLE SINCE 1983" is **Lakers LeBron in a yellow jersey**; 12.40-13.66 s "THE KNICKS SWEPT THEM OUT OF THAT ROUND" is LeBron in a Lakers jersey at a **Rockets** game (red crowd, Rockets floor) - not Sixers, not Knicks. The 14.4-18.2 s helicopter is three clips (HE1-HE3) of the same grey-sky helicopter, 3.8 s; no note says it is LeBron's helicopter or the Camden facility (UPLOAD cites only a helicopter *heard* during Simons' session). The payoff, "One of us left on a helicopter, the other one was sitting on the curb", is spoken by Tyrese Maxey, who is **never named in the script**, and the "curb" (car trouble that day, per UPLOAD.md) is never explained. Maxey's face appears 18.3-20.1 s with only the quote as caption.
- **WHY IT MATTERS:** Words/picture mismatch is a retention and trust killer; a viewer who knows basketball reads Lakers LeBron over "Sixers" as cheap, and a joke without its setup earns a blank face, not a replay.
- **WHAT WOULD PROVE ME WRONG:** The helicopter clip is verified as the Camden departure and the Lakers-uniform shots hold retention in the 3-12 s window (Studio retention curve), or a user poll shows viewers do not notice.
- **PROPOSED FIX:** Use Sixers-media-day clips of LeBron (the Q1/Q2 clips exist) as b-roll beyond the quotes; add "Tyrese Maxey" and "car trouble" in the narration: "Maxey, whose car broke down that morning:". Add a `uniform_ok` field to shots.json for any Short about a team move.
- **CONFIDENCE:** high on the Lakers uniforms (UPLOAD.md admits it); medium on the Rockets-game read (frames are small); high on the unnamed Maxey.
- **COUNTER-ARGUMENT:** There is almost no Sixers-LeBron footage in week one; Lakers footage is the only visual for "LeBron"; the Q clips carry the credibility.

### 3. Five of the eight Shorts are two story families; #11/#14 and #15/#16 reuse the same footage and ending shape
- **CLAIM:** The batch cannibalises itself and looks templated, a direct hit on YouTube's "inauthentic / repetitive content" language.
- **EVIDENCE:** Push-off rule: #11 (Jordan, 29 s), #14 (four stars, 26.6 s), and #17 (flopping, explicitly "tied to the push-offs" in its own script via Daigneault). #11's shot at ~5.5 s ("NOW THE NBA", Raptors player pushing Mitchell #45) is the same NBA-video clip as #14's opening 0.89-1.40 s (Mitchell #45); both use Brown/Oubre and Barrett/Mobley from the NBA's one video. Heat-GTA: #15 and #16 reuse the same assets (H1_tower, H2_arena, H3_sign, H5_tower2, P_poster) in the same order for their first ~5 s, same neon-sign and poster frames (storyboards #15 0.00-5.1 s and #16 1.96-5.85 s). Ending shapes: all 8 end on a question ("Which star gets called first?", "So how many points does Giannis put on his old team?", "Do flops finally die this season?", "So is LeBron all in on Philly, or just flying through?", "Smart, or a mistake?", "...buying a championship, or paying for 2019?", "So who is actually playing hard on November nineteenth?"). UPLOAD.md for #16/#17 say "post a day apart" - that is the only mitigation.
- **WHY IT MATTERS:** Shorts of the same family compete for the same seed audience, and the second one's viewer has already seen the opening footage. Round 6 itself cites YouTube: "better ... a better video and fewer of them".
- **WHAT WOULD PROVE ME WRONG:** #15 and #16 have similar swipe rates and the second one's views are not suppressed by the first.
- **PROPOSED FIX:** Cap one Short per story family per week; make #16 the only Heat/GTA Short (fold the Adams joke into one 30 s Short) and #14 or #11 the only push-off Short; vary the closer (a statement, a result tease, an unanswered fact) at least every third Short.
- **CONFIDENCE:** high on the reuse (evidence is visible), medium on penalty size.
- **COUNTER-ARGUMENT:** Two different angles on one hot week is how news channels gain topical authority; different titles and speakers; shared b-roll is the only available official footage.

### 4. The "proven" rule lane is not what we are actually making
- **CLAIM:** Round 4's evidence for the rule/ban/"caught" lane (REBOUND: 13 Shorts median 7.7M vs 775K) is evergreen listicle curiosity, with huge-channel reach; we make short-lived preseason news *explainers* that quote the league's own press video.
- **EVIDENCE:** The cited winners are "NBA Players CAUGHT CHEATING" 42M, "3 NBA Rules You Didn't Know Exist" 36M, "3 WEIRDEST Bans In NBA History" 12M (Round 4). Our #11/#14/#17 are "the NBA just issued guidance this week" Shorts built from the NBA's official 2026-27 video, which every outlet and House of Highlights-type account has. REBOUND is a 3.4M-sub channel; a 13-Short median whose top three outliers drive it is not a lane effect. Round 5 labels the lane [PROVEN] "(rule/ban titles got 2.5x the channel median, n=26)": observational, pooled across channels with different baselines. The channel itself has 469 subs and an own median of 29,841 views over 80 Shorts (CSV); its own top hits (80,698 "NBA Players Are Doing THIS", 79,220 "Why Does No One Like Bronny James", 73,001 "Why NBA Players Stopped Shooting Underhand") are timeless "why/odd" curiosities, not news. The channel's 7-month gap and Sora-AI backlog (Roadmap) also mean the audience is not an NBA-news audience.
- **WHY IT MATTERS:** We may be spending a limited upload cadence on the format with the weakest fit to our own history, and the doc treats it as settled.
- **WHAT WOULD PROVE ME WRONG:** #11/#14/#17 views beat the channel's 30K median by 2x+ within 7 days while a "why/odd" Short in the same week does not.
- **PROPOSED FIX:** Rebalance the next 6 Shorts as 3 rule-news and 3 evergreen "Why/How" oddities (the channel's own historic hits); compare 7-day median per type.
- **CONFIDENCE:** medium.
- **COUNTER-ARGUMENT:** Own hits are 7+ months old with a different channel state; REBOUND's lane is still the best signal we have.

### 5. We have no outcome data, and the pipeline is optimised to a gate that does not predict outcomes
- **CLAIM:** Passing `qa_short.py` is uncorrelated with retention by construction; the gate thresholds were set from n=8 or vendor posts, then loosened after the Shorts were built, then called "PASS".
- **EVIDENCE:** SKILL.md and the Lessons log still state the gate as avg shot <=1.9 s, no shot over 3 s, 18-35 s; the code is avg <=2.6, shot <=3.6 (quote 4.5), length 21-45 (`qa_short.py` lines near `chk(avg <= 2.6`, `d > (4.5 ... else 3.6)`, `21 <= total <= 45`). Commit c979f5d "Apply Round 6 findings: loosen unsupported gates". Round 6 says the shot-length rule is "unsupported and partly contradicted by the channel we copy". Measured actual avg shot: #11 1.46, #12 1.90, #13 1.41, #14 1.33, #15 1.44, #16 1.35, #17 1.32, #18 1.24 s, vs Clank's biggest 2026 Shorts at 2.0-4.7 s per cut (Round 3). The gate only warns below 1.3 s. A pipeline whose only measurement is "did it pass our own thresholds" and whose thresholds were copied from "what did we already build" is circular. The documented test ("1.9 vs 2.8 s A/B pending") has not been run; every Short is built at the fast end.
- **WHY IT MATTERS:** Goodhart: we optimise cuts-per-second, kind-ratios and LUFS because those are checkable, while the failure causes (#2, #3, #6) are not.
- **WHAT WOULD PROVE ME WRONG:** A regression of 24 h swipe rate on gate metrics across >=20 Shorts showing the gate metrics explain the variance.
- **PROPOSED FIX:** Treat the gate as a hygiene check, rename it, and stop describing PASS as quality. Make a 2-column log (gate metrics | 24 h viewed%) mandatory for each posted Short. Fix SKILL.md/Lessons to match the code.
- **CONFIDENCE:** high.
- **COUNTER-ARGUMENT:** A hygiene gate catches real failures (#15 v1 talking head, loudness bugs); with n=0 outcomes you need some defaults.

### 6. Hyper-fast cutting is an untested house style, ~40% faster than the channel it copies
- **CLAIM:** 17-20 shots in 23-27 s, new image every ~1.3 s, 2-3-word captions changing every 0.3-0.8 s: a sensory-overload recipe that is also the reason the Short cannot establish who or where.
- **EVIDENCE:** shots.json arithmetic above; #17 has a 0.36 s shot (1.00 -> 1.36 s, V03) and #11 a 0.41 s shot; storyboards show captions changing at ~0.3-0.5 s steps (e.g. #15 6.14/6.45/7.22 s, #18 7.99-9.45 s). The "A new image about every second until 5 s" instruction is in SKILL.md with no source; the doc's own Round 6 table rates faster-cutting [HYPOTHESIS].
- **WHY IT MATTERS:** Cut rate only helps if each shot reads; unidentified players (see #7) and sub-0.5 s shots read as noise. Viewers of 41-second stories need orientation more than novelty.
- **WHAT WOULD PROVE ME WRONG:** An A/B of the same script at ~1.3 s and ~2.2 s avg shot shows no retention gain for the slower cut.
- **PROPOSED FIX:** Run the pending A/B: re-cut #14 or #17 at ~2.2 s avg and post a day apart on equal footing; set a minimum shot of 0.8 s in the gate.
- **CONFIDENCE:** medium.
- **COUNTER-ARGUMENT:** Fast cutting is the style of many top Shorts; Clank's "biggest cut every 2-4.7 s" is the max, not the mean.

### 7. Player/identity and word-picture sync are never verified, and I found concrete misses
- **CLAIM:** The pipeline has no per-shot identity or sync check; names are spoken over clips nobody verified.
- **EVIDENCE:** #13: caption "GRADEY DICK, TWO UNPROTECTED" (9.34-9.89 s) plays over the Kawhi photoshoot clip V10_kawhi_raptors_pose (shot 6, 9.25-10.58 s); the clip named V06_gradey_dick starts at 10.58 s under "FIRSTS, A PICK SWAP" - the clips are one slot late (shots.json vs storyboard). #17: caption "TIMBERWOLVES COACH CHRIS FINCH" and "LOVES IT" are over flop clips of unnamed players (fine as b-roll but viewers will read them as Finch's team/target); UPLOAD.md says the Avdija clip is "not independently number-verified". #14: "CJ MCCOLLUM, FIRMED UP" shows a Knicks #11 ball handler vs a Hawks #3 (storyboard 14.31 s); I cannot tell from the small frame who "firmed up" and no identity log exists; "Paul George" clip is a Sixers #PLA frame. Lessons log says "preview frames are too small to prove a face: say 'verify'", but there is no mechanism that forces it.
- **WHY IT MATTERS:** Basketball viewers comment on wrong-player shots first, and comments of "that's not X" kill trust.
- **WHAT WOULD PROVE ME WRONG:** A frame-by-frame check by a human finds #13 shots 6/7 are correct and #14's McCollum shot is verified.
- **PROPOSED FIX:** Add `who` and `src_post` to every named shot in shots.json; a script asserts each spoken name has a shot with that `who` within +-0.5 s; spot check the 5 named shots by a high-res frame.
- **CONFIDENCE:** high on #13 off-by-one (shots.json order is explicit); low-medium on #14 McCollum (small frame).
- **COUNTER-ARGUMENT:** The clips come from official NBA/team videos whose own captions identify them; errors, if any, are one-frame slips.

### 8. #15 and #16 have weak stories: no turn, no payoff, announcement as story
- **CLAIM:** Both are "something will happen in six weeks" announcements; the closing question has no answer and no argument.
- **EVIDENCE:** #16 words: "Giannis is about to face the Bucks ... Thirteen years in Milwaukee. After the trade, he watched a video from Bucks fans, and said this... Now he plays them on a neon court... So how many points does Giannis put on his old team?" - the event is Nov 18; the only quote is generic sentiment ("Don't cry because it's over, laugh, smile because it happened"); the question is not an argument. #15: the claim is Adams' *joke* ("joked" is in the script and the card), but the hook line says "one NBA center **warned** about exactly this", and the folder title is "Steven Adams Says GTA 6 Will Ruin November". qa_short warns "no turn word (But/However/Until/Now) in the first 40%" for #14, #16, #17, #18 (I re-ran it); #15's only turn is at "But only for November". Voice is slowest on these two: 221 wpm (#16), 227 (#15) vs the doc's 240-290.
- **WHY IT MATTERS:** A news hook with no reversal and no "what will happen" payoff gives no reason to stay beyond 8 s, and there is nothing to argue about in the comments.
- **WHAT WOULD PROVE ME WRONG:** #16 retention curve flat above 60% to the end and comments full of point predictions.
- **PROPOSED FIX:** Give every script a one-line "turn" in notes ("Giannis said X; what happens if he scores 40?"); end on an assertion people argue with ("Giannis scores 40 on them and no Bucks fan can be mad. Right?") or drop the Short until the game happens.
- **CONFIDENCE:** medium.
- **COUNTER-ARGUMENT:** "Event upcoming" Shorts get search traffic as Nov 18 approaches; a sentimental quote is emotional.

### 9. Footage dependence and rights risk: ~100% third-party official clips, one voice, one caption style
- **CLAIM:** The channel is, by construction, "other people's video + AI narration": every Short is built from X posts by the NBA/teams/ESPN or the NBA's own press video.
- **EVIDENCE:** SKILL.md section 4 (X posts first, archive.org second); #17's UPLOAD: "Footage: the NBA Official account's 2026-27 Areas of Focus ... videos" (full runtime); #14 same; #11 old Finals footage of 1998 (NBA-owned); #13 Ballmer clip is an old Microsoft clip used "as a joke beat". UPLOAD template sets "Altered/synthetic content: No (AI narrator, real footage)". Round 6 notes the copyright-claim rule for >60 s is "unresolved". The skill's mitigation is "original value (research, an opinion line, verified numbers)" - but #14-#18 have no notes.md with the required `Lane:`/`Concept:`/`Added value:` (only #11 and #12 have notes.md; I listed the folders).
- **WHY IT MATTERS:** A Content ID claim or reused-content demonetisation hits the whole channel; the NBA is a litigious rights holder; the YouTube monetisation requirement (10M views, YPP) in the Roadmap depends on it.
- **WHAT WOULD PROVE ME WRONG:** A written YouTube/NBA position that team/league-posted promo footage is licensed for reuse, or no claims after 30 days.
- **PROPOSED FIX:** Make notes.md mandatory in the gate (Lane/Concept/Added value present); track "% runtime from one rights-holder video" (e.g. #17 ~100% NBA video); add at least one non-official visual per Short (our own graphic, a diagram, a stat card).
- **CONFIDENCE:** medium (policy outcomes are probabilistic); the notes.md omission is fact.
- **COUNTER-ARGUMENT:** The whole competitor set (Clank, Ahmed's, REBOUND) does the same; promo footage is posted to be shared.

### 10. Overclaims and logic flaws relative to the sources
- **CLAIM:** Several lines state more than the source supports.
- **EVIDENCE:** (a) #13: "The Clippers gave up ten first-round picks for Kawhi Leonard" - UPLOAD cites ESPN: "a total of 10 first-rounders **to acquire and retain** Leonard"; historically the 2019 trade picks went to OKC for Paul George, not Kawhi (Kawhi signed as a free agent); the cover "10 PICKS FOR KAWHI?" and the hook repeat the compression. (b) #12 v2: "there's one number in this story nobody's talking about" (the $9.6M qualifying offer) - the same notes.md cite Shams reporting it; and the closing "lose eighty-seven million, or just win a hundred ninety?" compares a five-year $200M deal with a **one-year** $9.6M QO (200 - 9.6 = 190.4), an apples-to-oranges counterfactual; notes.md also say "No report of him taking the $9.6M QO". (c) #18: "Then he signed for eight million dollars, and made one promise" - UPLOAD says the deal was reported Sep 28, same day as media day, and the quote is a statement, not a promise; Maxey's line is a joke, not news. (d) #15: "warned" vs "joked" (see #8). (e) #11: "ESPN says no" (Jordan's shove) - notes.md: "Barrett's defender is identified as Mobley via ESPN's description (no number visible)"; the "ESPN says no" verdict on Jordan is a reading of the 'force/full-extension' test applied to a 1998 play, a contestable opinion stated as the outlet's finding.
- **WHY IT MATTERS:** NBA comment sections punish factual slips; the Lessons log's "Trusting one source on contracts" mistake is the same family.
- **WHAT WOULD PROVE ME WRONG:** The ESPN article text states those exact equivalences; a source says Clippers' ten picks were for Kawhi.
- **PROPOSED FIX:** Add a "claim -> exact source quote" table to notes.md for each number/attribution; reword #13 to "ten first-round picks to land Paul George and keep Kawhi"; remove "nobody's talking about".
- **CONFIDENCE:** medium-high on (a),(b); medium on (c),(e) (I only have UPLOAD.md summaries).
- **COUNTER-ARGUMENT:** Scripts are short and "reportedly" is used; shorthand is normal in Shorts.

### 11. Audio design is unmeasured and has contradictory history
- **CLAIM:** The sound design is a constant boom + clicks recipe applied from the skill, not evidence.
- **EVIDENCE:** sfx.json: `boom` at 0.0 gain -12 in #15, #16, #17, #18 (identical "hook" tag); #14 has none; commit f7956ce "LeBron v6: boom removed" and Lessons "vine boom ruins it" vs SKILL.md "A sound on the hook word: one boom". I measured loudness per segment in #15: narration windows -14.0/-14.3 LUFS, Adams' real quotes -16.6 and -17.3 LUFS: the **real voice is 2-3 dB quieter than our TTS** (the voice is lifted before mixing; the quotes are not). The "click" SFX fire on card appearance (#14 6.45 s; #15 3.3/4.2/12.39 s). TTS pace 221-259 wpm continuous with no pauses; no measurement of pitch/energy variation anywhere in the repo. Whole-Short LUFS I measured: -14.3 to -14.7 (fine).
- **WHY IT MATTERS:** Real quotes are the emotional peak of #15/#16/#18; if they are quieter than the narrator the Short sounds like the TTS is the star. A sound at 0.0 s on every Short becomes a signature or a nuisance; we cannot know which.
- **WHAT WOULD PROVE ME WRONG:** 24 h viewed% higher with boom than without on a same-script pair; listeners rate quote vs narrator as balanced.
- **PROPOSED FIX:** Lift quote segments to the narration LUFS (target -14 +-1 per segment) and add a per-segment loudness line to qa; run boom vs no-boom as a pair on #16/#17.
- **CONFIDENCE:** high on the loudness gap; low on boom impact.
- **COUNTER-ARGUMENT:** A 3 dB quieter quote can read as natural dynamics; one sample.

### 12. Evidence base: survivorship, topic-vs-style confounds, tiny n elevated to "PROVEN"
- **CLAIM:** The "PROVEN" labels mean "a pattern is present in public data", not that it causes views; the sample is survivors.
- **EVIDENCE:** Round 5/6 tables: "name-first titles 237K vs 494K (n=20)" (one channel), "21+ s 848K vs 291K" (n=52 vs 82; shorter Clank Shorts are likely clips vs stories, a content confound), "turn in first 10-40%" (n=8 Shorts), "speech pace 240-290 wpm" (n=8), "💀 median 7.7M vs 0.4M (n=9, driven by a few hits)", "Round 4: emoji 🤔 worst" (n=5, flagged "too small to act on" in Round 5 but kept in SKILL.md/qa title advice). Competitor set = channels that survived (Clank 145K, REBOUND 3.4M, Courtside 804K); no failed channels sampled; Round 6 admits "Almost every popular 'viral formula' is vendor opinion" and "no competitor has tested styles". Round 6's statement that comments do not drive reach rests on Clank's correlation (0.06 vs 0.16 comments/1000) which is also confounded by view count.
- **WHY IT MATTERS:** The skill still lists these as "[PROVEN]" in section "Evidence-backed rules" and tells every agent to follow them; wrong rules scale across all Shorts.
- **WHAT WOULD PROVE ME WRONG:** A pooled regression on >=500 NBA Shorts with channel fixed effects showing the same effects.
- **PROPOSED FIX:** Relabel "PROVEN" as "OBSERVED (n=..., one channel)" in SKILL.md; keep only rules with a mechanism (no filler first word, loudness, no dead air) as hard gates.
- **CONFIDENCE:** high.
- **COUNTER-ARGUMENT:** The notes already label tiers honestly, and n is what a free toolchain can produce.

### 13. Captions: house style tested on nobody, positioned on faces
- **CLAIM:** ALL-CAPS red/green captions (user's house style) read slower (Round 6 cites lab studies at 12-20% slower) and, in dual-face frames, sit on the face/chest; the competitor winners use sentence case.
- **EVIDENCE:** Round 5/6; storyboards: #15 captions over Adams' mouth-level/chin zone ("LOOK AT ALL", "MATE."), #18 over LeBron's torso, #17 across Daigneault's chest; #16 captions overlay Giannis' chin at ~11-17 s. Hook text "FLOP = TECHNICAL" in #17 is static for 2.5 s over moving action; hook text in #14 is absent (no `--hook-text`), so #14's hook relies on audio alone.
- **WHY IT MATTERS:** On silent autoplay the caption is the hook; legibility and face-blocking affect first-3-s retention.
- **WHAT WOULD PROVE ME WRONG:** A caption A/B (same Short, karaoke vs metasports) showing no difference.
- **PROPOSED FIX:** Run `--caption-style karaoke` vs `metasports` on the same Short (already listed as open test; make it the first test); move captions ~8% lower in face-dominant shots.
- **CONFIDENCE:** low-medium.
- **COUNTER-ARGUMENT:** The user likes the look; ALL CAPS is also used by REBOUND and Hoop Facts.

### 14. The loop gate and "last word before the end" create cut-off endings
- **CLAIM:** The "loop" is visual-only and the voice is cut by the video end; the loop gate is checkable not meaningful.
- **EVIDENCE:** warns I reproduced: #18 last word ends 0.13 s before the end, #17 0.09 s, #14 **-0.01 s** (the last word ends after the video, voice clipped), #16 0.14 s. Every Short ends with a spoken question and a hard cut to the first frame; the first frame is a different image with no sentence continuity, so the "loop" works only if the viewer does not notice. Round 6 says engaged views exclude loops; replay counts matter for public view count only.
- **WHY IT MATTERS:** Clipped last words ("... or just flying through?") feel like a bug; the only evidence for loops is vendor anecdote.
- **WHAT WOULD PROVE ME WRONG:** Studio shows >100% average % viewed on looped Shorts versus non-looped.
- **PROPOSED FIX:** Make `tail >= 0.25 s` a hard check (not warn) and write the last line to echo the first sentence in words, not just image.
- **CONFIDENCE:** medium-high on the cut-off; low on loop value.
- **COUNTER-ARGUMENT:** 0.1 s is inaudible in the mix; a hard loop cut is standard.

### 15. Posting plan risk: 2/day from a 469-sub channel, 7 months dormant, with no read of the first batch
- **CLAIM:** The plan multiplies exposure of a recipe nobody has measured.
- **EVIDENCE:** Roadmap: 469 subs, last upload 7 months ago, "2 a day clears" the fan-funding bar (33K views/day); Lessons: Duren and Wembanyama posted Oct 4, results "due within 36 hours" and "do not spend time on them". Round 6: ">=3 a day unsupported", "frequency: fewer, better". The #12 folder is stale and confusing: root script.txt/shots.json/words.json are v1, the posted "(v2)" mp4 is `_v2/final.mp4` built from `_v2/script.txt`; `script_v2.txt` at root contains the lines (nine points vs Orlando, "ninety minutes before the deadline", monthly weigh-ins) that UPLOAD.md says were removed as unverified; running qa_short on the root files FAILs #12 (34% cards, a 4.2 s shot). A reviewer cannot tell which version is live.
- **WHY IT MATTERS:** If the batch underperforms, we will have burned the re-test window with 8-16 same-recipe Shorts before learning anything.
- **WHAT WOULD PROVE ME WRONG:** #12 and Wembanyama beat the 30K median by 2x within 36 h.
- **PROPOSED FIX:** Hold #14-#18 to 1/day; post two different-format Shorts first (one fast cut, one 2.2 s cut; one news, one "why"); decide the next 10 after reading Viewed-vs-swiped on the first 4.
- **CONFIDENCE:** medium.
- **COUNTER-ARGUMENT:** Fresh channels need volume to get tested; news decays, so waiting costs relevance.

---

## (b) Things that look fine but I distrust

1. **"Passes qa_short.py" in every UPLOAD.md.** It passes `--infer-kinds`, a flag that marks everything not named c* as `action`. Photoshoots (Kawhi #2 pose in #13), posters, hype-video clips and a drone shot of a pink tower (H1_tower, 4 uses across #15/#16) all count as "b-roll that shows the story". `kind` is self-declared in shots.json.
2. **"6+ distinct source clips".** Counts cuts of the same official video as distinct clips: #14 is ~13 cuts of one NBA video (B1-B13 + two cards); #17 is ~all the NBA's single flopping video.
3. **The 21 s floor.** All four Oct-4 Shorts land at 22.9-23.8 s: built to the threshold, with the n=52 vs 82 comparison confounded by clip vs story type. Not evidence that 23 s beats 18 s.
4. **-14 LUFS.** Harmless, but Round 6 admits YouTube normalises on playback and the -14 target is vendor-repeated; the real problem is the quote/voice mismatch (see #11).
5. **Titles with a "Why/How/Did" first word (1.64x, n=28).** The recommended titles for #14-#18 start with "The NBA...", "Will The NBA...", "Giannis...", "LeBron...", "The Heat..." and trigger the name-first warn. The skill's own rule is violated by its own picks, with no cost since the warn is non-blocking.
6. **Covers.** Three covers per Short were produced even though Round 6 says the Shorts feed shows none; time is cheap but is also the only A/B surface we are not using.
7. **"Real audio quotes <=4 s".** #16's Q2 runs 5.17 s of a static talking head (12.75-17.92 s) and #15's quotes total 6.38 s; gate allows 4.5 s.
8. **Hub/Artifact upload steps.** Process overhead (720p preview, 1080p upload, ArtifactData doc) per Short competes with research time and has no retention value.
9. **Voice "ElevenLabs same voice always".** Brand consistency vs. monotony is untested; same voice + same boom + same closer = recognisable template to both viewer and classifier.

---

## (c) Steelman the opposite: the three biggest process choices

**1. Choice: fast cuts (avg 1.2-1.5 s), 3+ cuts in the first 3 s.**
Opposite: *slow, legible, 2.5-3.5 s shots with fewer cuts.* Best case: Clank's biggest Shorts cut every 2-4.7 s (Round 3), and a story Short is a *comprehension* task: viewers must map name -> face -> action. Our 0.4-0.8 s shots make identity impossible to register, so a swipe at 3 s may be confusion not boredom. A held, readable shot at 0.0 with a big caption plus one punch-in is closer to what the best stories do. Fast cuts help only in montage Shorts.

**2. Choice: build every Short from official third-party X clips and AI narration (news lane).**
Opposite: *original visuals and an original angle: our own graphics, one data visual per Short, evergreen "why/how" oddities.* Best case: the channel's own 80-Short history shows its hits were evergreen curiosity ("Why Does No One Like Bronny", "Why NBA Players Stopped Shooting Underhand"); evergreen Shorts get search/suggested traffic for months while news Shorts decay in 48 h; a licensing/inauthentic-content strike on news clips would be fatal; original angle is the only YouTube-endorsed defense.

**3. Choice: high cadence (2/day) with a fixed recipe and gate.**
Opposite: *1 Short/day or less, one experiment per Short, full read of the retention curve before the next.* Best case: Round 6 quotes YouTube "fewer, better"; our own notes call the recipe a hypothesis list; each Short is a 1-sample experiment, and running eight identical-format Shorts before reading the first curve wastes the 14-day re-test window the Roadmap warns about. Learning rate, not volume, is the scarce resource.

---

## (d) Prioritised experiments that would settle disagreements

1. **Read-out first (zero cost):** Collect 24 h and 7 d Viewed-vs-swiped and average % viewed for #12, Wembanyama and the next 4 posted Shorts; log gate metrics next to them. Without this nothing below can be judged. Decision rule: if viewed% < 60% on >= 3 of 4, rewrite hooks before making any more Shorts.
2. **Hook type A/B (same story, 2 versions, posted 24 h apart, or Studio Test & Compare if available):** statement hook vs question/stakes hook ("Four NBA stars were just called for the same illegal move. Which one is still legal?"). Settles criticism #1.
3. **Cut-rate A/B:** re-cut #17 at ~2.2 s avg vs the current 1.32 s. Settles #6 and the "fast = better" belief.
4. **Footage fidelity A/B:** #18 as built vs a version using only Sixers-uniform LeBron clips and a Maxey/car-trouble setup line. Settles #2.
5. **Story-family cap test:** post #16 alone one week, #15+#16 together another week; compare second-Short views vs first. Settles #3.
6. **Lane A/B with equal effort:** one rule-news Short vs one evergreen "Why" Short (the channel's historic hit type) in the same week; 7-day median views. Settles #4.
7. **Boom vs no-boom and quote-lift (+3 dB) on a same-script pair.** Settles #11.
8. **Caption A/B:** karaoke/sentence-case vs ALL-CAPS on the same Short. Settles #13.
9. **Gate validity check:** after >= 20 posted Shorts, correlate gate metrics (avg shot, action %, talking-head %) with 24 h viewed%. If |r| < 0.2, stop describing PASS as quality. Settles #5.
10. **Factual audit:** have a person (or a second agent) re-verify the 5 named-shot identities and 6 numbers per Short against sources before posting; count slips per Short. Settles #7 and #10.
