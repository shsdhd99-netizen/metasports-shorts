# Why S02 and S03 underperformed, and how we stop it happening again (Oct 24, 2026)

Evidence tiers: **[V]** measured in our files or data; **[H]** a likely cause we cannot prove yet (three soccer Shorts is a tiny sample).

## The numbers (Studio, Oct 17-24)
| Short | Length | Stayed to watch | Avg % viewed | Views |
|---|---|---|---|---|
| S01 The goalkeeper who hid a cheat sheet in his sock | 60 s | **80.4%** | 94.0% | 30,099 |
| S03 Goalkeepers who danced on the line to win a final | 71 s | 64.7% | 71.8% | 1,576 |
| S02 Players who got in TROUBLE the day before a derby | 64 s | 56.2% | 74.5% | 1,265 |

"Stayed to watch" is the share of people who saw the Short in the feed and did not swipe past it. It is decided in the first second or two. YouTube keeps showing a Short only while that number is high, so the drop from 80% to 56-65% is the whole story: S02 and S03 were shown to a first test audience and then stopped. [V]

## What S01 did that S02 and S03 did not
1. **Frame 1 showed the promise.** S01 opens on Lehmann's hand going into his sock while the title on screen says "hid a CHEAT SHEET in their sock". S02 opens on a close-up of Balotelli's face (soft, with TV scan lines and a channel logo) under "got in TROUBLE": nothing on screen is trouble. S03 opens on Dudek's face under "DANCED on the line": the dance does not appear until 54 s. Many people watch the first second with the sound off, so the picture has to carry the hook by itself. [V frames; the cause is H]
2. **The hook word was a thing you can picture.** "A cheat sheet in their sock" is an object. "Trouble" is a category: it is never said again, and the story is really about fireworks and a fire. On Ahmed's Goal, titles built on vague words (trouble, drama, crazy, wild) have a median of 200K views against 277K for the channel (34 Shorts). [H]
3. **The promise came back fast and stayed.** S01 is back on the sheet of paper at 18 s and the rest of the story is about it. S03 spends its first 46 s on Liverpool's 3-0 comeback (a different story), names 11 people and clubs in the first 15 s, and reaches the dance at 54 s. S03 lost people through the middle: 72% average viewed against S01's 94%. [V measured from words.json]
4. **Length.** S01 ran 60 s; S02 64 s; S03 71 s. Ahmed's Shorts run longer, so length alone did not sink them, but anything over 60 s can be blocked worldwide by one copyright claim. [V rule]
5. **S02 went out on the same day as S01**, so the two competed for the same first audience. [H]

## What it was not
- **The title's shape (plural or singular).** CORRECTED later on Oct 24 (`Niche Study - Soccer Story Shorts`): the "318K vs 217K" comparison above was an era effect. Ahmed's singular titles all date from 2024, when his channel was tiny, and his plural titles sit exactly at his channel median (0.99x). Title shape is neutral. **Post the spoken line 1 as the title.** [V Ahmed data]

## What Ahmed's best titles have in common (his last ~390 Shorts)
The top of the list promises a human conflict with clear stakes: refused to play, rejected by their own country then got revenge, teammates who didn't like each other, bullied, disrespected, transfers that backfired. The bottom is news questions ("Is X about to be sacked?") and neutral facts ("players who started in a different position", "most interesting stats"). [V list; Research Notes/Ahmed Network Data (Oct 21, 2026)]

## What other creators' guides say (third-party, not YouTube's own data)
- The first frame is the hook in a Short: there is no intro, and sound is often off. Intro cards, logos and wide establishing shots are the common swipe triggers. [Prepublish](https://prepublish.ai/guides/youtube-shorts-retention), [AIbrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook)
- "Viewed vs swiped away" (what Studio now calls "Stayed to watch") is the main diagnostic; guides aim for 75-80% stayed, and say to compare against your own Shorts rather than a universal number. [Subscribr](https://subscribr.ai/youtube-strategy/youtube-shorts-analytics-metrics-growth)
- Our own NBA channel agrees: #42 and #48 (83-87% stayed) open on a sharp star close-up; #52 (59%) opened on a soft black-and-white archive frame.

## The rules from now on (in `.claude/skills/story-short/SKILL.md` and `Soccer Channel/Lessons Learned.md`)
1. **Frame 1 = the promise happening**: the object or the act in the title, sharp and lit, no channel logo, no scan lines. A face only when the title is about the face.
2. **The hook word is an object or a strong human verb** (hid, refused, banned, rejected, got revenge), never a category word (trouble, crazy, drama).
3. **Say and show the promised thing again by about 20 s**, and keep the story on it. One story; no more than about 10 names in the first 15 s.
4. **Under 60 s** (59.9 at most).
5. **One soccer Short a day.**
6. **Title = the spoken line 1** (plural is fine).

## What the tools now check (`Tools/qa_short.py`)
- **Gate:** frame 1 must be lit (the picture at 0.0 and 0.1 s, captions left out). This caught S04: its first 0.25 s was a dark blur of someone passing the camera. Fixed on Oct 24: S04 now opens straight on Zidane.
- **Warnings (story format):** the title's promise is not said again by 25 s (list the object and its synonyms as `"promise"` in cuts.json, e.g. `["sheet", "paper", "note", "sock"]`; otherwise the title card's CAPS words are used); more than 10 different names in the first 15 s.

## The four scheduled soccer Shorts, checked against the rules
| Short | Frame 1 | Promise back at | Names in 15 s | Length | Verdict |
|---|---|---|---|---|---|
| S06 5 goals in 9 minutes | Lewandowski's bicycle kick | 13 s | 7 | 58.8 s | fits |
| S05 Cheat sheet on a water bottle | Pickford, then the bottle at 0.7 s | 19 s | 6 | 59.7 s | fits |
| S07 Worse odds than the Loch Ness monster | Leicester lifting the trophy | 11 s | 5 | 55.2 s | fits |
| S04 Sent off in their very last game | Zidane (dark first 0.25 s fixed today) | 32 s (the headbutt) | 9 | 57.9 s | riskiest: its promise lands late, so it now goes out after S07 |
