import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    if re.search("^PB(?:-[A-Z0-9]{8}){4}$", key):
        return True
    return False
