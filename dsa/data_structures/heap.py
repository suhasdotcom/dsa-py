"""
Multiple Heap implementations and related data structures
"""


def max_heapify(a_iterable, start_index=0):
    """
    Make a max heap out of provided iterable

    :param a_iterable: the regular sequence iterable
    :param start_index: start heapify, defaults to 0
    :return: a heap iterable
    """

    if len(a_iterable)-start_index < 2:
        return a_iterable

    _left_child_index = left_child_index(start_index, a_iterable)
    _right_child_index = right_child_index(start_index, a_iterable)

    if _left_child_index is not None \
            and left_child_element(start_index, a_iterable) > a_iterable[start_index]:
        a_iterable[start_index], a_iterable[_left_child_index] = \
            a_iterable[_left_child_index], a_iterable[start_index]

    if _right_child_index is not None \
            and right_child_element(start_index, a_iterable) > a_iterable[start_index]:
        a_iterable[start_index], a_iterable[_right_child_index] = \
            a_iterable[_right_child_index], a_iterable[start_index]

    if _left_child_index is not None:
        max_heapify(a_iterable, _left_child_index)

    if _right_child_index is not None:
        max_heapify(a_iterable, _right_child_index)

    return a_iterable


def left_child_index(curr_index, a_iterable=None):
    """
    Gives left child index for this iterable (2*i+1) if left-child-index in within the iterable or if the iterable
    is None, None if index is beyond the given iterable

    :param curr_index: current index
    :param a_iterable: provided iterable, defaults to None
    :return: left child index for this iterable (2*i+1), or None if index is beyond the given iterable
    """
    _left_child_index = 2 * curr_index + 1

    if a_iterable is None:
        return _left_child_index

    if _left_child_index >= len(a_iterable):
        return None

    return _left_child_index


def right_child_index(curr_index, a_iterable=None):
    """
    Gives right child index for this iterable (2*i+2) if right-child-index in within the iterable or if the iterable
    is None, None if index is beyond the given iterable

    :param curr_index: current index
    :param a_iterable: provided iterable, defaults to None
    :return: right child index for this iterable (2*i+2), or None if index is beyond the given iterable
    """
    _right_child_index = 2 * curr_index + 2

    if a_iterable is None:
        return _right_child_index

    if _right_child_index >= len(a_iterable):
        return None

    return _right_child_index


def left_child_element(curr_index, a_iterable):
    """
    Gives left child for this iterable (2*i+1th element) if left-child-index in within the iterable limits
    , None if index is beyond the given iterable

    :param curr_index: current index
    :param a_iterable: provided iterable
    :return: left child element for this iterable (2*i+1th element), or None if index is beyond the given iterable
    """
    _left_child_index = left_child_index(curr_index, a_iterable)

    if _left_child_index is None:
        return None

    return a_iterable[_left_child_index]


def right_child_element(curr_index, a_iterable=None):
    """
    Gives right child for this iterable (2*i+2nd element) if right-child-index in within the iterable limits
    , None if index is beyond the given iterable

    :param curr_index: current index
    :param a_iterable: provided iterable
    :return: right child element for this iterable (2*i+2nd element), or None if index is beyond the given iterable
    """
    _right_child_index = right_child_index(curr_index, a_iterable)

    if _right_child_index is None:
        return None

    return a_iterable[_right_child_index]


class HeapNode:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left
