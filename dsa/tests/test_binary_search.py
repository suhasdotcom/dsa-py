import math

import search.binary_search as binary_search


def test_empty_iterable_search_returns_minus_1():
    assert binary_search.binary_search([], 1) == -1


def test_one_element_not_matched_returns_minus_1():
    assert binary_search.binary_search([2], 1) == -1


def test_one_element_matched_returns_index_0():
    assert binary_search.binary_search([1], 1) == 0


def test_two_element_first_element_matched_returns_1():
    assert binary_search.binary_search([1, 1], 1) == 0


def test_three_element_iterable_matched_returns_1():
    assert binary_search.binary_search([1, 1, 1], 1) == 1


def test_returns_correct_element_index_in_natural_numbers_iterable():
    n_iter = [1, 3, 5, 7, 9, 10, 11, 14, 17]
    assert binary_search.binary_search(n_iter, 11) == 6
    assert binary_search.binary_search(n_iter, 11, low=3) == 6
    assert binary_search.binary_search(n_iter, 11, low=3, high=7) == 6
    assert binary_search.binary_search(n_iter, 11, low=3, high=5) == -1


def test_returns_correct_index_on_negative_element_iterable_as_well():
    n_iter = [-99, -7, -3, -1, 0, 7, 9, 78, 99, 100]
    assert binary_search.binary_search(n_iter, 100) == 9
    assert binary_search.binary_search(n_iter, -7) == 1
    assert binary_search.binary_search(n_iter, -99) == 0
    assert binary_search.binary_search(n_iter, 0) == 4
    assert binary_search.binary_search(n_iter, 56) == -1
    assert binary_search.binary_search(n_iter, -99, low=4, high=0) == -1


# ============================================ position finder related test cases =====================================#
def test_gives_zeroth_position_in_an_empty_iterable():
    assert binary_search.find_position_in_sorted_iterable([], 1) == 0


def test_gives_zeroth_position_in_one_element_iterable_containing_higher_element():
    assert binary_search.find_position_in_sorted_iterable([2], 1) == 0


def test_gives_last_position_in_one_element_iterable_containing_lower_element():
    assert binary_search.find_position_in_sorted_iterable([1], 2) == 1


def test_gives_mid_index_in_iterable_where_element_is_found():
    n_iter = [0, 1, 2]
    assert binary_search.find_position_in_sorted_iterable(n_iter, 2) == 2
    assert binary_search.find_position_in_sorted_iterable(n_iter, 0) == 0
    assert binary_search.find_position_in_sorted_iterable(n_iter, 1) == 1
    assert binary_search.find_position_in_sorted_iterable(n_iter, 1, low=1, high=2) == 1


def test_returns_correct_insertion_index_on_negative_element_iterable_as_well():
    n_iter = [-99, -7, -3, -1, 0, 7, 9, 78, 99, 100]
    assert binary_search.find_position_in_sorted_iterable(n_iter, 100) == 9
    assert binary_search.find_position_in_sorted_iterable(n_iter, -7) == 1
    assert binary_search.find_position_in_sorted_iterable(n_iter, -99) == 0
    assert binary_search.find_position_in_sorted_iterable(n_iter, -100) == 0
    assert binary_search.find_position_in_sorted_iterable(n_iter, -math.inf) == 0
    assert binary_search.find_position_in_sorted_iterable(n_iter, math.inf) == 10
    assert binary_search.find_position_in_sorted_iterable(n_iter, 0) == 4
    assert binary_search.find_position_in_sorted_iterable(n_iter, 56) == 7
    assert binary_search.find_position_in_sorted_iterable(n_iter, 101) == 10


# ================================================= test cases for descending =========================================#
def test_empty_descending_iterable_search_returns_minus_1():
    assert binary_search.binary_search([], 1, descending=True) == -1


def test_one_element_descending_iterable_not_matched_returns_minus_1():
    assert binary_search.binary_search([2], 1, descending=True) == -1


def test_one_element_descending_iterable_matched_returns_index_0():
    assert binary_search.binary_search([1], 1, descending=True) == 0


def test_two_element_descending_iterable_first_element_matched_returns_1():
    assert binary_search.binary_search([1, 1], 1, descending=True) == 0


def test_three_element_descending_iterable_matched_returns_1():
    assert binary_search.binary_search([1, 1, 1], 1, descending=True) == 1


def test_returns_correct_element_index_in_natural_numbers_iterable_descending():
    n_iter = [17, 14, 11, 10, 9, 7, 5, 3, 1]
    assert binary_search.binary_search(n_iter, 11, descending=True) == 2
    assert binary_search.binary_search(n_iter, 11, low=3, descending=True) == -1
    assert binary_search.binary_search(n_iter, 11, low=3, high=7, descending=True) == -1
    assert binary_search.binary_search(n_iter, 11, low=1, high=2, descending=True) == 2
    assert binary_search.binary_search(n_iter, 11, low=1, high=1, descending=True) == -1


def test_returns_correct_index_on_negative_element_iterable_descending_as_well():
    n_iter = [100, 99, 78, 9, 7, 0, -1, -3, -7, -99]
    assert binary_search.binary_search(n_iter, 100, descending=True) == 0
    assert binary_search.binary_search(n_iter, -7, descending=True) == 8
    assert binary_search.binary_search(n_iter, -99, descending=True) == 9
    assert binary_search.binary_search(n_iter, 0, descending=True) == 5
    assert binary_search.binary_search(n_iter, 56, descending=True) == -1
    assert binary_search.binary_search(n_iter, -99, low=4, high=0, descending=True) == -1


# ============================================ position finder related test cases =====================================#
def test_gives_zeroth_position_in_an_empty_iterable_descending():
    assert binary_search.find_position_in_sorted_iterable([], 1, descending=True) == 0


def test_gives_zeroth_position_in_one_element_descending_iterable_containing_higher_element():
    assert binary_search.find_position_in_sorted_iterable([2], 1, descending=True) == 1


def test_gives_last_position_in_one_element_descending_iterable_containing_lower_element():
    assert binary_search.find_position_in_sorted_iterable([1], 2, descending=True) == 0


def test_gives_mid_index_in_descending_iterable_where_element_is_found():
    n_iter = [2, 1, 0]
    assert binary_search.find_position_in_sorted_iterable(n_iter, 2, descending=True) == 0
    assert binary_search.find_position_in_sorted_iterable(n_iter, 0, descending=True) == 2
    assert binary_search.find_position_in_sorted_iterable(n_iter, 1, descending=True) == 1
    assert binary_search.find_position_in_sorted_iterable(n_iter, 1, low=1, high=2, descending=True) == 1


def test_returns_correct_insertion_index_on_negative_element_descending_iterable_as_well():
    n_iter = [100, 99, 78, 9, 7, 0, -1, -3, -7, -99]
    assert binary_search.find_position_in_sorted_iterable(n_iter, 100, descending=True) == 0
    assert binary_search.find_position_in_sorted_iterable(n_iter, -7, descending=True) == 8
    assert binary_search.find_position_in_sorted_iterable(n_iter, -99, descending=True) == 9
    assert binary_search.find_position_in_sorted_iterable(n_iter, -100, descending=True) == 10
    assert binary_search.find_position_in_sorted_iterable(n_iter, -math.inf, descending=True) == 10
    assert binary_search.find_position_in_sorted_iterable(n_iter, math.inf, descending=True) == 0
    assert binary_search.find_position_in_sorted_iterable(n_iter, 0, descending=True) == 5
    assert binary_search.find_position_in_sorted_iterable(n_iter, 56, descending=True) == 3
    assert binary_search.find_position_in_sorted_iterable(n_iter, 101, descending=True) == 0
