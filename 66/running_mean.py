import itertools

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    totals = itertools.accumulate(sequence)
    for acc, i in enumerate(list(totals), start=1):
        yield round(i/acc, 2)
