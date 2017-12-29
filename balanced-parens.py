def balanced_parens(string):
    openers = []

    for item in string:
        if item == '(':
            openers.append(item)
        elif item == ")":
            if not openers:
                return False
            else:
                openers.pop()

    return True


class Node(object):  # ...
    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

def insert_binary_search(root, new_data):
    """insert new data onto binary search tree"""

    if root.data == new_data:
        return

    elif root.data < new_data:
        if root.right:
            current = root.right
            add_node(current)
        else:
            root.right = Node(new_data)
            return
    elif root.data > new_data:
        if root.left:
            current = root.left
            add_node(current)

