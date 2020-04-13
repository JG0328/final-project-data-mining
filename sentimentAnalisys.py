import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import accuracy_score 
import numpy as np 
import copy 
import json

df=pd.read_csv("final1.csv")


vectorizer = TfidfVectorizer(use_idf=True, strip_accents='ascii')

tweets = vectorizer.fit_transform(df.text.values.astype('U'))
sentiments = df.sentiment_label

tweets_train, tweets_test, sentiment_train, sentiment_test = train_test_split(tweets, sentiments, test_size=0.3, train_size=0.7, random_state=100) 

classifier = naive_bayes.MultinomialNB()
classifier.fit(tweets_train, sentiment_train)

sentiment_predicted = classifier.predict(tweets_test)

data = []
for text, sentiment in zip(tweets_test, sentiment_predicted):
    print(text)
    data.append({"sentiment": sentiment })


with open('predicted.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)




print(accuracy_score(sentiment_test, sentiment_predicted))





#tweet = np.array(["criminals getting bailed jail since years due corona concern innocent sant still jail since years even years old s time", "yogi children lessor god barbarism yogi government disgusting people need quarantine amp treatment infected"])
#vector = vectorizer.transform(tweet)
#print(classifier.predict(vector))



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