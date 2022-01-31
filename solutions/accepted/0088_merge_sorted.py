#!/usr/bin/env python3
# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/629110466/
# Time: 28ms (98.39%)
# Mem: 13.9 MB (99.97%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m > 0 and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m = m-1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        return nums1




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                # ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
                # ([1], 1, [], 0, [1]),
                # ([0], 0, [1], 1, [1]),
                ([2,0], 1, [1], 1, [1,2]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
