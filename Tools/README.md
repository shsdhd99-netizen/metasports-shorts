# Tools (MetaSports)

> **Nov 7, 2026 (later): the queue, QA sweep, Hub sync and roadmap.** `queue_rank.py` v2 plans every slot of the next 7 days (`Research Notes/Auto Queue.md`, `--apply` writes slots into READY cards); `qa_sweep.py` runs qa_final on every waiting draft and reads back every scheduled upload on YouTube (`Research Notes/QA Board.md`); `hub_sync.py` turns the repo's state into Hub/task writes (results, posted, slot labels, missing cards, UP NEXT); `roadmap.py` rewrites the LIVE STATUS block of the roadmap; `lab.py predict --folder F` scores a Short before voicing (backtested daily). Map: `Research Notes/Tools, Scoring and QA (Nov 7, 2026).md`.


> **Nov 7, 2026: `lab.py` (the lab).** Tests that run, log and score themselves, plus a repeatable study of every part of a Short. `python lab.py auto` (daily: measure every Short, score the live tests in `Research Notes/Lab/tests.json`, write `Scoreboard.md` and a study with a Rule check); `python lab.py assign nba|fc --folder F` (the arms the next Short must use; writes the card's `**Arms:**` line); `python lab.py study --part edit|script|package|topic|length` (the same study for any part). `next_arm.py` now calls it. Also Nov 7: QA no longer fails on a short tag list or a missing pinned comment, and the 35%-one-source / cut-count / shot-length lints are gone (Theory Ranking C2).


> **Oct 13, 2026:** see the "Oct 13 changes" box at the top of `../Tools Guide.md` (assemble no-loop fix, new QA checks, pointer.py, critic_v2.md, voice_fx silence-only trimming).

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