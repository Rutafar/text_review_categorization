from src.data.import_dataset import import_cleaned_training_set, import_cleaned_testing_set
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.feature_selection import SelectKBest, chi2
from data.export_dataset import export_comments
from models.classification_model import lsa
from features.explore import bag_of_words, only_nouns, tf_idf
import matplotlib.pyplot as plt
from sklearn import svm
from datetime import datetime
import numpy as np

def main():
    start = datetime.now()
    print('Importing training....')
    training = import_cleaned_training_set()
    print('Importing testing....')
    testing = import_cleaned_testing_set()
    print('Taking Out comments')
    comments_training = extract_comments_from_reviews(training)
    comments_testing = extract_comments_from_reviews(testing)
    print('Taking Out categories')
    categories_training = extract_categories_from_reviews(training)
    categories_testing = extract_categories_from_reviews(testing)
    print('Generating bag of words')
    categories_training = np.asarray(categories_training)
    categories_testing = np.asarray(categories_testing)
    bow_vectorizer_training, bow_features_training = bag_of_words(comments_training)
    bow_vectorizer_testing, bow_features_testing = bag_of_words(comments_testing)
    print(datetime.now() - start)

    #print(bow_features_testing.shape)
    '''
    nouns = only_nouns(comments)
    print(datetime.now() - start)
    bow_vectorizer_nouns, bow_features_nouns = bag_of_words(nouns)
    '''

    print('Lsa 500 - training')
    reduced_training = lsa(bow_features_training, 100)
    selector = SelectKBest(score_func=chi2, k=4).fit_transform(reduced_training.support_vectors_, categories_training)
    print(selector.scores_)
    print(datetime.now() - start)
    '''
    print('Lsa 500 - testing')
    reduced_testing = lsa(bow_features_testing, 100)
    print(datetime.now() - start)
    #print(reduced_training, categories_training)
    print('Model part')
    train_model(reduced_training, categories_training, reduced_testing, categories_testing)
    print(datetime.now() - start)
'''





def extract_comments_from_reviews(dataset):
    comments_only = [review.reviewText for review in dataset]
    return comments_only

def extract_categories_from_reviews(dataset):

    categories_only = [review.category for review in dataset]
    return categories_only


def train_model(training, training_categories, test, test_categories):
    start = datetime.now()
    clf = svm.SVC(kernel='linear', C=1.0)
    print('Fitting')

    clf.fit(training, training_categories)
    print(datetime.now()-start)
    print('Predicting')
    predicted = clf.predict(test)
    print(datetime.now()-start)
    #print("Predicted: " + predicted)
    print("Accuracy: " + str(accuracy_score(test_categories, predicted)))
    print("Used Confuse, it was very effective" + confusion_matrix(test_categories, predicted))
    print("F1 Score - Vettel wins" + f1_score(test_categories, predicted))

def extract_cenas(dataset):
    movies = [[review.reviewText, review.category] for review in dataset]
    return movies


if __name__ == '__main__':
    main()