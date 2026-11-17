"""Meta ads (9:16): coach-only takes per line (face tracking + coach-only transcription), rough word-timed ranges.
voice_id.py (SELECTS=selects_meta) then trims every take to the silent gap after/before the prompter's voice.
Times = seconds in the portrait working copies C000xP.mp4 (same timing as the Sony originals).
Ad 2 and Ad 3 end with Ad 1's offer section, as the coach instructed on camera ("Ad script 1-லிருந்து எடுத்து போட்டுக்கோங்க")."""
TAIL = [  # shared: challenge -> 3 days -> offer -> CTA (from C0001)
 ('A15', 'C0001', 178.05, 181.25, 'அதுக்காகத்தான் இந்த 3 days couple transformation challenge.', "That's why this 3-day couple transformation challenge."),
 ('A16', 'C0001', 191.40, 194.60, 'மூணு நாள்ல உங்க family-க்குள்ள ஒரு மாற்றம் வருமா?', 'Can a change come into your family in 3 days?'),
 ('A17', 'C0001', 195.75, 197.70, 'Yes, அது possible.', 'Yes, it is possible.'),
 ('A18', 'C0001', 201.38, 202.45, 'Day 1:', 'Day 1:'),
 ('A19', 'C0001', 205.85, 208.55, 'உங்க mobile-ஐ continuous-ஆ பாத்துக்கிட்டு இல்லாம,', 'instead of watching your mobile continuously,'),
 ('A20', 'C0001', 227.10, 229.80, 'உங்க habit pattern-ஐ tune பண்றது எப்படி.', 'how to tune your habit pattern.'),
 ('A21', 'C0001', 274.35, 279.30, 'Day 2: நீங்க மட்டும் இல்ல, உங்க whole family-யும் healthy-ஆ இருக்கிறது எப்படி.', 'Day 2: not just you - how your whole family stays healthy.'),
 ('A22', 'C0001', 297.50, 301.80, 'Day 3: உங்க family-க்குள்ள happiness கொண்டு வர routine எப்படி.', 'Day 3: the routine that brings happiness into your family.'),
 ('A23', 'C0001', 335.70, 339.48, 'Plus, financial independence achieve பண்றது எப்படிங்கிற roadmap session.', 'Plus a roadmap session on achieving financial independence.'),
 ('A24', 'C0001', 379.00, 381.15, 'இதுக்கு just ₹555 மட்டும்தான்.', 'All this for just Rs 555.'),
 ('A25', 'C0001', 437.55, 442.85, 'இந்த 3 days session live-ஆ attend பண்ணிட்டு உங்களுக்கு value-வே கிடைக்கலைன்னு நினைச்சீங்கன்னா,', 'Attend the 3-day live sessions; if you feel you got no value,'),
 ('A26', 'C0001', 445.95, 447.60, '100% money back.', '100% money back.'),
 ('A27', 'C0001', 456.05, 457.75, 'Risk முழுசா என் பக்கம்.', 'The risk is fully on me.'),
 ('A28', 'C0001', 465.50, 469.50, 'ஆனா Trichy-ல இந்த batch-க்கு 5 couples மட்டும்தான்.', 'But only 5 couples in Trichy for this batch.'),
 ('A29', 'C0001', 471.80, 474.05, 'நானே personal-ஆ train பண்ணப்போறேன்.', 'I will train them personally.'),
 ('A30', 'C0001', 476.80, 479.60, 'அந்த lucky couples நீங்களா இருக்கணும்னா,', 'If you want to be those lucky couples,'),
 ('A31', 'C0001', 481.75, 485.10, 'கீழ இருக்கிற link-ஐ click பண்ணி இப்பவே register பண்ணுங்க.', 'click the link below and register now.'),
]
TRIO = [  # habits / routine / happiness (C0001)
 ('A11', 'C0001', 114.20, 116.15, 'உங்களோட daily habits,', 'your daily habits,'),
 ('A12', 'C0001', 116.90, 118.60, 'உங்க family routine,', 'your family routine,'),
 ('A13', 'C0001', 120.30, 122.10, 'வீட்டுல இருக்கிற happiness,', 'the happiness at home -'),
]
AD1 = [
 ('A01', 'C0001', 30.62, 33.92, 'இவங்கதான் வேதாரண்யத்துல இருந்து கிருத்திகா & ஆனந்த்.', 'These are Kirthika and Anand from Vedaranyam.'),
 ('A02', 'C0001', 36.35, 40.65, 'இவங்க ரெண்டு பேரும் தனித்தனியா இல்ல, சேர்ந்தே மாறினாங்க.', 'They did not change separately - they changed together.'),
 ('A03', 'C0001', 44.10, 47.45, 'இவங்கள மாதிரியே நீங்களும் couple-ஆ weight குறைக்கணும்னு நினைச்சீங்கன்னா,', 'If you also want to lose weight as a couple like them,'),
 ('A04', 'C0001', 49.10, 51.30, 'உங்களுக்கு மூணு problem வரும்.', 'you will face three problems.'),
 ('A05', 'C0001', 52.55, 55.60, 'Diet consistent-ஆ follow பண்ண முடியாது.', 'You cannot follow a diet consistently.'),
 ('A06', 'C0001', 57.05, 59.15, 'Gym-க்கு நேரம் இருக்காது.', 'No time for the gym.'),
 ('A07', 'C0001', 71.15, 75.55, 'அப்புறம் "நாளைக்கு ஆரம்பிக்கலாம்"னு ஒருத்தருக்கொருத்தர் சமாதானப்படுத்திப்பீங்க.', 'And you reassure each other "let\'s start tomorrow".'),
 ('A08', 'C0001', 78.35, 79.90, 'ஆனா உண்மை என்ன தெரியுமா?', 'But do you know the truth?'),
 ('A09', 'C0001', 90.45, 92.55, 'Problem diet-ல இல்ல.', 'The problem is not the diet.'),
 ('A10', 'C0001', 95.35, 97.15, 'உங்க daily habits-ல இருக்கு.', 'It is in your daily habits.'),
] + TRIO + [
 ('A14', 'C0001', 123.25, 127.35, 'இது மூணும் ஒண்ணோட ஒண்ணு connected-ஆவே இருக்கும்.', 'All three are connected to each other.'),
] + TAIL
AD2 = [
 ('B01', 'C0002', 27.75, 31.70, 'நிறைய couples weight loss-ல fail ஆகுறதுக்கு காரணம் diet இல்ல.', 'Many couples fail at weight loss - and the reason is not the diet.'),
 ('B02', 'C0002', 41.65, 43.20, 'மூணு நாள் diet...', 'Three days of diet...'),
 ('B03', 'C0002', 44.10, 46.00, 'அப்புறம் biryani.', 'then biryani.'),
 ('B04', 'C0002', 50.75, 54.45, 'Gym membership கட்டி, முழுசா ரெண்டு வாரம் கூட போறது இல்ல.', 'Pay for the gym, never go even two full weeks.'),
 ('B05', 'C0002', 79.50, 81.65, '"நீ முதல்ல ஆரம்பி, அப்புறம் நான் வரேன்."', '"You start first, I\'ll join later."'),
 ('B06', 'C0002', 86.65, 89.25, 'கடைசில ரெண்டு பேருமே ஆரம்பிக்கிறது இல்ல.', 'In the end, neither of you starts.'),
 ('B07', 'C0002', 93.55, 95.40, 'இவர்தான் ஜோசப் ராஜ்.', 'This is Joseph Raj.'),
 ('B08', 'C0002', 96.45, 98.70, 'வயசு 62.', 'Age 62.'),
 ('B09', 'C0002', 117.20, 119.90, '"இந்த வயசுல என்ன மாறப்போகுது"ன்னு நினைச்சாரு.', 'He thought "what will change at this age?"'),
 ('B10', 'C0002', 145.55, 149.10, 'இப்போ ideal weight touch பண்ணி, healthy-ஆ, fit-ஆ இருக்காரு.', 'Now he has touched his ideal weight - healthy and fit.'),
 ('B11', 'C0002', 154.00, 157.20, '62 வயசுல முடியும்னா, உங்களுக்கு என்ன காரணம்?', 'If it is possible at 62, what is your excuse?'),
 ('B12', 'C0002', 161.35, 162.95, 'Weight மட்டும் problem இல்ல.', 'Weight is not the only problem.'),
] + TRIO + [
 ('B14', 'C0002', 173.65, 177.70, 'இது மூணும் சேர்ந்தா மட்டும்தான் couples ஜெயிக்க முடியும்.', 'Only when all three come together can couples win.'),
] + TAIL
AD3 = [
 ('C01', 'C0003', 5.90, 8.30, 'இந்த apple-ஐ catch பண்றது ரொம்ப easy.', 'Catching this apple is very easy.'),
 ('C02', 'C0003', 58.10, 62.20, 'ஆனா 25 kilo குறைக்கிறது, அதுவும் possible தான்.', 'But losing 25 kilos - that is possible too.'),
 ('C03', 'C0003', 68.30, 69.85, 'இவர்தான் ஜோன்ஸ்.', 'This is Jones.'),
 ('C04', 'C0003', 147.55, 153.60, '92 kilo-லருந்து 67 kilo. 25 kilo குறைச்சது diet-னால மட்டும் இல்ல.', '92 kg to 67 kg. 25 kg lost - not by diet alone.'),
 ('C05', 'C0003', 154.55, 156.60, 'Habits மாறினதனால.', 'Because his habits changed.'),
 ('C06', 'C0003', 169.45, 172.05, 'நம்ம வீட்டுல problem சாப்பாடு மட்டும் இல்ல.', 'At home, the problem is not just food.'),
 ('C07', 'C0003', 175.50, 177.10, 'கையில எப்பவும் mobile.', 'Phone always in hand.'),
 ('C08', 'C0003', 177.85, 179.45, 'Late night-ல dinner.', 'Late-night dinner.'),
 ('C09', 'C0003', 180.60, 181.85, 'சரியா தூங்குறது இல்ல.', 'No proper sleep.'),
 ('C10', 'C0003', 183.40, 184.70, 'Walking இல்ல.', 'No walking.'),
 ('C11', 'C0003', 189.10, 192.70, 'வீட்டுல ரெண்டு பேரும் அதே pattern-ல மாட்டிக்கிட்டு இருக்கீங்க.', 'Both of you are stuck in the same pattern at home.'),
] + TAIL
ADS = {'ad1_kirthika_anand': AD1, 'ad2_joseph_raj': AD2, 'ad3_jones_92_67': AD3}
SEL = []   # unique takes for voice_id.py
for ad in ADS.values():
    for t in ad:
        if t[0] not in [s[0] for s in SEL]: SEL.append(t)
