# Daily Log (newest first)

One entry per channel per day, written by the daily runs (`.claude/skills/daily-run/SKILL.md`): data pulled, what was learned,
research with sources, what was made, what changed in the rules or tools.

## Sat Oct 24, 2026 (manual session; the automatic runs start Sun Oct 25)

**Data.** Studio exports Oct 17-24 for both channels (`Research Notes/Studio Export Read (Oct 24, 2026).md`). API analytics:
no token in the cloud yet (needs `YT_REFRESH_TOKEN` / `YT_REFRESH_TOKEN_FC`).

**Learned.**
- FC: S01 80% stayed vs S02 56% and S03 65%. Cause: frame 1 and the first line did not show the promise, and S03 reached its
  promise at 54 s. Full write-up: `Research Notes/Why S02 and S03 Underperformed (Oct 24, 2026).md`.
- Ahmed's Goal data: plural "Players who..." titles beat singular ones (median 318K vs 217K, 500 vs 73 Shorts). The
  singular-title advice is withdrawn.
- Ahmed's best titles promise a human conflict (refused, rejected, bullied, backfired); his worst are news questions and neutral facts.
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
