#!/usr/bin/env python3
# 1837. Sum of Digits in Base K
# https://leetcode.com/problems/sum-of-digits-in-base-k/

# Easy

# Accepted Solution 2
# Result: https://leetcode.com/submissions/detail/634541840/
# Time: 28ms (89.575)
# Mem: 13.9MB (95.11%)

# Accepted Solution 1
# Result: https://leetcode.com/submissions/detail/634546312/
# Time: 24ms (98.72%)
# Mem: 13.8 MB (95.11%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution2:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n>0:
            result += n%k
            n //=k
        return result

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def base(n,k, result):
            if not n: return result
            return base(n//k, k, result + n%k)
        return base(n,k,0)
        
if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (34,6,9),
                (10,10,1),

                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
