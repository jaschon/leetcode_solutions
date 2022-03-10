#!/usr/bin/env python3
# 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/656760256/
# Time: 4140ms (13.91%)
# Mem: 24.6MB (95.21%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. same as the last one. 
# 2. presum rows and cols
# 3. when you check a region loop over the rows,
# - it is just the sums of the large rectangle - the smaller rectangles

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        height = len(matrix)
        width = len(matrix[0])
        
        for row in range(height):
            total = 0
            for col in range(width):
                total += matrix[row][col]
                matrix[row][col] = total
        self.matrix = matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for row in range(row1, row2+1):
            check = self.matrix[row][col1-1] if col1 != 0 else 0
            result += (self.matrix[row][col2] - check)
        return result


if __name__ == "__main__":
    pass

