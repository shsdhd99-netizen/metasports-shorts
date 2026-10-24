# Editing practice log (Oct 15, 2026): what was applied to real videos, and what could not be done

## Applied (each on a real render, checked on frames and loudness)
| Lesson | Where | Result |
|---|---|---|
| Keep numbers out of the caption band (captions sit at about 55-65% of the height) | #42 and #36 cards | Cards first collided with captions (#42 v1 draft); all card text now stays above y=1040. Verified on the storyboard |
| Never end a clip on the source's own cut | #42 Kobe and LeBron clips, #36 | A Kobe clip ran into a Dirk Nowitzki interview cut; a LeBron close-up ran into an OKC player. Found on the contact strip, re-cut shorter. Rule: look at the LAST frame of every clip, not only the first |
| Frame 1 and every shot must show the player the line names | #42 | A "bench" frame showed a Wolves player instead of LeBron: re-cut. Verified each clip by eye and logged it in `sources.csv` |
| Effects only on something that happens on screen | #42 | One whoosh into the FG% card. The "boom" on 31,502 was tried and dropped: no picture event for it, and the number already lands |
| No rim sound on an airball (frame 1) | #42 | Silent by design |
| Controlled push-ins, never on already-soft clips | #42 `_v2` | See `_v2/CHANGES.md` |
| Music is a tested variable, not a default | #42 | Two music renders (see below); the no-music render stays the post-ready file |
| Repeated footage only as deliberate second visit with a change of scale | #42 airball | Two visits to one continuous play, the second with a stronger push-in |

## Music test on #42 (draft only, nothing posted)
Files in `Productions/MetaSports/2026-10-14 42 .../_v1/`: `final_music_typebeat.mp4` (the "free for profit" type beat from Downloads/music, -21 dB) and `final_music_raws.mp4` (the commercial song "4 Raws", EsDeeKid, -21 dB). Both normalise to -14 LUFS with true peak -1.9 / -1.7 dBTP, the voice stays intact, and loudness range drops slightly (1.1 to 1.0 / 0.9 LU: the bed fills the gaps). I could not judge by ear; I do not claim music helps. **Risks recorded:** "free for profit" is a label from the file name, unverified, so treat the type beat as Content ID unknown; "4 Raws" is a label-owned commercial recording, so a baked-in render should expect a claim (a 23 s Short is under the 1-minute block, but ad revenue would go to the claimant). Per `Library/Music Guide.md` and the owner's Oct 14 rule, a real song goes in through the YouTube app's sound picker at upload, not baked in, unless the owner says yes for that video. Only the type-beat render is in the Hub (the Hub's 1 GB asset storage is full).

## Could not do (honest)
- **Drift keyframes:** the `edit.drift` project file is a binary container (it starts `DRIFTPRJ`), and the `drift-live` tools were not available in this session, so I could not inspect or write Drift's own keyframes. Motion was done through `assemble.py`'s ffmpeg engine (`zoom` per shot). No claim of Drift keyframe skill.
- **Watching competitor visuals:** not done here (the competitor breakdown of the same day already says visuals are [H]).
- **Listening:** every audio judgement above is measured (LUFS, true peak, spectrum share), none by ear.

## Tool notes found today (so nobody repeats them)
- `qa_short.py` "clipped runs at full scale" is a false alarm on stereo exports: `export_check.py` downmixes with `-ac 1`, and correlated L/R then reads +3 dB. Real peaks: L and R -1.99 dBFS, 0 samples above 0.999, EBU true peak about -1.9 dBTP.
- In PowerShell, `$f` and `$F` (and `$v` and `$V`) are the SAME variable. A loop variable overwrote a folder path twice today.
- `Set-Content -Encoding utf8` writes a BOM; `assemble.py` fails on a BOM in `shots.json`. Use `[IO.File]::WriteAllText` with `UTF8Encoding($false)`.
- ffmpeg `-ss` past the real video-stream end (container duration is longer) returns no frame: use `-sseof -0.4` for a last-frame check.
- `assemble.py --out-name` does not keep the first render: it still rewrote `final.mp4` in this session. Render one variant at a time and rename.
- Python 3.12 has cv2 (footage QC) but not faster-whisper; Python 3.14 (`py -3`) has faster-whisper but not cv2. The speech-to-text check of the export is therefore skipped by QA.