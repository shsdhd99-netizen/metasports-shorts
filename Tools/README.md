# Tools (MetaSports)

> **Nov 7, 2026 (efficiency pass): build a Short in 4 commands.** `build.py status|voice|cut|render F` runs each stage with its gate and prints the next command (tested on a copy of #99: cut plan to SHIP + Hub files in 89 s). `script_lint.py` is now the PRE-VOICE GATE (exit 1 on FIX: length by channel at the measured 234 wpm, line 1 over 11 words, filler opener, question/CTA ending, a bare "3-0"; shows the predicted score; the #42 checklist only with `--format42`). `anchors.py` is the one cue-word matcher (anchor_shots, fill_len, cut_list, precut_lint) and warns when an anchor pins mid-sentence while a later copy starts a phrase (the #99 "Last" re-cut). `cut_list.py` fills missing `len` itself (fill_len is optional) and fills sources.csv links from `cuts.json "urls"`, a `.url` sidecar or the file name (no hand patching). `precut_lint.py` times shots like the cut will and adds: no action shot in 3 s, overlay text reaching the caption band, overlays too fast to read, shots over 6 s. `espn_clip.py games|clips|get` finds a game's ESPN clips and downloads 1080p with the source link. `tool_check.py` compiles every tool on the running Python and runs self-tests + smoke runs (Sundays). footage_qc's blown-up/soft warnings are one line per Short now (was 337 lines in 14 Shorts).

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