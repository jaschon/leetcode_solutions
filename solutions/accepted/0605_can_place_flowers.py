#!/usr/bin/env python3
# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/622583720/
# Time: 229ms (26.99%)
# Mem: 14.7MB (8.05%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                if (i==0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0: return True
        return False

class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0: return True
        return False


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution2(),
            Solution(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,0,0,0,1], 1, True),
                ([1,0,0,0,1], 2, False),
                ([0,0,0,0,0,1,0,0], 0, True),
                ([1,0,0,0,1,0,0], 2, True),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
