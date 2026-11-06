# Account 3: prep + review (set up Nov 6, 2026)
Why: Accounts 1/2 are the one BUILDER (voice, render, QA, schedule). Most of a build's 60-90 min goes on research, the script and finding footage. Account 3 does that ahead of time, and reviews each finished DRAFT with fresh eyes. So the builder only voices, cuts and checks (about 30 min a Short), and fewer mistakes go out.
Account 3 runs in its own copy of the repo (`~/Documents/metasports-prep`, made by `bash Tools/claude_acct.sh 3`), at the same time as the builder.

## Never (these belong to the builder)
- No ElevenLabs: `voice_take.py`, `voiceover.py`, `retake_sentence.py`, `revoice.py` (voice credits are shared, and only the builder spends them).
- No renders or uploads: `assemble.py`, `nat_sound.py`, `yt_schedule.py --go`, `schedule_ready.py`.
- Never edit `BUILDER.txt`, `Research Notes/Scheduled Uploads.csv`, any `DRAFT*.mp4`, the Hubs or the task list.
- Never `git add -A`. Add only the files you wrote, by path. `git pull --no-rebase` before every push; never force-push.
- No keys in chat or git. The usual owner rules apply: never post, never open Studio, never invent a stat, keep qualifiers.

## Team protocol (label A3; see `TEAM HANDOFF.md`)
Start: `python Tools/team.py inbox` (act, then `--ack`). Before each item: `team.py claim "<task>"`. After: `team.py done "<task>: <file>"`. After a review: `team.py say BUILDER "REVIEW <folder>: GO" or "FIX: ..."`. After prepping: `team.py say BUILDER "PREP ready: <folder>"`.

## The loop (in this order, every session)
1. **Review every new DRAFT** (one the builder pushed in the last 48 h with no `REVIEW.md` next to it):
   - extract frames at 0.3, 1, 2, 3, 5 s, then every 5 s, plus the last 1 s (`ffmpeg`), and LOOK at them;
   - read `script.txt` against `notes.md`'s source table (every number, date and name);
   - run `python Tools/qa_short.py --folder F --video <draft>`;
   - run `script_lint.py`;
   - apply `Tools/critic_v2.md`.
   Write `REVIEW.md` in the folder: **GO** or **FIX**, at most 3 fixes, each with the evidence (a frame time, the source line). Check hardest:
   - frame 1 shows the promise;
   - the named person is on screen when named;
   - no stale words ("this season", "just", "tonight");
   - the payoff is in the last 2-3 s and held on screen;
   - pace is 230-260 wpm;
   - the copy-check is still clean.
2. **Prep the next empty slots** in `Research Notes/Two-Week Plan (Nov 7-20, 2026).md`, soonest first, aiming at 4-5 prepped Shorts ahead per channel:
   - a folder named `<slot date> <NN or SNN> <Title>` (NBA under `Productions/MetaSports/`, FC under `Soccer Channel/Productions/`);
   - `script.txt` (NBA 22-25 s: about 90-105 words at 240-260 wpm; FC 230-250 words, under 59.5 s; numbers spelled for the voice `{6-1|six-one}`);
   - `notes.md` with a claims table (claim, source URL, exact quote; 2+ sources for every FC story);
   - `title_caption.txt` (FC);
   - `UPLOAD.md` draft (title = line 1, 3-8 tags, pinned comment, and a `**Slot:**` line);
   - a footage plan: `cuts_plan.json` or `clips_manifest.json` with each shot's source and second range (ESPN video ids, X posts via `x_clip.py`, archive.org, or YouTube preview frames from `yt_sheet.py`); frame 1 must show the promise.
   Run `copy_check.py` (TAKEN means drop or re-angle), `idea_gauge.py` and `script_lint.py`. Then put `PREP: ready to voice (account 3, <date>)` as the first line of notes.md.
   Use the study rules:
   - NBA: a watchable moment or a star record list; FC: keeper/penalty first.
   - The "rejection ladder" and "first in N years" payoff devices.
   - A Why/How/What opener for explainers.
3. **Judge at 72 h**: for each Short posted 3 days ago, run `python Tools/test_log.py result ...` (stayed %, the 90% hold ratio, views vs the channel's last 10). One tiered lesson per Short in `Research Notes/Lessons Learned (running log).md`.
4. **Refine** only what the owner approved (for example `Research Notes/Autopilot Skill - Proposed Edits (Nov 6, 2026).md` once the owner says yes). Each tool change gets a test run before the commit.

## End of session
`bash Tools/handoff.sh "PC account 3" "<prepped: ...; reviewed: ...; next: ...>"`. This writes `HANDOFF - prep (account 3).md`, never the builder's handoff.
