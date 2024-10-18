

class BinaryNode():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def set_left(self, node):
        """Sets the left child of the node."""
        self.left = node

    def set_right(self, node):
        """Sets the right child of the node."""
        self.right = node

    def get_left(self):
        """Returns the left child of the node."""
        return self.left

    def get_right(self):
        """Returns the right child of the node."""
        return self.right
