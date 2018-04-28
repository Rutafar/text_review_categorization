from sklearn.decomposition import TruncatedSVD
from sklearn.feature_selection import SelectKBest
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score,recall_score
from features.explore import bag_of_words, only_nouns, tf_idf
from sklearn import svm
from datetime import datetime
import numpy as np
from visualization.visualize import plot_confusion_matrix


def train_model(training, training_categories, test, test_categories):
    clf = svm.SVC(kernel='linear', C=1.0)

    print('Fit')
    clf.fit(training, training_categories)

    print('Predict')
    predicted = clf.predict(test)

    print('Metrics')
    accuracy = accuracy_score(test_categories, predicted)
    confusion = confusion_matrix(test_categories, predicted)
    plot_confusion_matrix(confusion)
    precision = precision_score(test_categories, predicted, average='macro')
    recall = recall_score(test_categories, predicted, average='macro')
    f_measure = np.round((2*precision*recall)/(precision+recall),2)


