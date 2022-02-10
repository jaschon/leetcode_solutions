#!/usr/bin/env python3
# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/638187999/
# Time: 874ms (53.88%)
# Mem: 27.5 MB (49.97%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0 
        lside = 0
        rside = len(height)-1
        # area = height * width
        # --> height = the smaller of height[i] and height[j]
        # --> width = j-i
        while lside < rside:
                area = max(area, min(height[lside], height[rside]) * (rside-lside))
                if height[lside] < height[rside]:
                    lside += 1
                else:
                    rside -= 1
        return area


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        area = 0 
        # area = height * width
        # --> height = the smaller of height[i] and height[j]
        # --> width = j-i
        for lside in range(len(height)):
            for rside in range(lside+1, len(height)):
                area = max(area, min(height[lside], height[rside]) * (rside-lside))
        return area

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,8,6,2,5,4,8,3,7], 49),
                ([1,1], 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
