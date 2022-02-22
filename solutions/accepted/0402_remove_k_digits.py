#!/usr/bin/env python3
# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/

# Medium

# Accepted
# Result: https://leetcode.com/problems/remove-k-digits/submissions/
# Time: 32ms (98.22%)
# Mem: 13.2MB (67.26%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# greedy!!!!
#put stuff on stack
# loop and take off everything less than num on stack until you reached k
# join stack, strip off leading zeros and return

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("1432219", 3, "1219"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
