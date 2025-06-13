
# define a function with parameter of type BinaryTree and int such that it return the closest value 
# in BT to val parameter provided
import unittest
from Tree_module import BinaryTree
from Node_module import BinaryNode
def find_closest_value_BST_helper(tree: BinaryNode, val: int, closest_val: int) -> int:
    if tree is None:
        return closest_val

    # Update closest value if current node is closer
    if abs(val - closest_val) > abs(val - tree.value):
        closest_val = tree.value

    # Move left or right depending on BST property
    if val < tree.value:
        return find_closest_value_BST_helper(tree.get_left(), val, closest_val)
    elif val > tree.value:
        return find_closest_value_BST_helper(tree.get_right(), val, closest_val)
    else:
        return tree.value  # exact match

def find_closest_value_BST(bt:BinaryTree,val:int) ->int:
    '''
    Recursive Entry Function
    AVG : Time = O(lg(N)), Space = O(log(N)) because we are using frame stack in recursion 
    Worst : one branch exists, O(lg(N)), Space  = O(N)
    '''
    return find_closest_value_BST_helper(bt.root,val,float("inf"))
def find_closest_value_BST_iter_helper(tree: BinaryNode, val: int, closest_val: int) -> int:
    current_node = tree
    while current_node is not None:
        # Update closest value if current node is closer
        if abs(val - closest_val) > abs(val - current_node.value):
            closest_val = current_node.value

        # Move left or right based on BST property
        if val < current_node.value:
            current_node = current_node.get_left()
        elif val > current_node.value:
            current_node = current_node.get_right()
        else:
            break  # exact match
    return closest_val
    
def find_closest_value_BST_iter(bt:BinaryTree,val:int) ->int:
    '''
    AVG : Time = O(lg(N)), Space = O(1) 
    Worst : one branch exists, O(lg(N)), Space  = O(1)
    '''
    return find_closest_value_BST_iter_helper(bt.root,val,float("inf"))
    

class FindClosestValue(unittest.TestCase):
     def setUp(self):
        self.tree = BinaryTree()
        for val in [10, 5, 2, 5, 13, 22, 14]:
            self.tree.insert(val)

     def test_exact_match(self):
        self.assertEqual(find_closest_value_BST(self.tree, 13), 13)
        self.assertEqual(find_closest_value_BST_iter(self.tree, 10), 10)

     def test_closest_lower(self):
        self.assertEqual(find_closest_value_BST(self.tree, 12), 13)
        self.assertEqual(find_closest_value_BST_iter(self.tree, 3), 2)

     def test_closest_higher(self):
        self.assertEqual(find_closest_value_BST(self.tree, 24), 22)
        self.assertEqual(find_closest_value_BST_iter(self.tree, 12), 13)

     def test_negative_value(self):
        self.assertEqual(find_closest_value_BST(self.tree, -10), 2)
        self.assertEqual(find_closest_value_BST_iter(self.tree, -3), 2)

     def test_large_positive(self):
        self.assertEqual(find_closest_value_BST(self.tree, 100), 22)
        self.assertEqual(find_closest_value_BST_iter(self.tree, 100), 22)

if __name__ == '__main__':
    unittest.main()