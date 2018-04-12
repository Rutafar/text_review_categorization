from src.utils.utils import get_file_path
import pandas as pd


def import_dataset(dataset_name):
    with open(get_file_path("raw\\" + dataset_name), encoding="utf8") as json_file:
        dataframe = (pd.read_json(json_file, lines=True)).sample(n=100000)

    train = dataframe.sample(n=70000)
    test = dataframe.sample(n=30000)
    return train, test

def export_sampled_datasets(train, test):
    return 0