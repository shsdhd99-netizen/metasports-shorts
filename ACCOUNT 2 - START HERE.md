# Account 2: start here

You are the second Claude account on the MetaSports project (written Oct 29, 2026). The owner runs two YouTube Shorts channels:
- **MetaSports** (@MetaSportsClips): NBA, AI voice, 20-30 s moment and stat Shorts.
- **MetaSports FC**: soccer story Shorts in the style of Ahmed's Goal, 50-59 s.

The **main account** already runs the daily machine: research at 3:43 AM ET, an NBA build at 4:41, a soccer build at 5:39 and a stats check at 7:07 PM. It also owns the Hubs, the owner's to-do list and the posting schedule. **Your job is the workshop around it:** deeper research, a backlog of Shorts built in advance, real-audio versions, re-edits and tool fixes. You hand finished work back through the repo, and the main account schedules it.

The owner is not technical and reads on a phone. Keep chat short and plain, and name Shorts by their title.

---

## 1. The owner's standing rules (never relax them)
1. **Never post, schedule or replace a public video, and never open YouTube Studio.** Everything you make is a DRAFT; the owner posts.
2. **Never print, commit or ask for an API key.** Keys live only in this account's environment settings, never in chat or files. Before any commit, check the staged diff: `git diff --cached | grep -c "AQ\\.Ab8"` must print 0.
3. **No cookies with yt-dlp, and no DRM, paywall or protected-media workarounds.** If a download returns 403, or a player won't hand over a plain file (Sky Sports, Arsenal.com), drop that source and don't work around it.
4. **Never invent a stat.** Every number in a script has a source and its exact words in `notes.md`. Keep qualifiers ("reportedly"). When sources disagree, word the line so it's true under both (example: "with time running out" when reports say both the 87th and 88th minute).
5. **Gemini reports are tier [S]** (one model's view). Never claim you listened to anything yourself.
6. **No promo outro, no "follow" ask, no cards** (one card of 1.5 s at most, never in the first 4 s, and only when nothing else can carry the proof). TikTok and Instagram cuts are paused.
7. **Posting cadence** belongs to the main account: up to 2 Shorts per channel a day, 6+ hours apart.
8. Don't put model names in anything you commit. Commit messages end with the attribution lines your own session gives you.

## 2. One-time setup (the owner does this on this account)
- **GitHub:** connect GitHub on this Claude account with access to `shsdhd99-netizen/metasports-shorts`.
- **Cloud environment:** set network access to **Full** (ESPN, archive.org, x.com, ElevenLabs, Google and Basketball-Reference are all needed).
- **Secrets** (environment settings, never chat):
  - `ELEVENLABS_API_KEY`: the same ElevenLabs key as the main account. **Both accounts share one credit pool** (see section 6).
  - `GEMINI_API_KEY`: a new free key from Google AI Studio, ideally on another Google account, so the two accounts don't share a quota.
- **No access to the Hubs or the to-do list is needed.** They stay with the main account, so there's one source of truth.

## 3. Every session: first 10 minutes
1. Clone the repo. `git fetch origin main-329h3w account2`, then check out `account2`. If it doesn't exist yet, create it from `main-329h3w`. Then `git merge --no-edit origin/main-329h3w` so you start from the latest work.
2. Run `bash Tools/cloud_setup.sh`. It should print `key: set` and `gemini: set`.
3. Read, in this order:
   - `CLOUD STATE - read this first.md`: the newest sections at the top.
   - `MetaSports - Playbook.md`: **THE RULES** at the top win over everything else.
   - `Soccer Channel/Playbook.md`: the soccer channel rules.
   - `.claude/skills/cloud-short/SKILL.md` (NBA), `.claude/skills/story-short/SKILL.md` (soccer) and `.claude/skills/daily-run/SKILL.md`: the build steps.
   - `Research Notes/Lessons Learned (running log).md` and `Soccer Channel/Lessons Learned.md`: the latest entries.
   - `Research Notes/Daily Log.md` (latest entries) and today's `Research Notes/Daily Research/<date>.md`.
   - `Research Notes/Account 2/Queue.md` and `Log.md`: your own queue and notes.
4. Check credits before any voice work (section 6).

## 4. Where your work goes, and what you never touch
**Branch:** work and push only on `account2`. Never push to `main-329h3w` and never force-push. If your session was handed another branch name, push there and say so in `Log.md`. The main account merges `account2` at the start of every daily run.

**Your files:**
- NBA Shorts: `Productions/MetaSports/A2 <YYYY-MM-DD> <Title>/`
- Soccer Shorts: `Soccer Channel/Productions/A2 <YYYY-MM-DD> <Title>/`
- Your notes: `Research Notes/Account 2/` (`Queue.md`, `Log.md`, and any research files you write)
- Tool fixes in `Tools/` are allowed. Keep each one small, run a real Short through it before committing, and describe it in `Log.md`.

**Don't edit** (the main account owns them, and edits would collide): `UPLOAD SCHEDULE.md`, `CLOUD STATE - read this first.md`, `Research Notes/Daily Log.md`, `Research Notes/Outcome Log.md`, the idea banks (suggest additions in your `Log.md` instead), the Hubs, the owner's to-do list, and any production folder that isn't yours.

**Numbers:** don't give your Shorts a number (#80, S19...). The main account numbers each one when it schedules it, so the two accounts never collide.

## 5. Hand-off: what "built" means
A Short is `built` when its folder has all of this:
- `script.txt`, plus `notes.md` with lane, concept, added value, copy check and a **claims table** (each line, its source and the exact quote), and the footage list with sources and anything illustrative flagged.
- `cuts_plan.json` / `cuts.json`, `words.json`, `voice.mp3`, and `title_caption.txt` for soccer.
- **DRAFT files:**
  - NBA: `DRAFT - awaiting approval - <Title> (real audio).mp4` when a live call exists, plus a narrated spare or a music/no-music pair.
  - Soccer: `(music)` and `(no music)`, plus `(real audio)` when a live English call exists.
- `qa_short.py --full` **PASS** on every DRAFT (soccer folders pick up the story profile on their own).
- A Gemini pre-check READY (`python Tools/yt_watch.py "<DRAFT>" --precheck --out-dir "Research Notes/Watch Reports/drafts"`). A FIX line means check that timestamp yourself, then fix it or explain why it's fine.
- `UPLOAD.md` with 3 title options (option 1 = line 1), empty description, 3-8 tags of about 100-150 characters (`python Tools/tags_fit.py --cap 150 "..."`), a pinned comment, which version to post and why, and whether it's **news** (must post the morning after) or **evergreen**.

Then add a line to `Research Notes/Account 2/Queue.md`, commit and push to `account2`.

Queue statuses:
- `built`: everything above is done. The main account puts it on the Hub at its next run.
- `voice-ready`: script, notes, sources, footage in `src/` and a cut plan are done, but there's no voice yet (usually because of credits). The main account voices and builds it.
- `research`: a vetted idea with sources and a footage test passed, but no script yet.

## 6. Voice credits (shared with the main account)
- ElevenLabs Creator plan: about 121K characters a cycle, resetting on the 19th of each month. On Oct 29: 36,270 used.
- The main account's two daily builds use about 3,000-4,000 characters a day, which is most of the cycle.
- **Check before every voice job:** `. <key> && python Tools/voiceover.py --check` prints `Characters used: X of Y`. (Load the key from the environment; never print it.)
- **Only voice when** `Y - X - (days until the 19th × 3,500)` is bigger than this Short's script length × 2 (allowing a retake). Otherwise stop at `voice-ready`.
- `voice_take.py` repairs a single bad word with `retake_sentence.py` before paying for a new take. Use that rather than re-recording.

## 7. The task list (work top to bottom; log each item in `Log.md`)

### A. Build ahead (highest value)
1. **Jokić breaks Westbrook's triple-double record (pre-build).** He has 200, Westbrook's record is 209, so he needs 10 more (ESPN, Oct 28). Build everything now except the record night: research, script with a slot for the night's numbers, archive and ESPN footage of his milestones, and his Oct 28, 2015 debut (2 points; Basketball-Reference). When it happens, the main account adds the night's clip and posts the next morning. Status: `voice-ready`, with a note on what's missing.
2. **Make a milestone calendar** (`Research Notes/Account 2/Milestones.md`): NBA and soccer records likely to fall in the next 6 weeks (career totals, streaks, anniversaries of famous moments), each with the source, the gap left and a footage plan. Pre-build the top 2 like item 1.
3. **Soccer backlog** (`Soccer Channel/Idea Bank.md`). Pick by the footage test: frame 1 plus one proof clip per beat must exist before you script. Check archive.org first, then ESPN's public match clips.
   - **Ronaldo moved the Coca-Cola bottles:** script and notes are already in `Soccer Channel/Productions/2026-10-27 S09 Ronaldo Moved The Coca-Cola Bottles/`. Re-check every claim (especially the reported market-value drop), then find footage and build.
   - Unmade ideas, in this order: Henry's handball and the money FIFA reportedly paid Ireland; Ronaldinho jailed in Paraguay and the prison futsal tournament (every line "reportedly"); Pelé's laces at the 1970 kickoff; Lampard's ghost goal and goal-line technology; Cantona's kick and the community service; Balotelli at his own club.
   - Every claim in the bank is UNVERIFIED until it's in that Short's `notes.md` with a source.
4. **NBA weekly countdown test:** one "3 times [star] did X" Short, with a #3/#2/#1 corner badge (`overlay` in `cuts.json`; see THE RULES in the NBA Playbook) and the best one last. Use one of the 3-4 biggest names.
5. **Real-audio passes:** for any `built` Short with a live broadcast call but no real-audio version, make one (`Tools/nat_sound.py`; recipe in section 9).

### B. Research
6. **Sunday competitor review:** run the competitor scan (`Research Notes/Competitor Watchlist.csv`; newest 30 per channel; flag 3x+ outliers). Have Gemini watch the top 5 (`python Tools/yt_watch.py <id>`). Write `Research Notes/Account 2/Competitors <date>.md` with outliers, lanes, title wording, and **one** lesson only if 3+ Shorts support it.
7. **Footage source map:** write `Research Notes/Account 2/Footage Sources.md`, listing which public sources give a plain file for each league and competition. Known so far:
   - **Works:**
     - ESPN's public clip API: `site.api.espn.com/apis/site/v2/sports/<sport>/<league>/summary?event=<id>`, `videos[].links.source.HD.href`. Covers NBA, LaLiga and some Carabao Cup studio segments.
     - archive.org full broadcasts, by HTTP seek: `ffmpeg -ss T -i URL -t D -c copy`.
     - X posts via `Tools/x_clip.py`. Check the post first with `cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`.
     - Mixkit stock: `Tools/stock.py`.
   - **Doesn't work:** Sky Sports and Arsenal.com players; some X posts return 403 (drop them); YouTube downloads (blocked; `Tools/yt_sheet.py` gives preview frames only).
8. **Ahmed-style NBA test:** "The NBA star who skipped a Finals practice to go wrestling" (#78) posts Sat Oct 31. At 72 h (Tue Nov 3), compare its views (and stayed %, once the owner's Studio export arrives) with the channel median. If it wins, script 3 more NBA history stories in that format, one per week.
9. **GTA 6 channel plan:** the owner decided to start it on Nov 12 (launch Nov 19). From Nov 12, draft the research plan in `Research Notes/Account 2/GTA6 Plan.md`: competitor channels, formats and a launch-week schedule. The owner's part is a console to record on and a channel name.

### C. Finishing and tools
10. **`Tools/deflash.py`:** it drops the audio track and decodes the whole file into memory, so a 33 s 1080p source failed. Make it keep the audio (copy the stream) and process frames as a stream. Until then, use it only on cut clips, never on sources.
11. **`Tools/footage_qc.py`:** the story-format allowance for archive footage (blow-ups up to 6x) is keyed on the folder path containing "Soccer Channel". Make it also follow `qa_short.py --profile story`, so Ahmed-style NBA tests on 1990s archive footage are judged the same way.
12. **`Tools/assemble.py`:** two renders running at once in the same folder break each other (one came out with a 0.2 s picture). Add a lock file or per-render temp names. Until then, always render one after the other.
13. **Music test tally:** NBA music side #70 and #72, no-music side #71 and #74 (posts Fri Oct 30). Once all four are 72 h old, write the comparison in `Log.md` (views at 72 h; stayed % when the owner's Studio export arrives). Real-audio posts are a separate arm, outside the test.

### Owner-only (never attempt; at most remind once)
Posting; the Studio export (Mondays); the YouTube Analytics sign-in; swapping the old Gemini key.

## 8. Quality bar (short version; the skills have the full rules)
**NBA:**
- 20-30 s. Line 1 is 11 words or fewer and states the strange thing (not a question).
- **Frame 1 shows line 1 happening.** Shot 1 holds 2.0 s or more. At most 2 shots in the first 3 s.
- About 10-15 shots of about 2 s. Wide plays use `"blurfit": true, "blurfit_aspect": 0.75`.
- Replay the key second once before the payoff (`"replay": true`, often `"speed": 0.5`).
- One fact the clip can't show (YouTube's originality rule). End on the payoff.

**Soccer:**
- Ahmed's shape: title read as line 1, "Back in [year]...", a turn every 8-12 s, the payoff as the last line.
- About 230-250 words, ending under 59.5 s after `tighten_voice.py`.
- Title card in `title_caption.txt` (1-2 CAPS words). Global names only. At most 3 shots in the first 5 s.
- Render both versions: `assemble.py --caption-style ahmed --no-music` and with music. **One after the other, never in parallel.**

**Both:**
- Name a person, show the person.
- No logos or burned-in text from other creators.
- Look at `_check/sheet.jpg` and `Tools/shot_strip.py` before `--verified`.
- QA must PASS. Then look at frame 1, every overlay and the last frame yourself.

## 9. Recipes and pitfalls learned this week
- **Voice:** `. <key> && cd Tools && python voice_take.py --script "../<folder>/script.txt" --takes 3`. Then `tighten_voice.py --folder F`, adding `--thresh 0.25 --keep 0.12` for NBA. Then `fill_len.py F`, `cut_list.py --folder F`, `anchor_shots.py --folder F`.
- **QA "voice is cut off":** pad the tail: `ffmpeg -i voice.mp3 -af apad=pad_dur=0.25 ...`, then re-render.
- **Real audio** (see `Productions/MetaSports/2026-10-30 79 Two Buzzer-Beaters From 40 And 50 Feet`):
  1. Get word timings of the call with faster-whisper `small.en`.
  2. Cut the narrated words out of the voice and insert silence the length of the call.
  3. Add the call's words to `words.json` with `"live": true`.
  4. Cut each live shot from the same seconds as the call: `at` = the first word's source time minus the shot's `lead`.
  5. Render with `--no-music`, then `nat_sound.py --burst A-B --bed-db -26..-30 --tail 0.4`.
  6. Keep the narrated render as the copyright fallback.
- **One-frame flashes** (common in ESPN and archive encodes): `deflash.py clip --check`, then fix only the flagged cut clips.
- **Waiting on a background job:** never `pgrep -f <name>` inside a loop whose own command line contains that name; it finds itself. Wait for the output file instead.
- **Disk:** sources are git-ignored. Delete a Short's `src/` after the owner posts it.

## 10. Reporting
End every session with 3-5 plain lines in chat: what you built or researched, what's in the queue now, credits used, and anything only the owner can do. Put the detail in `Research Notes/Account 2/Log.md`.
