#!/usr/bin/env python3
# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/636692671/
# Time: 160ms (95.95%)
# Mem: 15.6MB (26.96%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j,n in enumerate(nums):
            if n != 0:
                nums[i], nums[j] = n, nums[i]
                i += 1
        return nums


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([0,1,0,3,12].copy(), [1,3,12,0,0]),
                ([0], [0].copy()),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
