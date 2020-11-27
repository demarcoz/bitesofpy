import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(names, aliases=None, points=None, awake=None):
    data = []
    if awake:
        for index, name in enumerate(names):
            record = SEPARATOR.join([names[index], aliases[index], str(points[index]), str(awake[index])])
            data.append(record)
        return data
    if points:
        for index, name in enumerate(names):
            record = SEPARATOR.join([names[index], aliases[index], str(points[index])])
            data.append(record)
        return data
    if aliases:
        for index, name in enumerate(names):
            record = SEPARATOR.join([names[index], aliases[index]])
            data.append(record)
        return data
    return names
