#!/usr/bin/env python3
# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/621905258/
# Time: 39ms (33.34%)
# Mem: 14.4MB

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        if rowIndex == 0: return [1]
        for line in range(1, rowIndex+2):
            count = 1;
            result.append([])
            for i in range(1, line + 1):
                result[line-1].append(count)
                count = int(count * (line - i) / i);
        return result[rowIndex]

class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        for line in range(1, rowIndex+2):
            count = 1;
            result = []
            for i in range(1, line + 1):
                result.append(count)
                count = int(count * (line - i) / i);
        return result

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (3, [1,3,3,1]),
                (0, [1]),
                (1, [1,1]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
