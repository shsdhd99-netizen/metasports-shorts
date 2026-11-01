# Editing Study (Nov 1, 2026): how the best Shorts are actually edited, and how ours look next to them

Scope (owner, Nov 1): look at the editing itself, frame by frame, not whether editing moves views. I downloaded six Shorts and read their frames and cuts: CoachClank "He Didn't Have To Do That" (26M) and "6'8 vs 7'9" (34M), swishyhoopz "The Craziest Basketball War" (30M), HoopiverseYT "Every Country Has Their Own Version of NBA Players" (3.9M), Ahmed's Goal "Transfers that completely BACKFIRED" (1.9M), our #48 "Who Has Missed The Most Threes" (posted) and our #82 Wemby draft. Contact sheets were 1 frame per second. Gemini's 213 watch reports in `Watch Reports/` were used only as a cross-check of shot counts (flash-lite shot counts can be off by about 3).
As a side result, 171 Gemini reports show a channel's top-half and bottom-half Shorts edit almost identically (shots per 10 s 3.77 vs 3.73; music in 100% vs 97%), so editing details don't explain the gap. That is not the question here; the rest of this page is craft.

## 1. What each reference actually does

| | Footage framing | Captions | Cuts / rhythm | Extra graphics | Signature move |
|---|---|---|---|---|---|
| **CoachClank** (34M, 26M) | Broadcast game footage zoomed so the player fills about 60% of frame height; extended top and bottom with a soft blur, never black bars; scorebug visible, lower third of the frame | Small, thin, sentence-case white, 3-4 words, vertically at about 50%, no colour, no highlight; exactly the line being spoken | One clip per sentence; 7-8 scene cuts in 21 s; the 14-second one has NO cuts (one held shot with captions only) | None | Restraint: the footage is the star; the caption is invisible |
| **swishyhoopz** (30M) | Phone/creator footage, full-bleed 9:16, no blur fill | Bold italic, white with black outline, centred at about 50%, 3-4 words, word-by-word | 10 cuts in 26 s (about one per 2.6 s) | **Escalating counter** in neon yellow-green digits (10 -> 40 -> 80) over the action | The counter turns the story's number into a visible score |
| **HoopiverseYT** (3.9M) | Side-by-side "original vs copy" clips, full-bleed, brand watermark bottom | Coloured words with emoji stickers (a flushed face), "*Laugh*" asides | Almost no cuts (1 scene change): clips run long, a text label does the work | Colour-coded labels ("ORIGINAL", "Chinese Version") | The comparison label, not the cut, makes the structure |
| **Ahmed's Goal** (1.9M, 77 s) | Photos with face cut-outs over a club crest, blurred stadium backgrounds, slow push-ins on stills | Small white, centred, narrow, exactly the spoken words | 60 changes in 77 s (about 1.3 s per picture) | A stamped text sticker ("4TH IN SPAIN") on the key stat | A new picture for every noun in the sentence |
| **Ours #48** (posted) | Broadcast footage in a band over a darkened blur fill; subject medium | Bold white all-caps, black outline, with the key word in orange/green; centred at about 57% | 22 cuts in 23 s (about one per 1 s) | A big orange counter (5,933 -> 5,825 -> 1,028) with a small label and a green repeat of the number as a caption | The counter + caption pairing |
| **Ours #82** (v1) | 3:4 window of a 16:9 broadcast frame over a blurred fill | Same | Hook (0-8 s) is the same play from the same camera three times | Orange "POINT 40" and "43 PTS / 6 BLK" | See section 3 |

## 2. What the winners share, frame by frame
1. **The footage is big.** In CoachClank and swishy the subject is 50-70% of the frame height from the first frame. In our v1 hook the subject was about 15% (wide camera, zoom 1.15).
2. **No black.** Every reference fills the unused space with soft blur or more picture. Our fill is a dark blur that reads as black at the top of the frame.
3. **The caption stays out of the way.** CoachClank's captions are small enough to read the picture around them. Ours are larger and coloured; on a wide shot they sit on the players' bodies (see #82's "A THREE" over Kuminga).
4. **One number, made visible.** Swishy and ours both turn the key number into a graphic. Swishy's rises as the story escalates; ours replaces one number with the next. Escalation (the same slot counting up) is clearer than replacement.
5. **A new image per idea.** Ahmed's channel changes the picture on every noun; CoachClank changes it every sentence. Neither shows the same picture twice in a row.
6. **No filler at the end.** Their last frame is the payoff image, not a held face.

## 3. What is wrong with our edit, seen on the frames
- **#82 v1, 0-8 s:** the live wide, the "rewind" and the slow-motion replay were all the same camera on the same play, so for 8 seconds the picture never changes. `qa_short` passes it (the clip ranges differ). The subject (Wemby) is a few pixels tall.
- **Scorebug cut in half** wherever the 3:4 window is used ("105 S"). The note cites the scorebug as proof, but the viewer can't read it.
- **Static ending:** 3.9 s on one close-up with a held 43 PTS / 6 BLK.
- **Caption on the players** in wide shots.
- **#48:** double number (counter and a green caption repeating the same number), and cuts every second with no room for the footage to play.

## 4. Changes made (opt-in, no existing render changed)
1. **`Tools/edit_lint.py`** (new). Reads `cuts.json` and flags: same angle three times in the first 8 s, a 3:4 window on a shot whose note relies on the scorebug, a closing shot longer than 2.8 s, a wide hook shot at zoom under 1.3. It is advice, not a gate (exit 1 on any flag). Run: `python Tools/edit_lint.py --folder "<Short folder>"`. On #82 it found all four problems; on #73 it found the clipped bug and the small hook subject.
2. **#82 v2** (`DRAFT - ... (v2 tighter hook, no music).mp4`): the live block at zoom 1.6 so Wemby and Kuminga fill the frame, the rewind at zoom 1.35 (so it no longer looks like the same picture), the half-speed contact unchanged. The source has no second angle of the block (the other ESPN clip is a first-quarter play), so the hook angle remains one camera; the lint still flags it. v1 is kept untouched.
3. **Rule for scripts and shot lists (added to the lint docstring and here):** put the proof object (scorebug, name on a jersey) on a shot that uses the whole frame OR a window that includes it; do not cite what the crop hides.

## 5. Not implemented (decided against, with the reason)
- **CoachClank-style small caption:** a caption redesign changes the look of the channel; the owner chose the current caption house style. Proposed as a test: `--caption-style clank` already exists in `assemble.py`; try it on one Short per week. [H]
- **Escalating counter (swishy):** `overlay.py` can already put a number on a clip; making it count up in the same slot needs a small feature (a "from/to" spec). Candidate for the next study round.
- **Removing the dark fill:** a lighter blur fill is a one-line change in `broll.py` (`eq=brightness=-0.12`), but would change every Short; test on #73's demo first.

## 6. #73 demo re-edit
Not done in this pass: #73's single X source video is not on disk and needs re-downloading (`x_clip.py`). Next session: re-cut #73 with the lint's two flags fixed (hook zoom 1.5, bug on a full-frame shot) as `DEMO - editing upgrade`, using the existing voice.
