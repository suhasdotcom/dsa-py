def linear_search(a_iterable, item_to_find):
    index = 0
    for element in a_iterable:
        if element == item_to_find:
            return index
        index += 1

    return -1

