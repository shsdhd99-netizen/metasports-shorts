# Voice investigation (Oct 5, 2026): "the voice has gotten worse, started to glitch"
Method: no listening is possible for me, so I measured. Free local tools: faster-whisper (what does a recogniser hear vs the script?) and Praat (HNR = harmonics-to-noise ratio, jitter, shimmer, pitch jumps) on 64 narration takes (all Shorts, raw and final), plus a voice lab (same 583-character script, 8 ElevenLabs settings).

## Facts found
- The voice is a CLONE ("pham v2", category cloned). Its own saved settings: stability 1.0, similarity 0.7, speed 1.0. Our pipeline overrode them with stability 0.45 / similarity 0.8 / speed 1.1 and then time-stretched with atempo (up to x1.6). These defaults were unchanged since the first commit; the Wemby take the user liked (HNR 9.3-9.9, PASS) was one good draw of the same settings.
- Plan: ElevenLabs Starter (90,000 characters per cycle; 51,844 used on Oct 5; resets Oct 8). Models available: eleven_v4, eleven_v4_turbo, eleven_v3, eleven_multilingual_v2 (only v2 has a speed control). v4/v4_turbo read at ~155 wpm and would need a x1.6 stretch (worse), so not adopted.
- Time-stretch costs quality (PROVEN on our takes): atempo x1.165 lowers HNR 8.6 -> 8.1 and raises shimmer; x1.4 -> 7.7. rubberband is worse (HNR 5.0-6.9, shimmer 13-17%).
- Recording variance matters as much as settings: HNR ranged 6.7-9.9 across takes (+-0.7 dB between takes of the same text). Short pieces (1.5-3 s, from spliced Shorts) measured lowest (6.7-7.4).
- Per-piece `loudnorm` in splice_voice ducked the last 0.25 s of narration pieces by 1-4 dB (e.g. #25 piece 0: -4.6 dB): sentence ends sound swallowed. Raw ElevenLabs output is also very quiet (+10 dB gain needed). Replaced by a plain measured gain + limiter.
- Several MP3 re-encodes (128 kbps from ElevenLabs -> atempo -> default-bitrate mp3 -> splice mp3 -> AAC). Intermediates now use libmp3lame -q:a 0.
- No word-level glitches were found by speech recognition (all differences were names or numbers written differently), so the audible problem is acoustic (stretch artifacts, noisy clone at low stability, squashed sentence ends), not wrong words. The recogniser itself hallucinated phrases over silent tails (fixed with VAD and dropping words squeezed into <0.03 s).
- The skill already said to run voice_check after voiceover; the recent builds skipped it. Now it is automatic (voice_take.py).
- Lab on one script (HNR, WER-real): v0 old settings 7.8 (stretch x1.33 -> 6.7); v1 stab .65 8.5; v2 stab .85 8.1; v3 stab .65 speed 1.2 8.5 with no stretch (268 wpm raw); v8 speed 1.15 7.9 (237 wpm); v9 stab .75 8.6.

## Decision
Default settings: stability 0.65, similarity 0.7, native speed auto (1.2/1.15/1.1 by script length so the narration stays >= 22.5 s), stretch cap x1.08, 0.3 s tail pad, plain-gain splice, gate + retry (max 3 takes). User listening test sent Oct 5 (A old, B calm+stretched, C new native fast): taste is the user's call; if they prefer another, change defaults in voiceover.py and re-run revoice.py.
Pilot: #21 re-voiced (22.2 s, 242 wpm, QA PASS, HNR 8.3).
Not verified: the new voice by ear (nobody has listened yet).
