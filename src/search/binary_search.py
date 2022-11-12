"""
Implementation of binary-search and binary-search related algorithms and helpers
"""


def binary_search(a_iterable, item_to_find):
    """
    iterative binary_search implementation

    :param a_iterable: a sorted iterable
    :param item_to_find: actual item to find
    :return: index of item if found, -1 if not found
    """
    low, high, mid = _binary_search_helper(a_iterable, item_to_find)
    return mid if low < high else -1


def _binary_search_helper(a_iterable, item):
    a_iterable_length = len(a_iterable)
    high = a_iterable_length
    low = 0
    mid = (low + high) // 2

    while low < high:
        mid = (low + high) // 2
        if item == a_iterable[mid]:
            break
        elif item < a_iterable[mid]:
            high = mid
        elif item > a_iterable[mid]:
            low = mid

    return low, high, mid
