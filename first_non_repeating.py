"""Note: Write a solution that only iterates over the string once and uses O(1)
additional memory, since this is what you would be asked to do during a real
interview.

Given a string s, find and return the first instance of a non-repeating
character in it. If there is no such character, return '_'.


>>> first_non_repeating("abacabad")
'c'

>>> first_non_repeating('abacabaabacaba')
'_'


"""

def first_non_repeating(string):

    chars = {}
    no_repeats = set()

    for i in range(len(string)):
        # if string[i] not in chars:
        #     chars[string[i]] = [i]
        # else:
        #     chars[string[i]].append(i)
        chars[string[i]] = chars.get(string[i], []) + [i]
    for lst in chars.values():
        if len(lst) == 1:
            no_repeats.add(lst[0])

    if no_repeats:
        return string[min(no_repeats)]
    else:
        return '_'



if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NODES ADDED SUCCESSFULLY!\n"
