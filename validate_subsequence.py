
# -------------------------
# you can create subsequences of a list by removing some or no element 
# from the list without changing the order of remaining elements
# write a function such that it accepts  two  arrays and 
# determines if array provided in the second argument is a valid
# subsequence of array provided in the first argument 
# https://en.wikipedia.org/wiki/Subsequence
# Time = O(n) | space = O(1)
# ------------------------
import unittest
from typing import List, Any
def is_subsequence_one (seq : List[Any], potential_subseq :List[Any])-> bool:
    """
    Determines if the array `subseq` is a valid subsequence of the array `seq`.
    Returns:
    bool: True if `subseq` is a subsequence of `seq`, False otherwise.
    """
    if len(potential_subseq) > len(seq):
        return False
    seq_index = 0
    subseq_index = 0
    while seq_index < len(seq) and subseq_index < len (potential_subseq):
        if seq[seq_index] == potential_subseq[subseq_index] :
            subseq_index += 1
        seq_index += 1
    return subseq_index == len(potential_subseq)
# ----------------------------------
def is_subsequence_two (seq : List[Any], potential_subseq :List[Any])-> bool:
    """
    Determines if the array `subseq` is a valid subsequence of the array `seq`.
    Returns:
    bool: True if `subseq` is a subsequence of `seq`, False otherwise.
    """
    if len(potential_subseq) > len(seq):
        return False
    seq_index = 0
    for number in seq:
        if seq_index == len(potential_subseq):
          break;
        if number == potential_subseq[seq_index]:
            seq_index += 1
    return seq_index == len(potential_subseq)

class testISSubsequence(unittest.TestCase):
    def test_basic_subsequence(self):
        seq = [1, 2, -1, 5, 90, 0]
        sub_seq = [1, 2, 5, 90, 0]
        self.assertTrue(is_subsequence_one(seq,sub_seq))
        self.assertTrue(is_subsequence_two(seq,sub_seq))
        
    def test_at_front_subsequence(self):
        seq = [1, 2, -1, 5, 90, 0]
        sub_seq = [1, 2, -1]
        self.assertTrue(is_subsequence_one(seq,sub_seq))
        self.assertTrue(is_subsequence_two(seq,sub_seq))
        
    def test_at_end_subsequence(self):
        seq = [1, 2, -1, 5, 90, 0]
        sub_seq = [5, 90, 0]
        self.assertTrue(is_subsequence_one(seq,sub_seq))
        self.assertTrue(is_subsequence_two(seq,sub_seq))
    def test_one_element_subsequence(self):
        seq = [1]
        sub_seq = [1]
        self.assertTrue(is_subsequence_one(seq,sub_seq))
        self.assertTrue(is_subsequence_two(seq,sub_seq))
        
        seq = [1, 2, 3]
        sub_seq = [3]
        self.assertTrue(is_subsequence_one(seq,sub_seq))
        self.assertTrue(is_subsequence_two(seq,sub_seq))
        
    def test_empty_subsequence(self):
        #both empty
        seq = []
        sub_seq = []
        self.assertTrue(is_subsequence_one(seq,sub_seq))
        self.assertTrue(is_subsequence_two(seq,sub_seq))
        # only sub empty
        seq = [1, 2, 3]
        sub_seq = []
        self.assertTrue(is_subsequence_one(seq,sub_seq))
        self.assertTrue(is_subsequence_two(seq,sub_seq))
        
    def test_not_longer_subsequence(self):
        seq = [-1, -6, 1, 100]
        sub_seq = [-1, -6, 1, 100, -8]
        self.assertFalse(is_subsequence_one(seq,sub_seq))
        self.assertFalse(is_subsequence_two(seq,sub_seq))
        
    def test_not_order_subsequence(self):
        seq = [-1, -6, 1, 100]
        sub_seq = [-1, 100, 1]
        self.assertFalse(is_subsequence_one(seq,sub_seq))
        self.assertFalse(is_subsequence_two(seq,sub_seq))
    
    def test_not_present_subsequence(self):
        seq = [-1, -6, 1, 100]
        sub_seq = [5]
        self.assertFalse(is_subsequence_one(seq,sub_seq))
        self.assertFalse(is_subsequence_two(seq,sub_seq))
        
    def test_wiki_sample(self):
        SEQ1 = "ACGGTGTCGTGCTATGCTGATGCTGACTTATATGCTA"
        SEQ2 = "CGTTCGGCTATGCTTCTACTTATTCTA"
        seq = list(SEQ1) 
        sub_seq = list(SEQ2)
        self.assertTrue(is_subsequence_one(seq,sub_seq))
        self.assertTrue(is_subsequence_two(seq,sub_seq))
        


if __name__ == '__main__':
    unittest.main()
            
     
    

