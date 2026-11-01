# S20 Barcelona signed Messi on a paper napkin (Oct 31, 2026; FC daily run, script only)

> **Status: script and notes only.** `cloud_setup.sh`: `key: MISSING` (ElevenLabs). No voice, render or QA; nothing faked. 196 words: expect about 52-54 s at S18's pace. If the voice runs past 59.5 s, cut "Messi was thirteen." or "Some of them said... benefit." first; never add.

- **Lane:** secret object (the napkin), about the biggest name in the sport. Rotation: S16 topical, S17 goalkeeper trick, S18 revenge, S19 topical/goalkeeper (unvoiced), so S20 is not a goalkeeper Short and can go between S19 and the next goalkeeper one.
- **Stranger test:** Messi + a napkin + "almost a million dollars": passes.
- **Copy check:** `copy_check.py "Messi napkin contract"`: FRESH (top 738 views). It is a well-known story, so the angle is the ending (couldn't afford to keep him / the napkin worth a fortune), not the napkin alone.
- **Frame 1:** the napkin itself (Bonhams/AP photo of it, sharp) with 13-year-old Messi; line 1 names both.
- **Music test:** S17 music, S18 none, S19 music, so S20 = **no music** side.
- **Rejected today:** Pelé paid to tie his laces (Idea Bank S06): every account traces to secondary blogs; sources disagree on the fee ($120K vs $140K) and on who made the "pact" (the Dassler brothers per Wikipedia, their sons Armin and Horst per another). Banked with that caution.

## Claims and sources
| Line | Source | Exact words |
|---|---|---|
| Growth hormone treatment, about $1,000 a month; Newell's and River both wanted him, neither could afford it | [SI, Feb 6 2012 (Balagué book extract)](https://www.si.com/soccer/2012/02/06/barca-extract) | "although coveted by both Newell's Old Boys and River Plate... neither club can afford the approximate $1000 per month across two years for the growth hormone treatment" |
| He went to Barcelona for a trial; the club was slow; his father was tired of waiting | [90min](https://www.90min.com/lionel-messi-contract-napkin-sells-staggering-amount-auction); SI 2012 | 90min: Messi "had been on trial with Barca", the club was slow to offer a contract; father Jorge "had reportedly grown frustrated"; SI: "Jorge Messi was tired of being messed about" |
| Some said it would be 10-12 years before they saw the benefit | SI 2012 | "Barça were not too interested. They said, 'It will be 10 or 12 years before we see the benefit'." |
| Dec 14 2000, Rexach (sporting director), lunch at a tennis club with Minguella and Gaggioli; wrote it on a napkin | [NPR via OPB, May 18 2024](https://opb.org/article/2024/05/18/napkin-securing-lionel-messi-s-first-contract-fetches-nearly-1-million-at-auction); 90min | NPR: Rexach wrote the napkin "contract" at a Pompeia Tennis Club restaurant lunch, dated Dec. 14, 2000; 90min: "with transfer advisor Josep Minguella and agent Horacio Gaggioli present" |
| "regardless of any dissenting opinions, to sign the player Lionel Messi" | 90min (napkin wording) | "hereby agrees, under his responsibility and regardless of any dissenting opinions, to sign the player Lionel Messi, provided that we keep to the amounts agreed upon" |
| Messi was 13 | NPR; 90min | "aged only 13 at the time" |
| Barcelona's all-time top scorer | NPR | he set Barcelona's all-time goal record |
| 2021: agreed a new contract, couldn't register it under LaLiga's rules | Barcelona statement, Aug 5 2021 ([Al Jazeera](https://www.aljazeera.com/sports/2021/8/5/messi-to-leave-barcelona-due-to-financial-structural-obstacles)) | "Despite FC Barcelona and Lionel Messi having reached an agreement and the clear intention of both parties to sign a new contract today, this cannot happen because of financial and structural obstacles (Spanish La Liga regulations)" |
| Messi left in tears | AP, Aug 8 2021 ([WJLA](https://wjla.com/news/nation-world/messi-breaks-down-says-he-wasnt-ready-to-leave-barcelona-08-08-2021)) | "Messi breaks down, says he wasn't ready to leave Barcelona"; he "cried profusely as he stepped up to the podium" |
| Napkin sold for £762,400 (almost $1M), three years later (May 2024) | NPR | sold by Bonhams "for 762,400 British pounds (about $968,600)" |

**Cautions:** don't say Barcelona sold the napkin or tried to buy it (it was sold on behalf of agent Horacio Gaggioli). Don't say "there was no paper" (legend, not checked). The diagnosis is debated in later reporting; "growth hormone treatment" is what the sources say, keep it at that.

## Footage leads (not downloaded: no voice to cut to today)
- The napkin: AP/Bonhams photos and video of the lot (May 2024).
- Young Messi: La Masia / Barcelona youth footage; the 2004 debut; record-goal moments (Barcelona's own channels; YouTube blocks cloud downloads, so the PC or X: `Tools/x_clip.py` @FCBarcelona).
- Aug 8 2021 farewell press conference in tears (Barcelona's own stream; widely on X).
- Stock: hormone injection pen (Mixkit/Pexels) for the treatment line; a tennis-club terrace for the lunch.

## Beats
1. Line 1 over the napkin close-up (frame 1).
2. Rosario kid / treatment / two clubs say no (fast, ~1.5 s pictures).
3. Trial, waiting, father; the lunch; the napkin text burned in as an overlay ("regardless of any dissenting opinions").
4. Records montage, then the 2021 statement and the tears.
5. Payoff: the auction hammer / the napkin, "£762,400" on screen. End there.
