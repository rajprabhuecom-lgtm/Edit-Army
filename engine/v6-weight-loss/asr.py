import sherpa_onnx, soundfile as sf, json, sys
M='asr/sherpa-onnx-whisper-large-v3/large-v3-'
sil=[float(x) for x in sys.argv[1].split()]
a,sr=sf.read('a16.wav',dtype='float32')
cuts=[0.0]+[(sil[i]+sil[i+1])/2 for i in range(0,len(sil),2)]+[len(a)/sr]
out=[]
for task in ['transcribe','translate']:
    r=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=M+'encoder.int8.onnx',decoder=M+'decoder.int8.onnx',tokens=M+'tokens.txt',language='ta',task=task,num_threads=4)
    res=[]
    for s,e in zip(cuts,cuts[1:]):
        st=r.create_stream(); st.accept_waveform(sr,a[int(s*sr):int(e*sr)]); r.decode_stream(st); res.append(st.result.text)
    out.append(res); del r
for (s,e),t,tr in zip(zip(cuts,cuts[1:]),*out): print(f'{s:6.2f}-{e:6.2f} | {t} | {tr}')
