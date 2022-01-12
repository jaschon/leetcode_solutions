#!/usr/bin/env python3
# 2119. A Number After a Double Reversal
# https://leetcode.com/problems/a-number-after-a-double-reversal/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/618544860/
# Time: 24ms (96.09%)
# Mem: 14.1 (89.50%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or str(num)[-1] != '0'

class Solution2:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0

class Solution3:
    def isSameAfterReversals(self, num: int) -> bool:
        return num % 10 != 0 if num != 0 else True

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (526, True),
                (1800, False),
                (0, True),



                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
