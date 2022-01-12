#!/usr/bin/env python3
# 1486. XOR Operation in an Array
# https://leetcode.com/problems/xor-ope

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/618528038/
# Time: 32ms (66.23%)
# Mem: 14.5 MB (16.23%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from functools import reduce
from operator import xor
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(xor, [start+2*i for i in range(n)])



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (5,0,8),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
