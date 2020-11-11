import re


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    lines = passwd.strip().splitlines()
    users = {}
    for line in lines:
        user, _, _, _, name, _, _ = line.split(":")
        name = re.sub(",+$", "", name)
        name = re.sub(",+", " ", name)
        name = "unknown" if name == "" else name
        users[user] = name
    return users
