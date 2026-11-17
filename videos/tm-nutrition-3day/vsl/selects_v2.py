"""VSL v2 selects: only the COACH speaking (face tracking: mouth moving + voice), never the off-camera prompter.
How these were chosen (scripts/face_track.py -> who_speaks.py -> transcribe_client.py):
  * the prompter reads each line first, the coach repeats it; prompter lines have voice but no mouth movement and are dropped
  * every take below is a stretch where the coach's mouth moves, transcribed on its own, matched to the script
  * trimmed on word timings to drop "okay வா", repeats and chatter
Times are seconds in the working copies (C0007L.mp4 / C0008L.mp4)."""
SEL = [
 # id     file    a       b       spoken by the coach (cleaned)                                                         meaning
 ('V01', 'C0007', 45.50, 50.75, 'உங்க வீட்டுல ரெண்டு பேரும் weight குறைக்கணும்னு எத்தனை தடவை முடிவு பண்ணியிருப்பீங்க?', 'How many times have you both decided to lose weight?'),
 ('V02', 'C0007', 55.45, 59.65, 'இந்த video-வ முழுசா பாருங்க. உங்க family-க்கான answer இந்த video-ல இருக்கு.', 'Watch fully - the answer for your family is in this video.'),
 ('V03', 'C0007', 75.40, 78.95, 'Hi, நான் Coach Pradheesh பேசுறேன். TM Nutrition Centre, Trichy.', 'Hi, I am Coach Pradheesh, TM Nutrition Centre, Trichy.'),
 ('V04', 'C0007', 101.35, 105.30, '18 வருஷமா நூற்றுக்கணக்கான families-ஐ healthy-ஆ மாத்தியிருக்கோம்.', '18 years, hundreds of families made healthy. (CONFIRM)'),
 ('V05', 'C0007', 109.40, 111.90, 'இப்போ புது batch, couples-க்கு மட்டும்.', 'Now a new batch, only for couples.'),
 ('V06', 'C0007', 139.95, 142.15, 'மூணு நாள் diet... அப்புறம் biryani.', 'Three days of diet... then biryani.'),
 ('V07', 'C0007', 146.10, 149.60, 'Gym membership கட்டி, முழுசா ரெண்டு வாரம் கூட போறது இல்ல.', 'Pay for the gym, never go even two full weeks.'),
 ('V08', 'C0007', 154.40, 157.30, 'ராத்திரி 12 மணி வரைக்கும் கையில mobile.', 'Mobile in hand till midnight.'),
 ('V09', 'C0007', 162.80, 167.55, '"நாளைக்கு ஆரம்பிச்சுக்கலாம்"னு ரெண்டு பேரும் ஒருவருக்கொருவர் சமாதானப்படுத்திப்பீங்க.', '"Let\'s start tomorrow" - you reassure each other.'),
 ('V10', 'C0007', 202.20, 205.60, 'Problem will power-ல இல்ல. உங்க வீட்டோட pattern-ல இருக்கு.', 'The problem is not willpower. It is your home\'s pattern.'),
 ('V11', 'C0008', 17.10, 18.62, 'இவரு 58 வயசு.', 'He is 58.'),
 ('V12', 'C0008', 26.00, 30.35, 'இவரு Erode-லருந்து, 32 வயசு. 26 kg excess weight.', 'He is from Erode, 32. 26 kg excess weight.'),
 ('V13', 'C0007', 325.70, 327.60, 'இவங்க 48 வயசு.', 'She is 48.'),
 ('V14', 'C0008', 37.95, 40.75, 'எல்லாருமே "இது எனக்கு வேலை செய்யாது"னு நினைச்சாங்க.', 'Everyone thought "this won\'t work for me".'),
 ('V15', 'C0008', 47.25, 50.90, 'ஆனா அந்த மாற்றம் ஆரம்பிச்சது வெறும் மூணே நாள்ல.', 'But that change started in just 3 days.'),
 ('B01', 'T_vid_0608', 15.10, 18.90, 'இங்க day 1 வந்து, எனக்கு நெஞ்செரிச்சல் குறைய ஆரம்பிச்சது.', '(client) From day 1 here, my chest-burning started to reduce.'),
 ('B02', 'T_vid_0610', 21.80, 24.05, 'ரொம்ப active-ஆ, fresh-ஆ feel பண்ண ஆரம்பிச்சேன்.', '(client) I started feeling very active and fresh.'),
 ('V16', 'C0008', 57.20, 59.30, 'மூணு நாள்ல எல்லாம் change ஆயிடுமா?', 'Will everything change in 3 days?'),
 ('V17', 'C0008', 65.40, 66.10, 'அது எப்படி?', 'How?'),
 ('V18', 'C0008', 82.75, 85.10, 'Yes. Change start ஆகுறது possible.', 'Yes. Starting the change is possible.'),
 ('V19', 'C0008', 87.20, 89.10, 'Day 1: habits.', 'Day 1: habits.'),
 ('V20', 'C0008', 103.10, 107.00, 'நீங்க உங்க mobile-ஐ continuous-ஆ பாத்துக்கிட்டு இல்லாம,', 'Instead of watching your mobile continuously,'),
 ('V21', 'C0008', 147.90, 150.25, 'உங்களோட habit pattern-ஐ எப்படி tune பண்றது', 'how to tune your habit pattern'),
 ('V22', 'C0008', 167.35, 170.95, 'hand-hold guidance-ல சொல்லித்தர மாதிரி Day 1 இருக்கப்போகுது.', 'Day 1 is taught like hand-hold guidance.'),
 ('V23', 'C0008', 247.60, 253.75, 'உங்க health உங்களுக்கு மட்டும் இல்லாம, உங்க மொத்த family-யும் எப்படி healthy-ஆ இருக்கலாம்ங்கிறத நாங்க சொல்லித்தரப்போறோம்.', 'Day 2: not just you - how your whole family can be healthy.'),
 ('V24', 'C0008', 268.80, 271.90, 'Day 3, இது ரொம்ப important. Family happiness.', 'Day 3 is very important: family happiness.'),
 ('V25', 'C0008', 360.05, 365.70, 'அந்த happiness உங்க வீட்டுக்குள்ள வரணும்னா, நீங்களும் உங்க family-யும் என்ன routine follow பண்ணணும்ங்கிறதை,', 'For happiness to come home, what routine you and your family must follow,'),
 ('V26', 'C0008', 371.20, 375.40, 'எப்படி அந்த happiness-ஐ வீட்டுக்குள்ள கொண்டு வரணும்ங்கிறதையும் சொல்லித்தரப்போறோம்.', 'and how to bring that happiness home - we will teach that too.'),
 ('V27', 'C0008', 385.40, 389.80, 'இதோட financial independence-க்கான first step நீங்க எடுக்கப்போறீங்க.', 'With this, your first step towards financial independence.'),
 ('V28', 'C0008', 437.65, 441.20, 'இத்தனை secrets-உம் நாங்க just ₹555-க்கு கொடுக்கப்போறோம்.', 'All these secrets for just Rs 555.'),
 ('V29', 'C0008', 483.05, 489.05, '3 நாள் live-ஆ attend பண்ணிட்டு value-வே கிடைக்கலைன்னு நினைச்சீங்கன்னா, 100% money back.', 'Attend 3 days live; if you feel no value, 100% money back.'),
 ('V30', 'C0008', 491.30, 493.15, 'Risk முழுசா என் பக்கம்.', 'The risk is fully on my side.'),
 ('V31', 'C0008', 499.25, 503.50, 'ஆனா இந்த batch-க்கு Trichy-ல இருந்து வெறும் 5 couples மட்டும்தான்.', 'But for this batch, only 5 couples from Trichy.'),
 ('V32', 'C0008', 504.85, 507.65, 'நானே personal-ஆ train பண்ணப்போறேன்.', 'I will train them personally.'),
 ('V33', 'C0008', 514.15, 518.75, 'கீழே இருக்கிற button-ஐ click பண்ணி, உங்க family-ஓட இந்த journey-ஐ start பண்ணுங்க.', 'Click the button below and start this journey with your family.'),
]
