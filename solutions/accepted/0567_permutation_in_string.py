#!/usr/bin/env python3
# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/639417690/
# Time: 112ms (55.84%)
# Mem: 14.1MB (73.45%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        c1 = Counter(s1)
        c2 = Counter(s2[:len1-1])
        rem = 0

        for i in range(len1-1, len2):
            add = s2[i]
            c2[add] += 1
            if c2 == c1: return True
            c2[s2[rem]] -= 1
            if c2[s2[rem]] <= 0: del c2[s2[rem]]
            rem += 1
        return False


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("test", "estytesty", True),
                ("ab", "eidbaooo", True),
                ("ab", "eidboaoo", False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
