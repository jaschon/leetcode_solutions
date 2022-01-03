#!/usr/bin/env python3
# 1556. Thousand Separator
# https://leetcode.com/problems/thousand-separator/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/612371479/
# Time: 51ms (5.63%)
# Mem: 14.2MB (43.72%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000: return str(n)
        n = str(n)[::-1]
        return ".".join([n[i:i+3] for i in range(0, len(n), 3)])[::-1]


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)

                (987, "987"),
                (1234, "1.234"),

                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 200, *e[:-1])


            print()
