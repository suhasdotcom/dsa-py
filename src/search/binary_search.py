"""
Implementation of binary-search and binary-search related algorithms and helpers
"""


def binary_search(a_iterable, item_to_find):
    """
    iterative binary search implementation

    :param a_iterable: a sorted iterable
    :param item_to_find: actual item to find
    :return: index of item if found, -1 if not found
    """
    low, high, mid = _binary_search_helper(a_iterable, item_to_find)
    return mid if low < high else -1


def find_position_in_sorted_iterable(a_iterable, item_to_insert):
    """
    finds position to insert an item in a sorted iterable, uses binary search

    :param a_iterable: a sorted iterable
    :param item_to_insert: actual item to insert
    :return: index where to insert this item to
    """
    low, high, mid = _binary_search_helper(a_iterable, item_to_insert)
    if low <= high:
        return mid
    if a_iterable[mid] <= a_iterable[low]:
        return mid - 1
    if a_iterable[mid] >= a_iterable[high]:
        return mid + 1


def _binary_search_helper(a_iterable, item):
    """
    iterative binary-search helper function

    :param a_iterable: a sorted iterable
    :param item: item to judge position of
    :return: a tuple denoting low, high and mid indices
    """
    a_iterable_length = len(a_iterable)
    high = a_iterable_length
    low = 0
    mid = (low + high) // 2

    while low < high:
        mid = (low + high) // 2
        if item == a_iterable[mid]:
            break
        elif item > a_iterable[mid]:
            low = mid
        elif item < a_iterable[mid]:
            high = mid

    return low, high, mid
