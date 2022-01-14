#!/usr/bin/env python3
# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/619861056/
# Time: 32ms (63.11%)
# Mem: 14.2 MB (72.74%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

#NOTE: Needs cache. Will timeout without it!

from functools import cache
@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        return fib(n+1)


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (2,2),
                (3, 3),
                (38, 38),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
