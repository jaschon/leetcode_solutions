#!/usr/bin/env python3
# 268. Missing Number
# https://leetcode.com/problems/missing-number/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/628398085/
# Time: 128ms (87.33%)
# Mem: 16.5MB (5.72%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

#SLOW
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        largest = max(nums)
        if largest == len(nums)-1:
            return largest+1
        for n in range(0, largest):
            if not n in nums:
                return n


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        diff = set(range(0,len(nums))) - set(nums)
        if not diff:
            return len(nums)
        else:
            return next(iter(diff))
        
if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([3,0,1], 2),
                ([0,1], 2),
                ([9,6,4,2,3,5,7,0,1], 8),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
