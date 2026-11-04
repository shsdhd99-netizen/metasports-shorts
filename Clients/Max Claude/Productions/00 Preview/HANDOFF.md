# HANDOFF: Max Claude's preview video (Nov 3, 2026, evening)

Read this first, then `../../README.md` (the client) and `HEDRA.md` (manual Hedra steps). The general method is the
skill `.claude/skills/client-avatar-video/SKILL.md`.

**Client:** Max Claude ("Mr. Claude"), a teacher. **Product:** a ~43 s private preview lesson, "How Fingerprints Catch
Criminals", in HIS cloned voice with HIS face talking at the start and end, in 16:9 and 9:16.
**Owner:** non-technical, often on the phone. Plain English, short updates. The owner sends files to Max; we never do.

## Privacy rules (non-negotiable)
- His photo, voice memo, voice clone audio and any video showing his face are **private**. He consented to their use
  only for this private preview. **Never commit them, never upload them anywhere except the tool that makes the
  talking clip (Hedra / HeyGen, or a local model), never put them on Netlify, artifacts, Hugging Face Spaces or any
  public page.** Ask the owner before any hosted link, even a private one.
- Everything private is already git-ignored (the repo `.gitignore` starts with `/*`; check new paths with
  `git check-ignore -v <path>` before `git add`). Commit only code and docs: `render.py`, `prep.py`, `hedra.py`,
  `rebuild.sh`, `words.json` (script words and timings only), `*.md`, `sources.csv`.
- Keys only from the environment: `HEDRA_API_KEY`, `ELEVENLABS_API_KEY`, `NETLIFY_AUTH_TOKEN`. Never print or commit
  them. If one is missing, stop and tell the owner which one to add in the environment settings.
- **Open item:** on Nov 3 the owner pasted a Netlify token in chat (it was used from a temp file only, never written to
  the repo). Ask the owner to revoke it in Netlify and add a new one as `NETLIFY_AUTH_TOKEN` in the environment.

## State at handoff
| Step | State |
|---|---|
| 1. His inputs (Netlify form `demo-request`) | Done. 1 submission (Nov 3 14:41 UTC, consent on), 0 spam. `input/photo.jpg` 1200x1600 frontal selfie in his classroom; `input/voice.m4a` 52.7 s. |
| 2. Narration | Done. Voice clone `work/voice_id.txt`, eleven_multilingual_v2, stability 0.55, similarity 0.8, speed 0.9. `work/voice.mp3` 43.47 s; last word ends 43.20 s. `words.json` rebuilt from this take (it was ~2 s slower than the old one). |
| 3. Stock clips | Done. 9 Mixkit clips in `work/src/`. Mixkit now serves 15054, 12962, 47323, 23678, 33712 only at 720p (1080p/4K return 403). |
| 4. Talking clips (Hedra) | **NOT DONE: the blocker.** The Hedra key is a v3 API key and works, but the **API wallet is $0.00**. Web-plan credits do not fund the API. Cost if funded: Character-3 1080p 6.25 cents/s, about $1 for all four clips. |
| 5. Render + QA | Done with the **photo placeholder** at start/end. -14.2 LUFS, 0 black frames, ends 0.25 s after "your name." 16:9 captions moved to y=1000 so they clear his mouth/chin; 9:16 captions (y=1380) sit on his collar, fine. |
| 6. Delivery | Both placeholder versions were sent to the owner on Nov 3. **Final versions with talking clips not delivered yet.** |

Code changes on branch `main-329h3w`: `render.py` cuts are now **anchored to words** (word index + lead), not fixed
seconds, so a new narration take only needs a new `words.json`. New `prep.py` rebuilds every private input;
new `hedra.py` makes the four clips through the Hedra v3 API.

## How to finish (pick the first route that works)

### 0. Rebuild the private inputs (any new session, cloud or PC)
A fresh checkout has none of the private files. With the three keys in the environment:
```bash
cd "Clients/Max Claude/Productions/00 Preview/work"
python3 prep.py            # inputs from Netlify, narration (only if voice.mp3 is missing), open/close.mp3, Mixkit clips
```
A new narration take has new timing; `prep.py` rewrites `words.json` and the cuts follow it automatically. It refuses to
continue if the words differ from `words.json` (that would break the anchors; then fix `script.txt` or the anchors in
`render.py`). After a new take, commit the new `words.json`.

### A. Hedra API (best quality, ~$1, fully automatic)
Owner adds a few dollars to the **Hedra API wallet** (Hedra's API / developer billing page, not the web-app plan). Then:
```bash
python3 hedra.py           # prints the wallet, uploads photo + open.mp3/close.mp3, makes all 4 clips at 1080p
bash rebuild.sh            # both versions, ~5 min
```
API notes (v3, verified Nov 3): base `https://api.hedra.com/v3`, header `X-API-Key`. `POST /files` (multipart `file`)
returns a presigned `url`; `POST /models/hedra-character-3` with `{"input": {prompt, start_image:{source:"url",url},
audio:{source:"url",url}, aspect_ratio:"16:9"|"9:16", resolution:"1080p"}}` returns `job_id`; poll
`GET /jobs/{id}/status` until COMPLETED; download `GET /jobs/{id}` → `outputs[0].url`. `GET /balance` = API wallet.
The old `/web-app/public` API rejects v3 keys. Spec: `https://api.hedra.com/v3/openapi.json`.

### B. Free, on the owner's PC (RTX 3060 12 GB): a local talking-head model
Nothing leaves the PC, so this is also the most private route. Untested here; set it up with the owner when the session
runs on the PC (owner said Oct 19: "you are able to run from my pc now").
1. Get the files onto the PC: pull the branch, put the three keys in the PC environment, run `python prep.py` (Windows:
   `python`, ffmpeg is installed). Or the owner copies `input/photo.jpg`, `work/open.mp3`, `work/close.mp3` over.
2. Install one audio-driven portrait model in its own folder outside the repo (models download from GitHub /
   Hugging Face, several GB):
   - **SadTalker** (github.com/OpenTalker/SadTalker): easiest, runs well on 6-12 GB GPUs, Windows guide in its README.
     `python inference.py --driven_audio open.mp3 --source_image photo.jpg --result_dir out --still --preprocess full --enhancer gfpgan`
     `--still --preprocess full` keeps the whole photo and natural head motion low; output is 512-px face pasted back.
   - **EchoMimic** (github.com/antgroup/echomimic, v1 "accelerated"): more natural lips and expressions, needs ~12 GB,
     slower to set up. Try only if SadTalker looks stiff.
   - **Sonic** (Tencent) / **Hallo2**: better still but heavier (often 16 GB+ or Linux-first); skip on a 3060 unless
     the others fail.
   - Not these: Wav2Lip / MuseTalk / LatentSync need a *video* of him (they only redo the mouth); LivePortrait needs a
     driving video, not audio.
3. Make both clips per format. For 9:16 crop `photo.jpg` to 9:16 first (it is already 3:4, so `crop=900:1600:150:0`),
   for 16:9 the model output is cover-cropped by `render.py`. Upscale to at least 1080 tall if needed
   (`ffmpeg -vf scale=-2:1080:flags=lanczos`). Clips must run the full audio length and start at audio time 0.
4. Save as `work/open_talk.mp4`, `work/close_talk.mp4` (+ `_9x16` versions, optional), then `bash rebuild.sh`
   (on Windows use Git Bash, or `python render.py both`).

### C. Free web credits, done by the owner (phone or PC)
- **Hedra web app** free plan (hedra.com → Create → Character-3): steps in `HEDRA.md`. Uses plan credits, not the API
  wallet. Likely watermark and resolution cap on free; fine for a private preview.
- **HeyGen** free plan, Photo Avatar / Avatar IV: about 1 minute a month, watermarked, 720p (Nov 2 check).
- Others with free credits that take photo + uploaded audio (check current limits first): Dreamina/CapCut
  (OmniHuman), Kling AI Avatar, D-ID trial. Only use services whose terms keep uploads private.
- **Phone delivery gotcha (Nov 3):** the Claude app on the owner's phone only *plays* MP3/MP4 cards and cannot save
  them; a zip did not help either. Ways around: open the session at claude.ai in the phone's **browser**, do it on the
  PC, or (only with the owner's yes) a private download page that is deleted afterwards.
- The owner then sends the clips back in chat; save them under the four names in `work/` and run `rebuild.sh`.

### D. Cloud CPU (free, slow, untested)
The cloud container has 4 CPUs, 15 GB RAM, no GPU. SadTalker can run on CPU (`--cpu`); expect many minutes per 4-second
clip. Only if the network policy allows GitHub/Hugging Face model downloads. Try it if A-C are all blocked.

## QA before sending (look at the frames yourself)
1. `bash rebuild.sh` prints "using open_talk.mp4 ..." for each clip it found.
2. Lips: extract the first 4 s and the last 5 s at full frame rate (`ffmpeg -ss 0 -t 4 -vf fps=10,scale=480:-2,tile=8x5`)
   and check mouth shapes against `words.json` (open vowels on "hundred", "day", "door", "name"). The cutaway on
   "open a door" (~40.18-41.09 s) must come back still in sync.
3. Captions never over his mouth in either format. 16:9 y=1000, 9:16 y=1380 in `render.py` `ass()`; Hedra framing differs
   from the photo crop, so re-check and move them if needed.
4. Loudness ~-14 LUFS (`ffmpeg -i f.mp4 -af ebur128 -f null -`), no black frames (`blackdetect=d=0.05:pix_th=0.08`),
   nothing after the last word, duration ~43.4 s.
5. The face must still look like him (no warped teeth/eyes). Regenerate a clip that doesn't.

## Deliver
`SendUserFile` both `PREVIEW - Fingerprints (16x9).mp4` and `(9x16).mp4`, plus 3 plain lines on how it looks. Say it is
preview quality: the full version uses his 5-minute filmed recording. Then update `../../README.md` and commit code/docs only.

## Files (all under this folder)
- `HEDRA.md` manual Hedra steps; `sources.csv` licences; `HANDOFF.md` this file.
- `work/script.txt`, `work/words.json`, `work/voice_id.txt` (tracked); `work/render.py`, `work/rebuild.sh`,
  `work/prep.py`, `work/hedra.py` (tracked).
- Private, git-ignored: `input/photo.jpg`, `input/voice.m4a`, `work/voice.mp3`, `work/open.mp3`, `work/close.mp3`,
  `work/*_talk*.mp4`, `work/src/`, `PREVIEW - *.mp4`, and phone-delivery leftovers `work/max_audio.zip`,
  `work/open_audio.mp4`, `work/close_audio.mp4` (safe to delete).

## Nov 3, 8 PM ET: DONE on the PC with route B (SadTalker, free, nothing left the PC)
- Install (outside the repo, nothing system-wide): portable Python 3.10.11 from the NuGet package in `C:/Users/Admin/apps/py310`; `C:/Users/Admin/apps/SadTalker` (git clone) with its own `venv`, torch 2.0.1 cu118 (CUDA OK on the RTX 3060), `pip install --no-build-isolation basicsr==1.4.2` BEFORE `-r requirements.txt` (otherwise basicsr fails to build), checkpoints v0.0.2-rc + GFPGAN 1.4 weights. Install script used: in the session scratchpad; the steps above are all it does.
- Inputs staged in `C:/Users/Admin/apps/max_job/` (private, outside the repo): `photo.jpg`, `photo_9x16.jpg` (`crop=900:1600:150:0`), `open.mp3`, `close.mp3`.
- Command per clip (about 2-2.5 min each on the 3060): `venv/Scripts/python.exe inference.py --driven_audio ../max_job/open.mp3 --source_image ../max_job/photo_9x16.jpg --result_dir ../max_job/out_open_9x16 --still --preprocess full --enhancer gfpgan --size 512`. The 16:9 clips use the full `photo.jpg` (render.py cover-crops).
- SadTalker's clips end about 0.03 s before their audio: each was padded with `tpad=stop_mode=clone:stop_duration=0.5` (picture only) so the cut timeline doesn't slip a frame.
- `python render.py both` (render.py now works on Windows: filter paths escaped). QA: both 45.77 s, -14.4 LUFS, 0 black frames; lips checked on the first 3.5 s and last 5 s (mouth opens on "hundred", "signed", "name"; back in sync after the door cutaway); captions clear of his mouth in both formats.
- **Files for the owner (on the PC only, git-ignored):** `Clients/Max Claude/Productions/00 Preview/PREVIEW - Fingerprints (16x9).mp4` and `(9x16).mp4`. Not uploaded anywhere. The owner sends them to Max.
- Quality: SadTalker moves the mouth and a little of the head on a still photo; it's preview quality (no blinking body, 512 px face pasted back). Hedra (route A) would look more natural if the owner funds the API wallet (~$1).
- **Script note for the owner:** this narration still says "ridges that loop, split and stop", "millions of prints in seconds" and "the computer only suggests a match"; `../01 Fingerprints/notes.md` has the corrected, sourced wording. Re-voicing with the corrected script = edit `work/script.txt`, `python prep.py --revoice`, fix anchors in render.py if words changed, re-run SadTalker for open/close if those lines changed (they didn't), `python render.py both`.

## Nov 3, 9 PM ET: owner verdict on the SadTalker version: "not very good, not in sync at all"
- Clip placement was checked (prep.py and render.py cut at the same word anchors), so the poor sync is SadTalker itself (`--still` on one photo barely shapes the mouth).
- LatentSync 1.5 (lip-sync refiner over the SadTalker video) was started and **stopped**: C: fell to 7.9 GB free; LatentSync needs about 8 GB more (torch cu121 + checkpoints), which would push the disk under the 5 GB preflight blocker. Partial install and the 5.8 GB pip cache removed (14 GB free now). SadTalker (8 GB, `C:/Users/Admin/apps/SadTalker`) is still installed; delete it if disk is needed.
- **Next: route A (Hedra API).** Owner task "add $5 to the Hedra API wallet" is on the task list; then `HEDRA_API_KEY` in `Tools/.env` on the PC, `python hedra.py` (Windows: `python`), `python render.py both`, QA as above. The SadTalker clips in `work/*_talk*.mp4` get overwritten.
