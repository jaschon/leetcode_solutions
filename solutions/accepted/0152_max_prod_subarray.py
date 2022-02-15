#!/usr/bin/env python3
# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/641972922/
# Time: 88ms (74.59%)
# Mem: 14.4 MB (73.43%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# loop through numbers
# keep running total of current max and current min product
# update result each time
# return result

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        cur_min = cur_max = 1
        if not nums: return result
        for n in nums:
            stuff = [n, n * cur_min, n * cur_max]
            cur_min = min(stuff)
            cur_max = max(stuff)
            result = max(result, cur_max)
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
                ([2,3,-2,4], 6),
                ([-2,0,-1], 0),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
