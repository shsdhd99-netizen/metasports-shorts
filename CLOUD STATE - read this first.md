# CLOUD STATE (single source of truth for any agent or new chat; update as you go)
Last updated: 2026-10-14 (newest section at the bottom). Branch: `main-329h3w` (draft PR #1). The user posts the videos; NEVER upload/publish or open YouTube Studio.
**Owner, Oct 19 (standing until they say otherwise):** "you are able to run from my pc now, you do not need to look for cloud solutions." Prefer the PC when the session runs there. Lead with THE #42 FORMAT (what works), other formats allowed (`Library/THE 42 FORMAT.md`). When the owner is away from the PC, source footage in the cloud yourself.

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

## Oct 15, 2026 (about 04:00 UTC): production upgrade checkpoint
**Done and pushed (branch `main-329h3w`):**
- **YouTube Studio export:** analysed (audit §13). "Stayed to watch" tracks views at +0.77 (n=20). Hook gate added to the Playbook, Script Critic v3 (Hook anchor) and `script_lint.py`. Merged metrics file kept beside the Oct 14 original.
- **Competitor script breakdown:** `Research Notes/Competitor Script Breakdown (Oct 15, 2026)/`. 26 real YouTube captions, scored against each creator's local median. New critic checklist items 8-11.
- **QA:**
  - `footage_qc.py`: blow-up from the source log, softness, duplicates across files, flashes, busy picture, internal cuts.
  - `export_check.py`: captions = script, timing, safe width, local speech-to-text vs script, timeline, clipping.
  - `qa_short.py --full` runs both.
  - Captions auto-fit at 805 px.
  - Standards: `Library/Editing and Sound Standards.md`.
- **Desktop move:** prepared, NOT done (the PC isn't reachable). `Tools/sync_verify.py` plus `DESKTOP SYNC - read on the PC.md`. Tested on a simulated desktop.
- **New draft #44** (Flagg, $8M card vs carrying bags):
  - 37/45 APPROVE, voice A, `--full` PASS.
  - In the Hub as "DRAFT awaiting your approval" (`s44-flagg-bags`).
- **The owner's watch tool:** vendored at `Tools/vendor/watch/` (scene-change frames with timestamps). Rules are in its README_METASPORTS.md.

**The owner said (Oct 15):**
- #21 Jokic is already posted. Stop work on it (`_v6` kept, unused; Hub card set to posted).
- Then: look for Shorts with a finished voice and script but no b-roll, or revise unposted ones. **Result:**
  - **#04 Giannis trade:** voice and script, no b-roll in the cloud. But the CSV says it was rendered on the PC and abandoned (stale news, trade lane underperforms). Not rebuilt; the owner's call.
  - **#02:** rejected by the owner Sep 27.
  - **#36 v2:** the only strong unposted one. Its blocker is still the fan-account rookie-LeBron clips. No official or licensed rookie-season copy was found (Commons' nearest photo is April 2005, age 20). The 2007 Duncan-hug clip stays: it's soft, but it's the real moment.
  - **#33:** a corrupt clip, an 11x-stretched clip, generic rulebook footage under named players, and a niche-player technicality premise. Not worth reviving.
  - **#28** held to December; **#26, #27, #30, #32, #37, #38** rejected or abandoned earlier.
- **ElevenLabs:** 3,548 characters left (resets Nov 8), enough for about 3 new Shorts at 2 takes each in one voice.
- **Still open:** voice A vs F; OK on #36's clips; #44 approval; the owner runs the PC sync.

## Oct 19 (late morning UTC): THE #42 FORMAT production
- **Owner rules today:** lead with THE #42 FORMAT because it works (other formats still allowed: owner correction, Oct 19); "you are able to run from my PC now" (prefer the PC when the session runs there; the cloud session saw no PC session to reach).
- **#48 Harden, most missed threes:** EDITED DRAFT, QA PASS, in both A/B voices. Awaiting the owner's OK. Slot 1 = Alex file. `UPLOAD.md` has the title, tags and pinned comment; re-check the counts on posting day.
- **#51 LeBron, most turnovers:** script FITS, fact-checked, narrated in both voices. Needs frame 1 from the PC: LeBron's inbound stolen by Giddey, Mar 27 2025, a close replay. `PACKAGE.md` has the shot list.
- **New tool `Tools/nba_videos.py`:** official NBA.com team-site clips at 720p, searchable by player/team/game/text, from the cloud. Per-play clips include misses and blocks. That's how #48 got its frame 1.
- **Hub:** #10, #36, #42, #45, #46 marked posted; #48 (ready, no video asset: storage full, the file is in the chat and repo) and #51 (blocked: footage) added.
- **Next:** the owner OKs #48; the PC grabs #51's frame 1 and edits; script B2-B5 from the story bank, each only after its frame-1 clip exists. Daily retention routine keeps running; the owner's one-time Google sign-in (Tools Guide) turns on the API pull.

## Oct 19 (afternoon UTC): two more Shorts of our own, brainstorm to render (owner: "produce 2 more shorts of your own")
- **#52 Vince Carter, most losses ever (THE #42 FORMAT):** 756 losses (most ever), Crawford 718, last game a loss but his last shot a made three, 785 wins, 22 seasons. DRAFT, QA PASS in both voices. A/B slot 2 = Designed (#51 is still blocked). `UPLOAD.md` has title, tags, pinned comment.
- **#53 Why you can't bet on the opening tip (rule/ban lane):** the AP's Oct 16 2026 memo story (no more opening-tip, miss-next-shot or low-minutes under bets; no stacked under parlays) and why: Jontay Porter (AP, Apr 2024: under three minutes on Mar 20 2024, an $80,000 bet that would have paid $1.1 million, banned for life). DRAFT, QA PASS, Alex voice. Timely: post this week. Safety: no other identifiable player sits under a betting line; the referees' names on one broadcast strip are blurred.
- **Footage:** all from official NBA.com team-site uploads via `Tools/nba_videos.py` (720p). Copy-check: both FRESH.
- **Hub:** s52 (both voices) and s53 added with covers; s51 now takes the next open A/B slot.
- **Nothing posted or scheduled.** Both wait for the owner's listen and OK.

## Oct 20 (early UTC): owner request, Knecht/Bronny Short (#58)
- **Owner:** "the lakers just picked dalton knecht over bronny james. make a short about it!" Reports say the reverse: on Oct 19 the Lakers **waived Knecht (#17 pick) and kept Bronny (#55)** (Shams via Yahoo; ClutchPoints). Built the Short on the reported facts and told the owner.
- **#58:** DRAFT, QA PASS, Alex voice, 28.4 s. Split opening (Knecht over Bronny, #17 CUT / #55 KEPT), flipped at the end. Timely: post Oct 20-21. In the Hub as s58.
- **Daily stats check (Oct 19, 23:08 UTC):** views only (retention sign-in still pending). Kerr #49 is posted (1.7K, too new).

## Oct 20: first WNBA Shorts (#59, #60), owner request
- **Owner:** "could you try making some wnba shorts? the most popular topics on youtube, reshape them into its own video."
- **What's popular (YouTube Shorts search, Oct 20):** fights/techs (Women Hooping: 3.0M, 1.4M), Caitlin Clark and Angel Reese (1.2M; Clark clips 0.6-1.0M), dunks (3.2M), pay ("PAY US WHAT YOU OWE US" 156K). Picked the two lanes we can add facts to: Clark (biggest name) and pay.
- **#59 WNBA minimum beats last year's max:** $249,244 (2025 max) vs $270,000 (2026 minimum), the March 2026 deal, cap $1.5M to $7M, Wilson reportedly $1.4M. DRAFT, QA PASS, 23.8 s.
- **#60 Caitlin Clark did what no NBA player has:** 45 and 10 in 29 minutes (Opta: first in NBA or WNBA history under 30 minutes), first WNBA 40-10, six 30-10 games vs one for anyone else, fastest to 200 threes. DRAFT, QA PASS, 28.8 s.
- **WNBA footage:** wnba.com video plays from a protected stream (not used). Official/news posts on X work: WNBA, Indiana Fever, LV Aces, NBA, NY Post, Ballislife, FOS, SI (`Tools/x_clip.py`).
- **Tool fix:** `Tools/assemble.py` now snaps each shot to the 30 fps frame grid (#60's 15 shots had drifted 0.11 s past the voice).
- **Hub:** s59, s60 added. Nothing posted.


## Oct 21 (UTC): opening night, first-to-report Shorts (#61, #62)
- **Owner:** "make sure you are up to date on all viral stories and moments of tonight, and are first to report to the most viral things."
- **#61 Paul George broke a Celtics record and lost:** 38 in his Celtics debut (most ever), Boston led by 22, Pistons won 121-113. DRAFT, QA PASS, 22.8 s. Hub s61.
- **#62 Why LeBron isn't a Knick:** MSG chanted "We don't want you" at LeBron in his Sixers debut on the Knicks' ring night; LeBron "had visions of ... finishing my career in the Garden" and Rich Paul said he'd be a Knick if New York hadn't won. Real audio of the chant and of Rich Paul (`splice_voice.py`). Sixers 106-100, LeBron 14-9-7 (ESPN box score). DRAFT, QA PASS, 31.7 s. Hub s62. Listen to the chant: speech-to-text couldn't make out the crowd.
- **Live-game method:** poll `site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=<id>` in a background loop until STATUS_FINAL; voice everything before the result first, then record only the result piece.
- **#63 All three Williamses got a technical:** Thunder at Spurs, Fox threw Holmgren to the floor; flagrant 1 on Fox, technicals on Wembanyama, Jaylin, Jalen and Kenrich Williams (ESPN play-by-play, CBS). Wemby 0-for-12 start, 1-for-13 final; Thunder 116-104, SGA 32. DRAFT, QA PASS, 28.5 s. Hub s63. Listen to the names.
- **Finding clips fast:** articles about the moment embed the X posts (`curl` the article, grep `x.com/<acct>/status/<id>`); the X profile timeline endpoint is blocked. Multi-angle replay posts (e.g. BrickCenter) give several NBC camera angles of one moment.
- Nothing posted.

## Oct 21 (afternoon UTC): deep dive on opening night + 2 new Shorts (#64, #65)
- **Owner:** "do a deep dive on the best/biggest stories of last night, then make 2 shorts for the best stories." Ranking in `Research Notes/Opening Night Deep Dive (Oct 21, 2026).md`.
- **#64 Wemby's worst shooting night (THE #42 FORMAT):** 1-for-13, career low (old low on 10+ shots 3-13 as a rookie, every ESPN game log checked); first unanimous DPOY; missed his first 12, a rookie (Aday Mara) blocked his dunk; flip: 13 rebounds, 6 blocks, 12 points from one basket. DRAFT, QA PASS, 20.3 s. Hub s64.
- **#65 LeBron answers a Knicks fan:** "Ain't nothing soft in the Midwest ... I'm from Ohio, baby," said down six; then three straight LeBron baskets in 73 s for Philly's first lead since the 1st quarter, the assist on Brown's buzzer three, 106-100. DRAFT, QA PASS, 21.6 s. Hub s65. The voice take came back 12 dB quiet and was lifted.
- **Posting overlap:** #62 and #65 are the same game (post one, or a day apart); #63 and #64 both mention 1-for-13 (hours apart).
- **New source:** ESPN game summary API `videos` (direct 720p MP4s of every ESPN game clip). vidIQ is out of credits.
- Nothing posted.

## Oct 21 (about 17:00 UTC): second QA of all drafts, duplicates removed, new posting schedule
- **Owner:**
  - "make sure video ideas arent being used multiple times: focus on making good videos over the amount"
  - "run a second qa on all shorts ... gauge which 2 to post today (right now, and 5-7pm). that will be my new schedule, edit if needed."
- **Report:** `Research Notes/Second QA and Posting Schedule (Oct 21, 2026).md`, covering:
  - every draft's QA, audio and frame check;
  - the duplicate decisions;
  - an honest viral read (nothing is certain);
  - the schedule.
- **Rebuilt:**
  - **#64 v2:** frame 1 is a close-up of Wemby's face (ESPN clip). It ends on his only basket, the alley-oop, instead of a miss. v1 is in `_v1/`.
  - **#62 v2:** "Tonight" became "On opening night" (pieces `_n1` and `_n3` re-voiced). v1 is in `_v1/`.
  - **#63 v2:** the referee's real announcement replaces the 1-for-13 (done earlier today). Its UPLOAD and notes are rewritten.
- **On hold:**
  - **#65:** taken on YouTube (Chaz NBA, 546K, with the real audio).
  - **#61:** already told by Chris Smoove (31K).
- **Schedule (Playbook updated):**
  - 2 a day: late morning ET and 5-7 PM ET (aim 6 PM).
  - Morning = the freshest game story; evening = the biggest name or an evergreen one.
  - Never two Shorts from the same game on one day.
  - Re-run the copy-check the morning of posting.
- **Hub slots:**
  - Oct 21: #1 #64 now, #2 #62 at 6 PM.
  - Oct 22: #3 #63 (morning), #4 #52 Designed voice (6 PM).
  - Oct 23: #5 #60 (morning), #6 #59 (6 PM).
  - New Hub assets for the v2 files: s64 ca68679f..., s62 cc60fe65..., s63 b08de4a3....
- Nothing posted or scheduled; all files are labelled DRAFT.

## Oct 21 (evening UTC): soccer channel started, Ahmed format learned as a skill, 2 soccer drafts
- **Owner asked for:**
  - a second YouTube channel for soccer, grown alongside MetaSports;
  - why Ahmed's network wins;
  - an exact copy of his caption and editing style, with "do not try new things";
  - a separate space and a name recommendation;
  - 2 verified Shorts to review;
  - the method learned as a SKILL that moves to another account;
  - the NBA memory refined.
- **Research:** `Research Notes/Story Format Study - Ahmed (Oct 21, 2026).md`, plus the network deep dive and the CSV data, committed earlier.
- **Soccer space:** `Soccer Channel/`, with START HERE, Playbook, Channel Setup, Idea Bank (S03-S14), Outcome Log, Lessons Learned and Research/.
  - **Name recommendation:** MetaSports FC (@MetaSportsFC), free on Oct 21.
- **Skill:** `.claude/skills/story-short/` (SKILL, FORMAT, SCRIPT, SOURCING, QA, PORTABLE), plus a zip for claude.ai: `Soccer Channel/story-short-skill.zip`.
- **Drafts (nothing posted):**
  - **S01 "Goalkeepers who hid a cheat sheet in their sock":** Lehmann, 2006, 66 s. QA PASS (full).
  - **S02 "Players who got in TROUBLE the day before a derby":** Balotelli, 2011, 64 s. QA PASS (full).
  - Each has a music and a no-music version (`DRAFT - awaiting approval - ...mp4`).
  - Footage: archive.org broadcasts (2006 shootout, 2006 all goals, BBC MOTD 2011), Mixkit stock, BBC/mancity.com screenshot cards, a recreated note labelled "recreation", and a Köpke photo (CC BY-SA, credited on screen).
- **Tools:**
  - new: `cut_list.py`, `stock.py`;
  - `broll.py --blurfit/--delogo`; `--caption-style ahmed` + `title_caption.txt`;
  - qa/footage/export story profile; music bed `eleven_story_01.mp3`.
- **NBA memory:** the Playbook has the section "Oct 21, 2026: what Ahmed's network adds"; Lessons Learned and Tools Guide are updated. THE #42 FORMAT stays RULE 1.
- **ElevenLabs:** the Creator plan fits about 1 soccer Short a day (about 3K credits each with 2 takes), plus the NBA work.

## Oct 22 (01:00-02:00 UTC): no promo, no dead air, S03, tonight's NBA tracker, a 4-day plan
- **Owner:**
  - "remove the promo at the end, that will instantly kill retention";
  - "a new youtube bio that is short and simple";
  - "make sure videos have no unnecessary pauses";
  - "1 more soccer short";
  - "track the biggest nba stories of tonight to make a short later";
  - "plan/edit for the next few days".
- **New tool, `Tools/tighten_voice.py`:** cuts silences measured on the audio itself and trims the tail to 0.25 s. `--end-after WORD` drops an outro. Originals go to `_voice_pretighten/`.
  - Soccer setting: pauses over 0.09 s cut to 0.06 s.
  - NBA setting (`--thresh 0.25 --keep 0.12`) keeps real-audio quotes natural.
  - It is in the story-short skill (step 4b) and the Tools Guide.
- **Soccer:**
  - S01: promo cut and pauses tightened, 66.1 s to 59.5 s.
  - S02: tightened, 63.7 s to 63.0 s.
  - Both QA PASS (full), with new DRAFT files and new Hub versions.
  - **S03 "Goalkeepers who danced on the line to win a final"** (Dudek, Istanbul 2005; Grobbelaar 1984): 70.7 s, 720p archive.org broadcast, sources in notes.md.
  - The skill and docs now forbid any teaser or follow ask at the end. The zip is rebuilt.
- **Bio:** "Football stories that sound fake but are 100% real. New story every day." It is in Brand Kit.md and the soccer Hub brand/kit doc (v3).
- **NBA:** #62, #63, #52 (Designed voice; the Alex alternate in `_alex/` is untouched), #60 and #59 are tightened, re-anchored, re-rendered and QA'd. The old renders are in `_pre_tight/`.
- **Tonight:**
  - The tracker (scratchpad `nba_tonight/track.py`) saves every final game summary for Oct 21.
  - A check-in is scheduled for **Oct 22 05:20 UTC** (trig_01WZV4kDusLYgUeGCrm3V5Qt) to pick the biggest story and make one THE #42 FORMAT draft.
- **Plan:** `Content Plan (Oct 22-25).md`. NBA 2 a day; soccer 1 a day at noon ET (S01 Wed, S02 Thu, S03 Fri, S04 Sat, lead idea Lewandowski's 5 goals in 9 minutes; Cantona has no archive.org footage). Hub slots are updated.
- Nothing posted or scheduled on YouTube.

## Oct 22-23: FC channel push (owner: "make at least 4 new shorts", then "finish videos" with $5 of credits left)
- **MetaSports FC tracking:** `Tools/fc_track.py` logs to `Soccer Channel/Data/fc_channel_log.csv`. Oct 22: S01 live as "The goalkeeper who hid a cheat sheet in his sock", 4,866 views, 318 likes (6.5%), 29 subs.
- **S06 Lewandowski (5 goals in 9 minutes):** finished, DRAFT files in the folder.
- **Ready to finish after the weekly reset** (voice recorded and tightened, script sourced, research in the chat summary; each needs footage cut, render and QA):
  - **S04 Zidane** "Players who got sent off in their very last game" (57.7 s).
    - ABC 720p 2006 final on archive.org (`wc-2006-final-italy-vs-france-abc-720p-60fps-hd`).
    - File times: penalty about 14:30-15:30, Zidane header about 116:05, Materazzi down 121:00, headbutt replays 123:00-123:48, referee/assistant 125:12, red card 125:36, the walk past the trophy 126:00.
    - Golden Ball card made (`assets/card_goldenball.jpg`).
  - **S05 Pickford bottle** (66.7 s).
    - 2018 Colombia v England 4K and the Euro 2020 final BBC 720p (`euro-2020-final`) on archive.org.
    - The 2026 X photos are in `assets/`. Cards made: `card_bottle.jpg` (Almada "FEEL ON THE DAY" boxed), `card_messi.jpg`.
  - **S07 Leicester 5000-1** (63.1 s). `bpl-leicester-vs-everton-2015-2016` and the MOTD 2016 highlights on archive.org.
- `Tools/story_card.py` makes stat and photo cards for the story format.
- The NBA daily stats routine is paused until the owner's credits reset (re-enable trig_01V8xJ1ZGJ5gbtAon8MCHPxy).
