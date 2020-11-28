import itertools


def friends_teams(friends, team_size: int = 2, order_does_matter: bool = False):
    if order_does_matter:
        return itertools.permutations(friends, team_size)
    return itertools.combinations(friends, team_size)
