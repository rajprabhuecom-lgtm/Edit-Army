"""Transcribe only the stretches where the coach is speaking (from who_speaks.py), one by one.
usage: python3 transcribe_client.py C0008L  -> speak/<name>_client_text.json  [[a, b, text], ...]"""
import sys, json, numpy as np, soundfile as sf
from faster_whisper import WhisperModel
B = '/home/user/w/tm/'; name = sys.argv[1]
iv = json.load(open(B + f'speak/{name}.json'))['client']
au, sr = sf.read(B + f'mezz/{name[:-1]}.16k.wav', dtype='float32')
m = WhisperModel('/root/models/fw-large-v3', device='cpu', compute_type='int8', cpu_threads=4)
out = []
for a, b in iv:
    seg = au[int(max(0, a - .05) * sr):int((b + .1) * sr)]
    seg = np.concatenate([np.zeros(4000, np.float32), seg, np.zeros(4000, np.float32)])
    ss, _ = m.transcribe(seg, language='ta', beam_size=5, vad_filter=False, condition_on_previous_text=False, temperature=0.0,
                         compression_ratio_threshold=None, log_prob_threshold=None, no_speech_threshold=None, word_timestamps=True)
    ss = list(ss); txt = ' '.join(s.text.strip() for s in ss)
    words = [[round(a - .05 - .25 + w.start, 2), round(a - .05 - .25 + w.end, 2), w.word.strip()] for s in ss for w in (s.words or [])]
    out.append([a, b, txt, words]); print(f'{a:7.2f}-{b:7.2f} | {txt}', flush=True)
json.dump(out, open(B + f'speak/{name}_client_text.json', 'w'), ensure_ascii=False)
