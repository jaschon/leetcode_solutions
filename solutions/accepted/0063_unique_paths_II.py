#!/usr/bin/env python3
# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/647535574/
# Time: 41ms (85.53%)
# Mem: 14.1MB (64.38%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def __init__(self):
        self.mapper = {}
        self.grid = []

    def _paths(self, m: int, n: int) -> int:
        if (m,n) in self.mapper:
            return self.mapper[(m,n)]
        elif self.grid[m-1][n-1] == 1 or 0 in (m,n):
            return 0
        elif m == 1 and n == 1:
            return 1
        self.mapper[(m,n)] = self._paths(m-1, n) + self._paths(m, n-1)
        return self.mapper[(m,n)]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.grid = obstacleGrid
        return self._paths(len(self.grid), len(self.grid[0])) if self.grid else None




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                # ([[0,0,0],[0,1,0],[0,0,0]], 2),
                ([[1]], 0),
                ([[1], [0]], 0)


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
