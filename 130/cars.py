from collections import Counter

import requests

CAR_DATA = "https://bit.ly/2Ov65SJ"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    return Counter([_["automaker"] for _ in data if _["year"] == year]).most_common()[
        0
    ][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return {
        _["model"] for _ in data if _["automaker"] == automaker and _["year"] == year
    }
