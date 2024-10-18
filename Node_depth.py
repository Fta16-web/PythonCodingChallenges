from Tree_module import BinaryTree
from Node_module import BinaryNode
import unittest


# Depth of a Node (here) --> the distance of a node to the root -> Depth of root node is zero 
# Write a function that accepts a binary tree and returns the sum of all node depths.
# empty/one-node Btree has sumDepth = 0
# 
#                         4 <-(0)
#                       /    \
#                       2     6  <-(1)
#                      / \   /
#                     1   3  5  <-(2)   
#                     sum_depth = 0 + 1 + 1 + 2 + 2 + 2 = 8 
#                     Time: O(n), n is the number of nodes  
#                     Space: O(h), h is the height of the tree


# Recursive version
def sum_depth_rec(b_tree):
    if b_tree.root is None:
        return 0
    return sum_depth_rec_helper(b_tree.root, 0)

def sum_depth_rec_helper(b_node, depth):
    if b_node is None:
        return 0
    left_depth = sum_depth_rec_helper(b_node.left, depth + 1)
    right_depth = sum_depth_rec_helper(b_node.right, depth + 1)
    return depth + left_depth + right_depth

# Iterative version
def sum_depth_itr(b_tree):
    if b_tree.root is None:
        return 0
    sum_depth = 0
    stack = [{"node": b_tree.root, "depth": 0}]
    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            continue
        sum_depth += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sum_depth

class TestSumDepthFunctions(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(sum_depth_itr(BinaryTree()),0)
        self.assertEqual(sum_depth_rec(BinaryTree()),0)

    def test_one_node_tree(self):
        b_tree = BinaryTree(1)
        self.assertEqual(sum_depth_itr(b_tree),0)
        self.assertEqual(sum_depth_rec(b_tree),0)

    def test_balanced_tree(self):
         # small balanced tree
        b_tree = BinaryTree()
        my_entries = [10,-1,11]
        for i in my_entries:
            b_tree.insert(i)
        self.assertEqual(sum_depth_itr(b_tree),2)
        self.assertEqual(sum_depth_rec(b_tree),2)
        b_tree = BinaryTree()
        # larger balanced tree 
        my_entries = [9,0,15,-1,2,13,17]
        for i in my_entries:
            b_tree.insert(i)
        self.assertEqual(sum_depth_itr(b_tree),10)
        self.assertEqual(sum_depth_rec(b_tree),10)
    def test_unbalanced_tree(self):
         # small unbalanced tree
        b_tree = BinaryTree()
        my_entries = [10,0]
        for i in my_entries:
            b_tree.insert(i)
        self.assertEqual(sum_depth_itr(b_tree),1)
        self.assertEqual(sum_depth_rec(b_tree),1)
        b_tree = BinaryTree()
        # larger balanced tree 
        my_entries = [100,50,200,300,1000]
        for i in my_entries:
            b_tree.insert(i)
        self.assertEqual(sum_depth_itr(b_tree),7)
        self.assertEqual(sum_depth_rec(b_tree),7)
    def test_linear_tree(self):
         # left linear tree
        b_tree = BinaryTree()
        my_entries = [100,80,70,0]
        for i in my_entries:
            b_tree.insert(i)
        self.assertEqual(sum_depth_itr(b_tree),6)
        self.assertEqual(sum_depth_rec(b_tree),6)
        b_tree = BinaryTree()
        # right linear tree 
        my_entries = [100,150,200,300,1000]
        for i in my_entries:
            b_tree.insert(i)
        self.assertEqual(sum_depth_itr(b_tree),10)
        self.assertEqual(sum_depth_rec(b_tree),10)

# To run the tests
if __name__ == '__main__':
    unittest.main()