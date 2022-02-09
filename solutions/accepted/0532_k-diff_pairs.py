#!/usr/bin/env python3
# 532. K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/637966426/
# Time: 107ms (51.12%)
# Mem: 15.6MB (71.76%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0 or not nums: return 0
        result = 0
        counter = Counter(nums)
        for key in counter:
            if k == 0 and counter[key] > 1:
                result += 1
            elif k != 0 and key+k in counter:
                result += 1
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
                ([3,1,4,1,5], 2, 2),
                ([1,2,3,4,5], 1, 4),
                ([1,3,1,5,4], 0, 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
