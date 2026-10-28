import json, sys, subprocess, os
F=sys.argv[1]; R=os.path.join(F,"_realaudio")
w=json.load(open(os.path.join(F,"words.json")))
C1=32.91          # between "times." (ends 32.90) and "The Netherlands" (32.92)
SRC0=50.85        # source second shown at C1: wide shot of Umana's run-up; Krul saves at about 52.4
RESUME=36.96      # narration comes back 0.36 s after "it!" (source 54.60), over the roar
delta=RESUME-C1
live=[("It's",50.90,51.54),("Umaña",51.54,51.82),("who",51.82,52.04),("steps",52.04,52.32),("up,",52.32,52.76),("and",52.96,53.28),("Krul",53.28,53.66),("has",53.66,53.92),("saved",53.92,54.24),("it!",54.24,54.60)]
out=[x for x in w if x["start"]<C1]
out+=[{"word":a,"start":round(s-SRC0+C1,3),"end":round(e-SRC0+C1,3),"live":True} for a,s,e in live]
out+=[dict(x,start=round(x["start"]+delta,3),end=round(x["end"]+delta,3)) for x in w if x["start"]>=C1]
json.dump(out,open(os.path.join(R,"words.json"),"w"),indent=0)
subprocess.run(["ffmpeg","-v","error","-y","-i",os.path.join(F,"voice.mp3"),"-filter_complex",
 f"[0]atrim=0:{C1},asetpts=N/SR/TB[a];anullsrc=r=44100:cl=mono,atrim=0:{delta:.3f}[s];[0]atrim={C1},asetpts=N/SR/TB[b];[a][s][b]concat=n=3:v=0:a=1",
 "-ac","1","-ar","44100","-c:a","libmp3lame","-b:a","192k",os.path.join(R,"voice.mp3")],check=True)
s=open(os.path.join(F,"script.txt")).read().replace("both times. The Netherlands","both times. It's Umaña who steps up, and Krul has saved it! The Netherlands")
open(os.path.join(R,"script.txt"),"w").write(s)
plan=json.load(open(os.path.join(F,"cuts_plan.json")))
new=[]
for sh in plan["shots"]:
    if sh["clip"]=="K18":
        sh.update(at=SRC0, x=0.2, anchor="It's Umaña who", lead=round(50.90-SRC0,2),
                  why="Umana's penalty, wide: run-up and Krul's save, with the live call 'It's Umana who steps up, and Krul has saved it!' (FIFA). Real-audio version.")
        new.append(sh)
        new.append(dict(clip="K18B", src=sh["src"], at=54.36, x=0.5, blurfit=True, blurfit_aspect=0.75, kind="action", anchor="The Netherlands won", lead=0.54,
                        why="Krul runs off to celebrate and the Dutch players mob him (FIFA, same clip, the broadcast's next angle)"))
    else: new.append(sh)
plan["shots"]=new
json.dump(plan,open(os.path.join(R,"cuts_plan.json"),"w"),indent=1)
shots=json.load(open(os.path.join(F,"shots.json")))
ns=[]
for sh in shots:
    ns.append(sh)
    if sh["clip"]=="K18.mp4":
        sh.update(anchor="It's Umaña who", lead=round(50.90-SRC0,2))
        ns.append(dict(sh, clip="K18B.mp4", anchor="The Netherlands won", lead=0.54, why="Krul runs off, the Dutch players mob him (FIFA)"))
shots=ns
json.dump(shots,open(os.path.join(R,"shots.json"),"w"),indent=1)
sys.path.insert(0,"Tools"); from tighten_voice import srt; srt(out,os.path.join(R,"captions.srt"))
print("delta",round(delta,3),"end",out[-1]["end"],"burst",C1,"-",round(54.85-SRC0+C1,3))
