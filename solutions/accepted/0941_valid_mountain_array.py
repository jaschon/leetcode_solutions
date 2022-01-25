#!/usr/bin/env python3
# 941. Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/627705808/
# Time: 192ms (95.90%)
# Mem: 15.5MB (87.22%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        peak = False
        inc = False
        prev = arr[0]
        for i in range(1, len(arr)):
            if not peak and arr[i] > prev:
                prev = arr[i]
                inc = True
            elif not peak and arr[i] < prev:
                peak = True
                prev = arr[i]
                if not inc:
                    return False
            elif peak and arr[i] < prev:
                prev = arr[i]
            else:
                return False
        return peak and inc




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([2,1], False),
                ([3,5,5], False),
                ([0,3,2,1], True),
                ([0,2,3,3,5,2,1,0], False),
                ([0,2,3,5,2,1,0], True),
                ([0,2,3,5,2,1,1], False),
                ([0,1,2,3,4,5,6,7,8,9], False),
                ([9,8,7,6,5,4,3,2,1,0], False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
