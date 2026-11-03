import json, sys, subprocess, os
F=sys.argv[1]
w=json.load(open(os.path.join(F,"_words_narration.json")))
C1=4.015          # after "went at Luka Doncic." (ends 3.99), before "Nine" (4.04)
Q0,Q1=58.60,60.38 # Slater's soundbite (x.com/anthonyVslater/status/2113137207389352120): "I was telling him, he sucks. He can't score on me." (Whisper on the trial cut)
GAP=0.12
live=[("I was telling him,",0.00,0.56),("he sucks.",0.56,0.95),
      ("He can't",1.00,1.30),("score on me.",1.30,1.76)]
D=(Q1-Q0)+GAP*2
out=[x for x in w if x["start"]<C1]
T0=C1+GAP
out+=[{"word":a,"start":round(s+T0,3),"end":round(e+T0,3),"live":True} for a,s,e in live]
out+=[dict(x,start=round(x["start"]+D,3),end=round(x["end"]+D,3)) for x in w if x["start"]>=C1]
json.dump(out,open(os.path.join(F,"words.json"),"w"),indent=0)
subprocess.run(["ffmpeg","-v","error","-y","-i",os.path.join(F,"_voice_narration.mp3"),"-filter_complex",
 f"[0]atrim=0:{C1},asetpts=N/SR/TB[a];anullsrc=r=44100:cl=mono,atrim=0:{D:.3f}[s];[0]atrim={C1},asetpts=N/SR/TB[b];[a][s][b]concat=n=3:v=0:a=1",
 "-ac","1","-ar","44100","-c:a","libmp3lame","-b:a","192k",os.path.join(F,"voice.mp3")],check=True)
sys.path.insert(0,"Tools"); from tighten_voice import srt; srt(out,os.path.join(F,"captions.srt"))
s=open(os.path.join(F,"script.txt")).read().replace("Luka Doncic. ","Luka Doncic. I was telling him, he sucks. He can't score on me. ",1)
open(os.path.join(F,"script_spoken.txt"),"w").write(s)
print("window",T0,"-",round(T0+Q1-Q0,3),"end",out[-1]["end"])
