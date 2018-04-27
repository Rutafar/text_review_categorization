from sklearn.decomposition import TruncatedSVD
from sklearn.feature_selection import SelectKBest


def lsa(matrix, comppnents):

    ls = TruncatedSVD(n_components=comppnents)
    print('fitting')
    fit = ls.fit_transform(matrix)
    print(str(ls.explained_variance_ratio_.sum()))
    return ls, fit


def select_features(nr_features, training_set, training_labels):
    selector = SelectKBest(k=nr_features)
    transformed_set = selector.fit_transform(training_set, training_labels)
    return selector, transformed_set
