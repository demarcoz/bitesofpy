import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file, 'r') as f:
            movies.append(json.loads(f.read()))
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    comedies = [_ for _ in movies if "Comedy" in _['Genre']]
    return comedies[0]['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    nominations = {}
    for movie in movies:
        title = movie['Title']
        nominations[title] = int(movie['Awards'].split()[-2])
    return sorted(nominations, key=nominations.get)[-1]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    runtimes = {}
    for movie in movies:
        title = movie['Title']
        runtimes[title] = int(movie['Runtime'].split()[0])
    return sorted(runtimes, key=runtimes.get)[-1]
