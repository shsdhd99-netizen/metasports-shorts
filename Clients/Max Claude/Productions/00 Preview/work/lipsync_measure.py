"""Lag between audio envelope and mouth-region motion. usage: lipsync_measure.py VIDEO AUDIO [mouth_cx mouth_cy]
Positive lag = video mouth moves LATER than audio. numpy only (+ ffmpeg)."""
import subprocess, sys, numpy as np
V, Aud = sys.argv[1], sys.argv[2]; FPS = 30
cx, cy = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (484, 1188)  # mouth centre on 1088x1920 (A clip default; B clip: 514 1088)
w, h = 360, 200; x0, y0 = cx - w // 2, cy - h // 2
raw = subprocess.run(["ffmpeg","-v","error","-i",V,"-vf",f"fps={FPS},crop={w}:{h}:{x0}:{y0},format=gray","-f","rawvideo","-"],capture_output=True).stdout
fr = np.frombuffer(raw,np.uint8).reshape(-1,h,w).astype(np.float32)
mot = np.abs(np.diff(fr,axis=0)).mean((1,2)); mot = np.r_[mot[0],mot]
sd = fr.std((1,2))
ar = subprocess.run(["ffmpeg","-v","error","-i",Aud,"-ac","1","-ar","16000","-f","f32le","-"],capture_output=True).stdout
a = np.frombuffer(ar,np.float32); n = len(a)//(16000//FPS)
env = np.abs(a[:n*(16000//FPS)]).reshape(n,-1).mean(1)
N = min(len(mot),len(env)); mot, env, sd = mot[:N], env[:N], sd[:N]
def sm(x,k=3): return np.convolve(x,np.ones(k)/k,'same')
mot,env,sd=sm(mot),sm(env),sm(sd)
def z(x): return (x-x.mean())/(x.std()+1e-9)
lags = list(range(-12,19))  # -0.4..+0.6 s
res=[]
for s in range(0, N-6*FPS+1, 2*FPS):  # 6 s windows, 3 s hop
    e = z(env[s:s+6*FPS]); best=None
    for name,sig in (("mot",mot),("sd",sd)):
        sc=[]
        for L in lags:
            a0=s+L
            if a0<0 or a0+6*FPS>N: sc.append(-9); continue
            sc.append(float(np.mean(e*z(sig[a0:a0+6*FPS]))))
        i=int(np.argmax(sc)); 
        if best is None or sc[i]>best[1]: best=(lags[i]/FPS,sc[i],name)
    res.append(best); print(f"win {s/FPS:5.1f}s  lag {best[0]:+.2f}s  r={best[1]:.2f} ({best[2]})")
good=[r[0] for r in res if r[1]>0.25]
print("median lag (r>0.25): %s  n=%d/%d"%(f"{np.median(good):+.3f}s" if good else "n/a",len(good),len(res)))
