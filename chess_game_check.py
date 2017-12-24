"""Given a chessboard with one K and one Q, see if the K can attack the Q.

This function is given coordinates for the king and queen on a chessboard.
These coordinates are given as a letter A-H for the columns and 1-8 for the
row (see below for example):

Queens can move in any direction: horizontally, vertically, or diagonally,
as far as possible.

This function returns True if the king is in the line of attack of the queen.

For example, these boards show the king under attack:

8    . . . . . . . .      . . . . . . . .      . . . . . . . .    8
7    . . . . . . . .      . . . . . . . .      . K . . . . . .    7
6    . . . K . . . Q      . . . . K . . .      . . . . . . . .    6
5    . . . . . . . .      . . . . . . . .      . . . Q . . . .    5
4    . . . . . . . .      . . . . Q . . .      . . . . . . . .    4
3    . . . . . . . .      . . . . . . . .      . . . . . . . .    3
2    . . . . . . . .      . . . . . . . .      . . . . . . . .    2
1    . . . . . . . .      . . . . . . . .      . . . . . . . .    1
     A B C D E F G H      A B C D E F G H      A B C D E F G H

     K=D6, Q=H6           K=E6, Q=E4           K=B7, Q=D5

>>> check("D6", "H6")
True

>>> check("E6", "E4")
True

>>> check("B7", "D5")
True

>>> check("A1", "H8")
True

>>> check("A8", "H1")
True

>>> check("D6", "H7")
False

>>> check("E6", "F4")
False
"""

def letter_to_num(letter):
    """Given a capital letter, A-H, return corresponding number.
        A=1,B=2...
    """
    letters = 'ABCDEFGH'
    return letters.index(letter) + 1


# 8    . . . . . . . .      . . . . . . . .      . . . . . . . .    8
# 7    . . . . . . . .      . . . . . . . .      . K . . . . . .    7
# 6    . . . K . . . Q      . . . . K . . .      . . . . . . . .    6
# 5    . . . . . . . .      . . . . . . . .      . . . Q . . . .    5
# 4    . . . . . . . .      . . . . Q . . .      . . . . . . . .    4
# 3    . . . . . . . .      . . . . . . . .      . . . . . . . .    3
# 2    . . . . . . . .      . . . . . . . .      . . . . . . . .    2
# 1    . . . . . . . .      . . . . . . . .      . . . . . . . .    1
#      A B C D E F G H      A B C D E F G H      A B C D E F G H

#      K=D6, Q=H6           K=E6, Q=E4           K=B7, Q=D5


def check(king, queen):
    """Given a chessboard with one K and one Q, see if the K can attack the Q.

    This function is given coordinates for the king and queen on a chessboard.
    These coordinates are given as a letter A-H for the columns and 1-8 for the
    row, like "D6" and "B7":
    """

    letters = 'ABCDEFGH'
    nums = '12345678'
    # If K and Q are in same column or row, it's in check
    if king[0] == queen[0] or king[1] == queen[1]:
        return True

    # To check for descending diagonal, sum of row number and column number
    #(using helper function) is equal.
    elif letter_to_num(king[0]) + int(king[1]) == letter_to_num(queen[0]) + int(queen[1]):
        return True

    # To check for ascending diagonal, see if difference between index of king
    # and queen letters and numbers is the same.
    elif letters.index(king[0]) - letters.index(queen[0]) == nums.index(king[1]) - nums.index(queen[1]):
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT GAME!\n"
