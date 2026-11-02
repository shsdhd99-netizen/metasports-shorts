# Handoff, Sun Nov 1 2026 (cloud session -> owner's Claude terminal)

Branch `main-329h3w`. First: `git pull --no-rebase origin main-329h3w`. Rules unchanged: never publish, schedule or open
YouTube Studio; drafts only; never print/commit keys; Shorts under 60 s; no promo ending; tags filled to 490 (`Tools/tags_fit.py`).
Commits end with the Co-Authored-By / Claude-Session lines used in this repo's history.

## Unfinished (all work saved in git; the agents stopped at the 5-hour limit)
1. **#82 Wemby block -> point 40** (`Productions/MetaSports/2026-11-01 82 Wemby ...`). News: post TODAY (Sun Nov 1) or skip.
   Voice done, cuts done, `final.mp4` rendered; no-music version passed full QA; last check was whether both "point"s are
   audible. Left: real-audio version (`Tools/nat_sound.py`, live call on the dunk) if quick; name the file
   `DRAFT - awaiting approval - Wemby Blocked A Three And Scored Point 40 (<version>).mp4`; UPLOAD.md (title, 490 tags,
   pinned comment); NBA Hub card `shorts/n82` (artifact SAWcHwuAwBxJuyBQSs8a8U, slug cbc86845-4da2-4e02-8529-24503836c8ed)
   with a 1.5 Mbps asset copy; send it to the owner.
2. **Soccer research** (owner: "research and develop on soccer videos just like nba"). FC Shorts are ON HOLD until it's done.
   - Topic data: `Research Notes/Soccer Topic Study (Nov 1, 2026)/` (raw channel lists, `analyze.py`, `classified.tsv`,
     `results.txt`). Finish: ranked topics by outperformance vs each channel's median, title shapes, our FC data, 20 sourced
     candidate stories -> `Research Notes/Soccer Topic Study (Nov 1, 2026).md`.
   - Script craft: our hits (goalkeepers S01 30K, S05 28K, S03 15K, S17 9K) vs flops (all others 1-3K) line by line + web
     research -> `Research Notes/Soccer Script Craft (Nov 1, 2026).md` (do's, don'ts, template, one example goalkeeper script).
   - Then: FC Playbook v2, `.claude/skills/story-short/SKILL.md`, daily-run FC lanes. Then revise S20 (Messi napkin: voice +
     31-shot cut plan done, not rendered), S09, S19 against it.
3. **Editing study** (owner: editing to go from 15-30K to 100K+). Data so far in `Research Notes/Editing Study data (Nov 1, 2026)/`.
   Finish: mine the 221 `Research Notes/Watch Reports/*.json` + our shots/sfx/music data vs views; ranked changes ->
   `Research Notes/Editing Study (Nov 1, 2026).md`; implement top 2-4 as opt-in tool features; a `DEMO - editing upgrade`
   re-edit of #73 with its existing voice. **On the PC:** GEMINI_API_KEY exists there, so also run
   `python Tools/yt_watch.py --channel @CoachClank --top 10` (and @AhmedsGoal, @Swishyyy, + others from
   `Research Notes/Competitor Watchlist.csv`, and our own last 10 per channel), asking about editing and sound.

## Done today
- #74 was posted Sat evening (16K by Sun 9 AM); Hub card marked posted.
- #73 Bones Hyland finished (19.9 s, QA PASS, music + live call), on the NBA Hub for Mon Nov 2, 7-8 AM ET.
- Daily runs now fire 3:17 AM ET (NBA) and 4:23 AM ET (FC); `.claude/skills/daily-run/SKILL.md` "Nov 1 updates" override the
  out-of-date task prompts (prompts can only be edited from the runner sessions). Runs still lack `ELEVENLABS_API_KEY` in the
  cloud environment settings: owner to add it.
- `Tools/yt_schedule.py`: scheduled upload via the official API (Google now allows unverified projects to upload publicly).
  OFF until the owner adds `YT_UPLOAD_TOKEN`/`_FC` and says which mode (approve each, or all that pass QA).
- `UPLOAD SCHEDULE.md` updated (today-Tue plan, run times, keys, auto-scheduling).
- Waiting voiced: #67 Jordan insult (voice done, no footage yet).
