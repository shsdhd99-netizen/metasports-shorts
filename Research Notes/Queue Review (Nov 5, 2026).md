# Queue review (Thu Nov 5, 2026, PC terminal)

Sources: `Research Notes/Schedule Ready Log.md`, `Tools/next_gap.py` (both channels), `STATE.md`, `Experiments.csv`, `Production Queue.md`, `UPLOAD SCHEDULE.md`, and the per-folder UPLOAD.md cards. The Oct "STATUS BOARD" in `Production Queue.md` is stale; this page is the current picture.

## 1. What posts when (ET)

| Day / time | Channel | Short | State |
|---|---|---|---|
| Fri Nov 6, 7:15 AM | NBA | #94 Rodman Number 69 | uploaded + scheduled (Nov 4, 6:30 job) |
| Fri Nov 6, 3:30 PM | NBA | #95 Lendeborg, "His Teammates Talked A Rookie Into Chasing 40" | uploaded + scheduled by the main PC session (Nov 5 6:47 AM) |
| **Sat Nov 7, 3:30 PM** | NBA | **OPEN gap** (`next_gap.py nba`) | the Fri 6:45 AM gap-fill run builds it; best candidate #97 (needs tonight's Heat result, see 3) |
| Sat Nov 7, 12:00 PM | FC | S29 goalkeeper who says Spain were scared of a shootout | uploaded + scheduled |
| Sun Nov 8, 12:00 PM | FC | S09 Ronaldo moved the Coca-Cola bottles | uploaded + scheduled |
| Nov 9 onward | FC | **no built Short**. Scripts exist: S31 baby Messi (copy-check TAKEN), S32 Hull fan (needs a second source for the 1998 table line), S30 Ballon d'Or penalty, S21 Higuita scorpion (FRESH), S22 Ceni (CROWDED), S36 Martinez law (TAKEN) | build in this order: S21, S30, S31, S32 |
| Nov 5-6 | FC | S27, S28 | already on YouTube (scheduled/posted, ids not yet public) |

Slot rules unchanged: NBA 7-8 AM or 3:30 PM, FC 12 PM, at least 6 h apart on one channel, never replace an upload.
Best next sequence for NBA: Sat Nov 7 3:30 PM (#97 or a fresh Fri-night game), then the Klay OT winner (banked by the cloud run), then Curry's chase of Oscar Robertson on the scoring list (NBA.com: 2 points short of 17th all-time on Nov 2; he may pass it before we post, so treat as a "passed" story only if it happens on camera).

## 2. The five "waiting NBA Shorts" are mostly stale, close them out
The Oct 15-19 board lists #10 v2, #45, #42, #36 v4, #46 as "waiting for the owner's ear". Per STATE and Daily Log (Nov 4): #42 was posted Oct 16; #36 v4 became the Oct 18 "LeBron's Rookie Teammate" Short; #10 is a script only (and its Oct 19-20 window passed); #45/#46 are not on this PC. **Owner action: remove them from the to-do list** (the old Desktop shortcuts "MetaSports - post these" are also Oct items: lottery balls, Jokic/Westbrook HOLD, Height Gap HOLD, Bronny, Hart, free throw, Giannis trade; archive or confirm each).

## 3. Needs a re-edit or a refresh with new info or the new rules
| Item | Why | Do |
|---|---|---|
| **#97 Warriors 0-3 then five straight** | facts are as of Mon Nov 2 (5-3); the Warriors host the Heat tonight (Thu Nov 5) going for six straight | Fri morning: if they won, the line is "six straight"; if they lost, drop or reframe. Then voice, cuts, QA. Use a counting number for the streak and the 37-win preseason line. |
| **#96 Porzingis** | health story; footage identity not verified; any update changes the Short | only build after verifying he is on screen frame by frame; drop it if there is a return date or a diagnosis report; say only what the team said |
| FC drafts that failed the new reuse lint (S09: 7 repeats, S27: 4 repeats + 40% one source, S28: 60% one source, S29: 2 repeats + 58% one source) | new guard | **Do not replace.** They are already uploaded and the Nov 4 study found no retention penalty. Apply the guard to the next builds only. |
| Next FC builds (S21, S30, S31, S32) | new rules | at least 2 sources, no source over 35%, a counting number for the payoff, hold the payoff number for the last 3 s, shots 1.6-2.2 s, footage at height<=1080 (disk permitting) |
| NBA builds from now | new rules + Dyson study | literal picture per phrase, the rejecter's/team's label on screen at the key beat, counting overlay for the proof number (`overlay.py count`, built Nov 5), no card in the first 4 s |
| S26 "gloves off" | strongest repeater (36 overlaps) yet 12,967 views in about a day | check its retention curve Nov 7 (API lags 2 days): the cleanest test of the repetition hypothesis |

## 4. Facts to re-check on posting day
- #95: Warriors 124-112 Clippers (Nov 1), 37 pts, 13-19, 6-11 3PM; three late misses; his quote; all sources in the folder's notes.md. Late-news risk is already accepted (scheduled Fri 3:30 PM).
- #94 Rodman: card by the main session; not re-verified here.
- S29/S09: scheduled; nothing to change.

## 5. Open slots and risks
- NBA: Sat Nov 7 3:30 PM open; Sun Nov 8 onward open.
- FC: nothing built beyond Nov 8; builds due by Fri Nov 6 for a Nov 9 post.
- Disk: C: about 9 GB free (preflight blocks under 5 GB). Big folders to review by exact path: `C:/Users/Admin/apps/SadTalker` (8 GB, only needed if LatentSync is dropped), `C:/Users/Admin/apps/max_job/`.
- Hub: 1 GB asset store was full on Nov 4; `Tools/hub_pack.py` packs a DRAFT under 20 MB but nothing is uploaded until the owner approves deleting superseded assets by exact id.
- Voice credits: 67,649 of 121,224 characters left (resets Nov 18); a Short costs 1.2-4K.
- YouTube keys are missing in the cloud environment: both cloud routines (NBA 3:17, FC 4:23) hit "blocked" on Nov 5. The PC timers do the real work until the owner runs `Tools/copy_cloud_env.ps1`.
