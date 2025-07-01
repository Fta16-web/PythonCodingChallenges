'''
you are given two lists of integers representing the height of two groups of students 
you need to implement an function such that return true if we can put each group in line 
such that that the group on backline are not shorter than group in frontline
ex:
red_shirt = [5,8,1,3,4]
blue_shirt = [6,9,2,4,5]
true becuse 
    b:9, 6, 5, 4, 2
    r:8, 5, 4, 3, 1
'''

import unittest
from typing import List 
def class_photos(red_shirt_height:List[int], blue_shirt_height:list[int]):
    '''
    Returns True if one group can stand behind the other such that
    each student in the back row is not shorter (>=) than the one in front.
    Allows equal heights.
    Time: O(N log N), Space: O(1)
    '''
    if len(blue_shirt_height) != len(red_shirt_height):
        return False
    red_shirt_height.sort(reverse=True)
    blue_shirt_height.sort(reverse=True)
    back_line = 'RED' if red_shirt_height[0] > blue_shirt_height[0] else 'BLUE'
    for i in range(len(blue_shirt_height)):
        if(back_line == 'BLUE'):
            if (blue_shirt_height[i]< red_shirt_height[i]):
                return False
        else:
            if (blue_shirt_height[i]> red_shirt_height[i]):
                return False

    return True

class classPhotoesTest(unittest.TestCase):
    
    def test_case_1(self):
        self.assertTrue(class_photos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))

    def test_case_2(self):
        self.assertTrue(class_photos([6, 9, 2, 4, 5], [5, 8, 1, 3, 4]))

    def test_case_3(self):
        self.assertTrue(class_photos([6, 9, 2, 4, 5], [6, 9, 2, 4, 5]))  

    def test_case_4(self):
        self.assertTrue(class_photos([1, 2, 3], [4, 5, 6]))

    def test_case_5(self):
        self.assertTrue(class_photos([4, 5, 6], [1, 2, 3]))

    def test_case_6(self):
        self.assertTrue(class_photos([4, 5, 6], [4, 5, 6]))  

    def test_case_7(self):
        self.assertFalse(class_photos([4, 5, 6], [4, 5])) 

    def test_case_8(self):
        self.assertFalse(class_photos([4, 5, 6], [5, 5, 5])) 

    
if __name__ == "__main__":
    unittest.main()