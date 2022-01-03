#!/usr/bin/env python3
# https://leetcode.com/problems/shuffle-string/
# 1528. Shuffle String

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/612476043/
# Time: 79ms (15.66%)
# Mem: 14mb (99.10%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [" ",]*len(s)
        for i,j in enumerate(indices):
            result[j] = s[i]
        return "".join(result)

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            # Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("codeleet", [4,5,6,7,0,2,1,3], "leetcode"),
                ("abc", [0,1,2], "abc"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
