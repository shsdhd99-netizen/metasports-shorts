# #49 DRAFT, awaiting the owner's approval: "He's Not Steve Kerr… But His Name Is Steve" (NOT POSTED)

**File:** `DRAFT - awaiting approval - 49 Kerr lookalike (no music).mp4` (same as `final.mp4`): 19.9 s, 1080x1920, -14 LUFS, Alex voice, captions burned, no music.
**Video files are not in git.** Get it from the chat attachment (Oct 19) or rebuild it on the PC: `python Tools/assemble.py --folder "<this folder>" --no-music`, after the clips are re-cut from `src/` (`sources.csv` has every in-point and crop).

**Title:** He's Not Steve Kerr… But His Name Is Steve 😳 #nba
**Hashtags:** #nba #warriors #shorts
**Pinned comment:** Steve Gillis went viral at his first Warriors game in 2024. Kerr's verdict: "strikingly handsome." 😂
**Post window:** any time (an evergreen 2024 story). Don't add "this week": the Oct 2026 lookalike clip could not be confirmed as Gillis (notes.md).

## What changed from the script as voiced
The sentence "And on Friday, he was back, and Kerr spotted him again." was **cut out of the voice track**. The original take is kept in `_voice_prev/v1_with_friday/`.
- **Why:** the only footage of the Oct 16 moment (Polymarket Hoops) shows Lakers-branded bench chairs, which doesn't match NBC's "Chase Center vs Blazers".
- AOL/PFN reports Kerr has had more than one lookalike (another one in Oct 2025), and HITC says the clip doesn't establish who the fan is.
- The claim couldn't be verified, so it isn't in the Short.

## QA (`qa_short.py --full`, Oct 19): 1 rule overridden on purpose, everything else passes
- **Overridden:** "no action footage in the first 3 s". The rule targets talking-head hooks. Here the claim *is* a face: frame 1 is the lookalike, and 1.4 s later a labelled split screen puts him above the real Kerr. The owner decides whether to accept the override; the alternative is not to post.
- **Warnings kept:**
  - 100% faces (it's a face-comparison story)
  - shot 5 is a 1.2x reframe of a 1080 broadcast, 2.26x from source and soft. No better 2024 source exists; the X post is the broadcaster's own
- **Passes:** captions match the script word for word, speech-to-text matches 100%, -14.3 LUFS, no clipping, no repeated footage, every clip watched and logged in `sources.csv`.

## Shots (10, about 2.0 s each)
| # | Time | Clip | Shows |
|---|---|---|---|
| 1 | 0.0 | G1 | Gillis in profile, NBCS broadcast, Mar 9 2024 (frame 1 = the claim) |
| 2 | 1.4 | S1 | split screen: "STEVE GILLIS" (top) over "STEVE KERR" (bottom, 2026 Play-In presser) |
| 3 | 2.8 | G2 | Gillis close-up |
| 4 | 5.2 | G3 | Gillis close-up, side look |
| 5 | 7.0 | G4 | slow reframe onto his face ("put his face on the big screen") |
| 6 | 9.0 | G5 | Gillis ("Twice.", one soft pop) |
| 7 | 9.7 | K1 | the real Kerr, Play-In podium |
| 8 | 12.5 | K5 | Kerr, Warriors presser (what his sons saw on TV) |
| 9 | 15.7 | K6 | Kerr, Play-In podium, another moment |
| 10 | 17.6 | K4 | punch-in on Kerr's face for his quote |

## Music (owner approved copyrighted tracks for drafts, Oct 17)
- None in this cloud render: the owner's tracks are on the PC.
- **Suggested:** a light, playful instrumental at -22 LU, dipping under the quote (17.6 s).
- **Copyright risk:** a commercial track baked in can bring a Content ID claim (the revenue goes to the claimant; the video stays up).
- Adding a sound in the YouTube app at upload avoids baking it in.

## Rights
NBA/NBCS broadcast and press-conference clips from public X posts (sources.csv). A claim is possible; it's fair-use-style commentary, but not guaranteed.
