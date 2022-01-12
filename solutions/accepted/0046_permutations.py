#!/usr/bin/env python3
# 46. Permutations
# https://leetcode.com/problems/permutations/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/618579256/
# Time: 36ms (90.51%)
# Mem: 14.4MB (71.35%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from itertools import chain, permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums, len(nums))



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
