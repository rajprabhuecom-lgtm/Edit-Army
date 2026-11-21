import sherpa_onnx, soundfile as sf
M='asr/sherpa-onnx-whisper-large-v3/large-v3-'
a,sr=sf.read('a16.wav',dtype='float32')
C=[(0,3.6),(3.6,7.64),(7.64,10.2),(10.2,12.48),(15.25,17.66),(17.66,20.38),(20.38,22.48),(25.5,27.4),(27.36,29.6),(29.4,31.42),(31.42,33.5),(33.4,35.38),(35.38,38.2),(38.1,40.91),(40.91,42.6)]
r=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=M+'encoder.int8.onnx',decoder=M+'decoder.int8.onnx',tokens=M+'tokens.txt',language='ta',task='transcribe',num_threads=4)
for s,e in C:
    st=r.create_stream(); st.set_option('max_tokens_per_second','40'); st.accept_waveform(sr,a[int(s*sr):int(e*sr)]); r.decode_stream(st); print(f'{s:6.2f}-{e:6.2f} | {st.result.text}',flush=True)
