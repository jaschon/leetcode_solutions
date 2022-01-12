#!/usr/bin/env python3
# 1863. Sum of All Subset XOR Totals
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/618540252/
# Time: 87ms (45.31%)
# Mem: 14.3MB (60.85%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from itertools import chain, combinations
from operator import xor
from functools import reduce
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        combos = chain.from_iterable(combinations(nums, i) for i in range(1, len(nums)+1))
        return sum(reduce(xor, i) for i in combos)
        

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,3], 6),
                ([5,1,6], 28),
                ([3,4,5,6,7,8], 480),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
