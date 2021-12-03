#!/usr/bin/env python3
# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/
# Medium
# Accepted!
# 32ms (85.55%)
# 14.3 (58.37%)
# https://leetcode.com/submissions/detail/596487045/

import sys
sys.path.insert(0,'..')
from _helper import *


class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        times = 1
        stop = False
        for ch in s:
            if ch == " " and stop == False: 
                continue
            elif ch == "+" and stop == False: 
                stop = True
            elif ch == "-" and stop == False: 
                times = -1
                stop = True
            elif "0" <= ch <= "9":
                result = result * 10 + int(ch)
                stop = True
            else:
                break
        return max(-2147483648, min(2147483647, result*times))



if __name__ == "__main__":
    for e in (

            ("42", 42),
            ("   -42", -42),
            ("4193 with words", 4193),
            ("words and 987", 0),
            ("+-12", 0),
            ("-91283472332", -2147483648),
            ("00000-42a1234", 0),
            ("   +0 123", 0),
            ):

        funct = Solution().myAtoi

        print()

        test(funct, e[1], e[0])
        timer(funct, e[0])

        print()

