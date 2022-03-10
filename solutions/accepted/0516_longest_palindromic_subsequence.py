#!/usr/bin/env python3
# 516. Longest Palindromic Subsequence
# https://leetcode.com/problems/longest-palindromic-subsequence/

# Medium

# Accepted
# Result: 
# Time:
# Mem:

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# dp!
# if len is 1, return 1
# if empty, return 0
# if the first char is the same as the last, recurse with first and last taken off
# else
# get the max of the recursion of the string with the last char off and the recursion of the string
# with the first char taken off

class Solution:

    def __init__(self):
        self.memo = {}

    def longestPalindromeSubseq(self, s: str) -> int:

        if s in self.memo:
            return self.memo[s]

        if s == "":
            return 0

        if len(s) == 1:
            return 1

        if s[0] == s[-1]:
            self.memo[s] = self.longestPalindromeSubseq(s[1:-1]) + 2
            return self.memo[s]

        self.memo[s] = max(self.longestPalindromeSubseq(s[:-1]), self.longestPalindromeSubseq(s[1:]))
        return self.memo[s]


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("bbbab", 4),
                ("cbbd", 2),
                ('ABBDCACB', 5),


                ):

            # funct = inspect.getmembers(f)[-1][1]
            funct = f.longestPalindromeSubseq

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
