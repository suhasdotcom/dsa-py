"""
Quick sort implementation by the first principles
"""
import math
from collections import OrderedDict


class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass

    def isPalindrome(self, s, start, end):
        if end - start < 1:
            return True

        return s[start] == s[end] and \
               self.isPalindrome(s, start + 1, end - 1)

    def palindromeLenght(self, s, start, end):
        return (end - start) if self.isPalindrome(s, start, end - 1) else 0

    def expandPalindromeLength(self, s, index):
        return self.expandPalindromeLengthHelper(s, index - 1, index + 1)

    def expandPalindromeLengthHelper(self, s, start, end):
        """heading
        end is non-inclusive

        some not here
        some note there
        """
        if start >= end:
            return end - start
        elif start < 0 or end >= len(s):
            return end - start
        elif s[start] == s[end]:
            return 2 + self.expandPalindromeLengthHelper(s, start - 1, end + 1)
        else:
            return self.expandPalindromeLengthHelper(s, start - 1, end + 1)


def partition(a_iterable, start, end):
    pivot = a_iterable[end]
    i = -1
    for j in range(start, end - 1):
        if a_iterable[j] < pivot:
            i += 1
            a_iterable[i], a_iterable[j] = a_iterable[j], a_iterable[i]

    i += 1
    a_iterable[i], a_iterable[end] = a_iterable[end], a_iterable[i]
    return i


def quick_sort(a_iterable, start=0, end=None, descending=False):
    """
    Sorts the iterable using quick sort

    :param a_iterable: iterable to be sorted
    :param descending: Whether the iterable is to be sorted in descending manner, defaults to False
    :param end: end index of the iterable, defaults to len(a_iterable)-1
    :param start: start index of the iterable, defaults to 0
    :return: the sorted iterable
    """

    if end is None:
        end = len(a_iterable) - 1

    if end - start < 2:  # stop recursion if none or one element is present as that's already sorted
        return

    pivot = partition(a_iterable, start, end)

    quick_sort(a_iterable, 0, pivot - 1)
    quick_sort(a_iterable, pivot + 1, end)


if __name__ == '__main__':
    # orderedDict = OrderedDict()
    # math.inf
    # x = []
    # quick_sort(x)
    # print(x)
    #
    # x = [1]
    # quick_sort(x)
    # print(x)
    #
    # x = [10, 1]
    # quick_sort(x)
    # print(x)
    #
    # x = [1, 6, 2]
    # quick_sort(x)
    # print(x)
    #
    # x = [1, -10, -9, 7, 4, 2, -99]
    # quick_sort(x)
    # print(x)

    sol = Solution()
    print('a', sol.isPalindrome('a', 0, 0))
    print('', sol.isPalindrome('', 0, 0))
    print('aa', sol.isPalindrome('aa', 0, 1))
    print('aaa', sol.isPalindrome('aaa', 0, 2))
    print('ab', sol.isPalindrome('ab', 0, 1))
    print('aba', sol.isPalindrome('aba', 0, 2))
    print('madam', sol.isPalindrome('madam', 0, 4))
    print('a', sol.palindromeLenght('a', 0, 1))
    print('', sol.palindromeLenght('', 0, 0))
    print('aa', sol.palindromeLenght('aa', 0, 2))
    print('aaa', sol.palindromeLenght('aaa', 0, 3))
    print('ab', sol.palindromeLenght('ab', 0, 2))
    print('aba', sol.palindromeLenght('aba', 0, 3))
    print('madam', sol.palindromeLenght('madam', 0, 5))
    print('madab', sol.palindromeLenght('madab', 0, 5))
    print('madab', sol.palindromeLenght('madab', 1, 4))
    print('ababa', 2, sol.expandPalindromeLength('ababa', 2))
    print('ababa', 1, sol.expandPalindromeLength('ababa', 1))
    print('ababa', 0, sol.expandPalindromeLength('ababa', 0))
    print('ababa', 3, sol.expandPalindromeLength('ababa', 3))
