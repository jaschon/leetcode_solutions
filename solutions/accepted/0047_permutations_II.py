#!/usr/bin/env python3
# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/626888221/
# Time: 68ms (59.13%)
# Mem: 14.6MB (46.33%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for perm in permutations(nums):
            if not perm in result:
                result.add(perm)
        return result

class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(permutations(nums))

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
                ([1,1,2], [[1,1,2],[1,2,1], [2,1,1]]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
