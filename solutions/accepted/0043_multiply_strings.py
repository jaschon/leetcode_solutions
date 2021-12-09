#!/usr/bin/env python3
# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/598983265/
# Time: 168ms (27.05%)
# Mem: 14.2MB (83.47%)

import sys
sys.path.insert(0,'..')
from _helper import *

#BOX Multiply
# times each digit and add them up!

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        for i1, n1 in enumerate(num1[::-1]):
            x = (10**i1) * int(n1)
            for i2, n2 in enumerate(num2[::-1]):
                y = (10**i2) * int(n2)
                result += (x*y)
        return str(result)


class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        for i1, n1 in enumerate(num1[::-1]):
            x = (10**i1) * (ord(n1)-48)
            for i2, n2 in enumerate(num2[::-1]):
                y = (10**i2) * (ord(n2)-48)
                result += (x*y)
        return str(result)
        

if __name__ == "__main__":
    for e in (
            ("2", "3", "6"),
            ("123", "456", "56088"),

            ):

        funct = Solution().multiply

        print()

        test(funct, e[2], e[0], e[1])
        timer(funct, e[0], e[1])
        timer(Solution2().multiply, e[0], e[1])

        print()
