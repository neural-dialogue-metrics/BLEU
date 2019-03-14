def count_ngrams(max_order, length):
    """
    Compute the number of n-grams given the length of a sequence from 1 to max_order.
    :param max_order: int, n-grams number to compute from 1 to max_order.
    :param length: int, the length of the sequence.
    :return: List[int], the number for each n-grams, where the number of i gram
    is stored at i-1 of the list.

    >>> count_ngrams(3, 3)
    [3, 2, 1]
    >>> count_ngrams(2, 3)
    [3, 2]
    >>> count_ngrams(3, 4)
    [4, 3, 2]
    """
    possible_matches_by_order = [0] * max_order
    for order in range(1, max_order + 1):
        possible_matches = length - order + 1
        if possible_matches > 0:
            possible_matches_by_order[order - 1] += possible_matches
    return possible_matches_by_order


if __name__ == '__main__':
    import doctest

    doctest.testmod()
