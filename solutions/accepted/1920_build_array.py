#!/usr/bin/env python3

# https://leetcode.com/problems/build-array-from
# 1920. Build Array from Permutation

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/612242726/
# Time: 116ms (90.74%)
# Mem: 14.6MB (39.18%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


class Solution1:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution1().buildArray ,
            Solution().buildArray ,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([0,2,1,5,3,4], [0,1,2,4,5,3]),
                ([5,0,1,2,3,4], [4,5,0,1,2,3]),


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
