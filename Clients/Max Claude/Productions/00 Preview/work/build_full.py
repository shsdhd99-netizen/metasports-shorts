"""Full-script 9x16 preview: Max (Dreamina avatar, 2 clips) reads the whole script; short B-roll cutaways.
Clip A = voice 0..24.45 s, clip B = voice 24.55..end. Times below are on the voice.mp3 timeline. Output: PREVIEW - Fingerprints (9x16, full).mp4"""
import os, shutil, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render as R
W, END, FPS = R.W, R.END, R.FPS
# SYNC=1 uses the LatentSync clips (fallback: unsynced Dreamina clips). SHIFT = seconds the avatar video is moved earlier.
SYNC = os.environ.get("SYNC", "1") == "1"
# SyncNet (LatentSync eval, 25 fps frames) measured the synced clips at +2 (A) and +1 (B) frames = lips late; shifting the video
# EARLIER by 0.08 s (A) / 0.04 s (B) brought both to offset 0. Unsynced Dreamina clips measured -3 / -3 (lips early 0.12 s).
SHIFT_A = float(os.environ.get("SHIFT_A", "0.08" if SYNC else "0")); SHIFT_B = float(os.environ.get("SHIFT_B", "0.04" if SYNC else "0"))
A = os.path.join(W, "dreamina/A_sync_9x16.mp4" if SYNC else "dreamina/A_open_first_half_9x16.mp4")
B = os.path.join(W, "dreamina/B_sync_9x16.mp4" if SYNC else "dreamina/B_rest_of_script_9x16.mp4")
B_OFF = 24.55
# (t0, t1, kind, src, src_offset, fx)   kind: "A" avatar clip A, "B" avatar clip B, "R" b-roll
P = [
 (0.00, 11.25, "A", None, 0, 0.5),
 (11.25, 13.45, "R", "mk_12962", 2.0, "fit"),
 (13.45, 22.70, "A", None, 0, 0.5),
 (22.70, 25.10, "R", "mk_13807", 0.0, 0.3),
 (25.10, 26.50, "B", None, 0, 0.5),
 (26.50, 29.90, "R", "mk_32791", 7.0, 0.15),
 (29.90, 32.50, "R", "mk_23678", 0.0, 0.6),
 (32.50, 35.30, "B", None, 0, 0.5),
 (35.30, 39.90, "R", "mk_4773", 3.0, 0.4),
 (39.90, 41.00, "B", None, 0, 0.5),
 (41.00, 41.95, "R", "mk_33712", 0.0, 0.4),
 (41.95, END, "B", None, 0, 0.5),
]
OW, OH = 1080, 1920
def seg(i, tmp):
    t0, t1, kind, src, off, fx = P[i]; d = t1 - t0; out = os.path.join(tmp, f"s{i:02d}.mp4")
    if kind in ("A", "B"):
        ss = (t0 + SHIFT_A) if kind == "A" else (t0 - B_OFF + SHIFT_B)
        inp = ["-ss", f"{ss:.3f}", "-t", f"{d + 0.1:.3f}", "-i", A if kind == "A" else B]
        vf = f"fps={FPS},scale=-2:{OH},crop={OW}:{OH}"
    else:
        inp = ["-ss", f"{off:.3f}", "-t", f"{d + 0.1:.3f}", "-i", os.path.join(W, "src", src + ".mp4")]
        if fx == "fit":
            vf = (f"fps={FPS},split[a][b];[a]scale={OW}:{OH}:force_original_aspect_ratio=increase,crop={OW}:{OH},gblur=sigma=40,eq=brightness=-0.08[bg];"
                  f"[b]scale={OW}:-2[fg];[bg][fg]overlay=0:(H-h)/2")
        else:
            vf = f"fps={FPS},scale=-2:{OH},crop={OW}:{OH}:(iw-{OW})*{fx}:0"
    vf += f",setsar=1,format=yuv420p,trim=end_frame={round(d*FPS)}"
    R.run(["ffmpeg", "-v", "error", "-y", *inp, "-vf", vf, "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "16", out])
    return out
tmp = tempfile.mkdtemp(prefix="full_", dir=W)
segs = [seg(i, tmp) for i in range(len(P))]
lst = os.path.join(tmp, "list.txt"); open(lst, "w").write("".join(f"file '{s}'\n" for s in segs))
sub = os.path.join(tmp, "cap.ass"); R.ass("9x16", sub)
out = os.environ.get("OUT") or os.path.join(R.ROOT, "PREVIEW - Fingerprints (9x16, full avatar, synced).mp4" if SYNC else ("PREVIEW - Fingerprints (9x16, full avatar, synced).mp4" if SYNC else "PREVIEW - Fingerprints (9x16, full avatar).mp4"))
af = (f"[1:a]loudnorm=I=-14.5:TP=-2:LRA=11,aresample=48000,apad[v];"
      f"[2:a]aresample=48000,atrim=0:{END},volume=-21dB,afade=t=in:d=1,afade=t=out:st={END-1.2}:d=1.2[m];"
      f"[v][m]amix=inputs=2:duration=shortest:normalize=0,volume=4.2dB,alimiter=limit=0.74:level=false,atrim=0:{END}[a]")
R.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", os.path.join(W, "voice.mp3"), "-i", R.MUSIC,
       "-filter_complex", f"[0:v]subtitles='{R.fpath(sub)}':fontsdir='{R.fpath(R.FONT_DIR)}'[vv];{af}",
       "-map", "[vv]", "-map", "[a]", "-t", f"{END}", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
       "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])
shutil.rmtree(tmp, ignore_errors=True); print("wrote", out)
