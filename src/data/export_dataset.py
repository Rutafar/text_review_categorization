import pickle
from src.utils.utils import get_file_path


def export_dataset(review_set):
    with open(get_file_path("processed\\training.pkl"), "wb") as file:
        pickle.dump(review_set, file, pickle.HIGHEST_PROTOCOL)