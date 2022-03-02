#!/usr/bin/env python3

# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Easy

# Accepted
# Result: 
# Time:
# Mem:

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        result = []
        for n in nums2:
            if n in c and c[n] > 0:
                result.append(n)
                c[n] -= 1

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
                ([1,2,2,1], [2,2], [2,2]),
                ([4,9,5], [9,4,9,8,4], [4,9]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test_list(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
