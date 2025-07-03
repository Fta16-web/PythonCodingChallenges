'''
https://leetcode.com/problems/linked-list-cycle-ii/description/
Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.
The number of the nodes in the list is in the range [0, 10^4].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
###### Example ###############
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects 
to the second node.
3 ->2 ->0 -> -4 -|
    |-----------|    -                 |
'''
from typing import List
import unittest 
from Node_module import NodeList
def detectCycle( head)->NodeList | None:
    """
    :type head: ListNode
    :rtype: ListNode
    Floyd’s Tortoise and Hare algorithm
    Detects the start of a cycle in a linked list if it exists.
    Returns the node where the cycle begins, or None if no cycle.
    """
    if not head or not head.next:
        return None
    slow = fast = head
    # Detect possible cycles
    while fast and fast.next:
        slow = slow.next
        fast =fast.next.next
        if fast == slow: 
            # Cycle detected. Find the start of the cycle.
            slow = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
                
            return slow
    return None 

class TestDetectCycles(unittest.TestCase):
    def test_empty_list(self):
        vals =[]
        head= NodeList.link_vals(vals)
        result = detectCycle(head)
        self.assertIsNone(result)
    def test_single_node_list(self):
        vals =[1]
        head= NodeList.link_vals(vals)
        result = detectCycle(head)
        self.assertIsNone(result)   

    def test_multiple_node_list_no_cycle(self):
        vals =[3,2,0,-4]
        head= NodeList.link_vals(vals)
        result = detectCycle(head)
        self.assertIsNone(result)

    def test_multiple_node_list_with_cycle(self):
        vals =[1,2]
        head= NodeList.link_vals(vals)
        tail = NodeList.get_tail(head)
        tail.next = head
        result = detectCycle(head)
        self.assertEqual(result,head)
        # cycle tail to head
        vals =[3,2,0,-4]
        head= NodeList.link_vals(vals)
        tail = NodeList.get_tail(head)
        tail.next = head
        result = detectCycle(head)
        self.assertEqual(result,head)
        # cycle tail to 2nd node 
        head= NodeList.link_vals(vals)
        tail =  NodeList.get_tail(head)
        second_node = head.next
        tail.next = second_node
        result = detectCycle(head)
        self.assertEqual(result,second_node)
        # cycle tail to 3rd node 
        head= NodeList.link_vals(vals)
        tail =  NodeList.get_tail(head)
        third_node = head.next.next
        tail.next = third_node
        result = detectCycle(head)
        self.assertEqual(result,third_node)
        # selfloop / tail loop to inself 
        head= NodeList.link_vals(vals)
        tail =  NodeList.get_tail(head)
        tail.next = tail
        result = detectCycle(head)
        self.assertEqual(result,tail)
if __name__ == '__main__':
    unittest.main()