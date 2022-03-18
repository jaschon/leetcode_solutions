#!/usr/bin/env python3
# 343. Integer Break
# https://leetcode.com/problems/integer-break/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/660718491/
# Time: 51ms (43.61%)
# Mem: 13.9 MB (75.75%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def integerBreak(self, n: int) -> int:
               
        def loop(num):
            
            if num in self.memo:
                return self.memo[num]
            
            if num == 1:
                return num
            
            result = num if n != num else 0 #<--gotcha! needs to break up if not first run, else start at 0
            
            for i in range(1, num):
                result = max(result, loop(i)*loop(num-i))
                
            self.memo[num] = result
            return self.memo[num]
        
        self.memo = {}
        return loop(n)


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (2, 1),
                (10, 36),


                ):

            # funct = inspect.getmembers(f)[-1][1]
            funct = f.integerBreak

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
