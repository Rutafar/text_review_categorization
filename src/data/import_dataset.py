import pickle
from src.utils.utils import get_file_names, get_file_path
from data.export_dataset import export_training_testing
from numpy.random import choice
from tqdm import tqdm


def import_and_divide():
    files = get_file_names()
    training = list()
    testing = list()
    for file in files:
        with open(get_file_path('interim\\sample_' + file + '.pkl'), 'rb') as f:
            lines = pickle.load(f)
            t = choice(lines, size=70000, replace=False)
            for l in tqdm(t):
                lines.remove(l)
                l['category'] = file
                training.append(l)
            for l in lines:
                l['category'] = file
                testing.append(l)


    export_training_testing(training, testing)


def import_set():
    with open(get_file_path('interim\\training.pkl'), 'rb') as f:
        training = pickle.load(f)

    with open(get_file_path('interim\\testing.pkl'), 'rb') as f:
        testing = pickle.load(f)

    return training, testing


def import_cleaned_training_set():
    with open(get_file_path('processed\\training.pkl'), 'rb') as file:
        training = pickle.load(file)

    return training

def import_cleaned_testing_set():
    with open(get_file_path('processed\\testing.pkl'), 'rb') as file:
        testing = pickle.load(file)

    return testing