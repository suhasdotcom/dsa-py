import search.linear_search as linear_search


def test_empty_iterable_search_returns_minus_1():
    assert linear_search.linear_search([], 1) == -1


def test_one_element_not_matched_returns_minus_1():
    assert linear_search.linear_search([2], 1) == -1


def test_one_element_matched_returns_index_0():
    assert linear_search.linear_search([1], 1) == 0


def test_two_element_first_element_matched_returns_1():
    assert linear_search.linear_search([1, 1], 1) == 0


def test_three_element_iterable_matched_returns_1():
    assert linear_search.linear_search([1, 1, 1], 1) == 0


def test_returns_correct_element_index_in_natural_numbers_iterable():
    n_iter = [1, 3, 5, 7, 9, 10, 11, 14, 17]
    assert linear_search.linear_search(n_iter, 11) == 6


def test_returns_correct_index_on_negative_element_iterable_as_well():
    n_iter = [-99, -7, -3, -1, 0, 7, 9, 78, 99, 100]
    assert linear_search.linear_search(n_iter, 100) == 9
    assert linear_search.linear_search(n_iter, -7) == 1
    assert linear_search.linear_search(n_iter, -99) == 0
    assert linear_search.linear_search(n_iter, 0) == 4


def test_returns_correct_index_on_negative_unsorted_element_iterable_as_well():
    n_iter = [100, -1, -99, 7, -7, -3, 0, 9, 99, 78]
    assert linear_search.linear_search(n_iter, 100) == 0
    assert linear_search.linear_search(n_iter, -7) == 4
    assert linear_search.linear_search(n_iter, 99) == 8
    assert linear_search.linear_search(n_iter, 0) == 6
    assert linear_search.linear_search(n_iter, 56) == -1
