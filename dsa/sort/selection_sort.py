"""
Implementation of selection sort by the first principles
"""


def selection_sort(a_iterable):
    """
    This sort compares the extreme element in a run and places it in one of the extremes
    :param a_iterable: iterable to be sorted
    :return: an ascending sorted version of this iterable
    """

    a_iterable_length = len(a_iterable)

    for i in range(0, a_iterable_length):
        for j in range(i+1, a_iterable_length):
            if a_iterable[i] > a_iterable[j]:
                a_iterable[i], a_iterable[j] = a_iterable[j], a_iterable[i]

    return a_iterable
