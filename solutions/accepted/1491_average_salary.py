#!/usr/bin/env python3
# 1491. Average Salary Excluding the Minimum and Maximum Salary
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/650754220/
# Time: 47ms (42.29%)
# Mem: 13.9MB (36.14%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def average(self, salary: List[int]) -> float:
        low = min(salary)
        high = max(salary)
        
        add = sum(salary) - low - high
        
        return add / (len(salary)-2)


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([4000,3000,1000,2000], 2500.00000),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
