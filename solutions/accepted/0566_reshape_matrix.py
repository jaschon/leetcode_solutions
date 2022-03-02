#!/usr/bin/env python3
# 566. Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652160296/
# Time: 114ms (62.77%)
# Mem: 14.7MB (62.69%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

from itertools import chain
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        items = []
        for item in chain(mat):
            try:
                for i in chain(item):
                    items.append(i)
            except:
                items.append(item)
        if (r*c) != len(items):
            return mat
        results = []
        for row in range(r):
            results.append([])
            for col in range(c):
                results[row].append(items.pop(0))
        if items:
            results[-1].extend(items)
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
                # ([[1,2],[3,4]], 1, 4, [[1,2,3,4]]),
                # ([[1,2],[3,4]], 2, 4, [[1,2],[3,4]]),
                ([1,2], 1,1, [[1,2]]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
