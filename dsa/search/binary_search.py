"""
Implementation of binary-search and binary-search related algorithms and helpers
"""


def binary_search(a_iterable, item_to_find, low=0, high=None):
    """
    iterative binary search implementation

    :param a_iterable: a sorted iterable
    :param item_to_find: actual item to find
    :param low: lowest index to start binary search on, defaults to 0
    :param high: highest index to end binary search on, defaults to len(a_iterable)-1
    :return: index of item if found, -1 if not found
    """
    low, high, mid = _binary_search_helper(a_iterable, item_to_find, low=low, high=high)
    return mid if low <= high else -1


def find_position_in_sorted_iterable(a_iterable, item_to_insert, low=0, high=None):
    """
    finds position to insert an item in a sorted iterable, uses binary search

    :param a_iterable: a sorted iterable
    :param item_to_insert: actual item to insert
    :param low: lowest index to start binary search on, defaults to 0
    :param high: highest index to end binary search on, defaults to len(a_iterable)-1
    :return: index where to insert this item to
    """
    low, high, mid = _binary_search_helper(a_iterable, item_to_insert, low=low, high=high)
    return mid if low <= high else high + 1


def _binary_search_helper(a_iterable, item, low=0, high=None):
    """
    iterative binary-search helper function

    :param a_iterable: a sorted iterable
    :param item: item to judge position of
    :param low: lowest index to start binary search on, defaults to 0
    :param high: highest index to end binary search on, defaults to len(a_iterable)-1
    :return: a tuple denoting low, high and mid indices after all operations are done
    """
    a_iterable_length = len(a_iterable)
    if high is None:  # have to do it this way because defaulting high=len(a_iterable)-1 in the
        # function signature is not allowed by python
        high = a_iterable_length - 1

    mid = (low + high) // 2

    while low <= high:
        mid = (low + high) // 2
        if item == a_iterable[mid]:
            break
        elif item > a_iterable[mid]:
            low = mid + 1
        elif item < a_iterable[mid]:
            high = mid - 1

    return low, high, mid
