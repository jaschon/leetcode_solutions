#!/usr/bin/env python3
# 1588. Sum of All Odd Length Subarrays
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/619086017/
# Time: 62ms (61.17%)
# Mem: 13.9MB (98.64%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        length = len(arr)+1
        for n in range(1, length, 2):
            j = n
            for i in range(0, length-n):
                result += sum(arr[i:j])
                j+= 1
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
                ([1,4,2,5,3], 58),
                ([1,2], 3),
                ([10,11,12], 66),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
