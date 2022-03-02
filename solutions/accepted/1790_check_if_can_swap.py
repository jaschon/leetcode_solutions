#!/usr/bin/env python3

# 1790. Check if One String Swap Can Make Strings Equal
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652106226/
# Time: 32ms (86.86%)
# Mem: 13.9MB (85.57%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = {} 
        num_diffs = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diffs += 1
                if num_diffs > 2:
                    return False
                if (s2[i], s1[i]) in diffs:
                    del diffs[(s2[i], s1[i])]
                else:
                    diffs[(s1[i], s2[i])] = 1 

        return len(diffs) == 0 and num_diffs < 3



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("bank", "kanb", True),
                ("attack", "defend", False),
                ("kelb", "kelb", True),
                ("abcd", "dcba", False),
                ("aa", "ac", False),
                ("aa", "bb", False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
