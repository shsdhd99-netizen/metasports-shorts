# Shot plan: 2026-10-03 11 Would Jordans Push-Off Be Called Now

Footage rows (V) need cutting on the PC (YouTube blocks downloads from the cloud). Card rows (C) are already built in `clips/`.

Cut each V clip as `clips/<name>`, 1080x1920 (`Tools/broll.py sheet` to find the moment, then `broll.py cut ... --snap`), the length shown. Then run `python Tools/assemble.py --folder <this folder>` (add `--caption-style metasports` for the ALL CAPS look). `shots.json` and `sfx.json` are already written for it.

| # | Start | Length | Clip file | What must be on screen | Where to find it |
|---|---|---|---|---|---|
| 1 | 0.00 | 2.4s | `V01_jordan_vs_russell.mp4` | Jordan isolates Bryon Russell, 1998 Finals Game 6, final 40 s (Jazz in white, Bulls in red). Start on the crossover, so the first frame already has motion. | YouTube: NBA / ESPN Throwback 'Michael Jordan last shot 1998 Finals Game 6'. Archive.org full game 1998nbafinalsgame6 (480p) as fallback. |
| 2 | 2.44 | 1.6s | `V02_jordan_shot_falls.mp4` | The shot going in and the Bulls celebrating (no whistle, nothing called). | same game |
| 3 | 3.99 | 2.8s | `V03_refs_whistle_nba.mp4` | Ref blowing the whistle / referee huddle, clean modern broadcast shot. Fits 'the NBA rewrote how refs call it'. | NBA YouTube: 2026-27 points of emphasis video (Sept 29, 2026) |
| 4 | 6.77 | 3.4s | `c11_a_1.mp4` | **CARD (done)** ESPN card: headline + the Four F's line boxed in red. | built in the cloud |
| 5 | 10.15 | 2.5s | `V04_ballhandler_feels_defender.mp4` | A ball handler touching a defender with the off hand to feel him (legal), from the NBA's points-of-emphasis video or any modern clip. | NBA YouTube points-of-emphasis video |
| 6 | 12.69 | 3.1s | `V05_push_off_extended_arm.mp4` | A clear push-off: arm fully extended, defender stumbles back (the NBA's own foul example). | NBA YouTube points-of-emphasis video |
| 7 | 15.75 | 1.1s | `V06_jordan_russell_replay.mp4` | Slow replay of the Jordan push on Russell, left arm out. Hold it through 'whistled?'. | same game as V01 (replay angle, or a 'Jordan push-off' breakdown) |
| 8 | 16.84 | 3.2s | `c11_b_1.mp4` | **CARD (done)** ESPN card: 'By the NBA's new Four F's standard, Jordan wouldn't be whistled...' boxed. | built in the cloud |
| 9 | 20.01 | 1.2s | `V07_nba_example_title.mp4` | Cut to the NBA's example reel (the league's own clips), any foul example, 1 s. | NBA YouTube points-of-emphasis video |
| 10 | 21.18 | 1.8s | `V08_jaylen_brown_oubre.mp4` | Jaylen Brown (then Celtics) forearm into Kelly Oubre Jr.'s chest at the free-throw line. Verify both faces and jerseys. | NBA YouTube points-of-emphasis video (the clip ESPN describes) |
| 11 | 22.96 | 2.0s | `V09_barrett_mobley.mp4` | RJ Barrett (Raptors) pushes Evan Mobley (Cavs) in the paint and Mobley stumbles back. Verify both faces. | NBA YouTube points-of-emphasis video (the clip ESPN describes) |
| 12 | 24.93 | 0.9s | `V10_ref_offensive_foul_signal.mp4` | Referee signalling an offensive foul (fist behind head or hand on hip). | any modern broadcast clip |
| 13 | 25.87 | 1.9s | `V11_jordan_shot_clean.mp4` | Jordan's shot again, left hand away from Russell, ball in the air. Same as V02 but a different angle if possible. | same game as V01 |
| 14 | 27.82 | 1.2s | `V12_jaylen_brown_sixers_loop.mp4` | Jaylen Brown in a Sixers jersey (media day or scrimmage) for 1 s, THEN a 0.3 s freeze on the first frame of V01 so the Short loops back into its opening. | NBA / 76ers YouTube media day clips |
