import pandas as pd
import itertools
import matplotlib.pyplot as plt
import numpy as np

from src.utils.utils import get_file_path


def display_features(features, feature_names):
    df = pd.DataFrame(data=features, columns=feature_names)
    return df


def plot_confusion_matrix(confusion):
    classes = ['Automotive', 'Cell_Phones', 'Video_Games', 'Movies_and_TV']

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
    plt.tight_layout()
    plt.show()


def plot_explained_variance(file_name):
    file = open(get_file_path(file_name), "r")
    total = 0.0
    data = list()
    data_y = list()
    i = 1
    for num in file.read().split():
        total = float(num) + total
        data.append(total)
        data_y.append(i)
        i += 1
    plt.plot(data, data_y)
    plt.ylabel('Number of Components')
    plt.xlabel('Explained Variance')
    plt.title('Bag Of Nouns SVD Components Explained Variance')
    plt.show()