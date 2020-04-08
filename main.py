import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


def preProcessString(inputString):
    inputString = deEmojify(inputString)
    inputString = re.sub(
        r'https?:\/\/(www\.)?[-a-zA-Z0–9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', '', inputString, flags=re.MULTILINE)
    inputString = re.sub(
        r'[-a-zA-Z0–9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', '', inputString, flags=re.MULTILINE)
    inputString = re.sub(r"#(\w+)", ' ', inputString, flags=re.MULTILINE)
    inputString = re.sub(r"@(\w+)", ' ', inputString, flags=re.MULTILINE)

    inputString = inputString.lower()

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(inputString)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    inputString = ' '.join(filtered_sentence)

    inputString = ' '.join(re.split(r'\W+', inputString))

    return inputString


with open('data_expanded.json', encoding='utf-8') as handle:
    dictionary = json.loads(handle.read())
    for tweet in dictionary:
        print(tweet['tweet_id'])
        print(preProcessString(tweet['text']))
