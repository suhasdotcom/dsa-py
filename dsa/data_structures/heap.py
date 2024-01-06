"""
Implementation of a priority queue in terms of heap datastructure.
An array is visualized as a nearly complete binary tree. All the indices are started form 1 instead of 0.
"""


def parent_index(curr_index):
    """
    Returns the parent index of current index. Assumes 1-based indexing.
    :param curr_index: index whose parent index is to be determined.
    :return: curr_index/2
    """
    assert curr_index >= 1
    return curr_index // 2


def left_child_index(curr_index):
    """
    Returns the visualised left child of this index. Assumes 1-based indexing.
    :param curr_index: index whose conceptualised left child is to be determined.
    :return: curr_index * 2
    """
    assert curr_index >= 1
    return curr_index * 2


def right_child_index(curr_index):
    """
    Returns the visualised right child for this index. Assumes 1-based indexing.
    :param curr_index: index whose conceptualised right child is to be determined.
    :return: curr_index * 2 + 1
    """
    assert curr_index >= 1
    return curr_index * 2 + 1


def heapify(iterable, root_index, max=True):
    """
    Correct a single violation in the heap at root_index. Assumes 1-based indexing.
    :param iterable: the iterable to heapify at root index
    :param root_index: the index to heapify
    :param max: whether this is required to be max heap
    :return: an iterable heapified at root_index
    """
    assert root_index >= 1
    rc_index = right_child_index(root_index)
    lc_index = left_child_index(root_index)
    root_arr_index = root_index - 1
    rc_arr_index = rc_index - 1
    lc_arr_index = lc_index - 1

    if lc_arr_index < len(iterable):
        if not max and iterable[root_arr_index] > iterable[lc_arr_index]\
                or max and iterable[root_arr_index] < iterable[lc_arr_index]:
            iterable[root_arr_index], iterable[lc_arr_index] = iterable[lc_arr_index], iterable[root_arr_index]

    if rc_arr_index < len(iterable):
        if not max and iterable[root_arr_index] > iterable[rc_arr_index]\
                or max and iterable[root_arr_index] < iterable[rc_arr_index]:
            iterable[root_arr_index], iterable[rc_arr_index] = iterable[rc_arr_index], iterable[root_arr_index]

    return iterable
