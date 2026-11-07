# Team handoff: three accounts + the cloud (Nov 6, 2026)
Read this once. Each session's start prompt repeats the short version, plus its unread messages.

## Who is who (the label is on the window title, every commit, the board and the handoffs)
| Label | Account | Job | Where | Never |
|---|---|---|---|---|
| **A1** | Account 1 | **Builder**: voice, render, QA, Hub card, schedule | PC, `Documents/metasports-shorts` | runs at the same time as A2 |
| **A2** | Account 2 | **Builder (backup)**, when A1 is out of usage | same folder as A1 | runs at the same time as A1 |
| **A3** | Account 3 (new Pro) | **Prep + Review**: scripts, sources, footage plans, draft reviews, 72-h judgments, approved tool fixes | PC, its own copy `Documents/metasports-prep` | voices, renders, uploads, touches slots |
| **CLOUD** | the claude.ai app session (on **Account 1's** usage) | research run (3:43 AM ET), stats (6:08 PM ET), re-plans, studies, what the owner asks from the phone | cloud | builds anything that needs YouTube footage |
Start on the PC: Desktop icons **Claude A1 - Builder**, **Claude A2 - Builder backup**, **Claude A3 - Prep and Review** (from `Tools/make_shortcuts.bat`), or `bash Tools/claude_acct.sh 1|2|3`.

## How they talk (`python Tools/team.py ...`, everything goes through git under `Team/`)
- `inbox`: unread messages for me (`--ack` once acted on). Check it at the start of a session and after every task.
- `claim "<task>"`: before starting any Short or task. If someone holds it, the command refuses: pick something else. This is what stops double builds.
- `done "<task>"`: releases the claim and logs it under "done today". **Name the file you made** ("S30 prep: Soccer Channel/Productions/...").
- `status "now" "next"`: whenever you switch tasks.
- `say A1|A2|A3|CLOUD|BUILDER|ALL "..."`: hand something over ("Klay DRAFT pushed, review please"; "REVIEW: FIX x2 in S30").
- `board`: prints everyone's status, open claims, unread counts and the last messages, and rewrites **`TEAM BOARD.md`** (the owner's one-glance view; also pasted into `HANDOFF - latest.md`).

## The daily rhythm
| Time (ET) | Who | What |
|---|---|---|
| 3:43 AM | CLOUD | research run: last night's moments, soccer picks, competitor outliers; messages BUILDER the top pick |
| 6:30 AM | scheduler | uploads any Short with a slot + Arm + QA PASS |
| 6:45 AM | A1 | gap-fill: builds last night's moment for 3:30 PM, then the next planned Short (PREP-ready folders first) |
| 7-9 AM | A3 session 1 | reviews everything A1 pushed overnight (REVIEW.md, messages BUILDER), then preps 2 days ahead |
| 12 PM / 3:30 PM / 7:15 AM | YouTube | posts go live (FC 12 PM; NBA 7:15 AM planned, 3:30 PM fresh moment) |
| 6:08 PM | CLOUD | daily stats + retention, Outcome Log |
| 6:30 PM | scheduler | second upload pass |
| 7-9 PM | A3 session 2 | 72-h judgments; NBA record-list prep; after the games, a 3-pick moment shortlist with clip ids to BUILDER |

## A3: how to use the third account fully (targets are on the board)
- **Keep 4+ Shorts prepped ahead on each channel**, so A1 never researches; a build then takes about 30 min.
- **Review every DRAFT within 6 h** of it being pushed. Track the FIX rate; the builder fixes before scheduling.
- **Judge every Short at 72 h** (stayed %, the 90% hold ratio, views vs the last 10). One tiered lesson each.
- **One owner-approved refinement a day**, tested before committing (first in line: the autopilot skill rewrite, if approved).
- "Meaningful" = every `done` names a file. A day with no prepped folder, REVIEW.md or judgment logged is a wasted day.
Full rules: `Research Notes/ACCOUNT 3 - Prep and Review.md`.

### A3's first queue (from the two-week plan; A1 builds S30, S21, Klay and #92 today, so A3 starts after those)
1. **Review** the Klay DRAFT (Sat 7:15 AM) as soon as A1 pushes it; then S30 Kane and S21 Higuita.
2. **Prep NBA List 1** for Tue Nov 10 7:15 AM: "Who has missed the most free throws in NBA history?" (Basketball-Reference career FTA minus FT; copy-check; our two "most missed" lists did 24-25K).
3. **Prep FC new keeper 1** for Wed Nov 11: Bounou and Spain's 2022 shootout (2+ sources; the "Spain practised 1,000 penalties" line only with a quote).
4. **Footage plan for S22 Ceni** (Thu Nov 12) and **S31 Baby Messi** (Fri Nov 13): scripts exist; add the cuts plans, re-check copy, and lead S31 with a new angle (copy-check said TAKEN).
5. **Prep NBA List 2** (turnovers, Fri Nov 13) and **FC keeper 2** (Livakovic v Japan 2022, Sat Nov 14).
6. **Check #59 WNBA**: is the pay-deal (CBA) line still true for Sat Nov 14? Write the answer in its notes.md and message BUILDER.

## Builders (A1/A2): what changes
- Build **PREP-ready folders** (`PREP: ready to voice` on line 1 of notes.md) before researching anything new.
- Apply a folder's **REVIEW.md** fixes before it's scheduled. If you disagree, reply with `say A3`.
- Claim before building; `done` after pushing; tell A3 when a DRAFT is pushed.
- Today's list: `TERMINAL TO-DO (Nov 7).md` (Nov 6 list kept for history).
