"""Mouth aperture per frame (MediaPipe FaceMesh, local, run with the LatentSync venv python) + audio-envelope lag.
usage: <latentsync venv python> lip_aperture.py VIDEO AUDIO [out.npy]   (video 30 fps). Positive lag = mouth moves LATER than audio."""
import sys, subprocess, numpy as np, cv2, mediapipe as mp
V, Aud = sys.argv[1], sys.argv[2]; FPS = 30
cap = cv2.VideoCapture(V); fm = mp.solutions.face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)
ap = []
while True:
    ok, f = cap.read()
    if not ok: break
    f = cv2.resize(f, (544, 960)); r = fm.process(cv2.cvtColor(f, cv2.COLOR_BGR2RGB))
    if not r.multi_face_landmarks: ap.append(np.nan); continue
    L = r.multi_face_landmarks[0].landmark; g = lambda i: np.array([L[i].x * 544, L[i].y * 960])
    face = np.linalg.norm(g(10) - g(152))                       # forehead to chin = scale
    ap.append(np.linalg.norm(g(13) - g(14)) / face)             # inner-lip opening
ap = np.array(ap); 
if len(sys.argv) > 3: np.save(sys.argv[3], ap)
ar = subprocess.run(["ffmpeg", "-v", "error", "-i", Aud, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True).stdout
a = np.frombuffer(ar, np.float32); n = len(a) // (16000 // FPS); env = np.abs(a[:n * (16000 // FPS)]).reshape(n, -1).mean(1)
N = min(len(ap), len(env)); ap, env = ap[:N], env[:N]
ap = np.where(np.isnan(ap), np.nanmedian(ap), ap)
k = np.ones(3) / 3; ap_s = np.convolve(ap, k, 'same'); env_s = np.convolve(env, k, 'same')
z = lambda x: (x - x.mean()) / (x.std() + 1e-9)
res = []
for s in range(0, N - 6 * FPS + 1, 2 * FPS):
    e = z(env_s[s:s + 6 * FPS]); sc = []
    for L_ in range(-12, 19):
        a0 = s + L_
        sc.append(-9 if a0 < 0 or a0 + 6 * FPS > N else float(np.mean(e * z(ap_s[a0:a0 + 6 * FPS]))))
    i = int(np.argmax(sc)); res.append(((i - 12) / FPS, sc[i])); print(f"win {s/FPS:5.1f}s lag {(i-12)/FPS:+.2f}s r={sc[i]:.2f}")
g = [r[0] for r in res if r[1] > 0.3]
print("MEDIAN lag (r>0.3): %s  n=%d/%d  frames_with_face=%.0f%%" % (f"{np.median(g):+.3f}s" if g else "n/a", len(g), len(res), 100 * (1 - np.isnan(np.array(ap)).mean())))
