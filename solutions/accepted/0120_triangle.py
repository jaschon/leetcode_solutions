#!/usr/bin/env python3

# 120. Triangle
# https://leetcode.com/problems/triangle/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/648304519/
# Time: 98MB (47.58%)
# Mem: 17MB (12.39%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:

    def __init__(self):
        self.memo = {}

    def minimumTotal(self, triangle: List[List[int]], row=0, index=0) -> int:

        if (row,index) in self.memo:
            return self.memo[(row,index)]
        
        if row == len(triangle)-1:
            return triangle[row][index]

        self.memo[(row,index)] = triangle[row][index] + min(self.minimumTotal(triangle, row+1, index), self.minimumTotal(triangle, row+1, index+1))

        return self.memo[(row,index)]




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)

                ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),

                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
