#!/usr/bin/env python3

# 2164. Sort Even and Odd Indices Independently
# https://leetcode.com/problems/sort-even-and-odd-indices-independently/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/642194694/
# Time: 44ms (99.78%)
# Mem: 13.9MB (75.60%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from itertools import chain, zip_longest
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        return [_ for _ in chain(*zip_longest(sorted(nums[::2]), sorted(nums[1::2])[::-1])) if _ != None]




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([4,1,2,3], [2,3,4,1]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
