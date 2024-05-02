
# create a function that accepts a sorted array in ascending order 
# and generates an new array such that the elements are the squares of  
# provided element and is in ascendin order

from typing import List
import unittest

def get_sorted_square_array_one( array :List [int] ) -> List[int]:
    """
    Brute force, naive approach
    Time = O(nlg(n)) in sorting  | Space = O(n)
    """
    if any(array[i] > array[i+1] for i in range(len(array)-1)):
        raise ValueError("Input array must be sorted in ascending order.")
    squares =[] 
    for num in array:
        squares.append(num * num)
    return sorted(squares) # do not use list.sorted().it sorts in place and returns None
        
        
     
def get_sorted_square_array_two( array :List [int] ) -> List[int]:
    """
    using two pointers 
    Time = O(n) | Space = O(n)
    """
    if any(array[i] > array[i+1] for i in range(len(array)-1)):
        raise ValueError("Input array must be sorted in ascending order.") 
     
    if len(array) == 0:
        return []
    start_index = 0
    end_index = len(array) - 1
    squares =[0] * (end_index + 1)
    squares_index = end_index
    while end_index >= start_index:
        start_val = array[start_index] 
        end_val = array[end_index]
        if start_val * start_val > end_val * end_val:
            val = start_val * start_val
            start_index += 1
        else:
            val = end_val * end_val
            end_index -= 1
        squares[squares_index] = val
        squares_index -= 1
    return squares
class TestGetSortedSquareArray(unittest.TestCase):
    def test_normal_cases(self):
        #single element 
        array = [-3]
        expected = [9]
        self.assertEqual(get_sorted_square_array_one(array),expected)
        self.assertEqual(get_sorted_square_array_two(array),expected)
        #positive element
        array = [4, 5, 6]
        expected = [16, 25, 36]
        self.assertEqual(get_sorted_square_array_one(array),expected)
        self.assertEqual(get_sorted_square_array_two(array),expected)
        # negative elements
        array = [-6, -4, -2]
        expected = [4, 16 ,36]
        self.assertEqual(get_sorted_square_array_one(array),expected)
        self.assertEqual(get_sorted_square_array_two(array),expected)
        # mixed elements
        array = [-6, -2, 4, 10]
        expected = [4, 16, 36, 100]
        self.assertEqual(get_sorted_square_array_one(array),expected)
        self.assertEqual(get_sorted_square_array_two(array),expected)
        
    def test_edge_cases(self):
        # empty array
        array = []
        expected = []
        self.assertEqual(get_sorted_square_array_one(array),expected)
        self.assertEqual(get_sorted_square_array_two(array),expected)
        # all zero elements 
        array = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        self.assertEqual(get_sorted_square_array_one(array),expected)
        self.assertEqual(get_sorted_square_array_two(array),expected)
        # all large numbers 
        array = [1000, 1000000, 1000000]
        expected = [1000000, 1000000000000, 1000000000000]
        self.assertEqual(get_sorted_square_array_one(array),expected)
        self.assertEqual(get_sorted_square_array_two(array),expected)
    def test_change_array(self):
        #array after passing to function should not change
        array = [1, 2, 3]
        expected =[1, 2, 3]
        square = get_sorted_square_array_one(array)
        square = get_sorted_square_array_two(array)
        assert array == expected
        
    # def test_unsorted_input_raises_exception(self):
    #     unsorted_array = [4, 1, 3, 2]
    #     with self.assertRaises(ValueError) as context_one:
    #         get_sorted_square_array_one(unsorted_array)
    #     self.assertIn("Input array must be sorted in ascending order.", str(context_one.exception))

    #     with self.assertRaises(ValueError) as context_two:
    #         get_sorted_square_array_two(unsorted_array)
    #     self.assertIn("Input array must be sorted in ascending order.", str(context_two.exception))
#------------------------

if __name__ == '__main__':
    unittest.main()



