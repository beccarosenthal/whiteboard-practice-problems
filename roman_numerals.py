"""Converts positive integers to Roman numeral equivilant

Write a method that converts an integer to its Roman numeral equivalent,
i.e., 476 => 'CDLXXVI'.

For reference, these are the building blocks for how we
encode numbers with Roman numerals: I = 1, V = 5, X = 10, L = 50, C = 100,
D = 500, M = 1000.

For example::

    >>> roman_numerals(5)
    'V'

    >>> roman_numerals(467)
    'CCCCLXVII'

You should convert to "old-school Roman numerals", where subtraction isn't
used. So, for exmple, 4 is "IIII" and 9 is "VIIII"::

    >>> roman_numerals(99)
    'LXXXXVIIII'

You do not need to convert numbers over 4,999, or less than 1.

"""


ROMAN_DIGIT = {1: 'I',
               5: 'V',
               10: 'X',
               50: 'L',
               100: 'C',
               500: 'D',
               1000: 'M'}


def roman_numerals(num):
    """Converts positive integers to Roman numeral equivalent using Old-school style."""

    if num != int(num) or num > 4999 or num < 1:
        raise ValueError("Cannot convert")


    if num in ROMAN_DIGIT:
        return ROMAN_DIGIT[num]

    to_join = []
    while num > 0:
        if num >= 1000:
            to_join.append(ROMAN_DIGIT[1000])
            num -= 1000
        elif num >= 500:
            to_join.append(ROMAN_DIGIT[500])
            num -= 500
        elif num >= 100:
            to_join.append(ROMAN_DIGIT[100])
            num -= 100
        elif num >= 50:
            to_join.append(ROMAN_DIGIT[50])
            num -= 50
        elif num >= 10:
            to_join.append(ROMAN_DIGIT[10])
            num -= 10
        elif num >= 5:
            to_join.append(ROMAN_DIGIT[5])
            num -= 5
        elif num >= 1:
            to_join.append(ROMAN_DIGIT[1])
            num -= 1
        # print to_join

    return ''.join(to_join)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOOOO!\n"
