#!/usr/bin/env python3

# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/619224064/
# Time: 148ms (27.47%)
# Mem: 15.7MB (6.98%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cmp = ""
        i = 0
        while i < len(nums):
            if nums[i] == cmp:
                nums.pop(i)
            else:
                cmp = nums[i]
                i += 1
        return i


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                # ([1,1,2], 2),
                ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4,'_','_','_','_','_']),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])
            arr = e[0].copy()

            test(funct, e[-1], arr)
            # timer(funct, 5, arr.copy())


            print()
