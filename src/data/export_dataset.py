import pickle
from src.utils.utils import get_file_path


def export_dataset(set_to_save, name):
    with open(get_file_path("processed\\"+name + ".pkl"), "wb") as file:
        pickle.dump(set_to_save, file, pickle.HIGHEST_PROTOCOL)


def export_training_testing(training, testing):
    with open(get_file_path("interim\\training.pkl"), "wb") as file:
        pickle.dump(training, file, pickle.HIGHEST_PROTOCOL)

    with open(get_file_path("interim\\testing.pkl"), "wb") as file:
        pickle.dump(testing, file, pickle.HIGHEST_PROTOCOL)