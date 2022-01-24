#!/usr/bin/env python3
# 520. Detect Capital
# https://leetcode.com/problems/detect-capital/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/626850823/
# Time: 32ms
# Mem: 14.1MB

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = ['A' <= _ <= 'Z' for _ in word]
        return (all(caps)) or not any(caps) or (caps[0] and not any(caps[1:]))
        



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("USA", True),
                ("FlaG", False),
                ("A", True),
                ("a", True),
                ("lowercase", True),
                ("loWercase", False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
