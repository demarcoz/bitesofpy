import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    data = list(os.walk(directory))
    return (len(data) - 1, sum([len(_[2]) for _ in data]))