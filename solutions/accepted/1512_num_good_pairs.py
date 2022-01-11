#!/usr/bin/env python3
# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/617732061/
# Time: 36ms (52.45%)
# Mem: 14.1MB (73.89%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        length = len(nums)
        if length == 1: return result
        for i in range(length):
            for j in reversed(range(length)):
                if i == j: break
                if nums[i] == nums[j] and i < j:
                    result += 1
        return result




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,3,1,1,3], 4),
                ([1,1,1,1], 6),
                ([1,2,3], 0),
                ([1], 0),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
