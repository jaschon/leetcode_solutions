#!/usr/bin/env python3
# 264. Ugly Number II
# https://leetcode.com/problems/ugly-number-ii/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/655976981/
# Time: 247ms (48.01%)
# Mem: 14.1 MB (55.16%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. make seen set, heap array and current
# 2. loop through as many times as n
# a) get lowest value from heapq
# b) loop through factors 2,3,5
# c) add to seen if not found and add to the heap
# 3. return the last current

import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        current = 1
        heap = [1]
        seen = {1}

        for i in range(n):
            current = heapq.heappop(heap)
            for f in (2,3,5):
                new = current * f
                if not new in seen:
                    seen.add(new)
                    heapq.heappush(heap, new)
        return current


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (10, 12),
                (1,1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
