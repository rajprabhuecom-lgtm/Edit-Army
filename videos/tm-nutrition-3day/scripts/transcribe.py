"""Tamil transcription with Whisper large-v3 (faster-whisper, int8 CPU) with word timestamps.
usage: python3 transcribe.py in.wav out.json [start_s end_s]
Output: [{"s": start, "e": end, "t": text, "w": [[ws, we, word], ...]}]  (seconds in the source clip)
Model: Systran/faster-whisper-large-v3 in /root/models/fw-large-v3 (huggingface snapshot_download)."""
import sys, json
import soundfile as sf
from faster_whisper import WhisperModel
wav, out = sys.argv[1], sys.argv[2]
m = WhisperModel('/root/models/fw-large-v3', device='cpu', compute_type='int8', cpu_threads=4)
audio, sr = sf.read(wav, dtype='float32')  # 16 kHz mono wav (passing an array avoids PyAV)
assert sr == 16000
segs, info = m.transcribe(audio, language='ta', beam_size=1, word_timestamps=True, vad_filter=True,
                          vad_parameters=dict(min_silence_duration_ms=350), condition_on_previous_text=False,
                          temperature=0.0, compression_ratio_threshold=None, log_prob_threshold=None, no_speech_threshold=None)
res = []
for s in segs:
    res.append({'s': round(s.start, 2), 'e': round(s.end, 2), 't': s.text.strip(),
                'w': [[round(w.start, 2), round(w.end, 2), w.word] for w in (s.words or [])]})
    print(f'{s.start:7.2f}-{s.end:7.2f}  {s.text.strip()}', flush=True)
json.dump(res, open(out, 'w'), ensure_ascii=False, indent=0)
