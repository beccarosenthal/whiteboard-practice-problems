"""Given a string S, you are allowed to convert it to a palindrome by adding
characters in front of it. Find and return the shortest palindrome you can
find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd"."""


def shortest_palendrome(string):
    """ Given a string, convert it into a palindrome by adding characters to the
    beginning of it. Find and return the shortest possible palindrome you can
    make by performing this transformation.

    >>> shortest_palendrome('aacecaaa')
    'aaacecaaa'

    >>> shortest_palendrome('abcd')
    'dcbabcd'

    >>> shortest_palendrome('ab')
    'bab'

    >>> shortest_palendrome('')
    ''

    """

    if check_if_palendrome(string):
        return string

    elif len(string) <= 2:
        if string[0] != string[-1]:
            return string[-1] + string
        else:
            return string

    index = -1
    while index * -1 < len(string):
        if not check_if_palendrome(string[:index]):
            index -= 1
        else:
            beginning = ''.join(reversed([ch for ch in string[index:]]))

            return beginning + string

    if return_list:
        return ''.join(return_list)


    if letters_needed:
        return ''.join(letters_needed[-1]) + string


def check_if_palendrome(s):
    """given list, check if letters would form palindrome if joined"""

    if s == s[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT!\n"

