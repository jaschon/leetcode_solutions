#!/usr/bin/env python3
# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/
# Medium


# Accepted
# Result: https://leetcode.com/submissions/detail/599505145/
# Time: 28ms (86.40)
# Mem: 14.3MB (53.10%)

import sys
sys.path.insert(0,'..')
from _helper import *


### ADD SOLUTION CLASS HERE 

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        
        

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().myPow,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (2.00000, 10, 1024.00000),
                ):

            funct = f
            print()

            ### ADD EXTRA PARAM AFTER e[0]...
            test(funct, e[-1], e[0], e[1])

            ### NODE VERSION OF TEST
            # test_node(funct, cmp, val)

            timer(funct, e[0], e[1])
            # timer_amt(funct, 10, e[0])

            print()
