# Who builds Shorts right now (read this before building; one builder only)
`BUILDER.txt` holds one word: `pc` or `cloud`. Every daily run reads it first and builds ONLY if it names where it runs; otherwise it does zero-credit steps only.
**Value: `cloud`** (owner, Nov 3 night: "build in cloud so both accounts can edit"). Both Claude accounts work through git on `main-329h3w`; the PC does zero-credit chores.

## Division of labour
- **Cloud (either account):** research, scripts, fact table, voice, footage from X / ESPN / archive.org / Mixkit, edit, QA, upload cards, Hub cards, `learn.py`, scheduling through `yt_schedule.py` once the tokens are in the environment.
- **PC (no builds while this says `cloud`):** `MetaSports analytics` (3:20 AM), `schedule ready` timers, `preflight`; and **YouTube-only footage** (the cloud's YouTube downloads are blocked): when a story needs a YouTube clip, the cloud run writes the request to `Research Notes/PC Requests.md` (video id, wanted range, Short folder) and the PC session fetches it into the Short's `src/` and pushes it (only small files; see below).
- **Both accounts:** pull before editing, push small commits, never work the same Short folder at the same time (claim it with a line in `Research Notes/STATE.md`: `CLAIM <folder> <account> <time>`; release by deleting the line).

## Switching builder
Edit this one word. If the PC must build (cloud keys lost again), set `pc`, write the reason in `STATE.md`, and set it back to `cloud` when the keys return.
