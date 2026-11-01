import json, sys, subprocess, os
F=sys.argv[1]
w=json.load(open(os.path.join(F,"_words_narration.json")))
C1=12.04          # after "Even Luka noticed." (ends ~12.0), before "This" (12.06)
Q0,Q1=0.94,3.05   # Oct 30: starts after the "uh" at 0.82-0.92 (Gemini and Whisper both heard it); "definitely a big improvement from last year"
GAP=0.12
live=[("Definitely",0.98,1.60),("a",1.60,1.70),("big",1.70,1.82),("improvement",1.82,2.10),("from",2.10,2.36),("last",2.36,2.52),("year.",2.52,2.96)]
D=(Q1-Q0)+GAP*2
out=[x for x in w if x["start"]<C1]
T0=C1+GAP
out+=[{"word":a,"start":round(s-Q0+T0,3),"end":round(e-Q0+T0,3),"live":True} for a,s,e in live]
out+=[dict(x,start=round(x["start"]+D,3),end=round(x["end"]+D,3)) for x in w if x["start"]>=C1]
json.dump(out,open(os.path.join(F,"words.json"),"w"),indent=0)
subprocess.run(["ffmpeg","-v","error","-y","-i",os.path.join(F,"_voice_narration.mp3"),"-filter_complex",
 f"[0]atrim=0:{C1},asetpts=N/SR/TB[a];anullsrc=r=44100:cl=mono,atrim=0:{D:.3f}[s];[0]atrim={C1},asetpts=N/SR/TB[b];[a][s][b]concat=n=3:v=0:a=1",
 "-ac","1","-ar","44100","-c:a","libmp3lame","-b:a","192k",os.path.join(F,"voice.mp3")],check=True)
sys.path.insert(0,"Tools"); from tighten_voice import srt; srt(out,os.path.join(F,"captions.srt"))
s=open(os.path.join(F,"script.txt")).read().replace("Even Luka noticed. ","Even Luka noticed. Definitely a big improvement from last year. ")
open(os.path.join(F,"script_spoken.txt"),"w").write(s)
print("window",T0,"-",round(T0+Q1-Q0,3),"end",out[-1]["end"])
