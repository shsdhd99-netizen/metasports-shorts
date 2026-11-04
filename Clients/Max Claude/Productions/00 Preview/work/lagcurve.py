import numpy as np, subprocess, sys
FPS=30
def env(mp3):
    a=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",mp3,"-ac","1","-ar","16000","-f","f32le","-"],capture_output=True).stdout,np.float32)
    n=len(a)//533; return np.abs(a[:n*533]).reshape(n,-1).mean(1)
for nm,au in (("Aorig","A"),("Async","A"),("Borig","B"),("Bsync","B")):
    ap=np.load(f"../qa_tmp/{nm}.npy"); e=env(f"C:/Users/Admin/apps/max_job/full/{au}.mp3"); N=min(len(ap),len(e)); ap=np.nan_to_num(ap[:N],nan=np.nanmedian(ap)); e=e[:N]
    k=np.ones(5)/5; ap=np.convolve(ap,k,'same'); e=np.convolve(e,k,'same')
    out=[]
    for L in range(-15,22):
        x,y=(e[:N-L],ap[L:]) if L>=0 else (e[-L:],ap[:N+L])
        out.append((L/FPS,float(np.corrcoef(x,y)[0,1])))
    best=max(out,key=lambda t:t[1]); print(nm,"best lag %+.2f r=%.2f"%best," r@0=%.2f"%dict(out)[0.0])
