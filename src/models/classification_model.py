from sklearn.decomposition import TruncatedSVD


def lsa(matrix):
    ls = TruncatedSVD(n_components=500, n_iter=100)

    ls.fit_transform(matrix)
    print(ls.explained_variance_ratio_.sum())
    print(ls)