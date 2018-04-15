import datetime
from tqdm import tqdm
from src.utils.utils import get_file_names
from src.data.make_first_raw_dataset import import_dataset, export_sampled_datasets

start = datetime.datetime.now()


def file_pickling():
    files = get_file_names()
    for file in tqdm(files):
        test = import_dataset(file)
        export_sampled_datasets(test, file)


print(datetime.datetime.now() - start)