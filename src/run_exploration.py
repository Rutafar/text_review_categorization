from src.data.import_dataset import import_cleaned_training_set, import_cleaned_testing_set
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score,recall_score
from sklearn.feature_selection import SelectKBest, chi2
from data.export_dataset import export_comments
from models.classification_model import lsa
import itertools
from features.explore import bag_of_words, only_nouns, tf_idf
import matplotlib.pyplot as plt
from sklearn import svm
from datetime import datetime
import numpy as np

def main():
    start = datetime.now()
    print(start)
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
<<<<<<< HEAD

    tf, idf_train = tf_idf(bow_features_training)
    tf, idf_test = tf_idf(bow_features_testing)

=======
    tf, idf_train = tf_idf(bow_features_training)
    tf, idf_test = tf_idf(bow_features_testing)

    tf, idf = tf_idf(bow_features_training)
    print(idf.shape)
    print(bow_features_training.shape)
>>>>>>> 119175c29b8d8f5e2e7777e1c76fbd6ae0cc5b3d
    print('Lsa 100 - training bow normal')
    ls, reduced_training = lsa(idf_train, 100)
    selector = SelectKBest(k=4)
    s = selector.fit_transform(reduced_training, categories_training)
    print('Lsa 100 - testing bow normal')
    ls_test, reduced_testing = lsa(idf_test, 100)
    s_t = SelectKBest(k=4).fit_transform(reduced_testing, categories_testing)
<<<<<<< HEAD
=======
    print('MODEL BAG OF WORDS NORMAL')
    train_model(s, categories_training, s_t, categories_testing)

    '''
    print('Lsa 100 - training bow normal')

    ls, reduced_training = lsa(bow_features_training, 20)
    selector = SelectKBest(k=4)
    s = selector.fit_transform(reduced_training, categories_training)
    print('Lsa 100 - testing bow normal')
    ls_test, reduced_testing = lsa(bow_features_testing, 20)
    s_t = SelectKBest(k=4).fit_transform(reduced_testing, categories_testing)

>>>>>>> 119175c29b8d8f5e2e7777e1c76fbd6ae0cc5b3d
    print('MODEL BAG OF WORDS NORMAL')
    train_model(s, categories_training, s_t, categories_testing)

    '''
    print('Lsa 100 - training bow normal')

    ls, reduced_training = lsa(bow_features_training, 20)
    selector = SelectKBest(k=4)
    s = selector.fit_transform(reduced_training, categories_training)
    print('Lsa 100 - testing bow normal')
    ls_test, reduced_testing = lsa(bow_features_testing, 20)
    s_t = SelectKBest(k=4).fit_transform(reduced_testing, categories_testing)

    print('MODEL BAG OF WORDS NORMAL')
    train_model(s, categories_training, s_t, categories_testing)
    
    print('\n\nBag of Nouns')

    nouns_training = only_nouns(comments_training)
    nouns_testing = only_nouns(comments_testing)
    bow_vectorizer_nouns_training, bow_features_nouns_training = bag_of_words(nouns_training)
    bow_vectorizer_nouns_testing, bow_features_nouns_testing = bag_of_words(nouns_testing)

    ls_nouns, ls_reduced_nouns = lsa(bow_features_nouns_training, 100)
    ls_nouns_test, ls_reduces_nouns_testing = lsa(bow_features_nouns_testing,100)
    s_n = SelectKBest(k=4).fit_transform(ls_reduced_nouns, categories_training)
    s_n_t = SelectKBest(k=4).fit_transform(ls_reduces_nouns_testing, categories_testing)

    print('MODEL BAG OF NOUNS')
    train_model(s_n, categories_training, s_n_t, categories_testing)


<<<<<<< HEAD
    
=======

>>>>>>> 119175c29b8d8f5e2e7777e1c76fbd6ae0cc5b3d
    print('\n\nBigrams')
    bow_vec_train_big, bow_feat_train_big = bag_of_words(comments_training, 2)
    bow_vec_test_big, bow_feat_test_big = bag_of_words(comments_testing, 2)
    ls_big_train, ls_reduced_train_big = lsa(bow_feat_train_big, 50)
    ls_big_test, ls_reduced_test_big = lsa(bow_feat_test_big, 50)
    s_big = SelectKBest(k=4).fit_transform(ls_reduced_train_big, categories_training)
    s_big_t = SelectKBest(k=4).fit_transform(ls_reduced_test_big, categories_testing)
    print('MODEL BIGRAMS')
    train_model(s_big, categories_training, s_big_t, categories_testing)
    '''


    print(datetime.now() - start)
    #print(reduced_training, categories_training)
    #print('Model part')

    print(datetime.now() - start)








def extract_comments_from_reviews(dataset):
    comments_only = [review.reviewText for review in dataset]
    return comments_only

def extract_categories_from_reviews(dataset):

    categories_only = [review.category for review in dataset]
    return categories_only


def train_model(training, training_categories, test, test_categories):
    start = datetime.now()
    print(start)
    clf = svm.SVC(kernel='linear', C=1.0)
    print('Fitting')
    clf.fit(training, training_categories)
    print(datetime.now()-start)
    print('Predicting')
    predicted = clf.predict(test)
    print(datetime.now()-start)
    print("Accuracy: " + str(accuracy_score(test_categories, predicted)))
    confusion = confusion_matrix(test_categories, predicted)
    plot_confusion_matrix(confusion)
    #f1 = f1_score(test_categories, predicted, average='weighted')
    precision = precision_score(test_categories, predicted, average='macro')

    recall = recall_score(test_categories, predicted, average='macro')
    f_cenas = np.round((2*precision*recall)/(precision+recall),2)
    print("F Cenas " + str(f_cenas))
    print("Recall " + str(recall))
    print("Precision " + str(precision))
    #print("F1 Score - Vettel wins" + f1)

def extract_cenas(dataset):
    movies = [[review.reviewText, review.category] for review in dataset]
    return movies


def plot_confusion_matrix(confusion):
    classes= ['reviews_Automotive', 'reviews_Cell_Phones_and_Accessories', 'reviews_Video_Games', 'reviews_Movies_and_TV']

    confusion = confusion.astype('float') / confusion.sum(axis=1)[:, np.newaxis]
    plt.imshow(confusion, cmap=plt.cm.Blues ,interpolation='nearest' )
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    fmt = '.2f'
    thresh = confusion.max() / 2.
    for i, j in itertools.product(range(confusion.shape[0]), range(confusion.shape[1])):
        plt.text(j, i, format(confusion[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if confusion[i, j] > thresh else "black")
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.show()

def generate_concepts(components,feature_names):
    for i, comp in enumerate(components):
        termsInComp = zip(feature_names, comp)
        sortedTerms = sorted(termsInComp, key=lambda x: x[1], reverse=True)[:10]
        print("Concept %d:" % i)
        for term in sortedTerms:
            print(term[0])
        print(" ")


if __name__ == '__main__':
    main()