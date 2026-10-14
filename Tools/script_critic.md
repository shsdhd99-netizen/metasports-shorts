# Script Critic v3 (Oct 14, 2026): the strict pre-production gate

**What it is:** every script passes this **before** footage is cut or a voice is generated. Critic v2 (`Tools/critic_v2.md`) still reviews the finished export; v3 decides whether the story is worth making at all.

**Why a new critic:** the old scoring rubric ran backwards again.
- **#40 Jokic's preseason pass** scored highest in the queue (63/70) and got **660 views**.
- **#39 oldest triple-double** scored 46 and got 4.0K.
- Critic v2 passed #40 and #41 on craft (one measure, answering ending, proof on screen). Both flopped.
- **So craft is not the problem a critic has to catch. The premise is.** v3 scores the story first and is allowed to reject a script that follows every formatting rule.

**Calibrated on** our posted Shorts with known views (section 5). A critic that would have passed our flops is broken.

## 1. How to run it
1. Run `python Tools/script_lint.py "<folder>/script.txt"`. It reports length, the first sentence, stacked numbers, jargon, cadence, repeated words and unknown names. These are **risks to weigh, not scores**.
2. Read the script **aloud at 225 wpm**, or play the voice take if one exists.
3. Score the 9 categories, 1-5, using the anchors below. Write **one sentence of reasoning per score**, about this story, not the rules.
4. Check accuracy: **pass/fail** against `notes.md`.
5. Give the verdict (section 3). On REWRITE or REJECT, write the rewrite in the same pass, and give 2-3 alternative openings and payoffs for anything that passes below 40.
6. Log it in `Research Notes/Script Critic Log.md` with a 48 h view guess. Check the guesses at 10 posts.

## 2. The 10 categories
| # | Category | 5 (strong) | 3 (borderline) | 1 (fail) |
|---|---|---|---|---|
| 1 | **Premise**: is it worth telling? | A famous player, team or object, plus a fact that changes how you see them, that a casual fan would repeat to a friend. Best with a human element (family, a feud, a kind act, a real quote) | True and a bit surprising, but only fans who follow the league care (contracts, milestones, schedules) | A technicality (preseason stats, eligibility, rules memos, lottery mechanics), a niche or G League player, or a retold story |
| 2 | **Hook**: does line 1 stop the scroll? | Names or shows the star or object, and states the surprising claim as a **statement** within about 3 s ("Stephen Curry just…", "Only two players can still wear six"). It opens a question the viewer can put in words | Intriguing but vague ("This pass doesn't even count": whose? why care?) or slow (over 3.5 s) | No subject, no stakes, a naked number ("Ninety-two point nine.") or a quiz |
| 3 | **Clarity**: can a casual viewer follow it immediately? | No term needs explaining; one idea per sentence; numbers you can hear | One jargon term explained in a line | Needs league knowledge (preseason, G League, two-way, apron) or 3+ numbers in a sentence |
| 4 | **Progression**: does every line add something? | Each line adds a new fact or raises the stakes; there is a **turn** ("But the craziest part…") and the craziest beat comes last | One flat stretch or a repeated fact | A list of facts with no turn (fact chain), or background before the story starts |
| 5 | **Payoff**: is the ending memorable? | Surprising, funny or moving, in the subject's own words or one line you'd quote (Giannis: "a moment this rookie will never forget"; #23: "LeBron James versus LeBron James Junior") | Answers the hook with a number | A recap, a hedge, a debate question or a CTA |
| 6 | **Voice fit**: will it sound natural from our narrator? | Reads like telling a friend: contractions, mixed sentence lengths, no tongue-twisters, every name in `pronunciation.json` | A choppy stretch or one awkward number run | Staccato fact chain (mean under 8 words a sentence), stacked numbers, untested names |
| 7 | **Visual potential**: is there footage for it? | The hook moment and the payoff moment exist as real footage; every line can be proven on screen | The hook has footage; the middle needs cards | No footage of the key moment (park it) |
| 8 | **Originality**: is the angle ours? | Most fans haven't seen this angle; not the night's headline | A known story with our own angle | The same fact every outlet posted, or our own old winner retold |
| 9 | **Retention risks** (5 = none) | No slow line, no predictable reveal, no filler, 20-30 s | One soft spot | Several: slow middle, number dumps, a reveal guessed at line 2, over 32 s |
| 10 | **Accuracy** | **PASS:** every voiced claim matches a dated source in notes.md, with qualifiers kept ("listed", "reportedly", "regular season") | | **FAIL:** an unverified or overstated claim. A FAIL is a stop, whatever the other scores |

## 3. Verdict rules
- **APPROVE** (go to footage and voice). All of these:
  - accuracy PASS
  - total of categories 1-9 is **36 or more out of 45**
  - **Premise, Hook and Payoff are each 4 or more**
  - nothing below 3
- **REWRITE:** accuracy PASS and the premise is 4+, but anything else misses. Rewrite in the same pass, then score the rewrite.
- **REJECT:** premise 3 or under (no rewrite saves a weak premise), or an accuracy FAIL that can't be fixed.
  - Say whether a new angle on the same news exists. If it does, write that version.

**Hard rules the score can't override:**
- **No hook promise the video doesn't keep.** #41 promised "taller than Wembanyama" and delivered an unknown G Leaguer: bait.
- **No question or CTA ending.**
- **No respelling inside the script** (use `pronunciation.json`).

## 4. Rewriting checklist (use it on every REWRITE)
1. **Lead with the person, not the thing.** "Jokic is about to break a record nobody thought would fall" beats "Nikola Jokic has 198 triple-doubles."
2. **One number per sentence. Round where accuracy allows.** Say the number the viewer needs, not every number in the notes.
3. **Find the human beat:** the subject's own words, a family link, a reaction. Our winners #22 and #23 both had one.
4. **One turn, placed at 60-75%**, before the payoff: "But here's the part nobody saw coming…"
5. **End on the line you'd quote**, then stop.
6. **Cut background that doesn't change the answer.** Read every sentence and ask "would the payoff land without it?"
7. **Read it aloud.** Every sentence should sound like something a person would say to a friend.

## 5. Calibration on posted Shorts (scored with the views known, so this checks fit, not a blind prediction)
Per-category scores and one-line reasons are in `Research Notes/Script Critic Log.md`.

| Short | Views (Oct 14) | Premise | Hook | Payoff | Total /45 | v3 verdict |
|---|---|---|---|---|---|---|
| #22 Only two can wear six | 31K | 5 | 5 | 5 | 41 | APPROVE |
| Curry Kobes (old) | 30.8K | 5 | 5 | 4 | 42 | APPROVE once the CTA is cut |
| #03 Nobody voted against Wemby | 26K | 5 | 5 | 4 | 41 | APPROVE |
| #19 How tall is Flagg | 20K | 4 | 4 | 4 | 36 | APPROVE (just) |
| #23 LeBron vs his son | 9.8K | 5 | 4 | 5 | 39 | APPROVE |
| #39 Oldest triple-double | 4.0K | 4 | 4 | 4 | 30 | REWRITE (stacked ages) |
| #12 Duren's $87M | 2.8K | 3 | 4 | 1 | 26 | REJECT |
| #29 Big men won't shoot underhand | 1.6K | 3 | 3 | 4 | 31 | REJECT |
| #41 Taller than Wemby | 1.6K | 3 | 4 | 3 | 30 | REJECT (the hook oversells) |
| #40 Jokic's preseason pass | 660 | 2 | 3 | 3 | 28 | REJECT |

**Fit:** v3 approves all 5 Shorts over 9K and holds back all 5 under 5K (n=10, small; re-check at 10 new posts).
- The old rubric (Creative System v3 §4) put #40 first in the queue. It no longer ranks the queue.
