"""In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

For example:

>>> my_list     = [3, 4, 6, 10, 11, 15]
>>> alices_list = [1, 5, 8, 12, 14, 19]
>>> merge_lists(my_list, alices_list)
[1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
"""


def merge_lists(lst1, lst2):a
    "If given two sorted lists, merge them into one sorted list"

    reversed_sorted = []
    while lst1 and lst2:
        if lst1[-1] > lst2[-1]:
            reversed_sorted.append(lst1.pop())
        else:
            reversed_sorted.append(lst2.pop())


    if lst2:
        reversed_sorted += lst2.reverse()

    elif lst1:
        reversed_sorted.extend(lst1.reverse())

    return reversed_sorted.reverse()


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
