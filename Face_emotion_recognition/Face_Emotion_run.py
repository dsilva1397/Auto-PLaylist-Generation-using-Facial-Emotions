import numpy as np
from keras.models import load_model
import cv2
from keras.preprocessing import image
from tensorflow.keras.utils import img_to_array
from time import sleep
import time


def avr_emotion(detected_emotions):

    emotion_dict = { 
        'Fear': 0,
        'Neutral':0,
        'Happy':0,
        'Sad':0,
        'Disgust':0,
        'Angry':0,
        'Surprised':0
    }

    for emotion in detected_emotions:
        if emotion == 'Neutral':
            emotion_dict['Neutral'] +=1
        elif emotion == 'Fear':
            emotion_dict['Fear'] +=1
        elif emotion =='Sad':
            emotion_dict['Sad'] +=1
        elif emotion == 'Happy':
            emotion_dict['Happy'] +=1
        elif emotion =='Disgust':
            emotion_dict['Disgust'] +=1
        elif emotion == 'Angry':
            emotion_dict['Angry'] +=1
        elif emotion =='Surprise':
            emotion_dict['Surprised'] +=1
    return(emotion_dict)

face_classifier = cv2.CascadeClassifier(r'Face_emotion_recognition/haarcascade_frontalface_default.xml')
classifier =load_model(r'Face_emotion_recognition/model.h5')


emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)
now = time.time()
future = now + 10
detected_emotions = []

def detect_emo():
    while True:
        _, frame = cap.read()
        labels = []
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        faces = face_classifier.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)



            if np.sum([roi_gray])!=0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)

                prediction = classifier.predict(roi)[0]
                label=emotion_labels[prediction.argmax()]
                label_position = (x,y-10)
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                detected_emotions.append(label)
            else:
                cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow('Emotion Detector',cv2.resize(frame,(1600,960),interpolation = cv2.INTER_CUBIC))
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break

        # if time.time() > future:  ##after 10 second music will play
        #         cv2.destroyAllWindows()
        #         print("Music Player Opens", time)
        #         future = time.time() + 10
    cap.release()
    cv2.destroyAllWindows()

    return(detected_emotions)

def top2emo(emo):
    # emo=avr_emotion(detected_emotions)
    max_count = max(emo.values())
    max_emo = max(emo, key=emo.get)

    max2 = 0
    for feeling, v in emo.items():
        if(v>max2 and v<max_count):
            max2 = v
            max2_emo = feeling
    
    # Handling if there is just one major emotion.
    if max2 == 0:
        max2_emo = 'Neutral'

    # Handling if 1st Emotion is Neutral
    if max_emo == 'Neutral':
        temp = max2_emo
        max2_emo = max_emo
        max_emo = temp

    

    return(max_emo, max2_emo)
