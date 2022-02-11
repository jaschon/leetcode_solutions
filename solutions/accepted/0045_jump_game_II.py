#!/usr/bin/env python3
# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/639440808/
# Time: 232ms (47.82%)
# Mem: 14.8 MB (99.53%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 


class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = left = right = 0
        length = len(nums) - 1

        while right < length:
            most = 0
            for i in range(left, right+1): 
                #check all the values between left and right
                #and find largest
                #have to add index to num[i] value!
                most = max(most, nums[i]+i)
            left = right + 1
            right = most
            jumps += 1

        return jumps



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([2,3,1,1,4], 2),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
