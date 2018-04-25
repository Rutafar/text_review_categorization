from src.data.import_dataset import import_cleaned_training_set, import_cleaned_testing_set
from data.export_dataset import export_comments
from models.classification_model import lsa
from features.explore import bag_of_words, only_nouns, tf_idf
import matplotlib.pyplot as plt
from sklearn import svm
from datetime import datetime

def main():
    start = datetime.now()
    print('Importing training....')
    training = import_cleaned_training_set()
    print('Importing testing....')
    testing = import_cleaned_testing_set()
    print('Taking Out comments')
    comments = extract_comments_from_reviews(training)
    print('Taking Out categories')
    categories = extract_categories_from_reviews(training)
    print('generating bag of words - nouns')
    print(datetime.now() - start)
    bow_vectorizer, bow_features = bag_of_words(comments)
    '''
    nouns = only_nouns(comments)
    print(datetime.now() - start)
    bow_vectorizer_nouns, bow_features_nouns = bag_of_words(nouns)
    '''
    #print(datetime.now() - start)
    #print('lsa 1000')
    #lsa(bow_features_nouns, 1000)

    print('lsa 500')
    reduced = lsa(bow_features, 500)
    print(datetime.now() - start)
    print(reduced)
    print(reduced.shape, bow_features.shape)
    #print('training and testing')
    #train_model(bow_features, categories, testing)
    #lsa(bow_features)
    #tf, idf = tf_idf(comments)
    '''
    nouns = only_nouns(comments)
    print(nouns)
    bow_vectorizer_nouns, bow_features_nouns = bag_of_words(nouns)
    '''





def extract_comments_from_reviews(dataset):
    comments_only = [review.reviewText for review in dataset]
    return comments_only

def extract_categories_from_reviews(dataset):
    categories_only = [review.category for review in dataset]
    return categories_only


def train_model(features, categories, test):
    clf = svm.SVC(kernel='linear', C=1.0)
    print('fitting')
    clf.fit(features, categories)
    print('predicting')
    predicted = clf.predict(test)
    print(predicted)

if __name__ == '__main__':
    main()