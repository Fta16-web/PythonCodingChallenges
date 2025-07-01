# you are given an array of positive integers NO Zeros or floats 
# Each integer represents time consumption of an query 
# Assume you can do one query at a time
# find the order which gives us the minum waiting time for queries(Queries start)
# Ex: [3,2,1,2,6] is given we do queries in order 6 -> 1 -> 2 -> 2 -> 3
# 6 (Time 0 ) -> 1 (Time 0+6) -> 2 (Time 6+1)-> 2 (Time 7+2)-> 3 (Time 9+2) = 33 NOT OPTIMAL ORDER it should be 17
# You do not return the order just return the min
from typing import List
import unittest
def get_minimum_waiting_time(queries:List)->int:
    '''
    Greedy approach
    Time= O(OlgN) for sorting 
    Space = O(1) in place sorting 
    '''
    queries.sort()
    total_waiting_time = 0
    for i in range(len(queries)):
        queries_left = len(queries) - (i + 1)
        total_waiting_time += queries[i] * queries_left
    return total_waiting_time

class TestGetMinimumWaitingTime(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(get_minimum_waiting_time([3, 2, 1, 2, 6]), 17)

    def test_case_2(self):
        self.assertEqual(get_minimum_waiting_time([1, 2, 3]), 4)

    def test_case_3(self):
        self.assertEqual(get_minimum_waiting_time([5]), 0)

    def test_case_4(self):
        self.assertEqual(get_minimum_waiting_time([4, 3, 1, 2]), 10)

if __name__ == '__main__':
    unittest.main()