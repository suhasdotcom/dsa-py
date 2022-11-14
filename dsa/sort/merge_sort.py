"""
Merge sort implementation by the first principles
"""


def merge_sort(a_iterable, descending=False):
    """
    Sorts the iterable using merge sort

    :param a_iterable: iterable to be sorted
    :param descending: Whether the iterable is to be sorted in descending manner, defaults to False
    :return: the sorted iterable
    """

    a_iterable_length = len(a_iterable)

    if a_iterable_length < 2:  # stop recursion if none or one element is present as that's already sorted
        return a_iterable

    return merge_iterables(merge_sort(a_iterable[0:a_iterable_length // 2], descending=descending),
                           merge_sort(a_iterable[a_iterable_length // 2: a_iterable_length], descending=descending),
                           descending=descending)


def merge_iterables(a_iterable_1, a_iterable_2, descending=False):
    """
    Merges two iterables using finger sorting

    :param a_iterable_1: the first iterable
    :param a_iterable_2: the second iterable
    :param descending: Whether the iterable is to be sorted in descending manner, defaults to False
    :return: merged iterable
    """

    i = 0
    j = 0

    new_iterable = []

    a_iterable_1_length = len(a_iterable_1)
    a_iterable_2_length = len(a_iterable_2)

    final_new_iterable_length = a_iterable_1_length + a_iterable_2_length

    for counter in range(0, final_new_iterable_length):
        if i < a_iterable_1_length and j < a_iterable_2_length:
            if (not descending and a_iterable_1[i] < a_iterable_2[j])\
                    or (descending and a_iterable_1[i] > a_iterable_2[j]):
                new_iterable.append(a_iterable_1[i])
                i += 1
            else:
                new_iterable.append(a_iterable_2[j])
                j += 1

        elif i < a_iterable_1_length:
            new_iterable.append(a_iterable_1[i])
            i += 1

        elif j < a_iterable_2_length:
            new_iterable.append(a_iterable_2[j])
            j += 1

    return new_iterable
