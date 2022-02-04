#!/usr/bin/env python3
# 525. Contiguous Array
# https://leetcode.com/problems/contiguous-array/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/634497541/
# Time: 860ms (82.51%)
# Mem: 19.6MB (13.20%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapper = {0: -1, 1: 1}
        counter = {0: -1}
        max_len = 0
        count = 0
        for i, num in enumerate(nums):
            count += mapper[num]
            if count in counter:
                max_len = max(max_len, i - counter[count])
            else:
                counter[count] = i
        return max_len

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([0,1], 2),
                ([0,1,0], 2),
                ([0,0,1,0,0,0,1,1], 6),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
