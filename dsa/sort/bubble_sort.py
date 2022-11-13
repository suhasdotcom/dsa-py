"""
Implementation of bubble sort by first principles
"""


def bubble_sort(a_iterable):
    """
    This sort compares adjacent elements and pushes the heaviest elements to the end of the iterable. As this procedure
    looks like settling of bubbles hence the name bubble-sort

    :param a_iterable: The iterable to be sorted
    :return: ascending sorted iterable
    """

    a_iterable_length = len(a_iterable)
    for i in range(0, a_iterable_length-1):
        for j in range(0, a_iterable_length-i-1):
            if a_iterable[j] > a_iterable[j+1]:
                a_iterable[j], a_iterable[j+1] = a_iterable[j+1], a_iterable[j]

    return a_iterable
