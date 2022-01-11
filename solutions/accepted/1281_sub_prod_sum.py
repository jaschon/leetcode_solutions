#!/usr/bin/env python3
# 1281. Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/617738075/
# Time: 20ms (98.79%)
# Mem: 14.2 MB (42.29%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, add = 1,0
        for d in list(str(n)):
            d = int(d)
            prod *= d
            add += d
        return prod - add



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (234, 15),
                (4421, 21),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
