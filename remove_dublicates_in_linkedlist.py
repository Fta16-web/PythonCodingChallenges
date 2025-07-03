from typing import List
import unittest 
from Node_module import NodeList
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_dubs(head: NodeList):
    '''
    Removes duplicates from a sorted linked list.
    Time: O(N), Space: O(1)
    '''
    current_node = head
    while current_node is not None:
        next_distinct = current_node.next
        while next_distinct is not None and next_distinct.value == current_node.value:
            next_distinct = next_distinct.next
        current_node.next = next_distinct
        current_node = next_distinct
    return head

class TestRemoveDubs(unittest.TestCase):
     def test_remove_dubs(self):
        raw_values = [1, 1, 2, 3, 3, 4, 4, 4, 5]
        expected = [1, 2, 3, 4, 5]
        head = NodeList.link_vals(raw_values)
        new_head = remove_dubs(head)
        self.assertEqual(NodeList.to_do_list(new_head), expected)

     def test_remove_dubs_all_same(self):
        raw_values = [1, 1, 1]
        expected = [1]
        head = NodeList.link_vals(raw_values)
        new_head = remove_dubs(head)
        self.assertEqual(NodeList.to_do_list(new_head), expected)

     def test_remove_dubs_no_dupes(self):
        raw_values = [1, 2, 3]
        expected = [1, 2, 3]
        head = NodeList.link_vals(raw_values)
        new_head = remove_dubs(head)
        self.assertEqual(NodeList.to_do_list(new_head), expected)

     def test_remove_dubs_empty(self):
        raw_values = []
        expected = []
        head = NodeList.link_vals(raw_values)
        new_head = remove_dubs(head)
        self.assertEqual(NodeList.to_do_list(new_head), expected)

if __name__ == '__main__':
    unittest.main()
