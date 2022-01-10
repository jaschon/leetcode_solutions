#!/usr/bin/env python3
# 258. Add Digits
# https://leetcode.com/problems/add-digits/

# Easy

# Accepted
# Result:  https://leetcode.com/submissions/detail/617051157/
# Time: 60ms (6.24%)
# Mem: 14.2MB (74.61%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        return self.addDigits(sum(int(n) for n in str(num)))

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (38, 2),
                (0,0),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
