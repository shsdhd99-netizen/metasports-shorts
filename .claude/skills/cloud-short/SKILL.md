---
name: cloud-short
description: >
  The whole MetaSports Short pipeline, built to run in a cloud session (Linux) from nothing to an upload-ready file:
  research fresh NBA stories with real sources, write a retention-optimised script, voice it, find and download clips (X, archive.org,
  YouTube preview frames), put the proof on the footage (words over the play, a circle on the scorebug), render the cut with
  captions and sound effects, and write the upload package (short title, optional tags, pinned comment, one cover). Use when the user types /cloud-short, or asks to make a Short, "do the
  whole process", or "make N Shorts" in the cloud. Argument: a topic, or a number of Shorts to find topics for.
---

# /cloud-short  (run from the repo root; the user is non-technical, keep chat short and plain)

NEVER upload or publish anything and never open YouTube Studio. The user posts the files. Commit and push each finished Short.
Never print, commit or ask for ELEVENLABS_API_KEY in chat. If it is missing, tell the user to add it in the cloud environment's settings.
If a site is blocked (403 from the proxy), tell the user to set the environment's network access to Full.

## 0. Setup (once per session): `bash Tools/cloud_setup.sh`
Installs python packages, makes Chromium trust the proxy certificate, copies the voice id. Checks the four sites. Then read
THE RULES at the top of `MetaSports - Playbook.md` (Oct 26 overnight review; they win over this file) and
`Research Notes/Rule Changes Applied (Oct 26, 2026).md`.

## What the data says (Round 4, `Research Notes/Round 4 - Cloud Research (Oct 3, 2026).md`; read it)
- Lanes: see the OCT 26 LANES section below (it replaces Round 4's "rules and bans first"). Contracts/trades are flat; use them only with a rule, a number gap or a funny detail as the hook.
- Titles: see section 7 (Oct 26 overnight review: a short statement; title wording is a small factor; no title scoring).
- Every Short must add original value (research, an opinion line, verified numbers), never a repeated template: YouTube's inauthentic-content policy.
- Optional visual flag: `--auto-zoom 0.06`. NO `--hook-text` headline (user removed it Oct 4 2026): the first 3 seconds are carried by the real image + the spoken/captioned hook line.

Round 6 (`Research Notes/Round 6 - What Makes Shorts Go Viral (Oct 4, 2026).md`) contradicted or found unsupported: name/number-first titles, 18-35 s length, avg shot <=1.9 s, never-over-3-s shots, 6-11 AM posting, 3 covers. Where this file still says otherwise, Round 6 wins. Comments do not drive reach (do not over-invest in pinned comments); keep Shorts under 60 s (copyright-claim rule unresolved).

FIRST read `CLOUD STATE - read this first.md` in the repo root (current status, Hub, rules) and update it at the end of your work.

Before anything else, read `Research Notes/Lessons Learned (running log).md` and add to it whenever you learn something.

## OCT 26 LANES (Oct 26 overnight review; THE RULES §1 in the Playbook)
- **Moments: about half of NBA Shorts.** A funny, odd or skilful thing you can watch: game, bench, warm-up, fan, kid, mascot, broadcast desk. Narrate who, what, and the reaction or payoff. [S] `Research Notes/Similar Channels (Oct 26, 2026).md` §4; Swishyyy's moments get about 1.8x its explainers. Ours is untested.
- **Each moment needs one fact the clip can't show** (who, why, a number). [V official] YouTube cuts reach for narration that only describes the screen (`Research Notes/Shorts Mechanics and Policy (Oct 24, 2026).md` finding 3).
- **The other half rotates:** the star paradox (THE #42 FORMAT, one lane now, not the lead: its test ended 1 of 3 at 74%+ [V]); same-day news (or not at all; it goes up the morning after the game); and a **weekly countdown test**, "3 times [star] did X", with a visible #3 / #2 / #1 corner badge (`Tools/overlay.py` `"x": "left"` and `"box": "0xFDB927"`) and the best one last [H].
- **Review the split after 10 moment posts** (stayed % and 72 h views vs the channel median).
- Footage from the league, teams and broadcasters. Never another creator's edit or a reel as the base.
- Copy-check against Swishyyy's titles too (`Research Notes/Swishyyy Shorts (Oct 26, 2026).csv`).

## OCT 26 EDITING RULES (Oct 26 overnight review; they override anything older below)
Sources: `Research Notes/Retention and Editing Upgrade (Oct 26, 2026).md` (RET) and `Research Notes/Why NBA Views Dropped (Oct 26, 2026).md` (WHY), 37 posted NBA Shorts. Only 13 of 40 new-era Shorts held the 74% "stayed to watch" that every 10K+ Short had.
1. **Footage first.** Before writing, secure frame 1 and one clip that proves each beat, from any number of sources. Never cut away to filler to reach a clip count. [S] WHY §3.
2. **Frame 1 shows the thing line 1 is about, happening.** Sharp and lit; a face or an action, whichever proves line 1. [S] RET §2b.
3. **Line 1 is 11 words or fewer**, done by about 3 s. 11 or fewer: 72.6% stayed vs 62.2% [V] RET §1b.
4. **Hold the opening moment.** Shot 1 at least 2.0 s. At most 2 shots in the first 3 s and at most 3 in the first 5 s. No cut inside line 1. 3 or fewer in 5 s: 78.4% vs 66.5% (p=0.002) [V] RET §1b.
5. **About 10-15 shots of about 2 s;** a play may run 3-5 s. 15 or fewer: 75.0% / 6.1K vs 66.4% / 3.1K [V] WHY §2.
6. **Replay the key second once, before the payoff:** closer and/or at 0.5x. In `cuts_plan.json` give the replay shot the same `src`/`at` with `"speed": 0.5` and/or `"zoom": 1.3` (or `"shot_zoom"`), plus `"replay": true`; `cut_list.py` passes `"replay": true` into shots.json, so QA doesn't warn about the repeat. [S] RET §4 change 2; untested for us.
7. **Fill the frame.** Crop wide plays to about 3:4: `broll.py cut ... --blurfit --blurfit-aspect 0.75 --x <pos>` (cuts plan: `"blurfit": true, "blurfit_aspect": 0.75`). Never a full-width 16:9 strip over blur for a play. Full-width blur-fit only for a graphic or text that must be read whole. [S] RET §2b: 0 of 55 winners used a full-width strip.
8. **Proof on the footage, never on a card.** Words over the play (`overlay` in the cuts plan, `Tools/overlay.py`), the broadcast's own scorebug, a red circle (`broll.py circle`, `Tools/pointer.py`). Owner, Oct 26: "cut cards completely". A card only when nothing else can show the fact: 1.5 s at most, never in the first 4 s (QA FAILs both). Any card: 66.1% vs none 72.6% [V] WHY §2.
9. **No emoji stickers.** [S] RET §2b.
10. **No forced loop.** End on the payoff. Loop into frame 1 only when that image is the payoff. [S] RET §1b.
- Pace, word count and how many numbers are spoken showed no link [V] WHY §2.
- Music bed: untested (every new-era NBA Short had none). The owner decides on an A/B.
- **Removed (Oct 26 overnight review):** "3+ cuts in the first 3 s", "a new image every second", "avg shot 1.4-1.9 s", "no shot over 3 s", "evidence cards for any fact line", "6+ source clips / at most 35% per clip".

## THE QUALITY FORMULA (mandatory, every Short; the user should never have to ask)
A Short that is one talking head, text cards or repeated footage gets swiped (this happened to #15 v1). Build every Short to this recipe:
1. **Footage first (Oct 26 overnight review).** Before writing, secure frame 1 and one clip that proves each beat, from any number of sources (X posts, official reveal videos, team sites, archive.org). No frame 1, no script: change the angle or park it. Never cut away to filler to reach a clip count.
2. **Hook = frame 1 showing what line 1 is about, happening, plus line 1 of 11 words or fewer** (Oct 26 overnight review). Shot 1 holds at least 2.0 s; at most 2 shots in the first 3 s and 3 in the first 5 s. NO big headline text: the user removed the hook headline on Oct 4 2026 (captions only). `assemble.py` ignores `--hook-text` unless env ALLOW_HOOK_TEXT=1; do not use it.
3. **Recipe per 23-30 s:** ~40% b-roll that shows the story (`kind: action`), <=45% talking head or quote (`face`/`quote`), no cards (Oct 26), avg shot about 2 s (1.8-3.0).
4. **Real quotes in short bursts** (<=4 s) cut in with `Tools/splice_voice.py` (real audio + our narration), never a long raw interview. Cut to b-roll on the narration between quotes.
5. **No cards (Oct 26).** Proof sits on the footage: words over the play, the scorebug, a red circle. A card only when no footage can carry the fact, never in the first 4 s.
6. **Every shot in shots.json has `"kind": face|quote|action|card`.** Ends on the PAYOFF image that answers the first line. No forced loop: loop into frame 1 only when that image is the payoff; never add a shot just to loop (Oct 26 overnight review). The debate question goes in the pinned comment (Oct 13: our question/CTA endings stayed under 3K).
7. **Oct 13 gates (Playbook "Strict Short Formula", `Research Notes/Winning Formula v2`):** screen the premise first (one visible object + one idea a non-fan gets in second 1; never a bigger channel's story); no card in the first 4 s; every clip at least as long as its shot (`qa_short.py` fails a clip that runs short; a deliberate replay is a separate shot marked `"replay": true`); review the export with an independent agent using `Tools/critic_v2.md`. Script critics are advice, not gates: the old 0-100 craft score predicted views backwards, and Script Critic v3 blocks only on factual accuracy (Oct 26 overnight review).
7. **Gate:** `python Tools/qa_short.py --folder "<folder>"` must print PASS before delivery. FIX lines mean go back and get more footage. Then look at storyboard.jpg and the first-3-seconds frames.
Order: research -> frame 1 + a proof clip per beat -> script -> voice (`voiceover.py` per piece, `splice_voice.py` for quotes) -> shots.json with kinds -> assemble -> qa_short PASS -> package.

### Evidence-backed rules from Round 5 (`Research Notes/Round 5 - Competitor Formulas (Oct 4, 2026).md`; evidence tier in brackets)
- **Lanes: the OCT 26 LANES section above replaces the Oct 24 "1 post in 3 per lane" split** (Oct 26 overnight review: moments about half; the star paradox, same-day news and a weekly countdown rotate). Still true: retire a lane after 3 posts in a row below the channel median; templates decay (Korzemba 23M to 8K, REBOUND 42M to 184K, our #42 format 86.9 > 83.3 > 72.6 > 59.1% stayed); evergreen superstar history is a fallback when no moment or news exists (Rebound Rewind evergreen 245K vs news 133.5K). **Rules: visible rule-breaking only** (caught/banned/illegal: 1.42x the channel norm, n=79, 13 channels); **no paperwork rules** (bets, schedules, votes, stat credit: our weakest lane, 2.0K median, n=6) unless a superstar and a hard paradox carry it. Old lane rule ("rule/ban 2.5x, n=26") is outdated.
- [PROVEN] Write the concept in 8 words or fewer; a stranger must get it in one second. Put `Lane:`, `Concept:` and `Added value:` (opinion line or verified number) in notes.md with a source URL per number (inauthentic-content policy).
- [PROVEN] Story length 21+ s (CoachClank: 21 s+ got 848K vs 291K for 20 s or less). Frame 1 shows what line 1 is about, happening (Oct 26 overnight review; the feed shows no thumbnails, so do not over-invest in covers).
- [SUPPORTED] Speech 240-290 wpm; end on the payoff with no "subscribe/follow/like" outro; last word ends 0.15-0.4 s before the end; a turn word (But/Until/Now) in the first 40%. (The "last line echoes the first (loop)" rule was removed in the Oct 26 overnight review: no forced loop.)
- [SUPPORTED] Captions: sentence case, 64 px+, centred 45-62% of height, 3-4 words, none on screen over 1.7 s. The winners (Clank, Ahmed's, REBOUND) do this; our ALL CAPS red/green is the user's house style, so test `--caption-style karaoke` against it, do not switch everything.
- [HYPOTHESIS, A/B first] One accent colour; search keyword in the first 15 words; named series. (Title-wording tests and the 1.9 vs 2.8 s average-shot test were closed in the Oct 26 overnight review: title wording is a small factor [V] `Research Notes/Similar Channels (Oct 26, 2026).md` §1; about 2 s shots held better [V] WHY §2.)
- Tools/qa_short.py now fails on hard gates and prints `warn` lines for the SUPPORTED/HYPOTHESIS items. Treat warns as things to fix when cheap and to log in the A/B table.
- Every rule we add must carry its evidence tier and a source; if evidence is missing, call it HYPOTHESIS and put it on the A/B list.

### Round 7 retention findings (`Research Notes/Round 7 - Viewer Retention Deep Dive (Oct 4, 2026).md`; read its evidence labels)
- Funnel: shown in feed -> Viewed vs swiped -> engaged view -> average view duration / % viewed -> retention curve. A public view counts at first play, so judge by Viewed % and engaged views, not view count. APV over 100% = replayed watch time (YouTube has not said it earns extra reach).
- Most short-video sessions end early (about 70% before 20% of the video in one Shorts test): the first 3 s are the whole game; later drops are patched with a new fact or image every 3-4 s, not just fast cuts (fast cutting has no direct evidence).
- Our voice and captions run ~21-24 characters per second against Netflix's 20; keep captions to one line of 2-4 words, <= ~22 chars/s, speech 230-270 wpm.
- Real quote bursts (a new voice) re-trigger attention; keep 2-3 per Short; vary sound effects (2-5), do not repeat the same one.
- Our channel's NBA-era Shorts plateau at 20-45K views (46 of 60): likely a fixed test audience; we have no retention data. Ask the user for Studio exports per Short (Viewed %, avg % viewed, retention points) and fill `Research Notes/Outcome Log.md`.
- Critic verdicts: `Research Notes/Critique Round 1 - Verdicts.md` (one Short per story family per week; check the shot under every spoken name; notes.md with claim -> exact source; quotes at -16 LUFS; pad 0.3 s tail).

## STORY STANDARD (user, Oct 4: every story must have high retention and a real payoff; modelled on the Wembanyama Short that got 79.5% stayed / 100.3% avg viewed)
Shape (22-30 s, 90-120 words at 230-270 wpm): 1) tension hook, line 1 of 11 words or fewer (a universal rule, a surprising number or a conflict; never a flat recap) -> 2) the turn ("Until X", "But") -> 3) escalation: at least two beats where the stakes or the weirdness go UP ("But that's not even the crazy part") -> 4) the PAYOFF: the reveal/list/number the hook promised, with the key second replayed just before it -> 5) END ON THE PAYOFF line. No closing question, no forced loop (Oct 26 overnight review).
Scorecard (advice, not a gate since the Oct 26 overnight review; only the fact checks block; see `Research Notes/Critique Round 2*`): hook tension, promise vs delivery, turn in the first 40%, 2+ escalation beats, payoff clear, ends on payoff, no padding (every sentence adds a new fact), longest stretch without a new fact or image <= 3-4 s, footage matches every spoken name/number, claims sourced.
Pin shots to words: put `"anchor": "first words of the phrase"` on shots in shots.json and run `python Tools/anchor_shots.py --folder <folder>`; it sets every start from words.json and prints a table of the words spoken under each shot (check that a named person is on screen while the name is spoken). After a script rewrite re-run it instead of hand-retiming.

## 1. Research (this is where views come from; do real research, never invent)
- `python Tools/fresh_moments.py` for what is hot. Use WebSearch for the last 7 days: "NBA <player/team> <week>", media day, training camp,
  rule changes, contracts, records. Prefer stories with a number, a rule, a petty detail or a "that would not be allowed now" angle.
- **Research tools (Oct 26 overnight review):** `python Tools/yt_watch.py <link or id>` has Gemini watch a Short (a competitor's, or our
  own draft) and writes a scene-by-scene report to `Research Notes/Watch Reports/` (`--channel @handle --top 5` for a channel's best).
  It needs a free `GEMINI_API_KEY` in the environment settings; never ask for it in chat. Tier its numbers [S]. The channels we watch
  are in `Research Notes/Competitor Watchlist.csv` (the daily research task reads it).
- **Read the source itself**, not the snippet: ESPN/NBA.com/local papers open with `curl -sL -A "Mozilla/5.0" <url>` then strip tags (WebFetch and the
  Parallel tool are often blocked or rate-limited). For X posts, `curl "https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a"` returns the full text.
  Reporter tweets (Shams, Scotto) are the newest truth; when two sources disagree, say so in notes.md and use the safer wording ("reportedly").
- Copy-check: `python Tools/copy_check.py "<4-6 word topic>"`. TAKEN means skip. Never retell a bigger channel's story.
- Pick the angle with a built-in argument (win-or-lose, then-vs-now, rule-vs-legend). Keep a facts list with a source URL for every number.

## 2. Script (retention rules; Shorts live or die on "stayed to watch": aim for 74%+, judged at 72 h)
- 23-40 s (CoachClank's 31-45 s Shorts did best; Round 6), 95-150 words. Line 1 is 11 words or fewer and carries the scene, the name or the stakes (Oct 26 overnight review). No throat-clearing, no "did you know".
- Turn ("You see" / "But") inside the first third; a second re-hook ("But here's the twist") around 45%.
- Short sentences, one idea each; about one shot every 2 s, and a play may run 3-5 s (Oct 26 overnight review).
- End on the payoff that answers the opening line (one number or the subject's own words), then stop; it can be argued with, but it must not be a question (Oct 13 evidence).
- Spell numbers the voice might misread as `{$200 million|two hundred million dollars}`; hard names `{Maxey|Max-ee}`.
- Save `Productions/MetaSports/<date> NN <Title>/script.txt` (ONLY the spoken words, one paragraph) and `notes.md` (facts with links, titles, pin, warnings).

### The first 3 seconds decide everything (apply to every Short; viewers swipe in 1-3 s)
- **Line 1 is one claim about the name or the moment, 11 words or fewer, done by about 3 s** (Oct 26 overnight review) [V] RET §1b. Never a bare number first. Never open on "So" / "Did you know" / a setup sentence.
- **Frame 1 shows the thing line 1 is about, happening** (Oct 26 overnight review): real action or a close face, whichever proves line 1; never a title card, logo or a still. A push-in only on a static first shot: 2-5%, at most 4% a second (`footage_qc.py` warns above it).
- **Hold the opening moment (Oct 26 overnight review):** shot 1 at least 2.0 s; at most 2 shots in the first 3 s and 3 in the first 5 s; no cut inside line 1; then about one shot every 2 s; let a play run. Hook shots are real footage of the named player/moment; no cards.
- **No sound in the first second.** Voice only. Do not put `boom` at 0.0. That vine-boom open was on almost every Short and Round 7 says the same effect habituates. `assemble.py` drops anything before 1.0 s, drops a repeated file, drops two effects closer than 1.5 s, and refuses a gain louder than `Tools/sfx/catalog.json`.
- **Four effects when the pictures support them, never more than five, each one a different file.** Use the catalog gain. Never `falling`. Match the picture: `swish`/`rim`/`brick` only on a shot you can see, `whistle` on a whistle, `horn` on a buzzer, `dribble` on a dribble close-up, `whoosh` on a fast push-in, `whoosh_long` into the payoff, `boom_cinematic` once on the one reveal (not at 0), `boom` at most once on a stat (gain -18, after 1 s), `camera` on a presser or jersey, `click` only when a screenshot appears, `ding` once on one fact, `cha_ching` only on a salary graphic, `punch` on a hit you see, `ankle_breaker` only on a real crossover, `thud` on a fall. If the picture does not show it, leave it out.
- Sports editors use a whoosh on a zoom and a swish on a made basket, and they take effects back out on the listen-through. Vine boom, record scratch and sad violin are the sounds people now skip. Those files are not in `Tools/sfx`. Do not add them.
- The line after the hook must be a payoff promise or a turn ("and it might be the smartest move of his career"), not background.
- Check: extract frames at 0.05, 0.6, 1.1, 1.5, 2.1, 2.8, 3.5, 4.4 s with ffmpeg and look at them side by side. If frame 1 doesn't show the claim, change the shot, not the cut rate (Oct 26 overnight review).
- After posting, judge "Stayed to watch" at 72 h, not the next morning (Oct 26 overnight review; [V] `Research Notes/Posting Study (Oct 26, 2026).md` §1g): 74%+ is good; under 60% means the next Short needs a new first 2 seconds. Never re-upload the same Short.

## 3. Voice (pipeline v2, Oct 5 2026; the user said the voice had started to glitch). Evidence: `Research Notes/Voice Investigation (Oct 5, 2026).md`
Use `. key.sh && python Tools/voice_take.py --script "<folder>/script.txt" [--takes 3]` (NOT bare voiceover.py): it records, checks (free local speech recognition + voice-quality numbers) and re-records only when the check fails. Spliced Short: run it for every `_nN/script.txt` (add `-- --prev-text "..." --next-text "..."` with the neighbouring words so tone stays continuous), then `splice_voice.py`. Re-doing an existing Short: `python Tools/revoice.py --folder "<folder>"` (backs up, re-records, re-times pictures with anchor_shots, re-renders, QA).
Why: the voice is a CLONE ('pham v2'); the old settings (stability 0.45, similarity 0.8, speed 1.1, then atempo up to x1.6) gave the lowest voice-quality numbers and every time-stretch lowers quality (HNR -0.5 to -1.1 dB at x1.2-1.4; rubberband is worse than atempo). New defaults: stability 0.65, similarity 0.7, native speed auto (1.2/1.15/1.1: about 268/238/210 wpm), stretch capped at x1.08. splice_voice uses a plain measured gain (loudnorm ducked sentence ends by 1-4 dB). voiceover always pads 0.3 s of silence.
Quality gate for a take: voice_check has no REDO issue (every word said; numbers written differently are ignored; names may differ), HNR >= 7.6, jitter <= 3.4, shimmer <= 11.5 (this voice measures HNR 8-10). Take-to-take variation is about +-0.7 dB HNR, so a failing take is worth one more try (max 3 takes: credits are ~1 per character, plan Starter 90,000/month). Oct 24 2026: a failed take with 1-2 located word issues is fixed by `Tools/retake_sentence.py` (~5-10% of a full take's credits; voice_take.py tries it before a new take): it re-records only that sentence with the neighbours as previous/next text and splices it in.
Gives voice.mp3, words.json (word times) and captions.srt. All shot timing comes from words.json.
**Then take out the dead air (owner, Oct 22: "no unnecessary pauses"):** `python Tools/tighten_voice.py --folder <folder> --thresh 0.25 --keep 0.12` (before anchoring the shots). No outro or promo after the payoff, ever. Old takes are kept in `_voice_prev/` or `_voice_v1/`.

## 4. Footage (YouTube downloads are blocked from the cloud; use these instead, in this order)
1. **X posts** from official accounts (NBA, team accounts, ESPN, ClutchPoints; House of Highlights only for the broadcast part, cropped, when the league hasn't posted the moment): find them with
   `WebSearch "x.com <account> <moment> video"` (allowed_domains x.com), then `python Tools/x_clip.py <links...> --out src`. 720p-1080p, 10-130 s.
   Look at them with `python Tools/broll.py sheet src/<id>.mp4 --from 0 --to 30 --every 1 --out s.jpg`, cut with `broll.py cut src/<id>.mp4 --at T --len L --x 0.5 --out clips/V01.mp4`.
2. **archive.org** for old games (`https://archive.org/advancedsearch.php?q=title:(...)&output=json`, then ffmpeg `-ss` straight off the file URL). 480p: use blur-fit, not a hard crop, with `--blurfit-aspect 0.75` so the play still fills the frame.
3. **YouTube moments**: `python Tools/yt_sheet.py <id> --from 0 --to 120 --every 2 --out s.jpg` shows the video's own preview frames with timestamps (no download).
   Find ids with `python Tools/broll.py search "<query>"`. Write `<folder>/clips_manifest.json` ([{"file","video","at","len","x"}]) and the user (or the PC) runs `python Tools/pc_cut.py --folder "<folder>"`.
Quality bar: every shot matches its spoken line; check each player's identity frame by frame (preview frames are too small to prove a face: say "verify" in the plan).
**Framing (Oct 26 overnight review):** fill the frame. Wide plays get `--blurfit --blurfit-aspect 0.75 --x <pos>` (a 3:4 window, 1080x1440 over blur) or a full-frame crop; never a full-width 16:9 strip over blur. Full-width blur-fit only for a graphic or text that must be read whole.

## 5. Proof on the footage (Oct 26 overnight review: no cards)
- Numbers and short facts go over the play: `"overlay": [{"text": "50.7%", "size": 190, "y": 300, "start": 0, "end": 1.5}]` in the cuts plan (`Tools/overlay.py`). Keep text above y=1000 or below y=1300 (the caption band).
- Circle the broadcast's own scorebug, clock or score: `broll.py circle clips/A1.mp4 --at 0.62,0.88 --out clips/A1c.mp4`.
- Countdown badge (weekly countdown test): `{"text": "#3", "size": 120, "x": "left", "y": 230, "box": "0xFDB927", "color": "black", "start": 0, "end": 9}`.
- No emoji stickers.
- **A card only when nothing else can show the fact** (owner, Oct 26: "cut cards completely ... if added, keep brief"): 1.5 s at most, never in the first 4 s (QA FAILs both).
  `python Tools/card.py --url <article> --mark "<exact words>" --headline y0,y1 --byline y0,y1 --out "<folder>/clips/c01.mp4" --len 1.5`
  Look at the card PNG before using it. Article screenshots are for checking facts, not for the video.

## 6. Cut: write `shots.json` ([{"clip","start"}] with start = the word's time in words.json; or a `cuts_plan.json` for `cut_list.py`, where `"replay": true`, `"speed"`, `"blurfit_aspect"` and `"overlay"` pass through) and `sfx.json` (4 effects from `Tools/sfx` when the pictures support them, else 3, never more than 5; catalog gains; none before 1.0 s; no file twice; none within 1.5 s; each one matches a picture or one spoken beat),
then `python Tools/assemble.py --folder "<folder>" [--caption-style clank|metasports]`. No Drift on Linux, so the ffmpeg engine runs. Output final.mp4 (-14 LUFS), preview_1-3.jpg, storyboard.jpg.
**Look at storyboard.jpg card by card** before delivering. Copy to `READY TO POST - <Title> (Claude cut).mp4`.

## 7. Upload package (`UPLOAD.md`, template: `Productions/MetaSports/2026-09-28 01 Why LeBron Took a 92 Pay Cut/_claude_v4/UPLOAD.md`)
Rules: Oct 26 overnight review ([V] `Research Notes/Posting Study (Oct 26, 2026).md`; [V] `Research Notes/Similar Channels (Oct 26, 2026).md` §1).
- **Title:** 3 options, each a short statement pointing at the moment or the claim ("He Pretended To Be Klay Thompson"); true to the video. Title wording is a small factor: don't score titles and don't gate on them. No hashtag or one (#nba). No ALL-CAPS words.
- **Description:** leave it empty.
- **Tags (optional):** 3-8 relevant tags, about 100-150 characters: the names, the team, the event, common misspellings. Never fill the 500 characters. Check with `python Tools/tags_fit.py --cap 150 "tag1, tag2, ..."`.
- **Pinned comment:** the two-sided argument.
- **Cover:** one, `python Tools/thumb.py --shape short` (keep the face visible; single quotes around text with $). The feed shows no custom thumbnails: 5 minutes at most.
- **Slot:** `UPLOAD SCHEDULE.md` (NBA 11 AM ET; news the morning after the game). Write down the go-live time. Judge at 72 h.

## 7b. Add it to the phone app (the user is often on mobile)
The user's Shorts Hub is a claude.ai artifact: https://claude.ai/artifact/EZrk8n855PyYpMFnMnMJd4 (database collection `shorts`, one doc per Short).
1. Make a 720p preview: `ffmpeg -i final.mp4 -c:v libx264 -crf 25 -preset veryfast -vf scale=720:-2 -c:a aac -b:a 128k -movflags +faststart prev.mp4` (about 4 MB).
2. Upload it: `Artifact` tool, `url` = the hub URL, `asset: true`, `file_path` = prev.mp4. The result gives an asset id.
3. Write the doc with the `ArtifactData` tool (action `set`, collection `shorts`, doc_id like `s14-topic`): `{num, name, title, status: "ready"|"footage"|"posted", versions:[{label, assetId, note}], covers:[{label, assetId}], titles:[...], tags, pinned, postNote} (no description). Upload full 1080p (under 20 MB each; re-encode with -crf 24 if larger) so the app's Download button gives the real file. Ideas go in collection `ideas` ({rank, name, lane, checked, title, hook, facts, footage, pinned})`. For a Short still waiting on footage use status `footage` and `about` instead of versions; later `update` it to `ready` with the video.
4. Never delete other docs. The page updates live; no republish needed.

## 8. Deliver: commit + push to the session branch (Productions/** is allow-listed in .gitignore for READY TO POST files and _claude_v4), send the mp4 + cover + UPLOAD.md to the user with SendUserFile.
Report in 3-4 plain lines: what is finished, what is still missing (and why), the title pick.

## Known cloud limits
- YouTube video downloads: blocked (bot check). Preview frames and search still work.
- `Tools/.env` holds only the voice id; the key lives in the environment's settings. After a key is pasted in chat by mistake, tell the user to rotate it.
- Free alternatives to vidIQ: yt-dlp metadata (views, dates, channel stats via `channel_check.py`), `fresh_moments.py`, `copy_check.py`, Google Trends, YouTube Studio's own Research tab.
