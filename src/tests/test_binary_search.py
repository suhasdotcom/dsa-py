import search.binary_search as binary_search


def test_empty_iterable_search_returns_minus_1():
    assert binary_search.binary_search([], 1) == -1


def test_one_element_not_matched_returns_minus_1():
    assert binary_search.binary_search([2], 1) == -1


def test_one_element_matched_returns_index_0():
    assert binary_search.binary_search([1], 1) == 0


def test_two_element_first_element_matched_returns_1():
    """
    This method needs some explanation

    Actually, intuitively someone can argue that this method should return the 0th index for searching in an iterable
    having two equal elements of size two but that is not how the binary-search works. The mid here will be
    calculated as (0+2)//2 = 1 and as 1st indexed element itself is the element which was being searched hence,
    binary-search returns
    :return: None
    """
    assert binary_search.binary_search([1, 1], 1) == 1


def test_three_element_iterable_matched_returns_1():
    assert binary_search.binary_search([1, 1, 1], 1) == 1


def test_returns_correct_element_index_in_natural_numbers_iterable():
    n_iter = [1, 3, 5, 7, 9, 10, 11, 14, 17]
    assert binary_search.binary_search(n_iter, 11) == 6


def test_returns_correct_index_on_negative_element_iterable_as_well():
    n_iter = [-99, -7, -3, -1, 0, 7, 9, 78, 99, 100]
    assert binary_search.binary_search(n_iter, 100) == 9
    assert binary_search.binary_search(n_iter, -7) == 1
    assert binary_search.binary_search(n_iter, -99) == 0
    assert binary_search.binary_search(n_iter, 0) == 4
    assert binary_search.binary_search(n_iter, 56) == -1
