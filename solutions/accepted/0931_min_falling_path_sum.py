#!/usr/bin/env python3
# 931. Minimum Falling Path Sum
# https://leetcode.com/problems/minimum-falling-path-sum/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/648814205/
# Time: 215ms (41.07%)
# Mem: 15.8MB (17.82%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:

    def __init__(self):
        self.memo = {}

    def minFallingPathSum(self, matrix: List[List[int]], row=0, col=0) -> int:

        self.h = len(matrix)
        self.w = len(matrix[0])

        return min(self._path(matrix, 0, i) for i in range(self.w))

    def _path(self, matrix: List[List[int]], row=0, col=0) -> int:

        if row >= self.h or col >= self.w or col < 0:
            return 9000000

        if (row,col) in self.memo:
            return self.memo[(row,col)]

        if row == self.h-1:
            return matrix[row][col]

        self.memo[(row,col)] = matrix[row][col] + min(self._path(matrix, row+1, col), self._path(matrix, row+1, col+1), self._path(matrix, row+1, col-1))

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
                ([[2,1,3],[6,5,4],[7,8,9]], 13),
                # ([[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]], -36),
                # ([[-19,57],[-40,-5]], -59),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
