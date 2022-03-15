#!/usr/bin/env python3
# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/657995769/
# Time: 5732ms (32.75%)
# Mem: 14MB (81.51%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def numSquares(self, n: int) -> int:

        #make memo
        memo = [n]*(n+1)
        memo[0] = 0

        #loop through digits till value N (start at 1)
        for digit in range(1,n+1):
            #loop from beginning, checking if the digit-squared value is less than the cached value
            for square in range(1,digit+1):
                key = digit-(square**2)
                if key < 0:
                    break
                if 1+memo[key] < memo[digit]:
                    memo[digit] = 1 + memo[key]

        return memo[n]


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
