#!/usr/bin/env python3
# 231. Power of Two
# https://leetcode.com/problems/power-of-two/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/622600165/
# Time: 24ms (96.84%)
# Mem: 14.4MB (6.99%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return not (n & (n - 1))



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (1, True),
                (3, False),
                (16, True),
                (6, False),
                (27, False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
