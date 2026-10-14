# CLOUD STATE (single source of truth for any agent or new chat; update as you go)
Last updated: 2026-10-14 (newest section at the bottom). Branch: `main-329h3w` (draft PR #1). The user posts the videos; NEVER upload/publish or open YouTube Studio.

## Where everything lives (all in this repo, so any session can read it)
- Pipeline + quality rules: `.claude/skills/cloud-short/SKILL.md` (start with its QUALITY FORMULA and the evidence-tier rules).
- Memory of mistakes/wins: `Research Notes/Lessons Learned (running log).md` (add to it whenever you learn something).
- Research (every claim has an evidence tier PROVEN / SUPPORTED / HYPOTHESIS): Round 4 (cloud), 5 (competitors), 6 (what makes Shorts viral), 7 (retention deep dive), Idea Bank, Critique Round 1, all in `Research Notes/`. Where Round 6 contradicts older notes, Round 6 wins.
- Quality gate: `python Tools/qa_short.py --folder <folder>` must PASS before delivery (warn lines = unproven rules, log in A/B table).
- Tools: Tools/assemble.py (ffmpeg engine), x_clip.py (X videos), broll.py, card.py, splice_voice.py (real quote audio + narration), voiceover.py, thumb.py, copy_check.py, yt_sheet.py, pc_cut.py. anchor_shots.py (pin each shot to the word it illustrates, from `anchor` in shots.json), hub_pack.sh (`Tools/hub_pack.sh "Productions/MetaSports/<folder>"` makes _hub/s.mp4 + jpg covers for the Hub and refreshes the READY mp4).
- Captions: `--caption-style metasports` (ALL CAPS, house style), `clank`, `karaoke` (new, untested; A/B it).
- ElevenLabs key: lives ONLY in the cloud scratchpad/env, never in chat or git. If missing: ask the user to add it in the cloud environment settings. Cloud usage is limited: do not spawn more helper agents than needed.

## Phone Hub (the user's app)
https://claude.ai/artifact/EZrk8n855PyYpMFnMnMJd4. DB collection `shorts` (doc per Short: num, name, title, status, about, versions[{label,assetId,note}], covers, titles, tags, pinned, postNote; NO description) and `ideas`. Upload full 1080p under 20 MB with the Artifact tool (`asset:true`, files must be in the scratchpad), then ArtifactData `set` with the asset ids (`if_version` on existing docs). Downloads use the in-app downloads.save button.

## Shorts status
Posted by user (Oct 3-4): Wembanyama (24 s, record oddity: 79.5% stayed, 100.3% avg viewed, 20.6K views in ~10 h, rank 2/10) and #12 Duren (33 s, contract: 63% stayed, 59.7% avg viewed, 1.5K in 5.5 h, rank 8/10). See Outcome Log.md. Lane to favour: record/rule/oddity, one clear fact, 22-28 s, escalation, end on the payoff; de-prioritise contract/trade stories. Ready (in Hub, pushed): #1 LeBron pay cut (v6/v7), #11 Jordan push-off, #13 Kawhi picks (v3 re-synced), #14 NBA named four stars (tail fixed), #15 Heat Vice City + Adams, #16 Giannis vs Bucks in Vice City, #17 flopping crackdown (A house captions / B karaoke captions = A/B test), #18 LeBron helicopter (v2 Sixers footage; post before Oct 5 Sixers-Knicks), #19 Flagg height, #20 Bad Boys defense then vs now, #21 Jokic vs Westbrook record, #22 only one man can wear six (evergreen oddity), #23/#24/#25 Bronny (first season without LeBron + 16-for-15 roster spot; guaranteed deal does not guarantee a spot (overlaps #23: post one or a week apart); did he actually get better). Next up from the idea bank: ib02 screens (a week after #17), ib03 3-2-1 lottery, ib04 Hinkle, ib06 underhand, ib08 gather step, ib10 what players cannot wear, ib12 Giannis iguanas (post a day apart from other Heat Shorts). Idea bank: Research Notes/Idea Bank - Oct 4, 2026.md (+ idea_bank.json); top 12 are in the Hub ideas list (ids ib01-ib12). Same-story-family pairs (#15/#16, #11/#14/#17) must post a day apart.

## House rules (summary)
Real footage first (6+ clips before scripting), hook = real striking image + name/number line at 0.0 s, 3+ cuts in 3 s, 21-45 s, loop to the first shot, end on a comment-bait question, titles 4-7 words opening Why/How/What/Did/Is/He + one emoji, tags 440-490 chars, no description, one cover. Chat with the user: short, plain English, phone-friendly.

## Critic process
Before each batch of 3+ Shorts run an adversarial critic helper; log verdicts in `Research Notes/Critique Round 1 - Verdicts.md` style files; change only what evidence or a verified defect supports.

## Pending / next
Retention deep dive (Round 7), idea bank into Hub `ideas`, critique triage (accept/reject each point with reasons in `Research Notes/Critique Round 1 - Verdicts.md`), Shorts #19/#20 to Hub, then more Shorts from the idea bank. When the user sends analytics (due Oct 6): read Viewed-vs-swiped and average % viewed per Short, update the A/B table, and revise rules by evidence.

## Posting queue (Oct 5, all Round 2 rebuilds done, in Hub)
Posted by user: Wemby, #12 Duren, #18 LeBron helicopter, #22 ('Why Two Men Can Still Wear Six', rebuilt version, ~29K views in ~1 day), plus an older Steven Adams real-voice Short (~28K). Queue (field `slot`/`slotLabel` in Hub): 1 #21 Jokic, 2 #15 Adams-led, 3 #24 Bronny spot (before Oct 21 cut), 4 #19 Flagg, 5 #20 Bad Boys, 6 #16 Giannis six-player, 7 #25 Bronny better, 8 #14 Four F's, 9 #13 Kawhi picks, 10 #17 flopping (house vs karaoke A/B), 11 #1 LeBron min (`_claude_v8`, contract lane, last), 12 #11 Jordan/Brown (2 days after #14), 13 #23 father vs son: HOLD until after Oct 21 and only if Bronny made the roster. All pass qa_short; headline text removed; every one ends on its payoff, debate question lives in the pinned comment. Unverified on all: audio by ear. Free stats: `python3 Tools/channel_check.py @MetaSportsClips` (public views via yt-dlp); retention only from Studio screenshots or vidIQ (free plan 150 credits/cycle, 5 per analytics call; channel UCYiLzg5lBTgZ9Q2Sw_Hmwhw is connected). A daily routine (23:07 UTC) logs views to Research Notes/Outcome Log.md. Hub packing: Tools/hub_pack.sh. Round 2 verdicts: Research Notes/Critique Round 2 - Verdicts.md.

## Oct 4 user changes (latest)
- NO big hook headline over the first 2 s any more: captions only (assemble.py ignores --hook-text unless ALLOW_HOOK_TEXT=1). All queued Shorts get re-rendered without it.
- Every queued Short is being critiqued in the Round-1 format (Research Notes/Critique Round 2A/2B/2C) and revised so every story has high retention and a payoff (STORY STANDARD in the skill; ends on the payoff). Tools: anchor_shots.py pins shots to words.

## Visuals and editing (Oct 5)
Tools/visual_fx.py (audit, reframe, statcard, level, render; all options off by default) + Research Notes/Visuals and Editing Playbook (Oct 5, 2026).md. Top ideas: big stat card for spoken numbers, quote name tag + loudness levelling, face-tracked reframe. Retention gain is only SUPPORTED (Wemby n=1) / HYPOTHESIS; merge into assemble.py only after A/B on real results. assemble.py untouched.

## Round 8 (Oct 5): editing styles and caption test plan
Research Notes/Round 8 - Editing Styles and Caption Testing (Oct 5, 2026).md. Findings (mostly HYPOTHESIS, n small): top CoachClank hits are pure game footage from 0 s, no cards (we use ~21% cards); competitors use small white sentence-case captions, nobody uses red/green ALL CAPS, but no same-topic comparison shows caption style drives views; interview clips carry speaker name tags. A persistent top 'premise line' (used by Ahmed's, B/R, HoH) is NOT adopted: needs the user's OK (headline rule). Caption A/B plan: house vs clank first, same lane/length/slot, read stayed-to-watch at 48 h, call a winner only after 3 pairs with avg gap >= 4 points.

## Competitor viewing method + premise-line test (user, Oct 5)
- FREE METHOD (built Oct 5, tested): `python Tools/watch_short.py <tiktok url | local mp4> --out watch/<name>` downloads a competitor Short through the preinstalled Chromium (Tools/watch_dl.mjs; YouTube blocks this cloud IP with a bot check, TikTok pages still play), then writes report.md (cut rate, shots, loudness, words/min, hook, ending, whisper transcript) and sheet.jpg (frames 0.5 s apart for 4 s then 1/s; open it with Read to LOOK at captions/cards/zooms). Find a Short's TikTok cross-post with WebSearch (allowed_domains tiktok.com). X videos: Tools/x_clip.py. First test: CoachClank 'Shaq vs Normal Person' = 60 s, ~30 shots (2.0 s avg), small white sentence-case 2-4 word captions, pure footage, no cards, 309 wpm.
- Paid fallback: vidIQ connector `vidiq_watch_shortform_content` (10 credits per Short, scene-by-scene markdown; poll `vidiq_job_poll`), `vidiq_outliers` (5 credits, keyword + contentType short + sort vph), `vidiq_video_transcript`. Free plan = 150 credits per cycle (next renewal Oct 5 22:32 UTC); keep 40 in reserve. A scheduled reminder fires at 22:34 UTC to run it (outputs Round 9 note). Free fallback: yt-dlp metadata/storyboard thumbnails (Round 8).
- User APPROVED testing a persistent small premise line at the top (not the removed big hook headline). Built as option `--premise-line` in Tools/visual_fx.py (experimental, off by default). A/B: same-lane pair, same slot different days, compare stayed-to-watch at 48 h, call after 3 pairs.

## Cadence and retention reading (Oct 5, user)
User posts 2 Shorts per day. Queue pairs: Day1 #21+#15, Day2 #24+#19, Day3 #20+#16, Day4 #25+#14, Day5 #13+#17, Day6 #1+#11, #23 hold until after Oct 21. Studio (lifetime): Wemby 80.1% stayed / 104.1% AVD / 26.8K at 42 h; Duren 68.7% / 68.4% with a cliff at ~8-10 s where the hook ended and exposition began (see Outcome Log).

## Posting roadmap (Oct 5)
See `Posting Roadmap - Oct 2026.md` (channel median 29K; Bronny/free-throw/Luka/Curry/Wemby are this audience's best topics; 2/day at ~12:30 PM and ~7:30 PM ET, evidence weak, test it; order Day1 #24+#21, Day2 #15+#19(premise-line version), Day3 #25+#20, Day4 #16+#14, Day5 #13+#17, Day6 #11+#1, #23 after Oct 21). Hub slots follow it. Own-channel duplicate warning: underhand free throws already did 73K.

## Round 9 (Oct 5): competitors watched with the free tool (15 TikToks + our #21/#24/#15)
Research Notes/Round 9 - Competitor Shorts Watched (Oct 5, 2026).md. Findings (n small, HYPOTHESIS/SUPPORTED): story channels average 1.9-3.2 s per shot with 0-2 cuts in the first 3 s (ours 0.96-1.3 s, 2-5 cuts); CoachClank narrates 265-309 wpm, Ahmed 274 (ours 221-239); CoachClank story clips have no cards (ours ~21%); CoachClank/Ahmed captions small white sentence-case 3-4 words; Rebound Rewind keeps one title line for the whole video (supports the premise-line test). NOTE confound: the Wemby cut (80.1% stayed) used clank-style captions, Duren used metasports. Decisions: caption A/B = #14 (house, Thu Oct 8 7:30 PM) vs #17 (`final_clank.mp4`, clank captions, Fri Oct 9 7:30 PM), both rule explainers; for NEW builds aim at avg shot >= 1.7 s, fewer cards, faster narration (target 250-270 wpm). watch_short.py: retry if 'no video src'; whisper misspells names.

## Batch 2 (Oct 5) built, in Hub
#28 Hinkle, #29 underhand (Mitchell Robinson angle), #30 Giannis steps, #32 Spurs 29-point lead, #33 run out of players, #34 2007 draft, #35 Wemby rugby (all QA PASS; audio not checked by ear). #26 screens and #27 lottery still being finished by a helper; #31 banned gear blocked on footage (notes.md has the verified facts). Hub slots 14-22: #35 + #34 (Sun Oct 11), #29 + #32 (Mon Oct 12), #28/#30/#33 later. #17 has three versions in the Hub (clank captions = the one to post for the caption A/B).

## Oct 5 evening: voice decision, tighter scripts, ratings (user)
- USER CHOSE voice 'C' (native speed 1.2, no stretch, stability 0.65, similarity 0.7). Defaults now: speed auto (1.2 then 1.15, never below 21.5 s), light noise clean-up (`--clean light` = highpass 70 + afftdn nr10, HNR +1.1 dB; samples 1-4 sent to the user, awaiting a pick), 0.3 s tail pad, take gate, max stretch x1.08. Use `voice_take.py` (single voice) or `voice_pieces.py` (spliced; ONE continuous narration take cut at the quote joins), `revoice.py` to redo an existing Short. Lab (Oct 5): settings beyond stability>=0.65 are within take-to-take noise (+-0.5 dB HNR); afftdn denoise is the only measured gain.
- User wants: tighter scripts (95-105 words, 21-25 s, hook <= 10 words, turn by 6 s, every sentence adds a fact), more Shorts repurposing originally viral videos/topics (Idea Bank 2), and a RATING for every Short (Viral formula 0-100 from the strict critics, see Research Notes/Ratings), then 'list the best Short to post at 7:30'.
- Strict critic Round 3 (3A-3D) covers all 22 queued Shorts; reports in Research Notes/Critique Round 3*.md; audit numbers in Research Notes/Audit Summary - Oct 5 2026.md.

## Oct 13: first full week of posting (15 Shorts posted Oct 5-13), voice still open
- Numbers: 513 subs, 101 Shorts; the 15 new posts have a median of ~2.8K views (177 to 20.4K). Best new: #19 Flagg height 20.4K (103% avg viewed); mid: #23 LeBron vs son 6.5K, #17 flopping 6.7K, #15 Adams GTA 6.0K, #24 Bronny spot 5.7K, #34 2007 draft 4.4K; low (1.0-3.9K): #01, #16, #35, #13, #14, #20, #25 (posted twice), #29. Full table + tiered reads in `Research Notes/Outcome Log.md` (Oct 13 section). Roadmap (`Posting Roadmap - Oct 2026.md`) is STALE: the user posted in a different order from Oct 6; rebuild it from this data before the next batch.
- Retention (vidIQ): 100%+ avg viewed in all 3 Shorts above 19K views, but also in two Shorts that stayed under 3.4K, so looping alone does not make a breakout (SUPPORTED, n=16).
- The daily stats routine (trig_01V8xJ1ZGJ5gbtAon8MCHPxy) wakes THIS session; when the session is idle its notifications pile up (7 missed Oct 6-12). Run `channel_check.py` once and log it; missed days cannot be recovered except from vidIQ.
- Credits: vidIQ 145/150 (renews Nov 5); ElevenLabs 1,032 of 52,087 characters used this cycle (starter; the cap shown changed from 90,000, so re-check with `voiceover.py --check`).
- The user posted #23 (father vs son) although it was on HOLD; it did 6.5K with the best like rate (3.4%). #25 'Did Bronny Actually Get Better' was posted twice (Oct 6: 1.9K at 68.4%; Oct 13: 177 so far).
- OPEN: the user's complaint that all tested voices sound bad (pick among the 8 samples or approve a new approach before any bulk re-voice); edit-style pick A/B/C; fix phase for the queued Shorts (Round 3 ratings); add #36-#39 + ratings to the Hub.

## Oct 13 (later): handoff audit, formula v2, tool fixes, Batch 4 (owner request: "read the handoff file and complete all tasks, use a critic bot")
- **Handoff audit:** `Research Notes/Handoff Audit (Oct 13, 2026).md`.
  - No Grok work from Oct 6-13 is reachable from the cloud. Git, PRs, the Hub and scratch show nothing new; the PC paths and Google Drive are inaccessible (Drive connector auth error).
  - The 15 posts are our exact exports. #19 went up as the premise-line version, #17 with CoachClank captions. Titles of #17 and #20 were changed outside our options (#17's misstates the facts). The #25 re-post is an identical file.
- **Formula:** `Research Notes/Winning Formula v2 (Oct 13, 2026).md` (one visible object + one paradox in second 1; one measure; the ending answers the opening; red circle in frame 1 = HYPOTHESIS under test). The Round 3 critic score predicted views backwards (rho −0.63), so the critic is now `Tools/critic_v2.md`. The Playbook now opens with the canonical Strict Short Formula (overrides older lines).
- **Tool fixes (verified):**
  - `voice_fx.py` pause trimming cut syllables; it now cuts only inside measured silence.
  - `assemble.py` looped clips shorter than their shot (22 of 27 folders). It now slows small gaps and holds big ones, and writes `_render.json`.
  - `qa_short.py` fails replays and frozen holds, warns on cards in the first 4 s, and counts spelled-out numbers.
  - New `pointer.py` draws a red circle/arrow for opening A/B tests.
- **Voice:** a blind, loudness-matched lineup on one script is live: https://claude.ai/artifact/Y9P8QRytak2ikDRfMDqdj2 (files in `Research Notes/Voice Lineup (Oct 13, 2026)/`). The OWNER must pick a slot number. Do not bulk re-record before that. The Oct 5 samples were unfair (5-14 dB apart) and the two "tight" ones had damaged numbers.
- **Edit A/B:** #32 `_editB/` drops the article card at 1.5 s (QA PASS). **Later verdict: #32 rejected by Critic v2, do not post** (see the Oct 14 section).
  - Re-rendered with the fixed assembler: #21, #26, #27, #28, #30, #37, #38 (old exports in `_pre_oct13/`).
  - #33 is blocked: a corrupt clip plus an 11x replay; it needs new footage.
- **Batch 4:** `Research Notes/Batch 4 Concepts (Oct 13, 2026).md` has 4 researched concepts: Jokic pass, Wilt 48.5 minutes, Jordan No. 12, Sharp listed taller than Wemby. Being built: **#40 Jokic** and **#41 Sharp** (folders `2026-10-13 40 ...` and `2026-10-13 41 ...`), each with a plain and a red-circle opening. Each one passes or fails on Critic v2.
- **Posting order:** `Production Queue.md` (canonical).
- **Credits:** vidIQ 145/150 (renews Nov 5). ElevenLabs about 1.6K characters spent today on the lineup, plus the builders' takes.

## Oct 14 (00:20 UTC): both critic passes done, #40 and #41 rebuilt and ready (resumed after the usage-limit pause)
- **Critic v2 (independent agent)** reviewed the exports: `Research Notes/Critic v2 Review (Oct 13, 2026).md`.
  - #40: NEEDS REVISION.
  - #41: REJECT as cut, rewrite.
  - #32: REJECT, abandon. It is a retell of a 7.1M Short; "led the NBA Finals by 29" is wrong (it was Game 4). Do not post either A or B.
- **#40 v2 (ready):** the hook is attributed, matching the Denver Post quote ("probably", "NBA career"). Also:
  - the pass now plays under "No look"
  - BUFFALOES shows under "college gym"
  - it ends "six thousand and eighty. Not eighty-one."
  - the red ring is on the ball, 0-1.5 s
  - Second critic re-check: **PASS**. 21.3 s, QA PASS. Post the **ring** version on Wed Oct 14 (pointer test pair 1); log it as "ring, no pill".
- **#41 v2 (ready):** frame 1 shows Sharp beside a security guard (height reference). Also:
  - the doctored Clippers image is gone
  - the Wemby caption is off his chin
  - the scorebugs are cropped
  - it ends on the answer: "Three-point tries last season: Wembanyama, three hundred and fifty. Sharp, in the G League: zero."
  - The re-check's one fix (Raptors red under "Clippers") was applied Oct 14. 23.0 s, QA PASS.
  - Post the plain version Thu Oct 15. Re-check his status first; don't post if he plays a regular-season minute.
- **Rejected facts (kept out on purpose):**
  - Sharp's free-throw % (sources disagree: 39-43%).
  - The Hack-a-Sharp game (he made 5 of 8).
- **YouTube downloads are bot-blocked** in the cloud ("sign in to confirm"). X posts still download with yt-dlp.
- **Hub:**
  - s40 and s41 added with videos and covers.
  - s32 set to DO NOT POST.
  - #26 and #37 moved up into its slots.
- **Queue:** `Production Queue.md` updated (ranked; the calendar runs to Mon Oct 19). Only #40 and #41 have passed Critic v2. Next session: run Critic v2 on #39, #30 and #21 before their dates.
- **Credits:** ElevenLabs 10,349 of 52,087 characters used this cycle. vidIQ 145/150.
- **Owner decisions still open:**
  - The voice slot (lineup link in the queue).
  - OK or swap for the #36 clip.
  - Listen once to #40 and #41.

## Oct 14 (11:40 UTC): performance audit, Rules Audit, Creative System v3, voice audition, ideas finished (owner brief "Performance audit, existing ideas, editing, AI voice & rule challenge")
- **Read first:** `00 START HERE.md` (rewritten). Canonical files:
  - Audit: `Research Notes/Posted Video Audit (Oct 14, 2026).md` + `Posted Shorts - metrics (Oct 14, 2026).csv` (102 Shorts, vidIQ analytics as of Oct 14, 10 retention curves).
  - Rules: `Research Notes/Rules Audit (Oct 14, 2026).md` (every rule KEEP / REVISE / RETIRE / TEST with source and confidence).
  - How to build: `MetaSports - Playbook.md` → **CREATIVE SYSTEM v3** (replaces the Strict Short Formula; older material kept below it as background).
  - Voice: `Research Notes/Voice Audition (Oct 14, 2026)/` (12 takes measured; no migration; plain "Wembanyama"; the owner's ear picks).
  - Ideas: `Production Queue.md` + `Production Queue - all ideas (Oct 14, 2026).csv` (74 ideas, one status each).
- **Critic v2 (Oct 14):**
  - #39: post-mortem (it was already posted Oct 13, 23:49 UTC).
  - #30: abandon (DO NOT POST).
  - #21: rewritten to v3, re-checked (NEEDS REVISION, re-cut only), fixed to **v3.1** and frame-checked. Ready.
- **Ready to post, in order:** #40 ring (Wed Oct 14), #41 plain (Thu Oct 15; check his status), #21 v3.1 (Fri Oct 16, before Oct 22). Then #38 only after Critic v2, #36 only after the owner OKs the clip.
- **New packages (script-ready, footage-blocked):** #42 "Who Has Missed The Most Shots Ever" (score 60) and #43 "How Did Wilt Average 48.5 Minutes" (53). YouTube is bot-blocked in the cloud and X has no search, so they need X post URLs from the owner or a PC build.
- **Tools changed:** qa_short (unsupported FAILs → warnings; dead-air FAIL; replay-anywhere, slow-hook and naked-number warnings), captions (no lone-word cards; per-shot `cap_y`), voice_check (ordinals). See the Tools Guide box.
- **Experiments pre-registered** (Outcome Log, "Oct 14 pre-registered"): #40 ring vs #41 plain (pointer pair 1), 1 a day this week vs 2 a day before, score vs 48 h views. A one-time check-in fires 2026-10-18 00:30 UTC (`trig_01UPrcSVas2bcQoUB45YZpUN`) to compare #40 vs #41 at 48 h.
- **Hub (Oct 14):** s40 points at the re-captioned files (ring = POST THIS); s21 = v3.1; s39 = posted; s30 = DO NOT POST; s28 = HOLD to about Dec 9-11; slots re-numbered for 1 a day (s41 2, s21 3, s38 4, s36 5, s27 6, s37 7, s26 8).
- **Credits:** ElevenLabs 16,715 of 52,087 characters used this cycle (checked Oct 14, 11:40 UTC). vidIQ 70 credits left (renews Nov 5); each analytics call costs 5.
- **Owner decisions open:**
  1. Post times for #40 (and each next post) into the Outcome Log.
  2. Voice: play the 5 finalists (audition README) and name one, plus which "Wembanyama" is right.
  3. OK or swap the #36 fan-account clip.
  4. The premise pill test (needs your OK).
  5. X links for #42/#43 footage.

## Oct 14 (evening): old-video study, B-roll sourcing system, music system, voice emphasis, ready Shorts improved (owner brief "take this further")
- **Old videos** (`Research Notes/Posted Video Audit (Oct 14, 2026).md` §10 + the watch-reports appendix):
  - 4 old hits + 1 weak control watched scene by scene via vidIQ (50 credits). YouTube downloads and the embed workaround are blocked/refused.
  - What the hits did: exact-moment footage, the scorebug kept as proof and circled, escalation, a punch-line answer, and a music bed with payoff moves.
  - The control had the same music and effects, so those were house style, not the cause.
  - Old pace measured 182-212 wpm (the new posts already run faster).
- **B-roll:** `Library/B-roll Sourcing Guide.md`.
  - New `Tools/footage_lib.py` (log, match, sheet, verify, index, search). `x_clip.py` and `broll.py cut` now log automatically.
  - `sources.csv` is complete and verified for #40, #41, #21 and #38.
  - **#41 v3** replaces an Imagn agency photo (licence risk) with Mavericks preseason game footage of Sharp.
  - `Library/footage_library.csv` indexes all 643 clips (35 verified).
- **Music:** `Library/Music Guide.md`; library `Library/Music/` (4 ElevenLabs beds, clean licence; 3 Mixkit candidates).
  - `assemble.py` reads `music.json`: measured bed level, drops, hits, `--no-music`.
  - QA checks the licence, the level and the speech-band margin.
  - Intelligibility test: no words lost even at -2 LU.
  - Music versions exist for #40 (ring and plain), #41 v3, #21 and #38. Originals are untouched; the `final_*.mp4` renders are in the folders (not in git) and in the Hub.
- **Voice part 2** (Voice Audition README): our voice reads numbers flat, and "..." doesn't make a real pause. Emphasis now comes from the edit (Creative System v3 §5).
- **Owner listening page (Sound Check):** https://claude.ai/artifact/U58nqkg8BHDTJXNdy64Tcd. Five questions: voice, "Wembanyama", music per Short, level, beds.
- **Hub:**
  - s40, s41, s21 and s38 have "NEW … + music (listen first)" versions next to the originals.
  - s41's first version is v3.
  - Note on s40/s41: post both the same way, so the ring test stays fair.
- **#38: Critic v2 REJECT (Oct 14). DO NOT POST.** A retell of the media-day quote (our #18 used it); it drifts off its one measure; the quote shot is out of lip sync. Queue, CSV, Hub (slot 0) and UPLOAD banner updated. Sat Oct 17 → #36 if the owner OKs its clip, else #27 after Critic v2. `qa_short.py` now FAILs slowed quote shots.
- **#42:** still blocked on footage. Search engines don't index X posts, and the library has no LeBron miss or Kobe clip. The owner's X links or a PC build are needed.
- **Pre-registered** (Outcome Log, "Oct 14 (later)"): M1 music cohort (confounded this week with the posting rate), M2 (#40 and #41 must share audio), Q1 question hooks, P1 cut-in pause, S1 scorebug-as-proof.
- **Rules changed** (Rules Audit addendum): B10 no-music retired by the owner, plus B14 scorebug, C2 pace 200-265, B16-B19, C6, A13, D13 (sound-effect licences unknown).
- **Credits:** ElevenLabs 22,389 of 52,087 used (music generation bills here too, plus about 1.9K for the emphasis test). Music: 17 generated minutes a month on Starter, about 2.1 used. **vidIQ 5 credits left** (renews Nov 5), so the Oct 18 48 h check gets one retention call; use free public counts for the rest.

## CHECKPOINT Oct 14, 2026, ~22:15 UTC: end of the "Winning Formula & Voice Overhaul" run (replaces the 20:45 interim checkpoint)
**Read first:**
- `00 START HERE.md`
- `MetaSports - Playbook.md` → THE WINNING FORMULA (top)

**Done this run (verified):**
1. **Winning formula** (`Research Notes/Winning Formula Research (Oct 14, 2026).md`), from:
   - our 102 Shorts and 12 old scripts as voiced
   - our best Shorts (Curry 30.8K, Giannis 28.3K) vs our weakest
   - CoachClank's 148 Shorts (length and title lanes) plus 2 watched; Ahmed's 1 watched
   - Patterns sorted: supported / promising / creator-specific / preference.
   - **Blocked:** CoachClank's actual top Shorts. YouTube refuses this server, the TikTok profile hides its list from an automated browser, and vidIQ has 5 credits.
   - The Playbook's top section is now the one-page formula: 3 structures, fixed settings, a 10-step workflow, one test at a time.
2. **Voice** (Voice Audition README, Part 3):
   - **Diagnosis:** the clone is a copy of TTS recordings; it ran at 259-267 wpm; the denoise stripped the s/t/f detail.
   - **Rounds 2-3:** 9 library voices, then the finalists at the real pace on 2 scripts with 2 takes each.
   - **Primary: Alex.** **Backup:** our clone with fixed settings.
   - **Config:** `Tools/voice_config.json` + `Tools/pronunciation.json`; voiceover/voice_take/assemble updated.
3. **Applied to real Shorts:**
   - #40, #41 and #21 **v4** (`_v4/` subfolders; nothing overwritten).
   - Re-voiced, re-anchored, music retimed. #21 also re-cut 3 clips longer and split 2 shots.
   - All QA PASS. Frame sheets, flash scan, transcripts and music placement checked.
   - In the Hub as the top version of each card. `_v4/CHANGES.md` has the details.
4. **Sound:** `Library/Sound Library.md` (new):
   - the owner's tracks and their status
   - the CoachClank sound: two readings, not guessed
   - YouTube's music routes (copyrighted songs only via the app's Add sound picker by the owner)
   - dated trend evidence (none fits a narrated Short)
   - test edits T1 (timing) and T2 (a louder bed: no words lost)
5. **Sound Check round 3:** https://claude.ai/artifact/U58nqkg8BHDTJXNdy64Tcd (4 questions).
6. **Docs updated:** Playbook (formula; §6 voice; §7 experiments frozen), Rules Audit, Lessons, Outcome Log (formula freeze, V1), Music Guide, Tools Guide, START HERE, Production Queue + CSV.
   - The old-hit pace (182-212 → 206-252) is corrected everywhere.

**Open (owner):**
- Answer Sound Check round 3: voice, names, old vs new for 3 Shorts, music level.
- Check Alex's licence in ElevenLabs → Voice Library. I couldn't reach the terms page.
- Post #40 and #41 the same way (same voice, same music).

**Credits:**
- ElevenLabs about 36K of 52,087 used (resets Nov 8).
- vidIQ 5 (renews Nov 5).
- Music: 17 generated minutes a month, none used tonight.

**Side effect to know:** the 9 auditioned library voices were added to "My Voices" by the API. Harmless; remove unused ones in ElevenLabs if you like.

**Next session:**
- If the owner picks Alex: build the next queued Short to the Winning Formula with the house voice, end to end.
- If not: set `voice_config.json` "default" to "backup" (one line) and keep the old-voice versions.


## CHECKPOINT Oct 14, 2026, ~23:55 UTC: the "Winning Formula, New Stats & Voice Overhaul" run
**Done (verified):**
- **Stats:**
  - No owner stats file reached the cloud copy (asked).
  - Pulled public counts for all 104 Shorts: #40 got 655, #41 got 1.6K.
  - Metricool daily channel views (the per-video sync is still empty).
  - Audit §12.
- **Script Critic v3** (`Tools/script_critic.md`, plus the `script_lint.py` helper).
  - Calibrated on 10 posted Shorts: it fits all 10 (views known while scoring).
  - Queue scored: #21 and #36 rewritten to APPROVE; #27, #26 and #37 rejected; #09 and #10 need rewrites; #42 and #43 blocked on footage.
  - Log: `Research Notes/Script Critic Log.md`.
- **Voice round 4:**
  - A vs F vs current Pham vs original Pham vs a NEW clone "Pham v3" (`61QfR1QEcJUskHn8yioH`). The new clone is the flattest, so it isn't adopted.
  - pham v2's training data was found triplicated.
  - The pitch gate is added.
  - Voice README Part 4.
- **Real edits:**
  - #21 `_v5` (A) / `_v5_F` (F); #36 `_v2` (A) / `_v2_F` (F).
  - Rewritten scripts, no music, QA PASS, flash-free (`deflash.py`), transcripts checked.
  - In the Hub (top of each card).
- **Music:** no background bed by default (owner). Playbook, Music Guide, Sound Library and QA are updated.

**Open:**
- The owner picks A or F (then set `voice_config.json` "default"; F = "backup").
- The owner's OK on #36's fan-account clips.
- The owner's new stats files.
- A Metricool per-video re-check is scheduled for about 02:03 UTC; the fallback plan is in that check-in.

**Credits:** ElevenLabs about 46K of 52,087 used (resets Nov 8).
