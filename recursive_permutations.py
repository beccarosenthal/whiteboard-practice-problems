# """Write a recursive function for generating all permutations of an input string. Return them as a set.

# Don't worry about time or space complexity. if we wanted efficiency we'd write an iterative version.

# To start, assume every character in the input string is unique.

# Your function can have loops. it just needs to also be recursive."""

def recursive_permutations(string):
    """Given a string of any length, return all possible permutations of it
    ignoring efficiency.

    >>> recursive_permutations('CATS')
    set(['TASC', 'ATSC', 'ASCT', 'SACT', 'CTAS', 'SCAT', 'ACTS', 'ACST', 'ASTC', 'CAST', 'CATS', 'STCA', 'TACS', 'ATCS', 'CTSA', 'CSTA', 'TCSA', 'TSAC', 'TCAS', 'SCTA', 'TSCA', 'SATC', 'CSAT', 'STAC'])

    >>> recursive_permutations('S')
    set(['S'])

    >>> recursive_permutations('SA')
    set(['SA', 'AS'])

    """

    return_set = set()

    if len(string) == 1:
        return_set.add(string)

    for i in range(len(string)):

        first = string[i]
        rest = string[0:i] + string[i+1:]
        perm = recursive_permutations(rest)
        for item in perm:
            return_set.add(first + item)

    return return_set



if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

