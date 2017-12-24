"""Does word contains unique set of characters?

For example::

    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True

Uppercase and lowercase letters should be considered separately::

    >>> has_unique_chars("Bob")
    True
"""


def has_unique_chars(word):
    """Does word contains unique set of characters?"""

    chars = {}
    for letter in word:
        chars[letter] = chars.get(letter, 0) + 1
        if chars[letter] > 1:
            return False

    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME!\n"
