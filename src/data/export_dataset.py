import pickle
from src.utils.utils import get_file_path


def export_dataset(training, testing):
    with open(get_file_path("processed\\training_cleaned.pkl"), "wb") as file:
        pickle.dump(training, file, pickle.HIGHEST_PROTOCOL)

    with open(get_file_path("processed\\testing_cleaned.pkl"), "wb") as file:
        pickle.dump(testing, file, pickle.HIGHEST_PROTOCOL)



def export_training_testing(training, testing):
    with open(get_file_path("interim\\training.pkl"), "wb") as file:
        pickle.dump(training, file, pickle.HIGHEST_PROTOCOL)

    with open(get_file_path("interim\\testing.pkl"), "wb") as file:
        pickle.dump(testing, file, pickle.HIGHEST_PROTOCOL)