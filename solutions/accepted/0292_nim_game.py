#!/usr/bin/env python3
# 292. Nim Game
# https://leetcode.com/problems/nim-game/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/636680671/
# Time: 26ms (89.86%)
# Mem: 14 MB (78.57%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (4, False),
                (1, True),
                (2, True),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
