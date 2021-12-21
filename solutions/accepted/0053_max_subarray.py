#!/usr/bin/env python3
# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/605077615/
# Time: 656ms (98.13%)
# Mem: 28.9MB (10.83%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total, longest = -10000, -10000
        for n in nums:
            total = total if total > 0 else 0
            total += n
            longest = longest if longest > total else total
        return longest

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().maxSubArray  ,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([-2,1,-3,4,-1,2,1,-5,4], 6),
                ([5,4,-1,7,8], 23),
                ([1], 1),
                ([-2, -1], -1),


                ):

            funct = f
            print()

            ### ADD EXTRA PARAM AFTER e[0]...
            test(funct, e[-1], e[0])

            ### NODE VERSION OF TEST
            # test_node(funct, cmp, val)

            timer(funct, e[0])
            # timer_amt(funct, 10, e[0])

            print()
