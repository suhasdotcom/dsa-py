import math

import data_structures.heap as heap


# def test_empty_heap_iterable():
#     assert heap.traverse_heap_iterable([]) == []
#
#
# def test_single_element_iterable():
#     assert heap.traverse_heap_iterable([-1000]) == [-1000]
#
#
# def test_two_element_iterable():
#     assert heap.traverse_heap_iterable([-1, 2]) == [-1, 2]
#
#
# def test_four_element_iterable():
#     assert heap.traverse_heap_iterable([1, 2, 3, 4]) == [1, 2, 4, 3]

def test_empty_iterable_max_heapify():
    assert heap.max_heapify([]) == []


def test_single_element_iterable_max_heapify():
    assert heap.max_heapify([-1000]) == [-1000]


def test_two_element_iterable_max_heapify():
    assert heap.max_heapify([-1000, 2000]) == [2000, -1000]


def test_three_element_iterable_max_heapify():
    assert heap.max_heapify([-1000, 2000, 100]) == [2000, -1000, 100]


def test_ten_element_iterable_max_heapify():
    a_iterable = [-99, 10000, 34, 2, 6, -90, -99999, -math.inf, math.inf, -26635]
    max_heap = [math.inf, 10000, 34, 2, 6, -99, -90, -99999, -26635, -math.inf]
    assert heap.max_heapify(a_iterable) == max_heap
