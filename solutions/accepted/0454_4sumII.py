#!/usr/bin/env python3
# 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/633753879/
# Time: 973ms (47.88%)
# Mem: 14.1MB (98.30%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# sum first two indexes and put them in a dict
# then check all sums of the last two indexes and see if the reverse (* -1) value is in the dict
# if so, add 1 to result

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sums = {}
        result = 0
        for n1 in nums1:
            for n2 in nums2:
                sums[n1+n2] = sums.get(n1+n2, 0) + 1
        for n3 in nums3:
            for n4 in nums4:
                result += sums.get(-1*(n3+n4), 0)
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
                ([1,2], [-2,-1], [-1,2], [0,2], 2),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
