import sys, json, soundfile as sf
from faster_whisper import WhisperModel
m = WhisperModel('medium', device='cpu', compute_type='int8', cpu_threads=4)
P = {'main': "சென்னையில் weight loss பண்ண struggle பண்ற மக்களுக்கு ஒரு important update! Weight loss பண்ண try பண்ணிட்டு இருக்கீங்களா? ஆனா எது work ஆகுது, எது work ஆகலன்னு புரியலையா? Diet, workout-னு பல விஷயங்கள் try பண்ணியும், expected result கிடைக்காம struggle பண்றீங்களா? Busy lifestyle நால consistency maintain பண்ண முடியலையா? நம்ம clients-உம் இதே மாதிரிதான் struggle பண்ணியிருக்காங்க. ஆனா proper nutrition and fitness guidance follow பண்ணி, healthy-ஆன changes achieve பண்ணியிருக்காங்க. நான் தமிழ் இலக்கியா. New Life Nutritions-ல 5 years experience-ஓட, உங்களோட fitness and weight management journey-க்கு guide பண்ணிட்டு இருக்கேன். உங்களோட lifestyle and fitness goals-க்கு ஏத்த personalized guidance மூலமா, step-by-step-ஆ உங்களுக்கு support பண்றோம். இப்போ New Life Nutritions-ல 3 days free trial offer available! சென்னையில இருக்கிற நீங்களும் உங்களோட fitness journey-யை start பண்ண ready-ஆ இருந்தா, இந்த offer-ஐ miss பண்ணாதீங்க! கீழே இருக்கிற button-ஐ click பண்ணி, online registration-ஐ இப்போவே complete பண்ணுங்க. உங்களோட appointment-ஐ book பண்ணி, உங்களோட fitness journey-யை New Life Nutritions-ஓட இன்னைக்கே start பண்ணுங்க!",
     'testi': "நான் New Life Nutritions-ல join பண்ணேன். என்னோட weight, kg குறைஞ்சது. Coach தமிழ் இலக்கியா ரொம்ப நல்லா guide பண்ணாங்க. Healthy-ஆ இருக்கேன், energy இருக்கு."}
for n in sys.argv[1:]:
    a = sf.read(f'/home/user/w/audio/{n}16.wav', dtype='float32')[0]
    segs, info = m.transcribe(a, language='ta', word_timestamps=True, beam_size=1, initial_prompt=P[n], condition_on_previous_text=True)
    out = []
    for s in segs:
        out.append(dict(s=s.start, e=s.end, text=s.text, words=[(w.start, w.end, w.word) for w in s.words]))
        print(f'{s.start:6.2f}-{s.end:6.2f} {s.text}', flush=True)
    json.dump(out, open(f'/home/user/w/audio/{n}.tx.json', 'w'), ensure_ascii=False)
