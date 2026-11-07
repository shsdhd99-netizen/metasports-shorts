# Moving this to another Claude account or subscription

**Two ways:**
1. **Claude Code (recommended):**
   - Give the new session this GitHub repo (`shsdhd99-netizen/metasports-shorts`).
   - The skill loads from `.claude/skills/story-short/`, and the tools are in `Tools/`. Nothing else is needed.
2. **Claude.ai (no repo):**
   - Upload `Soccer Channel/story-short-skill.zip` in Settings -> Capabilities -> Skills.
   - The zip holds these instruction files and the format study. The tools it calls still live in the repo, so for rendering use option 1.

**What the new account needs (the owner sets these; never paste keys into chat):**
- **ElevenLabs API key:** an environment secret (`ELEVENLABS_API_KEY`) in the cloud environment's settings, or `Tools/.env` on a PC (git-ignored).
  - Creator plan: 100K credits a month, about 30 Shorts at 2 takes each.
- **The voice:** "Alex - Upbeat, Energetic and Clear" from the ElevenLabs Voice Library (voice_id `yl2ZDV1MzN4HbQJbMihG`).
  - A new ElevenLabs account must add it to My Voices once. Settings are in `Tools/voice_config.json`.
- **Network access set to Full** in the cloud environment, for archive.org, Mixkit, BBC and Wikimedia.
- **Fonts** are in the repo (`Tools/fonts/`, OFL): TikTok Sans for the captions; Caveat is in the S01 assets.
- **Python packages:** `bash Tools/cloud_setup.sh` installs them; ffmpeg and Chromium are already in the cloud image.

**State and memory:**
- Memory lives in files, not in Claude: `Soccer Channel/START HERE.md`, `Lessons Learned.md`, `Idea Bank.md` and `Outcome Log.md`.
- A new account picks up exactly where the last one stopped by reading them.
