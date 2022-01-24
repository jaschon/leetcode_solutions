#!/usr/bin/env python3
# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

# Medium

# Accepted
# Result: https://leetcode.com/problems/koko-eating-bananas/submissions/
# Time: 803ms (17.50%)
# Mem: 15.5MB (60.66%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from math import ceil
class Solution2:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            middle = (low+high)//2
            hour = 0
            for pile in piles:
                hour += ceil(pile/middle)  
            if hour <= h:
                high = middle
            else:
                low = middle + 1
        return high



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = (low+high)//2
            hour = sum(ceil(p/mid) for p in piles)
            if hour <= h:
                high = mid
            else:
                low = mid + 1
        return high


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([3,6,7,11], 8, 4),
                ([30,11,23,4,20], 5, 30),
                ([30,11,23,4,20], 6, 23),



                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
