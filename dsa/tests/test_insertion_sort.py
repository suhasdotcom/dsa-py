import math

import sort.insertion_sort as insertion_sort


def test_empty_element_iterable():
    assert insertion_sort.insertion_sort([]) == []


def test_one_element_iterable():
    assert insertion_sort.insertion_sort([1]) == [1]


def test_three_element_iterable():
    assert insertion_sort.insertion_sort([1, 4, 2]) == [1, 2, 4]


def test_four_element_iterable():
    assert insertion_sort.insertion_sort([1, 4, 2, 3]) == [1, 2, 3, 4]


def test_two_element_iterable():
    assert insertion_sort.insertion_sort([2, 1]) == [1, 2]


def test_four_sparse_element_iterable():
    assert insertion_sort.insertion_sort([-100, 400, -212, 13452]) == [-212, -100, 400, 13452]


def test_ten_element_sort_should_be_correct():
    a_iterable = [-99, 10000, 34, 2, 6, -90, -99999, -math.inf, math.inf, -26635]
    sorted_iterable = [-math.inf, -99999, -26635, -99, -90, 2, 6, 34, 10000, math.inf]
    assert insertion_sort.insertion_sort(a_iterable) == sorted_iterable


def test_fifty_element_sort_correct():
    a_iterable = [-59, 75, 33, -59, -37, 92, 82, -1, 82, -20, 52, 61, -7, 94, -36, -57, -95, 77, 30, 68, 7, 44, 13, 83,
                  30, -70, 77, -31, 11, -68, -92, 37, 97, -27, 79, 59, 75, -92, -63, 77, 88, -21, -31, 9, -41, -7, 19,
                  25, 18, 48]
    sorted_iterable = [-95, -92, -92, -70, -68, -63, -59, -59, -57, -41, -37, -36, -31, -31, -27, -21, -20, -7, -7, -1,
                       7, 9, 11, 13, 18, 19, 25, 30, 30, 33, 37, 44, 48, 52, 59, 61, 68, 75, 75, 77, 77, 77, 79, 82, 82,
                       83, 88, 92, 94, 97]
    assert insertion_sort.insertion_sort(a_iterable) == sorted_iterable


def test_hundred_sparse_element_sort_correct():
    a_iterable = [-196316, -455223, -597962, 185805, 450733, 507279, -577214, -401003, -696873, -15984, 580306, -149413,
                  56227, -672550, 962477, 110452, 793244, 842057, -602143, -773078, 622051, 216312, 33264, 347887,
                  181451, -443414, 313524, -55884, -330320, 767539, 996779, -179642, 629207, 587584, -656083, -634014,
                  -200278, 576178, 994236, -393641, -77829, -952109, -975275, -490171, 4759, -814419, 198613, -25868,
                  426576, -105138, -340629, 137583, 264538, 239676, -223113, 765736, 102489, -95318, 806402, -995931,
                  800560, -337056, 736569, 581187, -189158, -868370, 467378, -213358, 472517, -727895, -595829, 32451,
                  155395, 887807, 976554, 524984, -641614, -382204, -224771, 832089, 605706, 518383, -383275, -354729,
                  378332, 405512, -632246, 563345, 18940, 712969, 444105, -844489, 831813, -285773, 980232, -861934,
                  -65847, -328880, 380419, -447784]
    sorted_iterable = [-995931, -975275, -952109, -868370, -861934, -844489, -814419, -773078, -727895, -696873,
                       -672550, -656083, -641614, -634014, -632246, -602143, -597962, -595829, -577214, -490171,
                       -455223, -447784, -443414, -401003, -393641, -383275, -382204, -354729, -340629, -337056,
                       -330320, -328880, -285773, -224771, -223113, -213358, -200278, -196316, -189158, -179642,
                       -149413, -105138, -95318, -77829, -65847, -55884, -25868, -15984, 4759, 18940, 32451, 33264,
                       56227, 102489, 110452, 137583, 155395, 181451, 185805, 198613, 216312, 239676, 264538, 313524,
                       347887, 378332, 380419, 405512, 426576, 444105, 450733, 467378, 472517, 507279, 518383, 524984,
                       563345, 576178, 580306, 581187, 587584, 605706, 622051, 629207, 712969, 736569, 765736, 767539,
                       793244, 800560, 806402, 831813, 832089, 842057, 887807, 962477, 976554, 980232, 994236, 996779]
    assert insertion_sort.insertion_sort(a_iterable) == sorted_iterable
