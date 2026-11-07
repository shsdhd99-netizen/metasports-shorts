# Talking-head clips in Hedra (owner, about 10 minutes)

Private client material: his photo and voice clone. Do not commit any of these files, and do not upload them anywhere except Hedra.

You will make four clips: the opening and the closing line, each in 16:9 and 9:16.

## 1. Opening clip, 16:9
1. Go to hedra.com, sign in and open **Create > Character-3** (the talking-image model).
2. **Image:** upload `input/photo.jpg`.
3. **Audio:** choose *Upload audio* (not text-to-speech) and pick `work/open.mp3` (3.6 s: "Here's something you do a hundred times a day without noticing.").
4. **Aspect ratio:** 16:9. Use the highest resolution your plan allows (720p or more).
5. **Prompt (optional):** `A friendly teacher talking to camera in his classroom, natural small head movements, warm smile, steady camera.`
6. Generate. Watch it: the lips must match the words and the face must still look like him. If it doesn't, generate again.
7. Download it and save it as `work/open_talk.mp4`.

## 2. Closing clip, 16:9
Same steps, with audio `work/close.mp3` (4.3 s: "So the next time you open a door, remember: you just signed your name."). Save as `work/close_talk.mp4`.

## 3. The 9:16 versions
Repeat steps 1 and 2 with aspect ratio **9:16**. Save as `work/open_talk_9x16.mp4` and `work/close_talk_9x16.mp4`.
(If you skip these, the 9:16 video centre-crops the 16:9 clips. That works, but his face may be cut tighter.)

Do not trim the clips or change their audio. The edit takes the picture only; the sound stays the original narration, which is exactly the same audio Hedra used. Clips that run a little longer than the audio are fine.

## 4. Re-render both versions
From the repo folder:

```bash
bash "Clients/Max Claude/Productions/00 Preview/work/rebuild.sh"
```

It takes about 5 minutes and overwrites `PREVIEW - Fingerprints (16x9).mp4` and `PREVIEW - Fingerprints (9x16).mp4` in this folder. The opening clip plays from 0 to 3.55 s. The closing clip plays from 39.12 s, with a 0.9 s cutaway to the door handle on "open a door" (the clip keeps running underneath, so the lips stay in sync when it comes back).

Check the first and last 5 seconds of both files: the lips must be in sync, and the captions must not sit over his mouth. If they do, tell Claude and it will move them.
