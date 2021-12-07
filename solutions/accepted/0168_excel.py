#!/usr/bin/env python3
# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/
# Easy

# Accepted!
# Result: https://leetcode.com/submissions/detail/598
# Time: 28ms (80.73%)
# Mem: 14.3MB (44.25%)

import sys
sys.path.insert(0,'..')
from _helper import *

# char == (number % 26) + 'A'

import math
class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            r = math.floor(n % 26)
            n = math.floor(n / 26)
            if r == 0:
                result = "Z" + result
                n -= 1
            else:
                result = chr((r-1) + 65) + result
        return result
        
class Solution2:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            r = n % 26
            n = math.floor(n / 26)
            if r == 0:
                result = "Z" + result
                n -= 1
            else:
                result = chr((r-1) + 65) + result
        return result


alpha = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
class Solution3:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            r = n % 26
            n = math.floor(n / 26)
            if r == 0:
                result = 'Z' + result
                n -= 1
            else:
                result = alpha[r] + result
        return result


if __name__ == "__main__":
    for e in (
            (1, "A"),
            (28, "AB"),
            (701, "ZY"),
            (2147483647, "FXSHRXW"),
            (26, "Z"),


            ):

        funct = Solution().convertToTitle
        funct2 = Solution2().convertToTitle
        funct3 = Solution3().convertToTitle

        print()

        # test(funct, e[1], e[0])
        timer(funct, e[0])

        print()

        # test(funct2, e[1], e[0])
        timer(funct2, e[0])

        print()

        # test(funct3, e[1], e[0])
        timer(funct3, e[0])
