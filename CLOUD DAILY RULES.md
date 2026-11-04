# Cloud daily-run rules (read FIRST by the NBA and FC routines; edited by either account through git; Nov 3, 2026)
1. `git pull --no-rebase origin main-329h3w` (other accounts and the PC push too). Small commits, pull before editing, never open or merge a PR.
2. Read `Research Notes/BUILDER.txt`. Build a Short ONLY when it says `cloud`; otherwise do zero-credit steps and write `STATUS: not the builder`.
3. Read `Research Notes/STATE.md`, `USAGE.txt` (weekly over 90% means one `STATUS: skipped, low usage` line and zero-credit steps only), `BUILDER.md` (cloud vs PC split).
4. `bash Tools/cloud_setup.sh` then `python Tools/preflight.py --quiet`. On BLOCKED (no voice key, dead token, no credit) write the script and notes only, log why, stop spending credits.
5. Claim your Short folder in `STATE.md` (`CLAIM <folder> <account> <time>`) before building; delete the line when done. Never work a folder another account claimed.
6. Read `Research Notes/Learned Weights.md` before the lane: about 70% from lanes marked ABOVE, about 30% explicit one-variable experiments, skip a lane flagged PAUSE; n under 5 is a guess. Append the new Short's row (lane, fresh, music) with `python Tools/learn.py ingest` after filling the hand columns.
7. Cloud cannot download from YouTube. If a story needs a YouTube-only clip, add a line to `Research Notes/PC Requests.md` and pick a story with X, ESPN, archive.org or Mixkit footage instead.
8. Then follow `.claude/skills/daily-run/SKILL.md` for your channel. Never publish and never open YouTube Studio. Scheduling happens only through `Tools/yt_schedule.py` guard rails for a Short the owner approved (Hub card `approved: true` or the owner's words); otherwise every output is a draft.
9. End by updating `STATE.md`, appending a `STATUS:` line to `Research Notes/Daily Log.md`, `python Tools/learn.py all` (commit `Experiments.csv`, `Learned Weights.md`), push.
10. Do not commit video over 20 MB (the push fails); keep DRAFT renders local or on the Hub.

## NBA run (argument `nba`; Hub https://claude.ai/artifact/SAWcHwuAwBxJuyBQSs8a8U)
Follow `.claude/skills/daily-run/SKILL.md` with `nba`; read `Research Notes/What Makes Our Shorts Go Viral (Oct 24, 2026).md` first. Setup and newest Daily Log entries; `python Tools/yt_analytics.py daily` (log it if the token secrets are missing); learn from Shorts 72 h+ old; research last night's NBA games (last 24 hours, household-name stars; lane by rotation and Learned Weights); make ONE Short with the cloud-short pipeline that passes `python Tools/qa_short.py --full` (look at frame 1, every overlay and the last frame yourself; tags with `Tools/tags_fit.py`, 490 characters); put it on the NBA Hub for the next free slot per `UPLOAD SCHEDULE.md` with the TikTok/Instagram caption; log data, research with source links and changes in the Daily Log; commit and push.

## FC run (argument `fc`; Hub https://claude.ai/artifact/2UVAcbNpKq6j4YXBEF8ge3)
Follow the skill with `fc`; read the same viral note and `Soccer Channel/Playbook.md` (v2: goalkeeper lane first, others only as flagged experiments). `python Tools/yt_analytics.py --channel fc daily`; lessons into `Soccer Channel/Lessons Learned.md`; take the next unmade story from `Research Notes/Soccer Topic Study (Nov 1, 2026).md` section 7 or `Soccer Channel/Idea Bank.md` that passes the footage test; make ONE Short with the story-short skill (YouTube cut 50-59.5 s, music and no-music, `qa_short --full` PASS); Hub card for the next free 12:00 PM ET slot; log and push. FC folders already scripted but unvoiced: S29 (built on the PC), S31, S32, S30.

- Clip reuse (Nov 4): same source range twice, one source over 35% of runtime, or same angle back-to-back are flagged by `edit_lint`; fix them with more sources (evidence: reuse did not hurt retention, so advice only).

## Owner's rules, never relax them
Never publish or replace a video; never open YouTube Studio; scheduling only via `Tools/yt_schedule.py` guard rails for a Short the owner approved; never print, commit or ask for keys or tokens; never invent a stat; no teaser or promo at the end; no dead air; every Short under 59.5 s; at most 2 posts a day per channel, 6+ hours apart. If the ElevenLabs key is missing write the script only and say so on the Hub card. End with 3-5 plain lines for the owner: what was made, its slot, QA result, what you learned, what only the owner can do.
