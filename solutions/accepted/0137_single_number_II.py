#!/usr/bin/env python3
# 137. Single Number II
# https://leetcode.com/problems/single-number-ii/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/619231159/
# Time: 56ms (83.40%)
# Mem: 16MB (40.55%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([0,1,0,1,0,1,99], 99),
                ([2,2,3,2], 3),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
