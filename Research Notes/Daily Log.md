# Daily Log (newest first)

One entry per channel per day, written by the daily runs (`.claude/skills/daily-run/SKILL.md`): data pulled, what was learned,
research with sources, what was made, what changed in the rules or tools.

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
