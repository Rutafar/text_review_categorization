from nltk import pos_tag, bigrams
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import LatentDirichletAllocation
from features.normalize import tag_word
from sklearn.decomposition import TruncatedSVD

def bag_of_words(data, grams=1):
    vectorizer = CountVectorizer(ngram_range=(grams,grams))
    features = vectorizer.fit_transform(data)
    return vectorizer, features


def tf_idf(bow):
    tfidf = TfidfTransformer(smooth_idf=True,use_idf=True)
    idfs = tfidf.fit_transform(bow)

    return tfidf, idfs


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

def lsa(matrix):
    ls = TruncatedSVD(n_components=500, n_iter=100)

    ls.fit_transform(matrix)
    print(ls.explained_variance_ratio_.sum())
    print(ls)
