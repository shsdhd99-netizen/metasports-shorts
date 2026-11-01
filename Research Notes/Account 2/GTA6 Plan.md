# GTA 6 channel/series plan (written Sun Nov 1, 2026; start Thu Nov 12, launch Thu Nov 19)

The owner's part: a channel name, and a console only if gameplay recording is chosen (see section 3, which says to hold that back). Nothing here posts or uploads anything.

## 1. Launch date: verified
- **Thursday, November 19, 2026**, PS5 and Xbox Series X|S; no PC date announced. Sources: Take-Two's own earnings release ([SEC 8-K, Take-Two Q1 FY27](https://www.sec.gov/Archives/edgar/data/0000946581/000162828026054580/ttwo1q27earningsrelease.htm)); [Bloomberg, May 21, 2026](https://www.bloomberg.com/news/articles/2026-05-21/take-two-confirms-november-debut-for-grand-theft-auto-vi); CEO Strauss Zelnick: "It's November 19, 2026" (per [Vice](https://www.vice.com/en/article/take-two-ceo-confirms-gta-6-release-date-is-locked-in-amid-pre-order-rumors/)).
- History: first 2025, then May 26, 2026, then Nov 19, 2026 (from a search summary of those sources; the earlier dates are not re-verified one by one).
- Launch-week facts come from **one source** ([Newsweek](https://www.newsweek.com/entertainment/gta-6-trailer-cost-rockstar-grand-theft-auto-12108972), published late June 2026 by its own text): pre-orders opened June 25, 2026; **digital pre-load starts Nov 12** (our start date); standard $79.99, Ultimate $99.99; purchases before Nov 20 include the Vintage Vice City Pack; digital pre-orders include a free month of GTA+. Confirm on Rockstar's site before voicing.
- Not confirmed by any source I found: the exact unlock time on Nov 19, and a PC date.
- Same Newsweek page: a Netflix showcase "Grand Theft Auto 6: An Extended Look" on Thu Aug 27 (single source, already past).

## 2. Format fit with our Shorts pipeline
| Piece | Fit |
|---|---|
| 20-40 s AI-voice narrated Shorts, captions, 10-15 shots | Good for news and facts: release history, hype numbers, pre-load/bonus rules, explainers |
| Footage | Official trailers on Rockstar's channel via yt-dlp (the PC can download YouTube; see `Footage Sources.md`), cut into ~2 s shots. No leaked footage. Nothing recorded by us until the policy is checked (section 3) |
| Line 1 rule (11 words or fewer, states the strange thing) | Works, e.g. "GTA 6 has now been delayed twice." |
| One fact the clip can't show | Date, price, view counts: all available |
| Music | Our narration only; no trailer music (house rule) |
| Weak spot | Our rule "name a person, show the person": I did not verify which characters the trailers show, so watch the trailers first |
| Tools | `voice_take.py`, `cut_list.py`, `assemble.py`, `qa_short.py`; script lint is NBA-specific, so expect to override some checks |

## 3. Copyright and ToS cautions for game footage
Rockstar's page: [Policy on posting copyrighted Rockstar Games material](https://support.rockstargames.com/articles/200153756/rockstar-games-video-policy). **My direct fetches of it timed out twice, so the points below come from search summaries of the page (last updated Jan 10, 2025 per the summary) and [Game Informer's 2013 coverage](https://www.gameinformer.com/b/news/archive/2013/09/16/rockstar-details-allowable-content-and-uses-of-game-footage.aspx). Read the page itself before relying on any line.**
- The permission covers **non-commercial** use: "you don't make money through the game footage you post or use the material as part of a promotion for a product or service." **A monetized channel is a conflict.** The owner must decide whether to monetize or to avoid in-game footage.
- Isolated cinematics and cutscenes get removed; spoilers (the ending, big story twists) are prohibited; footage from leaked or pre-release copies is taken down.
- It is aimed at occasional, non-commercial fan use, not professional channels; Take-Two reviews videos case by case and may remove content that follows the rules; the policy can change. Contact quoted in the summary: copyright@take2games.com.
- That page covers in-game footage. **I found no text that licenses re-using Rockstar's marketing trailers.** They are still copyrighted: keep clips short and transformed (our own narration and facts), expect Content ID claims, never use trailer music.
- Our standing rules also apply: no cookies, no DRM workarounds, no other creators' edits as a base, no promo ending.
- Before Nov 19 any "gameplay" is a leak or a review copy, which the policy says gets removed. Hold anything that is not an official trailer.
- **Rule for the series: Phase 1 (Nov 12-18) uses official trailers plus narration only. Phase 2 (Nov 19 on) uses recorded gameplay only if the owner accepts the non-commercial limit.**

## 4. Two-week calendar (Thu Nov 12 to Wed Nov 25), one Short a day, two on launch day
| Date | Short | Footage | Facts to source on the day |
|---|---|---|---|
| Thu Nov 12 | Pre-load day: what you can do before launch | trailer clips | pre-load date and bonuses (Newsweek is one source; confirm on Rockstar) |
| Fri Nov 13 | The release date moved twice | trailers | 2025, May 26, 2026, Nov 19 (SEC, Bloomberg) |
| Sat Nov 14 | Trailer 1 broke a record: 93 million views in a day | Trailer 1 | [Tweaktown](https://www.tweaktown.com/news/105101/grand-theft-auto-6-trailer-2-fails-to-beat-the-world-record-set-by-1/index.html) |
| Sun Nov 15 | Trailer 2's 475M claim is not YouTube-only | Trailer 2 | [VGC](https://www.videogameschronicle.com/news/at-nearly-half-a-billion-views-rockstar-says-gta-6s-new-trailer-is-the-biggest-video-launch-of-all-time), [TechRadar](https://www.techradar.com/gaming/the-latest-grand-theft-auto-6-trailer-has-set-a-major-record-by-racking-up-475-million-views-in-just-24-hours) |
| Mon Nov 16 | $79.99 vs $99.99: what the extra $20 buys | trailer clips | Rockstar store page |
| Tue Nov 17 | What Rockstar lets you post about the game | the policy page, narrated | only after reading the page itself |
| Wed Nov 18 | Launch eve checklist (pre-load, bonuses ending Nov 20) | trailer clips | sourced items only; do not state a file size unless a source gives it |
| Thu Nov 19 AM | It's out (unlock time unconfirmed) | official launch/trailer clip | unlock time from Rockstar |
| Thu Nov 19 PM | First review scores | score screenshots with attribution, no game footage | OpenCritic/Metacritic (check) |
| Fri Nov 20 | The pre-order bonus window closed | | Newsweek point, re-confirm |
| Sat Nov 21 to Wed Nov 25 | One a day from a verified list: first-weekend sales if Take-Two gives numbers, GTA+ month, PC status, patch news | official trailers | each from a named source on the day |

## 5. Five sourced first-video ideas
1. **"GTA 6 has now been delayed twice"**: 2025, May 26, 2026, Nov 19, 2026; end on Zelnick's "It's November 19, 2026." Sources: [SEC release](https://www.sec.gov/Archives/edgar/data/0000946581/000162828026054580/ttwo1q27earningsrelease.htm), [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-21/take-two-confirms-november-debut-for-grand-theft-auto-vi), [Vice](https://www.vice.com/en/article/take-two-ceo-confirms-gta-6-release-date-is-locked-in-amid-pre-order-rumors/).
2. **"Trailer 1 got 93 million views in a day"** versus Trailer 2's 475M claim and why they are not the same number (YouTube alone reported at about 85-95M in roughly two days; 475M is Rockstar's all-platform claim). Sources: [Tweaktown](https://www.tweaktown.com/news/105101/grand-theft-auto-6-trailer-2-fails-to-beat-the-world-record-set-by-1/index.html), [PC Gamer](https://pcgamer.com/games/grand-theft-auto/rockstar-says-gta-6s-second-trailer-is-now-the-biggest-video-launch-of-all-time-whatever-that-means), [TechRadar](https://www.techradar.com/gaming/the-latest-grand-theft-auto-6-trailer-has-set-a-major-record-by-racking-up-475-million-views-in-just-24-hours). Fits our star-paradox lane.
3. **"You can download GTA 6 today"** (Nov 12 pre-load) and the bonuses that end Nov 20. Source: [Newsweek](https://www.newsweek.com/entertainment/gta-6-trailer-cost-rockstar-grand-theft-auto-12108972), a single source.
4. **"GTA 6 costs $79.99; the Ultimate costs $99.99"**: what the extra $20 buys (premium vehicles, weapons, apparel, plotlines per [GameBrief](https://www.gamebrief.net/blog/gta-6-release-date-price-pre-order-pc-2026); verify the list on the store).
5. **"Rockstar's rule for posting GTA footage"**: monetized channels aren't covered; cutscene-only videos get removed. Source: [Rockstar's policy page](https://support.rockstargames.com/articles/200153756/rockstar-games-video-policy). Read the page directly first.

## 6. Not done
- The competitor-channel review for GTA that the Account 2 brief mentions. I can run it on the PC once the owner names the channel.
- Direct reading of Rockstar's policy page (timed out); it is the first thing to re-read.
- Owner-only decisions: channel name, monetization yes or no, whether to record gameplay at all.
