#!/usr/bin/env python3
# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652678733/
# Time: 67ms (63.40%)
# Mem: 14.3MB (53.81%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        count = {}
        for i, n in enumerate(nums2):
            count[n] = -1
            for j in range(i+1,len(nums2)):
                if nums2[j] > nums2[i]:
                    count[n] = nums2[j]
                    break
        return [count[n] for n in nums1]




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([4,1,2], [1,3,4,2], [-1,3,-1]),
                ([2,4], [1,2,3,4], [3,-1]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
