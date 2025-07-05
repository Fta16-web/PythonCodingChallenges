from typing import List
import unittest


class BinaryNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


# --------------------------------
class NodeList:
    def __init__(self, val):
        self.value = val
        self.next = None

    @staticmethod
    def link_vals(nums: List[int]) -> "NodeList":
        """Helper to convert list to linked list"""
        if not nums:
            return None
        head = NodeList(nums[0])
        current = head
        for val in nums[1:]:
            current.next = NodeList(val)
            current = current.next
        return head

    @staticmethod
    def to_do_list(head: "NodeList") -> List[int]:
        """Helper to convert linked list to list"""
        vals = []
        current = head
        while current is not None:
            vals.append(current.value)
            current = current.next
        return vals

    @staticmethod
    def get_tail(head):
        if head is None or head.next is None:
            return head
        cur = head
        while cur.next is not None:
            cur = cur.next
        return cur

    def __str__(self):
        """Return a string representation of the linked list starting from this node."""
        vals = NodeList.to_do_list(self)
        res = "Head -> "
        for val in vals:
            res = res + str(val) + " -> "
        return res + "None"


#####################################################
class TestNodeModule(unittest.TestCase):
    # NodeList Tests
    def test_to_list(self):
        head = None
        self.assertEqual(NodeList.to_do_list(head), [])
        head = NodeList(1)
        self.assertEqual(NodeList.to_do_list(head), [1])
        head.next = NodeList(2)
        self.assertEqual(NodeList.to_do_list(head), [1, 2])
        head.next.next = NodeList(2)
        self.assertEqual(NodeList.to_do_list(head), [1, 2, 2])

    def test_to_link_values(self):
        vals = []
        head = NodeList.link_vals(vals)
        self.assertIsNone(head)

        vals = [0]
        head = NodeList.link_vals(vals)
        self.assertIsNone(head.next)
        self.assertEqual(head.value, vals[0])

        vals = [0, 2]
        head = NodeList.link_vals(vals)
        self.assertIsNone(head.next.next)
        self.assertEqual(head.next.value, vals[1])

    def test_get_tail(self):
        head = None
        self.assertIsNone(NodeList.get_tail(head))
        head = NodeList(2)
        self.assertEqual(NodeList.get_tail(head), head)
        head.next = NodeList(3)
        self.assertEqual(NodeList.get_tail(head), head.next)


if __name__ == "__main__":
    unittest.main()
