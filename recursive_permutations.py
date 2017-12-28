"""Write a recursive function for generating all permutations of an input string. Return them as a set.

Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

To start, assume every character in the input string is unique.

Your function can have loops—it just needs to also be recursive."""

def recursive_permutations(string):
    """Given a string of any length, return all possible permutations of it
    ignoring efficiency. """

    return_set = set()
    for i in range(len(string)):

