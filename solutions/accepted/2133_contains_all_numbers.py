#!/usr/bin/env python3
# 2133. Check if Every Row and Column Contains All Numbers
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/619799699/
# Time: 732ms (96.79%)
# Mem: 14.9MB (14.59%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        size = len(matrix)
        check = {_ for _ in range(1, size+1)}
        for r in matrix:
            if set(r) != check:
                return False
        for c in range(size):
            if set(m[c] for m in matrix) != check:
                return False
        return True




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([[1,2,3],[3,1,2],[2,3,1]], True),
                ([[1,1,1],[1,2,3],[1,2,3]], False),
                ([[1]], True),
                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
