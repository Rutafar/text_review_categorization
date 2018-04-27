from sklearn.decomposition import TruncatedSVD
from src.utils.utils import get_file_names, get_file_path
from sklearn.preprocessing import StandardScaler
from scipy.sparse import csr_matrix


def lsa(matrix, comppnents):

    ls = TruncatedSVD(n_components=comppnents)
    print('fitting')
    fit = ls.fit_transform(matrix)
    print(str(ls.explained_variance_ratio_.sum()))
    return ls, fit

