#!/usr/bin/env python3
# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/637286359/
# Time: 58ms (19.77%)
# Mem: 13.9MB (92.51%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        length = len(columnTitle)
        for n, c in enumerate(columnTitle):
            letter = (ord(c) - 64)
            if n == length:
                result += letter
            result = (result * 26) + letter
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
                ("A", 1),
                ("AB", 28),
                ("ZY", 701),
                ("FXSHRXW", 2147483647),
                ("", 0),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
