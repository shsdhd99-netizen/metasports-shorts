---
name: cloud-short
description: >
  The whole MetaSports Short pipeline, built to run in a cloud session (Linux) from nothing to an upload-ready file:
  research fresh NBA stories with real sources, write a retention-optimised script, voice it, find and download clips (X, archive.org,
  YouTube preview frames), build screenshot evidence cards, render the cut with captions and sound effects, and write the upload
  package (SEO title, description, pinned comment, covers). Use when the user types /cloud-short, or asks to make a Short, "do the
  whole process", or "make N Shorts" in the cloud. Argument: a topic, or a number of Shorts to find topics for.
---

# /cloud-short  (run from the repo root; the user is non-technical, keep chat short and plain)

NEVER upload or publish anything and never open YouTube Studio. The user posts the files. Commit and push each finished Short.
Never print, commit or ask for ELEVENLABS_API_KEY in chat. If it is missing, tell the user to add it in the cloud environment's settings.
If a site is blocked (403 from the proxy), tell the user to set the environment's network access to Full.

## 0. Setup (once per session): `bash Tools/cloud_setup.sh`
Installs python packages, makes Chromium trust the proxy certificate, copies the voice id. Checks the four sites. Then read
`MetaSports - Playbook.md`, `Tools/data/title_patterns.md`, `Research Notes/Round 3 - Deeper Findings.md` (they win over this file).

## What the data says (Round 4, `Research Notes/Round 4 - Cloud Research (Oct 3, 2026).md`; read it)
- Best lane: **rules, bans, 'caught'/referee stories and one-second oddities** (REBOUND's rule/ban Shorts median 7.7M vs 775K overall). Contracts/trades are flat; use them only with a rule, a number gap or a funny detail as the hook.
- Titles 5-7 words, one emoji at the end. Avoid 🤔 (worst in the data); prefer 😳 💀 😭. Start with Why/How/What/Did/Is or "He ...".
- Every Short must add original value (research, an opinion line, verified numbers), never a repeated template: YouTube's inauthentic-content policy.
- Optional visual flags: `--hook-text "NUMBER|HOOK?"` (headline over the first 2 s) and `--auto-zoom 0.06`; A/B them, don't assume.

Round 6 (`Research Notes/Round 6 - What Makes Shorts Go Viral (Oct 4, 2026).md`) contradicted or found unsupported: name/number-first titles, 18-35 s length, avg shot <=1.9 s, never-over-3-s shots, 6-11 AM posting, 3 covers. Where this file still says otherwise, Round 6 wins. Comments do not drive reach (do not over-invest in pinned comments); keep Shorts under 60 s (copyright-claim rule unresolved).

FIRST read `CLOUD STATE - read this first.md` in the repo root (current status, Hub, rules) and update it at the end of your work.

Before anything else, read `Research Notes/Lessons Learned (running log).md` and add to it whenever you learn something.

## THE QUALITY FORMULA (mandatory, every Short; the user should never have to ask)
A Short that is one talking head, text cards or repeated footage gets swiped (this happened to #15 v1). Build every Short to this recipe:
1. **Story first, footage second.** Before writing, find 6+ different real clips (X posts, official reveal videos, archive.org). If a topic has under 6, find a fresher angle (e.g. #15 got better when the Heat x GTA night was found) or drop it.
2. **Hook = a striking real image + a name/number line at 0.0 s**, 3+ cuts in the first 3 s, headline text (`--hook-text`, two short lines, each under 14 characters).
3. **Recipe per 23-30 s:** ~40% b-roll that shows the story (`kind: action`), <=45% talking head or quote (`face`/`quote`), <=25% cards, avg shot 1.4-1.9 s, no clip over 35%.
4. **Real quotes in short bursts** (<=4 s) cut in with `Tools/splice_voice.py` (real audio + our narration), never a long raw interview. Cut to b-roll on the narration between quotes.
5. **Cards only for proof**, <=2 s, only if the card is visually rich (headline + image). Dull white-page cards get replaced with b-roll.
6. **Every shot in shots.json has `"kind": face|quote|action|card`.** Last shot reuses the first clip (loop). Ends on a question.
7. **Gate:** `python Tools/qa_short.py --folder "<folder>"` must print PASS before delivery. FIX lines mean go back and get more footage. Then look at storyboard.jpg and the first-3-seconds frames.
Order: research -> find 6+ clips -> script around the clips -> voice (`voiceover.py` per piece, `splice_voice.py` for quotes) -> shots.json with kinds -> assemble -> qa_short PASS -> package.

### Evidence-backed rules from Round 5 (`Research Notes/Round 5 - Competitor Formulas (Oct 4, 2026).md`; evidence tier in brackets)
- [PROVEN] Lane: rule/ban/"caught", size/skill spectacle, one-second oddity or petty/funny player moment. Contract/trade/wholesome stories only with a rule or number gap as the hook. (rule/ban titles got 2.5x the channel median, n=26)
- [PROVEN] Write the concept in 8 words or fewer; a stranger must get it in one second. Put `Lane:`, `Concept:` and `Added value:` (opinion line or verified number) in notes.md with a source URL per number (inauthentic-content policy).
- [PROVEN] Story length 21+ s (CoachClank: 21 s+ got 848K vs 291K for 20 s or less). Frame 0 must be a face or moving action (the Shorts feed shows no thumbnails; do not over-invest in covers).
- [SUPPORTED] Speech 240-290 wpm; end on the payoff with no "subscribe/follow/like" outro; last word ends 0.15-0.4 s before the end and the last line echoes the first (loop); a turn word (But/Until/Now) in the first 40%.
- [SUPPORTED] Captions: sentence case, 64 px+, centred 45-62% of height, 3-4 words, none on screen over 1.7 s. The winners (Clank, Ahmed's, REBOUND) do this; our ALL CAPS red/green is the user's house style, so test `--caption-style karaoke` against it, do not switch everything.
- [HYPOTHESIS, A/B first] Title opening on an action/claim word (Why/How/He/Did) instead of a name (Clank name-first 237K vs 494K, n=20); average shot 1.9 vs 2.8 s (no evidence that faster is better; Clank's biggest cut every 2-4.7 s); one accent colour; search keyword in the first 15 words; named series.
- Tools/qa_short.py now fails on hard gates and prints `warn` lines for the SUPPORTED/HYPOTHESIS items. Treat warns as things to fix when cheap and to log in the A/B table.
- Every rule we add must carry its evidence tier and a source; if evidence is missing, call it HYPOTHESIS and put it on the A/B list.

## 1. Research (this is where views come from; do real research, never invent)
- `python Tools/fresh_moments.py` for what is hot. Use WebSearch for the last 7 days: "NBA <player/team> <week>", media day, training camp,
  rule changes, contracts, records. Prefer stories with a number, a rule, a petty detail or a "that would not be allowed now" angle.
- **Read the source itself**, not the snippet: ESPN/NBA.com/local papers open with `curl -sL -A "Mozilla/5.0" <url>` then strip tags (WebFetch and the
  Parallel tool are often blocked or rate-limited). For X posts, `curl "https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a"` returns the full text.
  Reporter tweets (Shams, Scotto) are the newest truth; when two sources disagree, say so in notes.md and use the safer wording ("reportedly").
- Copy-check: `python Tools/copy_check.py "<4-6 word topic>"`. TAKEN means skip. Never retell a bigger channel's story.
- Pick the angle with a built-in argument (win-or-lose, then-vs-now, rule-vs-legend). Keep a facts list with a source URL for every number.

## 2. Script (retention rules; Shorts live or die on "viewed vs swiped away", aim 70%+ at 3 s)
- 23-40 s (CoachClank's 31-45 s Shorts did best; Round 6), 95-150 words. First 6 words carry the scene, the number or the stakes. No throat-clearing, no "did you know".
- Turn ("You see" / "But") inside the first third; a second re-hook ("But here's the twist") around 45%.
- Short sentences, one idea each, so each can be a new shot every 1.5-3 s (no evidence that faster than ~2 s helps; test it).
- End on a two-sided argument the comments will fight over, then stop. A last line that echoes the first helps the loop.
- Spell numbers the voice might misread as `{$200 million|two hundred million dollars}`; hard names `{Maxey|Max-ee}`.
- Save `Productions/MetaSports/<date> NN <Title>/script.txt` (ONLY the spoken words, one paragraph) and `notes.md` (facts with links, titles, pin, warnings).

### The first 3 seconds decide everything (apply to every Short; viewers swipe in 1-3 s)
- **The number, name or stakes is the FIRST word**, spoken and on screen at 0.0 s ("92% pay cut. LeBron James just took one..."). Never open on "So" / "Did you know" / a setup sentence.
- **Frame 1 is already moving or already a face**: real action or a close face, never a title card, logo or a still. Punch in: put `"zoom": 0.12` on the first shot in shots.json (slow push 100% to 112%).
- **A new image about every second until 5 s** (cut, push-in or card), then every 1.5-2.5 s. Hook shots are real footage of the named player/moment; save screenshot cards for the fact lines after 4 s.
- **A sound on the hook word**: one `boom` (gain -12) at 0.0 on the number. Whoosh only for a jump to a card.
- The line after the hook must be a payoff promise or a turn ("and it might be the smartest move of his career"), not background.
- Check: extract frames at 0.05, 0.6, 1.1, 1.5, 2.1, 2.8, 3.5, 4.4 s with ffmpeg and look at them side by side. If two neighbours look alike, add a cut.
- After posting, read YouTube Studio's "Viewed vs Swiped Away" at 24 h: 70%+ is good, under 60% means rewrite the first 2 seconds.

## 3. Voice: `python Tools/voiceover.py --script "<folder>/script.txt"` then `python Tools/voice_check.py --folder "<folder>"`.
Same ElevenLabs voice always. Spoken-out numbers ("fifty-two million dollars") are false alarms for the checker; redo only clearly bad takes.
Gives voice.mp3, words.json (word times) and captions.srt. All shot timing comes from words.json.

## 4. Footage (YouTube downloads are blocked from the cloud; use these instead, in this order)
1. **X posts** from official accounts (NBA, team accounts, ESPN, ClutchPoints, House of Highlights): find them with
   `WebSearch "x.com <account> <moment> video"` (allowed_domains x.com), then `python Tools/x_clip.py <links...> --out src`. 720p-1080p, 10-130 s.
   Look at them with `python Tools/broll.py sheet src/<id>.mp4 --from 0 --to 30 --every 1 --out s.jpg`, cut with `broll.py cut src/<id>.mp4 --at T --len L --x 0.5 --out clips/V01.mp4`.
2. **archive.org** for old games (`https://archive.org/advancedsearch.php?q=title:(...)&output=json`, then ffmpeg `-ss` straight off the file URL). 480p: use blur-fit, not a hard crop.
3. **YouTube moments**: `python Tools/yt_sheet.py <id> --from 0 --to 120 --every 2 --out s.jpg` shows the video's own preview frames with timestamps (no download).
   Find ids with `python Tools/broll.py search "<query>"`. Write `<folder>/clips_manifest.json` ([{"file","video","at","len","x"}]) and the user (or the PC) runs `python Tools/pc_cut.py --folder "<folder>"`.
Quality bar: every shot matches its spoken line; check each player's identity frame by frame (preview frames are too small to prove a face: say "verify" in the plan).

## 5. Evidence cards (any fact line)
`python Tools/card.py --url <article> --mark "<exact words>" --headline y0,y1 --byline y0,y1 --out "<folder>/clips/c01.mp4" --len 2.4`
Red box timed to the word; cards sit above the caption band. ESPN pages are washed out by an overlay; card.py fixes it. Look at the card PNG before using it.
Basketball-Reference: `--selector "#all_all_salaries"` style crops via `webshot.mjs`.

## 6. Cut: write `shots.json` ([{"clip","start"}] with start = the word's time in words.json) and `sfx.json` (2-5 effects from `Tools/sfx`, each tied to something on screen),
then `python Tools/assemble.py --folder "<folder>" [--caption-style clank|metasports]`. No Drift on Linux, so the ffmpeg engine runs. Output final.mp4 (-14 LUFS), preview_1-3.jpg, storyboard.jpg.
**Look at storyboard.jpg card by card** before delivering. Copy to `READY TO POST - <Title> (Claude cut).mp4`.

## 7. Upload package (`UPLOAD.md`, template: `Productions/MetaSports/2026-09-28 01 Why LeBron Took a 92 Pay Cut/_claude_v4/UPLOAD.md`)
Title: 3 options, 4-7 words, opening on Why/How/What/Did/Is/He or an action/claim word (CoachClank name-first titles got half the views; question marks and digits showed no lift, Round 6), 1 emoji, no hashtags, no ALL-CAPS words, matches words people search that week.
NO description (the user doesn't use one). Tags: 25-30 comma-separated search tags, 440-490 characters total (YouTube's limit is 500): people, teams, the rule/event, season, 'nba shorts, basketball shorts'. Pinned comment: the two-sided argument. Covers: `python Tools/thumb.py --shape short`
x3 (one-line number hook; keep the face visible; use single quotes around text with $). Post time: YouTube says timing matters little (Round 6), so post when ready and write down the go-live time. Covers: the Shorts feed shows no custom thumbnails, so make just one (A) and spend no more than 5 minutes.

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
