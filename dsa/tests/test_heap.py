import data_structures.heap as heap
import pytest


def test_max_heapify_for_no_element():
    """
    Must raise an :func: `AssertionError` as the provided index is less than 1.
    """
    with pytest.raises(AssertionError):
        heap.heapify([], 0)


def test_max_heapify_for_one_element():
    assert heap.heapify([1], 1) == [1]


def test_max_heapify_for_two_elements_at_min_index():
    """
    Must shuffle the elements as root (the element 2) is less than the leaf (element 1).
    """
    assert heap.heapify([1, 2], 1) == [2, 1]


def test_max_heapify_for_two_elements_at_max_index():
    """
    No element shuffling will be done as root_index (2) has no leaves.
    """
    assert heap.heapify([1, 2], 2) == [1, 2]


def test_max_heapify_for_three_elements():
    """
    First the left child (element 2) will be shuffled with root (element 1) then right child (element 3) will be
    shuffled with root (element 2).
    """
    assert heap.heapify([1, 2, 3], 1) == [3, 1, 2]


def test_max_heapify_for_three_elements_at_middle_index():
    """
    No shuffling will be done as root (element 2) has not children.
    """
    assert heap.heapify([1, 2, 3], 2) == [1, 2, 3]


def test_max_heapify_for_four_elements_at_first_index():
    """
    Will shuffle only elements 1, 2, and 3 for root index shuffling. 4 will remain untouched.
    """
    assert heap.heapify([1, 2, 3, 4], 1) == ([3, 1, 2, 4])


def test_max_heapify_for_four_elements_at_second_index():
    """
    Will shuffle only elements 2 and 4 for second index shuffling. 1 and 4 will remain untouched as 2nd element's
    left index is 4 and right index is 5 and the iterable is only 4 elements long.
    """
    assert heap.heapify([1, 2, 3, 4], 2) == ([1, 4, 3, 2])
