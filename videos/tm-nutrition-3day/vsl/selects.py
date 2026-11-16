"""VSL selects: best take of each line, in story order.
Times are seconds in the working copies (C0007L.mp4 / C0008L.mp4 = rotated/scaled copies of the Sony originals, same timing).
Text is the cleaned line as spoken (Whisper large-v3, checked against the script doc and re-transcribed in short windows).
('bite', ...) rows are real testimonial clips played WITH their own audio (proof). Everything else is the coach on camera.
"""
SEL = [
 # id      file     a       b       spoken (cleaned)                                                                 meaning
 ('L01', 'C0007', 46.30, 50.80, 'உங்க வீட்டுல ரெண்டு பேரும் weight குறைக்கணும்னு எத்தனை தடவை முடிவு பண்ணியிருப்பீங்க?', 'How many times have the two of you decided to lose weight?'),
 ('L02', 'C0007', 55.10, 59.85, 'இந்த video-வ முழுசா பாருங்க. உங்க family-க்கான answer இந்த video-ல இருக்கு.', 'Watch this video fully. The answer for your family is in it.'),
 ('L03', 'C0007', 74.50, 78.95, 'Hi, நான் Coach Pradheesh பேசுறேன். TM Nutrition Centre, Trichy.', 'Hi, I am Coach Pradheesh, TM Nutrition Centre, Trichy.'),
 ('L04', 'C0007', 101.30, 105.30, '18 வருஷமா நூற்றுக்கணக்கான families-ஐ healthy-ஆ மாத்தியிருக்கோம்.', 'For 18 years we have made hundreds of families healthy. (CONFIRM 18 years)'),
 ('L05', 'C0007', 114.40, 117.55, 'இப்போ ஒரு புது batch, couples-க்கு மட்டும்.', 'Now a new batch, only for couples.'),
 ('L06', 'C0007', 136.70, 139.55, 'மூணு நாள் diet... அப்புறம் biryani.', 'Three days of diet... then biryani.'),
 ('L07', 'C0007', 145.85, 149.75, 'Gym membership கட்டி, முழுசா ரெண்டு வாரம் கூட போறது இல்ல.', 'Pay for a gym membership, and not go even two full weeks.'),
 ('L08', 'C0007', 153.80, 157.35, 'ராத்திரி பன்னெண்டு மணி வரைக்கும் கையில mobile.', 'Mobile in hand till midnight.'),
 ('L09', 'C0007', 162.40, 167.38, '"நாளைக்கு ஆரம்பிச்சுக்கலாம்"னு ரெண்டு பேரும் ஒருவருக்கொருவர் சமாதானப்படுத்திப்பீங்க.', '"Let\'s start tomorrow" - you both reassure each other.'),
 ('L10', 'C0007', 197.75, 201.95, 'Problem உங்க will power-ல இல்ல. உங்க வீட்டோட pattern-ல இருக்கு.', 'The problem is not your willpower. It is in your home\'s pattern.'),
 ('L11', 'C0007', 210.85, 212.70, 'இவரு 58 வயசு.', 'He is 58.'),
 ('L12', 'C0008', 25.70, 30.32, 'இவரு Erode-லருந்து, 32 வயசு. 26 kg excess weight.', 'He is from Erode, 32. 26 kg excess weight.'),
 ('L13', 'C0007', 321.90, 325.35, 'இவங்க 48 வயசு.', 'She is 48.'),
 ('L14', 'C0008', 37.60, 40.70, 'எல்லாருமே "இது எனக்கு வேலை செய்யாது"னு நினைச்சாங்க.', 'Everyone thought "this won\'t work for me".'),
 ('L15', 'C0008', 47.30, 51.05, 'ஆனா அந்த மாற்றம் ஆரம்பிச்சது வெறும் 3 நாள்ல.', 'But that change started in just 3 days.'),
 ('B01', 'T_vid_0608', 15.10, 18.90, 'இங்க day 1 வந்து, எனக்கு நெஞ்செரிச்சல் குறைய ஆரம்பிச்சது.', '(client) From day 1 here, my chest-burning started to reduce.'),
 ('B02', 'T_vid_0610', 21.80, 24.05, 'ரொம்ப active-ஆ, fresh-ஆ feel பண்ண ஆரம்பிச்சேன்.', '(client) I started feeling very active and fresh.'),
 ('L16', 'C0008', 57.30, 59.25, '3 நாள்ல எல்லாம் change ஆயிடுமா?', 'Will everything change in 3 days?'),
 ('L17', 'C0008', 60.95, 62.05, 'அது எப்படி?', 'How?'),
 ('L18', 'C0008', 82.08, 84.98, 'Yes. Change start ஆகுறது possible.', 'Yes. Starting the change is possible.'),
 ('L19', 'C0008', 87.10, 88.95, 'Day 1: Habits.', 'Day 1: Habits.'),
 ('L20', 'C0008', 88.90, 94.40, 'Day 1-ல நீங்க உங்க mobile-ஐ continuous-ஆ பாத்துக்கிட்டு இல்லாம,', 'On Day 1, instead of watching your mobile continuously,'),
 ('L21', 'C0008', 147.50, 150.50, 'உங்களோட habit pattern-ஐ எப்படி tune பண்றதுன்னு', 'how to tune your habit pattern'),
 ('L22', 'C0008', 150.40, 154.10, 'hand-hold guidance-ல சொல்லித்தர மாதிரி', 'taught like hand-hold guidance'),
 ('L23', 'C0008', 165.10, 166.90, 'Day 1 இருக்கப்போகுது.', 'is how Day 1 will be.'),
 ('L24', 'C0008', 172.90, 174.80, 'Day 2: Family health.', 'Day 2: Family health.'),
 ('L25', 'C0008', 210.30, 218.80, 'உங்க health உங்களுக்கு மட்டும் இல்லாம, உங்க மொத்த family-யும் எப்படி healthy-ஆ இருக்கப்போறீங்கன்னு நாங்க சொல்லித்தரப்போறோம்.', 'Not just your health - we will teach how your whole family will be healthy.'),
 ('L26', 'C0008', 254.60, 256.70, 'Day 3: Family happiness.', 'Day 3: Family happiness.'),
 ('L27', 'C0008', 263.40, 267.00, 'Day 3 ரொம்ப important.', 'Day 3 is very important.'),
 ('L28', 'C0008', 358.40, 367.95, 'அந்த happiness உங்க வீட்டுக்குள்ள வரணும்னா, நீங்களும் உங்க family-யும் என்ன routine follow பண்ணணும்,', 'For that happiness to come into your home, what routine you and your family must follow,'),
 ('L29', 'C0008', 367.00, 368.10, '+ ', '(joins L28 to L30: "எப்படி அந்த happiness")'),
 ('L30', 'C0008', 373.05, 375.25, 'எப்படி அந்த happiness-ஐ வீட்டுக்குள்ள கொண்டு வரணும்ங்கிறதையும் சொல்லப்போறோம்.', 'and how to bring that happiness home - we will tell you that too.'),
 ('L31', 'C0008', 385.40, 389.90, 'இதோட financial independence-க்கான first step நீங்க எடுக்கப் போறீங்க.', 'With this, you will take your first step towards financial independence.'),
 ('L32', 'C0008', 387.05, 389.60, 'first step நீங்க எடுக்கப் போறீங்க.', 'you will take your first step.'),
 ('L33', 'C0008', 437.40, 441.30, 'இத்தனை secrets-உம் நாங்க just ₹555-க்கு கொடுக்கப்போறோம்.', 'All these secrets, we are giving for just Rs 555.'),
 ('L34', 'C0008', 482.90, 489.10, '3 நாள் live-ஆ attend பண்ணிட்டு உங்களுக்கு value-வே கிடைக்கலைன்னு நினைச்சீங்கன்னா, 100% money back.', 'Attend the 3 days live and if you feel you got no value, 100% money back.'),
 ('L35', 'C0008', 489.10, 491.60, 'Risk முழுசா என் பக்கம்.', 'The risk is fully on my side.'),
 ('L36', 'C0008', 583.60, 589.85, 'ஆனா இந்த batch-க்கு Trichy-லருந்து வெறும் 5 couples-தான் நானே personal-ஆ train பண்ணப்போறேன்.', 'But for this batch I will personally train only 5 couples from Trichy.'),
 ('L37', 'C0008', 603.40, 608.15, 'கீழே இருக்கும் button-ஐ click பண்ணி, family-ஓட இந்த journey-ஐ start பண்ணுங்க.', 'Click the button below and start this journey with your family.'),
]
# L29 is a bridge: L28 ends on "follow பண்ணணும்" (365.5) and "எப்படி அந்த happiness" (365.98-367.9) sits before a 5 s pause; drop L29, keep L28 to 367.95.
# L27 ("Day 3 ரொம்ப important") has a 1.4 s mid-line pause in every take, and L32 is covered by the complete L31 take.
SEL = [s for s in SEL if s[0] not in ('L29', 'L27', 'L32')]
