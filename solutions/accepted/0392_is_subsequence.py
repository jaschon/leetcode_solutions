#!/usr/bin/env python3
# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652000179/
# Time: 57ms (28.94%)
# Mem: 14MB (73.22%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:

    def __init__(self):
        self.memo = {}

    def isSubsequence(self, s: str, t: str) -> bool:

        if s and not t or len(s) > len(t):
            return False

        if s == "":
            return True

        if (s,t) in self.memo:
            return self.memo[(s,t)]

        for i in range(len(t)):
            if s[0] == t[i]:
                self.memo[(s,t)] = self.isSubsequence(s[1:], t[i+1:])
                if self.memo[(s,t)] ==  True:
                    return True

        self.memo[(s,t)] = False
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
                ("abc", "ahbgdc", True),
                ("axc", "ahbgdc", False),
                ("abc", "", False),
                ("b", "abc", True),
                ("aaaaaa", "bbaaaa", False),
                ("bb", "ahbgdc", False),


                ):

            # funct = inspect.getmembers(f)[-1][1]
            funct = f.isSubsequence

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
