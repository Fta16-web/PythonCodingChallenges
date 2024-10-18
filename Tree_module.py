from Node_module import BinaryNode

class BinaryTree:
    def __init__(self, root_val=None):
        """Initializes the binary tree with an optional root value."""
        if root_val is not None:
            self.root = BinaryNode(root_val)
        else:
            self.root = None

    def insert(self, val):
        """Inserts a new value into the binary tree."""
        new_node = BinaryNode(val)
        if self.root is None:
            # Set new node as root if the tree is empty.
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current_node, new_node):
        """Helper method to insert a node into the tree recursively."""
        if new_node.value < current_node.value:
            if current_node.get_left() is None:
                current_node.set_left(new_node)
            else:
                self._insert_recursive(current_node.get_left(), new_node)
        else:
            if current_node.get_right() is None:
                current_node.set_right(new_node)
            else:
                self._insert_recursive(current_node.get_right(), new_node)

    def search(self, val):
        """Searches for a value in the binary tree."""
        return self._search_recursive(self.root, val)

    def _search_recursive(self, current_node, val):
        """Helper method to search for a value recursively."""
        if current_node is None:
            return False
        if current_node.value == val:
            return True
        elif val < current_node.value:
            return self._search_recursive(current_node.get_left(), val)
        else:
            return self._search_recursive(current_node.get_right(), val)

    def in_order_traversal(self):
        """Performs in-order traversal and returns a list of values."""
        values = []
        self._in_order_recursive(self.root, values)
        return values

    def _in_order_recursive(self, current_node, values):
        """Helper method for in-order traversal."""
        if current_node is not None:
            self._in_order_recursive(current_node.get_left(), values)
            values.append(current_node.value)
            self._in_order_recursive(current_node.get_right(), values)

    def pre_order_traversal(self):
        """Performs pre-order traversal and returns a list of values."""
        values = []
        self._pre_order_recursive(self.root, values)
        return values

    def _pre_order_recursive(self, current_node, values):
        """Helper method for pre-order traversal."""
        if current_node is not None:
            values.append(current_node.value)
            self._pre_order_recursive(current_node.get_left(), values)
            self._pre_order_recursive(current_node.get_right(), values)

    def post_order_traversal(self):
        """Performs post-order traversal and returns a list of values."""
        values = []
        self._post_order_recursive(self.root, values)
        return values

    def _post_order_recursive(self, current_node, values):
        """Helper method for post-order traversal."""
        if current_node is not None:
            self._post_order_recursive(current_node.get_left(), values)
            self._post_order_recursive(current_node.get_right(), values)
            values.append(current_node.value)
