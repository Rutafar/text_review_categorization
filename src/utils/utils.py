from os.path import dirname, join,  abspath

_BASIC_PATH = (join(dirname(dirname(dirname(abspath(__file__)))),"data"))


def get_file_path(filename):

    return join(_BASIC_PATH, filename)