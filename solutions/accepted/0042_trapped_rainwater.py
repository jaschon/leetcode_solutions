#!/usr/bin/env python3
# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# Hard

# Accepted
# Result: https://leetcode.com/submissions/detail/653381401/
# Time: 92ms (79.43%)
# Mem: 15.9MB (22.29%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. equation for each spot --> min(maxLeft, maxRight) - height[i]
# 2. calculate at each pos
# 3. two pointers, left and right
# 4a. if left_max < right_max
# - inc left pointer
# - cal new left_max based on left pos --> max(left_max, height[left])
# - run equation and add to result --> left_max - height[left]
# 4b. else
# - inc right pointer
# - calc new right_max based on right pos -> max(right_max, height[right])
# - run equation and add to result --> right_max - height[right]
# 5. return result

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]


        while left < right:

            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]

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
                ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
                ([4,2,0,3,2,5], 9),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
