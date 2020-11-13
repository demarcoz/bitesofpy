from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    seq = Counter(sequence.lower())
    gc = seq["g"] or 0
    gc += seq["c"] or 0
    tot = seq["a"] or 0
    tot += seq["g"] or 0
    tot += seq["c"] or 0
    tot += seq["t"] or 0 
    perc = gc / tot * 100
    return round(perc, 2)
