#!/usr/bin/env python3

# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/655309815/
# Time: 68ms (10.18%)
# Mem: 14.1MB (53.27%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


# 1. any value 1-9 can be taken, so return 0 if you see a 0
#2 any value with a 1 next to 0-6

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = { len(s) : 1 } #
        def loopy(i):
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0
            result = loopy(i+1) #take keep going if it doesn't start with 0
            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and  and s[i+1] in "0123456")):
                result += loopy(i+2) #try two values
            memo[i] = result
            return result
        return loopy(0)




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("12", 2),
                ("226", 3),
                # ("06", 0),
                # ("27", 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
