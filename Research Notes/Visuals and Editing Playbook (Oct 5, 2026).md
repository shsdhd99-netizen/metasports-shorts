# Visuals and Editing Playbook (Oct 5, 2026)
Tool: `Tools/visual_fx.py` (new, standalone; assemble.py/qa_short.py untouched; every option off by default). Tested on COPIES of #24 and #19 in the scratchpad (`.../scratchpad/visuals/`). Needs `opencv-python-headless==4.10.0.84` (4.10; OpenCV 5 dropped Haar) and numpy<2.1 for `audit`/`reframe` only.
Honest scope: nothing here measures retention. "Proven" = the tool works and the defect is real in our files. Retention gain is HYPOTHESIS unless stated. Not done: competitor frame pulls (yt-dlp video blocked in cloud; thumbnails only, not attempted), thumb.py/cover work, SFX timing, caption-vs-source-subtitle detector (edge-density metric did not flag anything, so it is unproven, do not use).

## Ranked (expected retention gain x confidence)
| # | Upgrade | Evidence it is needed | What I verified | Tier |
|---|---|---|---|---|
| 1 | **Stat/number card** (`statcard`, `fx.json statcards`) replaces tiny article screenshots | Critic 2B: Wemby (79.5% stayed) boxed every number on a card; #24 had 6 numbers with no visual. Our article cards render at ~6 px text on a blurred dark page (frames: `problems_24_original_frames.png`, cols 3-4) | Rendered `$1.3M / of $2.3M guaranteed` card: number 3x larger, boxed green, sits in top 40% so captions (45-62%) never cover it. Before/after: `before_after_24_...png` col 2 | need PROVEN (our critics + frames); gain SUPPORTED (Wemby n=1, confounded) |
| 2 | **Quote-clip treatment**: speaker name tag + level to narration (`level`, `fx.json nametags`) | Critic: wrong/unknown speaker, quote 4.4 dB under (#17), static face 8 s | Level tool matched #19 quotes: -20.6/-19.0 -> -18.3 LUFS (+2.5/+0.9 dB gain; after-measure -18.3 for all four pieces). On #24 quote was already within 1 dB, no gain applied. Name tag drawn at 66% height under captions, above Shorts UI | tool works PROVEN; retention HYPOTHESIS |
| 3 | **Face-tracked reframe** (`reframe`; `audit` for finished clips) | Critic: headless Banchero crop, wrong player centred, head cropped W1 | Synthetic test (portrait clip placed off-centre in 1920x1080): centre crop finds 0/4 faces, auto crop 4/4 (`reframe_centre-crop_vs_face-tracked.png`). Real landscape sources not available in cloud | tool PROVEN on synthetic; real-world recall UNPROVEN (Haar = frontal faces only; profiles and back views missed) |
| 4 | **Punch-in on key words** (`render --punch 0.07`) | Round 7 table: zoom is HYPOTHESIS (Carmi/Itti motion only) | Smooth 7% pulse (0.12 s up, 0.45 s settle) on 4 key words in #24 (numbers/units/SHOCK/BIG), one per shot, >=1.2 s apart; no shimmer (1.5x working size + eval=frame) | HYPOTHESIS; A/B 0 vs 0.07 before adopting |
| 5 | **Ken Burns on cards/stills** (`--kenburns 0.06`) | Static cards read as dead zones; audit motion metric: cards 17-23 vs footage 50-70 | Works; assemble already has `zoom`/`--auto-zoom` for footage, so only cards/stills are new | HYPOTHESIS |
| 6 | **Per-shot grade** (`--grade`) | #24 shots span luma 36-162 (std 34) | std 34.2 -> 25.6 (-25%) after clamped eq (brightness +-0.08, contrast +-12%); look natural in frames | consistency PROVEN; retention HYPOTHESIS |
| 7 | Caption polish | house style unchanged. Hold: scorebugs/ source graphics sit at 85% height under the 45-62% caption band, no overlap seen in #24 | none built | - |

## Measurements on #24 (27 shots, 28.2 s, `audit`)
Only 2/3 frames show a detected face on 9 of 27 shots; face height 0.07-0.20 of frame (small = wide shot); 12 of 27 shots reuse a clip; no shot is static (motion >=13); 3 card shots (2.1+2.2+1.7 s = 21% of runtime). Audio pieces: vo -18.1, quote -19.6, vo -20.7 LUFS (pre-lift). Run `python Tools/visual_fx.py audit --folder F --video F/final_nocap.mp4` (nocap avoids captions polluting the metrics).

## Exact commands (run from Tools/ on a COPY of the folder)
- `python visual_fx.py audit --folder "<copy>" --video "<copy>/final_nocap.mp4"`
- `python visual_fx.py statcard --big "$1.3M" --of "of $2.3M guaranteed" --label "BRONNY'S DEAL" --out clips/s01.mp4 --len 2 --color green`
- `python visual_fx.py level --folder "<copy>"` (writes voice_fx.mp3; needs _timeline.json from splice_voice)
- `python visual_fx.py reframe "<landscape src>" --at 12.0 --len 3 --out clips/V03.mp4`
- Full A/B build: `python visual_fx.py render --folder "<copy>" --out-name fx_all.mp4 --punch 0.07 --kenburns 0.06 --grade --level --fx fx.json` (baseline = same command with no flags).
Before/after frames: `Research Notes/Visuals Playbook Assets/before_after_24_top-base_bottom-fx.png` (top base, bottom fx; columns: punch-in 1.15 s, stat card 8.2 s, Knecht card 15.0 s, quote + name tag 23.6 s).

## Known issues seen
- Source broadcast scorebug ("95 GS 106 4TH") is visible in #24 shot 1-2 at the bottom; crop it with broll `--zoom 1.25 --y 0` at cut time.
- Name tag overlaps the speaker's hands on Q2; adjust y in `render` (0.665*H) if needed.
- Render is CPU only: ~80 s for 28 s Short when other jobs share the machine.

## Patch note: what to merge into assemble.py after rebuilds finish
1. `ffmpeg_engine`: add args `--punch`, `--kenburns`, `--grade`, `--level`; replace the per-shot `vf` block with `visual_fx.shot_filter(base, amp, pulses, L)` where `pulses = plan_punches(words, shots)` (see `cmd_render` lines for the exact use) and append `grade_filter` output for non-card footage.
2. Statcards: call `visual_fx.cmd_statcard` for entries in `fx.json` (or just pre-render with the CLI and list the mp4 in shots.json with kind `card`; no assemble change needed).
3. Level: `voice = visual_fx.level_voice(folder)` before the concat mux.
4. Name tags: the drawbox/drawtext block in `cmd_render` appended to `vf` before `finish()`.
5. Nothing changes unless the flags are passed. Do the stat card and name tag first (no assemble change needed for cards).
## Needs from the user
Only analytics: A/B punch-in (0 vs 0.07) and stat card vs article card on two same-lane Shorts; do not adopt 4-6 without that.
