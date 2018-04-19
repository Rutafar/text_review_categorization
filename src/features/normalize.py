from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, bigrams
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer


def letters_only(text):
    letters = re.sub("[^a-zA-Z]", " ", text)
    return letters


def lower_only(text):
    return text.lower().split()


def remove_stopwords(text):
    no_stopwords = [word for word in text if word not in stopwords.words("english")]

    return " ".join(no_stopwords)


def lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    word_categories = tag_word(text)
    lemma_list_of_words =list()
    for i in text:

        l1 = i
        for word in l1.split():
            cat = word_categories.get(word)

            if cat == ' ':
                lemma_list_of_words.append(word)
                continue
            else:
                lem = lemmatizer.lemmatize(word, cat)
                lemma_list_of_words.append(lem)

    #print(lemma_list_of_words)
    return lemma_list_of_words

'''
VB - verb
VBP - Verb
NN - noun
JJ - adj
'''


def tag_word(text):
    tags = pos_tag(text)
    word_categories = dict()
    for word in tags:
        t = ' '
        tag = word[1][0]
        if tag == 'N':
            t = wordnet.NOUN
        elif tag == 'V':
            t = wordnet.VERB
        elif tag == 'J':
            t = wordnet.ADJ
        elif tag == 'R':
            t = wordnet.ADV

        word_categories[word[0]] = t
    return word_categories


def bag_of_words(data):
    for text in data:
        vectorizer = CountVectorizer()
        print(vectorizer.fit_transform(text).todense())
        print(vectorizer.vocabulary_)


def bigrm(text):
    bigrm = bigrams(text.split())
    print (*map(' '.join, bigrm), sep=', ')


def only_nouns(data):
    noun_list = list()
    for text in data:
        tags = tag_word(text)
        nouns = [word for word in text if tags[word] == wordnet.NOUN]
        noun_list.append(nouns)


def clean(review):
    text = review.reviewText
    text = letters_only(text)
    text = lower_only(text)
    text = remove_stopwords(text)
    text = lemmatize(text)
    review.reviewText = text
    return review