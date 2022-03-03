#!/usr/bin/env python3
# 1232. Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652713526/
# Time: 66ms (80.63%)
# Mem: 14.3MB (90.40%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# use equation:  (y2-y1) * (x3-x1) == (x2-x1) * (y3-y1) 
# (y2-y1/x2-x1) = (y3-y1)/(x3-x1) works too, but you get divide by zero errors

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for p in range(2, len(coordinates)):
            x3, y3 = coordinates[p]
            if (y2-y1)*(x3-x1) != (x2-x1)*(y3-y1):
                return False
        return True

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]], False),
                ([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], True),
                ([[1,2],[2,3],[3,5]], False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
