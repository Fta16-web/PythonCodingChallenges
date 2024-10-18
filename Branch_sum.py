from Tree_module import BinaryTree

"""
create a function which accepts a binary tree and returns a 
a sorted list of all branches sum values


"""
def branch_sums (b_tree):
    '''
    time: O(n)
    space: O(n)
    '''
    sums = []
    calculate_branch_sums(b_tree.root, 0, sums)
    return sorted(sums)
# helper function recursive
def calculate_branch_sums(b_node, running_sum, sums):
    if b_node is None:
        return
    new_running_sum = running_sum + b_node.value
    if b_node.right is None and b_node.left is None:
        sums.append(new_running_sum)
    calculate_branch_sums(b_node.right,  new_running_sum, sums)
    calculate_branch_sums(b_node.left,  new_running_sum, sums)

#--------------------------------------
import unittest
class TestBranchSums(unittest.TestCase):
    def test_empty_tree(self):
        # Empty tree should return an empty list
        b_tree = BinaryTree()
        self.assertEqual(branch_sums(b_tree), [])

    def test_single_node(self):
        # Tree with a single node
        b_tree = BinaryTree(10)
        self.assertEqual(branch_sums(b_tree), [10])

    def test_small_tree(self):
        # Tree structure:
        #       10
        #      / \
        #     2   12
        #     __   __
        #     12   22
        my_lst = [10,2,12]
        b_tree = BinaryTree()
        for i in my_lst:
            b_tree.insert(i)
        self.assertEqual(branch_sums(b_tree), [12, 22]) 

    def test_larger_tree(self):
        # Tree structure:
        my_lst = [5,4,8,2,3,17,6]
        b_tree = BinaryTree()
        for i in my_lst:
            b_tree.insert(i)
        self.assertEqual(branch_sums(b_tree), [14, 19, 30]) 

    def test_tree_with_unbalanced_branches(self):
    
        my_lst = [3,2,4,5,6,7]
        b_tree = BinaryTree()
        for i in my_lst:
            b_tree.insert(i)
        self.assertEqual(branch_sums(b_tree), [5, 25])  
    def test_tree_with_one_branches(self):
    
        my_lst = [0,1,2,3,4]
        b_tree = BinaryTree()
        for i in my_lst:
            b_tree.insert(i)
        self.assertEqual(branch_sums(b_tree), [10]) 
   

    def test_tree_with_negative_values(self):
     
        my_lst = [-3,-4,-1,-2,3,5]
        b_tree = BinaryTree()
        for i in my_lst:
            b_tree.insert(i)
        self.assertEqual(branch_sums(b_tree), [-7, -6, 4] ) 

# To run the tests
if __name__ == '__main__':
    unittest.main()