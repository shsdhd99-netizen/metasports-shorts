# Editing study: the Dyson stick-figure Short (Fxyx1YxtQv8), watched Nov 5, 2026
Source: Gemini watch report `Watch Reports/Fxyx1YxtQv8.json` (tier [S], model-observed, not measured). Views were not checked.

## How it is edited
- 50.5 s long, 31 shots, average shot 1.6 s, longest 3.0 s. 3 shots in the first 3 s.
- **Every line is illustrated literally.** "Lost suction" shows a dirty patch on the carpet. "Clogged bag" shows the bag held up. "Rejected" shows a Hoover rep waving no. Nothing is generic b-roll.
- **Animated numbers carry the proof.** A counter runs to 5,127 prototypes, and a bar rises to $20 billion at the end. The numbers are not cards; they sit on top of the scene.
- **Logos and labels sit inside the scene** (HOOVER, Electrolux, DC01 1993, "No.1 Best Selling"), so the proof is on the picture.
- **One character, one world.** A stick figure on real photo cutouts. The look stays consistent, so it never feels like random stock.
- **Captions** are 2 words, ALL CAPS, white, pop-in, centred. AI voice at about 180 wpm (slower than ours). Quiet upbeat music from 0 s. No sound effects.
- **Story shape** is our format: problem, obsession, failure count, rejection by the giants, a back-door win, and it ends on the payoff number. No call to action.

## What we take (no new tools needed for most)
1. Under every number, show it counting up, not a still: our `overlay` text plus an ffmpeg counter; a small tool to add.
2. Literal picture per phrase: already our rule, and this shows it working at 1.6 s a shot.
3. Show the rejecter's logo or name on screen at the "they said no" beat (our "versus their own" lane).
4. Hold the payoff number on screen for the last 3 s.

## What we don't take
The stick-figure animation style. It's their look, and making it needs image generation per shot. Keep real footage.
