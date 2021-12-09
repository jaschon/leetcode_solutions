#!/usr/bin/env python3
# https://leetcode.com/problems/fibonacci-number/
# 509. Fibonacci Number
# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/598916175/
# Time: 45ms
# Mem: 14.4MB

import sys
sys.path.insert(0,'..')
from _helper import *

class Solution:
    def fib(self, n=0, count=0, amt=[0,1]) -> int:
        amt.append(amt[-1]+amt[-2])
        if count == 0: return amt[n]
        return self.fib(n, count+1, amt)

class Solution2:
    def fib(self, n=0) -> int:
        if n < 2: return n
        return self.fib(n-1) + self.fib(n-2)



if __name__ == "__main__":
    for e in (
            (2,1),
            (3,2),
            (4,3)


            ):

        funct = Solution().fib

        print()

        test(funct, e[1], e[0])
        timer(funct, e[0])
        print()
