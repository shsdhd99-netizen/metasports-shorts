# Account 2 log

Newest at the bottom. Each session: date, what was done, credits used (`voiceover.py --check` before and after), tool changes, ideas for the idea banks (the main account adds them), and anything only the owner can do.

## Fri Oct 30, 2026, ~7:15 PM ET (first Account 2 session)
- Owner shared the handover page and said the main account's usage is out for now.
- Checked out `account2` and merged `origin/main-329h3w` (7 commits, up to the FC daily run Oct 30). No conflicts.
- **Blocked, owner setup not done in this environment yet:** network access is not Full (ESPN API and archive.org both refused by the proxy) and neither `ELEVENLABS_API_KEY` nor `GEMINI_API_KEY` is set. No footage, voice or Gemini work is possible until both are fixed. Credits: not checked (no key).
- Nothing built, nothing added to the queue. Credits used: 0.
- Owner only: set this account's environment network to Full and add the two secrets (section 2 of the guide).

## Sun Nov 1, 2026 (PC session, tool fixes)
- `Tools/deflash.py`: frames now stream through pipes (flash check uses a 3-frame window; the rewrite decodes and encodes frame by frame) and the audio is stream-copied from the source (`-map 1:a? -c:a copy`). Tested on a 16 s 1080p Short copy (audio kept, 4.5 s) and on a synthetic clip with one white frame (found at 1.000 s, replaced, re-check shows 0).
- `Tools/footage_qc.py`: the story allowance (archive blow-ups up to 6x) now also applies with `--profile story` on the command line (so `qa_short.py --profile story --full` passes it through) or env `FOOTAGE_PROFILE=story`, as well as folders under "Soccer Channel". Checked the detector returns True with that flag; default behaviour unchanged.
- `Tools/assemble.py`: `--out-name` now works on both engines (the Drift path wrote final.mp4 regardless). Temp files are per output (`_final_tmp_<name>.mp4`, `_shots_tmp_<name>`, `final_nocap_<name>.mp4`; the default `final.mp4` keeps the old names). New lock file `_render[_<name>].lock` per output: a second render of the same output in the same folder stops with a message; a lock over 2 h old counts as stale; the lock is removed on exit. Tested the lock and the missing-input path in a temp folder; I did not run a full render (the main session is rendering). Not covered: preview_N.jpg and storyboard.jpg are still shared between two outputs in one folder.
- Same session: wrote `Jokic Record Prebuild.md` (voice-ready), `Milestones.md`, `Footage Sources.md` (PC reaches YouTube via yt-dlp; NBA.com is blocked 403), `Competitors 2026-11-01.md` (18 channels, titles only, no Gemini watches), `GTA6 Plan.md` (Rockstar policy page fetch timed out twice; section 3 is from search summaries). Credits: no voice used. The task list file `Terminal Handoff.md` named in the brief does not exist; I used `ACCOUNT 2 - START HERE.md` section 7 instead.
- Idea for the banks: three-angle runs on one live topic (Ahmed's Goal's Ballon d'Or run); a goalkeeper news hook is the version that fits our lanes.
