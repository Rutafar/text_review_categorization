import pickle
import random
from src.utils.utils import get_file_path


def read_pickle_files(file):
    with open(get_file_path('raw\\' + file+ '.pkl'), 'rb') as lines:
        return pickle.load(lines)


def divide(review_list):
    print("overall 1")
    overall_1 = sample_overall(review_list, 1)
    print("overall 2")
    overall_2 = sample_overall(review_list,2)
    print("overall 3")
    overall_3 = sample_overall(review_list,3)
    print("overall 4")
    overall_4 = sample_overall(review_list, 4)
    print("overall 5")
    overall_5 = sample_overall(review_list, 5)
    return overall_1 + overall_2 + overall_3 + overall_4 + overall_5


def sample_overall(review_list, overall_number):

    overall = list()
    while len(overall) < 20000:
        c = random.choice(review_list)

        if int(c['overall']) == overall_number:

            overall.append(c)


    return overall


def write_new_pickle(review_list, name):
    with open(get_file_path("interim\\sample_" + name + ".pkl"), "wb") as f:
        pickle.dump(review_list, f)

