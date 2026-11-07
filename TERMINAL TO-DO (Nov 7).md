# Terminal to-do (PC), from the cloud session, Sat Nov 7, 2026 (owner asked for it)
Read first: `HANDOFF - latest.md`, then `python Tools/team.py inbox` (A1 has 14 unread, A3 10).
Rules: claim before building (`team.py claim`), `done` after pushing; never post outside the scheduler's guard rails (`schedule_ready.py`); no keys in chat or git; small commits; `bash Tools/handoff.sh "PC account N" "<line>"` before stopping.
Open slots below are from `Research Notes/Coming Out.md` (11:59 AM ET) and `Tools/next_gap.py`; re-run `next_gap.py nba|fc` first in case one was filled since.

## Slots to fill, soonest first
1. [ ] **NBA Sun Nov 8, 7:15 AM ET: EMPTY (the next gap).** Build ONE Short and schedule it. The Nov 5 stories are now stale ("late news is dropped"): mark #98 Klay, #96 Porzingis and #97 Warriors `skip` unless one is still live news (#97 only if the streak is still going, with the new number). Better: an evergreen planned idea, or **List 1 "Who has missed the most free throws in NBA history?"** (Basketball-Reference career FTA minus FT; copy-check; our two "most missed" lists did 24-25K) and move List 1 off Mon Nov 9.
2. [ ] **NBA Sun Nov 8, 3:30 PM ET: MOMENT.** The 6:45 AM gap-fill builds Saturday night's best moment from `Research Notes/Daily Research/2026-11-08.md` (CLOUD research run, 3:43 AM ET). Same day only.
3. [ ] **FC Mon Nov 9, 12 PM ET: S38 Bounou** ("The goalkeeper who beat a team that practised 1,000 penalties"). Folder `Soccer Channel/Productions/2026-11-14 S38 ...` is `PREP: ready to voice`: voice, cut, `qa_final.py` SHIP, music + no-music, schedule. Use the 1,000-penalties line only with its quote (it's in notes.md).
4. [ ] **FC Mon Nov 9, 6 PM ET: S43** ("The goalkeeper who found out Chelsea's secret penalty plan"), `PREP: ready to voice` in `2026-11-17 S43 ...`. Second FC post that day: 6 h after S38, which is allowed (max 2 a day, 6 h apart). If it can't pass QA by Monday noon, leave the 6 PM slot empty, don't rush it.
5. [ ] **NBA Mon Nov 9, 7:15 AM ET:** List 1 (if not used for item 1), else the next planned idea in the Auto Queue.
6. [ ] **FC Tue Nov 10, 12 PM ET: S31 "The baby Messi bathed beat him in a World Cup final".** Script only, and copy-check said TAKEN: lead with a new angle (A3's job if A3 runs; otherwise rewrite line 1 before voicing), add a cuts plan.
7. [ ] **NBA Tue Nov 10 7:15 AM** (Curry passes DeRozan, only on the night it happens) and **3:30 PM moment**: as the Auto Queue says.

## Goalkeeper lane: what the numbers say (public views, Nov 7; use when ranking FC builds)
- Shootout goalkeeper stories at 72 h: S01 30K, S05 29K, S25 24K, S17 23K, S03 15K; S28 24K after one day; S26 19K.
- The misses: S27 (goalkeeper, no shootout) 1.3K, S19 Rulli (news-tied) 3.8K; every non-goalkeeper FC Short 1.0-3.3K.
- So: build S38/S43 (both shootout stories) ahead of S31/S32 (non-goalkeeper tests).

## Tidy-ups (5 min)
8. [ ] S29 and S30 are live, but their notes.md line 1 still says "script only": update both headers (posted date and id from `Scheduled Uploads.csv`).
9. [ ] 72-h judgments (A3's job; do them if A3 isn't running): S27 on Sun, S30 on Mon, S29 on Tue. One tiered line each in `Soccer Channel/Lessons Learned.md`.

## Unblock the cloud runs (cloud FC/NBA builds have stopped at preflight for 4 days)
10. [ ] Run `Tools/copy_cloud_env.ps1` so the owner can paste `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_UPLOAD_TOKEN`, `YT_UPLOAD_TOKEN_FC` into the cloud environment settings themselves. Never print them in chat and never commit them. Tell the owner when it's ready.

## Owner decisions still open (ask, don't do): see `OWNER TO-DO (Nov 6).md` items 5-11.

## Added Sat Nov 7 afternoon (CLOUD): things the cloud couldn't settle, for the terminal
The owner is away from home; the PC terminal is on. The cloud can't reach the PC (no Remote Control folder shared), so these come through git.
11. [ ] **Check the new Hub sections render.** Both Hubs got a jump bar, "How the Shorts are doing" and "Coming up" (`Tools/hub_tracker_block.py`; data = each Hub's db doc `tracker/current`). The cloud checked the code but couldn't view them live. Open NBA https://claude.ai/artifact/SAWcHwuAwBxJuyBQSs8a8U and FC https://claude.ai/artifact/2UVAcbNpKq6j4YXBEF8ge3 (Account 1). If a section says "could not load the numbers" or a chart is blank, fix it in `Tools/hub_tracker_block.py`, re-run it on the Hub's index.html and republish. Message CLOUD with what you found.
12. [ ] **The other account's Hubs** (NBA EZrk8n855PyYpMFnMnMJd4, FC LFsQtwomdpLAshoz4Xw62H) can only be opened by Account 2. When A2 runs: apply the same block (`python Tools/hub_tracker_block.py <their index.html> nba|fc <other hub url> <out>`), upload `Research Notes/Tracker/hub_<ch>.json` there and set `tracker/current`. Skip it if the owner says those Hubs are retired.
13. [ ] **The owner's website: no spec anywhere in the repo.** The owner wants the Shorts Hub to be "an all in one place, similar to how I want the website". Search the PC (outside the repo too: Desktop, Documents, the On Demand / Netlify site folders, `Clients/`) for notes on that website. Write what you find in `Research Notes/Website notes.md`; if nothing, add it to the owner's questions (item 15).
14. [ ] **The cloud runs are blocked at preflight** (YouTube secrets missing in the cloud environment, 4th day). Item 10 above: run `Tools/copy_cloud_env.ps1` so the owner can paste the values into the cloud environment settings when they're back.
15. [ ] **Owner's decisions to ask when they're back (don't decide for them):**
    - Merge the NBA and FC Hubs into one Shorts Hub with channel tabs (idea 1 in `HANDOFF - playbook.md`)? The cloud recommends yes, keeping the old Hubs until they switch.
    - The owner shared a personal detail (their SAT result) and asked for it in the handoff; the cloud's safety check blocked saving it to the shared repo. Ask whether they really want it stored where all accounts read it; store it only on a clear yes.
    - Pause the cloud FC/NBA build routines while preflight is blocked, or keep them running as zero-credit data runs?
    - New Studio export (Content > Shorts, both channels): the newest is Nov 4 (FC) and Oct 24 (NBA), so "stayed %" on the Hubs is stale for every newer Short.
