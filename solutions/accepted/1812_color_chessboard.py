#!/usr/bin/env python3

# 1812. Determine Color of a Chessboard Square
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

# Easy

# Accepted (Solution)
# Result: https://leetcode.com/submissions/detail/617083091/
# Time: 24ms (95.54%)
# Mem: 14.3MB (40.00%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = (ord(coordinates[0])-96) % 2 == 0
        y = int(coordinates[1]) % 2 == 0
        return x != y


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution3(),
            # Solution2(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                # ("a1", False),
                # ("h3", True),
                ("e5", False),
                ("h8", False),
                ("a8", True),
                ("h1", True),



                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
