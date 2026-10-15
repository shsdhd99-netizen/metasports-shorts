# Moving the cloud work back to the desktop (prepared Oct 15, 2026)

**Status: NOT DONE YET.** This cloud session can't reach your PC (`C:\Users\Admin\Documents\YouTube-Playbooks`), so nothing on the desktop has been changed. Everything below is ready for the move. The cloud copy stays in place until the desktop copy is verified.

## Easiest: let Claude do it on the PC
1. Open **Claude Desktop** on the PC, or open a terminal **in the desktop project folder** and run `claude remote-control`.
2. Say: *"Sync the cloud branch main-329h3w into this folder using DESKTOP SYNC - read on the PC.md."*
3. That session can see both copies, run the steps below and merge any file both sides changed by reading the two versions.

## By hand (about 10 minutes; Windows)
**What moves:**
- **The whole cloud copy:** 1,733 files, about 1.17 GB.
  - every doc, research note, tool, script and production folder in the git branch
  - **its media is the voice files, cards and images only; video stays out of git**
- **The draft videos** (#21 v5 and #36 v2 in voices A and F, plus the new drafts): download them from their **Hub cards**, https://claude.ai/artifact/EZrk8n855PyYpMFnMnMJd4.
- **Not moving:**
  - the cloud's working clips and downloads (about 6.9 GB of video, not in git). Ask if you want a specific production's clips, and I'll find a way to send that folder.
  - **keys:** `Tools/.env` never leaves either machine

**Steps:**
1. **Get the cloud copy** (any folder *outside* the project, e.g. Downloads):
   ```
   git clone --branch main-329h3w https://github.com/shsdhd99-netizen/metasports-shorts "%USERPROFILE%\Downloads\metasports-cloud"
   ```
   No git? On GitHub, open the repo, switch to the branch `main-329h3w`, then Code → Download ZIP, and unzip it there.
2. **Back up the desktop folder** (the plan step prints this command too):
   ```
   robocopy "C:\Users\Admin\Documents\YouTube-Playbooks" "C:\Users\Admin\Documents\YouTube-Playbooks-backup-20261015" /E /COPY:DAT /R:1 /W:1
   ```
3. **See the plan; nothing changes yet:**
   ```
   python "%USERPROFILE%\Downloads\metasports-cloud\Tools\sync_verify.py" plan "%USERPROFILE%\Downloads\metasports-cloud" "C:\Users\Admin\Documents\YouTube-Playbooks"
   ```
   - It writes `SYNC PLAN (cloud Oct 15).csv` in the project folder. Each cloud file is one of:
     - **new:** copied
     - **same:** nothing to do
     - **differs, desktop older than Oct 3:** replaced, since it can't contain newer desktop work
     - **differs, desktop changed since Oct 3** (by you or Grok): **kept**, with the cloud version saved beside it as `<name> (cloud Oct 15).<ext>`
   - Desktop-only files (your media, Grok's renders, `.env`) are counted and **never touched**.
4. **Apply:** the same command with `apply` instead of `plan`.
5. **Verify:** the same command with `verify`.
   - It re-hashes every file against `Tools/sync_manifest.csv` (SHA-256).
   - **"VERIFIED: every cloud file is on the desktop"** means the move is complete.
   - Anything else lists what's missing; don't retire the cloud copy.
6. **Review the "(cloud Oct 15)" twins.** For each pair, keep the newer content or merge the two. The cloud versions of the Playbook, Production Queue, START HERE and Research Notes are the current canonical ones unless you or Grok changed the desktop copy after Oct 3.
7. **Check one render works on the PC:**
   ```
   python Tools\qa_short.py --folder "Productions\MetaSports\2026-10-06 36 How Long Was LeBron Pro Before Boozer Was Born\_v2" --full
   ```
   - Its video isn't in git, so expect "final.mp4 not found" until you put the Hub download there.
   - The docs and tools part is verified by step 5.

**Tested in the cloud (Oct 15):** plan, apply and verify ran on a simulated desktop: an older copy plus a desktop-only file plus a Grok-style edit.
- 13 new files were copied and 1 older file was replaced.
- 20 changed files were kept, each with its cloud twin.
- The desktop-only file and the Grok edit were untouched.
- Verify said VERIFIED.

The real desktop hasn't been tested, because it isn't reachable from here.

## After it's verified
- Say "desktop verified" in chat. Until then, the cloud branch and its media stay as they are.
- Deleting the cloud copy is your call, and only after that message.
