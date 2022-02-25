#!/usr/bin/env python3
# 165. Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/648755339/
# Time: 34ms (69.83%)
# Mem: 13.9MB (92.33%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        clean1 = [int(i) for i in version1.split(".")]
        clean2 = [int(i) for i in version2.split(".")]


        len1 = len(clean1)
        len2 = len(clean2)

        if len1 > len2:
            for l in range(len1-len2):
                clean2.append(0)
        else:
            for l in range(len2-len1):
                clean1.append(0)

        for i in range(len(clean1)):
            if clean1[i] > clean2[i]:
                return 1
            elif clean2[i] > clean1[i]:
                return -1
        return 0



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("1.01", "1.001", 0),
                ("1.01.0.0.0.01", "1.001", 0),
                ("1.0", "1.0.0", 0),
                ("0.1", "1.1", -1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
