# Overnight log: resume here (Oct 14, 2026, about 11:55 PM ET)

**Claude stopped because the usage limit was reached.** Grok continued after that, because the limit was confirmed and the owner was asleep. Nothing was published, scheduled, or deleted. No keys were printed. No new voice was generated.

## Grok, after the limit (Oct 14 night)

- **Merge is committed and pushed.** Desktop `main-329h3w` is `d88a2d0` on origin. The PC upload notes, lessons, and outcome log were kept, with the cloud text appended under "Cloud copy (merged Oct 14)". Short 25 keeps the PC captions and effects; the cloud versions sit beside them as `captions (cloud Oct 15).ass` and `sfx (cloud Oct 15).json`. The channel log is the union, 8 rows. The 28 local `READY TO POST` files stayed untracked.
- **Backup** is still `C:\Users\Admin\Documents\YouTube-Playbooks-backup-20261014`.
- **`sync_verify.py` reported 1,050 "wrong"** because Git checked the text files out with Windows CRLF. The git blob for `00 START HERE.md` matches the manifest hash. The cloud copy does not need to be retired on that report. Two files matched as kept-desktop twins (the Short 25 sidecars).
- **#44 footage is on the PC.** Three NBA posts were downloaded into that folder's `src/`, and 8 clips were cut with the logged in-points: `M0`, `A1`, `A2`, `A3`, `A4`, `D0`, `D1`, `D2`. Frames were checked: media-day Flagg, Macao autographs, Macao with the ball, and #32 driving and dunking against Cleveland (79-61, 3rd). The three proof cards (`C1`, `C2`, `C3`) are not on disk, so the master was not re-rendered.
- **#42 sources are in that folder's `src/`.** The LeBron file is a real airball, not a rim clank. The Kobe file is the official NBA fadeaway video and is not cut yet.
- **Not done:** `channel_check.py`, a published-ID tracker, QA on the unposted READY files, a #44 re-render, and any Hub edit. Voice is still A or F. ElevenLabs was not touched.

The notes below are Claude's stop-note from before the merge. That merge was finished in the section above. Do not abort it again.

## What is done
- **Backup of the whole desktop project:** `C:\Users\Admin\Documents\YouTube-Playbooks-backup-20261014` (5,415 files, 10.7 GB, 0 failures).
- **Desktop state preserved in git:** commit `31a4546` on the desktop's branch `main-329h3w` (the desktop repo is `C:\Users\Admin\Documents\YouTube-Playbooks`).
  - It holds the PC's uncommitted work: Oct 5-13 Research Notes, `_v2/_v3/_v4` revision folders, productions #26-#30, tool edits.
  - It leaves out the 28 `READY TO POST*.mp4` files, which stay on disk and are in the backup.
  - 229 text files were scanned first: no API keys or tokens.
- **Merge of the cloud branch tried and ABORTED on purpose.** The desktop repo is clean (HEAD = `31a4546`, no merge in progress). `origin/main-329h3w` is 84 commits ahead.
  - Only 16 files conflict. `Tools/assemble.py`, `Tools/captions.py` and the skill files merged cleanly.
- **This clone** (`C:\Users\Admin\Documents\metasports-shorts`) = the cloud branch exactly. It has no media and no `Tools\.env`.

## The merge, when you resume (decisions already made)
In `YouTube-Playbooks`: `git merge origin/main-329h3w --no-commit --no-ff`, then resolve the 16 conflicts like this:
| Files | Resolution |
|---|---|
| 12 × `Productions/.../UPLOAD.md` (#11, 13, 14, 15, 17, 20, 21, 22, 23, 25) and #22 `notes.md` | Keep the **PC (ours)** text in place. Move the cloud's text to a section at the end: "Cloud-copy notes (merged Oct 14)". The PC holds the matching videos. |
| `Research Notes/Lessons Learned (running log).md`, `Research Notes/Outcome Log.md` | Keep **both**. Ours first (PC entries, Oct 5-13, including the Oct 10 Studio readings), then a labelled "cloud copy" section (cloud entries, Oct 13-15). Give the cloud's Outcome Log table rows their own header. |
| `Tools/data/channel_log.csv` | Union of rows, de-duplicated, sorted by date. |
| #25 `captions.ass`, `sfx.json` | Keep **ours** (the PC's render). Save the cloud's as `captions (cloud Oct 15).ass` and `sfx (cloud Oct 15).json`. |

Then:
1. **Repair mojibake.** Many PC `UPLOAD.md` titles have double-encoded emoji (`ðŸ¤¯` instead of the emoji). Re-decode them: bytes from cp1252, decoded as UTF-8; map U+0080-009F to the same byte.
2. **Commit** the merge, then check it with `python Tools\sync_verify.py verify C:\Users\Admin\Documents\metasports-shorts C:\Users\Admin\Documents\YouTube-Playbooks`. Files that were merged by hand will show as "wrong"; that's expected. Everything else should be identical.
3. **Push** only text. Never `git add` the READY TO POST mp4s (about 1.2 GB), and never a key.

## Things found that change the plan
- **The PC already knew "stayed %" is the gate** (its bar is 80%: #22 got 82.4% and #03 got 80.1%). Its notes are the best record of Oct 5-13: `Research Notes/Performance Audit (Oct 10, 2026).md`, `Creation Process (Oct 10, 2026).md`, `Refinement Backlog (Oct 10, 2026).md`, `Unposted Frame Check (Oct 10, 2026).md`, `Improve Next (Oct 10, 2026).md`. They are in the desktop folder now and will be in git after the merge.
- **Two numbering schemes collide.** On the PC, #26-#30 are "One-Second Height Gap", "Worst Team Gets Fewer Balls" (lottery), "Hart Added One Extra Line", "The NBA Final That Does Not Count" (posted Oct 5), and "Heave Miss Is Free". In the cloud, #26-#35 are different titles. **Match posted Shorts by YouTube ID, never by number.**
- **The PC's picture gate** (the unusual fact must be visible at 0.2 s without the caption; no top headline; at most 5 effects, none in the first second) agrees with the cloud's rules.
- **The PC's own backlog says:** #27 lottery needs a rewritten script before any voice; #30 and #06 need new footage; #02, #04, #05, #07, #08, #09, #10, #23, #26, #28 are rejected or held. The next new premise it picked was the 14-second shot-clock reset ("Improve Next").
- **Rendering on the PC:** Drift is installed (`C:\Program Files\Drift\drift.exe`), so `assemble.py` will use it unless you force the ffmpeg engine. An NVIDIA GPU is present. ffmpeg, yt-dlp, node and Python 3.12 are installed. YouTube downloads should work here (they were blocked in the cloud).
- **#44 (Cooper Flagg) draft:** its final video exists only in the cloud container and in the Hub (compressed copy). Its script, voice, shots and proof cards are in git (branch `main-329h3w`). Re-cut the clips on the PC (`x_clip.py` works) to regenerate the master.

## What is left (in order)
1. Do the merge above; verify; push text only.
2. Run `channel_check.py` on the PC to get the true published list with YouTube IDs; build ONE tracker (ID, URL, date, title, views, stayed %, status). Reconcile with `Table data.csv` and the queue. Record that #21 Jokic and #40/#41 were posted by you.
3. Run `qa_short.py --full` on every unposted READY file on the PC (it has the real clips) to find repeated or looping footage; fix the worthwhile ones in new versioned folders (never overwrite a READY file, per the Grok protocol in each folder's `GROK_CLAUDE_SYNC.md`).
4. Improve #36 (find a sharper official rookie-LeBron source now that YouTube works here) and #44 (a better source than the 720p NBA post).
5. Voice credits: 3,548 characters left (resets Nov 8). Reuse existing voices where possible.
6. Update the Hub (a claude.ai page; this session had no tool for it) and START HERE.

## Needs you
- Voice: A or F. OK on #36's fan-account clips. Approve or change #44. Nothing may be posted without you.
