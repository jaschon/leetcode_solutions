#!/usr/bin/env python3
# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
# 2042. Check if Numbers Are Ascending in a Sentence
# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/596501949/
# Time: 32ms (74.41%)
# Mem: 14.4MB (19.69%)

import sys
sys.path.insert(0,'..')
from _helper import *


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(_) for _ in s.split() if _.isdigit()]
        return nums == sorted(list(set(nums)))
        

if __name__ == "__main__":
    for e in (
            ("1 box has 3 blue 4 red 6 green and 12 yellow marbles", True),
            ("hello world 5 x 5", False),


            ):

        funct = Solution().areNumbersAscending

        print()

        test(funct, e[1], e[0])
        timer(funct, e[0])

        print()
