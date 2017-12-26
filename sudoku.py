""" Sudoku is a number-placement puzzle. The objective is to fill a 9 * 9 grid
    with numbers in such a way that each column, each row, and each of the nine
    3 * 3 sub-grids that compose the grid all contain all of the numbers from 1
    to 9 one time.

    Implement an algorithm that will check whether the given grid of numbers
    represents a valid Sudoku puzzle according to the layout rules described
    above. Note that the puzzle represented by grid does not have to be solvable.

    """

def sudoku(grid):
    """

    Given a grid,  determine if it is a valid sudoku puzzle.

    >>> grid = [['.',  '.', '.', '1', '4', '.', '.', '2', '.'], ['.', '.', '6', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '1', '.', '.', '.', '.', '.', '.'], ['.', '6', '7', '.', '.', '.', '.', '.', '9'], ['.', '.', '.', '.', '.', '.', '8', '1', '.'], ['.', '3', '.', '.', '.', '.', '.', '.', '6'], ['.', '.', '.', '.', '.', '7', '.', '.', '.'], ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
    >>> sudoku(grid)
    True

    >>> grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'], ['.', '.', '.', '.', '6', '.', '.', '.', '.'], ['7', '1', '.', '.', '7', '5', '.', '.', '.'], ['.', '7', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '8', '3', '.', '.', '.'], ['.', '.', '8', '.', '.', '7', '.', '6', '.'], ['.', '.', '.', '.', '.', '2', '.', '.', '.'], ['.', '1', '.', '2', '.', '.', '.', '.', '.'], ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
    >>> sudoku(grid)
    False

    >>> grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'], ['.', '.', '6', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '1', '.', '.', '.', '.', '.', '.'], ['.', '6', '7', '.', '.', '.', '.', '.', '9'], ['.', '.', '.', '.', '.', '.', '8', '1', '.'], ['.', '3', '.', '.', '.', '.', '.', '.', '6'], ['.', '.', '.', '.', '.', '7', '.', '.', '.'], ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
    >>> sudoku(grid)
    True

    >>> grid = [[".",".",".",".","8",".",".",".","."], [".",".",".",".",".",".","5",".","."], [".",".",".",".","4",".",".","2","."], [".",".",".","3",".","9",".",".","."], [".",".","1","8",".",".","9",".","."], [".",".",".",".",".","5","1",".","."], [".",".","3",".",".","8",".",".","."], [".","1","2",".","3",".",".",".","."], [".",".",".",".",".","7",".",".","1"]]
    >>> sudoku(grid)
    True

    >>> grid = [[".",".","5",".",".",".",".",".","."],[".",".",".","8",".",".",".","3","."], [".","5",".",".","2",".",".",".","."], [".",".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".",".","9"], [".",".",".",".",".",".","4",".","."], [".",".",".",".",".",".",".",".","7"], [".","1",".",".",".",".",".",".","."], ["2","4",".",".",".",".","9",".","."]]
    >>> sudoku(grid)
    False

    >>> grid = [[".","4",".",".",".",".",".",".","."], [".",".","4",".",".",".",".",".","."], [".",".",".","1",".",".","7",".","."], [".",".",".",".",".",".",".",".","."], [".",".",".","3",".",".",".","6","."], [".",".",".",".",".","6",".","9","."], [".",".",".",".","1",".",".",".","."], [".",".",".",".",".",".","2",".","."], [".",".",".","8",".",".",".",".","."]]
    >>> sudoku(grid)
    False
    """

    # Run helper function that checks rows and columns; return False if it comes
    # back as False
    if not sudoku_rows_and_columns(grid):
        return False

    subgrid1 = set()
    subgrid2 = set()
    subgrid3 = set()

    row_index = 0
    for row in grid:
        for i in range(len(row)):
            value = row[i]
            if not value.isdigit():
                continue
            elif i < 3:
                if value not in subgrid1:
                    subgrid1.add(value)
                else:
                    return False
            elif i < 6:
                if value not in subgrid2:
                    subgrid2.add(value)
                else:
                    return False
            else:
                if value not in subgrid3:
                    subgrid3.add(value)
                else:
                    return False

        row_index += 1
        if row_index == 3:
            subgrid1 = set()
            subgrid2 = set()
            subgrid3 = set()
            row_index = 0


    return True


def sudoku_rows_and_columns(grid):
    """ An older version of code that doesn't deal with 3x3 grids but takes
    care of all repeats in rows or columns."""

    columns = {}
    for row in grid:
        row_index = 0
        nums_in_row = set()
        for item in row:
            if not item.isdigit():
                row_index += 1
                continue
            elif item.isdigit() and item in nums_in_row:
                return False
            else:
                nums_in_row.add(item)
                if row_index not in columns:
                    columns.setdefault(row_index, set(item))
                elif item not in columns[row_index]:
                    columns[row_index].add(item)
                else:
                    return False

            row_index += 1

    return True

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
