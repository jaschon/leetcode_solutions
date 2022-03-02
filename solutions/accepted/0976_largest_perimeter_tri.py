#!/usr/bin/env python3
# 976. Largest Perimeter Triangle
# https://leetcode.com/problems/largest-perimeter-triangle/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/651480686/
# Time: 268ms (52%)
# Mem: 15.5MB (64.22%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. sort list
# 2. loop to check if side A + side b is greater than side C
# 3. return perimeter else 0

class Solution2:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-3, -1, -1):
            if (nums[i] + nums[i+1]) > nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([2,1,2], 5),
                ([1,2,1], 0),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
