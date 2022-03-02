#!/usr/bin/env python3
# 2185. Counting Words With a Given Prefix
# https://leetcode.com/problems/counting-words-with-a-given-prefix/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/651474173/
# Time: 50ms (73.70%)
# Mem: 14MB (32.16%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for i in words if i.startswith(pref))



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (["pay","attention","practice","attend"], "at", 2),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
