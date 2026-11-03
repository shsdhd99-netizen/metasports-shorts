# Handover: AI videos for Max Claude (for Account 1)

**How to start (from your phone):** open Claude Code on Account 1, start a session on the repo
`shsdhd99-netizen/metasports-shorts` (branch `main-329h3w`), and paste the prompt below. That's it.

---

## The prompt to paste

```
New client (a paid commission): Max Claude. He wants HIGH-QUALITY short videos with HIS OWN cloned voice and HIS OWN face
(an AI presenter of him), for many uses (lessons, promos, social posts). We deliver files only; we never post for him.
His sales site: https://ondemand-studio.netlify.app (source and all state: "Clients/Max Claude/README.md"). Call him "Mr. Claude".

Voice and face:
- Voice: ElevenLabs Professional Voice Clone from his 30-120 min of clean recordings, in an ElevenLabs account in HIS name.
- Face: an AI avatar of him (HeyGen digital twin or similar) from his 2-5 min on-camera recording + consent clip, in his account.
- Until his recordings arrive, make the example with a stock ElevenLabs voice and a placeholder (no fake Max face), and say so.
- His API keys go only in the environment settings or Tools/.env; never in chat or git.
Start by making ONE example for him: a 45-second vertical video of a short forensic science lesson,
"How Fingerprints Catch Criminals", made with our MetaSports Short pipeline.

Setup:
- git pull --no-rebase origin main-329h3w. Run bash Tools/cloud_setup.sh (it says if the ElevenLabs key is set).
- Make a folder Clients/Max Claude/ and keep everything for him there. Never mix his files with MetaSports.
- Read the example script and notes in "HANDOVER - Account 1 Client AI Videos.md" (section "The example").
- Our know-how is in .claude/skills/story-short/SKILL.md and "Research Notes/Full Review for Retention (Nov 2026).md".

Make the example:
1. Voice: Tools/voice_take.py with the script (a clear, calm teacher voice; ask me if you want a different ElevenLabs voice).
2. Pictures: free stock clips and images only (Mixkit, Pexels, Wikimedia Commons, public-domain FBI/NIST photos):
   fingerprints, magnifying glass, lab, fingerprint powder and brush, a computer match screen. Write the source of each in sources.csv.
3. Layout: his avatar talking at the start and end (full frame), B-roll in between with his avatar small in a corner
   or as split screen; when the avatar isn't ready, B-roll only. Edit with our tools (cuts_plan -> fill_len -> cut_list -> assemble), big centred captions, the key word in each caption in colour,
   light music under the voice, a new picture every 2-3 seconds, nothing after the last line.
4. python Tools/qa_short.py --full must pass. Look at the first frame, the middle and the last frame yourself.
5. Export 1080x1920 (and 1920x1080 if asked), captioned and clean versions. Save as "Clients/Max Claude/Productions/01 Fingerprints/DRAFT - Fingerprints Lesson.mp4", plus a short UPLOAD.md
   (title, caption, 5 hashtags).
6. Write "Clients/Max Claude/README.md" in plain words: what we can make for him, how long one takes, what it costs
   (about 3,000 ElevenLabs credits a video), and the 5 questions below for him to answer.
Commit and push to main-329h3w. Send me the video.

Rules: never post or schedule anything; never print or commit keys; only free or licensed pictures; facts must be correct
(sources in notes.md); say the voice is AI if a platform asks.
```

---

## The example (the agent uses this)

**Title:** How Fingerprints Catch Criminals 🔍

**Script (about 45 seconds, ~120 words):**
> Your fingerprints have been the same since before you were born.
> They form in the womb, around the fourth month, and they never change.
> Not even identical twins share them.
> Every print has ridges that split, stop and loop. Experts call these details minutiae.
> When you touch a glass, sweat and oil leave a copy of those ridges behind.
> Investigators dust it with fine powder, and the hidden print appears.
> Then a computer compares it against millions of prints in seconds.
> But the computer only suggests a match. A trained examiner makes the final call.
> So next time you grab a door handle, remember: you just signed your name.

**Facts to check (notes.md):**
- Ridges form before birth, around weeks 10-16, and stay the same for life.
- Identical twins have different fingerprints.
- "Minutiae" = ridge endings, splits (bifurcations) and dots.
- Latent prints come from sweat and oils; powder makes them visible.
- Computer systems (like the FBI's NGI) suggest candidates; a human examiner confirms.

**Pictures, line by line:** a close-up fingertip → baby/ultrasound stock → two twins → a print with circled details →
a hand on a glass → brush and powder revealing a print → a computer match screen → an examiner with a magnifier → a hand on a door handle.

---

## Questions for Max (also on his walkthrough page)
1. What will he use these for first (lessons, ads, social posts)? Which apps?
2. (Decided: his own voice and face.) Has he recorded them yet?
3. His look: logo, colours, font? Should his name or face appear?
4. How many videos a week, and how long each?
5. Does he want only the files, or should they be posted for him?

## Good to know
- One video costs about 3,000 ElevenLabs credits. Ideally Max gets his own ElevenLabs account, so MetaSports' credits aren't used.
- If the session says "key: MISSING", add `ELEVENLABS_API_KEY` in the environment settings (environment menu → Edit). Never paste keys in chat.
- Everything is a draft until you or Max approve it.
