# Auto-PLaylist-Generation-using-Facial-Emotions
A Thesis project for my Masters in AI in which I will try to analyse an individuals / groups facial emotion into 3 main categories and provide songs according to that.

#############################################################################################################################################################################################

Here we will use Vision Based Techinque that will be our input to a Deep-Learning Model.
This is a Classification Project, hence we wont measure the intensity of the emotion but just classify the Emotion.
We will classify our input as 7 classes -> Fear, Angry, Neutral, Disgust, Surprised, Sad and Happy.

FER 2013 -> Dataset by Google can be found at: https://www.kaggle.com/datasets/msambare/fer2013


##############################################################################

Problems in this Dataset:
Imbalance, Intra-Class Variation, Occulsion, Contrast Variation, Eyeglass, Outliers.


#############################################################################################################################################################################################

Folder Structure:
Here I have a Root Folder -> Auto-Playlist-Generation-Using-Facial-Emotions.
Followed by the Dataset Folder -> Archive
This Folder has -> Training and Test
For simplicity i have changed the emotion label to numbers as follows:
    0-> Angry
    1-> Disgust
    2-> Fear
    3-> Happy
    4-> Neutral
    5-> Sad
    6-> Surprised
