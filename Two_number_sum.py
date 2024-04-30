
# write an function such that  in accepts an array of distinct integers and another target integer 
# the funtion need to find  a pair of integers in the list such that they sum up to the target integer  
from typing import List, Dict, Optional, Tuple
import unittest

def two_number_sum_one(array : List[int], target_sum : int ) ->Tuple[int,int]:
    """
    Using two for loops 
    Time = O(n^2) | Space = O(1)
    """
    if len(array) <= 1 :
        return []
    for i in range (len(array)-1):
        first_num = array[i]
        for j in range (i+1 , len(array)):
            second_num = array[j]
            if first_num + second_num == target_sum:
                return [first_num, second_num]
    return []
# -----------------------------------------------
def two_number_sum_two(array : List[int], target_sum : int ) ->Tuple[int,int]:
    """
    Using dictionary 
    Time = O(n) | Space = O(n)
    """
    if len(array) <= 1 :
        return []
    nums = {} # declaring dictionary 
    for num in array:
        potential_first_num = target_sum - num
        if potential_first_num in nums:
            return [potential_first_num, num]
        else:
            nums[num] = True
        
    return []
# ----------------------------------------------
def two_number_sum_three(array : List[int], target_sum : int ) ->Tuple[int,int]:
    """
    Using double pointers "left and right indeces" 
    Time = O(nlg(n)) for sorting | Space = O(1)
    """
    if len(array) <= 1 :
        return []
    array.sort() # assuming the sorthing built-in is optimal O(nlg(n)) 
    left_index = 0
    right_index = len(array)-1
    while left_index < right_index:
        first_value = array[left_index]
        second_value = array[right_index]
        current_sum = first_value + second_value 
        if current_sum == target_sum:
            return [first_value, second_value]
        elif current_sum < target_sum:
            left_index += 1
        else:
            right_index -= 1   
    return []
# ----------------------------------------------
class TestTwoNumberSum(unittest.TestCase):
    def test_empty_array(self):
        array = []
        target_sum = 7
        expected = []
        self.assertEqual(two_number_sum_one(array,target_sum), expected)
        self.assertEqual(two_number_sum_two(array,target_sum), expected)
        self.assertEqual(two_number_sum_three(array,target_sum), expected)
        
    def test_array_of_len_one(self):    
        array =[7]
        target_sum = 7
        expected = []
        self.assertEqual(two_number_sum_one(array,target_sum), expected)
        self.assertEqual(two_number_sum_two(array,target_sum), expected)
        self.assertEqual(two_number_sum_three(array,target_sum), expected)
        
    def test_pair_exist(self):
        # array of len two  
        array =[-1, 15]
        target_sum = 14
        expected = [-1, 15]
        self.assertEqual(two_number_sum_one(array,target_sum), expected)
        self.assertEqual(two_number_sum_two(array,target_sum), expected)
        self.assertEqual(two_number_sum_three(array,target_sum), expected)
        
        # array of len more than two
        array = [100, -1, 5, 10 ,89 , 1001]
        target_sum = 1000
        expected = [-1, 1001]
        self.assertEqual(two_number_sum_one(array,target_sum), expected)
        self.assertEqual(two_number_sum_two(array,target_sum), expected)
        self.assertEqual(two_number_sum_three(array,target_sum), expected)
        
        
    def test_pair_not_exist(self):
        # array of len two 
        array =[-1, 15]
        target_sum = 7
        expected = []
        self.assertEqual(two_number_sum_one(array,target_sum), expected)
        self.assertEqual(two_number_sum_two(array,target_sum), expected)
        self.assertEqual(two_number_sum_three(array,target_sum), expected)
        
        # array of len more than two
        array = [100, -1, 5, 10 ,89 , 1001]
        target_sum = 7
        expected = []
        self.assertEqual(two_number_sum_one(array,target_sum), expected)
        self.assertEqual(two_number_sum_two(array,target_sum), expected)
        self.assertEqual(two_number_sum_three(array,target_sum), expected)
        
# ---------------------------------
if __name__ == '__main__':
     unittest.main()
     
    
    