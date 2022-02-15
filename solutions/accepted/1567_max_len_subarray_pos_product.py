#!/usr/bin/env python3
# 1567. Maximum Length of Subarray With Positive Product
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/641991261/
# Time: 961ms (38.84%)
# Mem: 28.1 MB (59.16%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

# REMEMBER:
# - a product of 0 turns product to zero, so it resets the count
# - a product of one neg number makes the result neg. a product of two makes it pos. 
# keep track of number of negs
# ---

# keep track of number of negs and pos
# loop through numbers
# if 0, reset vals
# if > 0, add 1 to pos. if negs > 0 add 1 to negs
# get max of result and pos
# if < 0, swap values. if pos > 0 add 1 to pos
# get max of result and pos
# return result

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        result = num_pos = num_neg = 0
        for n in nums:
            if n == 0:
                num_pos = num_neg = 0
            elif n > 0:
                num_pos += 1
                if num_neg:
                    num_neg += 1
                result = max(result, num_pos)
            else:
                num_pos, num_neg = num_neg, num_pos
                num_neg += 1
                if num_pos:
                    num_pos += 1
                result = max(result, num_pos)
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
                ([1,-2,-3,4], 4),
                ([0,1,-2,-3,-4], 3),
                ([-1,-2,-3,0,1], 2),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
