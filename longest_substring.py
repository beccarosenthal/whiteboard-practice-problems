"""Given a string, find the length of the longest substring
without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a
subsequence and not a substring."""

def longest_substring(s):
    """ Given a string, find the length of the longest substring
        without repeating characters.

        >>> longest_substring('abcabcbb')
        'abc'

        >>> longest_substring("bbbbb")
        'b'

        >>> longest_substring("pwwkew")
        'wke'

        >>> longest_substring('')
        ''
    """




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT!\n"
