# Handoff playbook (hand-written; `Tools/handoff.sh` copies it into every `HANDOFF - latest.md`)
Last edited Sat Nov 7, 2026 by the CLOUD session (owner asked: "make your handoff have more detail with how to do tasks etc. and new things to try in the backend"). Edit this file, not the generated handoff, when a how-to or an idea changes.

## 1. About the owner (facts they shared; use them, don't re-ask)
- (Personal detail the owner asked to add on Nov 7 is held back pending the owner's OK to store it in the shared repo.)
- Wants **one all-in-one place** for the Shorts work: the Shorts Hub should hold drafts, performance, schedule, to-dos and ideas together, "similar to how I want the website". Build toward that; ask what the website should hold before designing it (no spec in the repo yet).
- Works from the phone a lot: pages must read at phone width, steps short, Copy buttons for anything to paste.
- Standing rules: never post, schedule or replace outside `Tools/schedule_ready.py` guard rails; never open YouTube Studio; never print, commit or ask for keys; never invent a stat; no teaser or promo at the end; every Short under 59.5 s; at most 2 posts a day per channel, 6+ h apart. YouTube first: TikTok/Instagram cuts are paused until the owner says so.

## 2. Where everything is
| What | Where |
|---|---|
| NBA Hub (drafts, performance, coming up, to do, ideas) | https://claude.ai/artifact/SAWcHwuAwBxJuyBQSs8a8U |
| FC Hub (same layout) | https://claude.ai/artifact/2UVAcbNpKq6j4YXBEF8ge3 |
| Both-channel tracker dashboard | https://claude.ai/artifact/6kpu5HUkFtCzyFNjNCTPVv |
| Other account's Hubs and task list (only that account can open them) | NBA EZrk8n855PyYpMFnMnMJd4, FC LFsQtwomdpLAshoz4Xw62H, tasks Ki1UXnbxsdykE4dy7BwyLT |
| What goes live when | `Research Notes/Coming Out.md` (`python Tools/coming_out.py`) |
| Open slots + plan | `Research Notes/Auto Queue.md` (`python Tools/queue_rank.py`), `python Tools/next_gap.py nba|fc` |
| Rules | THE RULES in `MetaSports - Playbook.md`, `Soccer Channel/Playbook.md`, `CLOUD DAILY RULES.md`, `.claude/skills/daily-run/SKILL.md` |
| What the data says | `Research Notes/Learned Weights.md`, `Soccer Channel/Lessons Learned.md`, `Research Notes/Lessons Learned (running log).md` |
| Team protocol | `TEAM HANDOFF.md`, board `TEAM BOARD.md`, `python Tools/team.py inbox` |
| Today's terminal list | newest `TERMINAL TO-DO (<date>).md` |

## 3. How to do each task (step by step)

### Start any session (2 min)
1. `git pull --no-rebase origin main-329h3w`
2. Read `HANDOFF - latest.md` (this file is inside it), then the newest entries of `Research Notes/Daily Log.md`.
3. `python Tools/team.py inbox` (act, then `--ack`); `python Tools/team.py status "now: ..." "next: ..."`.
4. `bash Tools/cloud_setup.sh` (cloud) and `python Tools/preflight.py --quiet`. BLOCKED means script and notes only, no voice credits.

### Fill an open slot
1. `python Tools/next_gap.py nba` (or `fc`): it prints the next uncovered slot within 54 h.
2. `python Tools/team.py claim "<slot> <idea>"`. If it refuses, someone has it: pick another.
3. A folder whose notes.md line 1 says `PREP: ready to voice` goes first (Account 3 prepped it). Apply its `REVIEW.md` fixes if one exists.
4. Otherwise pick from `Research Notes/Idea Candidates.md` / the newest `Research Notes/Daily Research/<date>.md`: `python Tools/idea_gauge.py ...`, `python Tools/copy_check.py "<4-6 words>"` (FRESH only), confirm footage exists, then `python Tools/build_gate.py <ch> --shape <shape> --score <n>` must say BUILD.
5. Build (next two recipes), QA, Hub card, schedule, `python Tools/team.py done "<task>"` naming the folder.

### Build an NBA Short (20-30 s, a moment or a planned idea)
1. Script with `/nba-short`: line 1 at most 11 words, one fact the clip can't show, end on the payoff. Sources with exact words in notes.md.
2. Footage: `python Tools/nba_videos.py search --player <id> --q "<play>"`, `python Tools/x_clip.py <x links> --out src` (official accounts), archive.org. The cloud can't download from YouTube: add a line to `Research Notes/PC Requests.md` instead.
3. Voice: `python Tools/voiceover.py` (Alex voice; `--check` shows credits left); pace 240-260 wpm.
4. Cut: write cuts.json (frame 1 shows line 1; shot 1 at least 2 s; replay the key second once; wide plays `"blurfit": true, "blurfit_aspect": 0.75`), then `python Tools/cut_list.py --folder "<F>"`, `python Tools/shot_strip.py "<F>" strip.jpg` and look at it.
5. Real broadcast call available? Also render `python Tools/nat_sound.py ...` and post that one.
6. `/assemble` renders; then QA (below).

### Build an FC Short (50-59.5 s, story)
1. `/story-short`: goalkeeper-and-shootout stories first (5 of 5 at 15K+ at 72 h; everything else 1-3K). Title read aloud as line 1; a turn every 8-12 s; hard-number or ironic payoff; nothing after it.
2. Render **music and no-music** versions (open A/B test; log which one is posted).
3. Footage from X, archive.org, Mixkit or ESPN public clips; YouTube-only clips go to `PC Requests.md`.

### QA and ship
1. `python Tools/qa_final.py "<F>"` must say **SHIP** (it runs qa_short --full, portions, file checks, slot clash, stale wording).
2. Look yourself at frame 1, every overlay and the last frame (`python Tools/frame_sheet.py <mp4> --from 0 --to 3 --every 0.5`).
3. Optional: `python Tools/comfort_audit.py <mp4>` (loudness, flashes) and, with GEMINI_API_KEY, `python Tools/yt_watch.py "<mp4>" --precheck`.
4. Package in UPLOAD.md: short statement title, empty description, tags filled to about 490 characters (`python Tools/tags_fit.py "..."`), pinned-comment question, cover.

### Put a Short on its Hub
1. Upload a 1.5 Mbps copy as an asset (Artifact publish, `url` = the Hub, `asset: true`).
2. Read the card first, then write collection `shorts`, doc `<code>`: code, name, num, status (`ready` / `editing` / `posted`), slot, slotLabel, versions [{label, assetId, note}], titles, tags, postNote. Pin every write with `if_version`. Never overwrite numbers the owner typed in `results`.

### Schedule (only an approved Short)
1. Approved = Hub card `approved: true` or the owner's own words.
2. `python Tools/schedule_ready.py` (dry run: what it would schedule and why others are skipped), then `--go`. Then `python Tools/coming_out.py`.

### Read the numbers and judge a Short
1. The Hub's **How the Shorts are doing** section (or the tracker dashboard) has every Short: views, × channel median, verdict, stayed %, engaged %, avg % viewed, retention curve vs the channel median, views per day.
2. Judge at **72 h**, never the next morning (breakouts come on day 2-3). Write one tiered lesson ([V] measured, [S] seen, [H] guess) in the channel's Lessons Learned; a rule changes only with n and medians.
3. `python Tools/learn.py all` refreshes `Learned Weights.md` (lanes ABOVE / PAUSE).

### Refresh the tracker by hand (it also runs itself at 8:37 AM and 7:13 PM ET, scheduled task "MetaSports tracker refresh")
1. `python Tools/short_tracker.py` (add `--no-public` if yt-dlp is blocked).
2. Upload `Research Notes/Tracker/hub_nba.json` to the NBA Hub and `hub_fc.json` to the FC Hub as assets; set each Hub's db doc `tracker/current` to `{asset, updated_utc, file}`; delete the old asset.
3. Dashboard: upload shorts/history/retention/upcoming.json and repoint `datasets/<id>`.
4. Changed the Hub template? `python Tools/hub_tracker_block.py <hub index.html> nba|fc <other hub url> <out.html>` re-adds the tracker block (it replaces its own block between the MT markers).

### Studio export arrives (owner's weekly zip)
1. Unzip into `Research Notes/Studio exports/Content <from> to <to> <NBA|FC>/` (keep `Table data.csv`).
2. `python Tools/shorts_dataset.py --report`, then refresh the tracker: stayed % fills in on the Hubs.

### Cloud run blocked at preflight
- Missing YouTube secrets in the cloud environment: write the script and notes only, log `STATUS: blocked`, spend no credits. Fix is the owner's: `Tools/copy_cloud_env.ps1` on the PC, then paste YT_CLIENT_ID, YT_CLIENT_SECRET, YT_UPLOAD_TOKEN, YT_UPLOAD_TOKEN_FC into the cloud environment settings. Never paste keys in chat or git.

### End a session
1. Update `Research Notes/STATE.md`, add a `STATUS:` line to the Daily Log, commit and push.
2. `bash Tools/handoff.sh "<app|PC> account <1|2>" "<done / next>"`.

## 4. New things to try in the backend (ideas, not built yet; pick one, say which in the Daily Log)
| # | Idea | Why | Effort |
|---|---|---|---|
| 1 | **One Shorts Hub for both channels**: merge the NBA and FC Hubs into one page with channel tabs, the tracker, the schedule and the owner's task list | the owner's "all in one place"; today there are 2 Hubs + a dashboard + a task list on another account | medium: new page reading both channels' collections; keep the old Hubs until the owner switches |
| 2 | **Fill Hub results automatically** from the tracker (views, stayed or engaged, avg %) when a card is `posted` | the owner no longer types numbers; cards and the tracker agree | small: the refresh writes `results` only where the owner left it empty |
| 3 | **Predicted stayed %** from engaged % (39 Shorts have both): a fitted line with its error shown as a range, labelled as an estimate | stayed is the gate (74%+) but Studio-only and weekly | small; never shown as the real number |
| 4 | **Breakout alert**: at 24 h, a Short above 2× the channel median gets a push note and a "Part 2 / follow-up" idea queued for the next slot | breakouts come on day 2-3; a quick follow-up rides the wave | small (tracker + `PushNotification` or team message) |
| 5 | **Retention drop finder**: where a curve falls more than 0.15 below the channel median, make a frame sheet of that second and attach "what's on screen" to the card | turns curves into edit fixes | medium (`frame_sheet.py` needs the DRAFT on the machine) |
| 6 | **Prediction vs result**: log `lab.py predict`'s score at build time; show predicted vs actual on the Hub at 72 h | tells us if the scoring helps (NBA rho 0.29 today) | small |
| 7 | **Lane wear-out monitor**: rolling median of each lane's last 3 posts; flag at 2 under 5K (the goalkeeper series is the one to watch) | the template-collapse risk every channel hit | small, in `learn.py` |
| 8 | **Footage index**: a cached list of downloadable clips per star (NBA.com team sites, X, ESPN, archive.org) | the slowest build step is finding clips | medium |
| 9 | **One set of daily runs**: the cloud routines and the PC routines overlap; give the cloud research + stats + tracker, the PC builds | fewer skipped/blocked runs and duplicate logs | small (routine prompts + BUILDER.md) |
| 10 | **Weekly digest page** on Sundays: top 3 / bottom 3 with reasons, the rule kept and dropped, auto-built from the tracker | the Sunday review, readable on the phone | small |
