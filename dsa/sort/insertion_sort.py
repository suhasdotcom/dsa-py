from search.binary_search import find_position_in_sorted_iterable


def insertion_sort(a_iterable):
    """
    Sorts the iterable in ascending manner by performing insertion sort for O(lgn) comparisons using
    binary_search_position_finder

    :param a_iterable: a iterable to be sorted in ascending order
    :return: an ascending sorted iterable
    """

    a_iterable_length = len(a_iterable)

    unsorted_iterable_first_index = 1
    """
    0th index corresponds to first element and 1 element is always
    sorted, setting as 1 because a_iterable[1: len(a_iterable)] is unsorted
    """

    for i in range(unsorted_iterable_first_index, a_iterable_length):
        item_to_insert = a_iterable.pop(i)
        index_to_insert_item_at = find_position_in_sorted_iterable(a_iterable,
                                                                   item_to_insert,
                                                                   high=i-1)
        a_iterable.insert(index_to_insert_item_at, item_to_insert)
        unsorted_iterable_first_index += 1

    return a_iterable
