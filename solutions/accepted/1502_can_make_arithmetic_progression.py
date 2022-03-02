#!/usr/bin/env python3

# 1502. Can Make Arithmetic Progression From Sequence
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652083197/
# Time: 65ms (37.02%)
# Mem: 14MB (58.43%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        const = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if (arr[i+1]-arr[i]) != const:
                return False
        return True


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([3,5,1], True),
                ([1,2,4], False),
                ([1], True),
                ([], True),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
