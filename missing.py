"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    """
    # Find sum of all numbers up to n, subtract sum of items in list to find
    # missing one.

    lst_sum = None
    for num in nums:
        if lst_sum == None:
            lst_sum = 0
        lst_sum += num

    max_sum = 0
    for i in range(1, max_num + 1):
        max_sum += i

    missing = max_sum - lst_sum
    return missing

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
