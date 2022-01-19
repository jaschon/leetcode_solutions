#!/usr/bin/env python3
# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/623364919/
# Time: 224ms (81.12%)
# Mem: 16.3MB (12.70%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(i**2 for i in nums)

class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])

class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x: x**2, nums))

class Solution3:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(i*i for i in nums)

class Solution4:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i*i for i in nums])

class Solution5:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([pow(i,2) for i in nums])

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution5(),
            Solution(),
            Solution1(),
            Solution2(),
            Solution3(),
            Solution4(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([-7,-3,2,3,11], [4,9,9,49,121]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 100, *e[:-1])


            print()
