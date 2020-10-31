PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    return "".join(
            [_.swapcase() if _.lower() in "pybites" else _ for _ in text]
        )
