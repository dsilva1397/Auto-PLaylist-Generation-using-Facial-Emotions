# imports
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import  GaussianNB 
from sklearn.linear_model import  LogisticRegression 
from sklearn import svm
from sklearn import linear_model
from sklearn import tree

from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, recall_score
from numpy import mean
# from sklearn import preprocessing

import warnings
warnings.filterwarnings("ignore")


def Recommend_Songs(primary_emo, secondary_emo):

    # {'Fear', 'Neutral', 'Happy':, 'Sad':, 'Disgust':, 'Angry':, 'Surprised':}

    # {'Calm','Happy','Energetic','Sad'}
    
    # Fear
    if( primary_emo=='Fear' and secondary_emo =='Neutral'):

        Play = music_player[music_player['mood'] =='Calm' ]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Fear' and secondary_emo =='Happy'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)


    if( primary_emo=='Fear' and secondary_emo =='Sad'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Fear' and secondary_emo =='Disgust'):
        Play= music_player.loc[(music_player['mood'] =='Happy') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Fear' and secondary_emo =='Angry'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Sad')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Fear' and secondary_emo =='Surprised'):
        Play= music_player.loc[(music_player['mood'] =='Happy') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)


    # Happy

    if( primary_emo=='Happy' and secondary_emo =='Neutral'):
        Play = music_player[music_player['mood'] =='Energetic' ]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Happy' and secondary_emo =='Fear'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Happy' and secondary_emo =='Sad'):
        Play= music_player.loc[(music_player['mood'] =='Happy') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Happy' and secondary_emo =='Disgust'):
        Play= music_player.loc[(music_player['mood'] =='Happy') & (music_player['SE']=='Calm')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Happy' and secondary_emo =='Angry'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Happy' and secondary_emo =='Surprised'):
        Play= music_player.loc[(music_player['mood'] =='Happy') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)


    
    # Sad
    if( primary_emo=='Sad' and secondary_emo =='Neutral'):
        Play = music_player[music_player['mood'] =='Calm' ]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Sad' and secondary_emo =='Fear'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Sad' and secondary_emo =='Happy'):
        Play= music_player.loc[(music_player['mood'] =='Happy') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Sad' and secondary_emo =='Disgust'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Sad' and secondary_emo =='Angry'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Sad' and secondary_emo =='Surprised'):
        Play= music_player.loc[(music_player['mood'] =='Sad') & (music_player['SE']=='Calm')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)


    # Disgust
    if( primary_emo=='Disgust' and secondary_emo =='Neutral'):
        Play = music_player[music_player['mood'] =='Calm' ]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Disgust' and secondary_emo =='Fear'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Disgust' and secondary_emo =='Happy'):
        Play= music_player.loc[(music_player['mood'] =='Happy') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Disgust' and secondary_emo =='Sad'):
        Play= music_player.loc[(music_player['mood'] =='Happy') & (music_player['SE']=='Calm')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Disgust' and secondary_emo =='Angry'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Disgust' and secondary_emo =='Surprised'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)


    # Angry
    if( primary_emo=='Angry' and secondary_emo =='Neutral'):
        Play = music_player[music_player['mood'] =='Calm' ]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Angry' and secondary_emo =='Fear'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Sad')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Angry' and secondary_emo =='Happy'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Angry' and secondary_emo =='Sad'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Sad')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Angry' and secondary_emo =='Disgust'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Angry' and secondary_emo =='Surprised'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

        
    # Surprised
    if( primary_emo=='Surprised' and secondary_emo =='Neutral'):
        Play = music_player[music_player['mood'] =='Surprised' ]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Surprised' and secondary_emo =='Fear'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Surprised' and secondary_emo =='Happy'):
        Play= music_player.loc[(music_player['mood'] =='Happy') & (music_player['SE']=='Energetic')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Surprised' and secondary_emo =='Sad'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Sad')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Surprised' and secondary_emo =='Disgust'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    if( primary_emo=='Surprised' and secondary_emo =='Angry'):
        Play= music_player.loc[(music_player['mood'] =='Calm') & (music_player['SE']=='Happy')]
        Play = Play.sort_values(by="popularity", ascending=False)
        Play = Play[:5].reset_index(drop=True)

    return(Play['name'].tolist())

df = pd.read_csv('Face_emotion_recognition/data_moods.csv')
df = df.drop(['release_date', 'album','length'], axis = 1)
music_player = df[['name', 'artist', 'mood', 'popularity']]
df.insert(0, 'id_', range(1, 1 + len(df)))
    
X = df.drop(['mood','artist','name','id'], axis = 1)
y = df['mood']

# print(X.head(),'\n\n',y.head())

gnb = GaussianNB()
LR = LogisticRegression()
SVC = svm.SVC()
DT = tree.DecisionTreeClassifier()



acc=[]
acc1=[]
acc_SVC=[]
acc_DT = []
for r in range(100):
  X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.5)

  gnb.fit(X_train, y_train)
  LR.fit(X_train, y_train)
  SVC.fit(X_train, y_train)
  DT.fit(X_train, y_train)

  y_pred = gnb.predict(X_test)
  y_pred1= LR.predict(X_test)
  y_predSVC = SVC.predict(X_test)
  y_predDT = DT.predict(X_test)

  actual=y_test
  prediction=y_pred
  prediction1=y_pred1
  predSVC = y_predSVC
  predDT = y_predDT
  
  accuracy=accuracy_score(actual,prediction) 
  accuracy1=accuracy_score(actual,prediction1) 
  accSVC =accuracy_score(actual,predSVC) 
  accDT = accuracy_score(actual,predDT) 
  acc.append(accuracy)
  acc1.append(accuracy1)
  acc_SVC.append(accSVC)
  acc_DT.append(accDT)
print("GNB={}, LR={}, SVC={}, DT={}".format(mean(acc), mean(acc1), mean(acc_SVC),mean(acc_DT)))

# X_input=X.tail(5)
# print(gnb.predict(X_input))
# print(y.tail(5))

second_emo = gnb.predict(X)
df.insert(0, 'SE', second_emo)

songs = Recommend_Songs('Sad',"Neutral")
print(songs)