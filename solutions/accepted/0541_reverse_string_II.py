#!/usr/bin/env python3

# 541. Reverse String II
# https://leetcode.com/problems/reverse-string-ii/
# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/641323533/
# Time: 36ms (73.77%)
# Mem: 14MB (88.61%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return "".join(s)
        

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("abcdefg", 2, "bacdfeg"),
                ("abcd", 2, "bacd"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
