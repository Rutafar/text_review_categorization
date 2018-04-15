import pickle
from src.utils.utils import get_file_names
from data.make_sample_dataset import read_pickle_files


def sampling():
    files = get_file_names()
    for file in files:
        out = read_pickle_files(file)
        print(type(out))


def main():
    sampling()


if __name__ == '__main__':
    main()


