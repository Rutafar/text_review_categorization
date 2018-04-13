from src.utils.utils import get_file_path
import pandas as pd
import json
from pickle import dump

def import_dataset(dataset_name):
    reviews_list = list()
    with open(get_file_path("raw\\" + dataset_name), encoding="utf8") as json_file:
        for line in json_file:
            sample = json.loads(line)
            reviews_list.append(sample)

    return reviews_list


def export_sampled_datasets(train):
    with open(get_file_path("interim\\movies_and_tv.pkl"), "wb") as f:
        dump(train, f)
