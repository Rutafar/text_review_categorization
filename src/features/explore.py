from nltk import pos_tag, bigrams
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from features.normalize import tag_word


def bag_of_words(data):
    for text in data:
        vectorizer = CountVectorizer()
        features = vectorizer.fit_transform(text)
        print(vectorizer.vocabulary_)

def tdidf(text):
    tfidf = TfidfVectorizer.transform(text)
    return tfidf


def bigrm(text):
    bigrm = bigrams(text.split())
    print (*map(' '.join, bigrm), sep=', ')


def only_nouns(data):
    noun_list = list()
    for text in data:
        tags = tag_word(text.split())
        nouns = [word for word in text.split() if tags[word] == wordnet.NOUN]
        noun_list.append(' '.join(nouns))

    return noun_list

