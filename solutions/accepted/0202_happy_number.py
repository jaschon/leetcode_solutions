#!/usr/bin/env python3
# 202. Happy Number
# https://leetcode.com/problems/happy-number/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/618633069/
# Time: 36ms (68.32%)
# Mem: 14.4MB (15.94%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List

### Note: repeats if n = 2, 3 or 4

### ADD SOLUTION CLASS HERE 
class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 2:
            return n == 1
        if n < 5
            return False
        return self.isHappy(sum([int(i)**2 for i in str(n)]))
        



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (19, True),
                (9, False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
