#!/usr/bin/env python3
# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/646968017/
# Time: 91ms (38.61%)
# Mem: 14MB (17.06%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cmp = ""
        memo = {}
        i = 0
        while i < len(nums):
            if nums[i] == cmp and memo.get(nums[i], 0) > 1:
                nums.pop(i)
            else:
                cmp = nums[i]
                memo[nums[i]] = memo.get(nums[i],0) + 1
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
                ([1,1,1,2,2,3], 5, nums = [1,1,2,2,3,_]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
