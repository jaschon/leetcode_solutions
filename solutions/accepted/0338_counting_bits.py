#!/usr/bin/env python3
# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/623310021/
# Time: 94ms (59.45%)
# Mem: 21.1MB

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [f'{i:0b}'.count('1') for i in range(n+1)]

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (2, [0,1,1]),
                (5, [0,1,1,2,1,2]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
