# Daily Log (newest first)

One entry per channel per day, written by the daily runs (`.claude/skills/daily-run/SKILL.md`): data pulled, what was learned,
research with sources, what was made, what changed in the rules or tools.

## Tue Nov 3, 2026, 14:40 UTC (owner: "save the pacers, and find the key. do more research aswell ... see if you are fully able to takeover these channels")

**Key.** Not recoverable from here: no `ELEVENLABS_API_KEY` in the environment, no key file (the Nov 2 reset wiped the scratchpad), none in the repo or this session's history, no proxy-held credential (api.elevenlabs.io answers 401 without one), and no computer folder shared through Remote Control. Stand-ins failed: Everygen's subscription is inactive (402), vidIQ has 0 credits until Nov 5. The owner has to re-add it in the environment settings.
**Pacers.** #93 started: script (96 words), claims table, 6 sources downloaded and contact sheets checked; gaps logged (no bench/street-clothes shot, no 106-104 scoreboard). A check-in at 17:30 UTC voices and finishes it if the key is back by then; otherwise it dies tonight.
**Research.** Afternoon add-on in `Research Notes/Daily Research/2026-11-03.md`: three evergreen NBA picks (Rodman's banned No. 69 and house in Dallas, FRESH; Bubba Wells fouling out on purpose, known; the 0.3-second rule, partly taken).
**Automation.** Assessment written: `Research Notes/Automation Options (Nov 3, 2026).md` (about 95% automatable after a 30-minute setup; recommend one-tap approval now, autopilot with a veto window after two clean weeks).

## Tue Nov 3, 2026 (FC daily run; main session; build skipped: queue full, no voice key)

**Context.** Inbox empty. This account's FC Hub has no card at "ready"; the owner's PC has FC scheduled daily through Fri Nov 6 (S25 today, S26-S28), so the queue is full. The voice key is also missing since the Nov 2 container reset (owner task `setup-keys` added this morning).
**Scripted (no voice, no render):**
- **S32 "The Hull City fan who walked home from Chile"** (fan lane, this week's news): Karl Bushby's 28-year walk from the tip of South America to Hull (ESPN, Wikipedia citing Sky). Payoff: the month he set off, Hull were bottom of the Football League's lowest division, heading for bankruptcy; he came home to a Premier League club. 196 words. Copy check: news clips only, nobody with the Hull angle. The 1998 table line needs a stronger second source before voicing.
- **S30 "The Ballon d'Or winner who missed a penalty days later"** (penalty takers): Kane's Oct 31 night (trophy shown, penalty off the bar, lost the ball for the equaliser, late Silva draw, even Karl's last kick off the bar). Payoff: only his second miss in 27 Bundesliga penalties. 186 words. Sky and theScore read today; re-read Bundesliga.com before voicing.
- Not scripted: Higuita's scorpion kick (S21) is heavily TAKEN (England's own upload 7.5M, 3.7M, a Netflix doc); S33 Carrick v Roma waits for tonight's result.
- Folders: `Soccer Channel/Productions/2026-11-09 S32 ...` and `2026-11-10 S30 ...` (script.txt, title_caption.txt, notes.md with every claim, quote and link).

## Tue Nov 3, 2026 (NBA daily run; main session; build skipped: no voice key)

**Context.** Inbox empty. NBA is scheduled by the owner's PC through Thu Nov 5 (today: "Draymond Green Had A Triple-Double With Four Points" 7:15 AM, "Jokic Said No To His Own Parade" 3:30 PM). The cloud container was reset on Nov 2: `ELEVENLABS_API_KEY`, the session key file and `Tools/.env` (Gemini) are all gone.
**Not built.** Today's research pick 1 (the Pacers played with six players and nearly beat the Hawks; FRESH, sources in `Research Notes/Daily Research/2026-11-03.md`) is news that dies tonight, both slots are taken, and without the voice key no Short can be recorded. No script written: a news script that can't be voiced today has no use tomorrow.
**Owner task added:** "Add the voice and Gemini keys to the environment" (`setup-keys`, section Now, steps and copy blocks for the two variable names; never paste keys in chat).
**Next open NBA slot:** Fri Nov 6, 7:15 AM. Once the keys are back, the Friday build can use an evergreen pick.

## Mon Nov 2, 2026 (FC daily run; main session, with the voice key)

**Context.** Inbox empty. FC is scheduled daily through Fri Nov 6 by the owner's PC (`Research Notes/Scheduled Uploads.csv`) and S25-S28 are built, so the queue is full: **no build** (trigger rule: 3+ ready, write 2 scripts and stop). This account's FC Hub has no new card; nothing to post from here.
**Scripted (no voice, no render):**
- **S29 "The goalkeeper who says Spain were scared of a shootout"** (goalkeeper lane + this week's news): Martinez's 2022 shootout trick, then his Oct 30 claims that Spain's players said "we can't go to penalties" and that he'd have won; Spain won 1-0 in extra time. Payoff: the shootout king lost the next World Cup final without facing a penalty. 193 words. Every Spain line is his claim ("he says"). Copy check TAKEN only from 2022 compilations; nobody told the 2026 angle.
- **S31 "The baby Messi bathed beat him in a World Cup final"** (fan/kid lane, the Topic Study's next test): the 2007 charity-calendar bath photo, their first meeting in the 2026 final, the hug and Messi's advice; payoff: the baby took the world title off him. 212 words. Copy check **TAKEN** (the photo story itself: AP 427K, BeanymanSports 276K, fan edits 9M); the final is the new part. Owner's call.
- Folders: `Soccer Channel/Productions/2026-11-07 S29 ...` and `2026-11-08 S31 ...` (script.txt, title_caption.txt, notes.md with every claim, exact quote and link). Footage not checked yet: the footage test comes before voicing.
**Cautions logged.** 2007 photo month differs by source (Sept vs Dec), so "a few months old"; "11 saves" (Daily Star only) not used; Goal misprints the final as "2016".

## Mon Nov 2, 2026 (NBA daily run; main session, with the voice key)

**Context.** NBA is scheduled through Thu Nov 5 by the owner's PC (`Research Notes/Scheduled Uploads.csv`; today #73 at 7:15 AM and #83 at 3:30 PM). Inbox: empty. No other session had built today's top research pick.
**Built anyway, as an optional swap:** today's research pick 1 is news that dies tonight, and our best recent NBA Shorts are this type (Boozer 25K, Bronny 27K). #92 "This Rookie Told Luka He Sucks" can replace #83 (an evergreen) at 3:30 PM if the owner moves #83 to Fri Nov 6; otherwise it's skipped. Never three NBA posts in a day.
**Made.** #92: Lendeborg told Luka "he sucks, he can't score on me" in his debut (his own voice, Slater's soundbite), had 6 points and 5 turnovers when Luka scored 37 on Friday, then scored 37 on Sunday without Curry: the most by a Warriors rookie since Curry's 42 in 2010 (AP). 19.1 s, 12 shots, real-audio version to post plus a music spare; full QA PASS on both, comfort audit clean. Hub card `s92-lendeborg-luka` (ready), task `post-lendeborg` (due 3:30 PM ET, marked optional). Sources and footage: the folder's notes.md.
**Learned (craft, [S]).** QA and the comfort audit caught three things worth keeping in mind: the overlay number landed on a teammate (#20) for half a second until the shot was split; ESPN packages hide camera cuts near clip ends (slow the clip or trim before the cut); a real-audio quote needs its captions grouped into phrases, or single words flash for 0.2 s.

## Mon Nov 2, 2026 (FC daily run; routine; no ElevenLabs key; build skipped: queue full)

**Build skipped on purpose.** FC is built and scheduled through Fri Nov 6 (`Research Notes/Scheduled Uploads.csv`: S20 today 12:00, S25 Tue, S26 Wed, S27 Thu, S28 Fri, all from the owner's PC), and `key: MISSING` here anyway. A new script would duplicate work; per the 01:40 UTC catch-up entry, builds skip while the queue is full. No Hub change (nothing new to put on it).
**Data.** Analytics: no token (YT_CLIENT_ID / YT_REFRESH_TOKEN_FC not set); dataset FC rows unchanged (no Studio export since Oct 24). Public counts (yt-dlp, 09:30 UTC): **S17 Krul 20K at ~72 h**, S01 30K, S05 29K, S03 15K, S08 3.2K, S16 3.1K, S07 2.5K, S18 2.2K (~2 days), S19 Rulli 2.0K (~19 h), S06 2.0K, S04 1.9K, S02 1.8K, S15 1.1K.
**Learned.** Lessons Learned, Nov 2: goalkeeper-shootout stories 4 of 4 at 15K+, every other FC Short under 3.3K; S17 shows the subject carries it without a visible trick. The full queue to Fri is goalkeeper-heavy (breaks the 1-in-3 rotation on purpose): judge each at 72 h; two in a row under 5K = bring the rotation back.
**Research.** Today's research run already added the soccer picks (Martínez on the 2026 final, Kane's crossbar after the Ballon d'Or) to the Idea Bank with sources (`Research Notes/Daily Research/2026-11-02.md`); nothing added twice.

## Mon Nov 2, 2026, 01:40 UTC (main session catch-up after a 2.5-day stall)

**What happened.** This session's worker kept restarting from Fri Oct 30, 09:05 UTC to Mon Nov 2, 01:35 UTC, so 10 scheduled runs queued up unrun (FC build Oct 30, Oct 31, Nov 1; NBA build Oct 31, Nov 1; research Oct 31, Nov 1; stats Oct 30, Oct 31, Nov 1). Meanwhile the owner's PC session and the other account built and auto-scheduled both channels (`Research Notes/Scheduled Uploads.csv`): NBA twice a day through Thu Nov 5, FC daily through Fri Nov 6.
**Done.**
- #80 Boozer (built Oct 30, unfinished paperwork): notes.md with every claim's source, UPLOAD.md, DRAFTs committed. The owner posted it (o8UE_lsnZ9E, 25K). The other account's Hub lists it as #81, and #80 was reused for the Warriors Short; the folder and this account's card `s80-boozer-outshot-dad` say so.
- This account's Hubs and task list: #74, #77, #80 (NBA) and S17, S18 (FC) marked posted with public views; their post tasks ticked (all visibly live). Inbox empty.
- Stats check (the Nov 1 run): Outcome Log section above it. NBA last-7 median 8,200 (was 6,150); Bronny 27K, Boozer 25K, underhand 24K.
**Skipped (stale, on purpose).** The older stats runs (superseded by the Nov 1 one), both research runs (their news windows passed; tomorrow's 3:43 AM run covers Monday's games) and all five builds: every NBA and FC slot through Thursday/Friday is already filled and scheduled, so a new build now would duplicate work and spend voice credits for nothing.
**For the owner.** Two sets of daily runs now exist: this session's (research 3:43, NBA 4:41, FC 5:39 AM ET) and the other account's (NBA 3:17, FC 4:23 AM ET). While the queue is full, this session's builds will skip; say if you want them paused.

## Sun Nov 1, 2026 (NBA daily run; routine; no ElevenLabs key)

**Blocked.** `cloud_setup.sh`: `key: MISSING`, so no voice, render or QA; script, sources and cut plan only. Analytics: no token (YT_* missing); `yt_analytics.py` and the dataset hand columns not run. Nothing faked.
**Context.** #74 holds the Sun 7-8 AM NBA slot (Hub sync, Nov 1 00:45 UTC). Tags are back to 490 characters (owner, Nov 1).
**Research (Sat Oct 31 games; AP recaps on ESPN, ESPN box scores and play-by-play).** Candidates:
- **Spurs 121, Timberwolves 111** ([recap](https://www.espn.com/nba/recap?gameId=401909901)): Wembanyama 43 points, 6 blocks, 17-34; "reaching 40 points for the 10th time in the regular season"; blocked Kuminga's three and dunked on the run for point 40 (play-by-play: block 6:20, dunk 6:15, Q4). Also threw the ball off the backboard to himself (AP).
- Cavaliers 136, Bucks 111 ([recap](https://www.espn.com/nba/recap?gameId=401909900)): a 48-point second quarter, 72-46 at half.
- Rockets 119, Thunder 98 ([recap](https://www.espn.com/nba/recap?gameId=401909902)): Smith Jr. 30, Smart 7 of 10 from three; OKC's first game without Holmgren (out 2+ months).
- Blazers 112, Jazz 90 ([recap](https://www.espn.com/nba/recap?gameId=401909896)): a 17-0 first-quarter run. Maxey 38 without LeBron and Embiid (76ers 109-104 Hornets). Grizzlies still unbeaten (136-105 Kings).
**Pick:** Wemby's block-to-40th-point sequence: one clip, one oddity, a household-name star, and the play is in one ESPN clip (50343302, frame-checked). Rotation: #79 moment and #80 news were both skipped, so a moment fits. Copy check: FRESH for the backboard angle; "TAKEN" for the block/dunk query was a false match (old unrelated Wemby dunks). The backboard self-pass wasn't picked: #71 Haliburton already did the alley-oop-to-himself idea.
**Made.** #82 "Wemby Blocked A Three And Scored Point 40 Five Seconds Later" (numbered 82: the Hub's Boozer card already uses 81): script (65 words, about 17-20 s), notes with exact source words, cut plan, UPLOAD.md with tags at 486/490. Hub card `shorts/n82` = `editing` ("needs the ElevenLabs key"). News: post Sun Nov 1 or drop it.
**Lesson.** None new: no measured data reachable from this session (no Studio export since Oct 24, no API token).

## Sun Nov 1, 2026, about 00:45 UTC (owner asked: "update the shorts hubs"; this account's Hubs)

**Hubs updated** (this account's pair: NBA SAWcHwuAwBxJuyBQSs8a8U, FC 2UVAcbNpKq6j4YXBEF8ge3; the other account's EZrk/LFsQ Hubs and task list can't be opened from here).
- Statuses and views from the public channel lists (yt-dlp, Nov 1 00:35 UTC; single-video pages and RSS were blocked): every posted Short now shows its public views; stayed % only where a Studio export has it (nothing since Oct 24).
- NBA: new cards #69-#79 and the Boozer Short (made on the other account; its folder isn't in GitHub); **#74 "Why NBA Players Refuse This Free Throw" was never posted, so it is the one ready card (Sun Nov 1, 7-8 AM ET)**; #79 and #80 skipped (news windows passed); #73 and #67 stay scripts.
- FC: S04-S08 posted with views, new cards S15-S18 (posted) and S09 (script); S19/S20 stay scripts. **Nothing ready to post on FC.**
- TikTok/Instagram caption fields and S06's long-cut tab removed (cross-posting paused by the owner, Oct 26); the long cuts stay in GitHub.
- Channel stats: NBA last-7 median 7.8K (up from about 3.4K a week ago; #72 24K, #77 23K); FC goalkeeper Shorts 4 of 4 at 9K+ (S01 30K, S05 28K, S03 15K after a late climb, S17 9K), every other FC Short 1-3K.
- ElevenLabs: this session's key works; 83,440 credits left until Nov 19.

## Sat Oct 31, 2026 (NBA daily run; routine; no ElevenLabs key)

**Blocked.** `cloud_setup.sh`: `key: MISSING`, so no voice, render or QA; script, sources and cut plan only. Analytics: no token (YT_CLIENT_ID / YT_CLIENT_SECRET / YT_REFRESH_TOKEN missing), so `yt_analytics.py` and the dataset hand columns were not run. Nothing faked.
**Context.** No NBA build or Oct 31 research had been pushed by 10:42 UTC (the last NBA commit was the Oct 30 research at 07:55 UTC; Oct 30's picks, Slawson/LeBron and Boozer, were never built and are now too old). Saturday's NBA slot was open (`UPLOAD SCHEDULE.md`).
**Research (Fri Oct 30 games; AP recaps on ESPN, ESPN box scores).** Candidates:
- **Warriors 112, Lakers 95** ([recap](https://www.espn.com/nba/recap?gameId=401909285)): Lakers led 38-15 after one (Luka 21 in the quarter), Warriors won the second by the same 38-15; first team in the shot clock era to trail by 23+ after one and be tied or better at half; largest win in that era by a team down 20+ after one (old best: Warriors by 14, Mar 4, 1976); Curry passed Dominique Wilkins for 18th all-time. Luka 37, Curry 31.
- Mavericks 116, Rockets 111 ([recap](https://www.espn.com/nba/recap?gameId=401909283)): Irving 35 and Flagg 33 hand Houston its first loss; Durant (career 88% FT) missed two with 1:53 left; Irving's active FT streak now 54.
- 76ers 98, Knicks 93 ([recap](https://www.espn.com/nba/recap/_/gameId/401909280)): LeBron (41) 20/9/8, late go-ahead fadeaway and a chase-down block on Anunoby.
- Also: Murray 39 (Nuggets 127-120 Suns), Barnes 41 in a loss (Magic 121-114 Raptors), Pistons 5-1.
**Pick:** the Warriors/Lakers mirror score: same-day news with a number gap, two household names, a pattern you can see on the scoreboard. Lane rotation: last six NBA builds were evergreen, moment, evergreen, news, evergreen, moment, so news is within 1 in 3. `copy_check.py "Lakers 38-15 Warriors same score"`: FRESH.
**Made.** #80 "The Lakers Won A Quarter By 23 And Still Lost By 17": script (90 words, about 24 s; `script_lint.py`: only "after" repeated), notes with exact source words, cut plan from ESPN's public clips (all six downloadable today), UPLOAD.md. Hub card `shorts/n80` = `editing` ("needs the ElevenLabs key"). News: post Sat Oct 31 or drop it.
**Changed / noticed.**
- Tags: `tags_fit.py` now caps at 150 characters (Oct 26 Posting Study rule); the scheduled task's prompt still says 490. Followed the tool.
- This session's NBA Hub (artifact SAWcHwuAwBxJuyBQSs8a8U) has no cards after #68; the cards for #69-#79 seem to live on another account's Hub. The #80 card may need copying there.
## Sat Oct 31, 2026 (FC daily run; routine; no ElevenLabs key)

**Blocked.** `cloud_setup.sh`: `key: MISSING` (ElevenLabs), `gemini: MISSING`. Script and notes only; Hub card `editing`. No voice, render or QA, nothing faked. No long cut (paused by the owner Oct 26). Account 2: merged origin/account2 (its Oct 30 log only); its queue is empty.
**Data.** Analytics: no token (YT_CLIENT_ID / YT_REFRESH_TOKEN_FC not set). `shorts_dataset.py`: FC rows unchanged (needs a Studio export). Public counts (yt-dlp, 13:45 UTC): **S17 Krul 5.4K** (~1 day; was 1.2K Fri), S08 3.1K, S16 2.7K, S15 1.0K (3 days), S01 30K, S05 28K, S03 15K. S18 Mourinho not up yet (Sat slot).
**Learned.** No new lesson (nothing new has crossed 72 h). S17 is already 2x the non-goalkeeper ceiling at day 1: the goalkeeper-shootout pattern looks like 4 for 4; judge it at 72 h (Mon Nov 2).
**Lane.** S18 revenge, S19 topical/goalkeeper (unvoiced), so today: secret object, not a goalkeeper (keeps the goalkeeper series at most 1 in 3).
**Research.** Pelé paid to tie his laces (Idea Bank S06) checked and rejected for now: only secondary sources, conflicting fee and pact makers ([Wikipedia: Dassler brothers feud](https://en.wikipedia.org/wiki/Dassler_brothers_feud)). Pick: Messi's napkin contract, with the 2021 ending. Sources: [NPR via OPB](https://opb.org/article/2024/05/18/napkin-securing-lionel-messi-s-first-contract-fetches-nearly-1-million-at-auction), [SI 2012 book extract](https://www.si.com/soccer/2012/02/06/barca-extract), [90min](https://www.90min.com/lionel-messi-contract-napkin-sells-staggering-amount-auction), Barcelona's Aug 5 2021 statement ([Al Jazeera](https://www.aljazeera.com/sports/2021/8/5/messi-to-leave-barcelona-due-to-financial-structural-obstacles)), [AP via WJLA](https://wjla.com/news/nation-world/messi-breaks-down-says-he-wasnt-ready-to-leave-barcelona-08-08-2021). copy_check: FRESH.
**Made.** `Soccer Channel/Productions/2026-11-02 S20 Barcelona Signed Messi On A Paper Napkin/`: script.txt (196 words, ~52-54 s expected), notes.md (claims with exact words, cautions, beats), UPLOAD.md (no-music side). Hub card s20 `editing`.
**Idea Bank.** +S23 Begović's 13-second goal from his own box (Guinness), +S24 Ronaldo's 2003 audition v United; S06 Pelé caution added; idea S20 (Chelsea shootouts) relabelled since production S20 is the napkin.
**Backlog needing a voice:** S09 Ronaldo Coca-Cola, S19 Rulli, S20 Messi napkin (3 scripts). The FC Hub has nothing ready after S18.

## Fri Oct 30, 2026 (FC daily run; routine; no ElevenLabs key)

**Note.** The FC routine fired Oct 27, 28 and 29 too, but those notifications only reached this session today; one run was done (today's), nothing back-filled.
**Blocked.** `cloud_setup.sh`: `key: MISSING` (ElevenLabs), `gemini: MISSING`. Script and notes only; Hub card `editing`. No voice, render or QA, nothing faked. Long TikTok/IG cut not made (paused by the owner Oct 26; no voice anyway).
**Data.** `yt_analytics.py --channel fc daily`: no token (YT_CLIENT_ID / YT_CLIENT_SECRET / YT_REFRESH_TOKEN_FC not in the environment). `shorts_dataset.py --report`: FC still only the 3 Shorts with Studio data (S01-S03), so no new rows to hand-fill; the newer posts need the owner's Studio export. Public counts (yt-dlp): S01 30K, S05 28K, S03 15K, S08 3.0K, S07 2.5K, S16 2.4K, S06 2.0K, S04 1.9K, S02 1.8K, S17 1.2K (today), S15 1.0K.
**Learned.** Lessons Learned, Oct 30: non-goalkeeper ceiling (n=8, 1.0-3.0K) holds; S17 is the live test of whether "goalkeeper" or "a trick" drives the hits (judge Mon Nov 2).
**Lane.** Last posts: S15 versus-own, S16 topical, S17 goalkeeper trick, S18 (Sat) revenge. Pick: topical question answered with a story. S08 Hand of God is already posted (M40gpi_afJo), so the next unmade fitting idea was S19 Rulli.
**Research (sources and exact words in the S19 notes.md).** Rulli saved Ayari and Dunk as City (holders) beat Brighton 4-3 on pens, Oct 28 ([AP via ClickOnDetroit](https://www.clickondetroit.com/sports/2026/10/28/man-city-wins-penalty-shootout-to-advance-in-english-league-cup/), [SI](https://www.si.com/soccer/man-city-player-ratings-vs-brighton-survive-penalties-10-28-26)); 2021 final, 21 straight penalties then Rulli saved De Gea's, 11-10 ([SI 2021](https://www.si.com/soccer/2021/05/26/europa-league-final-villarreal-manchester-united-de-gea-penalty-kicks), [AP via KEYT](https://keyt.com/sports/2021/05/26/villarreal-defeats-manchester-united-in-dramatic-penalty-shootout-to-win-europa-league/), [AFP via Ahram](https://english.ahram.org.eg/News/413005.aspx)); City signed him Aug 2026 as Donnarumma's backup and had signed him in 2016 without him ever playing ([theScore](https://www.thescore.com/news/3578653)). copy_check: FRESH.
**Footage.** UEFA's full shootout (X_NSB3CnHoo), Man City and EFL extended highlights (FYOQPzXc4T4, e9T4cngiGaw) exist, but YouTube refuses cloud downloads (bot check): download on the PC or find the clips on X.
**Made.** `Soccer Channel/Productions/2026-11-01 S19 Man United's Penalty Nightmare Is Now Saving Man City/`: script.txt (186 words, ~50-52 s expected), notes.md, UPLOAD.md (music side of the A/B). Hub card s19 `editing` on the FC Hub named in the routine (2UVA...).
**Idea Bank.** +S21 Higuita's scorpion kick at Wembley (1995; jailed 1993), +S22 Rogério Ceni's 131 goals as a goalkeeper; S19 marked scripted.
**Noticed.** The routine's prompt still says 12 PM ET slots, a 2UVA Hub and long cuts; the daily-run skill (owner, Oct 26/28) says 8-9 AM ET, the LFsQ Hub for the main account and long cuts paused. Followed the skill on slots and long cuts; used the Hub the prompt names. That Hub's cards stop at S08 (S04-S07 still say `ready` with October slots).

## Tue Oct 27, 2026 (NBA daily run)

**Blocked.** `cloud_setup.sh`: `key: MISSING` (no ElevenLabs key in the environment), so no voice and no render. No analytics tokens either (analytics: no token). Nothing faked.
**Research.** No Oct 27 research file; used the Oct 26 scout. #2 Haliburton and #4 Nuggets kid are already built (#71, #72); #3 LaMelo/Ant is saturated (HoH 1.1M). Pick: scout #1, Bones Hyland's fake-throw technical (Wolves 117-94 Raptors, Oct 25). Sources are in the scout file (Yahoo/Big Lead, Heavy, ESPN box, AP via CBS).
**Made.** Script, notes, cut plan and UPLOAD.md for #73 (no-music side, to keep the alternation). Hub card s73 set to `editing`: needs the key. Footage in /tmp/scout_src is gone; re-download with `Tools/x_clip.py`.

## Tue Oct 27, 2026: FC daily build (routine; no ElevenLabs key)

**Hub check.** Ready and unposted: S05 (Pickford) and S08 (Hand of God) = 2, so a build was due.
**Blocked.** `ELEVENLABS_API_KEY` is not in the cloud environment, so no voice, render or QA. Per the daily-run skill: script and notes only, Hub card `editing`. Analytics: not run (no YT tokens checked; `yt-dlp` also missing, so `copy_check.py` could not run).
**Pick.** Idea Bank S10 as S09 "Ronaldo moved two Coca-Cola bottles, and billions disappeared" (global star, concrete object, versus-their-sponsor conflict; not another "Goalkeepers who..."). Script 216 words (target 230-250; do not add, check length after the voice). Sources in `Soccer Channel/Productions/2026-10-27 S09 Ronaldo Moved The Coca-Cola Bottles/notes.md` (SI, Snopes, Al Jazeera, ESPN). Twist kept honest: the $4bn drop is a same-day market-value change and Snopes rates the causation "Mixture".
**Open.** Footage not checked; Coca-Cola's exact quote needs a primary link; copy-check not run. Owner: add the ElevenLabs key to the environment settings.

## Sat Oct 24, 2026 (manual session; the automatic runs start Sun Oct 25)

**Data.** Studio exports Oct 17-24 for both channels (`Research Notes/Studio Export Read (Oct 24, 2026).md`). API analytics:
no token in the cloud yet (needs `YT_REFRESH_TOKEN` / `YT_REFRESH_TOKEN_FC`).

**Learned.**
- FC: S01 80% stayed vs S02 56% and S03 65%. Cause: frame 1 and the first line did not show the promise, and S03 reached its
  promise at 54 s. Full write-up: `Research Notes/Why S02 and S03 Underperformed (Oct 24, 2026).md`.
- Ahmed's Goal data: title shape (plural/singular) is neutral once the era is accounted for (the first read, 318K vs 217K, was
  an era effect; corrected the same day). The singular-title advice is withdrawn.
- Ahmed's best titles promise a human conflict (refused, rejected, bullied, backfired). His news questions now do as well as his
  evergreen Shorts (238K vs 245K, n=65 vs 45) and include his biggest recent hits.
- Third-party guides agree the first frame is the hook (sound often off) and target 75-80% "viewed vs swiped".

**Changed today.**
- `Tools/qa_short.py`: gate on a dark frame 1 (caught S04: someone passing the camera for 0.25 s; fixed and re-rendered);
  story-format warnings for a late promise (cuts.json `"promise"`) and for more than 10 names in the first 15 s.
- `Tools/yt_analytics.py`: `--channel fc` for the soccer channel's own token and files; a no-PC sign-in.
- `.claude/skills/story-short/SKILL.md`: hook rules, frame-1 rule, title advice.
- New: `.claude/skills/daily-run/SKILL.md` and `UPLOAD SCHEDULE.md`.

**Made.**
- NBA #66 Why SGA Ended His Own NBA Record (24.6 s, QA PASS). Sources: ClutchPoints, CBS Sports, Bleacher Report (Oct 23).
  Footage: Thunder team site on NBA.com ("Highlights: OKC 96, DEN 84", "2 Consistent. 2x MVP", "SGA - 10/5"), a Bulls clip, the 1962 Wilt photo.
- NBA #60 Caitlin Clark rebuilt from the logged in-points (28.2 s, QA PASS).
- FC S04 first-frame fix (both versions, QA PASS).

**Research leads.**
- NBA: the Thunder team site has no post-game interviews for regular-season games; the MVP reel ("2 Consistent. 2x MVP",
  May 17 2026) has the sharpest SGA close-ups, but each lasts only 0.5-1 s between flash transitions (slow them 0.5-0.75x).
- NBA: `Tools/nba_videos.py search --player <id>` finds a star's reels on every team site; the TBU podcast episodes have
  burned-in lower thirds (not usable).

## Wed Oct 28, 2026, evening (main session, owner's request)
- Owner: "yes, delete all footage / see how much of the to do list you can do yourself first / for all clips that are viral, experiment with using the actual audio for the moment".
- Real-audio versions built and QA'd: #75 rookie (to post today), #76 Pierce (Thu), S17 Krul (Fri). Tool: `Tools/nat_sound.py`.
- Deleted about 16 GB of old footage (git-ignored files only); kept src for #74, #75, #76, S16, S17.
- To-do list, done by Claude: morning runs now fire into the main session (new scheduled tasks; the old fresh-session ones are paused), so they can push and record. Loch Ness question closed (left out of the music test). The environment task is now just an optional Gemini key swap.
- Still the owner's: posting, the Studio export (vidIQ credits are 0 until Nov 5), the YouTube Analytics sign-in.

## Oct 28, 2026 (main session, owner's request)
- Task list rebuilt for the phone (Now tab with steps and Copy buttons, Note tab for messages to Claude).
- Posting times moved to 7-9 AM (owner), and the routines moved earlier. Both morning routines' pushes failed (403).
  - The research file was recovered into `Research Notes/Daily Research/2026-10-28.md`.
- Built #75 (rookie Brown Jr. / Tatum OT winner), #76 (Pierce wheelchair) and S16 (Fabregas stop scoring).
  - All three: full QA PASS and Gemini READY, on the Hubs and the task list.
- Posted (public channel): Nuggets kid (5.3K Wed morning) and S15 Barcelona (Wed morning).
  - Underhand is due today (the morning post), #75 about 4 PM.

## Thu Oct 29, 2026 (main session: morning routines)
- 06:20 UTC Bronny check: DNP again Wed (coach's decision, ESPN box score). #77 unchanged; posting Thu ~3 PM is cleared.
- Research run: `Research Notes/Daily Research/2026-10-29.md` (top NBA pick: two long buzzer-beaters 20 minutes apart; soccer: Fleetwood beat Arsenal on penalties without practising them, Mourinho's Clásico return). Gemini watched the two biggest outliers.
- NBA build: **#79 Two Buzzer-Beaters From 40 And 50 Feet**. Candidates: the buzzer-beater pair (verified video + two live calls), Jokić's 200th triple-double (no video found yet), Dybantsa's debut, Curry's 44. Picked the pair: a moment you can watch, real audio, and a box-score punchline (Jović 7 minutes; Edgecombe 1-for-6 from three, the 50-footer his only make).
  - Footage: ESPN's public clips of both shots (the broadcasts' calls, a replay, a behind-the-shooter close-up), NBA on X as backup.
  - Real-audio version 25.4 s (both calls in the announcers' voices, `nat_sound.py`, bed -28 dB); narrated spare 19.5 s. Both full QA PASS. Five clips had one-frame flashes from ESPN's encode, fixed with `deflash.py` (originals in `_check/preflash/`).
  - Slot: Fri Oct 30 ~2 PM ET (today's two NBA slots are taken by #76 and #77). Hub card s79, task post-buzzer-beaters.
- Note: `deflash.py` drops the audio track and decodes the whole file into memory; use it on cut clips, never on a long source (a 33 s 1080p source failed).
- FC build: **S18 The manager Barcelona soaked with sprinklers just got his revenge** (Mourinho: 2010 sprinklers, the Sept 2026 sprinkler gift, the Oct 25 Clásico winner and knee slide; payoff: Barcelona were chasing Real Madrid's own 1968 record). 54.3 s, both versions full QA PASS; no-music side of the test. Sat Oct 31 8-9 AM. Hub card s18, task post-s18-mourinho.
  - The research pick (Fleetwood beat Arsenal on penalties without practising them) failed the footage test: the free Sky highlights and Arsenal.com's player can't be downloaded plainly, ESPN has only a studio segment, and the only X video is a post-match interview. Kept in the Idea Bank.
  - Footage: ESPN's public Clásico clips (incl. the knee slide), archive.org's full 2010 semi-final broadcast (the run onto the pitch; the spray itself isn't on it), Mixkit stock for the gift. Premier Sports' knee-slide video on X refused the download (403): not used.

- 6:10 PM ET (owner asked "when should I post?"): live on the channels: #76 Pierce (4.5K) and S16 Fábregas (1.7K); #79 not up yet. The morning script review (other session, 6db47bd) had moved #79 to today, #77 to Fri morning (title "Bronny Is Shooting 100% This Season"), #74 to Fri ~3 PM, and re-cut #74 and S18 for fact fixes, but the Hubs and task list still had the old order and the old #74/S18 files. Fixed: re-cut files uploaded to both Hubs (S18 re-encoded under 20 MB), cards and tasks moved, #76/S16 marked posted. Re-checked the re-cut audio (local Whisper): "Still a record" and "just like that night in 2010" are gone. Lakers next play Fri 10 PM ET (ESPN schedule), so #77 holds Friday morning.
- Owner asked whether both channels can post at the same time: yes. The 1-hour gap was an [H] guess; the schedule now says the same sitting is fine.

## Fri Oct 30, 2026 (main session, after midnight: owner's questions)
- **Owner:** "do you think shorts are getting better?" and "i posted the rodman short instead of everything else... edit and qa everything else. dont be biased because i say something, always edit for best retention and viewer comfort".
- **Live:** #78 Rodman went up Thu evening (y5dxVvGGaMI) as Thursday's 2nd NBA post; #79 buzzer-beaters skipped (Wednesday news, a 3rd NBA post would break the 2-a-day rule). Saturday's NBA slot is open for Friday's daily build.
- **Are they getting better? (public views, `yt-dlp --flat-playlist`, 00:40 UTC)** NBA, in posting order, blocks of 10 (newest first, Rodman left out): medians **4,650 / 5,650 / 6,150 / 2,900**; 20K+ hits per block 1 / 2 / 1 / 1. So views per Short are flat at about 4-6K since mid-October, with a hit about 1 post in 10; the newest block is also the youngest (1-5 days old), so it may still rise (#72 grew from 19.8K to 23K on day 2). FC (10 Shorts): the three goalkeeper Shorts 30K, 28K, 15K; the other seven 1.0-3.0K, the newest four 1.0-3.0K. The topic decides the hits more than the edit [S, n small]. What would show "better" is stayed-to-watch %, which only Studio has (Analytics sign-in still pending).
- **Edit pass on the queue:** `Tools/comfort_audit.py` (new) + frame sheets every 0.5 s + Gemini as a strict retention editor (prompt below) on #77, #74, S17, S18.
  - **#77 Bronny (Fri AM):** re-edited (clear first frame, stat numbers on screen, Luka's "uh" cut and louder, real footage of Bronny shooting this month for "100%", "1 FOR 1" over opening night). QA PASS, Gemini READY. Hub + task updated.
  - **S17 Krul (Fri AM):** TyC Sports logos/banners blurred in all three versions (`broll.py --delogo`, several boxes now). Gemini 4.5 → 6.2. QA PASS ×3, Gemini READY. Hub + task updated.
  - **S18 Mourinho (Sat):** true peak +1.6 dBTP after the Oct 29 spliced fact fix; limited to -1.9 dBTP, picture unchanged. Gemini's other notes checked on the frames and not acted on (details in its notes.md). Hub + task updated.
  - **#74 free throws (Fri 3 PM):** Gemini 7.5/10, comfort audit clean (true peak -1.7 dBTP), no change: its main ask (don't reuse the opening shot at the end) is our loop rule.
- Strict-editor prompt (Gemini, [S]): "You are a strict YouTube Shorts retention editor... 1) SWIPE RISK 2) COMFORT 3) FIRST 2 SECONDS 4) ENDING 5) TOP 5 EDITS... SCORE x/10" (full text: scratch `editor_prompt.txt`, copied into `Research Notes/Watch Reports/drafts/editor_prompt.txt`).

## Tue Nov 3, 2026 (terminal run, handoff items 1-4)
- Done and committed: scheduler wrapper `Tools/schedule_ready.py` (+ `.bat`; dry run lists only #67/S09 as ambiguous two-DRAFT folders; Task Scheduler entry NOT registered, the classifier blocked it: owner runs the two `schtasks` lines in the .bat header); usage guard in daily-run (section 0a); `Tools/learn.py` + `Experiments.csv` (160 rows) + `Learned Weights.md` (best lead: FC "story" lane 5.4x, n=3, a guess); hook rule re-tested on engaged ratio (line 1 of 12+ words 0.490 n=6 vs 0.557 n=15) and `script_lint.py` flags it; story-short topic rule (soccer research was already finished; Playbook v2 already goalkeeper-first); `Tools/edit_upgrade.py` + DEMO re-cut of #73 (qa_short --full PASS, edit_lint clean).
- Usage: this terminal session cannot read /usage; owner should check it.
STATUS: DONE all handoff items 1-4 incl. item 15 (daily-run reads Learned Weights). Stopped because the task list is complete, not on a usage limit; /usage was not readable here. Owner: register the two schtasks lines in Tools/schedule_ready.bat.
- 17:00 ET step 1: `learn.py` now also shows engaged ratio per feature; added `Research Notes/BUILDER.txt` (provisional `pc`) + `BUILDER.md` + `STATE.md`.
- 17:20 ET step 2: FC build **S29** (goalkeeper lane; BUILDER.txt = pc; S25-S28 already voiced by another run, S29 had script only). Footage test PASSED on YouTube (PC can download): 2022 ball-throw (Backheel 0ZF7QTqQKoI 208 s, MM Comps U-9EFBuZtrU 67 s), 2026 Torres goal (FIFA e6a6lppWZkQ 11 s, highlights 6HaHNYjnghE 118 s). No face clip of the Los Edul interview found (line uses the footage of the final instead). Next: voice, cut, render, QA.
- 17:30 ET step 3: S29 voiced (take 1 passed the gate, 48.9 s, HNR 8.2/jitter 2.85/shimmer 11.04; ~1.2K ElevenLabs characters). Next: footage download and cut plan.
- 17:45 ET step 3b: S29 re-voiced at ElevenLabs speed 1.15 because 1.2 gave 48.9 s (QA story profile needs 50-59.9 s) and 1.1 gave 58.5 s (too close to 59.5).
- 18:00 ET step 3c: S29 voice repaired (sentence 11 'We can't go to penalties' retaken twice, 75 characters); voice_check CHECK, no REDO, 53.9 s, 192 words. Next: footage download (YouTube via yt-dlp on the PC).
- 18:30 ET step 4: S29 footage downloaded (CONMEBOL 2022 shootout yo0JkFMFM3A, FIFA 2026 highlights 6HaHNYjnghE, FIFA Torres goal e6a6lppWZkQ, FOX flxZ-hy9SMw) and mapped on contact sheets (_sheets/). Clean ball-throw footage NOT found (the Backheel breakdown has burned-in captions, MM Comps is a top-down graphic): that line will use Martinez/Tchouameni shots near it and notes.md will say so.
- 19:10 ET step 5: S29 cut (36 shots, 40/min), rendered final_music.mp4 and final_nomusic.mp4 (54.2 s). Next: QA --full, frame check, UPLOAD.md.
- 19:50 ET step 6: **S29 BUILT** (PC): `Soccer Channel/Productions/2026-11-07 S29 .../`. 54.2 s, 36 shots, both versions `qa_short --full` PASS (after three QA rounds: first-3 s action, a repeated goal clip, a 0.28 s picture/sound gap fixed by a 0.15 s clip pad, one green end-card frame at 1:45 of FIFA's highlights avoided). DRAFT files (music / no music) are in the folder (video is not committed). UPLOAD.md has title, 3 alternates, tags (481/490), pinned comment, slot Sat Nov 7 12:00 PM ET and an honest "known gaps" list (ball-throw not shown, 720p sources, generic 2026 footage). NOT on the Hub, NOT scheduled (two DRAFT files = the A/B arm is the owner's call; `schedule_ready.py` skips it by design).
- 19:55 ET: S29 DRAFT mp4s are 97 MB each (local only; the push of them failed and was undone). Before putting S29 on the Hub, re-encode under 20 MB (the Hub cap, see how S18 was done on Oct 29). Pushed: everything else (commit 31e2a9c).
- 20:10 ET step 7: owner: usage 98% left; task = prepare full automation (no videos): preflight check, unattended runners, usage file, runbook, pre-generated research/script backlog.
- 20:20 ET step 8: added Tools/preflight.py and USAGE.txt; wrote the Account 1 handoff (HANDOFF - Account 1 (Nov 3 night).md).
- 20:30 ET step 9: wrote Tools/run_daily.ps1 (unattended per-channel runner with preflight, BUILDER guard and lock). Not registered: the owner runs the schtasks lines in its header.
- 22:00 ET step 10: owner: build in cloud so both accounts can edit. Set BUILDER.txt=cloud, wrote CLOUD DAILY RULES.md, BUILDER.md (cloud/PC split), PC Requests.md, Tools/copy_cloud_env.ps1; re-pointed and ENABLED the NBA (3:17 AM ET) and FC (4:23 AM ET) cloud routines (they were disabled since Nov 2). Owner-only left: paste keys into the cloud environment, Publish app (Google OAuth), register the PC timers.
- 22:15 ET step 11: schtasks blocked again by auto mode even with owner OK; wrote Tools/register_tasks.ps1 (owner runs once) and EVERYTHING - index (Nov 3 night).md.
- 22:45 ET step 12: verified tasks (analytics 3:20, schedule ready AM 6:30 / PM 6:30, terminal resume Wed 1:30 PM). Wrote HANDOFF - Account 1 START HERE (Nov 4).md (the 1:30 PM session reads it) and Research Notes/Improvement Backlog.md; resume prompt re-pointed; preflight now expects the real task list. Cloud builds (BUILDER=cloud).
- 23:05 ET: owner clarified: the 1:30 PM start runs on THIS account (account 2) to START the automation and CHECK that everything works. Added section 3A (7-step proof, results to Research Notes/Automation Check.md) to HANDOFF - Account 1 START HERE (Nov 4).md and updated the resume prompt.
- 17:50 ET (PC account 1): fixed `.claude/settings.local.json` (two JSON objects glued together; merged, owner kept the `schtasks /create` allow rule). `schedule_ready.py`: A/B pairs scheduled only with a card `**Arm:** music|no-music` line, or `--default-arm` (opt-in; then a `**Post:** MUSIC version` line wins); same-channel slots under 6 h apart are now skipped (against Scheduled Uploads.csv and earlier picks in the run); skip reasons logged on `--go`. Timers unchanged (no `--default-arm`), so S09/S29/#67 still skip.
- **SLOT CLASH (owner):** S09 Ronaldo Coca-Cola and S29 goalkeeper both say Sat Nov 7 12:00 PM ET on FC. Not changed (safe option: leave both cards; the new guard refuses the second one). Pick one for Nov 7 and move the other.
- 19:45 ET (PC account 1): **#94 BUILT: "The NBA Banned Dennis Rodman's Jersey Number"** (`Productions/MetaSports/2026-11-06 94 Rodman Number 69/`). 19.2 s, Alex, no music, 12 shots; `qa_short --full` PASS after two fixes (B02 is in-game footage, so kind=action; the last shot repeats shot 1 on purpose, marked replay); first/middle/last frames checked. Footage: the real No. 69 jersey at his Dallas press conference (Dunkman827), Stern and Cuban, 2000 Mavericks highlights (720p). Every claim sourced in notes.md; left out: the year (1999/2000 split), the "salary cap" guest-house reason (one weak source). Slot Fri Nov 6 7:15 AM ET. **Card says HOLD** (owner asked for no scheduling without approval this run), so the timers skip it until the owner removes HOLD. DRAFT is 21 MB: not pushed, not on the Hub (re-encode under 20 MB first). Voice ~400 characters.
- Max Claude preview (handoff `Clients/Max Claude/Productions/00 Preview/HANDOFF.md`, route B on the PC): inputs rebuilt with `prep.py` (new narration take 45.52 s, words.json committed); `render.py` fixed for Windows (filter paths); placeholder 9:16 renders at -14.7 LUFS, no black frames. Installing SadTalker (portable Python 3.10 + venv under C:/Users/Admin/apps, nothing system-wide) for the talking clips. **Fact note for the owner:** the 00 Preview narration still says "ridges that loop, split and stop", "millions of prints in seconds" and "the computer only suggests a match"; `01 Fingerprints/notes.md` corrected those (a loop is a pattern, not a minutia; no source for "millions"/"seconds"; "usually", not "only"). Not changed: the placeholder was already sent to the owner, so switching scripts is the owner's call.
- 20:15 ET (PC account 1): owner approved #94 (HOLD lifted), S29 Sat Nov 7 (no-music) and S09 Sun Nov 8 (music) via **Arm:** lines. Dry run: all three would schedule; the 6:30 AM timer schedules them privately. Fixed yt_schedule.py crashing on emoji titles in the Windows console (#94's title was refused). Max preview files were NOT emailed or uploaded: they are on the PC only (00 Preview folder).
