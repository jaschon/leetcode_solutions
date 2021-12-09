#!/usr/bin/env python3
# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/ 
# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/599061332/
# Time: 36ms (88.76%)
# Mem: 14.2 MB (89.89%)

import sys
sys.path.insert(0,'..')
from _helper import *


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        answer = []
        for n in nums:
            total += n
            answer.append(total)
        return answer

        

if __name__ == "__main__":
    for e in (
            ([1,2,3,4], [1,3,6,10]),
            ([1,1,1,1,1], [1,2,3,4,5]),
            ([3,1,2,10,1], [3,4,6,16,17]),


            ):

        funct = Solution().runningSum

        print()

        test(funct, e[1], e[0])
        timer(funct, e[0])

        print()
