"""Voice audition round 3 (Oct 14, 2026, late): the finalists at our real pace, on two scripts, two takes each.

Why: round 2 ran library voices at speed 1.1 (154-196 wpm), slower than our 206-252 wpm house pace, and on one script.
This round: (1) the library finalists at native speed 1.2 (the API maximum), (2) the clone with "fixed" settings
(stability .5, similarity .75, speed 1.1, no denoise) vs production, (3) a second, story-voice script (our own Curry
Kobes Short, 30.8K) with two takes per voice to measure take-to-take consistency, (4) Alex on eleven_v3 once.
No respellings anywhere (round 1: plain "Wembanyama" was heard right; respelling was not).
Same measures as audition.py, plus consistency (speaker similarity between takes, wpm spread).
Run: . key.sh && python3 audition3.py <scratchpad>   (the scratchpad holds clonesrc/pv2_2.mp3 for the old-voice similarity)
I cannot hear audio: these are measurements; the owner's ear decides between the finalists.
"""
import json, os, re, subprocess, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "audition.py")).read()
ns = {"__file__": os.path.join(HERE, "audition.py")}
exec(src[:src.index("def main():")], ns)
tts, measure_ns, REF, V2 = ns["tts"], ns["measure"], ns["REF"], ns["V2"]
STORY = ("Stephen Curry just pulled one of the wildest sneaker moves the NBA has ever seen. In his first game after leaving "
         "Under Armour, he stepped on the court wearing Nike Kobes. Not customs, not tributes, actual Kobes. Fans noticed "
         "instantly. People courtside were pointing at his feet before he even touched the ball. But the craziest part? "
         "Under Armour executives were in the arena, watching him hoop in a rival brand. And Curry still dropped thirty "
         "like nothing happened.")
CLONE = "GDS7e7WiI4GqkoRxZAFG"
def st_(stab, sim, speed, style=0.0):
    d = {"stability": stab, "similarity_boost": sim, "style": style, "use_speaker_boost": True}
    if speed: d["speed"] = speed
    return d
VOICES = {  # key: (voice_id, model, settings, label)
    "P0_clone_prod": (CLONE, V2, st_(.65, .7, 1.15), "clone 'pham v2', production settings"),
    "P1_clone_fixed": (CLONE, V2, st_(.5, .75, 1.1), "clone 'pham v2', stability .5, speed 1.1"),
    "X1_alex_s12": ("yl2ZDV1MzN4HbQJbMihG", V2, st_(.5, .75, 1.2), "Alex (library), speed 1.2"),
    "X3_lucan_s12": ("15CVCzDByBinCIoCblXo", V2, st_(.5, .75, 1.2), "Lucan Rook (library), speed 1.2"),
    "X4_jon_s12": ("MFZUKuGQUsGJPQjTS4wC", V2, st_(.5, .75, 1.2), "Jon (library), speed 1.2"),
    "X5_alex_v3": ("yl2ZDV1MzN4HbQJbMihG", "eleven_v3", st_(.5, .75, None), "Alex (library) on eleven_v3"),
}
PLAN = [  # (take name, voice key, script name)
    ("R3_P1_ref", "P1_clone_fixed", "REF"), ("R3_X1_ref", "X1_alex_s12", "REF"), ("R3_X3_ref", "X3_lucan_s12", "REF"),
    ("R3_X4_ref", "X4_jon_s12", "REF"), ("R3_X5_ref", "X5_alex_v3", "REF"),
] + [(f"R3_{k.split('_')[0]}_story_t{t}", k, "STORY") for k in ("P0_clone_prod", "P1_clone_fixed", "X1_alex_s12", "X3_lucan_s12", "X4_jon_s12") for t in (1, 2)]
TEXT = {"REF": REF, "STORY": STORY}

def main():
    scr = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None
    resf = os.path.join(HERE, "results3.json")
    res = json.load(open(resf)) if os.path.exists(resf) else {}
    for name, vk, sk in PLAN:
        vid, model, sett, label = VOICES[vk]
        out = os.path.join(HERE, "takes", name + ".mp3")
        if not os.path.exists(out):
            tts(vid, model, sett, TEXT[sk], out)
        ns["REF"] = TEXT[sk]  # measure() scores WER against the module-level REF
        m = measure_ns(name); m.update(voice=vk, voice_id=vid, label=label, model=model, settings=sett, script=sk, chars=len(TEXT[sk]))
        res[name] = m
        print(f"{name:20} {m['dur']:>5}s wpm{m['wpm']:>4} WER {m['wer_clean']:>5}/{m['wer_phone']:>5} pitchSD {m['pitch_sd_semitones']} loudSD {m['loudness_sd_db']} HNR {m['hnr']} gaps>.3 {m['gaps_over_0p3']}")
        json.dump(res, open(resf, "w"), indent=1, default=float)
    # consistency + similarity to the old narration
    from resemblyzer import VoiceEncoder, preprocess_wav
    enc = VoiceEncoder("cpu")
    def emb(f):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-t", "90", "-ac", "1", "-ar", "16000", "/tmp/_a3.wav"])
        return enc.embed_utterance(preprocess_wav("/tmp/_a3.wav"))
    old = emb(os.path.join(scr, "clonesrc", "pv2_2.mp3")) if scr else None
    cons = {}
    for vk in ("P0_clone_prod", "P1_clone_fixed", "X1_alex_s12", "X3_lucan_s12", "X4_jon_s12"):
        a, b = (os.path.join(HERE, "takes", f"R3_{vk.split('_')[0]}_story_t{t}.wav") for t in (1, 2))
        ea, eb = emb(a), emb(b)
        ra, rb = res[f"R3_{vk.split('_')[0]}_story_t1"], res[f"R3_{vk.split('_')[0]}_story_t2"]
        cons[vk] = {"take_similarity": round(float(np.dot(ea, eb)), 3), "wpm_t1_t2": [ra["wpm"], rb["wpm"]],
                    "pitch_sd_t1_t2": [ra["pitch_sd_semitones"], rb["pitch_sd_semitones"]],
                    "similarity_to_old_voice": round(float(np.dot(ea, old)), 3) if old is not None else None}
        print(vk, cons[vk])
    json.dump(cons, open(os.path.join(HERE, "results3_consistency.json"), "w"), indent=1)

main()
