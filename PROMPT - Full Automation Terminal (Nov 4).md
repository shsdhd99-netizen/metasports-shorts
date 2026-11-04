# PROMPT: finish everything and automate both channels (paste into a Claude Code terminal in this repo)

```text
ROLE
You are the implementer for Admin's two YouTube Shorts channels: MetaSports Clips (NBA, @metasportsclips, 631 subs) and MetaSports FC (football, @MetaSportsFC, 145 subs). Goal: both channels run automatically every day, learn from their own numbers, and need Admin only for listening, approving and posting. Work in small committed steps on branch main-329h3w. Never open or merge a PR. Never force-push.

STEP 0: ORIENT (no skipping)
1. git fetch origin main-329h3w, then merge or rebase (a log CSV conflict: keep both sides). The repo is ahead of any local copy; automation pushes many commits a day.
2. Read in order: C:\Users\Admin\AGENTS.md; "HANDOFF - latest.md"; "Research Notes/STATE.md" and "Research Notes/BUILDER.txt"; "CLOUD DAILY RULES.md"; ".claude/skills/daily-run/SKILL.md" (the Nov 4 block first); "AUTOMATION TO-DO (Nov 3).md"; "Research Notes/Studio Analytics Review (Nov 4, 2026).md"; "Soccer Channel/Lessons Learned.md" (Nov 4 section); "Research Notes/Learned Weights.md".
3. Usage guard: run the usage tool if you have one. Over 90% weekly: do only the zero-credit steps (analytics, learn.py, schedule dry run), log "STATUS: skipped, low usage", commit, push, stop. If usage can't be read, say so and do research/scripts only (no voice, no render).

HARD RULES (Admin's; never relax)
- Never publish, schedule or replace a public video unless the existing yt_schedule.py guard rails allow it (see UPLOAD SCHEDULE.md). Every output is a DRAFT; Admin posts.
- Never print, commit, or ask for keys/tokens. Tools/.env stays untracked. Never touch the client_secret*.json in Downloads.
- Never invent a stat. Missing data is written as "missing" with the reason.
- Hub storage (1 GB) is full: upload nothing and delete only exact ids Admin approved.
- ElevenLabs voice credits are limited (resets on the 19th); spend only on a script that passes the pre-voice checks.
- Never sign into an account for Admin. Chrome is signed into the account that owns MetaSports FC only; NBA's Studio is on a different Google account, so if Studio says "no permission" log "Studio: wrong account" and use public counts.
- Never delete or mass-edit by name or glob; exact ids only. Do not shut the PC down.
- Commit only files you made (git add by path). Many untracked mp4s sit in the tree: never git add -A.

TASK 1: DATA (zero credits)
a. NBA: python Tools/yt_analytics.py daily. FC: python Tools/yt_analytics.py --channel fc daily. No token: use public counts via yt-dlp --flat-playlist --print "%(id)s %(view_count)s %(title)s" <channel>/shorts and python Tools/channel_check.py <handle>.
b. FC Studio (works with Chrome signed in): Studio > Analytics > Content > Advanced mode > download icon > CSV; unzip into "Research Notes/Studio exports/Content <dates> FC/". Also pull: traffic sources, per-Short retention curves for the top 4 FC Shorts, and "Stayed to watch" if shown. Note subs gained per Short.
c. python Tools/learn.py all --fetch, then read Research Notes/Learned Weights.md. Update Research Notes/Experiments.csv with the FC rows from the Nov 4 export (lane, subs gained, CTR, views at 72 h).
d. Write numbers into Research Notes/Daily Log.md and Outcome Log.md; never overwrite numbers Admin typed.

TASK 2: WHAT THE DATA SAYS (already found; verify, don't re-derive)
FC, Oct 7 - Nov 3: 127,234 views, 143 subs, 99% new viewers, 0% subscriber watch time. Goalkeeper Shorts are the hits (30.4K, 29.2K, 23.6K, 15.6K views, 83-96% viewed). The first of the pattern (sock cheat sheet) gave 87 of 143 subs; its water-bottle sequel gave 8 at the same views. CTR does not predict views. Manager/club-saga Shorts: 64-67% viewed, about 3K views.
NBA (public counts, Nov 4): last-7 median 3.2K vs normal 7K, trend DOWN. Winners: Bones Hyland technical (18K), LeBron 40 assists behind Kidd (8.8K), Flagg vs LeBron (5K). Losers: Kobe G7 misses, Jokic parade, Draymond triple-double (1-1.4K).
Deliverable: a one-page "Topic and Script Reset (Nov 2026)" in Research Notes: which lanes to build, which to pause, and why, citing n and medians. Apply the 70/30 rule from the daily-run skill.

TASK 3: TOPICS AND SCRIPTS
a. FC: 6 new goalkeeper/shootout ideas where each has its OWN new fact (not a repeat of cheat-sheet or substitute), plus 2 experiments changing ONE variable. NBA: 6 ideas from the winning shapes (watchable funny moment, live record chase with a star, rookie vs LeBron/star) plus a Bones Hyland follow-up. Run python Tools/idea_gauge.py and python Tools/copy_check.py on each. Skip flop shapes.
b. Add them to Soccer Channel/Idea Bank.md and the NBA queue CSV with sources, footage availability, risks.
c. Write full scripts for the top 3 per channel; run script_lint.py, script_cadence.py, copy_check.py; every "still/record/first/never/only/most" line gets a source row checked today. Script Critic v3 is advice; only a factual error blocks.

TASK 4: BUILD AND FINISH THE VIDEOS
a. Backlog first: the five rendered NBA Shorts (#10 v2, #45, #42, #36 v4, #46) and FC S09, S29. Run python Tools/qa_short.py --folder <F> --video <file> --full on each; fix real failures (known false alarm: the audio-clip one). LOOK at frame 1, every overlay and the last frame.
b. Apply the Nov 1 editing rules: frame 1 shows the claim, moving; shot 1 at least 2.0 s; at most 2 shots in the first 3 s; no black fill; no decorative SFX; no card in the first 4 s; end on the payoff.
c. New versions go in _v2, _v3; never overwrite. Each ready Short needs the DRAFT mp4, UPLOAD.md (title, empty description, tags to 490 chars via tags_fit.py, pinned comment, one cover) and, for FC, a "part 2" pinned line where it is a series.
d. Use /story-short (FC) and /cloud-short or /daily-run nba|fc as defined; build both music and no-music versions where the A/B is open. Check Research Notes/BUILDER.txt: only the named builder builds.

TASK 5: AUTOMATION (the main goal)
Close every gap in "AUTOMATION TO-DO (Nov 3).md" that a script can do, in this order:
1. Verify the PC timers fire (analytics 3:20 AM; schedule_ready 6:30 AM/PM; gap-fill NBA 6:45, FC 7:30) with schtasks /query; fix any that don't. Log results in Research Notes/STATE.md.
2. Make the Studio pull repeatable: a script or documented Chrome recipe so the weekly Studio zip lands in Research Notes/Studio exports/ with no manual step (NBA stays manual until its account is signed in; say so plainly).
3. Make learn.py also read subs-gained per Short and CTR from the Studio export, and add a "subs per 1K views" column to Learned Weights.md.
4. Add a preflight that fails loudly when keys, usage or the builder are wrong, so a skipped run is visible instead of silent.
5. Run python Tools/crosspost.py for each finished Short (captions only; Admin posts).
6. Update .claude/skills/daily-run, story-short, cloud-short only with lessons measured at n>=3 or tagged [S]/[H]; never relax the standing rules.

TASK 6: "CLAUDE PHOTOS"
Admin said "finish the Claude photos" and I could not find what that means. Search the repo and Documents for it (stills, B-roll images, covers, thumbnails). If it is covers/thumbnails, make one 9:16 cover per ready Short with Tools/thumb.py. If still unclear, write one line in the Daily Log and ask Admin; do not guess.

TASK 7: CLOSE OUT EVERY RUN
1. Update Research Notes/STATE.md, HANDOFF - latest.md, Production Queue.md status board, and the Hub card (read it first; pin every write with if_version).
2. git add by path, commit small, git fetch + merge/rebase, git push origin HEAD:main-329h3w. Confirm git status for your files is clean.
3. Report in 3-5 plain lines: what was made, QA result, what the numbers say, what only Admin can do (listen, post, sign in to the NBA Google account, add keys).
```
