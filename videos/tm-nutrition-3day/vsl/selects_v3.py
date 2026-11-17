"""VSL v3 selects (voice-ID trimmed, scripts/voice_id.py: start after the prompter's last syllable, end before his next; cuts snapped to the quietest 10 ms).
VSL v2 selects: only the COACH speaking (face tracking: mouth moving + voice), never the off-camera prompter.
How these were chosen (scripts/face_track.py -> who_speaks.py -> transcribe_client.py):
  * the prompter reads each line first, the coach repeats it; prompter lines have voice but no mouth movement and are dropped
  * every take below is a stretch where the coach's mouth moves, transcribed on its own, matched to the script
  * trimmed on word timings to drop "okay வா", repeats and chatter
Times are seconds in the working copies (C0007L.mp4 / C0008L.mp4)."""
SEL = [
 # id     file    a       b       spoken by the coach (cleaned)                                                         meaning
 ('V01', 'C0007', 46.42, 51.05, 'உங்க வீட்டுல ரெண்டு பேரும் weight குறைக்கணும்னு எத்தனை தடவை முடிவு பண்ணியிருப்பீங்க?', 'How many times have you both decided to lose weight?'),
 ('V02', 'C0007', 55.25, 59.91, 'இந்த video-வ முழுசா பாருங்க. உங்க family-க்கான answer இந்த video-ல இருக்கு.', 'Watch fully - the answer for your family is in this video.'),
 ('V03', 'C0007', 75.86, 79.25, 'Hi, நான் Coach Pradheesh பேசுறேன். TM Nutrition Centre, Trichy.', 'Hi, I am Coach Pradheesh, TM Nutrition Centre, Trichy.'),
 ('V04', 'C0007', 101.26, 105.40, '18 வருஷமா நூற்றுக்கணக்கான families-ஐ healthy-ஆ மாத்தியிருக்கோம்.', '18 years, hundreds of families made healthy. (CONFIRM)'),
 ('V05', 'C0007', 109.45, 111.85, 'இப்போ புது batch, couples-க்கு மட்டும்.', 'Now a new batch, only for couples.'),
 ('V06', 'C0007', 140.41, 142.46, 'மூணு நாள் diet... அப்புறம் biryani.', 'Three days of diet... then biryani.'),
 ('V07', 'C0007', 146.07, 149.90, 'Gym membership கட்டி, முழுசா ரெண்டு வாரம் கூட போறது இல்ல.', 'Pay for the gym, never go even two full weeks.'),
 ('V08', 'C0007', 154.77, 157.55, 'ராத்திரி 12 மணி வரைக்கும் கையில mobile.', 'Mobile in hand till midnight.'),
 ('V09', 'C0007', 162.60, 167.75, '"நாளைக்கு ஆரம்பிச்சுக்கலாம்"னு ரெண்டு பேரும் ஒருவருக்கொருவர் சமாதானப்படுத்திப்பீங்க.', '"Let\'s start tomorrow" - you reassure each other.'),
 ('V10', 'C0007', 202.10, 205.48, 'Problem will power-ல இல்ல. உங்க வீட்டோட pattern-ல இருக்கு.', 'The problem is not willpower. It is your home\'s pattern.'),
 ('V11', 'C0008', 16.95, 18.66, 'இவரு 58 வயசு.', 'He is 58.'),
 ('T11', 'T_vid_0606', 28.85, 38.85, 'HbA1c level 9.6 இருந்தது. தொடர்ந்து 4 மாசம் follow பண்ணதுல 5.4-ஆ குறைஞ்சிருச்சு. என்னுடைய 12 kg excess weight-ஐ குறைச்சு ideal weight reach ஆயிட்டேன்.', '(Raveendran, 58) HbA1c 9.6 -> 5.4 in 4 months; lost 12 kg excess, reached ideal weight.'),
 ('V12', 'C0008', 25.78, 30.55, 'இவரு Erode-லருந்து, 32 வயசு. 26 kg excess weight.', 'He is from Erode, 32. 26 kg excess weight.'),
 ('T12', 'T_vid_0608', 21.92, 27.80, 'ஆறு மாசத்துல 26 kg குறைச்சு, இப்போ ideal weight-ல fit-ஆ, happy-ஆ இருக்கேன்.', '(Sivakarthik, 32) Lost 26 kg in 6 months; now ideal weight, fit and happy.'),
 ('V13', 'C0007', 325.65, 327.85, 'இவங்க 48 வயசு.', 'She is 48.'),
 ('T13', 'T_vid_0610', 15.38, 19.50, 'Sugar, pressure border-ல இருந்தது. Over weight-ல இருந்தேன்.', '(Krishna Priya, 48) Sugar and pressure were borderline; I was overweight.'),
 ('T13b', 'T_vid_0610', 33.42, 36.52, 'Thyroid, sugar, pressure எல்லாம் control-க்கு வந்தது.', '(Krishna Priya) Thyroid, sugar, pressure all came under control.'),
 ('V14', 'C0008', 37.80, 40.76, 'எல்லாருமே "இது எனக்கு வேலை செய்யாது"னு நினைச்சாங்க.', 'Everyone thought "this won\'t work for me".'),
 ('T14', 'T_vid_0615', 0.02, 3.50, 'வணக்கம், என் பெயர் ஜோசப் ராஜ். வயசு 62 ஆகுது.', '(Joseph Raj) I am Joseph Raj, 62.'),
 ('T14b', 'T_vid_0615', 29.93, 33.45, 'இப்ப நானும் என் family-யும் healthy-ஆ, happy-ஆ இருக்கோம்.', '(Joseph Raj) Now my family and I are healthy and happy.'),
 ('V15', 'C0008', 46.95, 51.21, 'ஆனா அந்த மாற்றம் ஆரம்பிச்சது வெறும் மூணே நாள்ல.', 'But that change started in just 3 days.'),
 ('B01', 'T_vid_0608', 15.10, 18.90, 'இங்க day 1 வந்து, எனக்கு நெஞ்செரிச்சல் குறைய ஆரம்பிச்சது.', '(client) From day 1 here, my chest-burning started to reduce.'),
 ('B02', 'T_vid_0610', 21.80, 24.42, 'ரொம்ப active-ஆ, fresh-ஆ feel பண்ண ஆரம்பிச்சேன்.', '(client) I started feeling very active and fresh.'),
 ('V16', 'C0008', 57.66, 59.54, 'மூணு நாள்ல எல்லாம் change ஆயிடுமா?', 'Will everything change in 3 days?'),
 ('V17', 'C0008', 65.16, 66.24, 'அது எப்படி?', 'How?'),
 ('V18', 'C0008', 82.52, 85.40, 'Yes. Change start ஆகுறது possible.', 'Yes. Starting the change is possible.'),
 ('V19', 'C0008', 87.41, 89.20, 'Day 1: habits.', 'Day 1: habits.'),
 ('V20', 'C0008', 103.61, 107.20, 'நீங்க உங்க mobile-ஐ continuous-ஆ பாத்துக்கிட்டு இல்லாம,', 'Instead of watching your mobile continuously,'),
 ('V21', 'C0008', 147.67, 150.54, 'உங்களோட habit pattern-ஐ எப்படி tune பண்றது', 'how to tune your habit pattern'),
 ('V22', 'C0008', 167.11, 171.11, 'hand-hold guidance-ல சொல்லித்தர மாதிரி Day 1 இருக்கப்போகுது.', 'Day 1 is taught like hand-hold guidance.'),
 ('V23', 'C0008', 247.40, 254.01, 'உங்க health உங்களுக்கு மட்டும் இல்லாம, உங்க மொத்த family-யும் எப்படி healthy-ஆ இருக்கலாம்ங்கிறத நாங்க சொல்லித்தரப்போறோம்.', 'Day 2: not just you - how your whole family can be healthy.'),
 ('V24', 'C0008', 268.56, 272.19, 'Day 3, இது ரொம்ப important. Family happiness.', 'Day 3 is very important: family happiness.'),
 ('V25', 'C0008', 359.76, 366.00, 'அந்த happiness உங்க வீட்டுக்குள்ள வரணும்னா, நீங்களும் உங்க family-யும் என்ன routine follow பண்ணணும்ங்கிறதை,', 'For happiness to come home, what routine you and your family must follow,'),
 ('V26', 'C0008', 371.16, 375.63, 'எப்படி அந்த happiness-ஐ வீட்டுக்குள்ள கொண்டு வரணும்ங்கிறதையும் சொல்லித்தரப்போறோம்.', 'and how to bring that happiness home - we will teach that too.'),
 ('V27', 'C0008', 385.11, 390.06, 'இதோட financial independence-க்கான first step நீங்க எடுக்கப்போறீங்க.', 'With this, your first step towards financial independence.'),
 ('V28', 'C0008', 437.49, 441.46, 'இத்தனை secrets-உம் நாங்க just ₹555-க்கு கொடுக்கப்போறோம்.', 'All these secrets for just Rs 555.'),
 ('V29', 'C0008', 482.76, 489.34, '3 நாள் live-ஆ attend பண்ணிட்டு value-வே கிடைக்கலைன்னு நினைச்சீங்கன்னா, 100% money back.', 'Attend 3 days live; if you feel no value, 100% money back.'),
 ('V30', 'C0008', 491.60, 492.85, 'Risk முழுசா என் பக்கம்.', 'The risk is fully on my side.'),
 ('V31', 'C0008', 498.99, 503.35, 'ஆனா இந்த batch-க்கு Trichy-ல இருந்து வெறும் 5 couples மட்டும்தான்.', 'But for this batch, only 5 couples from Trichy.'),
 ('V32', 'C0008', 505.35, 507.74, 'நானே personal-ஆ train பண்ணப்போறேன்.', 'I will train them personally.'),
 ('V33', 'C0008', 513.99, 518.84, 'கீழே இருக்கிற button-ஐ click பண்ணி, உங்க family-ஓட இந்த journey-ஐ start பண்ணுங்க.', 'Click the button below and start this journey with your family.'),
]
