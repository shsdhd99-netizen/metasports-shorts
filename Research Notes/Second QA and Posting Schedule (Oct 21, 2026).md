# Second QA, duplicate check and posting schedule (Oct 21, 2026, about 15:15-17:00 UTC)

**Owner's ask:**
- "make sure video ideas arent being used multiple times: focus on making good videos over the amount"
- "after you are done with all shorts, run a second qa on all shorts that covers audio, broll/captions, etc. make sure you are SURE it can go viral."
- "then, gauge which 2 to post today (right now, and 5-7pm). that will be my new schedule, edit if needed."

Nothing was posted or scheduled. Every file is still labelled "DRAFT - awaiting approval".

## What the second QA checked (all 8 unposted drafts: #52, #59-#65)
- **QA tool:** `qa_short.py --full`: shot mix, held clips, captions against the script word for word, caption timing and position, export speech-to-text, clipping.
- **Audio:** loudness, loudness range and true peak of each DRAFT file (ffmpeg ebur128).
- **Files:** each DRAFT file is byte-identical to `final.mp4`.
- **Flash frames:** `deflash.py --check`.
- **Pictures:** a frame sheet of every shot (b-roll checked against each spoken name or number).
- **YouTube:** a fresh copy-check of the timely ones on Oct 21.

I can't listen to audio. Every "listen to" note below is for the owner.

| # | Short | QA | Audio (I / peak) | What the frames showed | Verdict |
|---|---|---|---|---|---|
| 64 | Wemby's worst shooting night (THE #42 FORMAT) | **PASS (v2)** | -14.3 LUFS / -1.5 dBFS | v1's frame 1 was a wide shot, Wemby tiny, and "with one basket" ran over a miss. **Rebuilt as v2:** frame 1 is a close-up of his face (ESPN clip), and the payoff now shows his only basket (the alley-oop dunk, ESPN play-by-play 3rd 0.0). | **Post today, now** |
| 62 | Why LeBron isn't a Knick (MSG chant + Rich Paul) | **PASS (v2)** | -14.2 / -1.6 | Clean. v1 said "Tonight", which would be wrong when posted Oct 21. **v2:** "On opening night" and "his Sixers debut was". The UPLOAD sheet listed 3 effects, but the renderer always dropped the camera click (1.05 s after the ding), so the sheet now says 2. | **Post today, 6 PM ET** |
| 63 | All three Williamses got a technical | PASS except the name speech-to-text (88%) | -14.2 / -1.3 | Clean (v2 already rebuilt: the referee's real announcement replaces Wemby's 1-for-13). With the players' names as a hint, the same speech model hears "Kenrich", "De'Aaron" and "Wembanyama" right, so the FIX is a speech-to-text name issue, not the voice. | Oct 22 morning |
| 52 | Vince Carter, most losses (THE #42 FORMAT) | PASS | -14.3 / -1.9 (Designed); -14.2 / -1.7 (Alex) | Archive footage is 720p blown up 2.7x and soft; a black-and-white close-up opens it. | Oct 22, 6 PM |
| 60 | Caitlin Clark 45 and 10 | PASS | -14.3 / -1.5 | Clean; two softer shots. | Oct 23 morning |
| 59 | WNBA minimum beats last year's max | PASS | -14.3 / -1.6 | Some phone video of arena screens (softer). | Oct 23, 6 PM |
| 61 | Paul George's record debut, still lost | PASS | -14.2 / -1.2 | Bottom blur bands; a purple broadcast wipe at the "15 in the 4th" shot. | **Hold**: same story already told by Chris Smoove (31K, "Paul George 38 Pts Celtics Debut! Pistons 23-0 4th QTR Run!") |
| 65 | LeBron answers a Knicks fan | PASS | -14.6 / -1.7 | Clean. | **Hold**: copy-check on Oct 21 is now TAKEN. Chaz NBA has 546K views on the clip with LeBron's real audio; ours narrates the quote. Also the same game as #62. |

All 8 files: no clipping, no flash frames, DRAFT = final.mp4 (the #52 Alex file = `_alex/final.mp4`).

## Duplicate ideas: what was fixed
- **#63 vs #64:** both told Wemby's 1-for-13. Fixed by #63 v2 (the 1-for-13 is now only in #64).
  - The two Shorts also shared one Wemby bench close-up (the Hoop Central post at 24.97 s). #64 v2 now uses an ESPN close-up instead, so they share no footage.
- **#62 vs #65:** same game, same star, and both end on "106-100, ring night". Kept #62 (fresh on YouTube, two real-audio bursts) and held #65 (taken on YouTube).
- **#61:** held; a bigger channel already told it.
- **Checked against posted Shorts:**
  - #10 ("Did The NBA Plan LeBron's First Game?") covered the schedule; #62 is a different story (the chant, why he isn't a Knick). It mentions ring night once as context.
  - No other posted Short covers Vince's losses, Clark's 45-10, the WNBA minimum, the three Williamses or Wemby's 1-for-13.

## Can they go viral? (honest read)
Nothing makes a Short certain to go viral. Here is how each one matches what has worked for us.

What has worked for us:
- A record or oddity about a famous name: Wemby record Short, 79.5% stayed / 26.8K; #22, 29K; #42, 25K.
- Frame 1 is a face or real action.
- It ends on the payoff.

The channel's recent median is 3,600 views (Oct 20 daily check).

- **#64:** the closest match to our winners. A career record for the biggest young star, a paradox (first unanimous DPOY), a flip, frame 1 on his face, 20 s, fresh on YouTube. **Best chance of the batch.**
- **#62:** LeBron is our audience's most-used star (#36 6.1K, #10 3.9K). Two real-audio bursts restart attention. Fresh on YouTube.
  - Risks: 31 s, and no number in the first 8 words (the conflict lands with the chant at 5.3 s).
- **#63:** an oddity plus real referee audio. The fight lane is popular on Shorts. Medium.
- **#52, #60:** evergreen record stories (THE #42 FORMAT / Clark). Medium. #52's archive footage is soft.
- **#59:** pay stories have been our flattest lane. Lowest of the ready ones.

## The new schedule (owner's, Oct 21; my edits in bold)
- **2 Shorts a day:** late morning ET (about 11 AM-12 PM) and 5-7 PM ET. **Aim for 6 PM ET** in the evening window: about an hour before the 7 PM ET tip-offs.
  - Evidence on timing is weak (YouTube says timing matters little, Round 6). Log the exact go-live time on each Hub card so we can compare.
- **Morning slot = the freshest story from last night's games.** Game stories decay within a day, and today's #65 lost its open lane in under 12 hours.
- **Evening slot = the biggest-name story of the day, or an evergreen one** when there is no fresh story.
- **Re-run `copy_check.py` on the morning of posting**, not only when building.
- **Never two Shorts from the same game on the same day.** The second waits until the next day, but only if it's a different idea.

| Slot | When | Short | Why |
|---|---|---|---|
| 1 | **Today, Oct 21, now** | #64 Wemby v2 | Freshest record story, best match to our winners |
| 2 | **Today, Oct 21, 6 PM ET** | #62 LeBron v2 | Biggest name, fresh on YouTube, different game from #64 |
| 3 | Wed Oct 22, late morning | #63 Williamses v2 | Oddity, keeps a day; a day after #64 (same game) |
| 4 | Wed Oct 22, 6 PM | #52 Vince (Designed voice) | THE #42 FORMAT voice test, evergreen |
| 5 | Thu Oct 23, late morning | #60 Clark | Evergreen; give the slot to a fresh game story if one is made |
| 6 | Thu Oct 23, 6 PM | #59 WNBA minimum | Evergreen, weakest lane, goes last |
| hold | | #65, #61 | Taken / already told by a bigger channel |

The Hub shows these as POST #1-#6 with these labels; #65 and #61 are under "On hold".
