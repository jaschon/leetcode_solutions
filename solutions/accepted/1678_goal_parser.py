#!/usr/bin/env python3
# 1678. Goal Parser Interpretation
# https://leetcode.com/problems/goal-parser-interpretation/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/627644451/
# Time: 45ms (27.7%)
# Mem: 14.2 MB (60.20%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
match = { "()": "o", "(al)": "al"}
class Solution2:
    def interpret(self, command: str) -> str:
        for m in match:
            command = command.replace(m, match[m])
        return command

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("G()(al)", "Goal"),
                ("G()()()()(al)", "Gooooal"),
                ("(al)G(al)()()G", "alGalooG"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
