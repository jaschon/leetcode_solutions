#!/usr/bin/env python3
# 1342. Number of Steps to Reduce a Number to Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/621960351/
# Time: 28ms (96.44%)
# Mem: 14.1MB (69.94%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution2:
    def numberOfSteps(self, num: int, c=0) -> int:
        if num == 0:
            return c
        if num % 2 == 0:
            num = num //2
        else:
            num -= 1
        return self.numberOfSteps(num, c+1)

class Solution:
    def numberOfSteps(self, num: int, c=0) -> int:
        if num == 0:
            return c
        return self.numberOfSteps(num//2 if not num % 2 == 0 else num-1, c+1)

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (14, 6),
                (8, 4),
                (123, 12),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
