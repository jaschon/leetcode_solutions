#!/usr/bin/env python3
# 2154. Keep Multiplying Found Values by Two
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/


# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/631834256/
# Time: 60ms (98.23%)
# Mem: 14.2 MB (26.19%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        for i in nums:
            if original in nums:
                original *= 2
            else:
                break
        return original

from collections import Counter
class Solution2:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = Counter(nums)
        while original in nums:
            original *= 2
        return original

class Solution3:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = Counter(nums)
        for num in nums:
            if original in nums:
                original *= 2
            else:
                break
        return original



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([5,3,6,1,12], 3, 24),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
