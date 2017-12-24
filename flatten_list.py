def flatten_list(lst):
    """Write a function that flattens an Array of Array objects into a
    flat Array. Your function must only do one level of flattening.

    >>> flatten_list([1, 2, 3])
    [1, 2, 3]

    >>> flatten_list([[1, 2, 3], ["a", "b", "c"], [1, 2, 3]])
    [1, 2, 3, 'a', 'b', 'c', 1, 2, 3]
    """

    return_list = []
    for item in lst:
        if type(item) == list:
            return_list.extend(flatten_list(item))
        else:
            return_list.append(item)

    return return_list

print flatten_list([1, 2, 3])
print flatten_list([[1, 2, 3], ["a", "b", "c"], [1, 2, 3]])

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
