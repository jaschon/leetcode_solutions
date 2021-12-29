#!/usr/bin/env python3
# https://leetcode.com/problems/concatenation-of-array/
# 1929. Concatenation of Array


# Easy

# Accepted (Solution 2)
# Result: https://leetcode.com/submissions/detail/609336412/
# Time: 142ms (5.24%)
# Mem: 14.6 MB (20.45%)

# Accepted (Solution 1)
# Result: https://leetcode.com/submissions/detail/609339875/
# Time: 117ms (10.61%)
# Mem: 14.6 MB (20.45%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums*2

from itertools import chain
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return list(chain(nums, nums))

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().getConcatenation  ,
            Solution2().getConcatenation  ,
            Solution1().getConcatenation  ,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,1], [1,2,1,1,2,1]),



                ):

            funct = f
            print()

            ### ADD EXTRA PARAM AFTER e[0]...
            test(funct, e[-1], e[0])

            ### NODE VERSION OF TEST
            # test_node(funct, cmp, val)

            timer(funct, e[0])
            # timer_amt(funct, 10, e[0])

            print()
