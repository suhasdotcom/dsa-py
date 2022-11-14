"""
Implementation of selection sort by the first principles
"""


def selection_sort(a_iterable, descending=False):
    """
    This sort compares the extreme element in a run and places it in one of the extremes
    :param a_iterable: iterable to be sorted
    :param descending: Whether the iterable is to be sorted in descending manner, defaults to False
    :return: sorted version of this iterable
    """

    a_iterable_length = len(a_iterable)

    for i in range(0, a_iterable_length):
        for j in range(i+1, a_iterable_length):
            if (not descending and a_iterable[i] > a_iterable[j])\
                    or (descending and a_iterable[i] < a_iterable[j]):
                a_iterable[i], a_iterable[j] = a_iterable[j], a_iterable[i]

    return a_iterable
