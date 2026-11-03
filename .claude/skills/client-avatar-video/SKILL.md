---
name: client-avatar-video
description: >
  Make a client's private AI video with THEIR cloned voice and THEIR face talking (talking-head avatar clips at the
  start/end, stock B-roll and captions in between), in 16:9 and 9:16. Covers fetching the client's photo and voice from
  the On Demand site's Netlify form, the ElevenLabs voice-clone narration with word timestamps, talking-head clips
  (Hedra API, free local models on the PC GPU, free web tiers), rendering, QA and delivery, with the privacy rules.
  Use when the user asks for a client preview, a talking-head/avatar video, Hedra/HeyGen clips, or to continue
  Max Claude's video. Argument: a client production folder (optional).
---

# /client-avatar-video

First read the client's `README.md` and the production folder's `HANDOFF.md` if there is one. The worked example is
`Clients/Max Claude/Productions/00 Preview/` (its scripts `work/prep.py`, `work/hedra.py`, `work/render.py` are the
templates for a new client: copy the folder layout, change the script, shot list and anchors).

## Privacy (a client's face and voice are biometric data)
- Use them only for what the client consented to (the site form's consent box). Never commit them: check every new path
  with `git check-ignore -v`. Never upload them anywhere except the talking-head tool itself (or a local model). No
  Netlify, artifacts, public Spaces, pastebins. A hosted download link, even a private one, needs the owner's yes and is
  deleted after use. Delete the client's files when asked (the consent text promises it).
- Keys only from the environment (`NETLIFY_AUTH_TOKEN`, `ELEVENLABS_API_KEY`, `HEDRA_API_KEY`). Never print them. If
  one is missing: stop and name it for the owner to add in the environment settings. If the owner pastes a key in chat,
  keep it in the scratchpad only (never the repo) and remind them to rotate it.

## Steps
1. **Inputs.** Netlify API: `GET /api/v1/sites/<site>/forms` → the form id; `GET /api/v1/forms/<id>/submissions?state=verified`
   and `?state=spam`; take the newest, check `consent`, download `data.photo.url` / `data.voice.url` with the same
   Bearer header into `input/` (git-ignored). On Demand site id: `795688f4-76fa-4c8f-b0fd-2a405dbb7415`, form `demo-request`.
2. **Voice clone.** Instant clone from the memo if none exists (denoise and level a quiet phone memo first). Narrate with
   `POST /v1/text-to-speech/<voice_id>/with-timestamps` (eleven_multilingual_v2; Max: stability 0.55, similarity 0.8,
   speed 0.9) → `audio_base64` + character alignment → `words.json` (`[{w,s,e}]`). Every take has different timing
   (Max's re-take was 2 s slower), so **anchor every cut to a word** (word index + lead in seconds), never to fixed
   seconds. Cut the first and last sentence (`open.mp3`, `close.mp3`) at the same anchors the render uses.
3. **B-roll.** Mixkit direct URLs: `https://assets.mixkit.co/videos/<id>/<id>-1080.mp4`, else `-720.mp4` (some ids are
   720p only). Log each in `sources.csv` with its licence.
4. **Talking-head clips** (photo + `open.mp3` / `close.mp3`, 16:9 and 9:16). Try in this order:
   - **Hedra API v3** (`hedra.py`): base `https://api.hedra.com/v3`, header `X-API-Key`; `POST /files` → url;
     `POST /models/hedra-character-3` `{"input":{prompt,start_image:{source:"url",url},audio:{source:"url",url},aspect_ratio,resolution:"1080p"}}`
     → `job_id`; poll `/jobs/<id>/status`; download `/jobs/<id>` `outputs[0].url`. ~6.25 cents/s at 1080p.
     **Check `GET /balance` first: the API wallet is separate from web-plan credits** (Nov 3: key valid, wallet $0).
     The old `/web-app/public` API rejects v3 keys.
   - **Free, local on the owner's PC** (RTX 3060 12 GB): SadTalker (`--still --preprocess full --enhancer gfpgan`) first,
     EchoMimic v1 if it looks stiff. Wav2Lip/MuseTalk/LatentSync need a video of the person, LivePortrait needs a
     driving video, so they don't fit a single photo. Nothing leaves the PC.
   - **Free web tiers, done by the owner:** Hedra web app (Create → Character-3, upload audio, not TTS), HeyGen free
     Photo Avatar/Avatar IV (~1 min/month, watermark, 720p). Write the owner a numbered click-by-click guide
     (`HEDRA.md` is the model) with exact file names to save back.
   - **Cloud CPU** (no GPU): SadTalker `--cpu` is possible but slow; last resort.
   Clips must start at audio time 0 and run the full audio; the render takes the picture only, the narration is the sound.
5. **Render** (`render.py both`): talking clip full frame at start, B-roll in between, talking clip at the end with a
   short cutaway (the clip keeps running underneath so the lips stay in sync), word-group captions with key words
   highlighted, voice to about -14 LUFS, music bed ~-21 dB, 0.25 s tail after the last word. Placeholder: the still
   photo with a slow push-in until clips exist.
6. **QA, looking at frame sheets yourself:** lips in sync at the start, end and after the cutaway; captions never over
   the mouth (16:9 needed y=1000 of 1080 for a close selfie crop, 9:16 y=1380 of 1920 was fine; re-check with real
   talking clips); -14 LUFS ±1; no black frames; nothing after the last line; face still looks like the person.
   Never interrupt or run two renders into the same output at once: a stopped render leaves a broken MP4 (check with
   `ffprobe`; "moov atom not found" means re-render).
7. **Deliver** with `SendUserFile` (both formats + 3 plain lines). Phone gotcha: the Claude phone app only plays
   MP3/MP4 cards and can't save them (a zip didn't help either). If the owner needs files on the phone: the claude.ai
   session in the phone browser, the PC, or a private download page only with their yes.
8. **Wrap up:** update the client README and `HANDOFF.md`; commit code/docs only; never commit the client's media.
