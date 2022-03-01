#!/usr/bin/env python3
# 1523. Count Odd Numbers in an Interval Range
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/650752438/
# Time: 47ms (32.85%)
# Mem: 13.8MB *74.37%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# number of odd is half of high-low
# add an extra one if any are odd
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = (high-low) //2

        if low % 2 != 0 or high %2 != 0:
            result += 1

        return result




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (3,7, 3),
                (8,10, 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
