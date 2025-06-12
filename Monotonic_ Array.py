'''
An array is monotonic if it is either monotone increasing or monotone decreasing. 
An array is monotone increasing if all its elements from left to right are non-decreasing.
An array is monotone decreasing if all  its elements from left to right are non-increasing.
Given an integer array return true if the given array is monotonic, or false otherwise.
'''
from typing import List
import unittest
def is_monotonic(array :List [int] ) -> bool:
   '''
   Time = O(n), space = O(1)
    case first elemenet > last element => array MD or not monotonic
    case first elemenet < last element => array MI or not monotonic
    case first elemenet == last element => all same elements or not monotonic
   '''
   n = len(array)
   if (n < 3 ):
      return True
   first = array[0]
   last = array[n-1]
   if first > last: #MD
       for k in range(n-1):
           if array[k]<array[k+1]:
               return False
   elif first == last:
       for k in range(n-1):
           if array[k] != array[k+1]:
               return False    
   else:
       for k in range(n-1):
           if array[k]> array[k+1]:
               return False
   return True    
       
def is_monotonic_2(array :List [int] ) -> bool:
    n = len(array)
    MD = MI = True
    for k in range(n-1):
           if array[k]> array[k+1]:
               MD = False
            if 

  
   
class TestIsMonotonic(unittest.TestCase):
    def test_edge_cases(self):
        # Empty array
        self.assertTrue(is_monotonic([]))
        # Single element
        self.assertTrue(is_monotonic([5]))
        # two elements
        self.assertTrue(is_monotonic([1,1]))
        self.assertTrue(is_monotonic([1,2]))
        self.assertTrue(is_monotonic([2,1]))
    def test_multiple_elements(self):
        # Multiple elements (Optional additions for robustness)
        self.assertTrue(is_monotonic([1, 2, 2, 3]))
        self.assertTrue(is_monotonic([5, 5, 5, 5]))
        self.assertTrue(is_monotonic([9, 7, 5, 3]))
        self.assertFalse(is_monotonic([1, 3, 2]))
        self.assertFalse(is_monotonic([1, -3, 2]))
        self.assertFalse(is_monotonic([1, 1, 1]))
        self.assertTrue(is_monotonic(list(range(100000))) )  # Increasing
        self.assertTrue(is_monotonic(list(range(100000, 0, -1))))  # Decreasing
    
if __name__ == '__main__':
    unittest.main()