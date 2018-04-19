import pickle
from src.utils.utils import get_file_names, get_file_path
from review.Review import create_review_from_sample
from tqdm import tqdm


def import_set():
    files = get_file_names()
    review_training_set = set()
    for file in tqdm(files):
        file_cat = 0
        with open(get_file_path('interim\\sample_' + file + '.pkl'), 'rb') as f:
            lines = pickle.load(f)

        for line in lines:
            review = create_review_from_sample(line, file_cat)
            review_training_set.add(review)

        file_cat = file_cat + 1

    return review_training_set
