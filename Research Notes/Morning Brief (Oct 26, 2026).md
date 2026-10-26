# Morning brief, Mon Oct 26 2026

Overnight run, about 12:50 AM to 9 AM ET. Usage ran out from about 4:20 to 8:40 AM ET, so some build work stalled (see "Not finished").

## 1. Post today (DRAFTs, your call)
| Channel | Short | When | Where |
|---|---|---|---|
| NBA | #69 Luka "Luka Just Did What Kobe Never Did 😳" (**v2 calm cut**) | 11 AM ET | NBA Hub |
| NBA | #70 Barkley "Chuck Failed A Test With The Answers 😭" | 4-5 PM ET (6+ h after #69) | NBA Hub |
| FC | S07 Leicester 5000-1 (**v2, no music**) | 12:30 PM ET (keep 1 h+ from NBA) | FC Hub |
| FC | S05 Pickford water bottle (v2, music) | Tue | FC Hub |

## 2. The key to retention (best answer so far)
1. **The first seconds decide reach.**
   - "Stayed to watch" tracks views (0.70, n=37).
   - All 6 of our 10K+ Shorts held 74%+.
   - Once people stay, they mostly finish (92% average viewed). The leak is the opening, not the middle.
2. **Open on one real moment and hold it.**
   - 3 or fewer shots in the first 5 s: 78.4% stayed, vs 66.5% with 4 or more (n=10 vs 27).
   - First line of 11 words or fewer: 72.6%, vs 62.2% for longer ones.
3. **Show it big. Proof goes on the footage, never on a card.**
   - No cards: 72.6% stayed; any card: 66.1%.
   - Winners crop wide footage to about 3:4 so players stay big. We were using thin 16:9 strips.
4. **Hacks that showed nothing for us:** forced loops, a sound at 0 s, push-ins.
5. **The topic still matters most.** Editing gets people through the door; the subject keeps them.

## 3. What the similar channels show (61 channels, 25,000 Shorts)
1. **Three winning families:**
   - **Countdown or game devices** (rankings 1/10 to 10/10, "last one is crazy", player-elimination games): about 180K for a typical Short. These are the fastest-growing in 2026. Ftblpranz went 0 to 188K subscribers in 5 months; roycebball reached 57K from 32 Shorts.
   - **Reposted clip + one funny caption:** 86K.
   - **Narrated story/moment** (us, Swishyyy, Hoopiverse, CoachClank, Ahmed's): 76K.
2. **Everyone shows the event in second 1.** Nobody opens on a card or a setup.
3. **Narrated channels that grow are moment-first:** one viral clip, plus who and why.
4. **Posting a lot doesn't explain who wins.** Some channels post 11 a day and some twice a week.
5. **Titles barely matter** (about 1.0x either way).

## 4. Posting: what's optimal
- **Time:** barely matters for us (0.09 link to views). YouTube says the same. Keep the slots; news goes out the morning after the game.
- **How often:** 1 a day per channel. Add a 2nd NBA Short only if it's as strong, 6+ h later. Never 3.
- **Tags:** not needed. YouTube says they play a "minimal role". Use 3-8 tags (about 100-150 characters) or none. **Stop filling the 500 characters.**
- **Description:** leave it empty (90-97% of our views come from the feed). No wall of tags.
- **Hashtags in the title:** none, or one (#nba / #football).
- **Judge at 72 h.** #48 had 25 views on night 1 and 14.6K two days later. Never re-upload.

## 5. Rules: were we feeding ourselves bad info? Yes, partly.
1. **Fast-cut and card rules came from generic advice and competitor averages.** Our own data says the opposite.
   - The QA script was fixed yesterday, but the old rules still sat in 6 files ("3+ cuts in 3 s", "1.4-1.9 s shots", evidence cards, "6+ clips").
   - An agent is rewriting those files now (see `Rules Review (Oct 26, 2026).md`).
2. **THE #42 FORMAT failed its own test** (1 of 3 reached 74%). It becomes one lane among several.
3. **The soccer rules rested on 3 Shorts.** S03, called a "flop", has since reached 14K.
4. **Soccer length:** the skill said 60-68 s, but QA fails anything over 60 s. Now it's under 59.5 s after tightening.

## 6. How to improve, automate and grow (efficiency)
1. **Add a free Gemini key.**
   - In the environment settings (cloud menu > Edit), add `GEMINI_API_KEY`, made at aistudio.google.com/apikey. Never paste it in chat.
   - Then `Tools/yt_watch.py` lets me *watch and hear* any Short: competitors' hits, and our own DRAFT before you post it.
   - This replaces vidIQ watching for free. Everygen's watcher needs the $29.99 Pro plan.
2. **Daily research runs by itself** at 5:43 AM ET, starting tomorrow:
   - last night's watchable NBA moments with video links;
   - soccer story ideas;
   - competitor outliers.
3. **Next automation (needs your OK):** a 2nd scheduled task at about 6:30 AM that *builds* the top pick into a DRAFT on the Hub. You'd only review and post.
4. **Daily retention without exports:** finish the one-time YouTube Analytics sign-in (`Tools Guide.md`, "Daily retention, automatically"). Then every Short's stayed % and retention curve arrive daily.
5. **Cut wasted effort:** 500-character tags, covers, title scoring, long cuts for other apps (paused).
6. **Grow with tests, one at a time:**
   - a weekly countdown Short ("3 times [star] did X", with a #3/#2/#1 badge; the tool is ready);
   - a replay of the key second;
   - music bed vs none (needs your yes);
   - FC at 12 PM vs 7 PM.

## 7. Built overnight
- **#70 Barkley:** moment Short, QA PASS, on the Hub.
- **Tools:**
  - `yt_watch.py` (the watcher);
  - `overlay.py` corner/badge counters;
  - `broll.py --blurfit-aspect 0.75` (3:4 framing; tested);
  - `cut_list.py` passes `replay` through so intentional replays pass QA.
- **Research notes:**
  - `Similar Channels (Oct 26, 2026).md` (+ data);
  - `Retention and Editing Upgrade`;
  - `Posting Study` (+ data);
  - `Rules Review`;
  - `Competitor Watchlist.csv`.
- **S08 Hand of God shirt:** voice recorded (52.9 s). Footage found and cut from the full 1986 broadcast (archive.org), with a shot plan for all 24 shots.

## 8. Finished after 9 AM (usage had run out 4:20-8:40 AM ET)
- **S08 Hand of God shirt:** built (52.8 s, music and no-music versions), full QA PASS, on the FC Hub for **Wed 12:30 PM ET**.
  - Frame 1 is the handball.
  - The plays are framed 3:4, and the handball is replayed at 0.5x under the £7.1M.
  - No cards.
- **Rule fixes applied** to the Playbook, START HERE, UPLOAD SCHEDULE, every skill and the Library specs. Change log: `Research Notes/Rule Changes Applied (Oct 26, 2026).md`.
- **QA:** new warnings for 4+ shots in the first 5 s and a first shot under 2 s. Clip-count gates are now warnings. Replays marked `"replay": true` pass the footage check.
- **Tags tool:** `tags_fit.py` now caps tags at 150 characters.
- **Still not done:** the overnight NBA moment scout. Tomorrow's 5:43 AM research task covers it.

## 9. Decisions for you
1. Add the free Gemini key? (Strongly recommended.)
2. NBA music bed test: yes or no?
3. OK a daily auto-build of the top pick as a DRAFT (never posted)?
4. Finish the YouTube Analytics sign-in for daily retention?
