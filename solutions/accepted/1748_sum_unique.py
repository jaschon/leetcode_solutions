#!/usr/bin/env python3
# 1748. Sum of Unique Elements
# https://leetcode.com/problems/sum-of-unique-elements/
# Easy
# Accepted!
# 28ms (95%)
# 14.4MB (11.40%)
# https://leetcode.com/submissions/detail/596067642/

import sys
sys.path.insert(0,'..')
from _helper import *

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        d = {}
        for n in nums:
            d[n] = 1 if not d.get(n) else d.get(n) + 1
        return sum([_ for _ in d if d[_] == 1])
        

if __name__ == "__main__":
    for e in (

            ([1,2,3,2], 4),
            ([1,1,1,1,1], 0),

            ):

        funct = Solution().sumOfUnique

        test(funct, e[1], e[0])
        timer(funct, e[0])

        print()


