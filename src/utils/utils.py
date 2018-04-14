from os.path import dirname, join,  abspath

_BASIC_PATH = (join(dirname(dirname(dirname(abspath(__file__)))),"data"))
_FILE_NAMES = ['reviews_Movies_and_TV', 'reviews_Automotive', 'reviews_Cell_Phones_and_Accessories']


def get_file_path(filename):

    return join(_BASIC_PATH, filename)


def get_file_names():
    return _FILE_NAMES
