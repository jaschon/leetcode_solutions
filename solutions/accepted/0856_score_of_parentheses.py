#!/usr/bin/env python3
# 856. Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/661852959/
# Time: 42ms (56.30%)
# Mem: 13.8MB (70.86%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [0]
        
        for p in s:
            if p == "(":
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += max(1, 2*last)
                
        return stack[-1]


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("()", 1),
                ("(())", 2),
                ("()()", 2),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
