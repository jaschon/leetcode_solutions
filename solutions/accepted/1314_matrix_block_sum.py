#!/usr/bin/env python3
# 1314. Matrix Block Sum
# https://leetcode.com/problems/matrix-block-sum/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/648256918/
# Time: 92ms (99.35%)
# Mem: 15.1MB (92.56%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE

#time out!
class Solution2:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        hlength = len(mat)
        wlength = len(mat[0])

        results = [ [None] * wlength for _ in range(hlength) ]

        for i in range(hlength):
            for j in range(wlength):
                total = 0 
                for m in range(max(i-k, 0), min(i+k+1, hlength)): 
                    for n in range(max(j-k,0), min(j+k+1, wlength)):
                        total += mat[m][n]
                results[i][j] = total
        return results

#faster
# make a presum of matrix (cumsum of left to right and top to bottom)
# answer is the value in matrix (i+k columns) and (i+k rows)
#if out of bounds, you subtract the value from mat[i-k][j-k-1]

class Solution:
    def _presum(self, mat):

        for r in range(self.hlength):
            for c in range(1, self.wlength):
                mat[r][c] += mat[r][c-1]

        for c in range(self.wlength):
            for r in range(self.hlength-1):
                mat[r+1][c] += mat[r][c]

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        self.hlength = len(mat)
        self.wlength = len(mat[0])

        self._presum(mat)

        results = []

        for i in range(self.hlength):
            tmp = []
            for j in range(self.wlength):
                upper_i = self.hlength-1 if (i+k) >= self.hlength else i+k
                upper_j = self.wlength-1 if (j+k) >= self.wlength else j+k
                lower_i = 0 if (i-k)<0 else i-k
                lower_j = 0 if (j-k)<0 else j-k
                tmp.append(mat[upper_i][upper_j])
                if lower_i !=0:
                    tmp[-1] -= mat[lower_i-1][upper_j]
                if lower_j != 0:
                    tmp[-1] -= mat[upper_i][lower_j-1]
                if lower_i != 0 and lower_j != 0:
                    tmp[-1] += mat[lower_i-1][lower_j-1]
            results.append(tmp)
        return results

#cleaned up, but slower?
class Solution1:
    def _presum(self, mat):

        for r in range(self.hlength):
            for c in range(1, self.wlength):
                mat[r][c] += mat[r][c-1]

        for c in range(self.wlength):
            for r in range(self.hlength-1):
                mat[r+1][c] += mat[r][c]

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        self.hlength = len(mat)
        self.wlength = len(mat[0])

        self._presum(mat)

        results = []

        for i in range(self.hlength):
            tmp = []
            for j in range(self.wlength):
                upper_i = self.hlength-1 if (i+k) >= self.hlength else i+k
                upper_j = self.wlength-1 if (j+k) >= self.wlength else j+k
                lower_i = 0 if (i-k)<0 else i-k
                lower_j = 0 if (j-k)<0 else j-k
                tmp.append(mat[upper_i][upper_j])
                if lower_i !=0:
                    tmp[-1] -= mat[lower_i-1][upper_j]
                if lower_j != 0:
                    tmp[-1] -= mat[upper_i][lower_j-1]
                if lower_i != 0 and lower_j != 0:
                    tmp[-1] += mat[lower_i-1][lower_j-1]
            results.append(tmp)
        return results


        

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([[1,2,3],[4,5,6],[7,8,9]], 1, [[12,21,16],[27,45,33],[24,39,28]]),
                # ([[1,2,3],[4,5,6],[7,8,9]], 2, [[45,45,45],[45,45,45],[45,45,45]]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
