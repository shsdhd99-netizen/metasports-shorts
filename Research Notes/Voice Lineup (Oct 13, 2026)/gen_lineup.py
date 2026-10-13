import sys,os,json,base64
sys.path.insert(0,"/home/user/metasports-shorts/Tools")
from voiceover import load_env, call
from voice_fx import tighten_gaps
S="/tmp/claude-0/-home-user-metasports-shorts/bc228739-3662-5759-8934-674d6d03bfcf/scratchpad/lineup/"
F="/home/user/metasports-shorts/Productions/MetaSports/2026-10-04 19 How Tall Is Cooper Flagg Really/"
TEXT=(open(F+"_n1/script.txt").read().strip()+" "+open(F+"_n2/script.txt").read().strip())
open(S+"text.txt","w").write(TEXT)
env=load_env(); key=env["ELEVENLABS_API_KEY"]
jobs=[("clone_C","GDS7e7WiI4GqkoRxZAFG","eleven_multilingual_v2",{"stability":0.65,"similarity_boost":0.7,"use_speaker_boost":True,"speed":1.2},False),
("charlie_v3","IKne3meq5aSn9XLyUdCD","eleven_v3",{"stability":0.5,"similarity_boost":0.75,"use_speaker_boost":True},True),
("liam_v3","TX3LPaxmHKxFdv7VOQHJ","eleven_v3",{"stability":0.5,"similarity_boost":0.75,"use_speaker_boost":True},True),
("adam_v3","pNInz6obpgDQGcFmaJgB","eleven_v3",{"stability":0.5,"similarity_boost":0.75,"use_speaker_boost":True},True)]
for name,vid,model,st,tight in jobs:
    res=call(f"/text-to-speech/{vid}?output_format=mp3_44100_128".replace("?","/with-timestamps?"),key,{"text":TEXT,"model_id":model,"voice_settings":st})
    raw=S+f"raw_{name}.mp3"; open(raw,"wb").write(base64.b64decode(res["audio_base64"]))
    if tight:
        _,rem=tighten_gaps(raw,None,S+f"ship_{name}.mp3"); print(name,"trimmed",round(rem,2),flush=True)
    else:
        os.system(f'cp "{raw}" "{S}ship_{name}.mp3"'); print(name,"native",flush=True)
print("chars per take",len(TEXT))
