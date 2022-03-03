#!/usr/bin/env python3
# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/652827329/
# Time: 64ms (50.09%)
# Mem: 14.4% (69.06%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# double binary search
# 1. get low, high range values
# 2. start loop while (low <= high)
# 3. make middle value which is avg of high and low == (high+low)//2
# 4. if target is higher than last item in middle row, increase low value
# 5. if target is lower than first item in middle row, increase high value
# 6. else break

# 7. repeat with cols in a row using the same formula

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        low, high = 0, rows-1

        while low <= high:

            middle = (high+low)//2

            if target > matrix[middle][-1]:
                low = middle + 1
            elif target < matrix[middle][0]:
                high = middle - 1
            else:
                break

        if not low <= high: return False

        left, right = 0, cols-1
        middle = (high+low)//2

        while left <= right:
            center = (left+right)//2
            if target  > matrix[middle][center]:
                left = center + 1
            elif target < matrix[middle][center]:
                right = center -1
            else:
                return True

        return False

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                # ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
                # ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
                ([[1]], 1, True),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
