#!/usr/bin/env python3
# 2169. Count Operations to Obtain Zero
# https://leetcode.com/problems/count-operations-to-obtain-zero/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/642166728/
# Time: 142ms (61.28%)
# Mem: 13.9MB (65.99%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution2:
    def countOperations(self, num1: int, num2: int, count=0) -> int:
        if num1 == 0 or num2 == 0:
            return count
        elif num1 >= num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
        return self.countOperations(num1, num2, count+1)

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            count +=1
        return count

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (2,3,3),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
