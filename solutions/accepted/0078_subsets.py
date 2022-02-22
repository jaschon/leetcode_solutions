#!/usr/bin/env python3
# 78. Subsets
# https://leetcode.com/problems/subsets/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/646975545/
# Time: 36ms (83.71%)
# Mem: 14MB (97.28%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(0, len(nums)+1):
            result += combinations(nums,i)
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
                ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
