# Prompt: deconstruct and rebuild how we make a Short (paste into the terminal session)

You are reviewing the whole MetaSports production system (NBA channel @MetaSportsClips and soccer channel MetaSports FC) to
make our Shorts hold viewers longer and stop small, avoidable mistakes. Branch `main-329h3w`; `git pull --no-rebase` first.
Standing rules: never publish, schedule or open YouTube Studio; never print or commit keys; drafts only; Shorts under 60 s.
Commit with the Co-Authored-By / Claude-Session lines used in this repo's history.

Goal: we sit at 15-30K views a Short. Find what keeps us from 100K+. Question every default. Don't accept a rule because it's
written down; keep it only if our data or strong outside evidence supports it. Every change needs evidence and a tier:
[V] measured on our data, [S] seen in a few examples, [H] guess. Never invent a number.

## 1. Read the system (skim, take notes as you go)
- How a Short is built: `.claude/skills/cloud-short/SKILL.md`, `nba-short`, `story-short` (+ `QA.md`), `daily-run`.
- The rules: THE RULES at the top of `MetaSports - Playbook.md`, `Soccer Channel/Playbook.md`, `Research Notes/Rule Changes Applied (Oct 26, 2026).md`.
- The tools that make every choice: `Tools/voice_take.py`, `tighten_voice.py`, `captions.py`, `cut_list.py`, `broll.py`,
  `assemble.py`, `fill_len.py`, `nat_sound.py`, `qa_short.py`, `export_check.py`. Write down each hard-coded default
  (caption font, size, y-position, words per caption, colour rules, highlight logic, animation; voice speed and pauses;
  shot length; zoom/blur-fit; music level; SFX choice and timing; first frame; ending).
- The evidence: `Research Notes/Shorts Dataset.csv`, `Studio exports/` (stayed %, retention curves), `Outcome Log.md`,
  `Lessons Learned (running log).md`, `Soccer Channel/Lessons Learned.md`, `Retention and Editing Upgrade (Oct 26, 2026).md`,
  `What Makes Our Shorts Go Viral (Oct 24, 2026).md`, `Watch Reports/` (221 JSON, many competitors), and today's unfinished
  `Editing Study data (Nov 1, 2026)/` and `Soccer Topic Study (Nov 1, 2026)/`.

## 2. Measure our own Shorts (all posted ones, both channels)
Public views now: `yt-dlp --flat-playlist --print "%(id)s %(view_count)s %(title)s" https://www.youtube.com/@MetaSportsClips/shorts`
(and the FC channel). Map each to its production folder. From each folder's words.json / shots.json / cuts.json / sfx.json /
music.json / captions and the final file, compute: words per minute, pauses, length, shots in the first 3 s / 5 s, median shot
length, zooms, overlays, captions (words per screen, chars, highlight count and which words), SFX count, music yes/no and level,
real audio yes/no, frame-1 brightness and subject, time to the first star name / number, time of the turn and the payoff, what
happens in the last 1 s. Correlate with views and stayed %. Look at the retention curves: for every drop, look at the frames at
that second and name the cause. Say when n is too small.

## 3. Watch competitors (GEMINI_API_KEY is on this PC; never print it)
`python Tools/yt_watch.py --channel <@handle> --top 10` for CoachClank, Ahmed's Goal, Ahmed's Basketball, Swishyyy and the top
NBA/soccer story channels in `Research Notes/Competitor Watchlist.csv`; also their median (not top) Shorts, and our last 10 per
channel. Use `--ask` for exact questions: caption colour per word and why that word, words per caption, position, font, outline,
pop animation; voice pace; shots per 10 s; zoom/punch-ins, speed ramps, freeze frames, circles/arrows; SFX type and moment;
music genre, volume, drops; real crowd/commentary; first 2 s; last 2 s; loop.

## 4. Deconstruct each part. For each: what we do now, what the winners do, what our data says, the change, and the test
- **Captions:** which words get colour. Test a clear rule, e.g. green = the number/payoff, red = the conflict/negative word,
  yellow = names, white = everything else; or only 1 coloured word per screen. Words per screen (1-3?), size, position
  (we use y 1100, max 700 px wide), stroke, pop-in timing vs the spoken word, all caps or not, emoji. Does colour on the
  wrong word (filler) hurt? Count it on our hits vs flops.
- **Voice and speed:** words per minute (NBA vs FC), gaps between sentences (`tighten_voice` keeps 0.12 s), emphasis, the
  first line's pace, speed changes. Is 233 wpm right for soccer stories?
- **First 2 seconds:** frame 1, line 1, the title said out loud or not, the promise, movement in frame 1, text on screen.
- **Pacing:** shot length, when to hold, replays, slow motion, where viewers leave on our curves.
- **Visuals:** zoom level, 3:4 blur-fit vs full crop, punch-ins on key words, proof on the footage (circles, numbers),
  colour grade, sharpness of old footage, logos.
- **Sound:** music yes/no (our A/B), genre, level, the drop before the payoff, SFX palette (whoosh, hit, riser), real crowd
  and commentary, loudness (LUFS), nothing ringing at the end.
- **Story:** the turn every 8-12 s, number gaps, irony, the payoff, the ending (no tease; a loop?).
- **Packaging:** title, frame 1 as the cover, tags (490), pinned comment, post time.
- **Process:** where mistakes slipped through (wrong fact, dark frame 1, voice glitches, mis-heard names, captions too
  fast, sound cut off, dead air). For each, add or fix a QA check in `Tools/qa_short.py` so it can't happen again.

## 5. Deliver
1. `Research Notes/Full Review for Retention (Nov 2026).md`: the 15 changes most likely to raise stayed % and views, ranked,
   each with evidence, tier, and how we'll know it worked (which number, after how many Shorts). Then a "small mistakes"
   checklist. Then what to stop doing.
2. Implement the clear wins in the tools, opt-in or default as the evidence supports (e.g. a caption colour rule in
   `captions.py`, punch-in zooms in `cut_list.py`, an SFX palette, new QA checks). Keep old behaviour available.
3. Update the skills (`cloud-short`, `story-short`, `nba-short`, `daily-run`) and THE RULES so every run uses the changes.
4. A before/after: re-edit one finished Short per channel (e.g. #73 and S17) with the new rules using the existing voice (no
   new ElevenLabs credits); save as `DEMO - review upgrade - <title>.mp4`; full QA must pass. Show me both side by side.
5. A one-page summary for me in plain English: what changes, why, and what you need from me.
Commit and push to `main-329h3w`.
