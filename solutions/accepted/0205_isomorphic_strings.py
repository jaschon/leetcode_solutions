#!/usr/bin/env python3
# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/621807145/
# Time: 28ms (99.29%)
# Mem: 14.4MB (44.38%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        match = {}
        rmatch = {}
        for p, r in zip(s, t):
            if not p in match:
                match[p] = r
            elif match[p] != r:
                return False
            if not r in rmatch:
                rmatch[r] = p
            elif rmatch[r] != p:
                return False
        return True



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                # ("egg", "add", True),
                # ("foo", "bar", False),
                # ("paper", "title", True),
                ("badc", "baba", False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
