#!/usr/bin/env python3
# 2108. Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/617043294/
# Time: 56ms (99.20%)
# Mem: 14.4MB (58.77%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w[::-1] == w:
                return w
        return ""


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (["abc","car","ada","racecar","cool"], "ada"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
