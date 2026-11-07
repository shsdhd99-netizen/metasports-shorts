"""Pronunciation test for the primary voice (Alex): hard NBA names, plain vs respelled. Whisper hears each take.
Run: . key.sh && python3 names_test.py   -> takes/N_*.mp3, names_results.json. I can't hear audio; whisper's spelling is a proxy."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "audition.py")).read(); ns = {"__file__": os.path.join(HERE, "audition.py")}
exec(src[:src.index("def main():")], ns)
PLAIN = ("Nikola Jokic. Luka Doncic. Shai Gilgeous-Alexander. Giannis Antetokounmpo. Victor Wembanyama. Alperen Sengun. "
         "Kristaps Porzingis. Jusuf Nurkic. Jonas Valanciunas. Bogdan Bogdanovic. Domantas Sabonis. Dereck Lively.")
RESP = ("Nikola Yokitch. Luka Dontchitch. Shai Gilgeous-Alexander. Yannis Antetokounmpo. Victor Wembanyama. Alperen Shengoon. "
        "Kristaps Porzingis. Yusuf Nurkitch. Yonas Valanchoonas. Bogdan Bogdanovitch. Domantas Sabonis. Dereck Lively.")
S = {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": True, "speed": 1.2}
out = {}
for name, text in [("N_alex_plain", PLAIN), ("N_alex_respelled", RESP)]:
    mp3 = os.path.join(HERE, "takes", name + ".mp3")
    if not os.path.exists(mp3): ns["tts"]("yl2ZDV1MzN4HbQJbMihG", "eleven_multilingual_v2", S, text, mp3)
    wav = mp3[:-4] + ".wav"; ns["sh"]("ffmpeg", "-v", "error", "-y", "-i", mp3, "-ac", "1", "-ar", "16000", wav)
    hyp, _ = ns["stt"](wav); out[name] = {"sent": text, "heard": hyp}; print(name, "|", hyp)
json.dump(out, open(os.path.join(HERE, "names_results.json"), "w"), indent=1)
