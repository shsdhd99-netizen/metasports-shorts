"""Voice audition round 2 (Oct 14, 2026, night): genuinely different voices from the ElevenLabs Voice Library.

Same script (REF) and the same measures as audition.py (so the 12 earlier takes compare directly), plus:
number-word loudness vs other words, and speaker similarity (Resemblyzer) to (a) our old narration
(the clone's training recordings = the old Shorts' voice) and (b) CoachClank's narrator.
Library voices are used directly by voice_id (no need to add them to the account). Settings for every library
voice: eleven_multilingual_v2, stability .5, similarity .75, style 0, speed 1.1. Writes results2.json.
I cannot hear audio: these are measurements; the owner's ear decides naturalness and energy.
"""
import json, os, sys, subprocess
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "audition.py")).read()
ns = {"__file__": os.path.join(HERE, "audition.py")}
exec(src[:src.index("def main():")], ns)
tts, measure, REF, V2 = ns["tts"], ns["measure"], ns["REF"], ns["V2"]
LIB = {"s": {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": True, "speed": 1.1}}
CANDS = [  # name, voice_id, label (ElevenLabs Voice Library: name, accent, use case, clones at Oct 14 2026)
    ("L1_larry", "fIGaHjfrR8KmMy0vGEVJ", "Larry - High-Energy Social Media (american, 101K clones)"),
    ("L2_alex", "yl2ZDV1MzN4HbQJbMihG", "Alex - Upbeat, Energetic and Clear (american, 1.2M clones)"),
    ("L3_dan", "9F4C8ztpNUmXkdDDbz3J", "Dan - Upbeat, Dynamic and Friendly (american, 867K clones)"),
    ("L4_titan", "dtSEyYGNJqjrtBArPCVZ", "Titan - Deep, Bold, and Powerful (american, 583K clones)"),
    ("L5_adam", "bfGb7JTLUnZebZRiFYyq", "Adam - Distinct, Deep and Engaging (american, 508K clones)"),
    ("L6_tomas", "8sGzMkj2HZn6rYwGx6G0", "Tomas - Energetic and Quick Speaker (american, 11K clones)"),
    ("L7_tyler", "GyIXYY876myKNtA1j8NI", "Tyler - Energetic Arena Announcer (canadian, 11K clones)"),
    ("L8_lucan", "15CVCzDByBinCIoCblXo", "Lucan Rook - Energetic Male (american, 356K clones)"),
    ("L9_jon", "MFZUKuGQUsGJPQjTS4wC", "Jon - Warm and Grounded Storyteller (american, 827K clones)"),
]
SCR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None  # scratchpad with clonesrc/ and watch9/ (for similarity refs)

def main():
    resf = os.path.join(HERE, "results2.json")
    res = json.load(open(resf)) if os.path.exists(resf) else {}
    for name, vid, label in CANDS:
        out = os.path.join(HERE, "takes", name + ".mp3")
        if not os.path.exists(out):
            tts(vid, V2, LIB["s"], REF, out)
        m = measure(name); m.update(voice_id=vid, label=label, model=V2, settings=LIB["s"], chars=len(REF))
        res[name] = m
        print(f"{name:10} {m['dur']:>5}s wpm{m['wpm']:>4} WER {m['wer_clean']:>5}/{m['wer_phone']:>5} names {m['names_clean']} pitchSD {m['pitch_sd_semitones']} loudSD {m['loudness_sd_db']} HNR {m['hnr']}")
        json.dump(res, open(resf, "w"), indent=1, default=float)
    # extras: number emphasis + speaker similarity, for the new takes and the earlier finalists
    from faster_whisper import WhisperModel
    from resemblyzer import VoiceEncoder, preprocess_wav
    import parselmouth, re
    enc = VoiceEncoder("cpu"); wm = WhisperModel("small", device="cpu", compute_type="int8")
    def emb(f, t=90):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-t", str(t), "-ac", "1", "-ar", "16000", "/tmp/_a2.wav"])
        return enc.embed_utterance(preprocess_wav("/tmp/_a2.wav"))
    refs = {}
    if SCR:
        refs["old_voice"] = emb(os.path.join(SCR, "clonesrc", "pv2_2.mp3"))
        c = emb(os.path.join(SCR, "watch9", "ck_alley", "video.mp4")) + emb(os.path.join(SCR, "watch9", "ck_shaq", "video.mp4"))
        refs["coachclank"] = c / np.linalg.norm(c)
    NUM = re.compile(r"\d|^(three|hundred|fifty|zero|five|seven|foot)$", re.I)
    extra = {}
    for name in [c[0] for c in CANDS] + ["A3_clone_raw_names", "A_clone_prod", "B_clone_expressive", "C_clone_v3", "G_liam_v3"]:
        wav = os.path.join(HERE, "takes", name + ".wav")
        if not os.path.exists(wav):
            continue
        segs, _ = wm.transcribe(wav, language="en", word_timestamps=True)
        ws = [(w.word.strip(), w.start, w.end) for s_ in segs for w in s_.words]
        snd = parselmouth.Sound(wav); x = snd.values[0]; sr = snd.sampling_frequency
        def db(a, b):
            a, b = int(a * sr), int(b * sr)
            return 20 * np.log10(np.sqrt(np.mean(x[a:b] ** 2)) + 1e-9) if b - a > 50 else None
        nums = [db(a, b) for w, a, b in ws if NUM.search(re.sub(r"[^a-z0-9]", "", w.lower()) or "x")]
        oth = [db(a, b) for w, a, b in ws if not NUM.search(re.sub(r"[^a-z0-9]", "", w.lower()) or "x") and len(w) > 4]
        nums = [v for v in nums if v is not None]; oth = [v for v in oth if v is not None]
        e = emb(wav)
        extra[name] = {"number_loudness_vs_other_db": round(float(np.mean(nums) - np.mean(oth)), 2) if nums and oth else None,
                       **{f"similarity_to_{k}": round(float(np.dot(e, v)), 3) for k, v in refs.items()}}
        print(name, extra[name])
    json.dump(extra, open(os.path.join(HERE, "results2_extra.json"), "w"), indent=1)

main()
