#!/usr/bin/env python3
# 1476. Subrectangle Queries
# https://leetcode.com/problems/subrectangle-queries/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/618390652/
# Time: 251ms (22.85%)
# Mem: 16MB (45.02%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rec = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for y in range(row1, row2+1):
            for x in range(col1, col2+1):
                self.rec[y][x] = newValue
        return newValue
        

    def getValue(self, row: int, col: int) -> int:
        return self.rec[row][col]



if __name__ == "__main__":
    com = ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
    val = [[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]

    obj = SubrectangleQueries(*val[0])
    print(obj.rec)
    print(obj.getValue(*val[1]))



