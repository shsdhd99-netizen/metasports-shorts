# Final critic review of the five finished Shorts (Oct 15, 2026)

**What I could and could not check.** I looked at every render as a storyboard (a frame about every 0.5 s with its caption) and a few frames at larger size; I measured loudness and true peak, ran `qa_short.py --full` (every Short passes except one false alarm, below) and the footage log. **I did not hear any render and I cannot play video**, so voice quality, music taste and effect timing by ear are NOT judged. The speech-to-text check of the exports was skipped (no one Python has both cv2 and faster-whisper). QA flag that is a false alarm: "audio clipping at full scale" (the check mixes stereo to mono, +3 dB; real true peaks are -1.9 to -2.9 dBTP).

## What #36 and #42 do well (the owner's references), and what I carried to the others
1. **Line 1 is a claim about a famous name, within 3 s** ("LeBron James has missed more shots than anyone"; "LeBron's teammate from his rookie year now has a son in the NBA"). The new ones: "Jalen Brunson never made the shot that won Game 4", "Only four players in NBA history have won titles with three teams", "The Knicks' first banner in 53 years goes up Oct 20".
2. **One idea, escalating, one number at a time.** #42: 15,541, then Kobe's 14,481, then 50.7 vs 44.7, then 31,502. Numbers never stack in one breath.
3. **Real footage under every line, the player named is the player shown.** Words and numbers are drawn ON the footage, never on a card (the owner's Oct 15 note on AI sheets): the 8 stat/proof cards in #36 and #42 were replaced.
4. **A human payoff**, not a stat: a record shot and a smile (#42), a father-son link and "One LeBron" (#36), a coach's instruction (#45), LeBron's own words (#46), a punchline (#10).
5. **A viewer question out loud by about 5-8 s** ("So is he a worse shooter? No." / "So who won it?" / "So why, at forty-one?" / "Did the NBA plan this?").
6. **21-24 s, one take of the Alex voice, effects only on something visible** (2-4 per Short, never the same sound twice: the tool refuses repeats).

## Evidence from our own data (Posted Shorts metrics, Oct 14-15; Studio export Oct 14)
- The winners had a famous name plus a concrete, absolute claim and a human or tidy payoff: #22 "Two men can still wear six" (31K), #3 Wemby vote (26K), #19 Flagg height (20K). The weakest were technicalities and niche players (#11 38 views, #25's second upload 193).
- "Engaged-view ratio" sits between 44% and 60% for nearly everything we posted; it does not separate hits from flops. Views do, and reach is set mostly by the platform's first test of the opening seconds, which I cannot see. So I did NOT claim any change "improves retention"; the new look (words over footage) is an untested hypothesis. #44 (4.4K, the best new post of the week) already used real footage and a human payoff.
- No music cohort exists yet; the three music drafts are tests. Do not say music raised views.

## Per-Short verdicts (hard)
| Short | Hook | Story | Footage | Weak spots | Verdict |
|---|---|---|---|---|---|
| **#42 most misses** (v3) | strong: name + absolute claim, but frame 1 is a wide shot (LeBron small) | clear paradox, one fact per beat, ends on a number | all real; the airball is the only LeBron miss; words over footage | Kobe clips soft (720p, 2.7x); ending is a number with no new loop (the pinned comment carries it); pace 163 wpm counts digits as one word | **Ready for your ear.** Best candidate to post first (evergreen) |
| **#36 Boozer/LeBron** (v4) | good (rookie year teammate has a son in the NBA) | father-son link, three facts, ends on "One LeBron" | rookie clips now official and sharp-ish; no Carlos Boozer footage exists | the 2007 shots are Eastern Conference Finals, not the Finals (line says "NBA Finals"); 3x blow-up, soft; more names than I like | **Ready, with one decision for you** (the ECF-as-Finals shots) |
| **#45 Brunson/Anunoby** | good: contrarian, then "So who won it?" at 4 s | tight; the coach's line pays off the setup | official 1080p; ESPN lower-third proves "29 points" | the replay of the tip-in under the coach's words is a stand-in (no Mike Brown footage cut); 3.9 s hold (QA warns); wide angles on the miss; June news, so a history Short | **Ready for your ear.** Strongest story of the five |
| **#46 four teams** | strong: "Only four players ever" | stat-first, but the question "So why, at forty-one?" and his quote carry it | six eras of footage, each used once | LeBron's face for 57% of the runtime (QA warns); 2012/2016/2020/1983 soft; "role players" shot is a generic game; voice says "wanna" in the quote | **Ready, weakest visually.** Post after #45/#42 |
| **#10 v2 banner night** | good, but a date-driven news Short | the three-date ladder works; "That's a documentary" lands | the opening is the June ceremony, not the banner | has a hard deadline (post Oct 19-20 BEFORE the game); LeBron-heavy | **Ready, time-limited.** Post first or skip |

## Fixes I made because of this review (re-rendered, not just noted)
Card numbers collided with captions (moved above y=1040); two clips ended in another shot's cut (re-cut); a celebrity in the crowd was under the coach's line (replaced); a Sixers clip was #33, not LeBron (dropped); "in under three months" was false (rewritten); the Hub's older fan-clip versions were removed.

## Not done / still open
Hearing any of it; Drift keyframes (binary project file, no live tools); a sixth Short (no more narration credits worth spending: about 1,050 characters left); the Hub still holds one asset I could not delete (permission blocked).