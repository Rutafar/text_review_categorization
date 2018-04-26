from sklearn.decomposition import TruncatedSVD
from src.utils.utils import get_file_names, get_file_path
from sklearn.preprocessing import StandardScaler
from scipy.sparse import csr_matrix


def lsa(matrix, comppnents):

    ls = TruncatedSVD(n_components=comppnents)
    print('fitting')
    fit = ls.fit_transform(matrix)
    '''
    with open(get_file_path('explained_nouns_back.txt'), 'a') as f:
        f.write(str(comppnents) + '\n')
        f.write(' '.join(str(i) for i in ls.explained_variance_ratio_) + '\n')
        f.write(' '.join(str(ls.explained_variance_ratio_.sum())) + '\n')
    '''
    return fit

def stand_matrix(data):
    x = StandardScaler(with_mean=False).fit_transform(data)
    x_sparse = csr_matrix(x)
    return x_sparse