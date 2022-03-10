#!/usr/bin/env python3
# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/

# Medium

# Accepted
# Result: 
# Time:
# Mem:

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. make a memo the size of the matrix
# 2 loop through all values
# 3 if value is a "1", store memo pos as the (min of the top, bottom and top right) + 1
# 4. set result to the max of result and the memo pos
# 5. return result ** 2


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[0]*(cols+1) for _ in range(rows+1)]
        result = 0
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                if matrix[row-1][col-1] == '1':
                    memo[row][col] = 1 + min(memo[row][col-1], memo[row-1][col], memo[row-1][col-1])
                    result = max(result, memo[row][col])

        return result * result


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4),
                ([["0","1"],["1","0"]], 1),
                ([["0"]], 0),
                ([["1"]], 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
