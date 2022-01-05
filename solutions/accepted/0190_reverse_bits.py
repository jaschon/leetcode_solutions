#!/usr/bin/env python3
# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/613785761/
# Time: 52ms (10.86%)
# Mem: 14.2MB

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:032b}"[::-1], 2)

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (43261596, 964176192),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
