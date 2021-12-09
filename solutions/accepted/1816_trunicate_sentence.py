#!/usr/bin/env python3
# https://leetcode.com/problems/truncate-sentence/
# 1816. Truncate Sentence
# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/599018136/
# Time: 28ms (84.35%)
# Mem: 14.2 MB (48.99%)

import sys
sys.path.insert(0,'..')
from _helper import *


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
        

if __name__ == "__main__":
    for e in (
            ("Hello how are you Contestant", 4, "Hello how are you"),


            ):

        funct = Solution().truncateSentence

        print()

        test(funct, e[2], e[0], e[1])
        timer(funct, e[0], e[1])

        print()
