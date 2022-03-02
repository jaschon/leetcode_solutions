#!/usr/bin/env python3
# 1822. Sign of the Product of an Array
# https://leetcode.com/problems/sign-of-the-product-of-an-

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652077509/
# Time: 63ms (82.42%)
# Mem: 14.1MB (50.59%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from functools import reduce
from operator import mul
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = reduce(mul, nums)
        if result == 0:
            return 0
        return 1 if result > 0 else -1



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([-1,-2,-3,-4,3,2,1], 1),
                ([1,5,0,2,-3], 0),
                ([-1,1,-1,1,-1], -1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
