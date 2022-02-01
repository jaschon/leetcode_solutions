#!/usr/bin/env python3
# 2124. Check if All A's Appears Before All B's
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/632447093/
# Time: 24ms (98.32%)
# Mem: 14MB (94.27%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def checkString(self, s: str) -> bool:
        return all(z != ("b", "a") for z in zip(s, s[1:]))


class Solution4:
    def checkString(self, s: str) -> bool:
        mode = s[0]
        switch = mode == 'b'
        for l in s:
            if mode == 'b' and l == 'a':
                return False
            elif mode == 'a' and l == 'b' and switch:
                return False
            elif mode == 'a' and not switch and l == 'b':
                mode = 'b'
                switch = True
        return True

class Solution2:
    def checkString(self, s: str) -> bool:
        if not s:
            return True
        elif s[:2] == "ba":
            return False
        else:
            return self.checkString(s[1:])


class Solution3:
    def checkString(self, s: str) -> bool:
        for z in zip(s, s[1:]):
            if z == ("b", "a"):
                return False
        return True


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            # Solution4(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("bbbbbbbb", True),
                # ("aaaaaaaaaa", True),
                # ("aaaabbbb", True),
                # ("abbbbbbbbbba", False),
                ("abaaabbbaaabbb", False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
