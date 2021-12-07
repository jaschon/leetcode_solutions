#!/usr/bin/env python3
# 1979. Find Greatest Common Divisor of Array
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Easy

# Accepted 
# Result: https://leetcode.com/submissions/detail/598517552/
# Time: 56ms (70.18%)
# Mem: 14.1MB (96.09%)

import sys
sys.path.insert(0,'..')
from _helper import *


import math
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        nums.sort()
        return math.gcd(nums[0], nums[-1])
        

if __name__ == "__main__":
    for e in (
            ([2,5,6,9,10], 2),
            ([7,5,6,8,3], 1),
            ([3,3], 3),
            ):

        funct = Solution().findGCD

        print()

        test(funct, e[1], e[0])
        timer(funct, e[0])

        print()
