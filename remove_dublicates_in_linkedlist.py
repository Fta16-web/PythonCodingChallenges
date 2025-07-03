from typing import List
import unittest 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_dubs(head: Node):
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
    def link_vals(self, nums: List[int]) -> Node:
        ''' Helper to convert list to linked list '''
        if not nums:
            return None
        head = Node(nums[0])
        current = head
        for val in nums[1:]:
            current.next = Node(val)
            current = current.next
        return head

    def to_do_list(self, head: Node) -> List[int]:
        ''' Helper to convert linked list to list '''
        vals = []
        current = head
        while current is not None:
            vals.append(current.value)
            current = current.next
        return vals

    def test_to_list(self):
        head = None
        self.assertEqual(self.to_do_list(head), []) 
        head = Node(1)
        self.assertEqual(self.to_do_list(head), [1])
        head.next = Node(2)
        self.assertEqual(self.to_do_list(head), [1, 2]) 
        head.next.next = Node(2)
        self.assertEqual(self.to_do_list(head), [1, 2, 2])

    def test_to_link_values(self):
        vals = []
        head = self.link_vals(vals)
        self.assertIsNone(head)

        vals = [0]
        head = self.link_vals(vals)
        self.assertIsNone(head.next)
        self.assertEqual(head.value, vals[0])

        vals = [0, 2]
        head = self.link_vals(vals)
        self.assertIsNone(head.next.next)
        self.assertEqual(head.next.value, vals[1])

    def test_duplicates(self):
        raw_values = [1, 1, 2, 3, 3, 4, 4, 4, 5]
        clean_list = [1, 2, 3, 4, 5]
        head = self.link_vals(raw_values)
        new_head = remove_dubs(head)
        self.assertEqual(self.to_do_list(new_head), clean_list)

    def test_all_duplicates(self):
        raw_values = [1, 1, 1, 1]
        clean_list = [1]
        head = self.link_vals(raw_values)
        new_head = remove_dubs(head)
        self.assertEqual(self.to_do_list(new_head), clean_list)

    def test_no_duplicates(self):
        raw_values = [1, 2, 3, 4]
        clean_list = [1, 2, 3, 4]
        head = self.link_vals(raw_values)
        new_head = remove_dubs(head)
        self.assertEqual(self.to_do_list(new_head), clean_list)
        raw_values = [1]
        clean_list = [1]
        head = self.link_vals(raw_values)
        new_head = remove_dubs(head)
        self.assertEqual(self.to_do_list(new_head), clean_list)
        
    def test_empty_list(self):
        raw_values = []
        clean_list = []
        head = self.link_vals(raw_values)
        new_head = remove_dubs(head)
        self.assertEqual(self.to_do_list(new_head), clean_list)

if __name__ == '__main__':
    unittest.main()
