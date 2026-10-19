# The plan, Oct 19, 2026: one proven format, the best voice, retention every day

**Owner, Oct 19:** "#42 did exceptionally well. Automate retention checks. Heavy review of what made it good, make similar videos in the same format, focus on what we KNOW works, stop making new formats. New ElevenLabs Creator plan: re-do the voice research, find the optimal voice, and test it on Shorts without waiting for approval. Think like CoachClank."

**What CoachClank does that we copy** (from 148 of his Shorts, audit Oct 4 and Oct 15):
- **one format, repeated about daily:** a claim about the clip on screen → why → a turn → a human payoff
- **15-30 s**
- **footage only**
- **one voice, never changed**
- **volume:** the format is the product, and each Short is one more pull of the same lever

So:
- **No new formats.**
- **One voice, picked once with evidence, then frozen.**
- **Measure every post the same way, automatically.**

## Hard facts this plan rests on (checked today)
| Fact | Source |
|---|---|
| #42 "Who Has Missed The Most Shots": **25,000 views at about 3.5 days, 84.3% stayed** (channel record), 7 subs at 1.5 days | channel_check Oct 19; Studio export Oct 17 |
| #42's numbers vs our other recent Shorts:<br>- line 1 ends at 3.3 s<br>- the question comes at 15.1 s<br>- 12 shots, median **2.0 s** (others 1.25-1.9 s), first cut at 2.7 s (others 1.2-1.9 s)<br>- 63 written tokens, about 212 spoken wpm: **the slowest read** | words.json / shots.json measured today |
| Same voice (Alex), same week, same LeBron subject:<br>- #46 49.8% stayed / 2.1K<br>- #36 4.3K<br>- #10 1.9K<br>So the **subject and the voice are not what made #42**. The **format** is | Studio export Oct 17, channel_check Oct 19 |
| ElevenLabs Creator:<br>- 121,224 credits/month<br>- 30 voice slots (3 used)<br>- instant cloning<br>- **1 Professional Voice Clone** slot<br>- models include **Eleven v4 and v4 Turbo** (released Sept 28, 2026, never tested by us)<br>- v4: better clone accuracy and audio tags, but **no speed or style slider** (stability and similarity only) | ElevenLabs API `/v1/user/subscription` and `/v1/models` today; docs: elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4 |
| YouTube Analytics API:<br>- gives views, **engagedViews**, average % viewed, average view duration, subscribers and the **full retention curve** (`audienceWatchRatio` by `elapsedVideoTimeRatio`)<br>- does **not** list Shorts "Stayed to watch / swiped away" | developers.google.com/youtube/analytics/metrics |
| engaged ÷ views as a proxy for "stayed":<br>- r = 0.63 (n=20, Oct 14 export), about ±7 points<br>- every Short under 0.50 had under 60% stayed<br>So it **catches flops but can't rank the top** | computed today |

## 1. Retention, automatically, every day
**Goal:** every morning, without the owner, each Short younger than 14 days gets views, engaged ÷ views, average % viewed, average view duration, subscribers and its retention curve, with flags. The exact "stayed %" comes from a weekly 30-second Studio export.

**Steps:**
1. Extend `Tools/yt_analytics.py`:
   - `daily`: per-video metrics for the last 30 days, plus the retention curve for each Short under 14 days old. It writes `Research Notes/Studio exports/api/daily YYYY-MM-DD.csv` and `retention YYYY-MM-DD.csv`.
   - `report`: plain-English flags:
     - engaged ratio under 0.50 = "likely swiped (under 60% stayed)"
     - the curve at 10% of the runtime under 0.70 = "weak start"
     - the curve dips more than 15 points inside 3 s = "lost them on line 2"
2. **Owner, one time (about 10 min, on the PC):**
   - make the Google Cloud OAuth client (steps already in `Tools Guide.md`)
   - run `python Tools/yt_analytics.py auth`
   - then **either** (a) let the PC run `Tools/daily_analytics.bat` from Windows Task Scheduler at 09:00 (it pulls and pushes the CSV to git), **or** (b) put three values in the cloud environment's secrets (`YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`), so the cloud routine pulls directly.
   - **Never paste them in chat.**
3. The existing daily cloud routine reads the newest API CSV (or pulls it itself, with secrets) and writes the Outcome Log, so no owner screenshots are needed.
4. **Exact "stayed":** the owner exports Studio → Content → Shorts → Export (CSV) once a week. The routine reminds on Mondays.

**Done when:**
- the tool runs against a recorded API-shaped fixture with tests passing
- the owner-step doc exists
- the routine prompt is updated

**Can't be done from the cloud alone:** the Google sign-in. Only the owner can approve read access.

## 2. The #42 format: a heavy review, then a written spec
**Steps:**
1. **Measure #42** against #46/#36/#10 (the same voice and subject, low results) and #22/#03/#44 (other winners):
   - pace per sentence
   - the hook's end
   - the question's time
   - the numbers count and order
   - shot lengths
   - frame 1
   - words over footage vs cards
   - effects and music
   - the ending
2. **Write `Library/THE #42 FORMAT.md`:**
   - the skeleton with a time budget per beat
   - what's measured to be true
   - the hard rules (what QA and the critic must enforce)
   - what we **don't** know yet (music, voice)
3. **Wire it in:**
   - Playbook top (replaces "the Winning Formula" as rule 1)
   - Script Critic: a "format fit" gate
   - `script_lint.py`: checks that line 1 is a "[famous name] has [bad-sounding record]" claim and that a "So is he… ? No." turn exists
4. **Retire every other format** in the queue. These stay on file but are **not produced**:
   - #47 Kawhi bounce
   - #50 Embiid dunk
   - news Shorts
   - rule explainers
   
   #49 (already rendered) stays as an optional draft, marked off-format.

## 3. The voice (Creator plan): evidence first, then frozen
**Control:** Alex on multilingual v2, speed 1.2. It is the voice on #42 and #44, our two best new Shorts. A challenger must beat it on measures, not on novelty.

**Steps:**
1. **CoachClank reference:**
   - download 3-5 of his Shorts' audio from TikTok (the route that worked on Oct 5 and Oct 13), with no cookies or login
   - measure his narrator: pace, pitch variety, loudness variety, pauses
   - that's the target profile, not his voice: **we never clone a real person's voice without their consent**
2. **Candidates** (one script = #42's, about 470 characters):
   - Alex × {v2 at 1.2 (control), v4 (stability 0.3 / 0.5) with a light atempo to match pace, v3}
   - pham v2 clone × {v2 at 1.1, v4}
   - a **new instant clone of the old Shorts' narration on v4** (v4 clones "more faithfully"; the source is the channel's own old uploads)
   - 2-3 Voice Library voices closest to the CoachClank profile, on v4 and v2
   - **About 15 takes ≈ 7K credits** (6% of the month)
3. **Measure each take:**
   - words right after a phone-speaker simulation (faster-whisper)
   - pace
   - pitch variety
   - loudness variety
   - HNR/jitter/shimmer
   - number emphasis (dB)
   - consistency across two takes
   - distance to the CoachClank profile
4. **Test on Shorts:** the top 2 voices narrate the next #42-format Short (#48 Harden), both rendered in full. I pick the winner by the measures and set it in `voice_config.json`. The owner can overrule by ear; nothing waits on that.
5. **PVC:**
   - only with clean, consented source audio (the owner's own voice, or a voice actor's with rights)
   - ElevenLabs requires the speaker to verify
   - not possible with the old-narration source; written down as an option

**What I can't do:** hear the takes. The choice uses measures, and I say so.

## 4. Produce #42-format Shorts (the only format)
**Pipeline per Short:**
1. a verified record that sounds bad about a famous star
2. the exact skeleton from section 2
3. footage that shows the bad thing in frame 1
4. the flip number as words over footage
5. the chosen voice
6. QA and the critic
7. a labelled draft

**Order:**
1. **#48 Harden, most missed threes:** script verified (Oct 17); the footage needs finding (X)
2. **LeBron, most turnovers ever:** verify; posting is spaced from LeBron posts
3. 2-3 more from a researched list of "bad-sounding records of famous players". Each must have:
   - a Basketball-Reference source
   - the flip
   - footage of the "bad" act

**Done when:** each draft is rendered, QA'd and critic-passed, with the fact check linked, plus labelled "DRAFT, awaiting approval".

## 5. Records
- Playbook / Production Queue / START HERE / Hub cards / Outcome Log updated
- one commit per finished part
- the handoff lists exactly what's a script, a narrated draft, an edited draft, QA-passed, or waiting on the owner

## Order of execution (fastest to value)
1. section 2.1-2.2: the #42 review and spec (it drives everything else)
2. section 1: the retention tool and owner steps (one hour; the owner can do the sign-in while I work)
3. section 3: the voice tests (the credits are there now)
4. section 4: #48 in the top two voices, then the next #42-format scripts
5. section 5
