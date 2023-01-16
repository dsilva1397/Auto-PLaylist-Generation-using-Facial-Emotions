from Face_Emotion_run import avr_emotion, detect_emo, top2emo
from Song_Mood import Recommend_Songs
from SoundCloud import Play_Songs


# Start Face-Emotion Detection.1
detected_emotions = detect_emo()
emo = avr_emotion(detected_emotions)

# Extract Emotions
maxemo, max2emo = top2emo(emo)
print(emo,'\n',maxemo,max2emo)

# Recommend Songs
songs=Recommend_Songs(maxemo,max2emo)
# songs=Recommend_Songs('Sad',"Angry")
print('\n',"---------------------------------------------------------")
print('Songs Recommended:')
print(songs)

# Start SoundCloud
print('\n',"---------------------------------------------------------")
Play_Songs(songs,0)