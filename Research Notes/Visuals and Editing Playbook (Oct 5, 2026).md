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

## Premise line (persistent top line, user-approved test, Oct 5)
Option: `render --premise-line "TEXT"` (off by default). White Montserrat Bold 44 px, sentence case, 45% black pill, centred at y=7% of height (about 134 px), whole video. Statcards shift down 60 px when it is on so they never collide. Not the removed hook headline: small, constant, and it states the premise, not a teaser.
Tested on copies of #19 and #20 (frames 0.3/2/10/20 s): `Research Notes/Visuals Playbook Assets/premise_line_19_top_20_bottom.png`. It sits above faces and well above the 45-62% caption band; at 2 s in #19 it overlaps only the top of a jumping player's frame, at 20 s it clears the Flagg face (face top is about 15%).
Commands (on COPIES; Tools/ cwd):
- `python visual_fx.py render --folder "<copy of #19>" --out-name premise.mp4 --premise-line "Flagg: 6-8 to 6-11?"`
- `python visual_fx.py render --folder "<copy of #20>" --out-name premise.mp4 --premise-line "Bad Boys vs Knicks"`
Text ideas: #19 "Flagg: 6-8 to 6-11?" (or "Flagg's real height"); #20 "Bad Boys vs Knicks" (or "Bad Boys defense, today"). Keep 2-4 words, one line, no emoji.
A/B plan (HYPOTHESIS, n small):
1. Post #19 WITH the line and #20 WITHOUT, same slot on different days; swap the arm on the next pair.
2. Same lane, similar length, same posting time, no other changes that day.
3. Compare "stayed to watch" and avg % viewed at 48 h, plus the 3-s retention point.
4. Record each pair in Outcome Log.md (arm, views, stayed %, APV).
5. Call it after 3 pairs: adopt only if the line arm wins on stayed-to-watch in 2 of 3 pairs by 3+ points.
6. If it ties or loses, drop it; the line costs nothing but adds no proven value yet.

## Style variants on #21 Jokic/Westbrook (Oct 5, copies; frames: `Visuals Playbook Assets/styles_A-house_B-clank_C-punch.png`, `coldopen_D_and_flash_E.png`)
Files: `.../scratchpad/visuals/styles/{A_house,B_clank,C_punch}.mp4` (12.9-15.7 MB). All five renders measure -14.4 LUFS integrated (loudness identical, so none of these styles changes audio level; PROVEN).
Setup: five copies (A..E) of the #21 folder minus big dirs; B/C/D/E differ only in shots.json / sfx.json / fx.json.
- **A house**: `python visual_fx.py render --folder A --out-name out.mp4` (21 shots, avg 1.06 s, schedule card at the end, house captions).
- **B clank**: `... --folder B --caption-style clank` with shots.json merged to 10 shots (avg 2.2 s), card removed. Result: captions small white sentence-case, readable but weak on bright footage (frame 3); the Oscar/Westbrook hook shot is held 2.5 s. 
- **C punch**: `... --folder C --punch 0.07 --kenburns 0.06` with fx.json statcard `{"at":4.99,"big":"209 vs 198","of":"Westbrook vs Jokic","label":"Career triple-doubles"}` replacing 3 shots (1.9 s) and sfx.json: boom at 0, `thud` at 8.3 (the "But" turn), `boom_cinematic` at 21.0 (payoff "Four games to spare"). Stat card readable at a glance; shows both numbers while only 209 has been said (198 comes 1.3 s later) which is a mild spoiler, split into two cards if it bothers you.
- **D cold open** (`fx.json {"coldopen":{"clip":"b11.mp4","in":1.0,"len":0.6}}`): mechanically works, no audio shift. On frames it HURTS here: the first words "Only two players..." play over an unrelated court shot and the Oscar/Westbrook hook image arrives 0.6 s late, breaking picture-voice match (Hasson, SUPPORTED mechanism). Only worth testing if the payoff image is also the hook subject. Tier HYPOTHESIS (not measured on viewers).
- **E flash cuts** (`fx.json {"flashes":"all"}`): 2 white frames at 20 cuts = 1.33 s (6% of runtime) of washed-out picture, faces go grey (frame E1). Hurts on frames at this cut rate; if used at all, flash only the turn and payoff (`"flashes":[8.3,21.0]`). Tier HYPOTHESIS.
Ranking (my judgement, not data): C > A > B for this story. C adds a visible number plus an audible turn/payoff at no cost; A is the safe baseline; B is a style A/B only (fewer cuts cut against the channel's measured fast cut lane, CoachClank captions untested here). Retention effect of all three: HYPOTHESIS until Studio numbers exist.
