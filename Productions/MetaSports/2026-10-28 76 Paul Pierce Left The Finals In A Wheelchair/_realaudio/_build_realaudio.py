import json, sys, subprocess, os
F=sys.argv[1]; R=os.path.join(F,"_realaudio")
w=json.load(open(os.path.join(F,"words.json")))
N1=(0.0, 14.966)    # ends between "confession." (14.954) and the narrator's "I" (14.977)
N2=(16.13, 17.88)   # "This year, on a podcast, he took it back." (ends before "Who" 17.891)
GAP=0.12
Q1=("B",15.88,17.50,[("I",15.96,16.30),("just",16.30,16.46),("had",16.46,16.64),("to",16.64,16.74),("go",16.74,16.86),("to",16.86,17.04),("a",17.04,17.14),("bathroom.",17.14,17.42)])
Q2=("C",1.75,3.18,[("Who",1.82,2.32),("asked",2.32,2.58),("for",2.58,2.78),("the",2.78,2.88),("wheelchair?",2.88,3.08)])
Q3=("C",31.45,35.75,[("Like,",31.46,31.52),("why",31.52,32.42),("would",32.42,32.68),("I",32.68,32.88),("take",32.88,33.94),("a",33.94,34.14),("wheelchair",34.14,34.62),("to",34.62,34.82),("go",34.82,34.94),("use",34.94,35.14),("the",35.14,35.26),("bathroom?",35.26,35.62)])
plan=[("vo",N1),("q",Q1),("vo",N2),("q",Q2),("q",Q3)]
t=0.0; out=[]; segs=[]; windows=[]
for kind,p in plan:
    if kind=="vo":
        a,b=p
        out += [dict(x, start=round(x["start"]-a+t,3), end=round(min(x["end"],b)-a+t,3)) for x in w if x["start"]>=a-0.001 and x["start"]<b]
        segs.append(("vo",a,b)); t += b-a
    else:
        k,f0,f1,ws=p
        out += [{"word":x,"start":round(s-f0+t,3),"end":round(e-f0+t,3),"live":True} for x,s,e in ws]
        segs.append(("sil",f1-f0)); windows.append((round(t,3),round(t+f1-f0,3),k,f0)); t += f1-f0
    segs.append(("sil",GAP)); t+=GAP
segs[-1]=("sil",0.3); t+=0.3-GAP
json.dump(out, open(os.path.join(R,"words.json"),"w"), indent=0)
fc=[]; ins=[]; n=0
for s_ in segs:
    if s_[0]=="vo": fc.append(f"[0]atrim={s_[1]:.3f}:{s_[2]:.3f},asetpts=N/SR/TB[s{n}]")
    else: fc.append(f"anullsrc=r=44100:cl=mono,atrim=0:{s_[1]:.3f}[s{n}]")
    ins.append(f"[s{n}]"); n+=1
fc.append("".join(ins)+f"concat=n={n}:v=0:a=1[o]")
subprocess.run(["ffmpeg","-v","error","-y","-i",os.path.join(F,"voice.mp3"),"-filter_complex",";".join(fc),"-map","[o]","-ac","1","-ar","44100","-c:a","libmp3lame","-b:a","192k",os.path.join(R,"voice.mp3")],check=True)
open(os.path.join(R,"script.txt"),"w").write(" ".join(x["word"] for x in out)+"\n")
plan_c=json.load(open(os.path.join(F,"cuts_plan.json")))
q_at={"P10":(15.93,"I just had"),"P12":(1.79,"Who asked for"),"P13":(31.43,"Like why would")}  # at = first word's source time - lead
for s in plan_c["shots"]:
    if s["clip"] in q_at:
        s["at"],s["anchor"]=q_at[s["clip"]]; s["lead"]=0.03; s["why"]+=" Real-audio version: Pierce's own voice, lip-synced."
json.dump(plan_c, open(os.path.join(R,"cuts_plan.json"),"w"), indent=1)
sh=json.load(open(os.path.join(F,"shots.json")))
for s in sh:
    c=s["clip"].replace(".mp4","")
    if c in q_at: s["anchor"]=q_at[c][1]; s["lead"]=0.03
json.dump(sh, open(os.path.join(R,"shots.json"),"w"), indent=1)
json.dump(windows, open(os.path.join(R,"_windows.json"),"w"))
sys.path.insert(0,"Tools"); from tighten_voice import srt; srt(out, os.path.join(R,"captions.srt"))
print("windows", windows, "total", round(t,2)); print(open(os.path.join(R,"script.txt")).read())
