#!/usr/bin/env python3
# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/615023958/
# Time: 56ms (79.31%)
# Mem: 14.5MB (13.28%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cmp = sorted(nums)
        return [cmp.index(n) for n in nums]


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([8,1,2,2,3], [4,0,1,1,3]),
                ([6,5,4,8], [2,1,0,3]),
                ([7,7,7,7], [0,0,0,0]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
