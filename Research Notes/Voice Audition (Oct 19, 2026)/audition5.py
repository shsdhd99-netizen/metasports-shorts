"""Voice audition round 5 (Oct 19, 2026): the Creator plan + Eleven v4, on the script of our record Short (#42).
Owner, Oct 19: "spend time working on the most optimal voice, test using shorts instead of waiting for my approval."

Same spoken text for every take: #42 _v3/script.txt through voiceover's parser (numbers spoken in full).
Measures (same code as rounds 1-4, `../Voice Audition (Oct 14, 2026)/audition.py`): pace, words heard right through a phone-speaker
simulation (faster-whisper), pitch and loudness variety, HNR/jitter/shimmer, pauses. Added: speaker similarity (resemblyzer) to
CoachClank's narration (one TikTok sample, music underneath) and to the #42 narration as posted (Alex v2).
I cannot hear audio. These are measurements; the pre-registered rules in README.md pick the winner.
Run: . key.sh && python3 audition5.py
"""
import json, os, subprocess, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OLD = os.path.join(ROOT, "Research Notes", "Voice Audition (Oct 14, 2026)", "audition.py")
src = open(OLD).read()
ns = {"__file__": os.path.join(HERE, "audition.py")}          # HERE inside the helpers -> this folder (takes/ go here)
exec(src[:src.index("def main():")], ns)
sys.path.insert(0, os.path.join(ROOT, "Tools"))
import voiceover
RAW = open(os.path.join(ROOT, "Productions", "MetaSports", "2026-10-14 42 Who Has Missed The Most Shots Ever", "_v3", "script.txt")).read().strip()
SPOKEN = " ".join(s for _, s in voiceover.parse_script(voiceover.apply_dictionary(RAW, "default")[0]))
ns["REF"] = SPOKEN
V2, V3, V4 = "eleven_multilingual_v2", "eleven_v3", "eleven_v4"
def s2(stab=.5, sim=.75, speed=1.2): return {"stability": stab, "similarity_boost": sim, "style": 0.0, "use_speaker_boost": True, "speed": speed}
def s4(stab=.5, sim=.75): return {"stability": stab, "similarity_boost": sim}
ALEX, PHAM, LIAM, DEUCE, NINJA = "yl2ZDV1MzN4HbQJbMihG", "GDS7e7WiI4GqkoRxZAFG", "VCgLBmBjldJmfphyB8sZ", "DaueUomjhh8LFuAV8aGj", "DcLiO3XaUWTu3gyon6hW"
DESIGNED = os.environ.get("DESIGNED_VOICE_ID", "")
CANDS = [  # name, voice_id, model, settings, label
    ("R5_A_v2", ALEX, V2, s2(), "Alex, multilingual v2, speed 1.2 (CONTROL: the #42 and #44 voice)"),
    ("R5_A_v4", ALEX, V4, s4(), "Alex, Eleven v4"),
    ("R5_A_v3", ALEX, V3, {"stability": .5}, "Alex, Eleven v3"),
    ("R5_F_v2", PHAM, V2, s2(speed=1.1), "pham v2 (our clone of the old channel narration), v2, speed 1.1"),
    ("R5_F_v4", PHAM, V4, s4(), "pham v2 clone, Eleven v4"),
    ("R5_L_v2", LIAM, V2, s2(), "Liam - Viral Short-Form (library, 443M chars/yr), v2, speed 1.2"),
    ("R5_L_v4", LIAM, V4, s4(), "Liam - Viral Short-Form, Eleven v4"),
    ("R5_D_v2", DEUCE, V2, s2(), "Deuce - Sports Podcast (library, young American), v2, speed 1.2"),
    ("R5_D_v4", DEUCE, V4, s4(), "Deuce, Eleven v4"),
    ("R5_N_v4", NINJA, V4, s4(), "Ninja - Engaging Sports (library, young American), Eleven v4"),
]
if DESIGNED:
    CANDS.append(("R5_Z_v4", DESIGNED, V4, s4(), "our designed voice (text-to-voice, owned by the account), Eleven v4"))


def tts192(vid, model, settings, text, out):
    import urllib.request as u
    body = json.dumps({"text": text, "model_id": model, "voice_settings": settings}).encode()
    req = u.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{vid}?output_format=mp3_44100_192", data=body,
                    headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"], "Content-Type": "application/json"})
    with u.urlopen(req, timeout=180) as r:
        open(out, "wb").write(r.read())


def main():
    resf = os.path.join(HERE, "results5.json")
    res = json.load(open(resf)) if os.path.exists(resf) else {}
    takes = int(os.environ.get("TAKES", "1"))
    only = set(filter(None, os.environ.get("ONLY", "").split(",")))
    for name, vid, model, sett, label in CANDS:
        if only and name not in only:
            continue
        for t in range(1, takes + 1):
            nm = f"{name}_t{t}"
            out = os.path.join(HERE, "takes", nm + ".mp3")
            if not os.path.exists(out):
                try:
                    tts192(vid, model, sett, SPOKEN, out)
                except Exception as e:
                    res[nm] = {"name": nm, "error": str(e)[:300]}; print(nm, "ERROR", str(e)[:200]); continue
            m = ns["measure"](nm); m.update(voice_id=vid, model=model, settings=sett, label=label)
            res[nm] = m
            json.dump(res, open(resf, "w"), indent=1, default=float)
            print(f"{nm:14} {m['dur']:>5}s wpm{m['wpm']:>4} WERphone {m['wer_phone']:>5} pitchSD {m['pitch_sd_semitones']} loudSD {m['loudness_sd_db']} HNR {m['hnr']} jit {m['jitter']} shim {m['shimmer']} gaps>.3 {m['gaps_over_0p3']}")
    # speaker similarity
    from resemblyzer import VoiceEncoder, preprocess_wav
    enc = VoiceEncoder("cpu")
    def emb(f, t=60):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-t", str(t), "-ac", "1", "-ar", "16000", "/tmp/_a5.wav"])
        return enc.embed_utterance(preprocess_wav("/tmp/_a5.wav"))
    import numpy as np
    clank = emb(os.environ.get("CLANK_REF", ""), 60) if os.environ.get("CLANK_REF") else None
    posted = emb(os.path.join(ROOT, "Productions", "MetaSports", "2026-10-14 42 Who Has Missed The Most Shots Ever", "_v3", "voice.mp3"))
    for nm, m in res.items():
        if "error" in m: continue
        e = emb(os.path.join(HERE, "takes", nm + ".mp3"))
        m["sim_to_42_voice"] = round(float(np.dot(e, posted)), 3)
        if clank is not None: m["sim_to_coachclank"] = round(float(np.dot(e, clank)), 3)
    json.dump(res, open(resf, "w"), indent=1, default=float)
    print("similarities written")


if __name__ == "__main__":
    main()
