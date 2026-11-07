# #43 production package: "How Did Wilt Average 48.5 Minutes? 🤯"

**Status: script-ready (v2) with verified facts; footage partly in hand. NOT rendered.**
- **Facts:** `Research Notes/Batch 4 Concepts (Oct 13, 2026).md`, section 4 (fact sheet) and section 8 (v2 script).
- **Score:** rubric v3 53/70 (Clarity 5, Novelty 4, Visual 2, Stakes 3, Name 4).
- **Blocker:** **identifiable Wilt footage.**
  - The downloaded 1962 All-Star film (archive.org, 480x360, black and white) is wide and grainy. Wilt can't be picked out reliably, so the "right person on his name" check would fail.
- **Next action:**
  1. ~~The archive.org 100-point game item~~ is the WCAU **radio** broadcast of the 4th quarter (metadata checked Oct 14), not film. Skip it.
  2. Or the owner pastes 1-2 X posts of Wilt film (NBA History account) to download with `Tools/x_clip.py`.
  3. Then voice → anchor → assemble → QA → Critic v2.

## Beats, 95 words, about 22-23 s
| Beat | Line |
|---|---|
| **Hook** | "Games last 48 minutes. Wilt averaged forty-eight and a half." (paradox; clear by about 3 s) |
| Turn | "For a whole season. How? Overtime." |
| Context (one measure: minutes) | "His team played 3,890 minutes. Wilt played 3,882 of them. Every second of seventy-nine games. Every overtime too. No rest. No foul-outs. No bench." |
| Question | "So where did the missing eight minutes go?" |
| **Payoff** | "January 3rd, 1962... Referee Norm Drucker hit Wilt with two technical fouls. Ejected. The only eight minutes Wilt sat all season, a referee made him sit." |

## Shot plan
| # | Words | Picture | Have it? |
|---|---|---|---|
| 1 | "Games last 48 minutes." | **Frame 1:** the 1962 arena game clock (ASG film, last frames of the contact sheet), clearly a game clock | ✓ `scratchpad/concepts/footage/wilt/asg1962.mp4` (lost when the container resets; re-download from archive.org `1962-nba-all-star-game`) |
| 2 | "Wilt averaged forty-eight and a half." | The B-Ref per-game row with **48.5** boxed (mark box x436 y195) | ✓ `bref_wilt_pergame.png` (same caveat) |
| 3-5 | "For a whole season... Overtime." / team minutes | **Identifiable Wilt (#13)** on court, film | ✗ need close Wilt frames |
| 6 | "Wilt played 3,882 of them." | One card: 3,890 vs 3,882 (B-Ref team page) | build |
| 7 | "No rest. No foul-outs. No bench." | Fast film cuts of Wilt running the floor | ✗ (same blocker) |
| 8 | "So where did the missing eight minutes go?" | The game clock again | ✓ |
| 9 | "January 3rd, 1962... Norm Drucker..." | Card: the ESPN Mag / NYT quote ("the only minutes Chamberlain missed...") with its source | build (page shot) |
| 10 | "...a referee made him sit." | Wilt on the bench, or back to the clock (loop) | ✗ / ✓ |

## Voice, captions, sound
- Clone, speed 1.15. Numbers in braces (digits on screen).
- "Drucker" → test-read on one line first.
- A buzzer sound only if the film's clock hits zero on screen. No music (TEST: low music for a history piece needs the owner's OK).

## Upload package (draft)
- **Title:** How Did Wilt Average 48.5 Minutes? 🤯
- **Hashtags:** #nba #wiltchamberlain #shorts
- **Tags (≤12):** wilt chamberlain, wilt 48.5 minutes, wilt chamberlain minutes record, 1961-62 warriors, wilt chamberlain ejected, norm drucker, nba records, nba history, most minutes per game, wilt 50 points season, philadelphia warriors, nba trivia
- **Pinned comment:** "Wilt played 3,882 of his team's 3,890 minutes in 1961-62. Could anyone today play every minute?"

## Risks
- **Copyright:** the archive.org film has no license listed. Use short cuts under commentary.
- **Accuracy:** never say "never left the floor". He sat 8 minutes, and that is the payoff.
