#!/usr/bin/env python3
# 1051. Height Checker
# https://leetcode.com/problems/height-checker/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/636550973/
# Time: 28ms (98.10%)
# Mem: 14MB (84.88%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len([h for h, s in zip(heights, sorted(heights)) if h != s])
        


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([5,1,2,3,4], 5),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
