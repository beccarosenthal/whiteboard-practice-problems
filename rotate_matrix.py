def rotate_matrix(list_of_lists):
    """
    >>> lst_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    >>> rotate_matrix(lst_1)
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    >>> lst_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    >>> rotate_matrix(lst_2)
    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

    """

    return_list = []
    for i in range(len(list_of_lists)):
        return_list.append([])

    for i in range(-1, -1 * (len(list_of_lists) + 1), -1):
        for j in range(len(list_of_lists[i])):
            return_list[j].append(list_of_lists[i][j])

    return return_list


lst_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print rotate_matrix(lst_1)


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
