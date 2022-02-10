#!/usr/bin/env python3
# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/638702451/
# Time: 28ms (93.87%)
# Mem: 13.9MB (95.12%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

# same as house robber problem #1, but run it twice.
# which is larger? skipping house 1 or skipping the last house

class Solution:
    def _rob(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        flip = False
        for n in nums:
            if flip:
                even = max(even + n, odd)
            else:
                odd = max(odd + n, even)
            flip = not flip
        return max(even, odd)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] #need this for 1 element lists
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([2,3,2], 3),
                ([1,2,3,1], 4),
                ([1,2,3], 3),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
