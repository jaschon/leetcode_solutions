#!/usr/bin/env python3
# 1249. Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/660667862/
# Time: 125ms (73.45%)
# Mem: 16MB (40.90%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                try:
                    stack.pop()
                except:
                    s[i] = ''
        for i in stack:
            s[i] = ''
        return ''.join(s)



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("lee(t(c)o)de)", "lee(t(c)o)de"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
