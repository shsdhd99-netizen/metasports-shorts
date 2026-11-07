# PC terminal (account 1) to CLOUD: what changed and what to use (Fri Nov 6, 2026, evening)
No keys here. College and personal items are deliberately NOT in this note (private, PC only).

## New tools (all in `Tools/`, committed; run from the repo root)
- `qa_portions.py "<folder>"`: QA by portion (SCRIPT, VOICE, FOOTAGE, EDIT, AUDIO, PACKAGE, LIVE).
- `qa_final.py "<folder>"`: ONE verdict SHIP / FIX / HOLD (portions + `qa_short --full` + file checks 1080x1920, 15-59.5 s, black first/last frame, title, sources). Writes `qa_final.json` in the folder and a line in `Research Notes/QA Final Log.csv`.
- `queue_rank.py [--apply]`: scores every waiting Short 0-100 (lane 30, topic stars 20, QA 20, proof 10, idea 10, package 10), assigns slots best-first, drops stale game-night moments, puts weak ones (under 55) in quiet filler slots, holds QA FAIL. Writes `Research Notes/Queue Rank.md`. Weights are judgement: tune them after 72 h results.
- `pin_helper.py`, `weekly_review.py`, `essay_check.py` (private use), `reel_read.py` / `reel_watch.py` (read saved reels: transcript, else download + Gemini watch; PC only because it needs the owner's logged-in browser cookies).
- `yt_edit.py` works for BOTH channels now (edit access granted by the owner; tokens live only in the PC's `Tools/.env`, never copy them to the cloud). Commands: `show|title|tags|privacy|publish-at|delete <id>` (delete needs the id typed twice).
- `daily-run` skill rewritten (about 90 lines; old overrides in `Research Notes/Rule History - daily-run skill before Nov 6 rewrite.md`). The owner approved the cloud proposal. Please read it before the next scheduled run and tell the PC if a step does not work from the cloud.

## Findings that matter to you
1. **All five top queued Shorts fail `qa_final` (HOLD)**: #77 Bronny, #80 Warriors flipped score, #78 Rodman, S16 Manager/stop scoring, S18 Barcelona sprinklers. Common causes: cards with a placeholder/missing title or no QA PASS line, no cover.jpg, under 15 tags, fewer than 2 source links in notes.md, source clips missing on disk (re-download needed), #78 is 54 s of script (long), S16 is 62 s. Some may be old card formats the checker cannot parse: the PC will fix cards one at a time. **Do not schedule any of them yet.** S17 (FC, 54) is the only fail-free filler; #79 filler (47).
2. **Sat Nov 7 7:15 AM and 3:30 PM NBA have nothing ready except Klay #98** (A1 build). Please do research for a Sat 3:30 PM moment from Friday night games (3:43 AM run).
3. **Style tests** (`Research Notes/Autopilot Schedule v2 (Nov 9-22, 2026).md` section 8): bargain-scouting lane (S39 Leicester), on-screen name tags, CRT-TV frame for archive footage, rapid-fire payoff list ending. One variable per Short, logged in `Test Log.csv`, only if the idea still rates 10+.
4. **Instagram DM / saved-reels reading works** (owner's thread, owner's saved folder). Reel notes are private on the PC. If you want research from them, ask the PC terminal for a specific topic; do not ask for raw notes.
5. **Ban-risk note:** the owner's Instagram has a third-party "Ghost Dashboard" extension with Auto-Unfollow. Do not suggest automation against Instagram; the owner is advised to remove it.
6. The Chrome extension connects to the PC terminal; scheduled runs in the cloud still cannot reach it.

## Asks for CLOUD
- Re-run the `daily-run` skill dry (no build) to check the rewrite reads cleanly from the cloud, and report in `Team/messages`.
- Update `Research Requests (Nov 6, 2026).md` with the two-source premises due Sunday night; target at least one FC premise rated 10+ for Mon 12:00 PM (international break, so only evergreen).
- Check why the cloud environment lacks the YouTube keys (preflight BLOCKED) and whether the owner needs to paste them (`Tools/copy_cloud_env.ps1`); cloud routines stay research-only until then.
