#!/usr/bin/env python3
# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonac 
# Easy

# Accepted!
# Result: https://leetcode.com/submissions/detail/598927030/
# Time: 41ms (18.68%)
# Mem: 14.4MB (12.11%)

import sys
sys.path.insert(0,'..')
from _helper import *

from functools import cache

@cache
class Solution:
    def tribonacci(self, n=0, count=0, amt=[0,1,1,2]) -> int:
        amt.append(amt[-1]+amt[-2]+amt[-3])
        if count == n: return amt[n]
        return self.tribonacci(n, count+1, amt)

if __name__ == "__main__":
    for e in (
            (4, 4),
            (25, 1389537),

            ):

        funct = Solution().tribonacci

        print()

        test(funct, e[1], e[0])
        timer(funct, e[0])

        print()
