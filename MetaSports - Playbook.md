# MetaSports — The Playbook

## THE RULES (Nov 7, 2026). Read this first. It wins over everything below and over every older file.
The owner approved the Theory Ranking on Nov 7 ("approve all ... refine rules to actually be useful and help you learn and make better videos").
- Evidence: `Research Notes/Theory Ranking and Rules Challenge (Nov 7, 2026).md`.
- Old text: `Research Notes/Rule History - Playbook THE RULES before Nov 7 rewrite.md`.
- Soccer: `Soccer Channel/Playbook.md` (rules F1-F6).

### How the rules work now (so they help us learn instead of just existing)
1. **A rule stays only if it earns its place.** It must be an owner rule, or the data backs it, or it is cheap house style that protects quality. Everything else is either a live test or scrapped.
2. **Every rule names its evidence and its check:**
   - **[V]** measured on our channels;
   - **[S]** small sample, or competitors;
   - **[O]** owner rule;
   - **[H]** house style (cheap, unmeasured).
   "Check" names the tool that enforces it, or the lab feature that re-tests it.
3. **The lab re-tests the rules by itself.**
   - `python Tools/lab.py auto` runs every day (daily-run step 6 and the stats check). It measures every Short, scores the live tests and writes `Research Notes/Lab/Scoreboard.md` plus a study of every part (`Research Notes/Lab/Study - all (<date>).md`).
   - Its **Rule check** table says, for each rule: SUPPORTED, NOT SHOWN yet, AGAINST (revisit) or, for scrapped rules, SCRAP STANDS or REVISIT.
   - On Sundays, any rule marked AGAINST or REVISIT is fixed or dropped here, with a dated line.
4. **Tests run themselves:**
   - At most 3 live per channel (`Research Notes/Lab/tests.json`); the rest queue.
   - Before scripting: `python Tools/lab.py assign nba|fc --folder <F>`. It prints the arm for each live test and writes the card's `**Arms:**` line. Follow it.
   - Arms are detected from the files (title, script, cuts, the uploaded file name), so nothing depends on remembering to log.
   - Score = the chance a B Short beats an A Short (50 = no difference).
   - A test decides at 6+ per arm with p 0.2 or less (score 70+ or 30-). At 12 per arm with no winner it closes as NO DIFFERENCE.
   - A decided test names the rule it changes. The next daily run edits that rule here, with the date and the score.
   - Edit, script, package or topic study on demand: `python Tools/lab.py study --part edit` (or `script`, `package`, `topic`, `length`).

### Owner rules (never relax them) [O]
- **O1** Drafts only. Never post, and never open YouTube Studio. Scheduling happens only through `schedule_ready.py` / `yt_schedule.py` (private + publishAt, guard rails). Never delete or re-upload a slow Short.
- **O2** Never put keys in chat, docs or git.
- **O3** Never invent a stat. Every claim has a source row in notes.md with its exact words, and two sources for numbers. Keep qualifiers.
- **O4** No promo, teaser or subscribe outro. The video stops on the payoff.
- **O5** No dead air: `tighten_voice.py` on every voice.
- **O6** No cards. When truly unavoidable: 1.5 s at most, never in the first 4 s. The proof goes on the footage.
- **O7** Under 60 s, ending before 59.5 s (`qa_final.py` fails longer). Our broadcast footage makes a Content ID block over 1 minute a real risk.
- **O8** Description empty; 0-1 hashtag. Tags are filled to about 490 characters by `tags_fit.py` (owner, Nov 1); a short tag list is a QA warning, never a fail.
- **O9** TikTok/Instagram get the same file (`crosspost.py`); no separate cuts.
- **O10** QA improves every day: one QA change logged in `QA Changelog.md`.

### Topic: what to make (the biggest lever)
- **N1 Premise first.** The subject and the first 3 s decide a Short; the edit doesn't. [V]
  - The stranger test: someone who doesn't follow the sport would stop for it.
  - One new sourced fact per Short.
  - Never retell a bigger channel's story: `copy_check.py` must say FRESH.
  - Check: `idea_gauge.py` 80%+, `build_gate.py`.
- **N2 NBA lanes, in this order:**
  1. **Family / kid / rookie stories** [V: 10.5K vs 4.7K, n=12/40, lab `topic_family_kid` SUPPORTED].
  2. **Last night's moment you can watch**, with one fact the clip can't show. It takes the 3:30 PM slot, the morning after or not at all [V: 9.3K, n=6].
  3. **"Who has ___ the most in NBA history?" lists and live star chases** [S: 25.6K, 24.0K, 5.6K; test `nba-lists`].
  4. Rule, history and news-explainer stories only when reframed as a curiosity you can watch: the underhand free throw got 29K as a curiosity, while the rule lane sits at 0.4x [V].
- **N3 About 70% of builds from proven lanes, about 30% from live tests.** Check: `lab.py assign`, `test_log.py status`.

### Script
- **S1 Line 1 is 11 words or fewer, says the strange thing, and frame 1 shows it happening.** [V: lab `script_line1_le11` SUPPORTED on NBA, 7.1K vs 4.0K] Check: `script_lint.py`.
- **S2 Turn early; every sentence adds a new fact; end on the payoff.** Never a question or a CTA as the last line; the debate goes nowhere (see P4). [S] Check: `script_lint.py`.
- **S3 Length:**
  - **NBA: 20-25 s** (about 60-85 words). [V: 25 s or less 7.1K vs 3.0K; lab `len_le25`] QA warns outside 18-27 s.
  - **FC: 50-59 s** (Soccer Playbook F2).
  - No pace target: the "over 230 wpm" idea did not hold up (lab `script_wpm_gt230`: 4.0K vs 7.1K). Use the voice_take default.

### Editing (house style: cheap, protects quality; none of it moves views measurably)
- **E1 Footage first:** secure frame 1 and one proof clip per beat before writing; never add filler to reach a clip count. Official league, team, broadcaster or archive footage, never another creator's edit. [H]
- **E2 Frame 1** is sharp, lit, big and moving; shot 1 runs about 2 s or more. [H; lab `edit_shot1_ge2` NOT SHOWN yet] Check: `qa_portions.py`, `qa_short.py`.
- **E3 Fill the frame:**
  - wide plays at a 3:4 window over blur (`"blurfit_aspect": 0.75`);
  - full width only for something that must be read whole;
  - name a person, show the person.
  [S] Check: `qa_short.py` and your eyes on the contact sheet.
- **E4 Proof on the footage:** words over the play (`overlay.py`) or a circle on the scorebug. No emoji stickers, no decorative SFX (one only for a visible event). [S]
- **E5 Replay the key second once** before the payoff when the footage has it (`"replay": true`). [H]
- **E6 Ending:**
  - hold the payoff on screen about 2-3 s (QA warns under 1.8 s) [S: hits keep 0.88 of viewers at 90% of the runtime, flops 0.65];
  - a natural loop into frame 1 is a queued test (`nba-loop`, `fc-loop`); never add a shot just to loop.
- **E7 Music:**
  - NBA: no music; render one file. The Oct 26 alternation never ran (almost every post went without music) and was dropped on Nov 7.
  - FC: the live test `fc-music` decides; the uploaded file name logs the arm automatically.
  - Real audio on a famous live call: queued test, render it only for that.
- **Scrapped on Nov 7** (no effect in our data, and they caused re-cuts; the lab keeps re-checking them): cut counts in the first 3 or 5 s, average-shot targets, "6+ source clips", "one source under 35%", "same source back-to-back", talking-head and b-roll shares.

### Package and posting
- **P1 Title:** short and searchable (the name + the key word). A statement or a Why/How/What/Who question both work. No ALL-CAPS words. [V: question vs statement no difference; test `nba-opener`]
- **P2 Posting grid:** NBA 7:15 AM (planned Short) and 3:30 PM (last night's moment); FC 12 PM ET (`next_gap.py`).
  - Up to 3 a day per channel, 6+ h apart, only if each is as strong (owner, Nov 5).
  - Don't chase hours: the NBA morning slot looks better (7.6K vs 5.0K), but p is 0.17, so the lab keeps watching `pkg_morning`.
  - Test: `nba-cadence` (1 vs 2 a day).
- **P3 News goes up the morning after or not at all.** Judge at 72 h; never at the next morning's check. [V]
- **P4 Pinned comment: optional.** When used, it's a source line ("Source: AP recap, Nov 6") or a "Part 2" pointer. No debate questions: comments aren't a ranking signal [V YouTube]. In Studio (owner step), link a series Short to its "related video".
- **P5 Cover:** one quick frame; the Shorts feed shows none. [V]

### QA and measurement
- **Q1 `qa_final.py` must say SHIP before a Short is scheduled.** Hard fails: facts and sources, files (1080x1920, 15-59.5 s), title, voice words, loudness and peaks, a dark frame 1, black or frozen frames. Everything else is a warning. LOOK at frame 1, every overlay and the last frame.
- **Q2 Judge a Short at 72 h.** The lab reads it 5-8 days after go-live, because the API runs about 2 days behind.
  - First choice: stayed % (Monday Studio export; 74%+ is the target) [V: 10.4K vs 3.8K, rank correlation 0.75].
  - FC stand-in: avg % viewed 85%+.
  - NBA has no API stand-in, so NBA is read on views.
- **Q3 Lanes:** PROVEN, TESTING or RETIRED (`Research Notes/Test and Learn Policy (Nov 5, 2026).md`); the lab's lane tests feed it.

## OLDER MATERIAL BELOW (history; THE RULES above win wherever anything below disagrees)

## Oct 22, 2026 (owner): no promo at the end, no dead air
- **No outro or promo** of any kind ("that will instantly kill retention"). The video stops on the payoff. (THE #42 FORMAT already ends this way; keep it so.)
- **No unnecessary pauses.** After the voice, run `python Tools/tighten_voice.py --folder F --thresh 0.25 --keep 0.12`.
  - It cuts every pause over 0.25 s to 0.12 s and the tail to 0.25 s.
  - The values are gentle so the real-audio quotes keep their rhythm.
  - Then run `anchor_shots.py`, move the sfx times, and run `assemble.py`.
  - The queued drafts #62, #63, #52, #60 and #59 were done this way on Oct 22.

## Oct 21, 2026: what Ahmed's network adds for MetaSports (evidence-tiered; THE RULES at the top win)
Sources:
- `Research Notes/Ahmed's Network and a Second Channel (Oct 21, 2026).md`
- `Research Notes/Story Format Study - Ahmed (Oct 21, 2026).md`
- Data: 3,154 Shorts across Ahmed's Goal, Basketball and Business.

Changes to how we work:
- **[V] Money and contract stories are the weakest NBA theme there too:** Ahmed's Basketball median 93K vs 159K overall. That is now two independent sources (ours and his), so keep contract stories only with a rule, a number gap or a funny detail as the hook.
- **[V] Cadence:**
  - Ahmed's steady state is about 2 a day per channel. When they pushed to about 3 a day (Jul-Sep 2026), medians fell and they pulled back.
  - **Ours (Oct 26):** up to 2 per channel per day. The 2nd only when it's as strong, 6+ hours later. Never 3. [S] Posting Study §1d.
- **[V] Series titles:** a title that works is reused for a new story ("Episode 2...12" on 126 of his Basketball titles). When a #42-format Short beats the channel median, its accusation title can become a series with a new star. HYPOTHESIS for us: log it in the Outcome Log when tried.
- **[V] Holding the first picture works for them:** the first picture holds about 2.5 s under a title card (0-1 cuts in 3 s), at 159K median. This backs holding the opening moment (THE RULES §2 at the top).
- **[V] They run a quiet music bed** about 20 dB under the voice. This is evidence for the open music A/B; the owner's Oct 14 call (no bed by default for MetaSports) still stands.
- **[HYPOTHESIS, test once]** Ahmed's 60-75 s story format: one NBA story told that way (title read as line 1, "Back in...", a turn every 10 s, a payoff number), posted in a normal slot. Compare stayed % and views to the #42-format posts that week. The tools now exist (`/story-short`, `--caption-style ahmed`, `cut_list.py`). Only with the owner's OK.
- **New tools usable on NBA Shorts:**
  - `Tools/cut_list.py` (one cut list cuts every clip, pins shots to words, fills sources.csv, draws the contact sheet);
  - `Tools/stock.py` (Mixkit stock for abstract lines);
  - `broll.py cut --blurfit` / `--delogo`; `--blurfit-aspect 0.75` keeps a 3:4 window of a wide play so the players fill the frame (Oct 26).

## THE WINNING FORMULA (canonical, Oct 14, 2026, night; updated that night with the #40/#41 results, Script Critic v3 and the owner's music and voice calls, and on Oct 15 with the YouTube Studio export). THE RULES at the top win over it (Oct 26 overnight review). Where anything further below disagrees, this section wins.
**Why this exists:**
- The owner asked to stop changing formats and rules every day.
- This page is the formula. Change it only on the rule in step 10.
- **Evidence:** `Research Notes/Winning Formula Research (Oct 14, 2026).md`, which covers:
  - our 102 Shorts
  - 12 old scripts as voiced
  - our best Shorts, Curry Kobes (30.8K) and Giannis game ball (28.3K)
  - CoachClank's 148 Shorts
  - Ahmed's
- **Nothing here guarantees views.** Distribution and topic still matter most.

### The premise test (new, and the most important rule)
**A famous player, team or object, plus a fact that changes how you see them, that a casual fan would repeat to a friend.** Best with a human element: family, a feud, a kind act, the subject's own words.
- **Never:** a technicality (preseason stats, rules memos, lottery or eligibility mechanics), a niche or G League player, or a story we already told. [S, n=22 new-era posts]
  - The bottom 6 were all technicalities, niche players or retells: 38 to 1.6K views. #40's preseason pass got 655.
  - The top 4 all had a famous subject and a retellable fact: 9.8K-31K.
  - Audit §12.
- **Script Critic v3 is advice, not a gate (Oct 26 overnight review)** (`Tools/script_critic.md`). [S] Rules Review §2 item 14.
  - Only its accuracy check (pass/fail) blocks a script.
  - Its premise, hook and payoff notes are worth reading; its score is not a pass mark.

### The hook gate (new Oct 15, from the YouTube Studio export; audit §13)
**"Stayed to watch (%)"** in Studio is the share of people who watched instead of swiping away. It tracks views more closely than anything else we measure: Spearman **+0.77** (n=20 new-era Shorts). Every Short at 73%+ stayed got 4.0K-31.8K views; every Short under 60% got 1.4K-4.8K. [V correlation; causation unproven, because the topic drives both]
- **Target: 74%+ stayed, read at 72 h (Oct 26 overnight review).** [V] Why NBA Views Dropped §1; Posting Study §1g.
- **Line 1 = one absolute, curious claim about a famous name or object, in one sentence of 11 words or fewer** (Oct 26 overnight review; [V] Retention Upgrade §1b). The words that did it: "only", "every… until", "never… until", "just [did]", "grew two inches".
  - 82%: "Only two NBA players are still allowed to wear number six."
  - 80%: "Every Defensive Player of the Year in NBA history had at least one voter who picked somebody else."
- **Line 1 never:**
  - opens with a number or a stat line ("Ninety-two point nine." → 48%)
  - lists penalties or details ("…took five first-round picks, fined them $30 million, and suspended…" → 50%)
  - centres a player casual fans don't know ("Knicks center Mitchell Robinson…" → 56%)
- **Checked by** `Tools/script_lint.py`: it flags number-led, list-like and long first lines. Script Critic v3's Hook note is advice.
- **Length doesn't matter in 22-33 s** (-0.05). Write what the story needs; don't trim for its own sake.
- **Views arrive in the first week, then stop** (#22: 17,206 in week 1, then 9). The 72 h and 7-day reads are the result. Ship the next one rather than nursing a weak post.

### What wins (sorted by how sure we are)
**Supported by several independent examples:**
1. **Line 1 states the surprising thing about a named player, as a statement, within about 3 s** (the hook gate above). "Stephen Curry just pulled one of the wildest sneaker moves…" / "Giannis just saved a rookie's first NBA memory."
2. **The footage is the exact moment** under every line. The proof is on screen.
3. **Tell it like a story to a friend.** Flowing sentences, one turn ("But the craziest part…", "Then it gets crazier", "but not this time, because…"), one short reaction aside.
4. **Lanes (Oct 26 overnight review):** see THE RULES §1 at the top. Moments are about half; a star paradox, same-day news and a weekly countdown test rotate through the rest.
5. **End on the payoff:** the answer, the number, or the feeling. Then stop. **Best: a person's reaction or own words** (Giannis: the rookie's face; #19: Flagg's "I'm 6-10"; CoachClank's top: Jokic clapping, Shaq's reason). Competitor breakdown, Oct 15: 5 of their top 9 vs 1 of their median 5.
6. **Voice from 0.0 s to the last frame**, no dead air.

**Promising, not proven:**
- fresh "just happened" moments
- (retired Oct 15: "20-30 s for one story". Length shows no link to views in 22-33 s, so length is whatever the story needs)
- (retired Oct 14 night: "a quiet music bed". The owner dropped beds)

**From the competitor script breakdown (Oct 15; real captions, n small; checks, not rules):**
- Say the viewer's question out loud by about 6-8 s, after the scene, never as line 1.
- Escalate (normal → strange → punchline); numbers only as a ladder.
- Two names is plenty for 25 s.
- Same topic, two scripts: CoachClank's underhand Short (10.9M, 25× their norm) opened on a scene and used 1 number; our #29 (1.4K) opened on a niche player's stat and used 8. `Research Notes/Competitor Script Breakdown (Oct 15, 2026)/README.md` §4.4.

**Creator-specific (don't copy):**
- CoachClank's own narrator and 265-309 wpm
- Ahmed's 60-120 s "Players who…" lists

**Owner preference (kept):**
- no hook headline text
- white Montserrat captions
- no background music bed (Oct 14 night; this replaced "music on")
- no vine boom

### The three structures (pick one per Short; no new formats)
| Structure | Use when | Beats (each line gets its own proof shot) | Our proof |
|---|---|---|---|
| **A. Moment + hidden detail** (first choice when a fresh moment exists) | a star did something visible in the last few days | 1. "[Star] just [did X]." → 2. the concrete detail → 3. the reaction or proof → 4. "But the craziest part…" the hidden detail → 5. payoff line | Curry Kobes 30.8K, Giannis 28.3K, Bronny 1v1 65K |
| **B. Paradox / record** | a fact that "can't be right" | 1. the paradox on the object → 2-3. facts on ONE measure, told as a story → 4. the turn → 5. the answer as one number or the subject's words | #22 31.8K, #03 27.0K, Korver 31.1K |
| **C. Arc** | a career, a family, an ending | 1. the feeling in one line → 2-4. escalation, craziest last → 5. the line that lands the feeling | Chris Paul 28.4K, Keldon |

### Fixed production settings (do not change per video)
| Item | Setting | Source |
|---|---|---|
| Length | whatever the story needs, normally 20-30 s, about 85-110 words | old hits 20-32 s; CoachClank's 20-62 s Shorts beat their under-20 s ones 2.8×; Studio export: no link to views in 22-33 s (-0.05) |
| Voice | **A (Alex) or F (our old voice, fixed), the owner's pick from the two real edits of #21 v5 and #36 v2.** Until the owner picks, the `voice_config.json` default stays A, and F is "backup". After the pick: one voice, no switching | Voice Audition README, Parts 3-4 |
| Names | `Tools/pronunciation.json`; never respell inside scripts | same |
| Music | **No background bed by default** (owner, Oct 14 night). Clean narration; effects only where the picture makes the sound; silence is fine. A real song only through the platform's own library (route A), when it adds something | `Library/Sound Library.md` |
| Copyrighted/trending songs | only through the YouTube app's "Add sound" picker, by the owner at upload, on a "for the app" render | `Library/Sound Library.md` §2 |
| Captions | house style (white Montserrat caps, 45-62% band) | Playbook §5 |
| Proof | every clip logged and verified in `sources.csv` | B-roll Sourcing Guide |
| QA | `qa_short.py` PASS + frame sheet + transcript of the final audio + Critic v2 | Playbook §5 |

### The 10-step workflow (every Short)
1. **Pick:** a fresh moment or a paradox about a famous subject (the premise test above). A casual fan must get the question by about 3 s.
2. **Lock the facts:** dated sources in `notes.md`.
3. **Footage first:** frame 1 plus one proof clip for every beat (`x_clip.py`, `broll.py cut`), from any number of sources. Never cut away to filler to reach a clip count (Oct 26 overnight review). No footage, no script.
4. **Write, then the critic (advice):**
   - Choose structure A, B or C and write in story voice.
   - Run `python Tools/script_lint.py`, then read **Script Critic v3** as advice. Only its accuracy check blocks (Oct 26 overnight review). Log it in `Research Notes/Script Critic Log.md`.
   - Read it aloud at 220 wpm: it should run 20-30 s.
5. **Voice:** `voice_take.py` (house voice, gate, pause cap), then `voice_check.py`. Fix names in `pronunciation.json`.
6. **Edit:** `anchor_shots.py`, then `assemble.py` with `music.json`. Follow THE RULES §2: hold the opening, replay the key second once, fill the frame. Hold the payoff shot longest.
7. **Sound:**
   - No bed.
   - Effects only where the picture makes the sound.
   - If a real song would help, note it in PACKAGE.md for the owner to add in the app.
   - Run `python Tools/deflash.py` on any clip the flash scan flags.
8. **QA:** `qa_short.py`, the frame sheet, the transcript of the final audio, a flash check around cuts, then Critic v2.
9. **Package and Hub:** PACKAGE.md (with the Music and sound block), the Hub upload, the queue status. **The owner posts.**
10. **Read and decide:** judge each post at 72 h and read it again at 7 days, in the Outcome Log. Studio's "Stayed to watch (%)" first (target 74%+), then views (Oct 26 overnight review). Views stop after week 1, so the 7-day read is the result.
    - **One A/B test at a time.**
    - Change this formula only on n≥3 posts pointing the same way, or one very large effect.
    - Never change two things in the same week.

---

## CREATIVE SYSTEM v3 (canonical, Oct 14, 2026). It replaces the Oct 13 "Strict Short Formula" and overrides any older line below.

**Built from:** our own results first.
- `Research Notes/Posted Video Audit (Oct 14, 2026).md`: 102 Shorts, analytics, 10 retention curves.
- `Research Notes/Rules Audit (Oct 14, 2026).md`: every rule marked KEEP / REVISE / RETIRE / TEST, with its evidence and its test.
- External research (CoachClank and others) only where it adds something; marked [E].

**Tiers:** [V] verified in our data · [E] external · [H] hypothesis.

**Nothing here guarantees views.** In our data, the biggest single factor is the channel's distribution state: the old era's median was 29.8K, the new era's is 2.8K. Craft can't fix that alone.

**Queue:** `Production Queue.md`. **Critic:** `Tools/critic_v2.md`. **The Oct 13 formula's full text** is in git history (commit 5234797).

### 1. What wins on this channel (the evidence in one paragraph; old-vs-new creative comparison: Posted Video Audit §10)
- **The pattern [V]:** the Shorts that reached the old-era band all give a casual fan, within about 3 s, something **specific, visible and surprising**:
  - a rule paradox on an object (#22, the #6 jersey)
  - a record paradox on a star (#03)
  - a number you can see (#19, Flagg's height)
  - a viral moment with a hidden reason (Curry's Kobes)
  - a kind act (Giannis)
  - a legend's sad ending (Chris Paul)
- **The low performers [V]** either:
  - opened on something with no stakes (#20 "Ninety-two point nine.", #29 a niche player's stat)
  - delayed the story with dense context (#13's 6-second hook, #12's contract cliff at 4-6 s)
  - were the night's most-covered fact (LeBron's 23rd season: 5.3K, even with winner-level retention)
  - were generic hype (the old Flagg Short: 4.9K)
- **Retention moves with views** (Spearman +0.52 new era, +0.45 old) [V], but it is **necessary, not sufficient**.
- **94.5% of views come from the Shorts feed** [V]. The first second is the whole game. Titles and tags barely matter for reach.

### 2. Pick the format first (Hook / Context / Payoff is the default skeleton inside each)
| Format | When | Shape | Our examples |
|---|---|---|---|
| **1. Paradox** (no longer the default: see THE RULES §1) | a fact that "can't be right" | Hook: the paradox over the object (≤3 s) → Context: facts on ONE measure, a new one every 2-3 s → Payoff: the answer as one number or the subject's own words | #22 31.8K, #03 27.0K, #19 20.6K, #40, #41 |
| **2. Moment + hidden reason** | a viral or visible moment fans half-saw | Hook: the moment itself on screen (a cold open of 0.5-1 s of action before the voice is allowed) → Context: what nobody noticed → Payoff: the reason | Curry Kobes 30.8K, Giannis game ball 28.3K |
| **3. Emotional arc** | a career, a family, an ending | Hook: the feeling in one line ("Chris Paul is proof that even legends don't get the ending they deserve") → Context: 3-4 beats of escalation → Payoff: the line that lands the feeling. A slower pace (about 220 wpm) is allowed | Chris Paul 28.4K, #23 father vs son 9.4K (top like rate) |

**When to break the default** (each needs one line of reasoning in PACKAGE.md):
- **Cold open:** the picture is the hook (a dunk, a fight, a gesture). Let 0.5-1 s of action play before the first word.
- **Reveal-first:** the answer IS the surprise ("He's 0-for-his-career from three"). Say it first, then show why.
- **Setup longer than 3 s:** only when a non-fan can't get the paradox otherwise. Measure time-to-question, and write it down.
- **Chronological story:** arcs only (format 3).
- **Never break:** accuracy, proof on screen, and no re-posts.

### 3. The checklist (every Short, before "ready")
1. **Premise:** a casual fan can state the question by about 3 s. Write that question. **Not** the night's most-covered fact, and **not** our own old winner retold.
2. **Frame 1:** the object, moment or person, readable at phone size, with a scale or context reference when the story is about size. No logo, intro, card or wide crowd.
3. **First line:** one idea, 11 words or fewer, no compound sentence, no naked number. A name or object plus the twist (Oct 26 overnight review).
4. **Context:** every sentence adds a fact or raises stakes; one measure (format 1); escalation (format 3). No background stretch.
5. **Payoff:** answers line 1 and fulfils the title. One number, or the subject's own words, then stop. No question, CTA or hedge.
6. **Accuracy:** every claim has a dated source in notes.md, and qualifiers are kept ("listed", "probably", "regular season"). Confidence comes from specifics, not from overclaiming (#17's "BAN" title cost retention).
7. **Proof on screen:** the right person on their name; the number visible (the broadcast scorebug, circled, when it's the exact game); the quote with its source. No footage that merely resembles the story; no team colours under another team's name. **Every clip logged and verified in `sources.csv`** (`Library/B-roll Sourcing Guide.md`); no agency photos taken from news posts.
8. **Footage-first:** frame 1 and a proof clip for every beat are secured **before** voicing.
9. **Voice:** the house voice in `Tools/voice_config.json` (Alex since Oct 14 night; see section 6), about 220-230 wpm. Every name and number heard correctly by the recogniser. No dead air over 0.6 s. Key numbers made to land by the edit (caption colour, circle, music drop, a cut-in pause), since the voice reads them flat.
10. **Captions:** readable, clear of faces, action and overlay text; no lone-word cards. **Cards:** none (owner, Oct 26). If one is unavoidable: 1.5 s at most, never in the first 4 s. **No emoji stickers.** (Oct 26 overnight review; [V] Why NBA Views Dropped §2, [S] Retention Upgrade §2b.)
11. **Sound:** no bed by default (owner, Oct 14; this line said otherwise until the Oct 26 overnight review). When a bed is used on purpose: chosen by story type, 20 dB under the voice, with the payoff marked by the music (silence, stop, swell or hit) and dropped under real quotes; the track logged in `music_library.csv` (`Library/Music Guide.md`). Effects only where the picture makes the sound, or on the single reveal. The voice at -14 LUFS; true peak ≤ -1 dBTP.
12. **Render:** inspected end to end (frame sheet + transcript of the final audio). `qa_short.py` PASS, then Critic v2 PASS (a separate agent), then the owner's listen.
13. **Package:** the title is a short statement of the premise and goes up **exactly** as written; no hashtag or one (#nba); tags filled to 490 characters (owner, Nov 1); no description; the debate question in the pinned comment (Oct 26 overnight review; THE RULES §3).

### 4. Scoring rubric (RETIRED for ranking, Oct 14 night: it put #40 first and #40 got 655 views; Script Critic v3 ranks the queue now; keep this only for feasibility notes)
| Factor | Weight | 1 | 3 | 5 |
|---|---|---|---|---|
| **Clarity in second 1** | ×3 | needs explaining | clear by about 4 s | the question lands with frame 1 + line 1 |
| **Novelty of the angle** | ×3 | everyone posted it | known event, our own angle | most fans haven't seen it |
| **Visual proof secured** | ×2 | no footage yet | some beats proven | frame 1 + every beat proven |
| **Stakes / emotion** | ×2 | trivia | mild surprise | unfair, funny or moving |
| **Audience name** | ×2 | niche player | known starter | LeBron/Bronny/Curry/Wemby/Jokic tier |
| **Pacing fit** | ×1 | needs 30 s+ of setup | fits about 25 s | fits 15-22 s |
| **Feasibility** | ×1 | days | hours | under 2 h |
| **Accuracy** | gate | fails → do not build | | |

- Maximum 70. Write the score and a 48 h view guess in the Outcome Log **before** posting.
- At 10 posts, check Spearman(score, 48 h views). If it is under 0.3, revise the weights.

### 5. Editing playbook (the defaults; QA FAILs are marked)
- **Frame 1:**
  - Push in gently (≤6%) only if the subject is small.
  - **Planned:** let 0.5-1 s of action open format 2.
- **Cuts (Oct 26 overnight review; THE RULES §2):**
  - Shot 1 runs at least 2.0 s. At most 2 shots in the first 3 s and 3 in the first 5 s.
  - About 10-15 shots of about 2 s. Let a play run 3-5 s.
  - Replay the key second once before the payoff: closer and/or at 0.5x, marked `"replay": true`.
- **Framing (Oct 26 overnight review):** crop wide plays to about 3:4 (`broll.py cut --blurfit --blurfit-aspect 0.75`). Full-width blur-fit only for a graphic or text that must be read whole. No emoji stickers.
- **Proof first** (full method: `Library/B-roll Sourcing Guide.md`):
  - Each line's picture must show what the line says (the critic's top finding in 3 of 3 builds). Exact player, game or moment beats generic footage; the old hits did this in 8/11 and 11/13 shots [S].
  - **Revised Oct 14:** when the clip IS the game being described, **keep the scorebug** and broadcast banners as proof, and circle the number when it's named (`broll.py circle`). Old hits: Luka's 1.5 s clock and 126-125 score; Kobe's "60 POINTS" [S].
  - Crop scorebugs only on stand-in shots (a wrong opponent is a critic FAIL, #39). Always crop tickers, watermarks and other creators' captions.
  - **Secure the opening visual before the script is final.**
  - Every clip gets a row in `sources.csv` (written automatically by `x_clip.py` and `broll.py cut`), checked with `footage_lib.py sheet` and marked with `footage_lib.py verify`. QA FAILs a missing or unverified clip once a log exists.
  - Never use agency photos (Getty, Imagn, AP) taken from news posts: #41's Dallas still was one (replaced in v3).
- **Movement:** only to reveal a detail or follow the ball. No random zooms, no flash cuts.
- **Cuts:** look at the 30 fps frames around every cut. A clip's first frame or its own internal cut can flash for one frame (#21 had two); fix with `in` or the shot start.
- **Captions:**
  - House style (white Montserrat ALL CAPS, the 45-62% band).
  - Re-crop the shot or move the band if a face sits in it (per shot: `"cap_y": 1305` in shots.json = 68%; default 1185).
  - The chunker now avoids lone-word cards (Oct 14).
- **Payoff visual:** the strongest image lands on the payoff line, never before it (an overlay can reveal in two steps, as #41's 350 → 0 did). **Hold the payoff shot longest** (the old free-throw hit held its payoff 3.5 s) [S].
- **Escalation:** where the story has them, build to the payoff with a count-up (Kobe 51-53-56-60) or escalating examples, the craziest last [S].
- **Ending:** cut on the last word, plus a 0.15-0.4 s tail. **No forced loop (Oct 26 overnight review):** end on the payoff. Loop into frame 1 only when that image is the payoff; never add a shot just to loop.
- **Sound (SUPERSEDED Oct 14 night: no background bed by default; see the Winning Formula and `Library/Sound Library.md`. The lines below apply only when a bed is used on purpose):**
  - A quiet bed (`music.json`, `bed_lu` -20, house range -24 to -16) chosen by story type:
    - stats/paradox → "Clever pulse"
    - reveal → "Dark build"
    - high energy/countdown → "Trap pulse"
    - emotional → "Warm piano"
  - **The payoff is marked by the music:** a beat of silence before the turn, the music stopping before the punchline, a swell, or the track's hit on the payoff line.
  - Music **always drops under real quote audio**.
  - QA FAILs a bed that crowds the speech band (under 12 dB at 1-4 kHz) or a track missing from `music_library.csv`.
  - Dry only when silence is the story (say why in PACKAGE.md).
  - Effects: 2-5, only where the picture makes the sound (whoosh on a circle, rim on a miss). The current `Tools/sfx` files have an unknown licence: replace them over time.
  - No clipping: music renders limit at -3 dBFS.
- **Emphasis** (Voice Audition part 2: our voice delivers numbers flat, -0.4 to +0.2 dB vs other words, and "..." adds only ~0.05 s):
  - Make key numbers land through the edit: a coloured caption, a circle, the music dropping, a cut-in 0.3-0.4 s pause before the payoff line (TEST P1).
- **QA gates:** the code of `Tools/qa_short.py` is the source of truth; read it there. The Oct 14 list that stood here ("fewer than 6 sources", "one clip filling 35%+", "3 shots in 3 s", short shot caps) was removed (Oct 26 overnight review). As of Oct 26 (Rules Review §5 O):
  - **FAIL:** voice starts after 0.4 s; a filler first word; no action footage in the first 3 s; a shot too long (NBA over 6 s, soccer over 3.6 s); a card over 1.5 s or in the first 4 s; dead air over 0.6 s; loudness off -14 by 1.5 LU; frozen or black frames; a dark frame 1; sound still ringing at the end; a quote shot not at 1.0x; voice cut off; an uncleared music track or one crowding the speech band; a clip missing or unverified in `sources.csv`; length outside the profile (NBA 12-60 s, soccer 50-59.9 s).
  - **warn (fix when it hurts the story):** shots in the first 3 s, average shot (1.8-3.0 s), clip count and clip share (NBA), talking head and b-roll share, card share, the same footage twice (a shot marked `"replay": true` is allowed), pace, slow hook, naked-number opening.

### 6. Voice (replaced Oct 14, night: see the Winning Formula and `Research Notes/Voice Audition (Oct 14, 2026)/README.md`, Part 3)
- **House voice:** Alex (`yl2ZDV1MzN4HbQJbMihG`), multilingual_v2, speed 1.2, stability .5, similarity .75. No denoise, no stretch, pauses capped at 0.38 s, a gentle compressor in the render.
  - All of it lives in `Tools/voice_config.json`.
- **Backup:** our clone "pham v2" at speed 1.1, stability .5, no denoise.
- **Why the old setup sounded wrong** [V]:
  - The clone is a copy of TTS recordings.
  - It ran at 259-267 wpm.
  - The light denoise removed two thirds of the s/t/f detail.
- **Pronunciation:** `Tools/pronunciation.json`. Never respell Wembanyama. Test each new hard name on one line first.
- **Never:**
  - stretch the voice
  - use Flash
  - put a spoken number next to a number-like word
- **Owner's ear:** Sound Check round 3, https://claude.ai/artifact/U58nqkg8BHDTJXNdy64Tcd

### 7. Experiments (FROZEN Oct 14 night: one test at a time. Only #1 is running; the rest are parked or house style. See the Outcome Log, "formula freeze")
1. **Red ring in frame 1:** #40 (ring) vs #41 (plain), then 2 more pairs.
2. **No card before 4 s:** every build follows it; compare at n≥6.
3. **Posting rate:** decided Oct 26: up to 2 per channel per day; the 2nd only when as strong and 6+ h later [S] Posting Study §1d.
4. **A premise pill on frame 1:** 3 pairs, needs the owner's OK (it breaks the no-headline rule) [B12].
5. **Format 2 with a 0.5-1 s cold open.**
6. **The prediction check:** score vs 48 h views at 10 posts [D1].
7. **(Oct 14) Music cohort (M1):** music vs no-music posts by avg % viewed; no reach claim without it. Confounded this week with the posting rate.
8. **(Oct 14) Question hook vs statement hook (Q1):** 3 pairs. Old hits used questions 3/4; new posts 0/20.
9. **(Oct 14) A cut-in pause before the final line (P1):** 3 vs 3.
10. **(Oct 14) Scorebug-as-proof with a circle (S1):** descriptive, n≥6.

### 8. What would change this system
- **If formats 1-3 built to this checklist** stay under a 5K median at 72 h across 6 posts, the problem is distribution, not craft. Test the posting rate first.
- **If high-retention Shorts** (110%+) keep getting under 3K, the feed's first test (frame 1 + topic) is the gap, not the middle of the video.

### 9. Per-batch loop (one pass per batch)
1. **Read:**
   - `channel_check.py`, and log it.
   - vidIQ analytics if 10+ credits (per-video avg % viewed, and retention curves for winners and losers).
   - Compare same-age posts.
2. **Pick:** score candidates with the rubric (section 4). Lock the facts with dated sources.
3. **Footage first:** frame 1 + a proof clip per beat. If you can't, don't script it.
4. **Write:**
   - Choose the format.
   - 2-3 hooks; pick by time-to-question.
   - Script length to fit the format.
5. **Voice:** `voice_take.py`, then `voice_check.py`.
6. **Edit:** anchor the shots, then `assemble.py`.
7. **QA:** `qa_short.py`, the watch sheet, then the Critic v2 agent. Fix, re-check.
8. **Package:** notes.md, UPLOAD.md and PACKAGE.md; the queue status; the Hub upload.
9. **After posting:** log the time; judge at 72 h and read again at 7 days (Oct 26 overnight review). Change a rule only at n≥3 or on a large effect.

---

## OLDER MATERIAL (Round 2, Sep 2026) — background only; where it conflicts with CREATIVE SYSTEM v3 above, v3 wins

> **Oct 26 overnight review:** the posting, title, tag and hashtag rules in this section were rewritten to point at THE RULES at the top. The rest is history: the numbers describe CoachClank and the niche in Sep 2026.

*Built only from the AI NBA story-Shorts niche: CoachClank's full channel (all 432 Shorts; 203 with dates and likes), 7 other channels in the niche, frame-by-frame watches of 12 Shorts, and 180 top comments. Checked Sept 26, 2026.*

---

## First, the honest answer to "is this bs?"

**Round 1's facts were real, but it compared you to the wrong channels** (general NBA-facts channels, not AI NBA story channels), and some of its advice was generic. Four things it told you were wrong for this niche:

| Round 1 said | The niche actually shows |
|---|---|
| Use your own voice | **A fast AI voice is fine.** 0 of 180 top CoachClank comments even mention the voice. |
| Slow down to ~170 words/min | **CoachClank talks at ~260–290 words/min.** Fast is the style. |
| Write keyword descriptions | **CoachClank uses no description and no tags at all.** |
| Your problem is subscriber conversion | **This niche converts low.** CoachClank: 0.13 subs per 1,000 views, yours: 0.21. **Your problem is reach per Short.** |

Everything below is only what the winners actually do.

---

## The benchmark: CoachClank

| | |
|---|---|
| Channel started | **May 31, 2025** (16 months ago) |
| Today | **144K subs · 432 Shorts · ~1.09 billion views** |
| A typical Short | **~500K views** (median) |
| Uploads | ~6 per week, every week |
| Length | median 20s |
| Length vs views | 21–30s → median 765K · 31–45s → median 1.13M · ≤20s → median 321K |
| Titles | 4–7 words, often a question; 1 emoji optional. No hashtags. (Round 3 data: Tools/data/title_patterns.md) |
| Its second-ever upload | "Kobe Bryant's FINAL GAME…" → **5.2M views**. New channels *can* pop fast in this niche. |

Other channels in the same niche, as proof it isn't one lucky guy:

| Channel | Subs | Typical Short | Best Short | Format |
|---|---|---|---|---|
| Ahmed's Basketball | 120K | ~99K | 822K | ~70s list stories ("NBA players who showed up unrecognizable after one summer") |
| Hoop Facts (started Nov 2025) | 51K | ~37K | 2.0M | 20–70s fact stories ("When The Spurs Memed Shaq") |
| Hoops Lore (started Jan 2026) | 16K | ~34K | 9.2M | 60–130s player-told stories |
| Med | 455K | ~772K | 1.5M | 2K "what if" simulations |
| Rebound Rewind | 234K | ~191K | 1.4M | "Every team's ___" lists |

---

## Why you're stuck at ~30K (the real reasons)

### 1. You retold stories that had already gone viral

Same topic, same facts, same length:

| Topic | CoachClank | You |
|---|---|---|
| Why no one shoots underhand | **10,000,000** | 73,000 |
| Dunking without jumping | **2,700,000** | 56,000 |
| The airless basketball | **23,000,000** | 44,000 |

The audience already saw it. Pauly Walnuts makes the same point about his own niche: people just watch the creator who made it first.

**Rule: never retell a story a bigger channel already posted.** Retelling *your own* winners is fine — CoachClank did the underhand story twice (10M, then 2.9M).

### 2. Your first line is a quiz. Theirs is a scene.

> **Round 3 check:** of CoachClank's 8 biggest 2026 Shorts, 6 open on a scene, a claim or a broken rule, 1 on a mystery question ("Why did this player…?") and 1 on "Did you know". A scene is the safe default; a mystery question works too.

| Topic | Your first line | CoachClank's first line |
|---|---|---|
| Underhand free throws | "Ever wonder why underhand free throws disappeared?" | Starts on the scene: fans mocking a player for shooting underhanded, even though he's making them. |
| Dunking without jumping | "Is it possible to dunk without jumping?" | Asks the question, then instantly explains why even the tallest players still have to jump a little. |

Quiz openers ask the viewer to care. Scene openers put them *in* the moment.

### 3. You end on a fact. They end on something to argue about. *(SUPERSEDED Oct 13: our data says end on the payoff that answers line 1; the argument goes in the pinned comment. See Strict Short Formula §3.)*

- CoachClank's underhand Short ends on Shaq saying he'd rather miss every free throw than look silly shooting underhanded.
- The top comment, with **48,000 likes**, just argues back that missing every free throw looks worse.

That argument in the comments is what spreads the Short.

### 4. You stopped

- **You:** 80 Shorts in 3.5 months, then 7 months dark.
- **CoachClank:** ~6 a week for 16 straight months.

---

## The recipe (what every MetaSports Short looks like now)

**Length:** stories 22–40 seconds (about 90–170 words); quick moments 15–25 seconds. CoachClank's 31–45s Shorts have the best median, and his 8 biggest 2026 Shorts ran 22–34s (Research Notes/Round 3 - Deeper Findings.md). **Posting (Oct 28):** 7-8 AM ET, plus a 2nd at about 3 PM when it's as strong; never 3. Full rules: THE RULES §3 at the top and `UPLOAD SCHEDULE.md`. Never two Shorts from the same game on one day; re-run `copy_check.py` the morning of posting; log the go-live time on each Hub card.

**Voice:**
- One AI voice, fast (~250 words/min).
- Always the same voice — that's your brand.

**The 3-part script:**
1. **Open with one of these 4** (the four opener types CoachClank uses — templates, fill in your moment):
   - **A scene:** "Fans were laughing at [player] for…"
   - **A rule:** "In the NBA, there's an unwritten rule that…"
   - **A strong opinion:** "[Player] has to be the most ___ player ever."
   - **The stakes:** "It's [player]'s last game, they're down 10 with two minutes left."
2. **The turn:** "But…" / "However…" / "You see…" → the unexpected part. Add one opinion line of your own, e.g. "But honestly, the funniest part is…"
3. **End on the payoff that answers the opening (one number or the subject's own words).** Then stop. *(Updated Oct 13.)* No "subscribe," no summary.

**Visuals:**
- The actual moment on screen from second one.
- Small, clean captions, 2–3 words at a time.
- Your red circles are fine.

**Title (Oct 26 overnight review):** a short statement pointing at the moment; no hashtag or one (#nba); title wording is a small factor, so don't score titles (THE RULES §3). [V] Similar Channels §1.
- For reference, CoachClank's biggest titles in Sep 2026:
  - "He Didn't Have To Do That 😭" (20M)
  - "This Cost Them The Game 😭" (7M)
  - "James Harden Makes No Sense 😭" (3M)
- Leave the description empty.

**The kinds of moments that hit** (CoachClank's top 30):

| Kind of moment | Example | Views |
|---|---|---|
| Size mismatches | "6'8 vs 7'9" | 30M |
| | "WNBA Player vs High School Kid" | 32M |
| Wholesome/respect moments | "NBA Player Teaches Manners" | 26M |
| Rule weirdness | "This Cost Them The Game" | 7M |
| | "The Unwritten Triple Double Rule" | 6.4M |
| Funny/petty players | "He Didn't Have To Do That" | 20M |
| | "200 IQ LaMelo" | 11M |
| "What happened to…" | "…the 7'7 Basketball Teen?" | 14M |
| Legendary moments with stakes | Kobe's 60-point finale | 5.2M |

---

## The one habit that matters most: fresh moments, daily

The season tips off **Oct 20**. Every game night creates moments nobody has told yet — that's your edge over retelling.

**The daily loop (~45 min):**
1. **Morning (15 min):** scan last night's highlights, NBA Reddit and NBA X/Twitter. Pick **one** moment that's funny, petty, weird, rule-related or wholesome.
2. **Check it's fresh (2 min):** search YouTube Shorts for it. If a big channel already told it, skip it or find a different angle.
3. **Write (10 min):** `/nba-short [the moment]` — it now follows this recipe.
4. **Build + post (20 min).** Same time every day.

**Target: 6–7 Shorts a week, every week.** Before opening night, use the 10 ready scripts in *MetaSports - Scripts (Batch 2)*. They're storylines CoachClank hasn't touched.

---

## Stop doing these

- Retelling CoachClank's (or anyone's) viral stories
- Quiz-question first lines
- Hashtag walls, tag walls and filled descriptions (Oct 26 overnight review: tags 3-8, description empty)
- Fight clips and off-topic AI comedy (your own data: they flopped)
- Going dark. If life gets busy, post fewer, but never zero.

---

## Money & risk (short version)

- **Shorts ad money:** from Feb 1, 2027, Shorts only pay in months when you have **10M+ Shorts views in the last 90 days**. CoachClank clears that easily; you'll need CoachClank-style reach first. Build reach now, money follows.
- **NBA footage:** every channel in this niche uses it, and claims happen. Keep Shorts **under 60 seconds** — claimed Shorts over 1 minute get blocked. Your narration + story is what makes it "yours" under YouTube's rules. Pure clip reposts with music are not.
- **AI:** fake realistic videos of real players are the one AI move to avoid (removal risk + a label required). An AI *voice* is fine.

---

## Your next 14 days (Sep 2026 plan, done; history only)

> **Round 3:** the full plan with checkpoints through Dec 27 is in **Roadmap - Next 90 Days**.

| Day | Do |
|---|---|
| 1 | Pick your one AI voice and set it to fast. Change the display name to "MetaSports." |
| 2–10 | Post the 10 Batch-2 scripts, one a day (dates are on each script). |
| 3 onward | Start the daily fresh-moment loop in the background: collect moments now, use them from opening night on. |
| 7 | First check-in. Which openers and titles got the most views in the first 48 hours? Do more of that. |
| 14 | Opening-night week is next: switch to 100% fresh moments from last night's games. |
