# Imagine you have a collection"array of positive integers" of  coins with diffrent values.The array could have duplicates.example: [1,2,1,1,3,22]
# you can use each element one time 
#  write a function that returns the minimum amount of change that we cannot create with our coins
from typing import List
import unittest

def get_min_non_constructable_change(coins:List[int]) -> int:
      """
     Time  O(nlgn) for sorting
     Space O(1) if sorting in place
      """
      # Sorting the array of coins to process them in ascending order.
      coins.sort()
      current_change_created = 0
      for coin in coins:
            if coin > current_change_created + 1: # there is a gap which can not be created next
                  return current_change_created + 1
            current_change_created += coin
      return current_change_created + 1
            
class TestGetMinNonConstructableChange(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(get_min_non_constructable_change([1, 2, 5]), 4)
        self.assertEqual(get_min_non_constructable_change([1, 1, 1, 1]), 5)

    def test_edge_cases(self):
        self.assertEqual(get_min_non_constructable_change([]), 1)
        self.assertEqual(get_min_non_constructable_change([1]), 2)
        self.assertEqual(get_min_non_constructable_change([2]), 1)

    def test_duplicates(self):
        self.assertEqual(get_min_non_constructable_change([1, 2, 2, 3, 5]), 14)
        self.assertEqual(get_min_non_constructable_change([1, 1, 1, 1, 2, 2, 2]), 11)

    def test_large_values(self):
        self.assertEqual(get_min_non_constructable_change([1, 1, 3, 7, 22, 45]), 6)
        self.assertEqual(get_min_non_constructable_change([1, 2, 2, 5, 10, 20, 50, 100]), 41)
        
    def test_sequential(self):
        self.assertEqual(get_min_non_constructable_change([1, 2, 3, 4, 5, 6, 7]), 29)
        self.assertEqual(get_min_non_constructable_change([1, 2, 3, 4]), 11)
        
    def test_non_sequential(self):
        self.assertEqual(get_min_non_constructable_change([3, 2, 1, 4]), 11)
        self.assertEqual(get_min_non_constructable_change([1, 3, 1, 3, 2, 5]), 16)
        self.assertEqual(get_min_non_constructable_change([2, 4, 6, 1, 9, 12]), 35)

if __name__ == "__main__":
    unittest.main()     