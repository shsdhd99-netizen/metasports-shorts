# Tools (MetaSports)

Run these from this folder. In File Explorer: open Tools, click the address bar, type cmd, Enter.

## Secrets (do this once)

1. Open .env in Notepad (created from .env.example with PLACEHOLDERS).
2. Vaughn must paste your real ElevenLabs API key and MetaSports voice ID after the = signs.
3. Never paste keys into chat. .env is gitignored.

    ELEVENLABS_API_KEY=...
    ELEVENLABS_VOICE_ID=...

To list voices (after the API key is in .env):

    python voiceover.py --list-voices
    python voiceover.py --check

## How to run

| Script | Command |
|---|---|
| Voiceover | python voiceover.py --script "path\to\script.txt"  -> voice.mp3 + captions.srt next to the script. Options: --dry-run, --list-voices, --check, --target-wpm 270 |
| Channel check | python channel_check.py  (default @MetaSportsClips) or python channel_check.py @YourHandle |
| Copy check | python copy_check.py "topic phrase"  -> FRESH / CROWDED / TAKEN |
| Fresh moments | python fresh_moments.py  -> data\fresh_moments.md |
| Thumbnail | python thumb.py --shape short --bg "frame.png" --text "53 YEARS" --out "cover.png" |

Claude slash commands (/voiceover, /channel-check, etc.) wrap the same scripts - see Tools Guide.md.

## ShortsOS

Do not block MetaSports posting on ShortsOS Phase 0 (bootstrap only; no app code yet).