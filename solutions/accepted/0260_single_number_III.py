#!/usr/bin/env python3
# 260. Single Number III
# https://leetcode.com/problems/single-number-iii/
# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/619234170/
# Time: 74ms (37.77%)
# Mem: 16.3MB (12.12%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums).most_common()
        return [c[-1][0], c[-2][0]]



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,1,3,2,5], [3,5]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
