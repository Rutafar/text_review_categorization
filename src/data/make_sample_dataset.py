import pickle
from src.utils.utils import get_file_path

def read_pickle_files(file):
    with open(get_file_path('interim\\' + file+ '.pkl'), 'rb') as lines:
        return pickle.load(lines)
