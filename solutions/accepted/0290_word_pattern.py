#!/usr/bin/env python3
# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/621786573/
# Time: 30ms (65.84%)
# Mem: 14.2MB (55.31%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        match = {}
        pmatch = {}
        if len(s) != len(pattern):
            return False
        for i, p in enumerate(pattern):
            if not p in match:
                match[p] = s[i]
            elif match[p] != s[i]:
                return False
            if not s[i] in pmatch:
                pmatch[s[i]] = p
            elif pmatch[s[i]] != p:
                return False
        return True


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            # Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("abba", "dog cat cat dog", True),
                ("abba", "dog cat cat fish", False),
                ("abba", "dog dog dog dog", False),
                ("aaa", "aa aa aa aa", False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
