"""Your quirky boss collects rare, old coins...

They found out you're a programmer and asked you to solve something they've been
wondering for a long time.

Write a function that, given:

an amount of money
a list of coin denominations
computes the number of ways to make the amount of money with coins of the
available denominations."""

def make_change(amt, coin_denoms):




if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
