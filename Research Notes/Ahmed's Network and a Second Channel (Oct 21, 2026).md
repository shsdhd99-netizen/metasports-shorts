# Ahmed's network, and how we'd run a second channel (Oct 21, 2026)

**Owner's ask:** "do you think you could replicate your entire skillset in order to automate another channel? separate info bases, but different niches. research 'ahmeds basketball' and all his channels, very similar to that."

**How the numbers were pulled:**
- Public data only (no login, no cookies), read Oct 21, 2026, about 16:00-16:40 UTC.
- yt-dlp channel listings (the last 400 Shorts per channel) and the channels' About panels.
- The channels' RSS upload feeds (the last 15 uploads, with exact times).
- Per-video metadata for 8 Shorts per channel (mweb client).
- Cover frames.

## The channels
| Channel | Sport | Subs | Total views | Videos | Joined | Median, last 400 Shorts | Top Short |
|---|---|---|---|---|---|---|---|
| **Ahmed's Basketball** (@AhmedsBasketball) | NBA | 121K | 377.5M | 1,175 | Dec 10, 2024 | **131,500** | 4.5M "NBA players who got to play alongside their CHILDHOOD HERO" |
| **Ahmed's Goal** (@AhmedsGoal) | Soccer | 424K | 752.9M | 1,373 | Feb 25, 2013 (older account; US) | **267,500** | 6.7M "What happens to the World Cup trophy from the previous winners" |
| Ahmed's NFL (@ahmedsnfl) | NFL | 1.07K | 1.07M | 67 | Dec 21, 2025 (US) | 6,100 (n=67) | 190K "Top 10 best throws in NFL history" |

For comparison, our channel's median over the last 7 Shorts was 3,600 (Oct 20 daily check).

## Is it one operator?
**Basketball and Goal: very likely the same operator.** This is inferred, not proven: neither About page links the other.
- **Same concept, retitled for each sport.**
  - 57 of Basketball's last 400 titles have a near-identical twin on Goal. Examples:
    - "NBA players who had everything but lost it all" / "World Cup players who had everything but lost it all"
    - "Iconic jersey numbers that ALMOST weren't WORN" (May 8) / "Iconic shirt numbers that were almost never worn" (May 9)
    - "Things that may never happen again in NBA history" / "... in football history"
  - Several twins went up a day apart.
- **Same packaging:**
  - list-story titles that start "Players who ...";
  - 62-88 s runtime;
  - no description, no tags;
  - the same small white sentence-case captions, centred near mid-height.
- Goal brands some Shorts with an "@AHMEDSGOAL" room backdrop.

**Ahmed's NFL: probably not part of it.** It has a different description ("I rank and edit viral videos"), a different format (Top 10/Top 5 ranking edits with hashtags in the title, up to 168 s), a different watermark and a fixed 12:00 UTC daily slot. The name may be a copy.

## What the network does (the playbook to copy)
1. **One format across sports:**
   - A list story about players with an emotional or surprising angle: rejected, refused, betrayed, regular jobs, childhood hero, fathers and sons, "sound fake but 100% real".
   - Not news, so every Short stays evergreen.
2. **One concept list, used on each channel.** An idea that works on one sport is retitled for the other, often within a day. That doubles the output of the research.
3. **Long Shorts:** 60-90 s (YouTube allows up to 3 minutes). Our Shorts are 20-30 s.
4. **Reposts:**
   - 11 (Basketball) and 12 (Goal) exact duplicate titles appear in the last 400 Shorts on each channel. Goal has three at 3x.
   - Example: "NBA players who started the craziest retirement gigs" sits twice in the last week (52K and 5.9K).
   - Flops, or proven ideas, get posted again.
5. **Volume, then a slowdown:**
   - Basketball averaged about 1.7 a day over its life, but only 15 uploads in the last 23 days.
   - Goal posted 15 uploads in 14 days.
   - Basketball's uploads cluster at the same minutes (02:08-02:11, 16:08-16:13, 21:07-21:11 UTC), so they look batch-scheduled.
6. **Footage:**
   - Mostly real photos and short game clips, with AI-style images mixed in (Round 5).
   - A list story needs one picture per player, not a long game clip, so it depends less on match footage. That matters most for soccer, where leagues claim footage hard.
7. **Results:**
   - Big hits came in spring and summer 2026: Basketball's top 3 came Mar-May; Goal's World Cup hits came in July.
   - The newest Shorts (1-2 days old) sit at 3K-28K, so newer posts start slower.

## Could we run another channel this way? Yes. Here is what carries over and what changes
**Carries over unchanged (sport-agnostic):**
- voice pipeline (ElevenLabs take + check);
- splice of real quotes;
- assemble with captions and effects;
- QA gate (`qa_short.py`, deflash, export check);
- copy-check;
- the Hub app pattern;
- daily stats routine;
- the critic/scorecard process;
- the research and fact-check discipline (claim -> exact source).

**Swaps per sport:**
- Footage tools: `nba_videos.py` is NBA-only. The ESPN game-summary API also serves soccer and NFL; official club, league and player posts on X work for any sport.
- Stats sources: Basketball-Reference becomes FBref/Transfermarkt or Pro-Football-Reference.
- The competitor set and title patterns.
- A voice of its own.
- The idea bank.

**Kept separate (the "separate info bases"):**
- Its own repo, or at least its own top-level folder, with its own CLOUD STATE, Playbook, Lessons Learned, Outcome Log and idea bank. Channel B's agent never reads channel A's notes.
- Its own Hub artifact and its own daily stats routine.

**Limits:**
- I still never post. You approve and upload on each channel.
- Voice budget (estimate):
  - A 60-90 s list story is about 250-350 words, roughly 1,500-2,100 ElevenLabs characters per take.
  - At 2 a day that is roughly 100K+ characters a month for the new channel alone, before retakes.
  - The Starter plan noted in our skill is 90K a month for everything, so a second channel needs a bigger plan.
- This cloud session can only reach the `metasports-shorts` repo. A separate repo has to be created by you and added to the environment.

## Which niche (recommendation)
1. **Soccer first.**
   - Evidence: the exact same format earns about twice the basketball median on Goal (267K vs 131K, last 400 Shorts).
   - Audience: global.
   - Timing: the 2026 World Cup just gave a fresh bank of stories.
   - Risk: league footage gets claimed fast. Use stills and official club or player posts, as Ahmed's list format does.
2. **NFL second.** The season is on, and it's a US audience. The only "Ahmed's" NFL channel is a small ranking-edit account (median 6.1K), so the list-story lane looks open there. This is a hypothesis: copy-check it before committing.

## Worth testing on MetaSports itself (HYPOTHESIS)
Ahmed's 60-90 s evergreen list stories ("NBA players who ...") reach a 131K median against our 3.6K. The gap also reflects channel size (121K vs about 550 subs) and volume, so it is not a clean comparison. A two-Short A/B (one list story vs one THE #42 FORMAT Short, same slot) would tell us if the format travels.
