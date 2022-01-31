#!/usr/bin/env python3
# Maximum XOR of Two Numbers
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/629040672/
# Time: 2577ms (55.78%)
# Mem: 33.4MB (97.65%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution2:
    def findMaximumXOR(self, nums: List[int]) -> int:
        result = 0
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                result = max(result, nums[i]^nums[j])
        return result

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        result = 0
        mask = 0
        lookup = set()
        length = len(nums)
        for i in range(30, -1, -1):
            mask |= (1<<i)
            check = result | (1<<i)
            for i in range(length):
                lookup.add(nums[i] & mask)
            for l in lookup:
                if check^l in lookup:
                    result = check
                    break
            lookup.clear()
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
                ([3,10,5,25,2,8], 28),
                ([14,70,53,83,49,91,36,80,92,51,66,70], 127),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
