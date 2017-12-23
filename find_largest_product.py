def find_largest_product(ints):
    """ Given list of integers, return the largest possible product of 3 items
    multiplied together.

    >>> find_largest_product([3, 2, 3, 1, 4, 6, 5])
    120

    >>> find_largest_product([-9, 2, 1, -7, 8, 7])
    504

    >>> find_largest_product([-1, -5, 0, -200, 1])
    1000

    >>> find_largest_product([-6, -5, -4, -3, -2, -1])
    -6

    >>> find_largest_product([-100, -4, 0, -500])
    0

    >>> find_largest_product([0, 0, 0, 0])
    0

    >>> find_largest_product([-3, -3, 2, 1])
    18

    >>> find_largest_product([3, 3, 0, -1])
    0

    >>> find_largest_product([-100, -100])
    'List Too Short'
    """
    # In order to figure out how to use the zeros
    length = len(ints)
    if length < 3:
        return 'List Too Short'

    # Get the highest and lowest number in list; remove them
    minimum_1 = min(ints)
    maximum_1 = max(ints)

    ints.remove(minimum_1)
    ints.remove(maximum_1)

    # get the second highest and lowest number in list; remove them
    minimum_2 = min(ints)
    maximum_2 = max(ints)

    # ints.remove(minimum_2)
    ints.remove(maximum_2)
    if ints:
        maximum_3 = max(ints)
    else:
        return maximum_1 * maximum_2 * minimum_2

    if minimum_1 * minimum_2 >= maximum_1 * maximum_2:
        if maximum_1 > 0:
            return minimum_1 * minimum_2 * maximum_1
        else:
            return maximum_1 * maximum_2 * maximum_3

    elif minimum_1 * minimum_2 <= maximum_1 * maximum_2 or maximum_1 <= 0:
        return maximum_1 * maximum_2 * maximum_3






if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
