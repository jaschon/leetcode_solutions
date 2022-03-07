#!/usr/bin/env python3

# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/655225680/
# Time: 1655 ms (15.52%)
# Mem: 17.5 MB (73.16%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])



if __name__ == "__main__":
    pass

