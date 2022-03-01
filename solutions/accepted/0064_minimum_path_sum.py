#!/usr/bin/env python3
# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/648767839/
# Time: 116ms (72.60%)
# Mem: 19.7MB (12.79%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:

    def __init__(self):
        self.memo = {}

    def minPathSum(self, grid: List[List[int]], row=0, col=0) -> int:
        if (row,col) in self.memo:
            return self.memo[(row, col)]
        if row == len(grid)-1 and col == len(grid[0])-1:
            return grid[row][col]
        if row >= len(grid) or col >= len(grid[0]):
            return 300

        self.memo[(row,col)] = grid[row][col] + min(self.minPathSum(grid, row+1, col), self.minPathSum(grid, row, col+1))
        return self.memo[(row,col)]



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([[1,3,1],[1,5,1],[4,2,1]], 7),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
