# Rule history: the Playbook's THE RULES section before the Nov 7, 2026 rewrite

Archived word for word on Nov 7, 2026, when the owner approved the Theory Ranking (`Research Notes/Theory Ranking and Rules Challenge (Nov 7, 2026).md`). The new rules are at the top of `MetaSports - Playbook.md`. Read this only for history.

## THE RULES (Oct 26 overnight review). Read this first. It wins over everything below.
The owner asked for a full review: "everything is up for debate". These rules replace the old ones.
- Each changed rule says **(Oct 26 overnight review)**, its evidence tier and its source.
- **Tiers:** [V] measured · [S] small sample, or seen on other channels · [H] a guess to test.
- **Sources** (in `Research Notes/`, all dated Oct 26, 2026): *Retention Upgrade* = `Retention and Editing Upgrade`; *Posting Study*; *Similar Channels*; *Why NBA Views Dropped*; *Rules Review*.
- Every change, old rule to new: `Research Notes/Rule Changes Applied (Oct 26, 2026).md`.

### 0. Full Review (Nov 1, 2026): what the review changed, and what it did not
Source: `Research Notes/Full Review for Retention (Nov 2026).md` (tiers as above; n is small everywhere, read the tier).
- **Premise and the first 1-3 s decide the Short, not the edit.** 15 of 16 of our Shorts with API curves have their steepest drop in the first 4 s, mostly not at a cut [V]. Inside six competitor channels the better and worse halves edit alike [S, n=128].
- **NBA moment: voice 22 s or less** (QA warns past 24 s): median 10.0K vs 3.1K public views, n=8 vs 16 [V small]. Line 1 of 11 words or fewer: 8.0K vs 3.4K, n=18 vs 6 [V small].
- **FC:** goalkeeper + odd device in a famous shootout is the only proven premise (4 of 4 at 15-30K; 0 of 8 others above 3.2K) [V n=12]. Voice 226-233 wpm is right (Ahmed's Goal 230) [S]. Open title-first stays the default; the next two goalkeeper Shorts test an action-first opener [H].
- **Stop:** decorative SFX (one only for a visible event), punch-in zooms, freeze frames, arrows, emoji, colouring function words. [S] CoachClank's three biggest Shorts: plain white small captions, no SFX; competitors' median SFX per 10 s is 0.
- **Picture:** footage big and moving from frame 1, no black fill, `edit_lint` flags fixed (it runs inside `qa_short`).
- **Tools (opt-in, default unchanged):** `assemble.py --caption-style clank`, `--color-rule word|none`, `broll.py --fill-brightness`. A/B plan: 2 Shorts per channel each, decide after 8 [H].
- **Hygiene:** time-free wording in line 1; one number on screen at a time; claim words (still/record/first/never/only/most) each get a dated source row.

### Owner rules (unchanged; never relax them)
- Never post, schedule or upload anything. Every output is a DRAFT. The owner posts.
- No cards. If one is truly unavoidable: 1.5 s at most, never in the first 4 s.
- No promo, teaser or subscribe outro. The video stops on the payoff.
- No dead air: run `Tools/tighten_voice.py` on every voice.
- Never put API keys in docs, chat or git.
- TikTok/Instagram RESUMED (owner, Nov 3: "start crossposting process"): post the SAME YouTube file; captions come from `python Tools/crosspost.py` (Research Notes/Crosspost Queue.md); still no separate long cut.

### 1. NBA lanes (Oct 26 overnight review)
- **Moments: about half of all NBA Shorts.** A funny, odd or skilful thing you can watch: in a game, on the bench, in warm-ups, a fan, a kid, a mascot, the broadcast desk. Narrate who, what, and the reaction or payoff. [S] Similar Channels §1 and §4; Swishyyy's moments get about 1.8x its explainers (Retention Upgrade §1c). Ours is untested.
- **Each moment needs one fact the clip can't show** (who, why, a number). YouTube cuts reach for narration that only describes the screen. [V official] `Shorts Mechanics and Policy (Oct 24, 2026).md` finding 3.
- **The other half rotates:**
  - **Star paradox.** THE #42 FORMAT (`Library/THE 42 FORMAT.md`) is now one lane here, not the lead. Its test ended 1 of 3 at 74%+ (#48 83.3%, #64 72.6%, #52 59.1%). [V] Rules Review §2 item 1.
  - **Same-day news, or not at all.** It goes up the morning after the game. A news Short that misses its day is skipped. [S] #63, a day late, held 57.6% (n=1); Posting Study answer 1.
  - **Weekly countdown test:** "3 times [star] did X", once a week. A visible #3 / #2 / #1 badge in a corner (`Tools/overlay.py`, e.g. `{"text": "#3", "size": 120, "x": "left", "y": 230, "box": "0xFDB927", "color": "black"}`). The best one goes last. [H] Similar Channels §2 and §4: countdown and elimination formats grew fastest; that the device is the cause is a guess.
- **Review the split after 10 moment posts:** their stayed % and 72 h views vs the channel median. Until then, about half are moments.
- **Still true:** a household-name star or an iconic object, and one idea a casual fan gets in second 1. No paperwork rules (bets, votes, stat credit). No future "can he…?" questions. Never retell a bigger channel's story (`copy_check.py`). Footage from the league, teams and broadcasters; never another creator's edit as the base.

### 2. Editing, every NBA Short (Oct 26 overnight review)
Rules marked "(FC too)" also apply to soccer. The full soccer rules are in `Soccer Channel/Playbook.md`.
1. **Footage first.** Before writing, secure frame 1 and one clip that proves each beat, from any number of sources. Never cut away to filler to reach a clip count. (FC too.) [S] Why NBA Views Dropped §3: the old 6-clip gate pushed filler. This replaces "find 6+ clips".
2. **Frame 1 shows the thing line 1 is about, happening.** Sharp and lit. A face or an action both work if it proves line 1. (FC too.) [S] Retention Upgrade §2b: 12 of 15 Shorts at 1M+ stay on one event. Face vs action showed no gap [V].
3. **Line 1 is 11 words or fewer:** one claim, done by about 3 s. Never a bare number first. (FC too: the spoken title.) [V] Retention Upgrade §1b: 72.6% vs 62.2% stayed (n=25 vs 12). **Re-tested Nov 3 on a second measure ([S], n=21 NBA Shorts with API engaged ratio, views 1K+): line 1 of 12+ words engaged 0.490 (n=6), under 12 words 0.557 (n=15); the four low openings (#76, Luka, Chuck, SGA) run 9-14 words and state the whole outcome in line 1, #75 (0.615) states a tension with no result. `script_lint.py` now flags 12+ words. Whether 'withhold the result in line 1' matters is untested (n too small to split); try it as ONE experiment, not a rule.**
4. **Hold the opening moment.** Shot 1 runs at least 2.0 s. At most 2 shots in the first 3 s. At most 3 shots in the first 5 s. No cut inside line 1. (FC too: shot 1 at least 2.0 s under the title card.) [V] Retention Upgrade §1b: 3 or fewer shots in 5 s held 78.4% vs 66.5% (p=0.002). Shot 1 of 2 s or more: 77.6% vs 68.4% [S].
5. **About 10-15 shots of about 2 s.** Let a play run 3-5 s. [V] Why NBA Views Dropped §2: 15 or fewer shots held 75.0% vs 66.4%.
6. **Replay the key second once, before the payoff.** Show it closer (`"zoom"`) and/or at half speed (`"speed": 0.5`). Mark it `"replay": true` in the cuts plan; `cut_list.py` passes it into shots.json, and QA then allows the repeat. (FC too, when the footage has it.) [S] Retention Upgrade §4 change 2: #42 showed its play twice; the winners show one event twice. Untested for us.
7. **Fill the frame.** Crop wide plays to about 3:4 or tighter: `broll.py cut --blurfit --blurfit-aspect 0.75 --x <pos>` (cuts plan: `"blurfit": true, "blurfit_aspect": 0.75`). Never put a play in a full-width 16:9 strip over blur. Keep full-width blur-fit only for a graphic or text that must be read whole. (FC too.) [S] Retention Upgrade §2b: 0 of 55 winners used a full-width strip.
8. **Proof goes on the footage, never on a card:** words over the play (`Tools/overlay.py`), a circle on the broadcast's own scorebug (`broll.py circle`). (FC too.) [V] Why NBA Views Dropped §2: any card 66.1% vs none 72.6%. Owner, Oct 26.
9. **No emoji stickers** on faces or footage. (FC too.) [S] Retention Upgrade §2b: 0 of 165 winner frames; seen on Hoopiverse's flops.
10. **No forced loop.** End on the payoff. Loop into frame 1 only when that image is the payoff; never add a shot to loop. (FC too.) [S] Retention Upgrade §1b: no gain within either build period. Loops don't count as engaged views [V YouTube].
11. **Real audio on viral moments (owner, Oct 28: "for all clips that are viral, experiment with using the actual audio for the moment").** (FC too.) [H] new test, n=0.
    - **The live call:** cut our narration words over the key second and let the broadcast play it: the call and the roar, about 2-4 s, captioned (words marked `"live": true`). Then narration resumes. #75 rookie: "To him, Jayson Tatum for the win! Yes, sir!".
    - **Real quotes:** when a shot shows someone saying a line, play their own voice, not our narrator reading it. Cut the quote shot from the same second as the words so the lips match (`at` = the first word's source time minus `lead`). #76 Pierce.
    - **Crowd bed:** each clip's own sound runs quietly under the narration (`--bed-db -15` NBA; -26 when the clip is mostly commentary, e.g. soccer; mute a talking head's bed with `--clip-db P11=-40`).
    - **How:** render with `assemble.py --no-music` (or with music for a music-side soccer Short), then `python Tools/nat_sound.py --folder <F>/_realaudio --video <render> --out final_live.mp4 --burst A-B`. Worked folders: `_realaudio` in #75, #76 and S17. QA allows up to 1.5 s of roar after a live word.
    - **Risk:** broadcast audio raises the chance of a Content ID claim. Keep the narrated version on the Hub as the fallback; if a real-audio post is blocked, post the spare.
    - **Measure:** log "real audio" in the Outcome Log and compare stayed % with narrated moment Shorts after 5 posts each.

**Removed (Oct 26 overnight review). Don't use them anywhere:** "3+ cuts in the first 3 s", "a new image every second", "average shot 1.4-1.9 s", "no shot over 3 s", "evidence cards for any fact line", "6+ source clips", "at most 35% from one clip".

### 3. Posting and the package (Oct 26 overnight review; the daily plan is `UPLOAD SCHEDULE.md`)
- **Up to 2 Shorts per channel per day (owner asked, Oct 26: 'is 1 short per day optimal?').** Post the 2nd only if it's as strong as the 1st, at least 6 h later; never 3. On our 2-post days, each post did as well as on 1-post days (4.1K vs 4.2K median), and the 2nd post did no worse. [S] Posting Study §1d. Limits: quality, and voice credits (about 2 Shorts a day total on the current ElevenLabs plan).
- **Times (owner, Oct 28):** first posts at 7-9 AM ET: NBA 7-8 AM, FC 8-9 AM. A 2nd post, when as strong, about 3 PM (NBA) / 4 PM (FC). Post time matters little; a steady slot matters more, and an early slot suits morning-after news. Keep the two channels at least 1 hour apart. [S] Posting Study answers 1 and 3 (the 1 h gap is [H]).
- **News** goes up the morning after the game. [V YouTube] Posting Study §3.
- **Judge a Short at 72 hours:** stayed % first, then views. Never at the next morning's check. [V] Posting Study §1g (#48: 25 views on day 0, then 14.6K on day 2).
- **Never re-upload** a Short to "try again". Make a new cut. [V] YouTube's spam warning, Posting Study §3.
- **Title:** a short statement pointing at the moment ("He Pretended To Be Klay Thompson"). Title wording is a small factor: no title scoring and no title gates. [V] Similar Channels §1 (25,000 Shorts: questions 1.01x, "This/The" 1.06x).
- **Title hashtags:** none, or one (#nba, or #football on FC). [S] Posting Study answer 6.
- **Description:** leave it empty. [V] Posting Study §1f (empty 1.00x vs filled 1.00x).
- **Tags:** fill the box to 490 characters (owner, Nov 1: "go back to filling"), most relevant first: the names, the team or club, the event, common misspellings, then wider topic tags. Check with `python Tools/tags_fit.py "tag1, tag2, ..."` (it counts the way YouTube does and stops at 490).
- **Pinned comment:** the two-sided argument (unchanged).

### 4. Script critic and QA (Oct 26 overnight review)
- **Script Critic v3 (`Tools/script_critic.md`) is advice, not a gate.** Its craft score and any title scoring don't predict views. Only its factual-accuracy checks block a script. [S] Rules Review §2 item 14: its two REJECTs (#40, #41) later beat the channel median.
- **Hard gates stay:** every fact has a dated source and its exact words in `notes.md`; `qa_short.py` must PASS; Critic v2 reviews the export on hand builds.
- **Target:** 74%+ stayed to watch, read at 72 h. [V] Why NBA Views Dropped §1: every 10K+ Short held 74%+.

### 5. Research tools (Oct 26 overnight review)
- **`Tools/yt_watch.py`:** Gemini watches a Short (a competitor's link or our own draft) and writes a scene-by-scene report to `Research Notes/Watch Reports/`. It needs a free `GEMINI_API_KEY` in the cloud environment's settings (never in chat or docs). Treat its numbers as [S].
- **`Research Notes/Competitor Watchlist.csv`:** the channels the daily research task checks. Add a channel when a study finds one worth watching.

### THE #42 FORMAT (now one lane: the star paradox)
Full spec: `Library/THE 42 FORMAT.md`.
- **Skeleton:** accusation → the count → "And he's [great]." → the old record → a human tie-in → "So is he [bad]? No." → two proof numbers → the flip number.
- About 75 words, 22-25 s. Frame 1 = the bad thing happening. About 12 shots of about 2 s. Words over footage, no cards.
- **Checks:** `script_lint.py` says whether a script FITS THE #42 FORMAT. A script in another lane doesn't need to fit.
- Rewrite the fixed lines every time. Retire the lane after 3 posts in a row below the channel median.
- #47 Kawhi and #50 Embiid are parked.


**NBA music-bed test (owner said yes, Oct 26):** NBA posts alternate music and no music, starting with #69 Luka (none) and #70 Barkley (music). Render both versions of every NBA Short, and mark on the Hub which one to post so the alternation holds. The bed is about 20 dB under the voice (`music.json`, bed_lu -20), from `Library/Music/` (ElevenLabs beds: no Content ID, no pay cut). Log music yes/no on every post in `Research Notes/Outcome Log.md`. Decide after 8 posts (4 each) on stayed %, judged at 72 h. Soccer keeps its own music A/B.

