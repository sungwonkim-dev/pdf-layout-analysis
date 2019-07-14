from os import listdir
from os.path import isfile, join


def get_files_in_path(path):
    files = [file for file in listdir(path) if isfile(join(path, file))]
    return files