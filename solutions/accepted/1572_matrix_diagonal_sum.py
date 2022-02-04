#!/usr/bin/env python3
# 1572. Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/634530818/
# Time: 128ms (51.46%)
# Mem: 14.3 MB (89.26%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)-1
        result = 0
        for i in range(l+1):
            n1, n2 = (i,i), (i,l-i)
            result += mat[n1[0]][n1[1]]
            if n1 != n2:
                result += mat[n2[0]][n2[1]]
        return result



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([[1,2,3], [4,5,6], [7,8,9]], 25),
                ([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]], 8),
                ([[5]], 5),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
