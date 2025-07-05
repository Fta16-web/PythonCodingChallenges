import unittest
from Node_module import NodeList

"""
recieves two linked lists such that each linked list represents 
a integer, head represents least valueable digit and the tail represents the most valueable digit 
ex:
1 -> 2 -> 3 represts 321
5 -> 9 - > 8 represents 895
returns 
6 -> 1 -> 2 -> 1 represents 1216
"""


def sum_of_linked_lists(
    linked_list_1: NodeList | None, liked_list_2: NodeList | None
) -> NodeList | None:
    """
    space:O()
    Time:O()
    """
    # we do not return this node ptr, dummy next points to head of result
    cur = dummy = NodeList(0)
    carry = 0
    node_1 = linked_list_1
    node_2 = liked_list_2

    while node_1 is not None or node_2 is not None or carry > 0:
        val_1 = node_1.value if node_1 is not None else 0
        val_2 = node_2.value if node_2 is not None else 0
        sum = val_1 + val_2 + carry
        new_value = sum % 10
        carry = sum // 10
        cur.next = NodeList(new_value)
        cur = cur.next

        if node_1 is not None:
            node_1 = node_1.next
        if node_2 is not None:
            node_2 = node_2.next

    return dummy.next


class TestSumOfLinledList(unittest.TestCase):
    def test_basic_no_carries(self):
        # both empty
        l1 = NodeList.link_vals([])
        l2 = NodeList.link_vals([])
        result = sum_of_linked_lists(l1, l2)
        self.assertEqual(NodeList.to_do_list(result), [])
        # one empty
        l1 = NodeList.link_vals([1])
        l2 = NodeList.link_vals([])
        result = sum_of_linked_lists(l1, l2)
        self.assertEqual(NodeList.to_do_list(result), [1])
        l1 = NodeList.link_vals([])
        l2 = NodeList.link_vals([1, 2])
        result = sum_of_linked_lists(l1, l2)
        self.assertEqual(NodeList.to_do_list(result), [1, 2])
        # equal sizes
        l1 = NodeList.link_vals([1, 2, 3])
        l2 = NodeList.link_vals([4, 5, 6])
        result = sum_of_linked_lists(l1, l2)
        self.assertEqual(NodeList.to_do_list(result), [5, 7, 9])
        # different sizes
        l1 = NodeList.link_vals([1, 2])
        l2 = NodeList.link_vals([4, 5, 6])
        result = sum_of_linked_lists(l1, l2)
        self.assertEqual(NodeList.to_do_list(result), [5, 7, 6])

    def test_basic_with_carries(self):
        # carry in end only
        l1 = NodeList.link_vals([1, 2, 9])
        l2 = NodeList.link_vals([4, 5, 6])
        result = sum_of_linked_lists(l1, l2)
        self.assertEqual(NodeList.to_do_list(result), [5, 7, 5, 1])
        # carry in all stages
        l1 = NodeList.link_vals([9, 9, 9])
        l2 = NodeList.link_vals([3, 5, 6])
        result = sum_of_linked_lists(l1, l2)
        self.assertEqual(NodeList.to_do_list(result), [2, 5, 6, 1])


if __name__ == "__main__":
    unittest.main()
