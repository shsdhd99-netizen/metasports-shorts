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
