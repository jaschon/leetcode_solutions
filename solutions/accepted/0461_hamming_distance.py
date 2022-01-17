#!/usr/bin/env python3
# 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/621922896/ 
# Time: 32ms (56.95%)
# Mem: 14.3 MB

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = f'{x:032b}'
        y = f'{y:032b}'
        result = 0
        for i in range(len(x)):
            result += 1 if x[i] != y[i] else 0
        return result



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (1, 4, 2),
                (3, 1, 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
