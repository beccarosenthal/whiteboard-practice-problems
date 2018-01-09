"""Use your Stack class to implement a new class MaxStack with a
method get_max() that returns the largest element in the stack.
get_max() should not remove the item."""

class Stack(object):

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):
    """ Given Stack, find max item in it """

    def get_max(self):
        current_max = None

