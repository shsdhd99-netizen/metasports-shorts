# Sound Library (canonical; Oct 14, 2026)

> **House rule (owner, Oct 14 night):**
> - **No generic background music.** No instrumental beds, stock tracks or AI-generated music by default.
> - **Clean narration.** Effects only where the picture makes the sound.
> - **Real songs or trending sounds:** only when they strengthen the story, and only through the platform's own music library, added by the owner at upload (route A, §2).
> - **A Short being under one minute does not clear a song's rights.**
> - Section 4's "subtle bed (default)" row is retired.

**What this covers:** every sound we have or have been given, what each may be used for, and how to use trending or copyrighted music.
- **Beds we generated or licensed** (levels, placement, the moves): `Library/Music Guide.md`. Every track has a row in `Library/Music/music_library.csv`.
- **This file** adds the owner's own sounds, the CoachClank reference, the permission rules for copyrighted and trending music, and the sound strategy.

Evidence tiers:
- **[V]** measured or tested on our files
- **[S]** small-n support
- **[E]** external rules or reports (dated)
- **[H]** hypothesis

## 1. What we have, and its status
| Sound | Where it came from | What it is | Licence / permission | Status |
|---|---|---|---|---|
| **"4 Raws", EsDeeKid** | Owner upload, Oct 3, 2026 (`/root/.claude/uploads/…/a5670acf-*.mp3`; a copy is in the scratchpad as `raws.mp3`, not in git) | Commercial UK rap single, 2:27. Billboard Hot 100 top 40 in Dec 2025-Jan 2026 [E] | Commercial recording. No licence held by us | **In-app only** (see section 2, route A). Tested in #01 v6 and dropped for Content ID risk. A late-2025 hit, not a current trend [E] |
| **"Blood Soda Freestyle" (instrumental), yuke / prod. DeemZ** | Owner upload, Oct 3, 2026 (`a18b93ec-*.mp3`; scratchpad `yuke.mp3`) | Commercial instrumental, 1:35 | Commercial recording. No licence | **In-app only**, if the song is in the Shorts picker. Never baked into our render |
| **Vine boom** | `Tools/sfx` | Meme SFX | Unknown (from "Downloads/music") | **Banned:** the owner said it "ruins" the LeBron Short |
| **`Tools/sfx/*`** (whoosh, rim, etc.) | "Downloads/music" | SFX | **Unknown** | Use sparingly; replace with ElevenLabs sound effects or Mixkit's free SFX and log the source |
| **ElevenLabs beds** (`eleven_*_01.mp3`) | Generated Oct 14 on our Starter plan | 4 instrumental beds | ElevenLabs Music Terms: commercial online use, no attribution [E] | **Default.** Unique audio, so low Content ID risk |
| **Mixkit tracks** (3) | mixkit.co | Stock instrumentals | Mixkit Free License: monetized YouTube OK [E] | Candidates; busier in the voice range |

**The CoachClank reference.** The owner pointed to "the CoachClank sound". What we can verify: [V]
- Both CoachClank TikToks we have use **"original sound - CoachClank"**: their own upload, not a reusable platform sound.
- **Inside it:** their narrator (a different voice from ours: 0.74 speaker similarity) plus a tonal music bed only **2.5-5 dB under the voice** in the rare gaps (n=2). Ours sits 16-20 dB under.
- **We could not identify the bed track.** We have no music-recognition service, and an "original sound" can't be traced through TikTok.
- **So the reference could mean either (a) the narration style or (b) the bed.** We don't guess:
  - (a) is handled in the voice work (`Research Notes/Voice Audition (Oct 14, 2026)/README.md`).
  - (b) is handled as a level test: section 5, test edit T2.
  - If the owner meant a specific song, the owner names it and we check it against section 2.

## 2. Copyrighted music: what's permitted, by route (YouTube Shorts; checked Oct 14, 2026)
The owner is open to copyrighted music. A track is not excluded because it's copyrighted. What decides is **how it gets into the Short.**

| Route | What it is | Allowed? | Content ID / money | Who does it |
|---|---|---|---|---|
| **A. YouTube Shorts audio library** (the "Add sound" picker in the YouTube app's Shorts editor) | Commercial songs licensed by YouTube for Shorts | **Yes, for songs in the picker** (varies by song and country). Up to 90 s of a song in a 3-minute Short, depending on the song [E: YouTube Help "Music eligibility for YouTube Shorts"] | YouTube places "a special Content ID claim" that is invisible to the creator and can't be disputed [E: YouTube Help 13053317]. Shorts ad revenue goes to a creator pool that also covers music licensing; the creator share is 45% with or without music [E: YouTube Shorts creators page] | **The owner, at upload, in the app.** Import our video from the gallery, tap Sound/Add sound, choose the song and segment, set the volume balance (the app has separate sliders for the original audio and the added music [E, third-party guides; confirm in the app]) |
| **B. YouTube Audio Library** (Studio) | Royalty-free tracks | Yes | "Won't receive a Content ID claim" [E: YouTube Help]. Some need a credit line | The owner downloads from Studio (we don't open Studio) |
| **C. Licensed by us** (ElevenLabs Music, Mixkit, a paid library) | Tracks we hold a licence for | Yes, within the licence | ElevenLabs: unique audio, low risk. Mixkit: medium (re-registered free tracks happen) | We bake it into the render (`music.json`) |
| **D. Another platform's library** (TikTok sounds) | TikTok's licences cover use on TikTok | **Not for YouTube.** Third-party summaries say TikTok's library licences don't extend off TikTok [E] | Standard claim if re-used on YouTube | Don't download TikTok sounds for our Shorts |
| **E. A commercial song baked into our upload** (e.g. "4 Raws" mixed in by us) | Unlicensed use | Technically possible; **the owner's risk call, per video** | "Eligible for standard copyright claims." A claim can monetize the Short for the rights holder, block it in some countries, or block it everywhere. **A Short over 1 minute with any active claim is blocked** (since Oct 15, 2024) [E: YouTube Help 13053317] | Only with the owner's explicit yes for that video, and only under 60 s |

**Default:** route C (our beds) is baked in. Route A is the way to use a copyrighted or trending song, and only the owner can do it, in the app.
- For a route-A Short we render a **"for the app" version**: voice + footage + captions, with no bed (or the bed lowered), so the added song doesn't fight our bed.
- The owner sets the song's level in the app. Starting point: the song slider at about 20-30% so the narration stays on top. This is a starting guess [H] to adjust by ear.
- **Never upload the same audio to TikTok and assume it's licensed.** On TikTok, add the song in TikTok's own editor (a personal account's general library is for TikTok only [E]).

## 3. Trending sounds (dated evidence; secondary sources)
**Checked Oct 14, 2026.** TikTok's Creative Center song chart needs a login from this server (it redirected to the hashtag page), so these come from third-party trackers:
- **Revid's sample of popular posts** (updated Oct 13, 2026): "Paper Moon Static" (Marnie Cusk), "BLUE WATER CANDY" (DJ Allanzinho JP), "VERITY HARDTEKK - Slowed" (shxnei), "Ramalama (Bang Bang)" (Róisín Murphy, the Halloween costume-walk trend).
- **SocialPilot and NewEngen October 2026 roundups:** Halloween formats, "Patient Zero" (Taylor Swift) montages, "We Fell in Love in October" (girl in red).

**Verdict for MetaSports** [S]:
- None of these fits a narrated NBA story. Both reference creators run their own original sound, and our narration fills the Short.
- A trending song only fits where the picture carries the Short without narration: a 1-2 s cold open, or an end montage. **No queued Short has either.**
- **Don't force a trend.**
- If one fits later:
  - route A only
  - note the date and source of the trend evidence in PACKAGE.md
  - drop it if the trend evidence is over 14 days old by posting day

## 4. Sound strategy (what each sound is for)
| Role | When | How | Evidence |
|---|---|---|---|
| **Narration** | Always: the voice carries the Short from 0.0 s to the end | The house voice (Playbook, Winning Formula) | All references, our hits [V] |
| ~~Subtle bed~~ (retired Oct 14 night) | Not by default | Only on purpose, with a reason in PACKAGE.md | 5/5 old Shorts watched had one, but it doesn't separate hits from misses [S]; the owner dropped it |
| **Silence as a move** | The beat before the turn or the punchline | `drops` in music.json (0.3 s) | Old hits' music moves [S] |
| **Dramatic bed** | Mysteries and reveals | "Dark build", decays on the answer word | #41 [V placement] |
| **Trending song** | Only a non-narrated cold open or montage | Route A by the owner | Section 3 |
| **Meme sound** | Only where the picture is the joke, and never the vine boom | Route A, or a licensed SFX | Owner preference |
| **SFX** | 2-5 per Short, only where the picture makes the sound (rim, whoosh on a circle) | `sfx.json` | Playbook §5 |

## 5. Test edits (done Oct 14 night; renders inspected, numbers measured; I can't hear them)
| Test | What | Result [V] | Where |
|---|---|---|---|
| **T1 timing** | Move every music drop, stop and hit onto the new voice's words (`Tools/retime.py`), then check by isolating the music (music render minus dry render) | **#40:** the drop before "It isn't." lands at 14.81 s (-44.7 → -74.5 dBFS); the bed is out before "Not eighty-one." **#41:** the decay comes in as "zero." ends (-33 → -54 → -71 dBFS over 23.1-23.5 s). **#21:** the break at 21.0-21.2 s, then the re-entry hit at 21.4 s on "Four games to spare." | `Productions/…/_v4/CHANGES.md` |
| **T2 level** | #40 v4 with the bed at -12 LU (closer to CoachClank) vs the house -20 LU | Phone simulation: every word heard at both levels. Speech-band margin 41 → 33 dB. Taste is the owner's call | `…40…/_v4/_test_bed12/`; Sound Check §4 |
| **T3 entry/exit** | Unchanged from the Oct 14 music versions: the bed enters with the voice at 0.0 s and exits by the track's own ending or a 0.5 s fade on the punchline | Verified on the same isolated-music read | Music Guide §5 |

**Not done:**
- **A route-A test (a real song added in the YouTube app):** only the owner can add a library song, in the app.
- **A trending-song edit:** no queued Short has a non-narrated cold open or montage, so a test would only force a trend.

## 6. Timing audio to the story (what the references do, and our rule)
**CoachClank:**
- Their two TikToks we have run a constant tonal bed under nonstop narration, mixed in as "original sound".
- We found no hits timed to jokes or reveals in them (n=2, measured on the mix; we can't separate the bed from the voice).

**Our old hits:**
- They marked the payoff with the music: a swell (Kobe), a riser and a clean cut (Luka), a decay to silence ("...son.").

**Our rule now** (no bed):
- Mark the payoff with **silence or an effect the picture earns**: a swish on the make, a whoosh on a proof card.
- If the owner adds a song in the app, start it after the hook line and let it cut on the payoff line.
