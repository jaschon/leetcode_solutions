#!/usr/bin/env python3
# 1356. Sort Integers by The Number of 1 Bits
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/653410837/
# Time: 79ms (78.00%)
# Mem: 14MB (98.04%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr.sort(key=lambda x: bin(x).count("1"))
        return arr


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([0,1,2,3,4,5,6,7,8], [0,1,2,4,8,3,5,6,7]),
                ([1024,512,256,128,64,32,16,8,4,2,1], [1,2,4,8,16,32,64,128,256,512,1024]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
