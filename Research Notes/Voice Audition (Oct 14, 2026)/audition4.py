"""Voice audition round 4 (Oct 14, 2026, late night): the owner's picks A (Alex) and F (our clone "pham v2", fixed settings)
against the current production Pham, the original "Pham" clone, and a NEW clone "Pham v3" built tonight.

Script: #21's rewritten script (_v5, Script Critic v3 APPROVE): a hook, explanation, NBA names, numbers and a payoff.
The same spoken text for every voice (names through pronunciation.json "default": Jokic -> Yokitch).
Two takes per voice (consistency). Same measures as audition.py plus speaker similarity to the old narration.
Run: . key.sh && python3 audition4.py <scratchpad>
I cannot hear audio: these are measurements; the owner's ear decides between the finalists.
"""
import json, os, re, subprocess, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
src = open(os.path.join(HERE, "audition.py")).read()
ns = {"__file__": os.path.join(HERE, "audition.py")}
exec(src[:src.index("def main():")], ns)
sys.path.insert(0, os.path.join(ROOT, "Tools"))
import voiceover
RAW = open(os.path.join(ROOT, "Productions", "MetaSports", "2026-10-04 21 How Close Is Jokic To Westbrooks Record", "_v5", "script.txt")).read().strip()
TEXT_SPOKEN = " ".join(s for _, s in voiceover.parse_script(voiceover.apply_dictionary(RAW, "default")[0]))
TEXT_REF = " ".join(d for d, _ in voiceover.parse_script(RAW))
V2 = "eleven_multilingual_v2"
def st(stab, sim, speed, style=0.0):
    return {"stability": stab, "similarity_boost": sim, "style": style, "use_speaker_boost": True, "speed": speed}
VOICES = {  # key: (voice_id, settings, label)
    "A_alex": ("yl2ZDV1MzN4HbQJbMihG", st(.5, .75, 1.2), "A: Alex (Voice Library), house settings"),
    "F_pv2_fixed": ("GDS7e7WiI4GqkoRxZAFG", st(.5, .75, 1.1), "F: pham v2, fixed settings"),
    "P0_pv2_current": ("GDS7e7WiI4GqkoRxZAFG", st(.65, .7, 1.15), "current production Pham (pham v2, Oct 5-14 settings)"),
    "P1_pham_orig": ("H2ovX6h6fD6dmyrg5SkI", st(.5, .75, 1.1), "original 'Pham' clone (one 27 s sample), fixed settings"),
    "N_pham_v3": ("61QfR1QEcJUskHn8yioH", st(.5, .75, 1.1), "NEW clone 'Pham v3' (de-duplicated recordings), fixed settings"),
}

def main():
    scr = os.path.abspath(sys.argv[1])
    resf = os.path.join(HERE, "results4.json")
    res = json.load(open(resf)) if os.path.exists(resf) else {}
    ns["REF"] = TEXT_REF
    for vk, (vid, sett, label) in VOICES.items():
        for t in (1, 2):
            name = f"R4_{vk}_t{t}"
            out = os.path.join(HERE, "takes", name + ".mp3")
            if not os.path.exists(out):
                ns["tts"](vid, V2, sett, TEXT_SPOKEN, out)
            m = ns["measure"](name); m.update(voice=vk, voice_id=vid, label=label, settings=sett)
            res[name] = m
            print(f"{name:24} {m['dur']:>5}s wpm{m['wpm']:>4} WER {m['wer_clean']:>5}/{m['wer_phone']:>5} pitchSD {m['pitch_sd_semitones']} loudSD {m['loudness_sd_db']} HNR {m['hnr']} gaps>.3 {m['gaps_over_0p3']} max_gap {m['max_gap']}")
            json.dump(res, open(resf, "w"), indent=1, default=float)
    from resemblyzer import VoiceEncoder, preprocess_wav
    enc = VoiceEncoder("cpu")
    def emb(f):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-t", "90", "-ac", "1", "-ar", "16000", "/tmp/_a4.wav"])
        return enc.embed_utterance(preprocess_wav("/tmp/_a4.wav"))
    old = emb(os.path.join(scr, "clonesrc", "pv2_0.mp3"))
    cons = {}
    for vk in VOICES:
        a, b = (os.path.join(HERE, "takes", f"R4_{vk}_t{t}.wav") for t in (1, 2))
        ea, eb = emb(a), emb(b)
        cons[vk] = {"take_similarity": round(float(np.dot(ea, eb)), 3), "similarity_to_old_narration": round(float(np.dot(ea, old)), 3),
                    "wpm": [res[f"R4_{vk}_t1"]["wpm"], res[f"R4_{vk}_t2"]["wpm"]],
                    "pitch_sd": [res[f"R4_{vk}_t1"]["pitch_sd_semitones"], res[f"R4_{vk}_t2"]["pitch_sd_semitones"]]}
        print(vk, cons[vk])
    json.dump(cons, open(os.path.join(HERE, "results4_consistency.json"), "w"), indent=1)

main()
