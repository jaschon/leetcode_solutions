#!/usr/bin/env python3
# 1779. Find Nearest Point That Has the Same X or Y Coordinate
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652014296/
# Time: 871ms (62.11%)
# Mem: 19.3MB (51.75%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        result = {}
        dist = 1000000

        for i, p in enumerate(points):
            if p[0] == x or p[1] == y:
                d = abs(x-p[0])+abs(y-p[1]) 
                if d < dist:
                    if d in result:
                        result[d].append(i)
                    else:
                        result[d] = [i]
        if result:
            return min(result[min(result.keys())])
        return -1


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]], 2),
                (3, 4, [[3,4]], 0),
                (3,4, [[2,3]], -1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
