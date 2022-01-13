#!/usr/bin/env python3
# 1844. Replace All Digits with Characters
# https://leetcode.com/problems/replace-all-digits-with-characters/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/619095310/
# Time: 44ms (21.38%)
# Mem: 14.1 (73.46%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution2:
    def replaceDigits(self, s: str) -> str:
        result = ""
        for ch in s:
            result = result + chr(ord(result[-1])+int(ch)) if ch < 'a' else result + ch
        return result

class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        for ch in s:
            if ch < 'a':
                result += chr(ord(result[-1])+int(ch)) 
            else:
                result += ch
        return result

class Solution3:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = chr(ord(s[i-1])+int(s[i])) 
        return "".join(s)


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("a1c1e1", "abcdef"),
                ("a1b2c3d4e", "abbdcfdhe"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
