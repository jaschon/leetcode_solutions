#!/usr/bin/env python3
# 2006. Count Number of Pairs With Absolute Difference K
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/617748832/
# Time: 397ms (8.83%)
# Mem: 14.3MB (54.51%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        result = 0
        length = len(nums)
        if length == 1: return result
        for i in range(length):
            for j in reversed(range(length)):
                if i == j: break
                if abs(nums[i] - nums[j]) == k:
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
                ([1,2,2,1], 1, 4),
                ([1,3], 3, 0),
                ([3,2,1,5,4], 2, 3),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
