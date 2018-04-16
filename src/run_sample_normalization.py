from src.utils.utils import get_file_names
from tqdm import tqdm
from data.make_sample_dataset import read_pickle_files, divide, write_new_pickle


def sampling():
    files = get_file_names()
    for file in files:
        print("reading file")
        out = read_pickle_files(file)
        print("sampling")
        review_list = divide(out)
        print("to pickle")
        write_new_pickle(review_list, file)


def main():
    sampling()


if __name__ == '__main__':
    main()


