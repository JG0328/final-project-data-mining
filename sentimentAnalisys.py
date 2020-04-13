import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score 
import numpy as np 
import copy 


df=pd.read_csv("final1.csv")


vectorizer = TfidfVectorizer(use_idf=True, strip_accents='ascii')

tweets = vectorizer.fit_transform(df.text.values.astype('U'))
sentiments = df.sentiment_label

tweets_train, tweets_test, sentiment_train, sentiment_test = train_test_split(tweets, sentiments, test_size=0.3, train_size=0.7, random_state=100) 

classifier = naive_bayes.MultinomialNB()
classifier.fit(tweets_train, sentiment_train)


tweet = np.array(["tune two funniest sports presenters best sports entertainment hbd corona day r g g kussh", "yogi children lessor god barbarism yogi government disgusting people need quarantine amp treatment infected"])

vector = vectorizer.transform(tweet)

print(classifier.predict(vector))






'''

def buildVocabulary(preprocessedTrainingData):
    all_words = []
    for tweet in preprocessedTrainingData:
        all_words.extend(tweet["text"])
    wordlist = nltk.FreqDist(all_words)
    return wordlist.keys()

def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)
    return features 


dictionary = []

with open('final.json', encoding='utf-8') as handle:
    dictionary = json.loads(handle.read())

word_features = buildVocabulary(dictionary)

preprocessedTrainingData = []
for tweet in dictionary:
    preprocessedTrainingData.append((tweet["text"], tweet["sentiment_label"]))

trainingFeatures = nltk.classify.apply_features(extract_features, preprocessedTrainingData)
print(trainingFeatures)
'''