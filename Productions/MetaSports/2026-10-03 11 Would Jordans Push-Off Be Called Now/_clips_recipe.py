"""Cuts the v2 B-roll for this Short (run from the repo root). Sources live in src/ (X posts). NBA-video cuts crop the
league's title banner out (top 14%) so no half-cut graphics show."""
import subprocess, os, sys
F = os.path.dirname(os.path.abspath(__file__))
S = "src/"
NBA, TB, HR = S + "2104962344031772863.mp4", S + "2006556195113533776.mp4", S + "1934060028732039621.mp4"
# name, source, W, H, at, len, cx, nba_banner_crop, slow
C = [
 ("S01_hook_dribble",   TB, 1080, 1080, 30.6, 0.98, 0.50, 0, 1),
 ("S02_russell_stumble", TB, 1080, 1080, 31.55, 0.92, 0.45, 0, 1),
 ("S03_jordan_rises",   TB, 1080, 1080, 36.55, 1.0, 0.45, 0, 1),
 ("S04_shot_net",       TB, 1080, 1080, 26.95, 1.6, 0.50, 0, 1),
 ("S05_nba_logo",       NBA, 1920, 1080, 4.3, 1.3, 0.50, 0, 1),
 ("S06_contact_wide",   NBA, 1920, 1080, 88.0, 1.6, 0.47, 1, 1),
 ("S08a_feel",          NBA, 1920, 1080, 67.4, 1.3, 0.50, 1, 1),
 ("S08b_firm",          NBA, 1920, 1080, 139.4, 1.3, 0.40, 1, 1),
 ("S09a_push",          NBA, 1920, 1080, 183.4, 1.5, 0.45, 1, 1),
 ("S09b_push2",         NBA, 1920, 1080, 154.6, 1.6, 0.52, 1, 1),
 ("S10_replay_push",    HR, 720, 720, 34.1, 0.75, 0.50, 0, 1.45),
  ("S13_brown_oubre",    NBA, 1920, 1080, 36.3, 1.8, 0.40, 1, 1),
 ("S14_barrett_mobley", NBA, 1920, 1080, 116.0, 2.0, 0.50, 1, 1),
 ("S15_barrett_wide",   NBA, 1920, 1080, 114.45, 0.95, 0.50, 1, 1),
 ("S16_jordan_shot",    TB, 1080, 1080, 40.9, 1.95, 0.55, 0, 1),
 ("S17_brown_dribble",  NBA, 1920, 1080, 34.0, 0.9, 0.40, 1, 1),
 ("S18_loop",           TB, 1080, 1080, 30.6, 0.4, 0.50, 0, 1),
]
for name, src, W, H, at, ln, cx, ban, slow in C:
    y0 = int(H * 0.14) if ban else 0
    h = H - y0
    w = int(h * 9 / 16) // 2 * 2
    x = int(max(0, min(W - w, cx * W - w / 2)))
    vf = f"crop={w}:{h}:{x}:{y0},scale=1080:1920:flags=lanczos,fps=30" + (f",setpts={slow}*PTS" if slow != 1 else "")
    out = os.path.join(F, "clips2", name + ".mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(at), "-t", str(ln), "-i", src, "-vf", vf, "-an",
                    "-c:v", "libx264", "-crf", "16", "-preset", "fast", "-pix_fmt", "yuv420p", out], check=True)
    print(name)

# S12: the league's title card, full width on a blurred copy (so the text is not cut off)
out = os.path.join(F, "clips2", "S12_nba_title.mp4")
fc = "[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30[bg];[b]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2,fps=30"
subprocess.run(["ffmpeg","-y","-loglevel","error","-ss","7.6","-t","1.2","-i",NBA,"-filter_complex",fc,"-an","-c:v","libx264","-crf","16","-preset","fast","-pix_fmt","yuv420p",out],check=True)
