"""Voice lab: generate the SAME text with different ElevenLabs settings and measure each take (cost: ~1 credit per character per variant).

  . key.sh && python voice_lab.py --script "<folder>/script.txt" --out lab_dir --variants v0,v1,v4      # run chosen presets
  python voice_lab.py --list                                                                          # show presets
Measures per take (free, local): words per minute as generated, voice quality (HNR/jitter/shimmer via voice_quality.py), whether a speech
recogniser hears every script word (WER, names ignored when respelled), and the time-stretch needed to reach 250 wpm. Saves lab_dir/<variant>.mp3
(+ _250.mp3 = the take sped up with atempo to about 250 wpm) so a person can listen. Never prints the API key.
"""
import argparse, base64, difflib, json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from voiceover import load_env, call, parse_script, words_from_alignment  # noqa: E402
import voice_quality as vq  # noqa: E402

PRESETS = {  # name: (model, settings, output_format)
    "v0": ("eleven_multilingual_v2", dict(stability=0.45, similarity_boost=0.8, use_speaker_boost=True, speed=1.1), "mp3_44100_128"),   # what we used so far
    "v1": ("eleven_multilingual_v2", dict(stability=0.65, similarity_boost=0.7, use_speaker_boost=True, speed=1.1), "mp3_44100_128"),
    "v2": ("eleven_multilingual_v2", dict(stability=0.85, similarity_boost=0.7, use_speaker_boost=True, speed=1.1), "mp3_44100_128"),
    "v3": ("eleven_multilingual_v2", dict(stability=0.65, similarity_boost=0.7, use_speaker_boost=True, speed=1.2), "mp3_44100_128"),
    "v4": ("eleven_v4", dict(stability=0.5, similarity_boost=0.75, use_speaker_boost=True), "mp3_44100_128"),
    "v5": ("eleven_v4_turbo", dict(stability=0.5, similarity_boost=0.75, use_speaker_boost=True), "mp3_44100_128"),
    "v6": ("eleven_v3", dict(stability=0.5, similarity_boost=0.75, use_speaker_boost=True), "mp3_44100_128"),
    "v8": ("eleven_multilingual_v2", dict(stability=0.65, similarity_boost=0.7, use_speaker_boost=True, speed=1.15), "mp3_44100_128"),
    "v9": ("eleven_multilingual_v2", dict(stability=0.75, similarity_boost=0.7, use_speaker_boost=True, speed=1.15), "mp3_44100_128"),
    "v7": ("eleven_multilingual_v2", dict(stability=0.65, similarity_boost=0.7, use_speaker_boost=False, speed=1.1), "mp3_44100_128"),
}


def heard_error(audio, want_text):
    from voice_check import norm_words, stt_local
    segs = parse_script(want_text)
    want = norm_words(" ".join(d for d, _ in segs))
    res = stt_local(audio)
    got = norm_words(res["text"])
    err, bad = 0, []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=want, b=got, autojunk=False).get_opcodes():
        if op != "equal":
            e, h = " ".join(want[i1:i2]), " ".join(got[j1:j2])
            if difflib.SequenceMatcher(a=e.replace(" ", ""), b=h.replace(" ", "")).ratio() < 0.72:  # not just a name spelled differently
                err += max(i2 - i1, j2 - j1); bad.append(f"{e}->{h}")
    return err / max(1, len(want)), bad[:6]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script"); ap.add_argument("--out", default="voice_lab"); ap.add_argument("--variants", default="v0,v1,v2,v3,v4")
    ap.add_argument("--list", action="store_true"); ap.add_argument("--voice-id")
    a = ap.parse_args()
    if a.list:
        for k, v in PRESETS.items(): print(k, v)
        return
    env = load_env(); key = env.get("ELEVENLABS_API_KEY"); voice = a.voice_id or env.get("ELEVENLABS_VOICE_ID")
    if not key or not voice: raise SystemExit("need ELEVENLABS_API_KEY / ELEVENLABS_VOICE_ID (source key.sh first)")
    raw = open(a.script, encoding="utf-8-sig").read()
    segs = parse_script(raw); spoken = " ".join(s for _, s in segs).strip()
    os.makedirs(a.out, exist_ok=True)
    print(f"{len(spoken)} characters per variant")
    for name in a.variants.split(","):
        model, st, fmt = PRESETS[name]
        res = call(f"/text-to-speech/{voice}/with-timestamps?output_format={fmt}", key, {"text": spoken, "model_id": model, "voice_settings": st})
        mp3 = os.path.join(a.out, f"{name}.mp3"); open(mp3, "wb").write(base64.b64decode(res["audio_base64"]))
        words = words_from_alignment(res.get("alignment") or res["normalized_alignment"])
        dur = words[-1][2] if words else 0; wpm = len(words) / (dur / 60) if dur else 0
        factor = max(1.0, min(1.6, 250 / wpm)) if wpm else 1.0
        s250 = os.path.join(a.out, f"{name}_250.mp3")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp3, "-filter:a", f"atempo={factor:.3f}", s250], check=True)
        w = vq.to_wav(mp3)
        try: m = vq.measure(w)
        finally: os.remove(w)
        w2 = vq.to_wav(s250)
        try: m2 = vq.measure(w2)
        finally: os.remove(w2)
        wer, bad = heard_error(mp3, raw)
        print(f"{name} {model:24s} stab {st['stability']} sim {st['similarity_boost']} spd {st.get('speed','-')}: {wpm:3.0f} wpm raw, stretch x{factor:.2f} | HNR {m['hnr']:.1f} jit {m['jitter']:.2f} shim {m['shimmer']:.1f} (after stretch HNR {m2['hnr']:.1f}) | WER {wer*100:.1f}% {bad}", flush=True)


if __name__ == "__main__":
    main()
