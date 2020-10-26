IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def _has_digit(name):
    if any(map(str.isdigit, name)):
        return True
    return False


def filter_names(names):
    counter = 1
    for name in names:
        if counter > MAX_NAMES or name.startswith(QUIT_CHAR):
            break
        if name.startswith(IGNORE_CHAR) or _has_digit(name):
            continue
        counter += 1
        yield name
